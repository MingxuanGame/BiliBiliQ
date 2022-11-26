import time
import asyncio
import logging
from typing import Dict, List, Tuple, Callable, Optional, cast

from bilibiliq.auth import Auth
from bilibiliq.internal.client import BaseRESTClient

from .type import Handler
from .utils import get_e_infos
from .model import At, Ats, Emoji
from .event import AtEvent, handle_event

logger = logging.getLogger("bilibiliq.message.at")
LAST_TIME: Dict[str, int] = {}


class AtClient(BaseRESTClient):
    def __init__(self, auth: Optional[Auth] = None, delay: int = 20) -> None:
        super().__init__(auth)
        self.at_service_status = False
        self.delay = delay
        self.at_coro: List[Tuple[Handler, Optional[Auth]]] = []
        self.__at_task: Optional[asyncio.Task] = None
        self.__at_sleep_task: Optional[asyncio.Task] = None

    async def fetch_ats(
        self,
        at_time: Optional[int] = None,
        count: Optional[int] = None,
        auth: Optional[Auth] = None,
        _e_infos: Optional[List[Emoji]] = None,
    ) -> Ats:
        if not auth:
            auth = self.auth
        if not auth:
            raise ValueError("Auth is None, cannot get ats.")
        if not _e_infos:
            _e_infos = await get_e_infos(self)

        params = {}
        if at_time:
            params["at_time"] = at_time
        if not count:
            return Ats(
                e_infos=_e_infos,
                **(
                    (
                        await self.request_api(
                            "x/msgfeed/at",
                            "GET",
                            auth,
                            params=params,
                        )
                    )[0]
                ),
            )
        if count <= 0:
            raise ValueError("Count must > 0.")
        elif count <= 20:
            data = await self.fetch_ats(at_time, _e_infos=_e_infos, auth=auth)
            data.items = data.items[:count]
            return data
        else:
            now_data = await self.fetch_ats(
                at_time, _e_infos=_e_infos, auth=auth
            )
            early_data = await self.fetch_ats(
                now_data.cursor.time,
                _e_infos=_e_infos,
                count=count - 20,
                auth=auth,
            )
            now_data.cursor = early_data.cursor
            now_data.items.extend(early_data.items)
            return now_data

    # Fetch Service
    def add_at_handler(
        self, handler: Handler, auth: Optional[Auth] = None
    ) -> None:
        if auth is None:
            auth = self.auth
        self.at_coro.append((handler, auth))

    def at_handle(
        self, auth: Optional[Auth] = None
    ) -> Callable[[Handler], Handler]:
        def wrapper(func: Handler) -> Handler:
            self.add_at_handler(func, auth)
            return func

        return wrapper

    async def _fetch_all_ats(self, auth: Auth) -> List[At]:
        last_time = LAST_TIME.get(str(auth.SESSDATA), int(time.time()))
        ats = await self.fetch_ats(auth=auth)
        at = [i for i in ats.items if i.at_time > last_time]
        last_time = int(time.time())
        LAST_TIME[str(auth.SESSDATA)] = last_time
        return at

    async def run_at_fetch_service(self) -> None:
        while self.at_service_status:
            cache: Dict[str, List[At]] = {}
            for coro, auth in self.at_coro:
                # Fetch latest ats
                try:
                    events = []
                    if auth is None:
                        logger.warn(
                            f"Auth is None while running {coro}, ignore."
                        )
                        continue
                    SESSDATA = cast(str, auth.SESSDATA)
                    if SESSDATA not in cache:
                        cache[SESSDATA] = await self._fetch_all_ats(auth)
                    for at in cache[SESSDATA]:
                        at_dict = at.dict()
                        at_dict["item"].pop("source_content")
                        at_dict["item"][
                            "source_content"
                        ] = at.item.source_content
                        at_dict["auth"] = auth
                        at_dict["timestamp"] = at.at_time
                        at_dict["sender_uid"] = at.user.mid
                        at_dict["receiver_id"] = cast(int, auth.DedeUserID)
                        events.append(AtEvent.parse_obj(at_dict))

                except Exception:
                    logger.exception("Raised exception while fetching ats.")
                    continue

                # Call coroutines
                asyncio.create_task(handle_event(coro, events, self))

            try:
                self.__at_sleep_task = asyncio.create_task(
                    asyncio.sleep(self.delay)
                )
                await self.__at_sleep_task
            except asyncio.CancelledError:
                self.at_service_status = False
                break
            finally:
                self.__at_sleep_task = None
        self.__at_task = None

    async def start_at_fetch_service(self) -> None:
        if self.__at_task is not None and not self.__at_task.cancelled():
            raise RuntimeError("Ats fetch service has already started.")
        self.at_service_status = True
        self.__at_task = asyncio.create_task(self.run_at_fetch_service())
        logger.info("Ats fetch service started.")

    def stop_at_fetch_service(self) -> None:
        if self.__at_task is None or self.__at_task.cancelled():
            return
        elif self.__at_sleep_task and not self.__at_sleep_task.done():
            # asyncio.sleep is running
            self.__at_sleep_task.cancel()
        else:
            self.at_service_status = False
            self.__at_task.cancel()
        logger.info("Ats fetch service is closed.")

    async def close(self):
        self.stop_at_fetch_service()
        await super().close()

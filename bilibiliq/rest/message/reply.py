import time
import asyncio
import logging
from typing import Dict, List, Tuple, Callable, Optional, cast

from bilibiliq.auth import Auth
from bilibiliq.internal.client import BaseRESTClient

from .type import Handler
from .utils import get_e_infos
from .model import Emoji, Reply, Replies
from .event import ReplyEvent, handle_event

logger = logging.getLogger("bilibiliq.message.reply")
LAST_TIME: Dict[str, int] = {}


class ReplyClient(BaseRESTClient):
    def __init__(self, auth: Optional[Auth] = None, delay: int = 20) -> None:
        super().__init__(auth)
        self.reply_service_status = False
        self.delay = delay
        self.reply_coro: List[Tuple[Handler, Optional[Auth]]] = []
        self.__reply_task: Optional[asyncio.Task] = None
        self.__reply_sleep_task: Optional[asyncio.Task] = None

    async def fetch_replies(
        self,
        reply_time: Optional[int] = None,
        count: Optional[int] = None,
        auth: Optional[Auth] = None,
        _e_infos: Optional[List[Emoji]] = None,
    ) -> Replies:
        if not auth:
            auth = self.auth
        if not auth:
            raise ValueError("Auth is None, cannot get replies.")
        if not _e_infos:
            _e_infos = await get_e_infos(self)

        params = {}
        if reply_time:
            params["reply_time"] = reply_time
        if not count:
            return Replies(
                e_infos=_e_infos,
                **(
                    (
                        await self.request_api(
                            "x/msgfeed/reply",
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
            data = await self.fetch_replies(
                reply_time, _e_infos=_e_infos, auth=auth
            )
            data.items = data.items[:count]
            return data
        else:
            now_data = await self.fetch_replies(
                reply_time, _e_infos=_e_infos, auth=auth
            )
            early_data = await self.fetch_replies(
                now_data.cursor.time,
                _e_infos=_e_infos,
                count=count - 20,
                auth=auth,
            )
            now_data.cursor = early_data.cursor
            now_data.items.extend(early_data.items)
            return now_data

    # Fetch Service
    def add_reply_handler(
        self, handler: Handler, auth: Optional[Auth] = None
    ) -> None:
        if auth is None:
            auth = self.auth
        self.reply_coro.append((handler, auth))

    def reply_handle(
        self, auth: Optional[Auth] = None
    ) -> Callable[[Handler], Handler]:
        def wrapper(func: Handler):
            self.add_reply_handler(func, auth)
            return func

        return wrapper

    async def _fetch_all_replies(self, auth: Auth) -> List[Reply]:
        last_time = LAST_TIME.get(str(auth.SESSDATA), int(time.time()))
        replies = await self.fetch_replies(auth=auth)
        reply = [i for i in replies.items if i.reply_time > last_time]
        LAST_TIME[str(auth.SESSDATA)] = int(time.time())
        return reply

    async def run_reply_fetch_service(self) -> None:
        while self.reply_service_status:
            cache: Dict[str, List[Reply]] = {}
            for coro, auth in self.reply_coro:
                # Fetch latest replies
                try:
                    events = []
                    if auth is None:
                        logger.warn(
                            f"Auth is None while running {coro}, ignore."
                        )
                        continue
                    SESSDATA = cast(str, auth.SESSDATA)
                    if SESSDATA not in cache:
                        cache[SESSDATA] = await self._fetch_all_replies(auth)
                    for reply in cache[SESSDATA]:
                        reply_dict = reply.dict()
                        for key in (
                            "root_reply_content",
                            "source_content",
                            "target_reply_content",
                        ):
                            reply_dict["item"].pop(key)
                            reply_dict["item"][key] = getattr(reply.item, key)
                        reply_dict["auth"] = auth
                        reply_dict["timestamp"] = reply.reply_time
                        reply_dict["sender_uid"] = reply.user.mid
                        reply_dict["receiver_id"] = cast(int, auth.DedeUserID)
                        events.append(ReplyEvent.parse_obj(reply_dict))

                except Exception:
                    logger.exception(
                        "Raised exception while fetching replies."
                    )
                    continue

                # Call coroutines
                asyncio.create_task(handle_event(coro, events, self))

            try:
                self.__reply_sleep_task = asyncio.create_task(
                    asyncio.sleep(self.delay)
                )
                await self.__reply_sleep_task
            except asyncio.CancelledError:
                self.reply_service_status = False
                break
            finally:
                self.__reply_sleep_task = None
        self.__reply_task = None

    async def start_reply_fetch_service(self) -> None:
        if self.__reply_task is not None and not self.__reply_task.cancelled():
            raise RuntimeError("Replies fetch service has already started.")
        self.reply_service_status = True
        self.__reply_task = asyncio.create_task(self.run_reply_fetch_service())
        logger.info("Replies fetch service started.")

    def stop_reply_fetch_service(self) -> None:
        if self.__reply_task is None or self.__reply_task.cancelled():
            return
        elif self.__reply_sleep_task and not self.__reply_sleep_task.done():
            # asyncio.sleep is running
            self.__reply_sleep_task.cancel()
        else:
            self.reply_service_status = False
            self.__reply_task.cancel()
        logger.info("Replies fetch service is closed.")

    async def close(self):
        self.stop_reply_fetch_service()
        await super().close()

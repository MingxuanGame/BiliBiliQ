import time
import asyncio
import logging
from typing import Dict, List, Tuple, Callable, Optional, cast

from bilibiliq.auth import Auth
from bilibiliq.typing import AnyDict
from bilibiliq.internal.client import BaseRESTClient

from .model import Notify
from .type import Handler
from .event import LikeEvent, handle_event

logger = logging.getLogger("bilibiliq.message.notify")
LAST_TIME: Dict[str, int] = {}


class SystemNotifyClient(BaseRESTClient):
    def __init__(self, auth: Optional[Auth] = None, delay: int = 20) -> None:
        super().__init__(auth)
        self.notify_service_status = False
        self.delay = delay
        self.notify_coro: List[Tuple[Handler, Optional[Auth]]] = []
        self.__notify_task: Optional[asyncio.Task] = None
        self.__notify_sleep_task: Optional[asyncio.Task] = None

    async def fetch_notifies(
        self,
        cursor: Optional[int] = None,
        count: Optional[int] = None,
        auth: Optional[Auth] = None,
    ) -> List[Notify]:
        if not auth:
            auth = self.auth
        if not auth or not auth.bili_jct:
            raise ValueError("Auth is invalid, cannot get notifies.")

        params: AnyDict = {"csrf": auth.bili_jct}
        if cursor:
            params["cursor"] = cursor
        if not count:
            count = 20
        if count <= 0:
            raise ValueError("Count must > 0.")
        elif count <= 20:
            data = cast(
                List[AnyDict],
                (
                    await self.request_message_api(
                        "x/sys-msg/query_notify_list",
                        "GET",
                        auth,
                        params=params,
                    )
                )[0],
            )
            return [Notify(**i) for i in data][:count]
        else:
            now_data = await self.fetch_notifies(cursor, auth=auth)
            early_data = await self.fetch_notifies(
                now_data[-1].cursor,
                count=count - 20,
                auth=auth,
            )
            now_data.extend(early_data)
            return now_data

    # Fetch Service
    def add_notify_handler(
        self, handler: Handler, auth: Optional[Auth] = None
    ) -> None:
        if auth is None:
            auth = self.auth
        self.notify_coro.append((handler, auth))

    def notify_handle(
        self, auth: Optional[Auth] = None
    ) -> Callable[[Handler], Handler]:
        def wrapper(func: Handler):
            self.add_notify_handler(func, auth)
            return func

        return wrapper

    async def _fetch_all_notifies(self, auth: Auth) -> List[Notify]:
        last_time = LAST_TIME.get(str(auth.SESSDATA), int(time.time()))
        notifies = await self.fetch_notifies(auth=auth)
        notify = [
            i
            for i in notifies
            if time.mktime(time.strptime(i.time_at, "%Y-%m-%d %H:%M:%S"))
            > last_time
        ]
        last_time = int(time.time())
        LAST_TIME[str(auth.SESSDATA)] = last_time
        return notify

    async def run_notify_fetch_service(self) -> None:
        while self.notify_service_status:
            cache: Dict[str, List[Notify]] = {}
            for coro, auth in self.notify_coro:
                # Fetch latest replies
                try:
                    if auth is None:
                        logger.warn(
                            f"Auth is None while running {coro}, ignore."
                        )
                        continue
                    SESSDATA = cast(str, auth.SESSDATA)
                    if SESSDATA not in cache:
                        cache[SESSDATA] = await self._fetch_all_notifies(auth)
                    events = [
                        LikeEvent(
                            timestamp=int(
                                time.mktime(
                                    time.strptime(
                                        notify.time_at, "%Y-%m-%d %H:%M:%S"
                                    )
                                )
                            ),
                            sender_uid=-1,
                            receiver_id=cast(int, auth.DedeUserID),
                            auth=auth,
                            **notify.dict(),
                        )
                        for notify in cache[SESSDATA]
                    ]

                except Exception:
                    logger.exception(
                        "Raised exception while fetching notifies."
                    )
                    continue

                # Call coroutines
                asyncio.create_task(
                    handle_event(coro, events, self)  # type:ignore
                )

            try:
                self.__notify_sleep_task = asyncio.create_task(
                    asyncio.sleep(self.delay)
                )
                await self.__notify_sleep_task
            except asyncio.CancelledError:
                self.notify_service_status = False
                break
            finally:
                self.__notify_sleep_task = None
        self.__notify_task = None

    async def start_notify_fetch_service(self) -> None:
        if (
            self.__notify_task is not None
            and not self.__notify_task.cancelled()
        ):
            raise RuntimeError("Notifies fetch service has already started.")
        self.notify_service_status = True
        self.__notify_task = asyncio.create_task(
            self.run_notify_fetch_service()
        )
        logger.info("Notifies fetch service started.")

    def stop_notify_fetch_service(self) -> None:
        if self.__notify_task is None or self.__notify_task.cancelled():
            return
        elif self.__notify_sleep_task and not self.__notify_sleep_task.done():
            # asyncio.sleep is running
            self.__notify_sleep_task.cancel()
        else:
            self.notify_service_status = False
            self.__notify_task.cancel()
        logger.info("Notifies fetch service is closed.")

    async def close(self):
        self.stop_notify_fetch_service()
        await super().close()

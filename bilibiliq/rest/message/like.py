import time
import asyncio
import logging
from typing import Dict, List, Tuple, Callable, Optional, cast

from bilibiliq.auth import Auth
from bilibiliq.internal.client import BaseRESTClient

from .type import Handler
from .model import Like, Likes
from .event import LikeEvent, handle_event

logger = logging.getLogger("bilibiliq.message.like")
LAST_TIME: Dict[str, int] = {}


class LikeClient(BaseRESTClient):
    def __init__(self, auth: Optional[Auth] = None, delay: int = 20) -> None:
        super().__init__(auth)
        self.like_service_status = False
        self.delay = delay
        self.like_coro: List[Tuple[Handler, Optional[Auth]]] = []
        self.__like_task: Optional[asyncio.Task] = None
        self.__like_sleep_task: Optional[asyncio.Task] = None

    async def fetch_likes(
        self,
        like_time: Optional[int] = None,
        count: Optional[int] = None,
        auth: Optional[Auth] = None,
    ) -> Likes:
        if not auth:
            auth = self.auth
        if not auth:
            raise ValueError("Auth is None, cannot get likes.")

        params = {}
        if like_time:
            params["like_time"] = like_time
        if not count:
            return Likes(
                **(
                    (
                        await self.request_api(
                            "x/msgfeed/like",
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
            data = await self.fetch_likes(like_time, auth=auth)
            data.items = data.items[:count]
            return data
        else:
            now_data = await self.fetch_likes(like_time, auth=auth)
            early_data = await self.fetch_likes(
                now_data.cursor.time,
                count=count - 20,
                auth=auth,
            )
            now_data.cursor = early_data.cursor
            now_data.items.extend(early_data.items)
            return now_data

    # Fetch Service
    def add_like_handler(
        self, handler: Handler, auth: Optional[Auth] = None
    ) -> None:
        if auth is None:
            auth = self.auth
        self.like_coro.append((handler, auth))

    def like_handle(
        self, auth: Optional[Auth] = None
    ) -> Callable[[Handler], Handler]:
        def wrapper(func: Handler):
            self.add_like_handler(func, auth)
            return func

        return wrapper

    async def _fetch_all_likes(self, auth: Auth) -> List[Like]:
        last_time = LAST_TIME.get(str(auth.SESSDATA), int(time.time()))
        likes = await self.fetch_likes(auth=auth)
        like = [
            i for i in likes.latest + likes.items if i.like_time > last_time
        ]
        last_time = int(time.time())
        LAST_TIME[str(auth.SESSDATA)] = last_time
        return like

    async def run_like_fetch_service(self) -> None:
        while self.like_service_status:
            cache: Dict[str, List[Like]] = {}
            for coro, auth in self.like_coro:
                # Fetch latest likes
                try:
                    if auth is None:
                        logger.warn(
                            f"Auth is None while running {coro}, ignore."
                        )
                        continue
                    SESSDATA = cast(str, auth.SESSDATA)
                    if SESSDATA not in cache:
                        cache[SESSDATA] = await self._fetch_all_likes(auth)
                    events = [
                        LikeEvent(
                            timestamp=like.like_time,
                            sender_uid=like.users[0].mid,
                            receiver_id=cast(int, auth.DedeUserID),
                            auth=auth,
                            **like.dict(),
                        )
                        for like in cache[SESSDATA]
                    ]

                except Exception:
                    logger.exception("Raised exception while fetching likes.")
                    continue

                # Call coroutines
                asyncio.create_task(
                    handle_event(coro, events, self)  # type:ignore
                )

            try:
                self.__like_sleep_task = asyncio.create_task(
                    asyncio.sleep(self.delay)
                )
                await self.__like_sleep_task
            except asyncio.CancelledError:
                self.like_service_status = False
                break
            finally:
                self.__like_sleep_task = None
        self.__like_task = None

    async def start_like_fetch_service(self) -> None:
        if self.__like_task is not None and not self.__like_task.cancelled():
            raise RuntimeError("Likes fetch service has already started.")
        self.like_service_status = True
        self.__like_task = asyncio.create_task(self.run_like_fetch_service())
        logger.info("Likes fetch service started.")

    def stop_like_fetch_service(self) -> None:
        if self.__like_task is None or self.__like_task.cancelled():
            return
        elif self.__like_sleep_task and not self.__like_sleep_task.done():
            # asyncio.sleep is running
            self.__like_sleep_task.cancel()
        else:
            self.like_service_status = False
            self.__like_task.cancel()
        logger.info("Likes fetch service is closed.")

    async def close(self):
        self.stop_like_fetch_service()
        await super().close()

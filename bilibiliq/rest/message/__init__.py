from typing import Callable, Optional

from bilibiliq.auth import Auth

from .at import AtClient
from .type import Handler
from .like import LikeClient
from .reply import ReplyClient
from .private_msg import PrivateMessageClient
from .system_notify import SystemNotifyClient


class MessageClient(
    PrivateMessageClient, ReplyClient, AtClient, LikeClient, SystemNotifyClient
):
    def __init__(self, auth: Optional[Auth] = None, delay: int = 20) -> None:
        super().__init__(auth, delay)

    def add_handler(
        self, handler: Handler, auth: Optional[Auth] = None
    ) -> None:
        if auth is None:
            auth = self.auth
        self.reply_coro.append((handler, auth))
        self.at_coro.append((handler, auth))
        self.msg_coro.append((handler, auth))
        self.like_coro.append((handler, auth))
        self.notify_coro.append((handler, auth))

    def handle(
        self, auth: Optional[Auth] = None
    ) -> Callable[[Handler], Handler]:
        def wrapper(func: Handler) -> Handler:
            self.add_handler(func, auth)
            return func

        return wrapper

    async def start_fetch_service(self):
        await self.start_msg_fetch_service()
        await self.start_like_fetch_service()
        await self.start_at_fetch_service()
        await self.start_reply_fetch_service()
        await self.start_notify_fetch_service()

    def stop_fetch_service(self):
        self.stop_msg_fetch_service()
        self.stop_like_fetch_service()
        self.stop_at_fetch_service()
        self.stop_reply_fetch_service()
        self.stop_notify_fetch_service()

    async def close(self):
        self.stop_fetch_service()
        await self.session.close()

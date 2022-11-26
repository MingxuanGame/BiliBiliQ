import json
import time
import asyncio
import logging
from functools import wraps
from typing import Dict, List, Tuple, Union, Literal, Optional, cast

from aiohttp import FormData

from bilibiliq.auth import Auth
from bilibiliq.utils import generate_dev_id
from bilibiliq.internal.client import BaseRESTClient

from .type import Handler
from .utils import get_e_infos
from .event import handle_event, make_message_event
from .model import (
    Text,
    Emoji,
    Image,
    Message,
    Messages,
    Sessions,
    MessageContent,
)

logger = logging.getLogger("bilibiliq.message.private_msg")
SEQNO: Dict[str, int] = {}


class PrivateMessageClient(BaseRESTClient):
    def __init__(self, auth: Optional[Auth] = None, delay: int = 20) -> None:
        super().__init__(auth)
        self.message_service_status = False
        self.delay = delay
        self.msg_coro: List[Tuple[Handler, Optional[Auth]]] = []
        self.__msg_task: Optional[asyncio.Task] = None
        self.__msg_sleep_task: Optional[asyncio.Task] = None

    async def get_sessions(
        self, session_type: int = 1, auth: Optional[Auth] = None
    ) -> Sessions:
        data = (
            await self.request_vc_api(
                "session_svr/v1/session_svr/get_sessions",
                "GET",
                auth,
                params={"session_type": session_type},
            )
        )[0]
        e_infos = await get_e_infos(self)
        return Sessions(e_infos=e_infos, **data)

    async def fetch_messages(
        self,
        talker_id: int,
        session_type: int = 1,
        size: Optional[int] = None,
        begin_seqno: Optional[int] = None,
        auth: Optional[Auth] = None,
    ) -> Messages:
        if not auth:
            auth = self.auth
        if not auth:
            raise ValueError("Auth is None, cannot get messages.")

        params = {
            "talker_id": talker_id,
            "session_type": session_type,
        }
        if size:
            params["size"] = size
        if begin_seqno:
            params["begin_seqno"] = begin_seqno
        return Messages.parse_obj(
            (
                await self.request_vc_api(
                    "svr_sync/v1/svr_sync/fetch_session_msgs",
                    "GET",
                    auth,
                    params=params,
                )
            )[0]
        )

    async def upload_image(
        self, image: bytes, auth: Optional[Auth] = None
    ) -> Image:
        if not auth:
            auth = self.auth
        if not auth or auth.bili_jct is None:
            raise ValueError("Auth is invalid, cannot upload an image.")
        form = FormData({"file_up": image, "csrf": auth.bili_jct})
        data = (
            await self.request_api(
                "x/dynamic/feed/draw/upload_bfs", "POST", auth=auth, data=form
            )
        )[0]
        url = data["image_url"]
        width = data["image_width"]
        height = data["image_height"]
        return Image(
            width=width,
            height=height,
            original=True,
            url=url,
            size=100,
            imageType=url.split(".")[-1],  # type: ignore
        )

    async def send_msg(
        self,
        receiver_id: int,
        msg_type: Literal[1, 2],
        message: Union[str, Image, List[MessageContent]],
        auth: Optional[Auth] = None,
    ) -> int:
        if not auth:
            auth = self.auth
        if not auth or auth.bili_jct is None or auth.DedeUserID is None:
            raise ValueError("Auth is invalid, cannot send messages.")

        if msg_type == 2:
            if not isinstance(message, Image):
                raise TypeError(
                    "The message must be Image object when msg_type=2."
                )
            content = message.to_dict()
        elif isinstance(message, str):
            content = {"content": message}
        else:
            content = {"content": ""}
            for i in message:
                if not isinstance(i, (Emoji, Text)):
                    logger.warn(
                        "Only support Emoji & Text when msg_type=1,ignore."
                    )
                content["content"] += str(i)
            if not content["content"]:
                raise ValueError("Message is empty.")

        params = {
            "msg[sender_uid]": auth.DedeUserID,
            "msg[receiver_id]": receiver_id,
            "msg[receiver_type]": 1,
            "msg[msg_type]": msg_type,
            "msg[msg_status]": 0,
            # ensure_ascii=False 保证表情被B站正常解析至 e_infos
            "msg[content]": json.dumps(content, ensure_ascii=False),
            "msg[timestamp]": int(time.time()),
            "msg[new_face_version]": 0,
            "msg[dev_id]": generate_dev_id(),
            "csrf_token": auth.bili_jct,
            "csrf": auth.bili_jct,
        }
        data = (
            await self.request_vc_api(
                "web_im/v1/web_im/send_msg", "POST", data=params, auth=auth
            )
        )[0]
        return data["msg_key"]

    # Fetch Services

    def add_message_handler(
        self, handler: Handler, auth: Optional[Auth] = None
    ) -> None:
        if auth is None:
            auth = self.auth
        self.msg_coro.append((handler, auth))

    def msg_handle(self, auth: Optional[Auth] = None):
        def wrapper(func: Handler):
            @wraps(func)
            def inner():
                self.add_message_handler(func, auth)
                return func

            return inner

        return wrapper

    async def _fetch_all_messages(
        self, auth: Auth
    ) -> List[Tuple[Message, int]]:
        sessions = await self.get_sessions()
        messages: List[Tuple[Message, int]] = []
        for session in sessions.session_list:
            talker_id = session.talker_id
            session_id = f"{auth.SESSDATA}-{talker_id}"
            last_seqno = SEQNO.get(session_id, session.max_seqno)
            session_messages = await self.fetch_messages(
                talker_id, begin_seqno=last_seqno
            )
            if messages_ := session_messages.messages:
                messages.extend(reversed([(i, talker_id) for i in messages_]))
            SEQNO[session_id] = session.max_seqno
        return messages

    async def run_msg_fetch_service(self) -> None:
        while self.message_service_status:
            cache: Dict[str, List[Tuple[Message, int]]] = {}
            for coro, auth in self.msg_coro:
                # Fetch latest messages
                try:
                    events = []
                    if auth is None:
                        logger.warn(
                            f"Auth is None while running {coro}, ignore."
                        )
                        continue
                    SESSDATA = cast(str, auth.SESSDATA)
                    if SESSDATA not in cache:
                        cache[SESSDATA] = await self._fetch_all_messages(auth)
                    for message, talker_id in cache[SESSDATA]:
                        events.append(
                            await make_message_event(
                                talker_id, message, self, auth
                            )
                        )
                except Exception:
                    logger.exception(
                        "Raised exception while fetching messages."
                    )
                    continue

                # Call coroutines
                asyncio.create_task(handle_event(coro, events, self))

            try:
                self.__msg_sleep_task = asyncio.create_task(
                    asyncio.sleep(self.delay)
                )
                await self.__msg_sleep_task
            except asyncio.CancelledError:
                self.message_service_status = False
                break
            finally:
                self.__msg_sleep_task = None
        self.__msg_task = None

    async def start_msg_fetch_service(self) -> None:
        if self.__msg_task is not None and not self.__msg_task.cancelled():
            raise RuntimeError("Messages fetch service has already started.")
        self.message_service_status = True
        self.__msg_task = asyncio.create_task(self.run_msg_fetch_service())
        logger.info("Messages fetch service started.")

    def stop_msg_fetch_service(self) -> None:
        if self.__msg_task is None or self.__msg_task.cancelled():
            return
        elif self.__msg_sleep_task and not self.__msg_sleep_task.done():
            # asyncio.sleep is running
            self.__msg_sleep_task.cancel()
        else:
            self.message_service_status = False
            self.__msg_task.cancel()
        logger.info("Messages fetch service is closed.")

    async def close(self):
        self.stop_msg_fetch_service()
        await super().close()

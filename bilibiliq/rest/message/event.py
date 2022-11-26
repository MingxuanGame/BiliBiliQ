import asyncio
import logging
from typing import TYPE_CHECKING, List, Optional, cast

from pydantic import BaseModel

from bilibiliq.auth import Auth

from .type import Handler, TypeMessageClient
from .model import At, Like, Reply, Notice, Notify, Recall, Message

if TYPE_CHECKING:
    from .private_msg import PrivateMessageClient

logger = logging.getLogger("bilibiliq.message")


class Event(BaseModel):
    auth: Auth
    """鉴权信息"""
    timestamp: int
    """消息发送时间戳"""
    sender_uid: int
    """发送者 UID"""
    receiver_id: int
    """接收者 UID"""


class MessageEvent(Event, Message):
    ...


class NoticeEvent(Event, Notice):
    ...


class ReplyEvent(Event, Reply):
    ...


class AtEvent(Event, At):
    ...


class LikeEvent(Event, Like):
    ...


class SystemNotifyEvent(Event, Notify):
    ...


class RecallEvent(Event, Recall):
    message: Optional[Message] = None
    """被撤回的消息"""


async def make_message_event(
    talker_id: int,
    message: Message,
    client: "PrivateMessageClient",
    auth: Auth,
) -> Event:
    if message.msg_type == 5:
        msg_key = cast(Recall, message.content[0]).msg_key
        messages = await client.fetch_messages(talker_id, size=200, auth=auth)
        recall_message = None
        if messages_ := messages.messages:
            for i in messages_:
                if i.msg_key == msg_key:
                    recall_message = i
                    break
        if not recall_message:
            logger.warn(f"Cannot find the message of key {msg_key}")
        return RecallEvent(
            timestamp=message.timestamp,
            sender_uid=message.sender_uid,
            receiver_id=message.receiver_id,
            msg_key=msg_key,
            message=recall_message,
            auth=auth,
        )
    elif len(message.content) == 1 and isinstance(message.content[0], Notice):
        return NoticeEvent(
            auth=auth,
            timestamp=message.timestamp,
            sender_uid=message.sender_uid,
            receiver_id=message.receiver_id,
            **message.content[0].dict(),
        )
    else:
        message_dict = message.dict()
        message_dict.pop("content")
        message_dict["content"] = message.content
        message_dict["auth"] = auth
        return MessageEvent.parse_obj(message_dict)


async def handle_event(
    coro: Handler, events: List[Event], client: TypeMessageClient
) -> None:
    try:
        await asyncio.gather(*[coro(event, client) for event in events])
    except Exception:
        logger.exception(f"Raised exception while running {coro}.")

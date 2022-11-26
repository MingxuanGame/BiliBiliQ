from typing import TYPE_CHECKING, Any, Union, TypeVar, Callable

if TYPE_CHECKING:
    from .at import AtClient
    from .event import Event
    from .like import LikeClient
    from .reply import ReplyClient
    from .private_msg import PrivateMessageClient
    from .system_notify import SystemNotifyClient

TypeMessageClient = Union[
    "PrivateMessageClient",
    "SystemNotifyClient",
    "ReplyClient",
    "AtClient",
    "LikeClient",
]
T_MessageClient = TypeVar("T_MessageClient", bound=TypeMessageClient)
Handler = Callable[["Event", T_MessageClient], Any]

"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PlayStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PlayStatusEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _PlayStatus.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    Pause: _PlayStatus.ValueType  # 0
    """暂停"""
    Play: _PlayStatus.ValueType  # 1
    """播放"""
    End: _PlayStatus.ValueType  # 2
    """终止"""

class PlayStatus(_PlayStatus, metaclass=_PlayStatusEnumTypeWrapper):
    """播放状态"""

Pause: PlayStatus.ValueType  # 0
"""暂停"""
Play: PlayStatus.ValueType  # 1
"""播放"""
End: PlayStatus.ValueType  # 2
"""终止"""
global___PlayStatus = PlayStatus

class _RoomType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _RoomTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _RoomType.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    Private: _RoomType.ValueType  # 0
    """私密"""
    Open: _RoomType.ValueType  # 1
    """公开"""

class RoomType(_RoomType, metaclass=_RoomTypeEnumTypeWrapper):
    """房间类型"""

Private: RoomType.ValueType  # 0
"""私密"""
Open: RoomType.ValueType  # 1
"""公开"""
global___RoomType = RoomType

class _MessageDomain:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _MessageDomainEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _MessageDomain.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DefaultDomain: _MessageDomain.ValueType  # 0
    """默认"""
    RoomMid: _MessageDomain.ValueType  # 1
    """房间用户"""
    SystemInfo: _MessageDomain.ValueType  # 2
    """系统通知"""

class MessageDomain(_MessageDomain, metaclass=_MessageDomainEnumTypeWrapper):
    """信息通知发送领域"""

DefaultDomain: MessageDomain.ValueType  # 0
"""默认"""
RoomMid: MessageDomain.ValueType  # 1
"""房间用户"""
SystemInfo: MessageDomain.ValueType  # 2
"""系统通知"""
global___MessageDomain = MessageDomain

class _MessageType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _MessageTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _MessageType.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DefaultType: _MessageType.ValueType  # 0
    """默认"""
    ChatMessage: _MessageType.ValueType  # 1
    """房间用户"""
    SystemMessage: _MessageType.ValueType  # 2
    """系统通知"""

class MessageType(_MessageType, metaclass=_MessageTypeEnumTypeWrapper):
    """通知信息类型"""

DefaultType: MessageType.ValueType  # 0
"""默认"""
ChatMessage: MessageType.ValueType  # 1
"""房间用户"""
SystemMessage: MessageType.ValueType  # 2
"""系统通知"""
global___MessageType = MessageType

class _TriggerType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _TriggerTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _TriggerType.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DefaultTrigger: _TriggerType.ValueType  # 0
    """默认"""
    Relation: _TriggerType.ValueType  # 1
    """关注、取消关注"""

class TriggerType(_TriggerType, metaclass=_TriggerTypeEnumTypeWrapper):
    """触发通知类型"""

DefaultTrigger: TriggerType.ValueType  # 0
"""默认"""
Relation: TriggerType.ValueType  # 1
"""关注、取消关注"""
global___TriggerType = TriggerType

@typing_extensions.final
class RoomMemberChangeEvent(google.protobuf.message.Message):
    """房间人员变更事件"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROOM_ID_FIELD_NUMBER: builtins.int
    OWNER_ID_FIELD_NUMBER: builtins.int
    MEMBERS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    room_id: builtins.int
    """房间id"""
    owner_id: builtins.int
    """房主id"""
    @property
    def members(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___UserInfoProto
    ]:
        """房间成员列表"""
    @property
    def message(self) -> global___MessageProto:
        """提示信息"""
    def __init__(
        self,
        *,
        room_id: builtins.int = ...,
        owner_id: builtins.int = ...,
        members: collections.abc.Iterable[global___UserInfoProto] | None = ...,
        message: global___MessageProto | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["message", b"message"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "members",
            b"members",
            "message",
            b"message",
            "owner_id",
            b"owner_id",
            "room_id",
            b"room_id",
        ],
    ) -> None: ...

global___RoomMemberChangeEvent = RoomMemberChangeEvent

@typing_extensions.final
class ProgressSyncEvent(google.protobuf.message.Message):
    """播放进度同步事件"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROOM_ID_FIELD_NUMBER: builtins.int
    SEASON_ID_FIELD_NUMBER: builtins.int
    EPISODE_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    room_id: builtins.int
    """房间id"""
    season_id: builtins.int
    """播放中的season_id"""
    episode_id: builtins.int
    """播放中的episode_id"""
    status: global___PlayStatus.ValueType
    """播放状态"""
    progress: builtins.int
    """房主播放进度"""
    @property
    def message(self) -> global___MessageProto:
        """提示信息"""
    def __init__(
        self,
        *,
        room_id: builtins.int = ...,
        season_id: builtins.int = ...,
        episode_id: builtins.int = ...,
        status: global___PlayStatus.ValueType = ...,
        progress: builtins.int = ...,
        message: global___MessageProto | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["message", b"message"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "episode_id",
            b"episode_id",
            "message",
            b"message",
            "progress",
            b"progress",
            "room_id",
            b"room_id",
            "season_id",
            b"season_id",
            "status",
            b"status",
        ],
    ) -> None: ...

global___ProgressSyncEvent = ProgressSyncEvent

@typing_extensions.final
class RoomUpdateEvent(google.protobuf.message.Message):
    """房间状态更新"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROOM_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    room_id: builtins.int
    """房间id"""
    type: global___RoomType.ValueType
    """房间变更状态"""
    @property
    def message(self) -> global___MessageProto:
        """提示信息"""
    def __init__(
        self,
        *,
        room_id: builtins.int = ...,
        type: global___RoomType.ValueType = ...,
        message: global___MessageProto | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["message", b"message"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "message", b"message", "room_id", b"room_id", "type", b"type"
        ],
    ) -> None: ...

global___RoomUpdateEvent = RoomUpdateEvent

@typing_extensions.final
class RoomDestroyEvent(google.protobuf.message.Message):
    """房间销毁通知"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROOM_ID_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    room_id: builtins.int
    """房间id"""
    @property
    def message(self) -> global___MessageProto:
        """提示信息"""
    def __init__(
        self,
        *,
        room_id: builtins.int = ...,
        message: global___MessageProto | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["message", b"message"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "message", b"message", "room_id", b"room_id"
        ],
    ) -> None: ...

global___RoomDestroyEvent = RoomDestroyEvent

@typing_extensions.final
class RoomTriggerEvent(google.protobuf.message.Message):
    """房间触发通知"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MID_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    TRIGGER_FIELD_NUMBER: builtins.int
    mid: builtins.int
    """操作人"""
    @property
    def message(self) -> global___MessageProto:
        """提示信息"""
    trigger: global___TriggerType.ValueType
    """触发类型"""
    def __init__(
        self,
        *,
        mid: builtins.int = ...,
        message: global___MessageProto | None = ...,
        trigger: global___TriggerType.ValueType = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["message", b"message"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "message", b"message", "mid", b"mid", "trigger", b"trigger"
        ],
    ) -> None: ...

global___RoomTriggerEvent = RoomTriggerEvent

@typing_extensions.final
class UserInfoProto(google.protobuf.message.Message):
    """用户信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MID_FIELD_NUMBER: builtins.int
    FACE_FIELD_NUMBER: builtins.int
    NICKNAME_FIELD_NUMBER: builtins.int
    LEVEL_FIELD_NUMBER: builtins.int
    SIGN_FIELD_NUMBER: builtins.int
    VIP_FIELD_NUMBER: builtins.int
    OFFICIAL_FIELD_NUMBER: builtins.int
    PENDANT_FIELD_NUMBER: builtins.int
    BUVID_FIELD_NUMBER: builtins.int
    mid: builtins.int
    """用户id"""
    face: builtins.str
    """用户头像url"""
    nickname: builtins.str
    """昵称"""
    level: builtins.int
    """等级"""
    sign: builtins.str
    """签名"""
    @property
    def vip(self) -> global___VipProto:
        """大会员信息"""
    @property
    def official(self) -> global___OfficialProto:
        """身份认证信息"""
    @property
    def pendant(self) -> global___PendantProto:
        """挂件信息"""
    buvid: builtins.str
    """设备buvid"""
    def __init__(
        self,
        *,
        mid: builtins.int = ...,
        face: builtins.str = ...,
        nickname: builtins.str = ...,
        level: builtins.int = ...,
        sign: builtins.str = ...,
        vip: global___VipProto | None = ...,
        official: global___OfficialProto | None = ...,
        pendant: global___PendantProto | None = ...,
        buvid: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "official", b"official", "pendant", b"pendant", "vip", b"vip"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "buvid",
            b"buvid",
            "face",
            b"face",
            "level",
            b"level",
            "mid",
            b"mid",
            "nickname",
            b"nickname",
            "official",
            b"official",
            "pendant",
            b"pendant",
            "sign",
            b"sign",
            "vip",
            b"vip",
        ],
    ) -> None: ...

global___UserInfoProto = UserInfoProto

@typing_extensions.final
class MessageProto(google.protobuf.message.Message):
    """通知信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTENT_FIELD_NUMBER: builtins.int
    CONTENT_TYPE_FIELD_NUMBER: builtins.int
    content: builtins.str
    """可带占位符匹配的消息体 ep "还没有其他小伙伴，[去邀请>]<https://big.bilibili.com/mobile/giftIndex?mid=123>" """
    content_type: builtins.int
    """消息体类型
    0:json格式的文本消息 1:支持全文本可点(破冰)
    """
    def __init__(
        self,
        *,
        content: builtins.str = ...,
        content_type: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "content", b"content", "content_type", b"content_type"
        ],
    ) -> None: ...

global___MessageProto = MessageProto

@typing_extensions.final
class VipProto(google.protobuf.message.Message):
    """大会员信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    DUE_DATE_FIELD_NUMBER: builtins.int
    VIP_PAY_TYPE_FIELD_NUMBER: builtins.int
    THEME_TYPE_FIELD_NUMBER: builtins.int
    AVATAR_SUBSCRIPT_FIELD_NUMBER: builtins.int
    NICKNAME_COLOR_FIELD_NUMBER: builtins.int
    type: builtins.int
    status: builtins.int
    due_date: builtins.int
    vip_pay_type: builtins.int
    theme_type: builtins.int
    avatar_subscript: builtins.int
    """大会员角标
    0:无角标 1:粉色大会员角标 2:绿色小会员角标
    """
    nickname_color: builtins.str
    """昵称色值，可能为空，色值示例：#FFFB9E60"""
    def __init__(
        self,
        *,
        type: builtins.int = ...,
        status: builtins.int = ...,
        due_date: builtins.int = ...,
        vip_pay_type: builtins.int = ...,
        theme_type: builtins.int = ...,
        avatar_subscript: builtins.int = ...,
        nickname_color: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "avatar_subscript",
            b"avatar_subscript",
            "due_date",
            b"due_date",
            "nickname_color",
            b"nickname_color",
            "status",
            b"status",
            "theme_type",
            b"theme_type",
            "type",
            b"type",
            "vip_pay_type",
            b"vip_pay_type",
        ],
    ) -> None: ...

global___VipProto = VipProto

@typing_extensions.final
class OfficialProto(google.protobuf.message.Message):
    """认证信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLE_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    role: builtins.int
    title: builtins.str
    desc: builtins.str
    type: builtins.int
    def __init__(
        self,
        *,
        role: builtins.int = ...,
        title: builtins.str = ...,
        desc: builtins.str = ...,
        type: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "desc",
            b"desc",
            "role",
            b"role",
            "title",
            b"title",
            "type",
            b"type",
        ],
    ) -> None: ...

global___OfficialProto = OfficialProto

@typing_extensions.final
class PendantProto(google.protobuf.message.Message):
    """挂件信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_NUMBER: builtins.int
    EXPIRE_FIELD_NUMBER: builtins.int
    IMAGE_ENHANCE_FIELD_NUMBER: builtins.int
    pid: builtins.int
    name: builtins.str
    image: builtins.str
    expire: builtins.int
    image_enhance: builtins.str
    def __init__(
        self,
        *,
        pid: builtins.int = ...,
        name: builtins.str = ...,
        image: builtins.str = ...,
        expire: builtins.int = ...,
        image_enhance: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "expire",
            b"expire",
            "image",
            b"image",
            "image_enhance",
            b"image_enhance",
            "name",
            b"name",
            "pid",
            b"pid",
        ],
    ) -> None: ...

global___PendantProto = PendantProto

@typing_extensions.final
class MessageEvent(google.protobuf.message.Message):
    """通用信息通知"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROOM_ID_FIELD_NUMBER: builtins.int
    MSG_ID_FIELD_NUMBER: builtins.int
    TS_FIELD_NUMBER: builtins.int
    OID_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    MSG_ID2_FIELD_NUMBER: builtins.int
    room_id: builtins.int
    """房间id"""
    msg_id: builtins.int
    """消息id"""
    ts: builtins.int
    """消息发送服务端时间 时间戳 单位秒"""
    oid: builtins.int
    """信息通知发送主体id"""
    domain: global___MessageDomain.ValueType
    """信息通知发送领域"""
    type: global___MessageType.ValueType
    """通知信息类型"""
    @property
    def message(self) -> global___MessageProto:
        """提示信息"""
    @property
    def user(self) -> global___UserInfoProto:
        """消息发送用户信息"""
    msg_id2: builtins.str
    """消息id str类型"""
    def __init__(
        self,
        *,
        room_id: builtins.int = ...,
        msg_id: builtins.int = ...,
        ts: builtins.int = ...,
        oid: builtins.int = ...,
        domain: global___MessageDomain.ValueType = ...,
        type: global___MessageType.ValueType = ...,
        message: global___MessageProto | None = ...,
        user: global___UserInfoProto | None = ...,
        msg_id2: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "message", b"message", "user", b"user"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "domain",
            b"domain",
            "message",
            b"message",
            "msg_id",
            b"msg_id",
            "msg_id2",
            b"msg_id2",
            "oid",
            b"oid",
            "room_id",
            b"room_id",
            "ts",
            b"ts",
            "type",
            b"type",
            "user",
            b"user",
        ],
    ) -> None: ...

global___MessageEvent = MessageEvent

@typing_extensions.final
class RemoveChatEvent(google.protobuf.message.Message):
    """聊天信息清除通知"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROOM_ID_FIELD_NUMBER: builtins.int
    MSG_ID_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    room_id: builtins.int
    """房间id"""
    msg_id: builtins.int
    """撤回的聊天信息id"""
    @property
    def message(self) -> global___MessageProto:
        """提示信息"""
    def __init__(
        self,
        *,
        room_id: builtins.int = ...,
        msg_id: builtins.int = ...,
        message: global___MessageProto | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["message", b"message"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "message", b"message", "msg_id", b"msg_id", "room_id", b"room_id"
        ],
    ) -> None: ...

global___RemoveChatEvent = RemoveChatEvent

@typing_extensions.final
class FreyaEventBody(google.protobuf.message.Message):
    """ "一起看"房间事件"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROOM_ID_FIELD_NUMBER: builtins.int
    WHITE_MID_FIELD_NUMBER: builtins.int
    IGNORE_MID_FIELD_NUMBER: builtins.int
    MEMBER_CHANGE_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    ROOM_UPDATE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    REMOVE_CHAT_FIELD_NUMBER: builtins.int
    ROOM_DESTROY_FIELD_NUMBER: builtins.int
    ROOM_TRIGGER_FIELD_NUMBER: builtins.int
    SEQUENCE_ID_FIELD_NUMBER: builtins.int
    room_id: builtins.int
    """房间id"""
    @property
    def white_mid(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.int
    ]:
        """接收事件消息的白名单用户"""
    @property
    def ignore_mid(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.int
    ]:
        """不处理信息的黑名单用户 优先级低于白名单 当白名单有数据时 忽略黑名单"""
    @property
    def member_change(self) -> global___RoomMemberChangeEvent:
        """房间人员变更事件"""
    @property
    def progress(self) -> global___ProgressSyncEvent:
        """播放进度同步事件"""
    @property
    def room_update(self) -> global___RoomUpdateEvent:
        """房间状态更新"""
    @property
    def message(self) -> global___MessageEvent:
        """通用信息通知"""
    @property
    def remove_chat(self) -> global___RemoveChatEvent:
        """聊天信息清除通知"""
    @property
    def room_destroy(self) -> global___RoomDestroyEvent:
        """房间销毁通知"""
    @property
    def room_trigger(self) -> global___RoomTriggerEvent:
        """房间触发通知"""
    sequence_id: builtins.int
    """消息序列号"""
    def __init__(
        self,
        *,
        room_id: builtins.int = ...,
        white_mid: collections.abc.Iterable[builtins.int] | None = ...,
        ignore_mid: collections.abc.Iterable[builtins.int] | None = ...,
        member_change: global___RoomMemberChangeEvent | None = ...,
        progress: global___ProgressSyncEvent | None = ...,
        room_update: global___RoomUpdateEvent | None = ...,
        message: global___MessageEvent | None = ...,
        remove_chat: global___RemoveChatEvent | None = ...,
        room_destroy: global___RoomDestroyEvent | None = ...,
        room_trigger: global___RoomTriggerEvent | None = ...,
        sequence_id: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "event",
            b"event",
            "member_change",
            b"member_change",
            "message",
            b"message",
            "progress",
            b"progress",
            "remove_chat",
            b"remove_chat",
            "room_destroy",
            b"room_destroy",
            "room_trigger",
            b"room_trigger",
            "room_update",
            b"room_update",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "event",
            b"event",
            "ignore_mid",
            b"ignore_mid",
            "member_change",
            b"member_change",
            "message",
            b"message",
            "progress",
            b"progress",
            "remove_chat",
            b"remove_chat",
            "room_destroy",
            b"room_destroy",
            "room_id",
            b"room_id",
            "room_trigger",
            b"room_trigger",
            "room_update",
            b"room_update",
            "sequence_id",
            b"sequence_id",
            "white_mid",
            b"white_mid",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["event", b"event"]
    ) -> typing_extensions.Literal[
        "member_change",
        "progress",
        "room_update",
        "message",
        "remove_chat",
        "room_destroy",
        "room_trigger",
    ] | None: ...

global___FreyaEventBody = FreyaEventBody

"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilibili.rpc.status_pb2
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class RoomErrorEvent(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    @property
    def status(self) -> bilibili.rpc.status_pb2.Status:
        """"""
    def __init__(
        self,
        *,
        status: bilibili.rpc.status_pb2.Status | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["status", b"status"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["status", b"status"]
    ) -> None: ...

global___RoomErrorEvent = RoomErrorEvent

@typing_extensions.final
class RoomJoinEvent(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RoomJoinEvent = RoomJoinEvent

@typing_extensions.final
class RoomLeaveEvent(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RoomLeaveEvent = RoomLeaveEvent

@typing_extensions.final
class RoomMessageEvent(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_PATH_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    target_path: builtins.str
    """"""
    @property
    def body(self) -> google.protobuf.any_pb2.Any:
        """"""
    def __init__(
        self,
        *,
        target_path: builtins.str = ...,
        body: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["body", b"body"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "body", b"body", "target_path", b"target_path"
        ],
    ) -> None: ...

global___RoomMessageEvent = RoomMessageEvent

@typing_extensions.final
class RoomOnlineEvent(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ONLINE_FIELD_NUMBER: builtins.int
    ALL_ONLINE_FIELD_NUMBER: builtins.int
    online: builtins.int
    """"""
    all_online: builtins.int
    """"""
    def __init__(
        self,
        *,
        online: builtins.int = ...,
        all_online: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "all_online", b"all_online", "online", b"online"
        ],
    ) -> None: ...

global___RoomOnlineEvent = RoomOnlineEvent

@typing_extensions.final
class RoomReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    JOIN_FIELD_NUMBER: builtins.int
    LEAVE_FIELD_NUMBER: builtins.int
    ONLINE_FIELD_NUMBER: builtins.int
    MSG_FIELD_NUMBER: builtins.int
    id: builtins.str
    """{type}://{room_id}"""
    @property
    def join(self) -> global___RoomJoinEvent:
        """"""
    @property
    def leave(self) -> global___RoomLeaveEvent:
        """"""
    @property
    def online(self) -> global___RoomOnlineEvent:
        """"""
    @property
    def msg(self) -> global___RoomMessageEvent:
        """"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        join: global___RoomJoinEvent | None = ...,
        leave: global___RoomLeaveEvent | None = ...,
        online: global___RoomOnlineEvent | None = ...,
        msg: global___RoomMessageEvent | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "event",
            b"event",
            "join",
            b"join",
            "leave",
            b"leave",
            "msg",
            b"msg",
            "online",
            b"online",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "event",
            b"event",
            "id",
            b"id",
            "join",
            b"join",
            "leave",
            b"leave",
            "msg",
            b"msg",
            "online",
            b"online",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["event", b"event"]
    ) -> typing_extensions.Literal[
        "join", "leave", "online", "msg"
    ] | None: ...

global___RoomReq = RoomReq

@typing_extensions.final
class RoomResp(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    JOIN_FIELD_NUMBER: builtins.int
    LEAVE_FIELD_NUMBER: builtins.int
    ONLINE_FIELD_NUMBER: builtins.int
    MSG_FIELD_NUMBER: builtins.int
    ERR_FIELD_NUMBER: builtins.int
    id: builtins.str
    """{type}://{room_id}"""
    @property
    def join(self) -> global___RoomJoinEvent:
        """"""
    @property
    def leave(self) -> global___RoomLeaveEvent:
        """"""
    @property
    def online(self) -> global___RoomOnlineEvent:
        """"""
    @property
    def msg(self) -> global___RoomMessageEvent:
        """"""
    @property
    def err(self) -> global___RoomErrorEvent:
        """"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        join: global___RoomJoinEvent | None = ...,
        leave: global___RoomLeaveEvent | None = ...,
        online: global___RoomOnlineEvent | None = ...,
        msg: global___RoomMessageEvent | None = ...,
        err: global___RoomErrorEvent | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "err",
            b"err",
            "event",
            b"event",
            "join",
            b"join",
            "leave",
            b"leave",
            "msg",
            b"msg",
            "online",
            b"online",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "err",
            b"err",
            "event",
            b"event",
            "id",
            b"id",
            "join",
            b"join",
            "leave",
            b"leave",
            "msg",
            b"msg",
            "online",
            b"online",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["event", b"event"]
    ) -> typing_extensions.Literal[
        "join", "leave", "online", "msg", "err"
    ] | None: ...

global___RoomResp = RoomResp
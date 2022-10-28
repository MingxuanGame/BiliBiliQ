"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilibili.app.archive.middleware.v1.preload_pb2
import bilibili.app.archive.v1.archive_pb2
import bilibili.app.dynamic.v2.dynamic_pb2
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

class _From:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FromEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _From.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ArchiveTab: _From.ValueType  # 0
    """"""
    DynamicTab: _From.ValueType  # 1
    """"""

class From(_From, metaclass=_FromEnumTypeWrapper): ...

ArchiveTab: From.ValueType  # 0
""""""
DynamicTab: From.ValueType  # 1
""""""
global___From = From

@typing_extensions.final
class Arc(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ARCHIVE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    @property
    def archive(self) -> bilibili.app.archive.v1.archive_pb2.Arc:
        """"""
    uri: builtins.str
    """"""
    def __init__(
        self,
        *,
        archive: bilibili.app.archive.v1.archive_pb2.Arc | None = ...,
        uri: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["archive", b"archive"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "archive", b"archive", "uri", b"uri"
        ],
    ) -> None: ...

global___Arc = Arc

@typing_extensions.final
class Dynamic(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DYNAMIC_FIELD_NUMBER: builtins.int
    @property
    def dynamic(self) -> bilibili.app.dynamic.v2.dynamic_pb2.DynamicItem:
        """"""
    def __init__(
        self,
        *,
        dynamic: bilibili.app.dynamic.v2.dynamic_pb2.DynamicItem | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["dynamic", b"dynamic"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["dynamic", b"dynamic"]
    ) -> None: ...

global___Dynamic = Dynamic

@typing_extensions.final
class SearchTabReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOCUS_FIELD_NUMBER: builtins.int
    TABS_FIELD_NUMBER: builtins.int
    focus: builtins.int
    """"""
    @property
    def tabs(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Tab
    ]:
        """"""
    def __init__(
        self,
        *,
        focus: builtins.int = ...,
        tabs: collections.abc.Iterable[global___Tab] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "focus", b"focus", "tabs", b"tabs"
        ],
    ) -> None: ...

global___SearchTabReply = SearchTabReply

@typing_extensions.final
class SearchTabReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEYWORD_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    FROM_FIELD_NUMBER: builtins.int
    keyword: builtins.str
    """"""
    mid: builtins.int
    """"""
    def __init__(
        self,
        *,
        keyword: builtins.str = ...,
        mid: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "from", b"from", "keyword", b"keyword", "mid", b"mid"
        ],
    ) -> None: ...

global___SearchTabReq = SearchTabReq

@typing_extensions.final
class SearchArchiveReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ARCHIVES_FIELD_NUMBER: builtins.int
    TOTAL_FIELD_NUMBER: builtins.int
    @property
    def archives(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Arc
    ]:
        """"""
    total: builtins.int
    """"""
    def __init__(
        self,
        *,
        archives: collections.abc.Iterable[global___Arc] | None = ...,
        total: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "archives", b"archives", "total", b"total"
        ],
    ) -> None: ...

global___SearchArchiveReply = SearchArchiveReply

@typing_extensions.final
class SearchArchiveReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEYWORD_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    PN_FIELD_NUMBER: builtins.int
    PS_FIELD_NUMBER: builtins.int
    PLAYER_ARGS_FIELD_NUMBER: builtins.int
    keyword: builtins.str
    """"""
    mid: builtins.int
    """"""
    pn: builtins.int
    """"""
    ps: builtins.int
    """"""
    @property
    def player_args(
        self,
    ) -> bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs:
        """"""
    def __init__(
        self,
        *,
        keyword: builtins.str = ...,
        mid: builtins.int = ...,
        pn: builtins.int = ...,
        ps: builtins.int = ...,
        player_args: bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs
        | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal["player_args", b"player_args"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "keyword",
            b"keyword",
            "mid",
            b"mid",
            "player_args",
            b"player_args",
            "pn",
            b"pn",
            "ps",
            b"ps",
        ],
    ) -> None: ...

global___SearchArchiveReq = SearchArchiveReq

@typing_extensions.final
class SearchDynamicReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DYNAMICS_FIELD_NUMBER: builtins.int
    TOTAL_FIELD_NUMBER: builtins.int
    @property
    def dynamics(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Dynamic
    ]:
        """"""
    total: builtins.int
    """"""
    def __init__(
        self,
        *,
        dynamics: collections.abc.Iterable[global___Dynamic] | None = ...,
        total: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "dynamics", b"dynamics", "total", b"total"
        ],
    ) -> None: ...

global___SearchDynamicReply = SearchDynamicReply

@typing_extensions.final
class SearchDynamicReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEYWORD_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    PN_FIELD_NUMBER: builtins.int
    PS_FIELD_NUMBER: builtins.int
    PLAYER_ARGS_FIELD_NUMBER: builtins.int
    keyword: builtins.str
    """"""
    mid: builtins.int
    """"""
    pn: builtins.int
    """"""
    ps: builtins.int
    """"""
    @property
    def player_args(
        self,
    ) -> bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs:
        """"""
    def __init__(
        self,
        *,
        keyword: builtins.str = ...,
        mid: builtins.int = ...,
        pn: builtins.int = ...,
        ps: builtins.int = ...,
        player_args: bilibili.app.archive.middleware.v1.preload_pb2.PlayerArgs
        | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal["player_args", b"player_args"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "keyword",
            b"keyword",
            "mid",
            b"mid",
            "player_args",
            b"player_args",
            "pn",
            b"pn",
            "ps",
            b"ps",
        ],
    ) -> None: ...

global___SearchDynamicReq = SearchDynamicReq

@typing_extensions.final
class Tab(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    title: builtins.str
    """"""
    uri: builtins.str
    """"""
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        uri: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "title", b"title", "uri", b"uri"
        ],
    ) -> None: ...

global___Tab = Tab
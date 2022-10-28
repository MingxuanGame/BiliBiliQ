"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class RegionConfig(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCENES_NAME_FIELD_NUMBER: builtins.int
    SCENES_TYPE_FIELD_NUMBER: builtins.int
    scenes_name: builtins.str
    """"""
    scenes_type: builtins.str
    """"""
    def __init__(
        self,
        *,
        scenes_name: builtins.str = ...,
        scenes_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "scenes_name", b"scenes_name", "scenes_type", b"scenes_type"
        ],
    ) -> None: ...

global___RegionConfig = RegionConfig

@typing_extensions.final
class RegionInfo(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TID_FIELD_NUMBER: builtins.int
    REID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    LOGO_FIELD_NUMBER: builtins.int
    GOTO_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    IS_BANGUMI_FIELD_NUMBER: builtins.int
    CHILDREN_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    tid: builtins.int
    """"""
    reid: builtins.int
    """"""
    name: builtins.str
    """"""
    logo: builtins.str
    """"""
    goto: builtins.str
    """"""
    param: builtins.str
    """"""
    uri: builtins.str
    """"""
    type: builtins.int
    """"""
    is_bangumi: builtins.int
    """"""
    @property
    def children(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___RegionInfo
    ]:
        """"""
    @property
    def config(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___RegionConfig
    ]:
        """"""
    def __init__(
        self,
        *,
        tid: builtins.int = ...,
        reid: builtins.int = ...,
        name: builtins.str = ...,
        logo: builtins.str = ...,
        goto: builtins.str = ...,
        param: builtins.str = ...,
        uri: builtins.str = ...,
        type: builtins.int = ...,
        is_bangumi: builtins.int = ...,
        children: collections.abc.Iterable[global___RegionInfo] | None = ...,
        config: collections.abc.Iterable[global___RegionConfig] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "children",
            b"children",
            "config",
            b"config",
            "goto",
            b"goto",
            "is_bangumi",
            b"is_bangumi",
            "logo",
            b"logo",
            "name",
            b"name",
            "param",
            b"param",
            "reid",
            b"reid",
            "tid",
            b"tid",
            "type",
            b"type",
            "uri",
            b"uri",
        ],
    ) -> None: ...

global___RegionInfo = RegionInfo

@typing_extensions.final
class RegionReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGIONS_FIELD_NUMBER: builtins.int
    @property
    def regions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___RegionInfo
    ]:
        """"""
    def __init__(
        self,
        *,
        regions: collections.abc.Iterable[global___RegionInfo] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["regions", b"regions"]
    ) -> None: ...

global___RegionReply = RegionReply

@typing_extensions.final
class RegionReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LANG_FIELD_NUMBER: builtins.int
    lang: builtins.str
    """"""
    def __init__(
        self,
        *,
        lang: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["lang", b"lang"]
    ) -> None: ...

global___RegionReq = RegionReq
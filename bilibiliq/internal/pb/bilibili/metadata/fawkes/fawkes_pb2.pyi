"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class FawkesReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIG_FIELD_NUMBER: builtins.int
    FF_FIELD_NUMBER: builtins.int
    config: builtins.str
    """客户端在fawkes系统中对应的已发布最新的config版本号"""
    ff: builtins.str
    """客户端在fawkes系统中对应的已发布最新的ff版本号"""
    def __init__(
        self,
        *,
        config: builtins.str = ...,
        ff: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "config", b"config", "ff", b"ff"
        ],
    ) -> None: ...

global___FawkesReply = FawkesReply

@typing_extensions.final
class FawkesReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    APPKEY_FIELD_NUMBER: builtins.int
    ENV_FIELD_NUMBER: builtins.int
    SESSION_ID_FIELD_NUMBER: builtins.int
    appkey: builtins.str
    """客户端在fawkes系统的唯一名"""
    env: builtins.str
    """客户端在fawkes系统中的环境参数"""
    session_id: builtins.str
    """启动id"""
    def __init__(
        self,
        *,
        appkey: builtins.str = ...,
        env: builtins.str = ...,
        session_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "appkey", b"appkey", "env", b"env", "session_id", b"session_id"
        ],
    ) -> None: ...

global___FawkesReq = FawkesReq

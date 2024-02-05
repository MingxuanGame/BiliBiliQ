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
class PlayerArgs(google.protobuf.message.Message):
    """视频秒开参数"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QN_FIELD_NUMBER: builtins.int
    FNVER_FIELD_NUMBER: builtins.int
    FNVAL_FIELD_NUMBER: builtins.int
    FORCE_HOST_FIELD_NUMBER: builtins.int
    VOICE_BALANCE_FIELD_NUMBER: builtins.int
    qn: builtins.int
    """清晰度"""
    fnver: builtins.int
    """流版本"""
    fnval: builtins.int
    """流类型"""
    force_host: builtins.int
    """返回url是否强制使用域名
    0:不强制使用域名 1:http域名 2:https域名
    """
    voice_balance: builtins.int
    """"""
    def __init__(
        self,
        *,
        qn: builtins.int = ...,
        fnver: builtins.int = ...,
        fnval: builtins.int = ...,
        force_host: builtins.int = ...,
        voice_balance: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "fnval",
            b"fnval",
            "fnver",
            b"fnver",
            "force_host",
            b"force_host",
            "qn",
            b"qn",
            "voice_balance",
            b"voice_balance",
        ],
    ) -> None: ...

global___PlayerArgs = PlayerArgs

"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _NetworkType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _NetworkTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _NetworkType.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NT_UNKNOWN: _NetworkType.ValueType  # 0
    """未知"""
    WIFI: _NetworkType.ValueType  # 1
    """WIFI"""
    CELLULAR: _NetworkType.ValueType  # 2
    """蜂窝网络"""
    OFFLINE: _NetworkType.ValueType  # 3
    """未连接"""
    OTHERNET: _NetworkType.ValueType  # 4
    """其他网络"""
    ETHERNET: _NetworkType.ValueType  # 5
    """以太网"""

class NetworkType(_NetworkType, metaclass=_NetworkTypeEnumTypeWrapper):
    """网络类型"""

NT_UNKNOWN: NetworkType.ValueType  # 0
"""未知"""
WIFI: NetworkType.ValueType  # 1
"""WIFI"""
CELLULAR: NetworkType.ValueType  # 2
"""蜂窝网络"""
OFFLINE: NetworkType.ValueType  # 3
"""未连接"""
OTHERNET: NetworkType.ValueType  # 4
"""其他网络"""
ETHERNET: NetworkType.ValueType  # 5
"""以太网"""
global___NetworkType = NetworkType

class _TFType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _TFTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _TFType.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TF_UNKNOWN: _TFType.ValueType  # 0
    """正常计费"""
    U_CARD: _TFType.ValueType  # 1
    """联通卡"""
    U_PKG: _TFType.ValueType  # 2
    """联通包"""
    C_CARD: _TFType.ValueType  # 3
    """移动卡"""
    C_PKG: _TFType.ValueType  # 4
    """移动包"""
    T_CARD: _TFType.ValueType  # 5
    """电信卡"""
    T_PKG: _TFType.ValueType  # 6
    """电信包"""

class TFType(_TFType, metaclass=_TFTypeEnumTypeWrapper):
    """免流类型"""

TF_UNKNOWN: TFType.ValueType  # 0
"""正常计费"""
U_CARD: TFType.ValueType  # 1
"""联通卡"""
U_PKG: TFType.ValueType  # 2
"""联通包"""
C_CARD: TFType.ValueType  # 3
"""移动卡"""
C_PKG: TFType.ValueType  # 4
"""移动包"""
T_CARD: TFType.ValueType  # 5
"""电信卡"""
T_PKG: TFType.ValueType  # 6
"""电信包"""
global___TFType = TFType

@typing_extensions.final
class Network(google.protobuf.message.Message):
    """网络类型标识
    gRPC头部:x-bili-network-bin
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    TF_FIELD_NUMBER: builtins.int
    OID_FIELD_NUMBER: builtins.int
    type: global___NetworkType.ValueType
    """网络类型"""
    tf: global___TFType.ValueType
    """免流类型"""
    oid: builtins.str
    """运营商"""
    def __init__(
        self,
        *,
        type: global___NetworkType.ValueType = ...,
        tf: global___TFType.ValueType = ...,
        oid: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "oid", b"oid", "tf", b"tf", "type", b"type"
        ],
    ) -> None: ...

global___Network = Network

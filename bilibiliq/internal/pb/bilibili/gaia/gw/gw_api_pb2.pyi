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

class _EncryptType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EncryptTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _EncryptType.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    INVALID_ENCRYPT_TYPE: _EncryptType.ValueType  # 0
    """非法值"""
    CLIENT_AES: _EncryptType.ValueType  # 1
    """同客户端人工约定AES加密私钥，存储在客户端"""
    SERVER_RSA_AES: _EncryptType.ValueType  # 2
    """客户端随机生成一个用于AES加密的私钥，并用服务端下发的RSA公钥来加密"""

class EncryptType(_EncryptType, metaclass=_EncryptTypeEnumTypeWrapper):
    """加密方式"""

INVALID_ENCRYPT_TYPE: EncryptType.ValueType  # 0
"""非法值"""
CLIENT_AES: EncryptType.ValueType  # 1
"""同客户端人工约定AES加密私钥，存储在客户端"""
SERVER_RSA_AES: EncryptType.ValueType  # 2
"""客户端随机生成一个用于AES加密的私钥，并用服务端下发的RSA公钥来加密"""
global___EncryptType = EncryptType

class _PayloadType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PayloadTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _PayloadType.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    INVALID_PAYLOAD: _PayloadType.ValueType  # 0
    """非法值"""
    DEVICE_APP_LIST: _PayloadType.ValueType  # 1
    """设备app列表，对应DeviceAppList"""

class PayloadType(_PayloadType, metaclass=_PayloadTypeEnumTypeWrapper):
    """负载类型"""

INVALID_PAYLOAD: PayloadType.ValueType  # 0
"""非法值"""
DEVICE_APP_LIST: PayloadType.ValueType  # 1
"""设备app列表，对应DeviceAppList"""
global___PayloadType = PayloadType

@typing_extensions.final
class DeviceAppList(google.protobuf.message.Message):
    """待加密的pb对象"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_FIELD_NUMBER: builtins.int
    SYSTEM_APP_LIST_FIELD_NUMBER: builtins.int
    USER_APP_LIST_FIELD_NUMBER: builtins.int
    source: builtins.str
    """上报类型
    first_installation:首次安装上报 first_open:每日启动上报
    """
    @property
    def system_app_list(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.str
    ]:
        """安装的系统程序列表"""
    @property
    def user_app_list(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.str
    ]:
        """安装的用户程序列表"""
    def __init__(
        self,
        *,
        source: builtins.str = ...,
        system_app_list: collections.abc.Iterable[builtins.str] | None = ...,
        user_app_list: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "source",
            b"source",
            "system_app_list",
            b"system_app_list",
            "user_app_list",
            b"user_app_list",
        ],
    ) -> None: ...

global___DeviceAppList = DeviceAppList

@typing_extensions.final
class FetchPublicKeyReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    PUBLIC_KEY_FIELD_NUMBER: builtins.int
    DEADLINE_FIELD_NUMBER: builtins.int
    version: builtins.str
    """版本号"""
    public_key: builtins.str
    """RSA公钥"""
    deadline: builtins.int
    """公钥过期时间"""
    def __init__(
        self,
        *,
        version: builtins.str = ...,
        public_key: builtins.str = ...,
        deadline: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "deadline",
            b"deadline",
            "public_key",
            b"public_key",
            "version",
            b"version",
        ],
    ) -> None: ...

global___FetchPublicKeyReply = FetchPublicKeyReply

@typing_extensions.final
class GaiaDeviceBasicInfo(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLATFORM_FIELD_NUMBER: builtins.int
    DEVICE_FIELD_NUMBER: builtins.int
    MOBI_APP_FIELD_NUMBER: builtins.int
    ORIGIN_FIELD_NUMBER: builtins.int
    APP_ID_FIELD_NUMBER: builtins.int
    SDKVER_FIELD_NUMBER: builtins.int
    APP_VERSION_FIELD_NUMBER: builtins.int
    APP_VERSION_CODE_FIELD_NUMBER: builtins.int
    BUILD_FIELD_NUMBER: builtins.int
    CHANNEL_FIELD_NUMBER: builtins.int
    BRAND_FIELD_NUMBER: builtins.int
    MODEL_FIELD_NUMBER: builtins.int
    OSVER_FIELD_NUMBER: builtins.int
    USER_AGENT_FIELD_NUMBER: builtins.int
    BUVID_LOCAL_FIELD_NUMBER: builtins.int
    BUVID_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    FTS_FIELD_NUMBER: builtins.int
    FIRST_FIELD_NUMBER: builtins.int
    NETWORK_FIELD_NUMBER: builtins.int
    platform: builtins.str
    """平台&应用信息
    android/ios/web/h5;
    """
    device: builtins.str
    """运行设备, 用于区分不同的app, 见客户端传入的对应参数。对于苹果系统，device有效值为phone, pad；安卓无法区分phone和pad，留空即可。"""
    mobi_app: builtins.str
    """包类型，用于区分不同的app, 见客户端传入的对应参数（mobi_app ）；对于web端请求，请传空"""
    origin: builtins.str
    """客户端appkey, 用以区分不同的客户端，对应客户端请求参数中的appkey,如果无法获取可传空“”"""
    app_id: builtins.str
    """app产品编号 //产品编号，由数据平台分配，粉=1，白=2，蓝=3，直播姬=4，HD=5，海外=6，OTT=7，漫画=8，TV野版=9，小视频=10，网易漫画=11，网易漫画lite=12，网易漫画HD=13,国际版=14"""
    sdkver: builtins.str
    """应用的版本信息
    SDK版本号   "sdkver": "2.6.6"
    """
    app_version: builtins.str
    """app版本  "app_version":"5.36.0" """
    app_version_code: builtins.str
    """app版本号 "app_version_code":"5360000" """
    build: builtins.str
    """app版本号，见客户端传入的对应参数；对于web端请求，请传空"""
    channel: builtins.str
    """渠道信息
    渠道标识，见客户端传入的对应参数；对于web端请求，请传空；对应chid
    """
    brand: builtins.str
    """机器硬件信息
    手机品牌，见客户端传入的对应参数；
    """
    model: builtins.str
    """手机型号，见客户端传入的对应参数"""
    osver: builtins.str
    """系统版本，见客户端传入的对应参数"""
    user_agent: builtins.str
    buvid_local: builtins.str
    """设备标识信息
    本地设备唯一标识
    """
    buvid: builtins.str
    """设备唯一标识"""
    mid: builtins.str
    """登陆用户信息
    最后一次登陆用户的mid，如果无登陆信息，传0即可
    """
    fts: builtins.int
    """本次启动信息
    app首次启动时间 "fts":1530447775661
    """
    first: builtins.int
    """是否首次启动 是：0 否：1"""
    network: builtins.str
    """网络相关的信息
    网络连接方式, WIFI/CELLULAR/OFFLINE/OTHERNET/ETHERNET "network":"WIFI", ESS_NETWORK_STATE、ACCESS_WIFI_STATE
    """
    def __init__(
        self,
        *,
        platform: builtins.str = ...,
        device: builtins.str = ...,
        mobi_app: builtins.str = ...,
        origin: builtins.str = ...,
        app_id: builtins.str = ...,
        sdkver: builtins.str = ...,
        app_version: builtins.str = ...,
        app_version_code: builtins.str = ...,
        build: builtins.str = ...,
        channel: builtins.str = ...,
        brand: builtins.str = ...,
        model: builtins.str = ...,
        osver: builtins.str = ...,
        user_agent: builtins.str = ...,
        buvid_local: builtins.str = ...,
        buvid: builtins.str = ...,
        mid: builtins.str = ...,
        fts: builtins.int = ...,
        first: builtins.int = ...,
        network: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "app_id",
            b"app_id",
            "app_version",
            b"app_version",
            "app_version_code",
            b"app_version_code",
            "brand",
            b"brand",
            "build",
            b"build",
            "buvid",
            b"buvid",
            "buvid_local",
            b"buvid_local",
            "channel",
            b"channel",
            "device",
            b"device",
            "first",
            b"first",
            "fts",
            b"fts",
            "mid",
            b"mid",
            "mobi_app",
            b"mobi_app",
            "model",
            b"model",
            "network",
            b"network",
            "origin",
            b"origin",
            "osver",
            b"osver",
            "platform",
            b"platform",
            "sdkver",
            b"sdkver",
            "user_agent",
            b"user_agent",
        ],
    ) -> None: ...

global___GaiaDeviceBasicInfo = GaiaDeviceBasicInfo

@typing_extensions.final
class GaiaEncryptMsgReq(google.protobuf.message.Message):
    """应用列表上报-请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEADER_FIELD_NUMBER: builtins.int
    ENCRYPT_PAYLOAD_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> global___GaiaMsgHeader:
        """上报头部"""
    encrypt_payload: builtins.bytes
    """加密数据"""
    def __init__(
        self,
        *,
        header: global___GaiaMsgHeader | None = ...,
        encrypt_payload: builtins.bytes = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["header", b"header"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "encrypt_payload", b"encrypt_payload", "header", b"header"
        ],
    ) -> None: ...

global___GaiaEncryptMsgReq = GaiaEncryptMsgReq

@typing_extensions.final
class GaiaMsgHeader(google.protobuf.message.Message):
    """风控通用消息头"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENCODE_TYPE_FIELD_NUMBER: builtins.int
    PAYLOAD_TYPE_FIELD_NUMBER: builtins.int
    ENCODED_AES_KEY_FIELD_NUMBER: builtins.int
    TS_FIELD_NUMBER: builtins.int
    encode_type: global___EncryptType.ValueType
    """加密类型"""
    payload_type: global___PayloadType.ValueType
    """类型"""
    encoded_aes_key: builtins.bytes
    """RAS加密后的aes_key"""
    ts: builtins.int
    """当前时间戳(ms)"""
    def __init__(
        self,
        *,
        encode_type: global___EncryptType.ValueType = ...,
        payload_type: global___PayloadType.ValueType = ...,
        encoded_aes_key: builtins.bytes = ...,
        ts: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "encode_type",
            b"encode_type",
            "encoded_aes_key",
            b"encoded_aes_key",
            "payload_type",
            b"payload_type",
            "ts",
            b"ts",
        ],
    ) -> None: ...

global___GaiaMsgHeader = GaiaMsgHeader

@typing_extensions.final
class UploadAppListReply(google.protobuf.message.Message):
    """应用列表上报-响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRACE_ID_FIELD_NUMBER: builtins.int
    trace_id: builtins.str
    """上报响应id"""
    def __init__(
        self,
        *,
        trace_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["trace_id", b"trace_id"]
    ) -> None: ...

global___UploadAppListReply = UploadAppListReply
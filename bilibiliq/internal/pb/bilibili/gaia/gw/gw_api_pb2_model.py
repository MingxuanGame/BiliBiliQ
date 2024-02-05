"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""

import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class EncryptType(str, Enum):
    """加密方式"""

    INVALID_ENCRYPT_TYPE = 'INVALID_ENCRYPT_TYPE'
    """非法值"""
    CLIENT_AES = 'CLIENT_AES'
    """同客户端人工约定AES加密私钥，存储在客户端"""
    SERVER_RSA_AES = 'SERVER_RSA_AES'
    """客户端随机生成一个用于AES加密的私钥，并用服务端下发的RSA公钥来加密"""


class PayloadType(str, Enum):
    """负载类型"""

    INVALID_PAYLOAD = 'INVALID_PAYLOAD'
    """非法值"""
    DEVICE_APP_LIST = 'DEVICE_APP_LIST'
    """设备app列表，对应DeviceAppList"""


class DeviceAppList(BaseModel):
    """待加密的pb对象"""

    source: builtins.str
    """上报类型
    first_installation:首次安装上报 first_open:每日启动上报
    """
    system_app_list: List[builtins.str]
    """安装的系统程序列表"""
    user_app_list: List[builtins.str]
    """安装的用户程序列表"""


class FetchPublicKeyReply(BaseModel):
    """"""

    version: builtins.str
    """版本号"""
    public_key: builtins.str
    """RSA公钥"""
    deadline: builtins.int
    """公钥过期时间"""


class GaiaDeviceBasicInfo(BaseModel):
    """"""

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


class GaiaEncryptMsgReq(BaseModel):
    """应用列表上报-请求"""

    header: Optional["GaiaMsgHeader"] = None
    """上报头部"""
    encrypt_payload: builtins.bytes
    """加密数据"""


class GaiaMsgHeader(BaseModel):
    """风控通用消息头"""

    encode_type: EncryptType
    """加密类型"""
    payload_type: PayloadType
    """类型"""
    encoded_aes_key: builtins.bytes
    """RAS加密后的aes_key"""
    ts: builtins.int
    """当前时间戳(ms)"""


class UploadAppListReply(BaseModel):
    """应用列表上报-响应"""

    trace_id: builtins.str
    """上报响应id"""


GaiaMsgHeader.update_forward_refs()
GaiaDeviceBasicInfo.update_forward_refs()
UploadAppListReply.update_forward_refs()
FetchPublicKeyReply.update_forward_refs()
DeviceAppList.update_forward_refs()
GaiaEncryptMsgReq.update_forward_refs()

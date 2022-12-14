"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class AntiHarassmentLimit(str, Enum):
    """"""

    DefaultLimit = 'DefaultLimit'
    """"""
    FollowLimit = 'FollowLimit'
    """"""
    ReFollowLimit = 'ReFollowLimit'
    """"""
    TwoWayFollow = 'TwoWayFollow'
    """"""
    AllLimit = 'AllLimit'
    """"""


class BizType(str, Enum):
    """"""

    InvalidBizType = 'InvalidBizType'
    """"""
    Im = 'Im'
    """"""
    Dm = 'Dm'
    """"""
    Reply = 'Reply'
    """"""
    ReplyMe = 'ReplyMe'
    """"""
    LikeMe = 'LikeMe'
    """"""
    AtMe = 'AtMe'
    """"""


class AntiHarassmentInfo(BaseModel):
    """"""

    limit: builtins.int
    """"""
    follow_time_limit_second: builtins.int
    """"""
    expire_time: builtins.int
    """"""


class AntiHarassmentSetting(BaseModel):
    """"""

    mid: builtins.int
    """"""
    auto_limit: builtins.bool
    """"""
    im: Optional["AntiHarassmentInfo"] = None
    """"""
    reply: Optional["AntiHarassmentInfo"] = None
    """"""
    dm: Optional["AntiHarassmentInfo"] = None
    """"""
    reply_me: Optional["AntiHarassmentInfo"] = None
    """"""
    like_me: Optional["AntiHarassmentInfo"] = None
    """"""
    at_me: Optional["AntiHarassmentInfo"] = None
    """"""
    auto_limit_expire_time: builtins.int
    """"""


class LoadAntiHarassmentSettingsReq(BaseModel):
    """"""

    biz_type: builtins.int
    """"""
    recv_mid: builtins.int
    """"""
    send_mid: builtins.int
    """"""


class LoadAntiHarassmentSettingsRsp(BaseModel):
    """"""

    anti_harassment_ret: builtins.bool
    """"""
    anti_harassment_setting: Optional["AntiHarassmentSetting"] = None
    """"""
    show_window: builtins.int
    """"""


class StoreAntiHarassmentSettingsReq(BaseModel):
    """"""

    biz_type: builtins.int
    """"""
    mid: builtins.int
    """"""
    anti_harassment_setting: Optional["AntiHarassmentSetting"] = None
    """"""


class StoreAntiHarassmentSettingsRsp(BaseModel):
    """"""


AntiHarassmentSetting.update_forward_refs()
StoreAntiHarassmentSettingsReq.update_forward_refs()
StoreAntiHarassmentSettingsRsp.update_forward_refs()
LoadAntiHarassmentSettingsRsp.update_forward_refs()
LoadAntiHarassmentSettingsReq.update_forward_refs()
AntiHarassmentInfo.update_forward_refs()

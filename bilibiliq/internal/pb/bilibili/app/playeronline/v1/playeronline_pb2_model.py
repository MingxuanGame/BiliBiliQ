"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class NoReply(BaseModel):
    """空回复"""


class PlayerOnlineReply(BaseModel):
    """获取在线人数-回复"""

    total_text: builtins.str
    """"""
    sec_next: builtins.int
    """下次轮询间隔时间"""
    bottom_show: builtins.bool
    """是否底部显示"""
    sdm_show: builtins.bool
    """"""
    sdm_text: builtins.str
    """"""
    total_number: builtins.int
    """"""
    total_number_text: builtins.str
    """"""


class PlayerOnlineReq(BaseModel):
    """获取在线人数-请求"""

    aid: builtins.int
    """稿件 avid"""
    cid: builtins.int
    """视频 cid"""
    play_open: builtins.bool
    """是否在播放中"""


class PremiereInfoReply(BaseModel):
    """"""

    premiere_over_text: builtins.str
    """"""
    participant: builtins.int
    """"""
    interaction: builtins.int
    """"""


class PremiereInfoReq(BaseModel):
    """"""

    aid: builtins.int
    """"""


class ReportWatchReq(BaseModel):
    """"""

    aid: builtins.int
    """"""
    biz: builtins.str
    """"""
    buvid: builtins.str
    """"""


PremiereInfoReq.update_forward_refs()
PremiereInfoReply.update_forward_refs()
PlayerOnlineReply.update_forward_refs()
ReportWatchReq.update_forward_refs()
PlayerOnlineReq.update_forward_refs()
NoReply.update_forward_refs()

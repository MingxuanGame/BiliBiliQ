"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class LiveStartEvent(BaseModel):
    """开播事件"""


class LiveEndEvent(BaseModel):
    """直播中止事件"""


class LiveOnlineEvent(BaseModel):
    """在线人数事件"""

    online: builtins.int
    """在线人数"""


class LiveUpdateEvent(BaseModel):
    """变更通知"""

    after_premiere_type: builtins.int
    """直播后状态
    1:下线 2:转点播
    """
    start_time: builtins.int
    """直播开始绝对时间 单位ms"""
    id: builtins.str
    """id"""
    progress: builtins.int
    """服务端播放进度，未打散，负数表示距离开播时间，正数表示已开播时间，单位：毫秒
    用户实际播放进度：progress - delay_time
    """


class CMDBody(BaseModel):
    """直播间事件"""

    start: Optional["LiveStartEvent"] = None
    """开播事件"""
    emergency: Optional["LiveEndEvent"] = None
    """直播中止事件"""
    online: Optional["LiveOnlineEvent"] = None
    """在线人数事件"""
    update: Optional["LiveUpdateEvent"] = None
    """变更通知"""


LiveOnlineEvent.update_forward_refs()
CMDBody.update_forward_refs()
LiveUpdateEvent.update_forward_refs()
LiveEndEvent.update_forward_refs()
LiveStartEvent.update_forward_refs()

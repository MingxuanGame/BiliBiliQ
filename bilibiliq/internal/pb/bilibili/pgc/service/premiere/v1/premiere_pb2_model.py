"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""

import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class PremiereStatusReq(BaseModel):
    """获取首播状态-请求"""

    ep_id: builtins.int
    """剧集epid"""


class PremiereStatusReply(BaseModel):
    """获取首播状态-响应"""

    progress: builtins.int
    """服务端播放进度 单位ms 用户实际播放进度：progress - delay_time"""
    start_time: builtins.int
    """起播时间戳 单位ms"""
    delay_time: builtins.int
    """延迟播放时长 单位ms"""
    online_count: builtins.int
    """首播在线人数"""
    status: builtins.int
    """首播状态
    1:预热 2:首播中 3:紧急停播 4:已结束
    """
    after_premiere_type: builtins.int
    """首播结束后跳转类型
    1:下架 2:转点播
    """


PremiereStatusReply.update_forward_refs()
PremiereStatusReq.update_forward_refs()

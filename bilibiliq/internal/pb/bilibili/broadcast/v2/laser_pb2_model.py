"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class LaserEventResp(BaseModel):
    """服务端下发Laser事件"""

    taskid: builtins.int
    """任务id"""
    action: builtins.str
    """指令名"""
    params: builtins.str
    """指令参数json字符串"""


LaserEventResp.update_forward_refs()
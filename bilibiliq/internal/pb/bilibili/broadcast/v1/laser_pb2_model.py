"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""

import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class LaserLogUploadResp(BaseModel):
    """服务端下发日志上报事件"""

    taskid: builtins.int
    """任务id"""
    date: builtins.str
    """下发时间"""


LaserLogUploadResp.update_forward_refs()

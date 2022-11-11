"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class RoomStatus(str, Enum):
    """"""

    Pause = 'Pause'
    """暂停:"""
    Play = 'Play'
    """播放:"""
    End = 'End'
    """终止:"""


class RoomEvent(BaseModel):
    """推送选项"""

    room_status: RoomStatus
    """RoomStatus 类型"""
    room_message: builtins.str
    """"""


RoomEvent.update_forward_refs()

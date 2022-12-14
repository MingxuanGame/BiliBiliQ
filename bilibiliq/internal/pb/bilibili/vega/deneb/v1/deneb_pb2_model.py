"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class MessagePullsReply(BaseModel):
    """"""

    data: Any
    """"""
    pn: builtins.int
    """"""
    ps: builtins.int
    """"""
    count: builtins.int
    """"""
    has_next: builtins.bool
    """"""


class MessagePullsReq(BaseModel):
    """"""

    start_seq_id: builtins.int
    """"""
    end_seq_id: builtins.int
    """"""
    pn: builtins.int
    """"""
    ps: builtins.int
    """"""


MessagePullsReply.update_forward_refs()
MessagePullsReq.update_forward_refs()

"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""

import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class Category(str, Enum):
    """"""

    CATEGORY_UNSPECIFIED = 'CATEGORY_UNSPECIFIED'
    """"""
    CATEGORY_ONE = 'CATEGORY_ONE'
    """"""
    CATEGORY_TWO = 'CATEGORY_TWO'
    """"""
    CATEGORY_THREE = 'CATEGORY_THREE'
    """"""


class ErrorReason(str, Enum):
    """"""

    PROBE_UNSPECIFIED = 'PROBE_UNSPECIFIED'
    """"""
    PROBE_CATEGORY_NOTFOUND = 'PROBE_CATEGORY_NOTFOUND'
    """"""


class CodeReply(BaseModel):
    """"""


class CodeReq(BaseModel):
    """"""

    code: builtins.int
    """"""


class DynamicMessageUpdate(BaseModel):
    """"""

    body: Optional["SimpleMessage"] = None
    """"""


class Embedded(BaseModel):
    """"""

    bool_val: builtins.bool
    """"""
    int32_val: builtins.int
    """"""
    int64_val: builtins.int
    """"""
    float_val: builtins.float
    """"""
    double_val: builtins.float
    """"""
    string_val: builtins.str
    """"""
    repeated_int32_val: List[builtins.int]
    """"""
    repeated_string_val: List[builtins.str]
    """"""
    map_string_val: Dict[builtins.str, builtins.str]
    """"""
    map_error_val: Dict[builtins.str, Optional["ErrorMessage"]]
    """"""


class ErrorMessage(BaseModel):
    """"""

    code: builtins.int
    """"""
    reason: builtins.str
    """"""
    message: builtins.str
    """"""


class ProbeReply(BaseModel):
    """"""

    content: builtins.str
    """"""
    timestamp: builtins.int
    """"""


class ProbeReq(BaseModel):
    """"""

    mid: builtins.int
    """"""
    buvid: builtins.str
    """"""


class ProbeStreamReply(BaseModel):
    """"""

    sequence: builtins.int
    """"""
    timestamp: builtins.int
    """"""
    content: builtins.str
    """"""


class ProbeStreamReq(BaseModel):
    """"""

    mid: builtins.int
    """"""
    sequence: builtins.int
    """"""


class ProbeSubReply(BaseModel):
    """"""

    message_id: builtins.int
    """"""


class ProbeSubReq(BaseModel):
    """"""

    buvid: builtins.int
    """"""


class SimpleMessage(BaseModel):
    """"""

    id: builtins.int
    """"""
    num: builtins.int
    """"""
    lang: builtins.str
    """"""
    cate: builtins.int
    """"""
    embedded: Optional["Embedded"] = None
    """"""


ProbeSubReply.update_forward_refs()
DynamicMessageUpdate.update_forward_refs()
Embedded.update_forward_refs()
ProbeReq.update_forward_refs()
CodeReq.update_forward_refs()
ErrorMessage.update_forward_refs()
ProbeReply.update_forward_refs()
ProbeStreamReq.update_forward_refs()
CodeReply.update_forward_refs()
ProbeSubReq.update_forward_refs()
SimpleMessage.update_forward_refs()
ProbeStreamReply.update_forward_refs()

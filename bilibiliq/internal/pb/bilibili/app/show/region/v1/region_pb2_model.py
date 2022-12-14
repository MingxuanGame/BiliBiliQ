"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class RegionConfig(BaseModel):
    """"""

    scenes_name: builtins.str
    """"""
    scenes_type: builtins.str
    """"""


class RegionInfo(BaseModel):
    """"""

    tid: builtins.int
    """"""
    reid: builtins.int
    """"""
    name: builtins.str
    """"""
    logo: builtins.str
    """"""
    goto: builtins.str
    """"""
    param: builtins.str
    """"""
    uri: builtins.str
    """"""
    type: builtins.int
    """"""
    is_bangumi: builtins.int
    """"""
    children: "List[RegionInfo]"
    """"""
    config: "List[RegionConfig]"
    """"""


class RegionReply(BaseModel):
    """"""

    regions: "List[RegionInfo]"
    """"""


class RegionReq(BaseModel):
    """"""

    lang: builtins.str
    """"""


RegionConfig.update_forward_refs()
RegionReply.update_forward_refs()
RegionReq.update_forward_refs()
RegionInfo.update_forward_refs()

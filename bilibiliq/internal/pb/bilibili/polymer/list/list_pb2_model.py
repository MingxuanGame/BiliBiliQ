"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class CheckAccountReply(BaseModel):
    """"""

    is_new: builtins.bool
    """"""


class CheckAccountReq(BaseModel):
    """"""

    uid: builtins.int
    """"""
    periods: builtins.str
    """"""


class FavoriteTabItem(BaseModel):
    """"""

    name: builtins.str
    """"""
    uri: builtins.str
    """"""
    type: builtins.str
    """"""


class FavoriteTabReply(BaseModel):
    """"""

    items: "List[FavoriteTabItem]"
    """"""


class FavoriteTabReq(BaseModel):
    """"""


FavoriteTabReq.update_forward_refs()
FavoriteTabItem.update_forward_refs()
CheckAccountReply.update_forward_refs()
CheckAccountReq.update_forward_refs()
FavoriteTabReply.update_forward_refs()

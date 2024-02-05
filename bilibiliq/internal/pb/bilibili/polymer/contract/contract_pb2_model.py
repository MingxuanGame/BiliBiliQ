"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""

import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class AddContractReply(BaseModel):
    """"""

    allow_message: builtins.bool
    """"""
    allow_reply: builtins.bool
    """"""
    input_text: builtins.str
    """"""
    input_title: builtins.str
    """"""


class AddContractReq(BaseModel):
    """"""

    common: Optional["CommonReq"] = None
    """"""
    mid: builtins.int
    """"""
    up_mid: builtins.int
    """"""
    aid: builtins.int
    """"""
    source: builtins.int
    """"""


class CommonReq(BaseModel):
    """"""

    platform: builtins.str
    """"""
    build: builtins.int
    """"""
    buvid: builtins.str
    """"""
    mobi_app: builtins.str
    """"""
    device: builtins.str
    """"""
    ip: builtins.str
    """"""
    spmid: builtins.str
    """"""


class ContractCard(BaseModel):
    """"""

    title: builtins.str
    """"""
    sub_title: builtins.str
    """"""


class ContractConfigReply(BaseModel):
    """"""

    is_follow_display: builtins.int
    """"""
    is_triple_display: builtins.int
    """"""
    contract_card: Optional["ContractCard"] = None
    """"""


class ContractConfigReq(BaseModel):
    """"""

    common: Optional["CommonReq"] = None
    """"""
    mid: builtins.int
    """"""
    up_mid: builtins.int
    """"""
    aid: builtins.int
    """"""
    source: builtins.int
    """"""


AddContractReq.update_forward_refs()
CommonReq.update_forward_refs()
ContractConfigReq.update_forward_refs()
AddContractReply.update_forward_refs()
ContractConfigReply.update_forward_refs()
ContractCard.update_forward_refs()

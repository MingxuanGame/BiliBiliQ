"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class HelloWorldReq(BaseModel):
    """"""

    content: builtins.str
    """"""


class HelloWorldResp(BaseModel):
    """"""

    data: builtins.str
    """"""


HelloWorldResp.update_forward_refs()
HelloWorldReq.update_forward_refs()

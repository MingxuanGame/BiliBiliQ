"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
import bilibiliq.internal.pb.bilibili.rpc.status_pb2_model


class AuthReq(BaseModel):
    """"""


class AuthResp(BaseModel):
    """"""


class FrameOption(BaseModel):
    """"""

    vega_id: builtins.int
    """"""
    req_id: builtins.str
    """"""
    sequence: builtins.int
    """"""
    is_ack: builtins.bool
    """"""
    status: bilibiliq.internal.pb.bilibili.rpc.status_pb2_model.Status
    """"""
    ack_origin: builtins.str
    """"""
    mid: builtins.int
    """"""


class HeartbeatReq(BaseModel):
    """"""


class HeartbeatResp(BaseModel):
    """"""


class MessageAckReq(BaseModel):
    """"""

    vega_id: builtins.str
    """"""
    req_id: builtins.str
    """"""
    origin: builtins.str
    """"""
    target_path: builtins.str
    """"""


class SubscribeReq(BaseModel):
    """"""

    target_paths: "List[TargetPath]"
    """"""


class TargetPath(BaseModel):
    """"""

    key: builtins.str
    """"""
    subs: Any
    """"""


class VegaFrame(BaseModel):
    """"""

    options: Optional["FrameOption"] = None
    """"""
    route_path: builtins.str
    """"""
    body: Any
    """"""
    sub_biz: Any
    """"""


VegaFrame.update_forward_refs()
AuthResp.update_forward_refs()
AuthReq.update_forward_refs()
MessageAckReq.update_forward_refs()
SubscribeReq.update_forward_refs()
FrameOption.update_forward_refs()
HeartbeatResp.update_forward_refs()
TargetPath.update_forward_refs()
HeartbeatReq.update_forward_refs()

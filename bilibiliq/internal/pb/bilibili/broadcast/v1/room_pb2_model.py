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


class RoomErrorEvent(BaseModel):
    """"""

    status: bilibiliq.internal.pb.bilibili.rpc.status_pb2_model.Status
    """"""


class RoomJoinEvent(BaseModel):
    """"""


class RoomLeaveEvent(BaseModel):
    """"""


class RoomMessageEvent(BaseModel):
    """"""

    target_path: builtins.str
    """"""
    body: Any
    """"""


class RoomOnlineEvent(BaseModel):
    """"""

    online: builtins.int
    """"""
    all_online: builtins.int
    """"""


class RoomReq(BaseModel):
    """"""

    id: builtins.str
    """{type}://{room_id}"""
    join: Optional["RoomJoinEvent"] = None
    """"""
    leave: Optional["RoomLeaveEvent"] = None
    """"""
    online: Optional["RoomOnlineEvent"] = None
    """"""
    msg: Optional["RoomMessageEvent"] = None
    """"""


class RoomResp(BaseModel):
    """"""

    id: builtins.str
    """{type}://{room_id}"""
    join: Optional["RoomJoinEvent"] = None
    """"""
    leave: Optional["RoomLeaveEvent"] = None
    """"""
    online: Optional["RoomOnlineEvent"] = None
    """"""
    msg: Optional["RoomMessageEvent"] = None
    """"""
    err: Optional["RoomErrorEvent"] = None
    """"""


RoomErrorEvent.update_forward_refs()
RoomJoinEvent.update_forward_refs()
RoomReq.update_forward_refs()
RoomMessageEvent.update_forward_refs()
RoomOnlineEvent.update_forward_refs()
RoomResp.update_forward_refs()
RoomLeaveEvent.update_forward_refs()

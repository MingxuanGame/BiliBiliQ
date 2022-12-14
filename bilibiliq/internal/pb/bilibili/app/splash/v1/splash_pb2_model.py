"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class ShowStrategy(BaseModel):
    """"""

    id: builtins.int
    """"""
    stime: builtins.int
    """"""
    etime: builtins.int
    """"""


class SplashItem(BaseModel):
    """"""

    id: builtins.int
    """"""
    type: builtins.int
    """"""
    card_type: builtins.int
    """"""
    duration: builtins.int
    """"""
    begin_time: builtins.int
    """"""
    end_time: builtins.int
    """"""
    thumb: builtins.str
    """"""
    hash: builtins.str
    """"""
    logo_url: builtins.str
    """"""
    logo_hash: builtins.str
    """"""
    video_url: builtins.str
    """"""
    video_hash: builtins.str
    """"""
    video_width: builtins.int
    """"""
    video_height: builtins.int
    """"""
    schema: builtins.str
    """"""
    schema_title: builtins.str
    """"""
    schema_package_name: builtins.str
    """"""
    schema_callup_whiteList: List[builtins.str]
    """"""
    skip: builtins.int
    """"""
    uri: builtins.str
    """"""
    uri_title: builtins.str
    """"""
    source: builtins.int
    """"""
    cm_mark: builtins.int
    """"""
    ad_cb: builtins.str
    """"""
    resource_id: builtins.int
    """"""
    request_id: builtins.str
    """"""
    client_ip: builtins.str
    """"""
    is_ad: builtins.bool
    """"""
    is_ad_loc: builtins.bool
    """"""
    extra: Any
    """"""
    card_index: builtins.int
    """"""
    server_type: builtins.int
    """"""
    index: builtins.int
    """"""
    click_url: builtins.str
    """"""
    show_url: builtins.str
    """"""
    time_target: builtins.int
    """"""
    encryption: builtins.int
    """"""
    enable_pre_download: builtins.bool
    """"""
    enable_background_download: builtins.bool
    """"""


class SplashReply(BaseModel):
    """-响应"""

    max_time: builtins.int
    """"""
    min_interval: builtins.int
    """"""
    pull_interval: builtins.int
    """"""
    list: "List[SplashItem]"
    """"""
    show: "List[ShowStrategy]"
    """"""


class SplashReq(BaseModel):
    """-请求"""

    width: builtins.int
    """"""
    height: builtins.int
    """"""
    birth: builtins.str
    """"""
    ad_extra: builtins.str
    """"""
    network: builtins.str
    """"""


SplashReq.update_forward_refs()
ShowStrategy.update_forward_refs()
SplashItem.update_forward_refs()
SplashReply.update_forward_refs()

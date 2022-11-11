"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
import bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model
import bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model


class DynamicButtonClickBizType(str, Enum):
    """"""

    DYNAMIC_BUTTON_CLICK_BIZ_TYPE_NONE = 'DYNAMIC_BUTTON_CLICK_BIZ_TYPE_NONE'
    """"""
    DYNAMIC_BUTTON_CLICK_BIZ_TYPE_LIVE = 'DYNAMIC_BUTTON_CLICK_BIZ_TYPE_LIVE'
    """"""
    DYNAMIC_BUTTON_CLICK_BIZ_TYPE_DYN_UP = (
        'DYNAMIC_BUTTON_CLICK_BIZ_TYPE_DYN_UP'
    )
    """"""


class ReserveButtonMode(str, Enum):
    """"""

    RESERVE_BUTTON_MODE_NONE = 'RESERVE_BUTTON_MODE_NONE'
    """"""
    RESERVE_BUTTON_MODE_RESERVE = 'RESERVE_BUTTON_MODE_RESERVE'
    """"""
    RESERVE_BUTTON_MODE_UP_CANCEL = 'RESERVE_BUTTON_MODE_UP_CANCEL'
    """"""


class ReserveButtonStatus(str, Enum):
    """"""

    RESERVE_BUTTON_STATUS_NONE = 'RESERVE_BUTTON_STATUS_NONE'
    """"""
    RESERVE_BUTTON_STATUS_UNCHECK = 'RESERVE_BUTTON_STATUS_UNCHECK'
    """"""
    RESERVE_BUTTON_STATUS_CHECK = 'RESERVE_BUTTON_STATUS_CHECK'
    """"""


class CreateDynReq(BaseModel):
    """创建动态-请求"""

    meta: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.UserCreateMeta
    """用户创建接口meta信息"""
    content: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.CreateContent
    """发布的内容"""
    scene: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.CreateScene
    """发布类型"""
    pics: List[
        bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.CreatePic
    ]
    """图片内容"""
    repost_src: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.DynIdentity
    """转发源"""
    video: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.CreateDynVideo
    """动态视频"""
    sketch_type: builtins.int
    """通用模板类型：2048方图 2049竖图 其他值无效"""
    sketch: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.Sketch
    """通用模板的元内容（网页内容）"""
    program: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.Program
    """小程序的内容"""
    dyn_tag: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.CreateTag
    """动态附加小卡"""
    attach_card: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.CreateAttachCard
    """动态附加大卡"""
    option: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.CreateOption
    """特殊的创建选项"""
    topic: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.CreateTopic
    """"""
    upload_id: builtins.str
    """"""


class CreateInitCheckReq(BaseModel):
    """"""

    scene: builtins.int
    """"""
    meta: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.MetaDataCtrl
    """"""
    repost: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.RepostInitCheck
    """"""


class CreatePageInfosReq(BaseModel):
    """"""

    topic_id: builtins.int
    """"""


class CreatePageInfosRsp(BaseModel):
    """"""

    topic: Optional["CreatePageTopicInfo"] = None
    """"""


class CreatePageTopicInfo(BaseModel):
    """"""

    topic_id: builtins.int
    """"""
    topic_name: builtins.str
    """"""


class CreatePermissionButtonClickReq(BaseModel):
    """"""

    type: DynamicButtonClickBizType
    """"""


class CreatePermissionButtonClickRsp(BaseModel):
    """"""


class CreatePlusButtonClickReq(BaseModel):
    """"""


class CreatePlusButtonClickRsp(BaseModel):
    """"""


class DynamicButtonClickReq(BaseModel):
    """"""


class DynamicButtonClickRsp(BaseModel):
    """"""


class HotSearchReq(BaseModel):
    """"""


class HotSearchRsp(BaseModel):
    """"""

    class HotSearchRsp_Item(BaseModel):
        """"""

        words: builtins.str
        """"""

    items: "List[HotSearchRsp_Item]"
    """"""
    version: builtins.str
    """"""


class ReserveButtonClickReq(BaseModel):
    """"""

    uid: builtins.int
    """"""
    reserve_id: builtins.int
    """"""
    reserve_total: builtins.int
    """"""
    cur_btn_status: builtins.int
    """"""
    spmid: builtins.str
    """"""
    dyn_id: builtins.int
    """"""
    dyn_type: builtins.int
    """"""


class ReserveButtonClickResp(BaseModel):
    """"""

    final_btn_status: ReserveButtonStatus
    """"""
    btn_mode: ReserveButtonMode
    """"""
    reserve_update: builtins.int
    """"""
    desc_update: builtins.str
    """"""
    has_activity: builtins.bool
    """"""
    activity_url: builtins.str
    """"""
    toast: builtins.str
    """"""


class SubmitCheckReq(BaseModel):
    """"""

    content: bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.CreateContent
    """"""
    pics: List[
        bilibiliq.internal.pb.bilibili.dynamic.common.dynamic_pb2_model.CreatePic
    ]
    """"""


class SubmitCheckRsp(BaseModel):
    """"""


class SuggestReq(BaseModel):
    """"""

    s: builtins.str
    """"""
    type: builtins.int
    """"""


class SuggestRsp(BaseModel):
    """"""

    list: List[builtins.str]
    """"""
    track_id: builtins.str
    """"""
    version: builtins.str
    """"""


HotSearchReq.update_forward_refs()
CreatePermissionButtonClickRsp.update_forward_refs()
CreatePlusButtonClickReq.update_forward_refs()
DynamicButtonClickRsp.update_forward_refs()
CreatePermissionButtonClickReq.update_forward_refs()
CreateDynReq.update_forward_refs()
SubmitCheckReq.update_forward_refs()
HotSearchRsp.update_forward_refs()
CreateInitCheckReq.update_forward_refs()
DynamicButtonClickReq.update_forward_refs()
SuggestReq.update_forward_refs()
ReserveButtonClickResp.update_forward_refs()
SubmitCheckRsp.update_forward_refs()
CreatePageInfosReq.update_forward_refs()
CreatePageTopicInfo.update_forward_refs()
ReserveButtonClickReq.update_forward_refs()
CreatePageInfosRsp.update_forward_refs()
CreatePlusButtonClickRsp.update_forward_refs()
SuggestRsp.update_forward_refs()

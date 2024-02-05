"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""

import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
import bilibiliq.internal.pb.bilibili.app.card.v1.single_pb2_model


class Card(BaseModel):
    """卡片信息"""

    small_cover_v5: (
        bilibiliq.internal.pb.bilibili.app.card.v1.single_pb2_model.SmallCoverV5
    )
    """小封面条目"""
    large_cover_v1: (
        bilibiliq.internal.pb.bilibili.app.card.v1.single_pb2_model.LargeCoverV1
    )
    """"""
    three_item_all_v2: (
        bilibiliq.internal.pb.bilibili.app.card.v1.single_pb2_model.ThreeItemAllV2
    )
    """"""
    three_item_v1: (
        bilibiliq.internal.pb.bilibili.app.card.v1.single_pb2_model.ThreeItemV1
    )
    """"""
    hot_topic: (
        bilibiliq.internal.pb.bilibili.app.card.v1.single_pb2_model.HotTopic
    )
    """"""
    three_item_h_v5: (
        bilibiliq.internal.pb.bilibili.app.card.v1.single_pb2_model.DynamicHot
    )
    """"""
    middle_cover_v3: (
        bilibiliq.internal.pb.bilibili.app.card.v1.single_pb2_model.MiddleCoverV3
    )
    """"""
    large_cover_v4: (
        bilibiliq.internal.pb.bilibili.app.card.v1.single_pb2_model.LargeCoverV4
    )
    """"""
    popular_top_entrance: (
        bilibiliq.internal.pb.bilibili.app.card.v1.single_pb2_model.PopularTopEntrance
    )
    """热门列表顶部按钮"""
    rcmd_one_item: (
        bilibiliq.internal.pb.bilibili.app.card.v1.single_pb2_model.RcmdOneItem
    )
    """"""
    small_cover_v5_ad: (
        bilibiliq.internal.pb.bilibili.app.card.v1.single_pb2_model.SmallCoverV5Ad
    )
    """"""


Card.update_forward_refs()

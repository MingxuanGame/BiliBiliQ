"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""

import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
import bilibiliq.internal.pb.bilibili.app.archive.middleware.v1.preload_pb2_model


class DT(str, Enum):
    """设备标识代码"""

    Unknown = 'Unknown'
    """未知"""
    Phone = 'Phone'
    """手机端"""
    Pad = 'Pad'
    """ipad端"""
    PC = 'PC'
    """web端"""
    TV = 'TV'
    """TV端"""
    Car = 'Car'
    """车机端"""
    Iot = 'Iot'
    """物联设备"""
    AndPad = 'AndPad'
    """apad端"""


class HistorySource(str, Enum):
    """搜索历史记录来源"""

    history_VALUE = 'history_VALUE'
    """主站历史记录页"""
    shopping_VALUE = 'shopping_VALUE'
    """会员购浏览记录"""


class CardArticle(BaseModel):
    """专栏卡片"""

    covers: List[builtins.str]
    """封面url"""
    name: builtins.str
    """UP主昵称"""
    mid: builtins.int
    """UP主mid"""
    displayAttention: builtins.bool
    """是否展示关注按钮"""
    badge: builtins.str
    """角标"""
    relation: Optional["Relation"] = None
    """关系信息"""


class CardCheese(BaseModel):
    """课程卡片"""

    cover: builtins.str
    """封面url"""
    progress: builtins.int
    """观看进度"""
    duration: builtins.int
    """总计时长"""
    subtitle: builtins.str
    """单集标题"""
    state: builtins.int
    """"""


class CardLive(BaseModel):
    """直播卡片"""

    cover: builtins.str
    """封面url"""
    name: builtins.str
    """主播昵称"""
    mid: builtins.int
    """主播mid"""
    tag: builtins.str
    """直播分区名"""
    ststus: builtins.int
    """直播状态"""
    display_attention: builtins.bool
    """是否展示关注按钮"""
    relation: Optional["Relation"] = None
    """关系信息"""


class CardOGV(BaseModel):
    """pgc稿件卡片"""

    cover: builtins.str
    """封面url"""
    progress: builtins.int
    """观看进度"""
    duration: builtins.int
    """总计时长"""
    subtitle: builtins.str
    """单集标题"""
    badge: builtins.str
    """"""
    state: builtins.int
    """"""


class CardUGC(BaseModel):
    """ugc稿件卡片"""

    cover: builtins.str
    """封面url"""
    progress: builtins.int
    """观看进度"""
    duration: builtins.int
    """视频长度"""
    name: builtins.str
    """UP主昵称"""
    mid: builtins.int
    """UP主mid"""
    display_attention: builtins.bool
    """是否展示关注按钮"""
    cid: builtins.int
    """历史观看视频cid"""
    page: builtins.int
    """历史观看视频分P"""
    subtitle: builtins.str
    """历史观看视频分P的标题"""
    relation: Optional["Relation"] = None
    """关系信息"""
    bvid: builtins.str
    """稿件bvid"""
    videos: builtins.int
    """总分P数"""
    short_link: builtins.str
    """短链接"""
    share_subtitle: builtins.str
    """分享副标题"""
    view: builtins.int
    """播放数"""
    state: builtins.int
    """"""


class ClearReq(BaseModel):
    """清空历史记录-请求"""

    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """


class Cursor(BaseModel):
    """游标信息"""

    max: builtins.int
    """本页最大值游标值"""
    maxTp: builtins.int
    """本页最大值游标类型"""


class CursorItem(BaseModel):
    """历史记录卡片信息"""

    card_ugc: Optional["CardUGC"] = None
    """ugc稿件"""
    card_ogv: Optional["CardOGV"] = None
    """pgc稿件"""
    card_article: Optional["CardArticle"] = None
    """专栏"""
    card_live: Optional["CardLive"] = None
    """直播"""
    card_cheese: Optional["CardCheese"] = None
    """课程"""
    title: builtins.str
    """标题"""
    uri: builtins.str
    """目标uri/url"""
    viewAt: builtins.int
    """观看时间"""
    kid: builtins.int
    """历史记录id"""
    oid: builtins.int
    """业务id"""
    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """
    tp: builtins.int
    """业务类型代码"""
    dt: Optional["DeviceType"] = None
    """设备标识"""
    has_share: builtins.bool
    """是否有分享按钮"""


class CursorReply(BaseModel):
    """获取历史记录列表(旧版)-响应"""

    items: "List[CursorItem]"
    """卡片内容"""
    tab: "List[CursorTab]"
    """顶部tab"""
    cursor: Optional["Cursor"] = None
    """游标信息"""
    hasMore: builtins.bool
    """是否未拉取完"""


class CursorReq(BaseModel):
    """获取历史记录列表(旧版)-请求"""

    cursor: Optional["Cursor"] = None
    """游标信息"""
    business: builtins.str
    """业务类型
    all:全部 archive:视频 live:直播 article:专栏
    """
    player_preload: Optional["PlayerPreloadParams"] = None
    """秒开参数(旧版)"""
    player_args: (
        bilibiliq.internal.pb.bilibili.app.archive.middleware.v1.preload_pb2_model.PlayerArgs
    )
    """秒开参数"""


class CursorTab(BaseModel):
    """业务分类表"""

    business: builtins.str
    """业务类型"""
    name: builtins.str
    """名称"""
    router: builtins.str
    """路由uri"""
    focus: builtins.bool
    """tab定位"""


class CursorV2Reply(BaseModel):
    """获取历史记录列表-响应"""

    items: "List[CursorItem]"
    """卡片内容"""
    cursor: Optional["Cursor"] = None
    """游标信息"""
    hasMore: builtins.bool
    """是否未拉取完"""
    empty_link: builtins.str
    """"""


class CursorV2Req(BaseModel):
    """获取历史记录列表-请求"""

    cursor: Optional["Cursor"] = None
    """游标信息"""
    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """
    player_preload: Optional["PlayerPreloadParams"] = None
    """秒开参数(旧版)"""
    player_args: (
        bilibiliq.internal.pb.bilibili.app.archive.middleware.v1.preload_pb2_model.PlayerArgs
    )
    """秒开参数"""
    is_local: builtins.bool
    """是否选择本机的播放历史"""


class DeleteReq(BaseModel):
    """删除历史记录-请求"""

    his_info: Optional["HisInfo"] = None
    """历史记录信息"""


class DeviceType(BaseModel):
    """设备类型"""

    type: DT
    """设备标识代码"""
    icon: builtins.str
    """图标url"""


class HisInfo(BaseModel):
    """历史记录信息"""

    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """
    kid: builtins.int
    """历史记录id"""


class HistoryTabReply(BaseModel):
    """获取历史记录tab-响应"""

    tab: "List[CursorTab]"
    """tab列表"""


class HistoryTabReq(BaseModel):
    """获取历史记录tab-请求"""

    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """
    source: HistorySource
    """查询请求来源"""
    keyword: builtins.str
    """搜索关键词"""


class LatestHistoryReply(BaseModel):
    """获取最新的历史记录-响应"""

    items: Optional["CursorItem"] = None
    """卡片内容"""
    scene: builtins.str
    """场景"""
    rtime: builtins.int
    """弹窗停留时间"""
    flag: builtins.str
    """分组的标志(客户端埋点上报)"""


class LatestHistoryReq(BaseModel):
    """获取最新的历史记录-请求"""

    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """
    player_preload: Optional["PlayerPreloadParams"] = None
    """秒开参数"""


class NoReply(BaseModel):
    """空响应"""


class Page(BaseModel):
    """页面信息"""

    pn: builtins.int
    """当前页码"""
    total: builtins.int
    """总计条目数"""


class PlayerPreloadParams(BaseModel):
    """秒开参数"""

    qn: builtins.int
    """清晰度"""
    fnver: builtins.int
    """流版本"""
    fnval: builtins.int
    """流类型"""
    forceHost: builtins.int
    """是否强制域名"""
    fourk: builtins.int
    """是否4K"""


class Relation(BaseModel):
    """关系信息"""

    status: builtins.int
    """关系状态
    1:未关注 2:已关注 3:被关注 4:互关
    """
    is_follow: builtins.int
    """用户关注UP主"""
    is_followed: builtins.int
    """UP主关注用户"""


class SearchReply(BaseModel):
    """搜索历史记录-响应"""

    items: "List[CursorItem]"
    """卡片内容"""
    hasMore: builtins.bool
    """是否未拉取完"""
    page: Optional["Page"] = None
    """页面信息"""


class SearchReq(BaseModel):
    """搜索历史记录-请求"""

    keyword: builtins.str
    """关键词"""
    pn: builtins.int
    """页码"""
    business: builtins.str
    """业务类型
    archive:视频 live:直播 article:专栏 goods:商品 show:展演
    """


CursorReq.update_forward_refs()
HistoryTabReply.update_forward_refs()
CursorV2Reply.update_forward_refs()
Page.update_forward_refs()
CardOGV.update_forward_refs()
CursorItem.update_forward_refs()
CursorReply.update_forward_refs()
CardUGC.update_forward_refs()
HisInfo.update_forward_refs()
CardLive.update_forward_refs()
SearchReply.update_forward_refs()
CursorV2Req.update_forward_refs()
DeleteReq.update_forward_refs()
NoReply.update_forward_refs()
LatestHistoryReply.update_forward_refs()
SearchReq.update_forward_refs()
ClearReq.update_forward_refs()
CardCheese.update_forward_refs()
CursorTab.update_forward_refs()
Cursor.update_forward_refs()
CardArticle.update_forward_refs()
Relation.update_forward_refs()
PlayerPreloadParams.update_forward_refs()
LatestHistoryReq.update_forward_refs()
DeviceType.update_forward_refs()
HistoryTabReq.update_forward_refs()

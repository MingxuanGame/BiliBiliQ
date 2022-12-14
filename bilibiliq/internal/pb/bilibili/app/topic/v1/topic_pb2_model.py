"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
import bilibiliq.internal.pb.bilibili.app.dynamic.v2.dynamic_pb2_model
import bilibiliq.internal.pb.bilibili.app.archive.middleware.v1.preload_pb2_model
import bilibiliq.internal.pb.bilibili.app.card.v1.common_pb2_model


class TopicCardType(str, Enum):
    """"""

    ILLEGAL_TYPE = 'ILLEGAL_TYPE'
    """"""
    DYNAMIC = 'DYNAMIC'
    """"""
    FOLD = 'FOLD'
    """"""
    VIDEO_SMALL_CARD = 'VIDEO_SMALL_CARD'
    """"""


class TopicDetailsExtMode(str, Enum):
    """"""

    MODE_ILLEGAL_TYPE = 'MODE_ILLEGAL_TYPE'
    """"""
    STORY = 'STORY'
    """"""


class ButtonMeta(BaseModel):
    """"""

    text: builtins.str
    """"""
    icon: builtins.str
    """"""


class DetailsTopInfo(BaseModel):
    """"""

    topic_info: Optional["TopicInfo"] = None
    """"""
    user: Optional["User"] = None
    """"""
    stats_desc: builtins.str
    """"""
    has_create_jurisdiction: builtins.bool
    """"""
    operation_content: Optional["OperationContent"] = None
    """"""
    head_img_url: builtins.str
    """"""
    head_img_backcolor: builtins.str
    """"""
    word_color: builtins.int
    """"""
    mission_page_show_type: builtins.int
    """"""
    mission_url: builtins.str
    """"""
    mission_text: builtins.str
    """"""
    topic_set: Optional["TopicSet"] = None
    """"""


class FoldCardItem(BaseModel):
    """"""

    is_show_fold: builtins.int
    """"""
    fold_count: builtins.int
    """"""
    card_show_desc: builtins.str
    """"""
    fold_desc: builtins.str
    """"""


class FunctionalCard(BaseModel):
    """"""

    capsules: "List[TopicCapsule]"
    """"""
    traffic_card: Optional["TrafficCard"] = None
    """"""
    game_card: Optional["GameCard"] = None
    """"""


class GameCard(BaseModel):
    """"""

    game_id: builtins.int
    """"""
    game_icon: builtins.str
    """"""
    game_name: builtins.str
    """"""
    score: builtins.str
    """"""
    game_tags: builtins.str
    """"""
    notice: builtins.str
    """"""
    game_link: builtins.str
    """"""


class InlineProgressBar(BaseModel):
    """"""

    icon_drag: builtins.str
    """"""
    icon_drag_hash: builtins.str
    """"""
    icon_stop: builtins.str
    """"""
    icon_stop_hash: builtins.str
    """"""


class LargeCoverInline(BaseModel):
    """"""

    base: bilibiliq.internal.pb.bilibili.app.card.v1.common_pb2_model.Base
    """"""
    cover_left_text1: builtins.str
    """"""
    cover_left_icon1: builtins.int
    """"""
    cover_left_text2: builtins.str
    """"""
    cover_left_icon2: builtins.int
    """"""
    right_top_live_badge: Optional["RightTopLiveBadge"] = None
    """"""
    extra_uri: builtins.str
    """"""
    inline_progress_bar: Optional["InlineProgressBar"] = None
    """"""
    topic_three_point: Optional["TopicThreePoint"] = None
    """"""
    cover_left_desc: builtins.str
    """"""
    hide_danmu_switch: builtins.bool
    """"""
    disable_danmu: builtins.bool
    """"""
    can_play: builtins.int
    """"""
    duration_text: builtins.str
    """"""
    relation_data: Optional["RelationData"] = None
    """"""


class LiveBadgeResource(BaseModel):
    """"""

    text: builtins.str
    """"""
    animation_url: builtins.str
    """"""
    animation_url_hash: builtins.str
    """"""
    background_color_light: builtins.str
    """"""
    background_color_night: builtins.str
    """"""
    alpha_light: builtins.int
    """"""
    alpha_night: builtins.int
    """"""
    font_color: builtins.str
    """"""


class OperationCard(BaseModel):
    """"""

    large_cover_inline: Optional["LargeCoverInline"] = None
    """"""


class OperationContent(BaseModel):
    """"""

    operation_card: Optional["OperationCard"] = None
    """"""


class PubLayer(BaseModel):
    """"""

    show_type: builtins.int
    """"""
    jump_link: builtins.str
    """"""
    button_meta: Optional["ButtonMeta"] = None
    """"""
    close_pub_layer_entry: builtins.bool
    """"""


class RelationData(BaseModel):
    """"""

    is_fav: builtins.bool
    """"""
    is_coin: builtins.bool
    """"""
    is_follow: builtins.bool
    """"""
    is_like: builtins.bool
    """"""
    like_count: builtins.int
    """"""


class RightTopLiveBadge(BaseModel):
    """"""

    live_status: builtins.int
    """"""
    in_live: Optional["LiveBadgeResource"] = None
    """"""
    live_stats_desc: builtins.str
    """"""


class SortContent(BaseModel):
    """"""

    sort_by: builtins.int
    """"""
    sort_name: builtins.str
    """"""


class ThreePointItem(BaseModel):
    """"""

    title: builtins.str
    """"""
    jump_url: builtins.str
    """"""


class TimeLineEvents(BaseModel):
    """"""

    event_id: builtins.int
    """"""
    title: builtins.str
    """"""
    time_desc: builtins.str
    """"""
    jump_link: builtins.str
    """"""


class TimeLineResource(BaseModel):
    """"""

    time_line_id: builtins.int
    """"""
    time_line_title: builtins.str
    """"""
    time_line_events: "List[TimeLineEvents]"
    """"""
    has_more: builtins.bool
    """"""


class TopicActivities(BaseModel):
    """"""

    activity: "List[TopicActivity]"
    """"""
    act_list_title: builtins.str
    """"""


class TopicActivity(BaseModel):
    """"""

    activity_id: builtins.int
    """"""
    activity_name: builtins.str
    """"""
    jump_url: builtins.str
    """"""
    icon_url: builtins.str
    """"""


class TopicCapsule(BaseModel):
    """"""

    name: builtins.str
    """"""
    jump_url: builtins.str
    """"""
    icon_url: builtins.str
    """"""


class TopicCardItem(BaseModel):
    """"""

    type: builtins.int
    """"""
    dynamic_item: bilibiliq.internal.pb.bilibili.app.dynamic.v2.dynamic_pb2_model.DynamicItem
    """"""
    ford_card_item: Optional["FoldCardItem"] = None
    """"""
    video_small_card_item: Optional["VideoSmallCardItem"] = None
    """"""


class TopicCardList(BaseModel):
    """"""

    topic_card_items: "List[TopicCardItem]"
    """"""
    offset: builtins.str
    """"""
    has_more: builtins.bool
    """"""
    topic_sort_by_conf: Optional["TopicSortByConf"] = None
    """"""


class TopicDetailsAllReply(BaseModel):
    """"""

    details_top_info: Optional["DetailsTopInfo"] = None
    """"""
    topic_activities: Optional["TopicActivities"] = None
    """"""
    topic_card_list: "TopicCardList"
    """"""
    functional_card: Optional["FunctionalCard"] = None
    """"""
    pub_layer: Optional["PubLayer"] = None
    """"""
    time_line_resource: Optional["TimeLineResource"] = None
    """"""
    topic_server_config: Optional["TopicServerConfig"] = None
    """"""


class TopicDetailsAllReq(BaseModel):
    """"""

    topic_id: builtins.int
    """"""
    sort_by: builtins.int
    """"""
    offset: builtins.str
    """"""
    page_size: builtins.int
    """"""
    local_time: builtins.int
    """"""
    player_args: bilibiliq.internal.pb.bilibili.app.archive.middleware.v1.preload_pb2_model.PlayerArgs
    """"""
    need_refresh: builtins.int
    """"""
    source: builtins.str
    """"""
    topic_details_ext_mode: builtins.int
    """"""


class TopicDetailsFoldReply(BaseModel):
    """"""

    topic_card_list: "TopicCardList"
    """"""
    fold_count: builtins.int
    """"""


class TopicDetailsFoldReq(BaseModel):
    """"""

    topic_id: builtins.int
    """"""
    offset: builtins.str
    """"""
    page_size: builtins.int
    """"""
    local_time: builtins.int
    """"""
    player_args: bilibiliq.internal.pb.bilibili.app.archive.middleware.v1.preload_pb2_model.PlayerArgs
    """"""
    from_sort_by: builtins.int
    """"""


class TopicInfo(BaseModel):
    """"""

    id: builtins.int
    """"""
    name: builtins.str
    """"""
    uid: builtins.int
    """"""
    view: builtins.int
    """"""
    discuss: builtins.int
    """"""
    fav: builtins.int
    """"""
    dynamics: builtins.int
    """"""
    state: builtins.int
    """"""
    jump_url: builtins.str
    """"""
    backcolor: builtins.str
    """"""
    is_fav: builtins.bool
    """"""
    description: builtins.str
    """"""
    create_source: builtins.int
    """"""
    share_pic: builtins.str
    """"""
    share: builtins.int
    """"""
    like: builtins.int
    """"""
    share_url: builtins.str
    """"""
    is_like: builtins.bool
    """"""
    type: builtins.int
    """"""
    stats_desc: builtins.str
    """"""
    fixed_topic_icon: builtins.str
    """"""


class TopicServerConfig(BaseModel):
    """"""

    pub_events_increase_threshold: builtins.int
    """"""
    pub_events_hidden_timeout_threshold: builtins.int
    """"""
    vert_online_refresh_time: builtins.int
    """"""


class TopicSet(BaseModel):
    """"""

    set_id: builtins.int
    """"""
    set_name: builtins.str
    """"""
    jump_url: builtins.str
    """"""
    desc: builtins.str
    """"""


class TopicSetDetailsReply(BaseModel):
    """"""

    topic_set_head_info: Optional["TopicSetHeadInfo"] = None
    """"""
    topic_info: "List[TopicInfo]"
    """"""
    has_more: builtins.bool
    """"""
    offset: builtins.str
    """"""
    sort_cfg: Optional["TopicSetSortCfg"] = None
    """"""


class TopicSetDetailsReq(BaseModel):
    """"""

    set_id: builtins.int
    """"""
    sort_by: builtins.int
    """"""
    offset: builtins.str
    """"""
    page_size: builtins.int
    """"""


class TopicSetHeadInfo(BaseModel):
    topic_set: Optional["TopicSet"] = None
    """"""
    topic_cnt_text: builtins.str
    """"""
    head_img_url: builtins.str
    """"""
    mission_url: builtins.str
    """"""
    mission_text: builtins.str
    """"""
    icon_url: builtins.str
    """"""
    is_fav: builtins.bool
    """"""
    is_first_time: builtins.bool
    """"""


class TopicSetSortCfg(BaseModel):
    """"""

    default_sort_by: builtins.int
    """"""
    all_sort_by: "List[SortContent]"
    """"""


class TopicSortByConf(BaseModel):
    """"""

    default_sort_by: builtins.int
    """"""
    all_sort_by: "List[SortContent]"
    """"""
    show_sort_by: builtins.int
    """"""


class TopicThreePoint(BaseModel):
    """"""

    dyn_three_point_items: "List[ThreePointItem]"
    """"""


class TrafficCard(BaseModel):
    """"""

    name: builtins.str
    """"""
    jump_url: builtins.str
    """"""
    icon_url: builtins.str
    """"""
    base_pic: builtins.str
    """"""
    benefit_point: builtins.str
    """"""
    card_desc: builtins.str
    """"""
    jump_title: builtins.str
    """"""


class User(BaseModel):
    """"""

    uid: builtins.int
    """"""
    face: builtins.str
    """"""
    name: builtins.str
    """"""
    name_desc: builtins.str
    """"""


class VideoCardBase(BaseModel):
    """"""

    cover: builtins.str
    """"""
    title: builtins.str
    """"""
    up_name: builtins.str
    """"""
    play: builtins.int
    """"""
    jump_link: builtins.str
    """"""
    aid: builtins.int
    """"""


class VideoSmallCardItem(BaseModel):
    """"""

    video_card_base: Optional["VideoCardBase"] = None
    """"""
    cover_left_badge_text: builtins.str
    """"""
    card_stat_icon1: builtins.int
    """"""
    card_stat_text1: builtins.str
    """"""
    card_stat_icon2: builtins.int
    """"""
    card_stat_text2: builtins.str
    """"""


TopicSortByConf.update_forward_refs()
TopicCardItem.update_forward_refs()
GameCard.update_forward_refs()
ThreePointItem.update_forward_refs()
FunctionalCard.update_forward_refs()
PubLayer.update_forward_refs()
TopicDetailsFoldReply.update_forward_refs()
RelationData.update_forward_refs()
TopicThreePoint.update_forward_refs()
VideoCardBase.update_forward_refs()
TopicSet.update_forward_refs()
InlineProgressBar.update_forward_refs()
DetailsTopInfo.update_forward_refs()
TimeLineEvents.update_forward_refs()
VideoSmallCardItem.update_forward_refs()
TopicActivities.update_forward_refs()
OperationCard.update_forward_refs()
ButtonMeta.update_forward_refs()
TopicDetailsFoldReq.update_forward_refs()
OperationContent.update_forward_refs()
FoldCardItem.update_forward_refs()
TrafficCard.update_forward_refs()
TopicActivity.update_forward_refs()
User.update_forward_refs()
TopicCapsule.update_forward_refs()
TopicCardList.update_forward_refs()
TopicDetailsAllReq.update_forward_refs()
TimeLineResource.update_forward_refs()
TopicDetailsAllReply.update_forward_refs()
LiveBadgeResource.update_forward_refs()
RightTopLiveBadge.update_forward_refs()
SortContent.update_forward_refs()
TopicSetDetailsReq.update_forward_refs()
TopicSetDetailsReply.update_forward_refs()
TopicServerConfig.update_forward_refs()
LargeCoverInline.update_forward_refs()
TopicSetHeadInfo.update_forward_refs()
TopicSetSortCfg.update_forward_refs()
TopicInfo.update_forward_refs()

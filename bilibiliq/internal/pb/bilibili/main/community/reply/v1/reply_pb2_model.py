"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class DetailListScene(str, Enum):
    """来源标识"""

    REPLY = 'REPLY'
    """评论区展开"""
    MSG_FEED = 'MSG_FEED'
    """回复消息推送"""
    NOTIFY = 'NOTIFY'
    """"""


class Mode(str, Enum):
    """排序方式"""

    DEFAULT = 'DEFAULT'
    """"""
    UNSPECIFIED = 'UNSPECIFIED'
    """默认排序"""
    MAIN_LIST_TIME = 'MAIN_LIST_TIME'
    """按时间"""
    MAIN_LIST_HOT = 'MAIN_LIST_HOT'
    """按热度"""


class SearchItemType(str, Enum):
    """"""

    DEFAULT_ITEM_TYPE = 'DEFAULT_ITEM_TYPE'
    """"""
    GOODS = 'GOODS'
    """"""
    VIDEO = 'VIDEO'
    """"""
    ARTICLE = 'ARTICLE'
    """"""


class SearchItemVideoSubType(str, Enum):
    """"""

    UGC = 'UGC'
    """"""
    PGC = 'PGC'
    """"""


class UserCallbackAction(str, Enum):
    """"""

    Dismiss = 'Dismiss'
    """"""


class UserCallbackScene(str, Enum):
    """"""

    Insert = 'Insert'
    """"""


class Activity(BaseModel):
    """活动"""

    activity_id: builtins.int
    """活动id"""
    activity_state: builtins.int
    """活动状态
    -1:待审 1:上线
    """
    activity_placeholder: builtins.str
    """参与活动的输入框文案"""


class ArticleSearchItem(BaseModel):
    """文章项目"""

    title: builtins.str
    """标题"""
    up_nickname: builtins.str
    """UP主昵称"""
    covers: List[builtins.str]
    """封面"""


class AtGroup(BaseModel):
    """评论at用户搜索组"""

    group_type: builtins.int
    """组类型"""
    group_name: builtins.str
    """组标题"""
    items: "List[AtItem]"
    """评论at用户搜索列表"""


class AtItem(BaseModel):
    """评论at用户搜索条目"""

    mid: builtins.int
    """用户mid"""
    name: builtins.str
    """用户名"""
    face: builtins.str
    """用户头像url"""
    fans: builtins.int
    """用户是否关注"""
    official_verify_type: builtins.int
    """用户认证类型"""


class AtSearchReply(BaseModel):
    """评论at用户搜索-响应"""

    groups: "List[AtGroup]"
    """评论at用户搜索组"""


class AtSearchReq(BaseModel):
    """评论at用户搜索-请求"""

    mid: builtins.int
    """"""
    keyword: builtins.str
    """关键字"""


class CM(BaseModel):
    """广告"""

    source_content: Any
    """广告数据(需要解包)"""


class Content(BaseModel):
    """评论主体信息"""

    message: builtins.str
    """评论文本"""
    menber: Dict[builtins.str, Optional["Member"]]
    """需要渲染的用户转义"""
    emote: Dict[builtins.str, Optional["Emote"]]
    """需要渲染的表情转义"""
    topic: Dict[builtins.str, Optional["Topic"]]
    """需要高亮的话题转义"""
    url: Dict[builtins.str, Optional["Url"]]
    """需要高亮的超链转义"""
    vote: Optional["Vote"] = None
    """投票信息"""
    at_name_to_mid: Dict[builtins.str, builtins.int]
    """at到的用户mid列表"""
    rich_text: Optional["RichText"] = None
    """富文本"""


class CursorReply(BaseModel):
    """页面游标回复"""

    next: builtins.int
    """下页数据"""
    prev: builtins.int
    """上页数据"""
    isBegin: builtins.bool
    """是否到顶"""
    isEnd: builtins.bool
    """是否到底"""
    mode: Mode
    """排序方式
    2:时间 3:热度
    """
    mode_text: builtins.str
    """当前排序mode在切换按钮上的展示文案"""


class CursorReq(BaseModel):
    """页面游标请求"""

    next: builtins.int
    """下页数据"""
    prev: builtins.int
    """上页数据"""
    mode: Mode
    """排序方式"""


class DetailListReply(BaseModel):
    """二级评论明细-响应"""

    cursor: Optional["CursorReply"] = None
    """页面游标"""
    subject_control: Optional["SubjectControl"] = None
    """评论区显示控制字段"""
    root: Optional["ReplyInfo"] = None
    """根评论信息(带二级评论)"""
    activity: Optional["Activity"] = None
    """评论区的活动"""
    likes: Optional["LikeInfo"] = None
    """"""


class DetailListReq(BaseModel):
    """二级评论明细-请求"""

    oid: builtins.int
    """目标评论区id"""
    type: builtins.int
    """目标评论区业务type"""
    root: builtins.int
    """根评论rpid"""
    rpid: builtins.int
    """目标评论rpid"""
    cursor: Optional["CursorReq"] = None
    """页面游标"""
    scene: "DetailListScene"
    """来源标识"""


class DialogListReply(BaseModel):
    """对话评论树-响应"""

    cursor: Optional["CursorReply"] = None
    """页面游标"""
    subject_control: Optional["SubjectControl"] = None
    """评论区显示控制字段"""
    replies: "List[ReplyInfo]"
    """子评论列表"""
    activity: Optional["Activity"] = None
    """评论区的活动"""


class DialogListReq(BaseModel):
    """对话评论树-请求"""

    oid: builtins.int
    """目标评论区id"""
    type: builtins.int
    """目标评论区业务type"""
    root: builtins.int
    """根评论rpid"""
    rpid: builtins.int
    """对话评论rpid"""
    cursor: Optional["CursorReq"] = None
    """页面游标"""


class Effects(BaseModel):
    """特效"""

    preloading: builtins.str
    """"""


class Emote(BaseModel):
    """表情项"""

    size: builtins.int
    """表情大小
    1:小 2:大
    """
    url: builtins.str
    """表情url"""
    jump_url: builtins.str
    """"""
    jump_title: builtins.str
    """"""
    id: builtins.int
    """"""
    package_id: builtins.int
    """"""
    gif_url: builtins.str
    """"""
    text: builtins.str
    """"""


class GoodsSearchItem(BaseModel):
    """商品项目"""

    id: builtins.int
    """商品id"""
    name: builtins.str
    """商品名"""
    price: builtins.str
    """价钱"""
    income: builtins.str
    """收入"""
    img: builtins.str
    """图片"""
    label: builtins.str
    """标签"""


class LikeInfo(BaseModel):
    """"""

    class LikeInfo_Item(BaseModel):
        """"""

        member: Optional["Member"] = None
        """"""

    items: "List[LikeInfo_Item]"
    """"""
    title: builtins.str
    """"""


class Lottery(BaseModel):
    """抽奖"""

    lottery_id: builtins.int
    """抽奖id"""
    lottery_status: builtins.int
    """抽奖状态
    0:未开奖 1:开奖中 2:已开奖
    """
    lottery_mid: builtins.int
    """抽奖人mid"""
    lottery_time: builtins.int
    """开奖时间"""
    oid: builtins.int
    """"""
    type: builtins.int
    """"""
    ctime: builtins.int
    """发送时间"""
    content: Optional["Content"] = None
    """抽奖评论正文"""
    member: Optional["Member"] = None
    """用户信息"""
    reply_control: Optional["ReplyControl"] = None
    """评论条目控制字段"""


class MainListReply(BaseModel):
    """主评论列表-响应"""

    cursor: Optional["CursorReply"] = None
    """页面游标"""
    replies: "List[ReplyInfo]"
    """评论列表"""
    subject_control: Optional["SubjectControl"] = None
    """评论区显示控制字段"""
    up_top: Optional["ReplyInfo"] = None
    """UP置顶评论"""
    admin_top: Optional["ReplyInfo"] = None
    """管理员置顶评论"""
    vote_top: Optional["ReplyInfo"] = None
    """投票置顶评论"""
    notice: Optional["Notice"] = None
    """评论区提示"""
    lottery: Optional["Lottery"] = None
    """抽奖评论"""
    activity: Optional["Activity"] = None
    """活动"""
    up_selection: Optional["UpSelection"] = None
    """精选评论区筛选后台信息"""
    cm: Optional["CM"] = None
    """广告"""
    effects: Optional["Effects"] = None
    """特效"""
    operation: Optional["Operation"] = None
    """"""
    top_replies: "List[ReplyInfo]"
    """"""
    qoe: Optional["QoeInfo"] = None
    """"""
    callbacks: Dict[builtins.str, builtins.int]
    """"""


class MainListReq(BaseModel):
    """主评论列表-请求"""

    oid: builtins.int
    """目标评论区id"""
    type: builtins.int
    """目标评论区业务type"""
    cursor: Optional["CursorReq"] = None
    """页面游标"""
    extra: builtins.str
    """扩展数据json"""
    ad_extra: builtins.str
    """广告扩展"""
    rpid: builtins.int
    """目标评论rpid"""
    seek_rpid: builtins.int
    """"""
    filter_tag_name: builtins.str
    """评论区筛选类型 取值可为: ["全部" "粉丝评论" "笔记长评"]"""


class Member(BaseModel):
    """用户信息"""

    class Member_RegionType(str, Enum):
        DEFAULT = 'DEFAULT'
        """默认"""
        MAINLAND = 'MAINLAND'
        """大陆地区"""
        GAT = 'GAT'
        """"""

    """默认"""
    """大陆地区"""
    """"""

    class Member_ShowStatus(str, Enum):
        SHOWDEFAULT = 'SHOWDEFAULT'
        """默认"""
        ZOOMINMAINLAND = 'ZOOMINMAINLAND'
        """"""
        RAW = 'RAW'
        """"""

    """默认"""
    """"""
    """"""

    class Member_Region(BaseModel):
        """NFT地区"""

        type: "Member.Member_RegionType"
        """地区类型"""
        icon: builtins.str
        """角标url"""
        show_status: "Member.Member_ShowStatus"
        """"""

    class Member_NftInteraction(BaseModel):
        """NFT信息"""

        itype: builtins.str
        """"""
        metadata_url: builtins.str
        """"""
        nft_id: builtins.str
        """"""
        region: Optional["Member.Member_Region"] = None
        """NFT地区"""

    mid: builtins.int
    """用户mid"""
    name: builtins.str
    """昵称"""
    sex: builtins.str
    """性别"""
    face: builtins.str
    """头像url"""
    level: builtins.int
    """等级"""
    official_verify_type: builtins.int
    """认证类型
    *********VIP相关*********
    """
    vip_type: builtins.int
    """会员类型
    0:不是大会员 1:月度会员 2:年度大会员
    """
    vip_status: builtins.int
    """会员状态"""
    vip_theme_type: builtins.int
    """会员样式"""
    vip_label_path: builtins.str
    """会员铭牌样式url
    *********装扮相关*********
    """
    garb_pendant_image: builtins.str
    """头像框url"""
    garb_card_image: builtins.str
    """装扮卡url"""
    garb_card_image_with_focus: builtins.str
    """有关注按钮时的装扮卡url"""
    garb_card_jump_url: builtins.str
    """专属装扮页面url"""
    garb_card_number: builtins.str
    """专属装扮id"""
    garb_card_fan_color: builtins.str
    """专属装扮id显示颜色"""
    garb_card_is_fan: builtins.bool
    """是否为专属装扮卡
    *********粉丝勋章相关*********
    """
    fans_medal_name: builtins.str
    """粉丝勋章名"""
    fans_medal_level: builtins.int
    """粉丝勋章等级"""
    fans_medal_color: builtins.int
    """粉丝勋章显示颜色"""
    vip_nickname_color: builtins.str
    """会员昵称颜色"""
    vip_avatar_subscript: builtins.int
    """会员角标
    0:无角标 1:粉色大会员角标 2:绿色小会员角标
    """
    vip_label_text: builtins.str
    """会员标签文"""
    vip_label_theme: builtins.str
    """会员标颜色"""
    fans_medal_color_end: builtins.int
    """粉丝勋章底色"""
    fans_medal_color_border: builtins.int
    """粉丝勋章边框颜色"""
    fans_medal_color_name: builtins.int
    """粉丝勋章名颜色"""
    fans_medal_color_level: builtins.int
    """粉丝勋章等级颜色"""
    fans_guard_level: builtins.int
    """"""
    face_nft: builtins.int
    """"""
    face_nft_new: builtins.int
    """是否NFT头像"""
    is_senior_member: builtins.int
    """是否为硬核会员"""
    nft_interaction: Optional["Member_NftInteraction"] = None
    """NFT信息"""
    fans_guard_icon: builtins.str
    """"""
    fans_honor_icon: builtins.str
    """"""


class MemberV2(BaseModel):
    """用户信息V2"""

    class MemberV2_RegionType(str, Enum):
        DEFAULT = 'DEFAULT'
        """默认"""
        MAINLAND = 'MAINLAND'
        """大陆地区"""
        GAT = 'GAT'
        """"""

    """默认"""
    """大陆地区"""
    """"""

    class MemberV2_ShowStatus(str, Enum):
        SHOWDEFAULT = 'SHOWDEFAULT'
        """"""
        ZOOMINMAINLAND = 'ZOOMINMAINLAND'
        """"""
        RAW = 'RAW'
        """"""

    """"""
    """"""
    """"""

    class MemberV2_Basic(BaseModel):
        """基本信息"""

        mid: builtins.int
        """用户mid"""
        name: builtins.str
        """昵称"""
        sex: builtins.str
        """性别"""
        face: builtins.str
        """头像url"""
        level: builtins.int
        """等级"""

    class MemberV2_Official(BaseModel):
        """认证"""

        verify_type: builtins.int
        """认证类型"""

    class MemberV2_Vip(BaseModel):
        """大会员"""

        type: builtins.int
        """会员类型
            0:不是大会员 1:月度会员 2:年度大会员
            """
        status: builtins.int
        """会员状态"""
        theme_type: builtins.int
        """会员样式"""
        label_path: builtins.str
        """会员铭牌样式url"""
        nickname_color: builtins.str
        """"""
        avatar_subscript: builtins.int
        """"""
        label_text: builtins.str
        """"""
        vip_label_theme: builtins.str
        """"""

    class MemberV2_Garb(BaseModel):
        """装扮"""

        pendant_image: builtins.str
        """头像框url"""
        card_image: builtins.str
        """装扮卡url"""
        card_image_with_focus: builtins.str
        """有关注按钮时的装扮卡url"""
        card_jump_url: builtins.str
        """专属装扮页面url"""
        card_number: builtins.str
        """专属装扮id"""
        card_fan_color: builtins.str
        """专属装扮id显示颜色"""
        card_is_fan: builtins.bool
        """是否为专属装扮卡"""

    class MemberV2_Medal(BaseModel):
        """粉丝勋章"""

        name: builtins.str
        """粉丝勋章名"""
        level: builtins.int
        """粉丝勋章等级"""
        color_start: builtins.int
        """粉丝勋章显示颜色"""
        color_end: builtins.int
        """粉丝勋章底色"""
        color_border: builtins.int
        """粉丝勋章边框颜色"""
        color_name: builtins.int
        """粉丝勋章名颜色"""
        color_level: builtins.int
        """粉丝勋章等级颜色"""
        guard_level: builtins.int
        """"""
        first_icon: builtins.str
        """"""
        level_bg_color: builtins.int
        """"""

    class MemberV2_Region(BaseModel):
        """NFT地区"""

        type: "MemberV2.MemberV2_RegionType"
        """地区类型"""
        icon: builtins.str
        """角标url"""
        show_status: "MemberV2.MemberV2_ShowStatus"
        """"""

    class MemberV2_Interaction(BaseModel):
        """NFT信息"""

        itype: builtins.str
        """"""
        metadata_url: builtins.str
        """"""
        nft_id: builtins.str
        """"""
        region: Optional["MemberV2.MemberV2_Region"] = None
        """NFT地区"""

    class MemberV2_Nft(BaseModel):
        """NFT"""

        face: builtins.int
        """"""
        interaction: Optional["MemberV2.MemberV2_Interaction"] = None
        """"""

    class MemberV2_Senior(BaseModel):
        """硬核会员"""

        is_senior_member: builtins.int
        """是否为硬核会员"""

    class MemberV2_Contractor(BaseModel):
        """契约"""

        is_contractor: builtins.bool
        """是否和up签订契约"""
        contract_desc: builtins.str
        """契约显示文案"""

    basic: Optional["MemberV2_Basic"] = None
    """基本信息"""
    official: Optional["MemberV2_Official"] = None
    """认证信息"""
    vip: Optional["MemberV2_Vip"] = None
    """大会员信息"""
    garb: Optional["MemberV2_Garb"] = None
    """装扮信息"""
    medal: Optional["MemberV2_Medal"] = None
    """粉丝勋章信息"""
    nft: Optional["MemberV2_Nft"] = None
    """NFT信息"""
    senior: Optional["MemberV2_Senior"] = None
    """硬核会员信息"""
    contractor: Optional["MemberV2_Contractor"] = None
    """契约信息"""


class Notice(BaseModel):
    """"""

    id: builtins.int
    """"""
    content: builtins.str
    """"""
    link: builtins.str
    """"""


class Operation(BaseModel):
    """"""

    type: builtins.int
    """"""
    id: builtins.int
    """"""
    title: Optional["OperationTitle"] = None
    """"""
    subtitle: Optional["OperationTitle"] = None
    """"""
    link: builtins.str
    """"""
    report_extra: builtins.str
    """"""
    icon: builtins.str
    """"""


class OperationTitle(BaseModel):
    """"""

    content: builtins.str
    """"""
    is_highlight: builtins.bool
    """"""


class PGCVideoSearchItem(BaseModel):
    """PGC视频项目"""

    title: builtins.str
    """标题"""
    category: builtins.str
    """类别"""
    cover: builtins.str
    """封面"""


class PreviewListReply(BaseModel):
    """评论区预览-回复"""

    cursor: Optional["CursorReply"] = None
    """页面游标"""
    replies: "List[ReplyInfo]"
    """评论列表"""
    subject_control: Optional["SubjectControl"] = None
    """评论区显示控制字段"""
    upTop: Optional["ReplyInfo"] = None
    """UP置顶评论"""
    admin_top: Optional["ReplyInfo"] = None
    """管理员置顶评论"""
    vote_top: Optional["ReplyInfo"] = None
    """投票置顶评论"""


class PreviewListReq(BaseModel):
    """评论区预览-请求"""

    oid: builtins.int
    """目标评论区id"""
    type: builtins.int
    """目标评论区业务type"""
    cursor: Optional["CursorReq"] = None
    """页面游标"""


class QoeInfo(BaseModel):
    """"""

    id: builtins.int
    """"""
    type: builtins.int
    """"""
    style: builtins.int
    """"""
    title: builtins.str
    """"""
    feedback_title: builtins.str
    """"""
    score_items: "List[QoeScoreItem]"
    """"""
    display_rank: builtins.int
    """"""


class QoeScoreItem(BaseModel):
    """"""

    title: builtins.str
    """"""
    url: builtins.str
    """"""
    score: builtins.float
    """"""


class ReplyCardLabel(BaseModel):
    """评论条目标签信息"""

    text_content: builtins.str
    """标签文本"""
    text_color_day: builtins.str
    """文本颜色"""
    text_color_night: builtins.str
    """文本颜色夜间"""
    label_color_day: builtins.str
    """标签颜色"""
    label_color_night: builtins.str
    """标签颜色夜间"""
    image: builtins.str
    """"""
    type: builtins.int
    """标签类型 0:UP主觉得很赞 1:妙评"""
    background: builtins.str
    """背景url"""
    background_width: builtins.float
    """背景宽"""
    background_height: builtins.float
    """背景高"""
    jump_url: builtins.str
    """点击跳转url"""
    effect: builtins.int
    """"""
    effect_start_time: builtins.int
    """"""


class ReplyControl(BaseModel):
    """评论条目控制字段"""

    action: builtins.int
    """操作行为标志
    0:无 1:已点赞 2:已点踩
    """
    up_like: builtins.bool
    """是否UP觉得很赞"""
    up_reply: builtins.bool
    """是否存在UP回复"""
    show_follow_btn: builtins.bool
    """是否显示关注按钮"""
    is_assist: builtins.bool
    """是否协管"""
    label_text: builtins.str
    """是否展示标签"""
    following: builtins.bool
    """是否关注"""
    followed: builtins.bool
    """是否粉丝"""
    blocked: builtins.bool
    """是否被自己拉黑"""
    has_folded_reply: builtins.bool
    """是否存在折叠的二级评论"""
    is_folded_reply: builtins.bool
    """是否折叠"""
    is_up_top: builtins.bool
    """是否UP置顶"""
    is_admin_top: builtins.bool
    """是否管理置顶"""
    is_vote_top: builtins.bool
    """是否置顶投票评论"""
    max_line: builtins.int
    """最大收起显示行数"""
    invisible: builtins.bool
    """该条评论可不可见"""
    is_contractor: builtins.bool
    """是否和up签订契约"""
    is_note: builtins.bool
    """是否是笔记评论"""
    card_labels: "List[ReplyCardLabel]"
    """评论条目标签列表"""
    sub_reply_entry_text: builtins.str
    """子评论数文案 "共x条回复" """
    sub_reply_title_text: builtins.str
    """子评论数文案 "相关回复共x条" """
    contract_desc: builtins.str
    """契约显示文案"""
    time_desc: builtins.str
    """发布时间文案 "x天前发布" """
    biz_scene: builtins.str
    """"""
    location: builtins.str
    """IP属地信息 "IP属地：xxx" """


class ReplyExtra(BaseModel):
    """"""

    season_id: builtins.int
    """"""
    season_type: builtins.int
    """"""
    ep_id: builtins.int
    """"""
    is_story: builtins.bool
    """"""


class ReplyInfo(BaseModel):
    """评论条目信息"""

    replies: "List[ReplyInfo]"
    """二级评论列表"""
    id: builtins.int
    """评论rpid"""
    oid: builtins.int
    """评论区对象id"""
    type: builtins.int
    """评论区类型"""
    mid: builtins.int
    """发布者UID"""
    root: builtins.int
    """根评论rpid"""
    parent: builtins.int
    """父评论rpid"""
    dialog: builtins.int
    """对话评论rpid"""
    like: builtins.int
    """点赞数"""
    ctime: builtins.int
    """发布时间"""
    count: builtins.int
    """回复数"""
    content: Optional["Content"] = None
    """评论主体信息"""
    member: Optional["Member"] = None
    """发布者信息"""
    reply_control: Optional["ReplyControl"] = None
    """评论控制字段"""
    member_v2: Optional["MemberV2"] = None
    """发布者信息V2"""


class ReplyInfoReply(BaseModel):
    """查询单条评论-响应"""

    reply: Optional["ReplyInfo"] = None
    """评论条目信息"""


class ReplyInfoReq(BaseModel):
    """查询单条评论-请求"""

    rpid: builtins.int
    """评论rpid"""
    scene: builtins.int
    """"""


class RichText(BaseModel):
    """富文本"""

    note: Optional["RichTextNote"] = None
    """笔记"""


class RichTextNote(BaseModel):
    """笔记"""

    summary: builtins.str
    """预览文本"""
    images: List[builtins.str]
    """笔记预览图片url列表"""
    click_url: builtins.str
    """笔记页面url"""
    last_mtime_text: builtins.str
    """发布日期 YYYY-mm-dd"""


class SearchItem(BaseModel):
    """评论搜索插入项目"""

    url: builtins.str
    """"""
    goods: Optional["GoodsSearchItem"] = None
    """商品"""
    video: Optional["VideoSearchItem"] = None
    """视频"""
    article: Optional["ArticleSearchItem"] = None
    """专栏"""


class SearchItemCursorReply(BaseModel):
    """评论搜索插入项目响应游标"""

    has_next: builtins.bool
    """是否有下一页"""
    next: builtins.int
    """下页"""


class SearchItemCursorReq(BaseModel):
    """评论搜索插入项目请求游标"""

    next: builtins.int
    """下一页"""
    item_type: SearchItemType
    """tab类型"""


class SearchItemPreHookReply(BaseModel):
    """评论搜索item前置发布-响应"""

    placeholder_text: builtins.str
    """输入框的文案"""
    background_text: builtins.str
    """背景空白的时候的文案"""
    ordered_type: "List[SearchItemType]"
    """有权限的tab栏的顺序"""


class SearchItemPreHookReq(BaseModel):
    """评论搜索item前置发布-请求"""

    oid: builtins.int
    """目标评论区id"""
    type: builtins.int
    """目标评论区业务type"""


class SearchItemReply(BaseModel):
    """评论搜索插入项目-回复"""

    cursor: Optional["SearchItemCursorReply"] = None
    """"""
    items: "List[SearchItem]"
    """搜索的结果"""
    extra: Optional["SearchItemReplyExtraInfo"] = None
    """附加信息"""


class SearchItemReplyExtraInfo(BaseModel):
    """"""

    event_id: builtins.str
    """"""


class SearchItemReq(BaseModel):
    """评论搜索插入项目-请求"""

    cursor: Optional["SearchItemCursorReq"] = None
    """页面游标"""
    oid: builtins.int
    """目标评论区id"""
    type: builtins.int
    """目标评论区业务type"""
    keyword: builtins.str
    """搜索关键词"""


class ShareRepliesInfoReq(BaseModel):
    """评论分享材料-请求"""

    rpids: List[builtins.int]
    """评论rpid列表"""
    oid: builtins.int
    """目标评论区id"""
    type: builtins.int
    """目标评论区业务type"""


class ShareRepliesInfoResp(BaseModel):
    """评论分享材料-响应"""

    class ShareRepliesInfoResp_ShareExtra(BaseModel):
        """"""

        is_pgc: builtins.bool
        """"""

    infos: "List[ShareReplyInfo]"
    """评论分享条目列表"""
    from_title: builtins.str
    """源内容标题"""
    from_up: builtins.str
    """源内容UP主"""
    from_pic: builtins.str
    """源内容封面url"""
    url: builtins.str
    """源内容页面url"""
    slogan_pic: builtins.str
    """logo url"""
    slogan_text: builtins.str
    """标语"""
    topic: Optional["ShareReplyTopic"] = None
    """"""
    extra: Optional["ShareRepliesInfoResp_ShareExtra"] = None
    """"""


class ShareReplyInfo(BaseModel):
    """评论分享条目信息"""

    member: Optional["Member"] = None
    """用户信息"""
    content: Optional["Content"] = None
    """评论主体信息"""
    title: builtins.str
    """分享标题(评论发布者昵称)"""
    sub_title: builtins.str
    """分享副标题 "发表了评论" """
    achievement_text: builtins.str
    """荣誉信息文案 "获得了up主点赞" """
    label_url: builtins.str
    """"""


class ShareReplyTopic(BaseModel):
    """"""

    topic: Optional["Topic"] = None
    """"""
    origin_text: builtins.str
    """"""


class SubjectControl(BaseModel):
    """评论区控制字段"""

    class SubjectControl_FilterTag(BaseModel):
        """评论区筛选类型"""

        name: builtins.str
        """类型名"""
        event_id: builtins.str
        """"""

    up_mid: builtins.int
    """UP主mid"""
    is_assist: builtins.bool
    """自己是否为协管"""
    read_only: builtins.bool
    """是否只读"""
    has_vote_access: builtins.bool
    """是否有发起投票权限"""
    has_lottery_access: builtins.bool
    """是否有发起抽奖权限"""
    has_folded_reply: builtins.bool
    """是否有被折叠评论"""
    bg_text: builtins.str
    """空评论区背景文案"""
    up_blocked: builtins.bool
    """是否被UP拉黑"""
    has_activity_access: builtins.bool
    """是否有发起活动权限"""
    show_title: builtins.bool
    """标题展示控制"""
    show_up_action: builtins.bool
    """是否显示UP主操作标志"""
    switcher_type: builtins.int
    """是否显示评论区排序切换按钮"""
    input_disable: builtins.bool
    """是否禁止输入框"""
    root_text: builtins.str
    """根评论输入框背景文案"""
    child_text: builtins.str
    """子评论输入框背景文案"""
    count: builtins.int
    """评论总数"""
    title: builtins.str
    """评论区标题"""
    giveup_text: builtins.str
    """离开态输入框的文案"""
    has_note_access: builtins.bool
    """是否允许笔记"""
    disable_jump_emote: builtins.bool
    """"""
    empty_background_text_plain: builtins.str
    """"""
    empty_background_text_highlight: builtins.str
    """"""
    empty_background_uri: builtins.str
    """"""
    support_filter_tags: "List[SubjectControl_FilterTag]"
    """评论区筛选类型列表"""


class SuggestEmotesReq(BaseModel):
    """评论表情推荐列表-请求"""

    oid: builtins.int
    """目标评论区id"""
    type: builtins.int
    """目标评论区业务type"""


class SuggestEmotesResp(BaseModel):
    """评论表情推荐列表-响应"""

    emotes: "List[Emote]"
    """表情推荐列表"""


class Topic(BaseModel):
    """话题项"""

    link: builtins.str
    """跳转url"""
    id: builtins.int
    """话题id"""


class UGCVideoSearchItem(BaseModel):
    """UGC视频项目"""

    title: builtins.str
    """标题"""
    up_nickname: builtins.str
    """UP主昵称"""
    duration: builtins.int
    """时长(单位为秒)"""
    cover: builtins.str
    """封面"""


class UpSelection(BaseModel):
    """精选评论"""

    pending_count: builtins.int
    """待审评论数"""
    ignore_count: builtins.int
    """忽略评论数"""


class Url(BaseModel):
    """超链项"""

    class Url_Extra(BaseModel):
        """扩展字段"""

        goods_item_id: builtins.int
        """"""
        goods_prefetched_cache: builtins.str
        """"""
        goods_show_type: builtins.int
        """"""
        is_word_search: builtins.bool
        """热词搜索"""
        goods_cm_control: builtins.int
        """"""

    title: builtins.str
    """标题"""
    state: builtins.int
    """"""
    prefix_icon: builtins.str
    """图标url"""
    app_url_schema: builtins.str
    """客户端内跳转uri"""
    app_name: builtins.str
    """"""
    app_package_name: builtins.str
    """"""
    click_report: builtins.str
    """点击上报数据"""
    is_half_screen: builtins.bool
    """是否半屏打开"""
    exposure_report: builtins.str
    """展现上报数据"""
    extra: Optional["Url_Extra"] = None
    """扩展字段"""
    underline: builtins.bool
    """是否下划线"""
    match_once: builtins.bool
    """"""
    pc_url: builtins.str
    """网页url"""
    icon_position: builtins.int
    """"""


class UserCallbackReply(BaseModel):
    """用户回调上报-响应"""


class UserCallbackReq(BaseModel):
    """用户回调上报-请求"""

    mid: builtins.int
    """用户mid"""
    scene: UserCallbackScene
    """"""
    action: UserCallbackAction
    """"""
    oid: builtins.int
    """目标评论区id"""
    type: builtins.int
    """目标评论区业务type"""


class VideoSearchItem(BaseModel):
    """视频项目"""

    type: SearchItemVideoSubType
    """"""
    ugc: Optional["UGCVideoSearchItem"] = None
    """UGC视频"""
    pgc: Optional["PGCVideoSearchItem"] = None
    """PGC视频"""


class Vote(BaseModel):
    """投票信息"""

    id: builtins.int
    """投票id"""
    title: builtins.str
    """投票标题"""
    count: builtins.int
    """参与人数"""


CursorReq.update_forward_refs()
ReplyInfo.update_forward_refs()
PreviewListReply.update_forward_refs()
UpSelection.update_forward_refs()
SearchItemCursorReq.update_forward_refs()
Lottery.update_forward_refs()
MainListReq.update_forward_refs()
MemberV2.MemberV2_Basic.update_forward_refs()
SearchItemReplyExtraInfo.update_forward_refs()
ShareRepliesInfoResp.update_forward_refs()
RichText.update_forward_refs()
GoodsSearchItem.update_forward_refs()
ReplyCardLabel.update_forward_refs()
Member.update_forward_refs()
Emote.update_forward_refs()
ArticleSearchItem.update_forward_refs()
AtItem.update_forward_refs()
CursorReply.update_forward_refs()
AtSearchReq.update_forward_refs()
LikeInfo.update_forward_refs()
DialogListReply.update_forward_refs()
ReplyInfoReq.update_forward_refs()
ShareReplyInfo.update_forward_refs()
PreviewListReq.update_forward_refs()
Url.Url_Extra.update_forward_refs()
MainListReply.update_forward_refs()
SearchItemCursorReply.update_forward_refs()
SearchItemReply.update_forward_refs()
ReplyExtra.update_forward_refs()
ReplyControl.update_forward_refs()
QoeInfo.update_forward_refs()
ReplyInfoReply.update_forward_refs()
SuggestEmotesReq.update_forward_refs()
MemberV2.MemberV2_Nft.update_forward_refs()
Member.Member_NftInteraction.update_forward_refs()
OperationTitle.update_forward_refs()
Content.update_forward_refs()
SearchItemPreHookReply.update_forward_refs()
UserCallbackReply.update_forward_refs()
ShareRepliesInfoResp.ShareRepliesInfoResp_ShareExtra.update_forward_refs()
MemberV2.update_forward_refs()
ShareRepliesInfoReq.update_forward_refs()
PGCVideoSearchItem.update_forward_refs()
ShareReplyTopic.update_forward_refs()
Url.update_forward_refs()
Activity.update_forward_refs()
DetailListReq.update_forward_refs()
SubjectControl.update_forward_refs()
MemberV2.MemberV2_Contractor.update_forward_refs()
Topic.update_forward_refs()
RichTextNote.update_forward_refs()
MemberV2.MemberV2_Vip.update_forward_refs()
MemberV2.MemberV2_Garb.update_forward_refs()
SearchItemReq.update_forward_refs()
UGCVideoSearchItem.update_forward_refs()
SearchItemPreHookReq.update_forward_refs()
DialogListReq.update_forward_refs()
MemberV2.MemberV2_Senior.update_forward_refs()
QoeScoreItem.update_forward_refs()
MemberV2.MemberV2_Medal.update_forward_refs()
VideoSearchItem.update_forward_refs()
AtGroup.update_forward_refs()
UserCallbackReq.update_forward_refs()
MemberV2.MemberV2_Official.update_forward_refs()
SearchItem.update_forward_refs()
SuggestEmotesResp.update_forward_refs()
Vote.update_forward_refs()
Notice.update_forward_refs()
CM.update_forward_refs()
DetailListReply.update_forward_refs()
Effects.update_forward_refs()
Operation.update_forward_refs()
AtSearchReply.update_forward_refs()

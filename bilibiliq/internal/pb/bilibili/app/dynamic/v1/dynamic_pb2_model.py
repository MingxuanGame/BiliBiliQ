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


class BgType(str, Enum):
    """"""

    bg_type_default = 'bg_type_default'
    """"""
    bg_type_face = 'bg_type_face'
    """"""


class CornerType(str, Enum):
    """"""

    corner_type_none = 'corner_type_none'
    """"""
    corner_type_text = 'corner_type_text'
    """"""
    corner_type_animation = 'corner_type_animation'
    """"""


class FoldType(str, Enum):
    """折叠分类"""

    FoldTypeZero = 'FoldTypeZero'
    """占位"""
    FoldTypePublish = 'FoldTypePublish'
    """用户发布折叠"""
    FoldTypeFrequent = 'FoldTypeFrequent'
    """转发超频折叠"""
    FoldTypeUnite = 'FoldTypeUnite'
    """联合投稿折叠"""
    FoldTypeLimit = 'FoldTypeLimit'
    """动态受限折叠"""


class MediaType(str, Enum):
    """播放器类型"""

    MediaTypeNone = 'MediaTypeNone'
    """本地"""
    MediaTypeUGC = 'MediaTypeUGC'
    """UGC"""
    MediaTypePGC = 'MediaTypePGC'
    """PGC"""
    MediaTypeLive = 'MediaTypeLive'
    """直播"""
    MediaTypeVCS = 'MediaTypeVCS'
    """小视频"""


class RelationStatus(str, Enum):
    """关注状态"""

    relation_status_none = 'relation_status_none'
    """"""
    relation_status_nofollow = 'relation_status_nofollow'
    """未关注"""
    relation_status_follow = 'relation_status_follow'
    """关注"""
    relation_status_followed = 'relation_status_followed'
    """被关注"""
    relation_status_mutual_concern = 'relation_status_mutual_concern'
    """互相关注"""
    relation_status_special = 'relation_status_special'
    """特别关注"""


class StyleType(str, Enum):
    """"""

    STYLE_TYPE_NONE = 'STYLE_TYPE_NONE'
    """"""
    STYLE_TYPE_LIVE = 'STYLE_TYPE_LIVE'
    """"""
    STYLE_TYPE_DYN_UP = 'STYLE_TYPE_DYN_UP'
    """"""


class SVideoType(str, Enum):
    """入口联播页类型"""

    TypeNone = 'TypeNone'
    """无类型"""
    TypeDynamic = 'TypeDynamic'
    """动态"""
    TypePopularIndex = 'TypePopularIndex'
    """热门分类"""
    TypePopularHotword = 'TypePopularHotword'
    """热点聚合"""


class VideoSubType(str, Enum):
    """番剧类型"""

    VideoSubTypeNone = 'VideoSubTypeNone'
    """没有子类型"""
    VideoSubTypeBangumi = 'VideoSubTypeBangumi'
    """番剧"""
    VideoSubTypeMovie = 'VideoSubTypeMovie'
    """电影"""
    VideoSubTypeDocumentary = 'VideoSubTypeDocumentary'
    """纪录片"""
    VideoSubTypeDomestic = 'VideoSubTypeDomestic'
    """国创"""
    VideoSubTypeTeleplay = 'VideoSubTypeTeleplay'
    """电视剧"""


class AddressComponent(BaseModel):
    """地址部件"""

    nation: builtins.str
    """国家"""
    province: builtins.str
    """省"""
    city: builtins.str
    """市"""
    district: builtins.str
    """区，可能为空字串"""
    street: builtins.str
    """街道，可能为空字串"""
    street_number: builtins.str
    """门牌，可能为空字串"""


class AdInfo(BaseModel):
    """行政区划信息"""

    nation_code: builtins.str
    """国家代码(ISO3166标准3位数字码)"""
    adcode: builtins.str
    """行政区划代码，规则详见：行政区划代码说明"""
    city_code: builtins.str
    """城市代码，由国家码+行政区划代码(提出城市级别)组合而来，总共为9位"""
    name: builtins.str
    """行政区划名称"""
    gps: Optional["Gps"] = None
    """行政区划中心点坐标"""


class CardCurrBatch(BaseModel):
    """付费课程批次卡"""

    title: builtins.str
    """标题"""
    cover: builtins.str
    """封面图"""
    uri: builtins.str
    """跳转地址"""
    text_1: builtins.str
    """展示项 1(本集标题)"""
    text_2: builtins.str
    """展示项 2(更新了多少个视频)"""
    badge: Optional["VideoBadge"] = None
    """角标"""


class CardCurrSeason(BaseModel):
    """付费课程系列卡"""

    title: builtins.str
    """标题"""
    cover: builtins.str
    """封面图"""
    uri: builtins.str
    """跳转地址"""
    text_1: builtins.str
    """展示项 1(更新信息)"""
    desc: builtins.str
    """描述信息"""
    badge: Optional["VideoBadge"] = None
    """角标"""


class CardPGC(BaseModel):
    """PGC视频卡片数据"""

    title: builtins.str
    """标题"""
    cover: builtins.str
    """封面图"""
    uri: builtins.str
    """秒开地址"""
    cover_left_text_1: builtins.str
    """视频封面展示项 1"""
    cover_left_text_2: builtins.str
    """视频封面展示项 2"""
    cover_left_text_3: builtins.str
    """封面视频展示项 3"""
    cid: builtins.int
    """cid"""
    season_id: builtins.int
    """season_id"""
    epid: builtins.int
    """epid"""
    aid: builtins.int
    """aid"""
    media_type: MediaType
    """视频源类型"""
    sub_type: VideoSubType
    """番剧类型"""
    is_preview: builtins.int
    """番剧是否为预览视频 0:否，1:是"""
    dimension: Optional["Dimension"] = None
    """尺寸信息"""
    badge: "List[VideoBadge]"
    """角标"""
    can_play: builtins.int
    """是否能够自动播放"""
    season: Optional["PGCSeason"] = None
    """PGC单季信息"""


class CardUGC(BaseModel):
    """UGC视频卡片数据"""

    title: builtins.str
    """标题"""
    cover: builtins.str
    """封面图"""
    uri: builtins.str
    """秒开地址"""
    cover_left_text_1: builtins.str
    """视频封面展示项 1"""
    cover_left_text_2: builtins.str
    """视频封面展示项 2"""
    cover_left_text_3: builtins.str
    """封面视频展示项 3"""
    avid: builtins.int
    """avid"""
    cid: builtins.int
    """cid"""
    media_type: MediaType
    """视频源类型"""
    dimension: Optional["Dimension"] = None
    """尺寸信息"""
    badge: "List[VideoBadge]"
    """角标"""
    can_play: builtins.int
    """是否能够自动播放"""


class DecoCardFan(BaseModel):
    """粉丝样式"""

    is_fan: builtins.int
    """是否是粉丝"""
    number: builtins.int
    """数量"""
    color: builtins.str
    """颜色"""


class DecorateCard(BaseModel):
    """装扮卡片"""

    id: builtins.int
    """装扮卡片id"""
    card_url: builtins.str
    """装扮卡片链接"""
    jump_url: builtins.str
    """装扮卡片点击跳转链接"""
    fan: Optional["DecoCardFan"] = None
    """粉丝样式"""


class Description(BaseModel):
    """文本描述"""

    text: builtins.str
    """文本内容"""
    type: builtins.str
    """文本类型"""
    uri: builtins.str
    """点击跳转链接"""
    emoji_type: builtins.str
    """emoji类型"""
    goods_type: builtins.str
    """商品类型"""


class Dimension(BaseModel):
    """尺寸信息"""

    height: builtins.int
    """"""
    width: builtins.int
    """"""
    rotate: builtins.int
    """"""


class DynamicItem(BaseModel):
    """动态卡片项"""

    card_type: builtins.str
    """卡片类型
    forward:转发 av:稿件视频 fold:折叠 pgc:pgc内容 courses:付费视频 upList:最近访问列表 followList:我的追番列表
    """
    item_type: builtins.str
    """转发类型下，items的类型"""
    modules: "List[Module]"
    """模块内容"""
    dyn_id_str: builtins.str
    """动态ID str"""
    orig_dyn_id_str: builtins.str
    """转发动态ID str"""
    r_type: builtins.int
    """r_type"""
    has_fold: builtins.int
    """该卡片下面是否含有折叠卡"""


class DynDetailsReply(BaseModel):
    """批量动态id获取动态详情返回值"""

    list: "List[DynamicItem]"
    """动态列表"""


class DynDetailsReq(BaseModel):
    """批量动态id获取动态详情请求参数"""

    teenagers_mode: builtins.int
    """青少年模式"""
    dynamic_ids: builtins.str
    """动态id"""
    qn: builtins.int
    """清晰度"""
    fnver: builtins.int
    """流版本"""
    fnval: builtins.int
    """流功能"""
    force_host: builtins.int
    """是否强制使用域名"""
    fourk: builtins.int
    """是否4k"""


class DynMixUpListSearchReply(BaseModel):
    """查看更多-搜索-响应"""

    items: "List[MixUpListItem]"
    """"""


class DynMixUpListSearchReq(BaseModel):
    """查看更多-搜索-请求"""

    name: builtins.str
    """"""


class DynMixUpListViewMoreReply(BaseModel):
    """查看更多-列表-响应"""

    items: "List[MixUpListItem]"
    """关注up主列表信息"""
    search_default_text: builtins.str
    """默认搜索文案"""


class DynOurCityItem(BaseModel):
    """动态同城物料"""

    card_type: builtins.str
    """卡片类型
    av:稿件 draw:图文
    """
    dyn_id: builtins.int
    """动态ID"""
    uri: builtins.str
    """跳转地址"""
    modules: "List[DynOurCityModule]"
    """模块列表"""
    rid: builtins.int
    """资源ID"""
    debug_info: builtins.str
    """透传服务端魔镜参数"""


class DynOurCityModule(BaseModel):
    """动态同城物料模块"""

    module_type: builtins.str
    """类型
    cover:封面 desc:描述 author:发布人 extend:扩展部分
    """
    module_cover: Optional["DynOurCityModuleCover"] = None
    """封面"""
    module_desc: Optional["DynOurCityModuleDesc"] = None
    """描述"""
    module_author: Optional["DynOurCityModuleAuthor"] = None
    """发布人"""
    module_extend: Optional["DynOurCityModuleExtend"] = None
    """扩展部分"""


class DynOurCityModuleAuthor(BaseModel):
    """动态同城物料-发布人模块"""

    mid: builtins.int
    """用户Mid"""
    name: builtins.str
    """用户昵称"""
    face: builtins.str
    """用户头像"""
    uri: builtins.str
    """跳转地址"""


class DynOurCityModuleCover(BaseModel):
    """动态同城物料-封面模块"""

    covers: List[builtins.str]
    """封面图 单图样式取第一个元素"""
    style: builtins.int
    """封面样式
    1:横图 2:竖图 3:方图
    """
    cover_left_icon_1: builtins.int
    """视频封面展示项图标 1"""
    cover_left_text_1: builtins.str
    """视频封面展示项 1"""
    cover_left_icon_2: builtins.int
    """视频封面展示项图标 2"""
    cover_left_text_2: builtins.str
    """视频封面展示项 2"""
    cover_left_text_3: builtins.str
    """封面视频展示项 3"""
    badge: "List[VideoBadge]"
    """角标"""


class DynOurCityModuleDesc(BaseModel):
    """动态同城物料-描述模块"""

    desc: builtins.str
    """描述信息"""


class DynOurCityModuleExtend(BaseModel):
    """动态同城物料-扩展部分模块"""

    type: builtins.str
    """类型"""
    extend_lbs: Optional["DynOurCityModuleExtendLBS"] = None
    """LBS模块"""


class DynOurCityModuleExtendLBS(BaseModel):
    """动态同城物料extent-LBS模块"""

    title: builtins.str
    """标题"""
    uri: builtins.str
    """跳转地址"""
    icon: builtins.str
    """小图标"""
    poi_type: builtins.int
    """poiType"""


class DynOurCityReply(BaseModel):
    """动态同城-响应"""

    offset: builtins.str
    """翻页游标"""
    has_more: builtins.int
    """是否还有更多数据
    1:有
    """
    style: builtins.int
    """样式类型
    1:双列 2:瀑布流
    """
    top_label: builtins.str
    """顶导信息"""
    list: "List[DynOurCityItem]"
    """列表详情"""
    top_button_label: builtins.str
    """顶导按钮信息"""
    city_id: builtins.int
    """城市ID"""
    city_name: builtins.str
    """城市名"""


class DynOurCityReq(BaseModel):
    """动态同城页-请求"""

    city_id: builtins.int
    """城市ID"""
    lat: builtins.float
    """纬度"""
    lng: builtins.float
    """经度"""
    offset: builtins.str
    """透传上一次接口请求返回的offset"""
    page_size: builtins.int
    """每页元素个数"""
    teenagers_mode: builtins.int
    """青少年模式
    1:开启青少年模式
    """
    qn: builtins.int
    """清晰度(旧版)"""
    fnver: builtins.int
    """流版本(旧版)"""
    fnval: builtins.int
    """流类型(旧版)"""
    force_host: builtins.int
    """是否强制使用域名(旧版)"""
    fourk: builtins.int
    """是否4k(旧版)"""
    lbs_state: builtins.int
    """是否开启lbs
    0:关闭 1:开启
    """
    refresh_city: builtins.int
    """是否刷新城市"""
    exp_conf: Optional["ExpConf"] = None
    """魔镜设置"""
    player_args: bilibiliq.internal.pb.bilibili.app.archive.middleware.v1.preload_pb2_model.PlayerArgs
    """秒开参数"""
    city_code: builtins.int
    """城市码"""
    build_time: builtins.int
    """构建时间"""


class DynOurCitySwitchReq(BaseModel):
    """动态同城开关-请求"""

    switch: builtins.int
    """开关参数
    0:关闭 1:开启
    """


class DynRedItem(BaseModel):
    """红点接口物料"""

    count: builtins.int
    """数字红点有效 更新数"""


class DynRedReply(BaseModel):
    """红点接口-响应"""

    red_type: builtins.str
    """类型
    count:数字红点 point:普通红点 no_point:没有红点
    """
    dyn_red_item: Optional["DynRedItem"] = None
    """红点具体信息"""
    default_tab: builtins.str
    """默认tab 值对应tab接口下发的anchor"""
    red_style: Optional["DynRedStyle"] = None
    """"""


class DynRedReq(BaseModel):
    """动态红点接口-请求"""

    tab_offset: "List[TabOffset]"
    """动态红点接口各tab offset信息"""


class DynRedStyle(BaseModel):
    """"""

    bg_type: builtins.int
    """"""
    corner_type: builtins.int
    """"""
    display_time: builtins.int
    """"""
    corner_mark: builtins.str
    """"""
    up: Optional["DynRedStyleUp"] = None
    """"""
    type: builtins.int
    """"""


class DynRedStyleUp(BaseModel):
    """"""

    uid: builtins.int
    """"""
    face: builtins.str
    """"""


class DynTab(BaseModel):
    """动态tab详情"""

    title: builtins.str
    """tab标题 优先展示用,未开启状态第一次请求返回同城,后续请求返回对应城市名"""
    uri: builtins.str
    """跳转链接"""
    bubble: builtins.str
    """气泡内容"""
    red_point: builtins.int
    """是否推红点"""
    city_id: builtins.int
    """城市ID"""
    is_popup: builtins.int
    """是否弹窗"""
    popup: Optional["Popup"] = None
    """弹窗内容"""
    defaultTab: builtins.bool
    """是否默认tab"""
    sub_title: builtins.str
    """副标题 对应城市名"""
    anchor: builtins.str
    """锚点字段"""
    internal_test: builtins.str
    """内测文案"""


class DynTabReply(BaseModel):
    """动态tab页-响应"""

    dyn_tab: "List[DynTab]"
    """动态tab详情列表"""


class DynTabReq(BaseModel):
    """动态tab页-请求"""

    teenagers_mode: builtins.int
    """青少年模式
    1:开启青少年模式
    """


class DynUpdOffsetReq(BaseModel):
    """最近访问-标记已读-请求"""

    host_uid: builtins.int
    """被访问者的UID"""
    read_offset: builtins.str
    """用户已读进度"""


class DynVideoPersonalReply(BaseModel):
    """最近访问-个人feed流列表-响应"""

    list: "List[DynamicItem]"
    """动态列表"""
    offset: builtins.str
    """偏移量"""
    has_more: builtins.int
    """是否还有更多数据"""
    read_offset: builtins.str
    """已读进度"""


class DynVideoPersonalReq(BaseModel):
    """最近访问-个人feed流列表-请求"""

    teenagers_mode: builtins.int
    """青少年模式
    1:开启青少年模式
    """
    host_uid: builtins.int
    """被访问者的mid"""
    offset: builtins.str
    """偏移量 第一页可传空"""
    page: builtins.int
    """标明下拉几次"""
    is_preload: builtins.int
    """是否是预加载"""
    qn: builtins.int
    """清晰度"""
    fnver: builtins.int
    """流版本"""
    fnval: builtins.int
    """流类型"""
    force_host: builtins.int
    """是否强制使用域名"""
    fourk: builtins.int
    """是否4k"""


class DynVideoReq(BaseModel):
    """动态视频页-请求"""

    teenagers_mode: builtins.int
    """青少年模式"""
    update_baseline: builtins.str
    """透传 update_baseline"""
    offset: builtins.str
    """透传 history_offset"""
    page: builtins.int
    """向下翻页数"""
    refresh_type: builtins.int
    """刷新方式
    1:向上刷新 2:向下翻页
    """
    qn: builtins.int
    """清晰度"""
    fnver: builtins.int
    """流版本"""
    fnval: builtins.int
    """流类型"""
    force_host: builtins.int
    """是否强制使用域名"""
    fourk: builtins.int
    """是否4K"""


class DynVideoReqReply(BaseModel):
    """动态视频页-响应"""

    list: "List[DynamicItem]"
    """动态列表"""
    update_num: builtins.int
    """更新的动态数"""
    history_offset: builtins.str
    """历史偏移"""
    update_baseline: builtins.str
    """更新基础信息"""
    has_more: builtins.int
    """是否还有更多数据"""


class Exp(BaseModel):
    """魔镜实验配置项"""

    exp_name: builtins.str
    """实验名"""
    exp_group: builtins.str
    """实验组"""


class ExpConf(BaseModel):
    """魔镜设置"""

    exp_enable: builtins.int
    """是否是魔镜请求"""
    exps: "List[Exp]"
    """实验配置"""


class Extend(BaseModel):
    """拓展"""

    type: builtins.str
    """类型
    topic:话题小卡 lbs:lbs hot:热门视频 game:游戏
    """
    ext_info_topic: Optional["ExtInfoTopic"] = None
    """话题小卡"""
    ext_info_lbs: Optional["ExtInfoLBS"] = None
    """lbs"""
    ext_info_hot: Optional["ExtInfoHot"] = None
    """热门视频"""
    ext_info_game: Optional["ExtInfoGame"] = None
    """游戏"""


class ExtInfoGame(BaseModel):
    """拓展信息-游戏小卡"""

    title: builtins.str
    """标题"""
    uri: builtins.str
    """跳转地址"""
    icon: builtins.str
    """小图标"""


class ExtInfoHot(BaseModel):
    """拓展信息-热门视频"""

    title: builtins.str
    """标题"""
    uri: builtins.str
    """跳转地址"""
    icon: builtins.str
    """小图标"""


class ExtInfoLBS(BaseModel):
    """拓展信息-lbs"""

    title: builtins.str
    """标题"""
    uri: builtins.str
    """跳转地址"""
    icon: builtins.str
    """小图标"""
    poi_type: builtins.int
    """poiType"""


class ExtInfoTopic(BaseModel):
    """拓展信息-话题小卡"""

    title: builtins.str
    """标题-话题名"""
    uri: builtins.str
    """跳转地址"""
    icon: builtins.str
    """小图标"""


class FollowListItem(BaseModel):
    """我的追番列表Item"""

    season_id: builtins.int
    """season_id"""
    title: builtins.str
    """标题"""
    cover: builtins.str
    """封面图"""
    url: builtins.str
    """跳转链接"""
    new_ep: Optional["NewEP"] = None
    """最新ep"""


class GeoCoderReply(BaseModel):
    """位置定位-响应"""

    address: builtins.str
    """以行政区划+道路+门牌号等信息组成的标准格式化地址"""
    address_component: Optional["AddressComponent"] = None
    """地址部件，address不满足需求时可自行拼接"""
    ad_info: Optional["AdInfo"] = None
    """行政区划信息"""


class GeoCoderReq(BaseModel):
    """位置定位-请求"""

    lat: builtins.float
    """纬度"""
    lng: builtins.float
    """经度"""


class Gps(BaseModel):
    """行政区划中心点坐标"""

    lat: builtins.float
    """纬度"""
    lng: builtins.float
    """经度"""


class LikeAnimation(BaseModel):
    """点赞动画"""

    begin: builtins.str
    """开始动画"""
    proc: builtins.str
    """过程动画"""
    end: builtins.str
    """结束动画"""
    like_icon_id: builtins.int
    """id"""


class LikeInfo(BaseModel):
    """点赞拓展信息"""

    animation: Optional["LikeAnimation"] = None
    """点赞动画"""
    is_like: builtins.int
    """是否点赞"""


class LikeUser(BaseModel):
    """点赞用户"""

    uid: builtins.int
    """用户mid"""
    uname: builtins.str
    """用户昵称"""
    uri: builtins.str
    """点击跳转链接"""


class LiveInfo(BaseModel):
    """直播信息"""

    is_living: builtins.int
    """是否在直播
    0:未直播 1:正在直播
    """
    uri: builtins.str
    """跳转链接"""


class MixUpListItem(BaseModel):
    """查看更多-列表单条数据"""

    uid: builtins.int
    """用户mid"""
    special_attention: builtins.int
    """特别关注
    0:否 1:是
    """
    reddot_state: builtins.int
    """小红点状态
    0:没有 1:有
    """
    live_info: "MixUpListLiveItem"
    """直播信息"""
    name: builtins.str
    """昵称"""
    face: builtins.str
    """头像"""
    official: Optional["OfficialVerify"] = None
    """认证信息"""
    vip: Optional["VipInfo"] = None
    """大会员信息"""
    relation: Optional["Relation"] = None
    """关注状态"""
    premiere_state: builtins.int
    """"""
    uri: builtins.str
    """"""


class MixUpListLiveItem(BaseModel):
    """直播信息"""

    status: builtins.bool
    """直播状态
    0:未直播 1:直播中
    """
    room_id: builtins.int
    """房间号"""
    uri: builtins.str
    """跳转地址"""


class Module(BaseModel):
    """模块"""

    module_type: builtins.str
    """类型
    fold:折叠 author:发布人 dynamic:动态卡片内容 state:计数信息 forward:转发 extend:小卡信息 dispute:争议小黄条 desc:描述信息
    likeUser:点赞用户 upList:最近访问列表 followList:我的追番
    """
    module_fold: Optional["ModuleFold"] = None
    """折叠"""
    module_author: Optional["ModuleAuthor"] = None
    """发布人"""
    module_dynamic: Optional["ModuleDynamic"] = None
    """动态卡片内容"""
    module_state: Optional["ModuleState"] = None
    """计数信息"""
    module_forward: Optional["ModuleForward"] = None
    """转发"""
    module_extend: Optional["ModuleExtend"] = None
    """小卡信息"""
    module_dispute: Optional["ModuleDispute"] = None
    """争议小黄条"""
    module_desc: Optional["ModuleDesc"] = None
    """描述信息"""
    module_likeUser: Optional["ModuleLikeUser"] = None
    """点赞用户"""
    module_upList: "ModuleDynUpList"
    """最近访问列表"""
    module_followList: "ModuleFollowList"
    """我的追番"""


class ModuleAuthor(BaseModel):
    """作者信息模块"""

    id: builtins.int
    """用户mid"""
    ptime_label_text: builtins.str
    """时间标签"""
    author: Optional["UserInfo"] = None
    """用户详情"""
    decorate_card: Optional["DecorateCard"] = None
    """装扮卡片"""


class ModuleDesc(BaseModel):
    """文本内容模块"""

    desc: "List[Description]"
    """文本描述"""


class ModuleDispute(BaseModel):
    """争议小黄条模块"""

    title: builtins.str
    """标题"""
    desc: builtins.str
    """描述内容"""
    uri: builtins.str
    """跳转链接"""


class ModuleDynamic(BaseModel):
    """动态详情模块"""

    card_type: builtins.str
    """卡片类型 
    ugc:ugc卡 pgc:pgc卡 currSeason:付费课程系列 currBatch:付费课程批次
    """
    card_ugc: Optional["CardUGC"] = None
    """ugc卡"""
    card_pgc: Optional["CardPGC"] = None
    """pgc卡"""
    card_curr_season: Optional["CardCurrSeason"] = None
    """付费课程系列"""
    card_curr_batch: Optional["CardCurrBatch"] = None
    """付费课程批次"""


class ModuleDynUpList(BaseModel):
    """最近访问up主列表"""

    module_title: builtins.str
    """标题展示文案"""
    show_all: builtins.str
    """“全部”按钮文案"""
    list: "List[UpListItem]"
    """up主列表"""


class ModuleExtend(BaseModel):
    """拓展信息"""

    extend: "List[Extend]"
    """拓展"""


class ModuleFold(BaseModel):
    """折叠模块"""

    fold_type: builtins.int
    """折叠分类(该字段废弃)"""
    text: builtins.str
    """折叠文案"""
    fold_ids: builtins.str
    """被折叠的动态"""
    fold_users: "List[UserInfo]"
    """被折叠的用户信息"""
    fold_type_v2: FoldType
    """折叠分类"""


class ModuleFollowList(BaseModel):
    """我的追番列表"""

    view_all_link: builtins.str
    """查看全部的跳转链接"""
    list: "List[FollowListItem]"
    """"""


class ModuleForward(BaseModel):
    """转发模块"""

    card_type: builtins.str
    """卡片类型"""
    modules: "List[Module]"
    """嵌套模型"""


class ModuleLikeUser(BaseModel):
    """点赞用户模块"""

    like_users: "List[LikeUser]"
    """点赞用户"""
    display_text: builtins.str
    """文案"""


class ModuleState(BaseModel):
    """计数信息模块"""

    repost: builtins.int
    """转发数"""
    like: builtins.int
    """点赞数"""
    reply: builtins.int
    """评论数"""
    like_info: Optional["LikeInfo"] = None
    """点赞拓展信息"""
    no_comment: builtins.bool
    """禁评"""
    no_forward: builtins.bool
    """禁转"""


class Nameplate(BaseModel):
    """认证名牌"""

    nid: builtins.int
    """nid"""
    name: builtins.str
    """名称"""
    image: builtins.str
    """图片地址"""
    image_small: builtins.str
    """小图地址"""
    level: builtins.str
    """等级"""
    condition: builtins.str
    """获取条件"""


class NewEP(BaseModel):
    """最新ep"""

    id: builtins.int
    """最新话epid"""
    index_show: builtins.str
    """更新至XX话"""
    cover: builtins.str
    """更新剧集的封面"""


class NoReply(BaseModel):
    """空响应"""


class NoReq(BaseModel):
    """空请求"""


class OfficialVerify(BaseModel):
    """认证信息"""

    type: builtins.int
    """认证类型
    127:未认证 0:个人 1:机构
    """
    desc: builtins.str
    """认证描述"""
    is_atten: builtins.int
    """"""


class OurCityClickReportReply(BaseModel):
    """动态同城点击上报-响应"""


class OurCityClickReportReq(BaseModel):
    """动态同城点击上报-请求"""

    dynamic_id: builtins.str
    """动态ID"""
    city_id: builtins.int
    """城市ID"""
    lat: builtins.float
    """纬度"""
    lng: builtins.float
    """经度"""


class PGCSeason(BaseModel):
    """PGC单季信息"""

    is_finish: builtins.int
    """是否完结"""
    title: builtins.str
    """标题"""
    type: builtins.int
    """类型"""


class PlayerPreloadParams(BaseModel):
    """秒开参数"""

    qn: builtins.int
    """清晰度"""
    fnver: builtins.int
    """流版本"""
    fnval: builtins.int
    """流类型"""
    force_host: builtins.int
    """是否强制使用域名"""
    fourk: builtins.int
    """是否4k"""


class Popup(BaseModel):
    """动态tab弹窗详情"""

    title: builtins.str
    """标题"""
    desc: builtins.str
    """文案"""
    uri: builtins.str
    """文案附加跳转地址"""


class Relation(BaseModel):
    """关注关系"""

    status: RelationStatus
    """关注状态"""
    is_follow: builtins.int
    """关注"""
    is_followed: builtins.int
    """被关注"""
    title: builtins.str
    """文案"""


class ShareInfo(BaseModel):
    """分享需要"""

    aid: builtins.int
    """稿件avid"""
    bvid: builtins.str
    """稿件bvid"""
    title: builtins.str
    """标题"""
    subtitle: builtins.str
    """副标题"""
    cover: builtins.str
    """稿件封面"""
    mid: builtins.int
    """up mid"""
    name: builtins.str
    """up昵称"""


class SVideoItem(BaseModel):
    """小视频卡片项"""

    card_type: builtins.str
    """卡片类型
    av:稿件视频
    """
    modules: "List[SVideoModule]"
    """模块内容"""
    dyn_id_str: builtins.str
    """动态ID str"""
    index: builtins.int
    """卡片游标"""


class SVideoModule(BaseModel):
    """小视频模块"""

    module_type: builtins.str
    """类型
    author:发布人 player:播放器内容 desc:描述信息 stat:计数信息
    """
    module_author: Optional["SVideoModuleAuthor"] = None
    """发布人"""
    module_player: Optional["SVideoModulePlayer"] = None
    """播放器内容"""
    module_desc: Optional["SVideoModuleDesc"] = None
    """描述信息"""
    module_stat: Optional["SVideoModuleStat"] = None
    """计数信息"""


class SVideoModuleAuthor(BaseModel):
    """作者信息模块"""

    mid: builtins.int
    """用户mid"""
    name: builtins.str
    """用户昵称"""
    face: builtins.str
    """用户头像"""
    pub_desc: builtins.str
    """发布描述"""
    is_attention: builtins.int
    """是否关注up
    1:已关注
    """
    uri: builtins.str
    """跳转地址"""


class SVideoModuleDesc(BaseModel):
    """文本内容模块"""

    text: builtins.str
    """文本内容"""
    uri: builtins.str
    """跳转地址"""


class SVideoModulePlayer(BaseModel):
    """播放器模块"""

    title: builtins.str
    """标题"""
    cover: builtins.str
    """封面图"""
    uri: builtins.str
    """跳转地址，秒开地址如果有会拼接player_preload可参考天马"""
    aid: builtins.int
    """aid"""
    cid: builtins.int
    """cid"""
    duration: builtins.int
    """视频时长"""
    dimension: Optional["Dimension"] = None
    """尺寸信息"""


class SVideoModuleStat(BaseModel):
    """计数信息模块"""

    stat_info: "List[SVideoStatInfo]"
    """计数内容"""
    share_info: Optional["ShareInfo"] = None
    """分享需要"""


class SVideoReply(BaseModel):
    """小视频连播页-响应"""

    list: "List[SVideoItem]"
    """列表"""
    offset: builtins.str
    """翻页游标"""
    has_more: builtins.int
    """是否还有更多数据
    1:有
    """
    top: Optional["SVideoTop"] = None
    """顶部"""


class SVideoReq(BaseModel):
    """小视频连播页-请求"""

    oid: builtins.int
    """当前素材的id"""
    type: SVideoType
    """当前素材类型
    1:动态(如果有oid则必传) 2:热门分类 3:热点聚合
    """
    offset: builtins.str
    """翻页offset"""
    qn: builtins.int
    """清晰度(旧版)"""
    fnver: builtins.int
    """流版本(旧版)"""
    fnval: builtins.int
    """流类型(旧版)"""
    force_host: builtins.int
    """是否强制使用域名(旧版)"""
    fourk: builtins.int
    """是否4k(旧版)"""
    spmid: builtins.str
    """当前页面spm"""
    from_spmid: builtins.str
    """上级页面spm"""
    player_preload: Optional["PlayerPreloadParams"] = None
    """秒开参数"""
    focus_aid: builtins.int
    """热门进入联播页的锚点aid"""
    player_args: bilibiliq.internal.pb.bilibili.app.archive.middleware.v1.preload_pb2_model.PlayerArgs
    """秒开参数"""


class SVideoStatInfo(BaseModel):
    """计数内容"""

    icon: builtins.int
    """计数icon
    1:分享符号 2:评论符号 3:点赞符号
    """
    num: builtins.int
    """计数值"""
    selected: builtins.int
    """选中状态
    1:选中
    """
    uri: builtins.str
    """跳转链接(如评论)"""


class SVideoTop(BaseModel):
    """顶部"""

    Title: builtins.str
    """联播页标题"""
    Desc: builtins.str
    """联播页导语"""


class TabOffset(BaseModel):
    """动态红点接口各tab offset信息"""

    tab: builtins.int
    """1:综合页 2:视频页"""
    offset: builtins.str
    """上一次对应列表页offset"""


class UpListItem(BaseModel):
    """up主列表"""

    has_update: builtins.int
    """是否有更新
    0:没有 1:有
    """
    face: builtins.str
    """up主头像"""
    name: builtins.str
    """up主昵称"""
    uid: builtins.int
    """up主uid"""


class UserInfo(BaseModel):
    """用户信息"""

    mid: builtins.int
    """用户mid"""
    name: builtins.str
    """用户昵称"""
    face: builtins.str
    """用户头像"""
    official: Optional["OfficialVerify"] = None
    """认证信息"""
    vip: Optional["VipInfo"] = None
    """大会员信息"""
    live: Optional["LiveInfo"] = None
    """直播信息"""
    uri: builtins.str
    """空间页跳转链接"""
    pendant: Optional["UserPendant"] = None
    """挂件信息"""
    nameplate: Optional["Nameplate"] = None
    """认证名牌"""


class UserPendant(BaseModel):
    """头像挂件信息"""

    pid: builtins.int
    """pid"""
    name: builtins.str
    """名称"""
    image: builtins.str
    """图片链接"""
    expire: builtins.int
    """有效期"""


class VideoBadge(BaseModel):
    """角标信息"""

    text: builtins.str
    """文案"""
    text_color: builtins.str
    """文案颜色-日间"""
    text_color_night: builtins.str
    """文案颜色-夜间"""
    bg_color: builtins.str
    """背景颜色-日间"""
    bg_color_night: builtins.str
    """背景颜色-夜间"""
    border_color: builtins.str
    """边框颜色-日间"""
    border_color_night: builtins.str
    """边框颜色-夜间"""
    bg_style: builtins.int
    """样式"""


class VipInfo(BaseModel):
    """大会员信息"""

    Type: builtins.int
    """大会员类型"""
    status: builtins.int
    """大会员状态"""
    due_date: builtins.int
    """到期时间"""
    label: Optional["VipLabel"] = None
    """标签"""
    theme_type: builtins.int
    """主题"""


class VipLabel(BaseModel):
    """大会员标签"""

    path: builtins.str
    """图片地址"""


Popup.update_forward_refs()
Nameplate.update_forward_refs()
CardCurrBatch.update_forward_refs()
DynRedStyleUp.update_forward_refs()
DynOurCityReply.update_forward_refs()
CardUGC.update_forward_refs()
ModuleFold.update_forward_refs()
ModuleExtend.update_forward_refs()
DynRedStyle.update_forward_refs()
DynTab.update_forward_refs()
DynRedItem.update_forward_refs()
DynOurCityModuleExtend.update_forward_refs()
DynTabReq.update_forward_refs()
Extend.update_forward_refs()
TabOffset.update_forward_refs()
DynVideoPersonalReq.update_forward_refs()
FollowListItem.update_forward_refs()
SVideoReply.update_forward_refs()
ModuleFollowList.update_forward_refs()
CardPGC.update_forward_refs()
GeoCoderReq.update_forward_refs()
Relation.update_forward_refs()
Description.update_forward_refs()
SVideoModuleDesc.update_forward_refs()
SVideoItem.update_forward_refs()
ModuleDynamic.update_forward_refs()
DynOurCityReq.update_forward_refs()
SVideoStatInfo.update_forward_refs()
DynTabReply.update_forward_refs()
DynDetailsReply.update_forward_refs()
DynMixUpListViewMoreReply.update_forward_refs()
MixUpListLiveItem.update_forward_refs()
ModuleAuthor.update_forward_refs()
SVideoReq.update_forward_refs()
VipLabel.update_forward_refs()
PGCSeason.update_forward_refs()
DynRedReq.update_forward_refs()
DynVideoReq.update_forward_refs()
LikeUser.update_forward_refs()
SVideoModuleStat.update_forward_refs()
UpListItem.update_forward_refs()
VipInfo.update_forward_refs()
DynOurCityItem.update_forward_refs()
ModuleDynUpList.update_forward_refs()
OurCityClickReportReply.update_forward_refs()
DynMixUpListSearchReq.update_forward_refs()
ShareInfo.update_forward_refs()
Gps.update_forward_refs()
LikeAnimation.update_forward_refs()
ExtInfoLBS.update_forward_refs()
VideoBadge.update_forward_refs()
ModuleLikeUser.update_forward_refs()
ExpConf.update_forward_refs()
DynVideoReqReply.update_forward_refs()
PlayerPreloadParams.update_forward_refs()
OfficialVerify.update_forward_refs()
DynOurCityModuleExtendLBS.update_forward_refs()
ExtInfoTopic.update_forward_refs()
SVideoModuleAuthor.update_forward_refs()
ModuleDispute.update_forward_refs()
GeoCoderReply.update_forward_refs()
DynRedReply.update_forward_refs()
NewEP.update_forward_refs()
DynOurCityModuleCover.update_forward_refs()
AddressComponent.update_forward_refs()
CardCurrSeason.update_forward_refs()
SVideoModule.update_forward_refs()
ModuleDesc.update_forward_refs()
DynUpdOffsetReq.update_forward_refs()
UserPendant.update_forward_refs()
DecoCardFan.update_forward_refs()
DynOurCityModuleAuthor.update_forward_refs()
DynOurCityModule.update_forward_refs()
AdInfo.update_forward_refs()
Exp.update_forward_refs()
UserInfo.update_forward_refs()
DynOurCitySwitchReq.update_forward_refs()
MixUpListItem.update_forward_refs()
SVideoModulePlayer.update_forward_refs()
DynamicItem.update_forward_refs()
LiveInfo.update_forward_refs()
NoReq.update_forward_refs()
ExtInfoHot.update_forward_refs()
LikeInfo.update_forward_refs()
ModuleState.update_forward_refs()
OurCityClickReportReq.update_forward_refs()
ModuleForward.update_forward_refs()
DynDetailsReq.update_forward_refs()
ExtInfoGame.update_forward_refs()
Dimension.update_forward_refs()
DynMixUpListSearchReply.update_forward_refs()
DynVideoPersonalReply.update_forward_refs()
DecorateCard.update_forward_refs()
Module.update_forward_refs()
DynOurCityModuleDesc.update_forward_refs()
SVideoTop.update_forward_refs()
NoReply.update_forward_refs()
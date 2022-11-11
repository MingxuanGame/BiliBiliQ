"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class AdAutoPlayVideoDto(BaseModel):
    """自动播放视频"""

    avid: builtins.int
    """avid"""
    cid: builtins.int
    """cid"""
    page: builtins.int
    """分P"""
    url: builtins.str
    """是否自动播放"""
    cover: builtins.str
    """是否自动播放"""
    auto_play: builtins.bool
    """是否自动播放"""
    btn_dyc_color: builtins.bool
    """按钮是否动态变色"""
    btn_dyc_time: builtins.int
    """按钮动态变色时间 ms"""
    biz_id: builtins.int
    """用于做联播是否是同一个视频的id"""
    process0_urls: List[builtins.str]
    """开始播放三方监控"""
    play_3s_urls: List[builtins.str]
    """播放3S三方监控"""
    play_5s_urls: List[builtins.str]
    """播放5S三方监控"""
    orientation: builtins.int
    """横竖屏"""


class AdBusinessMarkDto(BaseModel):
    """商业标信息"""

    type: builtins.int
    """商业标样式
    0:不展示标 1:实心+文字 2:空心框+文字 3:纯文字标 4:纯图片标
    """
    text: builtins.str
    """商业标文案"""
    text_color: builtins.str
    """商业标文案颜色,如#80FFFFFF RGBA"""
    text_color_night: builtins.str
    """夜间模式文字色"""
    bg_color: builtins.str
    """背景色"""
    bg_color_night: builtins.str
    """夜间模式背景色"""
    border_color: builtins.str
    """边框色"""
    border_color_night: builtins.str
    """夜间模式边框色"""
    img_url: builtins.str
    """图片商业标"""
    img_height: builtins.int
    """图片高度"""
    img_width: builtins.int
    """图片宽度"""
    bg_border_color: builtins.str
    """"""


class AdButtonDto(BaseModel):
    """按钮"""

    type: builtins.int
    """类型
    1:落地页 2:应用唤起 3:应用下载
    """
    text: builtins.str
    """按钮文案"""
    jump_url: builtins.str
    """按钮跳转地址"""
    report_urls: builtins.str
    """跳转监测链接"""
    dlsuc_callup_url: builtins.str
    """唤起schema"""
    game_id: builtins.int
    """游戏id"""
    game_monitor_param: builtins.str
    """游戏监控字段"""
    game_channel_id: builtins.int
    """"""
    game_channel_extra: builtins.str
    """"""


class AdCardDto(BaseModel):
    """卡片"""

    card_type: builtins.int
    """卡片类型"""
    title: builtins.str
    """标题"""
    desc: builtins.str
    """描述"""
    extra_desc: builtins.str
    """额外描述"""
    long_desc: builtins.str
    """长描述"""
    short_title: builtins.str
    """短标题, 弹幕广告目录面板标题"""
    danmu_title: builtins.str
    """弹幕/浮层广告的弹幕标题"""
    danmu_height: builtins.int
    """弹幕/浮层广告的弹幕高度，整型，分母为100"""
    danmu_width: builtins.int
    """弹幕/浮层广告的弹幕宽度，整型，分母为100"""
    danmu_life: builtins.int
    """弹幕/浮层广告生存时间，单位为毫秒"""
    danmu_begin: builtins.int
    """弹幕/浮层开始时间，单位为毫秒"""
    danmu_color: builtins.str
    """背景色值（含透明度）如#80FFFFFF"""
    danmu_h5url: builtins.str
    """弹幕/浮层广告H5落地页"""
    danmu_icon: builtins.str
    """弹幕/浮层 广告icon"""
    fold_time: builtins.int
    """折叠时间，永驻浮层折叠时间，单位为毫秒"""
    ad_tag: builtins.str
    """广告标文案"""
    covers: "List[AdCoverDto]"
    """cover数组"""
    jump_url: builtins.str
    """卡片跳转链接"""
    imax_landing_page_json_string: builtins.str
    """"""
    callup_url: builtins.str
    """app唤起schema"""
    universal_app: builtins.str
    """univeral link域名"""
    ori_price: builtins.str
    """原价, 单位为分"""
    cur_price: builtins.int
    """现价, 同上"""
    price_desc: builtins.str
    """券后/现价 价格描述"""
    price_symbol: builtins.str
    """价格单位符号"""
    goods_cur_price: builtins.str
    """券后价格 "1000" """
    goods_ori_price: builtins.str
    """原价 "¥1002" """
    good: Optional["AdGoodDto"] = None
    """开放平台商品"""
    rank: builtins.int
    """打分? 满分为100"""
    hot_score: builtins.int
    """热度"""
    button: Optional["AdButtonDto"] = None
    """按钮"""
    adver_logo: builtins.str
    """广告主logo"""
    adver_name: builtins.str
    """广告主name"""
    adver_page_url: builtins.str
    """广告主主页链接"""
    video_barrage: List[builtins.str]
    """视频弹幕，视频广告用"""
    ad_tag_style: Optional["AdBusinessMarkDto"] = None
    """商业标信息"""
    video: Optional["AdAutoPlayVideoDto"] = None
    """自动播放视频"""
    feedback_panel: Optional["AdFeedbackPanelDto"] = None
    """反馈面板功能模块，屏蔽、投诉、广告介绍"""
    adver_mid: builtins.int
    """"""
    adver_account_id: builtins.int
    """"""
    duration: builtins.str
    """"""
    quality_infos: "List[QualityInfo]"
    """"""
    dynamic_text: builtins.str
    """动态广告文本"""
    adver: Optional["AdverDto"] = None
    """广告主信息"""
    grade_level: builtins.int
    """评分"""
    support_transition: builtins.bool
    """"""
    transition: builtins.str
    """"""
    under_player_interaction_style: builtins.int
    """"""
    imax_landing_page_v2: builtins.str
    """"""
    subcard_module: Optional["SubCardModule"] = None
    """"""
    grade_denominator: builtins.int
    """"""
    star_level: builtins.int
    """"""
    bulletin: Optional["Bulletin"] = None
    """"""
    gift: Optional["Gift"] = None
    """"""
    game_tags: List[builtins.str]
    """"""
    ori_mark_hidden: builtins.int
    """"""
    use_multi_cover: builtins.bool
    """"""
    wx_program_info: Optional["WxProgramInfo"] = None
    """"""
    android_game_page_res: Optional["AndroidGamePageRes"] = None
    """"""
    not_clickable_area: Optional["NotClickableArea"] = None
    """"""
    forward_reply: Optional["ForwardReply"] = None
    """"""


class AdContentExtraDto(BaseModel):
    """额外广告数据"""

    layout: builtins.str
    """动态布局"""
    show_urls: List[builtins.str]
    """展现监控url"""
    click_urls: List[builtins.str]
    """点击监控url"""
    danmu_list_show_urls: List[builtins.str]
    """弹幕创意列表展示第三方上报"""
    danmu_list_click_urls: List[builtins.str]
    """弹幕创意列表点击第三方上报"""
    danmu_detail_show_urls: List[builtins.str]
    """弹幕详情页展示第三方上报"""
    danmu_trolley_add_urls: List[builtins.str]
    """弹幕商品添加购物车第三方上报"""
    use_ad_web_v2: builtins.bool
    """useWebView默认false"""
    open_whitelist: List[builtins.str]
    """app唤起白名单"""
    download_whitelist: Optional["AppPackageDto"] = None
    """app下载白名单"""
    card: Optional["AdCardDto"] = None
    """卡片相关信息"""
    report_time: builtins.int
    """视频播放和弹幕播放上报控制时间 ms"""
    appstore_priority: builtins.int
    """是否优先唤起app store"""
    sales_type: builtins.int
    """广告售卖类型"""
    preload_landingpage: builtins.int
    """落地页是否预加载"""
    special_industry: builtins.bool
    """是否需要展示风险行业提示"""
    special_industry_tips: builtins.str
    """风险行业提示"""
    enable_download_dialog: builtins.bool
    """是否展示下载弹框"""
    enable_share: builtins.bool
    """是否允许分享"""
    upzone_entrance_type: builtins.int
    """个人空间广告入口类型
    1:橱窗 2:商品店铺 3:小程序
    """
    upzone_entrance_report_id: builtins.int
    """个人空间广告入口上报id,橱窗id(当前用Mid)、店铺id或者小程序id"""
    share_info: Optional["AdShareInfoDto"] = None
    """分享数据"""
    topview_pic_url: builtins.str
    """topview图片链接，闪屏预下载用"""
    topview_video_url: builtins.str
    """topview视频链接，闪屏预下载用"""
    click_area: builtins.int
    """点击区域
    0:表示banner可点击 1:表示素材可点击
    """
    shop_id: builtins.int
    """店铺"""
    up_mid: builtins.int
    """up主"""
    track_id: builtins.str
    """回传id"""
    enable_store_direct_launch: builtins.int
    """商店直投"""
    product_id: builtins.int
    """DPA2.0商品ID"""
    enable_double_jump: builtins.bool
    """"""
    show1s_urls: List[builtins.str]
    """"""
    from_track_id: builtins.str
    """"""
    store_callup_card: builtins.bool
    """"""
    landingpage_download_style: builtins.int
    """"""
    special_industry_style: builtins.int
    """"""
    enable_h5_alert: builtins.bool
    """"""
    macro_replace_priority: builtins.int
    """"""
    feedback_panel_style: builtins.int
    """"""
    appstore_url: builtins.str
    """"""
    enable_h5_pre_load: builtins.int
    """"""
    h5_pre_load_url: builtins.str
    """"""
    cm_from_track_id: builtins.str
    """"""


class AdCoverDto(BaseModel):
    """广告卡片封面数据"""

    url: builtins.str
    """图片链接"""
    loop: builtins.int
    """动图循环次数
    0:无限循环
    """
    jump_url: builtins.str
    """图片点击跳转地址，截至目前为空"""
    report_urls: List[builtins.str]
    """跳转监测链接， 数组，单个图片的监控，出区别于click_urls，应前端要求。（此字段截至目前为空，使用时需再次确认）"""
    image_height: builtins.int
    """图片高度"""
    image_width: builtins.int
    """图片宽度"""


class AdDto(BaseModel):
    """广告内容"""

    creative_id: builtins.int
    """广告创意ID"""
    ad_cb: builtins.str
    """广告闭环上报回传数据"""
    extra: Optional["AdContentExtraDto"] = None
    """额外广告数据"""
    cm_mark: builtins.int
    """广告标记"""
    top_view_id: builtins.int
    """"""
    creative_type: builtins.int
    """"""
    card_type: builtins.int
    """"""
    creative_style: builtins.int
    """"""
    is_ad: builtins.int
    """"""
    creative_content: Optional["CreativeDto"] = None
    """"""


class AdFeedbackPanelDto(BaseModel):
    """反馈面板功能模块"""

    panel_type_text: builtins.str
    """面板类型，广告、推广"""
    feedback_panel_detail: "List[AdFeedbackPanelModuleDto]"
    """反馈面版信息"""
    toast: builtins.str
    """"""
    open_rec_tips: builtins.str
    """"""
    close_rec_tips: builtins.str
    """"""


class AdFeedbackPanelModuleDto(BaseModel):
    """反馈面版信息"""

    module_id: builtins.int
    """模块id"""
    icon_url: builtins.str
    """icon url"""
    jump_type: builtins.int
    """跳转类型
    1:气泡 2:H5
    """
    jump_url: builtins.str
    """跳转地址"""
    text: builtins.str
    """文案"""
    secondary_panel: "List[AdSecondFeedbackPanelDto]"
    """二级文案数组"""
    sub_text: builtins.str
    """"""


class AdGoodDto(BaseModel):
    """开放平台商品"""

    item_id: builtins.int
    """电商商品ID"""
    sku_id: builtins.int
    """电商SKU ID"""
    shop_id: builtins.int
    """店铺ID"""
    sku_num: builtins.int
    """SKU库存"""


class AdOgvEpDto(BaseModel):
    """有弹幕的ogv ep"""

    epid: builtins.int
    """分集epid"""
    has_recommend: builtins.bool
    """是否显示 "荐" """


class AdsControlDto(BaseModel):
    """广告控制"""

    has_danmu: builtins.int
    """视频是否有弹幕，如有，需请求弹幕广告"""
    cids: List[builtins.int]
    """有弹幕的分P视频的cid，已弃用"""
    eps: "List[AdOgvEpDto]"
    """有弹幕的ogv ep"""


class AdSecondFeedbackPanelDto(BaseModel):
    """二级文案"""

    reason_id: builtins.int
    """屏蔽理由id"""
    text: builtins.str
    """理由文案"""


class AdShareInfoDto(BaseModel):
    """分享"""

    title: builtins.str
    """分享标题"""
    subtitle: builtins.str
    """分享副标题"""
    image_url: builtins.str
    """分享图片url"""


class AdverDto(BaseModel):
    """广告主信息"""

    adver_id: builtins.int
    """"""
    adver_logo: builtins.str
    """"""
    adver_name: builtins.str
    """"""
    adver_type: builtins.int
    """"""
    adver_page_url: builtins.str
    """"""
    adver_desc: builtins.str
    """"""


class AndroidGamePageRes(BaseModel):
    """"""

    module1: Optional["Module1"] = None
    """"""
    module3: Optional["Module3"] = None
    """"""
    module4: Optional["Module4"] = None
    """"""
    module5: Optional["Module5"] = None
    """"""
    module6: Optional["Module6"] = None
    """"""
    module7: Optional["Module7"] = None
    """"""
    module8: Optional["Module8"] = None
    """"""
    module9: Optional["Module9"] = None
    """"""
    module10: Optional["Module10"] = None
    """"""
    module11: Optional["Module11"] = None
    """"""
    module12: Optional["Module12"] = None
    """"""
    module13: Optional["Module13"] = None
    """"""
    module_seq: List[builtins.int]
    """"""
    background_color: builtins.str
    """"""
    module14: Optional["Module14"] = None
    """"""


class AndroidTag(BaseModel):
    """"""

    text: builtins.str
    """"""
    type: builtins.int
    """"""


class AppPackageDto(BaseModel):
    """app下载白名单"""

    size: builtins.int
    """包大小(单位bytes)"""
    display_name: builtins.str
    """"""
    apk_name: builtins.str
    """"""
    url: builtins.str
    """url"""
    bili_url: builtins.str
    """bili schema url"""
    md5: builtins.str
    """包md5"""
    icon: builtins.str
    """包icon"""
    dev_name: builtins.str
    """开发者姓名"""
    auth_url: builtins.str
    """权限地址"""
    auth_name: builtins.str
    """权限名，逗号隔开"""
    version: builtins.str
    """版本"""
    update_time: builtins.str
    """更新时间,yy-mm-hh格式"""
    privacy_name: builtins.str
    """隐私协议标题"""
    privacy_url: builtins.str
    """隐私协议url"""


class Bulletin(BaseModel):
    """"""

    tag_text: builtins.str
    """"""
    text: builtins.str
    """"""


class Comment(BaseModel):
    """"""

    game_base_id: builtins.int
    """"""
    user_name: builtins.str
    """"""
    user_face: builtins.str
    """"""
    user_level: builtins.int
    """"""
    comment_no: builtins.str
    """"""
    grade: builtins.int
    """"""
    content: builtins.str
    """"""
    up_count: builtins.int
    """"""


class CreativeDto(BaseModel):
    """"""

    title: builtins.str
    """"""
    description: builtins.str
    """"""
    image_url: builtins.str
    """"""
    image_md5: builtins.str
    """"""
    url: builtins.str
    """"""
    click_url: builtins.str
    """"""
    show_url: builtins.str
    """"""
    video_id: builtins.int
    """"""
    thumbnail_url: builtins.str
    """"""
    thumbnail_url_md5: builtins.str
    """"""
    logo_url: builtins.str
    """"""
    logo_md5: builtins.str
    """"""
    username: builtins.str
    """"""


class CustomPlayUrl(BaseModel):
    """"""

    play_time: builtins.int
    """"""
    urls: List[builtins.str]
    """"""


class ForwardReply(BaseModel):
    """"""

    comment_id: builtins.int
    """"""
    message: builtins.str
    """"""
    highlight_text: builtins.str
    """"""
    highlight_prefix_icon: builtins.str
    """"""
    callup_url: builtins.str
    """"""
    jump_url: builtins.str
    """"""
    jump_type: builtins.int
    """"""
    author_name: builtins.str
    """"""
    author_icon: builtins.str
    """"""


class Gift(BaseModel):
    """"""

    icon: builtins.str
    """"""
    night_icon: builtins.str
    """"""
    text: builtins.str
    """"""
    url: builtins.str
    """"""


class IosGamePageRes(BaseModel):
    """"""

    logo: builtins.str
    """"""
    name: builtins.str
    """"""
    sub_titile: builtins.str
    """"""
    image_url: List[builtins.str]
    """"""
    desc: builtins.str
    """"""
    game_button: Optional["AdButtonDto"] = None
    """"""
    grade: builtins.float
    """"""
    rank_num: builtins.str
    """"""
    rank_name: builtins.str
    """"""


class Module1(BaseModel):
    """"""

    game_name: builtins.str
    """"""
    game_icon: builtins.str
    """"""
    developer_input_name: builtins.str
    """"""
    tag_list: "List[AndroidTag]"
    """"""


class Module3(BaseModel):
    """"""

    display: builtins.bool
    """"""
    quality_params: "List[QualityParmas]"
    """"""


class Module4(BaseModel):
    """"""

    display: builtins.bool
    """"""
    gift_num: builtins.int
    """"""
    gift_name: builtins.str
    """"""
    gift_icon_num: builtins.int
    """"""
    icon_urls: List[builtins.str]
    """"""


class Module5(BaseModel):
    """"""

    display: builtins.bool
    """"""
    game_summary: builtins.str
    """"""


class Module6(BaseModel):
    """"""

    display: builtins.bool
    """"""
    game_desc: builtins.str
    """"""


class Module7(BaseModel):
    """"""

    display: builtins.bool
    """"""
    screen_shots: "List[ScreenShots]"
    """"""


class Module8(BaseModel):
    """"""

    display: builtins.bool
    """"""
    tag_list: List[builtins.str]
    """"""


class Module9(BaseModel):
    """"""

    display: builtins.bool
    """"""
    dev_introduction: builtins.str
    """"""


class Module10(BaseModel):
    """"""

    display: builtins.bool
    """"""
    latest_update: builtins.str
    """"""


class Module11(BaseModel):
    """"""

    display: builtins.bool
    """"""
    star_number_list: List[builtins.int]
    """"""
    comment_str: builtins.str
    """"""
    grade: builtins.float
    """"""


class Module12(BaseModel):
    """"""

    display: builtins.bool
    """"""
    comment_list: "List[Comment]"
    """"""
    comment_num: builtins.str
    """"""
    show_all_comment: builtins.bool
    """"""


class Module13(BaseModel):
    """"""

    pkg_size: builtins.int
    """"""
    customer_service: builtins.str
    """"""
    website: builtins.str
    """"""
    authority: builtins.str
    """"""
    privacy: builtins.str
    """"""
    developer_name: builtins.str
    """"""
    update_time: builtins.str
    """"""
    game_version: builtins.str
    """"""
    android_pkg_name: builtins.str
    """"""


class Module14(BaseModel):
    """"""

    reward_list: "List[Reward]"
    """"""
    display: builtins.bool
    """"""


class NotClickableArea(BaseModel):
    """"""

    x: builtins.int
    """"""
    y: builtins.int
    """"""
    z: builtins.int
    """"""


class QualityInfo(BaseModel):
    """"""

    icon: builtins.str
    """"""
    text: builtins.str
    """"""
    is_bg: builtins.bool
    """"""
    bg_color: builtins.str
    """"""
    bg_color_night: builtins.str
    """"""


class QualityParmas(BaseModel):
    """"""

    first_line: builtins.str
    """"""
    second_line: builtins.str
    """"""
    grade: builtins.float
    """"""
    rank_icon: builtins.str
    """"""
    quality_type: builtins.int
    """"""


class Reward(BaseModel):
    """"""

    level: builtins.int
    """"""
    title: builtins.str
    """"""
    content: builtins.str
    """"""
    pic: builtins.str
    """"""
    reach: builtins.bool
    """"""


class ScreenShots(BaseModel):
    """"""

    url: builtins.str
    """"""
    height: builtins.int
    """"""
    width: builtins.int
    """"""
    seq: builtins.int
    """"""


class SourceContentDto(BaseModel):
    """广告数据"""

    request_id: builtins.str
    """广告请求id"""
    source_id: builtins.int
    """广告资源位source ID"""
    resource_id: builtins.int
    """广告资源位resource ID"""
    is_ad_loc: builtins.bool
    """广告位上报标记,对广告返回数据恒为true"""
    server_type: int
    """与天马现有逻辑一致, 0有含义
        0:内容 1:广告
        """
    client_ip: builtins.str
    """客户端IP回传拼接"""
    card_index: int
    """广告卡片位置在一刷中的位置, 天马用, 0有含义"""
    index: builtins.int
    """广告资源位source 位次"""
    ad_content: Optional["AdDto"] = None
    """广告内容"""


class SubCardModule(BaseModel):
    """"""

    subcard_type: builtins.str
    """"""
    icon: builtins.str
    """"""
    desc: builtins.str
    """"""
    rank_stars: builtins.str
    """"""
    amount_number: builtins.str
    """"""
    avatar: builtins.str
    """"""
    title: builtins.str
    """"""
    button: Optional["AdButtonDto"] = None
    """"""
    tag_infos: "List[TagInfo]"
    """"""


class Tab2ExtraDto(BaseModel):
    """"""

    cover_url: builtins.str
    """"""
    title: builtins.str
    """"""
    desc: builtins.str
    """"""
    button: Optional["AdButtonDto"] = None
    """"""
    auto_animate_time_ms: builtins.int
    """"""
    enable_click: builtins.bool
    """"""
    panel_url: builtins.str
    """"""
    download_whitelist: "List[AppPackageDto]"
    """"""
    open_whitelist: List[builtins.str]
    """"""
    use_ad_web_v2: builtins.bool
    """"""
    enable_store_direct_launch: builtins.bool
    """"""
    sales_type: builtins.int
    """"""
    landingpage_download_style: builtins.int
    """"""
    appstore_priority: builtins.int
    """"""
    appstore_url: builtins.str
    """"""
    appstore_delay_time: builtins.int
    """"""
    page_cover_type: builtins.int
    """"""
    page_pull_type: builtins.int
    """"""
    android_game_page_res: Optional["AndroidGamePageRes"] = None
    """"""
    ios_game_page_res: Optional["IosGamePageRes"] = None
    """"""
    ad_tag_style: Optional["AdBusinessMarkDto"] = None
    """"""
    feedback_panel: Optional["AdFeedbackPanelDto"] = None
    """"""
    ad_cb: builtins.str
    """"""
    url_type: builtins.int
    """"""


class TabExtraDto(BaseModel):
    """"""

    tab_url: builtins.str
    """"""
    enable_store_direct_launch: builtins.int
    """"""
    store_callup_card: builtins.int
    """"""
    sales_type: builtins.int
    """"""
    download_whitelist: "List[AppPackageDto]"
    """"""
    special_industry: builtins.bool
    """"""
    special_industry_tips: builtins.str
    """"""
    open_whitelist: List[builtins.str]
    """"""
    landingpage_download_style: builtins.int
    """"""
    appstore_priority: builtins.int
    """"""
    use_ad_web_v2: builtins.bool
    """"""
    enable_download_dialog: builtins.bool
    """"""
    appstore_url: builtins.str
    """"""
    appstore_delay_time: builtins.int
    """"""


class TabInfoDto(BaseModel):
    """"""

    tab_name: builtins.str
    """"""
    extra: Any
    """"""
    tab_version: builtins.int
    """"""


class TagInfo(BaseModel):
    """"""

    text: builtins.str
    """"""
    text_color: builtins.str
    """"""
    text_color_night: builtins.str
    """"""
    bg_color: builtins.str
    """"""
    bg_color_night: builtins.str
    """"""
    border_color: builtins.str
    """"""
    border_color_night: builtins.str
    """"""
    type: builtins.str
    """"""


class WxProgramInfo(BaseModel):
    """"""

    org_id: builtins.str
    """"""
    name: builtins.str
    """"""
    path: builtins.str
    """"""


AdDto.update_forward_refs()
AndroidTag.update_forward_refs()
SourceContentDto.update_forward_refs()
Tab2ExtraDto.update_forward_refs()
AdSecondFeedbackPanelDto.update_forward_refs()
TagInfo.update_forward_refs()
ForwardReply.update_forward_refs()
AdButtonDto.update_forward_refs()
AndroidGamePageRes.update_forward_refs()
Module9.update_forward_refs()
SubCardModule.update_forward_refs()
AdFeedbackPanelDto.update_forward_refs()
Reward.update_forward_refs()
AdCardDto.update_forward_refs()
AdGoodDto.update_forward_refs()
Module3.update_forward_refs()
ScreenShots.update_forward_refs()
Module12.update_forward_refs()
Module11.update_forward_refs()
AdOgvEpDto.update_forward_refs()
TabInfoDto.update_forward_refs()
Gift.update_forward_refs()
AdFeedbackPanelModuleDto.update_forward_refs()
Module6.update_forward_refs()
WxProgramInfo.update_forward_refs()
Module4.update_forward_refs()
AdBusinessMarkDto.update_forward_refs()
AppPackageDto.update_forward_refs()
Module5.update_forward_refs()
QualityParmas.update_forward_refs()
TabExtraDto.update_forward_refs()
Module13.update_forward_refs()
AdsControlDto.update_forward_refs()
IosGamePageRes.update_forward_refs()
Module7.update_forward_refs()
AdShareInfoDto.update_forward_refs()
CreativeDto.update_forward_refs()
AdverDto.update_forward_refs()
QualityInfo.update_forward_refs()
Module14.update_forward_refs()
Bulletin.update_forward_refs()
Module8.update_forward_refs()
CustomPlayUrl.update_forward_refs()
AdAutoPlayVideoDto.update_forward_refs()
NotClickableArea.update_forward_refs()
AdContentExtraDto.update_forward_refs()
Module10.update_forward_refs()
Module1.update_forward_refs()
Comment.update_forward_refs()
AdCoverDto.update_forward_refs()

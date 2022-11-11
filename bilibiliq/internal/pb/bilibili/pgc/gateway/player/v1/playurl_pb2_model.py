"""
Generated by generator/gen_pydantic.py. DO NOT EDIT!
isort:skip_file
"""
import builtins
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
import bilibiliq.internal.pb.bilibili.app.playurl.v1.playurl_pb2_model


class BusinessInfo(BaseModel):
    """其他业务信息"""

    is_preview: builtins.bool
    """当前视频是否是预览"""
    bp: builtins.bool
    """用户是否承包过"""
    marlin_token: builtins.str
    """drm使用"""


class Event(BaseModel):
    """事件"""

    shake: Optional["Shake"] = None
    """震动"""


class LivePlayInfo(BaseModel):
    """播放信息"""

    current_qn: builtins.int
    """"""
    quality_description: "List[QualityDescription]"
    """"""
    durl: "List[ResponseDataUrl]"
    """"""


class LivePlayViewReply(BaseModel):
    """直播播放页信息-响应"""

    room_info: Optional["RoomInfo"] = None
    """房间信息"""
    play_info: Optional["LivePlayInfo"] = None
    """播放信息"""


class LivePlayViewReq(BaseModel):
    """直播播放页信息-请求"""

    ep_id: builtins.int
    """剧集epid"""
    quality: builtins.int
    """清晰度
    0,10000:原画 400:蓝光 250:超清 150:高清 80:流畅
    """
    ptype: builtins.int
    """类型
    0:音频 2:hevc 4:dash 8:p2p, 16:蒙版
    """
    https: builtins.bool
    """是否请求https"""
    play_type: builtins.int
    """0:默认直播间播放 1:投屏播放"""
    device_type: builtins.int
    """投屏设备
    0:默认其他 1:OTT设备
    """


class PlayAbilityConf(BaseModel):
    """禁用功能配置"""

    background_play_disable: builtins.bool
    """后台播放"""
    flip_disable: builtins.bool
    """镜像反转"""
    cast_disable: builtins.bool
    """投屏"""
    feedback_disable: builtins.bool
    """反馈"""
    subtitle_disable: builtins.bool
    """字幕"""
    playback_rate_disable: builtins.bool
    """播放速度"""
    time_up_disable: builtins.bool
    """定时停止"""
    playback_mode_disable: builtins.bool
    """播放方式"""
    scale_mode_disable: builtins.bool
    """画面尺寸"""
    like_disable: builtins.bool
    """赞"""
    dislike_disable: builtins.bool
    """踩"""
    coin_disable: builtins.bool
    """投币"""
    elec_disable: builtins.bool
    """充电"""
    share_disable: builtins.bool
    """分享"""
    screen_shot_disable: builtins.bool
    """截图"""
    lock_screen_disable: builtins.bool
    """锁定"""
    recommend_disable: builtins.bool
    """相关推荐"""
    playback_speed_disable: builtins.bool
    """播放速度"""
    definition_disable: builtins.bool
    """清晰度"""
    selections_disable: builtins.bool
    """选集"""
    next_disable: builtins.bool
    """下一集"""
    edit_dm_disable: builtins.bool
    """编辑弹幕"""
    small_window_disable: builtins.bool
    """小窗"""
    shake_disable: builtins.bool
    """震动"""
    outer_dm_disable: builtins.bool
    """外层面板弹幕设置"""
    inner_dm_disable: builtins.bool
    """三点内弹幕设置"""
    freya_enter_disable: builtins.bool
    """一起看入口"""
    dolby_disable: builtins.bool
    """杜比音效"""
    freya_full_disable: builtins.bool
    """全屏一起看入口"""
    skip_oped_switch_disable: builtins.bool
    """"""


class PlayViewReply(BaseModel):
    """播放页信息-响应"""

    video_info: bilibiliq.internal.pb.bilibili.app.playurl.v1.playurl_pb2_model.VideoInfo
    """视频流信息"""
    play_conf: Optional["PlayAbilityConf"] = None
    """播放控件用户自定义配置"""
    business: Optional["BusinessInfo"] = None
    """业务需要的其他信息"""
    event: Optional["Event"] = None
    """事件"""


class PlayViewReq(BaseModel):
    """播放页信息-请求"""

    epid: builtins.int
    """剧集epid"""
    cid: builtins.int
    """视频cid"""
    qn: builtins.int
    """清晰度"""
    fnver: builtins.int
    """视频流版本"""
    fnval: builtins.int
    """视频流格式"""
    download: builtins.int
    """下载模式
    0:播放 1:flv下载 2:dash下载
    """
    force_host: builtins.int
    """流url强制是用域名
    0:允许使用ip 1:使用http 2:使用https
    """
    fourk: builtins.bool
    """是否4K"""
    spmid: builtins.str
    """当前页spm"""
    from_spmid: builtins.str
    """上一页spm"""
    teenagers_mode: builtins.int
    """青少年模式"""
    prefer_codec_type: bilibiliq.internal.pb.bilibili.app.playurl.v1.playurl_pb2_model.CodeType
    """视频编码"""
    is_preview: builtins.bool
    """是否强制请求预览视频"""
    room_id: builtins.int
    """一起看房间id"""


class ProjectReply(BaseModel):
    """投屏地址-响应"""

    project: bilibiliq.internal.pb.bilibili.app.playurl.v1.playurl_pb2_model.PlayURLReply
    """Ellipsis"""


class ProjectReq(BaseModel):
    """投屏地址-请求"""

    ep_id: builtins.int
    """剧集epid"""
    cid: builtins.int
    """视频cid"""
    qn: builtins.int
    """清晰度"""
    fnver: builtins.int
    """视频流版本"""
    fnval: builtins.int
    """视频流格式"""
    download: builtins.int
    """下载模式
    0:播放 1:flv下载 2:dash下载
    """
    forceHost: builtins.int
    """流url强制是用域名
    0:允许使用ip 1:使用http 2:使用https
    """
    fourk: builtins.bool
    """是否4K"""
    spmid: builtins.str
    """当前页spm"""
    fromSpmid: builtins.str
    """上一页spm"""
    protocol: builtins.int
    """使用协议
    0:默认乐播 1:自建协议 2:云投屏 3:airplay
    """
    device_type: builtins.int
    """投屏设备
    0:默认其他 1:OTT设备
    """
    use_new_project_code: builtins.bool
    """"""


class QualityDescription(BaseModel):
    """"""

    qn: builtins.int
    """"""
    desc: builtins.str
    """"""


class ResponseDataUrl(BaseModel):
    """"""

    url: builtins.str
    stream_type: builtins.int
    """表示stream类型,按位表示
    Value|  1   |  1  |  1   |  1   |     1
    --------------------------------------------
    desc | mask | p2p | dash | hevc | only-audio
    """
    ptag: builtins.int
    """表示支持p2p的cdn厂商,按位表示
    值   | 1  |  1  |  1  | 1  |  1  | 1  | 1  | 1
    -----------------------------------------------
    CDN	| hw | bdy | bsy | ws | txy | qn | js | bvc
    """


class RoomInfo(BaseModel):
    """房间信息"""

    room_id: builtins.int
    """房间长号"""
    uid: builtins.int
    """主播mid"""
    status: Optional["RoomStatusInfo"] = None
    """状态相关"""
    show: Optional["RoomShowInfo"] = None
    """展示相关"""


class RoomShowInfo(BaseModel):
    """房间信息-展示相关"""

    short_id: builtins.int
    """短号"""
    popularity_count: builtins.int
    """人气值"""
    live_start_time: builtins.int
    """最近一次开播时间戳"""


class RoomStatusInfo(BaseModel):
    """房间信息-状态相关"""

    live_status: builtins.int
    """直播间状态
    0:未开播 1:直播中 2:轮播中
    """
    live_screen_type: builtins.int
    """横竖屏方向
    0:横屏 1:竖屏
    """
    live_mark: builtins.int
    """是否开播过标识"""
    lock_status: builtins.int
    """封禁状态
    0:未封禁 1:审核封禁 2:全网封禁
    """
    lock_time: builtins.int
    """封禁时间戳"""
    hidden_status: builtins.int
    """隐藏状态
    0:不隐藏 1:隐藏
    """
    hidden_time: builtins.int
    """隐藏时间戳"""
    live_type: builtins.int
    """直播类型
    0:默认 1:摄像头直播 2;录屏直播 3:语音直播
    """
    room_shield: builtins.int
    """"""


class Shake(BaseModel):
    """震动"""

    file: builtins.str
    """文件地址"""


LivePlayInfo.update_forward_refs()
LivePlayViewReply.update_forward_refs()
PlayAbilityConf.update_forward_refs()
PlayViewReply.update_forward_refs()
ResponseDataUrl.update_forward_refs()
ProjectReply.update_forward_refs()
RoomStatusInfo.update_forward_refs()
PlayViewReq.update_forward_refs()
QualityDescription.update_forward_refs()
LivePlayViewReq.update_forward_refs()
Shake.update_forward_refs()
RoomInfo.update_forward_refs()
ProjectReq.update_forward_refs()
RoomShowInfo.update_forward_refs()
BusinessInfo.update_forward_refs()
Event.update_forward_refs()
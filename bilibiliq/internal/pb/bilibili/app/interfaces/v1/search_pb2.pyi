"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class DefaultWordsReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRACKID_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    SHOW_FIELD_NUMBER: builtins.int
    WORD_FIELD_NUMBER: builtins.int
    SHOW_FRONT_FIELD_NUMBER: builtins.int
    EXP_STR_FIELD_NUMBER: builtins.int
    GOTO_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    trackid: builtins.str
    """"""
    param: builtins.str
    """"""
    show: builtins.str
    """"""
    word: builtins.str
    """"""
    show_front: builtins.int
    """"""
    exp_str: builtins.str
    """"""
    goto: builtins.str
    """"""
    value: builtins.str
    """"""
    uri: builtins.str
    """"""
    def __init__(
        self,
        *,
        trackid: builtins.str = ...,
        param: builtins.str = ...,
        show: builtins.str = ...,
        word: builtins.str = ...,
        show_front: builtins.int = ...,
        exp_str: builtins.str = ...,
        goto: builtins.str = ...,
        value: builtins.str = ...,
        uri: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "exp_str",
            b"exp_str",
            "goto",
            b"goto",
            "param",
            b"param",
            "show",
            b"show",
            "show_front",
            b"show_front",
            "trackid",
            b"trackid",
            "uri",
            b"uri",
            "value",
            b"value",
            "word",
            b"word",
        ],
    ) -> None: ...

global___DefaultWordsReply = DefaultWordsReply

@typing_extensions.final
class NftFaceIcon(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGION_TYPE_FIELD_NUMBER: builtins.int
    ICON_FIELD_NUMBER: builtins.int
    SHOW_STATUS_FIELD_NUMBER: builtins.int
    region_type: builtins.int
    """"""
    icon: builtins.str
    """"""
    show_status: builtins.int
    """"""
    def __init__(
        self,
        *,
        region_type: builtins.int = ...,
        icon: builtins.str = ...,
        show_status: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "icon",
            b"icon",
            "region_type",
            b"region_type",
            "show_status",
            b"show_status",
        ],
    ) -> None: ...

global___NftFaceIcon = NftFaceIcon

@typing_extensions.final
class DefaultWordsReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FROM_FIELD_NUMBER: builtins.int
    LOGIN_EVENT_FIELD_NUMBER: builtins.int
    TEENAGERS_MODE_FIELD_NUMBER: builtins.int
    LESSONS_MODE_FIELD_NUMBER: builtins.int
    TAB_FIELD_NUMBER: builtins.int
    EVENT_ID_FIELD_NUMBER: builtins.int
    AVID_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    AN_FIELD_NUMBER: builtins.int
    IS_FRESH_FIELD_NUMBER: builtins.int
    login_event: builtins.int
    """"""
    teenagers_mode: builtins.int
    """"""
    lessons_mode: builtins.int
    """"""
    tab: builtins.str
    """"""
    event_id: builtins.str
    """"""
    avid: builtins.str
    """"""
    query: builtins.str
    """"""
    an: builtins.int
    """"""
    is_fresh: builtins.int
    """"""
    def __init__(
        self,
        *,
        login_event: builtins.int = ...,
        teenagers_mode: builtins.int = ...,
        lessons_mode: builtins.int = ...,
        tab: builtins.str = ...,
        event_id: builtins.str = ...,
        avid: builtins.str = ...,
        query: builtins.str = ...,
        an: builtins.int = ...,
        is_fresh: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "an",
            b"an",
            "avid",
            b"avid",
            "event_id",
            b"event_id",
            "from",
            b"from",
            "is_fresh",
            b"is_fresh",
            "lessons_mode",
            b"lessons_mode",
            "login_event",
            b"login_event",
            "query",
            b"query",
            "tab",
            b"tab",
            "teenagers_mode",
            b"teenagers_mode",
        ],
    ) -> None: ...

global___DefaultWordsReq = DefaultWordsReq

@typing_extensions.final
class SuggestionResult3Reply(google.protobuf.message.Message):
    """获取搜索建议-响应"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TRACKID_FIELD_NUMBER: builtins.int
    LIST_FIELD_NUMBER: builtins.int
    EXP_STR_FIELD_NUMBER: builtins.int
    trackid: builtins.str
    """搜索追踪id"""
    @property
    def list(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ResultItem
    ]:
        """搜索建议条目列表"""
    exp_str: builtins.str
    """搜索的abtest 实验信息"""
    def __init__(
        self,
        *,
        trackid: builtins.str = ...,
        list: collections.abc.Iterable[global___ResultItem] | None = ...,
        exp_str: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "exp_str", b"exp_str", "list", b"list", "trackid", b"trackid"
        ],
    ) -> None: ...

global___SuggestionResult3Reply = SuggestionResult3Reply

@typing_extensions.final
class SuggestionResult3Req(google.protobuf.message.Message):
    """获取搜索建议-请求"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEYWORD_FIELD_NUMBER: builtins.int
    HIGHLIGHT_FIELD_NUMBER: builtins.int
    TEENAGERS_MODE_FIELD_NUMBER: builtins.int
    keyword: builtins.str
    """关键字"""
    highlight: builtins.int
    """是否语法高亮
    0:不显示 1:显示
    """
    teenagers_mode: builtins.int
    """是否青少年模式
    1:开启青少年模式
    """
    def __init__(
        self,
        *,
        keyword: builtins.str = ...,
        highlight: builtins.int = ...,
        teenagers_mode: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "highlight",
            b"highlight",
            "keyword",
            b"keyword",
            "teenagers_mode",
            b"teenagers_mode",
        ],
    ) -> None: ...

global___SuggestionResult3Req = SuggestionResult3Req

@typing_extensions.final
class ResultItem(google.protobuf.message.Message):
    """搜索建议条目"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FROM_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    KEYWORD_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    COVER_FIELD_NUMBER: builtins.int
    COVER_SIZE_FIELD_NUMBER: builtins.int
    SUG_TYPE_FIELD_NUMBER: builtins.int
    TERM_TYPE_FIELD_NUMBER: builtins.int
    GOTO_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    OFFICIAL_VERIFY_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    FANS_FIELD_NUMBER: builtins.int
    LEVEL_FIELD_NUMBER: builtins.int
    ARCHIVES_FIELD_NUMBER: builtins.int
    PTIME_FIELD_NUMBER: builtins.int
    SEASON_TYPE_NAME_FIELD_NUMBER: builtins.int
    AREA_FIELD_NUMBER: builtins.int
    STYLE_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    RATING_FIELD_NUMBER: builtins.int
    VOTE_FIELD_NUMBER: builtins.int
    BADGES_FIELD_NUMBER: builtins.int
    STYLES_FIELD_NUMBER: builtins.int
    MODULE_ID_FIELD_NUMBER: builtins.int
    LIVE_LINK_FIELD_NUMBER: builtins.int
    FACE_NFT_NEW_FIELD_NUMBER: builtins.int
    NFT_FACE_ICON_FIELD_NUMBER: builtins.int
    title: builtins.str
    """显示结果(语法高亮)"""
    keyword: builtins.str
    """搜索关键字"""
    position: builtins.int
    """序号"""
    cover: builtins.str
    """图片"""
    cover_size: builtins.float
    """图片尺寸"""
    sug_type: builtins.str
    """sug词类型"""
    term_type: builtins.int
    """词条大类型"""
    goto: builtins.str
    """跳转类型"""
    uri: builtins.str
    """跳转uri"""
    @property
    def official_verify(self) -> global___OfficialVerify:
        """认证信息"""
    param: builtins.str
    """跳转参数"""
    mid: builtins.int
    """up主mid"""
    fans: builtins.int
    """粉丝数"""
    level: builtins.int
    """up主等级"""
    archives: builtins.int
    """up主稿件数"""
    ptime: builtins.int
    """投稿时间"""
    season_type_name: builtins.str
    """season类型名称"""
    area: builtins.str
    """地区"""
    style: builtins.str
    """作品风格"""
    label: builtins.str
    """描述信息"""
    rating: builtins.float
    """评分"""
    vote: builtins.int
    """投票数"""
    @property
    def badges(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ReasonStyle
    ]:
        """角标"""
    styles: builtins.str
    """"""
    module_id: builtins.int
    """"""
    live_link: builtins.str
    """"""
    face_nft_new: builtins.int
    """"""
    @property
    def nft_face_icon(self) -> global___NftFaceIcon:
        """"""

    def __init__(
        self,
        *,
        title: builtins.str = ...,
        keyword: builtins.str = ...,
        position: builtins.int = ...,
        cover: builtins.str = ...,
        cover_size: builtins.float = ...,
        sug_type: builtins.str = ...,
        term_type: builtins.int = ...,
        goto: builtins.str = ...,
        uri: builtins.str = ...,
        official_verify: global___OfficialVerify | None = ...,
        param: builtins.str = ...,
        mid: builtins.int = ...,
        fans: builtins.int = ...,
        level: builtins.int = ...,
        archives: builtins.int = ...,
        ptime: builtins.int = ...,
        season_type_name: builtins.str = ...,
        area: builtins.str = ...,
        style: builtins.str = ...,
        label: builtins.str = ...,
        rating: builtins.float = ...,
        vote: builtins.int = ...,
        badges: collections.abc.Iterable[global___ReasonStyle] | None = ...,
        styles: builtins.str = ...,
        module_id: builtins.int = ...,
        live_link: builtins.str = ...,
        face_nft_new: builtins.int = ...,
        nft_face_icon: global___NftFaceIcon | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "nft_face_icon",
            b"nft_face_icon",
            "official_verify",
            b"official_verify",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "archives",
            b"archives",
            "area",
            b"area",
            "badges",
            b"badges",
            "cover",
            b"cover",
            "cover_size",
            b"cover_size",
            "face_nft_new",
            b"face_nft_new",
            "fans",
            b"fans",
            "from",
            b"from",
            "goto",
            b"goto",
            "keyword",
            b"keyword",
            "label",
            b"label",
            "level",
            b"level",
            "live_link",
            b"live_link",
            "mid",
            b"mid",
            "module_id",
            b"module_id",
            "nft_face_icon",
            b"nft_face_icon",
            "official_verify",
            b"official_verify",
            "param",
            b"param",
            "position",
            b"position",
            "ptime",
            b"ptime",
            "rating",
            b"rating",
            "season_type_name",
            b"season_type_name",
            "style",
            b"style",
            "styles",
            b"styles",
            "sug_type",
            b"sug_type",
            "term_type",
            b"term_type",
            "title",
            b"title",
            "uri",
            b"uri",
            "vote",
            b"vote",
        ],
    ) -> None: ...

global___ResultItem = ResultItem

@typing_extensions.final
class OfficialVerify(google.protobuf.message.Message):
    """认证信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    type: builtins.int
    """认证类型
    127:未认证 0:个人 1:机构
    """
    desc: builtins.str
    """认证描述"""
    def __init__(
        self,
        *,
        type: builtins.int = ...,
        desc: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "desc", b"desc", "type", b"type"
        ],
    ) -> None: ...

global___OfficialVerify = OfficialVerify

@typing_extensions.final
class ReasonStyle(google.protobuf.message.Message):
    """角标"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    TEXT_COLOR_FIELD_NUMBER: builtins.int
    TEXT_COLOR_NIGHT_FIELD_NUMBER: builtins.int
    BG_COLOR_FIELD_NUMBER: builtins.int
    BG_COLOR_NIGHT_FIELD_NUMBER: builtins.int
    BORDER_COLOR_FIELD_NUMBER: builtins.int
    BORDER_COLOR_NIGHT_FIELD_NUMBER: builtins.int
    BG_STYLE_FIELD_NUMBER: builtins.int
    text: builtins.str
    """角标文案"""
    text_color: builtins.str
    """文案日间色值"""
    text_color_night: builtins.str
    """文案夜间色值"""
    bg_color: builtins.str
    """背景日间色值"""
    bg_color_night: builtins.str
    """背景夜间色值"""
    border_color: builtins.str
    """边框日间色值"""
    border_color_night: builtins.str
    """边框夜间色值"""
    bg_style: builtins.int
    """角标样式
    1:填充模式 2:镂空模式
    """
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        text_color: builtins.str = ...,
        text_color_night: builtins.str = ...,
        bg_color: builtins.str = ...,
        bg_color_night: builtins.str = ...,
        border_color: builtins.str = ...,
        border_color_night: builtins.str = ...,
        bg_style: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "bg_color",
            b"bg_color",
            "bg_color_night",
            b"bg_color_night",
            "bg_style",
            b"bg_style",
            "border_color",
            b"border_color",
            "border_color_night",
            b"border_color_night",
            "text",
            b"text",
            "text_color",
            b"text_color",
            "text_color_night",
            b"text_color_night",
        ],
    ) -> None: ...

global___ReasonStyle = ReasonStyle

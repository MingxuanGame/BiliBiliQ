"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import bilibili.app.card.v1.ad_pb2
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
class Args(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    UP_ID_FIELD_NUMBER: builtins.int
    UP_NAME_FIELD_NUMBER: builtins.int
    RID_FIELD_NUMBER: builtins.int
    RNAME_FIELD_NUMBER: builtins.int
    TID_FIELD_NUMBER: builtins.int
    TNAME_FIELD_NUMBER: builtins.int
    TRACK_ID_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    CONVERGE_TYPE_FIELD_NUMBER: builtins.int
    AID_FIELD_NUMBER: builtins.int
    type: builtins.int
    """"""
    up_id: builtins.int
    """"""
    up_name: builtins.str
    """"""
    rid: builtins.int
    """"""
    rname: builtins.str
    """"""
    tid: builtins.int
    """"""
    tname: builtins.str
    """"""
    track_id: builtins.str
    """"""
    state: builtins.str
    """"""
    converge_type: builtins.int
    """"""
    aid: builtins.int
    """"""
    def __init__(
        self,
        *,
        type: builtins.int = ...,
        up_id: builtins.int = ...,
        up_name: builtins.str = ...,
        rid: builtins.int = ...,
        rname: builtins.str = ...,
        tid: builtins.int = ...,
        tname: builtins.str = ...,
        track_id: builtins.str = ...,
        state: builtins.str = ...,
        converge_type: builtins.int = ...,
        aid: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "aid",
            b"aid",
            "converge_type",
            b"converge_type",
            "rid",
            b"rid",
            "rname",
            b"rname",
            "state",
            b"state",
            "tid",
            b"tid",
            "tname",
            b"tname",
            "track_id",
            b"track_id",
            "type",
            b"type",
            "up_id",
            b"up_id",
            "up_name",
            b"up_name",
        ],
    ) -> None: ...

global___Args = Args

@typing_extensions.final
class Avatar(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COVER_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    EVENT_V2_FIELD_NUMBER: builtins.int
    DEFALUT_COVER_FIELD_NUMBER: builtins.int
    cover: builtins.str
    """"""
    text: builtins.str
    """"""
    uri: builtins.str
    """"""
    type: builtins.int
    """"""
    event: builtins.str
    """"""
    event_v2: builtins.str
    """"""
    defalut_cover: builtins.int
    """"""
    def __init__(
        self,
        *,
        cover: builtins.str = ...,
        text: builtins.str = ...,
        uri: builtins.str = ...,
        type: builtins.int = ...,
        event: builtins.str = ...,
        event_v2: builtins.str = ...,
        defalut_cover: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "cover",
            b"cover",
            "defalut_cover",
            b"defalut_cover",
            "event",
            b"event",
            "event_v2",
            b"event_v2",
            "text",
            b"text",
            "type",
            b"type",
            "uri",
            b"uri",
        ],
    ) -> None: ...

global___Avatar = Avatar

@typing_extensions.final
class Base(google.protobuf.message.Message):
    """条目基本信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CARD_TYPE_FIELD_NUMBER: builtins.int
    CARD_GOTO_FIELD_NUMBER: builtins.int
    GOTO_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    COVER_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    THREE_POINT_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    PLAYER_ARGS_FIELD_NUMBER: builtins.int
    IDX_FIELD_NUMBER: builtins.int
    AD_INFO_FIELD_NUMBER: builtins.int
    MASK_FIELD_NUMBER: builtins.int
    FROM_TYPE_FIELD_NUMBER: builtins.int
    THREE_POINT_V2_FIELD_NUMBER: builtins.int
    THREE_POINT_V3_FIELD_NUMBER: builtins.int
    DESC_BUTTON_FIELD_NUMBER: builtins.int
    THREE_POINT_V4_FIELD_NUMBER: builtins.int
    UP_ARGS_FIELD_NUMBER: builtins.int
    card_type: builtins.str
    """卡片类型"""
    card_goto: builtins.str
    """卡片跳转类型?"""
    goto: builtins.str
    """跳转类型
    av:视频稿件 mid:用户空间
    """
    param: builtins.str
    """目标参数"""
    cover: builtins.str
    """封面url"""
    title: builtins.str
    """标题"""
    uri: builtins.str
    """跳转uri"""
    @property
    def three_point(self) -> global___ThreePoint:
        """"""

    @property
    def args(self) -> global___Args:
        """"""

    @property
    def player_args(self) -> global___PlayerArgs:
        """"""
    idx: builtins.int
    """条目排位序号"""
    @property
    def ad_info(self) -> bilibili.app.card.v1.ad_pb2.AdInfo:
        """"""

    @property
    def mask(self) -> global___Mask:
        """"""
    from_type: builtins.str
    """来源标识
    recommend:推荐 operation:管理?
    """
    @property
    def three_point_v2(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ThreePointV2
    ]:
        """"""

    @property
    def three_point_v3(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ThreePointV3
    ]:
        """"""

    @property
    def desc_button(self) -> global___Button:
        """"""

    @property
    def three_point_v4(self) -> global___ThreePointV4:
        """三点v4"""

    @property
    def up_args(self) -> global___UpArgs:
        """"""

    def __init__(
        self,
        *,
        card_type: builtins.str = ...,
        card_goto: builtins.str = ...,
        goto: builtins.str = ...,
        param: builtins.str = ...,
        cover: builtins.str = ...,
        title: builtins.str = ...,
        uri: builtins.str = ...,
        three_point: global___ThreePoint | None = ...,
        args: global___Args | None = ...,
        player_args: global___PlayerArgs | None = ...,
        idx: builtins.int = ...,
        ad_info: bilibili.app.card.v1.ad_pb2.AdInfo | None = ...,
        mask: global___Mask | None = ...,
        from_type: builtins.str = ...,
        three_point_v2: (
            collections.abc.Iterable[global___ThreePointV2] | None
        ) = ...,
        three_point_v3: (
            collections.abc.Iterable[global___ThreePointV3] | None
        ) = ...,
        desc_button: global___Button | None = ...,
        three_point_v4: global___ThreePointV4 | None = ...,
        up_args: global___UpArgs | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "ad_info",
            b"ad_info",
            "args",
            b"args",
            "desc_button",
            b"desc_button",
            "mask",
            b"mask",
            "player_args",
            b"player_args",
            "three_point",
            b"three_point",
            "three_point_v4",
            b"three_point_v4",
            "up_args",
            b"up_args",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "ad_info",
            b"ad_info",
            "args",
            b"args",
            "card_goto",
            b"card_goto",
            "card_type",
            b"card_type",
            "cover",
            b"cover",
            "desc_button",
            b"desc_button",
            "from_type",
            b"from_type",
            "goto",
            b"goto",
            "idx",
            b"idx",
            "mask",
            b"mask",
            "param",
            b"param",
            "player_args",
            b"player_args",
            "three_point",
            b"three_point",
            "three_point_v2",
            b"three_point_v2",
            "three_point_v3",
            b"three_point_v3",
            "three_point_v4",
            b"three_point_v4",
            "title",
            b"title",
            "up_args",
            b"up_args",
            "uri",
            b"uri",
        ],
    ) -> None: ...

global___Base = Base

@typing_extensions.final
class Button(google.protobuf.message.Message):
    """按钮信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    SELECTED_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    EVENT_V2_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    text: builtins.str
    """文案"""
    param: builtins.str
    """参数"""
    uri: builtins.str
    """"""
    event: builtins.str
    """事件"""
    selected: builtins.int
    """"""
    type: builtins.int
    """类型"""
    event_v2: builtins.str
    """事件v2"""
    @property
    def relation(self) -> global___Relation:
        """关系信息"""

    def __init__(
        self,
        *,
        text: builtins.str = ...,
        param: builtins.str = ...,
        uri: builtins.str = ...,
        event: builtins.str = ...,
        selected: builtins.int = ...,
        type: builtins.int = ...,
        event_v2: builtins.str = ...,
        relation: global___Relation | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["relation", b"relation"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "event",
            b"event",
            "event_v2",
            b"event_v2",
            "param",
            b"param",
            "relation",
            b"relation",
            "selected",
            b"selected",
            "text",
            b"text",
            "type",
            b"type",
            "uri",
            b"uri",
        ],
    ) -> None: ...

global___Button = Button

@typing_extensions.final
class DislikeReason(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    id: builtins.int
    """"""
    name: builtins.str
    """"""
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["id", b"id", "name", b"name"],
    ) -> None: ...

global___DislikeReason = DislikeReason

@typing_extensions.final
class LikeButton(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AID_FIELD_NUMBER: builtins.int
    COUNT_FIELD_NUMBER: builtins.int
    SHOW_COUNT_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    SELECTED_FIELD_NUMBER: builtins.int
    EVENT_V2_FIELD_NUMBER: builtins.int
    Aid: builtins.int
    """"""
    count: builtins.int
    """"""
    show_count: builtins.bool
    """"""
    event: builtins.str
    """"""
    selected: builtins.int
    """"""
    event_v2: builtins.str
    """"""
    def __init__(
        self,
        *,
        Aid: builtins.int = ...,
        count: builtins.int = ...,
        show_count: builtins.bool = ...,
        event: builtins.str = ...,
        selected: builtins.int = ...,
        event_v2: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "Aid",
            b"Aid",
            "count",
            b"count",
            "event",
            b"event",
            "event_v2",
            b"event_v2",
            "selected",
            b"selected",
            "show_count",
            b"show_count",
        ],
    ) -> None: ...

global___LikeButton = LikeButton

@typing_extensions.final
class Mask(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AVATAR_FIELD_NUMBER: builtins.int
    BUTTON_FIELD_NUMBER: builtins.int
    @property
    def avatar(self) -> global___Avatar:
        """"""

    @property
    def button(self) -> global___Button:
        """"""

    def __init__(
        self,
        *,
        avatar: global___Avatar | None = ...,
        button: global___Button | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "avatar", b"avatar", "button", b"button"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "avatar", b"avatar", "button", b"button"
        ],
    ) -> None: ...

global___Mask = Mask

@typing_extensions.final
class PlayerArgs(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IS_LIVE_FIELD_NUMBER: builtins.int
    AID_FIELD_NUMBER: builtins.int
    CID_FIELD_NUMBER: builtins.int
    SUB_TYPE_FIELD_NUMBER: builtins.int
    ROOM_ID_FIELD_NUMBER: builtins.int
    EP_ID_FIELD_NUMBER: builtins.int
    IS_PREVIEW_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    SEASON_ID_FIELD_NUMBER: builtins.int
    is_live: builtins.int
    """"""
    aid: builtins.int
    """"""
    cid: builtins.int
    """"""
    sub_type: builtins.int
    """"""
    room_id: builtins.int
    """"""
    ep_id: builtins.int
    """"""
    is_preview: builtins.int
    """"""
    type: builtins.str
    """"""
    duration: builtins.int
    """"""
    season_id: builtins.int
    """"""
    def __init__(
        self,
        *,
        is_live: builtins.int = ...,
        aid: builtins.int = ...,
        cid: builtins.int = ...,
        sub_type: builtins.int = ...,
        room_id: builtins.int = ...,
        ep_id: builtins.int = ...,
        is_preview: builtins.int = ...,
        type: builtins.str = ...,
        duration: builtins.int = ...,
        season_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "aid",
            b"aid",
            "cid",
            b"cid",
            "duration",
            b"duration",
            "ep_id",
            b"ep_id",
            "is_live",
            b"is_live",
            "is_preview",
            b"is_preview",
            "room_id",
            b"room_id",
            "season_id",
            b"season_id",
            "sub_type",
            b"sub_type",
            "type",
            b"type",
        ],
    ) -> None: ...

global___PlayerArgs = PlayerArgs

@typing_extensions.final
class ReasonStyle(google.protobuf.message.Message):
    """标签框信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    TEXT_COLOR_FIELD_NUMBER: builtins.int
    BG_COLOR_FIELD_NUMBER: builtins.int
    BORDER_COLOR_FIELD_NUMBER: builtins.int
    ICON_URL_FIELD_NUMBER: builtins.int
    TEXT_COLOR_NIGHT_FIELD_NUMBER: builtins.int
    BG_COLOR_NIGHT_FIELD_NUMBER: builtins.int
    BORDER_COLOR_NIGHT_FIELD_NUMBER: builtins.int
    ICON_NIGHT_URL_FIELD_NUMBER: builtins.int
    BG_STYLE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    ICON_BG_URL_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    EVENT_V2_FIELD_NUMBER: builtins.int
    RIGHT_ICON_TYPE_FIELD_NUMBER: builtins.int
    LEFT_ICON_TYPE_FIELD_NUMBER: builtins.int
    text: builtins.str
    """文案"""
    text_color: builtins.str
    """文字颜色"""
    bg_color: builtins.str
    """背景色"""
    border_color: builtins.str
    """边框色"""
    icon_url: builtins.str
    """图标url"""
    text_color_night: builtins.str
    """文字颜色-夜间"""
    bg_color_night: builtins.str
    """背景色-夜间"""
    border_color_night: builtins.str
    """边框色-夜间"""
    icon_night_url: builtins.str
    """图标url-夜间"""
    bg_style: builtins.int
    """背景风格id
    1:无背景 2:有背景
    """
    uri: builtins.str
    """"""
    icon_bg_url: builtins.str
    """"""
    event: builtins.str
    """"""
    event_v2: builtins.str
    """"""
    right_icon_type: builtins.int
    """"""
    left_icon_type: builtins.str
    """"""
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        text_color: builtins.str = ...,
        bg_color: builtins.str = ...,
        border_color: builtins.str = ...,
        icon_url: builtins.str = ...,
        text_color_night: builtins.str = ...,
        bg_color_night: builtins.str = ...,
        border_color_night: builtins.str = ...,
        icon_night_url: builtins.str = ...,
        bg_style: builtins.int = ...,
        uri: builtins.str = ...,
        icon_bg_url: builtins.str = ...,
        event: builtins.str = ...,
        event_v2: builtins.str = ...,
        right_icon_type: builtins.int = ...,
        left_icon_type: builtins.str = ...,
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
            "event",
            b"event",
            "event_v2",
            b"event_v2",
            "icon_bg_url",
            b"icon_bg_url",
            "icon_night_url",
            b"icon_night_url",
            "icon_url",
            b"icon_url",
            "left_icon_type",
            b"left_icon_type",
            "right_icon_type",
            b"right_icon_type",
            "text",
            b"text",
            "text_color",
            b"text_color",
            "text_color_night",
            b"text_color_night",
            "uri",
            b"uri",
        ],
    ) -> None: ...

global___ReasonStyle = ReasonStyle

@typing_extensions.final
class Relation(google.protobuf.message.Message):
    """关系信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    IS_FOLLOW_FIELD_NUMBER: builtins.int
    IS_FOLLOWED_FIELD_NUMBER: builtins.int
    status: builtins.int
    """关系状态"""
    is_follow: builtins.int
    """是否关注"""
    is_followed: builtins.int
    """是否粉丝"""
    def __init__(
        self,
        *,
        status: builtins.int = ...,
        is_follow: builtins.int = ...,
        is_followed: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "is_follow",
            b"is_follow",
            "is_followed",
            b"is_followed",
            "status",
            b"status",
        ],
    ) -> None: ...

global___Relation = Relation

@typing_extensions.final
class SharePlane(google.protobuf.message.Message):
    """分享面板信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ShareToEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.bool
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.bool = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "key", b"key", "value", b"value"
            ],
        ) -> None: ...

    TITLE_FIELD_NUMBER: builtins.int
    SHARE_SUBTITLE_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    COVER_FIELD_NUMBER: builtins.int
    AID_FIELD_NUMBER: builtins.int
    BVID_FIELD_NUMBER: builtins.int
    SHARE_TO_FIELD_NUMBER: builtins.int
    AUTHOR_FIELD_NUMBER: builtins.int
    AUTHOR_ID_FIELD_NUMBER: builtins.int
    SHORT_LINK_FIELD_NUMBER: builtins.int
    PLAY_NUMBER_FIELD_NUMBER: builtins.int
    FIRST_CID_FIELD_NUMBER: builtins.int
    title: builtins.str
    """标题"""
    share_subtitle: builtins.str
    """副标贴文案"""
    desc: builtins.str
    """备注"""
    cover: builtins.str
    """封面url"""
    aid: builtins.int
    """稿件avid"""
    bvid: builtins.str
    """稿件bvid"""
    @property
    def share_to(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[
        builtins.str, builtins.bool
    ]:
        """允许分享方式"""
    author: builtins.str
    """UP主昵称"""
    author_id: builtins.int
    """UP主mid"""
    short_link: builtins.str
    """短连接"""
    play_number: builtins.str
    """播放次数文案"""
    first_cid: builtins.int
    """"""
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        share_subtitle: builtins.str = ...,
        desc: builtins.str = ...,
        cover: builtins.str = ...,
        aid: builtins.int = ...,
        bvid: builtins.str = ...,
        share_to: (
            collections.abc.Mapping[builtins.str, builtins.bool] | None
        ) = ...,
        author: builtins.str = ...,
        author_id: builtins.int = ...,
        short_link: builtins.str = ...,
        play_number: builtins.str = ...,
        first_cid: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "aid",
            b"aid",
            "author",
            b"author",
            "author_id",
            b"author_id",
            "bvid",
            b"bvid",
            "cover",
            b"cover",
            "desc",
            b"desc",
            "first_cid",
            b"first_cid",
            "play_number",
            b"play_number",
            "share_subtitle",
            b"share_subtitle",
            "share_to",
            b"share_to",
            "short_link",
            b"short_link",
            "title",
            b"title",
        ],
    ) -> None: ...

global___SharePlane = SharePlane

@typing_extensions.final
class ThreePoint(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DISLIKE_REASONS_FIELD_NUMBER: builtins.int
    FEEDBACKS_FIELD_NUMBER: builtins.int
    WATCH_LATER_FIELD_NUMBER: builtins.int
    @property
    def dislike_reasons(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___DislikeReason
    ]:
        """"""

    @property
    def feedbacks(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___DislikeReason
    ]:
        """"""
    watch_later: builtins.int
    """稍后再看"""
    def __init__(
        self,
        *,
        dislike_reasons: (
            collections.abc.Iterable[global___DislikeReason] | None
        ) = ...,
        feedbacks: (
            collections.abc.Iterable[global___DislikeReason] | None
        ) = ...,
        watch_later: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "dislike_reasons",
            b"dislike_reasons",
            "feedbacks",
            b"feedbacks",
            "watch_later",
            b"watch_later",
        ],
    ) -> None: ...

global___ThreePoint = ThreePoint

@typing_extensions.final
class ThreePointV2(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    SUBTITLE_FIELD_NUMBER: builtins.int
    REASONS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    title: builtins.str
    """"""
    subtitle: builtins.str
    """"""
    @property
    def reasons(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___DislikeReason
    ]:
        """"""
    type: builtins.str
    """"""
    id: builtins.int
    """"""
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        subtitle: builtins.str = ...,
        reasons: collections.abc.Iterable[global___DislikeReason] | None = ...,
        type: builtins.str = ...,
        id: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "id",
            b"id",
            "reasons",
            b"reasons",
            "subtitle",
            b"subtitle",
            "title",
            b"title",
            "type",
            b"type",
        ],
    ) -> None: ...

global___ThreePointV2 = ThreePointV2

@typing_extensions.final
class ThreePointV3(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    SELECTED_TITLE_FIELD_NUMBER: builtins.int
    SUBTITLE_FIELD_NUMBER: builtins.int
    REASONS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    SELECTED_FIELD_NUMBER: builtins.int
    ICON_FIELD_NUMBER: builtins.int
    SELECTED_ICON_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    DEFAULT_ID_FIELD_NUMBER: builtins.int
    title: builtins.str
    """"""
    selected_title: builtins.str
    """"""
    subtitle: builtins.str
    """"""
    @property
    def reasons(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___DislikeReason
    ]:
        """"""
    type: builtins.str
    """"""
    id: builtins.int
    """"""
    selected: builtins.int
    """"""
    icon: builtins.str
    """"""
    selected_icon: builtins.str
    """"""
    url: builtins.str
    """"""
    default_id: builtins.int
    """"""
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        selected_title: builtins.str = ...,
        subtitle: builtins.str = ...,
        reasons: collections.abc.Iterable[global___DislikeReason] | None = ...,
        type: builtins.str = ...,
        id: builtins.int = ...,
        selected: builtins.int = ...,
        icon: builtins.str = ...,
        selected_icon: builtins.str = ...,
        url: builtins.str = ...,
        default_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "default_id",
            b"default_id",
            "icon",
            b"icon",
            "id",
            b"id",
            "reasons",
            b"reasons",
            "selected",
            b"selected",
            "selected_icon",
            b"selected_icon",
            "selected_title",
            b"selected_title",
            "subtitle",
            b"subtitle",
            "title",
            b"title",
            "type",
            b"type",
            "url",
            b"url",
        ],
    ) -> None: ...

global___ThreePointV3 = ThreePointV3

@typing_extensions.final
class ThreePointV4(google.protobuf.message.Message):
    """三点v4"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHARE_PLANE_FIELD_NUMBER: builtins.int
    WATCH_LATER_FIELD_NUMBER: builtins.int
    @property
    def share_plane(self) -> global___SharePlane:
        """分享面板信息"""

    @property
    def watch_later(self) -> global___WatchLater:
        """稍后再看"""

    def __init__(
        self,
        *,
        share_plane: global___SharePlane | None = ...,
        watch_later: global___WatchLater | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "share_plane", b"share_plane", "watch_later", b"watch_later"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "share_plane", b"share_plane", "watch_later", b"watch_later"
        ],
    ) -> None: ...

global___ThreePointV4 = ThreePointV4

@typing_extensions.final
class Up(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    AVATAR_FIELD_NUMBER: builtins.int
    OFFICIAL_ICON_FIELD_NUMBER: builtins.int
    DESC_BUTTON_FIELD_NUMBER: builtins.int
    COOPERATION_FIELD_NUMBER: builtins.int
    id: builtins.int
    """"""
    name: builtins.str
    """"""
    desc: builtins.str
    """"""
    @property
    def avatar(self) -> global___Avatar:
        """"""
    official_icon: builtins.int
    """"""
    @property
    def desc_button(self) -> global___Button:
        """"""
    cooperation: builtins.str
    """"""
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        name: builtins.str = ...,
        desc: builtins.str = ...,
        avatar: global___Avatar | None = ...,
        official_icon: builtins.int = ...,
        desc_button: global___Button | None = ...,
        cooperation: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "avatar", b"avatar", "desc_button", b"desc_button"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "avatar",
            b"avatar",
            "cooperation",
            b"cooperation",
            "desc",
            b"desc",
            "desc_button",
            b"desc_button",
            "id",
            b"id",
            "name",
            b"name",
            "official_icon",
            b"official_icon",
        ],
    ) -> None: ...

global___Up = Up

@typing_extensions.final
class UpArgs(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UP_ID_FIELD_NUMBER: builtins.int
    UP_NAME_FIELD_NUMBER: builtins.int
    UP_FACE_FIELD_NUMBER: builtins.int
    SELECTED_FIELD_NUMBER: builtins.int
    up_id: builtins.int
    """"""
    up_name: builtins.str
    """"""
    up_face: builtins.str
    """"""
    selected: builtins.int
    """"""
    def __init__(
        self,
        *,
        up_id: builtins.int = ...,
        up_name: builtins.str = ...,
        up_face: builtins.str = ...,
        selected: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "selected",
            b"selected",
            "up_face",
            b"up_face",
            "up_id",
            b"up_id",
            "up_name",
            b"up_name",
        ],
    ) -> None: ...

global___UpArgs = UpArgs

@typing_extensions.final
class WatchLater(google.protobuf.message.Message):
    """稍后再看信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AID_FIELD_NUMBER: builtins.int
    BVID_FIELD_NUMBER: builtins.int
    aid: builtins.int
    """稿件avid"""
    bvid: builtins.str
    """稿件bvid"""
    def __init__(
        self,
        *,
        aid: builtins.int = ...,
        bvid: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["aid", b"aid", "bvid", b"bvid"],
    ) -> None: ...

global___WatchLater = WatchLater

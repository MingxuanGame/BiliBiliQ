"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import bilibili.app.card.v1.common_pb2
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
class SmallCoverV5(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_FIELD_NUMBER: builtins.int
    COVER_GIF_FIELD_NUMBER: builtins.int
    UP_FIELD_NUMBER: builtins.int
    COVER_RIGHT_TEXT_1_FIELD_NUMBER: builtins.int
    RIGHT_DESC_1_FIELD_NUMBER: builtins.int
    RIGHT_DESC_2_FIELD_NUMBER: builtins.int
    RCMD_REASON_STYLE_FIELD_NUMBER: builtins.int
    HOTWORD_ENTRANCE_FIELD_NUMBER: builtins.int
    CORNER_MARK_STYLE_FIELD_NUMBER: builtins.int
    RIGHT_ICON_1_FIELD_NUMBER: builtins.int
    RIGHT_ICON_2_FIELD_NUMBER: builtins.int
    LEFT_CORNER_MARK_STYLE_FIELD_NUMBER: builtins.int
    COVER_RIGHT_TEXT_CONTENT_DESCRIPTION_FIELD_NUMBER: builtins.int
    RIGHT_DESC1_CONTENT_DESCRIPTION_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
    cover_gif: builtins.str
    """"""
    @property
    def up(self) -> bilibili.app.card.v1.common_pb2.Up:
        """"""
    cover_right_text_1: builtins.str
    """封面右下角标文案"""
    right_desc_1: builtins.str
    """右侧文案1"""
    right_desc_2: builtins.str
    """右侧文案2"""
    @property
    def rcmd_reason_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """右侧推荐原因标签框"""
    @property
    def hotword_entrance(self) -> global___HotwordEntrance:
        """"""
    @property
    def corner_mark_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """直播小卡的角标"""
    right_icon_1: builtins.int
    """右侧文案1图标id"""
    right_icon_2: builtins.int
    """右侧文案2图标id"""
    @property
    def left_corner_mark_style(
        self,
    ) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """左上角角标"""
    cover_right_text_content_description: builtins.str
    """"""
    right_desc1_content_description: builtins.str
    """"""
    def __init__(
        self,
        *,
        base: bilibili.app.card.v1.common_pb2.Base | None = ...,
        cover_gif: builtins.str = ...,
        up: bilibili.app.card.v1.common_pb2.Up | None = ...,
        cover_right_text_1: builtins.str = ...,
        right_desc_1: builtins.str = ...,
        right_desc_2: builtins.str = ...,
        rcmd_reason_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        hotword_entrance: global___HotwordEntrance | None = ...,
        corner_mark_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        right_icon_1: builtins.int = ...,
        right_icon_2: builtins.int = ...,
        left_corner_mark_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        cover_right_text_content_description: builtins.str = ...,
        right_desc1_content_description: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "base",
            b"base",
            "corner_mark_style",
            b"corner_mark_style",
            "hotword_entrance",
            b"hotword_entrance",
            "left_corner_mark_style",
            b"left_corner_mark_style",
            "rcmd_reason_style",
            b"rcmd_reason_style",
            "up",
            b"up",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "base",
            b"base",
            "corner_mark_style",
            b"corner_mark_style",
            "cover_gif",
            b"cover_gif",
            "cover_right_text_1",
            b"cover_right_text_1",
            "cover_right_text_content_description",
            b"cover_right_text_content_description",
            "hotword_entrance",
            b"hotword_entrance",
            "left_corner_mark_style",
            b"left_corner_mark_style",
            "rcmd_reason_style",
            b"rcmd_reason_style",
            "right_desc1_content_description",
            b"right_desc1_content_description",
            "right_desc_1",
            b"right_desc_1",
            "right_desc_2",
            b"right_desc_2",
            "right_icon_1",
            b"right_icon_1",
            "right_icon_2",
            b"right_icon_2",
            "up",
            b"up",
        ],
    ) -> None: ...

global___SmallCoverV5 = SmallCoverV5

@typing_extensions.final
class SmallCoverV5Ad(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_FIELD_NUMBER: builtins.int
    COVER_GIF_FIELD_NUMBER: builtins.int
    UP_FIELD_NUMBER: builtins.int
    COVER_RIGHT_TEXT1_FIELD_NUMBER: builtins.int
    RIGHT_DESC1_FIELD_NUMBER: builtins.int
    RIGHT_DESC2_FIELD_NUMBER: builtins.int
    RCMD_REASON_STYLE_FIELD_NUMBER: builtins.int
    HOTWORD_ENTRANCE_FIELD_NUMBER: builtins.int
    CORNER_MARK_STYLE_FIELD_NUMBER: builtins.int
    RIGHT_ICON1_FIELD_NUMBER: builtins.int
    RIGHT_ICON2_FIELD_NUMBER: builtins.int
    LEFT_CORNER_MARK_STYLE_FIELD_NUMBER: builtins.int
    COVER_RIGHT_TEXT_CONTENT_DESCRIPTION_FIELD_NUMBER: builtins.int
    RIGHT_DESC1_CONTENT_DESCRIPTION_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """"""
    cover_gif: builtins.str
    """"""
    @property
    def up(self) -> bilibili.app.card.v1.common_pb2.Up:
        """"""
    cover_right_text1: builtins.str
    """"""
    right_desc1: builtins.str
    """"""
    right_desc2: builtins.str
    """"""
    @property
    def rcmd_reason_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
    @property
    def hotword_entrance(self) -> global___HotwordEntrance:
        """"""
    @property
    def corner_mark_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
    right_icon1: builtins.int
    """"""
    right_icon2: builtins.int
    """"""
    @property
    def left_corner_mark_style(
        self,
    ) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
    cover_right_text_content_description: builtins.str
    """"""
    right_desc1_content_description: builtins.str
    """"""
    def __init__(
        self,
        *,
        base: bilibili.app.card.v1.common_pb2.Base | None = ...,
        cover_gif: builtins.str = ...,
        up: bilibili.app.card.v1.common_pb2.Up | None = ...,
        cover_right_text1: builtins.str = ...,
        right_desc1: builtins.str = ...,
        right_desc2: builtins.str = ...,
        rcmd_reason_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        hotword_entrance: global___HotwordEntrance | None = ...,
        corner_mark_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        right_icon1: builtins.int = ...,
        right_icon2: builtins.int = ...,
        left_corner_mark_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        cover_right_text_content_description: builtins.str = ...,
        right_desc1_content_description: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "base",
            b"base",
            "corner_mark_style",
            b"corner_mark_style",
            "hotword_entrance",
            b"hotword_entrance",
            "left_corner_mark_style",
            b"left_corner_mark_style",
            "rcmd_reason_style",
            b"rcmd_reason_style",
            "up",
            b"up",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "base",
            b"base",
            "corner_mark_style",
            b"corner_mark_style",
            "cover_gif",
            b"cover_gif",
            "cover_right_text1",
            b"cover_right_text1",
            "cover_right_text_content_description",
            b"cover_right_text_content_description",
            "hotword_entrance",
            b"hotword_entrance",
            "left_corner_mark_style",
            b"left_corner_mark_style",
            "rcmd_reason_style",
            b"rcmd_reason_style",
            "right_desc1",
            b"right_desc1",
            "right_desc1_content_description",
            b"right_desc1_content_description",
            "right_desc2",
            b"right_desc2",
            "right_icon1",
            b"right_icon1",
            "right_icon2",
            b"right_icon2",
            "up",
            b"up",
        ],
    ) -> None: ...

global___SmallCoverV5Ad = SmallCoverV5Ad

@typing_extensions.final
class HotwordEntrance(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOTWORD_ID_FIELD_NUMBER: builtins.int
    HOT_TEXT_FIELD_NUMBER: builtins.int
    H5_URL_FIELD_NUMBER: builtins.int
    ICON_FIELD_NUMBER: builtins.int
    hotword_id: builtins.int
    """"""
    hot_text: builtins.str
    """"""
    h5_url: builtins.str
    """"""
    icon: builtins.str
    """"""
    def __init__(
        self,
        *,
        hotword_id: builtins.int = ...,
        hot_text: builtins.str = ...,
        h5_url: builtins.str = ...,
        icon: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "h5_url",
            b"h5_url",
            "hot_text",
            b"hot_text",
            "hotword_id",
            b"hotword_id",
            "icon",
            b"icon",
        ],
    ) -> None: ...

global___HotwordEntrance = HotwordEntrance

@typing_extensions.final
class LargeCoverV1(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_FIELD_NUMBER: builtins.int
    COVER_GIF_FIELD_NUMBER: builtins.int
    AVATAR_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_1_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_2_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_3_FIELD_NUMBER: builtins.int
    COVER_BADGE_FIELD_NUMBER: builtins.int
    TOP_RCMD_REASON_FIELD_NUMBER: builtins.int
    BOTTOM_RCMD_REASON_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    OFFICIAL_ICON_FIELD_NUMBER: builtins.int
    CAN_PLAY_FIELD_NUMBER: builtins.int
    TOP_RCMD_REASON_STYLE_FIELD_NUMBER: builtins.int
    BOTTOM_RCMD_REASON_STYLE_FIELD_NUMBER: builtins.int
    RCMD_REASON_STYLE_V2_FIELD_NUMBER: builtins.int
    LEFT_COVER_BADGE_STYLE_FIELD_NUMBER: builtins.int
    RIGHT_COVER_BADGE_STYLE_FIELD_NUMBER: builtins.int
    COVER_BADGE_2_FIELD_NUMBER: builtins.int
    LIKE_BUTTON_FIELD_NUMBER: builtins.int
    TITLE_SINGLE_LINE_FIELD_NUMBER: builtins.int
    COVER_RIGHT_TEXT_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
    cover_gif: builtins.str
    """"""
    @property
    def avatar(self) -> bilibili.app.card.v1.common_pb2.Avatar:
        """"""
    cover_left_text_1: builtins.str
    """"""
    cover_left_text_2: builtins.str
    """"""
    cover_left_text_3: builtins.str
    """"""
    cover_badge: builtins.str
    """"""
    top_rcmd_reason: builtins.str
    """"""
    bottom_rcmd_reason: builtins.str
    """"""
    desc: builtins.str
    """"""
    official_icon: builtins.int
    """"""
    can_play: builtins.int
    """"""
    @property
    def top_rcmd_reason_style(
        self,
    ) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
    @property
    def bottom_rcmd_reason_style(
        self,
    ) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
    @property
    def rcmd_reason_style_v2(
        self,
    ) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
    @property
    def left_cover_badge_style(
        self,
    ) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
    @property
    def right_cover_badge_style(
        self,
    ) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
    cover_badge_2: builtins.str
    """"""
    @property
    def like_button(self) -> bilibili.app.card.v1.common_pb2.LikeButton:
        """"""
    title_single_line: builtins.int
    """"""
    cover_right_text: builtins.str
    """"""
    def __init__(
        self,
        *,
        base: bilibili.app.card.v1.common_pb2.Base | None = ...,
        cover_gif: builtins.str = ...,
        avatar: bilibili.app.card.v1.common_pb2.Avatar | None = ...,
        cover_left_text_1: builtins.str = ...,
        cover_left_text_2: builtins.str = ...,
        cover_left_text_3: builtins.str = ...,
        cover_badge: builtins.str = ...,
        top_rcmd_reason: builtins.str = ...,
        bottom_rcmd_reason: builtins.str = ...,
        desc: builtins.str = ...,
        official_icon: builtins.int = ...,
        can_play: builtins.int = ...,
        top_rcmd_reason_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        bottom_rcmd_reason_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        rcmd_reason_style_v2: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        left_cover_badge_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        right_cover_badge_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        cover_badge_2: builtins.str = ...,
        like_button: bilibili.app.card.v1.common_pb2.LikeButton | None = ...,
        title_single_line: builtins.int = ...,
        cover_right_text: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "avatar",
            b"avatar",
            "base",
            b"base",
            "bottom_rcmd_reason_style",
            b"bottom_rcmd_reason_style",
            "left_cover_badge_style",
            b"left_cover_badge_style",
            "like_button",
            b"like_button",
            "rcmd_reason_style_v2",
            b"rcmd_reason_style_v2",
            "right_cover_badge_style",
            b"right_cover_badge_style",
            "top_rcmd_reason_style",
            b"top_rcmd_reason_style",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "avatar",
            b"avatar",
            "base",
            b"base",
            "bottom_rcmd_reason",
            b"bottom_rcmd_reason",
            "bottom_rcmd_reason_style",
            b"bottom_rcmd_reason_style",
            "can_play",
            b"can_play",
            "cover_badge",
            b"cover_badge",
            "cover_badge_2",
            b"cover_badge_2",
            "cover_gif",
            b"cover_gif",
            "cover_left_text_1",
            b"cover_left_text_1",
            "cover_left_text_2",
            b"cover_left_text_2",
            "cover_left_text_3",
            b"cover_left_text_3",
            "cover_right_text",
            b"cover_right_text",
            "desc",
            b"desc",
            "left_cover_badge_style",
            b"left_cover_badge_style",
            "like_button",
            b"like_button",
            "official_icon",
            b"official_icon",
            "rcmd_reason_style_v2",
            b"rcmd_reason_style_v2",
            "right_cover_badge_style",
            b"right_cover_badge_style",
            "title_single_line",
            b"title_single_line",
            "top_rcmd_reason",
            b"top_rcmd_reason",
            "top_rcmd_reason_style",
            b"top_rcmd_reason_style",
        ],
    ) -> None: ...

global___LargeCoverV1 = LargeCoverV1

@typing_extensions.final
class ThreeItemAllV2(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_FIELD_NUMBER: builtins.int
    TOP_RCMD_REASON_STYLE_FIELD_NUMBER: builtins.int
    ITEM_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
    @property
    def top_rcmd_reason_style(
        self,
    ) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
    @property
    def item(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___TwoItemHV1Item
    ]:
        """"""
    def __init__(
        self,
        *,
        base: bilibili.app.card.v1.common_pb2.Base | None = ...,
        top_rcmd_reason_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        item: collections.abc.Iterable[global___TwoItemHV1Item] | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "base", b"base", "top_rcmd_reason_style", b"top_rcmd_reason_style"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "base",
            b"base",
            "item",
            b"item",
            "top_rcmd_reason_style",
            b"top_rcmd_reason_style",
        ],
    ) -> None: ...

global___ThreeItemAllV2 = ThreeItemAllV2

@typing_extensions.final
class TwoItemHV1Item(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    COVER_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    GOTO_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_1_FIELD_NUMBER: builtins.int
    COVER_LEFT_ICON_1_FIELD_NUMBER: builtins.int
    COVER_RIGHT_TEXT_FIELD_NUMBER: builtins.int
    title: builtins.str
    """"""
    cover: builtins.str
    """"""
    uri: builtins.str
    """"""
    param: builtins.str
    """"""
    @property
    def args(self) -> bilibili.app.card.v1.common_pb2.Args:
        """"""
    goto: builtins.str
    """"""
    cover_left_text_1: builtins.str
    """"""
    cover_left_icon_1: builtins.int
    """"""
    cover_right_text: builtins.str
    """"""
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        cover: builtins.str = ...,
        uri: builtins.str = ...,
        param: builtins.str = ...,
        args: bilibili.app.card.v1.common_pb2.Args | None = ...,
        goto: builtins.str = ...,
        cover_left_text_1: builtins.str = ...,
        cover_left_icon_1: builtins.int = ...,
        cover_right_text: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["args", b"args"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "args",
            b"args",
            "cover",
            b"cover",
            "cover_left_icon_1",
            b"cover_left_icon_1",
            "cover_left_text_1",
            b"cover_left_text_1",
            "cover_right_text",
            b"cover_right_text",
            "goto",
            b"goto",
            "param",
            b"param",
            "title",
            b"title",
            "uri",
            b"uri",
        ],
    ) -> None: ...

global___TwoItemHV1Item = TwoItemHV1Item

@typing_extensions.final
class RcmdOneItem(google.protobuf.message.Message):
    """推荐"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_FIELD_NUMBER: builtins.int
    TOPRCMDREASONSTYLE_FIELD_NUMBER: builtins.int
    ITEM_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
    @property
    def topRcmdReasonStyle(
        self,
    ) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """标签框信息"""
    @property
    def item(self) -> global___SmallCoverRcmdItem:
        """小封面推荐内容信息"""
    def __init__(
        self,
        *,
        base: bilibili.app.card.v1.common_pb2.Base | None = ...,
        topRcmdReasonStyle: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
        item: global___SmallCoverRcmdItem | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "base",
            b"base",
            "item",
            b"item",
            "topRcmdReasonStyle",
            b"topRcmdReasonStyle",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "base",
            b"base",
            "item",
            b"item",
            "topRcmdReasonStyle",
            b"topRcmdReasonStyle",
        ],
    ) -> None: ...

global___RcmdOneItem = RcmdOneItem

@typing_extensions.final
class SmallCoverRcmdItem(google.protobuf.message.Message):
    """小封面推荐内容信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    COVER_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    GOTO_FIELD_NUMBER: builtins.int
    COVERRIGHTTEXT1_FIELD_NUMBER: builtins.int
    RIGHTDESC1_FIELD_NUMBER: builtins.int
    RIGHTDESC2_FIELD_NUMBER: builtins.int
    COVERGIF_FIELD_NUMBER: builtins.int
    RIGHTICON1_FIELD_NUMBER: builtins.int
    RIGHTICON2_FIELD_NUMBER: builtins.int
    COVER_RIGHT_TEXT_CONTENT_DESCRIPTION_FIELD_NUMBER: builtins.int
    RIGHT_DESC1_CONTENT_DESCRIPTION_FIELD_NUMBER: builtins.int
    title: builtins.str
    """标题"""
    cover: builtins.str
    """封面url"""
    uri: builtins.str
    """跳转uri"""
    param: builtins.str
    """参数"""
    goto: builtins.str
    """跳转类型
    av:视频稿件
    """
    coverRightText1: builtins.str
    """封面右下角标文案"""
    rightDesc1: builtins.str
    """右侧文案1"""
    rightDesc2: builtins.str
    """右侧文案2"""
    coverGif: builtins.str
    """"""
    rightIcon1: builtins.int
    """右侧文案1图标id"""
    rightIcon2: builtins.int
    """右侧文案2图标id"""
    cover_right_text_content_description: builtins.str
    """"""
    right_desc1_content_description: builtins.str
    """"""
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        cover: builtins.str = ...,
        uri: builtins.str = ...,
        param: builtins.str = ...,
        goto: builtins.str = ...,
        coverRightText1: builtins.str = ...,
        rightDesc1: builtins.str = ...,
        rightDesc2: builtins.str = ...,
        coverGif: builtins.str = ...,
        rightIcon1: builtins.int = ...,
        rightIcon2: builtins.int = ...,
        cover_right_text_content_description: builtins.str = ...,
        right_desc1_content_description: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "cover",
            b"cover",
            "coverGif",
            b"coverGif",
            "coverRightText1",
            b"coverRightText1",
            "cover_right_text_content_description",
            b"cover_right_text_content_description",
            "goto",
            b"goto",
            "param",
            b"param",
            "rightDesc1",
            b"rightDesc1",
            "rightDesc2",
            b"rightDesc2",
            "rightIcon1",
            b"rightIcon1",
            "rightIcon2",
            b"rightIcon2",
            "right_desc1_content_description",
            b"right_desc1_content_description",
            "title",
            b"title",
            "uri",
            b"uri",
        ],
    ) -> None: ...

global___SmallCoverRcmdItem = SmallCoverRcmdItem

@typing_extensions.final
class ThreeItemV1(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_FIELD_NUMBER: builtins.int
    TITLEICON_FIELD_NUMBER: builtins.int
    MOREURI_FIELD_NUMBER: builtins.int
    MORETEXT_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
    titleIcon: builtins.int
    """"""
    moreUri: builtins.str
    """"""
    moreText: builtins.str
    """"""
    @property
    def items(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ThreeItemV1Item
    ]:
        """"""
    def __init__(
        self,
        *,
        base: bilibili.app.card.v1.common_pb2.Base | None = ...,
        titleIcon: builtins.int = ...,
        moreUri: builtins.str = ...,
        moreText: builtins.str = ...,
        items: collections.abc.Iterable[global___ThreeItemV1Item] | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["base", b"base"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "base",
            b"base",
            "items",
            b"items",
            "moreText",
            b"moreText",
            "moreUri",
            b"moreUri",
            "titleIcon",
            b"titleIcon",
        ],
    ) -> None: ...

global___ThreeItemV1 = ThreeItemV1

@typing_extensions.final
class ThreeItemV1Item(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_FIELD_NUMBER: builtins.int
    COVERLEFTTEXT_FIELD_NUMBER: builtins.int
    COVERLEFTICON_FIELD_NUMBER: builtins.int
    DESC1_FIELD_NUMBER: builtins.int
    DESC2_FIELD_NUMBER: builtins.int
    BADGE_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
    coverLeftText: builtins.str
    """"""
    coverLeftIcon: builtins.int
    """"""
    desc1: builtins.str
    """"""
    desc2: builtins.str
    """"""
    badge: builtins.str
    """"""
    def __init__(
        self,
        *,
        base: bilibili.app.card.v1.common_pb2.Base | None = ...,
        coverLeftText: builtins.str = ...,
        coverLeftIcon: builtins.int = ...,
        desc1: builtins.str = ...,
        desc2: builtins.str = ...,
        badge: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["base", b"base"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "badge",
            b"badge",
            "base",
            b"base",
            "coverLeftIcon",
            b"coverLeftIcon",
            "coverLeftText",
            b"coverLeftText",
            "desc1",
            b"desc1",
            "desc2",
            b"desc2",
        ],
    ) -> None: ...

global___ThreeItemV1Item = ThreeItemV1Item

@typing_extensions.final
class HotTopicItem(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COVER_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    PARAM_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    cover: builtins.str
    """"""
    uri: builtins.str
    """"""
    param: builtins.str
    """"""
    name: builtins.str
    """"""
    def __init__(
        self,
        *,
        cover: builtins.str = ...,
        uri: builtins.str = ...,
        param: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "cover",
            b"cover",
            "name",
            b"name",
            "param",
            b"param",
            "uri",
            b"uri",
        ],
    ) -> None: ...

global___HotTopicItem = HotTopicItem

@typing_extensions.final
class HotTopic(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
    desc: builtins.str
    """"""
    @property
    def items(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___HotTopicItem
    ]:
        """"""
    def __init__(
        self,
        *,
        base: bilibili.app.card.v1.common_pb2.Base | None = ...,
        desc: builtins.str = ...,
        items: collections.abc.Iterable[global___HotTopicItem] | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["base", b"base"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "base", b"base", "desc", b"desc", "items", b"items"
        ],
    ) -> None: ...

global___HotTopic = HotTopic

@typing_extensions.final
class DynamicHot(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_FIELD_NUMBER: builtins.int
    TOP_LEFT_TITLE_FIELD_NUMBER: builtins.int
    DESC1_FIELD_NUMBER: builtins.int
    DESC2_FIELD_NUMBER: builtins.int
    MORE_URI_FIELD_NUMBER: builtins.int
    MORE_TEXT_FIELD_NUMBER: builtins.int
    COVERS_FIELD_NUMBER: builtins.int
    COVER_RIGHT_TEXT_FIELD_NUMBER: builtins.int
    TOP_RCMD_REASON_STYLE_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
    top_left_title: builtins.str
    """"""
    desc1: builtins.str
    """"""
    desc2: builtins.str
    """"""
    more_uri: builtins.str
    """"""
    more_text: builtins.str
    """"""
    @property
    def covers(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.str
    ]:
        """"""
    cover_right_text: builtins.str
    """"""
    @property
    def top_rcmd_reason_style(
        self,
    ) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
    def __init__(
        self,
        *,
        base: bilibili.app.card.v1.common_pb2.Base | None = ...,
        top_left_title: builtins.str = ...,
        desc1: builtins.str = ...,
        desc2: builtins.str = ...,
        more_uri: builtins.str = ...,
        more_text: builtins.str = ...,
        covers: collections.abc.Iterable[builtins.str] | None = ...,
        cover_right_text: builtins.str = ...,
        top_rcmd_reason_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "base", b"base", "top_rcmd_reason_style", b"top_rcmd_reason_style"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "base",
            b"base",
            "cover_right_text",
            b"cover_right_text",
            "covers",
            b"covers",
            "desc1",
            b"desc1",
            "desc2",
            b"desc2",
            "more_text",
            b"more_text",
            "more_uri",
            b"more_uri",
            "top_left_title",
            b"top_left_title",
            "top_rcmd_reason_style",
            b"top_rcmd_reason_style",
        ],
    ) -> None: ...

global___DynamicHot = DynamicHot

@typing_extensions.final
class MiddleCoverV3(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_FIELD_NUMBER: builtins.int
    DESC1_FIELD_NUMBER: builtins.int
    DESC2_FIELD_NUMBER: builtins.int
    COVER_BADGE_STYLE_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
    desc1: builtins.str
    """"""
    desc2: builtins.str
    """"""
    @property
    def cover_badge_style(self) -> bilibili.app.card.v1.common_pb2.ReasonStyle:
        """"""
    def __init__(
        self,
        *,
        base: bilibili.app.card.v1.common_pb2.Base | None = ...,
        desc1: builtins.str = ...,
        desc2: builtins.str = ...,
        cover_badge_style: bilibili.app.card.v1.common_pb2.ReasonStyle
        | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "base", b"base", "cover_badge_style", b"cover_badge_style"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "base",
            b"base",
            "cover_badge_style",
            b"cover_badge_style",
            "desc1",
            b"desc1",
            "desc2",
            b"desc2",
        ],
    ) -> None: ...

global___MiddleCoverV3 = MiddleCoverV3

@typing_extensions.final
class LargeCoverV4(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_1_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_2_FIELD_NUMBER: builtins.int
    COVER_LEFT_TEXT_3_FIELD_NUMBER: builtins.int
    COVER_BADGE_FIELD_NUMBER: builtins.int
    CAN_PLAY_FIELD_NUMBER: builtins.int
    UP_FIELD_NUMBER: builtins.int
    SHORT_LINK_FIELD_NUMBER: builtins.int
    SHARE_SUBTITLE_FIELD_NUMBER: builtins.int
    PLAY_NUMBER_FIELD_NUMBER: builtins.int
    BVID_FIELD_NUMBER: builtins.int
    SUB_PARAM_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
    cover_left_text_1: builtins.str
    """"""
    cover_left_text_2: builtins.str
    """"""
    cover_left_text_3: builtins.str
    """"""
    cover_badge: builtins.str
    """"""
    can_play: builtins.int
    """"""
    @property
    def up(self) -> bilibili.app.card.v1.common_pb2.Up:
        """"""
    short_link: builtins.str
    """"""
    share_subtitle: builtins.str
    """"""
    play_number: builtins.str
    """"""
    bvid: builtins.str
    """"""
    sub_param: builtins.str
    """"""
    def __init__(
        self,
        *,
        base: bilibili.app.card.v1.common_pb2.Base | None = ...,
        cover_left_text_1: builtins.str = ...,
        cover_left_text_2: builtins.str = ...,
        cover_left_text_3: builtins.str = ...,
        cover_badge: builtins.str = ...,
        can_play: builtins.int = ...,
        up: bilibili.app.card.v1.common_pb2.Up | None = ...,
        short_link: builtins.str = ...,
        share_subtitle: builtins.str = ...,
        play_number: builtins.str = ...,
        bvid: builtins.str = ...,
        sub_param: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal["base", b"base", "up", b"up"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "base",
            b"base",
            "bvid",
            b"bvid",
            "can_play",
            b"can_play",
            "cover_badge",
            b"cover_badge",
            "cover_left_text_1",
            b"cover_left_text_1",
            "cover_left_text_2",
            b"cover_left_text_2",
            "cover_left_text_3",
            b"cover_left_text_3",
            "play_number",
            b"play_number",
            "share_subtitle",
            b"share_subtitle",
            "short_link",
            b"short_link",
            "sub_param",
            b"sub_param",
            "up",
            b"up",
        ],
    ) -> None: ...

global___LargeCoverV4 = LargeCoverV4

@typing_extensions.final
class PopularTopEntrance(google.protobuf.message.Message):
    """热门列表顶部按钮"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    @property
    def base(self) -> bilibili.app.card.v1.common_pb2.Base:
        """条目基本信息"""
    @property
    def items(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___EntranceItem
    ]:
        """按钮项"""
    def __init__(
        self,
        *,
        base: bilibili.app.card.v1.common_pb2.Base | None = ...,
        items: collections.abc.Iterable[global___EntranceItem] | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["base", b"base"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "base", b"base", "items", b"items"
        ],
    ) -> None: ...

global___PopularTopEntrance = PopularTopEntrance

@typing_extensions.final
class EntranceItem(google.protobuf.message.Message):
    """热门列表按钮信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GOTO_FIELD_NUMBER: builtins.int
    ICON_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    MODULE_ID_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    ENTRANCE_ID_FIELD_NUMBER: builtins.int
    BUBBLE_FIELD_NUMBER: builtins.int
    ENTRANCE_TYPE_FIELD_NUMBER: builtins.int
    goto: builtins.str
    """跳转类型"""
    icon: builtins.str
    """图标url"""
    title: builtins.str
    """标题"""
    module_id: builtins.str
    """入口模块id"""
    uri: builtins.str
    """跳转uri"""
    entrance_id: builtins.int
    """入口id"""
    @property
    def bubble(self) -> global___Bubble:
        """气泡信息"""
    entrance_type: builtins.int
    """入口类型
    1:代表分品类热门
    """
    def __init__(
        self,
        *,
        goto: builtins.str = ...,
        icon: builtins.str = ...,
        title: builtins.str = ...,
        module_id: builtins.str = ...,
        uri: builtins.str = ...,
        entrance_id: builtins.int = ...,
        bubble: global___Bubble | None = ...,
        entrance_type: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["bubble", b"bubble"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "bubble",
            b"bubble",
            "entrance_id",
            b"entrance_id",
            "entrance_type",
            b"entrance_type",
            "goto",
            b"goto",
            "icon",
            b"icon",
            "module_id",
            b"module_id",
            "title",
            b"title",
            "uri",
            b"uri",
        ],
    ) -> None: ...

global___EntranceItem = EntranceItem

@typing_extensions.final
class Bubble(google.protobuf.message.Message):
    """气泡信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUBBLE_CONTENT_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    STIME_FIELD_NUMBER: builtins.int
    bubble_content: builtins.str
    """文案"""
    version: builtins.int
    """版本"""
    stime: builtins.int
    """起始时间"""
    def __init__(
        self,
        *,
        bubble_content: builtins.str = ...,
        version: builtins.int = ...,
        stime: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "bubble_content",
            b"bubble_content",
            "stime",
            b"stime",
            "version",
            b"version",
        ],
    ) -> None: ...

global___Bubble = Bubble
import json
from queue import Empty, SimpleQueue
from typing import Any, Dict, List, Literal, Optional

from pydantic import Field, BaseModel, validator


def str_to_message(v, values):
    return parse_message(v, values["e_infos"], values["msg_type"] == 5)


class MessageContent(BaseModel):
    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError


class Emoji(MessageContent):
    text: str
    """表情名称"""
    url: str
    """表情链接"""
    size: int
    """表情尺寸"""

    def to_dict(self) -> Dict[str, Any]:
        return {"content": self.text}

    def __str__(self) -> str:
        return f"{self.text}"


class Text(MessageContent):
    text: str
    """消息内容"""

    def to_dict(self) -> Dict[str, Any]:
        return {"content": self.text}

    def __str__(self) -> str:
        return self.text


class Image(MessageContent):
    width: int
    """图片宽度"""
    height: int
    """图片高度"""
    image_type: str = Field(..., alias='imageType')
    """图片类型"""
    original: bool
    """是否为原图"""
    size: int
    """图片尺寸"""
    url: str
    """图片 URL"""

    def __str__(self) -> str:
        return "[图片]"

    def to_dict(self) -> Dict[str, Any]:
        return self.dict(by_alias=True)


class Module(BaseModel):
    title: str
    """标题"""
    detail: str
    """内容"""


class JumpUriConfig(BaseModel):
    all_uri: Optional[str] = None
    """跳转链接"""
    text: str
    """跳转文字内容"""


class Notice(MessageContent):
    title: str
    """通知标题"""
    text: str
    """通知内容"""
    modules: List[Module]
    """子内容"""
    jump_text: str
    """跳转文字内容 1"""
    jump_text_2: str
    """跳转文字内容 2"""
    jump_text_3: str
    """跳转文字内容 3"""
    jump_uri: str
    """跳转链接 1"""
    jump_uri_2: str
    """跳转链接 2"""
    jump_uri_3: str
    """跳转链接 3"""
    jump_uri_config: JumpUriConfig
    """跳转设置 1，基本同 jump_text+jump_uri"""
    jump_uri_2_config: JumpUriConfig
    """跳转设置 2，基本同 jump_text+jump_uri"""
    jump_uri_3_config: JumpUriConfig
    """跳转设置 3，基本同 jump_text+jump_uri"""

    def to_dict(self) -> Dict[str, Any]:
        # 此方法不应该被使用
        return self.dict()

    def __str__(self) -> str:
        return self.title


class Recall(MessageContent):
    msg_key: int
    """消息 ID"""

    def to_dict(self) -> Dict[str, Any]:
        # 撤回的 content 为字符串，非 JSON
        return {}


def parse_message(
    source: str,
    e_infos: Optional[List[Emoji]] = None,
    is_recall: bool = False,
    is_raw: bool = False,
) -> List[MessageContent]:
    if isinstance(source, list):
        return source
    if is_recall:
        # 撤回
        return [Recall(msg_key=int(source))]
    try:
        if not is_raw:
            content = json.loads(source)
            if "imageType" in content:
                # 图片
                return [Image.parse_obj(content)]
            elif "modules" in content:
                return [Notice.parse_obj(content)]
            content_str = content["content"]
        else:
            # is_raw 防止注入
            # e.g. source='{"content":"test"}'
            # output: [Text(text="test")]
            content_str = source
    except json.JSONDecodeError:
        # 回复的情况
        content_str = source

    # 文字 表情
    message = []
    cache_str = ""
    queue = SimpleQueue()
    for s in content_str:
        if s not in {"[", "]"}:
            cache_str += s
        elif s == "]":
            try:
                queue.get_nowait()
                # 这时 cache_str 即为表情名称
                if e_infos is None:
                    message.append(Text(text="[]"))
                else:
                    for face in e_infos:
                        if f"[{cache_str}]" == face.text:
                            message.append(face)
                            cache_str = ""
                            break
                    else:
                        message.append(Text(text="[]"))
            except Empty:
                cache_str += "]"
        else:  # s == "["
            message.append(Text(text=cache_str))
            cache_str = ""
            queue.put(1)
    message.append(Text(text=cache_str))

    # 去除空消息
    for i, m in enumerate(message):
        if isinstance(m, Text) and not m.text:
            message.pop(i)
    return message


class Message(BaseModel):
    e_infos: Optional[List[Emoji]] = None
    """表情数组"""
    sender_uid: int
    """发送者 UID"""
    receiver_type: int
    """接收类型，1为用户，2为粉丝团"""
    receiver_id: int
    """接收者 UID"""
    msg_type: Literal[1, 2, 5, 10, 12, 13]
    """
    消息类型
    1:文字消息
    2:图片消息
    5:撤回的消息
    12、13:通知
    """
    content: List[MessageContent]
    """消息内容"""
    msg_seqno: int
    """消息序号"""
    timestamp: int
    """消息发送时间戳"""
    notify_code: str
    """通知类型，非通知类型为空"""
    msg_key: int
    """消息 ID"""
    # new_face_version: int

    _ = validator("content", pre=True, allow_reuse=True)(str_to_message)


class Messages(BaseModel):
    messages: Optional[List[Message]] = None
    """消息数据"""
    has_more: bool
    """是否还有更多消息"""
    min_seqno: int
    """最早的消息的消息序号，以当前获取的最早为准"""
    max_seqno: int
    """最后一条消息的消息序号"""

    def __init__(self, **data: Any) -> None:
        if msg := data["messages"]:
            for i in msg:
                i["e_infos"] = data.get("e_infos")
        super().__init__(**data)


class Session(BaseModel):
    talker_id: int
    """发送者 UID"""
    session_type: int
    """接收类型，1为用户，2为粉丝团"""
    is_follow: int
    """是否关注"""
    # is_dnd: int
    session_ts: int
    """最后一条消息的时间"""
    unread_count: int
    """未读消息数"""
    last_msg: Message
    """最后一条消息"""
    max_seqno: int
    """最后一条消息的消息序号"""


class Sessions(BaseModel):
    session_list: List[Session]
    """会话列表"""
    has_more: bool
    """是否还有更多会话"""

    # show_level: bool
    def __init__(self, **data: Any) -> None:
        for i in data["session_list"]:
            i["last_msg"]["e_infos"] = data["e_infos"]
        super().__init__(**data)


class Cursor(BaseModel):
    is_end: bool
    """是否到达最后（是否还有未拉取的项目）"""
    id: int
    """本次拉取最后一条项目的 ID"""
    time: int
    """本次拉取最后一条项目的时间"""


class User(BaseModel):
    mid: int
    """用户 UID"""
    nickname: str
    """名称"""
    avatar: str
    """头像 URL"""


class SourceItem(BaseModel):
    type: str
    """
    回复类型
    reply：回复
    video：视频评论
    dynamic：动态评论
    """
    business_id: int
    """
    所属项目类型
    1：视频
    17：动态
    """
    business: str
    """项目类型"""
    title: str
    """
    标题
    动态/评论：动态/评论内容
    视频：视频标题
    """
    image: str
    """
    图片
    视频：封面
    动态：（如果有图）第一张图片的 URL
    其他情况为空
    """
    uri: str
    """所属项目 URL"""
    native_uri: str
    """BiliBili native URL"""
    # topic_details: List


class ReplyItem(SourceItem):
    subject_id: int
    """
    所属项目 ID
    动态：动态 ID
    视频：AV 号
    """
    root_id: int
    """父项目 ID，仅回复"""
    desc: str
    """简介（仅视频）"""
    source_id: int
    """项目 ID"""
    target_id: int
    """目标 ID，仅回复"""
    source_content: List[MessageContent]
    """回复内容"""
    root_reply_content: List[MessageContent]
    """父项回复内容，仅回复（同 `title`）"""
    target_reply_content: List[MessageContent]
    """目标回复内容，仅回复"""
    like_state: bool
    """是否已赞"""
    at_details: List[User]
    """@的用户"""


class Reply(BaseModel):
    id: int
    """当前回复列表 ID（不同于 `ReplyItem` 的 ID）"""
    user: User
    """回复用户"""
    item: ReplyItem
    """回复详情"""
    counts: int
    """发表数量"""
    is_multi: int
    """是否多人"""
    reply_time: int
    """回复时间戳"""


class Replies(BaseModel):
    e_infos: List[Emoji]
    """表情数组"""
    cursor: Cursor
    """记录信息"""
    items: List[Reply]
    """回复"""

    def __init__(self, **data: Any) -> None:
        for i in data["items"]:
            for key in (
                "root_reply_content",
                "source_content",
                "target_reply_content",
            ):
                i["item"][key] = parse_message(
                    i["item"][key], data["e_infos"], is_raw=True
                )
        super().__init__(**data)


class AtItem(SourceItem):
    subject_id: int
    """
    所属项目 ID
    动态：动态 ID
    视频：AV 号
    """
    root_id: int
    """父项目 ID，仅回复"""
    source_id: int
    """项目 ID"""
    target_id: int
    """目标 ID，仅回复"""
    source_content: List[MessageContent]
    """回复内容"""
    at_details: List[User]
    """@的用户"""


class At(BaseModel):
    id: int
    """当前 @ 列表 ID（不同于 `AtItem` 的 ID）"""
    user: User
    """发送 @ 的用户"""
    item: AtItem
    """@ 详情"""
    at_time: int
    """@ 的时间"""


class Ats(BaseModel):
    e_infos: List[Emoji]
    """表情数组"""
    cursor: Cursor
    """记录信息"""
    items: List[At]
    """@"""

    def __init__(self, **data: Any) -> None:
        for i in data["items"]:
            i["item"]["source_content"] = parse_message(
                i["item"]["source_content"], data["e_infos"], is_raw=True
            )
        super().__init__(**data)


class LikeItem(SourceItem):
    item_id: int
    """目标 ID，同 `target_id`"""
    # reply_business_id: int
    # like_business_id: int
    # detail_name: str  # 点击的信息
    desc: str
    """简介（仅视频）"""
    ctime: int
    """此项目被创建的时间"""


class Like(BaseModel):
    id: int
    """当前点赞列表 ID"""
    users: List[User]
    """点赞的用户"""
    item: LikeItem
    """点赞详情"""
    counts: int
    """点赞数"""
    like_time: int
    """点赞的时间"""


class Likes(BaseModel):
    latest: List[Like]
    cursor: Cursor
    items: List[Like]

    def __init__(self, **data: Any) -> None:
        data["items"] = data["total"]["items"]
        data["cursor"] = data["total"]["cursor"]
        data["latest"] = data["latest"]["items"]
        super().__init__(**data)


class Notify(BaseModel):
    id: int
    """通知 ID"""
    cursor: int
    """记录 ID"""
    title: str
    """通知标题"""
    content: str
    """通知正文"""
    time_at: str
    """通知时间"""
    mc: str
    """部分通知固定业务 ID"""

    @validator("content")
    def json_to_str(cls, v):
        try:
            return json.loads(v)["web"]
        except json.JSONDecodeError:
            return v

    # is_station: int
    # is_send: int
    # card_type: int
    # card_brief: str
    # card_msg_brief: str
    # card_cover: str
    # card_story_title: str
    # card_link: str

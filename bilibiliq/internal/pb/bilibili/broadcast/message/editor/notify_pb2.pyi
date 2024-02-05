"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Notify(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MSG_ID_FIELD_NUMBER: builtins.int
    MSG_TYPE_FIELD_NUMBER: builtins.int
    RECEIVER_UID_FIELD_NUMBER: builtins.int
    RECEIVER_TYPE_FIELD_NUMBER: builtins.int
    STORY_VERSION_FIELD_NUMBER: builtins.int
    OP_HASH_FIELD_NUMBER: builtins.int
    OP_SENDER_FIELD_NUMBER: builtins.int
    OP_CONTENT_FIELD_NUMBER: builtins.int
    msg_id: builtins.int
    """消息唯一标示"""
    msg_type: builtins.int
    """消息类型"""
    receiver_uid: builtins.int
    """接收方uid"""
    receiver_type: builtins.int
    """接收方类型"""
    story_version: builtins.int
    """故事的版本"""
    op_hash: builtins.int
    """操作结果的hash值"""
    op_sender: builtins.int
    """操作产生用户的uid"""
    op_content: builtins.str
    """patch内容"""
    def __init__(
        self,
        *,
        msg_id: builtins.int = ...,
        msg_type: builtins.int = ...,
        receiver_uid: builtins.int = ...,
        receiver_type: builtins.int = ...,
        story_version: builtins.int = ...,
        op_hash: builtins.int = ...,
        op_sender: builtins.int = ...,
        op_content: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "msg_id",
            b"msg_id",
            "msg_type",
            b"msg_type",
            "op_content",
            b"op_content",
            "op_hash",
            b"op_hash",
            "op_sender",
            b"op_sender",
            "receiver_type",
            b"receiver_type",
            "receiver_uid",
            b"receiver_uid",
            "story_version",
            b"story_version",
        ],
    ) -> None: ...

global___Notify = Notify

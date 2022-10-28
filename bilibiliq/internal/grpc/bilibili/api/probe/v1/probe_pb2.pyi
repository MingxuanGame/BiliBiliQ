"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Category:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CategoryEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _Category.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    CATEGORY_UNSPECIFIED: _Category.ValueType  # 0
    """"""
    CATEGORY_ONE: _Category.ValueType  # 1
    """"""
    CATEGORY_TWO: _Category.ValueType  # 2
    """"""
    CATEGORY_THREE: _Category.ValueType  # 3
    """"""

class Category(_Category, metaclass=_CategoryEnumTypeWrapper):
    """"""

CATEGORY_UNSPECIFIED: Category.ValueType  # 0
""""""
CATEGORY_ONE: Category.ValueType  # 1
""""""
CATEGORY_TWO: Category.ValueType  # 2
""""""
CATEGORY_THREE: Category.ValueType  # 3
""""""
global___Category = Category

class _ErrorReason:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ErrorReasonEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _ErrorReason.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PROBE_UNSPECIFIED: _ErrorReason.ValueType  # 0
    """"""
    PROBE_CATEGORY_NOTFOUND: _ErrorReason.ValueType  # 1
    """"""

class ErrorReason(_ErrorReason, metaclass=_ErrorReasonEnumTypeWrapper):
    """"""

PROBE_UNSPECIFIED: ErrorReason.ValueType  # 0
""""""
PROBE_CATEGORY_NOTFOUND: ErrorReason.ValueType  # 1
""""""
global___ErrorReason = ErrorReason

@typing_extensions.final
class CodeReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CodeReply = CodeReply

@typing_extensions.final
class CodeReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    code: builtins.int
    """"""
    def __init__(
        self,
        *,
        code: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["code", b"code"]
    ) -> None: ...

global___CodeReq = CodeReq

@typing_extensions.final
class DynamicMessageUpdate(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BODY_FIELD_NUMBER: builtins.int
    @property
    def body(self) -> global___SimpleMessage:
        """"""
    def __init__(
        self,
        *,
        body: global___SimpleMessage | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["body", b"body"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["body", b"body"]
    ) -> None: ...

global___DynamicMessageUpdate = DynamicMessageUpdate

@typing_extensions.final
class Embedded(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class MapStringValEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "key", b"key", "value", b"value"
            ],
        ) -> None: ...

    @typing_extensions.final
    class MapErrorValEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___ErrorMessage: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___ErrorMessage | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "key", b"key", "value", b"value"
            ],
        ) -> None: ...

    BOOL_VAL_FIELD_NUMBER: builtins.int
    INT32_VAL_FIELD_NUMBER: builtins.int
    INT64_VAL_FIELD_NUMBER: builtins.int
    FLOAT_VAL_FIELD_NUMBER: builtins.int
    DOUBLE_VAL_FIELD_NUMBER: builtins.int
    STRING_VAL_FIELD_NUMBER: builtins.int
    REPEATED_INT32_VAL_FIELD_NUMBER: builtins.int
    REPEATED_STRING_VAL_FIELD_NUMBER: builtins.int
    MAP_STRING_VAL_FIELD_NUMBER: builtins.int
    MAP_ERROR_VAL_FIELD_NUMBER: builtins.int
    bool_val: builtins.bool
    """"""
    int32_val: builtins.int
    """"""
    int64_val: builtins.int
    """"""
    float_val: builtins.float
    """"""
    double_val: builtins.float
    """"""
    string_val: builtins.str
    """"""
    @property
    def repeated_int32_val(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.int
    ]:
        """"""
    @property
    def repeated_string_val(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.str
    ]:
        """"""
    @property
    def map_string_val(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[
        builtins.str, builtins.str
    ]:
        """"""
    @property
    def map_error_val(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        builtins.str, global___ErrorMessage
    ]:
        """"""
    def __init__(
        self,
        *,
        bool_val: builtins.bool = ...,
        int32_val: builtins.int = ...,
        int64_val: builtins.int = ...,
        float_val: builtins.float = ...,
        double_val: builtins.float = ...,
        string_val: builtins.str = ...,
        repeated_int32_val: collections.abc.Iterable[builtins.int]
        | None = ...,
        repeated_string_val: collections.abc.Iterable[builtins.str]
        | None = ...,
        map_string_val: collections.abc.Mapping[builtins.str, builtins.str]
        | None = ...,
        map_error_val: collections.abc.Mapping[
            builtins.str, global___ErrorMessage
        ]
        | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "bool_val",
            b"bool_val",
            "double_val",
            b"double_val",
            "float_val",
            b"float_val",
            "int32_val",
            b"int32_val",
            "int64_val",
            b"int64_val",
            "map_error_val",
            b"map_error_val",
            "map_string_val",
            b"map_string_val",
            "repeated_int32_val",
            b"repeated_int32_val",
            "repeated_string_val",
            b"repeated_string_val",
            "string_val",
            b"string_val",
        ],
    ) -> None: ...

global___Embedded = Embedded

@typing_extensions.final
class ErrorMessage(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    REASON_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    code: builtins.int
    """"""
    reason: builtins.str
    """"""
    message: builtins.str
    """"""
    def __init__(
        self,
        *,
        code: builtins.int = ...,
        reason: builtins.str = ...,
        message: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "code", b"code", "message", b"message", "reason", b"reason"
        ],
    ) -> None: ...

global___ErrorMessage = ErrorMessage

@typing_extensions.final
class ProbeReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTENT_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    content: builtins.str
    """"""
    timestamp: builtins.int
    """"""
    def __init__(
        self,
        *,
        content: builtins.str = ...,
        timestamp: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "content", b"content", "timestamp", b"timestamp"
        ],
    ) -> None: ...

global___ProbeReply = ProbeReply

@typing_extensions.final
class ProbeReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MID_FIELD_NUMBER: builtins.int
    BUVID_FIELD_NUMBER: builtins.int
    mid: builtins.int
    """"""
    buvid: builtins.str
    """"""
    def __init__(
        self,
        *,
        mid: builtins.int = ...,
        buvid: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "buvid", b"buvid", "mid", b"mid"
        ],
    ) -> None: ...

global___ProbeReq = ProbeReq

@typing_extensions.final
class ProbeStreamReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEQUENCE_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    sequence: builtins.int
    """"""
    timestamp: builtins.int
    """"""
    content: builtins.str
    """"""
    def __init__(
        self,
        *,
        sequence: builtins.int = ...,
        timestamp: builtins.int = ...,
        content: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "content",
            b"content",
            "sequence",
            b"sequence",
            "timestamp",
            b"timestamp",
        ],
    ) -> None: ...

global___ProbeStreamReply = ProbeStreamReply

@typing_extensions.final
class ProbeStreamReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MID_FIELD_NUMBER: builtins.int
    SEQUENCE_FIELD_NUMBER: builtins.int
    mid: builtins.int
    """"""
    sequence: builtins.int
    """"""
    def __init__(
        self,
        *,
        mid: builtins.int = ...,
        sequence: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "mid", b"mid", "sequence", b"sequence"
        ],
    ) -> None: ...

global___ProbeStreamReq = ProbeStreamReq

@typing_extensions.final
class ProbeSubReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGE_ID_FIELD_NUMBER: builtins.int
    message_id: builtins.int
    """"""
    def __init__(
        self,
        *,
        message_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["message_id", b"message_id"],
    ) -> None: ...

global___ProbeSubReply = ProbeSubReply

@typing_extensions.final
class ProbeSubReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BUVID_FIELD_NUMBER: builtins.int
    buvid: builtins.int
    """"""
    def __init__(
        self,
        *,
        buvid: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["buvid", b"buvid"]
    ) -> None: ...

global___ProbeSubReq = ProbeSubReq

@typing_extensions.final
class SimpleMessage(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NUM_FIELD_NUMBER: builtins.int
    LANG_FIELD_NUMBER: builtins.int
    CATE_FIELD_NUMBER: builtins.int
    EMBEDDED_FIELD_NUMBER: builtins.int
    id: builtins.int
    """"""
    num: builtins.int
    """"""
    lang: builtins.str
    """"""
    cate: builtins.int
    """"""
    @property
    def embedded(self) -> global___Embedded:
        """"""
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        num: builtins.int = ...,
        lang: builtins.str = ...,
        cate: builtins.int = ...,
        embedded: global___Embedded | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["embedded", b"embedded"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "cate",
            b"cate",
            "embedded",
            b"embedded",
            "id",
            b"id",
            "lang",
            b"lang",
            "num",
            b"num",
        ],
    ) -> None: ...

global___SimpleMessage = SimpleMessage
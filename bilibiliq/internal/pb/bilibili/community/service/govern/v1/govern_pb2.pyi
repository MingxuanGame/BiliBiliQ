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
class QoeReportReq(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    SCENE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    CANCEL_FIELD_NUMBER: builtins.int
    BUSINESS_TYPE_FIELD_NUMBER: builtins.int
    OID_FIELD_NUMBER: builtins.int
    SCORE_RESULT_FIELD_NUMBER: builtins.int
    BUSINESS_DATA_FIELD_NUMBER: builtins.int
    id: builtins.int
    """"""
    scene: builtins.int
    """"""
    type: builtins.int
    """"""
    cancel: builtins.bool
    """"""
    business_type: builtins.str
    """"""
    oid: builtins.int
    """"""
    @property
    def score_result(self) -> global___QoeScoreResult:
        """"""
    business_data: builtins.str
    """"""
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        scene: builtins.int = ...,
        type: builtins.int = ...,
        cancel: builtins.bool = ...,
        business_type: builtins.str = ...,
        oid: builtins.int = ...,
        score_result: global___QoeScoreResult | None = ...,
        business_data: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal["score_result", b"score_result"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "business_data",
            b"business_data",
            "business_type",
            b"business_type",
            "cancel",
            b"cancel",
            "id",
            b"id",
            "oid",
            b"oid",
            "scene",
            b"scene",
            "score_result",
            b"score_result",
            "type",
            b"type",
        ],
    ) -> None: ...

global___QoeReportReq = QoeReportReq

@typing_extensions.final
class QoeScoreResult(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCORE_FIELD_NUMBER: builtins.int
    score: builtins.float
    """"""
    def __init__(
        self,
        *,
        score: builtins.float = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["score", b"score"]
    ) -> None: ...

global___QoeScoreResult = QoeScoreResult

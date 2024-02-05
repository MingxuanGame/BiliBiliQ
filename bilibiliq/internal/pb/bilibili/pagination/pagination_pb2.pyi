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
class FeedPagination(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_SIZE_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    IS_REFRESH_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    """"""
    offset: builtins.str
    """"""
    is_refresh: builtins.bool
    """"""
    def __init__(
        self,
        *,
        page_size: builtins.int = ...,
        offset: builtins.str = ...,
        is_refresh: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "is_refresh",
            b"is_refresh",
            "offset",
            b"offset",
            "page_size",
            b"page_size",
        ],
    ) -> None: ...

global___FeedPagination = FeedPagination

@typing_extensions.final
class FeedPaginationReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NEXT_OFFSET_FIELD_NUMBER: builtins.int
    PREV_OFFSET_FIELD_NUMBER: builtins.int
    LAST_READ_OFFSET_FIELD_NUMBER: builtins.int
    next_offset: builtins.str
    """"""
    prev_offset: builtins.str
    """"""
    last_read_offset: builtins.str
    """"""
    def __init__(
        self,
        *,
        next_offset: builtins.str = ...,
        prev_offset: builtins.str = ...,
        last_read_offset: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "last_read_offset",
            b"last_read_offset",
            "next_offset",
            b"next_offset",
            "prev_offset",
            b"prev_offset",
        ],
    ) -> None: ...

global___FeedPaginationReply = FeedPaginationReply

@typing_extensions.final
class Pagination(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_SIZE_FIELD_NUMBER: builtins.int
    NEXT_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    """"""
    next: builtins.str
    """"""
    def __init__(
        self,
        *,
        page_size: builtins.int = ...,
        next: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "next", b"next", "page_size", b"page_size"
        ],
    ) -> None: ...

global___Pagination = Pagination

@typing_extensions.final
class PaginationReply(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NEXT_FIELD_NUMBER: builtins.int
    PREV_FIELD_NUMBER: builtins.int
    next: builtins.str
    """"""
    prev: builtins.str
    """"""
    def __init__(
        self,
        *,
        next: builtins.str = ...,
        prev: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "next", b"next", "prev", b"prev"
        ],
    ) -> None: ...

global___PaginationReply = PaginationReply

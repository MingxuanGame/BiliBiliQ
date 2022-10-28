# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/app/interfaces/v1/space.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilibiliq.internal.pb.bilibili.app.archive.v1 import (
    archive_pb2 as bilibili_dot_app_dot_archive_dot_v1_dot_archive__pb2,
)
from bilibiliq.internal.pb.bilibili.app.dynamic.v2 import (
    dynamic_pb2 as bilibili_dot_app_dot_dynamic_dot_v2_dot_dynamic__pb2,
)
from bilibiliq.internal.pb.bilibili.app.archive.middleware.v1 import (
    preload_pb2 as bilibili_dot_app_dot_archive_dot_middleware_dot_v1_dot_preload__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n&bilibili/app/interfaces/v1/space.proto\x12\x19\x62ilibili.app.interface.v1\x1a\x30\x62ilibili/app/archive/middleware/v1/preload.proto\x1a%bilibili/app/archive/v1/archive.proto\x1a%bilibili/app/dynamic/v2/dynamic.proto\"A\n\x03\x41rc\x12-\n\x07\x61rchive\x18\x01 \x01(\x0b\x32\x1c.bilibili.app.archive.v1.Arc\x12\x0b\n\x03uri\x18\x02 \x01(\t\"@\n\x07\x44ynamic\x12\x35\n\x07\x64ynamic\x18\x01 \x01(\x0b\x32$.bilibili.app.dynamic.v2.DynamicItem\"M\n\x0eSearchTabReply\x12\r\n\x05\x66ocus\x18\x01 \x01(\x03\x12,\n\x04tabs\x18\x02 \x03(\x0b\x32\x1e.bilibili.app.interface.v1.Tab\":\n\x0cSearchTabReq\x12\x0f\n\x07keyword\x18\x01 \x01(\t\x12\x0b\n\x03mid\x18\x02 \x01(\x03\x12\x0c\n\x04\x66rom\x18\x03 \x01(\x05\"U\n\x12SearchArchiveReply\x12\x30\n\x08\x61rchives\x18\x01 \x03(\x0b\x32\x1e.bilibili.app.interface.v1.Arc\x12\r\n\x05total\x18\x02 \x01(\x03\"\x8d\x01\n\x10SearchArchiveReq\x12\x0f\n\x07keyword\x18\x01 \x01(\t\x12\x0b\n\x03mid\x18\x02 \x01(\x03\x12\n\n\x02pn\x18\x03 \x01(\x03\x12\n\n\x02ps\x18\x04 \x01(\x03\x12\x43\n\x0bplayer_args\x18\x05 \x01(\x0b\x32..bilibili.app.archive.middleware.v1.PlayerArgs\"Y\n\x12SearchDynamicReply\x12\x34\n\x08\x64ynamics\x18\x01 \x03(\x0b\x32\".bilibili.app.interface.v1.Dynamic\x12\r\n\x05total\x18\x02 \x01(\x03\"\x8d\x01\n\x10SearchDynamicReq\x12\x0f\n\x07keyword\x18\x01 \x01(\t\x12\x0b\n\x03mid\x18\x02 \x01(\x03\x12\n\n\x02pn\x18\x03 \x01(\x03\x12\n\n\x02ps\x18\x04 \x01(\x03\x12\x43\n\x0bplayer_args\x18\x05 \x01(\x0b\x32..bilibili.app.archive.middleware.v1.PlayerArgs\"!\n\x03Tab\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t*&\n\x04\x46rom\x12\x0e\n\nArchiveTab\x10\x00\x12\x0e\n\nDynamicTab\x10\x01\x32\xc2\x02\n\x05Space\x12_\n\tSearchTab\x12\'.bilibili.app.interface.v1.SearchTabReq\x1a).bilibili.app.interface.v1.SearchTabReply\x12k\n\rSearchArchive\x12+.bilibili.app.interface.v1.SearchArchiveReq\x1a-.bilibili.app.interface.v1.SearchArchiveReply\x12k\n\rSearchDynamic\x12+.bilibili.app.interface.v1.SearchDynamicReq\x1a-.bilibili.app.interface.v1.SearchDynamicReplyb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'bilibili.app.interfaces.v1.space_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _FROM._serialized_start = 970
    _FROM._serialized_end = 1008
    _ARC._serialized_start = 197
    _ARC._serialized_end = 262
    _DYNAMIC._serialized_start = 264
    _DYNAMIC._serialized_end = 328
    _SEARCHTABREPLY._serialized_start = 330
    _SEARCHTABREPLY._serialized_end = 407
    _SEARCHTABREQ._serialized_start = 409
    _SEARCHTABREQ._serialized_end = 467
    _SEARCHARCHIVEREPLY._serialized_start = 469
    _SEARCHARCHIVEREPLY._serialized_end = 554
    _SEARCHARCHIVEREQ._serialized_start = 557
    _SEARCHARCHIVEREQ._serialized_end = 698
    _SEARCHDYNAMICREPLY._serialized_start = 700
    _SEARCHDYNAMICREPLY._serialized_end = 789
    _SEARCHDYNAMICREQ._serialized_start = 792
    _SEARCHDYNAMICREQ._serialized_end = 933
    _TAB._serialized_start = 935
    _TAB._serialized_end = 968
    _SPACE._serialized_start = 1011
    _SPACE._serialized_end = 1333
# @@protoc_insertion_point(module_scope)

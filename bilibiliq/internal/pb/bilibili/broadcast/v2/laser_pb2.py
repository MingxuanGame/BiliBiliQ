# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/broadcast/v2/laser.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n!bilibili/broadcast/v2/laser.proto\x12\x15\x62ilibili.broadcast.v2\x1a\x1bgoogle/protobuf/empty.proto\"@\n\x0eLaserEventResp\x12\x0e\n\x06taskid\x18\x01 \x01(\x03\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x0e\n\x06params\x18\x03 \x01(\t2V\n\x05Laser\x12M\n\nWatchEvent\x12\x16.google.protobuf.Empty\x1a%.bilibili.broadcast.v2.LaserEventResp0\x01\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'bilibili.broadcast.v2.laser_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _LASEREVENTRESP._serialized_start = 89
    _LASEREVENTRESP._serialized_end = 153
    _LASER._serialized_start = 155
    _LASER._serialized_end = 241
# @@protoc_insertion_point(module_scope)

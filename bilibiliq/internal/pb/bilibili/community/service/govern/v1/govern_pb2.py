# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/community/service/govern/v1/govern.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n1bilibili/community/service/govern/v1/govern.proto\x12$bilibili.community.service.govern.v1\x1a\x1bgoogle/protobuf/empty.proto\"\xce\x01\n\x0cQoeReportReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05scene\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x0e\n\x06\x63\x61ncel\x18\x04 \x01(\x08\x12\x15\n\rbusiness_type\x18\x05 \x01(\t\x12\x0b\n\x03oid\x18\x06 \x01(\x03\x12J\n\x0cscore_result\x18\x07 \x01(\x0b\x32\x34.bilibili.community.service.govern.v1.QoeScoreResult\x12\x15\n\rbusiness_data\x18\x08 \x01(\t\"\x1f\n\x0eQoeScoreResult\x12\r\n\x05score\x18\x01 \x01(\x02\x32^\n\x03Qoe\x12W\n\tQoeReport\x12\x32.bilibili.community.service.govern.v1.QoeReportReq\x1a\x16.google.protobuf.Emptyb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'bilibili.community.service.govern.v1.govern_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _QOEREPORTREQ._serialized_start = 121
    _QOEREPORTREQ._serialized_end = 327
    _QOESCORERESULT._serialized_start = 329
    _QOESCORERESULT._serialized_end = 360
    _QOE._serialized_start = 362
    _QOE._serialized_end = 456
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/vega/deneb/v1/deneb.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\"bilibili/vega/deneb/v1/deneb.proto\x12\x16\x62ilibili.vega.deneb.v1\x1a\x19google/protobuf/any.proto\"p\n\x11MessagePullsReply\x12\"\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\x12\n\n\x02pn\x18\x02 \x01(\x05\x12\n\n\x02ps\x18\x03 \x01(\x05\x12\r\n\x05\x63ount\x18\x04 \x01(\x03\x12\x10\n\x08has_next\x18\x05 \x01(\x08\"S\n\x0fMessagePullsReq\x12\x14\n\x0cstart_seq_id\x18\x01 \x01(\x03\x12\x12\n\nend_seq_id\x18\x02 \x01(\x03\x12\n\n\x02pn\x18\x03 \x01(\x05\x12\n\n\x02ps\x18\x04 \x01(\x05\x32r\n\x0cVegaDenebRPC\x12\x62\n\x0cMessagePulls\x12\'.bilibili.vega.deneb.v1.MessagePullsReq\x1a).bilibili.vega.deneb.v1.MessagePullsReplyb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'bilibili.vega.deneb.v1.deneb_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _MESSAGEPULLSREPLY._serialized_start = 89
    _MESSAGEPULLSREPLY._serialized_end = 201
    _MESSAGEPULLSREQ._serialized_start = 203
    _MESSAGEPULLSREQ._serialized_end = 286
    _VEGADENEBRPC._serialized_start = 288
    _VEGADENEBRPC._serialized_end = 402
# @@protoc_insertion_point(module_scope)

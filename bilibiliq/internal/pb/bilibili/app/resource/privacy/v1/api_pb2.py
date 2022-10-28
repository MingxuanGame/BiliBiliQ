# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/app/resource/privacy/v1/api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n*bilibili/app/resource/privacy/v1/api.proto\x12 bilibili.app.resource.privacy.v1\"\x0e\n\x0cNoArgRequest\"\t\n\x07NoReply\"\xe3\x01\n\x11PrivacyConfigItem\x12P\n\x13privacy_config_type\x18\x01 \x01(\x0e\x32\x33.bilibili.app.resource.privacy.v1.PrivacyConfigType\x12\r\n\x05title\x18\x02 \x01(\t\x12\x43\n\x05state\x18\x03 \x01(\x0e\x32\x34.bilibili.app.resource.privacy.v1.PrivacyConfigState\x12\x11\n\tsub_title\x18\x04 \x01(\t\x12\x15\n\rsub_title_uri\x18\x05 \x01(\t\"f\n\x12PrivacyConfigReply\x12P\n\x13privacy_config_item\x18\x01 \x01(\x0b\x32\x33.bilibili.app.resource.privacy.v1.PrivacyConfigItem\"\xb0\x01\n\x17SetPrivacyConfigRequest\x12P\n\x13privacy_config_type\x18\x01 \x01(\x0e\x32\x33.bilibili.app.resource.privacy.v1.PrivacyConfigType\x12\x43\n\x05state\x18\x02 \x01(\x0e\x32\x34.bilibili.app.resource.privacy.v1.PrivacyConfigState*)\n\x12PrivacyConfigState\x12\t\n\x05\x63lose\x10\x00\x12\x08\n\x04open\x10\x01*/\n\x11PrivacyConfigType\x12\x08\n\x04none\x10\x00\x12\x10\n\x0c\x64ynamic_city\x10\x01\x32\xfa\x01\n\x07Privacy\x12u\n\rPrivacyConfig\x12..bilibili.app.resource.privacy.v1.NoArgRequest\x1a\x34.bilibili.app.resource.privacy.v1.PrivacyConfigReply\x12x\n\x10SetPrivacyConfig\x12\x39.bilibili.app.resource.privacy.v1.SetPrivacyConfigRequest\x1a).bilibili.app.resource.privacy.v1.NoReplyb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'bilibili.app.resource.privacy.v1.api_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _PRIVACYCONFIGSTATE._serialized_start = 620
    _PRIVACYCONFIGSTATE._serialized_end = 661
    _PRIVACYCONFIGTYPE._serialized_start = 663
    _PRIVACYCONFIGTYPE._serialized_end = 710
    _NOARGREQUEST._serialized_start = 80
    _NOARGREQUEST._serialized_end = 94
    _NOREPLY._serialized_start = 96
    _NOREPLY._serialized_end = 105
    _PRIVACYCONFIGITEM._serialized_start = 108
    _PRIVACYCONFIGITEM._serialized_end = 335
    _PRIVACYCONFIGREPLY._serialized_start = 337
    _PRIVACYCONFIGREPLY._serialized_end = 439
    _SETPRIVACYCONFIGREQUEST._serialized_start = 442
    _SETPRIVACYCONFIGREQUEST._serialized_end = 618
    _PRIVACY._serialized_start = 713
    _PRIVACY._serialized_end = 963
# @@protoc_insertion_point(module_scope)
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/pgc/gateway/player/v1/playurl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilibiliq.internal.pb.bilibili.app.playurl.v1 import (
    playurl_pb2 as bilibili_dot_app_dot_playurl_dot_v1_dot_playurl__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n,bilibili/pgc/gateway/player/v1/playurl.proto\x12\x1e\x62ilibili.pgc.gateway.player.v1\x1a%bilibili/app/playurl/v1/playurl.proto\"D\n\x0c\x42usinessInfo\x12\x12\n\nis_preview\x18\x01 \x01(\x08\x12\n\n\x02\x62p\x18\x02 \x01(\x08\x12\x14\n\x0cmarlin_token\x18\x03 \x01(\t\"=\n\x05\x45vent\x12\x34\n\x05shake\x18\x01 \x01(\x0b\x32%.bilibili.pgc.gateway.player.v1.Shake\"\xb2\x01\n\x0cLivePlayInfo\x12\x12\n\ncurrent_qn\x18\x01 \x01(\x05\x12O\n\x13quality_description\x18\x02 \x03(\x0b\x32\x32.bilibili.pgc.gateway.player.v1.QualityDescription\x12=\n\x04\x64url\x18\x03 \x03(\x0b\x32/.bilibili.pgc.gateway.player.v1.ResponseDataUrl\"\x91\x01\n\x11LivePlayViewReply\x12;\n\troom_info\x18\x01 \x01(\x0b\x32(.bilibili.pgc.gateway.player.v1.RoomInfo\x12?\n\tplay_info\x18\x02 \x01(\x0b\x32,.bilibili.pgc.gateway.player.v1.LivePlayInfo\"w\n\x0fLivePlayViewReq\x12\r\n\x05\x65p_id\x18\x01 \x01(\x03\x12\x0f\n\x07quality\x18\x02 \x01(\r\x12\r\n\x05ptype\x18\x03 \x01(\r\x12\r\n\x05https\x18\x04 \x01(\x08\x12\x11\n\tplay_type\x18\x05 \x01(\r\x12\x13\n\x0b\x64\x65vice_type\x18\x06 \x01(\x05\"\xae\x06\n\x0fPlayAbilityConf\x12\x1f\n\x17\x62\x61\x63kground_play_disable\x18\x01 \x01(\x08\x12\x14\n\x0c\x66lip_disable\x18\x02 \x01(\x08\x12\x14\n\x0c\x63\x61st_disable\x18\x03 \x01(\x08\x12\x18\n\x10\x66\x65\x65\x64\x62\x61\x63k_disable\x18\x04 \x01(\x08\x12\x18\n\x10subtitle_disable\x18\x05 \x01(\x08\x12\x1d\n\x15playback_rate_disable\x18\x06 \x01(\x08\x12\x17\n\x0ftime_up_disable\x18\x07 \x01(\x08\x12\x1d\n\x15playback_mode_disable\x18\x08 \x01(\x08\x12\x1a\n\x12scale_mode_disable\x18\t \x01(\x08\x12\x14\n\x0clike_disable\x18\n \x01(\x08\x12\x17\n\x0f\x64islike_disable\x18\x0b \x01(\x08\x12\x14\n\x0c\x63oin_disable\x18\x0c \x01(\x08\x12\x14\n\x0c\x65lec_disable\x18\r \x01(\x08\x12\x15\n\rshare_disable\x18\x0e \x01(\x08\x12\x1b\n\x13screen_shot_disable\x18\x0f \x01(\x08\x12\x1b\n\x13lock_screen_disable\x18\x10 \x01(\x08\x12\x19\n\x11recommend_disable\x18\x11 \x01(\x08\x12\x1e\n\x16playback_speed_disable\x18\x12 \x01(\x08\x12\x1a\n\x12\x64\x65\x66inition_disable\x18\x13 \x01(\x08\x12\x1a\n\x12selections_disable\x18\x14 \x01(\x08\x12\x14\n\x0cnext_disable\x18\x15 \x01(\x08\x12\x17\n\x0f\x65\x64it_dm_disable\x18\x16 \x01(\x08\x12\x1c\n\x14small_window_disable\x18\x17 \x01(\x08\x12\x15\n\rshake_disable\x18\x18 \x01(\x08\x12\x18\n\x10outer_dm_disable\x18\x19 \x01(\x08\x12\x18\n\x10inner_dm_disable\x18\x1a \x01(\x08\x12\x1b\n\x13\x66reya_enter_disable\x18\x1b \x01(\x08\x12\x15\n\rdolby_disable\x18\x1c \x01(\x08\x12\x1a\n\x12\x66reya_full_disable\x18\x1d \x01(\x08\x12 \n\x18skip_oped_switch_disable\x18\x1e \x01(\x08\"\x81\x02\n\rPlayViewReply\x12\x36\n\nvideo_info\x18\x01 \x01(\x0b\x32\".bilibili.app.playurl.v1.VideoInfo\x12\x42\n\tplay_conf\x18\x02 \x01(\x0b\x32/.bilibili.pgc.gateway.player.v1.PlayAbilityConf\x12>\n\x08\x62usiness\x18\x03 \x01(\x0b\x32,.bilibili.pgc.gateway.player.v1.BusinessInfo\x12\x34\n\x05\x65vent\x18\x04 \x01(\x0b\x32%.bilibili.pgc.gateway.player.v1.Event\"\xa5\x02\n\x0bPlayViewReq\x12\x0c\n\x04\x65pid\x18\x01 \x01(\x03\x12\x0b\n\x03\x63id\x18\x02 \x01(\x03\x12\n\n\x02qn\x18\x03 \x01(\x03\x12\r\n\x05\x66nver\x18\x04 \x01(\x05\x12\r\n\x05\x66nval\x18\x05 \x01(\x05\x12\x10\n\x08\x64ownload\x18\x06 \x01(\r\x12\x12\n\nforce_host\x18\x07 \x01(\x05\x12\r\n\x05\x66ourk\x18\x08 \x01(\x08\x12\r\n\x05spmid\x18\t \x01(\t\x12\x12\n\nfrom_spmid\x18\n \x01(\t\x12\x16\n\x0eteenagers_mode\x18\x0b \x01(\x05\x12<\n\x11prefer_codec_type\x18\x0c \x01(\x0e\x32!.bilibili.app.playurl.v1.CodeType\x12\x12\n\nis_preview\x18\r \x01(\x08\x12\x0f\n\x07room_id\x18\x0e \x01(\x03\"F\n\x0cProjectReply\x12\x36\n\x07project\x18\x01 \x01(\x0b\x32%.bilibili.app.playurl.v1.PlayURLReply\"\xed\x01\n\nProjectReq\x12\r\n\x05\x65p_id\x18\x01 \x01(\x03\x12\x0b\n\x03\x63id\x18\x02 \x01(\x03\x12\n\n\x02qn\x18\x03 \x01(\x03\x12\r\n\x05\x66nver\x18\x04 \x01(\x05\x12\r\n\x05\x66nval\x18\x05 \x01(\x05\x12\x10\n\x08\x64ownload\x18\x06 \x01(\r\x12\x11\n\tforceHost\x18\x07 \x01(\x05\x12\r\n\x05\x66ourk\x18\x08 \x01(\x08\x12\r\n\x05spmid\x18\t \x01(\t\x12\x11\n\tfromSpmid\x18\n \x01(\t\x12\x10\n\x08protocol\x18\x0b \x01(\x05\x12\x13\n\x0b\x64\x65vice_type\x18\x0c \x01(\x05\x12\x1c\n\x14use_new_project_code\x18\r \x01(\x08\".\n\x12QualityDescription\x12\n\n\x02qn\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\"A\n\x0fResponseDataUrl\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x13\n\x0bstream_type\x18\x02 \x01(\r\x12\x0c\n\x04ptag\x18\x03 \x01(\r\"\xa4\x01\n\x08RoomInfo\x12\x0f\n\x07room_id\x18\x01 \x01(\x03\x12\x0b\n\x03uid\x18\x02 \x01(\x03\x12>\n\x06status\x18\x03 \x01(\x0b\x32..bilibili.pgc.gateway.player.v1.RoomStatusInfo\x12:\n\x04show\x18\x04 \x01(\x0b\x32,.bilibili.pgc.gateway.player.v1.RoomShowInfo\"S\n\x0cRoomShowInfo\x12\x10\n\x08short_id\x18\x01 \x01(\x03\x12\x18\n\x10popularity_count\x18\x08 \x01(\x03\x12\x17\n\x0flive_start_time\x18\n \x01(\x03\"\xce\x01\n\x0eRoomStatusInfo\x12\x13\n\x0blive_status\x18\x01 \x01(\x03\x12\x18\n\x10live_screen_type\x18\x02 \x01(\x03\x12\x11\n\tlive_mark\x18\x03 \x01(\x03\x12\x13\n\x0block_status\x18\x04 \x01(\x03\x12\x11\n\tlock_time\x18\x05 \x01(\x03\x12\x15\n\rhidden_status\x18\x06 \x01(\x03\x12\x13\n\x0bhidden_time\x18\x07 \x01(\x03\x12\x11\n\tlive_type\x18\x08 \x01(\x03\x12\x13\n\x0broom_shield\x18\t \x01(\x03\"\x15\n\x05Shake\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t2\xca\x02\n\x07PlayURL\x12\x66\n\x08PlayView\x12+.bilibili.pgc.gateway.player.v1.PlayViewReq\x1a-.bilibili.pgc.gateway.player.v1.PlayViewReply\x12\x63\n\x07Project\x12*.bilibili.pgc.gateway.player.v1.ProjectReq\x1a,.bilibili.pgc.gateway.player.v1.ProjectReply\x12r\n\x0cLivePlayView\x12/.bilibili.pgc.gateway.player.v1.LivePlayViewReq\x1a\x31.bilibili.pgc.gateway.player.v1.LivePlayViewReplyb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'bilibili.pgc.gateway.player.v1.playurl_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _BUSINESSINFO._serialized_start = 119
    _BUSINESSINFO._serialized_end = 187
    _EVENT._serialized_start = 189
    _EVENT._serialized_end = 250
    _LIVEPLAYINFO._serialized_start = 253
    _LIVEPLAYINFO._serialized_end = 431
    _LIVEPLAYVIEWREPLY._serialized_start = 434
    _LIVEPLAYVIEWREPLY._serialized_end = 579
    _LIVEPLAYVIEWREQ._serialized_start = 581
    _LIVEPLAYVIEWREQ._serialized_end = 700
    _PLAYABILITYCONF._serialized_start = 703
    _PLAYABILITYCONF._serialized_end = 1517
    _PLAYVIEWREPLY._serialized_start = 1520
    _PLAYVIEWREPLY._serialized_end = 1777
    _PLAYVIEWREQ._serialized_start = 1780
    _PLAYVIEWREQ._serialized_end = 2073
    _PROJECTREPLY._serialized_start = 2075
    _PROJECTREPLY._serialized_end = 2145
    _PROJECTREQ._serialized_start = 2148
    _PROJECTREQ._serialized_end = 2385
    _QUALITYDESCRIPTION._serialized_start = 2387
    _QUALITYDESCRIPTION._serialized_end = 2433
    _RESPONSEDATAURL._serialized_start = 2435
    _RESPONSEDATAURL._serialized_end = 2500
    _ROOMINFO._serialized_start = 2503
    _ROOMINFO._serialized_end = 2667
    _ROOMSHOWINFO._serialized_start = 2669
    _ROOMSHOWINFO._serialized_end = 2752
    _ROOMSTATUSINFO._serialized_start = 2755
    _ROOMSTATUSINFO._serialized_end = 2961
    _SHAKE._serialized_start = 2963
    _SHAKE._serialized_end = 2984
    _PLAYURL._serialized_start = 2987
    _PLAYURL._serialized_end = 3317
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/im/type/im.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19\x62ilibili/im/type/im.proto\x12\x10\x62ilibili.im.type\",\n\x0b\x41\x63\x63ountInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07pic_url\x18\x02 \x01(\t\"Q\n\x0e\x46riendRelation\x12\x0b\n\x03uid\x18\x01 \x01(\x04\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x03 \x01(\t\x12\x11\n\tvip_level\x18\x04 \x01(\r\"\xeb\x01\n\rGroupRelation\x12\x10\n\x08group_id\x18\x01 \x01(\x04\x12\x11\n\towner_uid\x18\x02 \x01(\x04\x12\x12\n\ngroup_type\x18\x03 \x01(\r\x12\x13\n\x0bgroup_level\x18\x04 \x01(\r\x12\x13\n\x0bgroup_cover\x18\x05 \x01(\t\x12\x12\n\ngroup_name\x18\x06 \x01(\t\x12\x14\n\x0cgroup_notice\x18\x07 \x01(\t\x12\x0e\n\x06status\x18\x08 \x01(\x05\x12\x13\n\x0bmember_role\x18\t \x01(\x05\x12\x17\n\x0f\x66\x61ns_medal_name\x18\n \x01(\t\x12\x0f\n\x07room_id\x18\x0b \x01(\x04\"5\n\x08HighText\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\r\"H\n\x07ImgInfo\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x11\n\timageType\x18\x04 \x01(\t\"\\\n\x0bKeyHitInfos\x12\r\n\x05toast\x18\x01 \x01(\t\x12\x0f\n\x07rule_id\x18\x02 \x01(\r\x12-\n\thigh_text\x18\x03 \x03(\x0b\x32\x1a.bilibili.im.type.HighText\"\xaf\x02\n\x05Medal\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x10\n\x08medal_id\x18\x02 \x01(\x05\x12\r\n\x05level\x18\x03 \x01(\x05\x12\x12\n\nmedal_name\x18\x04 \x01(\t\x12\r\n\x05score\x18\x05 \x01(\x05\x12\x10\n\x08intimacy\x18\x06 \x01(\x05\x12\x15\n\rmaster_status\x18\x07 \x01(\x05\x12\x12\n\nis_receive\x18\x08 \x01(\x05\x12\x19\n\x11medal_color_start\x18\t \x01(\x03\x12\x17\n\x0fmedal_color_end\x18\n \x01(\x03\x12\x1a\n\x12medal_color_border\x18\x0b \x01(\x03\x12\x18\n\x10medal_color_name\x18\x0c \x01(\x03\x12\x19\n\x11medal_color_level\x18\r \x01(\x03\x12\x13\n\x0bguard_level\x18\x0e \x01(\x03\"\xcf\x03\n\x03Msg\x12\x12\n\nsender_uid\x18\x01 \x01(\x04\x12\x33\n\rreceiver_type\x18\x02 \x01(\x0e\x32\x1c.bilibili.im.type.RecverType\x12\x13\n\x0breceiver_id\x18\x03 \x01(\x04\x12\x12\n\ncli_msg_id\x18\x04 \x01(\x04\x12+\n\x08msg_type\x18\x05 \x01(\x0e\x32\x19.bilibili.im.type.MsgType\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\t\x12\x11\n\tmsg_seqno\x18\x07 \x01(\x04\x12\x11\n\ttimestamp\x18\x08 \x01(\x04\x12\x0f\n\x07\x61t_uids\x18\t \x03(\x04\x12\x12\n\nrecver_ids\x18\n \x03(\x04\x12\x0f\n\x07msg_key\x18\x0b \x01(\x04\x12\x12\n\nmsg_status\x18\x0c \x01(\r\x12\x12\n\nsys_cancel\x18\r \x01(\x08\x12\x13\n\x0bnotify_code\x18\x0e \x01(\t\x12/\n\nmsg_source\x18\x0f \x01(\x0e\x32\x1b.bilibili.im.type.MsgSource\x12\x18\n\x10new_face_version\x18\x10 \x01(\x05\x12\x34\n\rkey_hit_infos\x18\x11 \x01(\x0b\x32\x1d.bilibili.im.type.KeyHitInfos\"\xcb\x01\n\x0bRelationLog\x12\x33\n\x08log_type\x18\x01 \x01(\x0e\x32!.bilibili.im.type.RelationLogType\x12\x13\n\x0boplog_seqno\x18\x02 \x01(\x04\x12\x39\n\x0f\x66riend_relation\x18\x03 \x01(\x0b\x32 .bilibili.im.type.FriendRelation\x12\x37\n\x0egroup_relation\x18\x04 \x01(\x0b\x32\x1f.bilibili.im.type.GroupRelation\"\xf9\x04\n\x0bSessionInfo\x12\x11\n\ttalker_id\x18\x01 \x01(\x04\x12\x14\n\x0csession_type\x18\x02 \x01(\r\x12\x10\n\x08\x61t_seqno\x18\x03 \x01(\x04\x12\x0e\n\x06top_ts\x18\x04 \x01(\x04\x12\x12\n\ngroup_name\x18\x05 \x01(\t\x12\x13\n\x0bgroup_cover\x18\x06 \x01(\t\x12\x11\n\tis_follow\x18\x07 \x01(\r\x12\x0e\n\x06is_dnd\x18\x08 \x01(\r\x12\x11\n\tack_seqno\x18\t \x01(\x04\x12\x0e\n\x06\x61\x63k_ts\x18\n \x01(\x04\x12\x12\n\nsession_ts\x18\x0b \x01(\x04\x12\x14\n\x0cunread_count\x18\x0c \x01(\r\x12\'\n\x08last_msg\x18\r \x01(\x0b\x32\x15.bilibili.im.type.Msg\x12\x12\n\ngroup_type\x18\x0e \x01(\r\x12\x10\n\x08\x63\x61n_fold\x18\x0f \x01(\r\x12\x0e\n\x06status\x18\x10 \x01(\r\x12\x11\n\tmax_seqno\x18\x11 \x01(\x04\x12\x14\n\x0cnew_push_msg\x18\x12 \x01(\r\x12\x0f\n\x07setting\x18\x13 \x01(\r\x12\x13\n\x0bis_guardian\x18\x14 \x01(\r\x12\x14\n\x0cis_intercept\x18\x15 \x01(\x05\x12\x10\n\x08is_trust\x18\x16 \x01(\x05\x12\x17\n\x0fsystem_msg_type\x18\x17 \x01(\x05\x12\x33\n\x0c\x61\x63\x63ount_info\x18\x18 \x01(\x0b\x32\x1d.bilibili.im.type.AccountInfo\x12\x13\n\x0blive_status\x18\x19 \x01(\x05\x12\x1c\n\x14\x62iz_msg_unread_count\x18\x1a \x01(\x05\x12/\n\nuser_label\x18\x1b \x01(\x0b\x32\x1b.bilibili.im.type.UserLabel\"b\n\tUserLabel\x12\x12\n\nlabel_type\x18\x01 \x01(\x05\x12&\n\x05medal\x18\x02 \x01(\x0b\x32\x17.bilibili.im.type.Medal\x12\x19\n\x11guardian_relation\x18\x03 \x01(\x05*\x94\x06\n\x05\x43mdId\x12\x15\n\x11\x45N_CMD_ID_INVALID\x10\x00\x12\x18\n\x12\x45N_CMD_ID_SEND_MSG\x10\xc1\x9a\x0c\x12\x18\n\x12\x45N_CMD_ID_SYNC_MSG\x10\xa1\xc2\x1e\x12\x1d\n\x17\x45N_CMD_ID_SYNC_RELATION\x10\xa2\xc2\x1e\x12\x18\n\x12\x45N_CMD_ID_SYNC_ACK\x10\xa3\xc2\x1e\x12\'\n!EN_CMD_ID_SYNC_FETCH_SESSION_MSGS\x10\xa6\xc2\x1e\x12(\n\"EN_CMD_ID_SESSION_SVR_GET_SESSIONS\x10\xc1\x84=\x12(\n\"EN_CMD_ID_SESSION_SVR_NEW_SESSIONS\x10\xc2\x84=\x12(\n\"EN_CMD_ID_SESSION_SVR_ACK_SESSIONS\x10\xc3\x84=\x12&\n EN_CMD_ID_SESSION_SVR_UPDATE_ACK\x10\xc4\x84=\x12#\n\x1d\x45N_CMD_ID_SESSION_SVR_SET_TOP\x10\xc5\x84=\x12*\n$EN_CMD_ID_SESSION_SVR_REMOVE_SESSION\x10\xc7\x84=\x12)\n#EN_CMD_ID_SESSION_SVR_SINGLE_UNREAD\x10\xc8\x84=\x12+\n%EN_CMD_ID_SESSION_SVR_MY_GROUP_UNREAD\x10\xc9\x84=\x12-\n\'EN_CMD_ID_SESSION_SVR_UPDATE_UNFLW_READ\x10\xca\x84=\x12+\n%EN_CMD_ID_SESSION_SVR_GROUP_ASSIS_MSG\x10\xcb\x84=\x12)\n#EN_CMD_ID_SESSION_SVR_ACK_ASSIS_MSG\x10\xcc\x84=\x12*\n$EN_CMD_ID_SESSION_SVR_SESSION_DETAIL\x10\xcf\x84=\x12-\n\'EN_CMD_ID_SESSION_SVR_BATCH_SESS_DETAIL\x10\xd0\x84=\x12-\n\'EN_CMD_ID_SESSION_SVR_BATCH_RM_SESSIONS\x10\xd1\x84=*I\n\x11\x45NUM_BIZ_MSG_TYPE\x12\x17\n\x13\x42IZ_MSG_TYPE_NORMAL\x10\x00\x12\x1b\n\x17\x42IZ_MSG_TYPE_CARD_VIDEO\x10\x01*\x94\x03\n\tMsgSource\x12\x18\n\x14\x45N_MSG_SOURCE_UNKONW\x10\x00\x12\x15\n\x11\x45N_MSG_SOURCE_IOS\x10\x01\x12\x19\n\x15\x45N_MSG_SOURCE_ANDRIOD\x10\x02\x12\x14\n\x10\x45N_MSG_SOURCE_H5\x10\x03\x12\x14\n\x10\x45N_MSG_SOURCE_PC\x10\x04\x12\x1b\n\x17\x45N_MSG_SOURCE_BACKSTAGE\x10\x05\x12\x15\n\x11\x45N_MSG_SOURCE_BIZ\x10\x06\x12\x15\n\x11\x45N_MSG_SOURCE_WEB\x10\x07\x12\'\n#EN_MSG_SOURCE_AUTOREPLY_BY_FOLLOWED\x10\x08\x12*\n&EN_MSG_SOURCE_AUTOREPLY_BY_RECEIVE_MSG\x10\t\x12\'\n#EN_MSG_SOURCE_AUTOREPLY_BY_KEYWORDS\x10\n\x12%\n!EN_MSG_SOURCE_AUTOREPLY_BY_VOYAGE\x10\x0b\x12\x1f\n\x1b\x45N_MSG_SOURCE_VC_ATTACH_MSG\x10\x0c*\x8c\x0f\n\x07MsgType\x12\x17\n\x13\x45N_INVALID_MSG_TYPE\x10\x00\x12\x14\n\x10\x45N_MSG_TYPE_TEXT\x10\x01\x12\x13\n\x0f\x45N_MSG_TYPE_PIC\x10\x02\x12\x15\n\x11\x45N_MSG_TYPE_AUDIO\x10\x03\x12\x15\n\x11\x45N_MSG_TYPE_SHARE\x10\x04\x12\x19\n\x15\x45N_MSG_TYPE_DRAW_BACK\x10\x05\x12\x1b\n\x17\x45N_MSG_TYPE_CUSTOM_FACE\x10\x06\x12\x18\n\x14\x45N_MSG_TYPE_SHARE_V2\x10\x07\x12\x1a\n\x16\x45N_MSG_TYPE_SYS_CANCEL\x10\x08\x12\x1c\n\x18\x45N_MSG_TYPE_MINI_PROGRAM\x10\t\x12\x1a\n\x16\x45N_MSG_TYPE_NOTIFY_MSG\x10\n\x12\x1a\n\x16\x45N_MSG_TYPE_VIDEO_CARD\x10\x0b\x12\x1c\n\x18\x45N_MSG_TYPE_ARTICLE_CARD\x10\x0c\x12\x1c\n\x18\x45N_MSG_TYPE_PICTURE_CARD\x10\r\x12!\n\x1d\x45N_MSG_TYPE_COMMON_SHARE_CARD\x10\x0e\x12\x1c\n\x18\x45N_MSG_TYPE_BIZ_MSG_TYPE\x10\x32\x12\x1f\n\x1b\x45N_MSG_TYPE_MODIFY_MSG_TYPE\x10\x33\x12$\n EN_MSG_TYPE_GROUP_MEMBER_CHANGED\x10\x65\x12$\n EN_MSG_TYPE_GROUP_STATUS_CHANGED\x10\x66\x12%\n!EN_MSG_TYPE_GROUP_DYNAMIC_CHANGED\x10g\x12\"\n\x1e\x45N_MSG_TYPE_GROUP_LIST_CHANGED\x10h\x12#\n\x1f\x45M_MSG_TYPE_FRIEND_LIST_CHANGED\x10i\x12$\n EN_MSG_TYPE_GROUP_DETAIL_CHANGED\x10j\x12)\n%EN_MSG_TYPE_GROUP_MEMBER_ROLE_CHANGED\x10k\x12!\n\x1d\x45N_MSG_TYPE_NOTICE_WATCH_LIST\x10l\x12)\n%EN_MSG_TYPE_NOTIFY_NEW_REPLY_RECIEVED\x10m\x12&\n\"EN_MSG_TYPE_NOTIFY_NEW_AT_RECIEVED\x10n\x12*\n&EN_MSG_TYPE_NOTIFY_NEW_PRAISE_RECIEVED\x10o\x12&\n\"EN_MSG_TYPE_NOTIFY_NEW_UP_RECIEVED\x10p\x12,\n(EN_MSG_TYPE_NOTIFY_NEW_REPLY_RECIEVED_V2\x10q\x12)\n%EN_MSG_TYPE_NOTIFY_NEW_AT_RECIEVED_V2\x10r\x12-\n)EN_MSG_TYPE_NOTIFY_NEW_PRAISE_RECIEVED_V2\x10s\x12*\n&EN_MSG_TYPE_GROUP_DETAIL_CHANGED_MULTI\x10t\x12/\n+EN_MSG_TYPE_GROUP_MEMBER_ROLE_CHANGED_MULTI\x10u\x12#\n\x1f\x45N_MSG_TYPE_NOTIFY_ANTI_DISTURB\x10v\x12$\n\x1f\x45N_MSG_TYPE_SYS_GROUP_DISSOLVED\x10\xc9\x01\x12!\n\x1c\x45N_MSG_TYPE_SYS_GROUP_JOINED\x10\xca\x01\x12(\n#EN_MSG_TYPE_SYS_GROUP_MEMBER_EXITED\x10\xcb\x01\x12&\n!EN_MSG_TYPE_SYS_GROUP_ADMIN_FIRED\x10\xcc\x01\x12(\n#EN_MSG_TYPE_SYS_GROUP_MEMBER_KICKED\x10\xcd\x01\x12)\n$EN_MSG_TYPE_SYS_GROUP_ADMIN_KICK_OFF\x10\xce\x01\x12%\n EN_MSG_TYPE_SYS_GROUP_ADMIN_DUTY\x10\xcf\x01\x12\'\n\"EN_MSG_TYPE_SYS_GROUP_AUTO_CREATED\x10\xd0\x01\x12!\n\x1c\x45N_MSG_TYPE_SYS_FRIEND_APPLY\x10\xd2\x01\x12%\n EN_MSG_TYPE_SYS_FRIEND_APPLY_ACK\x10\xd3\x01\x12,\n\'EN_MSG_TYPE_SYS_GROUP_APPLY_FOR_JOINING\x10\xd4\x01\x12\x34\n/EN_MSG_TYPE_SYS_GROUP_ADMIN_ACCEPTED_USER_APPLY\x10\xd5\x01\x12#\n\x1e\x45N_MSG_TYPE_CHAT_MEMBER_JOINED\x10\xad\x02\x12#\n\x1e\x45N_MSG_TYPE_CHAT_MEMBER_EXITED\x10\xae\x02\x12#\n\x1e\x45N_MSG_TYPE_CHAT_GROUP_FREEZED\x10\xaf\x02\x12%\n EN_MSG_TYPE_CHAT_GROUP_DISSOLVED\x10\xb0\x02\x12#\n\x1e\x45N_MSG_TYPE_CHAT_GROUP_CREATED\x10\xb1\x02\x12#\n\x1e\x45N_MSG_TYPE_CHAT_POPUP_SESSION\x10\xb2\x02*l\n\nRecverType\x12\x11\n\rEN_NO_MEANING\x10\x00\x12\x17\n\x13\x45N_RECVER_TYPE_PEER\x10\x01\x12\x18\n\x14\x45N_RECVER_TYPE_GROUP\x10\x02\x12\x18\n\x14\x45N_RECVER_TYPE_PEERS\x10\x03*y\n\x0fRelationLogType\x12\x17\n\x13\x45N_INVALID_LOG_TYPE\x10\x00\x12\x11\n\rEN_ADD_FRIEND\x10\x01\x12\x14\n\x10\x45N_REMOVE_FRIEND\x10\x02\x12\x11\n\rEN_JOIN_GROUP\x10\x03\x12\x11\n\rEN_EXIT_GROUP\x10\x04*\x82\x01\n\x0cSESSION_TYPE\x12\x18\n\x14INVALID_SESSION_TYPE\x10\x00\x12\x13\n\x0fUN_FOLD_SESSION\x10\x01\x12\x1c\n\x18UN_FOLLOW_SINGLE_SESSION\x10\x02\x12\x14\n\x10MY_GROUP_SESSION\x10\x03\x12\x0f\n\x0b\x41LL_SESSION\x10\x04\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'bilibili.im.type.im_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _CMDID._serialized_start = 2352
    _CMDID._serialized_end = 3140
    _ENUM_BIZ_MSG_TYPE._serialized_start = 3142
    _ENUM_BIZ_MSG_TYPE._serialized_end = 3215
    _MSGSOURCE._serialized_start = 3218
    _MSGSOURCE._serialized_end = 3622
    _MSGTYPE._serialized_start = 3625
    _MSGTYPE._serialized_end = 5557
    _RECVERTYPE._serialized_start = 5559
    _RECVERTYPE._serialized_end = 5667
    _RELATIONLOGTYPE._serialized_start = 5669
    _RELATIONLOGTYPE._serialized_end = 5790
    _SESSION_TYPE._serialized_start = 5793
    _SESSION_TYPE._serialized_end = 5923
    _ACCOUNTINFO._serialized_start = 47
    _ACCOUNTINFO._serialized_end = 91
    _FRIENDRELATION._serialized_start = 93
    _FRIENDRELATION._serialized_end = 174
    _GROUPRELATION._serialized_start = 177
    _GROUPRELATION._serialized_end = 412
    _HIGHTEXT._serialized_start = 414
    _HIGHTEXT._serialized_end = 467
    _IMGINFO._serialized_start = 469
    _IMGINFO._serialized_end = 541
    _KEYHITINFOS._serialized_start = 543
    _KEYHITINFOS._serialized_end = 635
    _MEDAL._serialized_start = 638
    _MEDAL._serialized_end = 941
    _MSG._serialized_start = 944
    _MSG._serialized_end = 1407
    _RELATIONLOG._serialized_start = 1410
    _RELATIONLOG._serialized_end = 1613
    _SESSIONINFO._serialized_start = 1616
    _SESSIONINFO._serialized_end = 2249
    _USERLABEL._serialized_start = 2251
    _USERLABEL._serialized_end = 2349
# @@protoc_insertion_point(module_scope)
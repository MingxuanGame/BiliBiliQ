# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/main/community/reply/v1/reply.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n,bilibili/main/community/reply/v1/reply.proto\x12 bilibili.main.community.reply.v1\x1a\x19google/protobuf/any.proto\"U\n\x08\x41\x63tivity\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\x03\x12\x16\n\x0e\x61\x63tivity_state\x18\x02 \x01(\x03\x12\x1c\n\x14\x61\x63tivity_placeholder\x18\x03 \x01(\t\"G\n\x11\x41rticleSearchItem\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bup_nickname\x18\x02 \x01(\t\x12\x0e\n\x06\x63overs\x18\x03 \x03(\t\"j\n\x07\x41tGroup\x12\x12\n\ngroup_type\x18\x01 \x01(\x05\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12\x37\n\x05items\x18\x03 \x03(\x0b\x32(.bilibili.main.community.reply.v1.AtItem\"]\n\x06\x41tItem\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x03 \x01(\t\x12\x0c\n\x04\x66\x61ns\x18\x04 \x01(\x05\x12\x1c\n\x14official_verify_type\x18\x05 \x01(\x05\"J\n\rAtSearchReply\x12\x39\n\x06groups\x18\x01 \x03(\x0b\x32).bilibili.main.community.reply.v1.AtGroup\"+\n\x0b\x41tSearchReq\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x0f\n\x07keyword\x18\x02 \x01(\t\"2\n\x02\x43M\x12,\n\x0esource_content\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"\x83\x07\n\x07\x43ontent\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x45\n\x06menber\x18\x02 \x03(\x0b\x32\x35.bilibili.main.community.reply.v1.Content.MenberEntry\x12\x43\n\x05\x65mote\x18\x03 \x03(\x0b\x32\x34.bilibili.main.community.reply.v1.Content.EmoteEntry\x12\x43\n\x05topic\x18\x04 \x03(\x0b\x32\x34.bilibili.main.community.reply.v1.Content.TopicEntry\x12?\n\x03url\x18\x05 \x03(\x0b\x32\x32.bilibili.main.community.reply.v1.Content.UrlEntry\x12\x34\n\x04vote\x18\x06 \x01(\x0b\x32&.bilibili.main.community.reply.v1.Vote\x12R\n\x0e\x61t_name_to_mid\x18\x07 \x03(\x0b\x32:.bilibili.main.community.reply.v1.Content.AtNameToMidEntry\x12=\n\trich_text\x18\x08 \x01(\x0b\x32*.bilibili.main.community.reply.v1.RichText\x1aW\n\x0bMenberEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.bilibili.main.community.reply.v1.Member:\x02\x38\x01\x1aU\n\nEmoteEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.bilibili.main.community.reply.v1.Emote:\x02\x38\x01\x1aU\n\nTopicEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.bilibili.main.community.reply.v1.Topic:\x02\x38\x01\x1aQ\n\x08UrlEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.bilibili.main.community.reply.v1.Url:\x02\x38\x01\x1a\x32\n\x10\x41tNameToMidEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\x92\x01\n\x0b\x43ursorReply\x12\x0c\n\x04next\x18\x01 \x01(\x03\x12\x0c\n\x04prev\x18\x02 \x01(\x03\x12\x0f\n\x07isBegin\x18\x03 \x01(\x08\x12\r\n\x05isEnd\x18\x04 \x01(\x08\x12\x34\n\x04mode\x18\x05 \x01(\x0e\x32&.bilibili.main.community.reply.v1.Mode\x12\x11\n\tmode_text\x18\x06 \x01(\t\"]\n\tCursorReq\x12\x0c\n\x04next\x18\x01 \x01(\x03\x12\x0c\n\x04prev\x18\x02 \x01(\x03\x12\x34\n\x04mode\x18\x04 \x01(\x0e\x32&.bilibili.main.community.reply.v1.Mode\"\xcf\x02\n\x0f\x44\x65tailListReply\x12=\n\x06\x63ursor\x18\x01 \x01(\x0b\x32-.bilibili.main.community.reply.v1.CursorReply\x12I\n\x0fsubject_control\x18\x02 \x01(\x0b\x32\x30.bilibili.main.community.reply.v1.SubjectControl\x12\x39\n\x04root\x18\x03 \x01(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\x12<\n\x08\x61\x63tivity\x18\x04 \x01(\x0b\x32*.bilibili.main.community.reply.v1.Activity\x12\x39\n\x05likes\x18\x05 \x01(\x0b\x32*.bilibili.main.community.reply.v1.LikeInfo\"\xc5\x01\n\rDetailListReq\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x0c\n\x04type\x18\x02 \x01(\x03\x12\x0c\n\x04root\x18\x03 \x01(\x03\x12\x0c\n\x04rpid\x18\x04 \x01(\x03\x12;\n\x06\x63ursor\x18\x05 \x01(\x0b\x32+.bilibili.main.community.reply.v1.CursorReq\x12@\n\x05scene\x18\x06 \x01(\x0e\x32\x31.bilibili.main.community.reply.v1.DetailListScene\"\x97\x02\n\x0f\x44ialogListReply\x12=\n\x06\x63ursor\x18\x01 \x01(\x0b\x32-.bilibili.main.community.reply.v1.CursorReply\x12I\n\x0fsubject_control\x18\x02 \x01(\x0b\x32\x30.bilibili.main.community.reply.v1.SubjectControl\x12<\n\x07replies\x18\x03 \x03(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\x12<\n\x08\x61\x63tivity\x18\x04 \x01(\x0b\x32*.bilibili.main.community.reply.v1.Activity\"\x83\x01\n\rDialogListReq\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x0c\n\x04type\x18\x02 \x01(\x03\x12\x0c\n\x04root\x18\x03 \x01(\x03\x12\x0c\n\x04rpid\x18\x04 \x01(\x03\x12;\n\x06\x63ursor\x18\x05 \x01(\x0b\x32+.bilibili.main.community.reply.v1.CursorReq\"\x1d\n\x07\x45\x66\x66\x65\x63ts\x12\x12\n\npreloading\x18\x01 \x01(\t\"\x87\x01\n\x05\x45mote\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x10\n\x08jump_url\x18\x03 \x01(\t\x12\x12\n\njump_title\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\x03\x12\x12\n\npackage_id\x18\x06 \x01(\x03\x12\x0f\n\x07gif_url\x18\x07 \x01(\t\x12\x0c\n\x04text\x18\x08 \x01(\t\"f\n\x0fGoodsSearchItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\t\x12\x0e\n\x06income\x18\x04 \x01(\t\x12\x0b\n\x03img\x18\x05 \x01(\t\x12\r\n\x05label\x18\x06 \x01(\t\"\x9b\x01\n\x08LikeInfo\x12>\n\x05items\x18\x01 \x03(\x0b\x32/.bilibili.main.community.reply.v1.LikeInfo.Item\x12\r\n\x05title\x18\x02 \x01(\t\x1a@\n\x04Item\x12\x38\n\x06member\x18\x01 \x01(\x0b\x32(.bilibili.main.community.reply.v1.Member\"\xc7\x02\n\x07Lottery\x12\x12\n\nlottery_id\x18\x01 \x01(\x03\x12\x16\n\x0elottery_status\x18\x02 \x01(\x03\x12\x13\n\x0blottery_mid\x18\x03 \x01(\x03\x12\x14\n\x0clottery_time\x18\x04 \x01(\x03\x12\x0b\n\x03oid\x18\x05 \x01(\x03\x12\x0c\n\x04type\x18\x06 \x01(\x03\x12\r\n\x05\x63time\x18\x07 \x01(\x03\x12:\n\x07\x63ontent\x18\x08 \x01(\x0b\x32).bilibili.main.community.reply.v1.Content\x12\x38\n\x06member\x18\t \x01(\x0b\x32(.bilibili.main.community.reply.v1.Member\x12\x45\n\rreply_control\x18\n \x01(\x0b\x32..bilibili.main.community.reply.v1.ReplyControl\"\xb9\x08\n\rMainListReply\x12=\n\x06\x63ursor\x18\x01 \x01(\x0b\x32-.bilibili.main.community.reply.v1.CursorReply\x12<\n\x07replies\x18\x02 \x03(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\x12I\n\x0fsubject_control\x18\x03 \x01(\x0b\x32\x30.bilibili.main.community.reply.v1.SubjectControl\x12;\n\x06up_top\x18\x04 \x01(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\x12>\n\tadmin_top\x18\x05 \x01(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\x12=\n\x08vote_top\x18\x06 \x01(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\x12\x38\n\x06notice\x18\x07 \x01(\x0b\x32(.bilibili.main.community.reply.v1.Notice\x12:\n\x07lottery\x18\x08 \x01(\x0b\x32).bilibili.main.community.reply.v1.Lottery\x12<\n\x08\x61\x63tivity\x18\t \x01(\x0b\x32*.bilibili.main.community.reply.v1.Activity\x12\x43\n\x0cup_selection\x18\n \x01(\x0b\x32-.bilibili.main.community.reply.v1.UpSelection\x12\x30\n\x02\x63m\x18\x0b \x01(\x0b\x32$.bilibili.main.community.reply.v1.CM\x12:\n\x07\x65\x66\x66\x65\x63ts\x18\x0c \x01(\x0b\x32).bilibili.main.community.reply.v1.Effects\x12>\n\toperation\x18\r \x01(\x0b\x32+.bilibili.main.community.reply.v1.Operation\x12@\n\x0btop_replies\x18\x0e \x03(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\x12\x36\n\x03qoe\x18\x0f \x01(\x0b\x32).bilibili.main.community.reply.v1.QoeInfo\x12Q\n\tcallbacks\x18\x10 \x03(\x0b\x32>.bilibili.main.community.reply.v1.MainListReply.CallbacksEntry\x1a\x30\n\x0e\x43\x61llbacksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\xc0\x01\n\x0bMainListReq\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x0c\n\x04type\x18\x02 \x01(\x03\x12;\n\x06\x63ursor\x18\x03 \x01(\x0b\x32+.bilibili.main.community.reply.v1.CursorReq\x12\r\n\x05\x65xtra\x18\x04 \x01(\t\x12\x10\n\x08\x61\x64_extra\x18\x05 \x01(\t\x12\x0c\n\x04rpid\x18\x06 \x01(\x03\x12\x11\n\tseek_rpid\x18\x07 \x01(\x03\x12\x17\n\x0f\x66ilter_tag_name\x18\x08 \x01(\t\"\xba\n\n\x06Member\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x04 \x01(\t\x12\r\n\x05level\x18\x05 \x01(\x03\x12\x1c\n\x14official_verify_type\x18\x06 \x01(\x03\x12\x10\n\x08vip_type\x18\x07 \x01(\x03\x12\x12\n\nvip_status\x18\x08 \x01(\x03\x12\x16\n\x0evip_theme_type\x18\t \x01(\x03\x12\x16\n\x0evip_label_path\x18\n \x01(\t\x12\x1a\n\x12garb_pendant_image\x18\x0b \x01(\t\x12\x17\n\x0fgarb_card_image\x18\x0c \x01(\t\x12\"\n\x1agarb_card_image_with_focus\x18\r \x01(\t\x12\x1a\n\x12garb_card_jump_url\x18\x0e \x01(\t\x12\x18\n\x10garb_card_number\x18\x0f \x01(\t\x12\x1b\n\x13garb_card_fan_color\x18\x10 \x01(\t\x12\x18\n\x10garb_card_is_fan\x18\x11 \x01(\x08\x12\x17\n\x0f\x66\x61ns_medal_name\x18\x12 \x01(\t\x12\x18\n\x10\x66\x61ns_medal_level\x18\x13 \x01(\x03\x12\x18\n\x10\x66\x61ns_medal_color\x18\x14 \x01(\x03\x12\x1a\n\x12vip_nickname_color\x18\x15 \x01(\t\x12\x1c\n\x14vip_avatar_subscript\x18\x16 \x01(\x05\x12\x16\n\x0evip_label_text\x18\x17 \x01(\t\x12\x17\n\x0fvip_label_theme\x18\x18 \x01(\t\x12\x1c\n\x14\x66\x61ns_medal_color_end\x18\x19 \x01(\x03\x12\x1f\n\x17\x66\x61ns_medal_color_border\x18\x1a \x01(\x03\x12\x1d\n\x15\x66\x61ns_medal_color_name\x18\x1b \x01(\x03\x12\x1e\n\x16\x66\x61ns_medal_color_level\x18\x1c \x01(\x03\x12\x18\n\x10\x66\x61ns_guard_level\x18\x1d \x01(\x03\x12\x10\n\x08\x66\x61\x63\x65_nft\x18\x1e \x01(\x05\x12\x14\n\x0c\x66\x61\x63\x65_nft_new\x18\x1f \x01(\x05\x12\x18\n\x10is_senior_member\x18  \x01(\x05\x12P\n\x0fnft_interaction\x18! \x01(\x0b\x32\x37.bilibili.main.community.reply.v1.Member.NftInteraction\x12\x17\n\x0f\x66\x61ns_guard_icon\x18\" \x01(\t\x12\x17\n\x0f\x66\x61ns_honor_icon\x18# \x01(\t\x1a\xa3\x01\n\x06Region\x12\x41\n\x04type\x18\x01 \x01(\x0e\x32\x33.bilibili.main.community.reply.v1.Member.RegionType\x12\x0c\n\x04icon\x18\x02 \x01(\t\x12H\n\x0bshow_status\x18\x03 \x01(\x0e\x32\x33.bilibili.main.community.reply.v1.Member.ShowStatus\x1a\x86\x01\n\x0eNftInteraction\x12\r\n\x05itype\x18\x01 \x01(\t\x12\x14\n\x0cmetadata_url\x18\x02 \x01(\t\x12\x0e\n\x06nft_id\x18\x03 \x01(\t\x12?\n\x06region\x18\x04 \x01(\x0b\x32/.bilibili.main.community.reply.v1.Member.Region\"0\n\nRegionType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0c\n\x08MAINLAND\x10\x01\x12\x07\n\x03GAT\x10\x02\":\n\nShowStatus\x12\x0f\n\x0bSHOWDEFAULT\x10\x00\x12\x12\n\x0eZOOMINMAINLAND\x10\x01\x12\x07\n\x03RAW\x10\x02\"\x93\x0e\n\x08MemberV2\x12?\n\x05\x62\x61sic\x18\x01 \x01(\x0b\x32\x30.bilibili.main.community.reply.v1.MemberV2.Basic\x12\x45\n\x08official\x18\x02 \x01(\x0b\x32\x33.bilibili.main.community.reply.v1.MemberV2.Official\x12;\n\x03vip\x18\x03 \x01(\x0b\x32..bilibili.main.community.reply.v1.MemberV2.Vip\x12=\n\x04garb\x18\x04 \x01(\x0b\x32/.bilibili.main.community.reply.v1.MemberV2.Garb\x12?\n\x05medal\x18\x05 \x01(\x0b\x32\x30.bilibili.main.community.reply.v1.MemberV2.Medal\x12;\n\x03nft\x18\x06 \x01(\x0b\x32..bilibili.main.community.reply.v1.MemberV2.Nft\x12\x41\n\x06senior\x18\x07 \x01(\x0b\x32\x31.bilibili.main.community.reply.v1.MemberV2.Senior\x12I\n\ncontractor\x18\x08 \x01(\x0b\x32\x35.bilibili.main.community.reply.v1.MemberV2.Contractor\x1aL\n\x05\x42\x61sic\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x04 \x01(\t\x12\r\n\x05level\x18\x05 \x01(\x03\x1a\x1f\n\x08Official\x12\x13\n\x0bverify_type\x18\x01 \x01(\x03\x1a\xaa\x01\n\x03Vip\x12\x0c\n\x04type\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x03\x12\x12\n\ntheme_type\x18\x03 \x01(\x03\x12\x12\n\nlabel_path\x18\x04 \x01(\t\x12\x16\n\x0enickname_color\x18\x05 \x01(\t\x12\x18\n\x10\x61vatar_subscript\x18\x06 \x01(\x05\x12\x12\n\nlabel_text\x18\x07 \x01(\t\x12\x17\n\x0fvip_label_theme\x18\x08 \x01(\t\x1a\xa9\x01\n\x04Garb\x12\x15\n\rpendant_image\x18\x01 \x01(\t\x12\x12\n\ncard_image\x18\x02 \x01(\t\x12\x1d\n\x15\x63\x61rd_image_with_focus\x18\x03 \x01(\t\x12\x15\n\rcard_jump_url\x18\x04 \x01(\t\x12\x13\n\x0b\x63\x61rd_number\x18\x05 \x01(\t\x12\x16\n\x0e\x63\x61rd_fan_color\x18\x06 \x01(\t\x12\x13\n\x0b\x63\x61rd_is_fan\x18\x07 \x01(\x08\x1a\xcc\x01\n\x05Medal\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05level\x18\x02 \x01(\x03\x12\x13\n\x0b\x63olor_start\x18\x03 \x01(\x03\x12\x11\n\tcolor_end\x18\x04 \x01(\x03\x12\x14\n\x0c\x63olor_border\x18\x05 \x01(\x03\x12\x12\n\ncolor_name\x18\x06 \x01(\x03\x12\x13\n\x0b\x63olor_level\x18\x07 \x01(\x03\x12\x13\n\x0bguard_level\x18\x08 \x01(\x03\x12\x12\n\nfirst_icon\x18\t \x01(\t\x12\x16\n\x0elevel_bg_color\x18\x0b \x01(\x03\x1a\xa7\x01\n\x06Region\x12\x43\n\x04type\x18\x01 \x01(\x0e\x32\x35.bilibili.main.community.reply.v1.MemberV2.RegionType\x12\x0c\n\x04icon\x18\x02 \x01(\t\x12J\n\x0bshow_status\x18\x03 \x01(\x0e\x32\x35.bilibili.main.community.reply.v1.MemberV2.ShowStatus\x1a\x85\x01\n\x0bInteraction\x12\r\n\x05itype\x18\x01 \x01(\t\x12\x14\n\x0cmetadata_url\x18\x02 \x01(\t\x12\x0e\n\x06nft_id\x18\x03 \x01(\t\x12\x41\n\x06region\x18\x04 \x01(\x0b\x32\x31.bilibili.main.community.reply.v1.MemberV2.Region\x1a`\n\x03Nft\x12\x0c\n\x04\x66\x61\x63\x65\x18\x01 \x01(\x05\x12K\n\x0binteraction\x18\x02 \x01(\x0b\x32\x36.bilibili.main.community.reply.v1.MemberV2.Interaction\x1a\"\n\x06Senior\x12\x18\n\x10is_senior_member\x18\x01 \x01(\x05\x1a:\n\nContractor\x12\x15\n\ris_contractor\x18\x01 \x01(\x08\x12\x15\n\rcontract_desc\x18\x02 \x01(\t\"0\n\nRegionType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0c\n\x08MAINLAND\x10\x01\x12\x07\n\x03GAT\x10\x02\":\n\nShowStatus\x12\x0f\n\x0bSHOWDEFAULT\x10\x00\x12\x12\n\x0eZOOMINMAINLAND\x10\x01\x12\x07\n\x03RAW\x10\x02\"3\n\x06Notice\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"\xdc\x01\n\tOperation\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\x03\x12?\n\x05title\x18\x03 \x01(\x0b\x32\x30.bilibili.main.community.reply.v1.OperationTitle\x12\x42\n\x08subtitle\x18\x04 \x01(\x0b\x32\x30.bilibili.main.community.reply.v1.OperationTitle\x12\x0c\n\x04link\x18\x05 \x01(\t\x12\x14\n\x0creport_extra\x18\x06 \x01(\t\x12\x0c\n\x04icon\x18\x07 \x01(\t\"7\n\x0eOperationTitle\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x14\n\x0cis_highlight\x18\x02 \x01(\x08\"D\n\x12PGCVideoSearchItem\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\r\n\x05\x63over\x18\x03 \x01(\t\"\x95\x03\n\x10PreviewListReply\x12=\n\x06\x63ursor\x18\x01 \x01(\x0b\x32-.bilibili.main.community.reply.v1.CursorReply\x12<\n\x07replies\x18\x02 \x03(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\x12I\n\x0fsubject_control\x18\x03 \x01(\x0b\x32\x30.bilibili.main.community.reply.v1.SubjectControl\x12:\n\x05upTop\x18\x04 \x01(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\x12>\n\tadmin_top\x18\x05 \x01(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\x12=\n\x08vote_top\x18\x06 \x01(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\"h\n\x0ePreviewListReq\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x0c\n\x04type\x18\x02 \x01(\x03\x12;\n\x06\x63ursor\x18\x03 \x01(\x0b\x32+.bilibili.main.community.reply.v1.CursorReq\"\xb4\x01\n\x07QoeInfo\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\r\n\x05style\x18\x03 \x01(\x05\x12\r\n\x05title\x18\x04 \x01(\t\x12\x16\n\x0e\x66\x65\x65\x64\x62\x61\x63k_title\x18\x05 \x01(\t\x12\x43\n\x0bscore_items\x18\x06 \x03(\x0b\x32..bilibili.main.community.reply.v1.QoeScoreItem\x12\x14\n\x0c\x64isplay_rank\x18\x07 \x01(\x03\"9\n\x0cQoeScoreItem\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x02\"\xaf\x02\n\x0eReplyCardLabel\x12\x14\n\x0ctext_content\x18\x01 \x01(\t\x12\x16\n\x0etext_color_day\x18\x02 \x01(\t\x12\x18\n\x10text_color_night\x18\x03 \x01(\t\x12\x17\n\x0flabel_color_day\x18\x04 \x01(\t\x12\x19\n\x11label_color_night\x18\x05 \x01(\t\x12\r\n\x05image\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x07 \x01(\x05\x12\x12\n\nbackground\x18\x08 \x01(\t\x12\x18\n\x10\x62\x61\x63kground_width\x18\t \x01(\x01\x12\x19\n\x11\x62\x61\x63kground_height\x18\n \x01(\x01\x12\x10\n\x08jump_url\x18\x0b \x01(\t\x12\x0e\n\x06\x65\x66\x66\x65\x63t\x18\x0c \x01(\x03\x12\x19\n\x11\x65\x66\x66\x65\x63t_start_time\x18\r \x01(\x03\"\xc7\x04\n\x0cReplyControl\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\x03\x12\x0f\n\x07up_like\x18\x02 \x01(\x08\x12\x10\n\x08up_reply\x18\x03 \x01(\x08\x12\x17\n\x0fshow_follow_btn\x18\x04 \x01(\x08\x12\x11\n\tis_assist\x18\x05 \x01(\x08\x12\x12\n\nlabel_text\x18\x06 \x01(\t\x12\x11\n\tfollowing\x18\x07 \x01(\x08\x12\x10\n\x08\x66ollowed\x18\x08 \x01(\x08\x12\x0f\n\x07\x62locked\x18\t \x01(\x08\x12\x18\n\x10has_folded_reply\x18\n \x01(\x08\x12\x17\n\x0fis_folded_reply\x18\x0b \x01(\x08\x12\x11\n\tis_up_top\x18\x0c \x01(\x08\x12\x14\n\x0cis_admin_top\x18\r \x01(\x08\x12\x13\n\x0bis_vote_top\x18\x0e \x01(\x08\x12\x10\n\x08max_line\x18\x0f \x01(\x03\x12\x11\n\tinvisible\x18\x10 \x01(\x08\x12\x15\n\ris_contractor\x18\x11 \x01(\x08\x12\x0f\n\x07is_note\x18\x12 \x01(\x08\x12\x45\n\x0b\x63\x61rd_labels\x18\x13 \x03(\x0b\x32\x30.bilibili.main.community.reply.v1.ReplyCardLabel\x12\x1c\n\x14sub_reply_entry_text\x18\x14 \x01(\t\x12\x1c\n\x14sub_reply_title_text\x18\x15 \x01(\t\x12\x15\n\rcontract_desc\x18\x16 \x01(\t\x12\x11\n\ttime_desc\x18\x17 \x01(\t\x12\x11\n\tbiz_scene\x18\x18 \x01(\t\x12\x10\n\x08location\x18\x19 \x01(\t\"U\n\nReplyExtra\x12\x11\n\tseason_id\x18\x01 \x01(\x03\x12\x13\n\x0bseason_type\x18\x02 \x01(\x03\x12\r\n\x05\x65p_id\x18\x03 \x01(\x03\x12\x10\n\x08is_story\x18\x04 \x01(\x08\"\xd3\x03\n\tReplyInfo\x12<\n\x07replies\x18\x01 \x03(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\x12\n\n\x02id\x18\x02 \x01(\x03\x12\x0b\n\x03oid\x18\x03 \x01(\x03\x12\x0c\n\x04type\x18\x04 \x01(\x03\x12\x0b\n\x03mid\x18\x05 \x01(\x03\x12\x0c\n\x04root\x18\x06 \x01(\x03\x12\x0e\n\x06parent\x18\x07 \x01(\x03\x12\x0e\n\x06\x64ialog\x18\x08 \x01(\x03\x12\x0c\n\x04like\x18\t \x01(\x03\x12\r\n\x05\x63time\x18\n \x01(\x03\x12\r\n\x05\x63ount\x18\x0b \x01(\x03\x12:\n\x07\x63ontent\x18\x0c \x01(\x0b\x32).bilibili.main.community.reply.v1.Content\x12\x38\n\x06member\x18\r \x01(\x0b\x32(.bilibili.main.community.reply.v1.Member\x12\x45\n\rreply_control\x18\x0e \x01(\x0b\x32..bilibili.main.community.reply.v1.ReplyControl\x12=\n\tmember_v2\x18\x0f \x01(\x0b\x32*.bilibili.main.community.reply.v1.MemberV2\"L\n\x0eReplyInfoReply\x12:\n\x05reply\x18\x01 \x01(\x0b\x32+.bilibili.main.community.reply.v1.ReplyInfo\"+\n\x0cReplyInfoReq\x12\x0c\n\x04rpid\x18\x01 \x01(\x03\x12\r\n\x05scene\x18\x02 \x01(\x05\"R\n\x08RichText\x12>\n\x04note\x18\x01 \x01(\x0b\x32..bilibili.main.community.reply.v1.RichTextNoteH\x00\x42\x06\n\x04item\"[\n\x0cRichTextNote\x12\x0f\n\x07summary\x18\x01 \x01(\t\x12\x0e\n\x06images\x18\x02 \x03(\t\x12\x11\n\tclick_url\x18\x03 \x01(\t\x12\x17\n\x0flast_mtime_text\x18\x04 \x01(\t\"\xf1\x01\n\nSearchItem\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x42\n\x05goods\x18\x02 \x01(\x0b\x32\x31.bilibili.main.community.reply.v1.GoodsSearchItemH\x00\x12\x42\n\x05video\x18\x03 \x01(\x0b\x32\x31.bilibili.main.community.reply.v1.VideoSearchItemH\x00\x12\x46\n\x07\x61rticle\x18\x04 \x01(\x0b\x32\x33.bilibili.main.community.reply.v1.ArticleSearchItemH\x00\x42\x06\n\x04item\"7\n\x15SearchItemCursorReply\x12\x10\n\x08has_next\x18\x01 \x01(\x08\x12\x0c\n\x04next\x18\x02 \x01(\x03\"h\n\x13SearchItemCursorReq\x12\x0c\n\x04next\x18\x01 \x01(\x03\x12\x43\n\titem_type\x18\x02 \x01(\x0e\x32\x30.bilibili.main.community.reply.v1.SearchItemType\"\x93\x01\n\x16SearchItemPreHookReply\x12\x18\n\x10placeholder_text\x18\x01 \x01(\t\x12\x17\n\x0f\x62\x61\x63kground_text\x18\x02 \x01(\t\x12\x46\n\x0cordered_type\x18\x03 \x03(\x0e\x32\x30.bilibili.main.community.reply.v1.SearchItemType\"1\n\x14SearchItemPreHookReq\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x0c\n\x04type\x18\x02 \x01(\x03\"\xe2\x01\n\x0fSearchItemReply\x12G\n\x06\x63ursor\x18\x01 \x01(\x0b\x32\x37.bilibili.main.community.reply.v1.SearchItemCursorReply\x12;\n\x05items\x18\x02 \x03(\x0b\x32,.bilibili.main.community.reply.v1.SearchItem\x12I\n\x05\x65xtra\x18\x03 \x01(\x0b\x32:.bilibili.main.community.reply.v1.SearchItemReplyExtraInfo\",\n\x18SearchItemReplyExtraInfo\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\"\x82\x01\n\rSearchItemReq\x12\x45\n\x06\x63ursor\x18\x01 \x01(\x0b\x32\x35.bilibili.main.community.reply.v1.SearchItemCursorReq\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x03\x12\x0f\n\x07keyword\x18\x04 \x01(\t\"?\n\x13ShareRepliesInfoReq\x12\r\n\x05rpids\x18\x01 \x03(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x03\"\xf6\x02\n\x14ShareRepliesInfoResp\x12?\n\x05infos\x18\x01 \x03(\x0b\x32\x30.bilibili.main.community.reply.v1.ShareReplyInfo\x12\x12\n\nfrom_title\x18\x02 \x01(\t\x12\x0f\n\x07\x66rom_up\x18\x03 \x01(\t\x12\x10\n\x08\x66rom_pic\x18\x04 \x01(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x12\n\nslogan_pic\x18\x06 \x01(\t\x12\x13\n\x0bslogan_text\x18\x07 \x01(\t\x12@\n\x05topic\x18\x08 \x01(\x0b\x32\x31.bilibili.main.community.reply.v1.ShareReplyTopic\x12P\n\x05\x65xtra\x18\t \x01(\x0b\x32\x41.bilibili.main.community.reply.v1.ShareRepliesInfoResp.ShareExtra\x1a\x1c\n\nShareExtra\x12\x0e\n\x06is_pgc\x18\x01 \x01(\x08\"\xd5\x01\n\x0eShareReplyInfo\x12\x38\n\x06member\x18\x01 \x01(\x0b\x32(.bilibili.main.community.reply.v1.Member\x12:\n\x07\x63ontent\x18\x02 \x01(\x0b\x32).bilibili.main.community.reply.v1.Content\x12\r\n\x05title\x18\x03 \x01(\t\x12\x11\n\tsub_title\x18\x04 \x01(\t\x12\x18\n\x10\x61\x63hievement_text\x18\x05 \x01(\t\x12\x11\n\tlabel_url\x18\x06 \x01(\t\"^\n\x0fShareReplyTopic\x12\x36\n\x05topic\x18\x01 \x01(\x0b\x32\'.bilibili.main.community.reply.v1.Topic\x12\x13\n\x0borigin_text\x18\x02 \x01(\t\"\xb2\x05\n\x0eSubjectControl\x12\x0e\n\x06up_mid\x18\x01 \x01(\x03\x12\x11\n\tis_assist\x18\x02 \x01(\x08\x12\x11\n\tread_only\x18\x03 \x01(\x08\x12\x17\n\x0fhas_vote_access\x18\x04 \x01(\x08\x12\x1a\n\x12has_lottery_access\x18\x05 \x01(\x08\x12\x18\n\x10has_folded_reply\x18\x06 \x01(\x08\x12\x0f\n\x07\x62g_text\x18\x07 \x01(\t\x12\x12\n\nup_blocked\x18\x08 \x01(\x08\x12\x1b\n\x13has_activity_access\x18\t \x01(\x08\x12\x12\n\nshow_title\x18\n \x01(\x08\x12\x16\n\x0eshow_up_action\x18\x0b \x01(\x08\x12\x15\n\rswitcher_type\x18\x0c \x01(\x03\x12\x15\n\rinput_disable\x18\r \x01(\x08\x12\x11\n\troot_text\x18\x0e \x01(\t\x12\x12\n\nchild_text\x18\x0f \x01(\t\x12\r\n\x05\x63ount\x18\x10 \x01(\x03\x12\r\n\x05title\x18\x11 \x01(\t\x12\x13\n\x0bgiveup_text\x18\x12 \x01(\t\x12\x17\n\x0fhas_note_access\x18\x13 \x01(\x08\x12\x1a\n\x12\x64isable_jump_emote\x18\x14 \x01(\x08\x12#\n\x1b\x65mpty_background_text_plain\x18\x15 \x01(\t\x12\'\n\x1f\x65mpty_background_text_highlight\x18\x16 \x01(\t\x12\x1c\n\x14\x65mpty_background_uri\x18\x17 \x01(\t\x12W\n\x13support_filter_tags\x18\x18 \x03(\x0b\x32:.bilibili.main.community.reply.v1.SubjectControl.FilterTag\x1a+\n\tFilterTag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\t\"-\n\x10SuggestEmotesReq\x12\x0b\n\x03oid\x18\x01 \x01(\x03\x12\x0c\n\x04type\x18\x02 \x01(\x03\"L\n\x11SuggestEmotesResp\x12\x37\n\x06\x65motes\x18\x01 \x03(\x0b\x32\'.bilibili.main.community.reply.v1.Emote\"!\n\x05Topic\x12\x0c\n\x04link\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\"Y\n\x12UGCVideoSearchItem\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bup_nickname\x18\x02 \x01(\t\x12\x10\n\x08\x64uration\x18\x03 \x01(\x03\x12\r\n\x05\x63over\x18\x04 \x01(\t\":\n\x0bUpSelection\x12\x15\n\rpending_count\x18\x01 \x01(\x03\x12\x14\n\x0cignore_count\x18\x02 \x01(\x03\"\xd9\x03\n\x03Url\x12\r\n\x05title\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\x03\x12\x13\n\x0bprefix_icon\x18\x03 \x01(\t\x12\x16\n\x0e\x61pp_url_schema\x18\x04 \x01(\t\x12\x10\n\x08\x61pp_name\x18\x05 \x01(\t\x12\x18\n\x10\x61pp_package_name\x18\x06 \x01(\t\x12\x14\n\x0c\x63lick_report\x18\x07 \x01(\t\x12\x16\n\x0eis_half_screen\x18\x08 \x01(\x08\x12\x17\n\x0f\x65xposure_report\x18\t \x01(\t\x12:\n\x05\x65xtra\x18\n \x01(\x0b\x32+.bilibili.main.community.reply.v1.Url.Extra\x12\x11\n\tunderline\x18\x0b \x01(\x08\x12\x12\n\nmatch_once\x18\x0c \x01(\x08\x12\x0e\n\x06pc_url\x18\r \x01(\t\x12\x15\n\ricon_position\x18\x0e \x01(\x05\x1a\x89\x01\n\x05\x45xtra\x12\x15\n\rgoods_item_id\x18\x01 \x01(\x03\x12\x1e\n\x16goods_prefetched_cache\x18\x02 \x01(\t\x12\x17\n\x0fgoods_show_type\x18\x03 \x01(\x05\x12\x16\n\x0eis_word_search\x18\x04 \x01(\x08\x12\x18\n\x10goods_cm_control\x18\x05 \x01(\x03\"\x13\n\x11UserCallbackReply\"\xc3\x01\n\x0fUserCallbackReq\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x42\n\x05scene\x18\x02 \x01(\x0e\x32\x33.bilibili.main.community.reply.v1.UserCallbackScene\x12\x44\n\x06\x61\x63tion\x18\x03 \x01(\x0e\x32\x34.bilibili.main.community.reply.v1.UserCallbackAction\x12\x0b\n\x03oid\x18\x04 \x01(\x03\x12\x0c\n\x04type\x18\x05 \x01(\x03\"\xf1\x01\n\x0fVideoSearchItem\x12\x46\n\x04type\x18\x01 \x01(\x0e\x32\x38.bilibili.main.community.reply.v1.SearchItemVideoSubType\x12\x43\n\x03ugc\x18\x02 \x01(\x0b\x32\x34.bilibili.main.community.reply.v1.UGCVideoSearchItemH\x00\x12\x43\n\x03pgc\x18\x03 \x01(\x0b\x32\x34.bilibili.main.community.reply.v1.PGCVideoSearchItemH\x00\x42\x0c\n\nvideo_item\"0\n\x04Vote\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x03*6\n\x0f\x44\x65tailListScene\x12\t\n\x05REPLY\x10\x00\x12\x0c\n\x08MSG_FEED\x10\x01\x12\n\n\x06NOTIFY\x10\x02*K\n\x04Mode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0f\n\x0bUNSPECIFIED\x10\x01\x12\x12\n\x0eMAIN_LIST_TIME\x10\x02\x12\x11\n\rMAIN_LIST_HOT\x10\x03*J\n\x0eSearchItemType\x12\x15\n\x11\x44\x45\x46\x41ULT_ITEM_TYPE\x10\x00\x12\t\n\x05GOODS\x10\x01\x12\t\n\x05VIDEO\x10\x02\x12\x0b\n\x07\x41RTICLE\x10\x03**\n\x16SearchItemVideoSubType\x12\x07\n\x03UGC\x10\x00\x12\x07\n\x03PGC\x10\x01*!\n\x12UserCallbackAction\x12\x0b\n\x07\x44ismiss\x10\x00*\x1f\n\x11UserCallbackScene\x12\n\n\x06Insert\x10\x00\x32\x97\n\n\x05Reply\x12j\n\x08MainList\x12-.bilibili.main.community.reply.v1.MainListReq\x1a/.bilibili.main.community.reply.v1.MainListReply\x12p\n\nDetailList\x12/.bilibili.main.community.reply.v1.DetailListReq\x1a\x31.bilibili.main.community.reply.v1.DetailListReply\x12p\n\nDialogList\x12/.bilibili.main.community.reply.v1.DialogListReq\x1a\x31.bilibili.main.community.reply.v1.DialogListReply\x12s\n\x0bPreviewList\x12\x30.bilibili.main.community.reply.v1.PreviewListReq\x1a\x32.bilibili.main.community.reply.v1.PreviewListReply\x12\x85\x01\n\x11SearchItemPreHook\x12\x36.bilibili.main.community.reply.v1.SearchItemPreHookReq\x1a\x38.bilibili.main.community.reply.v1.SearchItemPreHookReply\x12p\n\nSearchItem\x12/.bilibili.main.community.reply.v1.SearchItemReq\x1a\x31.bilibili.main.community.reply.v1.SearchItemReply\x12j\n\x08\x41tSearch\x12-.bilibili.main.community.reply.v1.AtSearchReq\x1a/.bilibili.main.community.reply.v1.AtSearchReply\x12m\n\tReplyInfo\x12..bilibili.main.community.reply.v1.ReplyInfoReq\x1a\x30.bilibili.main.community.reply.v1.ReplyInfoReply\x12v\n\x0cUserCallback\x12\x31.bilibili.main.community.reply.v1.UserCallbackReq\x1a\x33.bilibili.main.community.reply.v1.UserCallbackReply\x12\x81\x01\n\x10ShareRepliesInfo\x12\x35.bilibili.main.community.reply.v1.ShareRepliesInfoReq\x1a\x36.bilibili.main.community.reply.v1.ShareRepliesInfoResp\x12x\n\rSuggestEmotes\x12\x32.bilibili.main.community.reply.v1.SuggestEmotesReq\x1a\x33.bilibili.main.community.reply.v1.SuggestEmotesRespb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'bilibili.main.community.reply.v1.reply_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _CONTENT_MENBERENTRY._options = None
    _CONTENT_MENBERENTRY._serialized_options = b'8\001'
    _CONTENT_EMOTEENTRY._options = None
    _CONTENT_EMOTEENTRY._serialized_options = b'8\001'
    _CONTENT_TOPICENTRY._options = None
    _CONTENT_TOPICENTRY._serialized_options = b'8\001'
    _CONTENT_URLENTRY._options = None
    _CONTENT_URLENTRY._serialized_options = b'8\001'
    _CONTENT_ATNAMETOMIDENTRY._options = None
    _CONTENT_ATNAMETOMIDENTRY._serialized_options = b'8\001'
    _MAINLISTREPLY_CALLBACKSENTRY._options = None
    _MAINLISTREPLY_CALLBACKSENTRY._serialized_options = b'8\001'
    _DETAILLISTSCENE._serialized_start = 14611
    _DETAILLISTSCENE._serialized_end = 14665
    _MODE._serialized_start = 14667
    _MODE._serialized_end = 14742
    _SEARCHITEMTYPE._serialized_start = 14744
    _SEARCHITEMTYPE._serialized_end = 14818
    _SEARCHITEMVIDEOSUBTYPE._serialized_start = 14820
    _SEARCHITEMVIDEOSUBTYPE._serialized_end = 14862
    _USERCALLBACKACTION._serialized_start = 14864
    _USERCALLBACKACTION._serialized_end = 14897
    _USERCALLBACKSCENE._serialized_start = 14899
    _USERCALLBACKSCENE._serialized_end = 14930
    _ACTIVITY._serialized_start = 109
    _ACTIVITY._serialized_end = 194
    _ARTICLESEARCHITEM._serialized_start = 196
    _ARTICLESEARCHITEM._serialized_end = 267
    _ATGROUP._serialized_start = 269
    _ATGROUP._serialized_end = 375
    _ATITEM._serialized_start = 377
    _ATITEM._serialized_end = 470
    _ATSEARCHREPLY._serialized_start = 472
    _ATSEARCHREPLY._serialized_end = 546
    _ATSEARCHREQ._serialized_start = 548
    _ATSEARCHREQ._serialized_end = 591
    _CM._serialized_start = 593
    _CM._serialized_end = 643
    _CONTENT._serialized_start = 646
    _CONTENT._serialized_end = 1545
    _CONTENT_MENBERENTRY._serialized_start = 1149
    _CONTENT_MENBERENTRY._serialized_end = 1236
    _CONTENT_EMOTEENTRY._serialized_start = 1238
    _CONTENT_EMOTEENTRY._serialized_end = 1323
    _CONTENT_TOPICENTRY._serialized_start = 1325
    _CONTENT_TOPICENTRY._serialized_end = 1410
    _CONTENT_URLENTRY._serialized_start = 1412
    _CONTENT_URLENTRY._serialized_end = 1493
    _CONTENT_ATNAMETOMIDENTRY._serialized_start = 1495
    _CONTENT_ATNAMETOMIDENTRY._serialized_end = 1545
    _CURSORREPLY._serialized_start = 1548
    _CURSORREPLY._serialized_end = 1694
    _CURSORREQ._serialized_start = 1696
    _CURSORREQ._serialized_end = 1789
    _DETAILLISTREPLY._serialized_start = 1792
    _DETAILLISTREPLY._serialized_end = 2127
    _DETAILLISTREQ._serialized_start = 2130
    _DETAILLISTREQ._serialized_end = 2327
    _DIALOGLISTREPLY._serialized_start = 2330
    _DIALOGLISTREPLY._serialized_end = 2609
    _DIALOGLISTREQ._serialized_start = 2612
    _DIALOGLISTREQ._serialized_end = 2743
    _EFFECTS._serialized_start = 2745
    _EFFECTS._serialized_end = 2774
    _EMOTE._serialized_start = 2777
    _EMOTE._serialized_end = 2912
    _GOODSSEARCHITEM._serialized_start = 2914
    _GOODSSEARCHITEM._serialized_end = 3016
    _LIKEINFO._serialized_start = 3019
    _LIKEINFO._serialized_end = 3174
    _LIKEINFO_ITEM._serialized_start = 3110
    _LIKEINFO_ITEM._serialized_end = 3174
    _LOTTERY._serialized_start = 3177
    _LOTTERY._serialized_end = 3504
    _MAINLISTREPLY._serialized_start = 3507
    _MAINLISTREPLY._serialized_end = 4588
    _MAINLISTREPLY_CALLBACKSENTRY._serialized_start = 4540
    _MAINLISTREPLY_CALLBACKSENTRY._serialized_end = 4588
    _MAINLISTREQ._serialized_start = 4591
    _MAINLISTREQ._serialized_end = 4783
    _MEMBER._serialized_start = 4786
    _MEMBER._serialized_end = 6124
    _MEMBER_REGION._serialized_start = 5714
    _MEMBER_REGION._serialized_end = 5877
    _MEMBER_NFTINTERACTION._serialized_start = 5880
    _MEMBER_NFTINTERACTION._serialized_end = 6014
    _MEMBER_REGIONTYPE._serialized_start = 6016
    _MEMBER_REGIONTYPE._serialized_end = 6064
    _MEMBER_SHOWSTATUS._serialized_start = 6066
    _MEMBER_SHOWSTATUS._serialized_end = 6124
    _MEMBERV2._serialized_start = 6127
    _MEMBERV2._serialized_end = 7938
    _MEMBERV2_BASIC._serialized_start = 6667
    _MEMBERV2_BASIC._serialized_end = 6743
    _MEMBERV2_OFFICIAL._serialized_start = 6745
    _MEMBERV2_OFFICIAL._serialized_end = 6776
    _MEMBERV2_VIP._serialized_start = 6779
    _MEMBERV2_VIP._serialized_end = 6949
    _MEMBERV2_GARB._serialized_start = 6952
    _MEMBERV2_GARB._serialized_end = 7121
    _MEMBERV2_MEDAL._serialized_start = 7124
    _MEMBERV2_MEDAL._serialized_end = 7328
    _MEMBERV2_REGION._serialized_start = 7331
    _MEMBERV2_REGION._serialized_end = 7498
    _MEMBERV2_INTERACTION._serialized_start = 7501
    _MEMBERV2_INTERACTION._serialized_end = 7634
    _MEMBERV2_NFT._serialized_start = 7636
    _MEMBERV2_NFT._serialized_end = 7732
    _MEMBERV2_SENIOR._serialized_start = 7734
    _MEMBERV2_SENIOR._serialized_end = 7768
    _MEMBERV2_CONTRACTOR._serialized_start = 7770
    _MEMBERV2_CONTRACTOR._serialized_end = 7828
    _MEMBERV2_REGIONTYPE._serialized_start = 6016
    _MEMBERV2_REGIONTYPE._serialized_end = 6064
    _MEMBERV2_SHOWSTATUS._serialized_start = 6066
    _MEMBERV2_SHOWSTATUS._serialized_end = 6124
    _NOTICE._serialized_start = 7940
    _NOTICE._serialized_end = 7991
    _OPERATION._serialized_start = 7994
    _OPERATION._serialized_end = 8214
    _OPERATIONTITLE._serialized_start = 8216
    _OPERATIONTITLE._serialized_end = 8271
    _PGCVIDEOSEARCHITEM._serialized_start = 8273
    _PGCVIDEOSEARCHITEM._serialized_end = 8341
    _PREVIEWLISTREPLY._serialized_start = 8344
    _PREVIEWLISTREPLY._serialized_end = 8749
    _PREVIEWLISTREQ._serialized_start = 8751
    _PREVIEWLISTREQ._serialized_end = 8855
    _QOEINFO._serialized_start = 8858
    _QOEINFO._serialized_end = 9038
    _QOESCOREITEM._serialized_start = 9040
    _QOESCOREITEM._serialized_end = 9097
    _REPLYCARDLABEL._serialized_start = 9100
    _REPLYCARDLABEL._serialized_end = 9403
    _REPLYCONTROL._serialized_start = 9406
    _REPLYCONTROL._serialized_end = 9989
    _REPLYEXTRA._serialized_start = 9991
    _REPLYEXTRA._serialized_end = 10076
    _REPLYINFO._serialized_start = 10079
    _REPLYINFO._serialized_end = 10546
    _REPLYINFOREPLY._serialized_start = 10548
    _REPLYINFOREPLY._serialized_end = 10624
    _REPLYINFOREQ._serialized_start = 10626
    _REPLYINFOREQ._serialized_end = 10669
    _RICHTEXT._serialized_start = 10671
    _RICHTEXT._serialized_end = 10753
    _RICHTEXTNOTE._serialized_start = 10755
    _RICHTEXTNOTE._serialized_end = 10846
    _SEARCHITEM._serialized_start = 10849
    _SEARCHITEM._serialized_end = 11090
    _SEARCHITEMCURSORREPLY._serialized_start = 11092
    _SEARCHITEMCURSORREPLY._serialized_end = 11147
    _SEARCHITEMCURSORREQ._serialized_start = 11149
    _SEARCHITEMCURSORREQ._serialized_end = 11253
    _SEARCHITEMPREHOOKREPLY._serialized_start = 11256
    _SEARCHITEMPREHOOKREPLY._serialized_end = 11403
    _SEARCHITEMPREHOOKREQ._serialized_start = 11405
    _SEARCHITEMPREHOOKREQ._serialized_end = 11454
    _SEARCHITEMREPLY._serialized_start = 11457
    _SEARCHITEMREPLY._serialized_end = 11683
    _SEARCHITEMREPLYEXTRAINFO._serialized_start = 11685
    _SEARCHITEMREPLYEXTRAINFO._serialized_end = 11729
    _SEARCHITEMREQ._serialized_start = 11732
    _SEARCHITEMREQ._serialized_end = 11862
    _SHAREREPLIESINFOREQ._serialized_start = 11864
    _SHAREREPLIESINFOREQ._serialized_end = 11927
    _SHAREREPLIESINFORESP._serialized_start = 11930
    _SHAREREPLIESINFORESP._serialized_end = 12304
    _SHAREREPLIESINFORESP_SHAREEXTRA._serialized_start = 12276
    _SHAREREPLIESINFORESP_SHAREEXTRA._serialized_end = 12304
    _SHAREREPLYINFO._serialized_start = 12307
    _SHAREREPLYINFO._serialized_end = 12520
    _SHAREREPLYTOPIC._serialized_start = 12522
    _SHAREREPLYTOPIC._serialized_end = 12616
    _SUBJECTCONTROL._serialized_start = 12619
    _SUBJECTCONTROL._serialized_end = 13309
    _SUBJECTCONTROL_FILTERTAG._serialized_start = 13266
    _SUBJECTCONTROL_FILTERTAG._serialized_end = 13309
    _SUGGESTEMOTESREQ._serialized_start = 13311
    _SUGGESTEMOTESREQ._serialized_end = 13356
    _SUGGESTEMOTESRESP._serialized_start = 13358
    _SUGGESTEMOTESRESP._serialized_end = 13434
    _TOPIC._serialized_start = 13436
    _TOPIC._serialized_end = 13469
    _UGCVIDEOSEARCHITEM._serialized_start = 13471
    _UGCVIDEOSEARCHITEM._serialized_end = 13560
    _UPSELECTION._serialized_start = 13562
    _UPSELECTION._serialized_end = 13620
    _URL._serialized_start = 13623
    _URL._serialized_end = 14096
    _URL_EXTRA._serialized_start = 13959
    _URL_EXTRA._serialized_end = 14096
    _USERCALLBACKREPLY._serialized_start = 14098
    _USERCALLBACKREPLY._serialized_end = 14117
    _USERCALLBACKREQ._serialized_start = 14120
    _USERCALLBACKREQ._serialized_end = 14315
    _VIDEOSEARCHITEM._serialized_start = 14318
    _VIDEOSEARCHITEM._serialized_end = 14559
    _VOTE._serialized_start = 14561
    _VOTE._serialized_end = 14609
    _REPLY._serialized_start = 14933
    _REPLY._serialized_end = 16236
# @@protoc_insertion_point(module_scope)
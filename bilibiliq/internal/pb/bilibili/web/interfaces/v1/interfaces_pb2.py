# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/web/interfaces/v1/interfaces.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n+bilibili/web/interfaces/v1/interfaces.proto\x12\x1a\x62ilibili.web.interfaces.v1\"M\n\x07\x41\x63\x63Info\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x04 \x01(\t\x12\x0c\n\x04sign\x18\x05 \x01(\t\"\x8c\x04\n\x0b\x41\x63\x63ountCard\x12\x0b\n\x03mid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x0c\n\x04rank\x18\x04 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x05 \x01(\t\x12\x10\n\x08spacesta\x18\x06 \x01(\x05\x12\x0c\n\x04sign\x18\x07 \x01(\t\x12=\n\nlevel_info\x18\x08 \x01(\x0b\x32).bilibili.web.interfaces.v1.CardLevelInfo\x12\x38\n\x07pendant\x18\t \x01(\x0b\x32\'.bilibili.web.interfaces.v1.PendantInfo\x12<\n\tnameplate\x18\n \x01(\x0b\x32).bilibili.web.interfaces.v1.NameplateInfo\x12:\n\x08official\x18\x0b \x01(\x0b\x32(.bilibili.web.interfaces.v1.OfficialInfo\x12\x43\n\x0fofficial_verify\x18\x0c \x01(\x0b\x32*.bilibili.web.interfaces.v1.OfficialVerify\x12\x30\n\x03vip\x18\r \x01(\x0b\x32#.bilibili.web.interfaces.v1.CardVip\x12\x0c\n\x04\x66\x61ns\x18\x0e \x01(\x03\x12\x0e\n\x06\x66riend\x18\x0f \x01(\x03\x12\x11\n\tattention\x18\x10 \x01(\x03\"\xf3\x02\n\x14\x41\x63tivityArchiveReply\x12,\n\x03\x61rc\x18\x01 \x01(\x0b\x32\x1f.bilibili.web.interfaces.v1.Arc\x12\x0c\n\x04\x62vid\x18\x02 \x01(\t\x12/\n\x05pages\x18\x03 \x03(\x0b\x32 .bilibili.web.interfaces.v1.Page\x12\x35\n\x08req_user\x18\x04 \x01(\x0b\x32#.bilibili.web.interfaces.v1.ReqUser\x12\x30\n\x05staff\x18\x05 \x03(\x0b\x32!.bilibili.web.interfaces.v1.Staff\x12\x41\n\x0cright_relate\x18\x06 \x01(\x0b\x32+.bilibili.web.interfaces.v1.OperationRelate\x12\x42\n\rbottom_relate\x18\x07 \x01(\x0b\x32+.bilibili.web.interfaces.v1.OperationRelate\"E\n\x12\x41\x63tivityArchiveReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0c\n\x04\x62vid\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63tivity_key\x18\x03 \x01(\t\"\xcb\x01\n\x0f\x41\x63tivityEpisode\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0b\n\x03\x61id\x18\x02 \x01(\x03\x12\x0c\n\x04\x62vid\x18\x03 \x01(\t\x12\x0b\n\x03\x63id\x18\x04 \x01(\x03\x12\r\n\x05title\x18\x05 \x01(\t\x12\r\n\x05\x63over\x18\x06 \x01(\t\x12\x32\n\x06\x61uthor\x18\x07 \x01(\x0b\x32\".bilibili.web.interfaces.v1.Author\x12\x32\n\x06rights\x18\x08 \x01(\x0b\x32\".bilibili.web.interfaces.v1.Rights\"{\n\x0c\x41\x63tivityGame\x12?\n\x07iframes\x18\x01 \x03(\x0b\x32..bilibili.web.interfaces.v1.ActivityGameIframe\x12\x12\n\ndisclaimer\x18\x02 \x01(\t\x12\x16\n\x0e\x64isclaimer_url\x18\x03 \x01(\t\"1\n\x12\x41\x63tivityGameIframe\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0e\n\x06height\x18\x02 \x01(\x03\"\xf2\x02\n\x0c\x41\x63tivityLive\x12\x0f\n\x07room_id\x18\x01 \x01(\x03\x12\x10\n\x08now_time\x18\x02 \x01(\x03\x12\x12\n\nstart_time\x18\x03 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x03\x12\x11\n\thover_pic\x18\x05 \x01(\t\x12\x16\n\x0ehover_jump_url\x18\x06 \x01(\t\x12\x13\n\x0b\x62reak_cycle\x18\x07 \x01(\x03\x12:\n\x08timeline\x18\x08 \x03(\x0b\x32(.bilibili.web.interfaces.v1.LiveTimeline\x12\x45\n\x10operation_relate\x18\t \x01(\x0b\x32+.bilibili.web.interfaces.v1.OperationRelate\x12\x12\n\nreply_type\x18\n \x01(\x03\x12\x10\n\x08reply_id\x18\x0b \x01(\x03\x12\x17\n\x0fhover_pic_close\x18\x0c \x01(\t\x12\x17\n\x0fgift_disclaimer\x18\r \x01(\t\"\x8f\x01\n\x19\x41\x63tivityLiveTimeInfoReply\x12\x10\n\x08now_time\x18\x01 \x01(\x03\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\x03\x12:\n\x08timeline\x18\x04 \x03(\x0b\x32(.bilibili.web.interfaces.v1.LiveTimeline\"/\n\x17\x41\x63tivityLiveTimeInfoReq\x12\x14\n\x0c\x61\x63tivity_key\x18\x01 \x01(\t\"\x8a\x03\n\x13\x41\x63tivitySeasonReply\x12@\n\x06status\x18\x01 \x01(\x0e\x32\x30.bilibili.web.interfaces.v1.ActivitySeasonStatus\x12\r\n\x05title\x18\x02 \x01(\t\x12\x36\n\x04live\x18\x03 \x01(\x0b\x32(.bilibili.web.interfaces.v1.ActivityLive\x12@\n\tsubscribe\x18\x04 \x01(\x0b\x32-.bilibili.web.interfaces.v1.ActivitySubscribe\x12\x36\n\x04game\x18\x05 \x01(\x0b\x32(.bilibili.web.interfaces.v1.ActivityGame\x12\x36\n\x04view\x18\x06 \x01(\x0b\x32(.bilibili.web.interfaces.v1.ActivityView\x12\x38\n\x05theme\x18\x07 \x01(\x0b\x32).bilibili.web.interfaces.v1.ActivityTheme\"D\n\x11\x41\x63tivitySeasonReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0c\n\x04\x62vid\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63tivity_key\x18\x03 \x01(\t\"\x7f\n\x15\x41\x63tivitySeasonSection\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\x03\x12=\n\x08\x65pisodes\x18\x04 \x03(\x0b\x32+.bilibili.web.interfaces.v1.ActivityEpisode\"\xc2\x03\n\x11\x41\x63tivitySubscribe\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\r\n\x05title\x18\x02 \x01(\t\x12\x14\n\x0c\x62utton_title\x18\x03 \x01(\t\x12\x1d\n\x15\x62utton_selected_title\x18\x04 \x01(\t\x12\x18\n\x10season_stat_view\x18\x05 \x01(\x03\x12\x1b\n\x13season_stat_danmaku\x18\x06 \x01(\x03\x12\x39\n\norder_type\x18\x07 \x01(\x0e\x32%.bilibili.web.interfaces.v1.OrderType\x12R\n\x16reserve_activity_param\x18\x08 \x01(\x0b\x32\x30.bilibili.web.interfaces.v1.ReserveActivityParamH\x00\x12\x46\n\x10\x66\x61v_season_param\x18\t \x01(\x0b\x32*.bilibili.web.interfaces.v1.FavSeasonParamH\x00\x12\x42\n\x0ejump_URL_param\x18\n \x01(\x0b\x32(.bilibili.web.interfaces.v1.JumpURLParamH\x00\x42\x07\n\x05param\"\x9f\x06\n\rActivityTheme\x12\x12\n\nbase_color\x18\x01 \x01(\t\x12\x18\n\x10loading_bg_color\x18\x02 \x01(\t\x12\x19\n\x11operated_bg_color\x18\x03 \x01(\t\x12\x1d\n\x15\x64\x65\x66\x61ult_element_color\x18\x04 \x01(\t\x12\x1b\n\x13hover_element_color\x18\x05 \x01(\t\x12\x1e\n\x16selected_element_color\x18\x06 \x01(\t\x12\x17\n\x0f\x62\x61se_font_color\x18\x07 \x01(\t\x12\x17\n\x0finfo_font_color\x18\x08 \x01(\t\x12\x15\n\rmask_bg_color\x18\t \x01(\t\x12\x15\n\rpage_bg_color\x18\n \x01(\t\x12\x17\n\x0f\x63\x65nter_logo_img\x18\x0b \x01(\t\x12\x13\n\x0bpage_bg_img\x18\x0c \x01(\t\x12\x1b\n\x13\x64\x65\x63orations2233_img\x18\r \x01(\t\x12\x1a\n\x12main_banner_bg_img\x18\x0e \x01(\t\x12\x1d\n\x15main_banner_title_img\x18\x0f \x01(\t\x12\x1a\n\x12like_animation_img\x18\x10 \x01(\t\x12\x16\n\x0e\x63ombo_like_img\x18\x11 \x01(\t\x12\x16\n\x0e\x63ombo_coin_img\x18\x12 \x01(\t\x12\x15\n\rcombo_fav_img\x18\x13 \x01(\t\x12\x15\n\rarrow_btn_img\x18\x14 \x01(\t\x12\x19\n\x11share_icon_bg_img\x18\x15 \x01(\t\x12\x1e\n\x16live_list_location_img\x18\x16 \x01(\t\x12%\n\x1dlive_list_location_img_active\x18\x17 \x01(\t\x12\x1a\n\x12player_loading_img\x18\x18 \x01(\t\x12\x11\n\tshare_img\x18\x19 \x01(\t\x12H\n\x08kv_color\x18\x1a \x03(\x0b\x32\x36.bilibili.web.interfaces.v1.ActivityTheme.KvColorEntry\x1a.\n\x0cKvColorEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb0\x03\n\x0c\x41\x63tivityView\x12,\n\x03\x61rc\x18\x01 \x01(\x0b\x32\x1f.bilibili.web.interfaces.v1.Arc\x12\x0c\n\x04\x62vid\x18\x02 \x01(\t\x12/\n\x05pages\x18\x03 \x03(\x0b\x32 .bilibili.web.interfaces.v1.Page\x12\x30\n\x05staff\x18\x04 \x03(\x0b\x32!.bilibili.web.interfaces.v1.Staff\x12\x35\n\x08req_user\x18\x05 \x01(\x0b\x32#.bilibili.web.interfaces.v1.ReqUser\x12\x41\n\x0cright_relate\x18\x06 \x01(\x0b\x32+.bilibili.web.interfaces.v1.OperationRelate\x12\x42\n\rbottom_relate\x18\x07 \x01(\x0b\x32+.bilibili.web.interfaces.v1.OperationRelate\x12\x43\n\x08sections\x18\x08 \x03(\x0b\x32\x31.bilibili.web.interfaces.v1.ActivitySeasonSection\"\x91\x06\n\x03\x41rc\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0e\n\x06videos\x18\x02 \x01(\x03\x12\x0f\n\x07type_id\x18\x03 \x01(\x05\x12\x11\n\ttype_name\x18\x04 \x01(\t\x12\x11\n\tcopyright\x18\x05 \x01(\x05\x12\x0b\n\x03pic\x18\x06 \x01(\t\x12\r\n\x05title\x18\x07 \x01(\t\x12\x0f\n\x07pubdate\x18\x08 \x01(\x03\x12\r\n\x05\x63time\x18\t \x01(\x03\x12\x0c\n\x04\x64\x65sc\x18\n \x01(\t\x12\r\n\x05state\x18\x0b \x01(\x05\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x0c \x01(\x05\x12\x11\n\tattribute\x18\r \x01(\x05\x12\x0b\n\x03tag\x18\x0e \x01(\t\x12\x0c\n\x04tags\x18\x0f \x03(\t\x12\x10\n\x08\x64uration\x18\x10 \x01(\x03\x12\x12\n\nmission_id\x18\x11 \x01(\x03\x12\x10\n\x08order_id\x18\x12 \x01(\x03\x12\x14\n\x0credirect_url\x18\x13 \x01(\t\x12\x0f\n\x07\x66orward\x18\x14 \x01(\x03\x12\x32\n\x06rights\x18\x15 \x01(\x0b\x32\".bilibili.web.interfaces.v1.Rights\x12\x32\n\x06\x61uthor\x18\x16 \x01(\x0b\x32\".bilibili.web.interfaces.v1.Author\x12.\n\x04stat\x18\x17 \x01(\x0b\x32 .bilibili.web.interfaces.v1.Stat\x12\x15\n\rreport_result\x18\x18 \x01(\t\x12\x0f\n\x07\x64ynamic\x18\x19 \x01(\t\x12\x11\n\tfirst_cid\x18\x1a \x01(\x03\x12\x38\n\tdimension\x18\x1b \x01(\x0b\x32%.bilibili.web.interfaces.v1.Dimension\x12\x39\n\nstaff_info\x18\x1c \x03(\x0b\x32%.bilibili.web.interfaces.v1.StaffInfo\x12\x11\n\tseason_id\x18\x1d \x01(\x03\x12\x33\n\x07\x64\x65sc_v2\x18\x1e \x03(\x0b\x32\".bilibili.web.interfaces.v1.DescV2\x12\x1c\n\x14is_chargeable_season\x18\x1f \x01(\x08\x12\x12\n\nis_blooper\x18  \x01(\x08\"1\n\x06\x41uthor\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x03 \x01(\t\"\xc2\x01\n\x04\x43\x61rd\x12\x35\n\x04\x63\x61rd\x18\x01 \x01(\x0b\x32\'.bilibili.web.interfaces.v1.AccountCard\x12\x30\n\x05space\x18\x02 \x01(\x0b\x32!.bilibili.web.interfaces.v1.Space\x12\x11\n\tfollowing\x18\x03 \x01(\x08\x12\x15\n\rarchive_count\x18\x04 \x01(\x03\x12\x15\n\rarticle_count\x18\x05 \x01(\x05\x12\x10\n\x08\x66ollower\x18\x06 \x01(\x03\"L\n\rCardLevelInfo\x12\x0b\n\x03\x63ur\x18\x01 \x01(\x05\x12\x0b\n\x03min\x18\x02 \x01(\x05\x12\x0f\n\x07now_exp\x18\x03 \x01(\x05\x12\x10\n\x08next_exp\x18\x04 \x01(\x05\"\x83\x01\n\x07\x43\x61rdVip\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x12\n\ndue_remark\x18\x02 \x01(\t\x12\x15\n\raccess_status\x18\x03 \x01(\x05\x12\x12\n\nvip_status\x18\x04 \x01(\x05\x12\x17\n\x0fvip_status_warn\x18\x05 \x01(\t\x12\x12\n\ntheme_type\x18\x06 \x01(\x05\"\xdb\x02\n\x16\x43lickActivitySeasonReq\x12\x39\n\norder_type\x18\x01 \x01(\x0e\x32%.bilibili.web.interfaces.v1.OrderType\x12R\n\x16reserve_activity_param\x18\x02 \x01(\x0b\x32\x30.bilibili.web.interfaces.v1.ReserveActivityParamH\x00\x12\x46\n\x10\x66\x61v_season_param\x18\x03 \x01(\x0b\x32*.bilibili.web.interfaces.v1.FavSeasonParamH\x00\x12\x42\n\x0ejump_URL_param\x18\x04 \x01(\x0b\x32(.bilibili.web.interfaces.v1.JumpURLParamH\x00\x12\r\n\x05spmid\x18\x05 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x06 \x01(\x03\x42\x07\n\x05param\"8\n\x06\x44\x65scV2\x12\x10\n\x08raw_text\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x03\x12\x0e\n\x06\x62iz_id\x18\x03 \x01(\x03\":\n\tDimension\x12\r\n\x05width\x18\x01 \x01(\x03\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12\x0e\n\x06rotate\x18\x03 \x01(\x03\"#\n\x0e\x46\x61vSeasonParam\x12\x11\n\tseason_id\x18\x01 \x01(\x03\"s\n\x08HotReply\x12\x33\n\x04page\x18\x01 \x01(\x0b\x32%.bilibili.web.interfaces.v1.ReplyPage\x12\x32\n\x07replies\x18\x02 \x03(\x0b\x32!.bilibili.web.interfaces.v1.Reply\" \n\x0cJumpURLParam\x12\x10\n\x08jump_url\x18\x01 \x01(\t\"u\n\x0cLiveTimeline\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\x03\x12\r\n\x05\x63over\x18\x04 \x01(\t\x12\x10\n\x08subtitle\x18\x05 \x01(\t\x12\x10\n\x08h5_cover\x18\x06 \x01(\t\"p\n\rNameplateInfo\x12\x0b\n\x03nid\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05image\x18\x03 \x01(\t\x12\x13\n\x0bimage_small\x18\x04 \x01(\t\x12\r\n\x05level\x18\x05 \x01(\t\x12\x11\n\tcondition\x18\x06 \x01(\t\"\t\n\x07NoReply\"9\n\x0cOfficialInfo\x12\x0c\n\x04role\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\",\n\x0eOfficialVerify\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\"\x99\x01\n\x0fOperationRelate\x12\r\n\x05title\x18\x01 \x01(\t\x12;\n\x0brelate_item\x18\x02 \x03(\x0b\x32&.bilibili.web.interfaces.v1.RelateItem\x12:\n\x0e\x61i_relate_item\x18\x03 \x03(\x0b\x32\".bilibili.web.interfaces.v1.Relate\"\xb5\x01\n\x04Page\x12\x0b\n\x03\x63id\x18\x01 \x01(\x03\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x0c\n\x04\x66rom\x18\x03 \x01(\t\x12\x0c\n\x04part\x18\x04 \x01(\t\x12\x10\n\x08\x64uration\x18\x05 \x01(\x03\x12\x0b\n\x03vid\x18\x06 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x07 \x01(\t\x12\x0f\n\x07weblink\x18\x08 \x01(\t\x12\x38\n\tdimension\x18\t \x01(\x0b\x32%.bilibili.web.interfaces.v1.Dimension\"G\n\x0bPendantInfo\x12\x0b\n\x03pid\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05image\x18\x03 \x01(\t\x12\x0e\n\x06\x65xpire\x18\x04 \x01(\x03\"\x1b\n\x0bReasonStyle\x12\x0c\n\x04text\x18\x01 \x01(\t\"Y\n\x06Relate\x12,\n\x03\x61rc\x18\x01 \x01(\x0b\x32\x1f.bilibili.web.interfaces.v1.Arc\x12\x0c\n\x04\x62vid\x18\x02 \x01(\t\x12\x13\n\x0bseason_type\x18\x03 \x01(\x03\"(\n\nRelateItem\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05\x63over\x18\x02 \x01(\t\".\n\x08Relation\x12\x11\n\tattribute\x18\x01 \x01(\x03\x12\x0f\n\x07special\x18\x03 \x01(\x03\"\xdf\x05\n\x05Reply\x12\x0c\n\x04rpid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x0b\n\x03mid\x18\x04 \x01(\x03\x12\x0c\n\x04root\x18\x05 \x01(\x03\x12\x0e\n\x06parent\x18\x06 \x01(\x03\x12\x0e\n\x06\x64ialog\x18\x07 \x01(\x03\x12\r\n\x05\x63ount\x18\x08 \x01(\x05\x12\x0e\n\x06rcount\x18\t \x01(\x05\x12\r\n\x05\x66loor\x18\n \x01(\x05\x12\r\n\x05state\x18\x0b \x01(\x05\x12\x12\n\nfans_grade\x18\x0c \x01(\x05\x12\x0c\n\x04\x61ttr\x18\r \x01(\x05\x12\r\n\x05\x63time\x18\x0e \x01(\x03\x12\x10\n\x08rpid_str\x18\x0f \x01(\t\x12\x10\n\x08root_str\x18\x10 \x01(\t\x12\x12\n\nparent_str\x18\x11 \x01(\t\x12\x12\n\ndialog_str\x18\x12 \x01(\t\x12\x0c\n\x04like\x18\x13 \x01(\x05\x12\x0c\n\x04hate\x18\x14 \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\x15 \x01(\x05\x12\x37\n\x06member\x18\x16 \x01(\x0b\x32\'.bilibili.web.interfaces.v1.ReplyMember\x12\x39\n\x07\x63ontent\x18\x17 \x01(\x0b\x32(.bilibili.web.interfaces.v1.ReplyContent\x12\x32\n\x07replies\x18\x18 \x03(\x0b\x32!.bilibili.web.interfaces.v1.Reply\x12\x0e\n\x06\x61ssist\x18\x19 \x01(\x05\x12\x37\n\x06\x66older\x18\x1a \x01(\x0b\x32\'.bilibili.web.interfaces.v1.ReplyFolder\x12<\n\tup_action\x18\x1b \x01(\x0b\x32).bilibili.web.interfaces.v1.ReplyUpAction\x12\x35\n\x05label\x18\x1c \x01(\x0b\x32&.bilibili.web.interfaces.v1.ReplyLabel\x12\x11\n\traw_input\x18\x1d \x01(\t\x12\x13\n\x0bshow_follow\x18\x1e \x01(\x08\"\x86\x03\n\x0cReplyContent\x12\r\n\x05rp_id\x18\x01 \x01(\x03\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x33\n\x04vote\x18\x03 \x01(\x0b\x32%.bilibili.web.interfaces.v1.ReplyVote\x12\x0e\n\x06topics\x18\x05 \x03(\t\x12\n\n\x02ip\x18\x06 \x01(\x05\x12\x0c\n\x04plat\x18\x07 \x01(\x05\x12\x0e\n\x06\x64\x65vice\x18\x08 \x01(\t\x12\x0f\n\x07version\x18\t \x01(\t\x12<\n\x07members\x18\n \x03(\x0b\x32+.bilibili.web.interfaces.v1.ReplyMemberInfo\x12\x42\n\x05\x65mote\x18\x0b \x03(\x0b\x32\x33.bilibili.web.interfaces.v1.ReplyContent.EmoteEntry\x1aT\n\nEmoteEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.bilibili.web.interfaces.v1.ReplyEmote:\x02\x38\x01\"\xca\x01\n\nReplyEmote\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x12\n\npackage_id\x18\x02 \x01(\x03\x12\r\n\x05state\x18\x03 \x01(\x03\x12\x0c\n\x04type\x18\x04 \x01(\x03\x12\x0c\n\x04\x61ttr\x18\x05 \x01(\x03\x12\x0c\n\x04text\x18\x06 \x01(\t\x12\x0b\n\x03url\x18\x07 \x01(\t\x12\x38\n\x04meta\x18\x08 \x01(\x0b\x32*.bilibili.web.interfaces.v1.ReplyEmoteMeta\x12\r\n\x05\x63time\x18\t \x01(\x03\x12\r\n\x05mtime\x18\n \x01(\x03\"N\n\x0eReplyEmoteMeta\x12<\n\x04size\x18\x01 \x01(\x0e\x32..bilibili.web.interfaces.v1.ReplyEmoteMetaSize\"\x96\x01\n\x0fReplyFansDetail\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x10\n\x08medal_id\x18\x02 \x01(\x05\x12\x12\n\nmedal_name\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x05\x12\r\n\x05level\x18\x05 \x01(\x05\x12\x10\n\x08intimacy\x18\x06 \x01(\x05\x12\x0e\n\x06status\x18\x07 \x01(\x05\x12\x10\n\x08received\x18\x08 \x01(\x05\"B\n\x0bReplyFolder\x12\x12\n\nhas_folded\x18\x01 \x01(\x08\x12\x11\n\tis_folded\x18\x02 \x01(\x08\x12\x0c\n\x04rule\x18\x03 \x01(\t\"\xad\x01\n\nReplyLabel\x12\x0c\n\x04rpid\x18\x01 \x01(\x03\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x12\n\ntext_color\x18\x03 \x01(\t\x12\x1d\n\x15text_color_night_mode\x18\x04 \x01(\t\x12\x10\n\x08\x62g_color\x18\x05 \x01(\t\x12\x1b\n\x13\x62g_color_night_mode\x18\x06 \x01(\t\x12\x0c\n\x04link\x18\x07 \x01(\t\x12\x10\n\x08position\x18\x08 \x01(\t\"M\n\x0eReplyLevelInfo\x12\x0b\n\x03\x63ur\x18\x01 \x01(\x05\x12\x0b\n\x03min\x18\x02 \x01(\x05\x12\x0f\n\x07now_exp\x18\x03 \x01(\x05\x12\x10\n\x08next_exp\x18\x04 \x01(\x05\"\x9d\x01\n\x0bReplyMember\x12\x39\n\x04info\x18\x01 \x01(\x0b\x32+.bilibili.web.interfaces.v1.ReplyMemberInfo\x12@\n\x0b\x66\x61ns_detail\x18\x02 \x01(\x0b\x32+.bilibili.web.interfaces.v1.ReplyFansDetail\x12\x11\n\tfollowing\x18\x03 \x01(\x05\"\xb9\x03\n\x0fReplyMemberInfo\x12\x0c\n\x04role\x18\x01 \x01(\x05\x12\x0b\n\x03mid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0b\n\x03sex\x18\x04 \x01(\t\x12\x0c\n\x04sign\x18\x05 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x06 \x01(\t\x12\x0c\n\x04rank\x18\x07 \x01(\t\x12\x14\n\x0c\x64isplay_rank\x18\x08 \x01(\t\x12>\n\nlevel_info\x18\t \x01(\x0b\x32*.bilibili.web.interfaces.v1.ReplyLevelInfo\x12\x38\n\x07pendant\x18\n \x01(\x0b\x32\'.bilibili.web.interfaces.v1.PendantInfo\x12<\n\tnameplate\x18\x0b \x01(\x0b\x32).bilibili.web.interfaces.v1.NameplateInfo\x12\x43\n\x0fofficial_verify\x18\x0c \x01(\x0b\x32*.bilibili.web.interfaces.v1.OfficialVerify\x12\x31\n\x03vip\x18\r \x01(\x0b\x32$.bilibili.web.interfaces.v1.ReplyVip\"E\n\tReplyPage\x12\x0e\n\x06\x61\x63ount\x18\x01 \x01(\x03\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\x12\x0b\n\x03num\x18\x03 \x01(\x03\x12\x0c\n\x04size\x18\x04 \x01(\x03\",\n\rReplyUpAction\x12\x0c\n\x04like\x18\x01 \x01(\x08\x12\r\n\x05reply\x18\x02 \x01(\x08\"\xcb\x01\n\x08ReplyVip\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x10\n\x08\x64ue_date\x18\x02 \x01(\x03\x12\x12\n\ndue_remark\x18\x03 \x01(\t\x12\x15\n\raccess_status\x18\x04 \x01(\x05\x12\x12\n\nvip_status\x18\x05 \x01(\x05\x12\x17\n\x0fvip_status_warn\x18\x06 \x01(\t\x12\x12\n\ntheme_type\x18\x07 \x01(\x05\x12\x33\n\x05label\x18\x08 \x01(\x0b\x32$.bilibili.web.interfaces.v1.VipLabel\"R\n\tReplyVote\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0b\n\x03\x63nt\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x04 \x01(\t\x12\x0f\n\x07\x64\x65leted\x18\x05 \x01(\x08\"L\n\x07ReqUser\x12\x10\n\x08\x66\x61vorite\x18\x01 \x01(\x08\x12\x0c\n\x04like\x18\x02 \x01(\x08\x12\x0f\n\x07\x64islike\x18\x03 \x01(\x08\x12\x10\n\x08multiply\x18\x04 \x01(\x03\"S\n\x14ReserveActivityParam\x12\x12\n\nreserve_id\x18\x01 \x01(\x03\x12\x0c\n\x04\x66rom\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0b\n\x03oid\x18\x04 \x01(\x03\"\xea\x01\n\x06Rights\x12\n\n\x02\x62p\x18\x01 \x01(\x05\x12\x0c\n\x04\x65lec\x18\x02 \x01(\x05\x12\x10\n\x08\x64ownload\x18\x03 \x01(\x05\x12\r\n\x05movie\x18\x04 \x01(\x05\x12\x0b\n\x03pay\x18\x05 \x01(\x05\x12\x0b\n\x03hd5\x18\x06 \x01(\x05\x12\x12\n\nno_reprint\x18\x07 \x01(\x05\x12\x10\n\x08\x61utoplay\x18\x08 \x01(\x05\x12\x0f\n\x07ugc_pay\x18\t \x01(\x05\x12\x16\n\x0eis_cooperation\x18\n \x01(\x05\x12\x17\n\x0fugc_pay_preview\x18\x0b \x01(\x05\x12\x0f\n\x07\x61rc_pay\x18\x0c \x01(\x05\x12\x12\n\nfree_watch\x18\r \x01(\x05\"\xa8\x02\n\rSeasonEpisode\x12\x11\n\tseason_id\x18\x01 \x01(\x03\x12\x12\n\nsection_id\x18\x02 \x01(\x03\x12\n\n\x02id\x18\x03 \x01(\x03\x12\x0b\n\x03\x61id\x18\x04 \x01(\x03\x12\x0b\n\x03\x63id\x18\x05 \x01(\x03\x12\r\n\x05title\x18\x06 \x01(\t\x12\x11\n\tattribute\x18\x07 \x01(\x03\x12,\n\x03\x61rc\x18\x08 \x01(\x0b\x32\x1f.bilibili.web.interfaces.v1.Arc\x12.\n\x04page\x18\t \x01(\x0b\x32 .bilibili.web.interfaces.v1.Page\x12\x0c\n\x04\x62vid\x18\n \x01(\t\x12<\n\x0b\x62\x61\x64ge_style\x18\x0b \x01(\x0b\x32\'.bilibili.web.interfaces.v1.ReasonStyle\"\x88\x01\n\rSeasonSection\x12\x11\n\tseason_id\x18\x01 \x01(\x03\x12\n\n\x02id\x18\x02 \x01(\x03\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\x03\x12;\n\x08\x65pisodes\x18\x05 \x03(\x0b\x32).bilibili.web.interfaces.v1.SeasonEpisode\"\xa9\x01\n\nSeasonStat\x12\x11\n\tseason_id\x18\x01 \x01(\x03\x12\x0c\n\x04view\x18\x02 \x01(\x05\x12\x0f\n\x07\x64\x61nmaku\x18\x03 \x01(\x05\x12\r\n\x05reply\x18\x04 \x01(\x05\x12\x0b\n\x03\x66\x61v\x18\x05 \x01(\x05\x12\x0c\n\x04\x63oin\x18\x06 \x01(\x05\x12\r\n\x05share\x18\x07 \x01(\x05\x12\x10\n\x08now_rank\x18\x08 \x01(\x05\x12\x10\n\x08his_rank\x18\t \x01(\x05\x12\x0c\n\x04like\x18\n \x01(\x05\"%\n\x05Space\x12\r\n\x05s_img\x18\x01 \x01(\t\x12\r\n\x05l_img\x18\x02 \x01(\t\"\x8c\x02\n\x05Staff\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x04 \x01(\t\x12\x30\n\x03vip\x18\x05 \x01(\x0b\x32#.bilibili.web.interfaces.v1.VipInfo\x12:\n\x08official\x18\x06 \x01(\x0b\x32(.bilibili.web.interfaces.v1.OfficialInfo\x12\x10\n\x08\x66ollower\x18\x07 \x01(\x03\x12\x13\n\x0blabel_style\x18\x08 \x01(\x05\x12\x36\n\x08relation\x18\t \x01(\x0b\x32$.bilibili.web.interfaces.v1.Relation\"\'\n\tStaffInfo\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\"\xd5\x01\n\x04Stat\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0c\n\x04view\x18\x02 \x01(\x05\x12\x0f\n\x07\x64\x61nmaku\x18\x03 \x01(\x05\x12\r\n\x05reply\x18\x04 \x01(\x05\x12\x0b\n\x03\x66\x61v\x18\x05 \x01(\x05\x12\x0c\n\x04\x63oin\x18\x06 \x01(\x05\x12\r\n\x05share\x18\x07 \x01(\x05\x12\x10\n\x08now_rank\x18\x08 \x01(\x05\x12\x10\n\x08his_rank\x18\t \x01(\x05\x12\x0c\n\x04like\x18\n \x01(\x05\x12\x0f\n\x07\x64islike\x18\x0b \x01(\x05\x12\x12\n\nevaluation\x18\x0c \x01(\t\x12\x11\n\targue_msg\x18\r \x01(\t\"X\n\x08Subtitle\x12\x14\n\x0c\x61llow_submit\x18\x01 \x01(\x08\x12\x36\n\x04list\x18\x02 \x03(\x0b\x32(.bilibili.web.interfaces.v1.SubtitleItem\"\xa8\x01\n\x0cSubtitleItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0b\n\x03lan\x18\x02 \x01(\t\x12\x0f\n\x07lan_doc\x18\x03 \x01(\t\x12\x0f\n\x07is_lock\x18\x04 \x01(\x08\x12\x12\n\nauthor_mid\x18\x05 \x01(\x03\x12\x14\n\x0csubtitle_url\x18\x06 \x01(\t\x12\x33\n\x06\x61uthor\x18\x07 \x01(\x0b\x32#.bilibili.web.interfaces.v1.AccInfo\"\xb0\x02\n\x03Tag\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x63over\x18\x03 \x01(\t\x12\x12\n\nhead_cover\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\x15\n\rshort_content\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x07 \x01(\x05\x12\r\n\x05state\x18\x08 \x01(\x05\x12\r\n\x05\x63time\x18\t \x01(\x03\x12\x37\n\ttag_count\x18\n \x01(\x0b\x32$.bilibili.web.interfaces.v1.TagCount\x12\x10\n\x08is_atten\x18\x0b \x01(\x05\x12\r\n\x05likes\x18\x0c \x01(\x03\x12\r\n\x05hates\x18\r \x01(\x03\x12\x11\n\tattribute\x18\x0e \x01(\x05\x12\r\n\x05liked\x18\x0f \x01(\x05\x12\r\n\x05hated\x18\x10 \x01(\x05\"4\n\x08TagCount\x12\x0c\n\x04view\x18\x01 \x01(\x03\x12\x0b\n\x03use\x18\x02 \x01(\x03\x12\r\n\x05\x61tten\x18\x03 \x01(\x03\"\xa6\x01\n\x0bUGCPayAsset\x12\r\n\x05price\x18\x01 \x01(\x03\x12R\n\x0eplatform_price\x18\x02 \x03(\x0b\x32:.bilibili.web.interfaces.v1.UGCPayAsset.PlatformPriceEntry\x1a\x34\n\x12PlatformPriceEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\xa9\x02\n\tUGCSeason\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05\x63over\x18\x03 \x01(\t\x12\x0b\n\x03mid\x18\x04 \x01(\x03\x12\r\n\x05intro\x18\x05 \x01(\t\x12\x12\n\nsign_state\x18\x06 \x01(\x05\x12\x11\n\tattribute\x18\x07 \x01(\x03\x12;\n\x08sections\x18\x08 \x03(\x0b\x32).bilibili.web.interfaces.v1.SeasonSection\x12\x34\n\x04stat\x18\t \x01(\x0b\x32&.bilibili.web.interfaces.v1.SeasonStat\x12\x10\n\x08\x65p_count\x18\n \x01(\x03\x12\x13\n\x0bseason_type\x18\x0b \x01(\x03\x12\x15\n\ris_pay_season\x18\x0c \x01(\x08\"\xa3\x03\n\x04View\x12,\n\x03\x61rc\x18\x01 \x01(\x0b\x32\x1f.bilibili.web.interfaces.v1.Arc\x12\x10\n\x08no_cache\x18\x02 \x01(\x08\x12/\n\x05pages\x18\x03 \x03(\x0b\x32 .bilibili.web.interfaces.v1.Page\x12\x36\n\x08subtitle\x18\x04 \x01(\x0b\x32$.bilibili.web.interfaces.v1.Subtitle\x12\x36\n\x05\x61sset\x18\x05 \x01(\x0b\x32\'.bilibili.web.interfaces.v1.UGCPayAsset\x12\x34\n\x05label\x18\x06 \x01(\x0b\x32%.bilibili.web.interfaces.v1.ViewLabel\x12\x30\n\x05staff\x18\x07 \x03(\x0b\x32!.bilibili.web.interfaces.v1.Staff\x12\x39\n\nugc_season\x18\x08 \x01(\x0b\x32%.bilibili.web.interfaces.v1.UGCSeason\x12\x17\n\x0fstein_guide_cid\x18\t \x01(\x03\"\x87\x02\n\x0fViewDetailReply\x12.\n\x04view\x18\x01 \x01(\x0b\x32 .bilibili.web.interfaces.v1.View\x12.\n\x04\x63\x61rd\x18\x02 \x01(\x0b\x32 .bilibili.web.interfaces.v1.Card\x12-\n\x04tags\x18\x03 \x03(\x0b\x32\x1f.bilibili.web.interfaces.v1.Tag\x12\x33\n\x05reply\x18\x04 \x01(\x0b\x32$.bilibili.web.interfaces.v1.HotReply\x12\x30\n\x07related\x18\x05 \x03(\x0b\x32\x1f.bilibili.web.interfaces.v1.Arc\"*\n\rViewDetailReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0c\n\x04\x62vid\x18\x02 \x01(\t\"\x19\n\tViewLabel\x12\x0c\n\x04type\x18\x01 \x01(\x03\"Q\n\x07VipInfo\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x14\n\x0cvip_pay_type\x18\x03 \x01(\x05\x12\x12\n\ntheme_type\x18\x04 \x01(\x05\"\x18\n\x08VipLabel\x12\x0c\n\x04path\x18\x01 \x01(\t*F\n\x14\x41\x63tivitySeasonStatus\x12\x0e\n\nStatusNone\x10\x00\x12\x0e\n\nStatusLive\x10\x01\x12\x0e\n\nStatusView\x10\x02*R\n\tOrderType\x12\x0c\n\x08TypeNone\x10\x00\x12\x15\n\x11TypeOrderActivity\x10\x01\x12\x11\n\rTypeFavSeason\x10\x02\x12\r\n\tTypeClick\x10\x03*i\n\x12ReplyEmoteMetaSize\x12\x1f\n\x1b\x45MOTE_META_SIZE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x45MOTE_META_SIZE_SMALL\x10\x01\x12\x17\n\x13\x45MOTE_META_SIZE_BIG\x10\x02\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'bilibili.web.interfaces.v1.interfaces_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _ACTIVITYTHEME_KVCOLORENTRY._options = None
    _ACTIVITYTHEME_KVCOLORENTRY._serialized_options = b'8\001'
    _REPLYCONTENT_EMOTEENTRY._options = None
    _REPLYCONTENT_EMOTEENTRY._serialized_options = b'8\001'
    _UGCPAYASSET_PLATFORMPRICEENTRY._options = None
    _UGCPAYASSET_PLATFORMPRICEENTRY._serialized_options = b'8\001'
    _ACTIVITYSEASONSTATUS._serialized_start = 13677
    _ACTIVITYSEASONSTATUS._serialized_end = 13747
    _ORDERTYPE._serialized_start = 13749
    _ORDERTYPE._serialized_end = 13831
    _REPLYEMOTEMETASIZE._serialized_start = 13833
    _REPLYEMOTEMETASIZE._serialized_end = 13938
    _ACCINFO._serialized_start = 75
    _ACCINFO._serialized_end = 152
    _ACCOUNTCARD._serialized_start = 155
    _ACCOUNTCARD._serialized_end = 679
    _ACTIVITYARCHIVEREPLY._serialized_start = 682
    _ACTIVITYARCHIVEREPLY._serialized_end = 1053
    _ACTIVITYARCHIVEREQ._serialized_start = 1055
    _ACTIVITYARCHIVEREQ._serialized_end = 1124
    _ACTIVITYEPISODE._serialized_start = 1127
    _ACTIVITYEPISODE._serialized_end = 1330
    _ACTIVITYGAME._serialized_start = 1332
    _ACTIVITYGAME._serialized_end = 1455
    _ACTIVITYGAMEIFRAME._serialized_start = 1457
    _ACTIVITYGAMEIFRAME._serialized_end = 1506
    _ACTIVITYLIVE._serialized_start = 1509
    _ACTIVITYLIVE._serialized_end = 1879
    _ACTIVITYLIVETIMEINFOREPLY._serialized_start = 1882
    _ACTIVITYLIVETIMEINFOREPLY._serialized_end = 2025
    _ACTIVITYLIVETIMEINFOREQ._serialized_start = 2027
    _ACTIVITYLIVETIMEINFOREQ._serialized_end = 2074
    _ACTIVITYSEASONREPLY._serialized_start = 2077
    _ACTIVITYSEASONREPLY._serialized_end = 2471
    _ACTIVITYSEASONREQ._serialized_start = 2473
    _ACTIVITYSEASONREQ._serialized_end = 2541
    _ACTIVITYSEASONSECTION._serialized_start = 2543
    _ACTIVITYSEASONSECTION._serialized_end = 2670
    _ACTIVITYSUBSCRIBE._serialized_start = 2673
    _ACTIVITYSUBSCRIBE._serialized_end = 3123
    _ACTIVITYTHEME._serialized_start = 3126
    _ACTIVITYTHEME._serialized_end = 3925
    _ACTIVITYTHEME_KVCOLORENTRY._serialized_start = 3879
    _ACTIVITYTHEME_KVCOLORENTRY._serialized_end = 3925
    _ACTIVITYVIEW._serialized_start = 3928
    _ACTIVITYVIEW._serialized_end = 4360
    _ARC._serialized_start = 4363
    _ARC._serialized_end = 5148
    _AUTHOR._serialized_start = 5150
    _AUTHOR._serialized_end = 5199
    _CARD._serialized_start = 5202
    _CARD._serialized_end = 5396
    _CARDLEVELINFO._serialized_start = 5398
    _CARDLEVELINFO._serialized_end = 5474
    _CARDVIP._serialized_start = 5477
    _CARDVIP._serialized_end = 5608
    _CLICKACTIVITYSEASONREQ._serialized_start = 5611
    _CLICKACTIVITYSEASONREQ._serialized_end = 5958
    _DESCV2._serialized_start = 5960
    _DESCV2._serialized_end = 6016
    _DIMENSION._serialized_start = 6018
    _DIMENSION._serialized_end = 6076
    _FAVSEASONPARAM._serialized_start = 6078
    _FAVSEASONPARAM._serialized_end = 6113
    _HOTREPLY._serialized_start = 6115
    _HOTREPLY._serialized_end = 6230
    _JUMPURLPARAM._serialized_start = 6232
    _JUMPURLPARAM._serialized_end = 6264
    _LIVETIMELINE._serialized_start = 6266
    _LIVETIMELINE._serialized_end = 6383
    _NAMEPLATEINFO._serialized_start = 6385
    _NAMEPLATEINFO._serialized_end = 6497
    _NOREPLY._serialized_start = 6499
    _NOREPLY._serialized_end = 6508
    _OFFICIALINFO._serialized_start = 6510
    _OFFICIALINFO._serialized_end = 6567
    _OFFICIALVERIFY._serialized_start = 6569
    _OFFICIALVERIFY._serialized_end = 6613
    _OPERATIONRELATE._serialized_start = 6616
    _OPERATIONRELATE._serialized_end = 6769
    _PAGE._serialized_start = 6772
    _PAGE._serialized_end = 6953
    _PENDANTINFO._serialized_start = 6955
    _PENDANTINFO._serialized_end = 7026
    _REASONSTYLE._serialized_start = 7028
    _REASONSTYLE._serialized_end = 7055
    _RELATE._serialized_start = 7057
    _RELATE._serialized_end = 7146
    _RELATEITEM._serialized_start = 7148
    _RELATEITEM._serialized_end = 7188
    _RELATION._serialized_start = 7190
    _RELATION._serialized_end = 7236
    _REPLY._serialized_start = 7239
    _REPLY._serialized_end = 7974
    _REPLYCONTENT._serialized_start = 7977
    _REPLYCONTENT._serialized_end = 8367
    _REPLYCONTENT_EMOTEENTRY._serialized_start = 8283
    _REPLYCONTENT_EMOTEENTRY._serialized_end = 8367
    _REPLYEMOTE._serialized_start = 8370
    _REPLYEMOTE._serialized_end = 8572
    _REPLYEMOTEMETA._serialized_start = 8574
    _REPLYEMOTEMETA._serialized_end = 8652
    _REPLYFANSDETAIL._serialized_start = 8655
    _REPLYFANSDETAIL._serialized_end = 8805
    _REPLYFOLDER._serialized_start = 8807
    _REPLYFOLDER._serialized_end = 8873
    _REPLYLABEL._serialized_start = 8876
    _REPLYLABEL._serialized_end = 9049
    _REPLYLEVELINFO._serialized_start = 9051
    _REPLYLEVELINFO._serialized_end = 9128
    _REPLYMEMBER._serialized_start = 9131
    _REPLYMEMBER._serialized_end = 9288
    _REPLYMEMBERINFO._serialized_start = 9291
    _REPLYMEMBERINFO._serialized_end = 9732
    _REPLYPAGE._serialized_start = 9734
    _REPLYPAGE._serialized_end = 9803
    _REPLYUPACTION._serialized_start = 9805
    _REPLYUPACTION._serialized_end = 9849
    _REPLYVIP._serialized_start = 9852
    _REPLYVIP._serialized_end = 10055
    _REPLYVOTE._serialized_start = 10057
    _REPLYVOTE._serialized_end = 10139
    _REQUSER._serialized_start = 10141
    _REQUSER._serialized_end = 10217
    _RESERVEACTIVITYPARAM._serialized_start = 10219
    _RESERVEACTIVITYPARAM._serialized_end = 10302
    _RIGHTS._serialized_start = 10305
    _RIGHTS._serialized_end = 10539
    _SEASONEPISODE._serialized_start = 10542
    _SEASONEPISODE._serialized_end = 10838
    _SEASONSECTION._serialized_start = 10841
    _SEASONSECTION._serialized_end = 10977
    _SEASONSTAT._serialized_start = 10980
    _SEASONSTAT._serialized_end = 11149
    _SPACE._serialized_start = 11151
    _SPACE._serialized_end = 11188
    _STAFF._serialized_start = 11191
    _STAFF._serialized_end = 11459
    _STAFFINFO._serialized_start = 11461
    _STAFFINFO._serialized_end = 11500
    _STAT._serialized_start = 11503
    _STAT._serialized_end = 11716
    _SUBTITLE._serialized_start = 11718
    _SUBTITLE._serialized_end = 11806
    _SUBTITLEITEM._serialized_start = 11809
    _SUBTITLEITEM._serialized_end = 11977
    _TAG._serialized_start = 11980
    _TAG._serialized_end = 12284
    _TAGCOUNT._serialized_start = 12286
    _TAGCOUNT._serialized_end = 12338
    _UGCPAYASSET._serialized_start = 12341
    _UGCPAYASSET._serialized_end = 12507
    _UGCPAYASSET_PLATFORMPRICEENTRY._serialized_start = 12455
    _UGCPAYASSET_PLATFORMPRICEENTRY._serialized_end = 12507
    _UGCSEASON._serialized_start = 12510
    _UGCSEASON._serialized_end = 12807
    _VIEW._serialized_start = 12810
    _VIEW._serialized_end = 13229
    _VIEWDETAILREPLY._serialized_start = 13232
    _VIEWDETAILREPLY._serialized_end = 13495
    _VIEWDETAILREQ._serialized_start = 13497
    _VIEWDETAILREQ._serialized_end = 13539
    _VIEWLABEL._serialized_start = 13541
    _VIEWLABEL._serialized_end = 13566
    _VIPINFO._serialized_start = 13568
    _VIPINFO._serialized_end = 13649
    _VIPLABEL._serialized_start = 13651
    _VIPLABEL._serialized_end = 13675
# @@protoc_insertion_point(module_scope)
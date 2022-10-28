# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/pgc/gateway/player/v2/playurl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import (
    timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n,bilibili/pgc/gateway/player/v2/playurl.proto\x12\x1e\x62ilibili.pgc.gateway.player.v2\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa1\x01\n\tBadgeInfo\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08\x62g_color\x18\x02 \x01(\t\x12\x16\n\x0e\x62g_color_night\x18\x03 \x01(\t\x12\x12\n\ntext_color\x18\x04 \x01(\t\x12H\n\x11\x62g_gradient_color\x18\x05 \x01(\x0b\x32-.bilibili.pgc.gateway.player.v2.GradientColor\"V\n\rBottomDisplay\x12\x37\n\x05title\x18\x01 \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.TextInfo\x12\x0c\n\x04icon\x18\x02 \x01(\t\"\x8d\x05\n\nButtonInfo\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\ntext_color\x18\x02 \x01(\t\x12\x18\n\x10text_color_night\x18\x03 \x01(\t\x12\x10\n\x08\x62g_color\x18\x04 \x01(\t\x12\x16\n\x0e\x62g_color_night\x18\x05 \x01(\t\x12\x0c\n\x04link\x18\x06 \x01(\t\x12\x13\n\x0b\x61\x63tion_type\x18\x07 \x01(\t\x12=\n\nbadge_info\x18\x08 \x01(\x0b\x32).bilibili.pgc.gateway.player.v2.BadgeInfo\x12\x36\n\x06report\x18\t \x01(\x0b\x32&.bilibili.pgc.gateway.player.v2.Report\x12\x1f\n\x17left_strikethrough_text\x18\n \x01(\t\x12\x42\n\x10simple_text_info\x18\x0b \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.TextInfo\x12\x17\n\x0fsimple_bg_color\x18\x0c \x01(\t\x12\x1d\n\x15simple_bg_color_night\x18\r \x01(\t\x12H\n\x11\x62g_gradient_color\x18\x0e \x01(\x0b\x32-.bilibili.pgc.gateway.player.v2.GradientColor\x12^\n\x13order_report_params\x18\x0f \x03(\x0b\x32\x41.bilibili.pgc.gateway.player.v2.ButtonInfo.OrderReportParamsEntry\x1a\x38\n\x16OrderReportParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\")\n\x08\x43\x61stTips\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\xcb\x01\n\x08\x43lipInfo\x12\x13\n\x0bmaterial_no\x18\x01 \x01(\x03\x12\r\n\x05start\x18\x02 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x05\x12;\n\tclip_type\x18\x04 \x01(\x0e\x32(.bilibili.pgc.gateway.player.v2.ClipType\x12\x12\n\ntoast_text\x18\x05 \x01(\t\x12=\n\nmulti_view\x18\x06 \x01(\x0b\x32).bilibili.pgc.gateway.player.v2.MultiView\"/\n\x10\x43ontinuePlayInfo\x12\x1b\n\x13\x63ontinue_play_ep_id\x18\x01 \x01(\x03\"\xef\x01\n\x06\x43oupon\x12\x14\n\x0c\x63oupon_token\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x03\x12\r\n\x05value\x18\x03 \x01(\t\x12\x10\n\x08use_desc\x18\x04 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x06 \x01(\t\x12\x17\n\x0fpay_button_text\x18\x07 \x01(\t\x12$\n\x1cpay_button_text_line_through\x18\x08 \x01(\t\x12\x13\n\x0breal_amount\x18\t \x01(\t\x12/\n\x0b\x65xpire_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x81\x01\n\nCouponInfo\x12:\n\x05toast\x18\x01 \x01(\x0b\x32+.bilibili.pgc.gateway.player.v2.CouponToast\x12\x37\n\x07pop_win\x18\x02 \x01(\x0b\x32&.bilibili.pgc.gateway.player.v2.PopWin\";\n\x0e\x43ouponTextInfo\x12\x18\n\x10positive_preview\x18\x01 \x01(\t\x12\x0f\n\x07section\x18\x02 \x01(\t\"\x8c\x01\n\x0b\x43ouponToast\x12\x41\n\ttext_info\x18\x01 \x01(\x0b\x32..bilibili.pgc.gateway.player.v2.CouponTextInfo\x12:\n\x06\x62utton\x18\x02 \x01(\x0b\x32*.bilibili.pgc.gateway.player.v2.ButtonInfo\"\x8f\x01\n\x08\x44\x61shItem\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08\x62\x61se_url\x18\x02 \x01(\t\x12\x12\n\nbackup_url\x18\x03 \x03(\t\x12\x11\n\tbandwidth\x18\x04 \x01(\r\x12\x0f\n\x07\x63odecid\x18\x05 \x01(\r\x12\x0b\n\x03md5\x18\x06 \x01(\t\x12\x0c\n\x04size\x18\x07 \x01(\x04\x12\x12\n\nframe_rate\x18\x08 \x01(\t\"\xc9\x01\n\tDashVideo\x12\x10\n\x08\x62\x61se_url\x18\x01 \x01(\t\x12\x12\n\nbackup_url\x18\x02 \x03(\t\x12\x11\n\tbandwidth\x18\x03 \x01(\r\x12\x0f\n\x07\x63odecid\x18\x04 \x01(\r\x12\x0b\n\x03md5\x18\x05 \x01(\t\x12\x0c\n\x04size\x18\x06 \x01(\x04\x12\x10\n\x08\x61udio_id\x18\x07 \x01(\r\x12\x12\n\nno_rexcode\x18\x08 \x01(\x08\x12\x12\n\nframe_rate\x18\t \x01(\t\x12\r\n\x05width\x18\n \x01(\x05\x12\x0e\n\x06height\x18\x0b \x01(\x05\"\x8b\x05\n\x06\x44ialog\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x03\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x12\n\nstyle_type\x18\x04 \x01(\t\x12<\n\x06\x63onfig\x18\x05 \x01(\x0b\x32,.bilibili.pgc.gateway.player.v2.DialogConfig\x12\x37\n\x05title\x18\x06 \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.TextInfo\x12:\n\x08subtitle\x18\x07 \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.TextInfo\x12\x38\n\x05image\x18\x08 \x01(\x0b\x32).bilibili.pgc.gateway.player.v2.ImageInfo\x12:\n\x06\x62utton\x18\t \x03(\x0b\x32*.bilibili.pgc.gateway.player.v2.ButtonInfo\x12?\n\x0b\x62ottom_desc\x18\n \x01(\x0b\x32*.bilibili.pgc.gateway.player.v2.ButtonInfo\x12\x36\n\x06report\x18\x0b \x01(\x0b\x32&.bilibili.pgc.gateway.player.v2.Report\x12\x16\n\x0e\x63ount_down_sec\x18\x0c \x01(\x05\x12\x43\n\x11right_bottom_desc\x18\r \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.TextInfo\x12\x45\n\x0e\x62ottom_display\x18\x0e \x03(\x0b\x32-.bilibili.pgc.gateway.player.v2.BottomDisplay\"\x89\x01\n\x0c\x44ialogConfig\x12\x15\n\ris_show_cover\x18\x01 \x01(\x08\x12\x1d\n\x15is_orientation_enable\x18\x02 \x01(\x08\x12\x1f\n\x17is_nested_scroll_enable\x18\x03 \x01(\x08\x12\"\n\x1ais_force_halfscreen_enable\x18\x04 \x01(\x08\":\n\tDimension\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x0e\n\x06rotate\x18\x03 \x01(\x05\"\xab\x01\n\tDolbyItem\x12<\n\x04type\x18\x01 \x01(\x0e\x32..bilibili.pgc.gateway.player.v2.DolbyItem.Type\x12\x37\n\x05\x61udio\x18\x02 \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.DashItem\"\'\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x43OMMON\x10\x01\x12\t\n\x05\x41TMOS\x10\x02\"O\n\x07\x45ndPage\x12\x36\n\x06\x64ialog\x18\x01 \x01(\x0b\x32&.bilibili.pgc.gateway.player.v2.Dialog\x12\x0c\n\x04hide\x18\x02 \x01(\x08\"=\n\x05\x45vent\x12\x34\n\x05shake\x18\x01 \x01(\x0b\x32%.bilibili.pgc.gateway.player.v2.Shake\"\x88\x01\n\x0b\x46reyaConfig\x12\x0c\n\x04\x64\x65sc\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x12\n\nissued_cnt\x18\x03 \x01(\x05\x12\x16\n\x0eis_always_show\x18\x04 \x01(\x08\x12\x15\n\rscreen_number\x18\x05 \x01(\x05\x12\x1a\n\x12\x66ull_screen_number\x18\x06 \x01(\x05\"7\n\rGradientColor\x12\x13\n\x0bstart_color\x18\x01 \x01(\t\x12\x11\n\tend_color\x18\x02 \x01(\t\"\xab\x03\n\x17HighDefinitionTrialInfo\x12\x12\n\ntrial_able\x18\x01 \x01(\x08\x12\x17\n\x0fremaining_times\x18\x02 \x01(\x05\x12\r\n\x05start\x18\x03 \x01(\x05\x12\x13\n\x0btime_length\x18\x04 \x01(\x05\x12:\n\x0bstart_toast\x18\x05 \x01(\x0b\x32%.bilibili.pgc.gateway.player.v2.Toast\x12\x38\n\tend_toast\x18\x06 \x01(\x0b\x32%.bilibili.pgc.gateway.player.v2.Toast\x12\x36\n\x06report\x18\x07 \x01(\x0b\x32&.bilibili.pgc.gateway.player.v2.Report\x12H\n\x14quality_open_tip_btn\x18\x08 \x01(\x0b\x32*.bilibili.pgc.gateway.player.v2.ButtonInfo\x12G\n\x13no_longer_trial_btn\x18\t \x01(\x0b\x32*.bilibili.pgc.gateway.player.v2.ButtonInfo\"\x18\n\tImageInfo\x12\x0b\n\x03url\x18\x01 \x01(\t\"N\n\tMultiView\x12\x17\n\x0f\x62utton_material\x18\x01 \x01(\t\x12\r\n\x05\x65p_id\x18\x02 \x01(\x03\x12\x0b\n\x03\x63id\x18\x03 \x01(\x03\x12\x0c\n\x04\x61vid\x18\x04 \x01(\x03\"\xd4\x04\n\x06PayTip\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x11\n\tshow_type\x18\x05 \x01(\x05\x12\x0b\n\x03img\x18\x06 \x01(\t\x12\x14\n\x0c\x62g_day_color\x18\x07 \x01(\t\x12\x16\n\x0e\x62g_night_color\x18\x08 \x01(\t\x12\x15\n\rbg_line_color\x18\t \x01(\t\x12\x1b\n\x13\x62g_night_line_color\x18\n \x01(\t\x12\x12\n\ntext_color\x18\x0b \x01(\t\x12\x18\n\x10text_night_color\x18\x0c \x01(\t\x12\x17\n\x0fview_start_time\x18\r \x01(\x03\x12:\n\x06\x62utton\x18\x0e \x03(\x0b\x32*.bilibili.pgc.gateway.player.v2.ButtonInfo\x12\x15\n\rurl_open_type\x18\x0f \x01(\x05\x12\x36\n\x06report\x18\x10 \x01(\x0b\x32&.bilibili.pgc.gateway.player.v2.Report\x12\x13\n\x0b\x61ngle_style\x18\x11 \x01(\x05\x12\x13\n\x0breport_type\x18\x12 \x01(\x05\x12Z\n\x13order_report_params\x18\x13 \x03(\x0b\x32=.bilibili.pgc.gateway.player.v2.PayTip.OrderReportParamsEntry\x1a\x38\n\x16OrderReportParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xed\x06\n\x0fPlayAbilityConf\x12\x1f\n\x17\x62\x61\x63kground_play_disable\x18\x01 \x01(\x08\x12\x14\n\x0c\x66lip_disable\x18\x02 \x01(\x08\x12\x14\n\x0c\x63\x61st_disable\x18\x03 \x01(\x08\x12\x18\n\x10\x66\x65\x65\x64\x62\x61\x63k_disable\x18\x04 \x01(\x08\x12\x18\n\x10subtitle_disable\x18\x05 \x01(\x08\x12\x1d\n\x15playback_rate_disable\x18\x06 \x01(\x08\x12\x17\n\x0ftime_up_disable\x18\x07 \x01(\x08\x12\x1d\n\x15playback_mode_disable\x18\x08 \x01(\x08\x12\x1a\n\x12scale_mode_disable\x18\t \x01(\x08\x12\x14\n\x0clike_disable\x18\n \x01(\x08\x12\x17\n\x0f\x64islike_disable\x18\x0b \x01(\x08\x12\x14\n\x0c\x63oin_disable\x18\x0c \x01(\x08\x12\x14\n\x0c\x65lec_disable\x18\r \x01(\x08\x12\x15\n\rshare_disable\x18\x0e \x01(\x08\x12\x1b\n\x13screen_shot_disable\x18\x0f \x01(\x08\x12\x1b\n\x13lock_screen_disable\x18\x10 \x01(\x08\x12\x19\n\x11recommend_disable\x18\x11 \x01(\x08\x12\x1e\n\x16playback_speed_disable\x18\x12 \x01(\x08\x12\x1a\n\x12\x64\x65\x66inition_disable\x18\x13 \x01(\x08\x12\x1a\n\x12selections_disable\x18\x14 \x01(\x08\x12\x14\n\x0cnext_disable\x18\x15 \x01(\x08\x12\x17\n\x0f\x65\x64it_dm_disable\x18\x16 \x01(\x08\x12\x1c\n\x14small_window_disable\x18\x17 \x01(\x08\x12\x15\n\rshake_disable\x18\x18 \x01(\x08\x12\x18\n\x10outer_dm_disable\x18\x19 \x01(\x08\x12\x18\n\x10inner_dm_disable\x18\x1a \x01(\x08\x12\x1b\n\x13\x66reya_enter_disable\x18\x1b \x01(\x08\x12\x15\n\rdolby_disable\x18\x1c \x01(\x08\x12\x1a\n\x12\x66reya_full_disable\x18\x1d \x01(\x08\x12 \n\x18skip_oped_switch_disable\x18\x1e \x01(\x08\x12\x1d\n\x15record_screen_disable\x18\x1f \x01(\x08\x12\x1e\n\x16\x63olor_optimize_disable\x18  \x01(\x08\"\xb2\x01\n\x12PlayAbilityExtConf\x12\x1c\n\x14\x61llow_close_subtitle\x18\x01 \x01(\x08\x12\x41\n\x0c\x66reya_config\x18\x02 \x01(\x0b\x32+.bilibili.pgc.gateway.player.v2.FreyaConfig\x12;\n\tcast_tips\x18\x03 \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.CastTips\"\x9d\x06\n\x14PlayViewBusinessInfo\x12\x12\n\nis_preview\x18\x01 \x01(\x08\x12\n\n\x02\x62p\x18\x02 \x01(\x08\x12\x14\n\x0cmarlin_token\x18\x03 \x01(\t\x12\x1c\n\x14playback_speed_color\x18\x04 \x01(\t\x12L\n\x12\x63ontinue_play_info\x18\x05 \x01(\x0b\x32\x30.bilibili.pgc.gateway.player.v2.ContinuePlayInfo\x12;\n\tclip_info\x18\x06 \x03(\x0b\x32(.bilibili.pgc.gateway.player.v2.ClipInfo\x12?\n\x0binline_type\x18\x07 \x01(\x0e\x32*.bilibili.pgc.gateway.player.v2.InlineType\x12\x19\n\x11\x65p_whole_duration\x18\x08 \x01(\x05\x12<\n\tdimension\x18\t \x01(\x0b\x32).bilibili.pgc.gateway.player.v2.Dimension\x12`\n\x0fquality_ext_map\x18\n \x03(\x0b\x32G.bilibili.pgc.gateway.player.v2.PlayViewBusinessInfo.QualityExtMapEntry\x12Q\n\x07\x65xp_map\x18\x0b \x03(\x0b\x32@.bilibili.pgc.gateway.player.v2.PlayViewBusinessInfo.ExpMapEntry\x12\x42\n\rdrm_tech_type\x18\x0c \x01(\x0e\x32+.bilibili.pgc.gateway.player.v2.DrmTechType\x1a\x64\n\x12QualityExtMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12=\n\x05value\x18\x02 \x01(\x0b\x32..bilibili.pgc.gateway.player.v2.QualityExtInfo:\x02\x38\x01\x1a-\n\x0b\x45xpMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\x98\x03\n\rPlayViewReply\x12=\n\nvideo_info\x18\x01 \x01(\x0b\x32).bilibili.pgc.gateway.player.v2.VideoInfo\x12\x42\n\tplay_conf\x18\x02 \x01(\x0b\x32/.bilibili.pgc.gateway.player.v2.PlayAbilityConf\x12\x46\n\x08\x62usiness\x18\x03 \x01(\x0b\x32\x34.bilibili.pgc.gateway.player.v2.PlayViewBusinessInfo\x12\x34\n\x05\x65vent\x18\x04 \x01(\x0b\x32%.bilibili.pgc.gateway.player.v2.Event\x12;\n\tview_info\x18\x05 \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.ViewInfo\x12I\n\rplay_ext_conf\x18\x06 \x01(\x0b\x32\x32.bilibili.pgc.gateway.player.v2.PlayAbilityExtConf\"\xe4\x03\n\x0bPlayViewReq\x12\x0c\n\x04\x65pid\x18\x01 \x01(\x03\x12\x0b\n\x03\x63id\x18\x02 \x01(\x03\x12\n\n\x02qn\x18\x03 \x01(\x03\x12\r\n\x05\x66nver\x18\x04 \x01(\x05\x12\r\n\x05\x66nval\x18\x05 \x01(\x05\x12\x10\n\x08\x64ownload\x18\x06 \x01(\r\x12\x12\n\nforce_host\x18\x07 \x01(\x05\x12\r\n\x05\x66ourk\x18\x08 \x01(\x08\x12\r\n\x05spmid\x18\t \x01(\t\x12\x12\n\nfrom_spmid\x18\n \x01(\t\x12\x16\n\x0eteenagers_mode\x18\x0b \x01(\x05\x12\x43\n\x11prefer_codec_type\x18\x0c \x01(\x0e\x32(.bilibili.pgc.gateway.player.v2.CodeType\x12\x12\n\nis_preview\x18\r \x01(\x08\x12\x0f\n\x07room_id\x18\x0e \x01(\x03\x12\x19\n\x11is_need_view_info\x18\x0f \x01(\x08\x12\x43\n\rscene_control\x18\x10 \x01(\x0b\x32,.bilibili.pgc.gateway.player.v2.SceneControl\x12\x41\n\x0cinline_scene\x18\x11 \x01(\x0e\x32+.bilibili.pgc.gateway.player.v2.InlineScene\x12\x13\n\x0bmaterial_no\x18\x12 \x01(\x03\"\xfb\x02\n\x06PopWin\x12\r\n\x05title\x18\x01 \x01(\t\x12\x36\n\x06\x63oupon\x18\x02 \x03(\x0b\x32&.bilibili.pgc.gateway.player.v2.Coupon\x12:\n\x06\x62utton\x18\x03 \x03(\x0b\x32*.bilibili.pgc.gateway.player.v2.ButtonInfo\x12\x13\n\x0b\x62ottom_text\x18\x04 \x01(\t\x12;\n\tpop_title\x18\x05 \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.TextInfo\x12:\n\x08subtitle\x18\x06 \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.TextInfo\x12?\n\x0b\x62ottom_desc\x18\x07 \x01(\x0b\x32*.bilibili.pgc.gateway.player.v2.ButtonInfo\x12\r\n\x05\x63over\x18\x08 \x01(\t\x12\x10\n\x08pop_type\x18\t \x01(\t\"\xdc\x03\n\tPromptBar\x12\x37\n\x05title\x18\x01 \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.TextInfo\x12;\n\tsub_title\x18\x02 \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.TextInfo\x12\x16\n\x0esub_title_icon\x18\x03 \x01(\t\x12\x10\n\x08\x62g_image\x18\x04 \x01(\t\x12H\n\x11\x62g_gradient_color\x18\x05 \x01(\x0b\x32-.bilibili.pgc.gateway.player.v2.GradientColor\x12:\n\x06\x62utton\x18\x06 \x03(\x0b\x32*.bilibili.pgc.gateway.player.v2.ButtonInfo\x12\x36\n\x06report\x18\x07 \x01(\x0b\x32&.bilibili.pgc.gateway.player.v2.Report\x12\x1b\n\x13\x66ull_screen_ip_icon\x18\x08 \x01(\t\x12T\n\x1d\x66ull_screen_bg_gradient_color\x18\t \x01(\x0b\x32-.bilibili.pgc.gateway.player.v2.GradientColor\"\'\n\x0eQualityExtInfo\x12\x15\n\rtrial_support\x18\x01 \x01(\x08\"H\n\x06Report\x12\x15\n\rshow_event_id\x18\x01 \x01(\t\x12\x16\n\x0e\x63lick_event_id\x18\x02 \x01(\t\x12\x0f\n\x07\x65xtends\x18\x03 \x01(\t\"h\n\x0bResponseUrl\x12\r\n\x05order\x18\x01 \x01(\r\x12\x0e\n\x06length\x18\x02 \x01(\x04\x12\x0c\n\x04size\x18\x03 \x01(\x04\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x12\n\nbackup_url\x18\x05 \x03(\t\x12\x0b\n\x03md5\x18\x06 \x01(\t\"u\n\x0cSceneControl\x12\x14\n\x0c\x66\x61v_playlist\x18\x01 \x01(\x08\x12\x14\n\x0csmall_window\x18\x02 \x01(\x08\x12\x0b\n\x03pip\x18\x03 \x01(\x08\x12\x15\n\rwas_he_inline\x18\x04 \x01(\x08\x12\x15\n\ris_need_trial\x18\x05 \x01(\x08\"L\n\x0cSegmentVideo\x12<\n\x07segment\x18\x01 \x03(\x0b\x32+.bilibili.pgc.gateway.player.v2.ResponseUrl\"\x15\n\x05Shake\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\"\xd5\x01\n\x06Stream\x12\x38\n\x04info\x18\x01 \x01(\x0b\x32*.bilibili.pgc.gateway.player.v2.StreamInfo\x12?\n\ndash_video\x18\x02 \x01(\x0b\x32).bilibili.pgc.gateway.player.v2.DashVideoH\x00\x12\x45\n\rsegment_video\x18\x03 \x01(\x0b\x32,.bilibili.pgc.gateway.player.v2.SegmentVideoH\x00\x42\t\n\x07\x63ontent\"\xb1\x02\n\nStreamInfo\x12\x0f\n\x07quality\x18\x01 \x01(\r\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08\x65rr_code\x18\x04 \x01(\r\x12:\n\x05limit\x18\x05 \x01(\x0b\x32+.bilibili.pgc.gateway.player.v2.StreamLimit\x12\x10\n\x08need_vip\x18\x06 \x01(\x08\x12\x12\n\nneed_login\x18\x07 \x01(\x08\x12\x0e\n\x06intact\x18\x08 \x01(\x08\x12\x12\n\nno_rexcode\x18\t \x01(\x08\x12\x11\n\tattribute\x18\n \x01(\x03\x12\x17\n\x0fnew_description\x18\x0b \x01(\t\x12\x14\n\x0c\x64isplay_desc\x18\x0c \x01(\t\x12\x13\n\x0bsuperscript\x18\r \x01(\t\"6\n\x0bStreamLimit\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\"C\n\x08TextInfo\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x11\n\ttextColor\x18\x02 \x01(\t\x12\x16\n\x0etextColorNight\x18\x03 \x01(\t\"\x83\x03\n\x05Toast\x12\x0c\n\x04text\x18\x01 \x01(\t\x12:\n\x06\x62utton\x18\x02 \x01(\x0b\x32*.bilibili.pgc.gateway.player.v2.ButtonInfo\x12\x17\n\x0fshow_style_type\x18\x03 \x01(\x05\x12\x0c\n\x04icon\x18\x04 \x01(\t\x12<\n\ntoast_text\x18\x05 \x01(\x0b\x32(.bilibili.pgc.gateway.player.v2.TextInfo\x12\x36\n\x06report\x18\x06 \x01(\x0b\x32&.bilibili.pgc.gateway.player.v2.Report\x12Y\n\x13order_report_params\x18\x07 \x03(\x0b\x32<.bilibili.pgc.gateway.player.v2.Toast.OrderReportParamsEntry\x1a\x38\n\x16OrderReportParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8c\x02\n\tVideoInfo\x12\x0f\n\x07quality\x18\x01 \x01(\r\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x12\x12\n\ntimelength\x18\x03 \x01(\x04\x12\x15\n\rvideo_codecid\x18\x04 \x01(\r\x12;\n\x0bstream_list\x18\x05 \x03(\x0b\x32&.bilibili.pgc.gateway.player.v2.Stream\x12<\n\ndash_audio\x18\x06 \x03(\x0b\x32(.bilibili.pgc.gateway.player.v2.DashItem\x12\x38\n\x05\x64olby\x18\x07 \x01(\x0b\x32).bilibili.pgc.gateway.player.v2.DolbyItem\"\xcf\x06\n\x08ViewInfo\x12\x36\n\x06\x64ialog\x18\x01 \x01(\x0b\x32&.bilibili.pgc.gateway.player.v2.Dialog\x12\x34\n\x05toast\x18\x02 \x01(\x0b\x32%.bilibili.pgc.gateway.player.v2.Toast\x12?\n\x0b\x63oupon_info\x18\x03 \x01(\x0b\x32*.bilibili.pgc.gateway.player.v2.CouponInfo\x12\x1b\n\x13\x64\x65mand_no_pay_epids\x18\x04 \x03(\x03\x12\x39\n\x08\x65nd_page\x18\x05 \x01(\x0b\x32\'.bilibili.pgc.gateway.player.v2.EndPage\x12K\n\nexp_config\x18\x06 \x03(\x0b\x32\x37.bilibili.pgc.gateway.player.v2.ViewInfo.ExpConfigEntry\x12\x37\n\x07pop_win\x18\x07 \x01(\x0b\x32&.bilibili.pgc.gateway.player.v2.PopWin\x12G\n\x14try_watch_prompt_bar\x18\x08 \x01(\x0b\x32).bilibili.pgc.gateway.player.v2.PromptBar\x12\x37\n\x07pay_tip\x18\t \x01(\x0b\x32&.bilibili.pgc.gateway.player.v2.PayTip\x12[\n\x1ahigh_definition_trial_info\x18\n \x01(\x0b\x32\x37.bilibili.pgc.gateway.player.v2.HighDefinitionTrialInfo\x12K\n\next_dialog\x18\x0b \x03(\x0b\x32\x37.bilibili.pgc.gateway.player.v2.ViewInfo.ExtDialogEntry\x1a\x30\n\x0e\x45xpConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1aX\n\x0e\x45xtDialogEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.bilibili.pgc.gateway.player.v2.Dialog:\x02\x38\x01*j\n\x08\x43lipType\x12\x0e\n\nNT_UNKNOWN\x10\x00\x12\x10\n\x0c\x43LIP_TYPE_OP\x10\x01\x12\x10\n\x0c\x43LIP_TYPE_ED\x10\x02\x12\x10\n\x0c\x43LIP_TYPE_HE\x10\x03\x12\x18\n\x14\x43LIP_TYPE_MULTI_VIEW\x10\x04*0\n\x08\x43odeType\x12\n\n\x06NOCODE\x10\x00\x12\x0b\n\x07\x43ODE264\x10\x01\x12\x0b\n\x07\x43ODE265\x10\x02*%\n\x0b\x44rmTechType\x12\x07\n\x03NON\x10\x00\x12\r\n\tFAIR_PLAY\x10\x01*<\n\x0bInlineScene\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nRELATED_EP\x10\x01\x12\x06\n\x02HE\x10\x02\x12\x08\n\x04SKIP\x10\x03*R\n\nInlineType\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x0e\n\nTYPE_WHOLE\x10\x01\x12\x10\n\x0cTYPE_HE_CLIP\x10\x02\x12\x10\n\x0cTYPE_PREVIEW\x10\x03*1\n\x07PlayErr\x12\t\n\x05NoErr\x10\x00\x12\x1b\n\x17WithMultiDeviceLoginErr\x10\x01\x32\xde\x01\n\x07PlayURL\x12\x66\n\x08PlayView\x12+.bilibili.pgc.gateway.player.v2.PlayViewReq\x1a-.bilibili.pgc.gateway.player.v2.PlayViewReply\x12k\n\rPlayViewComic\x12+.bilibili.pgc.gateway.player.v2.PlayViewReq\x1a-.bilibili.pgc.gateway.player.v2.PlayViewReplyb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'bilibili.pgc.gateway.player.v2.playurl_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _BUTTONINFO_ORDERREPORTPARAMSENTRY._options = None
    _BUTTONINFO_ORDERREPORTPARAMSENTRY._serialized_options = b'8\001'
    _PAYTIP_ORDERREPORTPARAMSENTRY._options = None
    _PAYTIP_ORDERREPORTPARAMSENTRY._serialized_options = b'8\001'
    _PLAYVIEWBUSINESSINFO_QUALITYEXTMAPENTRY._options = None
    _PLAYVIEWBUSINESSINFO_QUALITYEXTMAPENTRY._serialized_options = b'8\001'
    _PLAYVIEWBUSINESSINFO_EXPMAPENTRY._options = None
    _PLAYVIEWBUSINESSINFO_EXPMAPENTRY._serialized_options = b'8\001'
    _TOAST_ORDERREPORTPARAMSENTRY._options = None
    _TOAST_ORDERREPORTPARAMSENTRY._serialized_options = b'8\001'
    _VIEWINFO_EXPCONFIGENTRY._options = None
    _VIEWINFO_EXPCONFIGENTRY._serialized_options = b'8\001'
    _VIEWINFO_EXTDIALOGENTRY._options = None
    _VIEWINFO_EXTDIALOGENTRY._serialized_options = b'8\001'
    _CLIPTYPE._serialized_start = 10971
    _CLIPTYPE._serialized_end = 11077
    _CODETYPE._serialized_start = 11079
    _CODETYPE._serialized_end = 11127
    _DRMTECHTYPE._serialized_start = 11129
    _DRMTECHTYPE._serialized_end = 11166
    _INLINESCENE._serialized_start = 11168
    _INLINESCENE._serialized_end = 11228
    _INLINETYPE._serialized_start = 11230
    _INLINETYPE._serialized_end = 11312
    _PLAYERR._serialized_start = 11314
    _PLAYERR._serialized_end = 11363
    _BADGEINFO._serialized_start = 114
    _BADGEINFO._serialized_end = 275
    _BOTTOMDISPLAY._serialized_start = 277
    _BOTTOMDISPLAY._serialized_end = 363
    _BUTTONINFO._serialized_start = 366
    _BUTTONINFO._serialized_end = 1019
    _BUTTONINFO_ORDERREPORTPARAMSENTRY._serialized_start = 963
    _BUTTONINFO_ORDERREPORTPARAMSENTRY._serialized_end = 1019
    _CASTTIPS._serialized_start = 1021
    _CASTTIPS._serialized_end = 1062
    _CLIPINFO._serialized_start = 1065
    _CLIPINFO._serialized_end = 1268
    _CONTINUEPLAYINFO._serialized_start = 1270
    _CONTINUEPLAYINFO._serialized_end = 1317
    _COUPON._serialized_start = 1320
    _COUPON._serialized_end = 1559
    _COUPONINFO._serialized_start = 1562
    _COUPONINFO._serialized_end = 1691
    _COUPONTEXTINFO._serialized_start = 1693
    _COUPONTEXTINFO._serialized_end = 1752
    _COUPONTOAST._serialized_start = 1755
    _COUPONTOAST._serialized_end = 1895
    _DASHITEM._serialized_start = 1898
    _DASHITEM._serialized_end = 2041
    _DASHVIDEO._serialized_start = 2044
    _DASHVIDEO._serialized_end = 2245
    _DIALOG._serialized_start = 2248
    _DIALOG._serialized_end = 2899
    _DIALOGCONFIG._serialized_start = 2902
    _DIALOGCONFIG._serialized_end = 3039
    _DIMENSION._serialized_start = 3041
    _DIMENSION._serialized_end = 3099
    _DOLBYITEM._serialized_start = 3102
    _DOLBYITEM._serialized_end = 3273
    _DOLBYITEM_TYPE._serialized_start = 3234
    _DOLBYITEM_TYPE._serialized_end = 3273
    _ENDPAGE._serialized_start = 3275
    _ENDPAGE._serialized_end = 3354
    _EVENT._serialized_start = 3356
    _EVENT._serialized_end = 3417
    _FREYACONFIG._serialized_start = 3420
    _FREYACONFIG._serialized_end = 3556
    _GRADIENTCOLOR._serialized_start = 3558
    _GRADIENTCOLOR._serialized_end = 3613
    _HIGHDEFINITIONTRIALINFO._serialized_start = 3616
    _HIGHDEFINITIONTRIALINFO._serialized_end = 4043
    _IMAGEINFO._serialized_start = 4045
    _IMAGEINFO._serialized_end = 4069
    _MULTIVIEW._serialized_start = 4071
    _MULTIVIEW._serialized_end = 4149
    _PAYTIP._serialized_start = 4152
    _PAYTIP._serialized_end = 4748
    _PAYTIP_ORDERREPORTPARAMSENTRY._serialized_start = 963
    _PAYTIP_ORDERREPORTPARAMSENTRY._serialized_end = 1019
    _PLAYABILITYCONF._serialized_start = 4751
    _PLAYABILITYCONF._serialized_end = 5628
    _PLAYABILITYEXTCONF._serialized_start = 5631
    _PLAYABILITYEXTCONF._serialized_end = 5809
    _PLAYVIEWBUSINESSINFO._serialized_start = 5812
    _PLAYVIEWBUSINESSINFO._serialized_end = 6609
    _PLAYVIEWBUSINESSINFO_QUALITYEXTMAPENTRY._serialized_start = 6462
    _PLAYVIEWBUSINESSINFO_QUALITYEXTMAPENTRY._serialized_end = 6562
    _PLAYVIEWBUSINESSINFO_EXPMAPENTRY._serialized_start = 6564
    _PLAYVIEWBUSINESSINFO_EXPMAPENTRY._serialized_end = 6609
    _PLAYVIEWREPLY._serialized_start = 6612
    _PLAYVIEWREPLY._serialized_end = 7020
    _PLAYVIEWREQ._serialized_start = 7023
    _PLAYVIEWREQ._serialized_end = 7507
    _POPWIN._serialized_start = 7510
    _POPWIN._serialized_end = 7889
    _PROMPTBAR._serialized_start = 7892
    _PROMPTBAR._serialized_end = 8368
    _QUALITYEXTINFO._serialized_start = 8370
    _QUALITYEXTINFO._serialized_end = 8409
    _REPORT._serialized_start = 8411
    _REPORT._serialized_end = 8483
    _RESPONSEURL._serialized_start = 8485
    _RESPONSEURL._serialized_end = 8589
    _SCENECONTROL._serialized_start = 8591
    _SCENECONTROL._serialized_end = 8708
    _SEGMENTVIDEO._serialized_start = 8710
    _SEGMENTVIDEO._serialized_end = 8786
    _SHAKE._serialized_start = 8788
    _SHAKE._serialized_end = 8809
    _STREAM._serialized_start = 8812
    _STREAM._serialized_end = 9025
    _STREAMINFO._serialized_start = 9028
    _STREAMINFO._serialized_end = 9333
    _STREAMLIMIT._serialized_start = 9335
    _STREAMLIMIT._serialized_end = 9389
    _TEXTINFO._serialized_start = 9391
    _TEXTINFO._serialized_end = 9458
    _TOAST._serialized_start = 9461
    _TOAST._serialized_end = 9848
    _TOAST_ORDERREPORTPARAMSENTRY._serialized_start = 963
    _TOAST_ORDERREPORTPARAMSENTRY._serialized_end = 1019
    _VIDEOINFO._serialized_start = 9851
    _VIDEOINFO._serialized_end = 10119
    _VIEWINFO._serialized_start = 10122
    _VIEWINFO._serialized_end = 10969
    _VIEWINFO_EXPCONFIGENTRY._serialized_start = 10831
    _VIEWINFO_EXPCONFIGENTRY._serialized_end = 10879
    _VIEWINFO_EXTDIALOGENTRY._serialized_start = 10881
    _VIEWINFO_EXTDIALOGENTRY._serialized_end = 10969
    _PLAYURL._serialized_start = 11366
    _PLAYURL._serialized_end = 11588
# @@protoc_insertion_point(module_scope)

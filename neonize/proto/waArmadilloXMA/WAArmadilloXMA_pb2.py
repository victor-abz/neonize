# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: waArmadilloXMA/WAArmadilloXMA.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'waArmadilloXMA/WAArmadilloXMA.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waCommon import WACommon_pb2 as waCommon_dot_WACommon__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#waArmadilloXMA/WAArmadilloXMA.proto\x12\x0eWAArmadilloXMA\x1a\x17waCommon/WACommon.proto\"\xf0\x18\n\x16\x45xtendedContentMessage\x12\x30\n\x11\x61ssociatedMessage\x18\x01 \x01(\x0b\x32\x15.WACommon.SubProtocol\x12N\n\ntargetType\x18\x02 \x01(\x0e\x32:.WAArmadilloXMA.ExtendedContentMessage.ExtendedContentType\x12\x16\n\x0etargetUsername\x18\x03 \x01(\t\x12\x10\n\x08targetID\x18\x04 \x01(\t\x12\x1b\n\x13targetExpiringAtSec\x18\x05 \x01(\x03\x12K\n\rxmaLayoutType\x18\x06 \x01(\x0e\x32\x34.WAArmadilloXMA.ExtendedContentMessage.XmaLayoutType\x12\x38\n\x04\x63tas\x18\x07 \x03(\x0b\x32*.WAArmadilloXMA.ExtendedContentMessage.CTA\x12\'\n\x08previews\x18\x08 \x03(\x0b\x32\x15.WACommon.SubProtocol\x12\x11\n\ttitleText\x18\t \x01(\t\x12\x14\n\x0csubtitleText\x18\n \x01(\t\x12\x1a\n\x12maxTitleNumOfLines\x18\x0b \x01(\r\x12\x1d\n\x15maxSubtitleNumOfLines\x18\x0c \x01(\r\x12&\n\x07\x66\x61vicon\x18\r \x01(\x0b\x32\x15.WACommon.SubProtocol\x12*\n\x0bheaderImage\x18\x0e \x01(\x0b\x32\x15.WACommon.SubProtocol\x12\x13\n\x0bheaderTitle\x18\x0f \x01(\t\x12Q\n\x10overlayIconGlyph\x18\x10 \x01(\x0e\x32\x37.WAArmadilloXMA.ExtendedContentMessage.OverlayIconGlyph\x12\x14\n\x0coverlayTitle\x18\x11 \x01(\t\x12\x1a\n\x12overlayDescription\x18\x12 \x01(\t\x12\x19\n\x11sentWithMessageID\x18\x13 \x01(\t\x12\x13\n\x0bmessageText\x18\x14 \x01(\t\x12\x16\n\x0eheaderSubtitle\x18\x15 \x01(\t\x12\x14\n\x0cxmaDataclass\x18\x16 \x01(\t\x12\x12\n\ncontentRef\x18\x17 \x01(\t\x12\x14\n\x0cmentionedJID\x18\x18 \x03(\t\x12#\n\x08\x63ommands\x18\x19 \x03(\x0b\x32\x11.WACommon.Command\x1a\xb0\x01\n\x03\x43TA\x12H\n\nbuttonType\x18\x01 \x01(\x0e\x32\x34.WAArmadilloXMA.ExtendedContentMessage.CtaButtonType\x12\r\n\x05title\x18\x02 \x01(\t\x12\x11\n\tactionURL\x18\x03 \x01(\t\x12\x11\n\tnativeURL\x18\x04 \x01(\t\x12\x0f\n\x07\x63taType\x18\x05 \x01(\t\x12\x19\n\x11\x61\x63tionContentBlob\x18\x06 \x01(\t\"\xa1\x01\n\x10OverlayIconGlyph\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07\x45YE_OFF\x10\x01\x12\x0c\n\x08NEWS_OFF\x10\x02\x12\x0b\n\x07WARNING\x10\x03\x12\x0b\n\x07PRIVATE\x10\x04\x12\x08\n\x04NONE\x10\x05\x12\x0f\n\x0bMEDIA_LABEL\x10\x06\x12\x0e\n\nPOST_COVER\x10\x07\x12\x0e\n\nPOST_LABEL\x10\x08\x12\x13\n\x0fWARNING_SCREENS\x10\t\" \n\rCtaButtonType\x12\x0f\n\x0bOPEN_NATIVE\x10\x0b\"b\n\rXmaLayoutType\x12\n\n\x06SINGLE\x10\x00\x12\x0b\n\x07HSCROLL\x10\x01\x12\x0c\n\x08PORTRAIT\x10\x03\x12\x11\n\rSTANDARD_DXMA\x10\x0c\x12\r\n\tLIST_DXMA\x10\x0f\x12\x08\n\x04GRID\x10\x10\"\x80\x0e\n\x13\x45xtendedContentType\x12\x0f\n\x0bUNSUPPORTED\x10\x00\x12\x1a\n\x16IG_STORY_PHOTO_MENTION\x10\x04\x12\x1e\n\x1aIG_SINGLE_IMAGE_POST_SHARE\x10\t\x12\x16\n\x12IG_MULTIPOST_SHARE\x10\n\x12\x1e\n\x1aIG_SINGLE_VIDEO_POST_SHARE\x10\x0b\x12\x18\n\x14IG_STORY_PHOTO_SHARE\x10\x0c\x12\x18\n\x14IG_STORY_VIDEO_SHARE\x10\r\x12\x12\n\x0eIG_CLIPS_SHARE\x10\x0e\x12\x11\n\rIG_IGTV_SHARE\x10\x0f\x12\x11\n\rIG_SHOP_SHARE\x10\x10\x12\x14\n\x10IG_PROFILE_SHARE\x10\x13\x12\"\n\x1eIG_STORY_PHOTO_HIGHLIGHT_SHARE\x10\x14\x12\"\n\x1eIG_STORY_VIDEO_HIGHLIGHT_SHARE\x10\x15\x12\x12\n\x0eIG_STORY_REPLY\x10\x16\x12\x15\n\x11IG_STORY_REACTION\x10\x17\x12\x1a\n\x16IG_STORY_VIDEO_MENTION\x10\x18\x12\x1c\n\x18IG_STORY_HIGHLIGHT_REPLY\x10\x19\x12\x1f\n\x1bIG_STORY_HIGHLIGHT_REACTION\x10\x1a\x12\x14\n\x10IG_EXTERNAL_LINK\x10\x1b\x12\x15\n\x11IG_RECEIVER_FETCH\x10\x1c\x12\x12\n\rFB_FEED_SHARE\x10\xe8\x07\x12\x13\n\x0e\x46\x42_STORY_REPLY\x10\xe9\x07\x12\x13\n\x0e\x46\x42_STORY_SHARE\x10\xea\x07\x12\x15\n\x10\x46\x42_STORY_MENTION\x10\xeb\x07\x12\x18\n\x13\x46\x42_FEED_VIDEO_SHARE\x10\xec\x07\x12\x1c\n\x17\x46\x42_GAMING_CUSTOM_UPDATE\x10\xed\x07\x12\x1c\n\x17\x46\x42_PRODUCER_STORY_REPLY\x10\xee\x07\x12\r\n\x08\x46\x42_EVENT\x10\xef\x07\x12\x1f\n\x1a\x46\x42_FEED_POST_PRIVATE_REPLY\x10\xf0\x07\x12\r\n\x08\x46\x42_SHORT\x10\xf1\x07\x12\x1d\n\x18\x46\x42_COMMENT_MENTION_SHARE\x10\xf2\x07\x12\x14\n\x0f\x46\x42_POST_MENTION\x10\xf3\x07\x12\x1c\n\x17MSG_EXTERNAL_LINK_SHARE\x10\xd0\x0f\x12\x14\n\x0fMSG_P2P_PAYMENT\x10\xd1\x0f\x12\x19\n\x14MSG_LOCATION_SHARING\x10\xd2\x0f\x12\x1c\n\x17MSG_LOCATION_SHARING_V2\x10\xd3\x0f\x12,\n\'MSG_HIGHLIGHTS_TAB_FRIEND_UPDATES_REPLY\x10\xd4\x0f\x12)\n$MSG_HIGHLIGHTS_TAB_LOCAL_EVENT_REPLY\x10\xd5\x0f\x12\x17\n\x12MSG_RECEIVER_FETCH\x10\xd6\x0f\x12\x17\n\x12MSG_IG_MEDIA_SHARE\x10\xd7\x0f\x12&\n!MSG_GEN_AI_SEARCH_PLUGIN_RESPONSE\x10\xd8\x0f\x12\x13\n\x0eMSG_REELS_LIST\x10\xd9\x0f\x12\x10\n\x0bMSG_CONTACT\x10\xda\x0f\x12\x1b\n\x16MSG_THREADS_POST_SHARE\x10\xdb\x0f\x12\r\n\x08MSG_FILE\x10\xdc\x0f\x12\x17\n\x12MSG_AVATAR_DETAILS\x10\xdd\x0f\x12\x13\n\x0eMSG_AI_CONTACT\x10\xde\x0f\x12\x17\n\x12MSG_MEMORIES_SHARE\x10\xdf\x0f\x12\x1b\n\x16MSG_SHARED_ALBUM_REPLY\x10\xe0\x0f\x12\x15\n\x10MSG_SHARED_ALBUM\x10\xe1\x0f\x12\x18\n\x13MSG_OCCAMADILLO_XMA\x10\xe2\x0f\x12\x1c\n\x17MSG_GEN_AI_SUBSCRIPTION\x10\xe5\x0f\x12\x18\n\x13MSG_GEN_AI_REMINDER\x10\xe6\x0f\x12(\n#MSG_GEN_AI_MEMU_ONBOARDING_RESPONSE\x10\xe7\x0f\x12\x13\n\x0eMSG_NOTE_REPLY\x10\xe8\x0f\x12\x15\n\x10MSG_NOTE_MENTION\x10\xe9\x0f\x12\x13\n\x0eRTC_AUDIO_CALL\x10\xb8\x17\x12\x13\n\x0eRTC_VIDEO_CALL\x10\xb9\x17\x12\x1a\n\x15RTC_MISSED_AUDIO_CALL\x10\xba\x17\x12\x1a\n\x15RTC_MISSED_VIDEO_CALL\x10\xbb\x17\x12\x19\n\x14RTC_GROUP_AUDIO_CALL\x10\xbc\x17\x12\x19\n\x14RTC_GROUP_VIDEO_CALL\x10\xbd\x17\x12 \n\x1bRTC_MISSED_GROUP_AUDIO_CALL\x10\xbe\x17\x12 \n\x1bRTC_MISSED_GROUP_VIDEO_CALL\x10\xbf\x17\x12\x1b\n\x16RTC_ONGOING_AUDIO_CALL\x10\xc0\x17\x12\x1b\n\x16RTC_ONGOING_VIDEO_CALL\x10\xc1\x17\x12\x1a\n\x15\x44\x41TACLASS_SENDER_COPY\x10\xa0\x1f\x42*Z(go.mau.fi/whatsmeow/proto/waArmadilloXMA')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waArmadilloXMA.WAArmadilloXMA_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z(go.mau.fi/whatsmeow/proto/waArmadilloXMA'
  _globals['_EXTENDEDCONTENTMESSAGE']._serialized_start=81
  _globals['_EXTENDEDCONTENTMESSAGE']._serialized_end=3265
  _globals['_EXTENDEDCONTENTMESSAGE_CTA']._serialized_start=996
  _globals['_EXTENDEDCONTENTMESSAGE_CTA']._serialized_end=1172
  _globals['_EXTENDEDCONTENTMESSAGE_OVERLAYICONGLYPH']._serialized_start=1175
  _globals['_EXTENDEDCONTENTMESSAGE_OVERLAYICONGLYPH']._serialized_end=1336
  _globals['_EXTENDEDCONTENTMESSAGE_CTABUTTONTYPE']._serialized_start=1338
  _globals['_EXTENDEDCONTENTMESSAGE_CTABUTTONTYPE']._serialized_end=1370
  _globals['_EXTENDEDCONTENTMESSAGE_XMALAYOUTTYPE']._serialized_start=1372
  _globals['_EXTENDEDCONTENTMESSAGE_XMALAYOUTTYPE']._serialized_end=1470
  _globals['_EXTENDEDCONTENTMESSAGE_EXTENDEDCONTENTTYPE']._serialized_start=1473
  _globals['_EXTENDEDCONTENTMESSAGE_EXTENDEDCONTENTTYPE']._serialized_end=3265
# @@protoc_insertion_point(module_scope)

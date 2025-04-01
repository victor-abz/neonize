# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waHistorySync/WAWebProtobufsHistorySync.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waSyncAction import WASyncAction_pb2 as waSyncAction_dot_WASyncAction__pb2
from waChatLockSettings import WAProtobufsChatLockSettings_pb2 as waChatLockSettings_dot_WAProtobufsChatLockSettings__pb2
from waE2E import WAWebProtobufsE2E_pb2 as waE2E_dot_WAWebProtobufsE2E__pb2
from waCommon import WACommon_pb2 as waCommon_dot_WACommon__pb2
from waWeb import WAWebProtobufsWeb_pb2 as waWeb_dot_WAWebProtobufsWeb__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-waHistorySync/WAWebProtobufsHistorySync.proto\x12\x19WAWebProtobufsHistorySync\x1a\x1fwaSyncAction/WASyncAction.proto\x1a\x34waChatLockSettings/WAProtobufsChatLockSettings.proto\x1a\x1dwaE2E/WAWebProtobufsE2E.proto\x1a\x17waCommon/WACommon.proto\x1a\x1dwaWeb/WAWebProtobufsWeb.proto\"\xe2\x08\n\x0bHistorySync\x12H\n\x08syncType\x18\x01 \x02(\x0e\x32\x36.WAWebProtobufsHistorySync.HistorySync.HistorySyncType\x12>\n\rconversations\x18\x02 \x03(\x0b\x32\'.WAWebProtobufsHistorySync.Conversation\x12;\n\x10statusV3Messages\x18\x03 \x03(\x0b\x32!.WAWebProtobufsWeb.WebMessageInfo\x12\x12\n\nchunkOrder\x18\x05 \x01(\r\x12\x10\n\x08progress\x18\x06 \x01(\r\x12\x36\n\tpushnames\x18\x07 \x03(\x0b\x32#.WAWebProtobufsHistorySync.Pushname\x12\x41\n\x0eglobalSettings\x18\x08 \x01(\x0b\x32).WAWebProtobufsHistorySync.GlobalSettings\x12\x1a\n\x12threadIDUserSecret\x18\t \x01(\x0c\x12\x1f\n\x17threadDsTimeframeOffset\x18\n \x01(\r\x12\x42\n\x0erecentStickers\x18\x0b \x03(\x0b\x32*.WAWebProtobufsHistorySync.StickerMetadata\x12\x45\n\x10pastParticipants\x18\x0c \x03(\x0b\x32+.WAWebProtobufsHistorySync.PastParticipants\x12\x33\n\x0e\x63\x61llLogRecords\x18\r \x03(\x0b\x32\x1b.WASyncAction.CallLogRecord\x12R\n\x0f\x61iWaitListState\x18\x0e \x01(\x0e\x32\x39.WAWebProtobufsHistorySync.HistorySync.BotAIWaitListState\x12T\n\x18phoneNumberToLidMappings\x18\x0f \x03(\x0b\x32\x32.WAWebProtobufsHistorySync.PhoneNumberToLIDMapping\x12\x1a\n\x12\x63ompanionMetaNonce\x18\x10 \x01(\t\x12,\n$shareableChatIdentifierEncryptionKey\x18\x11 \x01(\x0c\x12\x34\n\x08\x61\x63\x63ounts\x18\x12 \x03(\x0b\x32\".WAWebProtobufsHistorySync.Account\"7\n\x12\x42otAIWaitListState\x12\x0f\n\x0bIN_WAITLIST\x10\x00\x12\x10\n\x0c\x41I_AVAILABLE\x10\x01\"\x8a\x01\n\x0fHistorySyncType\x12\x15\n\x11INITIAL_BOOTSTRAP\x10\x00\x12\x15\n\x11INITIAL_STATUS_V3\x10\x01\x12\x08\n\x04\x46ULL\x10\x02\x12\n\n\x06RECENT\x10\x03\x12\r\n\tPUSH_NAME\x10\x04\x12\x15\n\x11NON_BLOCKING_DATA\x10\x05\x12\r\n\tON_DEMAND\x10\x06\"\xf3\r\n\x0c\x43onversation\x12\n\n\x02ID\x18\x01 \x02(\t\x12;\n\x08messages\x18\x02 \x03(\x0b\x32).WAWebProtobufsHistorySync.HistorySyncMsg\x12\x0e\n\x06newJID\x18\x03 \x01(\t\x12\x0e\n\x06oldJID\x18\x04 \x01(\t\x12\x18\n\x10lastMsgTimestamp\x18\x05 \x01(\x04\x12\x13\n\x0bunreadCount\x18\x06 \x01(\r\x12\x10\n\x08readOnly\x18\x07 \x01(\x08\x12\x1c\n\x14\x65ndOfHistoryTransfer\x18\x08 \x01(\x08\x12\x1b\n\x13\x65phemeralExpiration\x18\t \x01(\r\x12!\n\x19\x65phemeralSettingTimestamp\x18\n \x01(\x03\x12\x62\n\x18\x65ndOfHistoryTransferType\x18\x0b \x01(\x0e\x32@.WAWebProtobufsHistorySync.Conversation.EndOfHistoryTransferType\x12\x1d\n\x15\x63onversationTimestamp\x18\x0c \x01(\x04\x12\x0c\n\x04name\x18\r \x01(\t\x12\r\n\x05pHash\x18\x0e \x01(\t\x12\x0f\n\x07notSpam\x18\x0f \x01(\x08\x12\x10\n\x08\x61rchived\x18\x10 \x01(\x08\x12=\n\x10\x64isappearingMode\x18\x11 \x01(\x0b\x32#.WAWebProtobufsE2E.DisappearingMode\x12\x1a\n\x12unreadMentionCount\x18\x12 \x01(\r\x12\x16\n\x0emarkedAsUnread\x18\x13 \x01(\x08\x12@\n\x0bparticipant\x18\x14 \x03(\x0b\x32+.WAWebProtobufsHistorySync.GroupParticipant\x12\x0f\n\x07tcToken\x18\x15 \x01(\x0c\x12\x18\n\x10tcTokenTimestamp\x18\x16 \x01(\x04\x12!\n\x19\x63ontactPrimaryIdentityKey\x18\x17 \x01(\x0c\x12\x0e\n\x06pinned\x18\x18 \x01(\r\x12\x13\n\x0bmuteEndTime\x18\x19 \x01(\x04\x12?\n\twallpaper\x18\x1a \x01(\x0b\x32,.WAWebProtobufsHistorySync.WallpaperSettings\x12\x43\n\x0fmediaVisibility\x18\x1b \x01(\x0e\x32*.WAWebProtobufsHistorySync.MediaVisibility\x12\x1e\n\x16tcTokenSenderTimestamp\x18\x1c \x01(\x04\x12\x11\n\tsuspended\x18\x1d \x01(\x08\x12\x12\n\nterminated\x18\x1e \x01(\x08\x12\x11\n\tcreatedAt\x18\x1f \x01(\x04\x12\x11\n\tcreatedBy\x18  \x01(\t\x12\x13\n\x0b\x64\x65scription\x18! \x01(\t\x12\x0f\n\x07support\x18\" \x01(\x08\x12\x15\n\risParentGroup\x18# \x01(\x08\x12\x15\n\rparentGroupID\x18% \x01(\t\x12\x19\n\x11isDefaultSubgroup\x18$ \x01(\x08\x12\x13\n\x0b\x64isplayName\x18& \x01(\t\x12\r\n\x05pnJID\x18\' \x01(\t\x12\x12\n\nshareOwnPn\x18( \x01(\x08\x12\x1d\n\x15pnhDuplicateLidThread\x18) \x01(\x08\x12\x0e\n\x06lidJID\x18* \x01(\t\x12\x10\n\x08username\x18+ \x01(\t\x12\x15\n\rlidOriginType\x18, \x01(\t\x12\x15\n\rcommentsCount\x18- \x01(\r\x12\x0e\n\x06locked\x18. \x01(\x08\x12N\n\x15systemMessageToInsert\x18/ \x01(\x0e\x32/.WAWebProtobufsHistorySync.PrivacySystemMessage\x12\x18\n\x10\x63\x61piCreatedGroup\x18\x30 \x01(\x08\x12\x12\n\naccountLid\x18\x31 \x01(\t\x12\x14\n\x0climitSharing\x18\x32 \x01(\x08\x12$\n\x1climitSharingSettingTimestamp\x18\x33 \x01(\x03\x12;\n\x13limitSharingTrigger\x18\x34 \x01(\x0e\x32\x1e.WACommon.LimitSharing.Trigger\x12!\n\x19limitSharingInitiatedByMe\x18\x35 \x01(\x08\"\xbc\x01\n\x18\x45ndOfHistoryTransferType\x12\x30\n,COMPLETE_BUT_MORE_MESSAGES_REMAIN_ON_PRIMARY\x10\x00\x12\x32\n.COMPLETE_AND_NO_MORE_MESSAGE_REMAIN_ON_PRIMARY\x10\x01\x12:\n6COMPLETE_ON_DEMAND_SYNC_BUT_MORE_MSG_REMAIN_ON_PRIMARY\x10\x02\"\x93\x01\n\x10GroupParticipant\x12\x0f\n\x07userJID\x18\x01 \x02(\t\x12>\n\x04rank\x18\x02 \x01(\x0e\x32\x30.WAWebProtobufsHistorySync.GroupParticipant.Rank\".\n\x04Rank\x12\x0b\n\x07REGULAR\x10\x00\x12\t\n\x05\x41\x44MIN\x10\x01\x12\x0e\n\nSUPERADMIN\x10\x02\"\xa6\x01\n\x0fPastParticipant\x12\x0f\n\x07userJID\x18\x01 \x01(\t\x12K\n\x0bleaveReason\x18\x02 \x01(\x0e\x32\x36.WAWebProtobufsHistorySync.PastParticipant.LeaveReason\x12\x0f\n\x07leaveTS\x18\x03 \x01(\x04\"$\n\x0bLeaveReason\x12\x08\n\x04LEFT\x10\x00\x12\x0b\n\x07REMOVED\x10\x01\"8\n\x17PhoneNumberToLIDMapping\x12\r\n\x05pnJID\x18\x01 \x01(\t\x12\x0e\n\x06lidJID\x18\x02 \x01(\t\"X\n\x07\x41\x63\x63ount\x12\x0b\n\x03lid\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x13\n\x0b\x63ountryCode\x18\x03 \x01(\t\x12\x19\n\x11isUsernameDeleted\x18\x04 \x01(\x08\"X\n\x0eHistorySyncMsg\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32!.WAWebProtobufsWeb.WebMessageInfo\x12\x12\n\nmsgOrderID\x18\x02 \x01(\x04\"(\n\x08Pushname\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x10\n\x08pushname\x18\x02 \x01(\t\"6\n\x11WallpaperSettings\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0f\n\x07opacity\x18\x02 \x01(\r\"\xac\x08\n\x0eGlobalSettings\x12I\n\x13lightThemeWallpaper\x18\x01 \x01(\x0b\x32,.WAWebProtobufsHistorySync.WallpaperSettings\x12\x43\n\x0fmediaVisibility\x18\x02 \x01(\x0e\x32*.WAWebProtobufsHistorySync.MediaVisibility\x12H\n\x12\x64\x61rkThemeWallpaper\x18\x03 \x01(\x0b\x32,.WAWebProtobufsHistorySync.WallpaperSettings\x12I\n\x10\x61utoDownloadWiFi\x18\x04 \x01(\x0b\x32/.WAWebProtobufsHistorySync.AutoDownloadSettings\x12M\n\x14\x61utoDownloadCellular\x18\x05 \x01(\x0b\x32/.WAWebProtobufsHistorySync.AutoDownloadSettings\x12L\n\x13\x61utoDownloadRoaming\x18\x06 \x01(\x0b\x32/.WAWebProtobufsHistorySync.AutoDownloadSettings\x12*\n\"showIndividualNotificationsPreview\x18\x07 \x01(\x08\x12%\n\x1dshowGroupNotificationsPreview\x18\x08 \x01(\x08\x12 \n\x18\x64isappearingModeDuration\x18\t \x01(\x05\x12!\n\x19\x64isappearingModeTimestamp\x18\n \x01(\x03\x12I\n\x12\x61vatarUserSettings\x18\x0b \x01(\x0b\x32-.WAWebProtobufsHistorySync.AvatarUserSettings\x12\x10\n\x08\x66ontSize\x18\x0c \x01(\x05\x12\x1d\n\x15securityNotifications\x18\r \x01(\x08\x12\x1a\n\x12\x61utoUnarchiveChats\x18\x0e \x01(\x08\x12\x18\n\x10videoQualityMode\x18\x0f \x01(\x05\x12\x18\n\x10photoQualityMode\x18\x10 \x01(\x05\x12W\n\x1eindividualNotificationSettings\x18\x11 \x01(\x0b\x32/.WAWebProtobufsHistorySync.NotificationSettings\x12R\n\x19groupNotificationSettings\x18\x12 \x01(\x0b\x32/.WAWebProtobufsHistorySync.NotificationSettings\x12G\n\x10\x63hatLockSettings\x18\x13 \x01(\x0b\x32-.WAProtobufsChatLockSettings.ChatLockSettings\"w\n\x14\x41utoDownloadSettings\x12\x16\n\x0e\x64ownloadImages\x18\x01 \x01(\x08\x12\x15\n\rdownloadAudio\x18\x02 \x01(\x08\x12\x15\n\rdownloadVideo\x18\x03 \x01(\x08\x12\x19\n\x11\x64ownloadDocuments\x18\x04 \x01(\x08\"\xf1\x01\n\x0fStickerMetadata\x12\x0b\n\x03URL\x18\x01 \x01(\t\x12\x12\n\nfileSHA256\x18\x02 \x01(\x0c\x12\x15\n\rfileEncSHA256\x18\x03 \x01(\x0c\x12\x10\n\x08mediaKey\x18\x04 \x01(\x0c\x12\x10\n\x08mimetype\x18\x05 \x01(\t\x12\x0e\n\x06height\x18\x06 \x01(\r\x12\r\n\x05width\x18\x07 \x01(\r\x12\x12\n\ndirectPath\x18\x08 \x01(\t\x12\x12\n\nfileLength\x18\t \x01(\x04\x12\x0e\n\x06weight\x18\n \x01(\x02\x12\x19\n\x11lastStickerSentTS\x18\x0b \x01(\x03\x12\x10\n\x08isLottie\x18\x0c \x01(\x08\"j\n\x10PastParticipants\x12\x10\n\x08groupJID\x18\x01 \x01(\t\x12\x44\n\x10pastParticipants\x18\x02 \x03(\x0b\x32*.WAWebProtobufsHistorySync.PastParticipant\"4\n\x12\x41vatarUserSettings\x12\x0c\n\x04\x46\x42ID\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\xa9\x01\n\x14NotificationSettings\x12\x16\n\x0emessageVibrate\x18\x01 \x01(\t\x12\x14\n\x0cmessagePopup\x18\x02 \x01(\t\x12\x14\n\x0cmessageLight\x18\x03 \x01(\t\x12 \n\x18lowPriorityNotifications\x18\x04 \x01(\x08\x12\x16\n\x0ereactionsMuted\x18\x05 \x01(\x08\x12\x13\n\x0b\x63\x61llVibrate\x18\x06 \x01(\t*/\n\x0fMediaVisibility\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x06\n\x02ON\x10\x02*E\n\x14PrivacySystemMessage\x12\x0c\n\x08\x45\x32\x45\x45_MSG\x10\x01\x12\x0e\n\nNE2EE_SELF\x10\x02\x12\x0f\n\x0bNE2EE_OTHER\x10\x03\x42)Z\'go.mau.fi/whatsmeow/proto/waHistorySync')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waHistorySync.WAWebProtobufsHistorySync_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\'go.mau.fi/whatsmeow/proto/waHistorySync'
  _globals['_MEDIAVISIBILITY']._serialized_start=5582
  _globals['_MEDIAVISIBILITY']._serialized_end=5629
  _globals['_PRIVACYSYSTEMMESSAGE']._serialized_start=5631
  _globals['_PRIVACYSYSTEMMESSAGE']._serialized_end=5700
  _globals['_HISTORYSYNC']._serialized_start=251
  _globals['_HISTORYSYNC']._serialized_end=1373
  _globals['_HISTORYSYNC_BOTAIWAITLISTSTATE']._serialized_start=1177
  _globals['_HISTORYSYNC_BOTAIWAITLISTSTATE']._serialized_end=1232
  _globals['_HISTORYSYNC_HISTORYSYNCTYPE']._serialized_start=1235
  _globals['_HISTORYSYNC_HISTORYSYNCTYPE']._serialized_end=1373
  _globals['_CONVERSATION']._serialized_start=1376
  _globals['_CONVERSATION']._serialized_end=3155
  _globals['_CONVERSATION_ENDOFHISTORYTRANSFERTYPE']._serialized_start=2967
  _globals['_CONVERSATION_ENDOFHISTORYTRANSFERTYPE']._serialized_end=3155
  _globals['_GROUPPARTICIPANT']._serialized_start=3158
  _globals['_GROUPPARTICIPANT']._serialized_end=3305
  _globals['_GROUPPARTICIPANT_RANK']._serialized_start=3259
  _globals['_GROUPPARTICIPANT_RANK']._serialized_end=3305
  _globals['_PASTPARTICIPANT']._serialized_start=3308
  _globals['_PASTPARTICIPANT']._serialized_end=3474
  _globals['_PASTPARTICIPANT_LEAVEREASON']._serialized_start=3438
  _globals['_PASTPARTICIPANT_LEAVEREASON']._serialized_end=3474
  _globals['_PHONENUMBERTOLIDMAPPING']._serialized_start=3476
  _globals['_PHONENUMBERTOLIDMAPPING']._serialized_end=3532
  _globals['_ACCOUNT']._serialized_start=3534
  _globals['_ACCOUNT']._serialized_end=3622
  _globals['_HISTORYSYNCMSG']._serialized_start=3624
  _globals['_HISTORYSYNCMSG']._serialized_end=3712
  _globals['_PUSHNAME']._serialized_start=3714
  _globals['_PUSHNAME']._serialized_end=3754
  _globals['_WALLPAPERSETTINGS']._serialized_start=3756
  _globals['_WALLPAPERSETTINGS']._serialized_end=3810
  _globals['_GLOBALSETTINGS']._serialized_start=3813
  _globals['_GLOBALSETTINGS']._serialized_end=4881
  _globals['_AUTODOWNLOADSETTINGS']._serialized_start=4883
  _globals['_AUTODOWNLOADSETTINGS']._serialized_end=5002
  _globals['_STICKERMETADATA']._serialized_start=5005
  _globals['_STICKERMETADATA']._serialized_end=5246
  _globals['_PASTPARTICIPANTS']._serialized_start=5248
  _globals['_PASTPARTICIPANTS']._serialized_end=5354
  _globals['_AVATARUSERSETTINGS']._serialized_start=5356
  _globals['_AVATARUSERSETTINGS']._serialized_end=5408
  _globals['_NOTIFICATIONSETTINGS']._serialized_start=5411
  _globals['_NOTIFICATIONSETTINGS']._serialized_end=5580
# @@protoc_insertion_point(module_scope)

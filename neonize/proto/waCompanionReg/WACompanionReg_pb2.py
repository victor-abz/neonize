# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waCompanionReg/WACompanionReg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#waCompanionReg/WACompanionReg.proto\x12\x0eWACompanionReg\"\xb4\t\n\x0b\x44\x65viceProps\x12\n\n\x02os\x18\x01 \x01(\t\x12\x37\n\x07version\x18\x02 \x01(\x0b\x32&.WACompanionReg.DeviceProps.AppVersion\x12>\n\x0cplatformType\x18\x03 \x01(\x0e\x32(.WACompanionReg.DeviceProps.PlatformType\x12\x17\n\x0frequireFullSync\x18\x04 \x01(\x08\x12H\n\x11historySyncConfig\x18\x05 \x01(\x0b\x32-.WACompanionReg.DeviceProps.HistorySyncConfig\x1a\xf1\x03\n\x11HistorySyncConfig\x12\x19\n\x11\x66ullSyncDaysLimit\x18\x01 \x01(\r\x12\x1b\n\x13\x66ullSyncSizeMbLimit\x18\x02 \x01(\r\x12\x16\n\x0estorageQuotaMb\x18\x03 \x01(\r\x12%\n\x1dinlineInitialPayloadInE2EeMsg\x18\x04 \x01(\x08\x12\x1b\n\x13recentSyncDaysLimit\x18\x05 \x01(\r\x12\x1d\n\x15supportCallLogHistory\x18\x06 \x01(\x08\x12&\n\x1esupportBotUserAgentChatHistory\x18\x07 \x01(\x08\x12#\n\x1bsupportCagReactionsAndPolls\x18\x08 \x01(\x08\x12\x1b\n\x13supportBizHostedMsg\x18\t \x01(\x08\x12\x30\n(supportRecentSyncChunkMessageCountTuning\x18\n \x01(\x08\x12\x1d\n\x15supportHostedGroupMsg\x18\x0b \x01(\x08\x12!\n\x19supportFbidBotChatHistory\x18\x0c \x01(\x08\x12(\n supportAddOnHistorySyncMigration\x18\r \x01(\x08\x12!\n\x19supportMessageAssociation\x18\x0e \x01(\x08\x1ag\n\nAppVersion\x12\x0f\n\x07primary\x18\x01 \x01(\r\x12\x11\n\tsecondary\x18\x02 \x01(\r\x12\x10\n\x08tertiary\x18\x03 \x01(\r\x12\x12\n\nquaternary\x18\x04 \x01(\r\x12\x0f\n\x07quinary\x18\x05 \x01(\r\"\xdf\x02\n\x0cPlatformType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x43HROME\x10\x01\x12\x0b\n\x07\x46IREFOX\x10\x02\x12\x06\n\x02IE\x10\x03\x12\t\n\x05OPERA\x10\x04\x12\n\n\x06SAFARI\x10\x05\x12\x08\n\x04\x45\x44GE\x10\x06\x12\x0b\n\x07\x44\x45SKTOP\x10\x07\x12\x08\n\x04IPAD\x10\x08\x12\x12\n\x0e\x41NDROID_TABLET\x10\t\x12\t\n\x05OHANA\x10\n\x12\t\n\x05\x41LOHA\x10\x0b\x12\x0c\n\x08\x43\x41TALINA\x10\x0c\x12\n\n\x06TCL_TV\x10\r\x12\r\n\tIOS_PHONE\x10\x0e\x12\x10\n\x0cIOS_CATALYST\x10\x0f\x12\x11\n\rANDROID_PHONE\x10\x10\x12\x15\n\x11\x41NDROID_AMBIGUOUS\x10\x11\x12\x0b\n\x07WEAR_OS\x10\x12\x12\x0c\n\x08\x41R_WRIST\x10\x13\x12\r\n\tAR_DEVICE\x10\x14\x12\x07\n\x03UWP\x10\x15\x12\x06\n\x02VR\x10\x16\x12\r\n\tCLOUD_API\x10\x17\x12\x10\n\x0cSMARTGLASSES\x10\x18\"z\n\x1a\x43ompanionEphemeralIdentity\x12\x11\n\tpublicKey\x18\x01 \x01(\x0c\x12<\n\ndeviceType\x18\x02 \x01(\x0e\x32(.WACompanionReg.DeviceProps.PlatformType\x12\x0b\n\x03ref\x18\x03 \x01(\t\"#\n\x13\x43ompanionCommitment\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\"n\n\x0fProloguePayload\x12\"\n\x1a\x63ompanionEphemeralIdentity\x18\x01 \x01(\x0c\x12\x37\n\ncommitment\x18\x02 \x01(\x0b\x32#.WACompanionReg.CompanionCommitment\"<\n\x18PrimaryEphemeralIdentity\x12\x11\n\tpublicKey\x18\x01 \x01(\x0c\x12\r\n\x05nonce\x18\x02 \x01(\x0c\"]\n\x0ePairingRequest\x12\x1a\n\x12\x63ompanionPublicKey\x18\x01 \x01(\x0c\x12\x1c\n\x14\x63ompanionIdentityKey\x18\x02 \x01(\x0c\x12\x11\n\tadvSecret\x18\x03 \x01(\x0c\"?\n\x17\x45ncryptedPairingRequest\x12\x18\n\x10\x65ncryptedPayload\x18\x01 \x01(\x0c\x12\n\n\x02IV\x18\x02 \x01(\x0c\"P\n\x12\x43lientPairingProps\x12\x1b\n\x13isChatDbLidMigrated\x18\x01 \x01(\x08\x12\x1d\n\x15isSyncdPureLidSession\x18\x02 \x01(\x08\x42*Z(go.mau.fi/whatsmeow/proto/waCompanionReg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waCompanionReg.WACompanionReg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(go.mau.fi/whatsmeow/proto/waCompanionReg'
  _globals['_DEVICEPROPS']._serialized_start=56
  _globals['_DEVICEPROPS']._serialized_end=1260
  _globals['_DEVICEPROPS_HISTORYSYNCCONFIG']._serialized_start=304
  _globals['_DEVICEPROPS_HISTORYSYNCCONFIG']._serialized_end=801
  _globals['_DEVICEPROPS_APPVERSION']._serialized_start=803
  _globals['_DEVICEPROPS_APPVERSION']._serialized_end=906
  _globals['_DEVICEPROPS_PLATFORMTYPE']._serialized_start=909
  _globals['_DEVICEPROPS_PLATFORMTYPE']._serialized_end=1260
  _globals['_COMPANIONEPHEMERALIDENTITY']._serialized_start=1262
  _globals['_COMPANIONEPHEMERALIDENTITY']._serialized_end=1384
  _globals['_COMPANIONCOMMITMENT']._serialized_start=1386
  _globals['_COMPANIONCOMMITMENT']._serialized_end=1421
  _globals['_PROLOGUEPAYLOAD']._serialized_start=1423
  _globals['_PROLOGUEPAYLOAD']._serialized_end=1533
  _globals['_PRIMARYEPHEMERALIDENTITY']._serialized_start=1535
  _globals['_PRIMARYEPHEMERALIDENTITY']._serialized_end=1595
  _globals['_PAIRINGREQUEST']._serialized_start=1597
  _globals['_PAIRINGREQUEST']._serialized_end=1690
  _globals['_ENCRYPTEDPAIRINGREQUEST']._serialized_start=1692
  _globals['_ENCRYPTEDPAIRINGREQUEST']._serialized_end=1755
  _globals['_CLIENTPAIRINGPROPS']._serialized_start=1757
  _globals['_CLIENTPAIRINGPROPS']._serialized_end=1837
# @@protoc_insertion_point(module_scope)

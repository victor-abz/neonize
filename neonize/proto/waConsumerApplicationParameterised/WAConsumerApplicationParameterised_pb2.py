# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: waConsumerApplicationParameterised/WAConsumerApplicationParameterised.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'waConsumerApplicationParameterised/WAConsumerApplicationParameterised.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waCommonParameterised import WACommonParameterised_pb2 as waCommonParameterised_dot_WACommonParameterised__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKwaConsumerApplicationParameterised/WAConsumerApplicationParameterised.proto\x12\"WAConsumerApplicationParameterised\x1a\x31waCommonParameterised/WACommonParameterised.proto\"\xcc\x32\n\x13\x43onsumerApplication\x12P\n\x07payload\x18\x01 \x01(\x0b\x32?.WAConsumerApplicationParameterised.ConsumerApplication.Payload\x12R\n\x08metadata\x18\x02 \x01(\x0b\x32@.WAConsumerApplicationParameterised.ConsumerApplication.Metadata\x1a\x81\x03\n\x07Payload\x12R\n\x07\x63ontent\x18\x01 \x01(\x0b\x32?.WAConsumerApplicationParameterised.ConsumerApplication.ContentH\x00\x12\x62\n\x0f\x61pplicationData\x18\x02 \x01(\x0b\x32G.WAConsumerApplicationParameterised.ConsumerApplication.ApplicationDataH\x00\x12P\n\x06signal\x18\x03 \x01(\x0b\x32>.WAConsumerApplicationParameterised.ConsumerApplication.SignalH\x00\x12\x61\n\x0bsubProtocol\x18\x04 \x01(\x0b\x32J.WAConsumerApplicationParameterised.ConsumerApplication.SubProtocolPayloadH\x00\x42\t\n\x07payload\x1aU\n\x12SubProtocolPayload\x12?\n\x0b\x66utureProof\x18\x01 \x01(\x0e\x32*.WACommonParameterised.FutureProofBehavior\x1a\xaa\x01\n\x08Metadata\x12i\n\x0fspecialTextSize\x18\x01 \x01(\x0e\x32P.WAConsumerApplicationParameterised.ConsumerApplication.Metadata.SpecialTextSize\"3\n\x0fSpecialTextSize\x12\t\n\x05SMALL\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\t\n\x05LARGE\x10\x03\x1a\x08\n\x06Signal\x1a\x80\x01\n\x0f\x41pplicationData\x12W\n\x06revoke\x18\x01 \x01(\x0b\x32\x45.WAConsumerApplicationParameterised.ConsumerApplication.RevokeMessageH\x00\x42\x14\n\x12\x61pplicationContent\x1a\x84\x0e\n\x07\x43ontent\x12\x39\n\x0bmessageText\x18\x01 \x01(\x0b\x32\".WACommonParameterised.MessageTextH\x00\x12\\\n\x0cimageMessage\x18\x02 \x01(\x0b\x32\x44.WAConsumerApplicationParameterised.ConsumerApplication.ImageMessageH\x00\x12`\n\x0e\x63ontactMessage\x18\x03 \x01(\x0b\x32\x46.WAConsumerApplicationParameterised.ConsumerApplication.ContactMessageH\x00\x12\x62\n\x0flocationMessage\x18\x04 \x01(\x0b\x32G.WAConsumerApplicationParameterised.ConsumerApplication.LocationMessageH\x00\x12j\n\x13\x65xtendedTextMessage\x18\x05 \x01(\x0b\x32K.WAConsumerApplicationParameterised.ConsumerApplication.ExtendedTextMessageH\x00\x12\x65\n\x11statusTextMessage\x18\x06 \x01(\x0b\x32H.WAConsumerApplicationParameterised.ConsumerApplication.StatusTextMesageH\x00\x12\x62\n\x0f\x64ocumentMessage\x18\x07 \x01(\x0b\x32G.WAConsumerApplicationParameterised.ConsumerApplication.DocumentMessageH\x00\x12\\\n\x0c\x61udioMessage\x18\x08 \x01(\x0b\x32\x44.WAConsumerApplicationParameterised.ConsumerApplication.AudioMessageH\x00\x12\\\n\x0cvideoMessage\x18\t \x01(\x0b\x32\x44.WAConsumerApplicationParameterised.ConsumerApplication.VideoMessageH\x00\x12l\n\x14\x63ontactsArrayMessage\x18\n \x01(\x0b\x32L.WAConsumerApplicationParameterised.ConsumerApplication.ContactsArrayMessageH\x00\x12j\n\x13liveLocationMessage\x18\x0b \x01(\x0b\x32K.WAConsumerApplicationParameterised.ConsumerApplication.LiveLocationMessageH\x00\x12`\n\x0estickerMessage\x18\x0c \x01(\x0b\x32\x46.WAConsumerApplicationParameterised.ConsumerApplication.StickerMessageH\x00\x12h\n\x12groupInviteMessage\x18\r \x01(\x0b\x32J.WAConsumerApplicationParameterised.ConsumerApplication.GroupInviteMessageH\x00\x12\x62\n\x0fviewOnceMessage\x18\x0e \x01(\x0b\x32G.WAConsumerApplicationParameterised.ConsumerApplication.ViewOnceMessageH\x00\x12\x62\n\x0freactionMessage\x18\x10 \x01(\x0b\x32G.WAConsumerApplicationParameterised.ConsumerApplication.ReactionMessageH\x00\x12j\n\x13pollCreationMessage\x18\x11 \x01(\x0b\x32K.WAConsumerApplicationParameterised.ConsumerApplication.PollCreationMessageH\x00\x12\x66\n\x11pollUpdateMessage\x18\x12 \x01(\x0b\x32I.WAConsumerApplicationParameterised.ConsumerApplication.PollUpdateMessageH\x00\x12Z\n\x0b\x65\x64itMessage\x18\x13 \x01(\x0b\x32\x43.WAConsumerApplicationParameterised.ConsumerApplication.EditMessageH\x00\x42\t\n\x07\x63ontent\x1a\x87\x01\n\x0b\x45\x64itMessage\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.WACommonParameterised.MessageKey\x12\x33\n\x07message\x18\x02 \x01(\x0b\x32\".WACommonParameterised.MessageText\x12\x13\n\x0btimestampMS\x18\x03 \x01(\x03\x1aj\n\x14PollAddOptionMessage\x12R\n\npollOption\x18\x01 \x03(\x0b\x32>.WAConsumerApplicationParameterised.ConsumerApplication.Option\x1a\x45\n\x0fPollVoteMessage\x12\x17\n\x0fselectedOptions\x18\x01 \x03(\x0c\x12\x19\n\x11senderTimestampMS\x18\x02 \x01(\x03\x1a\x31\n\x0cPollEncValue\x12\x12\n\nencPayload\x18\x01 \x01(\x0c\x12\r\n\x05\x65ncIV\x18\x02 \x01(\x0c\x1a\x83\x02\n\x11PollUpdateMessage\x12\x41\n\x16pollCreationMessageKey\x18\x01 \x01(\x0b\x32!.WACommonParameterised.MessageKey\x12R\n\x04vote\x18\x02 \x01(\x0b\x32\x44.WAConsumerApplicationParameterised.ConsumerApplication.PollEncValue\x12W\n\taddOption\x18\x03 \x01(\x0b\x32\x44.WAConsumerApplicationParameterised.ConsumerApplication.PollEncValue\x1a\xa4\x01\n\x13PollCreationMessage\x12\x0e\n\x06\x65ncKey\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12O\n\x07options\x18\x03 \x03(\x0b\x32>.WAConsumerApplicationParameterised.ConsumerApplication.Option\x12\x1e\n\x16selectableOptionsCount\x18\x04 \x01(\r\x1a\x1c\n\x06Option\x12\x12\n\noptionName\x18\x01 \x01(\t\x1a\xb5\x01\n\x0fReactionMessage\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.WACommonParameterised.MessageKey\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x13\n\x0bgroupingKey\x18\x03 \x01(\t\x12\x19\n\x11senderTimestampMS\x18\x04 \x01(\x03\x12%\n\x1dreactionMetadataDataclassData\x18\x05 \x01(\t\x12\r\n\x05style\x18\x06 \x01(\x05\x1a?\n\rRevokeMessage\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.WACommonParameterised.MessageKey\x1a\xe0\x01\n\x0fViewOnceMessage\x12\\\n\x0cimageMessage\x18\x01 \x01(\x0b\x32\x44.WAConsumerApplicationParameterised.ConsumerApplication.ImageMessageH\x00\x12\\\n\x0cvideoMessage\x18\x02 \x01(\x0b\x32\x44.WAConsumerApplicationParameterised.ConsumerApplication.VideoMessageH\x00\x42\x11\n\x0fviewOnceContent\x1a\xb3\x01\n\x12GroupInviteMessage\x12\x10\n\x08groupJID\x18\x01 \x01(\t\x12\x12\n\ninviteCode\x18\x02 \x01(\t\x12\x18\n\x10inviteExpiration\x18\x03 \x01(\x03\x12\x11\n\tgroupName\x18\x04 \x01(\t\x12\x15\n\rJPEGThumbnail\x18\x05 \x01(\x0c\x12\x33\n\x07\x63\x61ption\x18\x06 \x01(\x0b\x32\".WACommonParameterised.MessageText\x1a\xa3\x02\n\x13LiveLocationMessage\x12R\n\x08location\x18\x01 \x01(\x0b\x32@.WAConsumerApplicationParameterised.ConsumerApplication.Location\x12\x18\n\x10\x61\x63\x63uracyInMeters\x18\x02 \x01(\r\x12\x12\n\nspeedInMps\x18\x03 \x01(\x02\x12)\n!degreesClockwiseFromMagneticNorth\x18\x04 \x01(\r\x12\x33\n\x07\x63\x61ption\x18\x05 \x01(\x0b\x32\".WACommonParameterised.MessageText\x12\x16\n\x0esequenceNumber\x18\x06 \x01(\x03\x12\x12\n\ntimeOffset\x18\x07 \x01(\r\x1a\x85\x01\n\x14\x43ontactsArrayMessage\x12\x13\n\x0b\x64isplayName\x18\x01 \x01(\t\x12X\n\x08\x63ontacts\x18\x02 \x03(\x0b\x32\x46.WAConsumerApplicationParameterised.ConsumerApplication.ContactMessage\x1a\x45\n\x0e\x43ontactMessage\x12\x33\n\x07\x63ontact\x18\x01 \x01(\x0b\x32\".WACommonParameterised.SubProtocol\x1a\xf0\x02\n\x10StatusTextMesage\x12Y\n\x04text\x18\x01 \x01(\x0b\x32K.WAConsumerApplicationParameterised.ConsumerApplication.ExtendedTextMessage\x12\x10\n\x08textArgb\x18\x06 \x01(\x07\x12\x16\n\x0e\x62\x61\x63kgroundArgb\x18\x07 \x01(\x07\x12_\n\x04\x66ont\x18\x08 \x01(\x0e\x32Q.WAConsumerApplicationParameterised.ConsumerApplication.StatusTextMesage.FontType\"v\n\x08\x46ontType\x12\x0e\n\nSANS_SERIF\x10\x00\x12\t\n\x05SERIF\x10\x01\x12\x13\n\x0fNORICAN_REGULAR\x10\x02\x12\x11\n\rBRYNDAN_WRITE\x10\x03\x12\x15\n\x11\x42\x45\x42\x41SNEUE_REGULAR\x10\x04\x12\x10\n\x0cOSWALD_HEAVY\x10\x05\x1a\xdf\x02\n\x13\x45xtendedTextMessage\x12\x30\n\x04text\x18\x01 \x01(\x0b\x32\".WACommonParameterised.MessageText\x12\x13\n\x0bmatchedText\x18\x02 \x01(\t\x12\x14\n\x0c\x63\x61nonicalURL\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12\x35\n\tthumbnail\x18\x06 \x01(\x0b\x32\".WACommonParameterised.SubProtocol\x12l\n\x0bpreviewType\x18\x07 \x01(\x0e\x32W.WAConsumerApplicationParameterised.ConsumerApplication.ExtendedTextMessage.PreviewType\"\"\n\x0bPreviewType\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05VIDEO\x10\x01\x1av\n\x0fLocationMessage\x12R\n\x08location\x18\x01 \x01(\x0b\x32@.WAConsumerApplicationParameterised.ConsumerApplication.Location\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x1a\x45\n\x0eStickerMessage\x12\x33\n\x07sticker\x18\x01 \x01(\x0b\x32\".WACommonParameterised.SubProtocol\x1aY\n\x0f\x44ocumentMessage\x12\x34\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\".WACommonParameterised.SubProtocol\x12\x10\n\x08\x66ileName\x18\x02 \x01(\t\x1av\n\x0cVideoMessage\x12\x31\n\x05video\x18\x01 \x01(\x0b\x32\".WACommonParameterised.SubProtocol\x12\x33\n\x07\x63\x61ption\x18\x02 \x01(\x0b\x32\".WACommonParameterised.MessageText\x1aN\n\x0c\x41udioMessage\x12\x31\n\x05\x61udio\x18\x01 \x01(\x0b\x32\".WACommonParameterised.SubProtocol\x12\x0b\n\x03PTT\x18\x02 \x01(\x08\x1av\n\x0cImageMessage\x12\x31\n\x05image\x18\x01 \x01(\x0b\x32\".WACommonParameterised.SubProtocol\x12\x33\n\x07\x63\x61ption\x18\x02 \x01(\x0b\x32\".WACommonParameterised.MessageText\x1a\xcf\x01\n\x15InteractiveAnnotation\x12T\n\x08location\x18\x02 \x01(\x0b\x32@.WAConsumerApplicationParameterised.ConsumerApplication.LocationH\x00\x12V\n\x0fpolygonVertices\x18\x01 \x03(\x0b\x32=.WAConsumerApplicationParameterised.ConsumerApplication.PointB\x08\n\x06\x61\x63tion\x1a\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x1aK\n\x08Location\x12\x17\n\x0f\x64\x65greesLatitude\x18\x01 \x01(\x01\x12\x18\n\x10\x64\x65greesLongitude\x18\x02 \x01(\x01\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a\x44\n\x0cMediaPayload\x12\x34\n\x08protocol\x18\x01 \x01(\x0b\x32\".WACommonParameterised.SubProtocolB>Z<go.mau.fi/whatsmeow/proto/waConsumerApplicationParameterised')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waConsumerApplicationParameterised.WAConsumerApplicationParameterised_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z<go.mau.fi/whatsmeow/proto/waConsumerApplicationParameterised'
  _globals['_CONSUMERAPPLICATION']._serialized_start=167
  _globals['_CONSUMERAPPLICATION']._serialized_end=6643
  _globals['_CONSUMERAPPLICATION_PAYLOAD']._serialized_start=357
  _globals['_CONSUMERAPPLICATION_PAYLOAD']._serialized_end=742
  _globals['_CONSUMERAPPLICATION_SUBPROTOCOLPAYLOAD']._serialized_start=744
  _globals['_CONSUMERAPPLICATION_SUBPROTOCOLPAYLOAD']._serialized_end=829
  _globals['_CONSUMERAPPLICATION_METADATA']._serialized_start=832
  _globals['_CONSUMERAPPLICATION_METADATA']._serialized_end=1002
  _globals['_CONSUMERAPPLICATION_METADATA_SPECIALTEXTSIZE']._serialized_start=951
  _globals['_CONSUMERAPPLICATION_METADATA_SPECIALTEXTSIZE']._serialized_end=1002
  _globals['_CONSUMERAPPLICATION_SIGNAL']._serialized_start=1004
  _globals['_CONSUMERAPPLICATION_SIGNAL']._serialized_end=1012
  _globals['_CONSUMERAPPLICATION_APPLICATIONDATA']._serialized_start=1015
  _globals['_CONSUMERAPPLICATION_APPLICATIONDATA']._serialized_end=1143
  _globals['_CONSUMERAPPLICATION_CONTENT']._serialized_start=1146
  _globals['_CONSUMERAPPLICATION_CONTENT']._serialized_end=2942
  _globals['_CONSUMERAPPLICATION_EDITMESSAGE']._serialized_start=2945
  _globals['_CONSUMERAPPLICATION_EDITMESSAGE']._serialized_end=3080
  _globals['_CONSUMERAPPLICATION_POLLADDOPTIONMESSAGE']._serialized_start=3082
  _globals['_CONSUMERAPPLICATION_POLLADDOPTIONMESSAGE']._serialized_end=3188
  _globals['_CONSUMERAPPLICATION_POLLVOTEMESSAGE']._serialized_start=3190
  _globals['_CONSUMERAPPLICATION_POLLVOTEMESSAGE']._serialized_end=3259
  _globals['_CONSUMERAPPLICATION_POLLENCVALUE']._serialized_start=3261
  _globals['_CONSUMERAPPLICATION_POLLENCVALUE']._serialized_end=3310
  _globals['_CONSUMERAPPLICATION_POLLUPDATEMESSAGE']._serialized_start=3313
  _globals['_CONSUMERAPPLICATION_POLLUPDATEMESSAGE']._serialized_end=3572
  _globals['_CONSUMERAPPLICATION_POLLCREATIONMESSAGE']._serialized_start=3575
  _globals['_CONSUMERAPPLICATION_POLLCREATIONMESSAGE']._serialized_end=3739
  _globals['_CONSUMERAPPLICATION_OPTION']._serialized_start=3741
  _globals['_CONSUMERAPPLICATION_OPTION']._serialized_end=3769
  _globals['_CONSUMERAPPLICATION_REACTIONMESSAGE']._serialized_start=3772
  _globals['_CONSUMERAPPLICATION_REACTIONMESSAGE']._serialized_end=3953
  _globals['_CONSUMERAPPLICATION_REVOKEMESSAGE']._serialized_start=3955
  _globals['_CONSUMERAPPLICATION_REVOKEMESSAGE']._serialized_end=4018
  _globals['_CONSUMERAPPLICATION_VIEWONCEMESSAGE']._serialized_start=4021
  _globals['_CONSUMERAPPLICATION_VIEWONCEMESSAGE']._serialized_end=4245
  _globals['_CONSUMERAPPLICATION_GROUPINVITEMESSAGE']._serialized_start=4248
  _globals['_CONSUMERAPPLICATION_GROUPINVITEMESSAGE']._serialized_end=4427
  _globals['_CONSUMERAPPLICATION_LIVELOCATIONMESSAGE']._serialized_start=4430
  _globals['_CONSUMERAPPLICATION_LIVELOCATIONMESSAGE']._serialized_end=4721
  _globals['_CONSUMERAPPLICATION_CONTACTSARRAYMESSAGE']._serialized_start=4724
  _globals['_CONSUMERAPPLICATION_CONTACTSARRAYMESSAGE']._serialized_end=4857
  _globals['_CONSUMERAPPLICATION_CONTACTMESSAGE']._serialized_start=4859
  _globals['_CONSUMERAPPLICATION_CONTACTMESSAGE']._serialized_end=4928
  _globals['_CONSUMERAPPLICATION_STATUSTEXTMESAGE']._serialized_start=4931
  _globals['_CONSUMERAPPLICATION_STATUSTEXTMESAGE']._serialized_end=5299
  _globals['_CONSUMERAPPLICATION_STATUSTEXTMESAGE_FONTTYPE']._serialized_start=5181
  _globals['_CONSUMERAPPLICATION_STATUSTEXTMESAGE_FONTTYPE']._serialized_end=5299
  _globals['_CONSUMERAPPLICATION_EXTENDEDTEXTMESSAGE']._serialized_start=5302
  _globals['_CONSUMERAPPLICATION_EXTENDEDTEXTMESSAGE']._serialized_end=5653
  _globals['_CONSUMERAPPLICATION_EXTENDEDTEXTMESSAGE_PREVIEWTYPE']._serialized_start=5619
  _globals['_CONSUMERAPPLICATION_EXTENDEDTEXTMESSAGE_PREVIEWTYPE']._serialized_end=5653
  _globals['_CONSUMERAPPLICATION_LOCATIONMESSAGE']._serialized_start=5655
  _globals['_CONSUMERAPPLICATION_LOCATIONMESSAGE']._serialized_end=5773
  _globals['_CONSUMERAPPLICATION_STICKERMESSAGE']._serialized_start=5775
  _globals['_CONSUMERAPPLICATION_STICKERMESSAGE']._serialized_end=5844
  _globals['_CONSUMERAPPLICATION_DOCUMENTMESSAGE']._serialized_start=5846
  _globals['_CONSUMERAPPLICATION_DOCUMENTMESSAGE']._serialized_end=5935
  _globals['_CONSUMERAPPLICATION_VIDEOMESSAGE']._serialized_start=5937
  _globals['_CONSUMERAPPLICATION_VIDEOMESSAGE']._serialized_end=6055
  _globals['_CONSUMERAPPLICATION_AUDIOMESSAGE']._serialized_start=6057
  _globals['_CONSUMERAPPLICATION_AUDIOMESSAGE']._serialized_end=6135
  _globals['_CONSUMERAPPLICATION_IMAGEMESSAGE']._serialized_start=6137
  _globals['_CONSUMERAPPLICATION_IMAGEMESSAGE']._serialized_end=6255
  _globals['_CONSUMERAPPLICATION_INTERACTIVEANNOTATION']._serialized_start=6258
  _globals['_CONSUMERAPPLICATION_INTERACTIVEANNOTATION']._serialized_end=6465
  _globals['_CONSUMERAPPLICATION_POINT']._serialized_start=6467
  _globals['_CONSUMERAPPLICATION_POINT']._serialized_end=6496
  _globals['_CONSUMERAPPLICATION_LOCATION']._serialized_start=6498
  _globals['_CONSUMERAPPLICATION_LOCATION']._serialized_end=6573
  _globals['_CONSUMERAPPLICATION_MEDIAPAYLOAD']._serialized_start=6575
  _globals['_CONSUMERAPPLICATION_MEDIAPAYLOAD']._serialized_end=6643
# @@protoc_insertion_point(module_scope)

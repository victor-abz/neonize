# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: waWa6/WAWebProtobufsWa6.proto
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
    'waWa6/WAWebProtobufsWa6.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dwaWa6/WAWebProtobufsWa6.proto\x12\x11WAWebProtobufsWa6\"\x82 \n\rClientPayload\x12\x10\n\x08username\x18\x01 \x01(\x04\x12\x0f\n\x07passive\x18\x03 \x01(\x08\x12=\n\tuserAgent\x18\x05 \x01(\x0b\x32*.WAWebProtobufsWa6.ClientPayload.UserAgent\x12\x39\n\x07webInfo\x18\x06 \x01(\x0b\x32(.WAWebProtobufsWa6.ClientPayload.WebInfo\x12\x10\n\x08pushName\x18\x07 \x01(\t\x12\x11\n\tsessionID\x18\t \x01(\x0f\x12\x14\n\x0cshortConnect\x18\n \x01(\x08\x12\x41\n\x0b\x63onnectType\x18\x0c \x01(\x0e\x32,.WAWebProtobufsWa6.ClientPayload.ConnectType\x12\x45\n\rconnectReason\x18\r \x01(\x0e\x32..WAWebProtobufsWa6.ClientPayload.ConnectReason\x12\x0e\n\x06shards\x18\x0e \x03(\x05\x12=\n\tdnsSource\x18\x0f \x01(\x0b\x32*.WAWebProtobufsWa6.ClientPayload.DNSSource\x12\x1b\n\x13\x63onnectAttemptCount\x18\x10 \x01(\r\x12\x0e\n\x06\x64\x65vice\x18\x12 \x01(\r\x12Y\n\x11\x64\x65vicePairingData\x18\x13 \x01(\x0b\x32>.WAWebProtobufsWa6.ClientPayload.DevicePairingRegistrationData\x12\x39\n\x07product\x18\x14 \x01(\x0e\x32(.WAWebProtobufsWa6.ClientPayload.Product\x12\r\n\x05\x66\x62\x43\x61t\x18\x15 \x01(\x0c\x12\x13\n\x0b\x66\x62UserAgent\x18\x16 \x01(\x0c\x12\n\n\x02oc\x18\x17 \x01(\x08\x12\n\n\x02lc\x18\x18 \x01(\x05\x12I\n\x0fiosAppExtension\x18\x1e \x01(\x0e\x32\x30.WAWebProtobufsWa6.ClientPayload.IOSAppExtension\x12\x0f\n\x07\x66\x62\x41ppID\x18\x1f \x01(\x04\x12\x12\n\nfbDeviceID\x18  \x01(\x0c\x12\x0c\n\x04pull\x18! \x01(\x08\x12\x14\n\x0cpaddingBytes\x18\" \x01(\x0c\x12\x11\n\tyearClass\x18$ \x01(\x05\x12\x10\n\x08memClass\x18% \x01(\x05\x12\x41\n\x0binteropData\x18& \x01(\x0b\x32,.WAWebProtobufsWa6.ClientPayload.InteropData\x12S\n\x14trafficAnonymization\x18( \x01(\x0e\x32\x35.WAWebProtobufsWa6.ClientPayload.TrafficAnonymization\x1a\xcb\x01\n\tDNSSource\x12Q\n\tdnsMethod\x18\x0f \x01(\x0e\x32>.WAWebProtobufsWa6.ClientPayload.DNSSource.DNSResolutionMethod\x12\x11\n\tappCached\x18\x10 \x01(\x08\"X\n\x13\x44NSResolutionMethod\x12\n\n\x06SYSTEM\x10\x00\x12\n\n\x06GOOGLE\x10\x01\x12\r\n\tHARDCODED\x10\x02\x12\x0c\n\x08OVERRIDE\x10\x03\x12\x0c\n\x08\x46\x41LLBACK\x10\x04\x1a\xde\x04\n\x07WebInfo\x12\x10\n\x08refToken\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12I\n\x0bwebdPayload\x18\x03 \x01(\x0b\x32\x34.WAWebProtobufsWa6.ClientPayload.WebInfo.WebdPayload\x12O\n\x0ewebSubPlatform\x18\x04 \x01(\x0e\x32\x37.WAWebProtobufsWa6.ClientPayload.WebInfo.WebSubPlatform\x1a\xbb\x02\n\x0bWebdPayload\x12\x1c\n\x14usesParticipantInKey\x18\x01 \x01(\x08\x12\x1f\n\x17supportsStarredMessages\x18\x02 \x01(\x08\x12 \n\x18supportsDocumentMessages\x18\x03 \x01(\x08\x12\x1b\n\x13supportsURLMessages\x18\x04 \x01(\x08\x12\x1a\n\x12supportsMediaRetry\x18\x05 \x01(\x08\x12\x18\n\x10supportsE2EImage\x18\x06 \x01(\x08\x12\x18\n\x10supportsE2EVideo\x18\x07 \x01(\x08\x12\x18\n\x10supportsE2EAudio\x18\x08 \x01(\x08\x12\x1b\n\x13supportsE2EDocument\x18\t \x01(\x08\x12\x15\n\rdocumentTypes\x18\n \x01(\t\x12\x10\n\x08\x66\x65\x61tures\x18\x0b \x01(\x0c\"V\n\x0eWebSubPlatform\x12\x0f\n\x0bWEB_BROWSER\x10\x00\x12\r\n\tAPP_STORE\x10\x01\x12\r\n\tWIN_STORE\x10\x02\x12\n\n\x06\x44\x41RWIN\x10\x03\x12\t\n\x05WIN32\x10\x04\x1a\xba\n\n\tUserAgent\x12\x45\n\x08platform\x18\x01 \x01(\x0e\x32\x33.WAWebProtobufsWa6.ClientPayload.UserAgent.Platform\x12I\n\nappVersion\x18\x02 \x01(\x0b\x32\x35.WAWebProtobufsWa6.ClientPayload.UserAgent.AppVersion\x12\x0b\n\x03mcc\x18\x03 \x01(\t\x12\x0b\n\x03mnc\x18\x04 \x01(\t\x12\x11\n\tosVersion\x18\x05 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x06 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x07 \x01(\t\x12\x15\n\rosBuildNumber\x18\x08 \x01(\t\x12\x0f\n\x07phoneID\x18\t \x01(\t\x12Q\n\x0ereleaseChannel\x18\n \x01(\x0e\x32\x39.WAWebProtobufsWa6.ClientPayload.UserAgent.ReleaseChannel\x12\x1d\n\x15localeLanguageIso6391\x18\x0b \x01(\t\x12#\n\x1blocaleCountryIso31661Alpha2\x18\x0c \x01(\t\x12\x13\n\x0b\x64\x65viceBoard\x18\r \x01(\t\x12\x13\n\x0b\x64\x65viceExpID\x18\x0e \x01(\t\x12I\n\ndeviceType\x18\x0f \x01(\x0e\x32\x35.WAWebProtobufsWa6.ClientPayload.UserAgent.DeviceType\x12\x17\n\x0f\x64\x65viceModelType\x18\x10 \x01(\t\x1ag\n\nAppVersion\x12\x0f\n\x07primary\x18\x01 \x01(\r\x12\x11\n\tsecondary\x18\x02 \x01(\r\x12\x10\n\x08tertiary\x18\x03 \x01(\r\x12\x12\n\nquaternary\x18\x04 \x01(\r\x12\x0f\n\x07quinary\x18\x05 \x01(\r\"F\n\nDeviceType\x12\t\n\x05PHONE\x10\x00\x12\n\n\x06TABLET\x10\x01\x12\x0b\n\x07\x44\x45SKTOP\x10\x02\x12\x0c\n\x08WEARABLE\x10\x03\x12\x06\n\x02VR\x10\x04\"=\n\x0eReleaseChannel\x12\x0b\n\x07RELEASE\x10\x00\x12\x08\n\x04\x42\x45TA\x10\x01\x12\t\n\x05\x41LPHA\x10\x02\x12\t\n\x05\x44\x45\x42UG\x10\x03\"\x8a\x04\n\x08Platform\x12\x0b\n\x07\x41NDROID\x10\x00\x12\x07\n\x03IOS\x10\x01\x12\x11\n\rWINDOWS_PHONE\x10\x02\x12\x0e\n\nBLACKBERRY\x10\x03\x12\x0f\n\x0b\x42LACKBERRYX\x10\x04\x12\x07\n\x03S40\x10\x05\x12\x07\n\x03S60\x10\x06\x12\x11\n\rPYTHON_CLIENT\x10\x07\x12\t\n\x05TIZEN\x10\x08\x12\x0e\n\nENTERPRISE\x10\t\x12\x0f\n\x0bSMB_ANDROID\x10\n\x12\t\n\x05KAIOS\x10\x0b\x12\x0b\n\x07SMB_IOS\x10\x0c\x12\x0b\n\x07WINDOWS\x10\r\x12\x07\n\x03WEB\x10\x0e\x12\n\n\x06PORTAL\x10\x0f\x12\x11\n\rGREEN_ANDROID\x10\x10\x12\x10\n\x0cGREEN_IPHONE\x10\x11\x12\x10\n\x0c\x42LUE_ANDROID\x10\x12\x12\x0f\n\x0b\x42LUE_IPHONE\x10\x13\x12\x12\n\x0e\x46\x42LITE_ANDROID\x10\x14\x12\x11\n\rMLITE_ANDROID\x10\x15\x12\x12\n\x0eIGLITE_ANDROID\x10\x16\x12\x08\n\x04PAGE\x10\x17\x12\t\n\x05MACOS\x10\x18\x12\x0e\n\nOCULUS_MSG\x10\x19\x12\x0f\n\x0bOCULUS_CALL\x10\x1a\x12\t\n\x05MILAN\x10\x1b\x12\x08\n\x04\x43\x41PI\x10\x1c\x12\n\n\x06WEAROS\x10\x1d\x12\x0c\n\x08\x41RDEVICE\x10\x1e\x12\x0c\n\x08VRDEVICE\x10\x1f\x12\x0c\n\x08\x42LUE_WEB\x10 \x12\x08\n\x04IPAD\x10!\x12\x08\n\x04TEST\x10\"\x12\x11\n\rSMART_GLASSES\x10#\x1aK\n\x0bInteropData\x12\x11\n\taccountID\x18\x01 \x01(\x04\x12\r\n\x05token\x18\x02 \x01(\x0c\x12\x1a\n\x12\x65nableReadReceipts\x18\x03 \x01(\x08\x1a\xae\x01\n\x1d\x44\x65vicePairingRegistrationData\x12\x0e\n\x06\x65Regid\x18\x01 \x01(\x0c\x12\x10\n\x08\x65Keytype\x18\x02 \x01(\x0c\x12\x0e\n\x06\x65Ident\x18\x03 \x01(\x0c\x12\x0f\n\x07\x65SkeyID\x18\x04 \x01(\x0c\x12\x10\n\x08\x65SkeyVal\x18\x05 \x01(\x0c\x12\x10\n\x08\x65SkeySig\x18\x06 \x01(\x0c\x12\x11\n\tbuildHash\x18\x07 \x01(\x0c\x12\x13\n\x0b\x64\x65viceProps\x18\x08 \x01(\x0c\"-\n\x14TrafficAnonymization\x12\x07\n\x03OFF\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\"E\n\x07Product\x12\x0c\n\x08WHATSAPP\x10\x00\x12\r\n\tMESSENGER\x10\x01\x12\x0b\n\x07INTEROP\x10\x02\x12\x10\n\x0cINTEROP_MSGR\x10\x03\"\xb0\x02\n\x0b\x43onnectType\x12\x14\n\x10\x43\x45LLULAR_UNKNOWN\x10\x00\x12\x10\n\x0cWIFI_UNKNOWN\x10\x01\x12\x11\n\rCELLULAR_EDGE\x10\x64\x12\x11\n\rCELLULAR_IDEN\x10\x65\x12\x11\n\rCELLULAR_UMTS\x10\x66\x12\x11\n\rCELLULAR_EVDO\x10g\x12\x11\n\rCELLULAR_GPRS\x10h\x12\x12\n\x0e\x43\x45LLULAR_HSDPA\x10i\x12\x12\n\x0e\x43\x45LLULAR_HSUPA\x10j\x12\x11\n\rCELLULAR_HSPA\x10k\x12\x11\n\rCELLULAR_CDMA\x10l\x12\x12\n\x0e\x43\x45LLULAR_1XRTT\x10m\x12\x12\n\x0e\x43\x45LLULAR_EHRPD\x10n\x12\x10\n\x0c\x43\x45LLULAR_LTE\x10o\x12\x12\n\x0e\x43\x45LLULAR_HSPAP\x10p\"\x86\x01\n\rConnectReason\x12\x08\n\x04PUSH\x10\x00\x12\x12\n\x0eUSER_ACTIVATED\x10\x01\x12\r\n\tSCHEDULED\x10\x02\x12\x13\n\x0f\x45RROR_RECONNECT\x10\x03\x12\x12\n\x0eNETWORK_SWITCH\x10\x04\x12\x12\n\x0ePING_RECONNECT\x10\x05\x12\x0b\n\x07UNKNOWN\x10\x06\"T\n\x0fIOSAppExtension\x12\x13\n\x0fSHARE_EXTENSION\x10\x00\x12\x15\n\x11SERVICE_EXTENSION\x10\x01\x12\x15\n\x11INTENTS_EXTENSION\x10\x02\"\x9d\x03\n\x10HandshakeMessage\x12\x44\n\x0b\x63lientHello\x18\x02 \x01(\x0b\x32/.WAWebProtobufsWa6.HandshakeMessage.ClientHello\x12\x44\n\x0bserverHello\x18\x03 \x01(\x0b\x32/.WAWebProtobufsWa6.HandshakeMessage.ServerHello\x12\x46\n\x0c\x63lientFinish\x18\x04 \x01(\x0b\x32\x30.WAWebProtobufsWa6.HandshakeMessage.ClientFinish\x1a/\n\x0c\x43lientFinish\x12\x0e\n\x06static\x18\x01 \x01(\x0c\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x1a\x41\n\x0bServerHello\x12\x11\n\tephemeral\x18\x01 \x01(\x0c\x12\x0e\n\x06static\x18\x02 \x01(\x0c\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x1a\x41\n\x0b\x43lientHello\x12\x11\n\tephemeral\x18\x01 \x01(\x0c\x12\x0e\n\x06static\x18\x02 \x01(\x0c\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x42!Z\x1fgo.mau.fi/whatsmeow/proto/waWa6')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waWa6.WAWebProtobufsWa6_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\037go.mau.fi/whatsmeow/proto/waWa6'
  _globals['_CLIENTPAYLOAD']._serialized_start=53
  _globals['_CLIENTPAYLOAD']._serialized_end=4151
  _globals['_CLIENTPAYLOAD_DNSSOURCE']._serialized_start=1096
  _globals['_CLIENTPAYLOAD_DNSSOURCE']._serialized_end=1299
  _globals['_CLIENTPAYLOAD_DNSSOURCE_DNSRESOLUTIONMETHOD']._serialized_start=1211
  _globals['_CLIENTPAYLOAD_DNSSOURCE_DNSRESOLUTIONMETHOD']._serialized_end=1299
  _globals['_CLIENTPAYLOAD_WEBINFO']._serialized_start=1302
  _globals['_CLIENTPAYLOAD_WEBINFO']._serialized_end=1908
  _globals['_CLIENTPAYLOAD_WEBINFO_WEBDPAYLOAD']._serialized_start=1505
  _globals['_CLIENTPAYLOAD_WEBINFO_WEBDPAYLOAD']._serialized_end=1820
  _globals['_CLIENTPAYLOAD_WEBINFO_WEBSUBPLATFORM']._serialized_start=1822
  _globals['_CLIENTPAYLOAD_WEBINFO_WEBSUBPLATFORM']._serialized_end=1908
  _globals['_CLIENTPAYLOAD_USERAGENT']._serialized_start=1911
  _globals['_CLIENTPAYLOAD_USERAGENT']._serialized_end=3249
  _globals['_CLIENTPAYLOAD_USERAGENT_APPVERSION']._serialized_start=2486
  _globals['_CLIENTPAYLOAD_USERAGENT_APPVERSION']._serialized_end=2589
  _globals['_CLIENTPAYLOAD_USERAGENT_DEVICETYPE']._serialized_start=2591
  _globals['_CLIENTPAYLOAD_USERAGENT_DEVICETYPE']._serialized_end=2661
  _globals['_CLIENTPAYLOAD_USERAGENT_RELEASECHANNEL']._serialized_start=2663
  _globals['_CLIENTPAYLOAD_USERAGENT_RELEASECHANNEL']._serialized_end=2724
  _globals['_CLIENTPAYLOAD_USERAGENT_PLATFORM']._serialized_start=2727
  _globals['_CLIENTPAYLOAD_USERAGENT_PLATFORM']._serialized_end=3249
  _globals['_CLIENTPAYLOAD_INTEROPDATA']._serialized_start=3251
  _globals['_CLIENTPAYLOAD_INTEROPDATA']._serialized_end=3326
  _globals['_CLIENTPAYLOAD_DEVICEPAIRINGREGISTRATIONDATA']._serialized_start=3329
  _globals['_CLIENTPAYLOAD_DEVICEPAIRINGREGISTRATIONDATA']._serialized_end=3503
  _globals['_CLIENTPAYLOAD_TRAFFICANONYMIZATION']._serialized_start=3505
  _globals['_CLIENTPAYLOAD_TRAFFICANONYMIZATION']._serialized_end=3550
  _globals['_CLIENTPAYLOAD_PRODUCT']._serialized_start=3552
  _globals['_CLIENTPAYLOAD_PRODUCT']._serialized_end=3621
  _globals['_CLIENTPAYLOAD_CONNECTTYPE']._serialized_start=3624
  _globals['_CLIENTPAYLOAD_CONNECTTYPE']._serialized_end=3928
  _globals['_CLIENTPAYLOAD_CONNECTREASON']._serialized_start=3931
  _globals['_CLIENTPAYLOAD_CONNECTREASON']._serialized_end=4065
  _globals['_CLIENTPAYLOAD_IOSAPPEXTENSION']._serialized_start=4067
  _globals['_CLIENTPAYLOAD_IOSAPPEXTENSION']._serialized_end=4151
  _globals['_HANDSHAKEMESSAGE']._serialized_start=4154
  _globals['_HANDSHAKEMESSAGE']._serialized_end=4567
  _globals['_HANDSHAKEMESSAGE_CLIENTFINISH']._serialized_start=4386
  _globals['_HANDSHAKEMESSAGE_CLIENTFINISH']._serialized_end=4433
  _globals['_HANDSHAKEMESSAGE_SERVERHELLO']._serialized_start=4435
  _globals['_HANDSHAKEMESSAGE_SERVERHELLO']._serialized_end=4500
  _globals['_HANDSHAKEMESSAGE_CLIENTHELLO']._serialized_start=4502
  _globals['_HANDSHAKEMESSAGE_CLIENTHELLO']._serialized_end=4567
# @@protoc_insertion_point(module_scope)

"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class DeviceProps(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _PlatformType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _PlatformTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeviceProps._PlatformType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: DeviceProps._PlatformType.ValueType  # 0
        CHROME: DeviceProps._PlatformType.ValueType  # 1
        FIREFOX: DeviceProps._PlatformType.ValueType  # 2
        IE: DeviceProps._PlatformType.ValueType  # 3
        OPERA: DeviceProps._PlatformType.ValueType  # 4
        SAFARI: DeviceProps._PlatformType.ValueType  # 5
        EDGE: DeviceProps._PlatformType.ValueType  # 6
        DESKTOP: DeviceProps._PlatformType.ValueType  # 7
        IPAD: DeviceProps._PlatformType.ValueType  # 8
        ANDROID_TABLET: DeviceProps._PlatformType.ValueType  # 9
        OHANA: DeviceProps._PlatformType.ValueType  # 10
        ALOHA: DeviceProps._PlatformType.ValueType  # 11
        CATALINA: DeviceProps._PlatformType.ValueType  # 12
        TCL_TV: DeviceProps._PlatformType.ValueType  # 13
        IOS_PHONE: DeviceProps._PlatformType.ValueType  # 14
        IOS_CATALYST: DeviceProps._PlatformType.ValueType  # 15
        ANDROID_PHONE: DeviceProps._PlatformType.ValueType  # 16
        ANDROID_AMBIGUOUS: DeviceProps._PlatformType.ValueType  # 17
        WEAR_OS: DeviceProps._PlatformType.ValueType  # 18
        AR_WRIST: DeviceProps._PlatformType.ValueType  # 19
        AR_DEVICE: DeviceProps._PlatformType.ValueType  # 20
        UWP: DeviceProps._PlatformType.ValueType  # 21
        VR: DeviceProps._PlatformType.ValueType  # 22
        CLOUD_API: DeviceProps._PlatformType.ValueType  # 23
        SMARTGLASSES: DeviceProps._PlatformType.ValueType  # 24

    class PlatformType(_PlatformType, metaclass=_PlatformTypeEnumTypeWrapper): ...
    UNKNOWN: DeviceProps.PlatformType.ValueType  # 0
    CHROME: DeviceProps.PlatformType.ValueType  # 1
    FIREFOX: DeviceProps.PlatformType.ValueType  # 2
    IE: DeviceProps.PlatformType.ValueType  # 3
    OPERA: DeviceProps.PlatformType.ValueType  # 4
    SAFARI: DeviceProps.PlatformType.ValueType  # 5
    EDGE: DeviceProps.PlatformType.ValueType  # 6
    DESKTOP: DeviceProps.PlatformType.ValueType  # 7
    IPAD: DeviceProps.PlatformType.ValueType  # 8
    ANDROID_TABLET: DeviceProps.PlatformType.ValueType  # 9
    OHANA: DeviceProps.PlatformType.ValueType  # 10
    ALOHA: DeviceProps.PlatformType.ValueType  # 11
    CATALINA: DeviceProps.PlatformType.ValueType  # 12
    TCL_TV: DeviceProps.PlatformType.ValueType  # 13
    IOS_PHONE: DeviceProps.PlatformType.ValueType  # 14
    IOS_CATALYST: DeviceProps.PlatformType.ValueType  # 15
    ANDROID_PHONE: DeviceProps.PlatformType.ValueType  # 16
    ANDROID_AMBIGUOUS: DeviceProps.PlatformType.ValueType  # 17
    WEAR_OS: DeviceProps.PlatformType.ValueType  # 18
    AR_WRIST: DeviceProps.PlatformType.ValueType  # 19
    AR_DEVICE: DeviceProps.PlatformType.ValueType  # 20
    UWP: DeviceProps.PlatformType.ValueType  # 21
    VR: DeviceProps.PlatformType.ValueType  # 22
    CLOUD_API: DeviceProps.PlatformType.ValueType  # 23
    SMARTGLASSES: DeviceProps.PlatformType.ValueType  # 24

    @typing.final
    class HistorySyncConfig(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FULLSYNCDAYSLIMIT_FIELD_NUMBER: builtins.int
        FULLSYNCSIZEMBLIMIT_FIELD_NUMBER: builtins.int
        STORAGEQUOTAMB_FIELD_NUMBER: builtins.int
        INLINEINITIALPAYLOADINE2EEMSG_FIELD_NUMBER: builtins.int
        RECENTSYNCDAYSLIMIT_FIELD_NUMBER: builtins.int
        SUPPORTCALLLOGHISTORY_FIELD_NUMBER: builtins.int
        SUPPORTBOTUSERAGENTCHATHISTORY_FIELD_NUMBER: builtins.int
        SUPPORTCAGREACTIONSANDPOLLS_FIELD_NUMBER: builtins.int
        SUPPORTBIZHOSTEDMSG_FIELD_NUMBER: builtins.int
        SUPPORTRECENTSYNCCHUNKMESSAGECOUNTTUNING_FIELD_NUMBER: builtins.int
        SUPPORTHOSTEDGROUPMSG_FIELD_NUMBER: builtins.int
        SUPPORTFBIDBOTCHATHISTORY_FIELD_NUMBER: builtins.int
        SUPPORTADDONHISTORYSYNCMIGRATION_FIELD_NUMBER: builtins.int
        SUPPORTMESSAGEASSOCIATION_FIELD_NUMBER: builtins.int
        fullSyncDaysLimit: builtins.int
        fullSyncSizeMbLimit: builtins.int
        storageQuotaMb: builtins.int
        inlineInitialPayloadInE2EeMsg: builtins.bool
        recentSyncDaysLimit: builtins.int
        supportCallLogHistory: builtins.bool
        supportBotUserAgentChatHistory: builtins.bool
        supportCagReactionsAndPolls: builtins.bool
        supportBizHostedMsg: builtins.bool
        supportRecentSyncChunkMessageCountTuning: builtins.bool
        supportHostedGroupMsg: builtins.bool
        supportFbidBotChatHistory: builtins.bool
        supportAddOnHistorySyncMigration: builtins.bool
        supportMessageAssociation: builtins.bool
        def __init__(
            self,
            *,
            fullSyncDaysLimit: builtins.int | None = ...,
            fullSyncSizeMbLimit: builtins.int | None = ...,
            storageQuotaMb: builtins.int | None = ...,
            inlineInitialPayloadInE2EeMsg: builtins.bool | None = ...,
            recentSyncDaysLimit: builtins.int | None = ...,
            supportCallLogHistory: builtins.bool | None = ...,
            supportBotUserAgentChatHistory: builtins.bool | None = ...,
            supportCagReactionsAndPolls: builtins.bool | None = ...,
            supportBizHostedMsg: builtins.bool | None = ...,
            supportRecentSyncChunkMessageCountTuning: builtins.bool | None = ...,
            supportHostedGroupMsg: builtins.bool | None = ...,
            supportFbidBotChatHistory: builtins.bool | None = ...,
            supportAddOnHistorySyncMigration: builtins.bool | None = ...,
            supportMessageAssociation: builtins.bool | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["fullSyncDaysLimit", b"fullSyncDaysLimit", "fullSyncSizeMbLimit", b"fullSyncSizeMbLimit", "inlineInitialPayloadInE2EeMsg", b"inlineInitialPayloadInE2EeMsg", "recentSyncDaysLimit", b"recentSyncDaysLimit", "storageQuotaMb", b"storageQuotaMb", "supportAddOnHistorySyncMigration", b"supportAddOnHistorySyncMigration", "supportBizHostedMsg", b"supportBizHostedMsg", "supportBotUserAgentChatHistory", b"supportBotUserAgentChatHistory", "supportCagReactionsAndPolls", b"supportCagReactionsAndPolls", "supportCallLogHistory", b"supportCallLogHistory", "supportFbidBotChatHistory", b"supportFbidBotChatHistory", "supportHostedGroupMsg", b"supportHostedGroupMsg", "supportMessageAssociation", b"supportMessageAssociation", "supportRecentSyncChunkMessageCountTuning", b"supportRecentSyncChunkMessageCountTuning"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["fullSyncDaysLimit", b"fullSyncDaysLimit", "fullSyncSizeMbLimit", b"fullSyncSizeMbLimit", "inlineInitialPayloadInE2EeMsg", b"inlineInitialPayloadInE2EeMsg", "recentSyncDaysLimit", b"recentSyncDaysLimit", "storageQuotaMb", b"storageQuotaMb", "supportAddOnHistorySyncMigration", b"supportAddOnHistorySyncMigration", "supportBizHostedMsg", b"supportBizHostedMsg", "supportBotUserAgentChatHistory", b"supportBotUserAgentChatHistory", "supportCagReactionsAndPolls", b"supportCagReactionsAndPolls", "supportCallLogHistory", b"supportCallLogHistory", "supportFbidBotChatHistory", b"supportFbidBotChatHistory", "supportHostedGroupMsg", b"supportHostedGroupMsg", "supportMessageAssociation", b"supportMessageAssociation", "supportRecentSyncChunkMessageCountTuning", b"supportRecentSyncChunkMessageCountTuning"]) -> None: ...

    @typing.final
    class AppVersion(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PRIMARY_FIELD_NUMBER: builtins.int
        SECONDARY_FIELD_NUMBER: builtins.int
        TERTIARY_FIELD_NUMBER: builtins.int
        QUATERNARY_FIELD_NUMBER: builtins.int
        QUINARY_FIELD_NUMBER: builtins.int
        primary: builtins.int
        secondary: builtins.int
        tertiary: builtins.int
        quaternary: builtins.int
        quinary: builtins.int
        def __init__(
            self,
            *,
            primary: builtins.int | None = ...,
            secondary: builtins.int | None = ...,
            tertiary: builtins.int | None = ...,
            quaternary: builtins.int | None = ...,
            quinary: builtins.int | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["primary", b"primary", "quaternary", b"quaternary", "quinary", b"quinary", "secondary", b"secondary", "tertiary", b"tertiary"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["primary", b"primary", "quaternary", b"quaternary", "quinary", b"quinary", "secondary", b"secondary", "tertiary", b"tertiary"]) -> None: ...

    OS_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    PLATFORMTYPE_FIELD_NUMBER: builtins.int
    REQUIREFULLSYNC_FIELD_NUMBER: builtins.int
    HISTORYSYNCCONFIG_FIELD_NUMBER: builtins.int
    os: builtins.str
    platformType: global___DeviceProps.PlatformType.ValueType
    requireFullSync: builtins.bool
    @property
    def version(self) -> global___DeviceProps.AppVersion: ...
    @property
    def historySyncConfig(self) -> global___DeviceProps.HistorySyncConfig: ...
    def __init__(
        self,
        *,
        os: builtins.str | None = ...,
        version: global___DeviceProps.AppVersion | None = ...,
        platformType: global___DeviceProps.PlatformType.ValueType | None = ...,
        requireFullSync: builtins.bool | None = ...,
        historySyncConfig: global___DeviceProps.HistorySyncConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["historySyncConfig", b"historySyncConfig", "os", b"os", "platformType", b"platformType", "requireFullSync", b"requireFullSync", "version", b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["historySyncConfig", b"historySyncConfig", "os", b"os", "platformType", b"platformType", "requireFullSync", b"requireFullSync", "version", b"version"]) -> None: ...

global___DeviceProps = DeviceProps

@typing.final
class CompanionEphemeralIdentity(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PUBLICKEY_FIELD_NUMBER: builtins.int
    DEVICETYPE_FIELD_NUMBER: builtins.int
    REF_FIELD_NUMBER: builtins.int
    publicKey: builtins.bytes
    deviceType: global___DeviceProps.PlatformType.ValueType
    ref: builtins.str
    def __init__(
        self,
        *,
        publicKey: builtins.bytes | None = ...,
        deviceType: global___DeviceProps.PlatformType.ValueType | None = ...,
        ref: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["deviceType", b"deviceType", "publicKey", b"publicKey", "ref", b"ref"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["deviceType", b"deviceType", "publicKey", b"publicKey", "ref", b"ref"]) -> None: ...

global___CompanionEphemeralIdentity = CompanionEphemeralIdentity

@typing.final
class CompanionCommitment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HASH_FIELD_NUMBER: builtins.int
    hash: builtins.bytes
    def __init__(
        self,
        *,
        hash: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["hash", b"hash"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["hash", b"hash"]) -> None: ...

global___CompanionCommitment = CompanionCommitment

@typing.final
class ProloguePayload(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMPANIONEPHEMERALIDENTITY_FIELD_NUMBER: builtins.int
    COMMITMENT_FIELD_NUMBER: builtins.int
    companionEphemeralIdentity: builtins.bytes
    @property
    def commitment(self) -> global___CompanionCommitment: ...
    def __init__(
        self,
        *,
        companionEphemeralIdentity: builtins.bytes | None = ...,
        commitment: global___CompanionCommitment | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["commitment", b"commitment", "companionEphemeralIdentity", b"companionEphemeralIdentity"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["commitment", b"commitment", "companionEphemeralIdentity", b"companionEphemeralIdentity"]) -> None: ...

global___ProloguePayload = ProloguePayload

@typing.final
class PrimaryEphemeralIdentity(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PUBLICKEY_FIELD_NUMBER: builtins.int
    NONCE_FIELD_NUMBER: builtins.int
    publicKey: builtins.bytes
    nonce: builtins.bytes
    def __init__(
        self,
        *,
        publicKey: builtins.bytes | None = ...,
        nonce: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["nonce", b"nonce", "publicKey", b"publicKey"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["nonce", b"nonce", "publicKey", b"publicKey"]) -> None: ...

global___PrimaryEphemeralIdentity = PrimaryEphemeralIdentity

@typing.final
class PairingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMPANIONPUBLICKEY_FIELD_NUMBER: builtins.int
    COMPANIONIDENTITYKEY_FIELD_NUMBER: builtins.int
    ADVSECRET_FIELD_NUMBER: builtins.int
    companionPublicKey: builtins.bytes
    companionIdentityKey: builtins.bytes
    advSecret: builtins.bytes
    def __init__(
        self,
        *,
        companionPublicKey: builtins.bytes | None = ...,
        companionIdentityKey: builtins.bytes | None = ...,
        advSecret: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["advSecret", b"advSecret", "companionIdentityKey", b"companionIdentityKey", "companionPublicKey", b"companionPublicKey"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["advSecret", b"advSecret", "companionIdentityKey", b"companionIdentityKey", "companionPublicKey", b"companionPublicKey"]) -> None: ...

global___PairingRequest = PairingRequest

@typing.final
class EncryptedPairingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENCRYPTEDPAYLOAD_FIELD_NUMBER: builtins.int
    IV_FIELD_NUMBER: builtins.int
    encryptedPayload: builtins.bytes
    IV: builtins.bytes
    def __init__(
        self,
        *,
        encryptedPayload: builtins.bytes | None = ...,
        IV: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["IV", b"IV", "encryptedPayload", b"encryptedPayload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["IV", b"IV", "encryptedPayload", b"encryptedPayload"]) -> None: ...

global___EncryptedPairingRequest = EncryptedPairingRequest

@typing.final
class ClientPairingProps(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISCHATDBLIDMIGRATED_FIELD_NUMBER: builtins.int
    ISSYNCDPURELIDSESSION_FIELD_NUMBER: builtins.int
    ISSYNCDSNAPSHOTRECOVERYENABLED_FIELD_NUMBER: builtins.int
    isChatDbLidMigrated: builtins.bool
    isSyncdPureLidSession: builtins.bool
    isSyncdSnapshotRecoveryEnabled: builtins.bool
    def __init__(
        self,
        *,
        isChatDbLidMigrated: builtins.bool | None = ...,
        isSyncdPureLidSession: builtins.bool | None = ...,
        isSyncdSnapshotRecoveryEnabled: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["isChatDbLidMigrated", b"isChatDbLidMigrated", "isSyncdPureLidSession", b"isSyncdPureLidSession", "isSyncdSnapshotRecoveryEnabled", b"isSyncdSnapshotRecoveryEnabled"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["isChatDbLidMigrated", b"isChatDbLidMigrated", "isSyncdPureLidSession", b"isSyncdPureLidSession", "isSyncdSnapshotRecoveryEnabled", b"isSyncdSnapshotRecoveryEnabled"]) -> None: ...

global___ClientPairingProps = ClientPairingProps

"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _FutureProofBehavior:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FutureProofBehaviorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FutureProofBehavior.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PLACEHOLDER: _FutureProofBehavior.ValueType  # 0
    NO_PLACEHOLDER: _FutureProofBehavior.ValueType  # 1
    IGNORE: _FutureProofBehavior.ValueType  # 2

class FutureProofBehavior(_FutureProofBehavior, metaclass=_FutureProofBehaviorEnumTypeWrapper): ...

PLACEHOLDER: FutureProofBehavior.ValueType  # 0
NO_PLACEHOLDER: FutureProofBehavior.ValueType  # 1
IGNORE: FutureProofBehavior.ValueType  # 2
global___FutureProofBehavior = FutureProofBehavior

@typing.final
class MessageKey(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REMOTEJID_FIELD_NUMBER: builtins.int
    FROMME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    PARTICIPANT_FIELD_NUMBER: builtins.int
    remoteJID: builtins.str
    fromMe: builtins.bool
    ID: builtins.str
    participant: builtins.str
    def __init__(
        self,
        *,
        remoteJID: builtins.str | None = ...,
        fromMe: builtins.bool | None = ...,
        ID: builtins.str | None = ...,
        participant: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ID", b"ID", "fromMe", b"fromMe", "participant", b"participant", "remoteJID", b"remoteJID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ID", b"ID", "fromMe", b"fromMe", "participant", b"participant", "remoteJID", b"remoteJID"]) -> None: ...

global___MessageKey = MessageKey

@typing.final
class Command(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _CommandType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CommandTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Command._CommandType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        EVERYONE: Command._CommandType.ValueType  # 1
        SILENT: Command._CommandType.ValueType  # 2
        AI: Command._CommandType.ValueType  # 3
        AI_IMAGINE: Command._CommandType.ValueType  # 4

    class CommandType(_CommandType, metaclass=_CommandTypeEnumTypeWrapper): ...
    EVERYONE: Command.CommandType.ValueType  # 1
    SILENT: Command.CommandType.ValueType  # 2
    AI: Command.CommandType.ValueType  # 3
    AI_IMAGINE: Command.CommandType.ValueType  # 4

    COMMANDTYPE_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    LENGTH_FIELD_NUMBER: builtins.int
    VALIDATIONTOKEN_FIELD_NUMBER: builtins.int
    commandType: global___Command.CommandType.ValueType
    offset: builtins.int
    length: builtins.int
    validationToken: builtins.str
    def __init__(
        self,
        *,
        commandType: global___Command.CommandType.ValueType | None = ...,
        offset: builtins.int | None = ...,
        length: builtins.int | None = ...,
        validationToken: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["commandType", b"commandType", "length", b"length", "offset", b"offset", "validationToken", b"validationToken"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["commandType", b"commandType", "length", b"length", "offset", b"offset", "validationToken", b"validationToken"]) -> None: ...

global___Command = Command

@typing.final
class Mention(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _MentionType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _MentionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Mention._MentionType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PROFILE: Mention._MentionType.ValueType  # 0

    class MentionType(_MentionType, metaclass=_MentionTypeEnumTypeWrapper): ...
    PROFILE: Mention.MentionType.ValueType  # 0

    MENTIONTYPE_FIELD_NUMBER: builtins.int
    MENTIONEDJID_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    LENGTH_FIELD_NUMBER: builtins.int
    mentionType: global___Mention.MentionType.ValueType
    mentionedJID: builtins.str
    offset: builtins.int
    length: builtins.int
    def __init__(
        self,
        *,
        mentionType: global___Mention.MentionType.ValueType | None = ...,
        mentionedJID: builtins.str | None = ...,
        offset: builtins.int | None = ...,
        length: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["length", b"length", "mentionType", b"mentionType", "mentionedJID", b"mentionedJID", "offset", b"offset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["length", b"length", "mentionType", b"mentionType", "mentionedJID", b"mentionedJID", "offset", b"offset"]) -> None: ...

global___Mention = Mention

@typing.final
class MessageText(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    MENTIONEDJID_FIELD_NUMBER: builtins.int
    COMMANDS_FIELD_NUMBER: builtins.int
    MENTIONS_FIELD_NUMBER: builtins.int
    text: builtins.str
    @property
    def mentionedJID(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def commands(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Command]: ...
    @property
    def mentions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Mention]: ...
    def __init__(
        self,
        *,
        text: builtins.str | None = ...,
        mentionedJID: collections.abc.Iterable[builtins.str] | None = ...,
        commands: collections.abc.Iterable[global___Command] | None = ...,
        mentions: collections.abc.Iterable[global___Mention] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["text", b"text"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["commands", b"commands", "mentionedJID", b"mentionedJID", "mentions", b"mentions", "text", b"text"]) -> None: ...

global___MessageText = MessageText

@typing.final
class SubProtocol(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAYLOAD_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    payload: builtins.bytes
    version: builtins.int
    def __init__(
        self,
        *,
        payload: builtins.bytes | None = ...,
        version: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["payload", b"payload", "version", b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["payload", b"payload", "version", b"version"]) -> None: ...

global___SubProtocol = SubProtocol

@typing.final
class LimitSharing(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Trigger:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TriggerEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LimitSharing._Trigger.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: LimitSharing._Trigger.ValueType  # 0
        CHAT_SETTING: LimitSharing._Trigger.ValueType  # 1
        BIZ_SUPPORTS_FB_HOSTING: LimitSharing._Trigger.ValueType  # 2
        UNKNOWN_GROUP: LimitSharing._Trigger.ValueType  # 3

    class Trigger(_Trigger, metaclass=_TriggerEnumTypeWrapper): ...
    UNKNOWN: LimitSharing.Trigger.ValueType  # 0
    CHAT_SETTING: LimitSharing.Trigger.ValueType  # 1
    BIZ_SUPPORTS_FB_HOSTING: LimitSharing.Trigger.ValueType  # 2
    UNKNOWN_GROUP: LimitSharing.Trigger.ValueType  # 3

    SHARINGLIMITED_FIELD_NUMBER: builtins.int
    TRIGGER_FIELD_NUMBER: builtins.int
    LIMITSHARINGSETTINGTIMESTAMP_FIELD_NUMBER: builtins.int
    INITIATEDBYME_FIELD_NUMBER: builtins.int
    sharingLimited: builtins.bool
    trigger: global___LimitSharing.Trigger.ValueType
    limitSharingSettingTimestamp: builtins.int
    initiatedByMe: builtins.bool
    def __init__(
        self,
        *,
        sharingLimited: builtins.bool | None = ...,
        trigger: global___LimitSharing.Trigger.ValueType | None = ...,
        limitSharingSettingTimestamp: builtins.int | None = ...,
        initiatedByMe: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["initiatedByMe", b"initiatedByMe", "limitSharingSettingTimestamp", b"limitSharingSettingTimestamp", "sharingLimited", b"sharingLimited", "trigger", b"trigger"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["initiatedByMe", b"initiatedByMe", "limitSharingSettingTimestamp", b"limitSharingSettingTimestamp", "sharingLimited", b"sharingLimited", "trigger", b"trigger"]) -> None: ...

global___LimitSharing = LimitSharing

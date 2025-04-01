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
class MediaRetryNotification(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ResultType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ResultTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MediaRetryNotification._ResultType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        GENERAL_ERROR: MediaRetryNotification._ResultType.ValueType  # 0
        SUCCESS: MediaRetryNotification._ResultType.ValueType  # 1
        NOT_FOUND: MediaRetryNotification._ResultType.ValueType  # 2
        DECRYPTION_ERROR: MediaRetryNotification._ResultType.ValueType  # 3

    class ResultType(_ResultType, metaclass=_ResultTypeEnumTypeWrapper): ...
    GENERAL_ERROR: MediaRetryNotification.ResultType.ValueType  # 0
    SUCCESS: MediaRetryNotification.ResultType.ValueType  # 1
    NOT_FOUND: MediaRetryNotification.ResultType.ValueType  # 2
    DECRYPTION_ERROR: MediaRetryNotification.ResultType.ValueType  # 3

    STANZAID_FIELD_NUMBER: builtins.int
    DIRECTPATH_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    MESSAGESECRET_FIELD_NUMBER: builtins.int
    stanzaID: builtins.str
    directPath: builtins.str
    result: global___MediaRetryNotification.ResultType.ValueType
    messageSecret: builtins.bytes
    def __init__(
        self,
        *,
        stanzaID: builtins.str | None = ...,
        directPath: builtins.str | None = ...,
        result: global___MediaRetryNotification.ResultType.ValueType | None = ...,
        messageSecret: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["directPath", b"directPath", "messageSecret", b"messageSecret", "result", b"result", "stanzaID", b"stanzaID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["directPath", b"directPath", "messageSecret", b"messageSecret", "result", b"result", "stanzaID", b"stanzaID"]) -> None: ...

global___MediaRetryNotification = MediaRetryNotification

@typing.final
class ServerErrorReceipt(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STANZAID_FIELD_NUMBER: builtins.int
    stanzaID: builtins.str
    def __init__(
        self,
        *,
        stanzaID: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["stanzaID", b"stanzaID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["stanzaID", b"stanzaID"]) -> None: ...

global___ServerErrorReceipt = ServerErrorReceipt

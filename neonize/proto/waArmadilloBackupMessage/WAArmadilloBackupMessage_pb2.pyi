"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class BackupMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Subprotocol(google.protobuf.message.Message):
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

    @typing.final
    class Metadata(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing.final
        class FrankingMetadata(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            FRANKINGTAG_FIELD_NUMBER: builtins.int
            REPORTINGTAG_FIELD_NUMBER: builtins.int
            frankingTag: builtins.bytes
            reportingTag: builtins.bytes
            def __init__(
                self,
                *,
                frankingTag: builtins.bytes | None = ...,
                reportingTag: builtins.bytes | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing.Literal["frankingTag", b"frankingTag", "reportingTag", b"reportingTag"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing.Literal["frankingTag", b"frankingTag", "reportingTag", b"reportingTag"]) -> None: ...

        SENDERID_FIELD_NUMBER: builtins.int
        MESSAGEID_FIELD_NUMBER: builtins.int
        TIMESTAMPMS_FIELD_NUMBER: builtins.int
        FRANKINGMETADATA_FIELD_NUMBER: builtins.int
        PAYLOADVERSION_FIELD_NUMBER: builtins.int
        FUTUREPROOFBEHAVIOR_FIELD_NUMBER: builtins.int
        THREADTYPETAG_FIELD_NUMBER: builtins.int
        senderID: builtins.str
        messageID: builtins.str
        timestampMS: builtins.int
        payloadVersion: builtins.int
        futureProofBehavior: builtins.int
        threadTypeTag: builtins.int
        @property
        def frankingMetadata(self) -> global___BackupMessage.Metadata.FrankingMetadata: ...
        def __init__(
            self,
            *,
            senderID: builtins.str | None = ...,
            messageID: builtins.str | None = ...,
            timestampMS: builtins.int | None = ...,
            frankingMetadata: global___BackupMessage.Metadata.FrankingMetadata | None = ...,
            payloadVersion: builtins.int | None = ...,
            futureProofBehavior: builtins.int | None = ...,
            threadTypeTag: builtins.int | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["frankingMetadata", b"frankingMetadata", "futureProofBehavior", b"futureProofBehavior", "messageID", b"messageID", "payloadVersion", b"payloadVersion", "senderID", b"senderID", "threadTypeTag", b"threadTypeTag", "timestampMS", b"timestampMS"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["frankingMetadata", b"frankingMetadata", "futureProofBehavior", b"futureProofBehavior", "messageID", b"messageID", "payloadVersion", b"payloadVersion", "senderID", b"senderID", "threadTypeTag", b"threadTypeTag", "timestampMS", b"timestampMS"]) -> None: ...

    ENCRYPTEDTRANSPORTMESSAGE_FIELD_NUMBER: builtins.int
    ENCRYPTEDTRANSPORTEVENT_FIELD_NUMBER: builtins.int
    ENCRYPTEDTRANSPORTLOCALLYTRANSFORMEDMESSAGE_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    encryptedTransportMessage: builtins.bytes
    @property
    def encryptedTransportEvent(self) -> global___BackupMessage.Subprotocol: ...
    @property
    def encryptedTransportLocallyTransformedMessage(self) -> global___BackupMessage.Subprotocol: ...
    @property
    def metadata(self) -> global___BackupMessage.Metadata: ...
    def __init__(
        self,
        *,
        encryptedTransportMessage: builtins.bytes | None = ...,
        encryptedTransportEvent: global___BackupMessage.Subprotocol | None = ...,
        encryptedTransportLocallyTransformedMessage: global___BackupMessage.Subprotocol | None = ...,
        metadata: global___BackupMessage.Metadata | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["encryptedTransportEvent", b"encryptedTransportEvent", "encryptedTransportLocallyTransformedMessage", b"encryptedTransportLocallyTransformedMessage", "encryptedTransportMessage", b"encryptedTransportMessage", "metadata", b"metadata", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["encryptedTransportEvent", b"encryptedTransportEvent", "encryptedTransportLocallyTransformedMessage", b"encryptedTransportLocallyTransformedMessage", "encryptedTransportMessage", b"encryptedTransportMessage", "metadata", b"metadata", "payload", b"payload"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["payload", b"payload"]) -> typing.Literal["encryptedTransportMessage", "encryptedTransportEvent", "encryptedTransportLocallyTransformedMessage"] | None: ...

global___BackupMessage = BackupMessage

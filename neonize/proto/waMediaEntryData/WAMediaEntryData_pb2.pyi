"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MediaEntry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class ProgressiveJpegDetails(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SCANLENGTHS_FIELD_NUMBER: builtins.int
        SIDECAR_FIELD_NUMBER: builtins.int
        sidecar: builtins.bytes
        @property
        def scanLengths(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        def __init__(
            self,
            *,
            scanLengths: collections.abc.Iterable[builtins.int] | None = ...,
            sidecar: builtins.bytes | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["sidecar", b"sidecar"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["scanLengths", b"scanLengths", "sidecar", b"sidecar"]) -> None: ...

    @typing.final
    class DownloadableThumbnail(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FILESHA256_FIELD_NUMBER: builtins.int
        FILEENCSHA256_FIELD_NUMBER: builtins.int
        DIRECTPATH_FIELD_NUMBER: builtins.int
        MEDIAKEY_FIELD_NUMBER: builtins.int
        MEDIAKEYTIMESTAMP_FIELD_NUMBER: builtins.int
        OBJECTID_FIELD_NUMBER: builtins.int
        fileSHA256: builtins.bytes
        fileEncSHA256: builtins.bytes
        directPath: builtins.str
        mediaKey: builtins.bytes
        mediaKeyTimestamp: builtins.int
        objectID: builtins.str
        def __init__(
            self,
            *,
            fileSHA256: builtins.bytes | None = ...,
            fileEncSHA256: builtins.bytes | None = ...,
            directPath: builtins.str | None = ...,
            mediaKey: builtins.bytes | None = ...,
            mediaKeyTimestamp: builtins.int | None = ...,
            objectID: builtins.str | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["directPath", b"directPath", "fileEncSHA256", b"fileEncSHA256", "fileSHA256", b"fileSHA256", "mediaKey", b"mediaKey", "mediaKeyTimestamp", b"mediaKeyTimestamp", "objectID", b"objectID"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["directPath", b"directPath", "fileEncSHA256", b"fileEncSHA256", "fileSHA256", b"fileSHA256", "mediaKey", b"mediaKey", "mediaKeyTimestamp", b"mediaKeyTimestamp", "objectID", b"objectID"]) -> None: ...

    FILESHA256_FIELD_NUMBER: builtins.int
    MEDIAKEY_FIELD_NUMBER: builtins.int
    FILEENCSHA256_FIELD_NUMBER: builtins.int
    DIRECTPATH_FIELD_NUMBER: builtins.int
    MEDIAKEYTIMESTAMP_FIELD_NUMBER: builtins.int
    SERVERMEDIATYPE_FIELD_NUMBER: builtins.int
    UPLOADTOKEN_FIELD_NUMBER: builtins.int
    VALIDATEDTIMESTAMP_FIELD_NUMBER: builtins.int
    SIDECAR_FIELD_NUMBER: builtins.int
    OBJECTID_FIELD_NUMBER: builtins.int
    FBID_FIELD_NUMBER: builtins.int
    DOWNLOADABLETHUMBNAIL_FIELD_NUMBER: builtins.int
    HANDLE_FIELD_NUMBER: builtins.int
    FILENAME_FIELD_NUMBER: builtins.int
    PROGRESSIVEJPEGDETAILS_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    LASTDOWNLOADATTEMPTTIMESTAMP_FIELD_NUMBER: builtins.int
    fileSHA256: builtins.bytes
    mediaKey: builtins.bytes
    fileEncSHA256: builtins.bytes
    directPath: builtins.str
    mediaKeyTimestamp: builtins.int
    serverMediaType: builtins.str
    uploadToken: builtins.bytes
    validatedTimestamp: builtins.bytes
    sidecar: builtins.bytes
    objectID: builtins.str
    FBID: builtins.str
    handle: builtins.str
    filename: builtins.str
    size: builtins.int
    lastDownloadAttemptTimestamp: builtins.int
    @property
    def downloadableThumbnail(self) -> global___MediaEntry.DownloadableThumbnail: ...
    @property
    def progressiveJPEGDetails(self) -> global___MediaEntry.ProgressiveJpegDetails: ...
    def __init__(
        self,
        *,
        fileSHA256: builtins.bytes | None = ...,
        mediaKey: builtins.bytes | None = ...,
        fileEncSHA256: builtins.bytes | None = ...,
        directPath: builtins.str | None = ...,
        mediaKeyTimestamp: builtins.int | None = ...,
        serverMediaType: builtins.str | None = ...,
        uploadToken: builtins.bytes | None = ...,
        validatedTimestamp: builtins.bytes | None = ...,
        sidecar: builtins.bytes | None = ...,
        objectID: builtins.str | None = ...,
        FBID: builtins.str | None = ...,
        downloadableThumbnail: global___MediaEntry.DownloadableThumbnail | None = ...,
        handle: builtins.str | None = ...,
        filename: builtins.str | None = ...,
        progressiveJPEGDetails: global___MediaEntry.ProgressiveJpegDetails | None = ...,
        size: builtins.int | None = ...,
        lastDownloadAttemptTimestamp: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["FBID", b"FBID", "directPath", b"directPath", "downloadableThumbnail", b"downloadableThumbnail", "fileEncSHA256", b"fileEncSHA256", "fileSHA256", b"fileSHA256", "filename", b"filename", "handle", b"handle", "lastDownloadAttemptTimestamp", b"lastDownloadAttemptTimestamp", "mediaKey", b"mediaKey", "mediaKeyTimestamp", b"mediaKeyTimestamp", "objectID", b"objectID", "progressiveJPEGDetails", b"progressiveJPEGDetails", "serverMediaType", b"serverMediaType", "sidecar", b"sidecar", "size", b"size", "uploadToken", b"uploadToken", "validatedTimestamp", b"validatedTimestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["FBID", b"FBID", "directPath", b"directPath", "downloadableThumbnail", b"downloadableThumbnail", "fileEncSHA256", b"fileEncSHA256", "fileSHA256", b"fileSHA256", "filename", b"filename", "handle", b"handle", "lastDownloadAttemptTimestamp", b"lastDownloadAttemptTimestamp", "mediaKey", b"mediaKey", "mediaKeyTimestamp", b"mediaKeyTimestamp", "objectID", b"objectID", "progressiveJPEGDetails", b"progressiveJPEGDetails", "serverMediaType", b"serverMediaType", "sidecar", b"sidecar", "size", b"size", "uploadToken", b"uploadToken", "validatedTimestamp", b"validatedTimestamp"]) -> None: ...

global___MediaEntry = MediaEntry

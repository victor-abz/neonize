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
class EphemeralSetting(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DURATION_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    duration: builtins.int
    timestamp: builtins.int
    def __init__(
        self,
        *,
        duration: builtins.int | None = ...,
        timestamp: builtins.int | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal["duration", b"duration", "timestamp", b"timestamp"],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal["duration", b"duration", "timestamp", b"timestamp"],
    ) -> None: ...

global___EphemeralSetting = EphemeralSetting

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: waE2EGuest/WAWebProtobufsE2EGuest.proto
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
    'waE2EGuest/WAWebProtobufsE2EGuest.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'waE2EGuest/WAWebProtobufsE2EGuest.proto\x12\x16WAWebProtobufsE2EGuest\"\x8e\x03\n\x07Message\x12\x14\n\x0c\x63onversation\x18\x01 \x01(\t\x12P\n\x13\x65xtendedTextMessage\x18\x06 \x01(\x0b\x32\x33.WAWebProtobufsE2EGuest.Message.ExtendedTextMessage\x12\x46\n\x12messageContextInfo\x18# \x01(\x0b\x32*.WAWebProtobufsE2EGuest.MessageContextInfo\x1a\x65\n\x13\x45xtendedTextMessage\x12\x0c\n\x04text\x18\x01 \x01(\t\x12@\n\x0b\x63ontextInfo\x18\x11 \x01(\x0b\x32+.WAWebProtobufsE2EGuest.Message.ContextInfo\x1al\n\x0b\x43ontextInfo\x12\x10\n\x08stanzaID\x18\x01 \x01(\t\x12\x13\n\x0bparticipant\x18\x02 \x01(\t\x12\x36\n\rquotedMessage\x18\x03 \x01(\x0b\x32\x1f.WAWebProtobufsE2EGuest.Message\"+\n\x12MessageContextInfo\x12\x15\n\rmessageSecret\x18\x03 \x01(\x0c\x42&Z$go.mau.fi/whatsmeow/proto/waE2EGuest')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waE2EGuest.WAWebProtobufsE2EGuest_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$go.mau.fi/whatsmeow/proto/waE2EGuest'
  _globals['_MESSAGE']._serialized_start=68
  _globals['_MESSAGE']._serialized_end=466
  _globals['_MESSAGE_EXTENDEDTEXTMESSAGE']._serialized_start=255
  _globals['_MESSAGE_EXTENDEDTEXTMESSAGE']._serialized_end=356
  _globals['_MESSAGE_CONTEXTINFO']._serialized_start=358
  _globals['_MESSAGE_CONTEXTINFO']._serialized_end=466
  _globals['_MESSAGECONTEXTINFO']._serialized_start=468
  _globals['_MESSAGECONTEXTINFO']._serialized_end=511
# @@protoc_insertion_point(module_scope)

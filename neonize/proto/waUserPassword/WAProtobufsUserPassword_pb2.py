# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: waUserPassword/WAProtobufsUserPassword.proto
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
    'waUserPassword/WAProtobufsUserPassword.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,waUserPassword/WAProtobufsUserPassword.proto\x12\x17WAProtobufsUserPassword\"\x9b\x04\n\x0cUserPassword\x12@\n\x08\x65ncoding\x18\x01 \x01(\x0e\x32..WAProtobufsUserPassword.UserPassword.Encoding\x12\x46\n\x0btransformer\x18\x02 \x01(\x0e\x32\x31.WAProtobufsUserPassword.UserPassword.Transformer\x12L\n\x0etransformerArg\x18\x03 \x03(\x0b\x32\x34.WAProtobufsUserPassword.UserPassword.TransformerArg\x12\x17\n\x0ftransformedData\x18\x04 \x01(\x0c\x1a\xa9\x01\n\x0eTransformerArg\x12\x0b\n\x03key\x18\x01 \x01(\t\x12I\n\x05value\x18\x02 \x01(\x0b\x32:.WAProtobufsUserPassword.UserPassword.TransformerArg.Value\x1a?\n\x05Value\x12\x10\n\x06\x61sBlob\x18\x01 \x01(\x0cH\x00\x12\x1b\n\x11\x61sUnsignedInteger\x18\x02 \x01(\rH\x00\x42\x07\n\x05value\"G\n\x0bTransformer\x12\x08\n\x04NONE\x10\x00\x12\x16\n\x12PBKDF2_HMAC_SHA512\x10\x01\x12\x16\n\x12PBKDF2_HMAC_SHA384\x10\x02\"%\n\x08\x45ncoding\x12\x08\n\x04UTF8\x10\x00\x12\x0f\n\x0bUTF8_BROKEN\x10\x01\x42*Z(go.mau.fi/whatsmeow/proto/waUserPassword')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waUserPassword.WAProtobufsUserPassword_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z(go.mau.fi/whatsmeow/proto/waUserPassword'
  _globals['_USERPASSWORD']._serialized_start=74
  _globals['_USERPASSWORD']._serialized_end=613
  _globals['_USERPASSWORD_TRANSFORMERARG']._serialized_start=332
  _globals['_USERPASSWORD_TRANSFORMERARG']._serialized_end=501
  _globals['_USERPASSWORD_TRANSFORMERARG_VALUE']._serialized_start=438
  _globals['_USERPASSWORD_TRANSFORMERARG_VALUE']._serialized_end=501
  _globals['_USERPASSWORD_TRANSFORMER']._serialized_start=503
  _globals['_USERPASSWORD_TRANSFORMER']._serialized_end=574
  _globals['_USERPASSWORD_ENCODING']._serialized_start=576
  _globals['_USERPASSWORD_ENCODING']._serialized_end=613
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CombatScore.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x43ombatScore.proto\x12\x0b\x43ombatScore\"\x89\x01\n\x03\x43\x66g\x12\n\n\x02ID\x18\x01 \x01(\x05\x12\x10\n\x08\x44\x65scribe\x18\x02 \x01(\t\x12\x12\n\nFloorValue\x18\x03 \x01(\x05\x12\x16\n\x0eScoreReduction\x18\x04 \x01(\x05\x12\x12\n\nExposedAdd\x18\x05 \x01(\x05\x12\x11\n\tAttackAdd\x18\x06 \x01(\x05\x12\x11\n\tCombatOff\x18\x07 \x01(\x05\x62\x06proto3')



_CFG = DESCRIPTOR.message_types_by_name['Cfg']
Cfg = _reflection.GeneratedProtocolMessageType('Cfg', (_message.Message,), {
  'DESCRIPTOR' : _CFG,
  '__module__' : 'CombatScore_pb2'
  # @@protoc_insertion_point(class_scope:CombatScore.Cfg)
  })
_sym_db.RegisterMessage(Cfg)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CFG._serialized_start=35
  _CFG._serialized_end=172
# @@protoc_insertion_point(module_scope)

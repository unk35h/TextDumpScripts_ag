# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: InterestConfig.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14InterestConfig.proto\x12\x0eInterestConfig\"\xcb\x02\n\x03\x43\x66g\x12\n\n\x02ID\x18\x01 \x01(\x05\x12+\n\x05Group\x18\x02 \x03(\x0e\x32\x1c.InterestConfig.Cfg.RoleType\"\x8a\x02\n\x08RoleType\x12\x11\n\rRoleType_None\x10\x00\x12\x13\n\x0fRoleType_Player\x10\x01\x12\x12\n\x0eRoleType_Enemy\x10\x02\x12\x14\n\x10RoleType_Neutral\x10\x04\x12\x13\n\x0fRoleType_Bunker\x10\x08\x12\x14\n\x10RoleType_Trigger\x10\x10\x12\x11\n\rRoleType_Trap\x10 \x12\x10\n\x0cRoleType_Box\x10@\x12\x14\n\x0fRoleType_Friend\x10\x80\x01\x12\x14\n\x0fRoleType_Puppet\x10\x80\x02\x12\x19\n\x14RoleType_AvoidShadow\x10\x80\x04\x12\x15\n\x10RoleType_AirWall\x10\x80\x08\x62\x06proto3')



_CFG = DESCRIPTOR.message_types_by_name['Cfg']
_CFG_ROLETYPE = _CFG.enum_types_by_name['RoleType']
Cfg = _reflection.GeneratedProtocolMessageType('Cfg', (_message.Message,), {
  'DESCRIPTOR' : _CFG,
  '__module__' : 'InterestConfig_pb2'
  # @@protoc_insertion_point(class_scope:InterestConfig.Cfg)
  })
_sym_db.RegisterMessage(Cfg)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CFG._serialized_start=41
  _CFG._serialized_end=372
  _CFG_ROLETYPE._serialized_start=106
  _CFG_ROLETYPE._serialized_end=372
# @@protoc_insertion_point(module_scope)

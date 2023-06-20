# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RoleConfig.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10RoleConfig.proto\x12\nRoleConfig\"\xdb\x10\n\x03\x43\x66g\x12\n\n\x02ID\x18\x01 \x01(\x05\x12\x14\n\x0c\x46lowCavansID\x18\x02 \x01(\x05\x12\x19\n\x11\x41\x64\x64itionalRoleIDs\x18\x03 \x03(\x05\x12\x1f\n\x17SameDamageSourceRoleIDs\x18\x04 \x01(\x05\x12\x1f\n\x17\x41\x64\x64itionalRenderRoleIDs\x18\x05 \x03(\x05\x12.\n\x06\x41rmour\x18\x06 \x01(\x0e\x32\x1e.RoleConfig.Cfg.ArmourCategory\x12\x30\n\tShapePart\x18\x07 \x03(\x0e\x32\x1d.RoleConfig.Cfg.ShapePartType\x12\x1c\n\x14ShapePartAttachPoint\x18\x08 \x03(\t\x12\x0e\n\x06Radius\x18\t \x03(\x05\x12\x1b\n\x13ShapePartCollection\x18\n \x03(\x05\x12\x1c\n\x14\x44\x65stroyValChangeRule\x18\x0b \x03(\x05\x12\x17\n\x0f\x44\x65stroyValLimit\x18\x0c \x03(\x05\x12\x30\n\tDeathTime\x18\r \x01(\x0e\x32\x1d.RoleConfig.Cfg.DeathTimeType\x12\x0e\n\x06Melees\x18\x0e \x03(\x05\x12\x0f\n\x07\x41\x62ility\x18\x0f \x03(\x05\x12\x13\n\x0bRageAbility\x18\x10 \x03(\x05\x12\x14\n\x0c\x41voidAbility\x18\x11 \x03(\x05\x12\x17\n\x0fUseRunMoveCurve\x18\x12 \x01(\x08\x12\r\n\x05Speed\x18\x13 \x01(\x05\x12\x14\n\x0cHitRecoverID\x18\x14 \x03(\x05\x12\x1c\n\x14RoleHitBackRecoverID\x18\x15 \x01(\x05\x12\x18\n\x10HitBackRecoverID\x18\x16 \x01(\x05\x12\x10\n\x08HitAirID\x18\x17 \x03(\x05\x12\x0f\n\x07HitUpID\x18\x18 \x01(\x05\x12\x11\n\tHitDownID\x18\x19 \x01(\x05\x12\x12\n\nHitFloorID\x18\x1a \x01(\x05\x12\x0f\n\x07GetUpID\x18\x1b \x01(\x05\x12\x15\n\rQuickRecovery\x18\x1c \x01(\x05\x12\x0b\n\x03Run\x18\x1d \x01(\x05\x12\x0c\n\x04Idle\x18\x1e \x01(\x05\x12\x0e\n\x06Weight\x18\x1f \x01(\x05\x12\x0f\n\x07RunLeft\x18  \x01(\x05\x12\x10\n\x08RunRight\x18! \x01(\x05\x12\r\n\x05\x44\x65\x61th\x18\" \x01(\x05\x12\x18\n\x10NoAnimationDeath\x18# \x01(\x05\x12\x10\n\x08\x41irDeath\x18$ \x01(\x05\x12\x15\n\rFallDownDeath\x18% \x01(\x05\x12\x0e\n\x06\x41ppear\x18& \x01(\x05\x12\x14\n\x0cMovementStop\x18\' \x01(\x05\x12\x12\n\nCanHitBack\x18( \x01(\x08\x12\x10\n\x08\x43\x61nHitUp\x18) \x01(\x08\x12\x0e\n\x06RushID\x18* \x01(\x05\x12\x12\n\nRushStopID\x18+ \x01(\x05\x12\x11\n\tRushSpeed\x18, \x01(\x05\x12\x18\n\x10HitBackValidTime\x18- \x03(\x05\x12\x14\n\x0c\x42\x61lanceValue\x18. \x01(\x05\x12\x17\n\x0f\x45xtendAbilities\x18/ \x03(\x05\x12\x0f\n\x07RelaxID\x18\x30 \x01(\x05\x12\x10\n\x08RunStart\x18\x31 \x01(\x05\x12\x19\n\x11\x42\x61ttleIldeRecover\x18\x32 \x01(\x05\x12\x12\n\nBattleIdle\x18\x33 \x01(\x05\x12\x10\n\x08NearStop\x18\x34 \x01(\x05\x12\x15\n\rRotationSpeed\x18\x35 \x01(\x05\x12\x16\n\x0eLimitTurnAngle\x18\x36 \x01(\x05\x12\x11\n\tAllSkills\x18\x37 \x03(\x05\x12\x37\n\x0eMainDamageType\x18\x38 \x01(\x0e\x32\x1f.RoleConfig.Cfg.SkillDamageType\x12\x11\n\tCanBeGrab\x18\x39 \x01(\x08\x12\x13\n\x0bKeepForward\x18: \x01(\x08\"\x9c\x01\n\x0e\x41rmourCategory\x12\x17\n\x13\x41rmourCategory_None\x10\x00\x12\x17\n\x13\x41rmourCategory_Body\x10\x01\x12\x1e\n\x1a\x41rmourCategory_LightArmour\x10\x02\x12\x1e\n\x1a\x41rmourCategory_HeavyArmour\x10\x03\x12\x18\n\x14\x41rmourCategory_Metal\x10\x04\"\xff\x01\n\rShapePartType\x12\x16\n\x12ShapePartType_Body\x10\x00\x12\x19\n\x15ShapePartType_Foreleg\x10\x01\x12\x19\n\x15ShapePartType_Hindleg\x10\x02\x12\x1a\n\x16ShapePartType_LeftHand\x10\x03\x12\x1b\n\x17ShapePartType_RightHand\x10\x04\x12\x1a\n\x16ShapePartType_LeftFoot\x10\x05\x12\x1b\n\x17ShapePartType_RightFoot\x10\x06\x12\x16\n\x12ShapePartType_Head\x10\x07\x12\x16\n\x12ShapePartType_Tail\x10\x08\"r\n\rDeathTimeType\x12\"\n\x1e\x44\x65\x61thTimeType_ImmediatelyDeath\x10\x00\x12 \n\x1c\x44\x65\x61thTimeType_WaitHitRecover\x10\x01\x12\x1b\n\x17\x44\x65\x61thTimeType_WaitGetUp\x10\x02\"\x82\x02\n\x0fSkillDamageType\x12\x1b\n\x17SkillDamageType_Physics\x10\x00\x12\x18\n\x14SkillDamageType_Wind\x10\x02\x12\x18\n\x14SkillDamageType_Fire\x10\x04\x12\x17\n\x13SkillDamageType_Ice\x10\x06\x12\x19\n\x15SkillDamageType_Water\x10\x08\x12\x18\n\x14SkillDamageType_Dark\x10\n\x12\x19\n\x15SkillDamageType_Light\x10\x0c\x12\x1b\n\x17SkillDamageType_Thunder\x10\x0e\x12\x18\n\x13SkillDamageType_All\x10\xff\x01\x62\x06proto3')



_CFG = DESCRIPTOR.message_types_by_name['Cfg']
_CFG_ARMOURCATEGORY = _CFG.enum_types_by_name['ArmourCategory']
_CFG_SHAPEPARTTYPE = _CFG.enum_types_by_name['ShapePartType']
_CFG_DEATHTIMETYPE = _CFG.enum_types_by_name['DeathTimeType']
_CFG_SKILLDAMAGETYPE = _CFG.enum_types_by_name['SkillDamageType']
Cfg = _reflection.GeneratedProtocolMessageType('Cfg', (_message.Message,), {
  'DESCRIPTOR' : _CFG,
  '__module__' : 'RoleConfig_pb2'
  # @@protoc_insertion_point(class_scope:RoleConfig.Cfg)
  })
_sym_db.RegisterMessage(Cfg)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CFG._serialized_start=33
  _CFG._serialized_end=2172
  _CFG_ARMOURCATEGORY._serialized_start=1381
  _CFG_ARMOURCATEGORY._serialized_end=1537
  _CFG_SHAPEPARTTYPE._serialized_start=1540
  _CFG_SHAPEPARTTYPE._serialized_end=1795
  _CFG_DEATHTIMETYPE._serialized_start=1797
  _CFG_DEATHTIMETYPE._serialized_end=1911
  _CFG_SKILLDAMAGETYPE._serialized_start=1914
  _CFG_SKILLDAMAGETYPE._serialized_end=2172
# @@protoc_insertion_point(module_scope)
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CommonHit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x43ommonHit.proto\x12\tCommonHit\"\xea\t\n\x03\x43\x66g\x12\n\n\x02ID\x18\x01 \x01(\x05\x12-\n\x06Weapon\x18\x02 \x01(\x0e\x32\x1d.CommonHit.Cfg.WeaponCategory\x12\x39\n\x0c\x41ttackAction\x18\x03 \x01(\x0e\x32#.CommonHit.Cfg.AttackActionCategory\x12\x32\n\nDamageType\x18\x04 \x01(\x0e\x32\x1e.CommonHit.Cfg.SkillDamageType\x12-\n\x06\x41rmour\x18\x05 \x01(\x0e\x32\x1d.CommonHit.Cfg.ArmourCategory\x12\x10\n\x08\x43ueSheet\x18\x06 \x01(\t\x12\x0f\n\x07\x43ueName\x18\x07 \x01(\t\x12\x0e\n\x06\x43ueAwb\x18\x08 \x01(\t\x12\x12\n\nEffectPath\x18\t \x01(\t\x12\x10\n\x08\x44\x65scribe\x18\n \x01(\t\"\x91\x02\n\x0eWeaponCategory\x12\x17\n\x13WeaponCategory_None\x10\x00\x12\x18\n\x14WeaponCategory_Sword\x10\x01\x12\x1e\n\x1aWeaponCategory_LongHandled\x10\x02\x12\x16\n\x12WeaponCategory_Bow\x10\x03\x12\x18\n\x14WeaponCategory_Blunt\x10\x04\x12\x16\n\x12WeaponCategory_Gun\x10\x05\x12\x17\n\x13WeaponCategory_Claw\x10\x06\x12\x17\n\x13WeaponCategory_Body\x10\x07\x12\x18\n\x14WeaponCategory_Magic\x10\x08\x12\x16\n\x12WeaponCategory_Orb\x10\t\"\xf8\x01\n\x14\x41ttackActionCategory\x12\x1d\n\x19\x41ttackActionCategory_None\x10\x00\x12\x1d\n\x19\x41ttackActionCategory_Chop\x10\x01\x12!\n\x1d\x41ttackActionCategory_Stabbing\x10\x02\x12\x1e\n\x1a\x41ttackActionCategory_Pound\x10\x03\x12\x1e\n\x1a\x41ttackActionCategory_Shoot\x10\x04\x12\x1c\n\x18\x41ttackActionCategory_Hit\x10\x05\x12!\n\x1d\x41ttackActionCategory_MagicHit\x10\x06\"\x82\x02\n\x0fSkillDamageType\x12\x1b\n\x17SkillDamageType_Physics\x10\x00\x12\x18\n\x14SkillDamageType_Wind\x10\x02\x12\x18\n\x14SkillDamageType_Fire\x10\x04\x12\x17\n\x13SkillDamageType_Ice\x10\x06\x12\x19\n\x15SkillDamageType_Water\x10\x08\x12\x18\n\x14SkillDamageType_Dark\x10\n\x12\x19\n\x15SkillDamageType_Light\x10\x0c\x12\x1b\n\x17SkillDamageType_Thunder\x10\x0e\x12\x18\n\x13SkillDamageType_All\x10\xff\x01\"\x9c\x01\n\x0e\x41rmourCategory\x12\x17\n\x13\x41rmourCategory_None\x10\x00\x12\x17\n\x13\x41rmourCategory_Body\x10\x01\x12\x1e\n\x1a\x41rmourCategory_LightArmour\x10\x02\x12\x1e\n\x1a\x41rmourCategory_HeavyArmour\x10\x03\x12\x18\n\x14\x41rmourCategory_Metal\x10\x04\x62\x06proto3')



_CFG = DESCRIPTOR.message_types_by_name['Cfg']
_CFG_WEAPONCATEGORY = _CFG.enum_types_by_name['WeaponCategory']
_CFG_ATTACKACTIONCATEGORY = _CFG.enum_types_by_name['AttackActionCategory']
_CFG_SKILLDAMAGETYPE = _CFG.enum_types_by_name['SkillDamageType']
_CFG_ARMOURCATEGORY = _CFG.enum_types_by_name['ArmourCategory']
Cfg = _reflection.GeneratedProtocolMessageType('Cfg', (_message.Message,), {
  'DESCRIPTOR' : _CFG,
  '__module__' : 'CommonHit_pb2'
  # @@protoc_insertion_point(class_scope:CommonHit.Cfg)
  })
_sym_db.RegisterMessage(Cfg)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CFG._serialized_start=31
  _CFG._serialized_end=1289
  _CFG_WEAPONCATEGORY._serialized_start=345
  _CFG_WEAPONCATEGORY._serialized_end=618
  _CFG_ATTACKACTIONCATEGORY._serialized_start=621
  _CFG_ATTACKACTIONCATEGORY._serialized_end=869
  _CFG_SKILLDAMAGETYPE._serialized_start=872
  _CFG_SKILLDAMAGETYPE._serialized_end=1130
  _CFG_ARMOURCATEGORY._serialized_start=1133
  _CFG_ARMOURCATEGORY._serialized_end=1289
# @@protoc_insertion_point(module_scope)
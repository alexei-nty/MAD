# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/combat_challenge_global_settings.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import friendship_level_milestone_pb2 as pogoprotos_dot_enums_dot_friendship__level__milestone__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/combat_challenge_global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n:pogoprotos/settings/combat_challenge_global_settings.proto\x12\x13pogoprotos.settings\x1a\x31pogoprotos/enums/friendship_level_milestone.proto\"\xfc\x01\n\x1d\x43ombatChallengeGlobalSettings\x12\\\n(distance_check_override_friendship_level\x18\x01 \x01(\x0e\x32*.pogoprotos.enums.FriendshipLevelMilestone\x12\x31\n)get_combat_challenge_polling_interval_sec\x18\x02 \x01(\x05\x12\"\n\x1a\x65nable_downstream_dispatch\x18\x03 \x01(\x08\x12&\n\x1e\x65nable_challenge_notifications\x18\x04 \x01(\x08\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_friendship__level__milestone__pb2.DESCRIPTOR,])




_COMBATCHALLENGEGLOBALSETTINGS = _descriptor.Descriptor(
  name='CombatChallengeGlobalSettings',
  full_name='pogoprotos.settings.CombatChallengeGlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='distance_check_override_friendship_level', full_name='pogoprotos.settings.CombatChallengeGlobalSettings.distance_check_override_friendship_level', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_combat_challenge_polling_interval_sec', full_name='pogoprotos.settings.CombatChallengeGlobalSettings.get_combat_challenge_polling_interval_sec', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_downstream_dispatch', full_name='pogoprotos.settings.CombatChallengeGlobalSettings.enable_downstream_dispatch', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_challenge_notifications', full_name='pogoprotos.settings.CombatChallengeGlobalSettings.enable_challenge_notifications', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=387,
)

_COMBATCHALLENGEGLOBALSETTINGS.fields_by_name['distance_check_override_friendship_level'].enum_type = pogoprotos_dot_enums_dot_friendship__level__milestone__pb2._FRIENDSHIPLEVELMILESTONE
DESCRIPTOR.message_types_by_name['CombatChallengeGlobalSettings'] = _COMBATCHALLENGEGLOBALSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatChallengeGlobalSettings = _reflection.GeneratedProtocolMessageType('CombatChallengeGlobalSettings', (_message.Message,), {
  'DESCRIPTOR' : _COMBATCHALLENGEGLOBALSETTINGS,
  '__module__' : 'pogoprotos.settings.combat_challenge_global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.CombatChallengeGlobalSettings)
  })
_sym_db.RegisterMessage(CombatChallengeGlobalSettings)


# @@protoc_insertion_point(module_scope)
# module: gclient.gameplay.logic_moba_zombie.avatarmembers.cimp_zombie_combat_unit

import weapon_util

class CombatAvatarMember(ComponentWithProperty):
    def _DamageSoundEffect(self, result, caster, target, damage_data, is_system_damage, is_friend): ...

class ComponentWithProperty(object):
class PlayerCombatAvatarMember(CombatAvatarMember):
    def _DamageSoundEffect(self, result, caster, target, damage_data, is_system_damage, is_friend): ...


def Property(name, default, flag=2): ...


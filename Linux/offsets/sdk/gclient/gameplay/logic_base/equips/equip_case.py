# module: gclient.gameplay.logic_base.equips.equip_case

import consts
import equip_data

EQUIP_CASE_DICT: dict = {'Weapon': <class 'gclient.gameplay.logic_base.equips.weapon_case.WeaponCase'>, 'RightHandThrowable': <class 'gclient.gameplay.logic_base.equips.righthand_throwable_case.RightHandThrowableCase'>, 'LeftHand': <class 'gclient.gameplay.logic_base.equips.lefthand_case.LeftHandCase'>, 'ReplayWeapon': <class 'gclient.gameplay.logic_base.equips.replay_weapon_case.ReplayWeaponCase'>, 'ReplayLeftHand': <class 'gclient.gameplay.logic_base.equips.replay_lefthand_case.ReplayLeftHandCase'>, 'ReplayRightHandThrowable': <class 'gclient.gameplay.logic_base.equips.replay_righthand_throwable_case.ReplayRightHandThrowableCase'>, 'Item': <class 'gclient.gameplay.logic_base.equips.item_case.ItemCase'>, 'ReplayItem': <class 'gclient.gameplay.logic_base.equips.replay_item_case.ReplayItemCase'>, 'Melee': <class 'gclient.gameplay.logic_base.equips.melee_case.MeleeCase'>, 'ReplayMelee': <class 'gclient.gameplay.logic_base.equips.replay_melee_case.ReplayMeleeCase'>, 'None': <class 'gclient.gameplay.logic_base.equips.none_case.NoneCase'>, 'ReplayNone': <class 'gclient.gameplay.logic_base.equips.replay_none_case.ReplayNoneCase'>, 'GunMelee': <class 'gclient.gameplay.logic_base.equips.gun_melee_case.GunMeleeCase'>, 'ReplayGunMelee': <class 'gclient.gameplay.logic_base.equips.replay_gun_melee_case.ReplayGunMeleeCase'>, 'SamuraiSword': <class 'gclient.gameplay.logic_base.equips.samurai_sword_case.SamuraiSwordCase'>, 'ReplaySamuraiSword': <class 'gclient.gameplay.logic_base.equips.replay_samurai_sword_case.ReplaySamuraiSwordCase'>, 'DualMelee': <class 'gclient.gameplay.logic_base.equips.dual_melee_case.DualMeleeCase'>, 'ReplayDualMelee': <class 'gclient.gameplay.logic_base.equips.replay_dual_melee_case.ReplayDualMeleeCase'>, 'LeftXDroid': <class 'gclient.gameplay.logic_base.equips.left_xdroid_case.LeftXDroidCase'>, 'ReplayLeftXDroid': <class 'gclient.gameplay.logic_base.equips.replay_left_xdroid_case.ReplayLeftXDroidCase'>, 'CommonSkill': <class 'gclient.gameplay.logic_base.equips.common_skill_case.CommonSkillCase'>, 'ReplayCommonSkill': <class 'gclient.gameplay.logic_base.equips.replay_common_skill_case.ReplayCommonSkillCase'>, 'LeftShield': <class 'gclient.gameplay.logic_base.equips.leftshield_case.LeftShieldCase'>}

class EquipCaseFactory(object):
    def Create(weapon_id, *args, **kwargs): ...


def RegisterEquipCaseClass(cls): ...


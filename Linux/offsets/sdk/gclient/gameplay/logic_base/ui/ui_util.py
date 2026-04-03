# module: gclient.gameplay.logic_base.ui.ui_util

import cconst
import consts
import ibuff
import lang
import math
import six2
import sound_island_dist_data
import sound_map_dist_data
import ui_define

GunCostAmmos: dict = {1: 7, 2: 8, 3: 71, 5: 14, 4: 7, 6: 14, 7: 8, 8: 197}
LocalConfig: _LocalConfig = <gclient.config._LocalConfig object at 0x7040bf6d50>
USE_NEW_SKILL_NODE: bool = False
ZOMBIE_CRYSTAL_ITEM_ID: int = 308
ZOMBIE_RECOVER_ITEM_ID: int = 417

class AttrType(enum):
    ANTI_RESTORE_HP_TIME: int = 7
    AmmoMaxStack: int = 22
    AssassinateEnergyUp: int = 47
    BackpackFreeSlot: int = 21
    BanSprint: int = 62
    BombBuffDuration: int = 18
    BombBuffRange: int = 17
    BombDamage: int = 16
    BombDamageRange: int = 15
    CannonDamage: int = 46
    CureUavCureSpeed: int = 42
    CureUavRangeUp: int = 65
    CureUavTimeUp: int = 66
    CureValueUp: int = 58
    EnergySkillChargeSpeed: int = 56
    EnergyValueUp: int = 26
    ForbidChangeWeapon: int = 55
    ForbidRestoreArmor: int = 60
    ForbidRestoreHP: int = 59
    FullScanTime: int = 43
    GasDamage: int = 41
    GasFiledDamage: int = 44
    GasRange: int = 40
    GasTime: int = 39
    Goggle: int = 5
    GunDamage: int = 23
    HeatResist: int = 6
    HelpOtherFinishHp: int = 20
    HelpOtherSpeed: int = 2
    Invincible: int = 61
    KillReward: int = 10
    LightRayDamage: int = 36
    LightRayRange: int = 37
    LightRayTime: int = 35
    MagicFieldEffectScaleX: int = 28
    MagicFieldEffectScaleY: int = 29
    MagicFieldEffectScaleZ: int = 30
    MaxArmor: int = 3
    MaxHp: int = 1
    MaxStack: int = 12
    MissileDamage: int = 32
    MissileStrikeCount: int = 31
    MoveDamageReduce: int = 54
    Ninja: int = 4
    ParanoiaDistance: int = 49
    ParanoiaRadius: int = 50
    ParanoiaTime: int = 51
    RecoverArmorSpeed: int = 19
    RecoverArmorTime: int = 24
    RecoverSpeed: int = 11
    SatelliteScanInterval: int = 38
    SatelliteScanRange: int = 34
    SatelliteScanTime: int = 33
    ShadowRange: int = 53
    ShadowTime: int = 52
    ShieldDuration: int = 27
    SkillChargeSpeed: int = 57
    SkillMaxCount: int = 64
    SkillRange: int = 45
    SkillRechargeTime: int = 13
    StorePrice: int = 14
    SupplyProb: int = 8
    TaskReward: int = 9
    UavRecoverArmorSpeed: int = 48
    UseCureItemSpeed: int = 63
    ZombieDamageDown: int = 67
    name_to_values: dict = {'MaxHp': 1, 'HelpOtherSpeed': 2, 'MaxArmor': 3, 'Ninja': 4, 'Goggle': 5, 'HeatResist': 6, 'ANTI_RESTORE_HP_TIME': 7, 'SupplyProb': 8, 'TaskReward': 9, 'KillReward': 10, 'RecoverSpeed': 11, 'MaxStack': 12, 'SkillRechargeTime': 13, 'StorePrice': 14, 'BombDamageRange': 15, 'BombDamage': 16, 'BombBuffRange': 17, 'BombBuffDuration': 18, 'RecoverArmorSpeed': 19, 'HelpOtherFinishHp': 20, 'BackpackFreeSlot': 21, 'AmmoMaxStack': 22, 'GunDamage': 23, 'RecoverArmorTime': 24, 'EnergyValueUp': 26, 'ShieldDuration': 27, 'MagicFieldEffectScaleX': 28, 'MagicFieldEffectScaleY': 29, 'MagicFieldEffectScaleZ': 30, 'MissileStrikeCount': 31, 'MissileDamage': 32, 'SatelliteScanTime': 33, 'SatelliteScanRange': 34, 'LightRayTime': 35, 'LightRayDamage': 36, 'LightRayRange': 37, 'SatelliteScanInterval': 38, 'GasTime': 39, 'GasRange': 40, 'GasDamage': 41, 'CureUavCureSpeed': 42, 'FullScanTime': 43, 'GasFiledDamage': 44, 'SkillRange': 45, 'CannonDamage': 46, 'AssassinateEnergyUp': 47, 'UavRecoverArmorSpeed': 48, 'ParanoiaDistance': 49, 'ParanoiaRadius': 50, 'ParanoiaTime': 51, 'ShadowTime': 52, 'ShadowRange': 53, 'MoveDamageReduce': 54, 'ForbidChangeWeapon': 55, 'EnergySkillChargeSpeed': 56, 'SkillChargeSpeed': 57, 'CureValueUp': 58, 'ForbidRestoreHP': 59, 'ForbidRestoreArmor': 60, 'Invincible': 61, 'BanSprint': 62, 'UseCureItemSpeed': 63, 'SkillMaxCount': 64, 'CureUavRangeUp': 65, 'CureUavTimeUp': 66, 'ZombieDamageDown': 67}
    value_to_names: dict = {1: 'MaxHp', 2: 'HelpOtherSpeed', 3: 'MaxArmor', 4: 'Ninja', 5: 'Goggle', 6: 'HeatResist', 7: 'ANTI_RESTORE_HP_TIME', 8: 'SupplyProb', 9: 'TaskReward', 10: 'KillReward', 11: 'RecoverSpeed', 12: 'MaxStack', 13: 'SkillRechargeTime', 14: 'StorePrice', 15: 'BombDamageRange', 16: 'BombDamage', 17: 'BombBuffRange', 18: 'BombBuffDuration', 19: 'RecoverArmorSpeed', 20: 'HelpOtherFinishHp', 21: 'BackpackFreeSlot', 22: 'AmmoMaxStack', 23: 'GunDamage', 24: 'RecoverArmorTime', 26: 'EnergyValueUp', 27: 'ShieldDuration', 28: 'MagicFieldEffectScaleX', 29: 'MagicFieldEffectScaleY', 30: 'MagicFieldEffectScaleZ', 31: 'MissileStrikeCount', 32: 'MissileDamage', 33: 'SatelliteScanTime', 34: 'SatelliteScanRange', 35: 'LightRayTime', 36: 'LightRayDamage', 37: 'LightRayRange', 38: 'SatelliteScanInterval', 39: 'GasTime', 40: 'GasRange', 41: 'GasDamage', 42: 'CureUavCureSpeed', 43: 'FullScanTime', 44: 'GasFiledDamage', 45: 'SkillRange', 46: 'CannonDamage', 47: 'AssassinateEnergyUp', 48: 'UavRecoverArmorSpeed', 49: 'ParanoiaDistance', 50: 'ParanoiaRadius', 51: 'ParanoiaTime', 52: 'ShadowTime', 53: 'ShadowRange', 54: 'MoveDamageReduce', 55: 'ForbidChangeWeapon', 56: 'EnergySkillChargeSpeed', 57: 'SkillChargeSpeed', 58: 'CureValueUp', 59: 'ForbidRestoreHP', 60: 'ForbidRestoreArmor', 61: 'Invincible', 62: 'BanSprint', 63: 'UseCureItemSpeed', 64: 'SkillMaxCount', 65: 'CureUavRangeUp', 66: 'CureUavTimeUp', 67: 'ZombieDamageDown'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class OptionKey(enum):
    AirdropStore: str = 'airdrop_store'
    AirdropSword: str = 'airdrop_sword'
    Airdrops: str = 'airdrop'
    AssistAim: str = 'assist_aim'
    AutoReborn: str = 'relive'
    BattleTime: str = 'time'
    CanBuyTacticalLevel: str = 'can_buy_tactical_level'
    Coins: str = 'coins_range'
    DamageTeammate: str = 'damage_teammate'
    DisableBot: str = 'disable_bot'
    DisableSkill: str = 'disable_skill'
    ForbidAssistAim: str = 'forbid_assist_aim'
    HS_ONLY: str = 'hs_only'
    InfAmmo: str = 'infinite_ammo'
    InitTacticalLevel: str = 'tactical_level'
    LeaderMode: str = 'leader_mode'
    MaxArmor: str = 'maxarmor'
    MaxHp: str = 'max_hp'
    NoDeathTactical: str = 'disable_death_tactical_energy'
    PutInVehicle: str = 'vehicle'
    RoundToWin: str = 'round_to_win'
    Rounds: str = 'round_range'
    SafeRegionDamage: str = 'safe_region_damage'
    SafeRegionSpeed: str = 'safe_region_speed'
    Score: str = 'score'
    TaskCount: str = 'task_count'
    TaskType: str = 'task_type'
    WeatherType: str = 'weather'
    ZombieBuyback: str = 'zombie_buyback'
    ZombieHp: str = 'zombie_hp'
    ZombieRebornItem: str = 'zombie_reborn_item'
    ZombieRevive: str = 'zombie_revive'
    name_to_values: dict = {'MaxHp': 'max_hp', 'MaxArmor': 'maxarmor', 'DamageTeammate': 'damage_teammate', 'InfAmmo': 'infinite_ammo', 'DisableSkill': 'disable_skill', 'ForbidAssistAim': 'forbid_assist_aim', 'Rounds': 'round_range', 'LeaderMode': 'leader_mode', 'RoundToWin': 'round_to_win', 'Coins': 'coins_range', 'InitTacticalLevel': 'tactical_level', 'CanBuyTacticalLevel': 'can_buy_tactical_level', 'AutoReborn': 'relive', 'WeatherType': 'weather', 'PutInVehicle': 'vehicle', 'SafeRegionSpeed': 'safe_region_speed', 'SafeRegionDamage': 'safe_region_damage', 'Airdrops': 'airdrop', 'TaskCount': 'task_count', 'TaskType': 'task_type', 'AirdropStore': 'airdrop_store', 'AssistAim': 'assist_aim', 'DisableBot': 'disable_bot', 'NoDeathTactical': 'disable_death_tactical_energy', 'Score': 'score', 'BattleTime': 'time', 'AirdropSword': 'airdrop_sword', 'ZombieRevive': 'zombie_revive', 'ZombieHp': 'zombie_hp', 'ZombieRebornItem': 'zombie_reborn_item', 'ZombieBuyback': 'zombie_buyback', 'HS_ONLY': 'hs_only'}
    value_to_names: dict = {'max_hp': 'MaxHp', 'maxarmor': 'MaxArmor', 'damage_teammate': 'DamageTeammate', 'infinite_ammo': 'InfAmmo', 'disable_skill': 'DisableSkill', 'forbid_assist_aim': 'ForbidAssistAim', 'round_range': 'Rounds', 'leader_mode': 'LeaderMode', 'round_to_win': 'RoundToWin', 'coins_range': 'Coins', 'tactical_level': 'InitTacticalLevel', 'can_buy_tactical_level': 'CanBuyTacticalLevel', 'relive': 'AutoReborn', 'weather': 'WeatherType', 'vehicle': 'PutInVehicle', 'safe_region_speed': 'SafeRegionSpeed', 'safe_region_damage': 'SafeRegionDamage', 'airdrop': 'Airdrops', 'task_count': 'TaskCount', 'task_type': 'TaskType', 'airdrop_store': 'AirdropStore', 'assist_aim': 'AssistAim', 'disable_bot': 'DisableBot', 'disable_death_tactical_energy': 'NoDeathTactical', 'score': 'Score', 'time': 'BattleTime', 'airdrop_sword': 'AirdropSword', 'zombie_revive': 'ZombieRevive', 'zombie_hp': 'ZombieHp', 'zombie_reborn_item': 'ZombieRebornItem', 'zombie_buyback': 'ZombieBuyback', 'hs_only': 'HS_ONLY'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ParaAvatarReason(enum):
    Airplane: int = 1
    Born: int = 0
    HighSky: int = 3
    Reborn: int = 2
    Transfer: int = 4
    name_to_values: dict = {'Born': 0, 'Airplane': 1, 'Reborn': 2, 'HighSky': 3, 'Transfer': 4}
    value_to_names: dict = {0: 'Born', 1: 'Airplane', 2: 'Reborn', 3: 'HighSky', 4: 'Transfer'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...


def Add3DText(guid, text, position, text_color=(255, 0, 0, 255), scale=(0.01, 0.01, 0.01), rotation=(0, 0, 0)): ...
def BuildBackpackArmorDetailDesc(): ...
def GetGameSoundData(): ...
def GetListviewCreateNodeNum(listview): ...
def GetListviewCreateNodeNumHorizontal(listview): ...
def GetMaxGunTagLength(): ...
def GetMoneyShowForKM(money): ...
def GetSkillNodeCls(): ...
def GetUIImageRadiusInMapTagData(map_tag_id): ...
def GetWeaponAmmo(weapon, player): ...
def HasBanItemPickUp(combatitem): ...
def Hide3DText(guid): ...
def HideAll3DText(): ...
def IsMobaMainUIFirstVersion(): ...
def IsMobaMainUISecondVersion(): ...
def NeedSoloReviveNode(): ...
def SecondToShowTime(second): ...


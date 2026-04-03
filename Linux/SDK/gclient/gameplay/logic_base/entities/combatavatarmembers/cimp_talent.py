# module: gclient.gameplay.logic_base.entities.combatavatarmembers.cimp_talent

import cconst
import weapon_util

class CombatAvatarMember(object):
    def DealScatterOffsetByTalent(self, scatter_offset): ...
    def HasTalent(self, talent_id): ...
    def HasTalentCode(self, talent_code): ...

class HumanoidMonsterTalent(CombatAvatarMember):
    def DealScatterOffsetByTalent(self, scatter_offset): ...
    def HasTalent(self, talent_id): ...
    def HasTalentCode(self, talent_code): ...

class PlayerCombatAvatarMember(CombatAvatarMember):
    def CheckTalentRemoteShotDamageUp(self, weapon_id): ...
    def DealCheckCanEnterStateRelationshipByTalent(self, state, check_result): ...
    def DealJumpVelocityYByTalent(self, jump_velocity_y, accumulated_time): ...
    def DealRecoilDataByTalent(self, is_real_ads, shoot_idx, real_recoil_data): ...
    def DealScatterOffsetByTalent(self, scatter_offset): ...
    def DealStopSprintByTalent(self, by_state): ...
    def HasTalent(self, talent_id): ...
    def HasTalentCode(self, talent_code): ...

class TalentCode(enum):
    ADS_FLASH: int = 3
    AccumulateJump: int = 59
    AdaptSurmount1: int = 20
    AdaptSurmount2: int = 21
    AdaptSurmount3: int = 22
    AddSkillCountByKA: int = 89
    AdsMarkPos: int = 41
    AdsShield: int = 35
    ArmorEnergy: int = 116
    AssassinateChange1: int = 80
    AssassinateChange2: int = 81
    AttackHolographicRobot: int = 118
    BackWeakenDamage: int = 63
    BrokenArmorGenSmoke: int = 47
    BurnAmmo: int = 86
    CRISIS_AWARENESS: int = 2
    CannonSlowTarget: int = 69
    CannonUpgrade: int = 70
    ChangeSkill: int = 65
    ChangeSkillEntry: int = 67
    CoinsShield: int = 56
    Collection: int = 7
    CoolBlood: int = 11
    DamageShow: int = 13
    DamageSlowArmor: int = 87
    DamageSurmount1: int = 17
    DamageSurmount2: int = 18
    DamageSurmount3: int = 19
    DamageTalent5: int = 30
    DebuffEffectUp: int = 48
    Discount: int = 12
    DyingArmor: int = 31
    EnemyTrack: int = 4
    EnergySkillUpgrade: int = 43
    EnergySkillValueUp: int = 49
    EnergyTransfer: int = 55
    ExposeKillerToTeam: int = 37
    FeelLowHp: int = 83
    FeelSurmount1: int = 26
    FeelSurmount2: int = 27
    FeelSurmount3: int = 28
    FiringRecoilStable: int = 51
    GasPassiveSkill: int = 102
    GrenadeEnhance: int = 34
    HeadShotWeakenDamage: int = 64
    HighAlart: int = 33
    HitRecoverArmor: int = 57
    HitSlowDown: int = 15
    HitXrayToTeam: int = 61
    IceArmorRecoverSpeed: int = 100
    IceExtraArmor: int = 101
    InfoShielding: int = 36
    InitialRecoilStable: int = 53
    KillAddAmmo: int = 32
    KillEnemyMarkPos: int = 40
    KneeJerkReflex: int = 6
    LOCK: int = 1
    LuckyBulletDamage: int = 62
    MaxArmorToMaxHp: int = 46
    Radar: int = 14
    ReduceFallHurt: int = 45
    RemoteShotDamageUp: int = 52
    ResistTalent: int = 54
    Ruthless: int = 5
    SensingAroundEnemies: int = 110
    ShieldImpuls: int = 82
    ShieldWeakenDamage: int = 42
    ShowHitMe: int = 84
    SignalBan: int = 10
    Silencer: int = 8
    SlideAddAmmo: int = 29
    SlideAssault: int = 58
    SpecialCredit: int = 9
    SpecialMeleeAttack: int = 115
    SpeedLevelWeakenDamage: int = 38
    SpeedUpSkillByKA: int = 88
    SplitGrenade: int = 16
    SprintFiring: int = 60
    SuperCross: int = 44
    SurviveSurmount1: int = 23
    SurviveSurmount2: int = 24
    TeammateCue: int = 25
    ThrowableBombEffect: int = 50
    Trophies: int = 85
    UpgradeGunDamageInRange: int = 39
    UsingCureUav: int = 117
    name_to_values: dict = {'LOCK': 1, 'CRISIS_AWARENESS': 2, 'ADS_FLASH': 3, 'EnemyTrack': 4, 'Ruthless': 5, 'KneeJerkReflex': 6, 'Collection': 7, 'Silencer': 8, 'SpecialCredit': 9, 'SignalBan': 10, 'CoolBlood': 11, 'Discount': 12, 'DamageShow': 13, 'Radar': 14, 'HitSlowDown': 15, 'SplitGrenade': 16, 'DamageSurmount1': 17, 'DamageSurmount2': 18, 'DamageSurmount3': 19, 'AdaptSurmount1': 20, 'AdaptSurmount2': 21, 'AdaptSurmount3': 22, 'SurviveSurmount1': 23, 'SurviveSurmount2': 24, 'TeammateCue': 25, 'FeelSurmount1': 26, 'FeelSurmount2': 27, 'FeelSurmount3': 28, 'SlideAddAmmo': 29, 'DamageTalent5': 30, 'DyingArmor': 31, 'KillAddAmmo': 32, 'HighAlart': 33, 'GrenadeEnhance': 34, 'AdsShield': 35, 'InfoShielding': 36, 'ExposeKillerToTeam': 37, 'SpeedLevelWeakenDamage': 38, 'UpgradeGunDamageInRange': 39, 'KillEnemyMarkPos': 40, 'AdsMarkPos': 41, 'ShieldWeakenDamage': 42, 'EnergySkillUpgrade': 43, 'SuperCross': 44, 'ReduceFallHurt': 45, 'MaxArmorToMaxHp': 46, 'BrokenArmorGenSmoke': 47, 'DebuffEffectUp': 48, 'EnergySkillValueUp': 49, 'ThrowableBombEffect': 50, 'FiringRecoilStable': 51, 'RemoteShotDamageUp': 52, 'InitialRecoilStable': 53, 'ResistTalent': 54, 'EnergyTransfer': 55, 'CoinsShield': 56, 'HitRecoverArmor': 57, 'SlideAssault': 58, 'AccumulateJump': 59, 'SprintFiring': 60, 'HitXrayToTeam': 61, 'LuckyBulletDamage': 62, 'BackWeakenDamage': 63, 'HeadShotWeakenDamage': 64, 'ChangeSkill': 65, 'ChangeSkillEntry': 67, 'CannonSlowTarget': 69, 'CannonUpgrade': 70, 'AssassinateChange1': 80, 'AssassinateChange2': 81, 'ShieldImpuls': 82, 'FeelLowHp': 83, 'ShowHitMe': 84, 'Trophies': 85, 'BurnAmmo': 86, 'DamageSlowArmor': 87, 'SpeedUpSkillByKA': 88, 'AddSkillCountByKA': 89, 'IceArmorRecoverSpeed': 100, 'IceExtraArmor': 101, 'GasPassiveSkill': 102, 'SensingAroundEnemies': 110, 'SpecialMeleeAttack': 115, 'ArmorEnergy': 116, 'UsingCureUav': 117, 'AttackHolographicRobot': 118}
    value_to_names: dict = {1: 'LOCK', 2: 'CRISIS_AWARENESS', 3: 'ADS_FLASH', 4: 'EnemyTrack', 5: 'Ruthless', 6: 'KneeJerkReflex', 7: 'Collection', 8: 'Silencer', 9: 'SpecialCredit', 10: 'SignalBan', 11: 'CoolBlood', 12: 'Discount', 13: 'DamageShow', 14: 'Radar', 15: 'HitSlowDown', 16: 'SplitGrenade', 17: 'DamageSurmount1', 18: 'DamageSurmount2', 19: 'DamageSurmount3', 20: 'AdaptSurmount1', 21: 'AdaptSurmount2', 22: 'AdaptSurmount3', 23: 'SurviveSurmount1', 24: 'SurviveSurmount2', 25: 'TeammateCue', 26: 'FeelSurmount1', 27: 'FeelSurmount2', 28: 'FeelSurmount3', 29: 'SlideAddAmmo', 30: 'DamageTalent5', 31: 'DyingArmor', 32: 'KillAddAmmo', 33: 'HighAlart', 34: 'GrenadeEnhance', 35: 'AdsShield', 36: 'InfoShielding', 37: 'ExposeKillerToTeam', 38: 'SpeedLevelWeakenDamage', 39: 'UpgradeGunDamageInRange', 40: 'KillEnemyMarkPos', 41: 'AdsMarkPos', 42: 'ShieldWeakenDamage', 43: 'EnergySkillUpgrade', 44: 'SuperCross', 45: 'ReduceFallHurt', 46: 'MaxArmorToMaxHp', 47: 'BrokenArmorGenSmoke', 48: 'DebuffEffectUp', 49: 'EnergySkillValueUp', 50: 'ThrowableBombEffect', 51: 'FiringRecoilStable', 52: 'RemoteShotDamageUp', 53: 'InitialRecoilStable', 54: 'ResistTalent', 55: 'EnergyTransfer', 56: 'CoinsShield', 57: 'HitRecoverArmor', 58: 'SlideAssault', 59: 'AccumulateJump', 60: 'SprintFiring', 61: 'HitXrayToTeam', 62: 'LuckyBulletDamage', 63: 'BackWeakenDamage', 64: 'HeadShotWeakenDamage', 65: 'ChangeSkill', 67: 'ChangeSkillEntry', 69: 'CannonSlowTarget', 70: 'CannonUpgrade', 80: 'AssassinateChange1', 81: 'AssassinateChange2', 82: 'ShieldImpuls', 83: 'FeelLowHp', 84: 'ShowHitMe', 85: 'Trophies', 86: 'BurnAmmo', 87: 'DamageSlowArmor', 88: 'SpeedUpSkillByKA', 89: 'AddSkillCountByKA', 100: 'IceArmorRecoverSpeed', 101: 'IceExtraArmor', 102: 'GasPassiveSkill', 110: 'SensingAroundEnemies', 115: 'SpecialMeleeAttack', 116: 'ArmorEnergy', 117: 'UsingCureUav', 118: 'AttackHolographicRobot'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...



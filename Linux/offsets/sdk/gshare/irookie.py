# module: gshare.irookie

import six2

AUTO_FINISH_GUIDES: dict = {1: [40, 41, 42, 43, 44, 45, 46, 47, 48]}
CurGuideVersion: int = 56
TYPE_OFFSET: int = 60
_reload_all: bool = True

class CombatGuideType(enum):
    BeHuntGuide: int = 1207
    Begin: int = 1200
    End: int = 1259
    HighSkyParachute: int = 1208
    HuntGuide: int = 1206
    MedicineRecommend: int = 1215
    SafeRegionAlert: int = 1214
    ShopGuide: int = 1202
    ShopMedicineGuide: int = 1216
    SkillGuide: int = 1204
    SlideGuide: int = 1209
    StropGuide: int = 1201
    StropUavGuide: int = 1210
    TacticalUpgradeGuide: int = 1211
    UavGuide: int = 1205
    VehicleGuide: int = 1203
    WeaponQualityGuide: int = 1213
    name_to_values: dict = {'Begin': 1200, 'StropGuide': 1201, 'ShopGuide': 1202, 'VehicleGuide': 1203, 'SkillGuide': 1204, 'UavGuide': 1205, 'HuntGuide': 1206, 'BeHuntGuide': 1207, 'HighSkyParachute': 1208, 'SlideGuide': 1209, 'StropUavGuide': 1210, 'TacticalUpgradeGuide': 1211, 'WeaponQualityGuide': 1213, 'SafeRegionAlert': 1214, 'MedicineRecommend': 1215, 'ShopMedicineGuide': 1216, 'End': 1259}
    value_to_names: dict = {1200: 'Begin', 1201: 'StropGuide', 1202: 'ShopGuide', 1203: 'VehicleGuide', 1204: 'SkillGuide', 1205: 'UavGuide', 1206: 'HuntGuide', 1207: 'BeHuntGuide', 1208: 'HighSkyParachute', 1209: 'SlideGuide', 1210: 'StropUavGuide', 1211: 'TacticalUpgradeGuide', 1213: 'WeaponQualityGuide', 1214: 'SafeRegionAlert', 1215: 'MedicineRecommend', 1216: 'ShopMedicineGuide', 1259: 'End'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CustomMapType(area_map):
    IS_CUSTOM_TYPE: bool = True
    clear: method_descriptor = <method 'clear' of 'area_map' objects>
    copy: method_descriptor = <method 'copy' of 'area_map' objects>
    dict: method_descriptor = <method 'dict' of 'area_map' objects>
    dsize: method_descriptor = <method 'dsize' of 'area_map' objects>
    get: method_descriptor = <method 'get' of 'area_map' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_map' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_map' objects>
    iteritems: method_descriptor = <method 'iteritems' of 'area_map' objects>
    iterkeys: method_descriptor = <method 'iterkeys' of 'area_map' objects>
    itervalues: method_descriptor = <method 'itervalues' of 'area_map' objects>
    normal_iteritems: method_descriptor = <method 'normal_iteritems' of 'area_map' objects>
    normal_iterkeys: method_descriptor = <method 'normal_iterkeys' of 'area_map' objects>
    normal_itervalues: method_descriptor = <method 'normal_itervalues' of 'area_map' objects>
    pop: method_descriptor = <method 'pop' of 'area_map' objects>
    props_all: method_descriptor = <method 'props_all' of 'area_map' objects>
    size: method_descriptor = <method 'size' of 'area_map' objects>
    total_size: method_descriptor = <method 'total_size' of 'area_map' objects>
    update: method_descriptor = <method 'update' of 'area_map' objects>
    weak_dict: method_descriptor = <method 'weak_dict' of 'area_map' objects>

    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class GuideType(enum):
    Airdrop: int = 2
    AppScore: int = 8
    Backpack: int = 6
    Coin: int = 1
    End: int = 50
    FallParachateGuide: int = 48
    FriendLike: int = 34
    GunArmory: int = 35
    GunOverview: int = 36
    HallFirstMatch: int = 30
    HallFirstNewGunPart: int = 28
    HallLegend: int = 26
    HallPersonalShare: int = 25
    HallPersonalSpace: int = 24
    HallRankGunGod: int = 32
    HallRankGunShare: int = 33
    HallRecruit: int = 27
    HallSecondMatch: int = 23
    HallWarehouseGuiseSkin: int = 29
    InspectionGuide: int = 40
    LeaderboardLocating: int = 31
    LevelChoice: int = 5
    MobaFirstBuyAmmo: int = 19
    MobaFirstCallAirdrop: int = 16
    MobaFirstCallUav: int = 22
    MobaFirstCloseParachute: int = 12
    MobaFirstFindSupply: int = 14
    MobaFirstMarkLocation: int = 10
    MobaFirstOpenParachute: int = 11
    MobaFirstOutSafeRegion: int = 18
    MobaFirstPickAirdrop: int = 17
    MobaFirstPickupTacticalEnergy: int = 13
    MobaFirstSkill: int = 9
    MobaFirstTacticalUpgrade: int = 15
    MobaFirstUseSkill: int = 21
    MobaFirstUseStrop: int = 20
    PickupAirdropGuide: int = 47
    Reborn: int = 4
    Reward: int = 7
    ShopGuide: int = 41
    Skill: int = 3
    SkillGuide: int = 44
    SkinMetal: int = 38
    StropGuide: int = 45
    SystemAirdropGuide: int = 46
    TrialBackpackGuide: int = 49
    UavAgainGuide: int = 43
    UavGuide: int = 42
    V6Gacha: int = 37
    name_to_values: dict = {'Coin': 1, 'Airdrop': 2, 'Skill': 3, 'Reborn': 4, 'LevelChoice': 5, 'Backpack': 6, 'Reward': 7, 'AppScore': 8, 'MobaFirstSkill': 9, 'MobaFirstMarkLocation': 10, 'MobaFirstOpenParachute': 11, 'MobaFirstCloseParachute': 12, 'MobaFirstPickupTacticalEnergy': 13, 'MobaFirstFindSupply': 14, 'MobaFirstTacticalUpgrade': 15, 'MobaFirstCallAirdrop': 16, 'MobaFirstPickAirdrop': 17, 'MobaFirstOutSafeRegion': 18, 'MobaFirstBuyAmmo': 19, 'MobaFirstUseStrop': 20, 'MobaFirstUseSkill': 21, 'MobaFirstCallUav': 22, 'HallSecondMatch': 23, 'HallPersonalSpace': 24, 'HallPersonalShare': 25, 'HallLegend': 26, 'HallRecruit': 27, 'HallFirstNewGunPart': 28, 'HallWarehouseGuiseSkin': 29, 'HallFirstMatch': 30, 'LeaderboardLocating': 31, 'HallRankGunGod': 32, 'HallRankGunShare': 33, 'FriendLike': 34, 'GunArmory': 35, 'GunOverview': 36, 'V6Gacha': 37, 'SkinMetal': 38, 'InspectionGuide': 40, 'ShopGuide': 41, 'UavGuide': 42, 'UavAgainGuide': 43, 'SkillGuide': 44, 'StropGuide': 45, 'SystemAirdropGuide': 46, 'PickupAirdropGuide': 47, 'FallParachateGuide': 48, 'TrialBackpackGuide': 49, 'End': 50}
    value_to_names: dict = {1: 'Coin', 2: 'Airdrop', 3: 'Skill', 4: 'Reborn', 5: 'LevelChoice', 6: 'Backpack', 7: 'Reward', 8: 'AppScore', 9: 'MobaFirstSkill', 10: 'MobaFirstMarkLocation', 11: 'MobaFirstOpenParachute', 12: 'MobaFirstCloseParachute', 13: 'MobaFirstPickupTacticalEnergy', 14: 'MobaFirstFindSupply', 15: 'MobaFirstTacticalUpgrade', 16: 'MobaFirstCallAirdrop', 17: 'MobaFirstPickAirdrop', 18: 'MobaFirstOutSafeRegion', 19: 'MobaFirstBuyAmmo', 20: 'MobaFirstUseStrop', 21: 'MobaFirstUseSkill', 22: 'MobaFirstCallUav', 23: 'HallSecondMatch', 24: 'HallPersonalSpace', 25: 'HallPersonalShare', 26: 'HallLegend', 27: 'HallRecruit', 28: 'HallFirstNewGunPart', 29: 'HallWarehouseGuiseSkin', 30: 'HallFirstMatch', 31: 'LeaderboardLocating', 32: 'HallRankGunGod', 33: 'HallRankGunShare', 34: 'FriendLike', 35: 'GunArmory', 36: 'GunOverview', 37: 'V6Gacha', 38: 'SkinMetal', 40: 'InspectionGuide', 41: 'ShopGuide', 42: 'UavGuide', 43: 'UavAgainGuide', 44: 'SkillGuide', 45: 'StropGuide', 46: 'SystemAirdropGuide', 47: 'PickupAirdropGuide', 48: 'FallParachateGuide', 49: 'TrialBackpackGuide', 50: 'End'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GuideTypeNew(enum):
    MobaFirstAirdrop: int = 610
    MobaFirstFirstKill: int = 604
    MobaFirstFirstPickup: int = 605
    MobaFirstKillTwoRobot: int = 608
    MobaFirstLeaveAirplane: int = 601
    MobaFirstLookAtAirdrop: int = 609
    MobaFirstOpenParachute: int = 602
    MobaFirstOutSafeRegion: int = 611
    MobaFirstPurplePickup: int = 606
    MobaFirstShowSafeRegion: int = 612
    MobaFirstSkill: int = 600
    MobaFirstTacticalUpgrade: int = 607
    MobaFirstTurnView: int = 603
    name_to_values: dict = {'MobaFirstSkill': 600, 'MobaFirstLeaveAirplane': 601, 'MobaFirstOpenParachute': 602, 'MobaFirstTurnView': 603, 'MobaFirstFirstKill': 604, 'MobaFirstFirstPickup': 605, 'MobaFirstPurplePickup': 606, 'MobaFirstTacticalUpgrade': 607, 'MobaFirstKillTwoRobot': 608, 'MobaFirstLookAtAirdrop': 609, 'MobaFirstAirdrop': 610, 'MobaFirstOutSafeRegion': 611, 'MobaFirstShowSafeRegion': 612}
    value_to_names: dict = {600: 'MobaFirstSkill', 601: 'MobaFirstLeaveAirplane', 602: 'MobaFirstOpenParachute', 603: 'MobaFirstTurnView', 604: 'MobaFirstFirstKill', 605: 'MobaFirstFirstPickup', 606: 'MobaFirstPurplePickup', 607: 'MobaFirstTacticalUpgrade', 608: 'MobaFirstKillTwoRobot', 609: 'MobaFirstLookAtAirdrop', 610: 'MobaFirstAirdrop', 611: 'MobaFirstOutSafeRegion', 612: 'MobaFirstShowSafeRegion'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GuideVersion(enum):
    Default: int = 0
    New: int = 2
    NewGuideUI: int = 32
    NewMobaFirst: int = 16
    NewRookieGuide: int = 8
    V20240325: int = 1
    name_to_values: dict = {'Default': 0, 'V20240325': 1, 'New': 2, 'NewRookieGuide': 8, 'NewMobaFirst': 16, 'NewGuideUI': 32}
    value_to_names: dict = {0: 'Default', 1: 'V20240325', 2: 'New', 8: 'NewRookieGuide', 16: 'NewMobaFirst', 32: 'NewGuideUI'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class HallGuideType(enum):
    ClanEntrance: int = 1818
    ClanFilter: int = 1821
    ClanInfo: int = 1820
    ClanList: int = 1819
    ClanRefresh: int = 1822
    GunGuiseAppearance: int = 1831
    GunGuiseChoose: int = 1832
    GunGuiseEmma: int = 1828
    GunGuiseEntrance: int = 1829
    GunGuiseEquip: int = 1833
    GunGuiseGun: int = 1830
    GunGuiseTry: int = 1834
    GunSelectDrawer: int = 1862
    GunSmithAIRecommend: int = 1812
    GunSmithApplyRecommend: int = 1813
    GunSmithEmma: int = 1807
    GunSmithEntrance: int = 1808
    GunSmithGun: int = 1809
    GunSmithModity: int = 1810
    GunSmithRecommend: int = 1811
    GunSmithTry: int = 1814
    GunSysEntrance: int = 1864
    HeroEmma: int = 1800
    HeroEmmaSkill: int = 1804
    HeroEntrance: int = 1801
    HeroFavor: int = 1805
    HeroNew: int = 1802
    HeroSkill: int = 1803
    HeroSkinChoose: int = 1857
    HeroSkinClaim: int = 1854
    HeroSkinConfirm: int = 1853
    HeroSkinDetails: int = 1856
    HeroSkinEmma: int = 1860
    HeroSkinEntrance: int = 1855
    HeroSkinEquip: int = 1858
    HeroSkinTry: int = 1859
    HeroTry: int = 1806
    LegendMedal: int = 1863
    NewbieEmma: int = 1852
    NewbieEntrance: int = 1851
    NobleCoin: int = 1835
    NobleCoinUse: int = 1836
    NobleEmma: int = 1837
    PassBigReward: int = 1841
    PassElite: int = 1843
    PassEntrance: int = 1838
    PassGo: int = 1839
    PassMission: int = 1845
    PassPremium: int = 1844
    PassRewards: int = 1840
    PassUpgrade: int = 1842
    PassWeeklyMission: int = 1846
    PersonalInfoEmma: int = 1849
    PersonalInfoEntrance: int = 1847
    PersonalInfoSetting: int = 1848
    PersonalInfoTitle: int = 1850
    RankedEmma: int = 1815
    RankedEntrance: int = 1816
    RankedReward: int = 1817
    SkinMetal: int = 1861
    StashChoose: int = 1824
    StashConfirm: int = 1826
    StashEmma: int = 1827
    StashEntrance: int = 1823
    StashTen: int = 1825
    name_to_values: dict = {'HeroEmma': 1800, 'HeroEntrance': 1801, 'HeroNew': 1802, 'HeroSkill': 1803, 'HeroEmmaSkill': 1804, 'HeroFavor': 1805, 'HeroTry': 1806, 'GunSmithEmma': 1807, 'GunSmithEntrance': 1808, 'GunSmithGun': 1809, 'GunSmithModity': 1810, 'GunSmithRecommend': 1811, 'GunSmithAIRecommend': 1812, 'GunSmithApplyRecommend': 1813, 'GunSmithTry': 1814, 'RankedEmma': 1815, 'RankedEntrance': 1816, 'RankedReward': 1817, 'ClanEntrance': 1818, 'ClanList': 1819, 'ClanInfo': 1820, 'ClanFilter': 1821, 'ClanRefresh': 1822, 'StashEntrance': 1823, 'StashChoose': 1824, 'StashTen': 1825, 'StashConfirm': 1826, 'StashEmma': 1827, 'GunGuiseEmma': 1828, 'GunGuiseEntrance': 1829, 'GunGuiseGun': 1830, 'GunGuiseAppearance': 1831, 'GunGuiseChoose': 1832, 'GunGuiseEquip': 1833, 'GunGuiseTry': 1834, 'NobleCoin': 1835, 'NobleCoinUse': 1836, 'NobleEmma': 1837, 'PassEntrance': 1838, 'PassGo': 1839, 'PassRewards': 1840, 'PassBigReward': 1841, 'PassUpgrade': 1842, 'PassElite': 1843, 'PassPremium': 1844, 'PassMission': 1845, 'PassWeeklyMission': 1846, 'PersonalInfoEntrance': 1847, 'PersonalInfoSetting': 1848, 'PersonalInfoEmma': 1849, 'PersonalInfoTitle': 1850, 'NewbieEntrance': 1851, 'NewbieEmma': 1852, 'HeroSkinConfirm': 1853, 'HeroSkinClaim': 1854, 'HeroSkinEntrance': 1855, 'HeroSkinDetails': 1856, 'HeroSkinChoose': 1857, 'HeroSkinEquip': 1858, 'HeroSkinTry': 1859, 'HeroSkinEmma': 1860, 'SkinMetal': 1861, 'GunSelectDrawer': 1862, 'LegendMedal': 1863, 'GunSysEntrance': 1864}
    value_to_names: dict = {1800: 'HeroEmma', 1801: 'HeroEntrance', 1802: 'HeroNew', 1803: 'HeroSkill', 1804: 'HeroEmmaSkill', 1805: 'HeroFavor', 1806: 'HeroTry', 1807: 'GunSmithEmma', 1808: 'GunSmithEntrance', 1809: 'GunSmithGun', 1810: 'GunSmithModity', 1811: 'GunSmithRecommend', 1812: 'GunSmithAIRecommend', 1813: 'GunSmithApplyRecommend', 1814: 'GunSmithTry', 1815: 'RankedEmma', 1816: 'RankedEntrance', 1817: 'RankedReward', 1818: 'ClanEntrance', 1819: 'ClanList', 1820: 'ClanInfo', 1821: 'ClanFilter', 1822: 'ClanRefresh', 1823: 'StashEntrance', 1824: 'StashChoose', 1825: 'StashTen', 1826: 'StashConfirm', 1827: 'StashEmma', 1828: 'GunGuiseEmma', 1829: 'GunGuiseEntrance', 1830: 'GunGuiseGun', 1831: 'GunGuiseAppearance', 1832: 'GunGuiseChoose', 1833: 'GunGuiseEquip', 1834: 'GunGuiseTry', 1835: 'NobleCoin', 1836: 'NobleCoinUse', 1837: 'NobleEmma', 1838: 'PassEntrance', 1839: 'PassGo', 1840: 'PassRewards', 1841: 'PassBigReward', 1842: 'PassUpgrade', 1843: 'PassElite', 1844: 'PassPremium', 1845: 'PassMission', 1846: 'PassWeeklyMission', 1847: 'PersonalInfoEntrance', 1848: 'PersonalInfoSetting', 1849: 'PersonalInfoEmma', 1850: 'PersonalInfoTitle', 1851: 'NewbieEntrance', 1852: 'NewbieEmma', 1853: 'HeroSkinConfirm', 1854: 'HeroSkinClaim', 1855: 'HeroSkinEntrance', 1856: 'HeroSkinDetails', 1857: 'HeroSkinChoose', 1858: 'HeroSkinEquip', 1859: 'HeroSkinTry', 1860: 'HeroSkinEmma', 1861: 'SkinMetal', 1862: 'GunSelectDrawer', 1863: 'LegendMedal', 1864: 'GunSysEntrance'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class NewerGuideRecord(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    clear: method_descriptor = <method 'clear' of 'area_map' objects>
    copy: method_descriptor = <method 'copy' of 'area_map' objects>
    dict: method_descriptor = <method 'dict' of 'area_map' objects>
    dsize: method_descriptor = <method 'dsize' of 'area_map' objects>
    get: method_descriptor = <method 'get' of 'area_map' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_map' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_map' objects>
    iteritems: method_descriptor = <method 'iteritems' of 'area_map' objects>
    iterkeys: method_descriptor = <method 'iterkeys' of 'area_map' objects>
    itervalues: method_descriptor = <method 'itervalues' of 'area_map' objects>
    normal_iteritems: method_descriptor = <method 'normal_iteritems' of 'area_map' objects>
    normal_iterkeys: method_descriptor = <method 'normal_iterkeys' of 'area_map' objects>
    normal_itervalues: method_descriptor = <method 'normal_itervalues' of 'area_map' objects>
    pop: method_descriptor = <method 'pop' of 'area_map' objects>
    props_all: method_descriptor = <method 'props_all' of 'area_map' objects>
    size: method_descriptor = <method 'size' of 'area_map' objects>
    total_size: method_descriptor = <method 'total_size' of 'area_map' objects>
    update: method_descriptor = <method 'update' of 'area_map' objects>
    weak_dict: method_descriptor = <method 'weak_dict' of 'area_map' objects>

    def ClearCombatGuide(self): ...
    def ClearHallGuide(self): ...
    def FinishCombatGuide(self, guide_type): ...
    def FinishGuide(self, guide_type): ...
    def HasBit(self, guide_type): ...
    def HasCombatGuide(self, guide_type): ...
    def HasGuide(self, guide_type): ...
    def HasGuideNew(self, guide_type): ...
    def SetBit(self, guide_type): ...
    def TransferRecord(self): ...
    def _initProperty(self, data): ...
    @property
    def debug(self): ...    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class enum(object):
    name_to_values: dict = {}
    value_to_names: dict = {}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...


def IsMobaFirstNew(guide_type): ...
def IsMobaFirstOld(guide_type): ...
def IsUIIdNew(guide_type): ...
def IsUIIdOld(guide_type): ...
def Property(name, default, flag=2): ...
def UseNewGuideUI(avatar): ...
def UseNewMobaFirst(avatar): ...
def UseNewRookieGuide(avatar): ...


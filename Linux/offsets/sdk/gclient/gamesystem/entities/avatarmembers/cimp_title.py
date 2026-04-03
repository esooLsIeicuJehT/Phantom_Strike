# module: gclient.gamesystem.entities.avatarmembers.cimp_title

import consts
import equip_data
import events
import gun_mod_data
import gunmaster_leaderboard_data
import lbs_const
import location_util
import six2

CLIENT_ONLY: int = 1
LocalConfig: _LocalConfig = <gclient.config._LocalConfig object at 0x7040bf6d50>
SERVER_ONLY: int = 4

class CCurTitle(Title):
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
    @property
    def begin_time(self): ...    @property
    def expired_time(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def proto(self): ...    @property
    def rank_key(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    @property
    def valid(self): ...    def values(self): ...

class CCurTitles(Titles):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gclient.gamesystem.entities.avatarmembers.cimp_title.CCurTitle'>
    append: method_descriptor = <method 'append' of 'area_list' objects>
    assign: method_descriptor = <method 'assign' of 'area_list' objects>
    clear: method_descriptor = <method 'clear' of 'area_list' objects>
    copy: method_descriptor = <method 'copy' of 'area_list' objects>
    delete: method_descriptor = <method 'delete' of 'area_list' objects>
    extend: method_descriptor = <method 'extend' of 'area_list' objects>
    get: method_descriptor = <method 'get' of 'area_list' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_list' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_list' objects>
    insert: method_descriptor = <method 'insert' of 'area_list' objects>
    list: method_descriptor = <method 'list' of 'area_list' objects>
    pop: method_descriptor = <method 'pop' of 'area_list' objects>
    size: method_descriptor = <method 'size' of 'area_list' objects>
    slice: method_descriptor = <method 'slice' of 'area_list' objects>
    sorted: method_descriptor = <method 'sorted' of 'area_list' objects>
    update: method_descriptor = <method 'update' of 'area_list' objects>

    def on_setattr(self, key, old, new): ...

class CTitle(Title):
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
    @property
    def begin_time(self): ...    @property
    def expired_time(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def proto(self): ...    @property
    def rank_key(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    @property
    def valid(self): ...    def values(self): ...

class CTitles(Titles):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gclient.gamesystem.entities.avatarmembers.cimp_title.CTitle'>
    append: method_descriptor = <method 'append' of 'area_list' objects>
    assign: method_descriptor = <method 'assign' of 'area_list' objects>
    clear: method_descriptor = <method 'clear' of 'area_list' objects>
    copy: method_descriptor = <method 'copy' of 'area_list' objects>
    delete: method_descriptor = <method 'delete' of 'area_list' objects>
    extend: method_descriptor = <method 'extend' of 'area_list' objects>
    get: method_descriptor = <method 'get' of 'area_list' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_list' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_list' objects>
    insert: method_descriptor = <method 'insert' of 'area_list' objects>
    list: method_descriptor = <method 'list' of 'area_list' objects>
    pop: method_descriptor = <method 'pop' of 'area_list' objects>
    size: method_descriptor = <method 'size' of 'area_list' objects>
    slice: method_descriptor = <method 'slice' of 'area_list' objects>
    sorted: method_descriptor = <method 'sorted' of 'area_list' objects>
    update: method_descriptor = <method 'update' of 'area_list' objects>

    def RefreshGunTitle(self): ...
    def on_append(self): ...

class Dict(object):
    convert: method_descriptor = <method 'convert' of 'dict' objects>
    get_type: method_descriptor = <method 'get_type' of 'dict' objects>
    getname: method_descriptor = <method 'getname' of 'dict' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'dict' objects>
    name: getset_descriptor = <attribute 'name' of 'dict' objects>

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

class Int(object):
    convert: method_descriptor = <method 'convert' of 'int' objects>
    get_type: method_descriptor = <method 'get_type' of 'int' objects>
    getname: method_descriptor = <method 'getname' of 'int' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'int' objects>
    name: getset_descriptor = <attribute 'name' of 'int' objects>

class PlayerAvatarMember(object):
    def GetGunTitles(self): ...
    def GetMostChallengingTitle(self): ...
    def HadShowPlayInfoTabTitlesReddot(self): ...
    def HasPlayInfoTabTitlesReddot(self): ...
    def HasPlayInfoTitleReddot(self, title): ...
    def HasPlayInfoTitlesReddot(self, is_tab=False): ...
    def HasTitleRedDot(self): ...
    def RefreshGunTitleMap(self): ...
    def UpdatePlayInfoTitlesReddot(self, title): ...
    def _on_set_cur_titles(self, old): ...
    def _on_set_titles(self, old): ...

class Title(CustomMapType):
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
    @property
    def begin_time(self): ...    @property
    def expired_time(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def proto(self): ...    @property
    def rank_key(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    @property
    def valid(self): ...    def values(self): ...

class Titles(CustomListType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.ititle.Title'>
    append: method_descriptor = <method 'append' of 'area_list' objects>
    assign: method_descriptor = <method 'assign' of 'area_list' objects>
    clear: method_descriptor = <method 'clear' of 'area_list' objects>
    copy: method_descriptor = <method 'copy' of 'area_list' objects>
    delete: method_descriptor = <method 'delete' of 'area_list' objects>
    extend: method_descriptor = <method 'extend' of 'area_list' objects>
    get: method_descriptor = <method 'get' of 'area_list' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_list' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_list' objects>
    insert: method_descriptor = <method 'insert' of 'area_list' objects>
    list: method_descriptor = <method 'list' of 'area_list' objects>
    pop: method_descriptor = <method 'pop' of 'area_list' objects>
    size: method_descriptor = <method 'size' of 'area_list' objects>
    slice: method_descriptor = <method 'slice' of 'area_list' objects>
    sorted: method_descriptor = <method 'sorted' of 'area_list' objects>
    update: method_descriptor = <method 'update' of 'area_list' objects>


def GetCurPlayerLocalConfig(config_name, default=None, trans_to_dict=True): ...
def Property(name, default, flag=2): ...
def SetCurPlayerLocalConfig(config_name, value): ...
def rpc_method(rpctype, *types): ...


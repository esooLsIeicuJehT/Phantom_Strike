# module: gclient.gamesystem.entities.avatarmembers.cimp_friend

import cconst
import config
import consts
import events
import json
import six2
import switches
import time

CLIENT_STUB: int = 8
cmp_to_key: builtin_function_or_method = <built-in function cmp_to_key>

class ApplyFriends(IFriends):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.ifriend.ApplyFriend'>
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

    def UpdateByPlayerInfoTotal(self, delta, info_dict): ...
    def UpdatePlayerInfo(self, data): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class AuthBindName(enum):
    APPLE: str = 'apple'
    DISCORD: str = 'discord'
    FACEBOOK: str = 'facebook'
    GOOGLE: str = 'google'
    GUEST: str = 'guest'
    LINE: str = 'line'
    STEAM: str = 'steam'
    TIKTOK: str = 'tiktok'
    TWITTER_X: str = 'twitter'
    VK: str = 'vk'
    name_to_values: dict = {'GUEST': 'guest', 'FACEBOOK': 'facebook', 'GOOGLE': 'google', 'TWITTER_X': 'twitter', 'APPLE': 'apple', 'TIKTOK': 'tiktok', 'DISCORD': 'discord', 'VK': 'vk', 'LINE': 'line', 'STEAM': 'steam'}
    value_to_names: dict = {'guest': 'GUEST', 'facebook': 'FACEBOOK', 'google': 'GOOGLE', 'twitter': 'TWITTER_X', 'apple': 'APPLE', 'tiktok': 'TIKTOK', 'discord': 'DISCORD', 'vk': 'VK', 'line': 'LINE', 'steam': 'STEAM'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class Bool(object):
    convert: method_descriptor = <method 'convert' of 'bool' objects>
    get_type: method_descriptor = <method 'get_type' of 'bool' objects>
    getname: method_descriptor = <method 'getname' of 'bool' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'bool' objects>
    name: getset_descriptor = <attribute 'name' of 'bool' objects>

class CApplyFriends(ApplyFriends):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.ifriend.ApplyFriend'>
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

    def UpdateByPlayerInfoTotal(self, delta, info_dict): ...
    def UpdatePlayerInfo(self, data): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class CBlackListFriends(IFriends):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.ifriend.IFriend'>
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

    def UpdateByPlayerInfoTotal(self, delta, info_dict): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def on_setattr(self, key, old, new): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class CFriend(IFriend):
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

    def CombatCopyMasterField(): ...
    def DBMetaData(): ...
    def FriendRankField(): ...
    def GetArmedPhotoProfile(self): ...
    def GlobalRankField(): ...
    def IsFBFriend(self): ...
    def IsGameFriend(self): ...
    def IsSourceFrom(self, friend_from): ...
    def PlayerCardField(): ...
    def PlayerSimpleField(): ...
    def QualifyingLevelByMatchType(self, match_type): ...
    def SearchFriendField(): ...
    def ShowModelField(): ...
    def TeamMemberField(): ...
    def Update(self, info): ...
    def UpdateByPlayerInfo(self, info): ...
    def ZoneField(): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    @property
    def legend_rank(self): ...    def on_setattr(self, key, old, new): ...
    @property
    def qualifying_level(self): ...    @property
    def qualifying_score(self): ...    @property
    def rank_class(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    @property
    def show_qualifying_level(self): ...    @property
    def show_qualifying_score(self): ...    @property
    def show_rank_class(self): ...    def update2(self, data): ...
    def values(self): ...

class CFriendAppliedMap(CustomFloatMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: type = <class 'float'>
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
    def on_setattr(self, key, old, new): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class CFriends(IFriends):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gclient.gamesystem.entities.avatarmembers.cimp_friend.CFriend'>
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

    def UpdateByPlayerInfoTotal(self, delta, info_dict): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def on_setattr(self, key, old, new): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class CustomFloatMapType(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: type = <class 'float'>
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

class CustomListType(area_list):
    IS_CUSTOM_TYPE: bool = True
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

class CustomStrMapType(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: type = <class 'str'>
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

class IFriend(IPlayer):
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

    def CombatCopyMasterField(): ...
    def DBMetaData(): ...
    def FriendRankField(): ...
    def GetArmedPhotoProfile(self): ...
    def GlobalRankField(): ...
    def IsFBFriend(self): ...
    def IsGameFriend(self): ...
    def IsSourceFrom(self, friend_from): ...
    def PlayerCardField(): ...
    def PlayerSimpleField(): ...
    def QualifyingLevelByMatchType(self, match_type): ...
    def SearchFriendField(): ...
    def ShowModelField(): ...
    def TeamMemberField(): ...
    def Update(self, info): ...
    def UpdateByPlayerInfo(self, info): ...
    def ZoneField(): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    @property
    def legend_rank(self): ...    @property
    def qualifying_level(self): ...    @property
    def qualifying_score(self): ...    @property
    def rank_class(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    @property
    def show_qualifying_level(self): ...    @property
    def show_qualifying_score(self): ...    @property
    def show_rank_class(self): ...    def update2(self, data): ...
    def values(self): ...

class IFriends(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.ifriend.IFriend'>
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

    def UpdateByPlayerInfoTotal(self, delta, info_dict): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class List(object):
    convert: method_descriptor = <method 'convert' of 'list' objects>
    get_type: method_descriptor = <method 'get_type' of 'list' objects>
    getname: method_descriptor = <method 'getname' of 'list' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'list' objects>
    name: getset_descriptor = <attribute 'name' of 'list' objects>

class LoginChannelType(enum):
    APPLE: int = 16
    DISCORD: int = 24
    FACEBOOK: int = 4
    GOOGLE: int = 3
    GUEST: int = 1
    LINE: int = 9
    PASSPORT: int = 25
    STEAM: int = 7
    TIKTOK: int = 23
    TWITTER_X: int = 5
    VK: int = 17
    name_to_values: dict = {'GUEST': 1, 'GOOGLE': 3, 'FACEBOOK': 4, 'TWITTER_X': 5, 'STEAM': 7, 'LINE': 9, 'APPLE': 16, 'VK': 17, 'TIKTOK': 23, 'DISCORD': 24, 'PASSPORT': 25}
    value_to_names: dict = {1: 'GUEST', 3: 'GOOGLE', 4: 'FACEBOOK', 5: 'TWITTER_X', 7: 'STEAM', 9: 'LINE', 16: 'APPLE', 17: 'VK', 23: 'TIKTOK', 24: 'DISCORD', 25: 'PASSPORT'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PlayerAvatarMember(object):
    def AddBlacklist(self, entity_id): ...
    def AddFriendByEntityID(self, entity_id, apply_from, verify_msg='', extra=None): ...
    def CanSendFriendApply(self, target_id): ...
    def CheckNeedFriendLikeRookieGuide(self): ...
    def GetFriendListByFriendSource(self, friend_from): ...
    def GetFriendRemarkName(self, friend_id): ...
    def GetGender(self): ...
    def GetGenderTexture(self): ...
    def GetInviteSortedClosedFriendsWithSearch(self, search_text): ...
    def GetInviteSortedFriends(self): ...
    def GetInviteSortedFriendsWithSearch(self, search_text): ...
    def GetLikeFriends(self, friend_from): ...
    def GetOnlineCloseFriendIdsByFriendSource(self, friend_from): ...
    def GetOnlineFriendIds(self): ...
    def GetOnlineFriendListByFriendSource(self, friend_from): ...
    def GetPlatformInfo(self, platform, platform_openid): ...
    def GetVacantFriends(self): ...
    def HasApplyFriendForRecentlyTimer(self, friend_id): ...
    def IsFriendApplyListInTime(self, aid): ...
    def IsFriendsReachMaxLimit(self): ...
    def IsSpecifyPlatformFriend(self, guid, source_from): ...
    def OnLikeFriendLogin(self, friend_id): ...
    def OnQueryIngameFriendListCallback(self, result): ...
    def PushApplyFriendInfo(self, count_change, data): ...
    def PushFriendInfo(self, delta, data): ...
    def QueryRandomOnlinePlayersForRecommend(self, language_filter, qualifying_filter, filter_area, manually=False): ...
    def RefreshSocialPlatformFriends(self): ...
    def RefreshSocialPlatformFriendsInGame(self): ...
    def RemarkFriend(self, entity_id, remark): ...
    def RemoveBlackList(self, entity_id): ...
    def RemoveFriend(self, entity_id): ...
    def ReplayQueryInviteListRecommend(self, data): ...
    def ReplayQueryInviteListRecommendManually(self, data): ...
    def ReplyFriendApply(self, entity_id, accept): ...
    def SearchFriendAccurateByKeyCallback(self, key, friend_info_list): ...
    def SearchFriendByKey(self, key): ...
    def SearchFriendFuzzyByKeyCallback(self, key, friend_info_list): ...
    def SendPlatformFriendDataToServer(self): ...
    def StartRecentlyFriendApply(self, friend_id): ...
    def TryAddFriend(self, target_id, from_source=0, extra=None): ...
    def _PopRecentlyFriendApplyTimer(self, friend_id): ...

class Str(object):
    convert: method_descriptor = <method 'convert' of 'str' objects>
    get_type: method_descriptor = <method 'get_type' of 'str' objects>
    getname: method_descriptor = <method 'getname' of 'str' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'str' objects>
    name: getset_descriptor = <attribute 'name' of 'str' objects>


def Property(name, default, flag=2): ...
def UnicodeToUTF8(d): ...
def rpc_method(rpctype, *types): ...


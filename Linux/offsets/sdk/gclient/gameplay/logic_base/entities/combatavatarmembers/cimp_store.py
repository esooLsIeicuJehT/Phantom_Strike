# module: gclient.gameplay.logic_base.entities.combatavatarmembers.cimp_store

import airdrop_support_data
import cPickle
import cconst
import collections
import consts
import events
import formula
import ichat
import lang
import six2
import time
import zlib

CLIENT_STUB: int = 8

class BinData(object):
    convert: method_descriptor = <method 'convert' of 'bin' objects>
    get_type: method_descriptor = <method 'get_type' of 'bin' objects>
    getname: method_descriptor = <method 'getname' of 'bin' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'bin' objects>
    name: getset_descriptor = <attribute 'name' of 'bin' objects>

class CCommodityCaseBase(CommodityCaseBase):
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

    def CalPriceWithAttr(self, ori_price): ...
    def CanBuy(self, count, left_coins, left_capacity=0): ...
    def OnBuy(self, count, extra): ...
    def _initProperty(self, data): ...
    @property
    def buy_limit(self): ...    @property
    def category(self): ...    @property
    def cd(self): ...    @property
    def combat_item_id(self): ...    @property
    def combat_item_proto(self): ...    @property
    def desc(self): ...    @property
    def desc_short(self): ...    @property
    def display_order(self): ...    @property
    def is_lock(self): ...    @property
    def is_share_cd(self): ...    @property
    def item_count(self): ...    @property
    def item_icon(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def logic_code(self): ...    @property
    def name(self): ...    def on_setattr(self, key, old, new): ...
    @property
    def owner(self): ...    @property
    def price(self): ...    @property
    def proto(self): ...    @property
    def quality(self): ...    @property
    def quick_item_icon(self): ...    @property
    def quick_item_icon_big(self): ...    @property
    def quick_item_no_money_icon(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    @property
    def take_capacity(self): ...    def update2(self, data): ...
    def values(self): ...

class CDefineGoodsItems(CustomIntListType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: type = <class 'int'>
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

    def on_append(self): ...
    def on_pop(self, inx, old): ...

class CStoreRecord(CustomMapType):
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
    def on_setattr(self, key, old, new): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class CStoreTimeRecords(CustomMapType):
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
    def on_setattr(self, key, old, new): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class CSupportItems(ISupportItems):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gclient.gameplay.logic_base.entities.combatavatarmembers.cimp_store.CCommodityCaseBase'>
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

    def CanBuyTeammate(self, guid): ...
    def GetCaseByCategories(self): ...
    def GetTotalCategories(self): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def on_setattr(self, key, old, new): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class CombatAvatarMember(object):
class CombatItemType(enum):
    AIRDROP: int = 104
    AMMO: int = 102
    AMMOBAG: int = 115
    AMMO_SUPPLEMENT: int = 113
    ARMOR_UPGRADE: int = 118
    BLOOD_CRYSTAL: int = 117
    BOX: int = 103
    BROKEN_TALENT_CORE: int = 112
    COIN: int = 105
    CONTRACT: int = 107
    EQUIP: int = 101
    GENECODE: int = 109
    NONE: int = 0
    RANDOM_TALENT: int = 110
    REBORN_CHANCE: int = 108
    SHUTTER_CLUE: int = 120
    SKILL_UPGRADE: int = 119
    TACTICAL_CORE: int = 111
    TACTICAL_ENERGY: int = 116
    TALENT: int = 106
    TROPHIES: int = 114
    name_to_values: dict = {'NONE': 0, 'EQUIP': 101, 'AMMO': 102, 'BOX': 103, 'AIRDROP': 104, 'COIN': 105, 'TALENT': 106, 'CONTRACT': 107, 'REBORN_CHANCE': 108, 'GENECODE': 109, 'RANDOM_TALENT': 110, 'TACTICAL_CORE': 111, 'BROKEN_TALENT_CORE': 112, 'AMMO_SUPPLEMENT': 113, 'TROPHIES': 114, 'AMMOBAG': 115, 'TACTICAL_ENERGY': 116, 'BLOOD_CRYSTAL': 117, 'ARMOR_UPGRADE': 118, 'SKILL_UPGRADE': 119, 'SHUTTER_CLUE': 120}
    value_to_names: dict = {0: 'NONE', 101: 'EQUIP', 102: 'AMMO', 103: 'BOX', 104: 'AIRDROP', 105: 'COIN', 106: 'TALENT', 107: 'CONTRACT', 108: 'REBORN_CHANCE', 109: 'GENECODE', 110: 'RANDOM_TALENT', 111: 'TACTICAL_CORE', 112: 'BROKEN_TALENT_CORE', 113: 'AMMO_SUPPLEMENT', 114: 'TROPHIES', 115: 'AMMOBAG', 116: 'TACTICAL_ENERGY', 117: 'BLOOD_CRYSTAL', 118: 'ARMOR_UPGRADE', 119: 'SKILL_UPGRADE', 120: 'SHUTTER_CLUE'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CommodityCaseBase(CustomMapType):
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

    def CalPriceWithAttr(self, ori_price): ...
    def CanBuy(self, count, left_coins, left_capacity=0): ...
    def OnBuy(self, count, extra): ...
    def _initProperty(self, data): ...
    @property
    def buy_limit(self): ...    @property
    def category(self): ...    @property
    def cd(self): ...    @property
    def combat_item_id(self): ...    @property
    def combat_item_proto(self): ...    @property
    def desc(self): ...    @property
    def desc_short(self): ...    @property
    def display_order(self): ...    @property
    def is_lock(self): ...    @property
    def is_share_cd(self): ...    @property
    def item_count(self): ...    @property
    def item_icon(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def logic_code(self): ...    @property
    def name(self): ...    @property
    def owner(self): ...    @property
    def price(self): ...    @property
    def proto(self): ...    @property
    def quality(self): ...    @property
    def quick_item_icon(self): ...    @property
    def quick_item_icon_big(self): ...    @property
    def quick_item_no_money_icon(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    @property
    def take_capacity(self): ...    def update2(self, data): ...
    def values(self): ...

class CustomIntListType(CustomListType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: type = <class 'int'>
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

class Dict(object):
    convert: method_descriptor = <method 'convert' of 'dict' objects>
    get_type: method_descriptor = <method 'get_type' of 'dict' objects>
    getname: method_descriptor = <method 'getname' of 'dict' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'dict' objects>
    name: getset_descriptor = <attribute 'name' of 'dict' objects>

class EntityID(object):
    convert: method_descriptor = <method 'convert' of 'entityid' objects>
    get_type: method_descriptor = <method 'get_type' of 'entityid' objects>
    getname: method_descriptor = <method 'getname' of 'entityid' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'entityid' objects>
    name: getset_descriptor = <attribute 'name' of 'entityid' objects>

class GameStoreReason(enum):
    BUY_CAPACITY_LIMIT: int = 8
    BUY_CD: int = 4
    BUY_COUNT_LIMIT: int = 3
    CANT_BUY_REBORN_CHANCE: int = 7
    FORBID_REBORN: int = 9
    HAS_AIRDROP: int = 6
    INVALID_GOODS: int = 5
    LACK_OF_COINS: int = 1
    NO_SUCH_ITEM: int = 2
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'LACK_OF_COINS': 1, 'NO_SUCH_ITEM': 2, 'BUY_COUNT_LIMIT': 3, 'BUY_CD': 4, 'INVALID_GOODS': 5, 'HAS_AIRDROP': 6, 'CANT_BUY_REBORN_CHANCE': 7, 'BUY_CAPACITY_LIMIT': 8, 'FORBID_REBORN': 9}
    value_to_names: dict = {0: 'SUCCESS', 1: 'LACK_OF_COINS', 2: 'NO_SUCH_ITEM', 3: 'BUY_COUNT_LIMIT', 4: 'BUY_CD', 5: 'INVALID_GOODS', 6: 'HAS_AIRDROP', 7: 'CANT_BUY_REBORN_CHANCE', 8: 'BUY_CAPACITY_LIMIT', 9: 'FORBID_REBORN'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ISupportItems(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.isupport.CommodityCaseBase'>
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

    def CanBuyTeammate(self, guid): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class Int(object):
    convert: method_descriptor = <method 'convert' of 'int' objects>
    get_type: method_descriptor = <method 'get_type' of 'int' objects>
    getname: method_descriptor = <method 'getname' of 'int' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'int' objects>
    name: getset_descriptor = <attribute 'name' of 'int' objects>

class List(object):
    convert: method_descriptor = <method 'convert' of 'list' objects>
    get_type: method_descriptor = <method 'get_type' of 'list' objects>
    getname: method_descriptor = <method 'getname' of 'list' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'list' objects>
    name: getset_descriptor = <attribute 'name' of 'list' objects>

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

class PlayerCombatAvatarMember(object):
    def BuyPersonalStoreItem(self, goodsid, extra=None): ...
    def BuyPersonalStoreTeammate(self, guid): ...
    def BuySupportResult(self, reason, items): ...
    def CheckBuyGoods(self, show_tips): ...
    def GetPersonalStoreData(self): ...
    def OnBuyPersonStoreResult(self, goodsid, result): ...
    def OnBuyPersonStoreTeammateResult(self, guid, result): ...
    def OnGetPersonStoreData(self, data): ...
    def OnGetStationStoreData(self, store_guid, data): ...
    def OnWildShopBuyHallGunSuccess(self, backpack_no, slot): ...
    def ProcessBuyResult(self, result, name): ...
    def ReplayRequestBuySupportItem(self, teammate_id, item_id): ...
    def SendRequestChat(self, content, voice_id=None, text_id=None): ...
    def SendRequestSupportItemChat(self, content, voice_id=None): ...
    def ServerPromptBuySuccessFieldShop(self, proto_id, extra_data, extra_info=None): ...
    def SupportBuyTeammateResult(self, reason, guid): ...
    def _on_set_fast_buy_items(self, old): ...

class Str(object):
    convert: method_descriptor = <method 'convert' of 'str' objects>
    get_type: method_descriptor = <method 'get_type' of 'str' objects>
    getname: method_descriptor = <method 'getname' of 'str' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'str' objects>
    name: getset_descriptor = <attribute 'name' of 'str' objects>


def Property(name, default, flag=2): ...
def rpc_method(rpctype, *types): ...


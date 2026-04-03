# module: gshare.icombat_item

import combat_item_data
import equip_data
import formula
import gun_mod_data
import lobby_item_data
import math
import random
import six2
import weapon_util

COMPONENT: str = 'Client'

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

class CustomFloatListType(CustomListType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: type = <class 'float'>
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

class CustomIntMapType(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: type = <class 'int'>
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

class EquipmentType(enum):
    ARMOR: int = 15
    COIN_TOOLS: int = 21
    CRACK_SCANNER: int = 20
    EMERGENCY_NEEDLE: int = 16
    GRENADE_LAUNCHER: int = 5
    GUN: int = 1
    GUN_MELEE: int = 3
    INVISIBLE: int = 19
    INVISIBLE2: int = 22
    MEDICINE: int = 17
    MELEE: int = 2
    NONE: int = 0
    NORMAL_TACTICAL: int = 18
    SKILL: int = 13
    SP_GUN: int = 4
    SP_SKILL: int = 23
    SUPPORT: int = 14
    THROWABLE_WEAPON_LEFT: int = 12
    THROWABLE_WEAPON_RIGHT: int = 11
    name_to_values: dict = {'NONE': 0, 'GUN': 1, 'MELEE': 2, 'GUN_MELEE': 3, 'SP_GUN': 4, 'GRENADE_LAUNCHER': 5, 'THROWABLE_WEAPON_RIGHT': 11, 'THROWABLE_WEAPON_LEFT': 12, 'SKILL': 13, 'SUPPORT': 14, 'ARMOR': 15, 'EMERGENCY_NEEDLE': 16, 'MEDICINE': 17, 'NORMAL_TACTICAL': 18, 'INVISIBLE': 19, 'CRACK_SCANNER': 20, 'COIN_TOOLS': 21, 'INVISIBLE2': 22, 'SP_SKILL': 23}
    value_to_names: dict = {0: 'NONE', 1: 'GUN', 2: 'MELEE', 3: 'GUN_MELEE', 4: 'SP_GUN', 5: 'GRENADE_LAUNCHER', 11: 'THROWABLE_WEAPON_RIGHT', 12: 'THROWABLE_WEAPON_LEFT', 13: 'SKILL', 14: 'SUPPORT', 15: 'ARMOR', 16: 'EMERGENCY_NEEDLE', 17: 'MEDICINE', 18: 'NORMAL_TACTICAL', 19: 'INVISIBLE', 20: 'CRACK_SCANNER', 21: 'COIN_TOOLS', 22: 'INVISIBLE2', 23: 'SP_SKILL'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ICombatItem(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: NoneType = None
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
    def ammo(self): ...    @property
    def contract_id(self): ...    @property
    def drop_timestamp(self): ...    @property
    def dye_owner_id(self): ...    @property
    def ecotope_name(self): ...    @property
    def equip_id(self): ...    @property
    def equip_proto(self): ...    @property
    def equip_type(self): ...    @property
    def from_id(self): ...    @property
    def guise_item_id(self): ...    @property
    def guise_name(self): ...    @property
    def guise_template_id(self): ...    @property
    def gun_id(self): ...    @property
    def id(self): ...    @property
    def inner_count(self): ...    @property
    def is_box(self): ...    @property
    def is_custom_gun(self): ...    @property
    def is_die_drop(self): ...    @property
    def is_gun(self): ...    @property
    def is_gun_melee(self): ...    @property
    def is_melee(self): ...    @property
    def is_sp_gun(self): ...    @property
    def is_throwable_weapon(self): ...    @property
    def item_proto(self): ...    @property
    def item_source(self): ...    @property
    def item_sub_type(self): ...    @property
    def item_type(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def left_hand_ammo(self): ...    @property
    def max_stack(self): ...    @property
    def open_avatar_id(self): ...    @property
    def ornament_item_id(self): ...    @property
    def owner_id(self): ...    @property
    def owner_name(self): ...    @property
    def quality(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    @property
    def skin_ground_item_id(self): ...    @property
    def skin_item_id(self): ...    @property
    def skin_template_id(self): ...    def update2(self, data): ...
    def values(self): ...

class ICombatItemBox(ICombatItem):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: NoneType = None
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
    def ammo(self): ...    @property
    def contract_id(self): ...    @property
    def drop_timestamp(self): ...    @property
    def dye_owner_id(self): ...    @property
    def ecotope_name(self): ...    @property
    def equip_id(self): ...    @property
    def equip_proto(self): ...    @property
    def equip_type(self): ...    @property
    def from_id(self): ...    @property
    def guise_item_id(self): ...    @property
    def guise_name(self): ...    @property
    def guise_template_id(self): ...    @property
    def gun_id(self): ...    @property
    def id(self): ...    @property
    def inner_count(self): ...    @property
    def is_box(self): ...    @property
    def is_custom_gun(self): ...    @property
    def is_die_drop(self): ...    @property
    def is_gun(self): ...    @property
    def is_gun_melee(self): ...    @property
    def is_melee(self): ...    @property
    def is_sp_gun(self): ...    @property
    def is_throwable_weapon(self): ...    @property
    def item_proto(self): ...    @property
    def item_source(self): ...    @property
    def item_sub_type(self): ...    @property
    def item_type(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def left_hand_ammo(self): ...    @property
    def max_stack(self): ...    @property
    def open_avatar_id(self): ...    @property
    def ornament_item_id(self): ...    @property
    def owner_id(self): ...    @property
    def owner_name(self): ...    @property
    def quality(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    @property
    def skin_ground_item_id(self): ...    @property
    def skin_item_id(self): ...    @property
    def skin_template_id(self): ...    def update2(self, data): ...
    def values(self): ...

class ICombatItemBoxes(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.icombat_item.ICombatItemBox'>
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

class ICombatItems(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.icombat_item.ICombatItem'>
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

    def Add(self, item): ...
    def Get(self, guid): ...
    def Has(self, guid): ...
    def Remove(self, guid): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class IParts(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.iitem.IPart'>
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

    def Add(self, slot, part_id): ...
    def Clear(self): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class IdManager(object):
    def bytes2id(bytes): ...
    def genid(): ...
    def id2bytes(uid): ...
    def id2str(uid): ...
    def is_valid_id(entityid): ...
    def str2id(string): ...


def CreateCombatEntityData(guid, position, backpack_item): ...
def CreateCombatItem(cls, item_id, count, data=None): ...
def CreateCombatItemByBackpackItem(cls, item, relative_pos, extra=None): ...
def CreateCombatItemByData(cls, data): ...
def CreateCombatItemData(item_id, count=1, extra=None): ...
def ExtraProperty(name, default): ...
def Property(name, default, flag=2): ...


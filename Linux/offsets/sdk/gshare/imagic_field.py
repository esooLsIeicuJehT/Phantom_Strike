# module: gshare.imagic_field

import consts
import formula
import six2
import snare_data
import spell_data

CLIENT_SIMULATE_METHODS: set = {1}
COMPONENT: str = 'Client'
SPELL_DAMAGE_SHAPE_CYLINDER: int = 2
SPELL_DAMAGE_SHAPE_HALF_SPHERE: int = 4
SPELL_DAMAGE_SHAPE_RECTANGLE: int = 3
SPELL_DAMAGE_SHAPE_SPHERE: int = 1
SPELL_SHAPE_ALIGN_MODE_BOTTOM: int = 1
SPELL_SHAPE_ALIGN_MODE_CENTER: int = 0

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

class CustomListMapType(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomListTypeMetaClass = <class 'common.classutils.CustomListType'>
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

class IAvatarAttrsShadow(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.icombat_attr.IModAttrShadow'>
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

class ICombatAttr(CustomMapType):
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

    def CalResult(self, base_value, attr_name, gun_type=0, equip_id=''): ...
    def CheckAttrBool(self, attr_name, gun_type=0, equip_id=''): ...
    def CheckAttrIsCov(self, attr_name, gun_type=0, equip_id=''): ...
    def DoCalResult(self, base_value, attr_name, gun_type=0, equip_id='', use_shadow=False): ...
    def GetAttrValue(self, attr_name, gun_type=0, equip_id='', use_shadow=False): ...
    def HasAttr(self, attr_name, gun_type=0, equip_id=''): ...
    def OnAdd_BackpackFreeSlot(self, attr): ...
    def OnAdd_MaxArmor(self, attr): ...
    def OnAdd_MaxHp(self, attr): ...
    def OnRemove_BackpackFreeSlot(self, attr): ...
    def OnRemove_MaxArmor(self, attr): ...
    def OnRemove_MaxHp(self, attr): ...
    def OnUpdate_BackpackFreeSlot(self, attr): ...
    def OnUpdate_MaxArmor(self, attr): ...
    def OnUpdate_MaxHp(self, attr): ...
    def OnUpdate_StorePrice(self, attr): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class IEquipAttrsShadow(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.icombat_attr.IEquipAttrShadow'>
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

class IGunAttrsShadow(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.icombat_attr.IGunAttrShadow'>
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

class IMagicField(object):
    ai_sensor_type: cached_property = <gshare.decorators.cached_property object at 0x6f78093390>
    block_proto: cached_property = <gshare.decorators.cached_property object at 0x6f78092f10>
    can_through_wall: cached_property = <gshare.decorators.cached_property object at 0x6f78093090>
    collision_filter: cached_property = <gshare.decorators.cached_property object at 0x6f78093010>
    destruction: cached_property = <gshare.decorators.cached_property object at 0x6f78093350>
    equip_id: cached_property = <gshare.decorators.cached_property object at 0x6f78092f50>
    field_size: cached_property = <gshare.decorators.cached_property object at 0x6f78093150>
    is_invincible: cached_property = <gshare.decorators.cached_property object at 0x6f780930d0>
    is_movable: cached_property = <gshare.decorators.cached_property object at 0x6f78093290>
    is_onewaypenetrate: cached_property = <gshare.decorators.cached_property object at 0x6f78093050>
    is_shield: cached_property = <gshare.decorators.cached_property object at 0x6f78093250>
    live_time: cached_property = <gshare.decorators.cached_property object at 0x6f78092fd0>
    particle_shield_proto: cached_property = <gshare.decorators.cached_property object at 0x6f78092f90>
    phy_material_type_id: cached_property = <gshare.decorators.cached_property object at 0x6f78093210>
    skill_attack_method_client: cached_property = <gshare.decorators.cached_property object at 0x6f78093310>
    skill_delay: cached_property = <gshare.decorators.cached_property object at 0x6f780932d0>
    snare_enter_code: cached_property = <gshare.decorators.cached_property object at 0x6f78093190>
    snare_leave_code: cached_property = <gshare.decorators.cached_property object at 0x6f780931d0>
    snare_proto: cached_property = <gshare.decorators.cached_property object at 0x6f78093110>
    spell_proto: cached_property = <gshare.decorators.cached_property object at 0x6f78092ed0>

    def GetScaleByAttr(self, base_scale): ...
    def GetScaleByAttrX(self, base_scale): ...
    def GetScaleByAttrY(self, base_scale): ...
    def GetScaleByAttrZ(self, base_scale): ...
    def NeedCreateStoryTick(self): ...
    def NeedCreateTrigger(self): ...
    @property
    def owner(self): ...
class InVehicleDamage(enum):
    OnlyPlayer: int = 1
    OnlyVehicle: int = 2
    PlayerAndVehicle: int = 3
    name_to_values: dict = {'OnlyPlayer': 1, 'OnlyVehicle': 2, 'PlayerAndVehicle': 3}
    value_to_names: dict = {1: 'OnlyPlayer', 2: 'OnlyVehicle', 3: 'PlayerAndVehicle'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class LifeState(enum):
    Destroy: int = 2
    Empty: int = 0
    Start: int = 1
    name_to_values: dict = {'Empty': 0, 'Start': 1, 'Destroy': 2}
    value_to_names: dict = {0: 'Empty', 1: 'Start', 2: 'Destroy'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MagicFieldCombatAttr(ICombatAttr):
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

    def CalResult(self, base_value, attr_name, gun_type=0, equip_id=''): ...
    def CheckAttrBool(self, attr_name, gun_type=0, equip_id=''): ...
    def CheckAttrIsCov(self, attr_name, gun_type=0, equip_id=''): ...
    def DoCalResult(self, base_value, attr_name, gun_type=0, equip_id='', use_shadow=False): ...
    def GetAttrValue(self, attr_name, gun_type=0, equip_id='', use_shadow=False): ...
    def HasAttr(self, attr_name, gun_type=0, equip_id=''): ...
    def OnAdd_BackpackFreeSlot(self, attr): ...
    def OnAdd_MaxArmor(self, attr): ...
    def OnAdd_MaxHp(self, attr): ...
    def OnRemove_BackpackFreeSlot(self, attr): ...
    def OnRemove_MaxArmor(self, attr): ...
    def OnRemove_MaxHp(self, attr): ...
    def OnUpdate_BackpackFreeSlot(self, attr): ...
    def OnUpdate_MaxArmor(self, attr): ...
    def OnUpdate_MaxHp(self, attr): ...
    def OnUpdate_StorePrice(self, attr): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class MagicFieldDestructionType(enum):
    ALL: int = 2
    ENEMY: int = 1
    ENEMY_AND_SELF: int = 3
    NONE: int = 0
    name_to_values: dict = {'NONE': 0, 'ENEMY': 1, 'ALL': 2, 'ENEMY_AND_SELF': 3}
    value_to_names: dict = {0: 'NONE', 1: 'ENEMY', 2: 'ALL', 3: 'ENEMY_AND_SELF'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PropertyMetaClass(type):
    mro: method_descriptor = <method 'mro' of 'type' objects>

class cached_property(object):
class enum(object):
    name_to_values: dict = {}
    value_to_names: dict = {}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...


def ExtraEntityProperty(name, default): ...
def Property(name, default, flag=2): ...


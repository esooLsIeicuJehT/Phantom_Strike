# module: gclient.gameplay.logic_base.entities.snare

import MType
import cconst
import formula
import icombat_item
import math
import random
import six2

class ClientAreaEntity(ClientEntity):
    area: getset_descriptor = <attribute 'area' of 'entity' objects>
    logger: Logger = <Logger ClientAreaEntity (DEBUG)>

    def _addComponent(component): ...
    def _callComponents(self, name, *args, **kwargs): ...
    def _delComponent(component): ...
    def _finiComponents(self): ...
    def _initComponents(self, bdict): ...
    def _on_timer(self, timerid): ...
    def _orded_dispatch_rpc(self, method, *args): ...
    def _postComponents(self, bdict): ...
    def _tickComponents(self, dtime): ...
    def add_repeat_timer(self, delay, func): ...
    def add_timer(self, delay, func): ...
    def cancel_timer(self, timerid): ...
    def deactive(self): ...
    def destroy(self, *args, **kwargs): ...
    def destroyObject(self): ...
    @property
    def dir(self): ...    def entity_method(self, md5, index, args): ...
    def get_gtick(self): ...
    def init_from_dict(self, *args, **kwargs): ...
    def is_deactived(self): ...
    def is_destroyed(self): ...
    def onEntityClassRegistered(): ...
    def on_del_space_data(self, key): ...
    def on_enter_space(self): ...
    def on_leave_space(self): ...
    def on_lose_server(self): ...
    def on_out_sight(self): ...
    def on_play_spectator_finished(self, msg): ...
    def on_set_space_center(self, cent): ...
    def on_set_space_data(self, key, value): ...
    def on_setattr(self, key, old, new): ...
    def on_speed(self, speed): ...
    def on_update_direction(self, stamp, yaw): ...
    def on_update_position(self, stamp, x, y, z): ...
    def on_update_position_and_direction(self, stamp, x, y, z, yaw): ...
    def on_update_space_data(self, data): ...
    @property
    def pos(self): ...    def pre_reload_script(self): ...
    def set_server(self, server): ...
    def set_tick(self, period): ...
    def setdefault(self, key, dft): ...
    @property
    def space(self): ...    @property
    def speed(self): ...    def tick(self, dtime): ...
    @property
    def yaw(self): ...
class CombatItem(ICombatItem):
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

class CombatItems(ICombatItems):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gclient.gameplay.logic_base.entities.snare.CombatItem'>
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
    def on_setattr(self, key, old, new): ...
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

class IItemSpaceSnare(object):
class ItemSpaceSnare(ClientAreaEntity):
    IsATM: bool = False
    IsATMGuardAI: bool = False
    IsAirDrop: bool = False
    IsAmmoBox: bool = False
    IsArrow: bool = False
    IsAttackDrone: bool = False
    IsAvatar: bool = False
    IsBarrieCannon: bool = False
    IsBomb: bool = False
    IsBuilding: bool = False
    IsChaosUav: bool = False
    IsCombatAvatar: bool = False
    IsCombatAvatarSniper: bool = False
    IsCombatAvatarZombieXray: bool = False
    IsCombatTeam: bool = False
    IsCombatUnit: bool = False
    IsContrabandPlane: bool = False
    IsCrack: bool = False
    IsCrow: bool = False
    IsCureUav: bool = False
    IsCureUavFix: bool = False
    IsDestructible: bool = False
    IsDummyCombatAvatar: bool = False
    IsEmoteTree: bool = False
    IsEnergyStronghold: bool = False
    IsEntityAttach: bool = False
    IsEntityMaster: bool = False
    IsGameLogic: bool = False
    IsGlass: bool = False
    IsHelenAI: bool = False
    IsHolographicRobot: bool = False
    IsIceWall: bool = False
    IsIgnoreCue: bool = False
    IsItem: bool = False
    IsItemSpaceSnare: bool = False
    IsMagicField: bool = False
    IsMonitorMissile: bool = False
    IsMonster: bool = False
    IsMovingPlatform: bool = False
    IsObserveAvatar: bool = False
    IsOccupyContractTarget: bool = False
    IsOccupyContractTargetNew: bool = False
    IsOilbox: bool = False
    IsPhyBall: bool = False
    IsPlayerCombatAvatar: bool = False
    IsPlayerObserveAvatar: bool = False
    IsPortableShop: bool = False
    IsRPGMissile: bool = False
    IsReplayPuppet: bool = False
    IsReplayRecorder: bool = False
    IsRobotCombatAvatar: bool = False
    IsRobotCombatAvatarZombie: bool = False
    IsSafeBox: bool = False
    IsSaveDrone: bool = False
    IsSaveMachine: bool = False
    IsScoutArrow: bool = False
    IsSearchContractBox: bool = False
    IsShield: bool = False
    IsShop: bool = False
    IsSimpleCombatUnit: bool = False
    IsSpellDrone: bool = False
    IsStickyMaster: bool = False
    IsStronghold: bool = False
    IsStropUav: bool = False
    IsSupply: bool = False
    IsSwordSpirit: bool = False
    IsSyncTransEntity: bool = False
    IsSystemKiller: bool = False
    IsVehicle: bool = False
    IsVirtualInteractionEntity: bool = False
    NinjaBeacon: bool = False
    area: getset_descriptor = <attribute 'area' of 'entity' objects>
    is_fps_avatar: bool = False
    is_replay_avatar: bool = False
    is_replay_room: bool = False
    logger: Logger = <Logger ItemSpaceSnare (DEBUG)>

    def CreateItemEntity(self, guid): ...
    def OnItemEntityCreated(self, entity): ...
    def RemoveItemEntity(self, guid): ...
    def ShowModel(self): ...
    def _addComponent(component): ...
    def _callComponents(self, name, *args, **kwargs): ...
    def _delComponent(component): ...
    def _finiComponents(self): ...
    def _initComponents(self, bdict): ...
    def _on_timer(self, timerid): ...
    def _orded_dispatch_rpc(self, method, *args): ...
    def _postComponents(self, bdict): ...
    def _tickComponents(self, dtime): ...
    def add_repeat_timer(self, delay, func): ...
    def add_timer(self, delay, func): ...
    def cancel_timer(self, timerid): ...
    def deactive(self): ...
    def destroy(self, *args, **kwargs): ...
    def destroyObject(self): ...
    @property
    def dir(self): ...    def entity_method(self, md5, index, args): ...
    def get_gtick(self): ...
    def init_from_dict(self, *args, **kwargs): ...
    def is_deactived(self): ...
    def is_destroyed(self): ...
    def onEntityClassRegistered(): ...
    def on_del_space_data(self, key): ...
    def on_enter_space(self): ...
    def on_leave_space(self): ...
    def on_lose_server(self): ...
    def on_out_sight(self): ...
    def on_play_spectator_finished(self, msg): ...
    def on_set_space_center(self, cent): ...
    def on_set_space_data(self, key, value): ...
    def on_setattr(self, key, old, new): ...
    def on_speed(self, speed): ...
    def on_update_direction(self, stamp, yaw): ...
    def on_update_position(self, stamp, x, y, z): ...
    def on_update_position_and_direction(self, stamp, x, y, z, yaw): ...
    def on_update_space_data(self, data): ...
    @property
    def pos(self): ...    def pre_reload_script(self): ...
    def set_server(self, server): ...
    def set_tick(self, period): ...
    def setdefault(self, key, dft): ...
    @property
    def space(self): ...    @property
    def speed(self): ...    def tick(self, dtime): ...
    @property
    def yaw(self): ...
class SnareComponent(IItemSpaceSnare):

def Components(*components, **kwargs): ...
def Property(name, default, flag=2): ...
def with_tag(*args): ...


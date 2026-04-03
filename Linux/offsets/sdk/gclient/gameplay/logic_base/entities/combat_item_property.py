# module: gclient.gameplay.logic_base.entities.combat_item_property

import cconst
import consts
import events
import six2

class CCombatItem(ICombatItem):
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
    def _on_set_count(self, old): ...
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
    def max_stack(self): ...    def on_setattr(self, key, old, new): ...
    @property
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

class CCombatItems(ICombatItems):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gclient.gameplay.logic_base.entities.combat_item_property.CCombatItem'>
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
    def GetTalentCoreItem(self): ...
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


def Property(name, default, flag=2): ...


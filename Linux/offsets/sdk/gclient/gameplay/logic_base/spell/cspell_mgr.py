# module: gclient.gameplay.logic_base.spell.cspell_mgr

import events
import six2

class CSpell(ISpell):
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

    def ChangePctProgress(self, delta): ...
    def ClearProgress(self): ...
    def ClockProgress(self): ...
    def FillProgress(self): ...
    def StartCharge(self, charge_speed=None): ...
    def StopCharge(self): ...
    def _initProperty(self, data): ...
    @property
    def charge_equip_id(self): ...    @property
    def charge_limit(self): ...    @property
    def charge_time(self): ...    @property
    def cur_charge_speed(self): ...    @property
    def cur_energy_progress(self): ...    @property
    def cur_pct_progress(self): ...    @property
    def hide_cd_when_charging(self): ...    @property
    def in_energy_limit(self): ...    @property
    def is_charge_finished(self): ...    @property
    def is_charging(self): ...    @property
    def is_energy_skill(self): ...    @property
    def is_in_cd(self): ...    @property
    def is_passive_skill(self): ...    def items(self): ...
    def keys(self): ...
    def on_setattr(self, key, old, new): ...
    @property
    def proto(self): ...    def setdefault(self, key, default): ...
    @property
    def show_decrease_charging_time(self): ...    @property
    def show_increase_charging_time(self): ...    def show_memory_status(self): ...
    @property
    def spell_cd(self): ...    @property
    def spell_value(self): ...    def update2(self, data): ...
    def values(self): ...

class CSpellMgr(ISpellMgr):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gclient.gameplay.logic_base.spell.cspell_mgr.CSpell'>
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

    def AddSpell(self, spell_id, level=1, count=0): ...
    def CheckCanSpell(self, spell_id): ...
    def Clear(self): ...
    def ClearCurrentGunSpell(self): ...
    def ClearCurrentSpell(self, spell_id=None): ...
    def OnSpellStop(self, spell_id, extra): ...
    def OnSpellStrike(self, spell_id, extra): ...
    def OnTick(self): ...
    def RemoveSpell(self, spell_id): ...
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

class ISpell(CustomMapType):
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

    def ChangePctProgress(self, delta): ...
    def ClearProgress(self): ...
    def ClockProgress(self): ...
    def FillProgress(self): ...
    def StartCharge(self, charge_speed=None): ...
    def StopCharge(self): ...
    def _initProperty(self, data): ...
    @property
    def charge_equip_id(self): ...    @property
    def charge_limit(self): ...    @property
    def charge_time(self): ...    @property
    def cur_charge_speed(self): ...    @property
    def cur_energy_progress(self): ...    @property
    def cur_pct_progress(self): ...    @property
    def hide_cd_when_charging(self): ...    @property
    def in_energy_limit(self): ...    @property
    def is_charge_finished(self): ...    @property
    def is_charging(self): ...    @property
    def is_energy_skill(self): ...    @property
    def is_in_cd(self): ...    @property
    def is_passive_skill(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def proto(self): ...    def setdefault(self, key, default): ...
    @property
    def show_decrease_charging_time(self): ...    @property
    def show_increase_charging_time(self): ...    def show_memory_status(self): ...
    @property
    def spell_cd(self): ...    @property
    def spell_value(self): ...    def update2(self, data): ...
    def values(self): ...

class ISpellMgr(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.ispell_mgr.ISpell'>
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

    def AddSpell(self, spell_id, level=1, count=0): ...
    def CheckCanSpell(self, spell_id): ...
    def Clear(self): ...
    def OnSpellStop(self, spell_id, extra): ...
    def OnSpellStrike(self, spell_id, extra): ...
    def OnTick(self): ...
    def RemoveSpell(self, spell_id): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...


def Property(name, default, flag=2): ...


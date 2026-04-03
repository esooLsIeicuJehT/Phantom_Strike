# module: gclient.gameplay.logic_base.entities.robotcomponents.robot_spell

import six2
import spell_util

CLIENT_STUB: int = 8

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

class EntityID(object):
    convert: method_descriptor = <method 'convert' of 'entityid' objects>
    get_type: method_descriptor = <method 'get_type' of 'entityid' objects>
    getname: method_descriptor = <method 'getname' of 'entityid' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'entityid' objects>
    name: getset_descriptor = <attribute 'name' of 'entityid' objects>

class Int(object):
    convert: method_descriptor = <method 'convert' of 'int' objects>
    get_type: method_descriptor = <method 'get_type' of 'int' objects>
    getname: method_descriptor = <method 'getname' of 'int' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'int' objects>
    name: getset_descriptor = <attribute 'name' of 'int' objects>

class PropertyMetaClass(type):
    mro: method_descriptor = <method 'mro' of 'type' objects>

class RobotSpellComponent(object):
    def CheckCanAttack(self, spell_id): ...
    def EndAttack(self, spell_id=None): ...
    def OnSpellResult(self, cur_result): ...
    def RobotStartSpell(self, spell_id, spell_level): ...
    def RobotStopSpell(self, spell_id): ...
    def TryAttack(self, spell_id, spell_level=1, extra=None): ...

class Str(object):
    convert: method_descriptor = <method 'convert' of 'str' objects>
    get_type: method_descriptor = <method 'get_type' of 'str' objects>
    getname: method_descriptor = <method 'getname' of 'str' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'str' objects>
    name: getset_descriptor = <attribute 'name' of 'str' objects>


def Property(name, default, flag=2): ...
def rpc_method(rpctype, *types): ...


# module: gclient.util.weapon_model_cue

import MEngine
import cconst
import six2
import time

class EquipCaseFactory(object):
    def Create(weapon_id, *args, **kwargs): ...

class IdManager(object):
    def bytes2id(bytes): ...
    def genid(): ...
    def id2bytes(uid): ...
    def id2str(uid): ...
    def is_valid_id(entityid): ...
    def str2id(string): ...

class WeaponModelCue(object):
    def CueSwitchReloadTwinWeaponCase(self): ...
    def CueSwitchToOriginWeapon(self): ...
    def CueSwitchToTwinWeapon(self): ...

class defaultdict(dict):
    clear: method_descriptor = <method 'clear' of 'dict' objects>
    copy: method_descriptor = <method 'copy' of 'collections.defaultdict' objects>
    default_factory: member_descriptor = <member 'default_factory' of 'collections.defaultdict' objects>
    fromkeys: builtin_function_or_method = <built-in method fromkeys of type object at 0x702850e7d8>
    get: method_descriptor = <method 'get' of 'dict' objects>
    items: method_descriptor = <method 'items' of 'dict' objects>
    keys: method_descriptor = <method 'keys' of 'dict' objects>
    pop: method_descriptor = <method 'pop' of 'dict' objects>
    popitem: method_descriptor = <method 'popitem' of 'dict' objects>
    setdefault: method_descriptor = <method 'setdefault' of 'dict' objects>
    update: method_descriptor = <method 'update' of 'dict' objects>
    values: method_descriptor = <method 'values' of 'dict' objects>



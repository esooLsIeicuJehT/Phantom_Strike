# module: gclient.gameplay.logic_base.comps.comp_advertising

import cPickle
import cconst
import events
import zlib

AD_RECORD_KEY_KILL: str = 'ad_kill'
LocalConfig: _LocalConfig = <gclient.config._LocalConfig object at 0x7040bf6d50>

class GameResult(enum):
    DEFEAT: int = 200
    DRAW: int = 100
    QUIT: int = 300
    VICTORY: int = 1
    name_to_values: dict = {'VICTORY': 1, 'DRAW': 100, 'DEFEAT': 200, 'QUIT': 300}
    value_to_names: dict = {1: 'VICTORY', 100: 'DRAW', 200: 'DEFEAT', 300: 'QUIT'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PlayerCombatAvatarMember(object):
    def AdvertisingRecord(self, property_name, add_count): ...
    def OnAdvertisingCoinsChange(self, old, _=None): ...
    def OnAdvertisingSettleDataComing(self): ...

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



# module: gclient.gamesystem.uigunsmith.gun_smith_util

import cdata_util
import consts
import gun_type_data
import gun_ui_util
import six2
import weapon_util

GUN_TYPE_ICON_DICT: dict = {(1,): (10504, 10505), (2,): (10506, 10507), (3,): (10508, 10509), (4,): (1014, 1015), (5, 6): (10510, 10511), (7, 8): (10512, 10513)}
GUN_TYPE_ICON_DICT_SINGLE: dict = {1: (10504, 10505), 2: (10506, 10507), 3: (10508, 10509), 4: (1014, 1015), 5: (10510, 10511), 6: (10510, 10511), 7: (10512, 10513), 8: (1175, 1176)}
LocalConfig: _LocalConfig = <gclient.config._LocalConfig object at 0x7040bf6d50>
TAB_DIY: str = 'btn_appearance'
TAB_MODIFY: str = 'btn_modify'
TAB_OVERVIEW: str = 'btn_achievement'

class OrderedDict(dict):
    clear: method_descriptor = <method 'clear' of 'collections.OrderedDict' objects>
    copy: method_descriptor = <method 'copy' of 'collections.OrderedDict' objects>
    fromkeys: builtin_function_or_method = <built-in method fromkeys of type object at 0x70285412c8>
    get: method_descriptor = <method 'get' of 'dict' objects>
    items: method_descriptor = <method 'items' of 'collections.OrderedDict' objects>
    keys: method_descriptor = <method 'keys' of 'collections.OrderedDict' objects>
    move_to_end: method_descriptor = <method 'move_to_end' of 'collections.OrderedDict' objects>
    pop: method_descriptor = <method 'pop' of 'collections.OrderedDict' objects>
    popitem: method_descriptor = <method 'popitem' of 'collections.OrderedDict' objects>
    setdefault: method_descriptor = <method 'setdefault' of 'collections.OrderedDict' objects>
    update: method_descriptor = <method 'update' of 'collections.OrderedDict' objects>
    values: method_descriptor = <method 'values' of 'collections.OrderedDict' objects>

class gun_type_enum(enum):
    AR: int = 1
    LMG: int = 4
    MR: int = 5
    NG: int = 9
    NONE: int = 0
    PT: int = 7
    RL: int = 8
    SG: int = 3
    SMG: int = 2
    SR: int = 6
    name_to_values: dict = {'NONE': 0, 'AR': 1, 'SMG': 2, 'SG': 3, 'LMG': 4, 'MR': 5, 'SR': 6, 'PT': 7, 'RL': 8, 'NG': 9}
    value_to_names: dict = {0: 'NONE', 1: 'AR', 2: 'SMG', 3: 'SG', 4: 'LMG', 5: 'MR', 6: 'SR', 7: 'PT', 8: 'RL', 9: 'NG'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...


def GetSortedGunDisplayInfo(): ...
def OpenGunSysUI(gun_id, backpack_no=None, tab_type='btn_modify', **show_info): ...
def ShowTrialActivate(gun_id, is_trial_backpack=True): ...


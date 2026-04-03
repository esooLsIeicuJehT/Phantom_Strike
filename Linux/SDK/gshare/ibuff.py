# module: gshare.ibuff

import buff_data
import six2
import sys
import time

CLIENT_BUFF_BASE: int = 1000
COMPONENT: str = 'Client'
TickInterval: float = 0.2

class BuffCategory(CustomMapType):
    CALLBACK: dict = {'add': 'OnAddBuffCategory', 'remove': 'OnRemoveBuffCategory'}
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'common.classutils.CustomMapType'>
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

    def Add(self, buff): ...
    def Remove(self, buff): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class BuffCategoryShadow(CustomMapType):
    CALLBACK: dict = {'add': 'OnAddBuffCategory', 'remove': 'OnRemoveBuffCategory'}
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'common.classutils.CustomMapType'>
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

    def Add(self, buff): ...
    def Remove(self, buff): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class BuffConflictRule(enum):
    COEXIST: int = 0
    LATEST: int = 1
    name_to_values: dict = {'COEXIST': 0, 'LATEST': 1}
    value_to_names: dict = {0: 'COEXIST', 1: 'LATEST'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class BuffEffect(enum):
    ANTI_RESTORE_ARMOR: str = 'ANTI_RESTORE_ARMOR'
    ANTI_RESTORE_HP: str = 'ANTI_RESTORE_HP'
    ANTI_SPRINT: str = 'ANTI_SPRINT'
    BURN: str = 'BURN'
    DYING_DECREASE_HP: str = 'DYING_DECREASE_HP'
    INVINCIBLE: str = 'INVINCIBLE'
    RESTORE_ARMOR: str = 'RESTORE_ARMOR'
    RESTORE_HP: str = 'RESTORE_HP'
    name_to_values: dict = {'RESTORE_HP': 'RESTORE_HP', 'RESTORE_ARMOR': 'RESTORE_ARMOR', 'ANTI_RESTORE_HP': 'ANTI_RESTORE_HP', 'ANTI_RESTORE_ARMOR': 'ANTI_RESTORE_ARMOR', 'INVINCIBLE': 'INVINCIBLE', 'DYING_DECREASE_HP': 'DYING_DECREASE_HP', 'BURN': 'BURN', 'ANTI_SPRINT': 'ANTI_SPRINT'}
    value_to_names: dict = {'RESTORE_HP': 'RESTORE_HP', 'RESTORE_ARMOR': 'RESTORE_ARMOR', 'ANTI_RESTORE_HP': 'ANTI_RESTORE_HP', 'ANTI_RESTORE_ARMOR': 'ANTI_RESTORE_ARMOR', 'INVINCIBLE': 'INVINCIBLE', 'DYING_DECREASE_HP': 'DYING_DECREASE_HP', 'BURN': 'BURN', 'ANTI_SPRINT': 'ANTI_SPRINT'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class BuffEffectCateory(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'common.classutils.CustomMapType'>
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

    def Add(self, buff): ...
    def Remove(self, buff): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class BuffEffectCateoryShadow(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'common.classutils.CustomMapType'>
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

    def Add(self, buff): ...
    def Remove(self, buff): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class BuffExtraInfo(enum):
    NeedCasterId: int = 1
    NeedCasterTeamId: int = 2
    NeedUnknown: int = 0
    name_to_values: dict = {'NeedUnknown': 0, 'NeedCasterId': 1, 'NeedCasterTeamId': 2}
    value_to_names: dict = {0: 'NeedUnknown', 1: 'NeedCasterId', 2: 'NeedCasterTeamId'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class BuffFactory(object):
    def CreateSimple(kind, duration, level=1, stack=1): ...

class BuffKind(enum):
    FIREWALL: int = 1028
    FLASH_BOMB: int = 7
    KRAKEN: int = 1010
    XRAY_BOMB: int = 6
    name_to_values: dict = {'XRAY_BOMB': 6, 'FLASH_BOMB': 7, 'KRAKEN': 1010, 'FIREWALL': 1028}
    value_to_names: dict = {6: 'XRAY_BOMB', 7: 'FLASH_BOMB', 1010: 'KRAKEN', 1028: 'FIREWALL'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ClientBuffFactory(object):
    Cache: defaultdict = defaultdict(<class 'list'>, {})

    def CreateRestoreSsp(duration, number): ...
    def CreateSimple(kind, duration, level=1): ...
    def CreateSuperSprint(duration): ...
    def EnqueueCache(kind, buff): ...

class ClientBuffKind(enum):
    ANTI_RESTORE_SSP: int = 1001
    FeelSurmount1: int = 1004
    FeelSurmount1Forever: int = 1005
    FeelSurmount3: int = 1003
    RESTORE_SSP: int = 1000
    SUPER_SPRINT: int = 1002
    name_to_values: dict = {'RESTORE_SSP': 1000, 'ANTI_RESTORE_SSP': 1001, 'SUPER_SPRINT': 1002, 'FeelSurmount3': 1003, 'FeelSurmount1': 1004, 'FeelSurmount1Forever': 1005}
    value_to_names: dict = {1000: 'RESTORE_SSP', 1001: 'ANTI_RESTORE_SSP', 1002: 'SUPER_SPRINT', 1003: 'FeelSurmount3', 1004: 'FeelSurmount1', 1005: 'FeelSurmount1Forever'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

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

class IBuff(CustomMapType):
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
    @property
    def buff_owner(self): ...    @property
    def buff_owner_team(self): ...    @property
    def effect(self): ...    @property
    def fl_degree(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def number(self): ...    @property
    def proto(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class IBuffShadow(CustomMapType):
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
    @property
    def buff_owner(self): ...    @property
    def buff_owner_team(self): ...    @property
    def effect(self): ...    @property
    def fl_degree(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def number(self): ...    @property
    def proto(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class IBuffs(CustomMapType):
    CALLBACK: dict = {'add': 'OnAddBuff', 'remove': 'OnRemoveBuff'}
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.ibuff.IBuff'>
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

    def AddBuff(self, buff): ...
    def Clear(self): ...
    def GetBuff(self, guid): ...
    def GetBuffsByEffect(self, effect): ...
    def GetBuffsByType(self, kind): ...
    def GetBuffsByTypeFromCategory(self, kind): ...
    def HasBuffsByEffect(self, effect): ...
    def HasBuffsByType(self, kind): ...
    def RemoveBuff(self, guid): ...
    def RemoveBuffsByEffect(self, effect): ...
    def RemoveBuffsByType(self, kind): ...
    def RemoveExpires(self): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class IBuffsShadow(CustomMapType):
    CALLBACK: dict = {'add': 'OnAddBuff', 'remove': 'OnRemoveBuff'}
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.ibuff.IBuffShadow'>
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

    def AddBuff(self, buff): ...
    def Clear(self): ...
    def GetBuff(self, guid): ...
    def GetBuffsByEffect(self, effect): ...
    def GetBuffsByType(self, kind): ...
    def GetBuffsByTypeFromCategory(self, kind): ...
    def HasBuffsByEffect(self, effect): ...
    def HasBuffsByType(self, kind): ...
    def RemoveBuff(self, guid): ...
    def RemoveBuffsByEffect(self, effect): ...
    def RemoveBuffsByType(self, kind): ...
    def RemoveExpires(self): ...
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

class enum(object):
    name_to_values: dict = {}
    value_to_names: dict = {}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...


def ExtraProperty(name, default): ...
def Property(name, default, flag=2): ...


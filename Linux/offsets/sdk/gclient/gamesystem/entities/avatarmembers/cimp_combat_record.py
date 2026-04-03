# module: gclient.gamesystem.entities.avatarmembers.cimp_combat_record

import cconst
import consts
import events
import six2
import skin_unlock_data
import time
import yearly_review_common

CLIENT_STUB: int = 8
GLOBAL_CACHE: dict = {}

class BinData(object):
    convert: method_descriptor = <method 'convert' of 'bin' objects>
    get_type: method_descriptor = <method 'get_type' of 'bin' objects>
    getname: method_descriptor = <method 'getname' of 'bin' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'bin' objects>
    name: getset_descriptor = <attribute 'name' of 'bin' objects>

class Cache(OrderedDict):
    _OrderedDict__marker: object = <object object at 0x702c5c4b30>
    get: method_descriptor = <method 'get' of 'dict' objects>

    def _OrderedDict__update(self, other=(), /, **kwds): ...
    def clean(self): ...
    def cleantimeout(self, now, count=1000): ...
    def clear(self): ...
    def copy(self): ...
    def fromkeys(iterable, value=None): ...
    def front_item(self): ...
    def front_key(self): ...
    def front_value(self): ...
    def getdatas(self): ...
    def invalid(self, key): ...
    def items(self): ...
    def iteritems(self): yield ...
    def iterkeys(self): ...
    def itervalues(self): yield ...
    def keys(self): ...
    def move_to_end(self, key, last=True): ...
    def pop(self, key, default=<object object at 0x702c5c4b30>): ...
    def popitem(self, last=True): ...
    def select(self, key, timeout=None): ...
    def setdefault(self, key, default=None): ...
    def update(self, key, value, timeout=0): ...
    def values(self): ...

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

class DataCache(object):
    def Clear(self): ...
    def GetCacheData(self): ...
    def OnlyNotify(self, key, data): ...
    def OnlyQuery(self, key): ...
    def PopQueue(self, key): ...
    def Query(self, key, callback, *args, **kwargs): ...
    def Update(self, key, data, timeout=0): ...
    def invalid(self, key): ...

class Dict(object):
    convert: method_descriptor = <method 'convert' of 'dict' objects>
    get_type: method_descriptor = <method 'get_type' of 'dict' objects>
    getname: method_descriptor = <method 'getname' of 'dict' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'dict' objects>
    name: getset_descriptor = <attribute 'name' of 'dict' objects>

class EntityID(object):
    convert: method_descriptor = <method 'convert' of 'entityid' objects>
    get_type: method_descriptor = <method 'get_type' of 'entityid' objects>
    getname: method_descriptor = <method 'getname' of 'entityid' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'entityid' objects>
    name: getset_descriptor = <attribute 'name' of 'entityid' objects>

class List(object):
    convert: method_descriptor = <method 'convert' of 'list' objects>
    get_type: method_descriptor = <method 'get_type' of 'list' objects>
    getname: method_descriptor = <method 'getname' of 'list' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'list' objects>
    name: getset_descriptor = <attribute 'name' of 'list' objects>

class PlayerAvatarMember(object):
    def GetYearReviewCareerData(self, avatar_id=''): ...
    def OnAvatarCreatedReviewRecord(self): ...
    def OnGetYearReviewCareerData(self, avatar_id, data): ...
    def _GetYearReviewCareerDataWorker(self, avatar_id): ...
    def _OnGetYearReviewCareerDataCallback(self, avatar_id, data): ...

class Str(object):
    convert: method_descriptor = <method 'convert' of 'str' objects>
    get_type: method_descriptor = <method 'get_type' of 'str' objects>
    getname: method_descriptor = <method 'getname' of 'str' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'str' objects>
    name: getset_descriptor = <attribute 'name' of 'str' objects>

class YearTitlesMap(CustomIntMapType):
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
    def on_setattr(self, key, old, new): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class partial(object):
    args: member_descriptor = <member 'args' of 'functools.partial' objects>
    func: member_descriptor = <member 'func' of 'functools.partial' objects>
    keywords: member_descriptor = <member 'keywords' of 'functools.partial' objects>


def Property(name, default, flag=2): ...
def rpc_method(rpctype, *types): ...


# module: gclient.gamesystem.entities.avatarmembers.cimp_recent

import events
import six2

CLIENT_STUB: int = 8
cmp_to_key: builtin_function_or_method = <built-in function cmp_to_key>

class Bool(object):
    convert: method_descriptor = <method 'convert' of 'bool' objects>
    get_type: method_descriptor = <method 'get_type' of 'bool' objects>
    getname: method_descriptor = <method 'getname' of 'bool' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'bool' objects>
    name: getset_descriptor = <attribute 'name' of 'bool' objects>

class CRecentPlayer(IRecentPlayer):
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

    def CombatCopyMasterField(): ...
    def DBMetaData(): ...
    def FriendRankField(): ...
    def GetArmedPhotoProfile(self): ...
    def GlobalRankField(): ...
    def PlayerCardField(): ...
    def PlayerSimpleField(): ...
    def QualifyingLevelByMatchType(self, match_type): ...
    def SearchFriendField(): ...
    def ShowModelField(): ...
    def TeamMemberField(): ...
    def Update(self, info): ...
    def ZoneField(): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    @property
    def legend_rank(self): ...    def on_setattr(self, key, old, new): ...
    @property
    def qualifying_level(self): ...    @property
    def qualifying_score(self): ...    @property
    def rank_class(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    @property
    def show_qualifying_level(self): ...    @property
    def show_qualifying_score(self): ...    @property
    def show_rank_class(self): ...    def update2(self, data): ...
    def values(self): ...

class CRecentPlayers(RecentPlayers):
    COUNT_LIMIT: int = 20
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gclient.gamesystem.entities.avatarmembers.cimp_recent.CRecentPlayer'>
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

    def UpdateAllRecord(self, info_dict): ...
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

class Dict(object):
    convert: method_descriptor = <method 'convert' of 'dict' objects>
    get_type: method_descriptor = <method 'get_type' of 'dict' objects>
    getname: method_descriptor = <method 'getname' of 'dict' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'dict' objects>
    name: getset_descriptor = <attribute 'name' of 'dict' objects>

class IRecentPlayer(IPlayer):
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

    def CombatCopyMasterField(): ...
    def DBMetaData(): ...
    def FriendRankField(): ...
    def GetArmedPhotoProfile(self): ...
    def GlobalRankField(): ...
    def PlayerCardField(): ...
    def PlayerSimpleField(): ...
    def QualifyingLevelByMatchType(self, match_type): ...
    def SearchFriendField(): ...
    def ShowModelField(): ...
    def TeamMemberField(): ...
    def Update(self, info): ...
    def ZoneField(): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    @property
    def legend_rank(self): ...    @property
    def qualifying_level(self): ...    @property
    def qualifying_score(self): ...    @property
    def rank_class(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    @property
    def show_qualifying_level(self): ...    @property
    def show_qualifying_score(self): ...    @property
    def show_rank_class(self): ...    def update2(self, data): ...
    def values(self): ...

class List(object):
    convert: method_descriptor = <method 'convert' of 'list' objects>
    get_type: method_descriptor = <method 'get_type' of 'list' objects>
    getname: method_descriptor = <method 'getname' of 'list' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'list' objects>
    name: getset_descriptor = <attribute 'name' of 'list' objects>

class PlayerAvatarMember(object):
    def GetInviteRecentPlayersWithSearch(self, search_text): ...
    def GetRecentPlayersNoFriend(self): ...
    def UpdateRecentInfo(self, delta, info_dict): ...

class RecentPlayers(CustomMapType):
    COUNT_LIMIT: int = 20
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.irecent_match.IRecentPlayer'>
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

    def UpdateAllRecord(self, info_dict): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class Str(object):
    convert: method_descriptor = <method 'convert' of 'str' objects>
    get_type: method_descriptor = <method 'get_type' of 'str' objects>
    getname: method_descriptor = <method 'getname' of 'str' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'str' objects>
    name: getset_descriptor = <attribute 'name' of 'str' objects>


def Property(name, default, flag=2): ...
def rpc_method(rpctype, *types): ...


# module: gshare.iclan

import clan_apply_qualifying_data
import clan_style_data
import consts
import game_const_data
import six2
import time

AGREE_MIN_ROLE: int = 2
APPLY_LIMIT: int = 50
APPLY_LIST_LIMIT: int = 120
ASSIGN_CEO_MIN_JOIN_TIME: int = 0
AgreeToApplyErrno: dict = {0: 867, 876: 862, 878: 853}
ApplyConfig: dict = {'apply_verify': (<class 'int'>, None), 'apply_level': (<class 'int'>, <function <lambda> at 0x6fa51a6f20>), 'apply_score': (<class 'int'>, <function <lambda> at 0x6fa51a6fc0>)}
BOARD_CHANGE_CD: int = 60
BOARD_MAX_LENGTH: int = 100
BriefFields: dict = {'id': '', 'no': 0, 'name': '', 'icon': 0, 'country_icon': 0, 'board': '', 'styles': [], 'online': 0, 'apply_verify': 0, 'apply_level': -1, 'apply_score': -1, 'current_members': 0, 'max_members': 0, 'member_info': {}, 'creator': '', 'change_name_time': 0}
BriefQueryFields: dict = {'id': 1, 'no': 1, 'name': 1, 'icon': 1, 'country_icon': 1, 'language': 1, 'styles': 1, 'board': 1, 'ceo': 1, 'apply_verify': 1, 'apply_level': 1, 'apply_score': 1, 'current_members': 1, 'online': 1, 'total_scores': 1, 'create_time': 1, 'members': 1}
CHANGE_NAME_CD: int = 2592000
CHANGE_NAME_COST: int = 500
CHAT_MSG_LIMIT: int = 20
CHAT_MSG_TIMEOUT: int = 2592000
CHECK_CLAN_MEMBER_VAILD: int = 2
CLAN_ALL_FILTERS: dict = {'apply_verify': (<class 'int'>, <function <lambda> at 0x6fa51a7240>), 'apply_score': (<class 'int'>, <function <lambda> at 0x6fa51a74c0>)}
CLAN_DEFAULT_COUNTRY_ICON: int = 1
CLAN_MAIL_NUM: int = 2
CLAN_MAX_MEMBERS: int = 30
CLAN_NO_BASE: int = 101350
CLAN_ROLE_MAX_COUNT: dict = {2: 1, 4: 1, 8: 1}
COMPONENT: str = 'Client'
CREATE_MIN_LEVEL: int = 1
CREATE_POSSIBLE_FIELDS: dict = {'id': <class 'str'>, 'name': <class 'str'>, 'icon': <class 'int'>, 'country_icon': <class 'int'>, 'board': <class 'str'>, 'styles': <class 'list'>, 'region_pids': <class 'list'>, 'money_type': <class 'int'>, 'apply_score': <class 'int'>, 'apply_level': <class 'int'>, 'apply_verify': <class 'int'>, 'language': <class 'str'>, 'country_code': <class 'str'>}
CREATE_REQUIRED_FIELDS: dict = {'name': <class 'str'>, 'icon': <class 'int'>, 'country_icon': <class 'int'>, 'board': <class 'str'>, 'styles': <class 'list'>, 'region_pids': <class 'list'>, 'money_type': <class 'int'>, 'apply_score': <class 'int'>, 'apply_level': <class 'int'>, 'apply_verify': <class 'int'>, 'language': <class 'str'>, 'country_code': <class 'str'>}
DataFields: dict = {1: {'id': '', 'no': 0, 'name': '', 'icon': 0, 'country_icon': 0, 'board': '', 'styles': [], 'online': 0, 'apply_verify': 0, 'apply_level': -1, 'apply_score': -1, 'current_members': 0, 'max_members': 0, 'member_info': {}, 'creator': '', 'change_name_time': 0, 'ceo': {}}, 2: {'id': '', 'no': 0, 'name': '', 'icon': 0, 'country_icon': 0, 'board': '', 'styles': [], 'online': 0, 'apply_verify': 0, 'apply_level': -1, 'apply_score': -1, 'current_members': 0, 'max_members': 0, 'member_info': {}, 'creator': '', 'change_name_time': 0, 'ceo': {}, 'appliers': {}, 'shield_appliers': {}, 'mail_sent': 0}, 8: {'id': '', 'no': 0, 'name': '', 'icon': 0, 'country_icon': 0, 'board': '', 'styles': [], 'online': 0, 'apply_verify': 0, 'apply_level': -1, 'apply_score': -1, 'current_members': 0, 'max_members': 0, 'member_info': {}, 'creator': '', 'change_name_time': 0, 'members': {}, 'managers_info': {}}, 3: {'members': {}, 'current_members': 0}, 4: {'members': {}, 'player_info': {}}, 7: {'members': {}, 'player_info': {}, 'appliers': {}, 'shield_appliers': {}}, 5: {'id': '', 'no': 0, 'name': '', 'icon': 0, 'country_icon': 0, 'board': '', 'styles': [], 'online': 0, 'apply_verify': 0, 'apply_level': -1, 'apply_score': -1, 'current_members': 0, 'max_members': 0, 'member_info': {}, 'creator': '', 'change_name_time': 0, 'ceo': {}, 'total_scores': {}}, 6: {'members': {}, 'player_info': {}, 'ach_logs': []}}
EClanFilter_APPLYABLE: str = 'applyable'
EClanFilter_FULL: str = 'full'
EClanFilter_LANGUAGE: str = 'language'
EClanFilter_LEVEL: str = 'apply_level'
EClanFilter_REGION: str = 'region_pids'
EClanFilter_SCORE: str = 'apply_score'
EClanFilter_STYLE: str = 'styles'
EClanFilter_VERIFY: str = 'apply_verify'
INVITE_MIN_ROLE: int = 1
JOURNAL_EXPIRE: float = 604800.0
JOURNAL_MAX_COUNT: int = 50
KICK_MIN_ROLE: int = 2
LeaveToKickErrno: dict = {0: 0, 1: 906, 2: 906}
MAIL_BODY_MAX_LENGTH: int = 450
MAIL_OVERDUE: int = 0
MANAGER_MIN_ROLE: int = 2
MANAGER_MODIFY_NAME_TIME: int = 259200
MAX_STYLE_NUM: int = 4
NAME_MAX_LENGTH: int = 14
NAME_MIN_LENGTH: int = 3
PAGE_SIZE: int = 10
SyncFields: dict = {'id': '', 'no': -1, 'name': '', 'icon': 0, 'role': 0, 'jt': 0.0}
USURP_FINAL_DAYS: int = 15
USURP_MIN_ROLE: int = 1
USURP_WARNING_DAYS: int = 10

class AgreeErrno(enum):
    ALREADY: int = 878
    FORBIDDEN: int = 875
    FULL: int = 876
    NOT_FOUND: int = 877
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'FULL': 876, 'ALREADY': 878, 'NOT_FOUND': 877, 'FORBIDDEN': 875}
    value_to_names: dict = {0: 'SUCCESS', 876: 'FULL', 878: 'ALREADY', 877: 'NOT_FOUND', 875: 'FORBIDDEN'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ApplyErrno(enum):
    ALREADY: int = 2
    APPLY_AGREED: int = 867
    APPLY_LIST_LIMIT: int = 866
    CLAN_APPLY_LIMIT: int = 865
    FAILED: int = 7
    FULL: int = 862
    HAS_CLAN: int = 853
    INVALID_CLAN: int = 970
    INVALID_INVITER: int = 996
    INVALID_REGION: int = 12
    LIMIT_LEVEL: int = 861
    LIMIT_SCORE: int = 958
    SUCCESS: int = 0
    VERIFY: int = 863
    name_to_values: dict = {'SUCCESS': 0, 'APPLY_AGREED': 867, 'ALREADY': 2, 'FULL': 862, 'LIMIT_LEVEL': 861, 'LIMIT_SCORE': 958, 'HAS_CLAN': 853, 'FAILED': 7, 'VERIFY': 863, 'APPLY_LIST_LIMIT': 866, 'CLAN_APPLY_LIMIT': 865, 'INVALID_REGION': 12, 'INVALID_CLAN': 970, 'INVALID_INVITER': 996}
    value_to_names: dict = {0: 'SUCCESS', 867: 'APPLY_AGREED', 2: 'ALREADY', 862: 'FULL', 861: 'LIMIT_LEVEL', 958: 'LIMIT_SCORE', 853: 'HAS_CLAN', 7: 'FAILED', 863: 'VERIFY', 866: 'APPLY_LIST_LIMIT', 865: 'CLAN_APPLY_LIMIT', 12: 'INVALID_REGION', 970: 'INVALID_CLAN', 996: 'INVALID_INVITER'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class AssignErrno(enum):
    DUPLICATED: int = 908
    FORBIDDEN: int = 875
    LIMITED: int = 907
    LIMIT_JOIN_TIME: int = 6
    NOT_ALLOWED: int = 909
    NOT_FOUND: int = 906
    NO_CLAN: int = 880
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'NO_CLAN': 880, 'NOT_FOUND': 906, 'FORBIDDEN': 875, 'LIMITED': 907, 'DUPLICATED': 908, 'LIMIT_JOIN_TIME': 6, 'NOT_ALLOWED': 909}
    value_to_names: dict = {0: 'SUCCESS', 880: 'NO_CLAN', 906: 'NOT_FOUND', 875: 'FORBIDDEN', 907: 'LIMITED', 908: 'DUPLICATED', 6: 'LIMIT_JOIN_TIME', 909: 'NOT_ALLOWED'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CLAN_ACH_LOG_TYPE(enum):
    ITEM_QUALITY: int = 4
    QUALIFYING_LEVEL: int = 2
    QUALIFYING_RANK: int = 3
    WIN: int = 1
    name_to_values: dict = {'WIN': 1, 'QUALIFYING_LEVEL': 2, 'QUALIFYING_RANK': 3, 'ITEM_QUALITY': 4}
    value_to_names: dict = {1: 'WIN', 2: 'QUALIFYING_LEVEL', 3: 'QUALIFYING_RANK', 4: 'ITEM_QUALITY'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ChangeBoardErrno(enum):
    CD: int = 5
    FORBIDDEN: int = 875
    FREEZING: int = 6
    INVALID: int = 3
    NO_CLAN: int = 880
    OVER_LEN: int = 4
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'NO_CLAN': 880, 'FORBIDDEN': 875, 'INVALID': 3, 'OVER_LEN': 4, 'CD': 5, 'FREEZING': 6}
    value_to_names: dict = {0: 'SUCCESS', 880: 'NO_CLAN', 875: 'FORBIDDEN', 3: 'INVALID', 4: 'OVER_LEN', 5: 'CD', 6: 'FREEZING'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ChangeIconErrno(enum):
    ALREADY: int = 4
    FORBIDDEN: int = 2
    INVALID: int = 5
    LACK_GOLD: int = 3
    NO_CLAN: int = 1
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'NO_CLAN': 1, 'FORBIDDEN': 2, 'LACK_GOLD': 3, 'ALREADY': 4, 'INVALID': 5}
    value_to_names: dict = {0: 'SUCCESS', 1: 'NO_CLAN', 2: 'FORBIDDEN', 3: 'LACK_GOLD', 4: 'ALREADY', 5: 'INVALID'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ChangeNameErrno(enum):
    CD: int = 887
    DUPLICATED: int = 851
    FORBIDDEN: int = 875
    FREEZING: int = 8
    GM: int = 10
    INVALID: int = 850
    ITEM: int = 12
    LACK_ITEM: int = 7
    MONEY: int = 966
    NO_CLAN: int = 880
    OVER_LEN: int = 4
    REGION_INVALID: int = 856
    SUCCESS: int = 0
    TIMEOUT: int = 11
    name_to_values: dict = {'SUCCESS': 0, 'NO_CLAN': 880, 'FORBIDDEN': 875, 'INVALID': 850, 'OVER_LEN': 4, 'DUPLICATED': 851, 'MONEY': 966, 'LACK_ITEM': 7, 'FREEZING': 8, 'CD': 887, 'GM': 10, 'TIMEOUT': 11, 'ITEM': 12, 'REGION_INVALID': 856}
    value_to_names: dict = {0: 'SUCCESS', 880: 'NO_CLAN', 875: 'FORBIDDEN', 850: 'INVALID', 4: 'OVER_LEN', 851: 'DUPLICATED', 966: 'MONEY', 7: 'LACK_ITEM', 8: 'FREEZING', 887: 'CD', 10: 'GM', 11: 'TIMEOUT', 12: 'ITEM', 856: 'REGION_INVALID'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ChangeStylesErrno(enum):
    FORBIDDEN: int = 875
    INVALID: int = 896
    NO_CLAN: int = 880
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'NO_CLAN': 880, 'FORBIDDEN': 875, 'INVALID': 896}
    value_to_names: dict = {0: 'SUCCESS', 880: 'NO_CLAN', 875: 'FORBIDDEN', 896: 'INVALID'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ClanApplySource(enum):
    CLAN_LIST: int = 3
    DEFAULT: int = 0
    MEMBER_INVITE: int = 2
    SEARCH: int = 1
    name_to_values: dict = {'DEFAULT': 0, 'SEARCH': 1, 'MEMBER_INVITE': 2, 'CLAN_LIST': 3}
    value_to_names: dict = {0: 'DEFAULT', 1: 'SEARCH', 2: 'MEMBER_INVITE', 3: 'CLAN_LIST'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ClanApplys(CustomFloatMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: type = <class 'float'>
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

    def Add(self, guid): ...
    def Clear(self): ...
    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class ClanRole(enum):
    CEO: int = 8
    CHEER: int = 2
    NONE: int = 0
    STAFF: int = 1
    VP: int = 4
    name_to_values: dict = {'NONE': 0, 'STAFF': 1, 'CHEER': 2, 'VP': 4, 'CEO': 8}
    value_to_names: dict = {0: 'NONE', 1: 'STAFF', 2: 'CHEER', 4: 'VP', 8: 'CEO'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ConfigureApplyErrno(enum):
    FORBIDDEN: int = 875
    FREEZING: int = 4
    INVALID_KEY: int = 895
    INVALID_VALUE: int = 896
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'FORBIDDEN': 875, 'INVALID_KEY': 895, 'INVALID_VALUE': 896, 'FREEZING': 4}
    value_to_names: dict = {0: 'SUCCESS', 875: 'FORBIDDEN', 895: 'INVALID_KEY', 896: 'INVALID_VALUE', 4: 'FREEZING'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CreateErrno(enum):
    ALREADY: int = 853
    CHECKSUM: int = 10
    CREATING: int = 1
    EXTRA_FIELDS: int = 858
    GEN_NO_ERROR: int = 3
    INVALID_ICON: int = 896
    INVALID_REGION: int = 856
    INVALID_STYLE: int = 17
    LACK_FIELDS: int = 6
    LEVEL: int = 14
    MAX_CREATINGS: int = 13
    MONEY: int = 852
    NAME_ERROR: int = 851
    NO_NAME: int = 850
    SAVE_ERROR: int = 8
    SUCCESS: int = 0
    WANT_AD_LENGTH: int = 12
    name_to_values: dict = {'SUCCESS': 0, 'CREATING': 1, 'ALREADY': 853, 'GEN_NO_ERROR': 3, 'NAME_ERROR': 851, 'LACK_FIELDS': 6, 'EXTRA_FIELDS': 858, 'SAVE_ERROR': 8, 'MONEY': 852, 'CHECKSUM': 10, 'NO_NAME': 850, 'WANT_AD_LENGTH': 12, 'MAX_CREATINGS': 13, 'LEVEL': 14, 'INVALID_ICON': 896, 'INVALID_REGION': 856, 'INVALID_STYLE': 17}
    value_to_names: dict = {0: 'SUCCESS', 1: 'CREATING', 853: 'ALREADY', 3: 'GEN_NO_ERROR', 851: 'NAME_ERROR', 6: 'LACK_FIELDS', 858: 'EXTRA_FIELDS', 8: 'SAVE_ERROR', 852: 'MONEY', 10: 'CHECKSUM', 850: 'NO_NAME', 12: 'WANT_AD_LENGTH', 13: 'MAX_CREATINGS', 14: 'LEVEL', 896: 'INVALID_ICON', 856: 'INVALID_REGION', 17: 'INVALID_STYLE'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CustomFloatMapType(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: type = <class 'float'>
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

class DataType(enum):
    ACH_LOGS: int = 6
    APPLY_PLAYER_INFO: int = 7
    BRIEF: int = 1
    FETCH_RECOMMENT: int = 5
    MANAGER: int = 2
    MEMBERS: int = 3
    PLAYER_INFO: int = 4
    SHARE: int = 8
    name_to_values: dict = {'BRIEF': 1, 'MANAGER': 2, 'MEMBERS': 3, 'PLAYER_INFO': 4, 'FETCH_RECOMMENT': 5, 'ACH_LOGS': 6, 'APPLY_PLAYER_INFO': 7, 'SHARE': 8}
    value_to_names: dict = {1: 'BRIEF', 2: 'MANAGER', 3: 'MEMBERS', 4: 'PLAYER_INFO', 5: 'FETCH_RECOMMENT', 6: 'ACH_LOGS', 7: 'APPLY_PLAYER_INFO', 8: 'SHARE'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class JournalType(enum):
    ASSIGN: int = 3
    ASSIGN_CEO: int = 7
    IMPEACH: int = 6
    JOIN: int = 1
    KICK: int = 9
    LEAVE: int = 2
    NONE: int = 0
    OFFLINE: int = 10
    UNLOCK_HERO: int = 8
    UPGRADE: int = 4
    USURP: int = 5
    name_to_values: dict = {'NONE': 0, 'JOIN': 1, 'LEAVE': 2, 'ASSIGN': 3, 'UPGRADE': 4, 'USURP': 5, 'IMPEACH': 6, 'ASSIGN_CEO': 7, 'UNLOCK_HERO': 8, 'KICK': 9, 'OFFLINE': 10}
    value_to_names: dict = {0: 'NONE', 1: 'JOIN', 2: 'LEAVE', 3: 'ASSIGN', 4: 'UPGRADE', 5: 'USURP', 6: 'IMPEACH', 7: 'ASSIGN_CEO', 8: 'UNLOCK_HERO', 9: 'KICK', 10: 'OFFLINE'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class KickErrno(enum):
    FAILED: int = 3
    FORBIDDEN: int = 875
    NOT_ALLOWED: int = 4
    NOT_FOUND: int = 906
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'NOT_FOUND': 906, 'FORBIDDEN': 875, 'FAILED': 3, 'NOT_ALLOWED': 4}
    value_to_names: dict = {0: 'SUCCESS', 906: 'NOT_FOUND', 875: 'FORBIDDEN', 3: 'FAILED', 4: 'NOT_ALLOWED'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class LeaveErrno(enum):
    FORBIDDEN: int = 3
    NO_CLAN: int = 1
    NO_MEMBER: int = 2
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'NO_CLAN': 1, 'NO_MEMBER': 2, 'FORBIDDEN': 3}
    value_to_names: dict = {0: 'SUCCESS', 1: 'NO_CLAN', 2: 'NO_MEMBER', 3: 'FORBIDDEN'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SendMailErrno(enum):
    BODY_OVER_LEN: int = 5
    CD: int = 6
    FORBIDDEN: int = 875
    FREEZING: int = 7
    INVALID: int = 896
    NO_CLAN: int = 880
    NUM_LIMIT: int = 917
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'NO_CLAN': 880, 'FORBIDDEN': 875, 'INVALID': 896, 'BODY_OVER_LEN': 5, 'CD': 6, 'FREEZING': 7, 'NUM_LIMIT': 917}
    value_to_names: dict = {0: 'SUCCESS', 880: 'NO_CLAN', 875: 'FORBIDDEN', 896: 'INVALID', 5: 'BODY_OVER_LEN', 6: 'CD', 7: 'FREEZING', 917: 'NUM_LIMIT'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class enum(object):
    name_to_values: dict = {}
    value_to_names: dict = {}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...


def CalcClanTotalQualifyingScore(members): ...
def CalcQualifyingLevel(qualifying_match_type, qualifying_score): ...
def CheckClanApplyConditionsSatisfied(avatar, clan_info): ...
def CheckQualifyingScore(score, rank, apply_score): ...
def DecodeLogKey(log_key): ...
def EnableClan(): ...
def GenLogKey(log_type, match_type=0, any=0): ...
def GetClanQualifyingLevel(total_scores, current_members): ...
def GetClanQueryKey(page, filters, hostnum, extra=None): ...
def GetClanRecommendKey(page, filters, hostnum, extra=None): ...
def GetClanRecommendOuterLinkKey(use_filter, filters, from_open, extra=None): ...
def GetMaxQualifyingLevel(q_scores): ...
def GetQualifyingScoreLevel(avatar): ...
def IsRegionValid(region_pids): ...
def IsStyleValid(styles): ...
def MergeDict(*dicts): ...


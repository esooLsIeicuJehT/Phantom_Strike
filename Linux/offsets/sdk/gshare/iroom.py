# module: gshare.iroom

import consts
import hashlib
import match_data
import room_data
import six2
import space_data

COMPONENT: str = 'Client'
MAX_WATCHER_COUNT: int = 30
WATCHER_SLOT_OFFSET: int = 10000

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

class DeviceType(enum):
    Mobile: int = 1
    PC: int = 2
    name_to_values: dict = {'Mobile': 1, 'PC': 2}
    value_to_names: dict = {1: 'Mobile', 2: 'PC'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class IRoom(CustomMapType):
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

    def CanChangeOption(self, options): ...
    def CanKickout(self, owner_id, target_id): ...
    def CanMatch(self, avatar_id): ...
    def GetMember(self, avatar_id): ...
    def GetMemberRoomSlot(self, avatar_id): ...
    def IsGameMember(self, avatarid): ...
    def IsInRoom(self, avatarid): ...
    def IsRoomOwner(self, avatarid): ...
    def IsRoomWatcher(self, avatarid): ...
    def IsValidSlot(self, slot): ...
    def IsWaitingState(self): ...
    def Pack(self): ...
    def PackCommon(self): ...
    def PackMetaInfo(self): ...
    def UpdteOptions(self, options): ...
    def _initProperty(self, data): ...
    @property
    def battle_count(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def need_password(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    @property
    def team_count(self): ...    def update2(self, data): ...
    def values(self): ...
    @property
    def watcher_count(self): ...
class IRoomMember(PlayerFrame):
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

    def HasMap(self, spaceno): ...
    def _initProperty(self, data): ...
    @property
    def is_battler(self): ...    @property
    def is_watcher(self): ...    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class IRoomMembers(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.iroom.IRoomMember'>
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

class JoinRoomCode(enum):
    Destroy: int = 5
    Full: int = 1
    Gaming: int = 3
    InRoom: int = 4
    Password: int = 2
    Success: int = 0
    name_to_values: dict = {'Success': 0, 'Full': 1, 'Password': 2, 'Gaming': 3, 'InRoom': 4, 'Destroy': 5}
    value_to_names: dict = {0: 'Success', 1: 'Full', 2: 'Password', 3: 'Gaming', 4: 'InRoom', 5: 'Destroy'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class NoPersistentTitles(CustomListType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.ititle.NoPersistentTitle'>
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

class OptionKey(enum):
    AirdropStore: str = 'airdrop_store'
    AirdropSword: str = 'airdrop_sword'
    Airdrops: str = 'airdrop'
    AssistAim: str = 'assist_aim'
    AutoReborn: str = 'relive'
    BattleTime: str = 'time'
    CanBuyTacticalLevel: str = 'can_buy_tactical_level'
    Coins: str = 'coins_range'
    DamageTeammate: str = 'damage_teammate'
    DisableBot: str = 'disable_bot'
    DisableSkill: str = 'disable_skill'
    ForbidAssistAim: str = 'forbid_assist_aim'
    HS_ONLY: str = 'hs_only'
    InfAmmo: str = 'infinite_ammo'
    InitTacticalLevel: str = 'tactical_level'
    LeaderMode: str = 'leader_mode'
    MaxArmor: str = 'maxarmor'
    MaxHp: str = 'max_hp'
    NoDeathTactical: str = 'disable_death_tactical_energy'
    PutInVehicle: str = 'vehicle'
    RoundToWin: str = 'round_to_win'
    Rounds: str = 'round_range'
    SafeRegionDamage: str = 'safe_region_damage'
    SafeRegionSpeed: str = 'safe_region_speed'
    Score: str = 'score'
    TaskCount: str = 'task_count'
    TaskType: str = 'task_type'
    WeatherType: str = 'weather'
    ZombieBuyback: str = 'zombie_buyback'
    ZombieHp: str = 'zombie_hp'
    ZombieRebornItem: str = 'zombie_reborn_item'
    ZombieRevive: str = 'zombie_revive'
    name_to_values: dict = {'MaxHp': 'max_hp', 'MaxArmor': 'maxarmor', 'DamageTeammate': 'damage_teammate', 'InfAmmo': 'infinite_ammo', 'DisableSkill': 'disable_skill', 'ForbidAssistAim': 'forbid_assist_aim', 'Rounds': 'round_range', 'LeaderMode': 'leader_mode', 'RoundToWin': 'round_to_win', 'Coins': 'coins_range', 'InitTacticalLevel': 'tactical_level', 'CanBuyTacticalLevel': 'can_buy_tactical_level', 'AutoReborn': 'relive', 'WeatherType': 'weather', 'PutInVehicle': 'vehicle', 'SafeRegionSpeed': 'safe_region_speed', 'SafeRegionDamage': 'safe_region_damage', 'Airdrops': 'airdrop', 'TaskCount': 'task_count', 'TaskType': 'task_type', 'AirdropStore': 'airdrop_store', 'AssistAim': 'assist_aim', 'DisableBot': 'disable_bot', 'NoDeathTactical': 'disable_death_tactical_energy', 'Score': 'score', 'BattleTime': 'time', 'AirdropSword': 'airdrop_sword', 'ZombieRevive': 'zombie_revive', 'ZombieHp': 'zombie_hp', 'ZombieRebornItem': 'zombie_reborn_item', 'ZombieBuyback': 'zombie_buyback', 'HS_ONLY': 'hs_only'}
    value_to_names: dict = {'max_hp': 'MaxHp', 'maxarmor': 'MaxArmor', 'damage_teammate': 'DamageTeammate', 'infinite_ammo': 'InfAmmo', 'disable_skill': 'DisableSkill', 'forbid_assist_aim': 'ForbidAssistAim', 'round_range': 'Rounds', 'leader_mode': 'LeaderMode', 'round_to_win': 'RoundToWin', 'coins_range': 'Coins', 'tactical_level': 'InitTacticalLevel', 'can_buy_tactical_level': 'CanBuyTacticalLevel', 'relive': 'AutoReborn', 'weather': 'WeatherType', 'vehicle': 'PutInVehicle', 'safe_region_speed': 'SafeRegionSpeed', 'safe_region_damage': 'SafeRegionDamage', 'airdrop': 'Airdrops', 'task_count': 'TaskCount', 'task_type': 'TaskType', 'airdrop_store': 'AirdropStore', 'assist_aim': 'AssistAim', 'disable_bot': 'DisableBot', 'disable_death_tactical_energy': 'NoDeathTactical', 'score': 'Score', 'time': 'BattleTime', 'airdrop_sword': 'AirdropSword', 'zombie_revive': 'ZombieRevive', 'zombie_hp': 'ZombieHp', 'zombie_reborn_item': 'ZombieRebornItem', 'zombie_buyback': 'ZombieBuyback', 'hs_only': 'HS_ONLY'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class OptionType(enum):
    Hard: int = 2
    Normal: int = 1
    Relaxed: int = 3
    UserDefine: int = 4
    name_to_values: dict = {'Normal': 1, 'Hard': 2, 'Relaxed': 3, 'UserDefine': 4}
    value_to_names: dict = {1: 'Normal', 2: 'Hard', 3: 'Relaxed', 4: 'UserDefine'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PlayerFrame(CustomMapType):
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

class RoomDeviceType(enum):
    Mobile: int = 1
    PC: int = 2
    name_to_values: dict = {'Mobile': 1, 'PC': 2}
    value_to_names: dict = {1: 'Mobile', 2: 'PC'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RoomStatus(enum):
    Gaming: int = 2
    Waiting: int = 1
    name_to_values: dict = {'Waiting': 1, 'Gaming': 2}
    value_to_names: dict = {1: 'Waiting', 2: 'Gaming'}

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


def GetMd5(password): ...
def GetOptionsByType(match_type, option_type): ...
def IsBattleSlot(slot): ...
def Property(name, default, flag=2): ...


# module: gclient.gamesystem.uihall.room.room_config

import consts

RoomCheckboxOptionList: list = ['relive', 'damage_teammate', 'infinite_ammo', 'disable_skill', 'airdrop_store', 'vehicle', 'leader_mode', 'zombie_reborn_item', 'zombie_buyback', 'hs_only']
RoomComboxOptionList: list = ['weather', 'airdrop', 'safe_region_speed', 'safe_region_damage', 'task_type', 'max_hp', 'round_range', 'coins_range', 'assist_aim', 'score', 'time', 'airdrop_sword', 'zombie_hp', 'zombie_revive']
RoomMatchTypeList: list = [1004, 1200, 1400, 1800, 1012, 1900]
_reload_all: bool = True

class AirdropPostType(enum):
    FREQUENT: int = 2
    NORMAL: int = 1
    NULL: int = 0
    name_to_values: dict = {'NULL': 0, 'NORMAL': 1, 'FREQUENT': 2}
    value_to_names: dict = {0: 'NULL', 1: 'NORMAL', 2: 'FREQUENT'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ContractType(enum):
    CRYSTAL: int = 4
    ESCORT: int = 5
    HUNT: int = 3
    NONE: int = 0
    OCCUPY: int = 1
    SEARCH: int = 2
    SafeBox: int = 7
    WORSHIP: int = 6
    name_to_values: dict = {'NONE': 0, 'OCCUPY': 1, 'SEARCH': 2, 'HUNT': 3, 'CRYSTAL': 4, 'ESCORT': 5, 'WORSHIP': 6, 'SafeBox': 7}
    value_to_names: dict = {0: 'NONE', 1: 'OCCUPY', 2: 'SEARCH', 3: 'HUNT', 4: 'CRYSTAL', 5: 'ESCORT', 6: 'WORSHIP', 7: 'SafeBox'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

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

class RoomAirDrop(enum):
    Frequent: int = 2
    Null: int = 0
    Standard: int = 1
    name_to_values: dict = {'Standard': 1, 'Frequent': 2, 'Null': 0}
    value_to_names: dict = {1: 'Standard', 2: 'Frequent', 0: 'Null'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RoomAssistAim(enum):
    ForbidAll: int = 2
    ForbidNew: int = 1
    NONE: int = 0
    name_to_values: dict = {'NONE': 0, 'ForbidNew': 1, 'ForbidAll': 2}
    value_to_names: dict = {0: 'NONE', 1: 'ForbidNew', 2: 'ForbidAll'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RoomBaseConfig(object):
    DefaultShowOption: list = ['relive', 'damage_teammate', 'airdrop_store', 'assist_aim']
    RoomModeList: list = [1, 2, 3, 4]

class RoomGunfightConfig(object):
    DefaultShowOption: list = ['damage_teammate', 'infinite_ammo', 'round_to_win', 'leader_mode', 'assist_aim']
    RoomModeList: list = [1, 4]

class RoomHotspotConfig(object):
    RoomModeList: list = [1, 2, 4]

class RoomMobaConfig(object):
    DefaultShowOption: list = ['relive', 'damage_teammate', 'airdrop_store', 'assist_aim']
    RoomModeList: list = [1, 2, 4]

class RoomRoundCount(enum):
    name_to_values: dict = {}
    value_to_names: dict = {}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RoomSafeRegionDamage(enum):
    High: float = 1.5
    Low: float = 0.5
    Standard: float = 1.0
    name_to_values: dict = {'Standard': 1.0, 'High': 1.5, 'Low': 0.5}
    value_to_names: dict = {1.0: 'Standard', 1.5: 'High', 0.5: 'Low'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RoomSafeRegionSpeed(enum):
    Fast: float = 1.5
    Slow: float = 0.5
    Standard: float = 1.0
    name_to_values: dict = {'Standard': 1.0, 'Fast': 1.5, 'Slow': 0.5}
    value_to_names: dict = {1.0: 'Standard', 1.5: 'Fast', 0.5: 'Slow'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RoomSnipeConfig(object):
    DefaultShowOption: list = ['score', 'infinite_ammo', 'hs_only']
    RoomModeList: list = [1, 4]

class RoomSquadfightConfig(object):
    DefaultShowOption: list = ['round_range', 'damage_teammate', 'infinite_ammo', 'disable_skill', 'assist_aim']
    RoomModeList: list = [1, 2, 3, 4]

class RoomTaskCount(enum):
    Less: float = 0.5
    Null: int = 0
    Standard: float = 1.0
    name_to_values: dict = {'Standard': 1.0, 'Less': 0.5, 'Null': 0}
    value_to_names: dict = {1.0: 'Standard', 0.5: 'Less', 0: 'Null'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RoomTaskType(enum):
    MoreKill: int = 3
    MoreOccupy: int = 1
    MoreSearch: int = 2
    Standard: int = 0
    name_to_values: dict = {'Standard': 0, 'MoreKill': 3, 'MoreOccupy': 1, 'MoreSearch': 2}
    value_to_names: dict = {0: 'Standard', 3: 'MoreKill', 1: 'MoreOccupy', 2: 'MoreSearch'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RoomWeather(enum):
    Cloudy: int = 2
    Rain: int = 1
    Standard: int = -1
    Sunny: int = 0
    name_to_values: dict = {'Standard': -1, 'Sunny': 0, 'Rain': 1, 'Cloudy': 2}
    value_to_names: dict = {-1: 'Standard', 0: 'Sunny', 1: 'Rain', 2: 'Cloudy'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RoomZombieConfig(object):
    DefaultShowOption: list = ['relive', 'assist_aim']
    RoomModeList: list = [1, 4]

class RoomZombieReviveFrequency(enum):
    High: int = 2
    Low: int = 0
    Mid: int = 1
    name_to_values: dict = {'Low': 0, 'Mid': 1, 'High': 2}
    value_to_names: dict = {0: 'Low', 1: 'Mid', 2: 'High'}

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



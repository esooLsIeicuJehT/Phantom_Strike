# module: gshare.icc_voice

CC_NAME: dict = {5: 'team', 1: 'team', 2: 'nearby', 3: 'ridicule', 6: 'room'}
CC_Nearby_Maxuser: int = 100
CC_Nearby_Radius: int = 50
CC_Nearby_Radius_Map: dict = {1400: 100}
IG_CHANNEL_LIST: list = [1, 2, 3, 4]

class CCChannelType(enum):
    CombatHallTeam: int = 4
    CombatTeam: int = 1
    HallTeam: int = 5
    KillRidicule: int = 3
    Nearby: int = 2
    NoMike: int = 0
    Room: int = 6
    name_to_values: dict = {'NoMike': 0, 'CombatTeam': 1, 'Nearby': 2, 'KillRidicule': 3, 'CombatHallTeam': 4, 'HallTeam': 5, 'Room': 6}
    value_to_names: dict = {0: 'NoMike', 1: 'CombatTeam', 2: 'Nearby', 3: 'KillRidicule', 4: 'CombatHallTeam', 5: 'HallTeam', 6: 'Room'}

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



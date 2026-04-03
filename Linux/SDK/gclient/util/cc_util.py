# module: gclient.util.cc_util

import MConfig
import MPlatform
import cconst
import config
import formula
import six2

CC_Channel_Open_Map: dict = {1: (1,), 2: (2, 1)}
CC_SID_COMBAT_TEAM: int = 4
CC_SID_MAP: dict = {5: 0, 1: 4, 2: 1, 3: 2, 6: 3}
CC_SID_NEARBY: int = 1
CC_SID_RIDICULE: int = 2
CC_SID_ROOM: int = 3
CC_SID_TEAM: int = 0
CC_SID_TOTAL: int = 5
GLOBAL_TEAMMATE_VOLUME: dict = {}

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


def GetCombatTeammateVolume(teammate_id): ...
def HasRecordPermission(): ...
def RefreshCombatTeammateVolume(teammate_id): ...
def RefreshHallTeammateVolume(teammate_id): ...
def RequestRecordPermission(callback=None): ...
def SetCombatTeammateVolume(teammate_id, masterid, volume): ...
def SetHallTeammateVolume(teammate_id, volume): ...
def UpdateCCVolume(): ...
def UpdateMicRatio(): ...


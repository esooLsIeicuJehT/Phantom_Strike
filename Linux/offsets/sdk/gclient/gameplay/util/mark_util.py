# module: gclient.gameplay.util.mark_util

import consts
import events
import formula
import replay_util
import scene_node_data
import six2

class ParaAvatarStage(enum):
    Cinematics: int = 1
    CloseParachute: int = 6
    Default: int = 0
    Finish: int = 9
    FreeFall: int = 3
    FreeFallWithWeapon: int = 4
    LandGround: int = 8
    OnAircraft: int = 2
    OpenParachute: int = 5
    Parachute: int = 7
    name_to_values: dict = {'Default': 0, 'Cinematics': 1, 'OnAircraft': 2, 'FreeFall': 3, 'FreeFallWithWeapon': 4, 'OpenParachute': 5, 'CloseParachute': 6, 'Parachute': 7, 'LandGround': 8, 'Finish': 9}
    value_to_names: dict = {0: 'Default', 1: 'Cinematics', 2: 'OnAircraft', 3: 'FreeFall', 4: 'FreeFallWithWeapon', 5: 'OpenParachute', 6: 'CloseParachute', 7: 'Parachute', 8: 'LandGround', 9: 'Finish'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...


def GetPlayerIdBySlot(slot): ...
def GetPlayerOwnSlot(): ...
def PlayMarkSound(pos, mark_type): ...
def TeammateMarkOnSetattrImp(key, old, new, member_id): ...


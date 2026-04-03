# module: gclient.gamesystem.uihall.room.room_util

import lang

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


def GetRoomModeText(room_mode): ...


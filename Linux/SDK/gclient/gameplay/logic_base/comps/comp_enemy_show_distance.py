# module: gclient.gameplay.logic_base.comps.comp_enemy_show_distance

import formula
import replay_util
import six2

class EPerformanceLevel(enum):
    LEVEL_0: int = 0
    LEVEL_1: int = 1
    LEVEL_2: int = 2
    LEVEL_3: int = 3
    LEVEL_4: int = 4
    LEVEL_5: int = 5
    LEVEL_HIGHEST: int = 10
    name_to_values: dict = {'LEVEL_0': 0, 'LEVEL_1': 1, 'LEVEL_2': 2, 'LEVEL_3': 3, 'LEVEL_4': 4, 'LEVEL_5': 5, 'LEVEL_HIGHEST': 10}
    value_to_names: dict = {0: 'LEVEL_0', 1: 'LEVEL_1', 2: 'LEVEL_2', 3: 'LEVEL_3', 4: 'LEVEL_4', 5: 'LEVEL_5', 10: 'LEVEL_HIGHEST'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GameLogicEnemyShowStateComp(object):
    DISTANCE_FOR_SHOW_ENEMY_EFFECT: int = 50

    def TickEnemyDistanceForShow(self): ...



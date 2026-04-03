# module: gclient.gameplay.logic_base.entities.combatavatarmembers.cimp_report

import consts
import six2

class DeadType(enum):
    AVATAR: int = 1
    FALL: int = 3
    SAFE_REGION: int = 2
    UNKNOWN: int = 0
    name_to_values: dict = {'UNKNOWN': 0, 'AVATAR': 1, 'SAFE_REGION': 2, 'FALL': 3}
    value_to_names: dict = {0: 'UNKNOWN', 1: 'AVATAR', 2: 'SAFE_REGION', 3: 'FALL'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PlayerCombatAvatarMember(object):
    def GenerateReportDataInGame(self): ...



# module: gclient.gameplay.logic_dlc.ui.squad_fight_hud_bottom_like_comp

import events

class BackpackSlot(enum):
    ARMOR_PIECE: int = 5002
    CRACK_SCANNER: int = 5004
    EMERGENCY_NEEDLE: int = 5003
    FAKE_SLOT_1: int = 8001
    FAKE_SLOT_2: int = 8002
    LAUNCHER_WEAPON: int = 1005
    MEDICINE_1: int = 7001
    MEDICINE_2: int = 7002
    NONE: int = 0
    SKILL_WEAPON: int = 4001
    SKILL_WEAPON2: int = 4002
    SKILL_WEAPON3: int = 4003
    SUPPORT_WEAPON: int = 5001
    TACTICAL_WEAPON_1: int = 3001
    TACTICAL_WEAPON_2: int = 3002
    TALENT_1: int = 6001
    TALENT_2: int = 6002
    VICE_WEAPON: int = 1003
    WEAPON_1: int = 1001
    WEAPON_2: int = 1002
    WEAPON_3: int = 1004
    name_to_values: dict = {'NONE': 0, 'WEAPON_1': 1001, 'WEAPON_2': 1002, 'WEAPON_3': 1004, 'VICE_WEAPON': 1003, 'LAUNCHER_WEAPON': 1005, 'TACTICAL_WEAPON_1': 3001, 'TACTICAL_WEAPON_2': 3002, 'SKILL_WEAPON': 4001, 'SKILL_WEAPON2': 4002, 'SKILL_WEAPON3': 4003, 'SUPPORT_WEAPON': 5001, 'ARMOR_PIECE': 5002, 'EMERGENCY_NEEDLE': 5003, 'CRACK_SCANNER': 5004, 'MEDICINE_1': 7001, 'MEDICINE_2': 7002, 'TALENT_1': 6001, 'TALENT_2': 6002, 'FAKE_SLOT_1': 8001, 'FAKE_SLOT_2': 8002}
    value_to_names: dict = {0: 'NONE', 1001: 'WEAPON_1', 1002: 'WEAPON_2', 1004: 'WEAPON_3', 1003: 'VICE_WEAPON', 1005: 'LAUNCHER_WEAPON', 3001: 'TACTICAL_WEAPON_1', 3002: 'TACTICAL_WEAPON_2', 4001: 'SKILL_WEAPON', 4002: 'SKILL_WEAPON2', 4003: 'SKILL_WEAPON3', 5001: 'SUPPORT_WEAPON', 5002: 'ARMOR_PIECE', 5003: 'EMERGENCY_NEEDLE', 5004: 'CRACK_SCANNER', 7001: 'MEDICINE_1', 7002: 'MEDICINE_2', 6001: 'TALENT_1', 6002: 'TALENT_2', 8001: 'FAKE_SLOT_1', 8002: 'FAKE_SLOT_2'}

    def IsSkill(slot): ...
    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SquadFightHudBottomLikeComp(object):
    def OnUpdateItemCount(self, item, old, new): ...



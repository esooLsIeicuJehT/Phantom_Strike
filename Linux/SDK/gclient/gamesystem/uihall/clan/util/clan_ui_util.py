# module: gclient.gamesystem.uihall.clan.util.clan_ui_util

import cconst
import clan_log_data
import common_ui_util
import ichat
import iclan
import lobby_item_data
import match_client_data
import rank_level_data
import six2
import ui_helper

CLAN_APPLY_CD: int = 30
CLAN_ROLE_TYPE_TEXT_DICT: dict = {0: 0, 1: 937, 2: 938, 4: 939, 8: 940}
CLAN_STYLE_CATEGORIES: range = range(1, 4)
CLAN_STYLE_CATEGORY_ACTIVE: int = 3
CLAN_STYLE_CATEGORY_BATTLE: int = 1
CLAN_STYLE_CATEGORY_NAME_DICT: dict = {1: 928, 2: 929, 3: 930}
CLAN_STYLE_CATEGORY_SOCIAL: int = 2

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


def CalcQualifyingLevel(qualifying_score, match_type=1004, cache=False): ...
def GetClanLogContent(log_info): ...
def GetClanLogContentByType_2(log_type, match_type, value, log_info): ...
def GetClanLogContentByType_4(log_type, match_type, value, log_info): ...
def GetClanLogLikeContent(msg): ...
def GetClanLogLikeContentByLogKey(log_key): ...
def GetClanRoleName(role_type): ...
def GetCommonClanLogContent(log_type, match_type, value, log_info): ...


# module: gshare.ichat

import chat_language_data
import copy
import six2

CHANNEL: int = 2
CHAT_BUBBLES: int = 14
CLAN_CHANNEL_CD: int = 60
COMPONENT: str = 'Client'
CONTENT: int = 3
EXTRA: int = 12
FROM: int = 6
GUID: int = 1
HEAD_FRAME: int = 13
IG_MESSAGE_TYPES: tuple = (3, 2, 4)
LANG_CHANNEL_CD: int = 10
LANG_CHANNEL_HEAD: str = 'Lang_'
MSG_TYPE: int = 10
NAME: int = 7
OFFICIAL_HEAD: int = 9
SEGMENT: int = 8
SEND_TIME: int = 11
SHARE_MSG_TYPES: tuple = (15, 14, 13)
SOUND: int = 4
TO: int = 5
VERSION: int = 0
WORLD_CHANNEL_CD: int = 10
channel: int = 106
cur_version: int = 16
key: str = 'th'
key_num: int = 15
msg_sample: list = [16, '', '', '', '', '', '', '', '', '', '', '', '', '', '']
name: str = 'Lang_th'
proto: taggeddict = {'channel': 106, 'channel_pic': 11320, 'id': 'th'}

class ChatChannel(enum):
    Clan: int = 8
    CombatTeam: int = 1
    HallFriend: int = 4
    HallRecruit: int = 6
    HallTeam: int = 2
    HallWorld: int = 3
    Lang_ar: int = 108
    Lang_en: int = 102
    Lang_es: int = 103
    Lang_in: int = 105
    Lang_ja: int = 110
    Lang_pt: int = 104
    Lang_ru: int = 107
    Lang_th: int = 106
    Lang_tw: int = 109
    Lang_zh: int = 101
    Room: int = 7
    System: int = 5
    name_to_values: dict = {'CombatTeam': 1, 'HallTeam': 2, 'HallWorld': 3, 'HallFriend': 4, 'System': 5, 'HallRecruit': 6, 'Room': 7, 'Clan': 8, 'Lang_in': 105, 'Lang_ar': 108, 'Lang_en': 102, 'Lang_es': 103, 'Lang_ja': 110, 'Lang_zh': 101, 'Lang_ru': 107, 'Lang_pt': 104, 'Lang_tw': 109, 'Lang_th': 106}
    value_to_names: dict = {1: 'CombatTeam', 2: 'HallTeam', 3: 'HallWorld', 4: 'HallFriend', 5: 'System', 6: 'HallRecruit', 7: 'Room', 8: 'Clan', 105: 'Lang_in', 108: 'Lang_ar', 102: 'Lang_en', 103: 'Lang_es', 110: 'Lang_ja', 101: 'Lang_zh', 107: 'Lang_ru', 104: 'Lang_pt', 109: 'Lang_tw', 106: 'Lang_th'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class IdManager(object):
    def bytes2id(bytes): ...
    def genid(): ...
    def id2bytes(uid): ...
    def id2str(uid): ...
    def is_valid_id(entityid): ...
    def str2id(string): ...

class MessageType(enum):
    ClanAch: int = 11
    ClanAchLike: int = 12
    ClanJion: int = 9
    ClanQuick: int = 10
    IgMarkMsg: int = 3
    IgRequestItem: int = 8
    IgShortMsg: int = 2
    Normal: int = 1
    Recruit: int = 6
    ShareClan: int = 15
    ShareCombat: int = 13
    ShareGun: int = 14
    SystemHorn: int = 5
    TeamReservation: int = 4
    Voice: int = 7
    name_to_values: dict = {'Normal': 1, 'IgShortMsg': 2, 'IgMarkMsg': 3, 'TeamReservation': 4, 'SystemHorn': 5, 'Recruit': 6, 'Voice': 7, 'IgRequestItem': 8, 'ClanJion': 9, 'ClanQuick': 10, 'ClanAch': 11, 'ClanAchLike': 12, 'ShareCombat': 13, 'ShareGun': 14, 'ShareClan': 15}
    value_to_names: dict = {1: 'Normal', 2: 'IgShortMsg', 3: 'IgMarkMsg', 4: 'TeamReservation', 5: 'SystemHorn', 6: 'Recruit', 7: 'Voice', 8: 'IgRequestItem', 9: 'ClanJion', 10: 'ClanQuick', 11: 'ClanAch', 12: 'ClanAchLike', 13: 'ShareCombat', 14: 'ShareGun', 15: 'ShareClan'}

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


def IsLangChannel(channel): ...
def NewMsg(): ...
def NewRecruitMsg(avatar, extra): ...
def NewSystemChat(content, code, args, limit_info=None, channel=5, msg_type=5, **extras): ...
def NewSystemHorn(content, limit_info): ...


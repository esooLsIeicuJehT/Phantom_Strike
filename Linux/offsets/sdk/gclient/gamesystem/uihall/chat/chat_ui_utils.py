# module: gclient.gamesystem.uihall.chat.chat_ui_utils

import consts
import gun_ui_util
import ichat
import iclan
import izone
import match_client_data
import six2
import text_message_data
import ui_helper

AT_TEXT_TEMPLATE: str = '#0000ff%s#E'
SHARE_TEMPLATE_DICT: dict = {13: 771, 14: 772, 15: 773}

class CustomMapType(area_map):
    IS_CUSTOM_TYPE: bool = True
    clear: method_descriptor = <method 'clear' of 'area_map' objects>
    copy: method_descriptor = <method 'copy' of 'area_map' objects>
    dict: method_descriptor = <method 'dict' of 'area_map' objects>
    dsize: method_descriptor = <method 'dsize' of 'area_map' objects>
    get: method_descriptor = <method 'get' of 'area_map' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_map' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_map' objects>
    iteritems: method_descriptor = <method 'iteritems' of 'area_map' objects>
    iterkeys: method_descriptor = <method 'iterkeys' of 'area_map' objects>
    itervalues: method_descriptor = <method 'itervalues' of 'area_map' objects>
    normal_iteritems: method_descriptor = <method 'normal_iteritems' of 'area_map' objects>
    normal_iterkeys: method_descriptor = <method 'normal_iterkeys' of 'area_map' objects>
    normal_itervalues: method_descriptor = <method 'normal_itervalues' of 'area_map' objects>
    pop: method_descriptor = <method 'pop' of 'area_map' objects>
    props_all: method_descriptor = <method 'props_all' of 'area_map' objects>
    size: method_descriptor = <method 'size' of 'area_map' objects>
    total_size: method_descriptor = <method 'total_size' of 'area_map' objects>
    update: method_descriptor = <method 'update' of 'area_map' objects>
    weak_dict: method_descriptor = <method 'weak_dict' of 'area_map' objects>

    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

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


def CheckChatInputKeyTextDelete(last_text, new_text, key_text, has_ime): ...
def GenChatMatchName(match_type, space_no, hall_match_type=None): ...
def GetAtTextByMsg(msg): ...
def GetShareInfo(share_type, *share_data): ...
def GetShareInfoByShareType_ShareClan(clan): ...
def GetShareInfoByShareType_ShareCombat(match_type, combat_record): ...
def GetShareInfoByShareType_ShareGun(weapon, sp_info=None): ...
def GetShareTextByMsg(msg): ...
def GetShareTextByShareInfo(share_type, share_info): ...
def PostShareInfo_ShareClan(share_type, share_info): ...
def PostShareInfo_ShareCombat(share_type, share_info): ...
def PostShareInfo_ShareGun(share_type, share_info): ...


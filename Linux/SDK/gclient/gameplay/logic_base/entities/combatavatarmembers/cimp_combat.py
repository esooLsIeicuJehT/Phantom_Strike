# module: gclient.gameplay.logic_base.entities.combatavatarmembers.cimp_combat

import cdata_util
import events
import praise_feedback_data
import random
import six2
import string_message_data

CLIENT_STUB: int = 8

class CombatAvatarMember(object):
    def OnReceiveLike(self, info): ...

class Dict(object):
    convert: method_descriptor = <method 'convert' of 'dict' objects>
    get_type: method_descriptor = <method 'get_type' of 'dict' objects>
    getname: method_descriptor = <method 'getname' of 'dict' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'dict' objects>
    name: getset_descriptor = <attribute 'name' of 'dict' objects>

class PlayerCombatAvatarMember(CombatAvatarMember):
    def LikeTeammateId(self, t_id, key): ...
    def OnReceiveLike(self, info): ...

class SettleBeLikedType(enum):
    Achieve: int = 7
    MVP_ACE: int = 4
    MemberBuy: int = 5
    PickMemberEquip: int = 2
    PickMemberMark: int = 3
    RealBuyMember: int = 8
    Revive: int = 1
    SquadFightBuy: int = 9
    Watch: int = 6
    name_to_values: dict = {'Revive': 1, 'PickMemberEquip': 2, 'PickMemberMark': 3, 'MVP_ACE': 4, 'MemberBuy': 5, 'Watch': 6, 'Achieve': 7, 'RealBuyMember': 8, 'SquadFightBuy': 9}
    value_to_names: dict = {1: 'Revive', 2: 'PickMemberEquip', 3: 'PickMemberMark', 4: 'MVP_ACE', 5: 'MemberBuy', 6: 'Watch', 7: 'Achieve', 8: 'RealBuyMember', 9: 'SquadFightBuy'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...


def Property(name, default, flag=2): ...
def rpc_method(rpctype, *types): ...


# module: gclient.gamesystem.entities.avatarmembers.cimp_recruit

import cconst
import cdata_util
import events
import ichat
import irecruit
import six2

CLIENT_STUB: int = 8

class BinData(object):
    convert: method_descriptor = <method 'convert' of 'bin' objects>
    get_type: method_descriptor = <method 'get_type' of 'bin' objects>
    getname: method_descriptor = <method 'getname' of 'bin' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'bin' objects>
    name: getset_descriptor = <attribute 'name' of 'bin' objects>

class DeviceType(enum):
    Mobile: int = 1
    PC: int = 2
    name_to_values: dict = {'Mobile': 1, 'PC': 2}
    value_to_names: dict = {1: 'Mobile', 2: 'PC'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class Dict(object):
    convert: method_descriptor = <method 'convert' of 'dict' objects>
    get_type: method_descriptor = <method 'get_type' of 'dict' objects>
    getname: method_descriptor = <method 'getname' of 'dict' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'dict' objects>
    name: getset_descriptor = <attribute 'name' of 'dict' objects>

class EntityID(object):
    convert: method_descriptor = <method 'convert' of 'entityid' objects>
    get_type: method_descriptor = <method 'get_type' of 'entityid' objects>
    getname: method_descriptor = <method 'getname' of 'entityid' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'entityid' objects>
    name: getset_descriptor = <attribute 'name' of 'entityid' objects>

class Float(object):
    convert: method_descriptor = <method 'convert' of 'float' objects>
    get_type: method_descriptor = <method 'get_type' of 'float' objects>
    getname: method_descriptor = <method 'getname' of 'float' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'float' objects>
    name: getset_descriptor = <attribute 'name' of 'float' objects>

class Int(object):
    convert: method_descriptor = <method 'convert' of 'int' objects>
    get_type: method_descriptor = <method 'get_type' of 'int' objects>
    getname: method_descriptor = <method 'getname' of 'int' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'int' objects>
    name: getset_descriptor = <attribute 'name' of 'int' objects>

class List(object):
    convert: method_descriptor = <method 'convert' of 'list' objects>
    get_type: method_descriptor = <method 'get_type' of 'list' objects>
    getname: method_descriptor = <method 'getname' of 'list' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'list' objects>
    name: getset_descriptor = <attribute 'name' of 'list' objects>

class PlayerAvatarMember(object):
    def AddRecruitMsg(self, msg): ...
    def CheckAcceptRecruit(self, match_type, division): ...
    def ClearRecruitMsg(self): ...
    def DelRecruitMsg(self, msg_guid): ...
    def DeleteRecruit(self, a_id): ...
    def GetMyRecruitInfo(self, old=None): ...
    def GetRecruitGuids(self): ...
    def GetRecruitGuidsByFilterInfo(self, match_id, language_code, mic, channel): ...
    def GetRecruitMessage(self, guid): ...
    def OnGetCurrentRecruitTeamInfo(self, info): ...
    def OnJoinRecruitTeam(self, a_id): ...
    def RefreshRecruitInfo(self): ...
    def TryGetCurrentRecruitTeamInfo(self): ...
    def _UpdateRecruitMsg(self, msg): ...
    def _on_set_recruit_team_guid(self, old): ...

class Str(object):
    convert: method_descriptor = <method 'convert' of 'str' objects>
    get_type: method_descriptor = <method 'get_type' of 'str' objects>
    getname: method_descriptor = <method 'getname' of 'str' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'str' objects>
    name: getset_descriptor = <attribute 'name' of 'str' objects>


def Property(name, default, flag=2): ...
def rpc_method(rpctype, *types): ...


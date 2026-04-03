# module: gclient.gameplay.logic_base.entities.combatavatarmembers.cimp_building

import events
import formula

CLIENT_STUB: int = 8

class CombatAvatarMember(object):
    def CheckIsOutDoor(self, door, position=None): ...

class Dict(object):
    convert: method_descriptor = <method 'convert' of 'dict' objects>
    get_type: method_descriptor = <method 'get_type' of 'dict' objects>
    getname: method_descriptor = <method 'getname' of 'dict' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'dict' objects>
    name: getset_descriptor = <attribute 'name' of 'dict' objects>

class DoorState(enum):
    DOOR_STATE_CLOSED: int = 0
    DOOR_STATE_INSIDE: int = 2
    DOOR_STATE_OUTSIDE: int = 1
    name_to_values: dict = {'DOOR_STATE_CLOSED': 0, 'DOOR_STATE_OUTSIDE': 1, 'DOOR_STATE_INSIDE': 2}
    value_to_names: dict = {0: 'DOOR_STATE_CLOSED', 1: 'DOOR_STATE_OUTSIDE', 2: 'DOOR_STATE_INSIDE'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class EntityID(object):
    convert: method_descriptor = <method 'convert' of 'entityid' objects>
    get_type: method_descriptor = <method 'get_type' of 'entityid' objects>
    getname: method_descriptor = <method 'getname' of 'entityid' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'entityid' objects>
    name: getset_descriptor = <attribute 'name' of 'entityid' objects>

class HumanoidMonsterBuilding(CombatAvatarMember):
    def CheckIsOutDoor(self, door, position=None): ...

class Int(object):
    convert: method_descriptor = <method 'convert' of 'int' objects>
    get_type: method_descriptor = <method 'get_type' of 'int' objects>
    getname: method_descriptor = <method 'getname' of 'int' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'int' objects>
    name: getset_descriptor = <attribute 'name' of 'int' objects>

class MonsterBuilding(CombatAvatarMember):
    def CheckIsOutDoor(self, door, position=None): ...

class PlayerCombatAvatarMember(object):
    def ChangeDoorState(self, door, is_open, player_position=None): ...
    def ChangeDoorStateForDouble(self, door, is_open, player_position=None): ...


def rpc_method(rpctype, *types): ...


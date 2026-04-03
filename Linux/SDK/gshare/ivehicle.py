# module: gshare.ivehicle

import formula
import six2
import vehicle_data

COMPONENT: str = 'Client'

class CustomListType(area_list):
    IS_CUSTOM_TYPE: bool = True
    append: method_descriptor = <method 'append' of 'area_list' objects>
    assign: method_descriptor = <method 'assign' of 'area_list' objects>
    clear: method_descriptor = <method 'clear' of 'area_list' objects>
    copy: method_descriptor = <method 'copy' of 'area_list' objects>
    delete: method_descriptor = <method 'delete' of 'area_list' objects>
    extend: method_descriptor = <method 'extend' of 'area_list' objects>
    get: method_descriptor = <method 'get' of 'area_list' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_list' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_list' objects>
    insert: method_descriptor = <method 'insert' of 'area_list' objects>
    list: method_descriptor = <method 'list' of 'area_list' objects>
    pop: method_descriptor = <method 'pop' of 'area_list' objects>
    size: method_descriptor = <method 'size' of 'area_list' objects>
    slice: method_descriptor = <method 'slice' of 'area_list' objects>
    sorted: method_descriptor = <method 'sorted' of 'area_list' objects>
    update: method_descriptor = <method 'update' of 'area_list' objects>

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

class DrivingState(enum):
    DrivingState_Accel: int = 2
    DrivingState_Brake: int = 1
    DrivingState_Static: int = 0
    name_to_values: dict = {'DrivingState_Static': 0, 'DrivingState_Brake': 1, 'DrivingState_Accel': 2}
    value_to_names: dict = {0: 'DrivingState_Static', 1: 'DrivingState_Brake', 2: 'DrivingState_Accel'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class IEntityMasterComponent(object):
class ISimpleCombatUnit(ISimpleCombatUnitBase):
    IsATM: bool = False
    IsATMGuardAI: bool = False
    IsAirDrop: bool = False
    IsAmmoBox: bool = False
    IsArrow: bool = False
    IsAttackDrone: bool = False
    IsAvatar: bool = False
    IsBarrieCannon: bool = False
    IsBomb: bool = False
    IsBuilding: bool = False
    IsChaosUav: bool = False
    IsCombatAvatar: bool = False
    IsCombatAvatarSniper: bool = False
    IsCombatAvatarZombieXray: bool = False
    IsCombatTeam: bool = False
    IsCombatUnit: bool = False
    IsContrabandPlane: bool = False
    IsCrack: bool = False
    IsCrow: bool = False
    IsCureUav: bool = False
    IsCureUavFix: bool = False
    IsDestructible: bool = False
    IsDummyCombatAvatar: bool = False
    IsEmoteTree: bool = False
    IsEnergyStronghold: bool = False
    IsEntityAttach: bool = False
    IsEntityMaster: bool = False
    IsGameLogic: bool = False
    IsGlass: bool = False
    IsHelenAI: bool = False
    IsHolographicRobot: bool = False
    IsIceWall: bool = False
    IsIgnoreCue: bool = False
    IsItem: bool = False
    IsItemSpaceSnare: bool = False
    IsMagicField: bool = False
    IsMonitorMissile: bool = False
    IsMonster: bool = False
    IsMovingPlatform: bool = False
    IsObserveAvatar: bool = False
    IsOccupyContractTarget: bool = False
    IsOccupyContractTargetNew: bool = False
    IsOilbox: bool = False
    IsPhyBall: bool = False
    IsPlayerCombatAvatar: bool = False
    IsPlayerObserveAvatar: bool = False
    IsPortableShop: bool = False
    IsRPGMissile: bool = False
    IsReplayPuppet: bool = False
    IsReplayRecorder: bool = False
    IsRobotCombatAvatar: bool = False
    IsRobotCombatAvatarZombie: bool = False
    IsSafeBox: bool = False
    IsSaveDrone: bool = False
    IsSaveMachine: bool = False
    IsScoutArrow: bool = False
    IsSearchContractBox: bool = False
    IsShield: bool = False
    IsShop: bool = False
    IsSimpleCombatUnit: bool = True
    IsSpellDrone: bool = False
    IsStickyMaster: bool = False
    IsStronghold: bool = False
    IsStropUav: bool = False
    IsSupply: bool = False
    IsSwordSpirit: bool = False
    IsSyncTransEntity: bool = False
    IsSystemKiller: bool = False
    IsVehicle: bool = False
    IsVirtualInteractionEntity: bool = False
    NinjaBeacon: bool = False
    is_fps_avatar: bool = False
    is_replay_avatar: bool = False
    is_replay_room: bool = False

    @property
    def is_alive(self): ...    @property
    def is_invincible(self): ...
class IVehicle(ISimpleCombatUnit):
    IsATM: bool = False
    IsATMGuardAI: bool = False
    IsAirDrop: bool = False
    IsAmmoBox: bool = False
    IsArrow: bool = False
    IsAttackDrone: bool = False
    IsAvatar: bool = False
    IsBarrieCannon: bool = False
    IsBomb: bool = False
    IsBuilding: bool = False
    IsChaosUav: bool = False
    IsCombatAvatar: bool = False
    IsCombatAvatarSniper: bool = False
    IsCombatAvatarZombieXray: bool = False
    IsCombatTeam: bool = False
    IsCombatUnit: bool = False
    IsContrabandPlane: bool = False
    IsCrack: bool = False
    IsCrow: bool = False
    IsCureUav: bool = False
    IsCureUavFix: bool = False
    IsDestructible: bool = False
    IsDummyCombatAvatar: bool = False
    IsEmoteTree: bool = False
    IsEnergyStronghold: bool = False
    IsEntityAttach: bool = False
    IsEntityMaster: bool = False
    IsGameLogic: bool = False
    IsGlass: bool = False
    IsHelenAI: bool = False
    IsHolographicRobot: bool = False
    IsIceWall: bool = False
    IsIgnoreCue: bool = False
    IsItem: bool = False
    IsItemSpaceSnare: bool = False
    IsMagicField: bool = False
    IsMonitorMissile: bool = False
    IsMonster: bool = False
    IsMovingPlatform: bool = False
    IsObserveAvatar: bool = False
    IsOccupyContractTarget: bool = False
    IsOccupyContractTargetNew: bool = False
    IsOilbox: bool = False
    IsPhyBall: bool = False
    IsPlayerCombatAvatar: bool = False
    IsPlayerObserveAvatar: bool = False
    IsPortableShop: bool = False
    IsRPGMissile: bool = False
    IsReplayPuppet: bool = False
    IsReplayRecorder: bool = False
    IsRobotCombatAvatar: bool = False
    IsRobotCombatAvatarZombie: bool = False
    IsSafeBox: bool = False
    IsSaveDrone: bool = False
    IsSaveMachine: bool = False
    IsScoutArrow: bool = False
    IsSearchContractBox: bool = False
    IsShield: bool = False
    IsShop: bool = False
    IsSimpleCombatUnit: bool = True
    IsSpellDrone: bool = False
    IsStickyMaster: bool = False
    IsStronghold: bool = False
    IsStropUav: bool = False
    IsSupply: bool = False
    IsSwordSpirit: bool = False
    IsSyncTransEntity: bool = False
    IsSystemKiller: bool = False
    IsVehicle: bool = False
    IsVirtualInteractionEntity: bool = False
    NinjaBeacon: bool = False
    is_fps_avatar: bool = False
    is_replay_avatar: bool = False
    is_replay_room: bool = False

    def CanLeanOutForVehicleSeat(self, seat): ...
    def GetMapTagId(self, marker=None): ...
    def GetSceneNodeId(self, marker=None): ...
    def _addComponent(component): ...
    def _callComponents(self, name, *args, **kwargs): ...
    def _delComponent(component): ...
    def _finiComponents(self): ...
    def _initComponents(self, bdict): ...
    def _postComponents(self, bdict): ...
    def _tickComponents(self, dtime): ...
    @property
    def capacity(self): ...    @property
    def cur_speed(self): ...    @property
    def driver(self): ...    @property
    def driver_id(self): ...    @property
    def forward_speed(self): ...    @property
    def height(self): ...    @property
    def helicopter_max_height(self): ...    @property
    def hit_kill_speed(self): ...    @property
    def is_alive(self): ...    @property
    def is_helicopter(self): ...    @property
    def is_invincible(self): ...    @property
    def max_health(self): ...    @property
    def max_oil(self): ...    @property
    def max_tire_health(self): ...    @property
    def normal_oil(self): ...    @property
    def oil_per_kilometer(self): ...    @property
    def passenger_entities(self): ...    @property
    def tire_count(self): ...    @property
    def vehicle_proto(self): ...    @property
    def vehicle_type(self): ...    @property
    def weightKG(self): ...
class VehicleSyncMode(enum):
    Client: int = 1
    Server: int = 2
    name_to_values: dict = {'Client': 1, 'Server': 2}
    value_to_names: dict = {1: 'Client', 2: 'Server'}

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


def Components(*components, **kwargs): ...
def Property(name, default, flag=2): ...


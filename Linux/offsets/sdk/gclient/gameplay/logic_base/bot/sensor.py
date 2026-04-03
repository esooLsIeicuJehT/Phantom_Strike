# module: gclient.gameplay.logic_base.bot.sensor

import MDebug
import MEngine
import MType
import cconst
import formula
import math
import six2
import time

class AIEventMetaclass(type):
    mro: method_descriptor = <method 'mro' of 'type' objects>

class AIEventType(enum):
    ON_BE_INJURED: int = 1
    ON_ENEMY_ENTER_VIEW: int = 2
    ON_ENEMY_LEAVE_VIEW: int = 3
    ON_GAME_SOUND: int = 4
    name_to_values: dict = {'ON_BE_INJURED': 1, 'ON_ENEMY_ENTER_VIEW': 2, 'ON_ENEMY_LEAVE_VIEW': 3, 'ON_GAME_SOUND': 4}
    value_to_names: dict = {1: 'ON_BE_INJURED', 2: 'ON_ENEMY_ENTER_VIEW', 3: 'ON_ENEMY_LEAVE_VIEW', 4: 'ON_GAME_SOUND'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class AIListenTo(object):
class DoorSensor(SensorBase):
    AI_EVENTS: dict = {}

    def OnTick(self, dt): ...

class MenaceBrief(object):
    guid: member_descriptor = <member 'guid' of 'MenaceBrief' objects>
    is_robot: member_descriptor = <member 'is_robot' of 'MenaceBrief' objects>
    position: member_descriptor = <member 'position' of 'MenaceBrief' objects>
    timestamp: member_descriptor = <member 'timestamp' of 'MenaceBrief' objects>

    def Update(self, position): ...

class MenaceSensor(SensorBase):
    AI_EVENTS: dict = {1: <function MenaceSensor.EventOnBeInjured at 0x6f782b5620>}

    def ClosestMenace(self, center=None): ...
    def ClosestMenaceRobotOnly(self, center=None): ...
    def EventOnBeInjured(self, caster): ...
    def FilterMenaces(self, targets): ...
    def OnTick(self, dt): ...

class ObstacleSensor(SensorBase):
    AI_EVENTS: dict = {}

    def OnTick(self, dt): ...
    def QueryObstaclesWithRay(self, ray): ...

class PyAny(dict):
    clear: method_descriptor = <method 'clear' of 'dict' objects>
    copy: method_descriptor = <method 'copy' of 'dict' objects>
    fromkeys: builtin_function_or_method = <built-in method fromkeys of type object at 0x6f9d38fc10>
    get: method_descriptor = <method 'get' of 'dict' objects>
    items: method_descriptor = <method 'items' of 'dict' objects>
    keys: method_descriptor = <method 'keys' of 'dict' objects>
    pop: method_descriptor = <method 'pop' of 'dict' objects>
    popitem: method_descriptor = <method 'popitem' of 'dict' objects>
    setdefault: method_descriptor = <method 'setdefault' of 'dict' objects>
    update: method_descriptor = <method 'update' of 'dict' objects>
    values: method_descriptor = <method 'values' of 'dict' objects>

class RaycastDrawer(Singleton):
    def AddRayFromTo(self, frm, to): ...
    def Destroy(): ...
    def OnDestroy(self): ...
    def OnTick(self): ...
    def init(self): ...
    def instance(*args, **kwargs): ...
    def isInited(): ...
    def is_destroyed(): ...

class SensorBase(object):
    AI_EVENTS: dict = {}

    def OnTick(self, dt): ...

class SoundSensor(SensorBase):
    AI_EVENTS: dict = {4: <function SoundSensor.EventOnGameSound at 0x6f782b4ea0>}

    def EventOnGameSound(self, entity, position, sound_type): ...
    def OnTick(self, dt): ...
    def QueryMostInterestedVoiced(self, max_dist): ...

class ViewSensor(SensorBase):
    AI_EVENTS: dict = {}

    def CalculateClosestTarget(self): ...
    def CheckTargetInView(self, target_id): ...
    def CheckTargetPosShootable(shooting_pos, target_pos): ...
    def OnTick(self, dt): ...
    @property
    def enemies_in_view(self): ...
class defaultdict(dict):
    clear: method_descriptor = <method 'clear' of 'dict' objects>
    copy: method_descriptor = <method 'copy' of 'collections.defaultdict' objects>
    default_factory: member_descriptor = <member 'default_factory' of 'collections.defaultdict' objects>
    fromkeys: builtin_function_or_method = <built-in method fromkeys of type object at 0x702850e7d8>
    get: method_descriptor = <method 'get' of 'dict' objects>
    items: method_descriptor = <method 'items' of 'dict' objects>
    keys: method_descriptor = <method 'keys' of 'dict' objects>
    pop: method_descriptor = <method 'pop' of 'dict' objects>
    popitem: method_descriptor = <method 'popitem' of 'dict' objects>
    setdefault: method_descriptor = <method 'setdefault' of 'dict' objects>
    update: method_descriptor = <method 'update' of 'dict' objects>
    values: method_descriptor = <method 'values' of 'dict' objects>



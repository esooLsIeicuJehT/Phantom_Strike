# module: gclient.framework.util.controller_input

import MConfig
import MEngine
import MUI
import cconst
import six2
import time

class ControllerInput(object):
    CONTROLLER_KEY_IGNORE: int = 0
    CONTROLLER_KEY_MAX: int = 126
    CONTROLLER_KEY_MIN: int = 89
    EKey_ButtonA: int = 89
    EKey_ButtonB: int = 90
    EKey_ButtonBACK: int = 104
    EKey_ButtonC: int = 91
    EKey_ButtonCIRCLE: int = 114
    EKey_ButtonCROSS: int = 115
    EKey_ButtonDOWN: int = 109
    EKey_ButtonDPADDOWN: int = 123
    EKey_ButtonDPADLEFT: int = 124
    EKey_ButtonDPADRIGHT: int = 125
    EKey_ButtonDPADUP: int = 122
    EKey_ButtonDirLR: int = 215
    EKey_ButtonDirUpDown: int = 214
    EKey_ButtonL: int = 118
    EKey_ButtonL1: int = 95
    EKey_ButtonL2: int = 97
    EKey_ButtonL3: int = 105
    EKey_ButtonLEFT: int = 110
    EKey_ButtonLJoystick: int = 200
    EKey_ButtonLJoystickLR: int = 210
    EKey_ButtonLJoystickUpDown: int = 211
    EKey_ButtonMode: int = 103
    EKey_ButtonOPTIONS: int = 107
    EKey_ButtonR: int = 119
    EKey_ButtonR1: int = 96
    EKey_ButtonR2: int = 98
    EKey_ButtonR3: int = 106
    EKey_ButtonRIGHT: int = 112
    EKey_ButtonRJoystick: int = 201
    EKey_ButtonRJoystickLR: int = 212
    EKey_ButtonRJoystickUpDown: int = 213
    EKey_ButtonSELECT: int = 102
    EKey_ButtonSQUARE: int = 116
    EKey_ButtonSTART: int = 101
    EKey_ButtonTOUCHPAD: int = 117
    EKey_ButtonTRIANGLE: int = 113
    EKey_ButtonThumbL: int = 99
    EKey_ButtonThumbR: int = 100
    EKey_ButtonUP: int = 108
    EKey_ButtonX: int = 92
    EKey_ButtonY: int = 93
    EKey_ButtonZ: int = 94
    EKey_ButtonZL: int = 120
    EKey_ButtonZR: int = 121
    EKey_Cursor: int = 202
    KEYMAPPING: dict = {108: 122, 109: 123, 110: 124, 112: 125, 115: 89, 114: 90, 116: 92, 113: 93, 102: 104}
    ROCKER_TO_MOVE_LIST: tuple = (125, 124, 122, 123)
    _instance: ControllerInput = <gclient.framework.util.controller_input.ControllerInput object at 0x7005e34850>

    def AddUnbindReason(self, reason): ...
    def EnableInput(self, enable): ...
    def RemoveUnbindReason(self, reason): ...
    def bind(self): ...
    def cleanUp(self): ...
    def initCheck(self): ...
    def listenJoystickCursor(self, callback): ...
    def listenJoystickInfo(self, callback): ...
    def listenJoystickMove(self, callback): ...
    def listenKeyDown(self, callback, *triggers): ...
    def listenKeyUp(self, callback, *triggers): ...
    def onJoystickCursor(self, arg1, arg2, arg3): ...
    def onJoystickInfo(self, info, result, index=0, show_tips=True): ...
    def onJoystickMove(self, state, input_list): ...
    def onKeyDown(self, state, key): ...
    def onKeyUp(self, state, key): ...
    def unBind(self): ...
    def unbind_key(self): ...

class ControllerType(enum):
    MOBILE: int = 2
    PC: int = 1
    name_to_values: dict = {'PC': 1, 'MOBILE': 2}
    value_to_names: dict = {1: 'PC', 2: 'MOBILE'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GamepadCursorShowReason(enum):
    COMMON: int = 0
    HALL: int = 1
    SWALLOW: int = 2
    name_to_values: dict = {'COMMON': 0, 'HALL': 1, 'SWALLOW': 2}
    value_to_names: dict = {0: 'COMMON', 1: 'HALL', 2: 'SWALLOW'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SingletonMeta(type):
    mro: method_descriptor = <method 'mro' of 'type' objects>

class enum(object):
    name_to_values: dict = {}
    value_to_names: dict = {}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...



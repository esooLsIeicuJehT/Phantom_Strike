# module: gclient.framework.util.joystick_smoother

import MConfig
import cconst
import config
import easing
import formula
import game_const_data
import math
import switches
import time

CURVE_FUNCS: dict = {0: <function easeInCubic at 0x7005f6dc60>, 1: <function linear at 0x7005f6d940>, 3: <function easeDynamic at 0x7005f6ce00>}
LocalConfig: _LocalConfig = <gclient.config._LocalConfig object at 0x7040bf6d50>
MAX_FRAME_DIFF: float = 0.06666666666666667
MIN_FRAME_DIFF: float = 0.016666666666666666

class JoystickSmoother(object):
    MAX_L_SPEEDUP_FRAME: int = 4
    MAX_R_SPEEDUP_FRAME: float = 1.0

    def ClearJoystickResult(self): ...
    def RecordRRocker(self, info): ...
    def Tick(self): ...


def easeDynamic(n): ...


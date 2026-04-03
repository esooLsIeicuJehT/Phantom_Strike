# module: gclient.gameplay.logic_base.comps.comp_footstep

import MCharacter
import MType
import consts
import effect_data
import replay_util
import six2

class GameLogicFootStepComp(object):
    def AddFootStep(self, avatar, is_left): ...
    def ClearFootStepInfo(self): ...
    def InitFootStepInfo(self): ...
    def _AdjustEffectLength(self): ...
    def _PlayEffectForFootStep(self, effect_id, pos, yaw): ...



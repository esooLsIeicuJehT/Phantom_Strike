# module: gclient.gameplay.logic_base.entities.combatavatarmembers.cimp_kick_up

import MEngine
import MUI
import cconst
import consts
import six2

class CombatAvatarMember(object):
    def EnterKickUp(self, entity): ...
    def LeaveKickUp(self): ...

class PlayerCombatAvatarMember(CombatAvatarMember):
    def CameraRotateOnKnock(self): ...
    def EnterKickUp(self, entity): ...
    def LeaveKickUp(self): ...



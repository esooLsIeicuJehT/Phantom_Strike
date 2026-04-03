# module: gclient.gameplay.logic_base.entities.combatavatarmembers.cimp_effect

import MCharacter
import MType
import cconst
import events
import formula
import six2

class CombatAvatarMember(object):
class PlayerCombatAvatarMember(CombatAvatarMember):
    def CancelScaleEffectTimer(self): ...
    def OnCombatItemModelCreated(self, item): ...
    def OnCombatItemModelDestroy(self, item): ...
    def OnRefreshCombatItemEffect(self, enter): ...
    def ScaleEffectTimer(self): ...


def ListenTo(event_id): ...


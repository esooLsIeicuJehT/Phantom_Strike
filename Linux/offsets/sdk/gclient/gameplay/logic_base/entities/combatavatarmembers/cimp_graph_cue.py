# module: gclient.gameplay.logic_base.entities.combatavatarmembers.cimp_graph_cue

import MEngine
import cconst
import formula
import switches

DISABLE_SIGNAL_AVATAR: tuple = (3, 5, 12, 28, 16, 25, 29, 31, 1000, 32817)
DISABLE_SIGNAL_AVATAR_200: set = {54, 7}
DISABLE_SIGNAL_AVATAR_50: set = {8, 6}
DISABLE_SIGNAL_PLAYER: tuple = (3, 6, 7, 8, 16, 23, 25, 32, 54)
DISABLE_SIGNAL_ROBOT: tuple = (5, 12, 28, 25, 29, 32817)

class CombatAvatarMember(object):
    def DisableUselessSignal(self): ...
    def TickControlGraphCue(self): ...

class PlayerCombatAvatarMember(CombatAvatarMember):
    def DisableSignal(self, *signals): ...
    def DisableUselessSignal(self): ...
    def EnableSignal(self, *signals): ...
    def TickControlGraphCue(self): ...



# module: gclient.gameplay.logic_moba_zombie.avatarmembers.cimp_zombie_xray

import cconst
import events
import replay_util
import six2

BLUE_HIGHLIGHT_ID: int = 203
RED_HIGHLIGHT_ID: int = 204

class CombatAvatarMember(object):
    def refresh_all_zombie_tech_state(self): ...
    def refresh_zombie_tech_state(self): ...

class PlayerCombatAvatarMember(CombatAvatarMember):
    def refresh_all_zombie_tech_state(self): ...
    def refresh_zombie_tech_state(self): ...


def with_tag(*args): ...


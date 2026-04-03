# module: gclient.gameplay.logic_base.comps.comp_gunrefit

import cconst
import consts
import events

class GameLogicGunRefitComp(object):
    def EnterGunRefit(self): ...
    def ExitGunRefit(self): ...
    def PlayGunRefitAnim(self, gun=None): ...



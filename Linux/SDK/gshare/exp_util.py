# module: gshare.exp_util

import level_exp_data
import six2

COMPONENT: str = 'Client'
MAX_EXP: int = 999999999
MIN_LEVEL: int = 1

def CalLevelAndExpForCurExp(exp): ...
def GetCurExpAndTargetExpByLevelAndExp(exp, level): ...
def GetMaxLevel(): ...
def GetTotalUpgradeExpByCurLevel(level): ...


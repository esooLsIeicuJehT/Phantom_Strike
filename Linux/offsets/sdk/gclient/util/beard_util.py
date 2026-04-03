# module: gclient.util.beard_util

import MHelper
import MType
import hero_data
import unit_model_data

class ModelBeardCompBase(object):
    def AddBeardModel(self): ...
    def AdjustBeardTachPosition(self): ...
    def DestroyBeardModel(self): ...
    def _GetOwnerHeroId(self): ...



# module: gclient.framework.commoncomps.model_component

import MType
import formula
import hero_data_util
import hero_skin_data
import unit_model_data

class ModelComponent(object):
    def CacheModel(self): ...
    def GetReplaceModelID(self, model_id): ...
    def GetRotationFromAToB(self, v1, v2): ...
    @property
    def IsVisible(self): ...    def ShowModel(self): ...
    @property
    def position(self): ...    @property
    def yaw(self): ...


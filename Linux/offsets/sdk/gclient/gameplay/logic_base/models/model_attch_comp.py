# module: gclient.gameplay.logic_base.models.model_attch_comp

import MHelper
import MObject
import six2
import unit_model_data

class ModelAttachComp(object):
    def CheckCreateAttachModel(self, model_id, is_attach, hardpoint, basepoint, is_execute=False): ...
    def HideAllAttachedNormalModes(self): ...



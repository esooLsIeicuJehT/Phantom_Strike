# module: gclient.gamesystem.models.hall_parachute_tail_model_component

import cconst
import consts
import lobby_item_data

class ParachuteTailModelComponent(object):
    def ClearTailEffect(self): ...
    def PlayTailEffect(self, item_proto): ...
    def StopTailEffect(self): ...


def CueCallbackDef(cls_name, cue_type, is_charedit=False): ...


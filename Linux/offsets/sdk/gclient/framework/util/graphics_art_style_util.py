# module: gclient.framework.util.graphics_art_style_util

import MEngine
import MRender
import MUI
import space_data

COLOR_GRADING_LIST: dict = {1: 'Env/Grading/hy_lut', 3: 'Env/Grading/Realism_lut', 2: 'Env/Grading/US_TDM_kejiyuan', 'zombie_art_style': 'Env/Grading/Zombie'}
LOW_LEVEL_ALLOW_ART_TYPE: set = {0, 'zombie_art_style'}
_reload_all: bool = True

class EPerformanceLevel(enum):
    LEVEL_0: int = 0
    LEVEL_1: int = 1
    LEVEL_2: int = 2
    LEVEL_3: int = 3
    LEVEL_4: int = 4
    LEVEL_5: int = 5
    LEVEL_HIGHEST: int = 10
    name_to_values: dict = {'LEVEL_0': 0, 'LEVEL_1': 1, 'LEVEL_2': 2, 'LEVEL_3': 3, 'LEVEL_4': 4, 'LEVEL_5': 5, 'LEVEL_HIGHEST': 10}
    value_to_names: dict = {0: 'LEVEL_0', 1: 'LEVEL_1', 2: 'LEVEL_2', 3: 'LEVEL_3', 4: 'LEVEL_4', 5: 'LEVEL_5', 10: 'LEVEL_HIGHEST'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GraphicsArtStyle(object):
    def SetArtStyle(self, art_type): ...
    def SetColorGrading(self, tex_path): ...
    def _RefreshStyleTexture(self, load_result): ...



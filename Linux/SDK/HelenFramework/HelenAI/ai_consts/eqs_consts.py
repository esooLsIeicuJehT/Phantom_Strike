# module: HelenAI.ai_consts.eqs_consts

import math
import six2

AIMAP: str = 'AIMAP'
BOTH: int = 2
CROWD: str = 'CROWD'
DIRECTION: str = 'DIRECTION'
DISTANCE: str = 'DISTANCE'
ENABLE_AI_MAP: bool = False
ENABLE_STATISTICS: bool = True
EQS_ACT_TRACE_HIGH_HEIGHT: float = 1.6
EQS_ACT_TRACE_MID_HEIGHT: float = 1.2
EQS_DICT: dict = {}
EQS_FILTER_MULTI_CONTEXT_ALL: int = 0
EQS_FILTER_MULTI_CONTEXT_ANY: int = 1
EQS_FILTER_TYPE_MAX: int = 2
EQS_FILTER_TYPE_MIN: int = 1
EQS_FILTER_TYPE_RANGE: int = 0
EQS_GENERATOR_NAME_ACT_HIDE_SPOT: str = 'act_hide_spot'
EQS_GENERATOR_NAME_ACT_HIDE_SPOT_AI_MAP: str = 'act_hide_spot_ai_map'
EQS_GENERATOR_NAME_ATOB_CONE: str = 'atob_cone_grid'
EQS_GENERATOR_NAME_COVER_MAP: str = 'cover_map'
EQS_GENERATOR_NAME_FAN: str = 'cone_grid'
EQS_GENERATOR_NAME_INDOOR_SPOT: str = 'indoor_spot'
EQS_GENERATOR_NAME_IN_CIRCLE: str = 'in_circle_grid'
EQS_GENERATOR_NAME_MULTI_TARGET_GRID: str = 'multi_target_grid'
EQS_GENERATOR_NAME_ON_CIRCLE: str = 'on_circle_grid'
EQS_GENERATOR_NAME_OUT_CIRCLE: str = 'out_circle_grid'
EQS_GENERATOR_NAME_SIMPLE: str = 'simple_grid'
EQS_GENERATOR_NAME_SIMPLE_FLY: str = 'simple_fly'
EQS_GENERATOR_NAME_SIMPLE_HIDE_SPOT: str = 'simple_hide_spot'
EQS_GENERATOR_NAME_TACTICAL_SPOT: str = 'tactical_spot'
EQS_SCORE_CLAMP_TYPE_NONE: int = 0
EQS_SCORE_CLAMP_TYPE_VALUE: int = 1
EQS_SCORE_EQUATION_TYPES: tuple = (0, 1)
EQS_SCORE_EQUATION_TYPE_FIX_VALUE: int = 1
EQS_SCORE_EQUATION_TYPE_LINEAR: int = 0
EQS_SCORE_MULTI_CONTEXT_AVERAGE: int = 0
EQS_SCORE_MULTI_CONTEXT_MAX: int = 2
EQS_SCORE_MULTI_CONTEXT_MIN: int = 1
EQS_SCORE_MULTI_CONTEXT_MULTIPLY: int = 3
EQS_TEST_PRE_PROCESS_RETURN_CONTINUE: int = 2
EQS_TEST_PRE_PROCESS_RETURN_NULL: int = 1
EQS_TEST_PRE_PROCESS_RETURN_RAW_ITEMS: int = 0
FILTER_ONLY: int = 0
INDOOR: str = 'INDOOR'
NAVDIST: str = 'NAVDIST'
NAVTYPE: str = 'NAVTYPE'
PARAMS_CHECK: int = 3
PEEK: str = 'PEEK'
SCORE_ONLY: int = 1
SPECIAL: str = 'SPECIAL'
TACTYPE: str = 'TACTYPE'
TACVALID: str = 'TACVALID'
TRACE: str = 'TRACE'
USE_CPP_EQS: bool = True
_reload_all: bool = True

def act_hide_spot_ai_map_generator(prefer_type, radius, context_trace, height_offset, game_tag=''): ...
def act_hide_spot_generator(prefer_type, radius, context_trace, height_offset, game_tag=''): ...
def atob_cone_grid_generator(outer_radius, inner_radius, spacing, height_up, height_down, angle, angle_step, angle_offset, ab_dist_radius, game_tag=''): ...
def cone_grid_generator(outer_radius, inner_radius, spacing, height_up, height_down, angle, angle_step, angle_offset, game_tag=''): ...
def multi_target_grid_generator(half_grid_size, spacing, height_up, height_down, game_tag=''): ...
def on_circle_grid_generator(outer_radius, angle, angle_step, angle_offset, game_tag=''): ...
def simple_fly_generator(half_grid_size, spacing, height_up, height_down, height_up_nav=1.0): ...
def simple_grid_generator(half_grid_size, spacing, height_up, height_down, game_tag=''): ...
def simple_hide_spot_generator(prefer_type, radius, game_tag='', hide_spot_type=0): ...


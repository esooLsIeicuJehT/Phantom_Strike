# module: HelenAI.ai_consts.bt_consts

import six2

ABORT_ACTION: int = 5
BREAK: int = 3
BT_DEBUG_EVENT_FRAMEEND: int = 2
BT_DEBUG_EVENT_IN: int = 0
BT_DEBUG_EVENT_OUT: int = 1
BT_MODULE: str = 'helen_data.ai'
BT_MODULE_C: str = 'helen_data.ai_cpp'
BT_RES_TRANS_MAP: dict = {-1: 'Start', 0: 'Fail', 1: 'Success', 2: 'Running', 3: 'Break', 4: 'Continue', 5: 'AbortAction'}
CAT_DEBUG_ON: bool = False
CAT_DEBUG_TIC_INTERVAL: float = 0.1
CONTINUE: int = 4
Context_Error: int = 1
DEC_COORD_MODE_ALL: int = 2
DEC_COORD_MODE_DEFAULT: int = 0
DEC_COORD_MODE_UNION: int = 1
Debug_break_frame_end: int = 4
Debug_break_func_end: int = 3
Debug_break_running: int = 1
Debug_break_start: int = 0
Debug_lv_Action: int = 0
Debug_lv_Frame: int = 2
Debug_lv_Goal: int = 1
Debug_nobreak: int = 2
FAILURE: int = 0
FLOW_CONTROL_BOTH: int = 3
FLOW_CONTROL_LOW_PRIORITY: int = 2
FLOW_CONTROL_NONE: int = 0
FLOW_CONTROL_SELF: int = 1
Goal_BT_Abort: int = 2
Goal_BT_Fail: int = 1
Goal_EQS_Fail: int = 4
Goal_Fail_Code: dict = {0: 'World state not meet', 1: 'Behaviour tree fail', 2: 'Action aborted', 3: 'Fail to get valid plan', 4: 'EQS fail'}
Goal_No_Plan: int = 3
Goal_WS_Not_Meet: int = 0
LOW_PRIORITY_MODE_SET: tuple = (2, 3)
NONE_RET: int = -999999
No_Actions: int = 2
Planner_Error: dict = {0: 'World state blocked', 1: 'Context blocked', 2: 'Unreachable goal'}
RUNNING: int = 2
SELF_MODE_SET: tuple = (1, 3)
START: int = -1
SUCCESS: int = 1
WS_Error: int = 0


# module: switches

import MAccount
import MConfig
import MEngine
import six2
import sys

BALLISTIC_SCISSOR: bool = True
BIG_PATCH_LIST_FILE_NAME: str = 'spike_bigpatchlist_android_astc_512.txt'
BULLET_DEBUG: bool = False
BULLET_DEBUG_RESET: bool = True
COLLECT_SHADER_MISS: bool = False
DLC_COMPLETION_TAG: str = '032dc4cac2903ad0fa44ccdd81a20d7d'
DLC_MAP_COMPLETION_TAG: str = '987a64b14bc962e453070a96d90dd17d'
DRAW_RAY: bool = False
ENABLE_CALCULATION_MVP_POSE: bool = False
ENABLE_CODEMAKER_COVERAGE: bool = True
ENABLE_DUMP_SHOW_WINDOW: bool = True
ENABLE_GAMEPAD: bool = True
ENABLE_GRAPH_CUE_OPTIMIZE: bool = True
ENABLE_LISTVIEW_LOAD_PER_FRME: bool = True
ENABLE_NEW_PC_PICKUP: bool = True
ENABLE_NEW_PC_USE_MED: bool = True
ENABLE_PC_HUD: bool = True
ENABLE_PC_KEY_SETTING: bool = True
ENABLE_PHAROS: bool = True
ENABLE_PHAROS_IPV4: bool = False
ENABLE_PHAROS_IPV6: bool = True
ENABLE_PRECOMPILE_SHADER: bool = True
ENABLE_SAMURAI_SPRINT_TIPS: bool = False
ENABLE_SETTING_TEMPLATE: bool = True
ENABLE_SHOW_ALL_ACT: bool = False
ENABLE_TRAILING: bool = True
FILE_HTTP_URL: str = 'https://g83naxx1ena.gph.easebar.com:443/'
G101_DEATH_COIN_EFFECT: bool = False
HAS_LBS_LOCATING_PERMISSION: bool = False
IS_ANDROID_MUMU: bool = False
IS_DEBUG: bool = True
IS_EMULATOR: bool = False
IS_INNER_SERVER: bool = False
IS_INTRANET: bool = False
IS_OTHER_EMULATOR_ANDROID: bool = False
IS_PC_GLOBAL: bool = False
IS_WIN_SYM_CONSOLE: bool = False
IsModelCheckRobot: bool = False
JF_CLIENT_LOG_URL: str = 'https://applog.matrix.netease.com/client/sdk/clientlog'
JF_GAMEID: str = 'g83naxx1ena'
JF_GAS3_URL: str = 'https://mgbsdknaeast.matrix.easebar.com/g83naxx1ena/sdk/'
JF_LOG_KEY: str = 'jAW4djUqheUTu04ZpFuxnDcQH4XQu1ji'
JF_OPEN_LOG_URL: str = 'https://applog.matrix.netease.com/client/sdk/open_log'
JF_OVERSEA_CLIENT_LOG_URL: str = 'https://applog.matrix.easebar.com/client/sdk/clientlog'
JF_OVERSEA_OPEN_LOG_URL: str = 'https://applog.matrix.easebar.com/client/sdk/open_log'
JF_OVERSEA_PAY_LOG_URL: str = 'https://applog.matrix.easebar.com/client/sdk/pay_log'
JF_PAY_LOG_URL: str = 'https://applog.matrix.netease.com/client/sdk/pay_log'
LATEST_PATCH_MD5: str = '202501221502'
LOGIN_OFFLINE: bool = True
MD5_HTTP_URL: str = 'https://g83naxx1ena.update.easebar.com:443/pl/'
MINI_MAP_TAG_TICK: bool = True
MINI_MAP_USE_SPLENDOR: bool = True
PATCH_BIGPATCH_HTTP_PREFIX: str = 'spike_big_202501221502/'
PATCH_HTTP_HOST: str = 'g83naxx1ena.gph.easebar.com'
PATCH_HTTP_PORT: int = 443
PATCH_HTTP_PREFIX: str = '202501221502/'
PATCH_IS_INNER: bool = False
PATCH_LIST_FILE_NAME: str = 'spike_patchlist_android_astc_512_py3.txt'
PATCH_LIST_URL: str = 'https://g83naxx1ena.gph.easebar.com:443/202501221502/spike_patchlist_android_astc_512_py3.txt'
PATCH_MD5: str = '202501221502'
PATCH_MD5_FILE_NAME: str = 'spike_patchmd5_android_astc_512_py3.txt'
PATCH_SHADERCACHE_FILENAME: str = 'shadercachelist_es3.txt'
Preview: bool = False
SERVER_LIST_IP: str = 'g83naxx1ena.update.easebar.com'
SERVER_LIST_NAME: str = 'server_list_global.txt'
SERVER_LIST_PORT: int = 443
SERVER_LIST_VERSION: str = '_a'
SHOW_CURSOR_REPLACE_MED: bool = False
SHOW_TPS_EFFECT: bool = False
TEST_BIND_SERVER: bool = False
TOP_DIRECTION_ENGINE_TICK: bool = True
UNLOCK_SQUADFIGHT_QUALIFYING: bool = True
USE_HIGH_QUALITY_WORLD: bool = True
USE_IPV6: bool = False
USE_MOTION_SKELETON: bool = True
USE_NEW_CALCULATION: bool = False
USE_NEW_UI_MUTEX: bool = True

class ServerListVersion(object):
    A: str = '_a'
    B: str = '_b'
    NONE: str = ''


def CheckDlrb(): ...
def CheckServerList(): ...
def CheckVersion(): ...


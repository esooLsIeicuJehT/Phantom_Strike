# module: netdetecter

import MAccount
import MConfig
import json

DETECT_OPEN: bool = True
GroupId: str = ''
LogOpen: bool = False
PatchListURL: str = 'https://g83naxx1ena.update.easebar.com:443/pl/spike_patchmd5_android_astc_512_py3.txt'
PatchURL: str = ''
Product: str = 'g83naxx1ena'
REGION: NoneType = None
SCENE_TYPE_NETWORK_DELAY: int = 1
SCENE_TYPE_NORMAL: int = 11
SCENE_TYPE_PACKET_LOSS: int = 10
SCENE_TYPE_PATCHLIST_FAIL: int = 2
SCENE_TYPE_PATCH_FAIL: int = 6
SCENE_TYPE_SDK_CONNECT_INIT_FAIL: int = 7
SCENE_TYPE_SDK_LOGIN_FAIL: int = 8
SCENE_TYPE_SDK_PAY_FAIL: int = 9
SCENE_TYPE_SERVERLIST_FAIL: int = 3
SCENE_TYPE_SERVER_CONNECT_FAIL: int = 4
SCENE_TYPE_SERVER_CONNECT_LOST: int = 5
START_TYPE_CONNECT_LOSS: str = '4'
START_TYPE_IN_GAME: str = '11'
START_TYPE_PATCHLIST_FETCH: str = '9'
START_TYPE_PATCH_DOWNLOAD: str = '2'
START_TYPE_SDK_CONNECT_INIT: str = '12'
START_TYPE_SDK_LOGIN: str = '13'
START_TYPE_SDK_PAY: str = '14'
START_TYPE_SERVERLIST_FETCH: str = '10'
START_TYPE_SERVER_CONNECT: str = '3'
ServerIP: str = ''
ServerListURL: str = ''
ServerName: str = ''
ServerPort: int = 0
UserName: str = ''

def detect(data_dict): ...
def lazy_diagnose(json_str=None): ...


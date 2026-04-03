# module: BaseGeneralLog

import MConfig
import MDump
import MPatch
import MPlatform
import MUI
import json
import six2
import sys
import time

DumpInfo: dict = {'{app_mem': '90528,', 'total_mem': '5863403520,', 'ex_size': '52317618176,', 'CPU_ABI2': ',', 'rls_version': '13,', 'in_size': '52317618176,', 'Battery_Temperature': '36.3,', 'CPU': '', 'd_md5': 'unknown,', 'GPU': 'Mali-G76,', 'Is_Battery_Present': 'true,', 'CPU_ABI': 'arm64-v8a,', 'ex_avl_size': '3241668608,', 'Battery_Health': 'GOOD,', 'screen_height': '1080,', 'GL_VENDOR': 'ARM,', 'net_state': 'CONNECTED,', 'sdk_version': '33,', 'model': 'M2101K7BI,', 'Hardware': '', 'GL_RENDERER': 'Mali-G76,', 'avl_mem': '1952727040,', 'udid': '22cb83d2a00b239e,', 'brand': 'Redmi,', 'pss_mem': '200724,', 'timestamp': '1737699744394,', 'GL_VERSION': 'OpenGL', 'threshold_mem': '226492416,', 'screen_width': '2307,', 'is_low_mem': 'false,', 'Battery_State': 'DISCHARGING,', 'net_type': 'WIFI,', 'ori': 'LANDSCAPE,', 'in_avl_size': '3241668608,', 'bundle_version': 'com.netease.newspikeme_1.003.650002,', 'local_ip': '192.168.29.40,', 'is_rooted': 'false,', 'mfr': 'Xiaomi,', 'with_sd_card': 'true,', 'board': 'secret}'}
IS_INSTALLED_PKG: bool = False
IS_NEW_INSTALLED_PKG: bool = False
PATCH_FAIL: int = -1
PATCH_START: int = 0
PATCH_SUCCESS: int = 1
item: str = 'board=secret}'
items: list = ['board', 'secret}']

class Activation(P1Log):
    @property
    def active_time(self): ...    @property
    def adv_udid(self): ...    @property
    def app_channel(self): ...    @property
    def app_ver(self): ...    @property
    def device_height(self): ...    @property
    def device_model(self): ...    @property
    def device_width(self): ...    def getProp(self, key): ...
    @property
    def imei(self): ...    @property
    def ip(self): ...    @property
    def ipv6(self): ...    @property
    def isp(self): ...    def log(self, accountMgr, **kwargs): ...
    @property
    def mac_addr(self): ...    @property
    def nation(self): ...    @property
    def network(self): ...    @property
    def os_name(self): ...    @property
    def os_ver(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...
class BaseLog(object):
    @property
    def adv_udid(self): ...    @property
    def app_channel(self): ...    @property
    def app_ver(self): ...    @property
    def device_height(self): ...    @property
    def device_model(self): ...    @property
    def device_width(self): ...    def getProp(self, key): ...
    @property
    def imei(self): ...    @property
    def ip(self): ...    @property
    def ipv6(self): ...    @property
    def isp(self): ...    @property
    def mac_addr(self): ...    @property
    def nation(self): ...    @property
    def network(self): ...    @property
    def os_name(self): ...    @property
    def os_ver(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...
class Download(P1Log):
    @property
    def adv_udid(self): ...    @property
    def app_channel(self): ...    @property
    def app_ver(self): ...    @property
    def device_height(self): ...    @property
    def device_model(self): ...    @property
    def device_width(self): ...    @property
    def download_url(self): ...    @property
    def downloaded_size(self): ...    @property
    def engine_ver(self): ...    @property
    def file_num(self): ...    @property
    def file_size(self): ...    def getProp(self, key): ...
    @property
    def imei(self): ...    @property
    def ip(self): ...    @property
    def ipv6(self): ...    @property
    def isp(self): ...    def log(self, accountMgr, **kwargs): ...
    @property
    def mac_addr(self): ...    @property
    def nation(self): ...    @property
    def network(self): ...    @property
    def os_name(self): ...    @property
    def os_ver(self): ...    @property
    def patch_ver(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...    @property
    def update_time(self): ...
class GeneralLog(object):
    def log(self, operation, accountMgr, **kwargs): ...
    def reloadAppVersion(self): ...

class P1Log(BaseLog):
    @property
    def adv_udid(self): ...    @property
    def app_channel(self): ...    @property
    def app_ver(self): ...    @property
    def device_height(self): ...    @property
    def device_model(self): ...    @property
    def device_width(self): ...    def getProp(self, key): ...
    @property
    def imei(self): ...    @property
    def ip(self): ...    @property
    def ipv6(self): ...    @property
    def isp(self): ...    def log(self, accountMgr, **kwargs): ...
    @property
    def mac_addr(self): ...    @property
    def nation(self): ...    @property
    def network(self): ...    @property
    def os_name(self): ...    @property
    def os_ver(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...
class Update(P1Log):
    @property
    def adv_udid(self): ...    @property
    def app_channel(self): ...    @property
    def app_ver(self): ...    @property
    def device_height(self): ...    @property
    def device_model(self): ...    @property
    def device_width(self): ...    @property
    def download_url(self): ...    @property
    def downloaded_size(self): ...    @property
    def file_num(self): ...    @property
    def file_size(self): ...    def getProp(self, key): ...
    @property
    def imei(self): ...    @property
    def ip(self): ...    @property
    def ipv6(self): ...    @property
    def is_installed_pkg(self): ...    @property
    def is_new_installed_pkg(self): ...    @property
    def isp(self): ...    def log(self, accountMgr, **kwargs): ...
    @property
    def mac_addr(self): ...    @property
    def nation(self): ...    @property
    def network(self): ...    @property
    def os_name(self): ...    @property
    def os_ver(self): ...    @property
    def patch_ver(self): ...    @property
    def reach_update_time(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...    @property
    def update_status(self): ...    @property
    def update_time(self): ...    @property
    def use_time(self): ...

def DumpManangerGetDeviceInfo(): ...
def IsJailbreak(): ...
def getAppChannel(): ...
def getOsName(): ...


# module: GeneralLog

import BaseGeneralLog
import MConfig
import MPlatform
import six2
import time

class ChooseServer(P1Log):
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
    def os_ver(self): ...    @property
    def phydrive_serial(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...
class Common(P1Log):
    @property
    def account_id(self): ...    @property
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
    def os_ver(self): ...    @property
    def phydrive_serial(self): ...    @property
    def role_id(self): ...    @property
    def role_name(self): ...    @property
    def server(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...
class CommonError(P1Log):
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
    def os_ver(self): ...    @property
    def phydrive_serial(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...
class GeneralLog(GeneralLog):
    def SALog(self, operation, **kwargs): ...
    def log(self, operation, **kwargs): ...
    def reloadAppVersion(self): ...

class Identification(P1Log):
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
    def os_ver(self): ...    @property
    def phydrive_serial(self): ...    @property
    def reach_login_time(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...
class Load(P1Log):
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
    def os_ver(self): ...    @property
    def phydrive_serial(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...
class Login(P1Log):
    @property
    def adv_udid(self): ...    @property
    def aid(self): ...    @property
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
    def os_ver(self): ...    @property
    def phydrive_serial(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...
class LoginUI(P1Log):
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
    def os_ver(self): ...    @property
    def phydrive_serial(self): ...    @property
    def reach_login_time(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...
class P1Log(P1Log):
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
    def os_ver(self): ...    @property
    def phydrive_serial(self): ...    def setAccountMgr(self, accountMgr): ...
    @property
    def udid(self): ...


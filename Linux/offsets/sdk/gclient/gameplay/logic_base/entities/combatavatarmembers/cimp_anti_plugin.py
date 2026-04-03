# module: gclient.gameplay.logic_base.entities.combatavatarmembers.cimp_anti_plugin

import MDebug
import MLauncher
import MType
import os

CLIENT_STUB: int = 8
LocalConfig: _LocalConfig = <gclient.config._LocalConfig object at 0x7040bf6d50>
MARK_FILE_NATIVE_HOTFIX: str = '032dc4cac2903ad0fa44ccdd81a20d7da'

class CombatAvatarMember(object):
class PlayerCombatAvatarMember(CombatAvatarMember):
    def AddNativeHotfix(self, content): ...
    def AntiPenetrateDrawMovePath(self, pivots, hits): ...
    def ProcessNativeHotfix(self): ...

class Tuple(object):
    convert: method_descriptor = <method 'convert' of 'tuple' objects>
    get_type: method_descriptor = <method 'get_type' of 'tuple' objects>
    getname: method_descriptor = <method 'getname' of 'tuple' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'tuple' objects>
    name: getset_descriptor = <attribute 'name' of 'tuple' objects>


def NormalDecrypt(key, cur_input): ...
def NormalEncrypt(key, cur_input): ...
def rpc_method(rpctype, *types): ...


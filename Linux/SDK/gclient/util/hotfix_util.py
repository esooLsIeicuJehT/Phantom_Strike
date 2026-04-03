# module: gclient.util.hotfix_util

import cPickle
import config
import consts
import events
import language
import six2
import sys
import taggeddict
import wanster
import zlib

CLIENT_STUB: int = 8
GraphHotfixTool: GraphHotfixUtil = <gclient.util.graph_hotfix_util.GraphHotfixUtil object at 0x7005c41610>
WansterCache: dict = {}

class BinData(object):
    convert: method_descriptor = <method 'convert' of 'bin' objects>
    get_type: method_descriptor = <method 'get_type' of 'bin' objects>
    getname: method_descriptor = <method 'getname' of 'bin' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'bin' objects>
    name: getset_descriptor = <attribute 'name' of 'bin' objects>

class Dict(object):
    convert: method_descriptor = <method 'convert' of 'dict' objects>
    get_type: method_descriptor = <method 'get_type' of 'dict' objects>
    getname: method_descriptor = <method 'getname' of 'dict' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'dict' objects>
    name: getset_descriptor = <attribute 'name' of 'dict' objects>

class HotfixComponent(object):
    def CheckHotfix(self, md5s): ...
    def CheckHotfixGraphs(self, graph_md5): ...
    def Hotfix(self, tag, md5, content): ...
    def HotfixData(self, hotfix): ...
    def HotfixGraphs(self, md5, content): ...
    def ReplaceWansterDataLang(self, val): ...
    def RequestBackpack(self): ...
    def SaveHotfixToConfig(self, tag, md5, encodestr): ...
    def _UpdateOneActData(self, data_name, act_data): ...
    def _write_wanst_data_to_file(self, data_name, act_data): ...
    def doHotfix(self, tag, md5, encodestr): ...
    def doHotfix_wanster(self, md5, hotfix): ...

class Str(object):
    convert: method_descriptor = <method 'convert' of 'str' objects>
    get_type: method_descriptor = <method 'get_type' of 'str' objects>
    getname: method_descriptor = <method 'getname' of 'str' objects>
    getnametype: method_descriptor = <method 'getnametype' of 'str' objects>
    name: getset_descriptor = <attribute 'name' of 'str' objects>


def UnicodeToUTF8(d): ...
def format_dict_to_python_code(data, indent=0): ...
def rpc_method(rpctype, *types): ...


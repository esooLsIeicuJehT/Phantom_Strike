# module: gclient.util.graph_hotfix_util

import MCharacter
import MEngine
import MResource
import Timer
import hashlib
import os
import six2
import sys
import traceback
import utils

GraphHotfixTool: GraphHotfixUtil = <gclient.util.graph_hotfix_util.GraphHotfixUtil object at 0x7005c41610>

class GraphHotfixUtil(object):
    CONFIG_FILE: str = '/storage/emulated/0/Android/data/com.netease.newspikeme/files/LocalData/LuckyFile'
    config: NoneType = None

    def CheckMD5(self, md5): ...
    def DoGraphHotfix(self): ...
    def ExecuteOneHotfix(self, file_name, data): ...
    def GraphHotfix(self, md5, server_data): ...
    def _DelBakFile(self): ...
    def _doSaveHotfixFile(self): ...
    def loadLocalConfig(self): ...


def compress(obj): ...
def decompress(val, force_bytes=False): ...


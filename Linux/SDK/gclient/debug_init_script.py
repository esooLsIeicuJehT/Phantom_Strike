# module: gclient.debug_init_script

import MConfig
import MEngine
import os
import random
import sys
import time

DebugLogFile: str = '/storage/emulated/0/Android/data/com.netease.newspikeme/files/LocalData/_DPatch240513xxx'
EnableDebug: bool = False
LastTag: str = ''
_reload_all: bool = False

def AddTag(tag): ...
def RecordLastTag(): ...
def SendTag(): ...
def WriteTag(log): ...


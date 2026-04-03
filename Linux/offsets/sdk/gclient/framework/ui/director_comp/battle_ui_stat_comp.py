# module: gclient.framework.ui.director_comp.battle_ui_stat_comp

import MConfig
import MEngine
import MImGui
import MPlatform
import MSystem
import MType
import MUI
import Timer
import cc
import ccs
import ccui
import functools
import os
import six2
import time

class BattleUiStatComp(object):
    def DebugStartStatUiOpacity(self): ...
    def DebugStopStatUiOpacity(self): ...
    def DebugWriteOpacityInfo(self): ...
    def ShowUiNodeOpacityStatus(self, root=None, layer=0, category=None, brief=None, csb_name=None, show_log=False): ...
    def stat_ui_and_scene_nodes(self): ...
    def write_ui_touch_status(self, root=None, layer=0, category=None, brief=None, csb_name=None, node_path=None, stat_scene_ui=False, dir_name='stat_touch', parent_visible=True): ...

class defaultdict(dict):
    clear: method_descriptor = <method 'clear' of 'dict' objects>
    copy: method_descriptor = <method 'copy' of 'collections.defaultdict' objects>
    default_factory: member_descriptor = <member 'default_factory' of 'collections.defaultdict' objects>
    fromkeys: builtin_function_or_method = <built-in method fromkeys of type object at 0x702850e7d8>
    get: method_descriptor = <method 'get' of 'dict' objects>
    items: method_descriptor = <method 'items' of 'dict' objects>
    keys: method_descriptor = <method 'keys' of 'dict' objects>
    pop: method_descriptor = <method 'pop' of 'dict' objects>
    popitem: method_descriptor = <method 'popitem' of 'dict' objects>
    setdefault: method_descriptor = <method 'setdefault' of 'dict' objects>
    update: method_descriptor = <method 'update' of 'dict' objects>
    values: method_descriptor = <method 'values' of 'dict' objects>


def dict_2_sort_list(d): ...
def format_value(value, indent=0): ...
def write_debug_data_to_file(name2data, dir_name='stat_opacity', file_name='stat_opacity_data'): ...


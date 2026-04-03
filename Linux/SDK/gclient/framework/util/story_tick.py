# module: gclient.framework.util.story_tick

import MEngine
import six2
import sys
import time

class SingletonMeta(type):
    mro: method_descriptor = <method 'mro' of 'type' objects>

class StoryTick(object):
    _instance: StoryTick = <gclient.framework.util.story_tick.StoryTick object at 0x7005e37fd0>

    def Add(self, func, frames=0): ...
    def Remove(self, func): ...
    def doAdd(self, func, frames): ...
    def doRemove(self, func): ...
    def onTick(self, _, dtime): ...

class StoryTickComponent(object):
    def AddStoryTick(self, func, frames=0): ...
    def ClearAllStoryTick(self): ...
    def RemoveStoryTick(self, func): ...

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



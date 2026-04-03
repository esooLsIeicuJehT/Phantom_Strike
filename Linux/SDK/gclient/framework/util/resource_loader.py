# module: gclient.framework.util.resource_loader

import MConfig
import MObject
import MResource
import Timer
import functools
import six2

ResourceLoader: _ResourceLoader = <gclient.framework.util.resource_loader._ResourceLoader object at 0x7040c51950>

class _ResourceLoader(object):
    def ChangePrimitives(self, entity, resources, materials=None, use_ready_to_appear=False, done=None): ...
    def LoadResource(self, entity, resources, materials=None, disablemip=False, done=None, use_ready_to_appear=False): ...
    def OnChangePrimitives(self, done, use_ready_to_appear, entity, model): ...
    def OnEntityReadyToAppear(self, entity, done, prim): ...
    def OnEntityResourceUpdated(self, done, entity): ...



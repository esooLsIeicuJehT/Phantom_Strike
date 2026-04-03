# module: gclient.framework.util.external_image_util

import MUI
import cconst
import six2

class SingletonMeta(type):
    mro: method_descriptor = <method 'mro' of 'type' objects>

class UIExternalImageBindMgr(object):
    _instance: UIExternalImageBindMgr = <gclient.framework.util.external_image_util.UIExternalImageBindMgr object at 0x6f5419bb90>

    def AddExternalImage(self, key, path, callback): ...
    def ClearAllExternalImages(self): ...
    def RemoveExternalImage(self, key): ...
    def SetExternalImage2023Cb(self, key, guid, is_ok, width, height): ...
    def SetExternalImageCb(self, key, isok): ...



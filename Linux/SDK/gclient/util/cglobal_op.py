# module: gclient.util.cglobal_op

import MRender
import cconst
import six2
import switches

class GlobalOp(object):
    _instance: NoneType = None

    def Clear(self, op_key): ...
    def ClearAll(self): ...
    def Pop(self, op_key, key): ...
    def Push(self, op_key, key, **kwargs): ...

class SingletonMeta(type):
    mro: method_descriptor = <method 'mro' of 'type' objects>


def Op_Xray(value, **kwargs): ...
def Op_blur(value, **kwargs): ...


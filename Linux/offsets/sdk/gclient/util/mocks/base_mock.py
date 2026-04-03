# module: gclient.util.mocks.base_mock

import Timer
import functools
import inspect

class EntityServerMock(Swallower):
    def destroy(self): ...
    def on_rpc(self, method, *args, **kwargs): ...

class Swallower(object):

def mock_method(func): ...


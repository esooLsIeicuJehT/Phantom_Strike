# module: gclient.util.post_process_manager

import MConfig
import MEngine
import MPlatform
import MRender
import cconst

class PostprocessManager(object):
    def Destroy(self): ...
    def DisablePostprocess(self, pp): ...
    def EnablePostprocess(self, pp, **kwargs): ...
    def _EnablePostprocess(self, pp, enable, **kwargs): ...



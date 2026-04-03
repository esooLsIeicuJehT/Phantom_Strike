# module: gclient.framework.util.low_fps_util

import config
import random
import time

upload_record_count: int = 0
upload_record_time: float = 0.0

class LowFpsCheck(object):
    def CheckLowFpsForLevel1(self): ...
    def CheckLowFpsForLevel2(self): ...
    def EnableLowFpsCheck(self, value): ...
    def UploadLowFpsRecord(self): ...



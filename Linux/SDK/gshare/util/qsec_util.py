# module: gshare.util.qsec_util

import hashlib
import json
import six2

COMPONENT: str = 'Client'
EssentialDataLookup: dict = {'weapon': 'gclient.data.ets_data.weapon'}

def calculate_md5(data): ...
def recursive_dict(data): ...


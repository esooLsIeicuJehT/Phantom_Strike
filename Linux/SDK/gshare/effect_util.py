# module: gshare.effect_util

import MCharacter
import MEngine
import MHelper
import MObject
import MType
import Timer
import cconst
import consts
import effect_data
import formula
import functools
import gun_skin_template_data
import material_type_data
import math
import random
import random_effect_data
import replay_util
import six2
import switches
import time
import weapon_data
import weapon_util

HitEffectMinInterval: float = 0.4
HitEffectRecords: defaultdict = defaultdict(<class 'float'>, {})
LocalConfig: _LocalConfig = <gclient.config._LocalConfig object at 0x7040bf6d50>

class EPerformanceLevel(enum):
    LEVEL_0: int = 0
    LEVEL_1: int = 1
    LEVEL_2: int = 2
    LEVEL_3: int = 3
    LEVEL_4: int = 4
    LEVEL_5: int = 5
    LEVEL_HIGHEST: int = 10
    name_to_values: dict = {'LEVEL_0': 0, 'LEVEL_1': 1, 'LEVEL_2': 2, 'LEVEL_3': 3, 'LEVEL_4': 4, 'LEVEL_5': 5, 'LEVEL_HIGHEST': 10}
    value_to_names: dict = {0: 'LEVEL_0', 1: 'LEVEL_1', 2: 'LEVEL_2', 3: 'LEVEL_3', 4: 'LEVEL_4', 5: 'LEVEL_5', 10: 'LEVEL_HIGHEST'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

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

class deque(object):
    append: method_descriptor = <method 'append' of 'collections.deque' objects>
    appendleft: method_descriptor = <method 'appendleft' of 'collections.deque' objects>
    clear: method_descriptor = <method 'clear' of 'collections.deque' objects>
    copy: method_descriptor = <method 'copy' of 'collections.deque' objects>
    count: method_descriptor = <method 'count' of 'collections.deque' objects>
    extend: method_descriptor = <method 'extend' of 'collections.deque' objects>
    extendleft: method_descriptor = <method 'extendleft' of 'collections.deque' objects>
    index: method_descriptor = <method 'index' of 'collections.deque' objects>
    insert: method_descriptor = <method 'insert' of 'collections.deque' objects>
    maxlen: getset_descriptor = <attribute 'maxlen' of 'collections.deque' objects>
    pop: method_descriptor = <method 'pop' of 'collections.deque' objects>
    popleft: method_descriptor = <method 'popleft' of 'collections.deque' objects>
    remove: method_descriptor = <method 'remove' of 'collections.deque' objects>
    reverse: method_descriptor = <method 'reverse' of 'collections.deque' objects>
    rotate: method_descriptor = <method 'rotate' of 'collections.deque' objects>


def ClearWorldEffect(effect): ...
def ClearWorldEffectImmediately(effect_id): ...
def ConfigBallisticEffect(ballistic_effect_id, is_ads, bullet_speed, hit_dis, is_fps_ballistic=True, gun_type=None, custom_scale=None): ...
def GetHitPosFromTarget(target, hit_pos, hit_normal): ...
def GetRandomAdsBallisticStartPos(muzzle_trans, radius, angle): ...
def PlayBallisticEffect(caster, spell_id, ballistic_effect, simple_version, context=None, init_context=False, use_context=False): ...
def PlayBloodDecalEffect(target, hit_pos, hit_dir): ...
def PlayHitEffect(caster, spell_id, hit_effect, is_immune=False): ...
def PreprocessRandomEffectCache(random_cache, pattern): ...
def TestTpsballistic(): ...
def WarpperPlayEffectInWorld(effect_id, pos, time=-1, insure_play=False, sound_event_id=None): ...
def WarpperPlayEffectInWorld2(effect_id, trans, time=-1, hook_suffix=None, insure_play=False): ...
def WrapperHitEffectResult(target, hit_pos, hit_normal, hit_material_type, hit_dir, caster, weapon_id, effect_id=0, extra_effect_id=None): ...


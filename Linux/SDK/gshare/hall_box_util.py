# module: gshare.hall_box_util

import all_gain_box_data
import box_probability_show_data
import choose_box_data
import consts
import hall_item_util
import hall_ui_util
import lobby_item_data
import random_box_data
import six2
import sys
import unique_random_box_data
import unique_random_box_guaranteed_data

class defaultdict(dict):
    clear: method_descriptor = <method 'clear' of 'dict' objects>
    copy: method_descriptor = <method 'copy' of 'collections.defaultdict' objects>
    default_factory: member_descriptor = <member 'default_factory' of 'collections.defaultdict' objects>
    fromkeys: builtin_function_or_method = <built-in method fromkeys of type object at 0x70252317d8>
    get: method_descriptor = <method 'get' of 'dict' objects>
    items: method_descriptor = <method 'items' of 'dict' objects>
    keys: method_descriptor = <method 'keys' of 'dict' objects>
    pop: method_descriptor = <method 'pop' of 'dict' objects>
    popitem: method_descriptor = <method 'popitem' of 'dict' objects>
    setdefault: method_descriptor = <method 'setdefault' of 'dict' objects>
    update: method_descriptor = <method 'update' of 'dict' objects>
    values: method_descriptor = <method 'values' of 'dict' objects>


def GetBoxDataForWarehouse(item_proto): ...
def GetItemListFromTreasureBox(item_proto): ...
def GetTreasureChooseBoxChooseLimit(item_proto): ...
def GetUniqueBoxGuranteeItemData(box_item_id): ...
def GetUniqueRandomDropBoxRewardDict(group_id): ...
def IsAvatarHasItem(avatar, item_id, include_experience_item=False, include_upgrade_item=False): ...


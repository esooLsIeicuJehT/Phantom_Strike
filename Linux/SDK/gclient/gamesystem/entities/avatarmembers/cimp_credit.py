# module: gclient.gamesystem.entities.avatarmembers.cimp_credit

import config
import consts
import events

class AvatarMember(object):
    def ReceiveCreDitWeekReward(self): ...
    def ShowCreditScorePoint(self): ...
    def _on_set_week_reward_state(self, old): ...

class ICreditScoreRecords(CustomListType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.icredit.ICreditScoreRecord'>
    append: method_descriptor = <method 'append' of 'area_list' objects>
    assign: method_descriptor = <method 'assign' of 'area_list' objects>
    clear: method_descriptor = <method 'clear' of 'area_list' objects>
    copy: method_descriptor = <method 'copy' of 'area_list' objects>
    delete: method_descriptor = <method 'delete' of 'area_list' objects>
    extend: method_descriptor = <method 'extend' of 'area_list' objects>
    get: method_descriptor = <method 'get' of 'area_list' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_list' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_list' objects>
    insert: method_descriptor = <method 'insert' of 'area_list' objects>
    list: method_descriptor = <method 'list' of 'area_list' objects>
    pop: method_descriptor = <method 'pop' of 'area_list' objects>
    size: method_descriptor = <method 'size' of 'area_list' objects>
    slice: method_descriptor = <method 'slice' of 'area_list' objects>
    sorted: method_descriptor = <method 'sorted' of 'area_list' objects>
    update: method_descriptor = <method 'update' of 'area_list' objects>

class WeekRewardState(enum):
    CanReceive: int = 1
    Default: int = 0
    Received: int = 2
    name_to_values: dict = {'Default': 0, 'CanReceive': 1, 'Received': 2}
    value_to_names: dict = {0: 'Default', 1: 'CanReceive', 2: 'Received'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...


def Property(name, default, flag=2): ...


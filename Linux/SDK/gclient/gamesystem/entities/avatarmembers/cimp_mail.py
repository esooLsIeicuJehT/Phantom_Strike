# module: gclient.gamesystem.entities.avatarmembers.cimp_mail

import consts
import events
import six2

TAB_SYS: int = 1

class CMail(IMail):
    IS_CUSTOM_TYPE: bool = True
    ITEM_SEP_ATTR: str = '*'
    ITEM_SEP_PAIR: str = ';'
    ITEM_SOURCE: str = 'item_source'
    KEY_ACTIVATED: str = 'activated'
    KEY_ASK_INFO: str = 'ask'
    KEY_ASK_PRESENT_ITEM: str = 'ask_present_item'
    KEY_BATTLE_HELP: str = 'from_avatarid'
    KEY_BUTTON: str = 'button'
    KEY_CLAN_SENDER: str = 'clan_sender'
    KEY_EXPIRED_TIME: str = 'expired_time'
    KEY_FORMAT: str = 'format_id'
    KEY_GIFT_INFO: str = 'gift'
    KEY_ITEMS: str = 'items'
    KEY_ITEMS_EXTRA: str = 'items_extra'
    KEY_ITEM_EXPIRE_TIME: str = 'item_expire_time'
    KEY_ITEM_HAS_GET: str = 'has_get'
    KEY_LINKS: str = 'links'
    KEY_MALL_ASK_INFO: str = 'mall_ask'
    KEY_MALL_GIFT_HAS_SEND: str = 'has_send_gift'
    KEY_MALL_GIFT_INFO: str = 'mall_gift'
    KEY_MULTI_MAIL_ARGS: str = 'args'
    KEY_MULTI_MAIL_ID: str = 'multi_mail_id'
    KEY_PLUGIN_REPORT: str = 'rerole_id'
    KEY_PRESENT_ITEM: str = 'present_item'
    KEY_TAB: str = 'tab'
    KEY_THANK_INFO: str = 'thank'
    KEY_URL: str = 'url'
    clear: method_descriptor = <method 'clear' of 'area_map' objects>
    copy: method_descriptor = <method 'copy' of 'area_map' objects>
    dict: method_descriptor = <method 'dict' of 'area_map' objects>
    dsize: method_descriptor = <method 'dsize' of 'area_map' objects>
    get: method_descriptor = <method 'get' of 'area_map' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_map' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_map' objects>
    iteritems: method_descriptor = <method 'iteritems' of 'area_map' objects>
    iterkeys: method_descriptor = <method 'iterkeys' of 'area_map' objects>
    itervalues: method_descriptor = <method 'itervalues' of 'area_map' objects>
    normal_iteritems: method_descriptor = <method 'normal_iteritems' of 'area_map' objects>
    normal_iterkeys: method_descriptor = <method 'normal_iterkeys' of 'area_map' objects>
    normal_itervalues: method_descriptor = <method 'normal_itervalues' of 'area_map' objects>
    pop: method_descriptor = <method 'pop' of 'area_map' objects>
    props_all: method_descriptor = <method 'props_all' of 'area_map' objects>
    size: method_descriptor = <method 'size' of 'area_map' objects>
    total_size: method_descriptor = <method 'total_size' of 'area_map' objects>
    update: method_descriptor = <method 'update' of 'area_map' objects>
    weak_dict: method_descriptor = <method 'weak_dict' of 'area_map' objects>

    def Activate(self): ...
    def Consumed(self): ...
    def Expired(self, now): ...
    def GetItems(self): ...
    def HasItems(self): ...
    def IsRead(self): ...
    def MarkRead(self): ...
    def RefillBody(self, country_code='zh'): ...
    def SetConsumed(self): ...
    def _initProperty(self, data): ...
    @property
    def is_activated(self): ...    @property
    def item_str(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def multi_mail_args(self): ...    @property
    def multi_mail_id(self): ...    def on_setattr(self, key, old, new): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    @property
    def tab(self): ...    def update2(self, data): ...
    def values(self): ...

class CMailExtraMap(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    clear: method_descriptor = <method 'clear' of 'area_map' objects>
    copy: method_descriptor = <method 'copy' of 'area_map' objects>
    dict: method_descriptor = <method 'dict' of 'area_map' objects>
    dsize: method_descriptor = <method 'dsize' of 'area_map' objects>
    get: method_descriptor = <method 'get' of 'area_map' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_map' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_map' objects>
    iteritems: method_descriptor = <method 'iteritems' of 'area_map' objects>
    iterkeys: method_descriptor = <method 'iterkeys' of 'area_map' objects>
    itervalues: method_descriptor = <method 'itervalues' of 'area_map' objects>
    normal_iteritems: method_descriptor = <method 'normal_iteritems' of 'area_map' objects>
    normal_iterkeys: method_descriptor = <method 'normal_iterkeys' of 'area_map' objects>
    normal_itervalues: method_descriptor = <method 'normal_itervalues' of 'area_map' objects>
    pop: method_descriptor = <method 'pop' of 'area_map' objects>
    props_all: method_descriptor = <method 'props_all' of 'area_map' objects>
    size: method_descriptor = <method 'size' of 'area_map' objects>
    total_size: method_descriptor = <method 'total_size' of 'area_map' objects>
    update: method_descriptor = <method 'update' of 'area_map' objects>
    weak_dict: method_descriptor = <method 'weak_dict' of 'area_map' objects>

    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def on_setattr(self, key, old, new): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class CMails(Mails):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gclient.gamesystem.entities.avatarmembers.cimp_mail.CMail'>
    clear: method_descriptor = <method 'clear' of 'area_map' objects>
    copy: method_descriptor = <method 'copy' of 'area_map' objects>
    dict: method_descriptor = <method 'dict' of 'area_map' objects>
    dsize: method_descriptor = <method 'dsize' of 'area_map' objects>
    get: method_descriptor = <method 'get' of 'area_map' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_map' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_map' objects>
    iteritems: method_descriptor = <method 'iteritems' of 'area_map' objects>
    iterkeys: method_descriptor = <method 'iterkeys' of 'area_map' objects>
    itervalues: method_descriptor = <method 'itervalues' of 'area_map' objects>
    normal_iteritems: method_descriptor = <method 'normal_iteritems' of 'area_map' objects>
    normal_iterkeys: method_descriptor = <method 'normal_iterkeys' of 'area_map' objects>
    normal_itervalues: method_descriptor = <method 'normal_itervalues' of 'area_map' objects>
    pop: method_descriptor = <method 'pop' of 'area_map' objects>
    props_all: method_descriptor = <method 'props_all' of 'area_map' objects>
    size: method_descriptor = <method 'size' of 'area_map' objects>
    total_size: method_descriptor = <method 'total_size' of 'area_map' objects>
    update: method_descriptor = <method 'update' of 'area_map' objects>
    weak_dict: method_descriptor = <method 'weak_dict' of 'area_map' objects>

    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def on_setattr(self, key, old, new): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class CustomMapType(area_map):
    IS_CUSTOM_TYPE: bool = True
    clear: method_descriptor = <method 'clear' of 'area_map' objects>
    copy: method_descriptor = <method 'copy' of 'area_map' objects>
    dict: method_descriptor = <method 'dict' of 'area_map' objects>
    dsize: method_descriptor = <method 'dsize' of 'area_map' objects>
    get: method_descriptor = <method 'get' of 'area_map' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_map' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_map' objects>
    iteritems: method_descriptor = <method 'iteritems' of 'area_map' objects>
    iterkeys: method_descriptor = <method 'iterkeys' of 'area_map' objects>
    itervalues: method_descriptor = <method 'itervalues' of 'area_map' objects>
    normal_iteritems: method_descriptor = <method 'normal_iteritems' of 'area_map' objects>
    normal_iterkeys: method_descriptor = <method 'normal_iterkeys' of 'area_map' objects>
    normal_itervalues: method_descriptor = <method 'normal_itervalues' of 'area_map' objects>
    pop: method_descriptor = <method 'pop' of 'area_map' objects>
    props_all: method_descriptor = <method 'props_all' of 'area_map' objects>
    size: method_descriptor = <method 'size' of 'area_map' objects>
    total_size: method_descriptor = <method 'total_size' of 'area_map' objects>
    update: method_descriptor = <method 'update' of 'area_map' objects>
    weak_dict: method_descriptor = <method 'weak_dict' of 'area_map' objects>

    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class IMail(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    ITEM_SEP_ATTR: str = '*'
    ITEM_SEP_PAIR: str = ';'
    ITEM_SOURCE: str = 'item_source'
    KEY_ACTIVATED: str = 'activated'
    KEY_ASK_INFO: str = 'ask'
    KEY_ASK_PRESENT_ITEM: str = 'ask_present_item'
    KEY_BATTLE_HELP: str = 'from_avatarid'
    KEY_BUTTON: str = 'button'
    KEY_CLAN_SENDER: str = 'clan_sender'
    KEY_EXPIRED_TIME: str = 'expired_time'
    KEY_FORMAT: str = 'format_id'
    KEY_GIFT_INFO: str = 'gift'
    KEY_ITEMS: str = 'items'
    KEY_ITEMS_EXTRA: str = 'items_extra'
    KEY_ITEM_EXPIRE_TIME: str = 'item_expire_time'
    KEY_ITEM_HAS_GET: str = 'has_get'
    KEY_LINKS: str = 'links'
    KEY_MALL_ASK_INFO: str = 'mall_ask'
    KEY_MALL_GIFT_HAS_SEND: str = 'has_send_gift'
    KEY_MALL_GIFT_INFO: str = 'mall_gift'
    KEY_MULTI_MAIL_ARGS: str = 'args'
    KEY_MULTI_MAIL_ID: str = 'multi_mail_id'
    KEY_PLUGIN_REPORT: str = 'rerole_id'
    KEY_PRESENT_ITEM: str = 'present_item'
    KEY_TAB: str = 'tab'
    KEY_THANK_INFO: str = 'thank'
    KEY_URL: str = 'url'
    clear: method_descriptor = <method 'clear' of 'area_map' objects>
    copy: method_descriptor = <method 'copy' of 'area_map' objects>
    dict: method_descriptor = <method 'dict' of 'area_map' objects>
    dsize: method_descriptor = <method 'dsize' of 'area_map' objects>
    get: method_descriptor = <method 'get' of 'area_map' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_map' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_map' objects>
    iteritems: method_descriptor = <method 'iteritems' of 'area_map' objects>
    iterkeys: method_descriptor = <method 'iterkeys' of 'area_map' objects>
    itervalues: method_descriptor = <method 'itervalues' of 'area_map' objects>
    normal_iteritems: method_descriptor = <method 'normal_iteritems' of 'area_map' objects>
    normal_iterkeys: method_descriptor = <method 'normal_iterkeys' of 'area_map' objects>
    normal_itervalues: method_descriptor = <method 'normal_itervalues' of 'area_map' objects>
    pop: method_descriptor = <method 'pop' of 'area_map' objects>
    props_all: method_descriptor = <method 'props_all' of 'area_map' objects>
    size: method_descriptor = <method 'size' of 'area_map' objects>
    total_size: method_descriptor = <method 'total_size' of 'area_map' objects>
    update: method_descriptor = <method 'update' of 'area_map' objects>
    weak_dict: method_descriptor = <method 'weak_dict' of 'area_map' objects>

    def Activate(self): ...
    def Consumed(self): ...
    def Expired(self, now): ...
    def GetItems(self): ...
    def HasItems(self): ...
    def IsRead(self): ...
    def MarkRead(self): ...
    def RefillBody(self, country_code='zh'): ...
    def SetConsumed(self): ...
    def _initProperty(self, data): ...
    @property
    def is_activated(self): ...    @property
    def item_str(self): ...    def items(self): ...
    def keys(self): ...
    @property
    def multi_mail_args(self): ...    @property
    def multi_mail_id(self): ...    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    @property
    def tab(self): ...    def update2(self, data): ...
    def values(self): ...

class Mails(CustomMapType):
    IS_CUSTOM_TYPE: bool = True
    VALUE_TYPE: CustomMapTypeMetaClass = <class 'gshare.imail.IMail'>
    clear: method_descriptor = <method 'clear' of 'area_map' objects>
    copy: method_descriptor = <method 'copy' of 'area_map' objects>
    dict: method_descriptor = <method 'dict' of 'area_map' objects>
    dsize: method_descriptor = <method 'dsize' of 'area_map' objects>
    get: method_descriptor = <method 'get' of 'area_map' objects>
    get_owner: method_descriptor = <method 'get_owner' of 'area_map' objects>
    get_parent: method_descriptor = <method 'get_parent' of 'area_map' objects>
    iteritems: method_descriptor = <method 'iteritems' of 'area_map' objects>
    iterkeys: method_descriptor = <method 'iterkeys' of 'area_map' objects>
    itervalues: method_descriptor = <method 'itervalues' of 'area_map' objects>
    normal_iteritems: method_descriptor = <method 'normal_iteritems' of 'area_map' objects>
    normal_iterkeys: method_descriptor = <method 'normal_iterkeys' of 'area_map' objects>
    normal_itervalues: method_descriptor = <method 'normal_itervalues' of 'area_map' objects>
    pop: method_descriptor = <method 'pop' of 'area_map' objects>
    props_all: method_descriptor = <method 'props_all' of 'area_map' objects>
    size: method_descriptor = <method 'size' of 'area_map' objects>
    total_size: method_descriptor = <method 'total_size' of 'area_map' objects>
    update: method_descriptor = <method 'update' of 'area_map' objects>
    weak_dict: method_descriptor = <method 'weak_dict' of 'area_map' objects>

    def _initProperty(self, data): ...
    def items(self): ...
    def keys(self): ...
    def setdefault(self, key, default): ...
    def show_memory_status(self): ...
    def update2(self, data): ...
    def values(self): ...

class PlayerAvatarMember(object):
    def GetSortedMails(self): ...
    def GetSortedMailsByTab(self, tab=1): ...
    def GetUnClaimedMailNumber(self): ...
    def GetUnClaimedMailNumberByTab(self, tab): ...
    def GetUnreadActiveMailNumber(self): ...
    def GetUnreadMailConsiderExtraItemsNumber(self): ...
    def GetUnreadMailNumber(self): ...
    def GetUnreadMailNumberByTab(self, tab): ...
    def HasReadMail(self): ...
    def HasUnreadMail(self): ...
    def RefreshSortedMails(self): ...

class PropertyMetaClass(type):
    mro: method_descriptor = <method 'mro' of 'type' objects>


def Property(name, default, flag=2): ...


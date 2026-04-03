# module: gclient.util.serverlist_fetcher

import GeneralLog
import MConfig
import functools
import json
import lang
import netdetecter
import six2
import switches
import sys
import utils

INNER_SERVER_LIST: OrderedDict = OrderedDict([('Offline', ()), ('LocalServer', (('{localhost}', 33360), ('{localhost}', 33363))), ('本地跨服-31002', (('{localhost}', 33357), ('{localhost}', 33359))), ('本地跨服-31003', (('{localhost}', 34357), ('{localhost}', 34359))), (20001, (('35.200.123.155', 4010), ('35.200.123.155', 4020))), (21001, [('59.111.2.229', '4010'), ('59.111.2.229', '4020'), ('59.111.2.229', '4030'), ('59.111.2.229', '4040')]), (21003, [('59.111.2.38', '4010'), ('59.111.2.38', '4020'), ('59.111.2.38', '4030'), ('59.111.2.38', '4040')]), (22001, [('42.186.105.47', '4010'), ('42.186.105.47', '4020'), ('42.186.105.47', '4030'), ('42.186.105.47', '4040'), ('42.186.105.48', '4010'), ('42.186.105.48', '4020'), ('42.186.105.48', '4030'), ('42.186.105.48', '4040'), ('42.186.105.49', '4010'), ('42.186.105.49', '4020'), ('42.186.105.49', '4030'), ('42.186.105.49', '4040')]), (22002, [('42.186.105.50', '4010'), ('42.186.105.50', '4020'), ('42.186.105.50', '4030'), ('42.186.105.50', '4040'), ('42.186.105.51', '4010'), ('42.186.105.51', '4020'), ('42.186.105.51', '4030'), ('42.186.105.51', '4040'), ('42.186.105.52', '4010'), ('42.186.105.52', '4020'), ('42.186.105.52', '4030'), ('42.186.105.52', '4040')]), (23002, [('42.186.230.150', '4010'), ('42.186.230.150', '4020'), ('42.186.230.150', '4030'), ('42.186.230.150', '4040')]), (26001, (('42.186.101.199', 4020),)), (26002, (('42.186.231.119', 4020),)), ('29001-A服', (('8.215.41.128', 4010),)), ('公共服', (('10.212.18.175', 43366), ('10.212.18.175', 43363)))])

class HttpRequest(object):
class LoginEntryInfo(object):
    def Update(self, info): ...
    @property
    def center_server_id(self): ...    @property
    def gate_list(self): ...    @property
    def show_name(self): ...
class OrderedDict(dict):
    clear: method_descriptor = <method 'clear' of 'collections.OrderedDict' objects>
    copy: method_descriptor = <method 'copy' of 'collections.OrderedDict' objects>
    fromkeys: builtin_function_or_method = <built-in method fromkeys of type object at 0x70285412c8>
    get: method_descriptor = <method 'get' of 'dict' objects>
    items: method_descriptor = <method 'items' of 'collections.OrderedDict' objects>
    keys: method_descriptor = <method 'keys' of 'collections.OrderedDict' objects>
    move_to_end: method_descriptor = <method 'move_to_end' of 'collections.OrderedDict' objects>
    pop: method_descriptor = <method 'pop' of 'collections.OrderedDict' objects>
    popitem: method_descriptor = <method 'popitem' of 'collections.OrderedDict' objects>
    setdefault: method_descriptor = <method 'setdefault' of 'collections.OrderedDict' objects>
    update: method_descriptor = <method 'update' of 'collections.OrderedDict' objects>
    values: method_descriptor = <method 'values' of 'collections.OrderedDict' objects>


def FetchServerList(callback): ...
def GetHttpClient(name=None, max_clients=2, **kwargs): ...
def GetHttpDns(domain, dns_callback): ...
def UnicodeToUTF8(d): ...
def _DNS_FetchServerList(domain, port, url_name, callback, ip): ...
def _FetchServerList(domain, host, port, url_name, use_httpdns, callback): ...
def _ParseInnerServerList(reply): ...
def _ParseOuterServerList(reply): ...


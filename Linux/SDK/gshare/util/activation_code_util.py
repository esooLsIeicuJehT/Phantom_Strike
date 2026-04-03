# module: gshare.util.activation_code_util

import random
import six2
import time_util

AutoGainAfterCompletingChallenge: int = 2
CODE_ALPHABET: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7', '8', '9']
CODE_ALPHABET_SET: set = {'R', 'C', '2', 'W', 'K', 'S', '9', 'Q', 'F', 'I', 'E', '4', 'T', 'L', 'M', 'J', '7', '5', 'V', 'G', 'N', '6', 'H', 'Z', '8', '3', 'P', 'D', 'Y', 'A', 'B', 'U', 'X', 'O'}
CODE_BODY_LENGTH: int = 9
CODE_PREFIX_LENGTH: int = 1
CODE_TOTAL_LENGTH: int = 10
COMPONENT: str = 'Client'
GainProbabilityPerGame: float = 0.2
INVITE_CODE_ACTIVITY_END_TIME: str = '2023-11-30 23:59:59'
INVITE_CODE_ACTIVITY_END_TIMESTAMP: float = 1701368999.0
INVITE_CODE_COPY_PREFIX: str = '###'
INVITE_CODE_LOGIN_END_TIME: str = '2023-9-21 23:59:59'
INVITE_CODE_LOGIN_END_TIMESTAMP: float = 1695320999.0
MaxGainPerDay: int = 24
NORMAL_CODE_PREFIXS: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
NORMAL_CODE_PREFIX_SHARDS: dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18}
PersonalMaxCount: int = 8
SUPER_CODE_PREFIX: str = 'Z'
VALID_PREFIX: set = {'R', 'C', 'K', 'S', 'Q', 'F', 'I', 'E', 'L', 'M', 'J', 'G', 'N', 'H', 'Z', 'P', 'D', 'A', 'B', 'O'}
_reload_all: bool = True

class ActivationCodeCheckResult(object):
    ALPHABET: int = 3
    EMPTY: int = 1
    LENGTH: int = 2
    OK: int = 0

class ActivationCodeUseResult(object):
    DB_ERROR: int = 1
    FORMAT: int = 3
    FULL: int = 5
    INVALID: int = 2
    SUCCESS: int = 0
    USED: int = 4

class ActivationCodeUseResultNew(object):
    AVATAR_INVALID: int = 2
    CODE_INVALID: int = 1
    INVITED: int = 3
    MULTI_LOGIN: int = 4
    SUCCESS: int = 0

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


def EnableActivateAct(): ...
def EnableActivateLogin(): ...
def FilterPasteText(text): ...
def IsInInviteCodeActivityEndTime(): ...
def IsInInviteCodeLoginEndTime(): ...
def IsInvalid(code): ...
def IsSuper(code): ...
def SelectPasteText(text): ...
def _GenerateBody(): ...


# module: gshare.consts

import functools
import math
import six2
import time

ADD_REWARD_ITEM_SPECIAL_CODE: dict = {4000000010: 'AddMoneyByItem', 4000000020: 'AddMoneyByItem', 4000000040: 'AddMoneyByItem'}
AIRDROP_SHOP_CATEGORIES_SHOW: list = [999, 1]
ALL_BIND_PLATFORMS: tuple = (3, 16, 5, 24, 23, 17, 9, 7, 25, 4)
ALL_SOLD_MALL_GUN_SKIN_SUB_TYPES: tuple = (302, 303, 304, 305)
ANTI_PENETRATE_IGNORE_MOTION_STATES: set = {'Strop'}
ASK_FOR_REDEPLOY_CD: int = 15
AvatarCollisionBoneLimits: dict = {'head': <gshare.consts.CylinderMatcher object at 0x7040ffec10>, 'uppertop': <gshare.consts.BoxMatcher object at 0x7040ffee50>, 'upperbottom': <gshare.consts.BoxMatcher object at 0x7040ffee90>, 'lower': <gshare.consts.BoxMatcher object at 0x7040ffef50>, 'limbs_r_upperarm': <gshare.consts.CylinderMatcher object at 0x7040fff010>, 'limbs_r_forearm': <gshare.consts.CylinderMatcher object at 0x7040fff0d0>, 'limbs_r_hand': <gshare.consts.CylinderMatcher object at 0x7040fff110>, 'limbs_l_upperarm': <gshare.consts.CylinderMatcher object at 0x7040fff150>, 'limbs_l_forearm': <gshare.consts.CylinderMatcher object at 0x7040fff190>, 'limbs_l_hand': <gshare.consts.CylinderMatcher object at 0x7040fff1d0>, 'limbs_r_thigh': <gshare.consts.CylinderMatcher object at 0x7040fff210>, 'limbs_r_calf': <gshare.consts.CylinderMatcher object at 0x7040fff250>, 'limbs_l_thigh': <gshare.consts.CylinderMatcher object at 0x7040fff290>, 'limbs_l_calf': <gshare.consts.CylinderMatcher object at 0x7040fff2d0>}
AvatarCollisionBoneToNormalBone: dict = {'head': 'biped Head', 'uppertop': 'biped Spine', 'upperbottom': 'biped Spine', 'lower': 'biped Spine1', 'limbs_r_upperarm': 'biped R UpperArm', 'limbs_r_forearm': 'biped R Forearm', 'limbs_r_hand': 'biped R Hand', 'limbs_l_upperarm': 'biped L UpperArm', 'limbs_l_forearm': 'biped L Forearm', 'limbs_l_hand': 'biped L Hand', 'limbs_r_thigh': 'biped R Thigh', 'limbs_r_calf': 'biped R Calf', 'limbs_l_thigh': 'biped L Thigh', 'limbs_l_calf': 'biped L Calf'}
AvatarCollisionBone_Head: str = 'head'
AvatarCollisionBone_Limbs: str = 'limbs'
AvatarCollisionBone_Limbs_L_Calf: str = 'limbs_l_calf'
AvatarCollisionBone_Limbs_L_Forearm: str = 'limbs_l_forearm'
AvatarCollisionBone_Limbs_L_Hand: str = 'limbs_l_hand'
AvatarCollisionBone_Limbs_L_Thigh: str = 'limbs_l_thigh'
AvatarCollisionBone_Limbs_L_UpperArm: str = 'limbs_l_upperarm'
AvatarCollisionBone_Limbs_R_Calf: str = 'limbs_r_calf'
AvatarCollisionBone_Limbs_R_Forearm: str = 'limbs_r_forearm'
AvatarCollisionBone_Limbs_R_Hand: str = 'limbs_r_hand'
AvatarCollisionBone_Limbs_R_Thigh: str = 'limbs_r_thigh'
AvatarCollisionBone_Limbs_R_UpperArm: str = 'limbs_r_upperarm'
AvatarCollisionBone_Lower: str = 'lower'
AvatarCollisionBone_UpperBottom: str = 'upperbottom'
AvatarCollisionBone_UpperTop: str = 'uppertop'
AvatarEvent: NoneType = None
AvatarNormalBone_Head: str = 'biped Head'
AvatarNormalBone_L_Calf: str = 'biped L Calf'
AvatarNormalBone_L_Forearm: str = 'biped L Forearm'
AvatarNormalBone_L_Hand: str = 'biped L Hand'
AvatarNormalBone_L_Thigh: str = 'biped L Thigh'
AvatarNormalBone_L_UpperArm: str = 'biped L UpperArm'
AvatarNormalBone_Neck: str = 'biped Neck'
AvatarNormalBone_R_Calf: str = 'biped R Calf'
AvatarNormalBone_R_Forearm: str = 'biped R Forearm'
AvatarNormalBone_R_Hand: str = 'biped R Hand'
AvatarNormalBone_R_Thigh: str = 'biped R Thigh'
AvatarNormalBone_R_UpperArm: str = 'biped R UpperArm'
AvatarNormalBone_Spine: str = 'biped Spine'
AvatarNormalBone_Spine1: str = 'biped Spine1'
BACKPACK_MAX_COUNT: int = 10
BAN_ASSIST_AIM_MODE_NEWER_QUALIFYING_LEVEL: int = 17
BUY_TEAMMATE_ITEM: int = 999
BaseFinetuneSlotNum: int = 3
BoxHalf: dict = {'uppertop': [0.1632, 0.20400000000000001, 0.0612], 'upperbottom': [0.1632, 0.20400000000000001, 0.10200000000000001], 'lower': [0.153, 0.18359999999999999, 0.10200000000000001]}
CAN_WATCH_ROBOT: bool = False
COINS_ITEM_ID: int = 18
COMBAT_RELATION_I_KILL: int = 3
COMBAT_RELATION_KILL_ME: int = 2
COMBAT_RELATION_TEAMMATE: int = 1
COMPONENT: str = 'Client'
CREDIT_SCORE_ABUSE: int = 5
CREDIT_SCORE_ABUSE_COUNT: int = 3
CREDIT_SCORE_ABUSE_DAY: int = 10
CREDIT_SCORE_ADVANCE: dict = {1: 4, 2: 8, 3: 12}
CREDIT_SCORE_DAY_ADD_LIMIT: int = 40
CREDIT_SCORE_HANGUP: dict = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
CREDIT_SCORE_LEVEL_COUNT: dict = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2}
CREDIT_SCORE_MAX: int = 100
CREDIT_SCORE_RECOVER: int = 5
CREDIT_SCORE_REQUIRE: dict = {130004: 95, 100404: 80, 100401: 60}
CRYSTAL_SCANNER_ITEM_ID: int = 307
ClothesSubTypeList: list = [300, 310, 320, 330, 340, 350, 360]
CombatAvatarEvent: NoneType = None
CombatItemAmmoLimit: dict = {7: 200, 14: 200, 8: 200, 71: 200, 197: 24}
CombatItemPhysxArgs: dict = {101: (0.1, (0, -7, 0), 2, 4), 103: (0.1, (0, -4, 0), 0, -4)}
CountryCode_CHINA: str = '86'
CountryCode_JAPAN: str = '81'
CountryCode_TAIWAN: str = '886'
CylinderRadius: dict = {'head': 0.1224, 'limbs_l_thigh': 0.10200000000000001, 'limbs_l_calf': 0.8160000000000001, 'limbs_r_thigh': 0.10200000000000001, 'limbs_r_calf': 0.8160000000000001, 'limbs_l_upperarm': 0.0714, 'limbs_l_forearm': 0.0714, 'limbs_l_hand': 0.051000000000000004, 'limbs_r_upperarm': 0.0714, 'limbs_r_forearm': 0.0714, 'limbs_r_hand': 0.051000000000000004}
DEFAULT_ELO_SCORE: int = 1200
DEFAULT_HEAD_ID: int = 6030000040
DEFAULT_MATCH_MODE: int = 1
DEFAULT_MATCH_SPACENOS: list = [10]
DEFAULT_MATCH_TYPE: int = 1004
DEFAULT_ROBOT_ARM_CLOTHES: dict = {300: 3700000010}
DEFAULT_SUIT: int = 3700000010
DELAY_LEAVE_ISLAND_TIME: float = 5.0
DefaultBombSkinItemId: dict = {3: 6500000100, 4: 6500000200, 7: 6500000300, 12: 6500000400, 81: 6500000500}
EApplyListLimit: int = 100
EBlacklistLimit: int = 50
ECommonMallMoneyType: dict = {1: 'honor', 4: 'yuanbao', 3: 'pay_yuanbao', 2: 'free_yuanbao', 5: 'item', 6: 'limit_yuanbao', 7: 'metal'}
EErrorMessage_ANTI_ADDICTION_V2: str = 'AntiAddictionV2'
EErrorMessage_CHEAT: str = 'ClientCheat'
EErrorMessage_CbgPuton: str = 'CbgPuton'
EErrorMessage_ClientHeartbeatTimeout: str = 'ClientHeartbeatTimeout'
EErrorMessage_DeviceLimit: str = 'DeviceLimit'
EErrorMessage_ENGINE_VERSION: str = 'LogoffEngineVersion'
EErrorMessage_EnterSpaceFailed: str = 'EnterSpaceFailed'
EErrorMessage_FORBID_LOGIN: str = 'ForbidLogin'
EErrorMessage_FORBIT_MATCH: str = 'ForbitMatch'
EErrorMessage_KICKOUT: str = 'KickoutByServer'
EErrorMessage_MOBILE_ANTI_ADDITION: str = 'MobileAntiAddition'
EErrorMessage_MigrateInSpaceNotExists: str = 'MigrateInSpaceNotExists'
EErrorMessage_OnLoseClient: str = 'OnLoseClient'
EErrorMessage_PC_ANTI_ADDITION: str = 'PCAntiAddition'
EErrorMessage_ROLLSTUB_GUESS_BLOCKED: str = 'RollStubGuessBlocked'
EErrorMessage_RollStubCheckinButAvatarInBadStatus: str = 'RollStubCheckinButAvatarInBadStatus'
EErrorMessage_TRANSFER: str = 'TransferAvatar'
EErrorMessage_TeleportFailed: str = 'TeleportFailed'
EFRIENDSZ_APPLY_REASON_MAX_LEN: int = 17
EFRIEND_FROM_ACTIVITY: int = 10
EFRIEND_FROM_CALCULATION: int = 9
EFRIEND_FROM_CHAT: int = 4
EFRIEND_FROM_CLAN: int = 11
EFRIEND_FROM_CLAN_MEMBER: int = 12
EFRIEND_FROM_LBS: int = 2
EFRIEND_FROM_RECENT: int = 3
EFRIEND_FROM_RECOMMEND: int = 1
EFRIEND_FROM_REPLAY: int = 7
EFRIEND_FROM_ROOM: int = 8
EFRIEND_FROM_SEARCH: int = 0
EFRIEND_FROM_SPACE: int = 6
EFRIEND_FROM_TEAM: int = 5
EForbidPayStatus_ABANDON_FORBID: int = 2
EForbidPayStatus_NORMAL_FORBID: int = 1
EForbidPayStatus_NO_FORBID: int = 0
EFriendListLimit: int = 200
EFriendMaxLimit: int = 1000
EFriendRemarkMaxLength: int = 7
EFriendSZ_APPLY: int = 100
EFriendSZ_APPLY_INTERVAL_TIME: int = 3600
EFriendSZ_BLACKLIST: int = 100
EFriendSZ_FRIEND: int = 100
EFriendSZ_RECENT: int = 20
EHallStatus_BATTLE: int = 3
EHallStatus_BUSY: int = 6
EHallStatus_HALL: int = 0
EHallStatus_HALL_LOGIN: int = 8
EHallStatus_HIDE: int = 7
EHallStatus_MATCHING: int = 2
EHallStatus_OFFLINE: int = 9
EHallStatus_ROOM: int = 4
EHallStatus_TEAMING: int = 1
EHallStatus_WATCH: int = 5
EItemChangeType_ACT: str = 'act'
EItemChangeType_ALL_GAIN_BOX: str = 'all gain box'
EItemChangeType_AUTO_REMOVE_DEFAULT_SKIN: str = 'auto remove default skin'
EItemChangeType_BANNER_JUMP_REWARD: str = 'banner jump reward'
EItemChangeType_BIND_GUN_ITEM: str = 'bind gun item'
EItemChangeType_BIND_ITEMS: str = 'bind items'
EItemChangeType_BREAK_ITEM: str = 'break item'
EItemChangeType_COMMON_ITEM_UNLOCK: str = 'common item unlock'
EItemChangeType_CREATE_CLAN: str = 'create clan'
EItemChangeType_Choose_Box: str = 'choose box'
EItemChangeType_CreditScoreReward: str = 'credit score reward'
EItemChangeType_DAILY_FIRST_WIN: str = 'daily first win'
EItemChangeType_DAILY_SPECIAL_SHOP: str = 'daily special shop'
EItemChangeType_DECOMPOSE_ITEM: str = 'decompose item'
EItemChangeType_FAKE_GACHA_TICKET: str = 'fake gacha ticket'
EItemChangeType_FINE_TUNING: str = 'fine tuning'
EItemChangeType_FIRST_PAY: str = 'first pay'
EItemChangeType_Frag_Compose: str = 'frag compose'
EItemChangeType_GACHA: str = 'gacha'
EItemChangeType_GACHA_MILESTONE: str = 'gacha milestone'
EItemChangeType_GACHA_TOKEN: str = 'gacha token'
EItemChangeType_GM: str = 'gm'
EItemChangeType_GUN_BUY_UNLOCK: str = 'gun buy unlock'
EItemChangeType_GUN_EXP_EXTRA: str = 'gun extra exp'
EItemChangeType_GUN_LEVEL_UNLOCK: str = 'gun level unlock'
EItemChangeType_GUN_TASK_UNLOCK: str = 'gun task unlock'
EItemChangeType_IAP: str = 'iap'
EItemChangeType_ITEM_EXPIRED: str = 'item expired'
EItemChangeType_ITEM_UPGRADE: str = 'item upgrade'
EItemChangeType_LIGHTNING_DEAL: str = 'lightning deal'
EItemChangeType_LIMIT_YUANBAO: str = 'limit yuanbao'
EItemChangeType_LIMIT_YUANBAO_EXPIRED: str = 'limit yuanbao expired'
EItemChangeType_MAIL: str = 'mail'
EItemChangeType_MALL: str = 'mall'
EItemChangeType_NONE: str = 'none'
EItemChangeType_ORNAMENTS: str = 'use or recycle ornaments'
EItemChangeType_PAY: str = 'pay'
EItemChangeType_QUALIFYING: str = 'qualifying'
EItemChangeType_QUALIFYING_INHERIT: str = 'qualifying inherit'
EItemChangeType_REGULAR_GIFT_YUANBAO: str = 'regular gift yuanbao'
EItemChangeType_REWARD: str = 'reward'
EItemChangeType_ROOKIE: str = 'rookie'
EItemChangeType_Random_Drop_Box: str = 'random drop box'
EItemChangeType_Rank: str = 'rank item'
EItemChangeType_SAGM_ADDITEM: str = 'sa add item'
EItemChangeType_SAGM_ADDMONEY: str = 'sa add money'
EItemChangeType_SAGM_REDUCEITEM: str = 'sa reduce item'
EItemChangeType_SAGM_REDUCEMONEY: str = 'sa reduce money'
EItemChangeType_SCORE_PROTECT: str = 'score protect'
EItemChangeType_SCORE_REWARD: str = 'score reward'
EItemChangeType_SETTLE_REWARD: str = 'settle reward'
EItemChangeType_SKIN_UNLOCK: str = 'skin unlock'
EItemChangeType_Server_Migrate: str = 'server migrate'
EItemChangeType_TIME_LIMIT: str = 'time limit'
EItemChangeType_TIME_LIMIT_DELETE: str = 'time limit delete'
EItemChangeType_TIME_LIMIT_TRANS: str = 'time limit trans'
EItemChangeType_TRIAL_GUN: str = 'trial_gun'
EItemChangeType_UPGRADE_HALL_ITEM: str = 'upgrade hall item'
EItemChangeType_USE_ITEM: str = 'use item'
EItemChangeType_USE_STICKER: str = 'use sticker'
EItemChangeType_Unique_Random_Drop_Box: str = 'unique random drop box'
EItemSource_DECOMPOSE_ITEM: str = 'decompose item'
ELO_ATTENUATE_RATE: float = 0.5
ELO_DEFAULT: int = 1200
ELO_HALF_PERIOD: int = 2592000
ELO_MAX: int = 2600
ELO_MIN: int = 200
ELocalCurrencySource_FROM_ACCOUNT: int = 1
ELocalCurrencySource_FROM_AVATAR: int = 2
ELoginFailType_ABANDON: int = 14
ELoginFailType_ACCOUNT_RELAY: int = 2
ELoginFailType_ANTI_ADDICTION: int = 18
ELoginFailType_AVATAR_EXISTS: int = 17
ELoginFailType_BLOCKED_BY_ROLLSTUB: int = 12
ELoginFailType_CLIENT_CANCEL: int = 21
ELoginFailType_CREATE_AVATAR_FAILED: int = 9
ELoginFailType_CROSS_CREATE: int = 27
ELoginFailType_CallMethodInBadStatus: int = 3
ELoginFailType_DB_AVATAR_ID_INVALID: int = 26
ELoginFailType_DB_CENTER_DUMPLICATE_Error: int = 25
ELoginFailType_DB_CENTER_Error: int = 23
ELoginFailType_DB_EXTERNAL_HANDLER_Error: int = 24
ELoginFailType_DB_Error: int = 11
ELoginFailType_DB_LOCAL_Error: int = 22
ELoginFailType_DEVICE_IS_BANNED: int = 10
ELoginFailType_DEVICE_OS_ABANDOM: int = 28
ELoginFailType_HOSTNUM: int = 13
ELoginFailType_INVALID_AVATAR: int = 16
ELoginFailType_IS_MINOR: int = 20
ELoginFailType_NEWER_HOST_LOGIN: int = 19
ELoginFailType_QUERY_HOSTID_ERROR: int = 29
ELoginFailType_QUERY_HOSTID_INCONSISTENT: int = 30
ELoginFailType_SAUTH_DATA_ERROR: int = 5
ELoginFailType_SAUTH_ERROR: int = 15
ELoginFailType_SAUTH_FAILED: int = 7
ELoginFailType_SAUTH_NO_AID: int = 6
ELoginFailType_SAUTH_RETURN_NONE: int = 4
ELoginFailType_SELECT_WRONG_AVATAR: int = 8
ELoginFailType_SERVER_ERROR: int = 1
EMallSource_BuyMallItem: int = 2
EMallSource_BuyMallItems: int = 1
EMatchType_ALL_ACTIVE: tuple = (11, 1101, 1100, 1200, 1201, 1300, 1301, 1800, 1801, 1400, 1900, 1901)
EMatchType_ALL_Zombies: tuple = (1012, 1013, 1014)
EMatchType_BigHead: int = 1800
EMatchType_BigHead_WARM: int = 1801
EMatchType_GUNFIGHT: int = 1400
EMatchType_GrandTheft: int = 1700
EMatchType_GrandTheft_WARM: int = 1701
EMatchType_GrandThefts: tuple = (1700, 1701)
EMatchType_HOTSPOT: int = 1100
EMatchType_HOTSPOT_NEWER: int = 1101
EMatchType_Moba: int = 1004
EMatchType_MobaFirst: int = 1003
EMatchType_MobaFirstNew: int = 1001
EMatchType_Moba_Hard: int = 1500
EMatchType_Moba_LEISURE: int = 1006
EMatchType_Moba_NEWER: int = 1008
EMatchType_Moba_RANK_NEWER: int = 1002
EMatchType_Moba_RANK_WARM: int = 1005
EMatchType_Moba_WARM: int = 1007
EMatchType_Moba_ZOMBIE: int = 1012
EMatchType_Moba_ZOMBIE_LEISURE: int = 1014
EMatchType_Moba_ZOMBIE_WARM: int = 1013
EMatchType_ROOKIE_GUIDE: int = 14
EMatchType_ROOKIE_GUIDE_NEW: int = 100
EMatchType_Record: tuple = (1006, 1200, 1100, 1700, 1800, 1900)
EMatchType_SHOOT_RANGE: int = 11
EMatchType_SNIPE: int = 1900
EMatchType_SNIPE_NEWER: int = 1901
EMatchType_SQUADFIGHT: int = 1200
EMatchType_SQUADFIGHT_NEWER: int = 1201
EMatchType_SQUADFIGHT_RANK: int = 1300
EMatchType_SQUADFIGHT_RANK_WARM: int = 1301
EMatchType_UgcAll: int = 1000001
EMatchType_UgcEditor: int = 1000000
EMoneyItem_DICT: dict = {4000000010: 1, 4000000020: 2, 4000000040: 7}
EMoneyItem_DICT_NOR: dict = {4000000020: 4, 4000000010: 1, 4000000040: 7}
EMoneyItem_REVERSE_DICT: dict = {1: 4000000010, 2: 4000000020, 3: 4000000020, 4: 4000000020, 7: 4000000040}
EMoneyType_FREE_YUANBAO: int = 2
EMoneyType_HONOR: int = 1
EMoneyType_ITEM: int = 5
EMoneyType_LIMIT_YUANBAO: int = 6
EMoneyType_METAL: int = 7
EMoneyType_NONE: int = 0
EMoneyType_PAY_YUANBAO: int = 3
EMoneyType_YUANBAO: int = 4
ENTITY_DISSOLVING_TIME: float = 0.7
ERoomOp_CREATE: str = 'RoomOp_CREATE'
ERoomOp_DISMISS: str = 'RoomOp_DISMISS'
ERoomOp_JOIN: str = 'RoomOp_JOIN'
ERoomOp_KICKOUT: str = 'RoomOp_KICKOUT'
ERoomOp_LEAVE: str = 'RoomOp_LEAVE'
ERoomOp_UPDATE: str = 'RoomOp_UPDATE'
ERoomOp_UPDATE_ATTR: str = 'RoomOp_UPDATE_ATTR'
ERoomOp_UPDATE_MEMBER: str = 'RoomOp_UPDATE_MEMBER'
ERoomOp_UPDATE_OPTIONS: str = 'RoomOp_UPDATE_OPTIONS'
ETargetFilterSubType_ENEMY: int = 5
ETargetFilterSubType_ENEMY_AND_SELF: int = 1
ETargetFilterSubType_NOT_MYSELF: int = 6
ETargetFilterSubType_None: int = 0
ETargetFilterSubType_SELF: int = 3
ETargetFilterSubType_SELF_AND_TEAMMATES: int = 2
ETargetFilterSubType_TEAMMATES: int = 4
EWeaponPartOpticTypeSuffix: dict = {0: '_reddot', 1: '_reddot', 2: '_2x', 3: '_3x', 4: '_4x', 5: '_6x', 6: '_8x'}
EYuanBaoChangeType_MALL: int = 2
EYuanBaoChangeType_PAY: int = 1
EloType_To_MatchType: dict = {1100: (1100, 1101, 1200, 1201, 1800, 1801, 1900, 1901), 1004: (1004, 1005, 1012, 1013), 1006: (1006, 1007, 1008, 1500, 1014), 1700: (1700, 1701)}
FALL_HURT_DEATH_HEIGHT: int = 20
FALL_HURT_MAX_HURT_RATIO: float = 0.7
FALL_HURT_SPELL_ID: int = 18
FALL_HURT_START_HEIGHT: int = 8
FRIEND_WATCH_DELAY: int = 30
FinetuneBlueprintNum: int = 3
FinetuneTime: int = 3600
FriendRecentCount: int = 20
FullHp: float = 100.0
GACHA_DEFAULT_FREE_TIMES: dict = {1: 0, 10: 1}
GC_SERVER_HOST: str = '7.63.85.5:9873'
GENDER_FEMALE: int = 2
GENDER_MALE: int = 1
GLOBAL_AVATAR_INFO_FIELDS: tuple = ('_id', 'aid', 'name', 'db_hostnum', 'show_id')
GLOBAL_DATA_ROOM_DICT: str = 'RoomDict'
GLOBAL_DATA_ROOM_LIST: str = 'RoomList'
GMSDK_CUSTOMER: str = '/main/index'
GMSDK_SPRITE: str = '/sprite/index'
GRAND_THEFT_FUSION_WEIGHT_A: int = 1
GRAND_THEFT_GOAL_SCORE_MAX: int = 2000
GRAND_THEFT_GOAL_WEIGHT: float = 0.4
GRAND_THEFT_HISTORY_SCORE_MAX: int = 3400
GRAND_THEFT_INIT_ELO_LOWER_BOUND: int = 800
GRAND_THEFT_INIT_ELO_UPPER_BOUND: int = 2600
GRAND_THEFT_QUALIFYING_SCORE_DICT: dict = {1: 400, 2: 600, 3: 1000, 4: 1400, 5: 1900, 6: 2400, 7: 3000}
GUN_ACHIEVEMENT_ID_KILL: int = 38
GUN_ACHIEVEMENT_ID_KILL_HEADSHOT: int = 4
GUN_ACHIEVEMENT_ID_MAX_DAMAGE: int = 42
GUN_ACHIEVEMENT_ID_WIN: int = 40
GUN_BLUEPRINT_LIMIT: int = 4
GhostBackpackSlot: dict = {1001: {1}, 1002: {2}, 5003: {16}, 4001: {13}, 4002: {13}}
GunCostAmmos: dict = {1: 7, 2: 8, 3: 71, 5: 14, 4: 7, 6: 14, 7: 8, 8: 197}
GunSmithBackpackGunType: dict = {1001: (1, 2, 3, 4, 5, 6), 1002: (7, 8)}
HALL_SPACE_ID: int = 8
HIT_SOUND_MAX_DIST: float = 20.0
HOTFIX_PROPERTIES: tuple = ({'tag': 'common', 'path': 'hotfix.pyw', 'dir': '../client_hotfix', 'condition': <function <lambda> at 0x7040fe8900>}, {'tag': 'activity', 'path': 'hotfix.pyw', 'dir': '../client_hotfix_activity', 'condition': <function <lambda> at 0x7040fe89a0>}, {'tag': 'urgent', 'path': 'hotfix.pyw', 'dir': '../client_hotfix_urgent', 'condition': <function <lambda> at 0x7040fe8a40>}, {'tag': 'gray', 'path': '', 'dir': '', 'condition': <function <lambda> at 0x7040fe8ae0>}, {'tag': 'wanster', 'path': '', 'dir': '', 'condition': <function <lambda> at 0x7040fe8b80>})
HUNT_CONTRACT_ITEM_ID: int = 33
HeroFreeNum: int = 2
HeroFreeRefreshDay: int = 5
HiddenScoreParams: dict = {1004: [1, 1, 1200], 1006: [3, 0.4, 0], 1500: [3, 0.4, 0]}
High_Frequence_Avatar_Upload_Speed: int = 25
High_Frequence_PoseSender_Hz: int = 20
High_Frequence_Space_Hz: int = 30
HotspotTeamRobotBrains: dict = {1: ('HotspotFightBrain', 'HotspotProtectBrain'), 2: ('HotspotOccupyBrain', 'HotspotFightBrain'), 3: ('HotspotOccupyBrain', 'HotspotFightBrain', 'HotspotProtectBrain'), 4: ('HotspotOccupyBrain', 'HotspotOccupyBrain', 'HotspotFightBrain', 'HotspotProtectBrain'), 5: ('HotspotOccupyBrain', 'HotspotOccupyBrain', 'HotspotFightBrain', 'HotspotFightBrain', 'HotspotProtectBrain')}
IDLE_ROOM_PER_COUNT: int = 10
INNER_LBS_HOSTNUM: int = 12001
IPHONE_REWARD_STATUS_INIT: int = 0
IPHONE_REWARD_STATUS_MAIL: int = 2
IPHONE_REWARD_STATUS_WIN: int = 1
IS_PC_ISOLATION: bool = False
ITEM_QUALITY_MAX: int = 5
ITEM_QUALITY_MIN: int = 1
ItemDestroyDelay_DieDrop: int = 600
ItemDestroyDelay_Supply: int = 360
ItemSpecialExchangeList: list = [4100001160, 4100001320, 4100001720, 4100001850]
JumpType: tuple = (1, 8, 9, 10, 11, 'GunSkin', 'Item', 'hero')
LARGE_COINS_ITEM_ID: int = 19
LEGEND_MEDAL_ITEM_ID: int = 4100001360
LOCAL_TEST_LONG_HOSTING: bool = False
LanguageFilter2GuiLanguage: dict = {0: '', 1: 'zh', 2: 'en', 3: 'es', 4: 'pt', 5: 'ru', 6: 'ar', 7: 'in', 8: 'th', 9: 'vi', 10: 'ja'}
LanguageToCC: dict = {'zh': 'chs', 'en': 'eng', 'es': 'esp', 'pt': 'por', 'ru': 'rus', 'ar': 'ar'}
MAIL_MAX_COUNT: int = 300
MATCH_LEISURE_TO_RANK: dict = {1006: 1004, 1200: 1300}
MATCH_MAP_DEFAULT_OWN: int = 2
MATCH_MAP_TECHPARK: int = 8
MATCH_MAP_VALLEY: int = 2
MATCH_MAP_WAREHOUSE: int = 4
MATCH_STATUS_CANCEL_READY: int = 3
MATCH_STATUS_MATCHING: int = 4
MATCH_STATUS_NOT_READY: int = 1
MATCH_STATUS_READY: int = 2
MATCH_STATUS_START: int = 0
MATCH_STATUS_SUCCESS: int = 5
MAX_IDLE_ROOM_COUNT: int = 100
MAX_NAME_LENGTH_CN: int = 6
MAX_ROOM_COUNT: int = 5000
MAX_TEAM_MEMBER_COUNT: int = 4
MAX_TRACING_TASK_NUM: int = 5
MAX_WATCH_DELAY: int = 30
MIDDLE_COINS_ITEM_ID: int = 18
MINI_GUN_ID: int = 28
MINOR_HOST: str = 'sdk-os.mpsdk.easebar.com'
MOBA_WARM_TIMEOUT: int = 20
MatchSpaceMaxWaitTime: int = 240
MatchType_To_EloType: dict = {1100: 1100, 1101: 1100, 1200: 1100, 1201: 1100, 1800: 1100, 1801: 1100, 1900: 1100, 1901: 1100, 1004: 1004, 1005: 1004, 1012: 1004, 1013: 1004, 1006: 1006, 1007: 1006, 1008: 1006, 1500: 1006, 1014: 1006, 1700: 1700, 1701: 1700}
MatchType_To_TaskMatchType: dict = {1003: 1004, 1001: 1004, 1012: 1012, 1014: 1014, 1007: 1006, 1005: 1004, 1301: 1300, 1701: 1700, 1013: 1014, 1008: 1006, 1101: 1100, 1201: 1200, 1002: 1004, 1801: 1800, 1901: 1900}
MatchWinRankMap: dict = {1004: 1, 1006: 1}
Match_Newer_To_Normal: dict = {1008: 1006, 1101: 1100, 1201: 1200, 1002: 1004, 1801: 1800, 1901: 1900}
Match_Normal_To_Newer: dict = {1006: 1008, 1100: 1101, 1200: 1201, 1004: 1002, 1800: 1801, 1900: 1901}
Match_Normal_To_Warm: dict = {1006: 1007, 1004: 1005, 1300: 1301, 1700: 1701, 1012: 1013}
Match_Special_To_Normal: dict = {1003: 1004, 1001: 1004, 1012: 1004, 1014: 1006, 1007: 1006, 1005: 1004, 1301: 1300, 1701: 1700, 1013: 1004, 1008: 1006, 1101: 1100, 1201: 1200, 1002: 1004, 1801: 1800, 1901: 1900}
Match_Warm_To_Normal: dict = {1007: 1006, 1005: 1004, 1301: 1300, 1701: 1700, 1013: 1012}
MaxAdjustWaitTime: int = 240
MaxFinetuneSlotNum: int = 15
MobaBackpackSelectSlot: dict = {1: {11, 12}, 2: {14}, 3: {17}}
MobaBackpackSlot: dict = {1001: {1, 4}, 1002: {1, 4}, 1004: {3}, 1003: {2}, 1005: {5}, 5003: {16}, 4001: {13}, 4002: {13}, 4003: {23}, 7001: {17}, 7002: {17}, 3001: {11, 12}, 3002: {11, 12}, 8001: {19}, 8002: {22}, 5004: {20}}
MobaEquipmentSuitableSlots: dict = {1: [1001, 1002], 4: [1001, 1002], 3: [1004], 2: [1003], 5: [1005], 16: [5003], 13: [4001, 4002], 23: [4003], 17: [7001, 7002], 11: [3001, 3002], 12: [3001, 3002], 19: [8001], 22: [8002], 20: [5004]}
MobaNearRebornTime: float = 5.0
MoneyType_2_Str: dict = {2: 'free_yuanbao', 3: 'pay_yuanbao', 1: 'honor', 6: 'limit_yuanbao', 7: 'metal'}
NEW_MALL_PROTO_TIME: str = '2024-08-01 00:00:00'
NORMAL_BACKPAK_CAPACITY: int = 0
NORMAL_EMOTE_HERO_ID: int = 18
NormalBackpackSelectSlot: dict = {1: {18, 11, 12}, 2: {14}, 3: {17}}
NormalBackpackSlot: dict = {1001: {1}, 1002: {1}, 1004: {3}, 1003: {2}, 1005: {5}, 3001: {11, 12}, 3002: {11, 12}, 5002: {15}, 4001: {13}, 4002: {13}, 4003: {23}}
NormalBornSkills: set = {(9, 1)}
NormalEquipmentSuitableSlots: dict = {1: [1001, 1002], 3: [1004], 2: [1003], 5: [1005], 11: [3001, 3002], 12: [3001, 3002], 15: [5002], 13: [4001, 4002], 23: [4003]}
NotShowDecomposeTypes: list = ['gacha']
OCCUPY_CONTRACT_ITEM_ID: int = 34
OwnerRecentCount: int = 10
PACKAGE_TYPE_NETEASE_ABROAD: int = 2
PACKAGE_TYPE_NETEASE_GLOBAL: int = 3
PACKAGE_TYPE_NETEASE_MAINLAND: int = 1
PACKAGE_TYPE_NETEASE_TAIWAN: int = 4
PACKAGE_TYPE_UNDEFINED: int = 0
PARACHUTE_CHECK_ACTIVE_TIME: float = 2.0
PARACHUTE_INVITE_TIME: int = 10
PAY_ORDER_CHECK_FAILED: int = 100
PAY_SDK_CHECK_OK: int = 2
PENETRATE_MATERIAL_TYPE_ID_DAMAGE_CHANGE: dict = {7: 0.2}
PHYSICS_BULLET: int = 23
PHYSICS_CHARCTRL: int = 30
PHYSICS_COMMON_OBSTACLE: int = 2
PHYSICS_DROP_ITEM: int = 24
PHYSICS_GHOST: int = 1
PHYSICS_NOTHING: int = 0
PHYSICS_SHOOT_TEST: int = 19
PHYSICS_SHOOT_VERIFY: int = 16
PHYSICS_VEHICLE: int = 27
PLAYER_CHARCTRL_HALFHEIGHT: float = 0.4
PLAYER_CHARCTRL_RADIUS: float = 0.5
PLAYER_INFO_SETTING_ITEM_SUB_TYPES: tuple = (603, 607, 608, 611)
POSE_RECEIVER_INTERVAL: float = 0.1
POSE_SENDER_INTERVAL: float = 0.095
PRIVILEGE_ALL: int = 3
PRIVILEGE_BLACK: int = 0
PRIVILEGE_FRIEND: int = 2
PRIVILEGE_SELF: int = 1
PlayerIdentityRichText: dict = {1: '#o(anchor%s)', 2: '#o(creator%s)', 3: '#o(staff%s)'}
QualifyingHallMatchTypes: tuple = (1004, 1300)
RANDOM_CLOTHES_LIST: list = [{310: 300007, 320: 310000, 330: 350001}, {310: 300025, 320: 310000, 330: 350008}]
RENAME_CD_TIME: int = 172800
REPLAY_CLIENT_USE_HOST: str = '45.253.178.142:9872'
REPLAY_SERVER_USE_HOST: str = '7.63.85.5:9872'
REQUIRE_PACKAGE_MIN_VERSION: int = 173731
RESERVE_TIMEOUT: int = 3
ROBOT_CONTROL_CD: float = 2.0
ROBOT_FAR_DST: int = 100
ROBOT_FREE_COUNT: int = 4
ROBOT_FULL_COUNT: int = 6
ROBOT_LOSE_CLIENT_TIME: float = 2.0
ROBOT_MIDDLE_DST: int = 50
ROBOT_NEAR_DST: int = 20
ROOM_DESTROY_TIME: int = 3600
ROOM_WATCH_DELAY: int = 3
SAFE_REGION_ABTEST_HOSTNUMS: list = []
SEARCH_CONTRACT_ITEM_ID: int = 35
SEC_DAY: int = 86400
SEC_HOUR: int = 3600
SEC_MINUTE: int = 60
SEC_WEEK: int = 604800
SETTING_SHARE_REGION_NAME: dict = {12001: 'ASIA', 10001: 'NA/SA', 14001: 'EU'}
SETTLE_TAG_GUARD_ANGEL: int = 2
SETTLE_TAG_KILL_TOGETHER: int = 5
SETTLE_TAG_LONG_RUN: int = 7
SETTLE_TAG_OVER_EIGHT_KILL: int = 1
SETTLE_TAG_OVER_THREE_KILL: int = 3
SETTLE_TAG_PICK_GOLD: int = 6
SETTLE_TAG_SAVE_OTHERS: int = 4
SMALL_COINS_ITEM_ID: int = 17
SUPER_COINS_ITEM_ID: int = 36
SUPPORT_FAST_BUY_LIMIT: int = 10
ServerMigrateFields: list = ['level', 'exp', 'pay_yuanbao', 'free_yuanbao', 'record_yuanbao', 'record_free_yuanbao', 'record_pay_yuanbao', 'warehouse']
TAGS: tuple = ('IsAvatar', 'IsCombatAvatar', 'IsPlayerCombatAvatar', 'IsIgnoreCue', 'IsVehicle', 'IsGameLogic', 'IsBomb', 'IsMagicField', 'IsSimpleCombatUnit', 'IsCombatUnit', 'IsReplayRecorder', 'IsItem', 'IsItemSpaceSnare', 'is_fps_avatar', 'is_replay_avatar', 'is_replay_room', 'IsOccupyContractTarget', 'IsOccupyContractTargetNew', 'IsSearchContractBox', 'IsAmmoBox', 'IsSystemKiller', 'IsBuilding', 'IsSupply', 'IsGlass', 'IsAirDrop', 'IsVirtualInteractionEntity', 'IsDummyCombatAvatar', 'IsRobotCombatAvatar', 'IsPhyBall', 'IsHolographicRobot', 'IsShield', 'IsShop', 'IsCombatTeam', 'IsCureUav', 'IsCureUavFix', 'IsContrabandPlane', 'NinjaBeacon', 'IsEntityAttach', 'IsEntityMaster', 'IsMovingPlatform', 'IsBarrieCannon', 'IsRPGMissile', 'IsOilbox', 'IsArrow', 'IsStickyMaster', 'IsHelenAI', 'IsIceWall', 'IsCrow', 'IsStronghold', 'IsObserveAvatar', 'IsPlayerObserveAvatar', 'IsDestructible', 'IsMonster', 'IsCrack', 'IsEmoteTree', 'IsReplayPuppet', 'IsEnergyStronghold', 'IsSafeBox', 'IsStropUav', 'IsChaosUav', 'IsPortableShop', 'IsSaveMachine', 'IsSaveDrone', 'IsATM', 'IsAttackDrone', 'IsATMGuardAI', 'IsScoutArrow', 'IsRobotCombatAvatarZombie', 'IsCombatAvatarZombieXray', 'IsSwordSpirit', 'IsSyncTransEntity', 'IsSpellDrone', 'IsMonitorMissile', 'IsCombatAvatarSniper')
TALENT_ACTIVE_TIME: int = 300
TALENT_SLOT_INDEX: dict = {0: (1, 2, 3, 4, 5, 6), 1: (7,)}
THROWABLE_WEAPON_TALENT_ADDED: int = 1
TPS_AVATAR_MODEL_SCALE: float = 1.1
TRACE_SERVER_HOST: str = '10.90.56.231:9871'
UNIT_STATE_CLIMB: str = 'Climb'
UNIT_STATE_CLIMB_LADDER: str = 'ClimbLadder'
UNIT_STATE_CLOSE_PARACHUTE: str = 'CloseParachute'
UNIT_STATE_CROSS: str = 'Cross'
UNIT_STATE_CROUCH: str = 'Crouch'
UNIT_STATE_DEAD: str = 'Dead'
UNIT_STATE_DRIVE_VEHICLE: str = 'DriveVehicle'
UNIT_STATE_DROPWEAPON: str = 'DropWeapon'
UNIT_STATE_ENTER_PRONE: str = 'EnterProne'
UNIT_STATE_EXIT_PRONE: str = 'ExitProne'
UNIT_STATE_FIRE: str = 'Fire'
UNIT_STATE_FREEFALL: str = 'FreeFall'
UNIT_STATE_IDLE: str = 'Idle'
UNIT_STATE_JOG: str = 'Jog'
UNIT_STATE_JUMP: str = 'Jump'
UNIT_STATE_KICK_UP: str = 'KickUp'
UNIT_STATE_KNOCK_DOWN: str = 'KnockDown'
UNIT_STATE_LANDGROUND: str = 'LandGround'
UNIT_STATE_ON_AIRCRAFT: str = 'OnAircraft'
UNIT_STATE_ON_VEHICLE: str = 'OnVehicle'
UNIT_STATE_OPEN_FIRE_FREEFALL: str = 'FreeFallOpenFire'
UNIT_STATE_OPEN_PARACHUTE: str = 'OpenParachute'
UNIT_STATE_PARACHUTE: str = 'Parachute'
UNIT_STATE_PASSIVEFLY: str = 'PassiveFly'
UNIT_STATE_PICKUP: str = 'PickUp'
UNIT_STATE_PRONE: str = 'Prone'
UNIT_STATE_RAISELEFTHANDWEAPON: str = 'RaiseLeftHandWeapon'
UNIT_STATE_RAISEWEAPON: str = 'RaiseWeapon'
UNIT_STATE_RECHAMBER: str = 'Rechamber'
UNIT_STATE_RELOAD: str = 'Reload'
UNIT_STATE_RESCUE: str = 'RescueOther'
UNIT_STATE_SAMURAI_SPRINT: str = 'SamuraiSprint'
UNIT_STATE_SLIDE: str = 'Slide'
UNIT_STATE_SPELL: str = 'Spell'
UNIT_STATE_SPRINT: str = 'Sprint'
UNIT_STATE_STAND: str = 'Stand'
UNIT_STATE_STROP: str = 'Strop'
UNIT_STATE_SUPERSPRINT: str = 'SuperSprint'
UNIT_STATE_SWIM: str = 'Swim'
UNIT_STATE_WALK: str = 'Walk'
UNLOCK_QUALIFYING_LEVEL: int = 1
UNLOCK_RECRUIT_LEVEL: int = 5
UNLOCK_WORLD_CHAT_LEVEL: int = 5
USE_NEW_SERVER_CLIENT_CHANGE_CONTROL: bool = True
USE_SERVER_BIN_DATA: bool = True
VEHICLE_TYPE_CAR: int = 1
VEHICLE_TYPE_HELICOPTER: int = 4
VEHICLE_TYPE_MOTOR2: int = 2
VEHICLE_TYPE_MOTOR3: int = 3
WeaponPartModelTachPoint: dict = {1: '', 2: 'HP_barrel_attach', 3: 'HP_acog', 4: 'HP_stock_attach', 5: 'HP_mag_attach', 6: 'HP_pistolgrip_attach', 7: 'HP_grip_attach', 8: 'HP_tip', 9: 'HP_laser_attach', 10: 'HP_trigger', 11: '', 12: 'HP_hammer'}
WeaponPartParentType: dict = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 2, 8: 2, 9: 2, 10: 1, 11: 1, 12: 1}
WeaponPartTypeDataKeyInt: dict = {'recevier': 1, 'barrel': 2, 'optic': 3, 'stock': 4, 'ammunition': 5, 'reargrip': 6, 'under_barrel': 7, 'muzzle': 8, 'laser': 9, 'trigger': 10, 'bullet': 11, 'action': 12}
WeaponPartTypeDataKeyStr: dict = {1: 'recevier', 2: 'barrel', 3: 'optic', 4: 'stock', 5: 'ammunition', 6: 'reargrip', 7: 'under_barrel', 8: 'muzzle', 9: 'laser', 10: 'trigger', 11: 'bullet', 12: 'action'}
WeaponPartTypeNeedMutex: tuple = (8, 7, 6, 12)
WeaponPartTypeShowSequence: list = [1, 8, 2, 7, 3, 4, 5, 6, 9, 10, 11, 12]
WeaponPartTypeShowSequenceBackpack: list = [8, 2, 7, 3, 4, 5]
WeaponPartTypeShowSequenceBackpackMaxLength: int = 8
WeaponPartType_Action: int = 12
WeaponPartType_Ammunition: int = 5
WeaponPartType_Barrel: int = 2
WeaponPartType_Bullet: int = 11
WeaponPartType_Laser: int = 9
WeaponPartType_Muzzle: int = 8
WeaponPartType_Optic: int = 3
WeaponPartType_Reargrip: int = 6
WeaponPartType_Recevier: int = 1
WeaponPartType_Stock: int = 4
WeaponPartType_Trigger: int = 10
WeaponPartType_Underbarrel: int = 7
WildShopGunSortedDict: dict = {1: 1, 2: 2, 5: 3, 3: 4}
WildShopItemTypeWideList: list = [1, 2, 3]
YEAR_REVIEW_NEW_PLAYER_TIME: str = '2024-12-01 00:00:00'
ZOMBIE_BUFF_MAX_LV: int = 5
ZOMBIE_CRYSTAL_ITEM_ID: int = 308
ZOMBIE_CRYSTAL_SWORD_ITEM_ID: int = 272
ZOMBIE_CRYSTAL_SWORD_SKILL_ITEM_ID: int = 273
ZOMBIE_HERO_ID: int = 998
ZOMBIE_HP_PER_LEVEL: float = 25.0
ZOMBIE_RECOVER_ITEM_ID: int = 417
ZONE_PART_CAREER: int = 2
ZONE_PART_EQUIPMENT: int = 3
ZONE_PART_SEASON: int = 1
_TIME_ZONE: NoneType = None
beijing_tz: BeijingTZ = <gshare.consts.BeijingTZ object at 0x7040c6f5d0>
elo_type: int = 1700
factor_a: float = 1.02
factor_r: float = 1.02
match_type: int = 1701
match_types: tuple = (1700, 1701)

class AIEventType(enum):
    ON_BE_INJURED: int = 1
    ON_ENEMY_ENTER_VIEW: int = 2
    ON_ENEMY_LEAVE_VIEW: int = 3
    ON_GAME_SOUND: int = 4
    name_to_values: dict = {'ON_BE_INJURED': 1, 'ON_ENEMY_ENTER_VIEW': 2, 'ON_ENEMY_LEAVE_VIEW': 3, 'ON_GAME_SOUND': 4}
    value_to_names: dict = {1: 'ON_BE_INJURED', 2: 'ON_ENEMY_ENTER_VIEW', 3: 'ON_ENEMY_LEAVE_VIEW', 4: 'ON_GAME_SOUND'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class AISourceType(enum):
    AISourceBind: int = 2
    AISourceParachute: int = 0
    AISourceWander: int = 1
    AISourceWarmType1: int = 11
    AISourceWarmType2: int = 12
    AISourceWarmType3: int = 13
    AISourceWarmType4: int = 14
    AISourceWarmType5: int = 15
    AISourceWarmType6: int = 16
    AISourceWarmType7: int = 17
    name_to_values: dict = {'AISourceParachute': 0, 'AISourceWander': 1, 'AISourceBind': 2, 'AISourceWarmType1': 11, 'AISourceWarmType2': 12, 'AISourceWarmType3': 13, 'AISourceWarmType4': 14, 'AISourceWarmType5': 15, 'AISourceWarmType6': 16, 'AISourceWarmType7': 17}
    value_to_names: dict = {0: 'AISourceParachute', 1: 'AISourceWander', 2: 'AISourceBind', 11: 'AISourceWarmType1', 12: 'AISourceWarmType2', 13: 'AISourceWarmType3', 14: 'AISourceWarmType4', 15: 'AISourceWarmType5', 16: 'AISourceWarmType6', 17: 'AISourceWarmType7'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ActionSource(object):
    Client: int = 1
    Server: int = 0

class ActionTag(object):
    BATTLE: int = 2
    Hall: int = 1
    Replay: int = 3

class ActionType(object):
    ServerBind: int = 6
    ServerEnterBattle: int = 3
    ServerEnterHall: int = 2
    ServerLogin: int = 1
    ServerReplayFinish: int = 5
    ServerReplayStart: int = 4

class AdditionType(enum):
    AvatarExpCard: int = 1
    FreeExpCard: int = 4
    GunExpCard: int = 3
    Team: int = 2
    name_to_values: dict = {'AvatarExpCard': 1, 'Team': 2, 'GunExpCard': 3, 'FreeExpCard': 4}
    value_to_names: dict = {1: 'AvatarExpCard', 2: 'Team', 3: 'GunExpCard', 4: 'FreeExpCard'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class AirDropShopCategories(enum):
    BuyTeammate: int = 999
    CombatSupport: int = 1
    MapSupport: int = 4
    SpecialEquip: int = 2
    Vehicle: int = 3
    name_to_values: dict = {'CombatSupport': 1, 'SpecialEquip': 2, 'Vehicle': 3, 'MapSupport': 4, 'BuyTeammate': 999}
    value_to_names: dict = {1: 'CombatSupport', 2: 'SpecialEquip', 3: 'Vehicle', 4: 'MapSupport', 999: 'BuyTeammate'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class AirdropPostType(enum):
    FREQUENT: int = 2
    NORMAL: int = 1
    NULL: int = 0
    name_to_values: dict = {'NULL': 0, 'NORMAL': 1, 'FREQUENT': 2}
    value_to_names: dict = {0: 'NULL', 1: 'NORMAL', 2: 'FREQUENT'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class AnchorType(enum):
    COPPER: int = 1
    GOLD: int = 3
    SILVER: int = 2
    name_to_values: dict = {'GOLD': 3, 'SILVER': 2, 'COPPER': 1}
    value_to_names: dict = {3: 'GOLD', 2: 'SILVER', 1: 'COPPER'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class AssistAimModeConfig(enum):
    Expert: int = 3
    Newer: int = 2
    No: int = 1
    name_to_values: dict = {'No': 1, 'Newer': 2, 'Expert': 3}
    value_to_names: dict = {1: 'No', 2: 'Newer', 3: 'Expert'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class AudioSessionRoute(object):
    Amplifier: int = 0
    HeadPhone: int = 1

class AuthBindName(enum):
    APPLE: str = 'apple'
    DISCORD: str = 'discord'
    FACEBOOK: str = 'facebook'
    GOOGLE: str = 'google'
    GUEST: str = 'guest'
    LINE: str = 'line'
    STEAM: str = 'steam'
    TIKTOK: str = 'tiktok'
    TWITTER_X: str = 'twitter'
    VK: str = 'vk'
    name_to_values: dict = {'GUEST': 'guest', 'FACEBOOK': 'facebook', 'GOOGLE': 'google', 'TWITTER_X': 'twitter', 'APPLE': 'apple', 'TIKTOK': 'tiktok', 'DISCORD': 'discord', 'VK': 'vk', 'LINE': 'line', 'STEAM': 'steam'}
    value_to_names: dict = {'guest': 'GUEST', 'facebook': 'FACEBOOK', 'google': 'GOOGLE', 'twitter': 'TWITTER_X', 'apple': 'APPLE', 'tiktok': 'TIKTOK', 'discord': 'DISCORD', 'vk': 'VK', 'line': 'LINE', 'steam': 'STEAM'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class AvatarExpSource(enum):
    DAILY_TASK: int = 2
    FINISH_GAME: int = 1
    USE_EXP_ITEM: int = 3
    name_to_values: dict = {'FINISH_GAME': 1, 'DAILY_TASK': 2, 'USE_EXP_ITEM': 3}
    value_to_names: dict = {1: 'FINISH_GAME', 2: 'DAILY_TASK', 3: 'USE_EXP_ITEM'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class AvatarHeadType(enum):
    ITEM: int = 1
    URL: int = 2
    name_to_values: dict = {'ITEM': 1, 'URL': 2}
    value_to_names: dict = {1: 'ITEM', 2: 'URL'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class AvatarLoginBanType(enum):
    AccountMigrate: int = 6
    AntiCheat: int = 1
    ChatUnlaw: int = 5
    CheatTeam: int = 2
    Defalut: int = 0
    DeviceCheat: int = 7
    JoinCheat: int = 3
    MaliciousRefund: int = 8
    MouseCheat: int = 4
    name_to_values: dict = {'Defalut': 0, 'AntiCheat': 1, 'CheatTeam': 2, 'JoinCheat': 3, 'MouseCheat': 4, 'ChatUnlaw': 5, 'AccountMigrate': 6, 'DeviceCheat': 7, 'MaliciousRefund': 8}
    value_to_names: dict = {0: 'Defalut', 1: 'AntiCheat', 2: 'CheatTeam', 3: 'JoinCheat', 4: 'MouseCheat', 5: 'ChatUnlaw', 6: 'AccountMigrate', 7: 'DeviceCheat', 8: 'MaliciousRefund'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class BackpackSelectSlot(enum):
    MEDICINE: int = 3
    NONE: int = 0
    SUPPORT_WEAPON: int = 2
    TACTICAL_WEAPON: int = 1
    name_to_values: dict = {'NONE': 0, 'TACTICAL_WEAPON': 1, 'SUPPORT_WEAPON': 2, 'MEDICINE': 3}
    value_to_names: dict = {0: 'NONE', 1: 'TACTICAL_WEAPON', 2: 'SUPPORT_WEAPON', 3: 'MEDICINE'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class BackpackSlot(enum):
    ARMOR_PIECE: int = 5002
    CRACK_SCANNER: int = 5004
    EMERGENCY_NEEDLE: int = 5003
    FAKE_SLOT_1: int = 8001
    FAKE_SLOT_2: int = 8002
    LAUNCHER_WEAPON: int = 1005
    MEDICINE_1: int = 7001
    MEDICINE_2: int = 7002
    NONE: int = 0
    SKILL_WEAPON: int = 4001
    SKILL_WEAPON2: int = 4002
    SKILL_WEAPON3: int = 4003
    SUPPORT_WEAPON: int = 5001
    TACTICAL_WEAPON_1: int = 3001
    TACTICAL_WEAPON_2: int = 3002
    TALENT_1: int = 6001
    TALENT_2: int = 6002
    VICE_WEAPON: int = 1003
    WEAPON_1: int = 1001
    WEAPON_2: int = 1002
    WEAPON_3: int = 1004
    name_to_values: dict = {'NONE': 0, 'WEAPON_1': 1001, 'WEAPON_2': 1002, 'WEAPON_3': 1004, 'VICE_WEAPON': 1003, 'LAUNCHER_WEAPON': 1005, 'TACTICAL_WEAPON_1': 3001, 'TACTICAL_WEAPON_2': 3002, 'SKILL_WEAPON': 4001, 'SKILL_WEAPON2': 4002, 'SKILL_WEAPON3': 4003, 'SUPPORT_WEAPON': 5001, 'ARMOR_PIECE': 5002, 'EMERGENCY_NEEDLE': 5003, 'CRACK_SCANNER': 5004, 'MEDICINE_1': 7001, 'MEDICINE_2': 7002, 'TALENT_1': 6001, 'TALENT_2': 6002, 'FAKE_SLOT_1': 8001, 'FAKE_SLOT_2': 8002}
    value_to_names: dict = {0: 'NONE', 1001: 'WEAPON_1', 1002: 'WEAPON_2', 1004: 'WEAPON_3', 1003: 'VICE_WEAPON', 1005: 'LAUNCHER_WEAPON', 3001: 'TACTICAL_WEAPON_1', 3002: 'TACTICAL_WEAPON_2', 4001: 'SKILL_WEAPON', 4002: 'SKILL_WEAPON2', 4003: 'SKILL_WEAPON3', 5001: 'SUPPORT_WEAPON', 5002: 'ARMOR_PIECE', 5003: 'EMERGENCY_NEEDLE', 5004: 'CRACK_SCANNER', 7001: 'MEDICINE_1', 7002: 'MEDICINE_2', 6001: 'TALENT_1', 6002: 'TALENT_2', 8001: 'FAKE_SLOT_1', 8002: 'FAKE_SLOT_2'}

    def IsSkill(slot): ...
    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class BeijingTZ(tzinfo):
    fromutc: method_descriptor = <method 'fromutc' of 'datetime.tzinfo' objects>

    def dst(self, dt): ...
    def tzname(self, dt): ...
    def utcoffset(self, dt): ...

class BombMode(enum):
    NEW_MODE: int = 2
    NORMAL: int = 1
    name_to_values: dict = {'NORMAL': 1, 'NEW_MODE': 2}
    value_to_names: dict = {1: 'NORMAL', 2: 'NEW_MODE'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class BoxMatcher(object):
    def Calc(self, pos): ...
    def Check(self, pos, extra_threshold=0): ...

class BuffType(enum):
    NEGATIVE: int = 2
    OTHER: int = 3
    POSITIVE: int = 1
    name_to_values: dict = {'POSITIVE': 1, 'NEGATIVE': 2, 'OTHER': 3}
    value_to_names: dict = {1: 'POSITIVE', 2: 'NEGATIVE', 3: 'OTHER'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ClientDeviceInput(enum):
    GAMEPAD: int = 4
    KBM: int = 1
    TOUCH: int = 2
    name_to_values: dict = {'KBM': 1, 'TOUCH': 2, 'GAMEPAD': 4}
    value_to_names: dict = {1: 'KBM', 2: 'TOUCH', 4: 'GAMEPAD'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CoinResoure(enum):
    CONTRACT_REWARD: int = 1
    COST_DROP: int = 7
    COST_SHOP: int = 5
    COST_SUPPORT: int = 4
    COST_SYSTEM: int = 6
    DEFAULT: int = 0
    ENTER_COINS: int = 21
    FEED_BACK_REWARD: int = 2
    PICK_UP: int = 3
    PICK_UP_AIRDROP: int = 14
    PICK_UP_ATM: int = 13
    PICK_UP_BOX: int = 10
    PICK_UP_DEAD_BOX: int = 11
    PICK_UP_DROP: int = 12
    PICK_UP_WILD: int = 9
    REBORN_REWARD: int = 8
    SAVE_COINS: int = 20
    name_to_values: dict = {'DEFAULT': 0, 'CONTRACT_REWARD': 1, 'FEED_BACK_REWARD': 2, 'PICK_UP': 3, 'COST_SUPPORT': 4, 'COST_SHOP': 5, 'COST_SYSTEM': 6, 'COST_DROP': 7, 'REBORN_REWARD': 8, 'PICK_UP_WILD': 9, 'PICK_UP_BOX': 10, 'PICK_UP_DEAD_BOX': 11, 'PICK_UP_DROP': 12, 'PICK_UP_ATM': 13, 'PICK_UP_AIRDROP': 14, 'SAVE_COINS': 20, 'ENTER_COINS': 21}
    value_to_names: dict = {0: 'DEFAULT', 1: 'CONTRACT_REWARD', 2: 'FEED_BACK_REWARD', 3: 'PICK_UP', 4: 'COST_SUPPORT', 5: 'COST_SHOP', 6: 'COST_SYSTEM', 7: 'COST_DROP', 8: 'REBORN_REWARD', 9: 'PICK_UP_WILD', 10: 'PICK_UP_BOX', 11: 'PICK_UP_DEAD_BOX', 12: 'PICK_UP_DROP', 13: 'PICK_UP_ATM', 14: 'PICK_UP_AIRDROP', 20: 'SAVE_COINS', 21: 'ENTER_COINS'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CombatItemAmmo(enum):
    AR: int = 7
    MR: int = 14
    NONE: int = 0
    RPG: int = 197
    SG: int = 71
    SMG: int = 8
    name_to_values: dict = {'NONE': 0, 'AR': 7, 'SMG': 8, 'MR': 14, 'SG': 71, 'RPG': 197}
    value_to_names: dict = {0: 'NONE', 7: 'AR', 8: 'SMG', 14: 'MR', 71: 'SG', 197: 'RPG'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CombatItemBlowType(enum):
    Drop: int = 2
    Supply: int = 1
    name_to_values: dict = {'Supply': 1, 'Drop': 2}
    value_to_names: dict = {1: 'Supply', 2: 'Drop'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CombatItemId(enum):
    EMERGENCY_NEEDLE: int = 16
    name_to_values: dict = {'EMERGENCY_NEEDLE': 16}
    value_to_names: dict = {16: 'EMERGENCY_NEEDLE'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CombatItemTalentType(enum):
    RANDOME: tuple = (1,)
    SPEICAL: tuple = (2,)
    name_to_values: dict = {'RANDOME': (1,), 'SPEICAL': (2,)}
    value_to_names: dict = {(1,): 'RANDOME', (2,): 'SPEICAL'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CombatItemType(enum):
    AIRDROP: int = 104
    AMMO: int = 102
    AMMOBAG: int = 115
    AMMO_SUPPLEMENT: int = 113
    ARMOR_UPGRADE: int = 118
    BLOOD_CRYSTAL: int = 117
    BOX: int = 103
    BROKEN_TALENT_CORE: int = 112
    COIN: int = 105
    CONTRACT: int = 107
    EQUIP: int = 101
    GENECODE: int = 109
    NONE: int = 0
    RANDOM_TALENT: int = 110
    REBORN_CHANCE: int = 108
    SHUTTER_CLUE: int = 120
    SKILL_UPGRADE: int = 119
    TACTICAL_CORE: int = 111
    TACTICAL_ENERGY: int = 116
    TALENT: int = 106
    TROPHIES: int = 114
    name_to_values: dict = {'NONE': 0, 'EQUIP': 101, 'AMMO': 102, 'BOX': 103, 'AIRDROP': 104, 'COIN': 105, 'TALENT': 106, 'CONTRACT': 107, 'REBORN_CHANCE': 108, 'GENECODE': 109, 'RANDOM_TALENT': 110, 'TACTICAL_CORE': 111, 'BROKEN_TALENT_CORE': 112, 'AMMO_SUPPLEMENT': 113, 'TROPHIES': 114, 'AMMOBAG': 115, 'TACTICAL_ENERGY': 116, 'BLOOD_CRYSTAL': 117, 'ARMOR_UPGRADE': 118, 'SKILL_UPGRADE': 119, 'SHUTTER_CLUE': 120}
    value_to_names: dict = {0: 'NONE', 101: 'EQUIP', 102: 'AMMO', 103: 'BOX', 104: 'AIRDROP', 105: 'COIN', 106: 'TALENT', 107: 'CONTRACT', 108: 'REBORN_CHANCE', 109: 'GENECODE', 110: 'RANDOM_TALENT', 111: 'TACTICAL_CORE', 112: 'BROKEN_TALENT_CORE', 113: 'AMMO_SUPPLEMENT', 114: 'TROPHIES', 115: 'AMMOBAG', 116: 'TACTICAL_ENERGY', 117: 'BLOOD_CRYSTAL', 118: 'ARMOR_UPGRADE', 119: 'SKILL_UPGRADE', 120: 'SHUTTER_CLUE'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CombatState(enum):
    ALIVE: int = 0
    DEAD: int = 2
    DYING: int = 1
    GHOST: int = 3
    NONE: int = 4
    name_to_values: dict = {'ALIVE': 0, 'DYING': 1, 'DEAD': 2, 'GHOST': 3, 'NONE': 4}
    value_to_names: dict = {0: 'ALIVE', 1: 'DYING', 2: 'DEAD', 3: 'GHOST', 4: 'NONE'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CombatUnitType(enum):
    AttackDrone: int = 7
    Cannon: int = 5
    CureDrone: int = 6
    GasTank: int = 4
    Normal: int = 0
    OilBox: int = 8
    SatellitePlaceItem: int = 3
    Shield: int = 2
    ShieldBase: int = 1
    name_to_values: dict = {'Normal': 0, 'ShieldBase': 1, 'Shield': 2, 'SatellitePlaceItem': 3, 'GasTank': 4, 'Cannon': 5, 'CureDrone': 6, 'AttackDrone': 7, 'OilBox': 8}
    value_to_names: dict = {0: 'Normal', 1: 'ShieldBase', 2: 'Shield', 3: 'SatellitePlaceItem', 4: 'GasTank', 5: 'Cannon', 6: 'CureDrone', 7: 'AttackDrone', 8: 'OilBox'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CommonItemUnlockType(enum):
    BP: int = 1
    Task: int = 2
    name_to_values: dict = {'BP': 1, 'Task': 2}
    value_to_names: dict = {1: 'BP', 2: 'Task'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CompleteType(enum):
    HUNT_BY_OTHER: int = 2
    SUCCESS: int = 1
    name_to_values: dict = {'SUCCESS': 1, 'HUNT_BY_OTHER': 2}
    value_to_names: dict = {1: 'SUCCESS', 2: 'HUNT_BY_OTHER'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CylinderMatcher(object):
    def Calc(self, pos): ...
    def Check(self, pos, extra_threshold=0): ...

class DeviceType(enum):
    Mobile: int = 1
    PC: int = 2
    name_to_values: dict = {'Mobile': 1, 'PC': 2}
    value_to_names: dict = {1: 'Mobile', 2: 'PC'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class DroneFlag(enum):
    Destroyed: int = 7
    DropRope: int = 2
    FlyIn: int = 1
    FlyOut: int = 6
    Init: int = 0
    PackRope: int = 5
    Saved: int = 4
    Saving: int = 3
    name_to_values: dict = {'Init': 0, 'FlyIn': 1, 'DropRope': 2, 'Saving': 3, 'Saved': 4, 'PackRope': 5, 'FlyOut': 6, 'Destroyed': 7}
    value_to_names: dict = {0: 'Init', 1: 'FlyIn', 2: 'DropRope', 3: 'Saving', 4: 'Saved', 5: 'PackRope', 6: 'FlyOut', 7: 'Destroyed'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class EPlatform(enum):
    Android: str = 'android'
    IOS: str = 'ios'
    Macos: str = 'macos'
    Orbis: str = 'orbis'
    Switch: str = 'switch'
    Windows: str = 'windows'
    name_to_values: dict = {'IOS': 'ios', 'Android': 'android', 'Windows': 'windows', 'Switch': 'switch', 'Orbis': 'orbis', 'Macos': 'macos'}
    value_to_names: dict = {'ios': 'IOS', 'android': 'Android', 'windows': 'Windows', 'switch': 'Switch', 'orbis': 'Orbis', 'macos': 'Macos'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class EntityCreateType(enum):
    DissolveScale: int = 1
    Show: int = 2
    name_to_values: dict = {'DissolveScale': 1, 'Show': 2}
    value_to_names: dict = {1: 'DissolveScale', 2: 'Show'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class EntityDestroyType(enum):
    BreakAndDissolving: int = 2
    Delay: int = 1
    Dissolving: int = 3
    HideAndDelay: int = 0
    name_to_values: dict = {'HideAndDelay': 0, 'Delay': 1, 'BreakAndDissolving': 2, 'Dissolving': 3}
    value_to_names: dict = {0: 'HideAndDelay', 1: 'Delay', 2: 'BreakAndDissolving', 3: 'Dissolving'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class EquipUnlockType(enum):
    AVATAR_LEVEL: int = 0
    BP: int = 1
    name_to_values: dict = {'AVATAR_LEVEL': 0, 'BP': 1}
    value_to_names: dict = {0: 'AVATAR_LEVEL', 1: 'BP'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class EquipmentType(enum):
    ARMOR: int = 15
    COIN_TOOLS: int = 21
    CRACK_SCANNER: int = 20
    EMERGENCY_NEEDLE: int = 16
    GRENADE_LAUNCHER: int = 5
    GUN: int = 1
    GUN_MELEE: int = 3
    INVISIBLE: int = 19
    INVISIBLE2: int = 22
    MEDICINE: int = 17
    MELEE: int = 2
    NONE: int = 0
    NORMAL_TACTICAL: int = 18
    SKILL: int = 13
    SP_GUN: int = 4
    SP_SKILL: int = 23
    SUPPORT: int = 14
    THROWABLE_WEAPON_LEFT: int = 12
    THROWABLE_WEAPON_RIGHT: int = 11
    name_to_values: dict = {'NONE': 0, 'GUN': 1, 'MELEE': 2, 'GUN_MELEE': 3, 'SP_GUN': 4, 'GRENADE_LAUNCHER': 5, 'THROWABLE_WEAPON_RIGHT': 11, 'THROWABLE_WEAPON_LEFT': 12, 'SKILL': 13, 'SUPPORT': 14, 'ARMOR': 15, 'EMERGENCY_NEEDLE': 16, 'MEDICINE': 17, 'NORMAL_TACTICAL': 18, 'INVISIBLE': 19, 'CRACK_SCANNER': 20, 'COIN_TOOLS': 21, 'INVISIBLE2': 22, 'SP_SKILL': 23}
    value_to_names: dict = {0: 'NONE', 1: 'GUN', 2: 'MELEE', 3: 'GUN_MELEE', 4: 'SP_GUN', 5: 'GRENADE_LAUNCHER', 11: 'THROWABLE_WEAPON_RIGHT', 12: 'THROWABLE_WEAPON_LEFT', 13: 'SKILL', 14: 'SUPPORT', 15: 'ARMOR', 16: 'EMERGENCY_NEEDLE', 17: 'MEDICINE', 18: 'NORMAL_TACTICAL', 19: 'INVISIBLE', 20: 'CRACK_SCANNER', 21: 'COIN_TOOLS', 22: 'INVISIBLE2', 23: 'SP_SKILL'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class Faction(enum):
    ATTACKER: int = 0
    CHAOS: int = -1
    DEFENDER: int = 1
    name_to_values: dict = {'CHAOS': -1, 'ATTACKER': 0, 'DEFENDER': 1}
    value_to_names: dict = {-1: 'CHAOS', 0: 'ATTACKER', 1: 'DEFENDER'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class FailType(enum):
    OVER_TIME: int = 1
    SAFE_REGION: int = 3
    TEAM_DIE: int = 2
    name_to_values: dict = {'OVER_TIME': 1, 'TEAM_DIE': 2, 'SAFE_REGION': 3}
    value_to_names: dict = {1: 'OVER_TIME', 2: 'TEAM_DIE', 3: 'SAFE_REGION'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GameLogicCompKind(enum):
    AIRDROP: int = 2
    BOT_SQUAD: int = 20
    CONTRACT: int = 7
    ECOTOPE: int = 4
    ELO: int = 15
    GAME_TRACK: int = 14
    GRAND_THEFT: int = 22
    HELEN: int = 16
    HERO: int = 11
    INGAME_ACHIEVE: int = 6
    KILL_FEEDBACK: int = 5
    MAP_MARK: int = 13
    MOVING_PLATFORM: int = 21
    NONE: int = 0
    OCCLUSION: int = 12
    PARACHUTE: int = 3
    ROBOT: int = 9
    ROBOT_TEAM: int = 19
    SAFE_REGION: int = 1
    SKILL: int = 10
    TALENT: int = 8
    TASK: int = 18
    WARM_ROBOT: int = 17
    name_to_values: dict = {'NONE': 0, 'SAFE_REGION': 1, 'AIRDROP': 2, 'PARACHUTE': 3, 'ECOTOPE': 4, 'KILL_FEEDBACK': 5, 'INGAME_ACHIEVE': 6, 'CONTRACT': 7, 'TALENT': 8, 'ROBOT': 9, 'SKILL': 10, 'HERO': 11, 'OCCLUSION': 12, 'MAP_MARK': 13, 'GAME_TRACK': 14, 'ELO': 15, 'HELEN': 16, 'WARM_ROBOT': 17, 'TASK': 18, 'ROBOT_TEAM': 19, 'BOT_SQUAD': 20, 'MOVING_PLATFORM': 21, 'GRAND_THEFT': 22}
    value_to_names: dict = {0: 'NONE', 1: 'SAFE_REGION', 2: 'AIRDROP', 3: 'PARACHUTE', 4: 'ECOTOPE', 5: 'KILL_FEEDBACK', 6: 'INGAME_ACHIEVE', 7: 'CONTRACT', 8: 'TALENT', 9: 'ROBOT', 10: 'SKILL', 11: 'HERO', 12: 'OCCLUSION', 13: 'MAP_MARK', 14: 'GAME_TRACK', 15: 'ELO', 16: 'HELEN', 17: 'WARM_ROBOT', 18: 'TASK', 19: 'ROBOT_TEAM', 20: 'BOT_SQUAD', 21: 'MOVING_PLATFORM', 22: 'GRAND_THEFT'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GameStoreReason(enum):
    BUY_CAPACITY_LIMIT: int = 8
    BUY_CD: int = 4
    BUY_COUNT_LIMIT: int = 3
    CANT_BUY_REBORN_CHANCE: int = 7
    FORBID_REBORN: int = 9
    HAS_AIRDROP: int = 6
    INVALID_GOODS: int = 5
    LACK_OF_COINS: int = 1
    NO_SUCH_ITEM: int = 2
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'LACK_OF_COINS': 1, 'NO_SUCH_ITEM': 2, 'BUY_COUNT_LIMIT': 3, 'BUY_CD': 4, 'INVALID_GOODS': 5, 'HAS_AIRDROP': 6, 'CANT_BUY_REBORN_CHANCE': 7, 'BUY_CAPACITY_LIMIT': 8, 'FORBID_REBORN': 9}
    value_to_names: dict = {0: 'SUCCESS', 1: 'LACK_OF_COINS', 2: 'NO_SUCH_ITEM', 3: 'BUY_COUNT_LIMIT', 4: 'BUY_CD', 5: 'INVALID_GOODS', 6: 'HAS_AIRDROP', 7: 'CANT_BUY_REBORN_CHANCE', 8: 'BUY_CAPACITY_LIMIT', 9: 'FORBID_REBORN'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GenderType(enum):
    FEMALE: int = 2
    MALE: int = 1
    NONE: int = 0
    name_to_values: dict = {'NONE': 0, 'MALE': 1, 'FEMALE': 2}
    value_to_names: dict = {0: 'NONE', 1: 'MALE', 2: 'FEMALE'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GrenadeTriggerType(enum):
    Contact: int = 3
    ContactCheck: int = 4
    ContactSubBomb: int = 6
    LowSpeed: int = 5
    SinceTakeOut: int = 1
    SinceThrow: int = 2
    name_to_values: dict = {'SinceTakeOut': 1, 'SinceThrow': 2, 'Contact': 3, 'ContactCheck': 4, 'LowSpeed': 5, 'ContactSubBomb': 6}
    value_to_names: dict = {1: 'SinceTakeOut', 2: 'SinceThrow', 3: 'Contact', 4: 'ContactCheck', 5: 'LowSpeed', 6: 'ContactSubBomb'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GunExpSource(enum):
    COMBAT: int = 1
    EXP_CARD: int = 2
    Rookie: int = 3
    name_to_values: dict = {'COMBAT': 1, 'EXP_CARD': 2, 'Rookie': 3}
    value_to_names: dict = {1: 'COMBAT', 2: 'EXP_CARD', 3: 'Rookie'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GunID(enum):
    AR97: int = 27
    Gatling: int = 28
    M4A1: int = 1
    VSS: int = 25
    name_to_values: dict = {'M4A1': 1, 'VSS': 25, 'AR97': 27, 'Gatling': 28}
    value_to_names: dict = {1: 'M4A1', 25: 'VSS', 27: 'AR97', 28: 'Gatling'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GunPartUnlockType(enum):
    ITEM: int = 3
    Level: int = 1
    Rookie: int = 2
    name_to_values: dict = {'Level': 1, 'Rookie': 2, 'ITEM': 3}
    value_to_names: dict = {1: 'Level', 2: 'Rookie', 3: 'ITEM'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GunRank(enum):
    FullNation: int = 0
    FullProvince: int = 1
    FullService: int = -1
    name_to_values: dict = {'FullService': -1, 'FullNation': 0, 'FullProvince': 1}
    value_to_names: dict = {-1: 'FullService', 0: 'FullNation', 1: 'FullProvince'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GunSkinType(enum):
    Base: int = -1
    Meisai: int = 0
    SpecialModel: int = 1
    name_to_values: dict = {'Base': -1, 'Meisai': 0, 'SpecialModel': 1}
    value_to_names: dict = {-1: 'Base', 0: 'Meisai', 1: 'SpecialModel'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GunType(enum):
    AR: int = 1
    LMG: int = 4
    MR: int = 5
    NG: int = 9
    NONE: int = 0
    PT: int = 7
    RL: int = 8
    SG: int = 3
    SMG: int = 2
    SR: int = 6
    name_to_values: dict = {'NONE': 0, 'AR': 1, 'SMG': 2, 'SG': 3, 'LMG': 4, 'MR': 5, 'SR': 6, 'PT': 7, 'RL': 8, 'NG': 9}
    value_to_names: dict = {0: 'NONE', 1: 'AR', 2: 'SMG', 3: 'SG', 4: 'LMG', 5: 'MR', 6: 'SR', 7: 'PT', 8: 'RL', 9: 'NG'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class HelpState(enum):
    NONE: int = 0
    OTHER: int = 2
    SELF: int = 1
    name_to_values: dict = {'NONE': 0, 'SELF': 1, 'OTHER': 2}
    value_to_names: dict = {0: 'NONE', 1: 'SELF', 2: 'OTHER'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ItemID(enum):
    ACT_LOBBY_ITEM_ID: int = 4100000100
    AvatarExpBonus: int = 4100000170
    BP_SCORE: int = 4100000110
    CheapBp: int = 4100000431
    DEFAULT_DISPLAY_ITEM_ID: int = 6120000010
    DefaultChatBubbles: int = 6110000010
    DefaultHallMusic: int = 6100000010
    DefaultTailing: int = 6090000010
    EXP_LOBBY_ITEM_ID: int = 4100000010
    ElegantFinetuneTool: int = 4600000020
    FinetuneAccCard: int = 4610000010
    FinetuneTool: int = 4600000010
    GrandTheftCoins: int = 4100001270
    GunExpBonus: int = 4100000160
    Honor: int = 4000000010
    LimitedYuanbao: int = 4000000021
    Metal: int = 4000000040
    QualifyingRewardCard: int = 4100001780
    RANDOM_DEATH_BOX: int = 6060000100
    RANDOM_TRAILING: int = 6090000000
    RenameCard: int = 4100000120
    RoomCard: int = 4100000250
    SeasonMoney: int = 4000000030
    TASK_ACT_1000_BOX: int = 4200000070
    TASK_ACT_500_BOX: int = 4200000060
    UpgradePoint: int = 4100000340
    Yuanbao: int = 4000000020
    name_to_values: dict = {'RenameCard': 4100000120, 'EXP_LOBBY_ITEM_ID': 4100000010, 'ACT_LOBBY_ITEM_ID': 4100000100, 'BP_SCORE': 4100000110, 'TASK_ACT_500_BOX': 4200000060, 'TASK_ACT_1000_BOX': 4200000070, 'Honor': 4000000010, 'Yuanbao': 4000000020, 'LimitedYuanbao': 4000000021, 'SeasonMoney': 4000000030, 'Metal': 4000000040, 'FinetuneAccCard': 4610000010, 'FinetuneTool': 4600000010, 'ElegantFinetuneTool': 4600000020, 'AvatarExpBonus': 4100000170, 'GunExpBonus': 4100000160, 'RoomCard': 4100000250, 'UpgradePoint': 4100000340, 'CheapBp': 4100000431, 'DefaultTailing': 6090000010, 'GrandTheftCoins': 4100001270, 'QualifyingRewardCard': 4100001780, 'DefaultHallMusic': 6100000010, 'DefaultChatBubbles': 6110000010, 'RANDOM_TRAILING': 6090000000, 'RANDOM_DEATH_BOX': 6060000100, 'DEFAULT_DISPLAY_ITEM_ID': 6120000010}
    value_to_names: dict = {4100000120: 'RenameCard', 4100000010: 'EXP_LOBBY_ITEM_ID', 4100000100: 'ACT_LOBBY_ITEM_ID', 4100000110: 'BP_SCORE', 4200000060: 'TASK_ACT_500_BOX', 4200000070: 'TASK_ACT_1000_BOX', 4000000010: 'Honor', 4000000020: 'Yuanbao', 4000000021: 'LimitedYuanbao', 4000000030: 'SeasonMoney', 4000000040: 'Metal', 4610000010: 'FinetuneAccCard', 4600000010: 'FinetuneTool', 4600000020: 'ElegantFinetuneTool', 4100000170: 'AvatarExpBonus', 4100000160: 'GunExpBonus', 4100000250: 'RoomCard', 4100000340: 'UpgradePoint', 4100000431: 'CheapBp', 6090000010: 'DefaultTailing', 4100001270: 'GrandTheftCoins', 4100001780: 'QualifyingRewardCard', 6100000010: 'DefaultHallMusic', 6110000010: 'DefaultChatBubbles', 6090000000: 'RANDOM_TRAILING', 6060000100: 'RANDOM_DEATH_BOX', 6120000010: 'DEFAULT_DISPLAY_ITEM_ID'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ItemSubType(enum):
    AppearanceAni: int = 612
    Body: int = 320
    BombSkin: int = 650
    CardBackground: int = 608
    ChatBubbles: int = 611
    CostItem: int = 412
    Currency: int = 400
    DeathBox: int = 606
    Emote: int = 604
    Execute: int = 605
    Finetune: int = 460
    FinetuneAcl: int = 461
    GiftBag: int = 430
    GunExp: int = 411
    GunPart: int = 998
    GunSkin: int = 550
    Hair: int = 330
    Head: int = 310
    HeadFrame: int = 607
    Item: int = 410
    Mask: int = 340
    Music: int = 610
    Mustache: int = 350
    NONE: int = 0
    OriginGun: int = 999
    Ornament: int = 601
    ProfilePhoto: int = 603
    Sticker: int = 602
    Suit: int = 300
    SuperBag: int = 440
    Trailing: int = 609
    Treasure: int = 420
    Treasure_Choose: int = 426
    Treasure_Gun: int = 425
    Treasure_Micai: int = 421
    V6Token: int = 470
    Watch: int = 360
    name_to_values: dict = {'NONE': 0, 'Suit': 300, 'Head': 310, 'Body': 320, 'Hair': 330, 'Mask': 340, 'Mustache': 350, 'Watch': 360, 'Currency': 400, 'Item': 410, 'GunExp': 411, 'CostItem': 412, 'Treasure': 420, 'Treasure_Micai': 421, 'Treasure_Gun': 425, 'Treasure_Choose': 426, 'GiftBag': 430, 'SuperBag': 440, 'Finetune': 460, 'FinetuneAcl': 461, 'V6Token': 470, 'GunSkin': 550, 'Ornament': 601, 'Sticker': 602, 'ProfilePhoto': 603, 'Emote': 604, 'Execute': 605, 'DeathBox': 606, 'HeadFrame': 607, 'CardBackground': 608, 'Trailing': 609, 'Music': 610, 'ChatBubbles': 611, 'AppearanceAni': 612, 'BombSkin': 650, 'GunPart': 998, 'OriginGun': 999}
    value_to_names: dict = {0: 'NONE', 300: 'Suit', 310: 'Head', 320: 'Body', 330: 'Hair', 340: 'Mask', 350: 'Mustache', 360: 'Watch', 400: 'Currency', 410: 'Item', 411: 'GunExp', 412: 'CostItem', 420: 'Treasure', 421: 'Treasure_Micai', 425: 'Treasure_Gun', 426: 'Treasure_Choose', 430: 'GiftBag', 440: 'SuperBag', 460: 'Finetune', 461: 'FinetuneAcl', 470: 'V6Token', 550: 'GunSkin', 601: 'Ornament', 602: 'Sticker', 603: 'ProfilePhoto', 604: 'Emote', 605: 'Execute', 606: 'DeathBox', 607: 'HeadFrame', 608: 'CardBackground', 609: 'Trailing', 610: 'Music', 611: 'ChatBubbles', 612: 'AppearanceAni', 650: 'BombSkin', 998: 'GunPart', 999: 'OriginGun'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class LanguageFilter(enum):
    Arabia: int = 6
    English: int = 2
    Indonesia: int = 7
    Japanese: int = 10
    No: int = 0
    Portuguese: int = 4
    Russia: int = 5
    SimplifiedChinese: int = 1
    Spanish: int = 3
    Thailand: int = 8
    Vietnam: int = 9
    name_to_values: dict = {'No': 0, 'SimplifiedChinese': 1, 'English': 2, 'Spanish': 3, 'Portuguese': 4, 'Russia': 5, 'Arabia': 6, 'Indonesia': 7, 'Thailand': 8, 'Vietnam': 9, 'Japanese': 10}
    value_to_names: dict = {0: 'No', 1: 'SimplifiedChinese', 2: 'English', 3: 'Spanish', 4: 'Portuguese', 5: 'Russia', 6: 'Arabia', 7: 'Indonesia', 8: 'Thailand', 9: 'Vietnam', 10: 'Japanese'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class LifeState(enum):
    Destroy: int = 2
    Empty: int = 0
    Start: int = 1
    name_to_values: dict = {'Empty': 0, 'Start': 1, 'Destroy': 2}
    value_to_names: dict = {0: 'Empty', 1: 'Start', 2: 'Destroy'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class LoginAuthType(enum):
    APPLE: int = 27
    DISCORD: int = 37
    FACEBOOK: int = 4
    GOOGLE: int = 5
    GUEST: int = 2
    LINE: int = 18
    PASSPORT: int = 38
    STEAM: int = 16
    TIKTOK: int = 34
    TWITTER_X: int = 14
    VK: int = 28
    name_to_values: dict = {'GUEST': 2, 'FACEBOOK': 4, 'GOOGLE': 5, 'TWITTER_X': 14, 'STEAM': 16, 'LINE': 18, 'APPLE': 27, 'VK': 28, 'TIKTOK': 34, 'DISCORD': 37, 'PASSPORT': 38}
    value_to_names: dict = {2: 'GUEST', 4: 'FACEBOOK', 5: 'GOOGLE', 14: 'TWITTER_X', 16: 'STEAM', 18: 'LINE', 27: 'APPLE', 28: 'VK', 34: 'TIKTOK', 37: 'DISCORD', 38: 'PASSPORT'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class LoginChannelType(enum):
    APPLE: int = 16
    DISCORD: int = 24
    FACEBOOK: int = 4
    GOOGLE: int = 3
    GUEST: int = 1
    LINE: int = 9
    PASSPORT: int = 25
    STEAM: int = 7
    TIKTOK: int = 23
    TWITTER_X: int = 5
    VK: int = 17
    name_to_values: dict = {'GUEST': 1, 'GOOGLE': 3, 'FACEBOOK': 4, 'TWITTER_X': 5, 'STEAM': 7, 'LINE': 9, 'APPLE': 16, 'VK': 17, 'TIKTOK': 23, 'DISCORD': 24, 'PASSPORT': 25}
    value_to_names: dict = {1: 'GUEST', 3: 'GOOGLE', 4: 'FACEBOOK', 5: 'TWITTER_X', 7: 'STEAM', 9: 'LINE', 16: 'APPLE', 17: 'VK', 23: 'TIKTOK', 24: 'DISCORD', 25: 'PASSPORT'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class LogoutType(enum):
    AntiV2: int = 3610
    AvatarDelete: int = 3623
    CbgPuton: int = 3607
    CbgRelay: int = 3609
    Cheat: int = 3604
    ClientDataError: int = 3620
    DeviceLimit: int = 3608
    EngineVersion: int = 3611
    EnterSpaceFailed: int = 3619
    FakeLogout: int = 9000
    ForbidLogin: int = 3603
    ForbidMatch: int = 3602
    HeartbeatTimeout: int = 3613
    Kickout: int = 3601
    LoginOtherRegion: int = 3524
    LoseClient: int = 3614
    MigrateServer: int = 9003
    MigrateSpaceNotExists: int = 3616
    OnUpdateBadStatus: int = 3618
    PcAntiAddition: int = 3606
    RelaySuccess: int = 3615
    RollStubBlock: int = 3612
    RollStubHeartbeat: int = 9002
    RollStubPingError: int = 9001
    TeleportFailed: int = 3617
    Transfer: int = 3605
    name_to_values: dict = {'Kickout': 3601, 'ForbidMatch': 3602, 'ForbidLogin': 3603, 'Cheat': 3604, 'Transfer': 3605, 'PcAntiAddition': 3606, 'CbgPuton': 3607, 'DeviceLimit': 3608, 'CbgRelay': 3609, 'AntiV2': 3610, 'EngineVersion': 3611, 'RollStubBlock': 3612, 'HeartbeatTimeout': 3613, 'LoseClient': 3614, 'RelaySuccess': 3615, 'MigrateSpaceNotExists': 3616, 'TeleportFailed': 3617, 'OnUpdateBadStatus': 3618, 'EnterSpaceFailed': 3619, 'ClientDataError': 3620, 'AvatarDelete': 3623, 'LoginOtherRegion': 3524, 'FakeLogout': 9000, 'RollStubPingError': 9001, 'RollStubHeartbeat': 9002, 'MigrateServer': 9003}
    value_to_names: dict = {3601: 'Kickout', 3602: 'ForbidMatch', 3603: 'ForbidLogin', 3604: 'Cheat', 3605: 'Transfer', 3606: 'PcAntiAddition', 3607: 'CbgPuton', 3608: 'DeviceLimit', 3609: 'CbgRelay', 3610: 'AntiV2', 3611: 'EngineVersion', 3612: 'RollStubBlock', 3613: 'HeartbeatTimeout', 3614: 'LoseClient', 3615: 'RelaySuccess', 3616: 'MigrateSpaceNotExists', 3617: 'TeleportFailed', 3618: 'OnUpdateBadStatus', 3619: 'EnterSpaceFailed', 3620: 'ClientDataError', 3623: 'AvatarDelete', 3524: 'LoginOtherRegion', 9000: 'FakeLogout', 9001: 'RollStubPingError', 9002: 'RollStubHeartbeat', 9003: 'MigrateServer'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MagicFieldDestructionType(enum):
    ALL: int = 2
    ENEMY: int = 1
    ENEMY_AND_SELF: int = 3
    NONE: int = 0
    name_to_values: dict = {'NONE': 0, 'ENEMY': 1, 'ALL': 2, 'ENEMY_AND_SELF': 3}
    value_to_names: dict = {0: 'NONE', 1: 'ENEMY', 2: 'ALL', 3: 'ENEMY_AND_SELF'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MailStatus(enum):
    Read: int = 1
    Unread: int = 0
    name_to_values: dict = {'Unread': 0, 'Read': 1}
    value_to_names: dict = {0: 'Unread', 1: 'Read'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MallGunSkinSubType(enum):
    GunSkinBox: int = 303
    GunSkinGift: int = 305
    GunSkinItem: int = 301
    GunSkinPackage: int = 302
    GunSkinSaleSingle: int = 304
    name_to_values: dict = {'GunSkinItem': 301, 'GunSkinPackage': 302, 'GunSkinBox': 303, 'GunSkinSaleSingle': 304, 'GunSkinGift': 305}
    value_to_names: dict = {301: 'GunSkinItem', 302: 'GunSkinPackage', 303: 'GunSkinBox', 304: 'GunSkinSaleSingle', 305: 'GunSkinGift'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MallID(enum):
    UpgradePoint: int = 200018
    name_to_values: dict = {'UpgradePoint': 200018}
    value_to_names: dict = {200018: 'UpgradePoint'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MallRecommendAcquireSource(enum):
    Act: int = 1
    BP: int = 3
    Buy: int = 4
    Gacha: int = 2
    name_to_values: dict = {'Act': 1, 'Gacha': 2, 'BP': 3, 'Buy': 4}
    value_to_names: dict = {1: 'Act', 2: 'Gacha', 3: 'BP', 4: 'Buy'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MallRecommendType(enum):
    Act: int = 4
    GachaOff: int = 7
    Hot: int = 3
    NONE: int = 0
    New: int = 2
    SaleDiscount: int = 5
    SaleOff: int = 6
    SaleTimeLimit: int = 1
    name_to_values: dict = {'NONE': 0, 'SaleTimeLimit': 1, 'New': 2, 'Hot': 3, 'Act': 4, 'SaleDiscount': 5, 'SaleOff': 6, 'GachaOff': 7}
    value_to_names: dict = {0: 'NONE', 1: 'SaleTimeLimit', 2: 'New', 3: 'Hot', 4: 'Act', 5: 'SaleDiscount', 6: 'SaleOff', 7: 'GachaOff'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MallSubType(enum):
    GunSkinGuise: int = 3001
    GunSkinSkin: int = 3002
    ItemCollection: int = 410
    ItemOrnament: int = 601
    ItemProfilePhoto: int = 603
    ItemSticker: int = 602
    name_to_values: dict = {'GunSkinGuise': 3001, 'GunSkinSkin': 3002, 'ItemCollection': 410, 'ItemOrnament': 601, 'ItemSticker': 602, 'ItemProfilePhoto': 603}
    value_to_names: dict = {3001: 'GunSkinGuise', 3002: 'GunSkinSkin', 410: 'ItemCollection', 601: 'ItemOrnament', 602: 'ItemSticker', 603: 'ItemProfilePhoto'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MallType(enum):
    AnnualCard: int = 16
    Charge: int = 5
    ChargeLimit_JP: int = 17
    ChargeRule_JP: int = 18
    CrazySale: int = 12
    Daily: int = 11
    GiftPackage: int = 8
    GunSkin: int = 3
    Hero: int = 6
    HeroSkin: int = 15
    Item: int = 4
    Limited: int = 10
    Mystery: int = 9
    Qualifying: int = 7
    Recommend: int = 1
    name_to_values: dict = {'Recommend': 1, 'GunSkin': 3, 'Item': 4, 'Charge': 5, 'Hero': 6, 'Qualifying': 7, 'GiftPackage': 8, 'Mystery': 9, 'Limited': 10, 'Daily': 11, 'CrazySale': 12, 'HeroSkin': 15, 'AnnualCard': 16, 'ChargeLimit_JP': 17, 'ChargeRule_JP': 18}
    value_to_names: dict = {1: 'Recommend', 3: 'GunSkin', 4: 'Item', 5: 'Charge', 6: 'Hero', 7: 'Qualifying', 8: 'GiftPackage', 9: 'Mystery', 10: 'Limited', 11: 'Daily', 12: 'CrazySale', 15: 'HeroSkin', 16: 'AnnualCard', 17: 'ChargeLimit_JP', 18: 'ChargeRule_JP'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MarkType(enum):
    Attack: int = 7
    CommonEntity: int = 5
    Defence: int = 6
    EnemyCome: int = 8
    EntityWithToplogoAOI: int = 9
    Item: int = 3
    MarkEnemy: int = 2
    MarkPos: int = 1
    Mission: int = 4
    Vehicle: int = 10
    name_to_values: dict = {'MarkPos': 1, 'MarkEnemy': 2, 'Item': 3, 'Mission': 4, 'CommonEntity': 5, 'Defence': 6, 'Attack': 7, 'EnemyCome': 8, 'EntityWithToplogoAOI': 9, 'Vehicle': 10}
    value_to_names: dict = {1: 'MarkPos', 2: 'MarkEnemy', 3: 'Item', 4: 'Mission', 5: 'CommonEntity', 6: 'Defence', 7: 'Attack', 8: 'EnemyCome', 9: 'EntityWithToplogoAOI', 10: 'Vehicle'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MatchKind(enum):
    Default: int = 0
    NormalMatch: int = 2
    Qualifying: int = 1
    name_to_values: dict = {'Default': 0, 'Qualifying': 1, 'NormalMatch': 2}
    value_to_names: dict = {0: 'Default', 1: 'Qualifying', 2: 'NormalMatch'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MatchMode(enum):
    FIVE: int = 5
    FOUR: int = 4
    MULTI: int = 2
    SINGLE: int = 1
    SIX: int = 6
    THREE: int = 3
    name_to_values: dict = {'SINGLE': 1, 'MULTI': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6}
    value_to_names: dict = {1: 'SINGLE', 2: 'MULTI', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MatchQueueType(enum):
    Mobile: int = 2
    PC: int = 1
    name_to_values: dict = {'PC': 1, 'Mobile': 2}
    value_to_names: dict = {1: 'PC', 2: 'Mobile'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MaterialTypeID(enum):
    ParticleShieldInside: int = 7
    name_to_values: dict = {'ParticleShieldInside': 7}
    value_to_names: dict = {7: 'ParticleShieldInside'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MeleeWeaponType(enum):
    Axe: int = 2
    Katana: int = 3
    Knife: int = 1
    NONE: int = 0
    TwoHandAxe: int = 5
    name_to_values: dict = {'NONE': 0, 'Knife': 1, 'Axe': 2, 'Katana': 3, 'TwoHandAxe': 5}
    value_to_names: dict = {0: 'NONE', 1: 'Knife', 2: 'Axe', 3: 'Katana', 5: 'TwoHandAxe'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MissionResult(enum):
    Accept: int = 3
    Fail: int = 1
    Success: int = 0
    name_to_values: dict = {'Success': 0, 'Fail': 1, 'Accept': 3}
    value_to_names: dict = {0: 'Success', 1: 'Fail', 3: 'Accept'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MobaFirstGuideState(enum):
    AIRDROP: int = 6
    AIRDROP_ROBOT: int = 7
    END: int = 8
    FIRST_SUPPLY: int = 2
    NONE: int = 1
    SUPPLY_ROBOT: int = 3
    UAV: int = 4
    UAV_ROBOT: int = 5
    name_to_values: dict = {'NONE': 1, 'FIRST_SUPPLY': 2, 'SUPPLY_ROBOT': 3, 'UAV': 4, 'UAV_ROBOT': 5, 'AIRDROP': 6, 'AIRDROP_ROBOT': 7, 'END': 8}
    value_to_names: dict = {1: 'NONE', 2: 'FIRST_SUPPLY', 3: 'SUPPLY_ROBOT', 4: 'UAV', 5: 'UAV_ROBOT', 6: 'AIRDROP', 7: 'AIRDROP_ROBOT', 8: 'END'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MobaFirstGuideStateNew(enum):
    END: int = 8
    GAP_TIME_1: int = 4
    GAP_TIME_2: int = 6
    KILL_PARA_ROBOT: int = 2
    KILL_ROBOT: int = 5
    NONE: int = 1
    PICKUP_AIRDROP: int = 7
    PICKUP_DEATH_BOX: int = 3
    name_to_values: dict = {'NONE': 1, 'KILL_PARA_ROBOT': 2, 'PICKUP_DEATH_BOX': 3, 'GAP_TIME_1': 4, 'KILL_ROBOT': 5, 'GAP_TIME_2': 6, 'PICKUP_AIRDROP': 7, 'END': 8}
    value_to_names: dict = {1: 'NONE', 2: 'KILL_PARA_ROBOT', 3: 'PICKUP_DEATH_BOX', 4: 'GAP_TIME_1', 5: 'KILL_ROBOT', 6: 'GAP_TIME_2', 7: 'PICKUP_AIRDROP', 8: 'END'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ModelCharCtrlReason(enum):
    DEAD: int = 1
    DYING: int = 0
    EXECUTION: int = 5
    HOLOGRAPHICROBOT: int = 3
    KICK_UP: int = 6
    ON_AIRCRAFT: int = 2
    VEHICLE: int = 4
    name_to_values: dict = {'DYING': 0, 'DEAD': 1, 'ON_AIRCRAFT': 2, 'HOLOGRAPHICROBOT': 3, 'VEHICLE': 4, 'EXECUTION': 5, 'KICK_UP': 6}
    value_to_names: dict = {0: 'DYING', 1: 'DEAD', 2: 'ON_AIRCRAFT', 3: 'HOLOGRAPHICROBOT', 4: 'VEHICLE', 5: 'EXECUTION', 6: 'KICK_UP'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ModelFilterReason(enum):
    DEAD: int = 1
    DYING: int = 0
    MONSTER: int = 3
    ROBOT_MASTER: int = 2
    name_to_values: dict = {'DYING': 0, 'DEAD': 1, 'ROBOT_MASTER': 2, 'MONSTER': 3}
    value_to_names: dict = {0: 'DYING', 1: 'DEAD', 2: 'ROBOT_MASTER', 3: 'MONSTER'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ModelPoseType(enum):
    Crouch: int = 1
    Jump: int = 2
    Ladder: int = 6
    Prone: int = 4
    Slide: int = 3
    Stand: int = 0
    Swim: int = 5
    name_to_values: dict = {'Stand': 0, 'Crouch': 1, 'Jump': 2, 'Slide': 3, 'Prone': 4, 'Swim': 5, 'Ladder': 6}
    value_to_names: dict = {0: 'Stand', 1: 'Crouch', 2: 'Jump', 3: 'Slide', 4: 'Prone', 5: 'Swim', 6: 'Ladder'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MoveSpeedLevel(enum):
    Idle: int = 0
    Jog: int = 2
    KnockDown: int = 5
    Sprint: int = 3
    SuperSprint: int = 4
    Walk: int = 1
    name_to_values: dict = {'Idle': 0, 'Walk': 1, 'Jog': 2, 'Sprint': 3, 'SuperSprint': 4, 'KnockDown': 5}
    value_to_names: dict = {0: 'Idle', 1: 'Walk', 2: 'Jog', 3: 'Sprint', 4: 'SuperSprint', 5: 'KnockDown'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class Nothing(object):
class PlayerIdentity(enum):
    Anchor: int = 1
    Creator: int = 2
    Staff: int = 3
    name_to_values: dict = {'Anchor': 1, 'Creator': 2, 'Staff': 3}
    value_to_names: dict = {1: 'Anchor', 2: 'Creator', 3: 'Staff'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PoseSenderReason(enum):
    DEAD: int = 1
    DYING: int = 0
    EXECUTION: int = 4
    MOVING_PLATFORM: int = 3
    ROBOT_MASTER: int = 2
    name_to_values: dict = {'DYING': 0, 'DEAD': 1, 'ROBOT_MASTER': 2, 'MOVING_PLATFORM': 3, 'EXECUTION': 4}
    value_to_names: dict = {0: 'DYING', 1: 'DEAD', 2: 'ROBOT_MASTER', 3: 'MOVING_PLATFORM', 4: 'EXECUTION'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PrototypeId(enum):
    Default: int = 0
    Ghost: int = 1
    name_to_values: dict = {'Default': 0, 'Ghost': 1}
    value_to_names: dict = {0: 'Default', 1: 'Ghost'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PunishType(object):
    Disable: str = 'Disable'
    NoDamage: str = 'NoDamage'
    NoPunish: str = ''
    PullBack: str = 'PullBack'

class QualifyingFilter(enum):
    Bronze: int = 1
    Diamond: int = 5
    Gold: int = 3
    Legend: int = 7
    Master: int = 6
    No: int = 0
    Platinum: int = 4
    Silver: int = 2
    name_to_values: dict = {'No': 0, 'Bronze': 1, 'Silver': 2, 'Gold': 3, 'Platinum': 4, 'Diamond': 5, 'Master': 6, 'Legend': 7}
    value_to_names: dict = {0: 'No', 1: 'Bronze', 2: 'Silver', 3: 'Gold', 4: 'Platinum', 5: 'Diamond', 6: 'Master', 7: 'Legend'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RebornSkillInheritType(enum):
    CLEAR: int = 1
    KEEP: int = 0
    REFRESH: int = 2
    name_to_values: dict = {'KEEP': 0, 'CLEAR': 1, 'REFRESH': 2}
    value_to_names: dict = {0: 'KEEP', 1: 'CLEAR', 2: 'REFRESH'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RebornType(enum):
    AUTO: int = 1
    BUY: int = 3
    BecomeZombie: int = 4
    ISLAND: int = 2
    Recover: int = 5
    name_to_values: dict = {'AUTO': 1, 'ISLAND': 2, 'BUY': 3, 'BecomeZombie': 4, 'Recover': 5}
    value_to_names: dict = {1: 'AUTO', 2: 'ISLAND', 3: 'BUY', 4: 'BecomeZombie', 5: 'Recover'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RenameCode(enum):
    AVATAR_ERROR: int = 2
    ITEM_ERROR: int = 1
    NAME_DUPLICATE: int = 3
    NAME_INVALID: int = 4
    NAME_TIME_LIMIT: int = 5
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'ITEM_ERROR': 1, 'AVATAR_ERROR': 2, 'NAME_DUPLICATE': 3, 'NAME_INVALID': 4, 'NAME_TIME_LIMIT': 5}
    value_to_names: dict = {0: 'SUCCESS', 1: 'ITEM_ERROR', 2: 'AVATAR_ERROR', 3: 'NAME_DUPLICATE', 4: 'NAME_INVALID', 5: 'NAME_TIME_LIMIT'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ReplayDispatcher(enum):
    ReplayForAreaEntity: int = 2
    ReplayForCombatAvatar: int = 3
    ReplayForFpsWeaponCase: int = 4
    ReplayForHandModel: int = 1
    ReplayForHudFrontSight: int = 6
    ReplayForSpellWorker: int = 5
    name_to_values: dict = {'ReplayForHandModel': 1, 'ReplayForAreaEntity': 2, 'ReplayForCombatAvatar': 3, 'ReplayForFpsWeaponCase': 4, 'ReplayForSpellWorker': 5, 'ReplayForHudFrontSight': 6}
    value_to_names: dict = {1: 'ReplayForHandModel', 2: 'ReplayForAreaEntity', 3: 'ReplayForCombatAvatar', 4: 'ReplayForFpsWeaponCase', 5: 'ReplayForSpellWorker', 6: 'ReplayForHudFrontSight'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ReportAvatarChatReason(enum):
    HEAD_PIC: int = 5
    NAME: int = 0
    OTHER: int = 4
    POLITICS: int = 3
    SEX: int = 2
    WORD: int = 1
    name_to_values: dict = {'NAME': 0, 'WORD': 1, 'SEX': 2, 'POLITICS': 3, 'OTHER': 4, 'HEAD_PIC': 5}
    value_to_names: dict = {0: 'NAME', 1: 'WORD', 2: 'SEX', 3: 'POLITICS', 4: 'OTHER', 5: 'HEAD_PIC'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ReportAvatarType(enum):
    CLAN: int = 6
    ENEMY: int = 5
    HALL: int = 1
    KILLER: int = 2
    TEAMMATE: int = 4
    WATCH: int = 3
    name_to_values: dict = {'HALL': 1, 'KILLER': 2, 'WATCH': 3, 'TEAMMATE': 4, 'ENEMY': 5, 'CLAN': 6}
    value_to_names: dict = {1: 'HALL', 2: 'KILLER', 3: 'WATCH', 4: 'TEAMMATE', 5: 'ENEMY', 6: 'CLAN'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ReserveFriendStatus(enum):
    Agree: int = 10
    EnterHall: int = 5
    NoLongerAccept: int = 6
    NoReply: int = 0
    Refuse: int = 1
    name_to_values: dict = {'NoReply': 0, 'Refuse': 1, 'Agree': 10, 'NoLongerAccept': 6, 'EnterHall': 5}
    value_to_names: dict = {0: 'NoReply', 1: 'Refuse', 10: 'Agree', 6: 'NoLongerAccept', 5: 'EnterHall'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ReviewStatus(enum):
    ERROR: int = -1
    PASSED: int = 0
    PRPASSED: int = 1
    REFUSED: int = 3
    VERIFYING: int = 2
    name_to_values: dict = {'ERROR': -1, 'PASSED': 0, 'PRPASSED': 1, 'VERIFYING': 2, 'REFUSED': 3}
    value_to_names: dict = {-1: 'ERROR', 0: 'PASSED', 1: 'PRPASSED', 2: 'VERIFYING', 3: 'REFUSED'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ShareType(enum):
    Game: int = 1
    Task: int = 3
    Zone: int = 2
    name_to_values: dict = {'Game': 1, 'Zone': 2, 'Task': 3}
    value_to_names: dict = {1: 'Game', 2: 'Zone', 3: 'Task'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SigninState(enum):
    INVALID: int = 1
    NO_DIAMOND: int = 3
    SIGNINED: int = 2
    SUCCESS: int = 0
    name_to_values: dict = {'SUCCESS': 0, 'INVALID': 1, 'SIGNINED': 2, 'NO_DIAMOND': 3}
    value_to_names: dict = {0: 'SUCCESS', 1: 'INVALID', 2: 'SIGNINED', 3: 'NO_DIAMOND'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SkillAttackMethod(enum):
    BUFF: int = 2
    EXPLOSION: int = 1
    StoryTick: int = 4
    TRIGGER: int = 3
    TriggerCustom: int = 5
    name_to_values: dict = {'EXPLOSION': 1, 'BUFF': 2, 'TRIGGER': 3, 'StoryTick': 4, 'TriggerCustom': 5}
    value_to_names: dict = {1: 'EXPLOSION', 2: 'BUFF', 3: 'TRIGGER', 4: 'StoryTick', 5: 'TriggerCustom'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SkillDamageType(enum):
    BUFF: int = 4
    EXPLOSION: int = 3
    name_to_values: dict = {'EXPLOSION': 3, 'BUFF': 4}
    value_to_names: dict = {3: 'EXPLOSION', 4: 'BUFF'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SkinCoreType(enum):
    SkinCoreGem: int = 1
    SkinCoreMP5: int = 4
    SkinCoreScales: int = 2
    SkinCoreTwin: int = 3
    name_to_values: dict = {'SkinCoreGem': 1, 'SkinCoreScales': 2, 'SkinCoreTwin': 3, 'SkinCoreMP5': 4}
    value_to_names: dict = {1: 'SkinCoreGem', 2: 'SkinCoreScales', 3: 'SkinCoreTwin', 4: 'SkinCoreMP5'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SkinTwinType(enum):
    TwinMain: int = 2
    TwinSub: int = 1
    name_to_values: dict = {'TwinSub': 1, 'TwinMain': 2}
    value_to_names: dict = {1: 'TwinSub', 2: 'TwinMain'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SkinType(enum):
    Default: int = -1
    Illusion: int = 1
    Normal: int = 0
    name_to_values: dict = {'Default': -1, 'Normal': 0, 'Illusion': 1}
    value_to_names: dict = {-1: 'Default', 0: 'Normal', 1: 'Illusion'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SpellChargeType(enum):
    NONE: int = 0
    TIME: int = 2
    VALUE: int = 1
    name_to_values: dict = {'NONE': 0, 'VALUE': 1, 'TIME': 2}
    value_to_names: dict = {0: 'NONE', 1: 'VALUE', 2: 'TIME'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SpellDamageType(enum):
    GunWeapon: int = 1
    MeleeWeapon: int = 2
    name_to_values: dict = {'GunWeapon': 1, 'MeleeWeapon': 2}
    value_to_names: dict = {1: 'GunWeapon', 2: 'MeleeWeapon'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SurveyType(enum):
    AppScore: int = 100
    Star: int = 1
    name_to_values: dict = {'Star': 1, 'option': 2, 'AppScore': 100}
    option: int = 2
    value_to_names: dict = {1: 'Star', 2: 'option', 100: 'AppScore'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class TalentCode(enum):
    ADS_FLASH: int = 3
    AccumulateJump: int = 59
    AdaptSurmount1: int = 20
    AdaptSurmount2: int = 21
    AdaptSurmount3: int = 22
    AddSkillCountByKA: int = 89
    AdsMarkPos: int = 41
    AdsShield: int = 35
    ArmorEnergy: int = 116
    AssassinateChange1: int = 80
    AssassinateChange2: int = 81
    AttackHolographicRobot: int = 118
    BackWeakenDamage: int = 63
    BrokenArmorGenSmoke: int = 47
    BurnAmmo: int = 86
    CRISIS_AWARENESS: int = 2
    CannonSlowTarget: int = 69
    CannonUpgrade: int = 70
    ChangeSkill: int = 65
    ChangeSkillEntry: int = 67
    CoinsShield: int = 56
    Collection: int = 7
    CoolBlood: int = 11
    DamageShow: int = 13
    DamageSlowArmor: int = 87
    DamageSurmount1: int = 17
    DamageSurmount2: int = 18
    DamageSurmount3: int = 19
    DamageTalent5: int = 30
    DebuffEffectUp: int = 48
    Discount: int = 12
    DyingArmor: int = 31
    EnemyTrack: int = 4
    EnergySkillUpgrade: int = 43
    EnergySkillValueUp: int = 49
    EnergyTransfer: int = 55
    ExposeKillerToTeam: int = 37
    FeelLowHp: int = 83
    FeelSurmount1: int = 26
    FeelSurmount2: int = 27
    FeelSurmount3: int = 28
    FiringRecoilStable: int = 51
    GasPassiveSkill: int = 102
    GrenadeEnhance: int = 34
    HeadShotWeakenDamage: int = 64
    HighAlart: int = 33
    HitRecoverArmor: int = 57
    HitSlowDown: int = 15
    HitXrayToTeam: int = 61
    IceArmorRecoverSpeed: int = 100
    IceExtraArmor: int = 101
    InfoShielding: int = 36
    InitialRecoilStable: int = 53
    KillAddAmmo: int = 32
    KillEnemyMarkPos: int = 40
    KneeJerkReflex: int = 6
    LOCK: int = 1
    LuckyBulletDamage: int = 62
    MaxArmorToMaxHp: int = 46
    Radar: int = 14
    ReduceFallHurt: int = 45
    RemoteShotDamageUp: int = 52
    ResistTalent: int = 54
    Ruthless: int = 5
    SensingAroundEnemies: int = 110
    ShieldImpuls: int = 82
    ShieldWeakenDamage: int = 42
    ShowHitMe: int = 84
    SignalBan: int = 10
    Silencer: int = 8
    SlideAddAmmo: int = 29
    SlideAssault: int = 58
    SpecialCredit: int = 9
    SpecialMeleeAttack: int = 115
    SpeedLevelWeakenDamage: int = 38
    SpeedUpSkillByKA: int = 88
    SplitGrenade: int = 16
    SprintFiring: int = 60
    SuperCross: int = 44
    SurviveSurmount1: int = 23
    SurviveSurmount2: int = 24
    TeammateCue: int = 25
    ThrowableBombEffect: int = 50
    Trophies: int = 85
    UpgradeGunDamageInRange: int = 39
    UsingCureUav: int = 117
    name_to_values: dict = {'LOCK': 1, 'CRISIS_AWARENESS': 2, 'ADS_FLASH': 3, 'EnemyTrack': 4, 'Ruthless': 5, 'KneeJerkReflex': 6, 'Collection': 7, 'Silencer': 8, 'SpecialCredit': 9, 'SignalBan': 10, 'CoolBlood': 11, 'Discount': 12, 'DamageShow': 13, 'Radar': 14, 'HitSlowDown': 15, 'SplitGrenade': 16, 'DamageSurmount1': 17, 'DamageSurmount2': 18, 'DamageSurmount3': 19, 'AdaptSurmount1': 20, 'AdaptSurmount2': 21, 'AdaptSurmount3': 22, 'SurviveSurmount1': 23, 'SurviveSurmount2': 24, 'TeammateCue': 25, 'FeelSurmount1': 26, 'FeelSurmount2': 27, 'FeelSurmount3': 28, 'SlideAddAmmo': 29, 'DamageTalent5': 30, 'DyingArmor': 31, 'KillAddAmmo': 32, 'HighAlart': 33, 'GrenadeEnhance': 34, 'AdsShield': 35, 'InfoShielding': 36, 'ExposeKillerToTeam': 37, 'SpeedLevelWeakenDamage': 38, 'UpgradeGunDamageInRange': 39, 'KillEnemyMarkPos': 40, 'AdsMarkPos': 41, 'ShieldWeakenDamage': 42, 'EnergySkillUpgrade': 43, 'SuperCross': 44, 'ReduceFallHurt': 45, 'MaxArmorToMaxHp': 46, 'BrokenArmorGenSmoke': 47, 'DebuffEffectUp': 48, 'EnergySkillValueUp': 49, 'ThrowableBombEffect': 50, 'FiringRecoilStable': 51, 'RemoteShotDamageUp': 52, 'InitialRecoilStable': 53, 'ResistTalent': 54, 'EnergyTransfer': 55, 'CoinsShield': 56, 'HitRecoverArmor': 57, 'SlideAssault': 58, 'AccumulateJump': 59, 'SprintFiring': 60, 'HitXrayToTeam': 61, 'LuckyBulletDamage': 62, 'BackWeakenDamage': 63, 'HeadShotWeakenDamage': 64, 'ChangeSkill': 65, 'ChangeSkillEntry': 67, 'CannonSlowTarget': 69, 'CannonUpgrade': 70, 'AssassinateChange1': 80, 'AssassinateChange2': 81, 'ShieldImpuls': 82, 'FeelLowHp': 83, 'ShowHitMe': 84, 'Trophies': 85, 'BurnAmmo': 86, 'DamageSlowArmor': 87, 'SpeedUpSkillByKA': 88, 'AddSkillCountByKA': 89, 'IceArmorRecoverSpeed': 100, 'IceExtraArmor': 101, 'GasPassiveSkill': 102, 'SensingAroundEnemies': 110, 'SpecialMeleeAttack': 115, 'ArmorEnergy': 116, 'UsingCureUav': 117, 'AttackHolographicRobot': 118}
    value_to_names: dict = {1: 'LOCK', 2: 'CRISIS_AWARENESS', 3: 'ADS_FLASH', 4: 'EnemyTrack', 5: 'Ruthless', 6: 'KneeJerkReflex', 7: 'Collection', 8: 'Silencer', 9: 'SpecialCredit', 10: 'SignalBan', 11: 'CoolBlood', 12: 'Discount', 13: 'DamageShow', 14: 'Radar', 15: 'HitSlowDown', 16: 'SplitGrenade', 17: 'DamageSurmount1', 18: 'DamageSurmount2', 19: 'DamageSurmount3', 20: 'AdaptSurmount1', 21: 'AdaptSurmount2', 22: 'AdaptSurmount3', 23: 'SurviveSurmount1', 24: 'SurviveSurmount2', 25: 'TeammateCue', 26: 'FeelSurmount1', 27: 'FeelSurmount2', 28: 'FeelSurmount3', 29: 'SlideAddAmmo', 30: 'DamageTalent5', 31: 'DyingArmor', 32: 'KillAddAmmo', 33: 'HighAlart', 34: 'GrenadeEnhance', 35: 'AdsShield', 36: 'InfoShielding', 37: 'ExposeKillerToTeam', 38: 'SpeedLevelWeakenDamage', 39: 'UpgradeGunDamageInRange', 40: 'KillEnemyMarkPos', 41: 'AdsMarkPos', 42: 'ShieldWeakenDamage', 43: 'EnergySkillUpgrade', 44: 'SuperCross', 45: 'ReduceFallHurt', 46: 'MaxArmorToMaxHp', 47: 'BrokenArmorGenSmoke', 48: 'DebuffEffectUp', 49: 'EnergySkillValueUp', 50: 'ThrowableBombEffect', 51: 'FiringRecoilStable', 52: 'RemoteShotDamageUp', 53: 'InitialRecoilStable', 54: 'ResistTalent', 55: 'EnergyTransfer', 56: 'CoinsShield', 57: 'HitRecoverArmor', 58: 'SlideAssault', 59: 'AccumulateJump', 60: 'SprintFiring', 61: 'HitXrayToTeam', 62: 'LuckyBulletDamage', 63: 'BackWeakenDamage', 64: 'HeadShotWeakenDamage', 65: 'ChangeSkill', 67: 'ChangeSkillEntry', 69: 'CannonSlowTarget', 70: 'CannonUpgrade', 80: 'AssassinateChange1', 81: 'AssassinateChange2', 82: 'ShieldImpuls', 83: 'FeelLowHp', 84: 'ShowHitMe', 85: 'Trophies', 86: 'BurnAmmo', 87: 'DamageSlowArmor', 88: 'SpeedUpSkillByKA', 89: 'AddSkillCountByKA', 100: 'IceArmorRecoverSpeed', 101: 'IceExtraArmor', 102: 'GasPassiveSkill', 110: 'SensingAroundEnemies', 115: 'SpecialMeleeAttack', 116: 'ArmorEnergy', 117: 'UsingCureUav', 118: 'AttackHolographicRobot'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class TalentSource(enum):
    Caster: int = 1
    Target: int = 2
    name_to_values: dict = {'Caster': 1, 'Target': 2}
    value_to_names: dict = {1: 'Caster', 2: 'Target'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class TalentState(enum):
    Empty: int = 0
    name_to_values: dict = {'Empty': 0}
    value_to_names: dict = {0: 'Empty'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class TitleType(object):
    GUN_TITLE: int = 1
    HONOR_TITLE: int = 2

class UavType(enum):
    GlobalScan: int = 2
    PartScan: int = 1
    name_to_values: dict = {'PartScan': 1, 'GlobalScan': 2}
    value_to_names: dict = {1: 'PartScan', 2: 'GlobalScan'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class VehicleState(enum):
    CLIENT: int = 3
    DRIVING: int = 1
    IDLE: int = 0
    PHYSICS: int = 2
    name_to_values: dict = {'IDLE': 0, 'DRIVING': 1, 'PHYSICS': 2, 'CLIENT': 3}
    value_to_names: dict = {0: 'IDLE', 1: 'DRIVING', 2: 'PHYSICS', 3: 'CLIENT'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class VehicleSyncMode(enum):
    Client: int = 1
    Server: int = 2
    name_to_values: dict = {'Client': 1, 'Server': 2}
    value_to_names: dict = {1: 'Client', 2: 'Server'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class WarehouseItemType(enum):
    Clothes: int = 300
    Collection: int = 600
    GunGuise: int = 500
    GunSkin: int = 100
    Item: int = 400
    MeleeWeapon: int = 200
    NoShow: int = 900
    name_to_values: dict = {'GunSkin': 100, 'MeleeWeapon': 200, 'Clothes': 300, 'Item': 400, 'GunGuise': 500, 'Collection': 600, 'NoShow': 900}
    value_to_names: dict = {100: 'GunSkin', 200: 'MeleeWeapon', 300: 'Clothes', 400: 'Item', 500: 'GunGuise', 600: 'Collection', 900: 'NoShow'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class WayPointFlags(enum):
    END: int = 2
    OFFMESH_CONNECTION: int = 4
    START: int = 1
    name_to_values: dict = {'START': 1, 'END': 2, 'OFFMESH_CONNECTION': 4}
    value_to_names: dict = {1: 'START', 2: 'END', 4: 'OFFMESH_CONNECTION'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class WeaponArrowType(enum):
    Explode: int = 1
    name_to_values: dict = {'Explode': 1}
    value_to_names: dict = {1: 'Explode'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class WeaponPartFeature(enum):
    AmmunitionBreakAds: int = 12
    AmmunitionDefaultAction: int = 15
    AmmunitionHasSuppress: int = 16
    AmmunitionIsDrum: int = 9
    AmmunitionShowAmmo: int = 11
    BarrelOwnMuzzle: int = 5
    BarrelOwnUnderbarrel: int = 6
    DualWielding: int = 13
    ExplosiveArrow: int = 10
    NeedAdsFlash: int = 2
    NeedReflector: int = 4
    NeedSqueezeReload: int = 8
    OpticShowAmmo: int = 3
    OwnDefaultUnderbarrel: int = 14
    Silencer: int = 1
    StockOwnReargrip: int = 7
    name_to_values: dict = {'Silencer': 1, 'NeedAdsFlash': 2, 'OpticShowAmmo': 3, 'NeedReflector': 4, 'BarrelOwnMuzzle': 5, 'BarrelOwnUnderbarrel': 6, 'StockOwnReargrip': 7, 'NeedSqueezeReload': 8, 'AmmunitionIsDrum': 9, 'ExplosiveArrow': 10, 'AmmunitionShowAmmo': 11, 'AmmunitionBreakAds': 12, 'DualWielding': 13, 'OwnDefaultUnderbarrel': 14, 'AmmunitionDefaultAction': 15, 'AmmunitionHasSuppress': 16}
    value_to_names: dict = {1: 'Silencer', 2: 'NeedAdsFlash', 3: 'OpticShowAmmo', 4: 'NeedReflector', 5: 'BarrelOwnMuzzle', 6: 'BarrelOwnUnderbarrel', 7: 'StockOwnReargrip', 8: 'NeedSqueezeReload', 9: 'AmmunitionIsDrum', 10: 'ExplosiveArrow', 11: 'AmmunitionShowAmmo', 12: 'AmmunitionBreakAds', 13: 'DualWielding', 14: 'OwnDefaultUnderbarrel', 15: 'AmmunitionDefaultAction', 16: 'AmmunitionHasSuppress'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class WeaponPartOpticType(enum):
    Double: int = 2
    Holographic: int = 1
    Machine: int = 0
    Octuple: int = 6
    Quadruple: int = 4
    Sextuple: int = 5
    Triple: int = 3
    name_to_values: dict = {'Machine': 0, 'Holographic': 1, 'Double': 2, 'Triple': 3, 'Quadruple': 4, 'Sextuple': 5, 'Octuple': 6}
    value_to_names: dict = {0: 'Machine', 1: 'Holographic', 2: 'Double', 3: 'Triple', 4: 'Quadruple', 5: 'Sextuple', 6: 'Octuple'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class WeaponSchemeType(enum):
    Defalut: int = 0
    RankPlayer: int = 3
    Recommend: int = 2
    System: int = 1
    name_to_values: dict = {'Defalut': 0, 'System': 1, 'Recommend': 2, 'RankPlayer': 3}
    value_to_names: dict = {0: 'Defalut', 1: 'System', 2: 'Recommend', 3: 'RankPlayer'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class WeatherType(enum):
    Cloudy: int = 2
    Rain: int = 1
    Sunny: int = 0
    name_to_values: dict = {'Sunny': 0, 'Rain': 1, 'Cloudy': 2}
    value_to_names: dict = {0: 'Sunny', 1: 'Rain', 2: 'Cloudy'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class WildShopBuyResult(enum):
    AmmoFull: int = 5
    CountLimit: int = 1
    CountNotEnough: int = 2
    LackCoins: int = 3
    NoSuchItem: int = 4
    Success: int = 0
    name_to_values: dict = {'Success': 0, 'CountLimit': 1, 'CountNotEnough': 2, 'LackCoins': 3, 'NoSuchItem': 4, 'AmmoFull': 5}
    value_to_names: dict = {0: 'Success', 1: 'CountLimit', 2: 'CountNotEnough', 3: 'LackCoins', 4: 'NoSuchItem', 5: 'AmmoFull'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class WildShopItemType(enum):
    High_Gun: int = 101
    High_Module: int = 104
    High_Supply: int = 102
    High_Tactical: int = 103
    Ordinary_Gun: int = 1
    Ordinary_Module: int = 4
    Ordinary_Supply: int = 2
    Ordinary_Tactical: int = 3
    name_to_values: dict = {'Ordinary_Gun': 1, 'Ordinary_Supply': 2, 'Ordinary_Tactical': 3, 'Ordinary_Module': 4, 'High_Gun': 101, 'High_Supply': 102, 'High_Tactical': 103, 'High_Module': 104}
    value_to_names: dict = {1: 'Ordinary_Gun', 2: 'Ordinary_Supply', 3: 'Ordinary_Tactical', 4: 'Ordinary_Module', 101: 'High_Gun', 102: 'High_Supply', 103: 'High_Tactical', 104: 'High_Module'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class WildShopItemTypeUI(enum):
    FullAmmo: int = 4
    Gun: int = 1
    LoadoutGun: int = 5
    Supply: int = 2
    Talent: int = 3
    name_to_values: dict = {'Gun': 1, 'Supply': 2, 'Talent': 3, 'FullAmmo': 4, 'LoadoutGun': 5}
    value_to_names: dict = {1: 'Gun', 2: 'Supply', 3: 'Talent', 4: 'FullAmmo', 5: 'LoadoutGun'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class datetime(date):
    astimezone: method_descriptor = <method 'astimezone' of 'datetime.datetime' objects>
    combine: builtin_function_or_method = <built-in method combine of type object at 0x70285103c8>
    ctime: method_descriptor = <method 'ctime' of 'datetime.datetime' objects>
    date: method_descriptor = <method 'date' of 'datetime.datetime' objects>
    day: getset_descriptor = <attribute 'day' of 'datetime.date' objects>
    dst: method_descriptor = <method 'dst' of 'datetime.datetime' objects>
    fold: getset_descriptor = <attribute 'fold' of 'datetime.datetime' objects>
    fromisocalendar: builtin_function_or_method = <built-in method fromisocalendar of type object at 0x70285103c8>
    fromisoformat: builtin_function_or_method = <built-in method fromisoformat of type object at 0x70285103c8>
    fromordinal: builtin_function_or_method = <built-in method fromordinal of type object at 0x70285103c8>
    fromtimestamp: builtin_function_or_method = <built-in method fromtimestamp of type object at 0x70285103c8>
    hour: getset_descriptor = <attribute 'hour' of 'datetime.datetime' objects>
    isocalendar: method_descriptor = <method 'isocalendar' of 'datetime.date' objects>
    isoformat: method_descriptor = <method 'isoformat' of 'datetime.datetime' objects>
    isoweekday: method_descriptor = <method 'isoweekday' of 'datetime.date' objects>
    max: datetime = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
    microsecond: getset_descriptor = <attribute 'microsecond' of 'datetime.datetime' objects>
    min: datetime = datetime.datetime(1, 1, 1, 0, 0)
    minute: getset_descriptor = <attribute 'minute' of 'datetime.datetime' objects>
    month: getset_descriptor = <attribute 'month' of 'datetime.date' objects>
    now: builtin_function_or_method = <built-in method now of type object at 0x70285103c8>
    replace: method_descriptor = <method 'replace' of 'datetime.datetime' objects>
    resolution: timedelta = datetime.timedelta(microseconds=1)
    second: getset_descriptor = <attribute 'second' of 'datetime.datetime' objects>
    strftime: method_descriptor = <method 'strftime' of 'datetime.date' objects>
    strptime: builtin_function_or_method = <built-in method strptime of type object at 0x70285103c8>
    time: method_descriptor = <method 'time' of 'datetime.datetime' objects>
    timestamp: method_descriptor = <method 'timestamp' of 'datetime.datetime' objects>
    timetuple: method_descriptor = <method 'timetuple' of 'datetime.datetime' objects>
    timetz: method_descriptor = <method 'timetz' of 'datetime.datetime' objects>
    today: builtin_function_or_method = <built-in method today of type object at 0x70285103c8>
    toordinal: method_descriptor = <method 'toordinal' of 'datetime.date' objects>
    tzinfo: getset_descriptor = <attribute 'tzinfo' of 'datetime.datetime' objects>
    tzname: method_descriptor = <method 'tzname' of 'datetime.datetime' objects>
    utcfromtimestamp: builtin_function_or_method = <built-in method utcfromtimestamp of type object at 0x70285103c8>
    utcnow: builtin_function_or_method = <built-in method utcnow of type object at 0x70285103c8>
    utcoffset: method_descriptor = <method 'utcoffset' of 'datetime.datetime' objects>
    utctimetuple: method_descriptor = <method 'utctimetuple' of 'datetime.datetime' objects>
    weekday: method_descriptor = <method 'weekday' of 'datetime.date' objects>
    year: getset_descriptor = <attribute 'year' of 'datetime.date' objects>

class enum(object):
    name_to_values: dict = {}
    value_to_names: dict = {}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class timedelta(object):
    days: member_descriptor = <member 'days' of 'datetime.timedelta' objects>
    max: timedelta = datetime.timedelta(days=999999999, seconds=86399, microseconds=999999)
    microseconds: member_descriptor = <member 'microseconds' of 'datetime.timedelta' objects>
    min: timedelta = datetime.timedelta(days=-999999999)
    resolution: timedelta = datetime.timedelta(microseconds=1)
    seconds: member_descriptor = <member 'seconds' of 'datetime.timedelta' objects>
    total_seconds: method_descriptor = <method 'total_seconds' of 'datetime.timedelta' objects>

class tzinfo(object):
    dst: method_descriptor = <method 'dst' of 'datetime.tzinfo' objects>
    fromutc: method_descriptor = <method 'fromutc' of 'datetime.tzinfo' objects>
    tzname: method_descriptor = <method 'tzname' of 'datetime.tzinfo' objects>
    utcoffset: method_descriptor = <method 'utcoffset' of 'datetime.tzinfo' objects>


def CalculateEquipmentTypeToBackpackSlots(desc): ...
def CheckPlatform(platform): ...
def GetTimeZone(): ...
def GetTimeZoneSecond(): ...


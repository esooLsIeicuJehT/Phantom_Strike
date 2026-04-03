# module: gclient.cconst

import MEngine
import chat_emotion_data
import consts
import ichat
import lobby_item_data
import math
import six2

ADS_BALLISTIC_EFFECT_PARAM: dict = {'radius_max': 0.6, 'angle_max': 30}
ADS_FLASH_PARAM: dict = {'valid_aim_angle': 14, 'invalid_distance': 5, 'base_distance': 10, 'scale_distance': 1, 'scale_factor': 0.15, 'base_fov': 70, 'scale_max': 20}
AD_PERMISSION_CALENDAR: str = 'android.permission.WRITE_CALENDAR'
AD_PERMISSION_CAMERA: str = 'android.permission.CAMERA'
AD_PERMISSION_LOCATION: str = 'android.permission.ACCESS_COARSE_LOCATION'
AD_PERMISSION_LOCATION_COARSE: str = 'android.permission.ACCESS_COARSE_LOCATION'
AD_PERMISSION_LOCATION_FINE: str = 'android.permission.ACCESS_FINE_LOCATION'
AD_PERMISSION_RECORD: str = 'RECORD'
AD_PERMISSION_STORAGE: str = 'android.permission.WRITE_EXTERNAL_STORAGE'
AD_PERMISSION_STORAGE_READ: str = 'android.permission.READ_EXTERNAL_STORAGE'
AD_PERMISSION_STORAGE_READ_IMAGE: str = 'android.permission.READ_MEDIA_IMAGES'
AD_RECORD_COUNT_DICT: dict = {'ad_buy_item_count': ((3, 'buy_things'),), 'ad_skill_count': ((3, 'skill_cnt_3'),), 'ad_coin_cost': ((10000, 'coin_cost_10000'), (20000, 'coin_cost_20000')), 'ad_kill': ((2, 'kill_cnt_2'), (4, 'kill_cnt_4')), 'ad_mission': ((2, 'task_cnt_2'), (4, 'task_cnt_4'))}
AD_RECORD_FIRST_GAME: str = 'first_game'
AD_RECORD_JOIN_GAME: str = 'battle'
AD_RECORD_KEY_BUY_ITEM_COUNT: str = 'ad_buy_item_count'
AD_RECORD_KEY_COIN_COST: str = 'ad_coin_cost'
AD_RECORD_KEY_KILL: str = 'ad_kill'
AD_RECORD_KEY_MISSION: str = 'ad_mission'
AD_RECORD_KEY_SKILL_COUNT: str = 'ad_skill_count'
AD_RECORD_WIN_GAME: str = 'win_battle'
AIM_ENEMY_FADE_IN_TIME: float = 0.2
AIM_ENEMY_FADE_OUT_TIME: float = 0.5
AIRCRAFT_UNIT_MODEL_ID: int = 662
AIRDROP_MARK_LAND_EFFECT_ID: int = 156
AIRDROP_SHOP_CIRCLE_RANGE: float = 200.0
AIRDROP_SHOP_HIDE_MAP_TAG_TYPES_REVERSE: tuple = (5, 6, 7, 12, 4, 17)
AIRDROP_SHOP_ITEM_ID_UAV: int = 7
AIRDROP_SHOP_UAV_CIRCLE_RANGE: float = 500.0
ALERT_LEVEL_2_THREATEN_TEXT_COLOR: dict = {1: (195, 255, 0), 2: (248, 139, 39), 3: (255, 72, 94)}
ALERT_LEVEL_2_THREATEN_TEXT_ID: dict = {1: 537, 2: 538, 3: 539}
ALL_EMOTION_ICONS: list = [200145, 200146, 200147, 200148, 200149, 200150, 200151, 200152, 200153, 200154, 200155, 200156, 200157, 200158, 200159, 200160, 200161, 200162, 200129, 200130, 200131, 200132, 200133, 200134, 200135, 200136, 200137, 200138, 200139, 200140, 200141, 200142, 200143, 200144, 200001, 200002, 200003, 200004, 200005, 200006, 200007, 200008, 200009, 200010, 200011, 200012, 200013, 200014, 200015, 200016, 200017, 200018, 200019, 200020, 200021, 200022, 200023, 200024, 200025, 200026, 200027, 200028, 200029, 200030, 200031, 200032, 200033, 200034, 200035, 200036, 200037, 200038, 200039, 200040, 200041, 200042, 200043, 200044, 200045, 200046, 200047, 200048, 200049, 200050, 200051, 200052, 200053, 200054, 200055, 200056, 200057, 200058, 200059, 200060, 200061, 200062, 200063, 200064, 200065, 200066, 200067, 200068, 200069, 200070, 200071, 200072, 200073, 200074, 200075, 200076, 200077, 200078, 200079, 200080, 200081, 200082, 200083, 200084, 200085, 200086, 200087, 200088, 200089, 200090, 200091, 200092, 200093, 200094, 200095, 200096, 200097, 200098, 200099]
ALL_LANGUAGES: list = ['zh', 'en', 'es', 'pt', 'th', 'in', 'ru', 'ar', 'vi', 'tw', 'ja']
ALL_SHOW_LANGUAGES: list = ['zh', 'en', 'es', 'pt', 'in', 'th', 'ru', 'ar', 'vi', 'tw', 'ja']
ALL_VOICE_LANGUAGES: list = ['zh', 'en', 'es', 'pt']
AMMO_BOX_AMMO_COLOR: tuple = (255, 240, 97, 255)
AMMO_RECOMMAND_CD: int = 45
AMMO_RECOMMAND_CLOSE_TIME: int = 6
AMMO_RECOMMAND_GAME_TIME: int = 300
AMMO_RECOMMAND_LIMIT: dict = {7: 30, 8: 30, 14: 10}
APPLY_PARA_MASTER_CD: int = 10
APP_CHANNEL: list = ['g83naxx1ena@app_store', 'g83naxx1ena@google_play', 'g83naxx1ena@netease_global', 'g83naxx1me@app_store', 'g83naxx1me@google_play', 'g83naxx1me@netease_global', 'g83naxx2hmt@app_store', 'g83naxx2hmt@google_play', 'g83naxx2vn@app_store', 'g83naxx2vn@google_play', 'steam']
APP_STORE_URL: dict = {'g83naxx1ena@app_store_ios': 'https://apps.apple.com/us/app/blood-strike/id1637059453', 'g83naxx1ena@google_play_android': 'https://play.google.com/store/apps/details?id=com.netease.newspike', 'g83naxx1ena@netease_global_windows': 'https://www.blood-strike.com', 'g83naxx1me@app_store_ios': 'https://apps.apple.com/us/app/blood-strike-mena/id6478942258', 'g83naxx1me@google_play_android': 'https://play.google.com/store/apps/details?id=com.netease.newspikeme', 'g83naxx1me@netease_global_windows': 'https://www.blood-strike.com/ar/index.html', 'g83naxx2hmt@app_store_ios': 'https://apps.apple.com/app/%E8%A1%80%E6%88%B0%E7%AA%81%E6%93%8A/id6505139591', 'g83naxx2hmt@google_play_android': 'https://play.google.com/store/apps/details?id=com.netease.newspiketw', 'g83naxx2vn@app_store_ios': 'https://apps.apple.com/us/app/blood-strike-v%C3%A2y-h%C3%A3m/id6590610850', 'g83naxx2vn@google_play_android': 'https://play.google.com/store/apps/details?id=com.netease.newspikevn'}
ARMOR_ICON_MOVE_SCALE: float = 3.0
ARMOR_LEVEL_BAR_IMG: dict = {1: 10677, 2: 10678, 3: 10679, 4: 10680}
ARMY_MESSAGE_MODIFY: str = '战队宣言'
ARMY_NAME_MODIFY: str = '战队名称'
ARMY_NICKNAME: str = '战队昵称'
ASK_HELP_VISIBLE_TIME: int = 60
ASSIST_AIM_NEW_COUNTRY_CODES: tuple = ('55',)
ASSIST_AIM_NEW_DATA_STAMP: int = 1677859200
AUTO_CANCEL_TEAM_INVITE_TIME: int = 20
AUTO_FIRE_AIM_DISTANCE_DEFAULT: int = 3
AUTO_FIRE_AIM_RADIUS_PIX_DEFAULT: int = 100
AUTO_FIRE_FSM_INTERVAL: float = 0.1
AUTO_FIRE_LOCK_TIME: float = 0.4
AUTO_FIRE_MISS_TIME: float = 0.4
AVATAR_BONE_HEAD: str = 'biped Head'
AVATAR_BONE_LFOOT: str = 'biped L Foot'
AVATAR_BONE_LHAND: str = 'biped L Hand'
AVATAR_BONE_PELVIS: str = 'HP_Pelvis'
AVATAR_BONE_RFOOT: str = 'biped R Foot'
AVATAR_BONE_RHAND: str = 'biped R Hand'
AVATAR_HEIGHT: dict = {0: 1.8, 1: 1.3, 2: 1.8, 3: 1.3, 4: 1.0}
AVATAR_TOPLOGO_BIAS: tuple = (0, 0.5, 0)
AVATAR_TOPLOGO_BONE: str = 'biped Spine1'
AVATAR_TOPLOGO_HIT_ME_SHOW_TIME: float = 3.0
AdsPoseType2AttrName: dict = {0: 'ads_scatter_ratio_stand', 1: 'ads_scatter_ratio_crouch', 2: 'ads_scatter_ratio_jump', 3: 'ads_scatter_ratio_slide', 4: 'ads_scatter_ratio_prone'}
BALLISTIC_EFFECT_PARAM: dict = {'VelocityInRange': (10, 80), 'VelocityOutRange': (150, 250), 'PositionInRange': (10, 80), 'PositionOutRange': (0, 2), 'ScaleXInRange': (10, 80), 'ScaleXOutRange': (0.2, 2), 'ScaleZInRange': (10, 80), 'ScaleZOutRange': (0.2, 0.5), 'AdsVelocityInRange': (10, 80), 'AdsVelocityOutRange': (200, 600), 'AdsPositionInRange': (10, 80), 'AdsPositionOutRange': (0, 0), 'AdsScaleXInRange': (10, 80), 'AdsScaleXOutRange': (0.2, 2), 'AdsScaleZInRange': (10, 80), 'AdsScaleZOutRange': (0.2, 0.6), 'TpsVelocityFactor': 0.5}
BALLISTIC_EFFECT_PARAM_SR: dict = {'VelocityInRange': (10, 80), 'VelocityOutRange': (150, 250), 'PositionInRange': (10, 80), 'PositionOutRange': (0, 0), 'ScaleXInRange': (10, 80), 'ScaleXOutRange': (1, 1), 'ScaleZInRange': (10, 80), 'ScaleZOutRange': (1, 1), 'AdsVelocityInRange': (10, 80), 'AdsVelocityOutRange': (200, 600), 'AdsPositionInRange': (10, 80), 'AdsPositionOutRange': (0, 0), 'AdsScaleXInRange': (10, 80), 'AdsScaleXOutRange': (1, 1), 'AdsScaleZInRange': (10, 80), 'AdsScaleZOutRange': (1, 1), 'TpsVelocityFactor': 0.5}
BAN_INPUT_DRONE: int = 13
BAN_INPUT_EXECUTE: int = 12
BAN_INPUT_HELPING: int = 8
BAN_INPUT_HERO_SELECT: int = 6
BAN_INPUT_REASON_DEAD: int = 1
BAN_INPUT_REASON_GAME_STATE_WAITING: int = 11
BAN_INPUT_REASON_GRAPH_CONTROL: int = 3
BAN_INPUT_REASON_GUN_REFIT: int = 5
BAN_INPUT_REASON_ITEM_USING: int = 4
BAN_INPUT_REASON_LIGHT_ATTACK: int = 10
BAN_INPUT_REASON_RECONNECT: int = 2
BAN_INPUT_REASON_ROOKIEGUIDE: int = 9
BAN_INPUT_VEHICLE: int = 7
BAN_REASON_FIREWALL: int = 3
BAN_REASON_FLASH_BOMB: int = 1
BAN_REASON_KRAKEN: int = 2
BATTLEROYALE_MATCH_ID: int = 1006
BATTLEROYALE_MATCH_ID_RANK: int = 1004
BE_HUNTED_CONTRACT_ID: int = -1
BIG_EVENT_ID: int = 2
BIG_MAP_CHANGE_ICON_SCALE: float = 1.2
BIG_MAP_VEHICLE_SHOW_SCALE: float = 0.5
BLACK_IMG: int = 1000473
BLOOD_DECAL_PARAM: dict = {'prob': 0.4, 'cd': 1.0, 'distance': 5.0, 'max_life': 30.0, 'angle': 0.5}
BOMB_PATH_EFFECT_ID: int = 7
BOMB_PATH_EFFECT_SPEED: float = 30.0
BOMB_PATH_EFFECT_SPEED_LOW: float = 15.0
BOMB_SHOW_CLOSE_DISTANCE: int = 5
BOMB_SHOW_DISTANCE: int = 25
BORDER_FLAG_LEFT_NAME: set = {32, 40, 36}
BORDER_NODE_ROTATE: dict = {4: 90, 8: -90, 16: 0, 32: 180, 64: -90, 20: 45, 36: 135, 24: -45, 40: -135}
BP_ENTRANCE_VX_COLOR: dict = {1: (255, 33, 33, 255), 2: (154, 105, 0, 255), 3: (214, 203, 38, 255), 4: (0, 154, 121, 255), 5: (13, 172, 215, 255), 6: (212, 56, 255, 255)}
BP_ENTRANCE_VX_EXP_COLOR: dict = {1: (255, 104, 104, 255), 2: (255, 211, 104, 255), 3: (255, 253, 70, 255), 4: (104, 255, 253, 255), 5: (104, 255, 253, 255), 6: (255, 188, 60, 255)}
BREAK_STUCK_CD_TIME: int = 1800
BREAK_STUCK_WAIT_TIME: int = 20
BTN_COLOR_FORBIDDEN: tuple = (167, 180, 184)
BTN_COLOR_NORMAL: tuple = (35, 38, 44)
BigMapSelectPosMode2CircleMapTagID: dict = {1: 24, 2: 24}
BigMapSelectPosMode2MagicFieldID: dict = {}
BigMapSelectPosMode2Range: dict = {1: 200.0, 2: 500.0}
BigMapSelectPosMode2TalentAttrType: dict = {}
BoneTestTuple: tuple = ('biped', 'biped Head', 'HP_Spine_L', 'HP_Spine_R', 'biped L Foot', 'biped R Foot')
CALCULATION_COUNTDOWN_TIME: float = 60.0
CALCULATION_TEAMMATE_DISPLAY_TIME: float = 2.8
CALCULATION_VICTORY_RESULT_STAY_TIME: float = 3.0
CAMERA_COLLIDER_TARGET_POS_OFFSET: tuple = (0, 1.8, 0)
CAMERA_COLLIDER_TARGET_POS_OFFSET_VEHICLE: tuple = (0, 3, 0)
CAMERA_ID_AIRPLANE: int = 3
CAMERA_ID_ALS_TPS: int = 9
CAMERA_ID_CALCULATION: int = 13
CAMERA_ID_CHARACTER_TPS: int = 8
CAMERA_ID_COMMON_TPS: int = 5
CAMERA_ID_DEATH: int = 7
CAMERA_ID_DEFAULT: int = 0
CAMERA_ID_DYING: int = 12
CAMERA_ID_EMOTE: int = 19
CAMERA_ID_EXECUTE: int = 18
CAMERA_ID_FREEFALL: int = 1
CAMERA_ID_FREEFALL_FROM_CLOSE_PARACHUTE: int = 20
CAMERA_ID_GREAT_SWORD: int = 27
CAMERA_ID_HELICOPTER: int = 21
CAMERA_ID_HELICOPTER_LEANOUT: int = 22
CAMERA_ID_HELICOPTER_LEANOUT_LB: int = 24
CAMERA_ID_HELICOPTER_LEANOUT_RB: int = 23
CAMERA_ID_INTRO_CINEMATICS: int = 17
CAMERA_ID_LANDGROUND: int = 4
CAMERA_ID_LIGHT_ATTACK: int = 16
CAMERA_ID_LOOK_AROUND: int = 25
CAMERA_ID_NEW_MISSILE_SPELL: int = 29
CAMERA_ID_PARACHUTE: int = 26
CAMERA_ID_STROP: int = 6
CAMERA_ID_VEHICLE: int = 10
CAMERA_ID_VEHICLE_LEANOUT: int = 11
CAMERA_ID_VEHICLE_LEANOUT_LB: int = 15
CAMERA_ID_VEHICLE_LEANOUT_RB: int = 14
CANCEL_EXECUTE_CD_TIME: float = 0.3
CAN_ROTATE_GUN_ON_TOUCH_END: bool = True
CHAR_CTRL_HEIGHT_SIZE: dict = {1: 0.1, 2: 0.2, 3: 0.3}
CHECK_ADS_MARK_INTERVAL: float = 0.2
CHECK_AIM_ENEMY_INTERVAL: float = 0.2
CHECK_AIM_ENEMY_MAX_DISTANCE: int = 500
CHECK_CAMERA_INTERVAL: float = 0.5
CHECK_STROP_ENTER_SHOOT_TEST: bool = True
CHECK_SUPER_SPRINT_WHEN_STATE_END: set = {66, 6, 8, 42, 43, 12, 45, 19, 57}
CHIP_SWITCHES: bool = False
CLAN_MESSAGE_CREATE: str = '兵团宣言创建'
CLAN_MESSAGE_MODIFY: str = '兵团宣言修改'
CLAN_NAME_CREATE: str = '兵团名称创建'
CLAN_NAME_MODIFY: str = '兵团改名'
CLIENT_PRIORITY_UNIT_STATE: tuple = ('Swim', 'ClimbLadder')
COMBAT_CACHE_CSB_PATH: set = {'UIScript/ig_hud_right_jumpword.csb', 'UIScript/node_ig_escape_hud_mark.csb', 'UIScript/ig_hud_left_killrecord.csb', 'UIScript/node_c_handle_icon.csb', 'UIScript/node_ig_escape_hud_edgemask_new.csb'}
COMBAT_CACHE_CSB_PATH_PC: set = {'UIScript/ig_hud_right_jumpword_pc.csb', 'UIScript/node_ig_escape_hud_mark.csb', 'UIScript/ig_hud_left_killrecord.csb', 'UIScript/node_c_handle_icon.csb', 'UIScript/node_ig_escape_hud_edgemask_new.csb'}
COMBAT_CACHE_TIMELINE_PATH: set = {'UIScript/node_ig_escape_hud_mark.csb', 'UIScript/ig_hud_right_jumpword.csb', 'UIScript/ig_hud_left_killrecord.csb', 'UIScript/node_ig_escape_hud_edgemask_new.csb'}
COMBAT_CACHE_TIMELINE_PATH_PC: set = {'UIScript/ig_hud_left_killrecord.csb', 'UIScript/node_ig_escape_hud_mark.csb', 'UIScript/ig_hud_right_jumpword_pc.csb', 'UIScript/node_ig_escape_hud_edgemask_new.csb'}
COMBAT_ITEM_EFFECT_VISIBLE_DISTANCE: int = 6400
COMBAT_ITEM_MARK_LEVEL_2_COLOR: dict = {1: (255, 255, 255), 2: (36, 139, 255), 3: (207, 78, 255), 4: (238, 214, 56)}
COMBAT_ITEM_MARK_LEVEL_2_TEXT_COLOR: dict = {1: (255, 255, 255, 255), 2: (36, 139, 255, 255), 3: (207, 78, 255, 255), 4: (238, 214, 56, 255), 5: (255, 101, 101, 255)}
COMBAT_ITEM_SCALE_EFFECT_DISTANCE: int = 100
COMBAT_ITEM_SCALE_EFFECT_SCALE: float = 0.5
COMMON_CACHE_CSB_PATH: set = {'UIScript/node_ig_escape_bobao_skin_skill.csb', 'UIScript/node_ig_hud_grenade_explosion_prompt.csb', 'UIScript/node_ig_stronghold_name.csb', 'UIScript/node_ig_escape_hud_edgemask_2.csb', 'UIScript/node_ig_escape_map_biaoji.csb'}
COMMON_CACHE_CSB_PATH_PC: set = {'UIScript/node_ig_escape_bobao_skin_skill.csb', 'UIScript/node_ig_hud_grenade_explosion_prompt.csb', 'UIScript/node_ig_stronghold_name_pc.csb', 'UIScript/node_ig_escape_hud_edgemask_2.csb', 'UIScript/node_ig_escape_map_biaoji.csb'}
COMMON_CACHE_TIMELINE_PATH: set = {'UIScript/node_chat_mine.csb', 'UIScript/node_ig_escape_map_biaoji.csb', 'UIScript/node_chat_other.csb', 'UIScript/node_chat_message.csb', 'UIScript/node_ig_escape_hud_edgemask_2.csb'}
COMMON_CACHE_TIMELINE_PATH_add: builtin_function_or_method = <built-in method add of set object at 0x703aca4200>
COMMON_TOPLOGO_OFFSET_OCCUPY: tuple = (0, 2, 0)
CONTINUE_KILL_COUNT_FOR_VX_EFFECT: int = 5
CROUCH_WAY_CLICK: int = 0
CROUCH_WAY_LONG_CLICK: int = 1
CROUCH_WAY_ONE_CLICK_CP: int = 2
CUE_AUTO_POP_GRAPH: int = 32902
CUE_AUTO_PUSH_GRAPH: int = 32901
CUE_DOCKING_DETECT: int = 32817
CUE_SINGAL_EVENT: int = 32761
CUE_SINGAL_PLAYER_EVENT: int = 1000
CUE_SINGAL_REPLAY_ROBOT_EVENT: int = 1001
CUE_TYPE_ADS_STATE: int = 9
CUE_TYPE_AIRPLANE_ENV_PARAM: int = 41
CUE_TYPE_ANIM_END_DETACH_ITEMCASE_SFX: int = 60
CUE_TYPE_ANIM_END_DETACH_MELEE_SFX: int = 58
CUE_TYPE_ANIM_END_DETACH_SFX: int = 56
CUE_TYPE_ATTACH_EXECUTE_FREEZE_MODEL: int = 65
CUE_TYPE_ATTACH_LEFTHAND_WEAPON: int = 24
CUE_TYPE_ATTACH_NORMAL_MODEL: int = 62
CUE_TYPE_BAN_HANDIK: int = 28
CUE_TYPE_BREAK_UNITSTATE: int = 19
CUE_TYPE_CAMERA_SFX: int = 5
CUE_TYPE_CLEAR_GUN_SFX: int = 42
CUE_TYPE_CREEP_STAND_OK: int = 31
CUE_TYPE_DELAY_FIRE: int = 18
CUE_TYPE_EFFECT_ATTACH_DETACH: int = 32
CUE_TYPE_ENABLE_HANDIK: int = 12
CUE_TYPE_EXECUTE_THIRD_PERSON_MODEL: int = 63
CUE_TYPE_FIRE_BREAK: int = 21
CUE_TYPE_FIRE_END: int = 2
CUE_TYPE_FOOT: int = 25
CUE_TYPE_FPS_CAMERA_HAND_OFFSET_ENABLE: int = 36
CUE_TYPE_FPS_CAMERA_ROTATE: int = 33
CUE_TYPE_FPS_CAMERA_ROTATE_ENABLE: int = 34
CUE_TYPE_GUNFIRE_SOUND_EVENT: int = 54
CUE_TYPE_GUN_ANIM_SFX: int = 55
CUE_TYPE_GUN_FIRE_BULLET_EFFECT: int = 39
CUE_TYPE_GUN_FIRE_CAMERA_EFFECT: int = 40
CUE_TYPE_GUN_FIRE_MUZZLE_EFFECT: int = 38
CUE_TYPE_GUN_SFX: int = 6
CUE_TYPE_HAND_ANIM_SFX: int = 61
CUE_TYPE_HAND_MOVESTATE_CHANGE: int = 17
CUE_TYPE_HIDE_WEAPON: int = 27
CUE_TYPE_ITEMCASE_ANIM_SFX: int = 59
CUE_TYPE_LEFTHAND_WEAPON_SFX: int = 64
CUE_TYPE_MELEE_ANIM_SFX: int = 57
CUE_TYPE_MOTION_BLUR_TO_PERCENT: int = 29
CUE_TYPE_OPTIC_MODEL_CHANGE: int = 22
CUE_TYPE_RELOAD_AMMO: int = 16
CUE_TYPE_RELOAD_CAMERA_AIM: int = 26
CUE_TYPE_RELOAD_CHARGER_CONTROL: int = 13
CUE_TYPE_RELOAD_END: int = 14
CUE_TYPE_SEND_EVENT_TO_3P: int = 37
CUE_TYPE_SOUND_BREAK: int = 23
CUE_TYPE_SOUND_EVENT: int = 8
CUE_TYPE_SOUND_FAR_EVENT: int = 7
CUE_TYPE_SPELL_EVENT: int = 3
CUE_TYPE_SPELL_READY_EVENT: int = 67
CUE_TYPE_SWITCH_WEAPON: int = 20
CUE_TYPE_VARIABLE_EVENT_SYNC_STACK: int = 30
CUE_TYPE_VARIABLE_HAND_TO_WEAPON: int = 66
CUE_TYPE_WEAPON_ATTACH: int = 11
CUE_TYPE_WEAPON_SHOW_EFFECT: int = 53
CURRENT_ENGINE_VERSION: int = 650002
CURSOR_DISPLAYED_REASON_FOR_AIRDROP: int = 5
CURSOR_DISPLAYED_REASON_FOR_BACKPACK: int = 4
CURSOR_DISPLAYED_REASON_FOR_BIG_MAP: int = 13
CURSOR_DISPLAYED_REASON_FOR_CALCULATION: int = 2
CURSOR_DISPLAYED_REASON_FOR_FIELD_SHOP: int = 14
CURSOR_DISPLAYED_REASON_FOR_GAMETIPS: int = 8
CURSOR_DISPLAYED_REASON_FOR_GUNREFIT: int = 7
CURSOR_DISPLAYED_REASON_FOR_HALL: int = 18
CURSOR_DISPLAYED_REASON_FOR_HERO_CHOOSE: int = 11
CURSOR_DISPLAYED_REASON_FOR_INPUT_CTRL: int = 15
CURSOR_DISPLAYED_REASON_FOR_PARA_TRAINER_CHOOSE: int = 10
CURSOR_DISPLAYED_REASON_FOR_PC_GAME_CHAT: int = 19
CURSOR_DISPLAYED_REASON_FOR_PICKUP_LIST: int = 17
CURSOR_DISPLAYED_REASON_FOR_REPLAY: int = 1
CURSOR_DISPLAYED_REASON_FOR_SCOREBOARD: int = 16
CURSOR_DISPLAYED_REASON_FOR_SETTING: int = 9
CURSOR_DISPLAYED_REASON_FOR_SHOP: int = 6
CURSOR_DISPLAYED_REASON_FOR_TALENT_CHOOSE: int = 3
CURSOR_DISPLAYED_REASON_FOR_VEHICLE_SEAT_CHANGE: int = 12
CUSTOMER_SERVICE_URL: str = 'https://gm.163.com/user_help.html?paper_id=4415'
CUSTOM_FACE_SHOW_TYPE: list = [2000, 2001, 2002, 2003, 1001, 1002, 1006, 1003, 1004, 1005]
CameraEasingType: dict = {'linear': 0, 'easeInSine': 1, 'easeOutSine': 2, 'easeInOutSine': 3, 'easeInQuad': 4, 'easeOutQuad': 5, 'easeInOutQuad': 6, 'easeInCubic': 7, 'easeOutCubic': 8, 'easeInOutCubic': 9, 'easeInQuart': 10, 'easeOutQuart': 11, 'easeInOutQuart': 12, 'easeInQuint': 13, 'easeOutQuint': 14, 'easeInOutQuint': 15, 'easeInExpo': 16, 'easeOutExpo': 17, 'easeInOutExpo': 18, 'easeInCirc': 19, 'easeOutCirc': 20, 'easeInOutCirc': 21, 'easeInBack': 22, 'easeOutBack': 23, 'easeInOutBack': 24, 'easeInElastic': 25, 'easeOutElastic': 26, 'easeInOutElastic': 27, 'easeInBounce': 28, 'easeOutBounce': 29, 'easeInOutBounce': 30}
ControllerSystemModeValue: dict = {1: 4, 2: 8, 3: 12}
DAOJU_EMPTY_TEXTURE: dict = {3: 142, 4: 143, 9: 141, 10: 144, 20: 140}
DATA_CACHE_NAME_COMBAT_HISTORY: str = 'CombatHistory'
DATA_CACHE_NAME_LBS_GUN_INFO: str = 'LBSGunInfo'
DATA_CACHE_NAME_LBS_TOTAL_RANK: str = 'LBSTotalRankInfo'
DATA_CACHE_NAME_YEAR_REVIEW_DATA: str = 'YEAR_REVIEW_DATA'
DATA_CACHE_NAME_ZONE_INFO: str = 'ZoneCombatInfo'
DEBRUIJN32_LOOKUP: tuple = (0, 1, 28, 2, 29, 14, 24, 3, 30, 22, 20, 15, 25, 17, 4, 8, 31, 27, 13, 23, 21, 19, 16, 7, 26, 12, 18, 6, 11, 5, 10, 9)
DEBRUIJN32_NUMBER: int = 125613361
DEBUFF_TIPS_OPEN: bool = True
DEBUG_PRINT_PARACHUTE_SPEED: bool = False
DEBUG_SHOW_PC_TIPS: bool = True
DEFAULT_EXECUTE_INFO: tuple = (18, 0)
DEFAULT_HALL_SUIT_ID: int = 3000000010
DEFAULT_HERO_FPS_MODEL: int = 229
DEFAULT_HERO_MODEL_ID: int = 58
DEFAULT_JUMP_TOP_HEIGHT: int = -100
DEFAULT_LOGIN_VIDEO_NAME: str = 'og_login_video.mp4'
DEFAULT_MAX_BUY_LIMIT: int = 50
DEFAULT_ROOT_LEVEL_NAME: str = '$root'
DEFAULT_USE_FPS_CAMERA_ON_PARACHUTE: bool = True
DELAY_SHOOT_REASON_EMPTY_AMMO: int = 9
DELAY_SHOOT_REASON_FOR_CLIMB: int = 10
DELAY_SHOOT_REASON_FOR_CROSS: int = 11
DELAY_SHOOT_REASON_FOR_FIRE_REAL_ADS: int = 5
DELAY_SHOOT_REASON_FOR_LEFTHAND_BOMB: int = 12
DELAY_SHOOT_REASON_FOR_RAISEWEAPON: int = 1
DELAY_SHOOT_REASON_FOR_RECHAMBER: int = 4
DELAY_SHOOT_REASON_FOR_RELOAD: int = 3
DELAY_SHOOT_REASON_FOR_RELOAD_BREAK: int = 7
DELAY_SHOOT_REASON_FOR_SERVER_RELOAD: int = 13
DELAY_SHOOT_REASON_FOR_SPRINT: int = 2
DELAY_SHOOT_REASON_FOR_STROP: int = 8
DELAY_SHOOT_REASON_FOR_WAIT_MODEL_CUE: int = 6
DOCKING_MARK_EDGE_DISTANCE: float = 0.5
DOUBLE_EXP_2_ICON_ITEM: dict = {1: 41000000700, 3: 41000000400, 2: 41000003502}
EFFECT_FOV_SCALE_PARAM: dict = {'base_fov': 70, 'base_scale_factor': 1.0}
EInputType_ALPHABER: int = 2
EInputType_ALPHANUMERIC: int = 3
EInputType_EMAILADDRESS: int = 4
EInputType_NONE: int = 6
EInputType_NORMAL: int = 0
EInputType_NUMBER: int = 1
EInputType_PASSWORD: int = 5
ENEMY_TOPLOGO_VISIBLE_HEIGHT: dict = {0: 1.1, 1: 0.5, 4: 0.5}
ENGINE_VERSION_2024_OR_NEWER: bool = False
ENGINE_VERSION_VEHICLE_CCT: bool = True
EPostProcessGroup_AfterTonemapping: int = 4
EPostProcessGroup_BeforeAll: int = 0
EPostProcessGroup_BeforeSky: int = 1
EPostProcessGroup_BeforeTonemapping: int = 3
EPostProcessGroup_BeforeTranslucency: int = 2
EPostProcessGroup_BeforeUI: int = 5
EPostProcessGroup_Max: int = 6
ESetting_Base_Sensitivity_Factor: dict = {'sight_sensitivity': 5e-05, 'sight_sensitivity_x': 5e-05, 'sight_sensitivity_y': 5e-05, 'sight_sensitivity_reddot': 3.87109e-05, 'sight_sensitivity_reddot_x': 3.87109e-05, 'sight_sensitivity_reddot_y': 3.87109e-05, 'sight_sensitivity_2x': 2.65178e-05, 'sight_sensitivity_2x_x': 2.65178e-05, 'sight_sensitivity_2x_y': 2.65178e-05, 'sight_sensitivity_3x': 1.84362e-05, 'sight_sensitivity_3x_x': 1.84362e-05, 'sight_sensitivity_3x_y': 1.84362e-05, 'sight_sensitivity_4x': 1.40477e-05, 'sight_sensitivity_4x_x': 1.40477e-05, 'sight_sensitivity_4x_y': 1.40477e-05, 'sight_sensitivity_6x': 9.4755e-06, 'sight_sensitivity_6x_x': 9.4755e-06, 'sight_sensitivity_6x_y': 9.4755e-06, 'sight_sensitivity_8x': 8.1424e-06, 'sight_sensitivity_8x_x': 8.1424e-06, 'sight_sensitivity_8x_y': 8.1424e-06, 'fire_sensitivity': 5e-05, 'fire_sensitivity_x': 5e-05, 'fire_sensitivity_y': 5e-05, 'fire_sensitivity_reddot': 3.87109e-05, 'fire_sensitivity_reddot_x': 3.87109e-05, 'fire_sensitivity_reddot_y': 3.87109e-05, 'fire_sensitivity_2x': 2.65178e-05, 'fire_sensitivity_2x_x': 2.65178e-05, 'fire_sensitivity_2x_y': 2.65178e-05, 'fire_sensitivity_3x': 1.84362e-05, 'fire_sensitivity_3x_x': 1.84362e-05, 'fire_sensitivity_3x_y': 1.84362e-05, 'fire_sensitivity_4x': 1.40477e-05, 'fire_sensitivity_4x_x': 1.40477e-05, 'fire_sensitivity_4x_y': 1.40477e-05, 'fire_sensitivity_6x': 9.4755e-06, 'fire_sensitivity_6x_x': 9.4755e-06, 'fire_sensitivity_6x_y': 9.4755e-06, 'fire_sensitivity_8x': 8.1424e-06, 'fire_sensitivity_8x_x': 8.1424e-06, 'fire_sensitivity_8x_y': 8.1424e-06}
ESetting_Controller_Base_Sensitivity_Factor: dict = {'controller_sight_sensitivity': 0.015, 'controller_sight_sensitivity_x': 0.015, 'controller_sight_sensitivity_y': 0.015, 'controller_sight_sensitivity_reddot': 0.01161327, 'controller_sight_sensitivity_reddot_x': 0.01161327, 'controller_sight_sensitivity_reddot_y': 0.01161327, 'controller_sight_sensitivity_2x': 0.00795534, 'controller_sight_sensitivity_2x_x': 0.00795534, 'controller_sight_sensitivity_2x_y': 0.00795534, 'controller_sight_sensitivity_3x': 0.00553086, 'controller_sight_sensitivity_3x_x': 0.00553086, 'controller_sight_sensitivity_3x_y': 0.00553086, 'controller_sight_sensitivity_4x': 0.00421431, 'controller_sight_sensitivity_4x_x': 0.00421431, 'controller_sight_sensitivity_4x_y': 0.00421431, 'controller_sight_sensitivity_6x': 0.00284265, 'controller_sight_sensitivity_6x_x': 0.00284265, 'controller_sight_sensitivity_6x_y': 0.00284265, 'controller_sight_sensitivity_8x': 0.00244272, 'controller_sight_sensitivity_8x_x': 0.00244272, 'controller_sight_sensitivity_8x_y': 0.00244272, 'controller_fire_sensitivity': 0.015, 'controller_fire_sensitivity_x': 0.015, 'controller_fire_sensitivity_y': 0.015, 'controller_fire_sensitivity_reddot': 0.01161327, 'controller_fire_sensitivity_reddot_x': 0.01161327, 'controller_fire_sensitivity_reddot_y': 0.01161327, 'controller_fire_sensitivity_2x': 0.00795534, 'controller_fire_sensitivity_2x_x': 0.00795534, 'controller_fire_sensitivity_2x_y': 0.00795534, 'controller_fire_sensitivity_3x': 0.00553086, 'controller_fire_sensitivity_3x_x': 0.00553086, 'controller_fire_sensitivity_3x_y': 0.00553086, 'controller_fire_sensitivity_4x': 0.00421431, 'controller_fire_sensitivity_4x_x': 0.00421431, 'controller_fire_sensitivity_4x_y': 0.00421431, 'controller_fire_sensitivity_6x': 0.00284265, 'controller_fire_sensitivity_6x_x': 0.00284265, 'controller_fire_sensitivity_6x_y': 0.00284265, 'controller_fire_sensitivity_8x': 0.00244272, 'controller_fire_sensitivity_8x_x': 0.00244272, 'controller_fire_sensitivity_8x_y': 0.00244272}
ESetting_Controller_Fire_Panel_Name: list = [('controller_fire_sensitivity', 'controller_fire_sensitivity_x', 'controller_fire_sensitivity_y'), ('controller_fire_sensitivity_reddot', 'controller_fire_sensitivity_reddot_x', 'controller_fire_sensitivity_reddot_y'), ('controller_fire_sensitivity_2x', 'controller_fire_sensitivity_2x_x', 'controller_fire_sensitivity_2x_y'), ('controller_fire_sensitivity_3x', 'controller_fire_sensitivity_3x_x', 'controller_fire_sensitivity_3x_y'), ('controller_fire_sensitivity_4x', 'controller_fire_sensitivity_4x_x', 'controller_fire_sensitivity_4x_y'), ('controller_fire_sensitivity_6x', 'controller_fire_sensitivity_6x_x', 'controller_fire_sensitivity_6x_y'), ('controller_fire_sensitivity_8x', 'controller_fire_sensitivity_8x_x', 'controller_fire_sensitivity_8x_y')]
ESetting_Controller_Sight_Panel_Name: list = [('controller_sight_sensitivity', 'controller_sight_sensitivity_x', 'controller_sight_sensitivity_y'), ('controller_sight_sensitivity_reddot', 'controller_sight_sensitivity_reddot_x', 'controller_sight_sensitivity_reddot_y'), ('controller_sight_sensitivity_2x', 'controller_sight_sensitivity_2x_x', 'controller_sight_sensitivity_2x_y'), ('controller_sight_sensitivity_3x', 'controller_sight_sensitivity_3x_x', 'controller_sight_sensitivity_3x_y'), ('controller_sight_sensitivity_4x', 'controller_sight_sensitivity_4x_x', 'controller_sight_sensitivity_4x_y'), ('controller_sight_sensitivity_6x', 'controller_sight_sensitivity_6x_x', 'controller_sight_sensitivity_6x_y'), ('controller_sight_sensitivity_8x', 'controller_sight_sensitivity_8x_x', 'controller_sight_sensitivity_8x_y')]
ESetting_Controller_Slider_Fire_Range: dict = {'controller_fire_sensitivity': [1, 15], 'controller_fire_sensitivity_x': [1, 15], 'controller_fire_sensitivity_y': [1, 15], 'controller_fire_sensitivity_reddot': [1, 15], 'controller_fire_sensitivity_reddot_x': [1, 15], 'controller_fire_sensitivity_reddot_y': [1, 15], 'controller_fire_sensitivity_2x': [1, 15], 'controller_fire_sensitivity_2x_x': [1, 15], 'controller_fire_sensitivity_2x_y': [1, 15], 'controller_fire_sensitivity_3x': [1, 15], 'controller_fire_sensitivity_3x_x': [1, 15], 'controller_fire_sensitivity_3x_y': [1, 15], 'controller_fire_sensitivity_4x': [1, 15], 'controller_fire_sensitivity_4x_x': [1, 15], 'controller_fire_sensitivity_4x_y': [1, 15], 'controller_fire_sensitivity_6x': [1, 15], 'controller_fire_sensitivity_6x_x': [1, 15], 'controller_fire_sensitivity_6x_y': [1, 15], 'controller_fire_sensitivity_8x': [1, 15], 'controller_fire_sensitivity_8x_x': [1, 15], 'controller_fire_sensitivity_8x_y': [1, 15]}
ESetting_Controller_Slider_Sight_Fire_Range: dict = {'controller_sight_sensitivity': [1, 15], 'controller_sight_sensitivity_x': [1, 15], 'controller_sight_sensitivity_y': [1, 15], 'controller_sight_sensitivity_reddot': [1, 15], 'controller_sight_sensitivity_reddot_x': [1, 15], 'controller_sight_sensitivity_reddot_y': [1, 15], 'controller_sight_sensitivity_2x': [1, 15], 'controller_sight_sensitivity_2x_x': [1, 15], 'controller_sight_sensitivity_2x_y': [1, 15], 'controller_sight_sensitivity_3x': [1, 15], 'controller_sight_sensitivity_3x_x': [1, 15], 'controller_sight_sensitivity_3x_y': [1, 15], 'controller_sight_sensitivity_4x': [1, 15], 'controller_sight_sensitivity_4x_x': [1, 15], 'controller_sight_sensitivity_4x_y': [1, 15], 'controller_sight_sensitivity_6x': [1, 15], 'controller_sight_sensitivity_6x_x': [1, 15], 'controller_sight_sensitivity_6x_y': [1, 15], 'controller_sight_sensitivity_8x': [1, 15], 'controller_sight_sensitivity_8x_x': [1, 15], 'controller_sight_sensitivity_8x_y': [1, 15], 'controller_fire_sensitivity': [1, 15], 'controller_fire_sensitivity_x': [1, 15], 'controller_fire_sensitivity_y': [1, 15], 'controller_fire_sensitivity_reddot': [1, 15], 'controller_fire_sensitivity_reddot_x': [1, 15], 'controller_fire_sensitivity_reddot_y': [1, 15], 'controller_fire_sensitivity_2x': [1, 15], 'controller_fire_sensitivity_2x_x': [1, 15], 'controller_fire_sensitivity_2x_y': [1, 15], 'controller_fire_sensitivity_3x': [1, 15], 'controller_fire_sensitivity_3x_x': [1, 15], 'controller_fire_sensitivity_3x_y': [1, 15], 'controller_fire_sensitivity_4x': [1, 15], 'controller_fire_sensitivity_4x_x': [1, 15], 'controller_fire_sensitivity_4x_y': [1, 15], 'controller_fire_sensitivity_6x': [1, 15], 'controller_fire_sensitivity_6x_x': [1, 15], 'controller_fire_sensitivity_6x_y': [1, 15], 'controller_fire_sensitivity_8x': [1, 15], 'controller_fire_sensitivity_8x_x': [1, 15], 'controller_fire_sensitivity_8x_y': [1, 15]}
ESetting_Controller_Slider_Sight_Range: dict = {'controller_sight_sensitivity': [1, 15], 'controller_sight_sensitivity_x': [1, 15], 'controller_sight_sensitivity_y': [1, 15], 'controller_sight_sensitivity_reddot': [1, 15], 'controller_sight_sensitivity_reddot_x': [1, 15], 'controller_sight_sensitivity_reddot_y': [1, 15], 'controller_sight_sensitivity_2x': [1, 15], 'controller_sight_sensitivity_2x_x': [1, 15], 'controller_sight_sensitivity_2x_y': [1, 15], 'controller_sight_sensitivity_3x': [1, 15], 'controller_sight_sensitivity_3x_x': [1, 15], 'controller_sight_sensitivity_3x_y': [1, 15], 'controller_sight_sensitivity_4x': [1, 15], 'controller_sight_sensitivity_4x_x': [1, 15], 'controller_sight_sensitivity_4x_y': [1, 15], 'controller_sight_sensitivity_6x': [1, 15], 'controller_sight_sensitivity_6x_x': [1, 15], 'controller_sight_sensitivity_6x_y': [1, 15], 'controller_sight_sensitivity_8x': [1, 15], 'controller_sight_sensitivity_8x_x': [1, 15], 'controller_sight_sensitivity_8x_y': [1, 15]}
ESetting_Fire_Panel_Name: list = [('fire_sensitivity', 'fire_sensitivity_x', 'fire_sensitivity_y'), ('fire_sensitivity_reddot', 'fire_sensitivity_reddot_x', 'fire_sensitivity_reddot_y'), ('fire_sensitivity_2x', 'fire_sensitivity_2x_x', 'fire_sensitivity_2x_y'), ('fire_sensitivity_3x', 'fire_sensitivity_3x_x', 'fire_sensitivity_3x_y'), ('fire_sensitivity_4x', 'fire_sensitivity_4x_x', 'fire_sensitivity_4x_y'), ('fire_sensitivity_6x', 'fire_sensitivity_6x_x', 'fire_sensitivity_6x_y'), ('fire_sensitivity_8x', 'fire_sensitivity_8x_x', 'fire_sensitivity_8x_y')]
ESetting_Sight_Panel_Name: list = [('sight_sensitivity', 'sight_sensitivity_x', 'sight_sensitivity_y'), ('sight_sensitivity_reddot', 'sight_sensitivity_reddot_x', 'sight_sensitivity_reddot_y'), ('sight_sensitivity_2x', 'sight_sensitivity_2x_x', 'sight_sensitivity_2x_y'), ('sight_sensitivity_3x', 'sight_sensitivity_3x_x', 'sight_sensitivity_3x_y'), ('sight_sensitivity_4x', 'sight_sensitivity_4x_x', 'sight_sensitivity_4x_y'), ('sight_sensitivity_6x', 'sight_sensitivity_6x_x', 'sight_sensitivity_6x_y'), ('sight_sensitivity_8x', 'sight_sensitivity_8x_x', 'sight_sensitivity_8x_y')]
ESetting_Slider_Fire_Range: dict = {'fire_sensitivity': [1, 300], 'fire_sensitivity_x': [1, 300], 'fire_sensitivity_y': [1, 300], 'fire_sensitivity_reddot': [1, 300], 'fire_sensitivity_reddot_x': [1, 300], 'fire_sensitivity_reddot_y': [1, 300], 'fire_sensitivity_2x': [1, 300], 'fire_sensitivity_2x_x': [1, 300], 'fire_sensitivity_2x_y': [1, 300], 'fire_sensitivity_3x': [1, 300], 'fire_sensitivity_3x_x': [1, 300], 'fire_sensitivity_3x_y': [1, 300], 'fire_sensitivity_4x': [1, 300], 'fire_sensitivity_4x_x': [1, 300], 'fire_sensitivity_4x_y': [1, 300], 'fire_sensitivity_6x': [1, 300], 'fire_sensitivity_6x_x': [1, 300], 'fire_sensitivity_6x_y': [1, 300], 'fire_sensitivity_8x': [1, 300], 'fire_sensitivity_8x_x': [1, 300], 'fire_sensitivity_8x_y': [1, 300]}
ESetting_Slider_Gyroscope_Input_Cutoff_Range: list = [0, 100]
ESetting_Slider_Gyroscope_Input_Cutoff_Range_Real: list = [0, 0.05]
ESetting_Slider_Gyroscope_Sens_Mapper_Range: list = [0, 20]
ESetting_Slider_Gyroscope_Sens_Normal_Range: dict = {'gyroscope_sensitivity': [0, 300], 'gyroscope_sensitivity_reddot': [0, 300], 'gyroscope_sensitivity_2x': [0, 300], 'gyroscope_sensitivity_3x': [0, 300], 'gyroscope_sensitivity_4x': [0, 300], 'gyroscope_sensitivity_6x': [0, 300], 'gyroscope_sensitivity_8x': [0, 300]}
ESetting_Slider_Gyroscope_Sens_Shoot_Range: dict = {'gyroscope_shoot_sensitivity': [0, 300], 'gyroscope_shoot_sensitivity_reddot': [0, 300], 'gyroscope_shoot_sensitivity_2x': [0, 300], 'gyroscope_shoot_sensitivity_3x': [0, 300], 'gyroscope_shoot_sensitivity_4x': [0, 300], 'gyroscope_shoot_sensitivity_6x': [0, 300], 'gyroscope_shoot_sensitivity_8x': [0, 300]}
ESetting_Slider_MiniMapScale_Range: list = [20.0, 100.0]
ESetting_Slider_MiniMapScale_Range_Real: list = [1, 1.5]
ESetting_Slider_SceneViewFov_Range: list = [60, 120]
ESetting_Slider_Sight_Fire_Range: dict = {'sight_sensitivity': [1, 300], 'sight_sensitivity_x': [1, 300], 'sight_sensitivity_y': [1, 300], 'sight_sensitivity_reddot': [1, 300], 'sight_sensitivity_reddot_x': [1, 300], 'sight_sensitivity_reddot_y': [1, 300], 'sight_sensitivity_2x': [1, 300], 'sight_sensitivity_2x_x': [1, 300], 'sight_sensitivity_2x_y': [1, 300], 'sight_sensitivity_3x': [1, 300], 'sight_sensitivity_3x_x': [1, 300], 'sight_sensitivity_3x_y': [1, 300], 'sight_sensitivity_4x': [1, 300], 'sight_sensitivity_4x_x': [1, 300], 'sight_sensitivity_4x_y': [1, 300], 'sight_sensitivity_6x': [1, 300], 'sight_sensitivity_6x_x': [1, 300], 'sight_sensitivity_6x_y': [1, 300], 'sight_sensitivity_8x': [1, 300], 'sight_sensitivity_8x_x': [1, 300], 'sight_sensitivity_8x_y': [1, 300], 'fire_sensitivity': [1, 300], 'fire_sensitivity_x': [1, 300], 'fire_sensitivity_y': [1, 300], 'fire_sensitivity_reddot': [1, 300], 'fire_sensitivity_reddot_x': [1, 300], 'fire_sensitivity_reddot_y': [1, 300], 'fire_sensitivity_2x': [1, 300], 'fire_sensitivity_2x_x': [1, 300], 'fire_sensitivity_2x_y': [1, 300], 'fire_sensitivity_3x': [1, 300], 'fire_sensitivity_3x_x': [1, 300], 'fire_sensitivity_3x_y': [1, 300], 'fire_sensitivity_4x': [1, 300], 'fire_sensitivity_4x_x': [1, 300], 'fire_sensitivity_4x_y': [1, 300], 'fire_sensitivity_6x': [1, 300], 'fire_sensitivity_6x_x': [1, 300], 'fire_sensitivity_6x_y': [1, 300], 'fire_sensitivity_8x': [1, 300], 'fire_sensitivity_8x_x': [1, 300], 'fire_sensitivity_8x_y': [1, 300]}
ESetting_Slider_Sight_Range: dict = {'sight_sensitivity': [1, 300], 'sight_sensitivity_x': [1, 300], 'sight_sensitivity_y': [1, 300], 'sight_sensitivity_reddot': [1, 300], 'sight_sensitivity_reddot_x': [1, 300], 'sight_sensitivity_reddot_y': [1, 300], 'sight_sensitivity_2x': [1, 300], 'sight_sensitivity_2x_x': [1, 300], 'sight_sensitivity_2x_y': [1, 300], 'sight_sensitivity_3x': [1, 300], 'sight_sensitivity_3x_x': [1, 300], 'sight_sensitivity_3x_y': [1, 300], 'sight_sensitivity_4x': [1, 300], 'sight_sensitivity_4x_x': [1, 300], 'sight_sensitivity_4x_y': [1, 300], 'sight_sensitivity_6x': [1, 300], 'sight_sensitivity_6x_x': [1, 300], 'sight_sensitivity_6x_y': [1, 300], 'sight_sensitivity_8x': [1, 300], 'sight_sensitivity_8x_x': [1, 300], 'sight_sensitivity_8x_y': [1, 300]}
ESetting_Slider_TriggerRun_Range: list = [10, 100]
ESetting_Slider_Turnto_Range: list = [0, 300]
EXECUTE_CD_TIME: int = 2
EXECUTE_DISSOLVE_OPEN: bool = False
EXECUTE_DYING_TO_DEATH: bool = True
EXECUTION_ITEM_ID_NUKE_NECK: int = 6050000010
EXECUTION_ITEM_QUALITY_2_ICON: dict = {1: 11865, 2: 11866, 3: 11867, 4: 11868, 5: 11869, 6: 11870}
EnableDLCCheck: bool = True
F1_MAX_RATIO: float = 3.0
F2_MAX_RATIO: float = 5.0
FACE_BASE_MAP_GUID: str = 'fc7f12f4-d3cf-47fb-b435-624ccc9e99e8'
FOG_OFFSET_NORMAL: int = 50
FOG_OFFSET_ON_AIRCRAFT: int = 350
FORCE_OPEN_PARACHUTE_AIRPLANE: int = 1
FORCE_OPEN_PARACHUTE_ALWAYS: int = 0
FORCE_OPEN_PARACHUTE_CLOSE: int = 2
FPS_MOVE_GRAPH: str = 'FPS/Hand/fps_main_moveActions.graph'
FREEFALL_FORWARD_ACCELERATION: int = 20
FREEFALL_FORWARD_ACCELERATION_FOR_UAV: int = 100
FREEFALL_GRAVITY_ACC_RATIO: float = -7.5
FREEFALL_MAX_MOVE_X: float = 15.0
FREEFALL_MAX_MOVE_Z: float = 33.333333333333336
FREEFALL_MAX_MOVE_Z_FOR_UAV: float = 33.333333333333336
FREEFALL_MAX_Y: float = 36.11111111111111
FREEFALL_MIN_Y: float = 13.88888888888889
FREEFALL_NORMAL_Y: float = 25.0
FREEFALL_PITCH_RANGE: tuple = (-0.5, 1.1)
FREEFALL_SHAKE_SPEED_UP_THRESHOLD: float = 0.5
FRIEND_RECOMMEND: str = '好友推荐'
FRIEND_SEARCH: str = '好友搜索'
FULL_SLIDE_INTERVAL_ENABLE: bool = True
GACHA_ITEM_QUALITY_2_ICON: dict = {1: 10669, 2: 10649, 3: 10648, 4: 10647, 5: 10650}
GACHA_ITEM_QUALITY_2_TEXT_COLOR: dict = {1: (95, 95, 95, 95), 2: (0, 48, 105, 255), 3: (80, 0, 72, 255), 4: (102, 31, 0, 255), 5: (255, 255, 255, 255)}
GAMESTATE_CREATEROLE: int = 4
GAMESTATE_LOADING: int = 5
GAMESTATE_PLAYING: int = 6
GAMESTATE_PRELOADING: int = 3
GAMESTATE_SELSERVER: int = 2
GAMESTATE_START: int = 1
GAMESTATE_UNKNOWN: int = 0
GAME_SOUND_TIPS_FAR_RATIO: float = 1.0
GAME_SOUND_TIPS_FAR_RATIO_SQUAD_FIGHT: float = 1.0
GENDER_2_TEXTURE: dict = {0: 0, 1: 10173, 2: 10172}
GMSDK_TYPE_CLIENT_URL: int = 3
GMSDK_TYPE_CUSTOMERSERVICE: int = 1
GMSDK_TYPE_EXTRA_QUESTION: int = 2
GMSDK_TYPE_SPRITE: int = 0
GM_LANG_MAP: dict = {'zh': 'chs', 'ja': 'en', 'tw': 'en', 'ar': 'en', 'fr': 'fr', 'ru': 'ru', 'de': 'de', 'es': 'es'}
GRAND_THEFT_TIPS_TYPE_AIRDROP: int = 2
GRAND_THEFT_TIPS_TYPE_CASH_UP: int = 0
GRAND_THEFT_TIPS_TYPE_ENEMY_HELICOPTER: int = 1
GRAND_THEFT_TIPS_TYPE_ENTER_GAME: int = 8
GRAND_THEFT_TIPS_TYPE_FEVER_TIME: int = 7
GRAND_THEFT_TIPS_TYPE_FIRST: int = 2
GRAND_THEFT_TIPS_TYPE_LOSE_FIRST: int = 4
GRAND_THEFT_TIPS_TYPE_MARKED: int = 1
GRAND_THEFT_TIPS_TYPE_MONEY_PROGRESS: int = 3
GRAND_THEFT_TIPS_TYPE_OTHER_MARKED: int = 9
GRAND_THEFT_TIPS_TYPE_PROGRESS_ENEMY: int = 6
GRAND_THEFT_TIPS_TYPE_PROGRESS_FRIEND: int = 5
GRAND_THEFT_TIPS_TYPE_RE_FIRST: int = 3
GRAND_THEFT_TIPS_TYPE_SAVE_MACHINE: int = 4
GRAND_THEFT_TIPS_TYPE_SELF_HELICOPTER: int = 0
GRENADE_LAUNCHER_ITEM_ID: int = 471
GROWN_HEAD_RADIUS: list = [0.17, 0.23, 0.27, 0.33]
GROW_HEAD_SCALE: list = [1.3, 1.6, 2.0]
GUNSMITH_FINETUNE_ENABLE: bool = False
GUN_PART_ATTR_IN_EXCEL: tuple = ('optic_type_atom', 'mag_type_atom', 'action_type_atom', 'firerate_type_atom')
GUN_SMITH_COLOR_GREEN: tuple = (124, 208, 79)
GUN_SMITH_COLOR_RED: tuple = (255, 91, 91)
GUN_SPELL_HIT_ENEMY_MARK_INTERVAL: int = 60
GYROSCOPE_DEAD_RESPONSE_X_RADIAN: int = 3
GYROSCOPE_MAX_MOVE_SPEED_PER_SEC: float = 720.0
GYROSCOPE_ROTATION_RATE_THRESHOLD: float = 0.05
GYROSCOPE_TYPE: int = 3
GunPropertyRelatedAttrKeys: list = [10031, 50022, 70022, 150022, 150042, 150052, 150062, 150072, 150082, 150132, 150142, 30012, 30022, 60012, 20012, 20052]
HALL_CACHE_CSB_PATH: set = {'UIScript/node_c_download_tips.csb', 'UIScript/node_og_yindao_kuang.csb', 'UIScript/node_reddot.csb', 'UIScript/node_reddot_reward.csb', 'UIScript/node_og_hall_new_player.csb'}
HALL_CACHE_TIMELINE_PATH: set = {'UIScript/node_c_download_tips.csb', 'UIScript/node_og_hall_new_player.csb'}
HALL_EXECUTED_HERO_MODEL_POS: tuple = (0.41, 0.1, 0.35)
HALL_EXECUTED_HERO_MODEL_YAW: float = 3.14
HALL_HERO_MODEL_POS: tuple = (0, 0, 0)
HALL_RANK_GUN_GOD_LEVEL: int = 10
HALL_SPACE_CAMERA_LOCK_REASON_HALL_CALCULATION: int = 100
HALL_STATUS_2_TEXTURE: dict = {0: 10171, 1: 10171, 2: 10171, 3: 10170, 4: 10171, 5: 10171, 6: 10171, 7: 10169, 8: 10169, 9: 10169}
HAND_MODEL_TO_WEAPON_CUE_IDS: tuple = (95,)
HEARTBEAT_SCAN_CDTIME: float = 6.0
HEARTBEAT_SCAN_DELAY_TIME: float = 1.0
HEARTBEAT_SCAN_ONCETIME: int = 3
HEARTBEAT_SCAN_ONCE_POINT_EXIST: float = 2.5
HEARTBEAT_SCAN_WAITTIME: float = 3.8
HERO_AUDIO_DLC_ID_PACK: str = 'dlcid_pack_4003'
HERO_SKIN_DETAIL_OPEN: bool = True
HIDDEN_REASON_AIRPLANE: int = 8
HIDDEN_REASON_AOI: int = 43
HIDDEN_REASON_BACK: int = 38
HIDDEN_REASON_BOMB: int = 4
HIDDEN_REASON_BOMB_ADVANCE: int = 52
HIDDEN_REASON_CALCULATION: int = 25
HIDDEN_REASON_CHANGEWEAPON: int = 3
HIDDEN_REASON_CHAOS: int = 54
HIDDEN_REASON_CLIENT_BATCH: int = 15
HIDDEN_REASON_CLIMB_LADDER: int = 21
HIDDEN_REASON_COMMON: int = 1
HIDDEN_REASON_COMMON_SHOW: int = 37
HIDDEN_REASON_CONFIG: int = 40
HIDDEN_REASON_DEAD: int = 2
HIDDEN_REASON_DECAL: int = 33
HIDDEN_REASON_DLC_NODE: int = 39
HIDDEN_REASON_DRONE: int = 57
HIDDEN_REASON_DUAL_MUTEX: int = 50
HIDDEN_REASON_DYING: int = 5
HIDDEN_REASON_EMOTE: int = 47
HIDDEN_REASON_EXECUTE: int = 53
HIDDEN_REASON_FOLLOW_MODEL: int = 60
HIDDEN_REASON_FOR_FPS: int = 11
HIDDEN_REASON_FOR_TPS: int = 10
HIDDEN_REASON_GACHA: int = 51
HIDDEN_REASON_GAMEPAD: int = 55
HIDDEN_REASON_GAME_LOGIC: int = 49
HIDDEN_REASON_GHOST: int = 13
HIDDEN_REASON_GUNSMITH_CACHE: int = 9
HIDDEN_REASON_GUN_LOADING: int = 28
HIDDEN_REASON_GUN_OVERVIEW: int = 46
HIDDEN_REASON_GUN_PART: int = 16
HIDDEN_REASON_GUN_PART_MUTEX: int = 22
HIDDEN_REASON_GUN_PREPARING: int = 34
HIDDEN_REASON_GUN_SMITH: int = 61
HIDDEN_REASON_HEAD_MODEL: int = 41
HIDDEN_REASON_INFO_CHAOS: int = 59
HIDDEN_REASON_INTRO: int = 56
HIDDEN_REASON_JUMP: int = 36
HIDDEN_REASON_LEVEL_TASK: int = 31
HIDDEN_REASON_LIGHT_ATTACK: int = 29
HIDDEN_REASON_MALL: int = 35
HIDDEN_REASON_NOT_CHOOSE_HERO: int = 20
HIDDEN_REASON_PASS_BATTLE: int = 45
HIDDEN_REASON_RANK: int = 30
HIDDEN_REASON_REPLAY: int = 14
HIDDEN_REASON_REPLAY_ROOM: int = 44
HIDDEN_REASON_SPELL: int = 19
HIDDEN_REASON_SP_WEAPON: int = 62
HIDDEN_REASON_STROP: int = 24
HIDDEN_REASON_SWIM: int = 32
HIDDEN_REASON_TALENT: int = 18
HIDDEN_REASON_UI_COMMON1: int = 63
HIDDEN_REASON_UI_MUTEX: int = 48
HIDDEN_REASON_VEHICLE: int = 17
HIDDEN_REASON_WAREHOUSE: int = 26
HIDDEN_REASON_WATCH: int = 7
HIDDEN_REASON_WEAPONPART_BANNED: int = 6
HIDDEN_REASON_WEAPON_BY_CUE: int = 27
HIDE_PATH_EFFECT_SPELL_IDS: list = [28, 100, 101, 102, 200, 201]
HIDE_TOPLOGO_TIME_FOR_DETH: int = 10
HIGH_SKY_PARA_CLIENT_FIRST: bool = True
HIGH_SKY_PARA_HEIGHT_LIMIT: int = 7
HIGH_SKY_PARA_HEIGHT_LIMIT_FOR_CLOSE: int = 3
HIGH_SKY_PARA_MIN_SPEED_Z: int = 8
HIGH_SKY_SPEED_Y_LIMIT: float = -2.0
HOLOGRAPHIC_HIT_EFFECT_DURATION: float = 1.0
HOLOGRAPHIC_STAGE_ONE_DURATION: float = 1.0
HOLOGRAPHIC_STAGE_TWO_DURATION: float = 1.0
HOTSPOT_MATCH_ID: int = 1100
HOVER_SCALE9_PARAMS: dict = {14328: (10, 10, 10, 10), 13202: (28, 15, 10, 15), 14329: (2, 2, 2, 2), 13205: (42, 70, 18, 70), 14134: (18, 10, 18, 10)}
HUDSCENECOPY_REASON_COMMON: int = 1
HUDSCENECOPY_REASON_TEAMMATE_XRAY: int = 2
HY_VALLEY_SKY_TEXT_LEVEL: dict = {'zh': 'hy_valley_ch', 'en': 'hy_valley_en', 'ja': 'hy_valley_jp'}
HipMoveType2AttrName: dict = {0: 'hip_scatter_ratio_idle', 1: 'hip_scatter_ratio_walk', 2: 'hip_scatter_ratio_jog', 3: 'hip_scatter_ratio_sprint', 4: 'hip_scatter_ratio_super_sprint', 5: 'hip_scatter_ratio_knock_down'}
HipPoseType2AttrName: dict = {0: 'hip_scatter_ratio_stand', 1: 'hip_scatter_ratio_crouch', 2: 'hip_scatter_ratio_jump', 3: 'hip_scatter_ratio_slide', 4: 'hip_scatter_ratio_prone'}
ICEWOMAN_EFFECT_ID: int = 297
ICEWOMAN_EFFECT_TALENT_ID: int = 2202
ICEWOWAN_EXTRA_MAX_ARMOR_EFFECT_ID: int = 298
IG_CHAT_TEXT_TRANSLATE: bool = True
IG_VOICE_MARK_ITEM_TYPE_MAP: dict = {101: {1: 48}, 105: 49}
IG_VOICE_MARK_MAP: dict = {8: 41, 14: 42, 71: 43, 16: 45, 47: 47}
INVITE_JOINTEAM_CD: int = 5
IOS_PERMISSION_CAMERA: str = 'CAMERA'
IOS_PERMISSION_RECORD: str = 'RECORD'
IOS_PERMISSION_SPEECH: str = 'SPEECH'
IOS_PERMISSION_STORAGE: str = 'STORAGE'
ITEM_ATM_BLOW_INFO: dict = {'g': -9.8, 'duration': 0.6, 'rotate_pitch': 6.0, 'rotate_yaw': 9.0, 'rotate_roll': 6.28}
ITEM_BLOW_OUT_INFO: dict = {'g': -42, 'duration': 0.6, 'rotate_pitch': 6.0, 'rotate_yaw': 9.0, 'rotate_roll': 6.28, 'max_x_offset': 2.0, 'max_z_offset': 1.0, 'diff_z_offset': 0.6}
ITEM_DIE_DROP_INFO: dict = {'g': -30, 'duration': 0.6, 'rotate_pitch': 1.0, 'rotate_yaw': 1.0, 'rotate_roll': 1.0}
ITEM_QUALITY_2_COLOR_ICON: dict = {1: 10566, 2: 10567, 3: 10568, 4: 10569, 5: 11196, 6: 11196}
ITEM_QUALITY_2_COLOR_ICON_DECORATE: dict = {1: 14322, 2: 14323, 3: 14324, 4: 14325, 5: 14326, 6: 14327}
ITEM_QUALITY_2_COLOR_ICON_GACHA_ROLL: dict = {1: 13229, 2: 13230, 3: 13231, 4: 13232, 5: 13233, 6: 13234}
ITEM_QUALITY_2_COLOR_ICON_NEW: dict = {1: 10566, 2: 10567, 3: 10568, 4: 10569, 5: 10570, 6: 11196}
ITEM_QUALITY_2_COLOR_ICON_SQUARE: dict = {1: 14316, 2: 14317, 3: 14318, 4: 14319, 5: 14320, 6: 14321}
ITEM_QUALITY_2_COLOR_ICON_TILTED: dict = {1: 16003, 2: 16004, 3: 16005, 4: 16006, 5: 16007, 6: 16008}
ITEM_QUALITY_2_ICON_LEVEL_RECTANGLE: dict = {1: 234, 2: 235, 3: 236, 4: 237, 5: 238, 6: 238}
ITEM_QUALITY_2_ICON_LEVEL_RECTANGLE_BOTTOM_ARMS: dict = {1: 10245, 2: 10246, 3: 10247, 4: 10248, 5: 10249, 6: 10249}
ITEM_QUALITY_2_ICON_LEVEL_RECTANGLE_BOTTOM_ARMS_PC: dict = {1: 14537, 2: 14541, 3: 14542, 4: 14540, 5: 14539, 6: 14539}
ITEM_QUALITY_2_ICON_LEVEL_SMALL_WEAPON_BOTTOM_ARMS: dict = {1: 615, 2: 616, 3: 617, 4: 618, 5: 619, 6: 619}
ITEM_QUALITY_2_ICON_LEVEL_SQUARE: dict = {1: 239, 2: 240, 3: 241, 4: 242, 5: 243, 6: 243}
ITEM_QUALITY_2_ICON_LEVEL_SQUARE_BACKPACK: dict = {1: 10240, 2: 10241, 3: 10242, 4: 10243, 5: 10244, 6: 10244}
ITEM_QUALITY_2_ICON_SELECT_LEVEL_RECTANGLE_BOTTOM_ARMS: dict = {1: 10250, 2: 10251, 3: 10252, 4: 10253, 5: 10254, 6: 10254}
ITEM_QUALITY_2_LEVEL_RECTANGLE_BOTTOM_ARMS_COLOR: dict = {1: (213, 213, 213), 2: (8, 178, 255), 3: (213, 54, 255), 4: (228, 188, 29), 5: (255, 41, 52), 6: (255, 41, 52)}
ITEM_QUALITY_2_SELECT_LEVEL_RECTANGLE_BOTTOM_ARMS_COLOR: dict = {1: (213, 213, 213), 2: (8, 178, 255), 3: (213, 54, 255), 4: (228, 188, 29), 5: (255, 41, 52), 6: (255, 41, 52)}
ITEM_QUALITY_2_TAG_TEXT: dict = {1: 561, 2: 562, 3: 563, 4: 564, 5: 565, 6: 566}
ITEM_QUALITY_2_TEXTURE_BG_COLOR: dict = {1: (192, 192, 192), 2: (108, 156, 188), 3: (173, 123, 197), 4: (233, 203, 140), 5: (215, 130, 119), 6: (215, 130, 119)}
ITEM_QUALITY_BOTTOM_LINE_LEVEL: dict = {1: 596, 2: 592, 3: 594, 4: 597, 5: 593, 6: 595}
JUMP_FALL_BLEND_TIME_FACTOR: int = 4
KEYWORD_HOUSE_RANGE_TRIGGER: str = 'houseRangeTrigger'
KEYWORD_INDOOR_TRIGGER: str = 'indoorTrigger'
KILL_RIDICULE_SWITCH_OPEN: bool = False
KILL_RIDICULE_TIME: int = 3
LANG_ARABIA: str = 'ar'
LANG_CHINESE: str = 'zh'
LANG_CHINESE_FAN: str = 'tw'
LANG_CODE_TO_STRING: dict = {'zh': '中文', 'en': 'English', 'es': 'Español', 'pt': 'Português', 'th': 'แบบไทย', 'in': 'Indonesia', 'ru': 'Русский', 'ar': 'بالعربية', 'vi': 'Tiếng Việt', 'tw': '繁體', 'ja': '日本語'}
LANG_ENGLISH: str = 'en'
LANG_FRANCE: str = 'fr'
LANG_GERMANY: str = 'de'
LANG_INDONESIA: str = 'in'
LANG_JAPANESE: str = 'ja'
LANG_PORTUGAL: str = 'pt'
LANG_RUSSIA: str = 'ru'
LANG_SPAIN: str = 'es'
LANG_THAILAND: str = 'th'
LANG_VIETNAM: str = 'vi'
LBS_LANG_MAP: dict = {'zh': 'zh', 'en': 'en', 'es': 'es', 'pt': 'pt', 'ru': 'ru', 'ar': 'ar', 'th': 'th', 'in': 'id', 'tw': 'zh-hant', 'ja': 'ja', 'vi': 'vi', 'fr': 'fr', 'de': 'de'}
LEGEND_RANK_LEVEL: int = 25
LIGHT_ATTACK_CIRCLE_RANGE: int = 100
LIGHT_ATTACK_COUNTDOWN: int = 90
LIGHT_ATTACK_HEIGHT_DOWN: int = 50
LIGHT_ATTACK_HEIGHT_TOP: int = 100
LIGHT_ATTACK_VALID_WORLD_FIELDS: tuple = (5,)
LIGHT_ATTACK_VISIBLE_MARK_TYPE: tuple = (1, 2)
LIMITED_NUM_DICT: dict = {0: 14764, 1: 14765, 2: 14766, 3: 14767, 4: 14768, 5: 14769, 6: 14770, 7: 14771, 8: 14772, 9: 14773}
LIMITED_NUM_IMG: list = [14764, 14765, 14766, 14767, 14768, 14769, 14770, 14771, 14772, 14773, 14775]
LIMITED_POP: list = [1020, 750]
LOOK_AROUND_CAMERA_SWITCH: bool = True
MAGIC_BULLET_CHECK_INTERVAL: float = 0.1
MAGIC_BULLET_RANDOM_BONE: tuple = (('biped Spine', 'Head'), ('biped Spine', 'UpperTop'), ('biped L Thigh', 'Limbs_L_Thigh'), ('biped R Thigh', 'Limbs_R_Thigh'), ('biped L Calf', 'Limbs_L_Calf'), ('biped R Calf', 'Limbs_R_Calf'))
MALL_DLC_AUTO_DOWNLOAD_ITEM_CAL_INTERVAL: float = 0.1
MALL_DLC_AUTO_DOWNLOAD_ITEM_INTERVAL: float = 1.0
MALL_MODEL_BOUND_LENGTH_BASE: float = 1.25
MALL_MODEL_MAX_SCALE: float = 1.75
MALL_MODEL_POS_BASE: tuple = (1.5714, 0.8179, -0.8787)
MALL_MODEL_YAW_BASE: float = 0.785
MALL_ROLL_ITEM_QUALITY_2_TEXTURE_BG_COLOR: dict = {1: (213, 213, 213), 2: (8, 178, 255), 3: (213, 54, 255), 4: (228, 188, 29), 5: (255, 130, 12), 6: (255, 41, 52)}
MALL_ROLL_LIMITED_MAX_SPEED: float = 50.0
MALL_ROLL_LIMITED_MIN_SPEED: float = 20.0
MALL_ROLL_LIMITED_ONE_DURATION: float = 0.3
MALL_ROLL_LIMITED_TWO_DURATION: float = 0.3
MALL_ROLL_NOCYCLE_MAX_SPEED: float = 10.0
MALL_ROLL_NOCYCLE_MIN_SPEED: float = 1.0
MALL_ROLL_NOCYCLE_STAGE_ONE_DURATION: float = 2.0
MALL_ROLL_NOCYCLE_STAGE_TWO_DURATION: float = 2.0
MALL_ROLL_NO_CYCLE_ITEM_QUALITY_2_TEXT_COLOR: dict = {1: (213, 213, 213, 255), 2: (8, 178, 255, 255), 3: (213, 54, 255, 255), 4: (228, 188, 29, 255), 5: (255, 130, 12, 255), 6: (255, 41, 52, 255)}
MALL_ROLL_PROTECT_TIME: float = 10.0
MARK_BORN_ANIM_DURATION: float = 0.3
MARK_CAMERA_HIT_MAX_DISTANCE: int = 165
MARK_CAMERA_HIT_MAX_OPACITY: int = 255
MARK_CAMERA_HIT_MIN_DISTANCE: int = 30
MARK_CAMERA_HIT_MIN_OPACITY: int = 50
MARK_ENEMY_FADEIN_TIME: float = 0.05
MARK_ENEMY_FADEOUT_TIME: int = 1
MARK_ENEMY_SHOW_TIME: float = 2.0
MARK_FOV_DISTANCE: int = 30
MARK_FOV_DISTANCE_ROOM: int = 30
MARK_MAX_OPACITY: float = 1.0
MARK_MAX_OPACITY_AIRPLANE: float = 1.0
MARK_MAX_SCALE: int = 1
MARK_MIN_OPACITY: float = 0.39215686274509803
MARK_MIN_OPACITY_AIRPLANE: float = 1.0
MARK_MIN_OPACITY_ROOM: float = 0.15
MARK_MIN_SCALE: float = 0.9
MARK_OPACITY_IN_ADS: int = 66
MARK_OPACITY_IN_ADS_TEAMMATE_TOPLOGO: int = 150
MARK_TYPE_2_SOUND_ID: dict = {1: 136, 2: 132, 8: 132}
MARK_VISIBLE_DISTANCE: int = 1000
MARK_VISIBLE_DISTANCE_ROOM: int = 200
MAX_MARK_VISIBLE_DISTANCE: int = 1000
MAX_PITCH_FACTOR: float = 1.25
MAX_RECOMMEND_FRIEND_COUNT: int = 30
MAX_RECRUIT_MESSAGE: int = 15
MAX_TACTICAL_ENERGY_LEVEL: int = 6
MESSAGE_TYPE_SOURCE_MAP: dict = {1: (1, 2), 10: (5, 5), 12: (5, 5), 9: (5, 5)}
MIN_PITCH_FACTOR: float = -0.6
MOBA_CALCULATION_DELAY_SPEED: float = 0.5
MOBA_CALCULATION_DELAY_TIME: float = 2.0
MOBA_CALCULATION_PANEL_DETAIL_BG_COLOR: dict = {4: (198, 81, 251), 2: (170, 249, 100), 3: (161, 248, 244), 1: (248, 183, 83)}
MOBA_CALCULATION_PANEL_FRIEND_BG: dict = {4: 10387, 2: 10385, 3: 10386, 1: 10388}
MOBA_COMBAT_CACHE_CSB_PATH: set = set()
MOBA_COMBAT_CACHE_TIMELINE_PATH: set = set()
MONEY_TYPE_2_ICON: dict = {1: 40000000100, 4: 40000000200, 2: 40000000200, 3: 40000000200, 6: 40000000200, 7: 40000000400}
MONEY_TYPE_2_ICON_GACHA: dict = {1: 40000000103, 4: 40000000203, 2: 40000000203, 3: 40000000203, 6: 40000000203, 7: 14573}
MONITOR_MISSILE_TURN_VIEW_SENSITIVITY: float = 0.6
MOTION_SKELETON_REPLACEMENT: dict = {'Char/US_TPS/base.skeleton': 'Char/US_TPS/base_motion.skeleton'}
MOUSE_HOVER_TEXTURE_1: int = 14328
MOUSE_HOVER_TEXTURE_2: int = 13202
MOUSE_HOVER_TEXTURE_3: int = 14329
MOUSE_HOVER_TEXTURE_4: int = 13204
MOUSE_HOVER_TEXTURE_5: int = 13205
MOUSE_HOVER_TEXTURE_6: int = 13206
MOUSE_HOVER_TEXTURE_7: int = 14330
MOUSE_HOVER_TEXTURE_8: int = 13208
MOUSE_HOVER_TEXTURE_9: int = 14134
MOVE_DIRECTION_ONLY_DYING: bool = True
MPAY_LANG_MAP: dict = {'zh': 'zh_CN', 'en': 'en_US', 'es': 'es_ES', 'pt': 'pt_PT', 'th': 'th_TH', 'in': 'id_ID', 'ru': 'ru_RU', 'ar': 'en_US', 'vi': 'vi_VN', 'tw': 'zh_TW', 'ja': 'ja_JP', 'de': 'de_DE', 'fr': 'en_US'}
MSG_ALL_SOURCES_FILE_MAP: dict = {1: ('UIScript/node_chat_mine.csb', 'NormalTalkMine'), 2: ('UIScript/node_chat_other.csb', 'NormalTalkOther'), 5: ('UIScript/node_chat_message.csb', 'SystemMsgNode')}
MiniMapIconScale_Range: list = [0.8, 1.1]
MoveYawDelta: dict = {0: {0: 0.0, 8: 0.0, 2: 0.0, 4: 0.0, 6: 0.0, 7: 0.7853981633974483, 9: -0.7853981633974483, 1: -0.7853981633974483, 3: 0.7853981633974483}, 1: {0: 0.0, 8: 0.0, 2: 3.141592653589793, 4: 1.5707963267948966, 6: -1.5707963267948966, 7: 0.7853981633974483, 9: -0.7853981633974483, 1: 2.356194490192345, 3: -2.356194490192345}, 2: {0: 0.0, 8: 0.0, 2: 0.0, 4: 0.0, 6: 0.0, 7: 0.7853981633974483, 9: -0.7853981633974483, 1: -0.7853981633974483, 3: 0.7853981633974483}}
MoveYawDeltaFollowFace: dict = {0: 0.0, 8: 0.0, 2: 0.0, 4: 0.0, 6: 0.0, 7: 0.7853981633974483, 9: -0.7853981633974483, 1: -0.7853981633974483, 3: 0.7853981633974483}
MoveYawDeltaFollowJoystick: dict = {0: 0.0, 8: 0.0, 2: 3.141592653589793, 4: 1.5707963267948966, 6: -1.5707963267948966, 7: 0.7853981633974483, 9: -0.7853981633974483, 1: 2.356194490192345, 3: -2.356194490192345}
MoveYawDeltaLockFace: dict = {0: 0.0, 8: 0.0, 2: 0.0, 4: 0.0, 6: 0.0, 7: 0.0, 9: 0.0, 1: 0.0, 3: 0.0}
NODE_ACTIVATED_SIGNAL: int = 32777
NODE_DEACTIVATED_SIGNAL: int = 32778
NODE_PARABOLA_SIGNAL: int = 32787
NODE_TRANSITION_EXCUTE_SIGNAL: int = 32797
NORMAL_PITCH_FACTOR: float = 0.4
NOTICE_LANG_FILE_NAMES: dict = {'zh': 'notice_login_zh', 'en': 'notice_login_en', 'es': 'notice_login_es', 'pt': 'notice_login_pt', 'th': 'notice_login_th', 'in': 'notice_login_id', 'ru': 'notice_login_ru', 'ar': 'notice_login_ar', 'vi': 'notice_login_vn', 'tw': 'notice_login_tw', 'ja': 'notice_login_ja'}
NOTICE_LANG_FILE_NAMES_ME: dict = {'ar': 'notice_login_me_ar', 'en': 'notice_login_me_en'}
NOTICE_LANG_FILE_NAMES_STEAM: dict = {'zh': 'notice_login_steam_zh', 'en': 'notice_login_steam_en'}
NOTICE_LANG_FILE_RECHARGE_RULE: dict = {'zh': 'sanfang_zh', 'en': 'sanfang_en', 'es': 'sanfang_es', 'pt': 'sanfang_pt', 'th': 'sanfang_th', 'in': 'sanfang_id', 'ru': 'sanfang_ru', 'ar': 'sanfang_ar', 'vi': 'sanfang_vn', 'tw': 'sanfang_tw'}
NO_CHANGE_BIG_HEAD_PRIMS: tuple = ('head_pixel', '_10037mv13_head')
OCCUPY_ITEM_MARK_SHOW_DISTANCE: int = 150
OCCUPY_ITEM_MARK_SHOW_DISTANCE_ENEMY: int = 100
OCCUPY_ITEM_MARK_SHOW_ENEMY_TIME: int = 10
OG_CREATE_ROLE_MODEL_INIT_YAW: float = 2.0
OG_HERO_SELECT_MODEL_INIT_YAW: float = 2.0
OPACITY_REASON_ADS: int = 1
OPACITY_REASON_BIGMAP: int = 2
OPACITY_REASON_INSPECTION: int = 0
OPEN_LIKE_BUTTON: bool = True
OPEN_NGP_WINDOW: bool = True
OPEN_PARACHUTE_ACCELERATE: float = 15.0
OPTIC_FADE_TIME: float = 0.13
OVERLAY_ACTION_STATE_MAP: dict = {'Idle': 0, 'Cross': 1, 'Climb': 2}
PARACHUTE_ATTACH_EFFECT_FOR_SCRIPT: bool = True
PARACHUTE_CAN_SHOOT_SPEED_THRESHOLD: int = 60
PARACHUTE_FALL_ACTION_CHANGE_THRESHOLD: int = 20
PARACHUTE_FOLLOWER_NO_ATTACH: bool = False
PARACHUTE_FOLLOW_MAP: dict = {4: 10201, 2: 10199, 3: 10200, 1: 10202}
PARACHUTE_FORWARD_ACCELERATION: int = 10
PARACHUTE_FREEFALLWEAPON_SWITCH: bool = True
PARACHUTE_MAX_MOVE_Z: float = 22.22222222222222
PARACHUTE_MAX_Y: float = 12.5
PARACHUTE_MIN_Y: float = 4.444444444444445
PARACHUTE_NORMAL_Y: float = 10.0
PARACHUTE_ROTATE_PITCH_SPEED: float = 0.3141592653589793
PARACHUTE_ROTATE_ROLL_SPEED: float = 0.6981317007977318
PARACHUTE_ROTATE_YAW_SPEED: int = 1
PARACHUTE_SPEED_X_FACTOR_FOR_FPS: int = 8
PARTICLE_SHIELD_SLIDE_EXTRA_SPEED_RATIO: float = 0.5
PAYMENT_BUY_LIMIT_DURATION: int = 300
PC_PAY_REGION: dict = {'AR': 'Argentina', 'BD': 'Bangladesh', 'BR': 'Brazil', 'CL': 'Chile', 'CO': 'Colombia', 'ID': 'Indonesia', 'KZ': 'Kazakhstan', 'MY': 'Malaysia', 'MX': 'Mexico', 'NG': 'Nigeria', 'CN': 'Others', 'PH': 'Philippines', 'RU': 'Russia', 'TH': 'Thailand'}
PERSONAL_CARD_MVP_NAME_SIZE: int = 32
PERSONAL_CARD_MVP_TEAM_ICON_COLOR: str = '#D0D0D2'
PERSONAL_CARD_MVP_TEAM_NAME_COLOR: tuple = (231, 230, 230)
PERSONAL_CARD_MVP_TEAM_NAME_SIZE: int = 26
PHYSICS_AIR_DROP_BOX: int = 17
PHYSICS_BULLET: int = 23
PHYSICS_CAMERA: int = 11
PHYSICS_CHARCTRL: int = 30
PHYSICS_COMMON_OBSTACLE: int = 2
PHYSICS_DOOR: int = 26
PHYSICS_DROP_ITEM: int = 24
PHYSICS_GHOST: int = 1
PHYSICS_GLASSWALL: int = 3
PHYSICS_NOTHING: int = 0
PHYSICS_OBSTACLE_QUERY: int = 4
PHYSICS_PARTICLE_SHIELD: int = 12
PHYSICS_ROOM_TRIGGER: int = 14
PHYSICS_SELF: int = 31
PHYSICS_SELF_TRIGGER: int = 25
PHYSICS_SHOOT_TEST: int = 19
PHYSICS_SHOOT_VERIFY: int = 16
PHYSICS_THROWN: int = 15
PHYSICS_THROWN_TRIGGER: int = 13
PHYSICS_TREES: int = 18
PHYSICS_TRIGGER: int = 21
PHYSICS_VEHICLE: int = 27
PHYSICS_VISIBLE_OBSTACLE_QUERY: int = 5
PHYSICS_WATER: int = 29
PLACE_ENTITY_DISTANCE: int = 30
PLAYER_ALBUM_MESSAGE: str = '相册留言'
PLAYER_CHARCTRL_HALFHEIGHT: float = 0.4
PLAYER_CHARCTRL_RADIUS: float = 0.5
PLAYER_CHARCTRL_TPS_RADIUS: float = 0.4
PLAYER_LEAVE_MESSAGE: str = '玩家留言'
PLAYER_MESSAGE: str = '个人宣言'
PLAYER_NAME_CREATE: str = '角色创建'
PLAYER_NAME_MODIFY: str = '角色改名'
PLAYER_REPLY_MESSAGE: str = '回复留言'
PRINT_JOYSTICK_SHAKE_VALUE: bool = False
PROMPT_TALENT_NODE_QUALITY_2_ICON: dict = {1: 10450, 2: 10451, 3: 10452, 4: 10453, 5: 10454, 6: 10454}
QUALITY_2_RELOAD_WEAPON_VX_COLOR: dict = {1: (155, 155, 155), 2: (101, 184, 255), 3: (208, 95, 255), 4: (255, 229, 95), 5: (255, 95, 41), 6: (255, 160, 95)}
RANDOM_DEATH_BOX: int = 6060000100
RANDOM_MUSIC: int = 6100000050
RANDOM_TRAILING: int = 6090000000
REBORN_KEY_MAP: dict = {1: 68, 2: 69, 3: 70}
RELAY_STATE_KEY_DYING_MOVE: str = 'DyingMove'
RENDER_SET_DEFAULT: int = 0
RENDER_SET_HUD_SIGHT: int = 412316860416
RENDER_SET_HUD_SIGHT_OPTIC_OPEN: int = 9208409882624
RENDER_SET_SHADOW_PROXY: int = 34359738368
RENDER_STENCIL_DIY1: int = 32
RENDER_STENCIL_DIY2: int = 64
RENDER_STENCIL_DIY3: int = 96
RENDER_STENCIL_DIY4: int = 128
RENDER_STENCIL_DIY5: int = 160
RENDER_STENCIL_DIY6: int = 192
RENDER_STENCIL_ROLE: int = 224
ROOM_MESSAGE: str = '房间公告'
ROOM_NAME: str = '房间名称'
ROOM_REDPACK_EXPLAIN: str = '房间红包描述'
ROTATE_CHAR_HEIGHT: float = 0.5
ROTATE_CHAR_LENGTH: float = 1.8
ROTATE_CHAR_WIDTH: float = 0.5
SELECT_SKILL_SLOT_2_COLOR: dict = {4: (187, 73, 248), 2: (193, 255, 119), 3: (155, 238, 234), 1: (235, 174, 83)}
SELF_DEFINE_PC_KEY_MAP: dict = {1: 17, 2: 31, 3: 30, 4: 32, 5: 18, 6: 16, 7: 1, 8: 44, 9: 49}
SELF_DEFINE_PC_ROOM_SETTING_KEY_MAP: dict = {20: 44, 21: 45, 22: 46, 23: 47, 24: 36, 25: 37, 26: 38, 27: 25, 28: 26, 29: 27}
SELF_TRIGGER_RADIUS: int = 2
SETTING_WINDOW_TEXT_COLOR_DISABLE: tuple = (130, 138, 143, 15)
SETTING_WINDOW_TEXT_COLOR_ENABLE: tuple = (248, 255, 77, 15)
SHOOTINGRANGE_CHALLENGE_OPEN: bool = True
SHOOTINGRANGE_MATCH_ID: int = 11
SHOP_MARK_CAMERA_HIT_MAX_DISTANCE: int = 165
SHOP_MARK_CAMERA_HIT_MAX_OPACITY: int = 255
SHOP_MARK_CAMERA_HIT_MIN_DISTANCE: int = 30
SHOP_MARK_CAMERA_HIT_MIN_OPACITY: int = 100
SHOP_MARK_FOV_DISTANCE: int = 10
SHOP_MARK_MAX_OPACITY: float = 0.39215686274509803
SHOP_MARK_MIN_OPACITY: float = 1.0
SHOP_MARK_OFFSET: tuple = (0, 3, 0)
SHOP_MARK_SHOW_DISTANCE: int = 50
SHOP_MARK_VISIBLE_DISTANCE: int = 50
SHOW_DRAW_HOUSE_SHOOT: bool = False
SHOW_NODE_HOVER_SOUND_ID: int = 1025
SHOW_PLAYER_NATIONAL_FLAG_CARD: bool = True
SHOW_PLAYER_NATIONAL_FLAG_COMBAT: bool = True
SIDEBAR_TAB2_COLOR_SELECTED: tuple = (248, 255, 77)
SIDEBAR_TAB2_COLOR_UNSELECTED: tuple = (94, 94, 94)
SIDEBAR_TAB_COLOR_SELECTED: tuple = (12, 22, 31)
SIDEBAR_TAB_COLOR_UNSELECTED: tuple = (180, 180, 180)
SIGHT_OPTIC_STEALTH_HIDE_MODELS: tuple = (3726, 3788, 3777, 3791, 2845, 3855, 3856)
SOUND_CHARACTER_ACTION_DICT: dict = {('Stand', 'Walk'): 'stand_slow', ('Stand', 'Jog'): 'stand_normal', ('Stand', 'Sprint'): 'stand_fast', ('Stand', 'SuperSprint'): 'stand_sprint', ('Crouch', 'Walk'): 'squat_slow', ('Crouch', 'Jog'): 'squat_normal', ('Prone', 'Jog'): 'crawl_normal', ('Prone', 'Walk'): 'crawl_slow'}
SOUND_DISAPPEAR_EVENT_STR: str = 'sound_event_disappear'
SOUND_EMITTER_OBSTRUCT_OPEN: bool = True
SOUND_EVENT_STR: str = 'sound_event'
SOUND_EVENT_TYPE_CLICK: int = 1
SOUND_EVENT_TYPE_CLOSE_UI: int = 3
SOUND_EVENT_TYPE_SHOW_UI: int = 2
SOUND_GAME_STATE_INGAME: str = 'Ingame'
SOUND_GAME_STATE_OUTGAME: str = 'Outgame'
SOUND_GAME_STATE_SETTLE: str = 'Settlement'
SOUND_INGAME_BNK_FILE: str = 'music_ingame_basic_m.bnk'
SOUND_INGAME_GRAND_THEFT_BNK_FILE: str = 'music_ingame_payday_prepare.bnk'
SOUND_INGAME_ZOMBIE_BNK_FILE: str = 'music_ingame_xuejing_prepare.bnk'
SOUND_INGAME_ZOMBIE_BNK_FILE_2: str = 'music_ingame_xuejing_skydiving.bnk'
SOUND_OUTGAME_BNK_FILE: str = 'music_outgame_basic_m.bnk'
SOUND_OUTGAME_GRAND_THEFT_BNK_FILE: str = 'music_ingame_payday_victory.bnk'
SPELL_ID_MEDICINES: tuple = (23, 24, 51)
SPELL_ID_UAV: int = 19
SPELL_ID_WALL_BOMB: int = 227
SP_ITEM_QUALITY_2_COLOR_ICON: dict = {1: 10688, 2: 10689, 3: 10690, 4: 10691, 5: 10692, 6: 10693}
SP_ITEM_QUALITY_2_COLOR_ICON_PAY: dict = {1: 11309, 2: 11310, 3: 11311, 4: 11312, 5: 11313, 6: 11314}
SQUADFIGHT_MATCH_ID: int = 1200
SQUADFIGHT_MATCH_ID_RANK: int = 1300
SQUAD_FIGHT_CACHE_CSB_PATH: set = {'UIScript/node_og_yindao_kuang.csb', 'UIScript/ig_hud_team_arena_shop.csb', 'UIScript/node_ig_team_arena_equip.csb', 'UIScript/ig_main_hud_wait_countdown.csb', 'UIScript/ig_team_arena_result_bobao.csb'}
SQUAD_FIGHT_CACHE_TIMELINE_PATH: set = {'UIScript/node_og_yindao_kuang.csb', 'UIScript/ig_hud_team_arena_shop.csb', 'UIScript/node_ig_team_arena_equip.csb', 'UIScript/ig_main_hud_wait_countdown.csb', 'UIScript/ig_team_arena_result_bobao.csb'}
SQUAD_FIGHT_ROUND_SETTLE_CALCULATION_DELAY: int = 5
SQUAD_FIGHT_ROUND_SETTLE_CALCULATION_DELAY_AFTER_WATCH: int = 1
SQUAD_FIGHT_WATCH_LAST_KILL: float = 7.5
SQUAD_FIGHT_WATCH_LAST_KILL_AFTER_WATCH: float = 3.5
SQUAD_FIGHT_WATCH_TEAMMATE_DELAY_TIME: int = 3
SR_CHANGE_MINI_MAP_SCALE_DURATION: int = 1
STEALTH_MATERIAL_PATH: str = 'ShaderGraph/material/PBR0_IBL_Transparent'
STROP_LEAVE_DIRECTION_NORMAL: bool = True
STROP_LEAVE_SPEED: float = 10.0
STROP_SPEED: float = 15.0
STROP_VERTICAL_JUMP_OFF_SPEED_Y: float = 1.0
STR_ROTATE_WITH_IMAGE_NODE: str = 'RotateWithImageNode'
SUPPORT_RECORD_LOCALES: dict = {'zh': 'zh-CN', 'en': 'en', 'ja': 'ja', 'tw': 'zh-TW', 'es': 'es'}
SURVEY_INTERVAL: int = 604800
SURVEY_LAST_TOW_NUM_RANGE: tuple = (20, 40)
SWITCH_QUICK_MED_SOUND_ID: int = 1025
SYSTEM_SIGNAL_BASE: int = 32767
SprintMoveSidelingRadian: float = 0.5236
SystemModeRatio: dict = {1: 0.8, 2: 1, 3: 1.2}
TACH_POINT_ANIM_CAMERA: str = 'HP_Camera'
TACH_POINT_CHARGER_CHARGER: str = 'HP_mag_attach'
TACH_POINT_GUN_CHARGER: str = 'HP_mag_attach'
TACH_POINT_GUN_HANGINGS: str = 'HP_cosmetic'
TACH_POINT_GUN_LEFTHAND: str = 'HP_Hand_Left_IK'
TACH_POINT_GUN_RIGHTHAND: str = 'HP_gun'
TACH_POINT_GUN_SIGHT: str = 'HP_sight'
TACH_POINT_GUN_WEAPON: str = 'HP_Hand_Left_IK'
TACH_POINT_HAND_ANIM_WEAPON: str = 'tag_weapon'
TACH_POINT_HAND_CAMERA: str = 'tag_camera_scripted'
TACH_POINT_HAND_CHARGER_NEW: str = 'HP_Hand_D_new'
TACH_POINT_HAND_CHARGER_OLD: str = 'HP_Hand_D_old'
TACH_POINT_HAND_LEFTHAND: str = 'WL'
TACH_POINT_HAND_RIGHTARM: str = 'Bip001 R UpperArm'
TACH_POINT_HAND_RIGHTHAND: str = 'WR'
TACH_POINT_HAND_WEAPON: str = 'WL'
TACH_POINT_ITEM_HAND: str = 'HP_Hand'
TACTICAL_ARMOR_BROKEN_EFFECT: dict = {1: 227, 2: 224, 4: 226, 6: 225}
TACTICAL_ARMOR_RECOVER_EFFECT: dict = {1: 231, 2: 228, 4: 230, 6: 229}
TACTICAL_ARMOR_RECOVER_FINISH_EFFECT: dict = {1: 235, 2: 232, 4: 234, 6: 233}
TACTICAL_ARMOR_UPGRADE_EFFECT: dict = {1: 263, 2: 245, 4: 247, 6: 246}
TACTICAL_LEVEL_BG_COLOR: dict = {1: (56, 57, 58), 2: (19, 65, 67), 4: (56, 26, 61), 6: (198, 191, 87)}
TACTICAL_LEVEL_COLOR: dict = {1: (211, 211, 209), 2: (100, 160, 212), 4: (177, 114, 213), 6: (237, 203, 69)}
TACTICAL_LEVEL_ENERGY_BACKPACK_PROGRESS: dict = {1: 0, 2: 15, 3: 38, 4: 57, 5: 80, 6: 100}
TACTICAL_LEVEL_OPACITY: dict = {1: 255, 2: 142.8, 4: 142.8, 6: 155.55}
TALENT_CORE_COMBAT_ITEM_ID: int = 145
TALENT_CRISIS_MAX_DISTANCE: int = 400
TALENT_FEEL_SURMOUNT1_CD: int = 10
TALENT_FEEL_SURMOUNT1_DURATION: int = 3
TALENT_QUALITY_2_ICON_BACKPACK: dict = {1: 10462, 2: 10463, 3: 10464, 4: 10465, 5: 10466, 6: 10466}
TALENT_QUALITY_2_TEXT_COLOR: dict = {1: (213, 213, 213), 2: (8, 178, 255), 3: (213, 54, 255), 4: (228, 188, 29), 5: (255, 41, 52), 6: (255, 41, 52)}
TALENT_QUALITY_2_TEXT_COLOR_RGBA: dict = {1: (255, 255, 255, 255), 2: (197, 230, 255, 255), 3: (245, 197, 255, 255), 4: (255, 215, 108, 255), 5: (255, 101, 101, 255), 6: (255, 101, 101, 255)}
TALENT_QUALITY_2_TEXT_COLOR_STR: dict = {1: 'ffffff', 2: 'c5e6ff', 3: 'f5c5ff', 4: 'ffd76c', 5: 'ff6565', 6: 'ff6565'}
TALENT_RADAR_MAX_DISTANCE: int = 200
TALENT_TYPE_COLOR: dict = {10: (186, 59, 59), 11: (83, 117, 204), 12: (201, 163, 52), 13: (62, 175, 94)}
TALENT_TYPE_MOZU_BG: dict = {10: 10132, 11: 10133, 12: 10134, 13: 10135}
TALENT_TYPE_TEXTURE: dict = {10: 10124, 11: 10125, 12: 10126, 13: 10127, 20: 10124, 21: 10125, 22: 10126, 23: 10127}
TALENT_TYPE_TEXTURE_TUPO: dict = {10: 10128, 11: 10129, 12: 10130, 13: 10131}
TEAMMATE_AIRDROP_COLOR: dict = {4: (209, 0, 254), 2: (137, 253, 0), 3: (11, 206, 255), 1: (255, 179, 6)}
TEAMMATE_MAIN_BOTTOM_SLOT_2_IMG: dict = {1: 10226, 2: 10223, 3: 10224, 4: 10225}
TEAMMATE_MAIN_BOTTOM_SLOT_COLOR: dict = {1: (255, 179, 6), 2: (137, 253, 0), 3: (11, 206, 255), 4: (209, 0, 254)}
TEAMMATE_MAIN_BOTTOM_V2_SLOT_2_IMG: dict = {1: 10554, 2: 10551, 3: 10552, 4: 10553}
TEAMMATE_MARK_CAMERA_HIT_MAX_DISTANCE: int = 200
TEAMMATE_MARK_CAMERA_HIT_MAX_OPACITY: int = 255
TEAMMATE_MARK_CAMERA_HIT_MIN_DISTANCE: int = 50
TEAMMATE_MARK_CAMERA_HIT_MIN_OPACITY: int = 180
TEAMMATE_MARK_FOV_DISTANCE: int = 30
TEAMMATE_MARK_GUN_ICON_LEVEL: dict = {1: 479, 2: 480, 3: 481, 4: 482, 5: 483, 6: 483}
TEAMMATE_MARK_ITEM_QUALITY_LEVEL: dict = {1: 11385, 2: 11386, 3: 11387, 4: 11388, 5: 11389, 6: 11390}
TEAMMATE_MARK_LINE_MAX_DISTANCE: int = 10
TEAMMATE_MARK_LINE_MAX_LENGTH: int = 20
TEAMMATE_MARK_LINE_MIN_DISTANCE: int = 0
TEAMMATE_MARK_LINE_MIN_LENGTH: int = 45
TEAMMATE_MARK_MAX_OPACITY: float = 1.0
TEAMMATE_MARK_MIN_OPACITY: float = 0.7843137254901961
TEAMMATE_MARK_SLOT_2_COLOR: dict = {4: (200, 81, 253), 2: (163, 239, 86), 3: (160, 240, 238), 1: (235, 173, 83)}
TEAMMATE_MARK_SLOT_2_MARK_POS_ICON: dict = {1: 10189, 2: 10191, 3: 10190, 4: 10192}
TEAMMATE_MARK_TYPE_2_ICON: dict = {1: 10178, 2: 10179, 6: 10116, 7: 10117, 8: 10119}
TEAMMATE_MARK_TYPE_2_MAP_TAG_ID: dict = {1: 31, 2: 32, 6: 33, 7: 34, 8: 35}
TEAMMATE_MARK_TYPE_NEED_CHANGE_COLOR: set = {1, 6, 7}
TEAMMATE_MARK_TYPE_RED_COLOR: tuple = (2, 8)
TEAMMATE_MARK_VISIBLE_DISTANCE: int = 200
TEAMMATE_NAME_TEXT_COLOR: dict = {4: (155, 72, 179), 2: (113, 176, 46), 3: (40, 155, 203), 1: (189, 161, 63)}
TEAMMATE_NUM_2_IMAGE: dict = {4: 386, 2: 385, 3: 384, 1: 383}
TEAMMATE_NUM_EFFECT: dict = {1: 272, 2: 269, 3: 270, 4: 271}
TEAMMATE_SLOT_2_MARK_POS_MAP_TAG_ICON: dict = {1: 48, 2: 50, 3: 49, 4: 51}
TEAMMATE_SLOT_2_REBORN_NODE_TEXTURE: dict = {4: 10457, 2: 10455, 3: 10456, 1: 10458}
TEAMMATE_SLOT_2_SF_SHOP_REQUEST_ICON: dict = {1: 167, 2: 168, 3: 169, 4: 170}
TEAMMATE_TEXT_NAME_COLOR: dict = {4: 'c851fd', 2: 'a3ef56', 3: 'a0f0ee', 1: 'ebad53'}
TEAM_SLOT_2_COLOR: dict = {4: (155, 72, 179), 2: (113, 176, 46), 3: (40, 155, 203), 1: (189, 161, 63), 5: (159, 242, 238)}
TEAM_SLOT_TEXTUR: dict = {1: 10035, 2: 10036, 3: 10037, 4: 10038}
TERRAIN_NAME: set = {'Terrain0_002', 'Terrain0_001_grass', 'Terrain1', 'PCG_Terrain_001', 'Terrain0_001'}
THANKS_FLAG_LIVE_TIME: int = 5
THANKS_TIPS_ID_CALCULATION: int = 552
THANKS_TIPS_ID_IG: int = 551
TIMEOUT_FOR_REFUSE_AGAIN: int = 20
TIMEOUT_FOR_REFUSE_HALL_TEAM: int = 20
TIPS_QUALITY_2_BG_LEVEL: dict = {1: 256, 2: 257, 3: 258, 4: 259, 5: 260, 6: 260}
TOPLOGO_CSB_FILE: str = 'UIScript/node_ig_stronghold_name.csb'
TOPLOGO_CSB_FILE_PC: str = 'UIScript/node_ig_stronghold_name_pc.csb'
TOTAL_TEAMMATE_NUMBER: int = 4
TPS_IDLE_GRAPH: str = 'TPS/Locomotion/tps_idle.graph'
TPS_IDLE_GRAPH_1: str = 'TPS/Locomotion/tps_idle_1.graph'
TPS_IDLE_GRAPH_2: str = 'TPS/Locomotion/tps_idle_2.graph'
TURN_MODE_ACCEL_SHOW_RANGE: tuple = (0, 100)
TURN_MODE_DIS_ACCEL_DIS_MAX: int = 200
TURN_MODE_DIS_ACCEL_DIS_MIN: int = 10
TURN_MODE_DIS_ACCEL_REAL_RANGE: tuple = (0, 0.01)
TURN_MODE_DIS_MAX_WAIT_DURATION: float = 0.5
TURN_MODE_SPEED_ACCEL_MAX_DIS: int = 100
TURN_MODE_SPEED_ACCEL_MIN_DIS: int = 5
TURN_MODE_SPEED_ACCEL_REAL_RANGE: tuple = (1.0, 5.0)
TechState2Name: dict = {0: 'Normal', 3: 'Frozen', 4: 'Burnt', 5: 'Highlight', 6: 'Xray', 9: 'Edgeline', 20: 'DistanceEnemy', 21: 'HighLightXray'}
UI_GENDER_ALL: int = 2
UNENABLE_CHOOSE_MAP: tuple = (1300,)
UNIT_ID_BASE: int = 76
UNIT_ID_CUSTOMIZE_FEMALE: int = 216
UNIT_ID_CUSTOMIZE_MALE: int = 215
UNIT_STATE_BE_EXECUTED: str = 'BeExecuted'
UNIT_STATE_CLIMB: str = 'Climb'
UNIT_STATE_CLIMB_LADDER: str = 'ClimbLadder'
UNIT_STATE_CLOSE_PARACHUTE: str = 'CloseParachute'
UNIT_STATE_CROSS: str = 'Cross'
UNIT_STATE_CROUCH: str = 'Crouch'
UNIT_STATE_DEAD: str = 'Dead'
UNIT_STATE_DRIVE_VEHICLE: str = 'DriveVehicle'
UNIT_STATE_DROPWEAPON: str = 'DropWeapon'
UNIT_STATE_DUAL_FIRE: str = 'DualFire'
UNIT_STATE_EMOTE: str = 'Emote'
UNIT_STATE_ENTER_PRONE: str = 'EnterProne'
UNIT_STATE_EXECUTION: str = 'Execution'
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
USE_COMBAT_ITEM_CLIENT_ENTITY: bool = True
USE_NORMAL_GAUSSIAN_BLUR: bool = True
VERION_1_ARMOR_TXT_BG_COLOR: dict = {1: (211, 211, 209), 2: (100, 160, 212), 4: (177, 114, 213), 6: (237, 203, 69)}
WANSTER_FP_URL: str = 'https://newspike-replay.fp.ps.easebar.com/file/'
WAREHOUSE_MODEL_POS: tuple = (0.6, 0.08, 0.15)
WAREHOUSE_MODEL_YAW: float = 2.269
WAREHOUSE_QUALITY_LEVEL_COLOR: dict = {1: (213, 213, 213), 2: (8, 178, 255), 3: (213, 54, 255), 4: (228, 188, 29), 5: (255, 130, 12), 6: (255, 41, 52)}
WEAPON_DIY_NAME: str = '武器diy'
WEAPON_PARTS_MAX_COUNT: int = 8
WEAPON_PART_OPTIC_TYPE_2_ICON: dict = {0: 452, 1: 453, 2: 454, 3: 454, 4: 454, 5: 454, 6: 455}
WEAPON_PART_OPTIC_TYPE_2_ICON_BACKPACK: dict = {0: 1054, 1: 1055, 2: 1056, 3: 1056, 4: 1056, 5: 1056, 6: 1057}
WEAPON_PART_OPTIC_TYPE_2_SMALL_ICON: dict = {0: 379, 1: 380, 2: 381, 3: 381, 4: 381, 5: 381, 6: 382}
WEAPON_PART_QUALITY_COLOR: dict = {0: (213, 213, 213), 1: (213, 213, 213), 2: (8, 178, 255), 3: (213, 54, 255), 4: (228, 188, 29), 5: (255, 130, 12), 6: (255, 41, 52)}
WEAPON_QUALITY_2_BG_COLOR: dict = {1: (255, 255, 255), 2: (136, 204, 255), 3: (233, 122, 255), 4: (255, 214, 102), 5: (255, 87, 87), 6: (255, 87, 87)}
WEAPON_QUALITY_2_ICON_LEVEL: dict = {1: 229, 2: 230, 3: 231, 4: 232, 5: 233, 6: 233}
WEAPON_QUALITY_2_ICON_LEVEL_BACKPACK: dict = {0: 10566, 1: 10566, 2: 10567, 3: 10568, 4: 10569, 5: 10570, 6: 11196}
WEAPON_QUALITY_2_ICON_SELECT_LEVEL_BACKPACK: dict = {1: 10235, 2: 10236, 3: 10237, 4: 10238, 5: 10239, 6: 10239}
WEAPON_QUALITY_ICON_LEVEL_ARMORY: dict = {0: 11970, 1: 11970, 2: 11971, 3: 11972, 4: 11973, 5: 11974, 6: 11975}
ZOMBIE_ARMOR_COLOR: tuple = (237, 78, 78)
ZOMBIE_ARROW_COLOR: tuple = (255, 68, 48)
ZOMBIE_EXECUTION_ITEM_ID: int = 6050000180
ZOMBIE_FPS_MOVE_GRAPH: str = 'FPS/Hand/fps_zombie_moveActions.graph'
ZOMBIE_HP_COLOR: tuple = (255, 255, 255)
ZOMBIE_LEGEND_WEAPON_EFFECT_ID: int = 400
ZOMBIE_TPS_IDLE_GRAPH: str = 'TPS/Locomotion/zombie_tps_idle.graph'
ZOMBIE_TPS_IDLE_GRAPH_1: str = 'TPS/Locomotion/zombie_tps_idle_1.graph'
ZOMBIE_TPS_IDLE_GRAPH_2: str = 'TPS/Locomotion/zombie_tps_idle_2.graph'
_: str = 'SystemMsgNode'
_reload_all: bool = True
csb_path: str = 'UIScript/node_chat_message.csb'
end: int = 200099
guise_graph_var_f: list = ['ReloadAnimTime', 'EmptyReloadAnimTime']
guise_graph_var_s_low: dict = {'SkinIdleActivePoseAnimName': 'SkinIdleActivePoseLowAnimName'}
guise_graph_var_v3: list = ['SkinGunOffset']
guise_graph_var_z: list = ['CanInspectionPlayActive', 'SkinAdsRotate']
start: int = 200001
tab_conf: taggeddict = {'ui_list': 'list_1', 'id': 1, 'emotions': ((200001, 200099),), 'size': (26, 26), 'recent_save': 10, 'icon': 200001}
tab_id: int = 1
timezone_to_countrycode: dict = {8: '86', 9: '81'}
toplogo_enemy_show_ease_time: float = 0.3
toplogo_max_friend_opaticy: int = 255
toplogo_min_friend_opaticy: int = 100
toplogo_opaticy_delta: int = 5

class ActionKey(object):
    InteractivePress: int = 1
    InteractiveRelease: int = 2

class AssistAimFollowTriggerMode(enum):
    AdsIn: int = 3
    AdsNoShoot: int = 4
    AdsOut: int = 6
    AdsShoot: int = 5
    NoAdsNoShoot: int = 1
    NoAdsShoot: int = 2
    name_to_values: dict = {'NoAdsNoShoot': 1, 'NoAdsShoot': 2, 'AdsIn': 3, 'AdsNoShoot': 4, 'AdsShoot': 5, 'AdsOut': 6}
    value_to_names: dict = {1: 'NoAdsNoShoot', 2: 'NoAdsShoot', 3: 'AdsIn', 4: 'AdsNoShoot', 5: 'AdsShoot', 6: 'AdsOut'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class AssistAimMode(enum):
    AdsorbTarget: int = 1
    AimAndFollow: int = 9
    AimAndShoot: int = 8
    AimAndShootNoSearch: int = 21
    Follow: int = 7
    MagicBullet: int = 22
    Mark: int = 6
    Melee: int = 5
    SearchTarget: int = 4
    ShootAdsorb: int = 2
    SlowDown: int = 3
    TracingNoSearch: int = 20
    name_to_values: dict = {'AdsorbTarget': 1, 'ShootAdsorb': 2, 'SlowDown': 3, 'SearchTarget': 4, 'Melee': 5, 'Mark': 6, 'Follow': 7, 'AimAndShoot': 8, 'AimAndFollow': 9, 'TracingNoSearch': 20, 'AimAndShootNoSearch': 21, 'MagicBullet': 22}
    value_to_names: dict = {1: 'AdsorbTarget', 2: 'ShootAdsorb', 3: 'SlowDown', 4: 'SearchTarget', 5: 'Melee', 6: 'Mark', 7: 'Follow', 8: 'AimAndShoot', 9: 'AimAndFollow', 20: 'TracingNoSearch', 21: 'AimAndShootNoSearch', 22: 'MagicBullet'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class BannerRule(enum):
    CompletedAct: int = 3
    OnlyOnce: int = 2
    SameDay: int = 1
    name_to_values: dict = {'SameDay': 1, 'OnlyOnce': 2, 'CompletedAct': 3}
    value_to_names: dict = {1: 'SameDay', 2: 'OnlyOnce', 3: 'CompletedAct'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class BigMapSelectPosMode(enum):
    AirDropShop: int = 1
    AirDropShopUav: int = 2
    name_to_values: dict = {'AirDropShop': 1, 'AirDropShopUav': 2}
    value_to_names: dict = {1: 'AirDropShop', 2: 'AirDropShopUav'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class BorderFlag(enum):
    Behind: int = 64
    Bottom: int = 8
    BottomLeft: int = 24
    BottomRight: int = 40
    Empty: int = 0
    InScreen: int = 2
    Left: int = 16
    Right: int = 32
    Top: int = 4
    TopLeft: int = 20
    TopRight: int = 36
    name_to_values: dict = {'Empty': 0, 'InScreen': 2, 'Top': 4, 'Bottom': 8, 'Left': 16, 'Right': 32, 'Behind': 64, 'TopRight': 36, 'TopLeft': 20, 'BottomLeft': 24, 'BottomRight': 40}
    value_to_names: dict = {0: 'Empty', 2: 'InScreen', 4: 'Top', 8: 'Bottom', 16: 'Left', 32: 'Right', 64: 'Behind', 36: 'TopRight', 20: 'TopLeft', 24: 'BottomLeft', 40: 'BottomRight'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ChangeMaterialFunc(enum):
    CustomMaterial: int = 1
    CustomMaterialWholeBody: int = 2
    Empty: int = 0
    ShaderGraph: int = 3
    ShaderGraphWholeBody: int = 4
    name_to_values: dict = {'Empty': 0, 'CustomMaterial': 1, 'CustomMaterialWholeBody': 2, 'ShaderGraph': 3, 'ShaderGraphWholeBody': 4}
    value_to_names: dict = {0: 'Empty', 1: 'CustomMaterial', 2: 'CustomMaterialWholeBody', 3: 'ShaderGraph', 4: 'ShaderGraphWholeBody'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CharctrlResizeHeightReason(enum):
    Cross: int = 1
    Default: int = 0
    Dying: int = 2
    Rescue: int = 3
    name_to_values: dict = {'Default': 0, 'Cross': 1, 'Dying': 2, 'Rescue': 3}
    value_to_names: dict = {0: 'Default', 1: 'Cross', 2: 'Dying', 3: 'Rescue'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CombatStatusEnum(enum):
    BeHit: int = 2
    Fire: int = 1
    name_to_values: dict = {'Fire': 1, 'BeHit': 2}
    value_to_names: dict = {1: 'Fire', 2: 'BeHit'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CommonClickMode(enum):
    Double: int = 2
    Empty: int = 0
    Long: int = 3
    Single: int = 1
    name_to_values: dict = {'Empty': 0, 'Single': 1, 'Double': 2, 'Long': 3}
    value_to_names: dict = {0: 'Empty', 1: 'Single', 2: 'Double', 3: 'Long'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CommonItemTag(enum):
    Collection: int = 1
    name_to_values: dict = {'Collection': 1}
    value_to_names: dict = {1: 'Collection'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CommonPopBoxNeedShow(enum):
    CrossPlatformTip: int = 1
    name_to_values: dict = {'CrossPlatformTip': 1}
    value_to_names: dict = {1: 'CrossPlatformTip'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class CommonTopLogoIcon(enum):
    AirDrop: int = 139
    Hunt: int = 156
    MissionHunt: int = 148
    MissionOccupy: int = 146
    MissionSearch: int = 147
    MissionSmall: int = 172
    OccupyTarget: int = 154
    SearchBox: int = 155
    name_to_values: dict = {'OccupyTarget': 154, 'SearchBox': 155, 'Hunt': 156, 'AirDrop': 139, 'MissionOccupy': 146, 'MissionSearch': 147, 'MissionHunt': 148, 'MissionSmall': 172}
    value_to_names: dict = {154: 'OccupyTarget', 155: 'SearchBox', 156: 'Hunt', 139: 'AirDrop', 146: 'MissionOccupy', 147: 'MissionSearch', 148: 'MissionHunt', 172: 'MissionSmall'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ControllerSensitivityCurve(enum):
    DYNAMIC: int = 3
    LINEAR: int = 1
    NORMAL: int = 0
    name_to_values: dict = {'NORMAL': 0, 'LINEAR': 1, 'DYNAMIC': 3}
    value_to_names: dict = {0: 'NORMAL', 1: 'LINEAR', 3: 'DYNAMIC'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class DetectionConfigType(enum):
    LayoutIndex: int = 1
    SensitivityIndex: int = 2
    name_to_values: dict = {'LayoutIndex': 1, 'SensitivityIndex': 2}
    value_to_names: dict = {1: 'LayoutIndex', 2: 'SensitivityIndex'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ENGINE_VERSION(object):
    DEV: int = 650000
    V202101: int = 530045
    V202302: int = 639267
    V202302_01: int = 639268
    V202302_02: int = 639271
    V202302_03: int = 639273
    V202302_04: int = 639274
    V202302_05: int = 639275
    V202303: int = 650000
    V202303_01: int = 650001
    V202303_02: int = 650002
    V202303_03: int = 650003
    V202303_DEV: int = 650020
    V202401: int = 750000

class FaceCustomType(enum):
    BoneEye: int = 2000
    BoneJaw: int = 2003
    BoneMouth: int = 2002
    BoneNose: int = 2001
    Hair: int = 1002
    HairColor: int = 1006
    Mask: int = 1003
    Mustache: int = 1005
    Scar: int = 1004
    SkinColor: int = 1001
    name_to_values: dict = {'SkinColor': 1001, 'Hair': 1002, 'Mask': 1003, 'Scar': 1004, 'Mustache': 1005, 'HairColor': 1006, 'BoneEye': 2000, 'BoneNose': 2001, 'BoneMouth': 2002, 'BoneJaw': 2003}
    value_to_names: dict = {1001: 'SkinColor', 1002: 'Hair', 1003: 'Mask', 1004: 'Scar', 1005: 'Mustache', 1006: 'HairColor', 2000: 'BoneEye', 2001: 'BoneNose', 2002: 'BoneMouth', 2003: 'BoneJaw'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class FireMode(enum):
    FIRE_ADS: int = 2
    FIRE_DIY: int = 4
    FIRE_ONLY: int = 1
    FIRE_REAL_ADS: int = 3
    name_to_values: dict = {'FIRE_ONLY': 1, 'FIRE_ADS': 2, 'FIRE_REAL_ADS': 3, 'FIRE_DIY': 4}
    value_to_names: dict = {1: 'FIRE_ONLY', 2: 'FIRE_ADS', 3: 'FIRE_REAL_ADS', 4: 'FIRE_DIY'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class FpsUnitModelIdHardCode(enum):
    ParachuteL: int = 16
    ParachuteR: int = 17
    name_to_values: dict = {'ParachuteL': 16, 'ParachuteR': 17}
    value_to_names: dict = {16: 'ParachuteL', 17: 'ParachuteR'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class FrontSightMode(enum):
    Circle: int = 2
    Cross: int = 1
    name_to_values: dict = {'Cross': 1, 'Circle': 2}
    value_to_names: dict = {1: 'Cross', 2: 'Circle'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class FuncCompParachuteStage(enum):
    FreeFall: int = 1
    FreeFallWithGun: int = 3
    OnAircraft: int = 0
    Parachute: int = 2
    ParachuteEnd: int = 4
    name_to_values: dict = {'OnAircraft': 0, 'FreeFall': 1, 'Parachute': 2, 'FreeFallWithGun': 3, 'ParachuteEnd': 4}
    value_to_names: dict = {0: 'OnAircraft', 1: 'FreeFall', 2: 'Parachute', 3: 'FreeFallWithGun', 4: 'ParachuteEnd'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GameInputType(enum):
    MouseInput: int = 3
    MouseMove: int = 2
    MoveInput: int = 1
    name_to_values: dict = {'MoveInput': 1, 'MouseMove': 2, 'MouseInput': 3}
    value_to_names: dict = {1: 'MoveInput', 2: 'MouseMove', 3: 'MouseInput'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GameSound(enum):
    Bomb: int = 2
    CompoundBow: int = 5
    FootStep: int = 1
    Gun: int = 0
    Parachute: int = 3
    Vehicle: int = 4
    name_to_values: dict = {'Gun': 0, 'FootStep': 1, 'Bomb': 2, 'Parachute': 3, 'Vehicle': 4, 'CompoundBow': 5}
    value_to_names: dict = {0: 'Gun', 1: 'FootStep', 2: 'Bomb', 3: 'Parachute', 4: 'Vehicle', 5: 'CompoundBow'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GlobalSensiMode(enum):
    HIGH: int = 3
    LOW: int = 1
    MID: int = 2
    USER: int = 4
    name_to_values: dict = {'LOW': 1, 'MID': 2, 'HIGH': 3, 'USER': 4}
    value_to_names: dict = {1: 'LOW', 2: 'MID', 3: 'HIGH', 4: 'USER'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GraphDisableSlaveReason(enum):
    DEFAULT: int = 0
    EXECUTION: int = 2
    KNOCK_DOWN: int = 3
    LOSE_CLIENT: int = 1
    PARACHUTE_LOSE_CLIENT: int = 4
    ROBOT_CONTROL: int = 5
    name_to_values: dict = {'DEFAULT': 0, 'LOSE_CLIENT': 1, 'EXECUTION': 2, 'KNOCK_DOWN': 3, 'PARACHUTE_LOSE_CLIENT': 4, 'ROBOT_CONTROL': 5}
    value_to_names: dict = {0: 'DEFAULT', 1: 'LOSE_CLIENT', 2: 'EXECUTION', 3: 'KNOCK_DOWN', 4: 'PARACHUTE_LOSE_CLIENT', 5: 'ROBOT_CONTROL'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GunProperty(enum):
    accuracy_attri: int = 3
    damage_attri: int = 0
    fire_rate_attri: int = 5
    flexibility_attri: int = 4
    name_to_values: dict = {'damage_attri': 0, 'range_attri': 1, 'recoil_attri': 2, 'accuracy_attri': 3, 'flexibility_attri': 4, 'fire_rate_attri': 5}
    range_attri: int = 1
    recoil_attri: int = 2
    value_to_names: dict = {0: 'damage_attri', 1: 'range_attri', 2: 'recoil_attri', 3: 'accuracy_attri', 4: 'flexibility_attri', 5: 'fire_rate_attri'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GunUpgradeFeature(enum):
    UPGRADE_FEATURE_BASE: str = 'base'
    UPGRADE_FEATURE_BULLET_TRACE: str = 'bullet_trace'
    UPGRADE_FEATURE_DYNAMIC_KULL_UI: str = 'kill_hud_csb_path'
    UPGRADE_FEATURE_FIRE_LIGHT: str = 'fire_light'
    UPGRADE_FEATURE_FIRE_TIPS: str = 'tip_fire'
    UPGRADE_FEATURE_FIRST_RAISE_ANIM: str = 'first_raise_anim'
    UPGRADE_FEATURE_HIGH_IRON_SIGHT: str = 'high_iron_sight'
    UPGRADE_FEATURE_HIT_EFFECT: str = 'hit_effect'
    UPGRADE_FEATURE_INSPECT_ANIM: str = 'inspect_anim'
    UPGRADE_FEATURE_IRON_SIGHT: str = 'iron_sight'
    UPGRADE_FEATURE_KILL_EFFECT: str = 'kill_effect'
    UPGRADE_FEATURE_KILL_NUMBER: str = 'kill_num'
    UPGRADE_FEATURE_KILL_UI: str = 'kill_hud_id'
    UPGRADE_FEATURE_LINKAGE_RAISE_ANIM: str = 'linkage_raise_anim'
    UPGRADE_FEATURE_NEW_APPEAR: str = 'new_appear'
    UPGRADE_FEATURE_NEW_SOUND: str = 'new_sound_effect'
    UPGRADE_FEATURE_RAISE_ANIM: str = 'raise_anim'
    UPGRADE_FEATURE_RECEVIER_SHOW_AMMO: str = 'recevier_show_ammo'
    UPGRADE_FEATURE_RELOAD_ANIM: str = 'reload_anim'
    UPGRADE_FEATURE_RELOAD_TRANSFORM: str = 'reload_transform'
    UPGRADE_FEATURE_SHOW_3P_WEAPON: str = 'show_3p_weapon'
    UPGRADE_FEATURE_SPECIAL_SKILL: str = 'weapon_special_skill'
    UPGRADE_FEATURE_TRAIL_EFFECT: str = 'trail_effect'
    UPGRADE_FEATURE_UNLOCK_ITEM: str = 'bind_items'
    UPGRADE_FEATURE_UNLOCK_ITEM_1: str = 'bind_items_1'
    UPGRADE_FEATURE_UNLOCK_ITEM_2: str = 'bind_items_2'
    UPGRADE_FEATURE_UNLOCK_ITEM_3: str = 'bind_items_3'
    UPGRADE_FEATURE_UNLOCK_PARTS: str = 'unlock_part'
    name_to_values: dict = {'UPGRADE_FEATURE_BASE': 'base', 'UPGRADE_FEATURE_KILL_UI': 'kill_hud_id', 'UPGRADE_FEATURE_DYNAMIC_KULL_UI': 'kill_hud_csb_path', 'UPGRADE_FEATURE_FIRE_TIPS': 'tip_fire', 'UPGRADE_FEATURE_BULLET_TRACE': 'bullet_trace', 'UPGRADE_FEATURE_HIT_EFFECT': 'hit_effect', 'UPGRADE_FEATURE_TRAIL_EFFECT': 'trail_effect', 'UPGRADE_FEATURE_INSPECT_ANIM': 'inspect_anim', 'UPGRADE_FEATURE_RAISE_ANIM': 'raise_anim', 'UPGRADE_FEATURE_RELOAD_ANIM': 'reload_anim', 'UPGRADE_FEATURE_KILL_EFFECT': 'kill_effect', 'UPGRADE_FEATURE_UNLOCK_PARTS': 'unlock_part', 'UPGRADE_FEATURE_NEW_APPEAR': 'new_appear', 'UPGRADE_FEATURE_KILL_NUMBER': 'kill_num', 'UPGRADE_FEATURE_UNLOCK_ITEM': 'bind_items', 'UPGRADE_FEATURE_UNLOCK_ITEM_1': 'bind_items_1', 'UPGRADE_FEATURE_UNLOCK_ITEM_2': 'bind_items_2', 'UPGRADE_FEATURE_UNLOCK_ITEM_3': 'bind_items_3', 'UPGRADE_FEATURE_IRON_SIGHT': 'iron_sight', 'UPGRADE_FEATURE_HIGH_IRON_SIGHT': 'high_iron_sight', 'UPGRADE_FEATURE_NEW_SOUND': 'new_sound_effect', 'UPGRADE_FEATURE_FIRE_LIGHT': 'fire_light', 'UPGRADE_FEATURE_RECEVIER_SHOW_AMMO': 'recevier_show_ammo', 'UPGRADE_FEATURE_RELOAD_TRANSFORM': 'reload_transform', 'UPGRADE_FEATURE_LINKAGE_RAISE_ANIM': 'linkage_raise_anim', 'UPGRADE_FEATURE_FIRST_RAISE_ANIM': 'first_raise_anim', 'UPGRADE_FEATURE_SPECIAL_SKILL': 'weapon_special_skill', 'UPGRADE_FEATURE_SHOW_3P_WEAPON': 'show_3p_weapon'}
    value_to_names: dict = {'base': 'UPGRADE_FEATURE_BASE', 'kill_hud_id': 'UPGRADE_FEATURE_KILL_UI', 'kill_hud_csb_path': 'UPGRADE_FEATURE_DYNAMIC_KULL_UI', 'tip_fire': 'UPGRADE_FEATURE_FIRE_TIPS', 'bullet_trace': 'UPGRADE_FEATURE_BULLET_TRACE', 'hit_effect': 'UPGRADE_FEATURE_HIT_EFFECT', 'trail_effect': 'UPGRADE_FEATURE_TRAIL_EFFECT', 'inspect_anim': 'UPGRADE_FEATURE_INSPECT_ANIM', 'raise_anim': 'UPGRADE_FEATURE_RAISE_ANIM', 'reload_anim': 'UPGRADE_FEATURE_RELOAD_ANIM', 'kill_effect': 'UPGRADE_FEATURE_KILL_EFFECT', 'unlock_part': 'UPGRADE_FEATURE_UNLOCK_PARTS', 'new_appear': 'UPGRADE_FEATURE_NEW_APPEAR', 'kill_num': 'UPGRADE_FEATURE_KILL_NUMBER', 'bind_items': 'UPGRADE_FEATURE_UNLOCK_ITEM', 'bind_items_1': 'UPGRADE_FEATURE_UNLOCK_ITEM_1', 'bind_items_2': 'UPGRADE_FEATURE_UNLOCK_ITEM_2', 'bind_items_3': 'UPGRADE_FEATURE_UNLOCK_ITEM_3', 'iron_sight': 'UPGRADE_FEATURE_IRON_SIGHT', 'high_iron_sight': 'UPGRADE_FEATURE_HIGH_IRON_SIGHT', 'new_sound_effect': 'UPGRADE_FEATURE_NEW_SOUND', 'fire_light': 'UPGRADE_FEATURE_FIRE_LIGHT', 'recevier_show_ammo': 'UPGRADE_FEATURE_RECEVIER_SHOW_AMMO', 'reload_transform': 'UPGRADE_FEATURE_RELOAD_TRANSFORM', 'linkage_raise_anim': 'UPGRADE_FEATURE_LINKAGE_RAISE_ANIM', 'first_raise_anim': 'UPGRADE_FEATURE_FIRST_RAISE_ANIM', 'weapon_special_skill': 'UPGRADE_FEATURE_SPECIAL_SKILL', 'show_3p_weapon': 'UPGRADE_FEATURE_SHOW_3P_WEAPON'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GyroscopeCalibration(enum):
    Close: int = 0
    Open: int = 1
    name_to_values: dict = {'Close': 0, 'Open': 1}
    value_to_names: dict = {0: 'Close', 1: 'Open'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GyroscopeHorizontalReverse(enum):
    Close: int = 0
    Open: int = 1
    name_to_values: dict = {'Close': 0, 'Open': 1}
    value_to_names: dict = {0: 'Close', 1: 'Open'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GyroscopeMode(enum):
    AimOpen: int = 1
    AlwaysOpen: int = 0
    Never: int = 2
    name_to_values: dict = {'AlwaysOpen': 0, 'AimOpen': 1, 'Never': 2}
    value_to_names: dict = {0: 'AlwaysOpen', 1: 'AimOpen', 2: 'Never'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GyroscopeModeVehicle(enum):
    Close: int = 0
    Open: int = 1
    name_to_values: dict = {'Open': 1, 'Close': 0}
    value_to_names: dict = {1: 'Open', 0: 'Close'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GyroscopeSwitchMode(enum):
    AimEnd: int = 2
    AimStart: int = 1
    Lerp: int = 3
    name_to_values: dict = {'AimStart': 1, 'AimEnd': 2, 'Lerp': 3}
    value_to_names: dict = {1: 'AimStart', 2: 'AimEnd', 3: 'Lerp'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GyroscopeType(enum):
    Gyroscope: int = 1
    GyroscopePose: int = 3
    PoseSensor: int = 2
    name_to_values: dict = {'Gyroscope': 1, 'PoseSensor': 2, 'GyroscopePose': 3}
    value_to_names: dict = {1: 'Gyroscope', 2: 'PoseSensor', 3: 'GyroscopePose'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class GyroscopeVerticalReverse(enum):
    Close: int = 0
    Open: int = 1
    name_to_values: dict = {'Close': 0, 'Open': 1}
    value_to_names: dict = {0: 'Close', 1: 'Open'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class HallLevel(enum):
    LEVEL_ACTIVITY_INVITE: int = 74
    LEVEL_ACT_GUN_SKIN: int = 18
    LEVEL_ACT_LIGHT_AVATAR: int = 21
    LEVEL_ACT_LIGHT_WEAPON: int = 20
    LEVEL_COMMON_SHOW: int = 12
    LEVEL_GACHA_SHOW: int = 13
    LEVEL_GRAND_THEFT_OPEN_BOX: int = 71
    LEVEL_GRAND_THEFT_RANK: int = 70
    LEVEL_GUN_BACKPACK: int = 5
    LEVEL_GUN_SHOW: int = 6
    LEVEL_GUN_SHOW_NEW: int = 28
    LEVEL_HALL_EXECUTE_SHOW: int = 97
    LEVEL_HALL_LIGHT_AVATAR: int = 16
    LEVEL_HALL_LIGHT_WEAPON: int = 15
    LEVEL_HALL_LIGHT_WEAPON_MALL: int = 100
    LEVEL_HALL_MALL: int = 8
    LEVEL_HALL_WAREHOUSE: int = 2
    LEVEL_HALL_WAREHOUSE_NEW: int = 89
    LEVEL_HALL_WAREHOUSE_TRAIL: int = 91
    LEVEL_LBS_GUN_REFIT: int = 17
    LEVEL_MAIN_HALL: int = 1
    LEVEL_PASS: int = 14
    LEVEL_PERSONAL_SPACE: int = 7
    LEVEL_RANK: int = 10
    name_to_values: dict = {'LEVEL_MAIN_HALL': 1, 'LEVEL_HALL_WAREHOUSE': 2, 'LEVEL_HALL_MALL': 8, 'LEVEL_GUN_BACKPACK': 5, 'LEVEL_GUN_SHOW': 6, 'LEVEL_PERSONAL_SPACE': 7, 'LEVEL_RANK': 10, 'LEVEL_COMMON_SHOW': 12, 'LEVEL_GACHA_SHOW': 13, 'LEVEL_PASS': 14, 'LEVEL_HALL_LIGHT_WEAPON': 15, 'LEVEL_HALL_LIGHT_WEAPON_MALL': 100, 'LEVEL_HALL_LIGHT_AVATAR': 16, 'LEVEL_LBS_GUN_REFIT': 17, 'LEVEL_ACT_GUN_SKIN': 18, 'LEVEL_ACT_LIGHT_WEAPON': 20, 'LEVEL_ACT_LIGHT_AVATAR': 21, 'LEVEL_GUN_SHOW_NEW': 28, 'LEVEL_GRAND_THEFT_RANK': 70, 'LEVEL_GRAND_THEFT_OPEN_BOX': 71, 'LEVEL_ACTIVITY_INVITE': 74, 'LEVEL_HALL_WAREHOUSE_NEW': 89, 'LEVEL_HALL_WAREHOUSE_TRAIL': 91, 'LEVEL_HALL_EXECUTE_SHOW': 97}
    value_to_names: dict = {1: 'LEVEL_MAIN_HALL', 2: 'LEVEL_HALL_WAREHOUSE', 8: 'LEVEL_HALL_MALL', 5: 'LEVEL_GUN_BACKPACK', 6: 'LEVEL_GUN_SHOW', 7: 'LEVEL_PERSONAL_SPACE', 10: 'LEVEL_RANK', 12: 'LEVEL_COMMON_SHOW', 13: 'LEVEL_GACHA_SHOW', 14: 'LEVEL_PASS', 15: 'LEVEL_HALL_LIGHT_WEAPON', 100: 'LEVEL_HALL_LIGHT_WEAPON_MALL', 16: 'LEVEL_HALL_LIGHT_AVATAR', 17: 'LEVEL_LBS_GUN_REFIT', 18: 'LEVEL_ACT_GUN_SKIN', 20: 'LEVEL_ACT_LIGHT_WEAPON', 21: 'LEVEL_ACT_LIGHT_AVATAR', 28: 'LEVEL_GUN_SHOW_NEW', 70: 'LEVEL_GRAND_THEFT_RANK', 71: 'LEVEL_GRAND_THEFT_OPEN_BOX', 74: 'LEVEL_ACTIVITY_INVITE', 89: 'LEVEL_HALL_WAREHOUSE_NEW', 91: 'LEVEL_HALL_WAREHOUSE_TRAIL', 97: 'LEVEL_HALL_EXECUTE_SHOW'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class HallWeaponType(enum):
    Default: int = 0
    Gacha: int = 3
    GunSmith: int = 1
    Mall: int = 2
    name_to_values: dict = {'Default': 0, 'GunSmith': 1, 'Mall': 2, 'Gacha': 3}
    value_to_names: dict = {0: 'Default', 1: 'GunSmith', 2: 'Mall', 3: 'Gacha'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class HeartbeatSpellState(enum):
    Empty: int = 0
    Spelling: int = 1
    Waiting: int = 2
    name_to_values: dict = {'Empty': 0, 'Spelling': 1, 'Waiting': 2}
    value_to_names: dict = {0: 'Empty', 1: 'Spelling', 2: 'Waiting'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class HeroWindowType(enum):
    ACTION: int = 4
    Execution: int = 2
    MVP: int = 3
    Skin: int = 1
    name_to_values: dict = {'Skin': 1, 'Execution': 2, 'MVP': 3, 'ACTION': 4}
    value_to_names: dict = {1: 'Skin', 2: 'Execution', 3: 'MVP', 4: 'ACTION'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class HitFeedbackColor(enum):
    Green: int = 1
    Red: int = 0
    name_to_values: dict = {'Red': 0, 'Green': 1}
    value_to_names: dict = {0: 'Red', 1: 'Green'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class HitNoticeMode(enum):
    Mode_2D: int = 1
    Mode_3D: int = 2
    name_to_values: dict = {'Mode_2D': 1, 'Mode_3D': 2}
    value_to_names: dict = {1: 'Mode_2D', 2: 'Mode_3D'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class HotSpotMainUIStyle(enum):
    Version_1: int = 1
    Version_2: int = 2
    name_to_values: dict = {'Version_1': 1, 'Version_2': 2}
    value_to_names: dict = {1: 'Version_1', 2: 'Version_2'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class IconTextureType(enum):
    CDNTexture: int = 3
    DLCDefaultTexture: int = 4
    DLCTexture: int = 2
    NONE: int = 0
    Texture: int = 1
    name_to_values: dict = {'NONE': 0, 'Texture': 1, 'DLCTexture': 2, 'CDNTexture': 3, 'DLCDefaultTexture': 4}
    value_to_names: dict = {0: 'NONE', 1: 'Texture', 2: 'DLCTexture', 3: 'CDNTexture', 4: 'DLCDefaultTexture'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class IgChatTextId(enum):
    TEXT_ID_CASH: int = 1
    TEXT_ID_ITEM_ID: int = 5
    TEXT_ID_MEDICINE: int = 2
    TEXT_ID_THROWABLE_WEAPON: int = 3
    TEXT_ID_WEAPON: int = 4
    name_to_values: dict = {'TEXT_ID_CASH': 1, 'TEXT_ID_MEDICINE': 2, 'TEXT_ID_THROWABLE_WEAPON': 3, 'TEXT_ID_WEAPON': 4, 'TEXT_ID_ITEM_ID': 5}
    value_to_names: dict = {1: 'TEXT_ID_CASH', 2: 'TEXT_ID_MEDICINE', 3: 'TEXT_ID_THROWABLE_WEAPON', 4: 'TEXT_ID_WEAPON', 5: 'TEXT_ID_ITEM_ID'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class LayoutShareType(enum):
    AIR: str = 'AIR'
    HUD1: str = 'HUD1'
    HUD2: str = 'HUD2'
    PILOT: str = 'PILOT'
    SENS: str = 'SENS'
    name_to_values: dict = {'HUD1': 'HUD1', 'HUD2': 'HUD2', 'PILOT': 'PILOT', 'AIR': 'AIR', 'SENS': 'SENS'}
    value_to_names: dict = {'HUD1': 'HUD1', 'HUD2': 'HUD2', 'PILOT': 'PILOT', 'AIR': 'AIR', 'SENS': 'SENS'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class LimitYuanbaoBanUseWindowKey(enum):
    ClanCreate: str = 'ClanCreate'
    name_to_values: dict = {'ClanCreate': 'ClanCreate'}
    value_to_names: dict = {'ClanCreate': 'ClanCreate'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class LoadingBarCountDownTxtType(enum):
    Percent: int = 1
    Second: int = 0
    name_to_values: dict = {'Second': 0, 'Percent': 1}
    value_to_names: dict = {0: 'Second', 1: 'Percent'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MainUIType(enum):
    HotSpot: int = 2
    Moba: int = 1
    name_to_values: dict = {'Moba': 1, 'HotSpot': 2}
    value_to_names: dict = {1: 'Moba', 2: 'HotSpot'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MapCenterTickMode(enum):
    ROTATE_MAP: int = 0
    ROTATE_TAG: int = 1
    name_to_values: dict = {'ROTATE_MAP': 0, 'ROTATE_TAG': 1}
    value_to_names: dict = {0: 'ROTATE_MAP', 1: 'ROTATE_TAG'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MapTagType(enum):
    AirDrop: int = 14
    AirDropShop: int = 7
    AirlineArrow: int = 2
    CenterTag: int = 5
    ChaosUav: int = 20
    Crack: int = 18
    EnergyStronghold: int = 19
    Hunt: int = 8
    LightAttackMark: int = 17
    MapText: int = 1
    Mission: int = 13
    Radar: int = 9
    Remind: int = 11
    RobotDebug: int = 3
    Shop: int = 16
    TalentMark: int = 15
    TeammateMark: int = 12
    TeammateTag: int = 6
    Uav: int = 4
    ValDrone: int = 23
    Vehicle: int = 10
    ZombieNeedle: int = 21
    name_to_values: dict = {'MapText': 1, 'AirlineArrow': 2, 'RobotDebug': 3, 'Uav': 4, 'CenterTag': 5, 'TeammateTag': 6, 'AirDropShop': 7, 'Hunt': 8, 'Radar': 9, 'Vehicle': 10, 'Remind': 11, 'TeammateMark': 12, 'Mission': 13, 'AirDrop': 14, 'TalentMark': 15, 'Shop': 16, 'LightAttackMark': 17, 'Crack': 18, 'EnergyStronghold': 19, 'ChaosUav': 20, 'ZombieNeedle': 21, 'ValDrone': 23}
    value_to_names: dict = {1: 'MapText', 2: 'AirlineArrow', 3: 'RobotDebug', 4: 'Uav', 5: 'CenterTag', 6: 'TeammateTag', 7: 'AirDropShop', 8: 'Hunt', 9: 'Radar', 10: 'Vehicle', 11: 'Remind', 12: 'TeammateMark', 13: 'Mission', 14: 'AirDrop', 15: 'TalentMark', 16: 'Shop', 17: 'LightAttackMark', 18: 'Crack', 19: 'EnergyStronghold', 20: 'ChaosUav', 21: 'ZombieNeedle', 23: 'ValDrone'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MedExpandDir(enum):
    Right: int = 1
    UP: int = 0
    name_to_values: dict = {'UP': 0, 'Right': 1}
    value_to_names: dict = {0: 'UP', 1: 'Right'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MessageSource(enum):
    MINE_TALK: int = 1
    MINE_TALK_VOICE: int = 3
    OTHER_TALK: int = 2
    OTHER_TALK_VOICE: int = 4
    SYSTEM: int = 5
    name_to_values: dict = {'MINE_TALK': 1, 'OTHER_TALK': 2, 'MINE_TALK_VOICE': 3, 'OTHER_TALK_VOICE': 4, 'SYSTEM': 5}
    value_to_names: dict = {1: 'MINE_TALK', 2: 'OTHER_TALK', 3: 'MINE_TALK_VOICE', 4: 'OTHER_TALK_VOICE', 5: 'SYSTEM'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MobaDriveMode(enum):
    Drive_Mode_1: int = 1
    Drive_Mode_2: int = 2
    name_to_values: dict = {'Drive_Mode_1': 1, 'Drive_Mode_2': 2}
    value_to_names: dict = {1: 'Drive_Mode_1', 2: 'Drive_Mode_2'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MobaMainUIStyle(enum):
    Version_1: int = 1
    Version_2: int = 2
    name_to_values: dict = {'Version_1': 1, 'Version_2': 2}
    value_to_names: dict = {1: 'Version_1', 2: 'Version_2'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ModelHipDirection(enum):
    B: int = 1
    F: int = 0
    LB: int = 4
    LF: int = 2
    RB: int = 5
    RF: int = 3
    name_to_values: dict = {'F': 0, 'B': 1, 'LF': 2, 'RF': 3, 'LB': 4, 'RB': 5}
    value_to_names: dict = {0: 'F', 1: 'B', 2: 'LF', 3: 'RF', 4: 'LB', 5: 'RB'}

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

class MoveDirection(enum):
    Backward: int = 2
    Forward: int = 8
    Idle: int = 0
    Left: int = 4
    LeftBackward: int = 1
    LeftForward: int = 7
    Right: int = 6
    RightBackward: int = 3
    RightForward: int = 9
    name_to_values: dict = {'Idle': 0, 'LeftBackward': 1, 'Backward': 2, 'RightBackward': 3, 'Left': 4, 'Right': 6, 'LeftForward': 7, 'Forward': 8, 'RightForward': 9}
    value_to_names: dict = {0: 'Idle', 1: 'LeftBackward', 2: 'Backward', 3: 'RightBackward', 4: 'Left', 6: 'Right', 7: 'LeftForward', 8: 'Forward', 9: 'RightForward'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MoveRotationMode(enum):
    FollowFace: int = 0
    FollowJoystick: int = 1
    LockFace: int = 2
    name_to_values: dict = {'FollowFace': 0, 'FollowJoystick': 1, 'LockFace': 2}
    value_to_names: dict = {0: 'FollowFace', 1: 'FollowJoystick', 2: 'LockFace'}

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

class MoveStartDir(enum):
    MoveB: int = 3
    MoveF: int = 0
    MoveLB: int = 4
    MoveLF: int = 1
    MoveRB: int = 5
    MoveRF: int = 2
    name_to_values: dict = {'MoveF': 0, 'MoveLF': 1, 'MoveRF': 2, 'MoveB': 3, 'MoveLB': 4, 'MoveRB': 5}
    value_to_names: dict = {0: 'MoveF', 1: 'MoveLF', 2: 'MoveRF', 3: 'MoveB', 4: 'MoveLB', 5: 'MoveRB'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class MpFpsAction(enum):
    DropWeapon: int = 4
    Fire: int = 1
    Idle: int = 0
    Inspection: int = 7
    Melee: int = 6
    RaiseWeapon: int = 3
    Rechamber: int = 5
    Reload: int = 2
    name_to_values: dict = {'Idle': 0, 'Fire': 1, 'Reload': 2, 'RaiseWeapon': 3, 'DropWeapon': 4, 'Rechamber': 5, 'Melee': 6, 'Inspection': 7}
    value_to_names: dict = {0: 'Idle', 1: 'Fire', 2: 'Reload', 3: 'RaiseWeapon', 4: 'DropWeapon', 5: 'Rechamber', 6: 'Melee', 7: 'Inspection'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class OperationFireModeR(enum):
    FIX: int = 2
    FOLLOW: int = 1
    name_to_values: dict = {'FOLLOW': 1, 'FIX': 2}
    value_to_names: dict = {1: 'FOLLOW', 2: 'FIX'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class OperationMoveAndRFireMode(enum):
    BtnMoveBtnFire: int = 2
    PanelMoveBtnFire: int = 0
    PanelMovePanelFire: int = 1
    name_to_values: dict = {'PanelMoveBtnFire': 0, 'PanelMovePanelFire': 1, 'BtnMoveBtnFire': 2}
    value_to_names: dict = {0: 'PanelMoveBtnFire', 1: 'PanelMovePanelFire', 2: 'BtnMoveBtnFire'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class OperationMoveMode(enum):
    JOYSTICK: int = 2
    SCREEN: int = 1
    name_to_values: dict = {'SCREEN': 1, 'JOYSTICK': 2}
    value_to_names: dict = {1: 'SCREEN', 2: 'JOYSTICK'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ParachuteJumpBtnState(enum):
    Cinematics: int = 1
    CloseParachute: int = 6
    End: int = 7
    HighSkyOpen: int = 8
    LeaveAirplane: int = 3
    LeaveTrainerAirplane: int = 9
    LeaveTrainerPara: int = 10
    OpenParachute: int = 5
    Preview: int = 2
    WaitOpen: int = 4
    name_to_values: dict = {'Cinematics': 1, 'Preview': 2, 'LeaveAirplane': 3, 'WaitOpen': 4, 'OpenParachute': 5, 'CloseParachute': 6, 'End': 7, 'HighSkyOpen': 8, 'LeaveTrainerAirplane': 9, 'LeaveTrainerPara': 10}
    value_to_names: dict = {1: 'Cinematics', 2: 'Preview', 3: 'LeaveAirplane', 4: 'WaitOpen', 5: 'OpenParachute', 6: 'CloseParachute', 7: 'End', 8: 'HighSkyOpen', 9: 'LeaveTrainerAirplane', 10: 'LeaveTrainerPara'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PersonalCardSource(SlotsEnum):
    CHAT: int = 4
    CLAN: int = 18
    COMBAT_HISTORY_HotSpot: int = 17
    COMBAT_HISTORY_Moba: int = 15
    COMBAT_HISTORY_SquadFight: int = 16
    FRIEND: int = 0
    FRIEND_RECENT: int = 1
    FRIEND_RECOMMEND: int = 3
    FRIEND_SEARCH: int = 2
    INVITE_CLAN: int = 7
    INVITE_FRIEND: int = 5
    INVITE_RECENT: int = 6
    MVP_HotSpot: int = 10
    MVP_Moba: int = 8
    MVP_SquadFight: int = 9
    SELF: int = 19
    SETTLEMENT_DETAILS_HotSpot: int = 14
    SETTLEMENT_DETAILS_Moba: int = 12
    SETTLEMENT_DETAILS_SquadFight: int = 13
    SETTLEMENT_TEAM: int = 11

class PopupLevel2WindowBtnType(enum):
    NoButton: int = 1
    OneButton: int = 2
    TwoButton: int = 3
    name_to_values: dict = {'NoButton': 1, 'OneButton': 2, 'TwoButton': 3}
    value_to_names: dict = {1: 'NoButton', 2: 'OneButton', 3: 'TwoButton'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PreScaleWindowState(enum):
    CanBuy: int = 1
    CanGet: int = 3
    Got: int = 4
    WaitForGetReward: int = 2
    name_to_values: dict = {'CanBuy': 1, 'WaitForGetReward': 2, 'CanGet': 3, 'Got': 4}
    value_to_names: dict = {1: 'CanBuy', 2: 'WaitForGetReward', 3: 'CanGet', 4: 'Got'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PrizeLevel(enum):
    Medium: int = 2
    Super: int = 1
    name_to_values: dict = {'Super': 1, 'Medium': 2}
    value_to_names: dict = {1: 'Super', 2: 'Medium'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ProneState(enum):
    Default: int = 0
    EnterProne: int = 1
    ExitProne: int = 3
    Proning: int = 2
    name_to_values: dict = {'Default': 0, 'EnterProne': 1, 'Proning': 2, 'ExitProne': 3}
    value_to_names: dict = {0: 'Default', 1: 'EnterProne', 2: 'Proning', 3: 'ExitProne'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RankingWindowTab(enum):
    BattleRoyale: int = 100
    GunGod: int = 300
    ShootingRange: int = 400
    SquadFight: int = 200
    name_to_values: dict = {'BattleRoyale': 100, 'SquadFight': 200, 'GunGod': 300, 'ShootingRange': 400}
    value_to_names: dict = {100: 'BattleRoyale', 200: 'SquadFight', 300: 'GunGod', 400: 'ShootingRange'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class RoomTab(enum):
    TAB_ADD_FRIEND: int = 1
    TAB_CHAT: int = 2
    TAB_KICK_MEMBER: int = 4
    TAB_MEMBER_INFO: int = 10
    TAB_MUTE_MEMBER: int = 9
    TAB_SWAP_SLOT: int = 3
    TAB_SWAP_TO_TEAM: int = 7
    TAB_SWAP_TO_WATCH: int = 6
    TAB_TRANSFER_ROOMOWNER: int = 5
    TAB_UNMUTE_MEMBER: int = 8
    name_to_values: dict = {'TAB_ADD_FRIEND': 1, 'TAB_CHAT': 2, 'TAB_SWAP_SLOT': 3, 'TAB_KICK_MEMBER': 4, 'TAB_TRANSFER_ROOMOWNER': 5, 'TAB_SWAP_TO_WATCH': 6, 'TAB_SWAP_TO_TEAM': 7, 'TAB_UNMUTE_MEMBER': 8, 'TAB_MUTE_MEMBER': 9, 'TAB_MEMBER_INFO': 10}
    value_to_names: dict = {1: 'TAB_ADD_FRIEND', 2: 'TAB_CHAT', 3: 'TAB_SWAP_SLOT', 4: 'TAB_KICK_MEMBER', 5: 'TAB_TRANSFER_ROOMOWNER', 6: 'TAB_SWAP_TO_WATCH', 7: 'TAB_SWAP_TO_TEAM', 8: 'TAB_UNMUTE_MEMBER', 9: 'TAB_MUTE_MEMBER', 10: 'TAB_MEMBER_INFO'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SceneNodeNodeType(enum):
    Connect: int = 1
    Follow: int = 2
    Independent: int = 0
    name_to_values: dict = {'Independent': 0, 'Connect': 1, 'Follow': 2}
    value_to_names: dict = {0: 'Independent', 1: 'Connect', 2: 'Follow'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SceneNodeTransType(enum):
    Entity: int = 0
    World: int = 1
    name_to_values: dict = {'Entity': 0, 'World': 1}
    value_to_names: dict = {0: 'Entity', 1: 'World'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SelfDefinePcKeyTag(enum):
    ReplayRoomGod_Backward: int = 2
    ReplayRoomGod_Down: int = 6
    ReplayRoomGod_Forward: int = 1
    ReplayRoomGod_Left: int = 3
    ReplayRoomGod_ObserverSetting: int = 9
    ReplayRoomGod_Right: int = 4
    ReplayRoomGod_Setting: int = 7
    ReplayRoomGod_TeamList: int = 8
    ReplayRoomGod_Up: int = 5
    ReplayRoomSetting_CameraSwitch: int = 20
    ReplayRoomSetting_FreeCameraOp: int = 27
    ReplayRoomSetting_FreeCameraSpeedDown: int = 29
    ReplayRoomSetting_FreeCameraSpeedUp: int = 28
    ReplayRoomSetting_KillKing: int = 21
    ReplayRoomSetting_Nearest: int = 22
    ReplayRoomSetting_NearestFiring: int = 23
    ReplayRoomSetting_ShowWeaponInfo: int = 26
    ReplayRoomSetting_Toplogo: int = 25
    ReplayRoomSetting_Xray: int = 24
    name_to_values: dict = {'ReplayRoomGod_Forward': 1, 'ReplayRoomGod_Backward': 2, 'ReplayRoomGod_Left': 3, 'ReplayRoomGod_Right': 4, 'ReplayRoomGod_Up': 5, 'ReplayRoomGod_Down': 6, 'ReplayRoomGod_Setting': 7, 'ReplayRoomGod_TeamList': 8, 'ReplayRoomGod_ObserverSetting': 9, 'ReplayRoomSetting_CameraSwitch': 20, 'ReplayRoomSetting_KillKing': 21, 'ReplayRoomSetting_Nearest': 22, 'ReplayRoomSetting_NearestFiring': 23, 'ReplayRoomSetting_Xray': 24, 'ReplayRoomSetting_Toplogo': 25, 'ReplayRoomSetting_ShowWeaponInfo': 26, 'ReplayRoomSetting_FreeCameraOp': 27, 'ReplayRoomSetting_FreeCameraSpeedUp': 28, 'ReplayRoomSetting_FreeCameraSpeedDown': 29}
    value_to_names: dict = {1: 'ReplayRoomGod_Forward', 2: 'ReplayRoomGod_Backward', 3: 'ReplayRoomGod_Left', 4: 'ReplayRoomGod_Right', 5: 'ReplayRoomGod_Up', 6: 'ReplayRoomGod_Down', 7: 'ReplayRoomGod_Setting', 8: 'ReplayRoomGod_TeamList', 9: 'ReplayRoomGod_ObserverSetting', 20: 'ReplayRoomSetting_CameraSwitch', 21: 'ReplayRoomSetting_KillKing', 22: 'ReplayRoomSetting_Nearest', 23: 'ReplayRoomSetting_NearestFiring', 24: 'ReplayRoomSetting_Xray', 25: 'ReplayRoomSetting_Toplogo', 26: 'ReplayRoomSetting_ShowWeaponInfo', 27: 'ReplayRoomSetting_FreeCameraOp', 28: 'ReplayRoomSetting_FreeCameraSpeedUp', 29: 'ReplayRoomSetting_FreeCameraSpeedDown'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SensiSwitchMode(enum):
    ADS_B: int = 1
    ADS_E: int = 2
    ADS_M: int = 3
    name_to_values: dict = {'ADS_B': 1, 'ADS_E': 2, 'ADS_M': 3}
    value_to_names: dict = {1: 'ADS_B', 2: 'ADS_E', 3: 'ADS_M'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ServerState(object):
    Busy: int = 3
    Free: int = 1
    Full: int = 4
    Normal: int = 2
    Stop: int = 5

class ShootingRangeMainUIStyle(enum):
    Version_1: int = 1
    Version_2: int = 2
    name_to_values: dict = {'Version_1': 1, 'Version_2': 2}
    value_to_names: dict = {1: 'Version_1', 2: 'Version_2'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SigninState(enum):
    REISSUE: int = 2
    SIGNED: int = 1
    TIME_UNREACH: int = 4
    UNSIGNIN: int = 3
    name_to_values: dict = {'SIGNED': 1, 'REISSUE': 2, 'UNSIGNIN': 3, 'TIME_UNREACH': 4}
    value_to_names: dict = {1: 'SIGNED', 2: 'REISSUE', 3: 'UNSIGNIN', 4: 'TIME_UNREACH'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SingleShotGunFireMode(enum):
    OneShot: int = 1
    RunningShot: int = 2
    name_to_values: dict = {'OneShot': 1, 'RunningShot': 2}
    value_to_names: dict = {1: 'OneShot', 2: 'RunningShot'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SlotsEnum(object):
class SoundNoticeMode(enum):
    HUD: int = 2
    MINIMAP: int = 1
    name_to_values: dict = {'MINIMAP': 1, 'HUD': 2}
    value_to_names: dict = {1: 'MINIMAP', 2: 'HUD'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SpaceGlobalInfo(enum):
    AdRecord: int = 3
    MobaDeathRebornTips: int = 4
    MovingPlatform: int = 2
    name_to_values: dict = {'MovingPlatform': 2, 'AdRecord': 3, 'MobaDeathRebornTips': 4}
    value_to_names: dict = {2: 'MovingPlatform', 3: 'AdRecord', 4: 'MobaDeathRebornTips'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class StateRelationship(enum):
    BeExecuted: int = 50
    ChargeJump: int = 63
    ChargeJumpAir: int = 66
    Climb: int = 10
    ClimbLadder: int = 32
    CommonTpsSkill: int = 67
    Cross: int = 23
    Crouch: int = 6
    DriveVehicle: int = 33
    DropWeapon: int = 21
    DualFire: int = 57
    DualGun: int = 52
    DualReload: int = 54
    DualReloadEnd: int = 56
    DualReloading: int = 55
    Emote: int = 51
    EnterAds: int = 19
    EnterProne: int = 27
    Execution: int = 49
    ExitProne: int = 28
    Fire: int = 12
    GunInspection: int = 44
    GunRefit: int = 30
    HighFall: int = 45
    Idle: int = 1
    Inspirator: int = 46
    Item: int = 16
    Jog: int = 3
    Jump: int = 8
    KickUp: int = 65
    KnockDown: int = 11
    LeanOutVehicle: int = 34
    LeftShield: int = 64
    LeftXDroid: int = 62
    Medicine: int = 60
    Melee: int = 29
    MeleeAttack: int = 39
    MovingShield: int = 31
    OnVehicle: int = 7
    PickUp: int = 18
    PortableEquipment: int = 53
    Prone: int = 26
    RaiseLeftHandWeapon: int = 25
    RaiseWeapon: int = 20
    Rechamber: int = 22
    Reload: int = 13
    ReloadEnd: int = 43
    Reloading: int = 42
    RescueOther: int = 35
    SamuraiBlock: int = 58
    SamuraiSprint: int = 59
    ScanCore: int = 36
    Skill: int = 24
    SkillCantAir: int = 48
    SkillCantProne: int = 41
    SkillWeaponDrop: int = 38
    SkillWeaponRaise: int = 37
    Slide: int = 9
    Sprint: int = 4
    Strop: int = 17
    SuperSprint: int = 5
    Swim: int = 47
    ThrowableWeaponLeft: int = 15
    ThrowableWeaponRight: int = 14
    TripleShot: int = 61
    Walk: int = 2
    Xdroid: int = 40
    name_to_values: dict = {'Idle': 1, 'Walk': 2, 'Jog': 3, 'Sprint': 4, 'SuperSprint': 5, 'Crouch': 6, 'OnVehicle': 7, 'Jump': 8, 'Slide': 9, 'Climb': 10, 'KnockDown': 11, 'Fire': 12, 'Reload': 13, 'ThrowableWeaponRight': 14, 'ThrowableWeaponLeft': 15, 'Item': 16, 'Strop': 17, 'PickUp': 18, 'EnterAds': 19, 'RaiseWeapon': 20, 'DropWeapon': 21, 'Rechamber': 22, 'Cross': 23, 'Skill': 24, 'RaiseLeftHandWeapon': 25, 'Prone': 26, 'EnterProne': 27, 'ExitProne': 28, 'Melee': 29, 'GunRefit': 30, 'MovingShield': 31, 'ClimbLadder': 32, 'DriveVehicle': 33, 'LeanOutVehicle': 34, 'RescueOther': 35, 'ScanCore': 36, 'SkillWeaponRaise': 37, 'SkillWeaponDrop': 38, 'MeleeAttack': 39, 'Xdroid': 40, 'SkillCantProne': 41, 'Reloading': 42, 'ReloadEnd': 43, 'GunInspection': 44, 'HighFall': 45, 'Inspirator': 46, 'Swim': 47, 'SkillCantAir': 48, 'Execution': 49, 'BeExecuted': 50, 'Emote': 51, 'DualGun': 52, 'PortableEquipment': 53, 'DualReload': 54, 'DualReloading': 55, 'DualReloadEnd': 56, 'DualFire': 57, 'SamuraiBlock': 58, 'SamuraiSprint': 59, 'Medicine': 60, 'TripleShot': 61, 'LeftXDroid': 62, 'ChargeJump': 63, 'LeftShield': 64, 'KickUp': 65, 'ChargeJumpAir': 66, 'CommonTpsSkill': 67}
    value_to_names: dict = {1: 'Idle', 2: 'Walk', 3: 'Jog', 4: 'Sprint', 5: 'SuperSprint', 6: 'Crouch', 7: 'OnVehicle', 8: 'Jump', 9: 'Slide', 10: 'Climb', 11: 'KnockDown', 12: 'Fire', 13: 'Reload', 14: 'ThrowableWeaponRight', 15: 'ThrowableWeaponLeft', 16: 'Item', 17: 'Strop', 18: 'PickUp', 19: 'EnterAds', 20: 'RaiseWeapon', 21: 'DropWeapon', 22: 'Rechamber', 23: 'Cross', 24: 'Skill', 25: 'RaiseLeftHandWeapon', 26: 'Prone', 27: 'EnterProne', 28: 'ExitProne', 29: 'Melee', 30: 'GunRefit', 31: 'MovingShield', 32: 'ClimbLadder', 33: 'DriveVehicle', 34: 'LeanOutVehicle', 35: 'RescueOther', 36: 'ScanCore', 37: 'SkillWeaponRaise', 38: 'SkillWeaponDrop', 39: 'MeleeAttack', 40: 'Xdroid', 41: 'SkillCantProne', 42: 'Reloading', 43: 'ReloadEnd', 44: 'GunInspection', 45: 'HighFall', 46: 'Inspirator', 47: 'Swim', 48: 'SkillCantAir', 49: 'Execution', 50: 'BeExecuted', 51: 'Emote', 52: 'DualGun', 53: 'PortableEquipment', 54: 'DualReload', 55: 'DualReloading', 56: 'DualReloadEnd', 57: 'DualFire', 58: 'SamuraiBlock', 59: 'SamuraiSprint', 60: 'Medicine', 61: 'TripleShot', 62: 'LeftXDroid', 63: 'ChargeJump', 64: 'LeftShield', 65: 'KickUp', 66: 'ChargeJumpAir', 67: 'CommonTpsSkill'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class StateRelationshipResult(enum):
    Break: int = 1
    Cancel: int = 2
    Coexist: int = 3
    name_to_values: dict = {'Break': 1, 'Cancel': 2, 'Coexist': 3}
    value_to_names: dict = {1: 'Break', 2: 'Cancel', 3: 'Coexist'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class TeamInfoState(enum):
    Dead: int = 2
    Driving: int = 6
    KnockDown: int = 3
    Normal: int = 30
    Offline: int = 1
    OnAircraft: int = 4
    OnVehicle: int = 7
    Parachute: int = 5
    name_to_values: dict = {'Offline': 1, 'Dead': 2, 'KnockDown': 3, 'OnAircraft': 4, 'Parachute': 5, 'Driving': 6, 'OnVehicle': 7, 'Normal': 30}
    value_to_names: dict = {1: 'Offline', 2: 'Dead', 3: 'KnockDown', 4: 'OnAircraft', 5: 'Parachute', 6: 'Driving', 7: 'OnVehicle', 30: 'Normal'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class TeammateColor(enum):
    Blue: int = 3
    CYAN: int = 5
    Green: int = 2
    Purple: int = 4
    Yellow: int = 1
    name_to_values: dict = {'Yellow': 1, 'Green': 2, 'Blue': 3, 'Purple': 4, 'CYAN': 5}
    value_to_names: dict = {1: 'Yellow', 2: 'Green', 3: 'Blue', 4: 'Purple', 5: 'CYAN'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class TechState(enum):
    TechState_Burnt: int = 4
    TechState_DistanceEnemy: int = 20
    TechState_Edgeline: int = 9
    TechState_Frozen: int = 3
    TechState_HighLightXray: int = 21
    TechState_Highlight: int = 5
    TechState_Normal: int = 0
    TechState_Xray: int = 6
    name_to_values: dict = {'TechState_Normal': 0, 'TechState_Frozen': 3, 'TechState_Burnt': 4, 'TechState_Highlight': 5, 'TechState_Xray': 6, 'TechState_Edgeline': 9, 'TechState_DistanceEnemy': 20, 'TechState_HighLightXray': 21}
    value_to_names: dict = {0: 'TechState_Normal', 3: 'TechState_Frozen', 4: 'TechState_Burnt', 5: 'TechState_Highlight', 6: 'TechState_Xray', 9: 'TechState_Edgeline', 20: 'TechState_DistanceEnemy', 21: 'TechState_HighLightXray'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ThrowExpandDir(enum):
    Right: int = 1
    UP: int = 0
    name_to_values: dict = {'UP': 0, 'Right': 1}
    value_to_names: dict = {0: 'UP', 1: 'Right'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class TriggerAdsMode(enum):
    DCLICK: int = 4
    HOLDING: int = 2
    MIXING: int = 3
    SCLICK: int = 1
    name_to_values: dict = {'SCLICK': 1, 'HOLDING': 2, 'MIXING': 3, 'DCLICK': 4}
    value_to_names: dict = {1: 'SCLICK', 2: 'HOLDING', 3: 'MIXING', 4: 'DCLICK'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class TurnMode(enum):
    DISTANCE: int = 2
    FIX: int = 1
    SPEED: int = 3
    name_to_values: dict = {'FIX': 1, 'DISTANCE': 2, 'SPEED': 3}
    value_to_names: dict = {1: 'FIX', 2: 'DISTANCE', 3: 'SPEED'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class UIVersion(enum):
    Version_1: int = 1
    Version_2: int = 2
    name_to_values: dict = {'Version_1': 1, 'Version_2': 2}
    value_to_names: dict = {1: 'Version_1', 2: 'Version_2'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class UseItemMode(enum):
    ATTACK_DOWN: int = 3
    ATTACK_UP: int = 4
    BACKPACK: int = 7
    CANCEL_DOWN: int = 5
    CANCEL_UP: int = 6
    ITEM_DOWN: int = 1
    ITEM_UP: int = 2
    SECOND_SPELL_CANCEL_DOWN: int = 10
    SECOND_SPELL_CANCEL_UP: int = 11
    SECOND_SPELL_DOWN: int = 8
    SECOND_SPELL_UP: int = 9
    name_to_values: dict = {'ITEM_DOWN': 1, 'ITEM_UP': 2, 'ATTACK_DOWN': 3, 'ATTACK_UP': 4, 'CANCEL_DOWN': 5, 'CANCEL_UP': 6, 'BACKPACK': 7, 'SECOND_SPELL_DOWN': 8, 'SECOND_SPELL_UP': 9, 'SECOND_SPELL_CANCEL_DOWN': 10, 'SECOND_SPELL_CANCEL_UP': 11}
    value_to_names: dict = {1: 'ITEM_DOWN', 2: 'ITEM_UP', 3: 'ATTACK_DOWN', 4: 'ATTACK_UP', 5: 'CANCEL_DOWN', 6: 'CANCEL_UP', 7: 'BACKPACK', 8: 'SECOND_SPELL_DOWN', 9: 'SECOND_SPELL_UP', 10: 'SECOND_SPELL_CANCEL_DOWN', 11: 'SECOND_SPELL_CANCEL_UP'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class WindowDlcType(enum):
    CLAN: int = 4
    GACHA: int = 27
    MALL: NoneType = None
    RANK: int = 30
    name_to_values: dict = {'CLAN': 4, 'MALL': None, 'GACHA': 27, 'RANK': 30}
    value_to_names: dict = {4: 'CLAN', None: 'MALL', 27: 'GACHA', 30: 'RANK'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class WorldFieldType(enum):
    Gas: int = 1
    name_to_values: dict = {'Gas': 1}
    value_to_names: dict = {1: 'Gas'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class enum(object):
    name_to_values: dict = {}
    value_to_names: dict = {}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...


def DecodeRankWindowKey(rank_window_key): ...
def EncodeRankWindowKey(rank_tab, rank_key): ...
def FindLowestBit1(bit_number): ...
def GetFallActionByRollPitchParachute(pitch, roll): ...
def GetFallActionByXYFreeFall(x, y): ...
def warehouse_quality_color2str(quality): ...


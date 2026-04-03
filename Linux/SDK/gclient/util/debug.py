# module: gclient.util.debug

import Timer
import cconst
import logging
import six2
import sys

_logger: NoneType = None
flush_timer: NoneType = None
origin_print: NoneType = None

class LogManager(object):
    asyncwrite: bool = False
    created_modules: set = {'CombatAvatarSquadFight', 'GameLogicRookieGuide', 'ReplayGameLogicSniperMode', 'RobotCombatAvatarNowhere', 'BaitBombField', 'ClientAreaEntity', 'ReplayCombatAvatarSniperMode', 'CombatTeamEntity_SquadFight', 'AttachScoutArrowEntity', 'bhttp_client.BHttpClient', 'AdsShield', 'BaseSupply', 'CombatAvatarMobaZombie', 'IceWallField', 'ClientSpace', 'CombatTeamEntity_BigHead', 'PlayerCombatAvatarPlacement', 'ControlTargetBase', 'RepelBomb', 'Formula', 'GameLogicNowhere', 'ReplayRoomGameLogicSquadFight', 'VehicleCannon', 'HumanoidMonsterMonsterAI', 'ReconDrone', 'CombatAvatar', 'RobotCombatAvatarMoba', 'PlayerCombatAvatarSniperMode', 'CombatAvatarMobaFirst', 'PlayerCombatAvatarHotSpotBase', 'EnergyStronghold', 'Bomb', 'Preload', 'GameLogicBigHead', 'GrenadeLauncherBomb', 'LeadWayEntity', 'ReplayCombatAvatarShootingRange', 'GameLogicGrandTheft', 'ReplayGameLogicMobaZombie', 'PlayerCombatAvatarSquadFightBase', 'Shop', 'MovingPlatformTelpher', 'ClientEntity', 'HelenRobotCombatAvatarMoba', 'SuicideDrone', 'ThermiteBomb', 'PhyBall', 'ReplayCombatAvatarMoba', 'FireWallField', 'RobotCombatAvatarRookieGuideNew', 'PlayerCombatAvatarRookieGuideNew', 'ReplayCombatAvatarSquadFight', 'ReplayDummy', 'TrackBomb', 'AmmoBox', 'CombatAvatarPlacement', 'Supply', 'asynctimer', 'PlayerAvatar', 'ServerUtil', 'PlayerCombatAvatar', 'RobotCombatAvatarShootingRange', 'StropEntity', 'CombatAvatarBigHead', 'CureUav', 'HelenRobotCombatAvatarNoWhere', 'SearchContractBox', 'RobotCombatAvatarMobaZombieAi', 'InteractionEntity', 'NewCrystalMonster', 'CombatTeamEntity_Moba', 'SaveMachine', 'ReplayCombatAvatarMobaZombie', 'NavigateCannon', 'ATM', 'RobotCombatAvatarBigHead', 'SatellitePlaceItem', 'Arrow', 'RestrictWall', 'WaterSnare', 'CDrone', 'Vehicle', 'MonsterCommon', 'OccupyContractTarget', 'ScoutField', 'Helicopter', 'HolographicRobotMoba', 'ReplayGameLogicPlacement', 'TrackTrapBomb', 'HolographicRobot', 'CombatAvatarShootingRange', 'ReplayGameLogicGrandTheft', 'Pubsub', 'Space', 'ReplayGameLogicNowhere', 'CombatAvatarMobaFirstNew', 'GameLogicRookieGuideNew', 'CombatAvatarGrandTheft', 'PlayerCombatAvatarMobaZombie', 'Account', 'PlayerCombatAvatarNowhere', 'ValDrone', 'CombatAvatarHotSpot', 'DeathBoxDummyEntity', 'CombatAvatarGunFight', 'CrystalMonster', 'Airdrop', 'ReplayRoomGameLogicMoba', 'RobotCombatAvatarMobaFirstNew', 'GateClient', 'MoveFireWall', 'Oilbox', 'ScoutTotemField', 'NewMonsterCommon', 'RPGMissile', 'SafeBox', 'RobotCombatAvatarATMGuard', 'RobotCombatAvatarMobaZombie', 'PlayerCombatAvatarClientOffline', 'ReplayCombatAvatar', 'PlayerEntity', 'ChaosUAV', 'SyncTransEntity', 'ReplayCombatAvatarGunFight', 'BigHeadCalculationDoll', 'DestructibleCollections', 'ScoutArrow', 'GameLogicSquadFight', 'MovingShield', 'CombatAvatarHotSpotBase', 'FreeviewDummyEntity', 'RobotCombatAvatarSniperMode', 'GameLogicPlacement', 'RobotCombatAvatarGrandTheft', 'CombatAvatarSquadFightBase', 'ActivityItem', 'ReplayRoomGameLogicBase', 'Missile', 'MonsterAI', 'CalculationDoll', 'MonitorMissile', 'AsioServerProxy', 'PlayerCombatAvatarHotSpot', 'Stronghold', 'GameLogicShootingRange', 'PlayerCombatAvatarGrandTheft', 'CombatAvatarGunFightBase', 'KcpClient', 'RobotCombatAvatarSquadFight', 'ReplayRoomGameLogicBigHead', 'ClientEnv', 'CombatTeamEntity_GunFight', 'ReplayCombatAvatarMobaFirstNew', 'ThroughBomb', 'ReplayCombatAvatarHotSpot', 'GameLogicMobaZombie', 'GameLogicGunFight', 'Building', 'mobilerpc.SimpleAsyncBHTTPClient', 'DummyCombatAvatar', 'ReplayGameLogicGunFight', 'ReplayCombatAvatarNowhere', 'ExplodingArrowEntity', 'RobotCombatAvatarHotSpot', 'NinjaBeacon', 'ReplayCombatAvatarGrandTheft', 'BarrieCannon', 'ReplayRoomGameLogicMobaZombie', 'CombatTeamEntity_ShootingRange', 'ReplayGameLogicMobaFirst', 'TrackBomb2025', 'PlayerCombatAvatarGunFightBase', 'CombatItemEntity', 'GameLogicMoba', 'CombatAvatarMoba', 'PlayerCombatAvatarShootingRange', 'RobotCombatAvatarRookieGuide', 'GameLogicClientOffline', 'PlayerCombatAvatarRookieGuide', 'CombatAvatarRookieGuideNew', 'Crow', 'Entity', 'MagicField', 'PlayerCombatAvatarSquadFight', 'AircraftPlane', 'Model', 'RpcIndexer', 'SpaceSnare', 'PlayerCombatAvatarMoba', 'PlaceEntity', 'SaveDrone', 'ReplayGameLogicHotSpot', 'PlayerCombatAvatarBigHeadBase', 'AvatarEntity', 'PortableShop', 'ReplayGameLogicShootingRange', 'CommonMoveItem', 'ShockField', 'ClueBox', 'VehicleAirplane', 'CombatTeamEntity_GrandTheft', 'AsioGateClient', 'FollowShieldMagicField', 'BigHeadMostKillDummyEntity', 'ReplayGameLogicBase', 'SamuraiBlockField', 'ReplayGameLogicMoba', 'CombatTeamEntity_Nowhere', 'ModelCache', 'CombatAvatarBigHeadBase', 'CombatTeamEntity_SniperMode', 'ReplayCombatAvatarMobaFirst', 'PlayerCombatAvatarMobaFirst', 'CombatTeamEntity', 'GameLogicMobaFirstNew', 'ATMGuardMonster', 'RobotCombatAvatarMobaFirst', 'SaveDroneDummyEntity', 'CombatTeamEntity_HotSpot', 'Telnet', 'GameLogicSniperMode', 'OccupyContractTargetNew', 'CombatTeamEntity_MobaZombie', 'ItemSpaceSnare', 'GameLogicBase', 'EmoteTree', 'ReplayCombatAvatarBigHead', 'CombatAvatarRookieGuide', 'ReplayRoomGameLogicSniperMode', 'CombatAvatarSniperMode', 'AttackDrone', 'StickyObjectEntity', 'ReplayGameLogicBigHead', 'SwordSpirit', 'ReplayGameLogicSquadFight', 'PlayerCombatAvatarMobaFirstNew', 'TotemField', 'PlayerCombatAvatarGunFight', 'CureUavFix', 'Doll', 'Crack', 'BlastBomb', 'ClusterBomb', 'HolographicRobotNowhere', 'GameLogicHotSpot', 'RobotCombatAvatarGunFight', 'DollLike', 'CombatAvatarNowhere', 'ReplayRoomGameLogicGunFight', 'HolographicHitTargetDummyEntity', 'server.EntityManager', 'StropUAV', 'CombatAvatarClientOffline', 'PlayerCombatAvatarBigHead', 'FollowerInteractionEntity', 'CommonItem', 'server.EntityFactory', 'ReplayGameLogicMobaFirstNew', 'GameLogicMobaFirst', 'Avatar'}
    custom_handler: NoneType = None
    log_handle: str = 'stream'
    log_level: int = 10
    log_tag: str = ''
    run_tag: str = ''
    sa_log_tag: str = ''
    sys_logger: NoneType = None

    def _create_handler(logger): ...
    def get_logger(moduleName): ...
    def get_sa_logger(): ...
    def run_message(message): ...
    def set_asyncwrite(asyncwrite): ...
    def set_custom_handler(handler): ...
    def set_log_handle(handle): ...
    def set_log_level(lv): ...
    def set_log_tag(log_tag): ...
    def set_run_tag(run_tag): ...
    def set_sa_log_tag(tag): ...

class OperEnum(object):
    NT_BACKUP_D: int = 43
    NT_BACKUP_F: int = 40
    NT_BACKUP_I: int = 39
    NT_BACKUP_L: int = 42
    NT_BACKUP_S: int = 41
    NT_D_CLEAR: int = 3
    NT_D_CREATE_D: int = 2
    NT_D_CREATE_L: int = 1
    NT_D_REMOVE: int = 4
    NT_D_UPDATE: int = 5
    NT_D_UPDATE_D: int = 10
    NT_D_UPDATE_DL: int = 50
    NT_D_UPDATE_F: int = 7
    NT_D_UPDATE_I: int = 6
    NT_D_UPDATE_L: int = 9
    NT_D_UPDATE_LL: int = 51
    NT_D_UPDATE_S: int = 8
    NT_D_UPDATE_UD: int = 11
    NT_END: int = 54
    NT_INNER_D: int = 38
    NT_INNER_F: int = 35
    NT_INNER_I: int = 34
    NT_INNER_L: int = 37
    NT_INNER_S: int = 36
    NT_L_APPEND: int = 19
    NT_L_APPEND_D: int = 24
    NT_L_APPEND_F: int = 21
    NT_L_APPEND_I: int = 20
    NT_L_APPEND_L: int = 23
    NT_L_APPEND_S: int = 22
    NT_L_ASSIGN: int = 27
    NT_L_CLEAR: int = 12
    NT_L_EXTEND: int = 26
    NT_L_INSERT: int = 13
    NT_L_INSERT_D: int = 18
    NT_L_INSERT_F: int = 15
    NT_L_INSERT_I: int = 14
    NT_L_INSERT_L: int = 17
    NT_L_INSERT_S: int = 16
    NT_L_POP: int = 25
    NT_L_UPDATE: int = 28
    NT_L_UPDATE_D: int = 33
    NT_L_UPDATE_DL: int = 52
    NT_L_UPDATE_F: int = 30
    NT_L_UPDATE_I: int = 29
    NT_L_UPDATE_L: int = 32
    NT_L_UPDATE_LL: int = 53
    NT_L_UPDATE_S: int = 31
    NT_MSG_D: int = 45
    NT_MSG_L: int = 44
    NT_MSG_MAIL_B: int = 46
    NT_MSG_MAIL_C: int = 47
    NT_NONE: int = 0
    NT_RPC: int = 48
    NT_RPCR: int = 49
    from_string: builtin_function_or_method = <built-in method __getitem__ of dict object at 0x7005fe12c0>
    to_string: builtin_function_or_method = <built-in method __getitem__ of dict object at 0x7005fe28c0>


def ReplacePrintFunc(): ...
def RestoreOriginPrintFunc(): ...
def TestFetchServerList(domain, host, port, url_name, use_httpdns, callback): ...
def TestPing(server, group): ...
def enum(*sequential, **named): ...


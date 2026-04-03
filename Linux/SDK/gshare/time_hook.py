# module: gshare.time_hook

import datetime
import time

_OFFSET: float = 0.0
_datetime: NoneType = None
_time_gmtime: NoneType = None
_time_localtime: NoneType = None
_time_strftime: NoneType = None
_time_time: NoneType = None
logger: Logger = <Logger ServerUtil (DEBUG)>

class Crontab(object):
    TRIGGER_OFFSET: float = 5.1

    def _checkCrontabs(self): ...
    def _resetMinuteTimer(self): ...
    def init(self): ...
    def register(self, rule, callback): ...
    def resetTimer(self): ...
    def setup_frame_skipping_callback(self, callback): ...
    def stop(self): ...
    def unregister(self, rowid): ...

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

class datetime2(datetime):
    astimezone: method_descriptor = <method 'astimezone' of 'datetime.datetime' objects>
    combine: builtin_function_or_method = <built-in method combine of type object at 0x6f9d06f810>
    ctime: method_descriptor = <method 'ctime' of 'datetime.datetime' objects>
    date: method_descriptor = <method 'date' of 'datetime.datetime' objects>
    day: getset_descriptor = <attribute 'day' of 'datetime.date' objects>
    dst: method_descriptor = <method 'dst' of 'datetime.datetime' objects>
    fold: getset_descriptor = <attribute 'fold' of 'datetime.datetime' objects>
    fromisocalendar: builtin_function_or_method = <built-in method fromisocalendar of type object at 0x6f9d06f810>
    fromisoformat: builtin_function_or_method = <built-in method fromisoformat of type object at 0x6f9d06f810>
    fromordinal: builtin_function_or_method = <built-in method fromordinal of type object at 0x6f9d06f810>
    fromtimestamp: builtin_function_or_method = <built-in method fromtimestamp of type object at 0x6f9d06f810>
    hour: getset_descriptor = <attribute 'hour' of 'datetime.datetime' objects>
    isocalendar: method_descriptor = <method 'isocalendar' of 'datetime.date' objects>
    isoformat: method_descriptor = <method 'isoformat' of 'datetime.datetime' objects>
    isoweekday: method_descriptor = <method 'isoweekday' of 'datetime.date' objects>
    max: datetime = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
    microsecond: getset_descriptor = <attribute 'microsecond' of 'datetime.datetime' objects>
    min: datetime = datetime.datetime(1, 1, 1, 0, 0)
    minute: getset_descriptor = <attribute 'minute' of 'datetime.datetime' objects>
    month: getset_descriptor = <attribute 'month' of 'datetime.date' objects>
    replace: method_descriptor = <method 'replace' of 'datetime.datetime' objects>
    resolution: timedelta = datetime.timedelta(microseconds=1)
    second: getset_descriptor = <attribute 'second' of 'datetime.datetime' objects>
    strftime: method_descriptor = <method 'strftime' of 'datetime.date' objects>
    strptime: builtin_function_or_method = <built-in method strptime of type object at 0x6f9d06f810>
    time: method_descriptor = <method 'time' of 'datetime.datetime' objects>
    timestamp: method_descriptor = <method 'timestamp' of 'datetime.datetime' objects>
    timetuple: method_descriptor = <method 'timetuple' of 'datetime.datetime' objects>
    timetz: method_descriptor = <method 'timetz' of 'datetime.datetime' objects>
    toordinal: method_descriptor = <method 'toordinal' of 'datetime.date' objects>
    tzinfo: getset_descriptor = <attribute 'tzinfo' of 'datetime.datetime' objects>
    tzname: method_descriptor = <method 'tzname' of 'datetime.datetime' objects>
    utcfromtimestamp: builtin_function_or_method = <built-in method utcfromtimestamp of type object at 0x6f9d06f810>
    utcnow: builtin_function_or_method = <built-in method utcnow of type object at 0x6f9d06f810>
    utcoffset: method_descriptor = <method 'utcoffset' of 'datetime.datetime' objects>
    utctimetuple: method_descriptor = <method 'utctimetuple' of 'datetime.datetime' objects>
    weekday: method_descriptor = <method 'weekday' of 'datetime.date' objects>
    year: getset_descriptor = <attribute 'year' of 'datetime.date' objects>

    def now(*args): ...
    def today(*args): ...


def DoHookTime(offset): ...
def HookTime(offset): ...
def SetTime(year, mon, mday, hour=0, min=0, sec=0, ms=0): ...
def _gmtime(sec=0): ...
def _localtime(sec=None): ...
def _strftime(formats, tp=None): ...
def _time(): ...


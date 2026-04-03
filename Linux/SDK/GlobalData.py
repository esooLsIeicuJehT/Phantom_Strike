# module: GlobalData

EngineArgs: list = ['']
GameState: int = 0
IWorldVersion: int = 0
IsCharEditor: bool = False
IsCollectGunSkinPerformanceRobot: bool = False
IsCollectRaiseWeaponTime: bool = False
IsExportPhysics: bool = False
IsGeneratePivotData: bool = False
IsHelenSunshineEditor: bool = False
IsJarvisClient: bool = False
IsNewPC: bool = False
IsOfflineSceneEditorGame: bool = False
IsOnlineCharEditor: bool = False
IsProfileCollectionRobot: bool = False
IsSceneEditor: bool = False
IsSceneEditorGame: bool = False
IsSceneGame: bool = False
IsShaderCacheMissAnalyseRobot: bool = False
IsShaderCollectionRobot: bool = False
IsShaderPrecompileListRobot: bool = False
IsSkeletonEditor: bool = False
IsSunshineEditor: bool = False
IsUGC: bool = False
Offline: bool = False
PlaceEditorMode: int = 0
PlaceEditorPos: tuple = (0, 0, 0)
TelnetConsole: GameServerConsole = <common.GameServerConsole.GameServerConsole object at 0x70b17d4680>
camera: NoneType = None
m: NoneType = None
p: NoneType = None

def IsEditor(): ...
def IsRobot(): ...


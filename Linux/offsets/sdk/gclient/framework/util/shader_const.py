# module: gclient.framework.util.shader_const

import cconst
import six2

EShaderProfile_last: int = 45
PBR_FACE_SHADER_NAME: str = 'e761ea15-65b9-49af-b33d-4a888cf33c19'
PBR_GUN_ADVANCED_SKIN_SHADER_NAME: str = '4d88ee22-6e5e-4d52-b1e1-f171ca912f4d'
PBR_GUN_CHANGE_COLOR_SHADER_NAME: str = '5efcd177-e941-487d-bc74-1c56f46c71e4'
PBR_GUN_LIKE_SHADER_NAMES: set = {'4d88ee22-6e5e-4d52-b1e1-f171ca912f4d', 'cf8293a1-5681-4d91-8757-b82ae9957f94', '5efcd177-e941-487d-bc74-1c56f46c71e4'}
PBR_GUN_SHADER_NAME: str = 'cf8293a1-5681-4d91-8757-b82ae9957f94'
PBR_SCENE_SHADER_NAME: str = 'c2ad3450-e8c8-427a-a0de-be918e6d9515'
PBR_SHADER_NAME: str = '75f04182-8961-43ba-a39b-f213477099fb'
SG_SCOPE_SHADER_NAME: str = 'e477e0c5-dee0-4381-ad92-253b25906c14'
TextureSwitches: dict = {'tOverlayMap': ('EnableOverlayMap',), 'tOverlayNormal': ('EnableOverlayNormal',)}

class PbrGunAdvancedSkinShaderMacros(enum):
    AnisotropicEnable: int = 45
    EnableEmiMap2: int = 46
    EnableEmissive3UV: int = 47
    EnableEmissiveNoisemap: int = 48
    EnableFlowmap: int = 49
    EnableIBL: int = 50
    EnableMatcap: int = 51
    EnableMixmap: int = 52
    EnableOverlay: int = 53
    EnableOverlayMap: int = 54
    EnableOverlayMatChange: int = 55
    EnableOverlayNormal: int = 56
    EnableRazermap: int = 57
    EnableReflection: int = 58
    EnableScreenUV: int = 59
    LightMapEnable: int = 60
    LightmapConstEnable: int = 61
    name_to_values: dict = {'AnisotropicEnable': 45, 'EnableEmiMap2': 46, 'EnableEmissive3UV': 47, 'EnableEmissiveNoisemap': 48, 'EnableFlowmap': 49, 'EnableIBL': 50, 'EnableMatcap': 51, 'EnableMixmap': 52, 'EnableOverlay': 53, 'EnableOverlayMap': 54, 'EnableOverlayMatChange': 55, 'EnableOverlayNormal': 56, 'EnableRazermap': 57, 'EnableReflection': 58, 'EnableScreenUV': 59, 'LightMapEnable': 60, 'LightmapConstEnable': 61}
    value_to_names: dict = {45: 'AnisotropicEnable', 46: 'EnableEmiMap2', 47: 'EnableEmissive3UV', 48: 'EnableEmissiveNoisemap', 49: 'EnableFlowmap', 50: 'EnableIBL', 51: 'EnableMatcap', 52: 'EnableMixmap', 53: 'EnableOverlay', 54: 'EnableOverlayMap', 55: 'EnableOverlayMatChange', 56: 'EnableOverlayNormal', 57: 'EnableRazermap', 58: 'EnableReflection', 59: 'EnableScreenUV', 60: 'LightMapEnable', 61: 'LightmapConstEnable'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PbrGunChangeColorShaderMacros(enum):
    AnisotropicEnable: int = 45
    EnableAnimeMap: int = 46
    EnableChangeMap: int = 47
    EnableEmissive: int = 48
    EnableEmissive3UV: int = 49
    EnableIBL: int = 50
    EnableMixmap: int = 51
    EnableOverlay: int = 52
    EnableOverlayMap: int = 53
    EnableOverlayMatChange: int = 54
    EnableOverlayNormal: int = 55
    EnableRazermap: int = 56
    EnableReflection: int = 57
    LightMapEnable: int = 58
    LightmapConstEnable: int = 59
    name_to_values: dict = {'AnisotropicEnable': 45, 'EnableAnimeMap': 46, 'EnableChangeMap': 47, 'EnableEmissive': 48, 'EnableEmissive3UV': 49, 'EnableIBL': 50, 'EnableMixmap': 51, 'EnableOverlay': 52, 'EnableOverlayMap': 53, 'EnableOverlayMatChange': 54, 'EnableOverlayNormal': 55, 'EnableRazermap': 56, 'EnableReflection': 57, 'LightMapEnable': 58, 'LightmapConstEnable': 59}
    value_to_names: dict = {45: 'AnisotropicEnable', 46: 'EnableAnimeMap', 47: 'EnableChangeMap', 48: 'EnableEmissive', 49: 'EnableEmissive3UV', 50: 'EnableIBL', 51: 'EnableMixmap', 52: 'EnableOverlay', 53: 'EnableOverlayMap', 54: 'EnableOverlayMatChange', 55: 'EnableOverlayNormal', 56: 'EnableRazermap', 57: 'EnableReflection', 58: 'LightMapEnable', 59: 'LightmapConstEnable'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class PbrGunShaderMacros(enum):
    AnisotropicEnable: int = 45
    EnableEmissive: int = 46
    EnableEmissive3UV: int = 47
    EnableIBL: int = 48
    EnableMatcap: int = 49
    EnableMixmap: int = 50
    EnableOverlay: int = 51
    EnableOverlayMap: int = 52
    EnableOverlayMatChange: int = 53
    EnableOverlayNormal: int = 54
    EnableRazermap: int = 55
    EnableReflection: int = 56
    LightMapEnable: int = 57
    LightmapConstEnable: int = 58
    name_to_values: dict = {'AnisotropicEnable': 45, 'EnableEmissive': 46, 'EnableEmissive3UV': 47, 'EnableIBL': 48, 'EnableMatcap': 49, 'EnableMixmap': 50, 'EnableOverlay': 51, 'EnableOverlayMap': 52, 'EnableOverlayMatChange': 53, 'EnableOverlayNormal': 54, 'EnableRazermap': 55, 'EnableReflection': 56, 'LightMapEnable': 57, 'LightmapConstEnable': 58}
    value_to_names: dict = {45: 'AnisotropicEnable', 46: 'EnableEmissive', 47: 'EnableEmissive3UV', 48: 'EnableIBL', 49: 'EnableMatcap', 50: 'EnableMixmap', 51: 'EnableOverlay', 52: 'EnableOverlayMap', 53: 'EnableOverlayMatChange', 54: 'EnableOverlayNormal', 55: 'EnableRazermap', 56: 'EnableReflection', 57: 'LightMapEnable', 58: 'LightmapConstEnable'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class SGScpeShaderMacros(enum):
    EnableDarkEdge: int = 45
    EnableDarkEdge2: int = 46
    EnableScope: int = 47
    name_to_values: dict = {'EnableDarkEdge': 45, 'EnableDarkEdge2': 46, 'EnableScope': 47}
    value_to_names: dict = {45: 'EnableDarkEdge', 46: 'EnableDarkEdge2', 47: 'EnableScope'}

    def add_string(name, value): ...
    def from_string(name): ...
    def to_string(value): ...
    def to_values(): ...
    def values(): ...

class ShaderMacros(enum):
    Billboard: int = 32
    CSMDynamic: int = 21
    Candela: int = 19
    CastSunShadow: int = 9
    Clipping: int = 26
    Debug0: int = 41
    Debug1: int = 42
    Debug2: int = 43
    Debug3: int = 44
    DeferredShading: int = 6
    Dissolving: int = 31
    ENCODEHDR: int = 8
    EShaderProfile_Skinning0: int = 24
    EShaderProfile_Skinning1: int = 25
    Emissive: int = 30
    EnvMapEnable: int = 16
    Feature0: int = 4
    Fog: int = 5
    HDR: int = 7
    Instanced: int = 40
    LightMap: int = 38
    LitCount0: int = 34
    LitCount1: int = 35
    LodLevel0: int = 22
    LodLevel1: int = 23
    NoFarPlaneClip: int = 28
    NoNearPlaneClip: int = 29
    Platform0: int = 0
    Platform1: int = 1
    Platform2: int = 2
    Platform3: int = 3
    ReceiveDynamicShadow: int = 33
    ReflectionMapEnable: int = 18
    Ripple: int = 14
    SSR: int = 17
    ShelterMapEnable: int = 15
    Tangent: int = 36
    Transparent: int = 27
    UV3UV4: int = 39
    VTEnable: int = 20
    VertexColor: int = 37
    VolumetricFog: int = 10
    Weather0: int = 12
    Weather1: int = 13
    _7MRT: int = 11
    name_to_values: dict = {'Platform0': 0, 'Platform1': 1, 'Platform2': 2, 'Platform3': 3, 'Feature0': 4, 'Fog': 5, 'DeferredShading': 6, 'HDR': 7, 'ENCODEHDR': 8, 'CastSunShadow': 9, 'VolumetricFog': 10, '_7MRT': 11, 'Weather0': 12, 'Weather1': 13, 'Ripple': 14, 'ShelterMapEnable': 15, 'EnvMapEnable': 16, 'SSR': 17, 'ReflectionMapEnable': 18, 'Candela': 19, 'VTEnable': 20, 'CSMDynamic': 21, 'LodLevel0': 22, 'LodLevel1': 23, 'EShaderProfile_Skinning0': 24, 'EShaderProfile_Skinning1': 25, 'Clipping': 26, 'Transparent': 27, 'NoFarPlaneClip': 28, 'NoNearPlaneClip': 29, 'Emissive': 30, 'Dissolving': 31, 'Billboard': 32, 'ReceiveDynamicShadow': 33, 'LitCount0': 34, 'LitCount1': 35, 'Tangent': 36, 'VertexColor': 37, 'LightMap': 38, 'UV3UV4': 39, 'Instanced': 40, 'Debug0': 41, 'Debug1': 42, 'Debug2': 43, 'Debug3': 44}
    value_to_names: dict = {0: 'Platform0', 1: 'Platform1', 2: 'Platform2', 3: 'Platform3', 4: 'Feature0', 5: 'Fog', 6: 'DeferredShading', 7: 'HDR', 8: 'ENCODEHDR', 9: 'CastSunShadow', 10: 'VolumetricFog', 11: '_7MRT', 12: 'Weather0', 13: 'Weather1', 14: 'Ripple', 15: 'ShelterMapEnable', 16: 'EnvMapEnable', 17: 'SSR', 18: 'ReflectionMapEnable', 19: 'Candela', 20: 'VTEnable', 21: 'CSMDynamic', 22: 'LodLevel0', 23: 'LodLevel1', 24: 'EShaderProfile_Skinning0', 25: 'EShaderProfile_Skinning1', 26: 'Clipping', 27: 'Transparent', 28: 'NoFarPlaneClip', 29: 'NoNearPlaneClip', 30: 'Emissive', 31: 'Dissolving', 32: 'Billboard', 33: 'ReceiveDynamicShadow', 34: 'LitCount0', 35: 'LitCount1', 36: 'Tangent', 37: 'VertexColor', 38: 'LightMap', 39: 'UV3UV4', 40: 'Instanced', 41: 'Debug0', 42: 'Debug1', 43: 'Debug2', 44: 'Debug3'}

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


def GetAllGunSkinMaterialParamGroup(pbr_gun_macros): ...
def GetAllGunSkinMaterialParamGroupWrapper(): ...


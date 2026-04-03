# module: gclient.framework.ui.ui_harmtext

import MType
import MUI
import formula
import six2

class Color(object):
    aliceblue: Color = <gshare.color.Color object at 0x6f9c411950>
    antiquewhite: Color = <gshare.color.Color object at 0x6f9c417850>
    aqua: Color = <gshare.color.Color object at 0x6f9c417110>
    aquamarine: Color = <gshare.color.Color object at 0x6f9c4171d0>
    azure: Color = <gshare.color.Color object at 0x6f9c417790>
    beige: Color = <gshare.color.Color object at 0x6f9c417d90>
    bisque: Color = <gshare.color.Color object at 0x6f9c417810>
    black: Color = <gshare.color.Color object at 0x6f9c417d50>
    blanchedalmond: Color = <gshare.color.Color object at 0x6f9c417cd0>
    blue: Color = <gshare.color.Color object at 0x6f9c5045d0>
    blueviolet: Color = <gshare.color.Color object at 0x6f9c417690>
    brown: Color = <gshare.color.Color object at 0x6f9c417650>
    burlywood: Color = <gshare.color.Color object at 0x6f9c417450>
    cadetblue: Color = <gshare.color.Color object at 0x6f9c417c10>
    chartreuse: Color = <gshare.color.Color object at 0x6f9c417c50>
    chocolate: Color = <gshare.color.Color object at 0x6f9c417ad0>
    coral: Color = <gshare.color.Color object at 0x6f9c4ebd90>
    cornflowerblue: Color = <gshare.color.Color object at 0x6f9c417a90>
    cornsilk: Color = <gshare.color.Color object at 0x6f9c50c7d0>
    crimson: Color = <gshare.color.Color object at 0x6f9c417d10>
    cyan: Color = <gshare.color.Color object at 0x6f9c417190>
    darkblue: Color = <gshare.color.Color object at 0x6f9c417c90>
    darkcyan: Color = <gshare.color.Color object at 0x6f9c417a10>
    darkgoldenrod: Color = <gshare.color.Color object at 0x6f9c417e50>
    darkgray: Color = <gshare.color.Color object at 0x6f9c417b50>
    darkgreen: Color = <gshare.color.Color object at 0x6f9c417350>
    darkgrey: Color = <gshare.color.Color object at 0x6fa22c3750>
    darkkhaki: Color = <gshare.color.Color object at 0x6f9c417310>
    darkmagenta: Color = <gshare.color.Color object at 0x6f9c417f10>
    darkolivegreen: Color = <gshare.color.Color object at 0x6f9c50c250>
    darkorange: Color = <gshare.color.Color object at 0x6f9c417250>
    darkorchid: Color = <gshare.color.Color object at 0x6f9c417e90>
    darkred: Color = <gshare.color.Color object at 0x6f9c417a50>
    darksalmon: Color = <gshare.color.Color object at 0x6f9c417f90>
    darkseagreen: Color = <gshare.color.Color object at 0x6f9c417fd0>
    darkslateblue: Color = <gshare.color.Color object at 0x6f9c417f50>
    darkslategray: Color = <gshare.color.Color object at 0x6f9c417ed0>
    darkslategrey: Color = <gshare.color.Color object at 0x6f9c417bd0>
    darkturquoise: Color = <gshare.color.Color object at 0x6fa22d8b50>
    darkviolet: Color = <gshare.color.Color object at 0x6f9c424050>
    deeppink: Color = <gshare.color.Color object at 0x6f9c424150>
    deepskyblue: Color = <gshare.color.Color object at 0x6f9c424190>
    dimgray: Color = <gshare.color.Color object at 0x6f9c50c790>
    dimgrey: Color = <gshare.color.Color object at 0x6fa22da490>
    dodgerblue: Color = <gshare.color.Color object at 0x6f9c4240d0>
    firebrick: Color = <gshare.color.Color object at 0x6f9c424210>
    floralwhite: Color = <gshare.color.Color object at 0x6f9c424110>
    forestgreen: Color = <gshare.color.Color object at 0x6f9c424290>
    fuchsia: Color = <gshare.color.Color object at 0x6f9c5056d0>
    gainsboro: Color = <gshare.color.Color object at 0x6f9c4242d0>
    ghostwhite: Color = <gshare.color.Color object at 0x6f9c424310>
    gold: Color = <gshare.color.Color object at 0x6f9c424250>
    goldenrod: Color = <gshare.color.Color object at 0x6f9c424390>
    gray: Color = <gshare.color.Color object at 0x6fa4e072d0>
    green: Color = <gshare.color.Color object at 0x6fa22b2110>
    greenyellow: Color = <gshare.color.Color object at 0x6f9c4241d0>
    grey: Color = <gshare.color.Color object at 0x6f9c505e50>
    honeydew: Color = <gshare.color.Color object at 0x6f9c424410>
    hotpink: Color = <gshare.color.Color object at 0x6f9c504710>
    indianred: Color = <gshare.color.Color object at 0x6fa22c27d0>
    indigo: Color = <gshare.color.Color object at 0x6f9c4243d0>
    ivory: Color = <gshare.color.Color object at 0x6f9c424490>
    khaki: Color = <gshare.color.Color object at 0x6f9c424350>
    lavender: Color = <gshare.color.Color object at 0x6f9c424510>
    lavenderblush: Color = <gshare.color.Color object at 0x6f9c424550>
    lawngreen: Color = <gshare.color.Color object at 0x6f9c424590>
    lemonchiffon: Color = <gshare.color.Color object at 0x6f9c504650>
    lightblue: Color = <gshare.color.Color object at 0x6f9c424450>
    lightcoral: Color = <gshare.color.Color object at 0x6f9c424610>
    lightcyan: Color = <gshare.color.Color object at 0x6f9c4244d0>
    lightgoldenrodyellow: Color = <gshare.color.Color object at 0x6f9c424690>
    lightgray: Color = <gshare.color.Color object at 0x6f9c4246d0>
    lightgreen: Color = <gshare.color.Color object at 0x6f9c424750>
    lightgrey: Color = <gshare.color.Color object at 0x6f9c424710>
    lightpink: Color = <gshare.color.Color object at 0x6f9c504690>
    lightsalmon: Color = <gshare.color.Color object at 0x6fa21403d0>
    lightseagreen: Color = <gshare.color.Color object at 0x6f9c4245d0>
    lightskyblue: Color = <gshare.color.Color object at 0x6fa22da390>
    lightslategray: Color = <gshare.color.Color object at 0x6f9c4247d0>
    lightslategrey: Color = <gshare.color.Color object at 0x6f9c424650>
    lightsteelblue: Color = <gshare.color.Color object at 0x6f9c424810>
    lightyellow: Color = <gshare.color.Color object at 0x6f9c424890>
    lime: Color = <gshare.color.Color object at 0x6f9c4248d0>
    limegreen: Color = <gshare.color.Color object at 0x6f9c424910>
    linen: Color = <gshare.color.Color object at 0x6f9c505f10>
    magenta: Color = <gshare.color.Color object at 0x6f9c424950>
    maroon: Color = <gshare.color.Color object at 0x6f9c424790>
    mediumaquamarine: Color = <gshare.color.Color object at 0x6f9c4249d0>
    mediumblue: Color = <gshare.color.Color object at 0x6f9c424090>
    mediumorchid: Color = <gshare.color.Color object at 0x6f9c424a50>
    mediumpurple: Color = <gshare.color.Color object at 0x6fa219f590>
    mediumseagreen: Color = <gshare.color.Color object at 0x6f9c424a90>
    mediumslateblue: Color = <gshare.color.Color object at 0x6f9c424ad0>
    mediumspringgreen: Color = <gshare.color.Color object at 0x6fa22c20d0>
    mediumturquoise: Color = <gshare.color.Color object at 0x6f9c424850>
    mediumvioletred: Color = <gshare.color.Color object at 0x6f9c424b50>
    midnightblue: Color = <gshare.color.Color object at 0x6f9c424a10>
    mintcream: Color = <gshare.color.Color object at 0x6f9c424bd0>
    mistyrose: Color = <gshare.color.Color object at 0x6f9c424c10>
    moccasin: Color = <gshare.color.Color object at 0x6fa22d8390>
    navajowhite: Color = <gshare.color.Color object at 0x6f9c424c50>
    navy: Color = <gshare.color.Color object at 0x6f9c424c90>
    oldlace: Color = <gshare.color.Color object at 0x6f9c424b10>
    olive: Color = <gshare.color.Color object at 0x6f9c424d10>
    olivedrab: Color = <gshare.color.Color object at 0x6f9c424d50>
    orange: Color = <gshare.color.Color object at 0x6f9c424d90>
    orangered: Color = <gshare.color.Color object at 0x6f9c424dd0>
    orchid: Color = <gshare.color.Color object at 0x6f9c424e10>
    palegoldenrod: Color = <gshare.color.Color object at 0x6f9c424e50>
    palegreen: Color = <gshare.color.Color object at 0x6f9c424e90>
    paleturquoise: Color = <gshare.color.Color object at 0x6f9c424ed0>
    palevioletred: Color = <gshare.color.Color object at 0x6f9c424f10>
    papayawhip: Color = <gshare.color.Color object at 0x6f9c504a50>
    peachpuff: Color = <gshare.color.Color object at 0x6f9c424f50>
    peru: Color = <gshare.color.Color object at 0x6f9c50c0d0>
    pink: Color = <gshare.color.Color object at 0x6f9c50c110>
    plum: Color = <gshare.color.Color object at 0x6f9c424990>
    powderblue: Color = <gshare.color.Color object at 0x6f9c424fd0>
    purple: Color = <gshare.color.Color object at 0x6f9c425010>
    red: Color = <gshare.color.Color object at 0x6f9c425050>
    rosybrown: Color = <gshare.color.Color object at 0x6f9c425090>
    royalblue: Color = <gshare.color.Color object at 0x6f9c4250d0>
    saddlebrown: Color = <gshare.color.Color object at 0x6f9c425110>
    salmon: Color = <gshare.color.Color object at 0x6f9c425150>
    sandybrown: Color = <gshare.color.Color object at 0x6f9c425190>
    seagreen: Color = <gshare.color.Color object at 0x6f9c4251d0>
    seashell: Color = <gshare.color.Color object at 0x6f9c425210>
    sienna: Color = <gshare.color.Color object at 0x6f9c425250>
    silver: Color = <gshare.color.Color object at 0x6f9c425290>
    skyblue: Color = <gshare.color.Color object at 0x6f9c4252d0>
    slateblue: Color = <gshare.color.Color object at 0x6f9c425310>
    slategray: Color = <gshare.color.Color object at 0x6f9c425350>
    slategrey: Color = <gshare.color.Color object at 0x6f9c425390>
    snow: Color = <gshare.color.Color object at 0x6f9c4253d0>
    springgreen: Color = <gshare.color.Color object at 0x6f9c425410>
    steelblue: Color = <gshare.color.Color object at 0x6f9c425450>
    tan: Color = <gshare.color.Color object at 0x6f9c425490>
    teal: Color = <gshare.color.Color object at 0x6f9c4254d0>
    thistle: Color = <gshare.color.Color object at 0x6f9c50c090>
    tomato: Color = <gshare.color.Color object at 0x6f9c424f90>
    turquoise: Color = <gshare.color.Color object at 0x6f9c425550>
    violet: Color = <gshare.color.Color object at 0x6f9c424b90>
    wheat: Color = <gshare.color.Color object at 0x6f9c564750>
    white: Color = <gshare.color.Color object at 0x6f9c4255d0>
    whitesmoke: Color = <gshare.color.Color object at 0x6f9c425610>
    yellow: Color = <gshare.color.Color object at 0x6f9c424cd0>
    yellowgreen: Color = <gshare.color.Color object at 0x6f9c50c3d0>

    def To(self, cls): ...
    def _From(self, *args, **kwargs): ...
    @property
    def hsv(self): ...    @property
    def name(self): ...
class HarmTextType(object):
    Additional: int = 2
    Award: int = 4
    Critical: int = 3
    Hero: int = 0
    Monster: int = 1
    Pokemon: int = 5

class SingletonMeta(type):
    mro: method_descriptor = <method 'mro' of 'type' objects>

class _HarmTextAnimation(object):
    _instance: NoneType = None

class _MsgAnimation(object):
    _instance: NoneType = None


def ShowBulletinText(content): ...
def ShowDamageText(target, content, font_index=2, itype=0, color=(255, 255, 255), off_pos=None, scale=0.5): ...
def ShowMessageText(content, itype=0, sinkTime=3.0, strokeColor=<gshare.color.Color object at 0x6f9c424250>): ...


"""
BloodStrike Skin Changer Module
Changes weapon skins in BloodStrike

Based on real BloodStrike weapon and skin IDs from UnknownCheats:
- Weapon IDs: M4A1=1, MP5=2, AK47=40, VECTOR=38, SCAR=88, AUG=98
- Skin IDs: Various format like 101100029 (AK47), 11100018 (M4A1)
"""

import time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class WeaponSkin:
    """Weapon skin data"""
    weapon_id: int
    skin_id: int
    name: str
    rarity: str = "Common"


# Real BloodStrike Weapon IDs
class WeaponIDs:
    """BloodStrike weapon IDs"""
    M4A1 = 1
    MP5 = 2
    AK47 = 40
    VECTOR = 38
    SCAR = 88
    AUG = 98
    M249 = 54
    MP7 = 4
    UZI = 3
    P90 = 5
    HK416 = 89
    M16 = 90
    AWM = 60
    KAR98K = 61
    MOSIN = 62
    SVD = 63
    MK14 = 64


# Real BloodStrike Skin IDs (from UnknownCheats community)
class SkinIDs:
    """BloodStrike skin IDs"""
    # AK47 Skins
    AK47_DEFAULT = 0
    AK47_TACTICAL = 101100001
    AK47_BLOODLINE = 101100005
    AK47_FURY = 101100029
    
    # M4A1 Skins
    M4A1_DEFAULT = 0
    M4A1_CARBON = 11100005
    M4A1_PHANTOM = 11100018
    M4A1_GHOST = 11100025
    
    # MP5 Skins
    MP5_DEFAULT = 0
    MP5_TACTICAL = 20110001
    
    # Vector Skins
    VECTOR_DEFAULT = 0
    VECTOR_URBAN = 38110001
    
    # SCAR Skins
    SCAR_DEFAULT = 0
    SCAR_TACTICAL = 88110001
    
    # AUG Skins
    AUG_DEFAULT = 0
    AUG_STRIKER = 98110001


# Weapon Names for display
WEAPON_NAMES = {
    1: "M4A1",
    2: "MP5",
    3: "UZI",
    4: "MP7",
    5: "P90",
    38: "Vector",
    40: "AK47",
    54: "M249",
    60: "AWM",
    61: "Kar98k",
    62: "Mosin",
    63: "SVD",
    64: "MK14",
    88: "SCAR",
    89: "HK416",
    90: "M16",
    98: "AUG",
}

# Skin database
SKIN_DATABASE = {
    WeaponIDs.M4A1: [
        WeaponSkin(WeaponIDs.M4A1, 0, "Default", "Common"),
        WeaponSkin(WeaponIDs.M4A1, 11100005, "Carbon Fiber", "Rare"),
        WeaponSkin(WeaponIDs.M4A1, 11100018, "Phantom", "Epic"),
        WeaponSkin(WeaponIDs.M4A1, 11100025, "Ghost", "Legendary"),
    ],
    WeaponIDs.AK47: [
        WeaponSkin(WeaponIDs.AK47, 0, "Default", "Common"),
        WeaponSkin(WeaponIDs.AK47, 101100001, "Tactical", "Rare"),
        WeaponSkin(WeaponIDs.AK47, 101100005, "Bloodline", "Epic"),
        WeaponSkin(WeaponIDs.AK47, 101100029, "Fury", "Legendary"),
    ],
    WeaponIDs.MP5: [
        WeaponSkin(WeaponIDs.MP5, 0, "Default", "Common"),
        WeaponSkin(WeaponIDs.MP5, 20110001, "Tactical", "Rare"),
    ],
    WeaponIDs.VECTOR: [
        WeaponSkin(WeaponIDs.VECTOR, 0, "Default", "Common"),
        WeaponSkin(WeaponIDs.VECTOR, 38110001, "Urban", "Rare"),
    ],
    WeaponIDs.SCAR: [
        WeaponSkin(WeaponIDs.SCAR, 0, "Default", "Common"),
        WeaponSkin(WeaponIDs.SCAR, 88110001, "Tactical", "Rare"),
    ],
    WeaponIDs.AUG: [
        WeaponSkin(WeaponIDs.AUG, 0, "Default", "Common"),
        WeaponSkin(WeaponIDs.AUG, 98110001, "Striker", "Rare"),
    ],
}


class SkinChanger:
    """
    Skin changer implementation for BloodStrike.
    Modifies weapon appearance in-game.
    """
    
    def __init__(self, sdk, entity_manager):
        self.sdk = sdk
        self.entity_manager = entity_manager
        
        # Settings
        self.enabled = False
        self.selected_skins: Dict[int, int] = {}  # weapon_id -> skin_id
        
        # State
        self._applied_skins: Dict[int, int] = {}
        self._last_apply_time = 0
    
    def update(self) -> None:
        """Main update function"""
        if not self.enabled:
            return
        
        # Re-apply skins periodically
        current_time = time.time()
        if current_time - self._last_apply_time > 5.0:
            self.apply_all_skins()
            self._last_apply_time = current_time
    
    def set_skin(self, weapon_id: int, skin_id: int) -> None:
        """Set skin for a weapon"""
        self.selected_skins[weapon_id] = skin_id
        
        if self.enabled:
            self.apply_skin(weapon_id, skin_id)
    
    def get_skin(self, weapon_id: int) -> int:
        """Get current skin for a weapon"""
        return self.selected_skins.get(weapon_id, 0)
    
    def apply_skin(self, weapon_id: int, skin_id: int) -> bool:
        """Apply a skin to current weapon"""
        try:
            local_player = self.sdk.get_local_player()
            if not local_player:
                return False
            
            # Get weapon
            if hasattr(local_player, 'weapon') and local_player.weapon:
                weapon = local_player.weapon
                
                # Check if it's the right weapon type
                if hasattr(weapon, 'weapon_id'):
                    if weapon.weapon_id != weapon_id:
                        return False
                
                # Apply skin
                if hasattr(weapon, 'skin_id'):
                    weapon.skin_id = skin_id
                if hasattr(weapon, 'paint_id'):
                    weapon.paint_id = skin_id
                if hasattr(weapon, 'appearance_id'):
                    weapon.appearance_id = skin_id
                
                self._applied_skins[weapon_id] = skin_id
                return True
            
            return False
        except Exception as e:
            print(f"[SkinChanger] Apply failed: {e}")
            return False
    
    def apply_all_skins(self) -> None:
        """Apply all selected skins"""
        for weapon_id, skin_id in self.selected_skins.items():
            self.apply_skin(weapon_id, skin_id)
    
    def reset_skin(self, weapon_id: int) -> None:
        """Reset weapon skin to default"""
        if weapon_id in self.selected_skins:
            del self.selected_skins[weapon_id]
        if weapon_id in self._applied_skins:
            del self._applied_skins[weapon_id]
        self.apply_skin(weapon_id, 0)
    
    def reset_all_skins(self) -> None:
        """Reset all skins to default"""
        for weapon_id in list(self.selected_skins.keys()):
            self.reset_skin(weapon_id)
    
    def get_available_skins(self, weapon_id: int) -> List[WeaponSkin]:
        """Get all available skins for a weapon"""
        return SKIN_DATABASE.get(weapon_id, [])
    
    def get_weapon_name(self, weapon_id: int) -> str:
        """Get weapon name from ID"""
        return WEAPON_NAMES.get(weapon_id, f"Unknown ({weapon_id})")
    
    def get_all_weapons(self) -> List[int]:
        """Get list of all supported weapons"""
        return list(WEAPON_NAMES.keys())
    
    def set_enabled(self, enabled: bool) -> None:
        """Enable or disable skin changer"""
        self.enabled = enabled
        
        if enabled:
            self.apply_all_skins()
        else:
            self.reset_all_skins()
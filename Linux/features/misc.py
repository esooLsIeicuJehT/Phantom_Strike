"""
BloodStrike Miscellaneous Features
Various cheat features like infinite ammo, no recoil, etc.
"""

import time
from typing import Optional, Dict, Any
from dataclasses import dataclass


@dataclass
class MiscSettings:
    """Miscellaneous cheat settings"""
    # Movement
    speed_hack: bool = False
    speed_multiplier: float = 1.5
    infinite_stamina: bool = False
    no_clip: bool = False
    
    # Combat
    no_recoil: bool = False
    no_spread: bool = False
    rapid_fire: bool = False
    infinite_ammo: bool = False
    no_reload: bool = False
    
    # Visual
    no_fog: bool = False
    full_bright: bool = False
    xray_vision: bool = False
    fov_changer: bool = False
    custom_fov: float = 90.0
    
    # Other
    anti_afk: bool = False
    auto_pickup: bool = False
    auto_loot: bool = False


class MiscFeatures:
    """
    Miscellaneous cheat features implementation.
    """
    
    def __init__(self, sdk, entity_manager):
        self.sdk = sdk
        self.entity_manager = entity_manager
        self.settings = MiscSettings()
        
        # State
        self._last_afk_time = time.time()
    
    def update(self) -> None:
        """Main update function - call every frame"""
        local_player = self.sdk.get_local_player()
        if not local_player:
            return
        
        # Apply enabled features
        if self.settings.no_recoil:
            self._apply_no_recoil(local_player)
        
        if self.settings.no_spread:
            self._apply_no_spread(local_player)
        
        if self.settings.infinite_ammo:
            self._apply_infinite_ammo(local_player)
        
        if self.settings.speed_hack:
            self._apply_speed_hack(local_player)
        
        if self.settings.anti_afk:
            self._handle_anti_afk()
        
        if self.settings.xray_vision:
            self._apply_xray()
        
        if self.settings.fov_changer:
            self._apply_fov_changer()
    
    def _apply_no_recoil(self, player: Any) -> None:
        """Remove weapon recoil"""
        try:
            if hasattr(player, 'weapon') and player.weapon:
                weapon = player.weapon
                # BloodStrike-specific weapon attributes
                if hasattr(weapon, 'recoil'):
                    weapon.recoil = 0
                if hasattr(weapon, 'recoil_pattern'):
                    weapon.recoil_pattern = []
        except Exception as e:
            print(f"[Misc] No recoil failed: {e}")
    
    def _apply_no_spread(self, player: Any) -> None:
        """Remove weapon spread"""
        try:
            if hasattr(player, 'weapon') and player.weapon:
                weapon = player.weapon
                if hasattr(weapon, 'spread'):
                    weapon.spread = 0
                if hasattr(weapon, 'accuracy'):
                    weapon.accuracy = 1.0
        except Exception as e:
            print(f"[Misc] No spread failed: {e}")
    
    def _apply_infinite_ammo(self, player: Any) -> None:
        """Set infinite ammo"""
        try:
            if hasattr(player, 'weapon') and player.weapon:
                weapon = player.weapon
                if hasattr(weapon, 'ammo'):
                    weapon.ammo = 999
                if hasattr(weapon, 'reserve_ammo'):
                    weapon.reserve_ammo = 999
                if hasattr(weapon, 'magazine'):
                    weapon.magazine = 999
        except Exception as e:
            print(f"[Misc] Infinite ammo failed: {e}")
    
    def _apply_speed_hack(self, player: Any) -> None:
        """Apply movement speed modification"""
        try:
            if hasattr(player, 'movement') and player.movement:
                movement = player.movement
                if hasattr(movement, 'walk_speed'):
                    movement.walk_speed = movement.walk_speed * self.settings.speed_multiplier
                if hasattr(movement, 'run_speed'):
                    movement.run_speed = movement.run_speed * self.settings.speed_multiplier
                if hasattr(movement, 'sprint_speed'):
                    movement.sprint_speed = movement.sprint_speed * self.settings.speed_multiplier
        except Exception as e:
            print(f"[Misc] Speed hack failed: {e}")
    
    def _handle_anti_afk(self) -> None:
        """Prevent AFK kick"""
        current_time = time.time()
        
        # Simulate activity every 30 seconds
        if current_time - self._last_afk_time > 30:
            # Would need to send input or movement
            self._last_afk_time = current_time
    
    def _apply_xray(self) -> None:
        """Apply X-ray vision effect"""
        try:
            if hasattr(self.sdk.space, 'UseTechHighLightXray'):
                self.sdk.space.UseTechHighLightXray(True)
        except Exception as e:
            print(f"[Misc] X-ray failed: {e}")
    
    def _apply_fov_changer(self) -> None:
        """Change camera FOV"""
        try:
            if self.sdk.camera and hasattr(self.sdk.camera, 'fov'):
                self.sdk.camera.fov = self.settings.custom_fov
        except Exception as e:
            print(f"[Misc] FOV change failed: {e}")
    
    def set_speed_multiplier(self, multiplier: float) -> None:
        """Set speed hack multiplier"""
        self.settings.speed_multiplier = max(0.5, min(5.0, multiplier))
    
    def set_custom_fov(self, fov: float) -> None:
        """Set custom FOV"""
        self.settings.custom_fov = max(60.0, min(120.0, fov))
    
    def toggle_no_recoil(self, enabled: bool = None) -> bool:
        """Toggle no recoil"""
        if enabled is not None:
            self.settings.no_recoil = enabled
        else:
            self.settings.no_recoil = not self.settings.no_recoil
        return self.settings.no_recoil
    
    def toggle_no_spread(self, enabled: bool = None) -> bool:
        """Toggle no spread"""
        if enabled is not None:
            self.settings.no_spread = enabled
        else:
            self.settings.no_spread = not self.settings.no_spread
        return self.settings.no_spread
    
    def toggle_infinite_ammo(self, enabled: bool = None) -> bool:
        """Toggle infinite ammo"""
        if enabled is not None:
            self.settings.infinite_ammo = enabled
        else:
            self.settings.infinite_ammo = not self.settings.infinite_ammo
        return self.settings.infinite_ammo
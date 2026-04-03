"""
BloodStrike Aimbot Module
Implements aim assistance with multiple modes and settings

Based on research from UnknownCheats:
- Use StoryTick._instance for hooking game updates
- Use Space._instance.camera.placer.Rotate(yaw, pitch) for aim
- Bone names: biped Head, biped Spine1, biped Spine
"""

import math
import time
from typing import Optional, Tuple, List, Any
from dataclasses import dataclass
from enum import Enum


class AimTarget(Enum):
    HEAD = "head"
    NECK = "neck"
    CHEST = "chest"
    SPINE = "spine"
    CUSTOM = "custom"


class AimMode(Enum):
    HOLD = "hold"           # Aim while key is held
    TOGGLE = "toggle"       # Toggle aim on/off
    AUTO = "auto"           # Automatic aiming
    ON_KEY = "on_key"       # Aim only when specific key is pressed


@dataclass
class AimbotSettings:
    """Aimbot configuration settings"""
    enabled: bool = False
    target_bone: AimTarget = AimTarget.HEAD
    aim_mode: AimMode = AimMode.HOLD
    aim_key: int = 0x02     # Right mouse button
    
    # Aim settings
    smoothness: float = 0.5      # 0.0 = instant, 1.0 = very slow
    fov: float = 90.0            # Field of view in degrees
    max_distance: float = 500.0  # Maximum target distance
    
    # Advanced settings
    visibility_check: bool = True
    target_allies: bool = False
    silent_aim: bool = False     # Don't actually move view (for silent aim)
    prediction: bool = False     # Predict target movement
    prediction_factor: float = 1.0
    
    # RCS (Recoil Control System)
    rcs_enabled: bool = False
    rcs_smoothness: float = 0.8
    rcs_horizontal: float = 1.0
    rcs_vertical: float = 1.0
    
    # Trigger bot
    trigger_bot: bool = False
    trigger_delay: float = 0.0   # Delay in seconds
    trigger_key: int = 0x05      # Side mouse button


class Aimbot:
    """
    Aimbot implementation for BloodStrike.
    Uses the game's internal camera rotation for aim manipulation.
    """
    
    BONE_MAPPING = {
        AimTarget.HEAD: 'biped Head',
        AimTarget.NECK: 'biped Neck',
        AimTarget.CHEST: 'biped Spine1',
        AimTarget.SPINE: 'biped Spine',
    }
    
    def __init__(self, sdk, entity_manager):
        self.sdk = sdk
        self.entity_manager = entity_manager
        self.settings = AimbotSettings()
        
        # State
        self.current_target = None
        self.last_aim_time = 0
        self.is_active = False
        self.last_view_angles = (0.0, 0.0)
        self.shots_fired = 0
        self.last_recoil_time = 0
        
        # Hook callback
        self._hook_installed = False
    
    def update(self, delta_time: float = 0.016) -> None:
        """Main update function - call every frame"""
        if not self.settings.enabled:
            return
        
        # Update entity list
        self.entity_manager.update()
        
        # Check if aimbot key is active (for now, always active if enabled)
        # In a real implementation, you'd check actual key state
        if self.settings.aim_mode == AimMode.AUTO:
            self.is_active = True
        
        # Find target
        if self.current_target is None or not self.is_target_valid(self.current_target):
            self.current_target = self.find_best_target()
        
        # Aim at target
        if self.current_target and self.is_active:
            self.aim_at_target(self.current_target, delta_time)
    
    def find_best_target(self) -> Optional[Any]:
        """Find the best target based on settings"""
        if not self.sdk.camera:
            return None
        
        local_pos = self.sdk.get_camera_position()
        if not local_pos:
            return None
        
        best_target = None
        best_score = float('inf')
        
        for entity in self.entity_manager.get_players(alive_only=True, 
                                                        exclude_allies=not self.settings.target_allies):
            # Check distance
            distance = entity.get_distance(local_pos)
            if distance > self.settings.max_distance:
                continue
            
            # Get target bone position
            bone_name = self.BONE_MAPPING.get(self.settings.target_bone, 'biped Head')
            bone_pos = entity.get_bone_position(bone_name)
            
            if not bone_pos:
                continue
            
            # Check FOV
            if self.settings.fov < 180:
                screen_pos = self.sdk.world_to_screen(bone_pos)
                if screen_pos:
                    # Calculate angle to target
                    center_x = 1920 / 2  # Would need actual screen size
                    center_y = 1080 / 2
                    dx = abs(screen_pos[0] - center_x)
                    dy = abs(screen_pos[1] - center_y)
                    
                    # Convert pixel distance to degrees (approximate)
                    angle_dist = math.sqrt(dx*dx + dy*dy)
                    fov_radius = (self.settings.fov / 90.0) * center_x
                    
                    if angle_dist > fov_radius:
                        continue
            
            # Calculate score (lower is better)
            score = distance
            
            if score < best_score:
                best_score = score
                best_target = entity
        
        return best_target
    
    def is_target_valid(self, target: Any) -> bool:
        """Check if target is still valid"""
        if target is None:
            return False
        
        if not target.is_alive:
            return False
        
        distance = target.get_distance()
        if distance > self.settings.max_distance:
            return False
        
        return True
    
    def aim_at_target(self, target: Any, delta_time: float) -> None:
        """Aim at the specified target"""
        if not self.sdk.camera:
            return
        
        # Get target bone position
        bone_name = self.BONE_MAPPING.get(self.settings.target_bone, 'biped Head')
        target_pos = target.get_bone_position(bone_name)
        
        if not target_pos:
            return
        
        # Get current camera position
        camera_pos = self.sdk.get_camera_position()
        
        # Calculate required angles
        dx = target_pos[0] - camera_pos[0]
        dy = target_pos[1] - camera_pos[1]
        dz = target_pos[2] - camera_pos[2]
        
        distance_2d = math.sqrt(dx*dx + dz*dz)
        
        target_pitch = math.atan2(-dy, distance_2d)
        target_yaw = math.atan2(dx, dz)
        
        # Apply prediction if enabled
        if self.settings.prediction:
            # Would need velocity tracking
            pass
        
        # Apply smoothness
        if self.settings.smoothness > 0:
            smooth_factor = 1.0 - self.settings.smoothness
            target_pitch = self.last_view_angles[0] + (target_pitch - self.last_view_angles[0]) * smooth_factor
            target_yaw = self.last_view_angles[1] + (target_yaw - self.last_view_angles[1]) * smooth_factor
        
        # Apply RCS if enabled
        if self.settings.rcs_enabled:
            target_pitch, target_yaw = self.apply_rcs(target_pitch, target_yaw)
        
        # Apply rotation using BloodStrike's internal method
        self.apply_rotation(target_pitch, target_yaw)
        
        # Store last angles
        self.last_view_angles = (target_pitch, target_yaw)
    
    def apply_rotation(self, pitch: float, yaw: float) -> None:
        """Apply rotation to the game camera"""
        if self.settings.silent_aim:
            # Silent aim - would need to hook firing instead
            return
        
        try:
            # Access the camera placer to rotate
            if hasattr(self.sdk.camera, 'placer'):
                placer = self.sdk.camera.placer
                if hasattr(placer, 'Rotate'):
                    placer.Rotate(yaw, pitch)
        except Exception as e:
            print(f"[Aimbot] Rotation failed: {e}")
    
    def apply_rcs(self, pitch: float, yaw: float) -> Tuple[float, float]:
        """Apply recoil control to aim angles"""
        # This would need actual recoil pattern data
        return pitch, yaw
    
    def on_key_event(self, key: int, pressed: bool) -> None:
        """Handle key events"""
        if key == self.settings.aim_key:
            if self.settings.aim_mode == AimMode.HOLD:
                self.is_active = pressed
            elif self.settings.aim_mode == AimMode.TOGGLE and pressed:
                self.is_active = not self.is_active
            elif self.settings.aim_mode == AimMode.ON_KEY:
                self.is_active = pressed
    
    def set_target_bone(self, bone: AimTarget) -> None:
        """Change target bone"""
        self.settings.target_bone = bone
    
    def set_fov(self, fov: float) -> None:
        """Set aimbot FOV"""
        self.settings.fov = max(1.0, min(180.0, fov))
    
    def set_smoothness(self, smoothness: float) -> None:
        """Set aimbot smoothness"""
        self.settings.smoothness = max(0.0, min(1.0, smoothness))
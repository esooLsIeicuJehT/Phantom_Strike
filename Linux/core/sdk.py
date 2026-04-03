"""
BloodStrike Python SDK
Provides access to BloodStrike's internal game engine via embedded Python

Based on research from UnknownCheats forum:
- Key classes: Space, CombatAvatar, StoryTick
- Bone names: biped Head, biped Spine1, biped Spine, biped Neck
- Methods: GetBoneWorldPosition, GetScreenPointFromWorldPoint, Rotate
"""

import time
import math
from typing import Optional, List, Dict, Any, Tuple


class BloodStrikeSDK:
    """
    Main SDK class for interacting with BloodStrike's game engine.
    Uses the embedded Python interpreter within the game.
    """
    
    _instance = None
    
    def __init__(self):
        self.space = None
        self.camera = None
        self.local_player = None
        self.initialized = False
        self.entities = []
        
    @classmethod
    def get_instance(cls):
        """Get singleton instance of the SDK"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def initialize(self) -> bool:
        """
        Initialize the SDK by connecting to BloodStrike's internal Python.
        This code is designed to be injected into the game's Python interpreter.
        """
        try:
            # Access BloodStrike's internal Space instance
            # In the actual injection, these would be available globally
            global Space
            global StoryTick
            global CombatAvatar
            
            if 'Space' in globals() and hasattr(Space, '_instance'):
                self.space = Space._instance
                self.camera = self.space.camera if hasattr(self.space, 'camera') else None
                self.initialized = True
                return True
            return False
        except Exception as e:
            print(f"[SDK] Initialization failed: {e}")
            return False
    
    def initialize_internal(self) -> bool:
        """
        Initialize in internal mode - running inside game's Python interpreter.
        This assumes the code is injected into BloodStrike's CPython environment.
        """
        return self.initialize()
    
    def initialize_external(self, pid: int) -> bool:
        """
        Initialize in external mode - attach to game process via memory reading.
        
        Args:
            pid: Process ID of BloodStrike
            
        Returns:
            True if initialization successful
        """
        try:
            from utils.memory import MemoryReader
            
            # Create memory reader for the process
            self.memory_reader = MemoryReader(pid)
            
            # Open process memory
            if not self.memory_reader.open():
                print(f"[SDK] Failed to open process memory for PID {pid}")
                return False
            
            # In external mode, we can't directly access game objects
            # We would need to find memory addresses and read them
            # For now, mark as initialized but with limited functionality
            self.initialized = True
            print(f"[SDK] External mode initialized for PID {pid}")
            print("[SDK] Note: External mode has limited functionality")
            
            return True
        except Exception as e:
            print(f"[SDK] External initialization failed: {e}")
            return False
    
    def cleanup(self):
        """Cleanup SDK resources"""
        if hasattr(self, 'memory_reader') and self.memory_reader:
            self.memory_reader.close()
        self.initialized = False
    
    def get_local_player(self) -> Optional[Any]:
        """Get the local player entity"""
        if not self.initialized or not self.space:
            return None
        
        try:
            # Access local player through Space instance
            if hasattr(self.space, 'local_player'):
                return self.space.local_player
            elif hasattr(self.space, 'player'):
                return self.space.player
            return None
        except:
            return None
    
    def get_entities(self) -> List[Any]:
        """Get all entities in the game world"""
        if not self.initialized or not self.space:
            return []
        
        try:
            entities = []
            if hasattr(self.space, 'entities'):
                for ent in self.space.entities:
                    if ent and hasattr(ent, 'is_alive') and ent.is_alive:
                        entities.append(ent)
            return entities
        except:
            return []
    
    def get_camera_position(self) -> Tuple[float, float, float]:
        """Get the camera's world position"""
        if not self.camera:
            return (0, 0, 0)
        
        try:
            if hasattr(self.camera, 'pos'):
                pos = self.camera.pos
                return (pos.x, pos.y, pos.z)
            elif hasattr(self.camera, 'position'):
                pos = self.camera.position
                return (pos.x, pos.y, pos.z)
            return (0, 0, 0)
        except:
            return (0, 0, 0)
    
    def world_to_screen(self, world_pos: Tuple[float, float, float]) -> Optional[Tuple[float, float]]:
        """Convert world coordinates to screen coordinates"""
        if not self.camera:
            return None
        
        try:
            # Use BloodStrike's built-in projection method
            if hasattr(self.camera, 'GetScreenPointFromWorldPoint'):
                screen_pos = self.camera.GetScreenPointFromWorldPoint(world_pos)
                if screen_pos:
                    return (screen_pos.x, screen_pos.y)
            return None
        except:
            return None
    
    def get_bone_position(self, entity: Any, bone_name: str) -> Optional[Tuple[float, float, float]]:
        """Get the world position of a bone on an entity"""
        try:
            if hasattr(entity, 'model') and hasattr(entity.model, 'GetBoneWorldPosition'):
                pos = entity.model.GetBoneWorldPosition(bone_name)
                if pos:
                    return (pos.x, pos.y, pos.z)
            return None
        except:
            return None


class Vector3:
    """3D Vector class for mathematical operations"""
    
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar: float):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __truediv__(self, scalar: float):
        if scalar == 0:
            return Vector3(0, 0, 0)
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalized(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector3(0, 0, 0)
        return self / mag
    
    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def distance_to(self, other) -> float:
        return (self - other).magnitude()
    
    def to_tuple(self) -> Tuple[float, float, float]:
        return (self.x, self.y, self.z)
    
    @staticmethod
    def from_tuple(t: Tuple[float, float, float]):
        return Vector3(t[0], t[1], t[2])


class MathUtils:
    """Mathematical utilities for game calculations"""
    
    @staticmethod
    def calculate_angle(source: Vector3, target: Vector3) -> Tuple[float, float]:
        """Calculate pitch and yaw angles from source to target"""
        delta = target - source
        distance = math.sqrt(delta.x**2 + delta.z**2)
        
        pitch = math.atan2(-delta.y, distance)
        yaw = math.atan2(delta.x, delta.z)
        
        return (pitch, yaw)
    
    @staticmethod
    def degrees_to_radians(degrees: float) -> float:
        return degrees * (math.pi / 180)
    
    @staticmethod
    def radians_to_degrees(radians: float) -> float:
        return radians * (180 / math.pi)
    
    @staticmethod
    def smooth_angle(current: float, target: float, smoothness: float) -> float:
        """Smoothly interpolate between angles"""
        delta = target - current
        
        # Normalize angle to -pi to pi
        while delta > math.pi:
            delta -= 2 * math.pi
        while delta < -math.pi:
            delta += 2 * math.pi
        
        return current + delta * smoothness
    
    @staticmethod
    def is_point_in_fov(view_angle: Tuple[float, float], point_angle: Tuple[float, float], fov: float) -> bool:
        """Check if a point is within the FOV"""
        pitch_diff = abs(view_angle[0] - point_angle[0])
        yaw_diff = abs(view_angle[1] - point_angle[1])
        
        # Normalize angles
        while yaw_diff > math.pi:
            yaw_diff -= 2 * math.pi
        yaw_diff = abs(yaw_diff)
        
        return pitch_diff <= fov and yaw_diff <= fov
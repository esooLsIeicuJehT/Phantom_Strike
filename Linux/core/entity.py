"""
Entity Manager for BloodStrike
Handles entity iteration, filtering, and target selection
"""

import time
from typing import Optional, List, Dict, Any, Tuple
from dataclasses import dataclass
from enum import Enum


class EntityType(Enum):
    PLAYER = "player"
    NPC = "npc"
    ITEM = "item"
    PROJECTILE = "projectile"
    UNKNOWN = "unknown"


@dataclass
class EntityInfo:
    """Stores processed entity information"""
    entity: Any
    entity_type: EntityType
    position: Tuple[float, float, float]
    health: int
    max_health: int
    is_alive: bool
    is_visible: bool
    is_allied: bool
    distance: float
    name: str
    team_id: int
    
    # Bone positions
    head_pos: Optional[Tuple[float, float, float]] = None
    spine_pos: Optional[Tuple[float, float, float]] = None
    neck_pos: Optional[Tuple[float, float, float]] = None


class Entity:
    """Wrapper class for BloodStrike entities"""
    
    # Bone names for BloodStrike
    BONE_NAMES = {
        'head': 'biped Head',
        'spine': 'biped Spine1',
        'spine2': 'biped Spine',
        'neck': 'biped Neck',
        'left_shoulder': 'biped L Clavicle',
        'right_shoulder': 'biped R Clavicle',
        'left_hand': 'biped L Hand',
        'right_hand': 'biped R Hand',
        'left_foot': 'biped L Foot',
        'right_foot': 'biped R Foot',
    }
    
    def __init__(self, raw_entity: Any, local_player_pos: Tuple[float, float, float] = None):
        self.raw = raw_entity
        self._local_pos = local_player_pos
        self._bones_cache = {}
        
    @property
    def is_valid(self) -> bool:
        """Check if entity is valid"""
        return self.raw is not None
    
    @property
    def is_alive(self) -> bool:
        """Check if entity is alive"""
        if hasattr(self.raw, 'is_alive'):
            return self.raw.is_alive
        if hasattr(self.raw, 'hp'):
            return self.raw.hp > 0
        return False
    
    @property
    def health(self) -> int:
        """Get entity health"""
        if hasattr(self.raw, 'hp'):
            return self.raw.hp
        return 0
    
    @property
    def max_health(self) -> int:
        """Get entity max health"""
        if hasattr(self.raw, 'max_hp'):
            return self.raw.max_hp
        return 100
    
    @property
    def is_allied(self) -> bool:
        """Check if entity is an ally"""
        if hasattr(self.raw, 'is_allied'):
            return self.raw.is_allied
        if hasattr(self.raw, 'faction'):
            # Check faction against local player
            return False
        return False
    
    @property
    def position(self) -> Tuple[float, float, float]:
        """Get entity world position"""
        if hasattr(self.raw, 'pos'):
            pos = self.raw.pos
            return (pos.x, pos.y, pos.z)
        if hasattr(self.raw, 'position'):
            pos = self.raw.position
            return (pos.x, pos.y, pos.z)
        return (0, 0, 0)
    
    @property
    def name(self) -> str:
        """Get entity name"""
        if hasattr(self.raw, 'name'):
            return self.raw.name
        if hasattr(self.raw, 'entity_name'):
            return self.raw.entity_name
        return "Unknown"
    
    @property
    def team_id(self) -> int:
        """Get entity team ID"""
        if hasattr(self.raw, 'team_id'):
            return self.raw.team_id
        if hasattr(self.raw, 'faction'):
            return self.raw.faction
        return -1
    
    def get_bone_position(self, bone_name: str) -> Optional[Tuple[float, float, float]]:
        """Get world position of a specific bone"""
        if bone_name in self._bones_cache:
            return self._bones_cache[bone_name]
        
        if hasattr(self.raw, 'model'):
            model = self.raw.model
            if hasattr(model, 'GetBoneWorldPosition'):
                try:
                    bone_key = self.BONE_NAMES.get(bone_name, bone_name)
                    pos = model.GetBoneWorldPosition(bone_key)
                    if pos:
                        result = (pos.x, pos.y, pos.z)
                        self._bones_cache[bone_name] = result
                        return result
                except:
                    pass
        return None
    
    def get_screen_position(self, camera: Any) -> Optional[Tuple[float, float]]:
        """Convert entity position to screen coordinates"""
        pos = self.position
        if hasattr(camera, 'GetScreenPointFromWorldPoint'):
            try:
                screen_pos = camera.GetScreenPointFromWorldPoint(pos)
                if screen_pos:
                    return (screen_pos.x, screen_pos.y)
            except:
                pass
        return None
    
    def get_distance(self, from_pos: Tuple[float, float, float] = None) -> float:
        """Calculate distance to entity"""
        pos = self.position
        if from_pos is None:
            from_pos = self._local_pos if self._local_pos else (0, 0, 0)
        
        dx = pos[0] - from_pos[0]
        dy = pos[1] - from_pos[1]
        dz = pos[2] - from_pos[2]
        return (dx*dx + dy*dy + dz*dz) ** 0.5


class EntityManager:
    """
    Manages all entities in the game world.
    Provides filtering, sorting, and target selection functionality.
    """
    
    def __init__(self, sdk):
        self.sdk = sdk
        self.entities: List[Entity] = []
        self.local_entity: Optional[Entity] = None
        self.last_update = 0
        self.update_interval = 0.016  # ~60 FPS
        
    def update(self, force: bool = False) -> None:
        """Update entity list from game"""
        current_time = time.time()
        
        if not force and (current_time - self.last_update) < self.update_interval:
            return
        
        self.last_update = current_time
        self.entities.clear()
        
        if not self.sdk.initialized or not self.sdk.space:
            return
        
        try:
            # Get local player position for distance calculations
            local_pos = self.sdk.get_camera_position()
            
            # Get all entities from Space
            if hasattr(self.sdk.space, 'entities'):
                for raw_ent in self.sdk.space.entities:
                    if raw_ent:
                        entity = Entity(raw_ent, local_pos)
                        if entity.is_valid:
                            self.entities.append(entity)
            
            # Set local entity
            local_player = self.sdk.get_local_player()
            if local_player:
                self.local_entity = Entity(local_player, local_pos)
                
        except Exception as e:
            print(f"[EntityManager] Update failed: {e}")
    
    def get_players(self, alive_only: bool = True, exclude_allies: bool = True) -> List[Entity]:
        """Get all player entities"""
        players = []
        for entity in self.entities:
            if entity.is_alive or not alive_only:
                if not exclude_allies or not entity.is_allied:
                    players.append(entity)
        return players
    
    def get_closest_player(self, max_distance: float = float('inf'), 
                           fov: float = None, camera_angle: Tuple[float, float] = None) -> Optional[Entity]:
        """Get the closest player entity"""
        closest = None
        closest_dist = max_distance
        
        for entity in self.get_players(alive_only=True, exclude_allies=True):
            dist = entity.get_distance()
            
            # Check FOV if specified
            if fov is not None and camera_angle is not None:
                # Would need angle calculation here
                pass
            
            if dist < closest_dist:
                closest = entity
                closest_dist = dist
        
        return closest
    
    def get_best_target(self, preference: str = 'distance', 
                        max_distance: float = float('inf'),
                        min_health: int = 0,
                        max_health: int = 100) -> Optional[Entity]:
        """
        Get the best target based on preference.
        
        Args:
            preference: 'distance', 'health', 'fov'
            max_distance: Maximum distance to consider
            min_health: Minimum health threshold
            max_health: Maximum health threshold
        """
        candidates = []
        
        for entity in self.get_players(alive_only=True, exclude_allies=True):
            if entity.health < min_health or entity.health > max_health:
                continue
            
            dist = entity.get_distance()
            if dist > max_distance:
                continue
            
            candidates.append((entity, dist, entity.health))
        
        if not candidates:
            return None
        
        if preference == 'distance':
            candidates.sort(key=lambda x: x[1])
        elif preference == 'health':
            candidates.sort(key=lambda x: x[2])
        elif preference == 'fov':
            # Would need FOV calculation
            candidates.sort(key=lambda x: x[1])
        
        return candidates[0][0]
    
    def get_entities_in_radius(self, center: Tuple[float, float, float], 
                                radius: float) -> List[Entity]:
        """Get all entities within a radius of a point"""
        result = []
        for entity in self.entities:
            dist = entity.get_distance(center)
            if dist <= radius:
                result.append(entity)
        return result
    
    def get_entity_by_name(self, name: str) -> Optional[Entity]:
        """Find entity by name"""
        for entity in self.entities:
            if entity.name.lower() == name.lower():
                return entity
        return None
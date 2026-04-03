"""
Real ESP - Using Actual BloodStrike Game Data
Connects to the real game SDK for authentic player information
"""

import sys
import os
from typing import List, Optional, Tuple, Dict, Any
from dataclasses import dataclass

# Add the core path to import our real SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

@dataclass
class PlayerESPData:
    """Data structure for ESP player information"""
    entity: Any
    name: str
    health: int
    max_health: int
    position: Tuple[float, float, float]
    screen_position: Optional[Tuple[float, float]]
    is_enemy: bool
    is_local_player: bool
    distance: float
    team_id: Optional[int] = None
    box_min: Optional[Tuple[float, float]] = None
    box_max: Optional[Tuple[float, float]] = None
    skeleton_bones: Optional[List[Tuple[Tuple[float, float], Tuple[float, float]]]] = None

class RealESP:
    """
    Real ESP system that uses BloodStrike's actual game data
    """
    
    def __init__(self, sdk, config):
        self.sdk = sdk
        self.config = config
        self.esp_data: List[PlayerESPData] = []
        self.enabled = False
        
    def update(self):
        """Update ESP data from real game entities"""
        if not self.enabled or not self.sdk.initialized:
            self.esp_data = []
            return
            
        try:
            # Update entity list
            self.sdk.update()
            
            # Get all entities from the real SDK
            entities = self.sdk.get_entities()
            local_player = self.sdk.get_local_player()
            
            self.esp_data = []
            
            for entity in entities:
                # Get entity data from real SDK
                entity_data = self.sdk.get_entity_data(entity)
                if not entity_data:
                    continue
                    
                # Skip if this is the local player (unless configured to show)
                if entity_data['is_local_player'] and not getattr(self.config.esp, 'show_local_player', False):
                    continue
                    
                # Convert world position to screen position
                screen_pos = self.sdk.world_to_screen(entity_data['position'])
                
                # Create ESP data
                esp_data = PlayerESPData(
                    entity=entity_data['entity'],
                    name=entity_data['name'],
                    health=entity_data['hp'],
                    max_health=entity_data['max_hp'],
                    position=entity_data['position'],
                    screen_position=screen_pos,
                    is_enemy=entity_data['is_enemy'],
                    is_local_player=entity_data['is_local_player'],
                    distance=entity_data['distance']
                )
                
                # Calculate 2D box if we have screen position
                if screen_pos and getattr(self.config.esp, 'show_box', True):
                    esp_data.box_min, esp_data.box_max = self._calculate_2d_box(esp_data)
                
                # Get skeleton bones if enabled
                if screen_pos and getattr(self.config.esp, 'show_skeleton', True):
                    esp_data.skeleton_bones = self._get_skeleton_bones(entity)
                
                self.esp_data.append(esp_data)
                
            # Sort by distance (closest first)
            self.esp_data.sort(key=lambda x: x.distance)
            
        except Exception as e:
            print(f"[RealESP] Update error: {e}")
            self.esp_data = []
    
    def _calculate_2d_box(self, player_data: PlayerESPData) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """
        Calculate 2D bounding box for player
        """
        try:
            if not player_data.screen_position:
                return None, None
                
            screen_x, screen_y = player_data.screen_position
            
            # Estimate box size based on distance
            # Closer players = bigger boxes
            distance_factor = max(0.5, min(2.0, 100.0 / max(player_data.distance, 1.0)))
            
            box_width = 40 * distance_factor
            box_height = 80 * distance_factor
            
            box_min = (screen_x - box_width/2, screen_y - box_height/2)
            box_max = (screen_x + box_width/2, screen_y + box_height/2)
            
            return box_min, box_max
            
        except Exception as e:
            print(f"[RealESP] Box calculation error: {e}")
            return None, None
    
    def _get_skeleton_bones(self, entity) -> Optional[List[Tuple[Tuple[float, float], Tuple[float, float]]]]:
        """
        Get skeleton bones for ESP skeleton rendering
        """
        try:
            bones = []
            
            # Bone connections (based on BloodStrike SDK bone names)
            bone_connections = [
                ('biped Head', 'biped Neck'),
                ('biped Neck', 'biped Spine1'),
                ('biped Spine1', 'biped Spine'),
                ('biped Spine', 'HP_Pelvis'),
                ('HP_Pelvis', 'biped L Foot'),
                ('HP_Pelvis', 'biped R Foot'),
                ('biped Spine1', 'biped L Hand'),
                ('biped Spine1', 'biped R Hand'),
            ]
            
            # Try to get bone positions from the entity
            for bone_start, bone_end in bone_connections:
                if hasattr(entity, 'GetBoneWorldPosition'):
                    try:
                        start_pos = entity.GetBoneWorldPosition(bone_start)
                        end_pos = entity.GetBoneWorldPosition(bone_end)
                        
                        if start_pos and end_pos:
                            # Convert to screen coordinates
                            start_screen = self.sdk.world_to_screen(start_pos)
                            end_screen = self.sdk.world_to_screen(end_pos)
                            
                            if start_screen and end_screen:
                                bones.append((start_screen, end_screen))
                    except:
                        continue
            
            return bones if bones else None
            
        except Exception as e:
            print(f"[RealESP] Skeleton error: {e}")
            return None
    
    def get_esp_data(self) -> List[PlayerESPData]:
        """Get current ESP data"""
        return self.esp_data
    
    def toggle(self):
        """Toggle ESP on/off"""
        self.enabled = not self.enabled
        print(f"[RealESP] {'Enabled' if self.enabled else 'Disabled'}")
        return self.enabled
    
    def is_enabled(self) -> bool:
        """Check if ESP is enabled"""
        return self.enabled
    
    def get_player_count(self) -> int:
        """Get number of players detected"""
        return len(self.esp_data)
    
    def get_enemy_count(self) -> int:
        """Get number of enemies detected"""
        return sum(1 for player in self.esp_data if player.is_enemy)
    
    def get_team_count(self) -> int:
        """Get number of teammates detected"""
        return sum(1 for player in self.esp_data if not player.is_enemy and not player.is_local_player)

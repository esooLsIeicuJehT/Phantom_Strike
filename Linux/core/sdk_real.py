"""
BloodStrike Real SDK - Using Actual Game Classes
Connects to the real BloodStrike Python SDK for authentic data
"""

import sys
import os
from typing import Optional, List, Dict, Any, Tuple

# Add the game SDK path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'SDK'))

class BloodStrikeRealSDK:
    """
    Real SDK that uses BloodStrike's actual game classes
    This should be injected into the game's Python interpreter
    """
    
    _instance = None
    
    def __init__(self):
        self.space = None
        self.local_player = None
        self.entities = []
        self.initialized = False
        
    @classmethod
    def get_instance(cls):
        """Get singleton instance of the SDK"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def initialize(self) -> bool:
        """
        Initialize the SDK by connecting to BloodStrike's actual Python classes
        """
        try:
            # Import the real game classes
            from gclient.framework.entities.space import Space
            from gclient.gameplay.logic_base.entities.combat_avatar import CombatAvatar
            from gclient.gameplay.logic_base.entities.combat_avatar import PlayerCombatAvatar
            
            print("[RealSDK] Successfully imported BloodStrike game classes")
            
            # Get the current space instance
            if hasattr(Space, '_instance') and Space._instance:
                self.space = Space._instance
                print("[RealSDK] Found game space instance")
                
                # Find all CombatAvatar entities in the space
                self._find_entities()
                self.initialized = True
                return True
            else:
                print("[RealSDK] No active game space found")
                return False
                
        except ImportError as e:
            print(f"[RealSDK] Failed to import game classes: {e}")
            print("[RealSDK] Make sure this is running inside BloodStrike's Python interpreter")
            return False
        except Exception as e:
            print(f"[RealSDK] Initialization failed: {e}")
            return False
    
    def _find_entities(self):
        """Find all CombatAvatar entities in the current space"""
        try:
            if self.space and hasattr(self.space, 'entities'):
                self.entities = []
                
                # Iterate through all entities in the space
                for entity in self.space.entities.values():
                    # Check if it's a CombatAvatar (player)
                    if (hasattr(entity, 'IsCombatAvatar') and entity.IsCombatAvatar and
                        hasattr(entity, 'hp') and hasattr(entity, 'position')):
                        self.entities.append(entity)
                        
                        # Check if this is the local player
                        if hasattr(entity, 'IsAvatar') and entity.IsAvatar:
                            self.local_player = entity
                            print(f"[RealSDK] Found local player with HP: {entity.hp}")
                
                print(f"[RealSDK] Found {len(self.entities)} CombatAvatar entities")
                
        except Exception as e:
            print(f"[RealSDK] Error finding entities: {e}")
    
    def get_local_player(self):
        """Get the local player entity"""
        return self.local_player
    
    def get_entities(self):
        """Get all CombatAvatar entities"""
        return self.entities
    
    def get_entity_data(self, entity) -> Optional[Dict[str, Any]]:
        """
        Extract relevant data from a CombatAvatar entity
        """
        try:
            if not entity or not hasattr(entity, 'hp'):
                return None
                
            data = {
                'entity': entity,
                'hp': getattr(entity, 'hp', 0),
                'max_hp': getattr(entity, 'cur_maxhp', 100),
                'position': getattr(entity, 'position', (0, 0, 0)),
                'is_local_player': getattr(entity, 'IsAvatar', False),
                'is_enemy': False,  # Will be determined later
                'name': 'Unknown',
                'distance': 0
            }
            
            # Calculate distance from local player
            if self.local_player and entity != self.local_player:
                try:
                    local_pos = getattr(self.local_player, 'position', (0, 0, 0))
                    entity_pos = data['position']
                    
                    # Calculate 3D distance
                    dx = entity_pos[0] - local_pos[0]
                    dy = entity_pos[1] - local_pos[1] 
                    dz = entity_pos[2] - local_pos[2]
                    data['distance'] = (dx*dx + dy*dy + dz*dz) ** 0.5
                    
                except Exception as e:
                    print(f"[RealSDK] Error calculating distance: {e}")
            
            # Try to get team information
            if hasattr(entity, 'team_id'):
                data['team_id'] = entity.team_id
                if self.local_player and hasattr(self.local_player, 'team_id'):
                    data['is_enemy'] = entity.team_id != self.local_player.team_id
            
            return data
            
        except Exception as e:
            print(f"[RealSDK] Error extracting entity data: {e}")
            return None
    
    def world_to_screen(self, world_pos: Tuple[float, float, float]) -> Optional[Tuple[float, float]]:
        """
        Convert world coordinates to screen coordinates
        """
        try:
            if self.space and hasattr(self.space, 'camera'):
                camera = self.space.camera
                if hasattr(camera, 'GetScreenPointFromWorldPoint'):
                    screen_point = camera.GetScreenPointFromWorldPoint(world_pos)
                    if screen_point:
                        return (screen_point[0], screen_point[1])
            return None
        except Exception as e:
            print(f"[RealSDK] Error converting world to screen: {e}")
            return None
    
    def update(self):
        """Update entity list and data"""
        if self.initialized:
            self._find_entities()
    
    def cleanup(self):
        """Cleanup resources"""
        self.space = None
        self.local_player = None
        self.entities = []
        self.initialized = False

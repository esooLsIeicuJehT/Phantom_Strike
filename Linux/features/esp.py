"""
BloodStrike ESP Module
Implements visual overlays for entity information

Supports two modes:
1. Internal: Using BloodStrike's built-in rendering
2. External: Via IPC to an external overlay window
"""

import math
import json
import socket
import threading
import time
from typing import Optional, Tuple, List, Dict, Any
from dataclasses import dataclass
from enum import Enum


class ESPMode(Enum):
    INTERNAL = "internal"      # Render within game
    EXTERNAL_SOCKET = "socket" # Send data to external overlay via UDP
    EXTERNAL_FILE = "file"     # Write data to file for external reading


@dataclass
class ESPSettings:
    """ESP configuration settings"""
    enabled: bool = False
    mode: ESPMode = ESPMode.EXTERNAL_SOCKET
    
    # Player ESP
    player_boxes: bool = True
    player_skeleton: bool = True
    player_health: bool = True
    player_name: bool = True
    player_distance: bool = True
    player_weapon: bool = True
    player_snaplines: bool = False
    
    # Visual settings
    box_color_enemy: Tuple[int, int, int, int] = (255, 0, 0, 255)     # Red
    box_color_allied: Tuple[int, int, int, int] = (0, 255, 0, 255)    # Green
    box_color_visible: Tuple[int, int, int, int] = (255, 255, 0, 255) # Yellow
    skeleton_color: Tuple[int, int, int, int] = (255, 255, 255, 200)  # White
    health_bar_bg: Tuple[int, int, int, int] = (0, 0, 0, 180)
    health_bar_fg: Tuple[int, int, int, int] = (0, 255, 0, 255)
    
    # Filter settings
    max_distance: float = 500.0
    show_allies: bool = False
    show_dead: bool = False
    
    # Socket settings
    socket_host: str = "127.0.0.1"
    socket_port: int = 5555
    
    # File settings
    data_file: str = "/tmp/bloodstrike_esp_data.json"


@dataclass
class PlayerESPData:
    """ESP data for a single player"""
    id: int
    name: str
    team: int
    is_allied: bool
    is_alive: bool
    
    # Screen positions
    screen_pos: Tuple[float, float]       # Feet position
    head_pos: Tuple[float, float]         # Head screen position
    box_min: Tuple[float, float]          # Box top-left
    box_max: Tuple[float, float]          # Box bottom-right
    
    # Info
    health: int
    max_health: int
    distance: float
    weapon: str
    
    # Skeleton (list of line pairs)
    skeleton_bones: List[Tuple[Tuple[float, float], Tuple[float, float]]]


class ESP:
    """
    ESP implementation for BloodStrike.
    Collects entity data and sends it to renderer.
    """
    
    # Bone connections for skeleton ESP
    SKELETON_CONNECTIONS = [
        ('biped Head', 'biped Neck'),
        ('biped Neck', 'biped Spine1'),
        ('biped Spine1', 'biped Spine'),
        ('biped Spine', 'biped L Clavicle'),
        ('biped Spine', 'biped R Clavicle'),
        ('biped L Clavicle', 'biped L Hand'),
        ('biped R Clavicle', 'biped R Hand'),
        ('biped Spine', 'biped L Thigh'),
        ('biped Spine', 'biped R Thigh'),
        ('biped L Thigh', 'biped L Foot'),
        ('biped R Thigh', 'biped R Foot'),
    ]
    
    def __init__(self, sdk, entity_manager):
        self.sdk = sdk
        self.entity_manager = entity_manager
        self.settings = ESPSettings()
        
        # State
        self.esp_data: List[PlayerESPData] = []
        self.player_id_counter = 0
        
        # IPC
        self.socket = None
        self.file_handle = None
        self._running = False
    
    def start(self) -> bool:
        """Start the ESP system"""
        if self.settings.mode == ESPMode.EXTERNAL_SOCKET:
            return self._init_socket()
        elif self.settings.mode == ESPMode.EXTERNAL_FILE:
            return self._init_file()
        return True
    
    def stop(self) -> None:
        """Stop the ESP system"""
        self._running = False
        if self.socket:
            self.socket.close()
            self.socket = None
        if self.file_handle:
            self.file_handle.close()
            self.file_handle = None
    
    def _init_socket(self) -> bool:
        """Initialize UDP socket for IPC"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self._running = True
            return True
        except Exception as e:
            print(f"[ESP] Socket init failed: {e}")
            return False
    
    def _init_file(self) -> bool:
        """Initialize file for IPC"""
        try:
            self.file_handle = open(self.settings.data_file, 'w')
            self._running = True
            return True
        except Exception as e:
            print(f"[ESP] File init failed: {e}")
            return False
    
    def update(self) -> None:
        """Main update function - call every frame"""
        if not self.settings.enabled:
            return
        
        # Update entity manager
        self.entity_manager.update()
        
        # Collect ESP data
        self.esp_data.clear()
        
        local_pos = self.sdk.get_camera_position()
        if not local_pos:
            return
        
        for entity in self.entity_manager.entities:
            # Apply filters
            if not entity.is_alive and not self.settings.show_dead:
                continue
            if entity.is_allied and not self.settings.show_allies:
                continue
            
            distance = entity.get_distance(local_pos)
            if distance > self.settings.max_distance:
                continue
            
            # Get ESP data for this entity
            data = self._get_player_esp_data(entity, local_pos)
            if data:
                self.esp_data.append(data)
        
        # Send data via IPC
        self._send_data()
    
    def _get_player_esp_data(self, entity: Any, local_pos: Tuple[float, float, float]) -> Optional[PlayerESPData]:
        """Collect ESP data for a single player"""
        # Get screen position
        feet_screen = self.sdk.world_to_screen(entity.position)
        if not feet_screen:
            return None
        
        # Get head position
        head_world = entity.get_bone_position('head')
        head_screen = self.sdk.world_to_screen(head_world) if head_world else None
        
        if not head_screen:
            head_screen = feet_screen
        
        # Calculate bounding box
        height = abs(feet_screen[1] - head_screen[1])
        width = height * 0.4  # Approximate width based on height
        
        box_min = (head_screen[0] - width/2, head_screen[1])
        box_max = (head_screen[0] + width/2, feet_screen[1])
        
        # Get skeleton bones
        skeleton = self._get_skeleton_bones(entity)
        
        # Get weapon name
        weapon = "Unknown"
        if hasattr(entity.raw, 'weapon'):
            weapon = getattr(entity.raw.weapon, 'name', 'Unknown')
        
        return PlayerESPData(
            id=self.player_id_counter,
            name=entity.name,
            team=entity.team_id,
            is_allied=entity.is_allied,
            is_alive=entity.is_alive,
            screen_pos=feet_screen,
            head_pos=head_screen,
            box_min=box_min,
            box_max=box_max,
            health=entity.health,
            max_health=entity.max_health,
            distance=entity.get_distance(local_pos),
            weapon=weapon,
            skeleton_bones=skeleton
        )
    
    def _get_skeleton_bones(self, entity: Any) -> List[Tuple[Tuple[float, float], Tuple[float, float]]]:
        """Get skeleton bone lines for ESP"""
        bones = []
        
        for bone1_name, bone2_name in self.SKELETON_CONNECTIONS:
            pos1_world = entity.get_bone_position(bone1_name.replace('biped ', '').lower())
            pos2_world = entity.get_bone_position(bone2_name.replace('biped ', '').lower())
            
            if pos1_world and pos2_world:
                pos1_screen = self.sdk.world_to_screen(pos1_world)
                pos2_screen = self.sdk.world_to_screen(pos2_world)
                
                if pos1_screen and pos2_screen:
                    bones.append((pos1_screen, pos2_screen))
        
        return bones
    
    def _send_data(self) -> None:
        """Send ESP data via configured IPC method"""
        if not self._running:
            return
        
        # Serialize data
        data = {
            'timestamp': time.time(),
            'players': [
                {
                    'id': p.id,
                    'name': p.name,
                    'team': p.team,
                    'is_allied': p.is_allied,
                    'is_alive': p.is_alive,
                    'screen_pos': p.screen_pos,
                    'head_pos': p.head_pos,
                    'box_min': p.box_min,
                    'box_max': p.box_max,
                    'health': p.health,
                    'max_health': p.max_health,
                    'distance': p.distance,
                    'weapon': p.weapon,
                    'skeleton': [[list(b[0]), list(b[1])] for b in p.skeleton_bones]
                }
                for p in self.esp_data
            ]
        }
        
        json_data = json.dumps(data)
        
        if self.settings.mode == ESPMode.EXTERNAL_SOCKET and self.socket:
            try:
                self.socket.sendto(json_data.encode(), 
                                  (self.settings.socket_host, self.settings.socket_port))
            except Exception as e:
                print(f"[ESP] Socket send failed: {e}")
        
        elif self.settings.mode == ESPMode.EXTERNAL_FILE and self.file_handle:
            try:
                self.file_handle.seek(0)
                self.file_handle.write(json_data)
                self.file_handle.flush()
            except Exception as e:
                print(f"[ESP] File write failed: {e}")


class ESPRenderer:
    """
    External ESP overlay renderer.
    Receives data via socket/file and renders to a transparent overlay window.
    """
    
    def __init__(self, host: str = "127.0.0.1", port: int = 5555):
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
        
        # Rendering state
        self.esp_data = None
        self.last_update = 0
    
    def start(self) -> bool:
        """Start the ESP renderer"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.bind((self.host, self.port))
            self.socket.settimeout(0.1)
            self.running = True
            return True
        except Exception as e:
            print(f"[ESPRenderer] Start failed: {e}")
            return False
    
    def stop(self) -> None:
        """Stop the ESP renderer"""
        self.running = False
        if self.socket:
            self.socket.close()
    
    def receive_data(self) -> Optional[Dict]:
        """Receive ESP data from the game"""
        if not self.socket:
            return None
        
        try:
            data, addr = self.socket.recvfrom(65536)
            return json.loads(data.decode())
        except socket.timeout:
            return None
        except Exception as e:
            print(f"[ESPRenderer] Receive failed: {e}")
            return None
    
    def render_frame(self) -> None:
        """Render a single frame of ESP"""
        data = self.receive_data()
        if data:
            self.esp_data = data
            self.last_update = time.time()
        
        if not self.esp_data:
            return
        
        # Render would be implemented by GUI overlay
        # This is a placeholder for the rendering logic
        for player in self.esp_data.get('players', []):
            self._render_player(player)
    
    def _render_player(self, player: Dict) -> None:
        """Render ESP for a single player"""
        # Box
        if player.get('box_min') and player.get('box_max'):
            self._draw_box(player['box_min'], player['box_max'], 
                          color=(0, 255, 0, 255) if player['is_allied'] else (255, 0, 0, 255))
        
        # Health bar
        if player.get('health') is not None:
            health_percent = player['health'] / player.get('max_health', 100)
            self._draw_health_bar(player['box_min'], health_percent)
        
        # Name and distance
        if player.get('name'):
            self._draw_text(player['name'], player['head_pos'])
        
        # Skeleton
        for bone in player.get('skeleton', []):
            if len(bone) == 2:
                self._draw_line(tuple(bone[0]), tuple(bone[1]), (255, 255, 255, 200))
    
    # Placeholder rendering methods - would be implemented with actual graphics library
    def _draw_box(self, min_pos, max_pos, color):
        pass
    
    def _draw_health_bar(self, pos, percent):
        pass
    
    def _draw_text(self, text, pos):
        pass
    
    def _draw_line(self, start, end, color):
        pass
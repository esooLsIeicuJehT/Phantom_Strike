#!/usr/bin/env python3
"""
Internal BloodStrike Cheat - Using Real Game SDK
Based on the working internal code provided by the user
"""

import sys
import os
import math
import socket
import json
import time
from typing import Dict, List, Tuple, Any

# Add game SDK path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'SDK'))

try:
    from gclient.framework.entities.space import Space
    from gclient.framework.util.story_tick import StoryTick
    INTERNAL_MODE = True
    print("✅ BloodStrike internal SDK loaded successfully!")
except ImportError as e:
    print(f"❌ Failed to load internal SDK: {e}")
    print("   This script must be injected into BloodStrike's Python interpreter")
    INTERNAL_MODE = False

class BloodStrikeInternalCheat:
    """Main cheat class that runs inside BloodStrike"""
    
    def __init__(self):
        self.enabled = True
        self.aimbot_enabled = False
        self.esp_enabled = False
        self.ai_aimbot_enabled = False
        
        # UDP bridge for ESP
        self.esp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.esp_port = 1337
        
        # Aimbot settings
        self.aimbot_fov = 200
        self.aimbot_smoothness = 0.15
        self.aimbot_target_head = True
        
        # AI aimbot model (placeholder for trained AI)
        self.ai_model = None
        
        # Performance tracking
        self.last_aim_time = 0
        self.aim_cooldown = 0.016  # 60 FPS
        
        if INTERNAL_MODE:
            self.initialize_internal()
    
    def initialize_internal(self):
        """Initialize when running inside BloodStrike"""
        try:
            print("🎯 Initializing BloodStrike Internal Cheat...")
            
            # Add our tick functions to the game loop
            StoryTick._instance.Add(self.cheat_tick, 0.016)  # 60 FPS main loop
            StoryTick._instance.Add(self.esp_tick, 0.016)    # 60 FPS ESP update
            StoryTick._instance.Add(self.aimbot_tick, 0.008) # 120 FPS aimbot
            
            print("✅ Internal cheat initialized successfully!")
            print("🎮 Controls:")
            print("   F1 - Toggle ESP")
            print("   F2 - Toggle Aimbot") 
            print("   F3 - Toggle AI Aimbot")
            print("   F4 - Toggle Menu")
            print("   END - Panic (Disable All)")
            
        except Exception as e:
            print(f"❌ Failed to initialize internal cheat: {e}")
    
    def get_camera(self):
        """Get the game camera"""
        try:
            return Space._instance.camera
        except:
            return None
    
    def get_local_player(self):
        """Get the local player"""
        try:
            return Space._instance.owner
        except:
            return None
    
    def cheat_tick(self, args):
        """Main cheat tick - handle input and state"""
        try:
            # Handle keyboard input (simplified - you'd want proper input handling)
            # This is just a placeholder for input detection
            pass
        except Exception as e:
            print(f"Cheat tick error: {e}")
    
    def esp_tick(self, args):
        """ESP tick - send player data to external overlay via UDP"""
        if not self.esp_enabled or not INTERNAL_MODE:
            return
            
        try:
            cam = self.get_camera()
            me = self.get_local_player()
            
            if not cam or not me:
                return
            
            data = []
            
            for eid, ent in Space._instance.entities.items():
                # Skip self, dead, and allied entities
                if ent == me or not getattr(ent, 'is_alive', True) or getattr(ent, 'is_allied', False):
                    continue
                
                # Get head position
                try:
                    head_pos = ent.model.GetBoneWorldPosition('biped Head')
                except:
                    # Fallback to entity position if no model/bones
                    head_pos = getattr(ent, 'position', (0, 0, 0))
                
                # Convert world to screen coordinates
                try:
                    screen_pos = cam.engine_camera.GetScreenPointFromWorldPoint(head_pos)
                except:
                    continue
                
                # Only send if on screen
                if screen_pos[2] > 0:
                    player_data = {
                        "x": screen_pos[0],
                        "y": screen_pos[1],
                        "hp": getattr(ent, 'hp', 100),
                        "max_hp": getattr(ent, 'cur_maxhp', 100),
                        "name": getattr(ent, 'name', 'Enemy'),
                        "distance": self.calculate_distance(me.position, ent.position) if hasattr(me, 'position') and hasattr(ent, 'position') else 0,
                        "is_enemy": True
                    }
                    data.append(player_data)
            
            # Send data to external overlay
            if data:
                try:
                    json_data = json.dumps(data).encode()
                    self.esp_socket.sendto(json_data, ("127.0.0.1", self.esp_port))
                except:
                    pass  # Silently fail if external overlay isn't running
                    
        except Exception as e:
            print(f"ESP tick error: {e}")
    
    def aimbot_tick(self, args):
        """High-frequency aimbot tick"""
        if not self.aimbot_enabled or not INTERNAL_MODE:
            return
            
        current_time = time.time()
        if current_time - self.last_aim_time < self.aim_cooldown:
            return
            
        self.last_aim_time = current_time
        
        try:
            me = self.get_local_player()
            cam = self.get_camera()
            
            if not me or not cam or not getattr(me, 'is_alive', True):
                return
            
            # Find best target
            best_target = None
            min_dist = 9999
            
            for eid, ent in Space._instance.entities.items():
                if ent == me or not getattr(ent, 'is_alive', True) or getattr(ent, 'is_allied', False):
                    continue
                
                # Get target position (head or body)
                try:
                    if self.aimbot_target_head:
                        target_pos = ent.model.GetBoneWorldPosition('biped Head')
                    else:
                        target_pos = ent.model.GetBoneWorldPosition('biped Spine1')
                except:
                    target_pos = getattr(ent, 'position', (0, 0, 0))
                
                # World to screen
                screen_pos = cam.engine_camera.GetScreenPointFromWorldPoint(target_pos)
                if screen_pos[2] <= 0:  # Behind us
                    continue
                
                # Distance to center of screen
                cx, cy = 960, 540  # 1920x1080 / 2
                dist = math.sqrt((screen_pos[0] - cx)**2 + (screen_pos[1] - cy)**2)
                
                if dist < min_dist and dist < self.aimbot_fov:
                    min_dist = dist
                    best_target = target_pos
            
            if best_target:
                if self.ai_aimbot_enabled and self.ai_model:
                    # Use AI for prediction
                    self.ai_aim_at_target(best_target, cam)
                else:
                    # Traditional aimbot
                    self.aim_at_target(best_target, cam)
                    
        except Exception as e:
            print(f"Aimbot tick error: {e}")
    
    def aim_at_target(self, target_pos, camera):
        """Traditional aimbot - aim directly at target"""
        try:
            # Calculate angles to target
            dx = target_pos[0] - camera.position[0]
            dy = target_pos[1] - camera.position[1] 
            dz = target_pos[2] - camera.position[2]
            
            # Calculate yaw and pitch
            yaw = math.atan2(dy, dx)
            pitch = math.atan2(dz, math.sqrt(dx*dx + dy*dy))
            
            # Convert to degrees and apply smoothing
            yaw_deg = math.degrees(yaw)
            pitch_deg = math.degrees(pitch)
            
            # Apply smoothing (simple linear interpolation)
            current_yaw = getattr(camera, 'yaw', 0)
            current_pitch = getattr(camera, 'pitch', 0)
            
            new_yaw = current_yaw + (yaw_deg - current_yaw) * self.aimbot_smoothness
            new_pitch = current_pitch + (pitch_deg - current_pitch) * self.aimbot_smoothness
            
            # Apply rotation
            camera.placer.Rotate(new_yaw, new_pitch)
            
        except Exception as e:
            print(f"Aim error: {e}")
    
    def ai_aim_at_target(self, target_pos, camera):
        """AI aimbot with prediction"""
        try:
            # Placeholder for AI prediction
            # This would use a trained model to predict movement
            # and calculate optimal aim points
            
            # For now, just use traditional aimbot
            self.aim_at_target(target_pos, camera)
            
        except Exception as e:
            print(f"AI aim error: {e}")
    
    def calculate_distance(self, pos1, pos2):
        """Calculate 3D distance between two positions"""
        try:
            dx = pos1[0] - pos2[0]
            dy = pos1[1] - pos2[1]
            dz = pos1[2] - pos2[2]
            return math.sqrt(dx*dx + dy*dy + dz*dz)
        except:
            return 0
    
    def toggle_esp(self):
        """Toggle ESP on/off"""
        self.esp_enabled = not self.esp_enabled
        print(f"ESP {'ENABLED' if self.esp_enabled else 'DISABLED'}")
    
    def toggle_aimbot(self):
        """Toggle aimbot on/off"""
        self.aimbot_enabled = not self.aimbot_enabled
        print(f"Aimbot {'ENABLED' if self.aimbot_enabled else 'DISABLED'}")
    
    def toggle_ai_aimbot(self):
        """Toggle AI aimbot on/off"""
        self.ai_aimbot_enabled = not self.ai_aimbot_enabled
        print(f"AI Aimbot {'ENABLED' if self.ai_aimbot_enabled else 'DISABLED'}")
    
    def panic(self):
        """Disable all features"""
        self.esp_enabled = False
        self.aimbot_enabled = False
        self.ai_aimbot_enabled = False
        print("🚨 PANIC - All features disabled!")

# Initialize the cheat when this script is injected
if INTERNAL_MODE:
    print("🎯 Starting BloodStrike Internal Cheat...")
    cheat = BloodStrikeInternalCheat()
    print("✅ Cheat is now running in BloodStrike!")
else:
    print("❌ This script must be injected into BloodStrike's Python interpreter")
    print("   Inject this code into the game to enable real ESP and aimbot!")

#!/usr/bin/env python3
"""
Auto-Updating BloodStrike Cheat with Dynamic Offset Management
Automatically scans for offsets, updates itself, and persists data
"""

import sys
import os
import time
import json
from typing import Dict, List, Any, Optional

# Add paths
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'SDK'))
sys.path.insert(0, os.path.dirname(__file__))

try:
    from gclient.framework.entities.space import Space
    from gclient.framework.util.story_tick import StoryTick
    from gclient.gameplay.logic_base.entities.combat_avatar import CombatAvatar
    INTERNAL_MODE = True
except ImportError:
    INTERNAL_MODE = False
    print("⚠ Auto-updating cheat requires internal mode")

from auto_offset_scanner import get_scanner
from dynamic_offset_manager import get_manager, register_cheat_module
from ai_aimbot import get_ai_aimbot
from skin_changer import get_skin_changer

class AutoUpdatingCheat:
    """Main cheat class with automatic offset management"""
    
    def __init__(self):
        self.enabled = True
        self.initialized = False
        
        # Core components
        self.scanner = None
        self.manager = None
        self.ai_aimbot = None
        self.skin_changer = None
        
        # Cheat state
        self.esp_enabled = False
        self.aimbot_enabled = False
        self.skin_changer_enabled = False
        self.auto_update_enabled = True
        
        # Offsets (will be automatically updated)
        self.offsets = {}
        
        # Performance tracking
        self.last_update = time.time()
        self.update_count = 0
        
        if INTERNAL_MODE:
            self.initialize()
    
    def initialize(self):
        """Initialize the auto-updating cheat"""
        try:
            print("🚀 Initializing Auto-Updating BloodStrike Cheat...")
            
            # Initialize core components
            self.scanner = get_scanner()
            self.manager = get_manager()
            self.ai_aimbot = get_ai_aimbot()
            self.skin_changer = get_skin_changer()
            
            # Register this module for dynamic updates
            register_cheat_module("main_cheat", self)
            
            # Register offset callbacks
            self.register_offset_callbacks()
            
            # Load existing offsets
            self.load_offsets()
            
            # Hook into game loop
            self.hook_game_loop()
            
            # Start automatic updates
            if self.auto_update_enabled:
                self.start_auto_updates()
            
            self.initialized = True
            print("✅ Auto-updating cheat initialized successfully!")
            
            # Print current status
            self.print_status()
            
        except Exception as e:
            print(f"❌ Failed to initialize cheat: {e}")
    
    def register_offset_callbacks(self):
        """Register callbacks for offset updates"""
        # Health offset callback
        self.manager.register_offset_callback("health", self.on_health_offset_updated)
        
        # Position offset callback
        self.manager.register_offset_callback("position", self.on_position_offset_updated)
        
        # Camera offset callback
        self.manager.register_offset_callback("camera", self.on_camera_offset_updated)
        
        # Weapon offset callbacks for skin changer
        self.manager.register_offset_callback("weapon_model_id", self.on_weapon_model_updated)
        self.manager.register_offset_callback("weapon_texture_id", self.on_weapon_texture_updated)
        
        # Entity list callback
        self.manager.register_offset_callback("space_entities", self.on_entities_offset_updated)
    
    def on_health_offset_updated(self, new_value):
        """Called when health offset is updated"""
        print(f"💔 Health offset updated: {new_value}")
        self.offsets['health'] = new_value
    
    def on_position_offset_updated(self, new_value):
        """Called when position offset is updated"""
        print(f"📍 Position offset updated: {new_value}")
        self.offsets['position'] = new_value
    
    def on_camera_offset_updated(self, new_value):
        """Called when camera offset is updated"""
        print(f"📷 Camera offset updated: {new_value}")
        self.offsets['camera'] = new_value
    
    def on_weapon_model_updated(self, new_value):
        """Called when weapon model offset is updated"""
        print(f"🔫 Weapon model offset updated: {new_value}")
        self.offsets['weapon_model_id'] = new_value
    
    def on_weapon_texture_updated(self, new_value):
        """Called when weapon texture offset is updated"""
        print(f"🎨 Weapon texture offset updated: {new_value}")
        self.offsets['weapon_texture_id'] = new_value
    
    def on_entities_offset_updated(self, new_value):
        """Called when entities offset is updated"""
        print(f"👥 Entities offset updated: {new_value}")
        self.offsets['entities'] = new_value
    
    def hook_game_loop(self):
        """Hook into the game loop"""
        try:
            # Add main tick function
            StoryTick._instance.Add(self.main_tick, 0.016)  # 60 FPS
            
            # Add offset update tick
            StoryTick._instance.Add(self.offset_update_tick, 1.0)  # 1 FPS
            
            print("🎮 Hooked into game loop")
            
        except Exception as e:
            print(f"⚠ Failed to hook game loop: {e}")
    
    def start_auto_updates(self):
        """Start automatic offset updates"""
        try:
            # The scanner and manager are already running in background
            print("🔄 Auto-updates started")
            
        except Exception as e:
            print(f"⚠ Failed to start auto-updates: {e}")
    
    def main_tick(self, args):
        """Main cheat tick - runs every frame"""
        if not self.enabled or not self.initialized:
            return
        
        try:
            # Update ESP if enabled
            if self.esp_enabled:
                self.update_esp()
            
            # Update aimbot if enabled
            if self.aimbot_enabled:
                self.update_aimbot()
            
        except Exception as e:
            print(f"⚠ Main tick error: {e}")
    
    def offset_update_tick(self, args):
        """Offset update tick - runs every second"""
        if not self.auto_update_enabled:
            return
        
        try:
            # Check for new offsets
            self.check_for_updates()
            
            # Verify current offsets
            self.verify_offsets()
            
        except Exception as e:
            print(f"⚠ Offset update tick error: {e}")
    
    def update_esp(self):
        """Update ESP with current offsets"""
        try:
            space = self.get_space()
            if not space:
                return
            
            # Get entities using current offsets
            entities = self.get_entities(space)
            local_player = self.get_local_player(space)
            
            # Send ESP data to external overlay
            self.send_esp_data(entities, local_player, space)
            
        except Exception as e:
            print(f"⚠ ESP update error: {e}")
    
    def update_aimbot(self):
        """Update aimbot with current offsets"""
        try:
            space = self.get_space()
            if not space:
                return
            
            # Find targets using current offsets
            target = self.find_best_target(space)
            
            if target:
                # Aim at target using AI or traditional method
                if self.ai_aimbot:
                    self.ai_aim_at_target(target, space)
                else:
                    self.aim_at_target(target, space)
            
        except Exception as e:
            print(f"⚠ Aimbot update error: {e}")
    
    def get_space(self):
        """Get space instance using current offsets"""
        try:
            # Use scanner to get space
            space_offset = self.scanner.get_offset("space_instance")
            if space_offset:
                return space_offset
            
            # Fallback to direct access
            return getattr(Space, '_instance', None)
            
        except Exception:
            return None
    
    def get_entities(self, space):
        """Get entities using current offsets"""
        try:
            # Use current entities offset
            if hasattr(space, 'entities'):
                return space.entities
            
            # Use scanner to find entities
            entities_offset = self.scanner.get_offset("space_entities")
            if entities_offset:
                return entities_offset
            
            return {}
            
        except Exception:
            return {}
    
    def get_local_player(self, space):
        """Get local player using current offsets"""
        try:
            # Use direct access
            if hasattr(space, 'owner'):
                return space.owner
            
            # Look through entities for local player
            entities = self.get_entities(space)
            for entity in entities.values():
                if hasattr(entity, 'IsAvatar') and entity.IsAvatar:
                    return entity
            
            return None
            
        except Exception:
            return None
    
    def find_best_target(self, space):
        """Find best aimbot target using current offsets"""
        try:
            local_player = self.get_local_player(space)
            entities = self.get_entities(space)
            camera = self.get_camera(space)
            
            if not local_player or not camera:
                return None
            
            best_target = None
            min_distance = float('inf')
            
            for entity in entities.values():
                if entity == local_player:
                    continue
                
                if not getattr(entity, 'is_alive', True):
                    continue
                
                if getattr(entity, 'is_allied', False):
                    continue
                
                # Get head position using current offsets
                head_pos = self.get_head_position(entity)
                if not head_pos:
                    continue
                
                # Convert to screen coordinates
                screen_pos = self.world_to_screen(head_pos, camera)
                if not screen_pos or screen_pos[2] <= 0:
                    continue
                
                # Calculate distance to center
                cx, cy = 960, 540  # Screen center
                distance = ((screen_pos[0] - cx) ** 2 + (screen_pos[1] - cy) ** 2) ** 0.5
                
                if distance < min_distance and distance < 200:  # FOV limit
                    min_distance = distance
                    best_target = head_pos
            
            return best_target
            
        except Exception as e:
            print(f"⚠ Target finding error: {e}")
            return None
    
    def get_head_position(self, entity):
        """Get head position using current offsets"""
        try:
            # Try to get bone position
            if hasattr(entity, 'model') and hasattr(entity.model, 'GetBoneWorldPosition'):
                return entity.model.GetBoneWorldPosition('biped Head')
            
            # Fallback to entity position
            return getattr(entity, 'position', None)
            
        except Exception:
            return None
    
    def get_camera(self, space):
        """Get camera using current offsets"""
        try:
            # Use scanner to get camera
            camera_offset = self.scanner.get_offset("camera")
            if camera_offset:
                return camera_offset
            
            # Fallback to direct access
            return getattr(space, 'camera', None)
            
        except Exception:
            return None
    
    def world_to_screen(self, world_pos, camera):
        """Convert world to screen using current offsets"""
        try:
            if hasattr(camera, 'engine_camera') and hasattr(camera.engine_camera, 'GetScreenPointFromWorldPoint'):
                return camera.engine_camera.GetScreenPointFromWorldPoint(world_pos)
            return None
        except Exception:
            return None
    
    def aim_at_target(self, target, space):
        """Traditional aimbot"""
        try:
            camera = self.get_camera(space)
            if not camera:
                return
            
            # Calculate aim angles (simplified)
            # This would use proper math in a real implementation
            print(f"🎯 Aiming at target: {target}")
            
        except Exception as e:
            print(f"⚠ Aim error: {e}")
    
    def ai_aim_at_target(self, target, space):
        """AI aimbot with prediction"""
        try:
            # Use AI aimbot for prediction
            if self.ai_aimbot:
                # This would integrate with the AI aimbot
                print(f"🧠 AI aiming at target: {target}")
            
        except Exception as e:
            print(f"⚠ AI aim error: {e}")
    
    def send_esp_data(self, entities, local_player, space):
        """Send ESP data to external overlay"""
        try:
            # This would send UDP data to external overlay
            # For now, just count players
            enemy_count = sum(1 for e in entities.values() 
                            if e != local_player and not getattr(e, 'is_allied', False))
            
            if hasattr(self, 'last_enemy_count') == False or enemy_count != self.last_enemy_count:
                print(f"👥 ESP: {enemy_count} enemies detected")
                self.last_enemy_count = enemy_count
            
        except Exception as e:
            print(f"⚠ ESP data error: {e}")
    
    def check_for_updates(self):
        """Check for offset updates"""
        try:
            # The scanner automatically updates offsets
            # This function can trigger additional checks
            pass
            
        except Exception as e:
            print(f"⚠ Update check error: {e}")
    
    def verify_offsets(self):
        """Verify current offsets"""
        try:
            verification_results = self.scanner.verify_offsets()
            
            # Check if any critical offsets failed
            critical_offsets = ['health', 'position', 'camera', 'space_entities']
            failed_critical = [name for name in critical_offsets 
                             if name in verification_results and not verification_results[name]]
            
            if failed_critical:
                print(f"⚠ Critical offsets failed verification: {failed_critical}")
            
        except Exception as e:
            print(f"⚠ Offset verification error: {e}")
    
    def load_offsets(self):
        """Load offsets from scanner"""
        try:
            for name, offset in self.scanner.found_offsets.items():
                self.offsets[name] = offset.value
            
            print(f"📁 Loaded {len(self.offsets)} offsets")
            
        except Exception as e:
            print(f"⚠ Failed to load offsets: {e}")
    
    def toggle_esp(self):
        """Toggle ESP"""
        self.esp_enabled = not self.esp_enabled
        print(f"👁️  ESP {'ENABLED' if self.esp_enabled else 'DISABLED'}")
    
    def toggle_aimbot(self):
        """Toggle aimbot"""
        self.aimbot_enabled = not self.aimbot_enabled
        print(f"🎯 Aimbot {'ENABLED' if self.aimbot_enabled else 'DISABLED'}")
    
    def toggle_skin_changer(self):
        """Toggle skin changer"""
        self.skin_changer_enabled = not self.skin_changer_enabled
        self.skin_changer.toggle_skin_changer()
        print(f"🎨 Skin Changer {'ENABLED' if self.skin_changer_enabled else 'DISABLED'}")
    
    def toggle_auto_update(self):
        """Toggle auto updates"""
        self.auto_update_enabled = not self.auto_update_enabled
        print(f"🔄 Auto-updates {'ENABLED' if self.auto_update_enabled else 'DISABLED'}")
    
    def force_update(self):
        """Force immediate offset update"""
        try:
            print("🔄 Forcing immediate offset update...")
            success = self.manager.auto_update_cheat()
            print(f"✅ Force update {'successful' if success else 'failed'}")
        except Exception as e:
            print(f"⚠ Force update error: {e}")
    
    def print_status(self):
        """Print current cheat status"""
        print("\n" + "="*60)
        print("🎯 AUTO-UPDATING BLOODSTRIKE CHEAT STATUS")
        print("="*60)
        
        # Basic status
        print(f"📊 Status: {'ENABLED' if self.enabled else 'DISABLED'}")
        print(f"👁️  ESP: {'ON' if self.esp_enabled else 'OFF'}")
        print(f"🎯 Aimbot: {'ON' if self.aimbot_enabled else 'OFF'}")
        print(f"🎨 Skin Changer: {'ON' if self.skin_changer_enabled else 'OFF'}")
        print(f"🔄 Auto-updates: {'ON' if self.auto_update_enabled else 'OFF'}")
        
        # Offset status
        print(f"\n📁 Offsets: {len(self.offsets)} loaded")
        for name in ['health', 'position', 'camera', 'space_entities']:
            if name in self.offsets:
                print(f"   ✅ {name}: Available")
            else:
                print(f"   ❌ {name}: Missing")
        
        # Scanner status
        if self.scanner:
            stats = self.scanner.get_statistics()
            print(f"\n🔍 Scanner: {stats['patterns_found']}/{stats['total_patterns']} patterns")
            print(f"   Success rate: {stats['success_rate']:.1%}")
        
        print("="*60)
    
    def panic(self):
        """Disable all features"""
        self.esp_enabled = False
        self.aimbot_enabled = False
        print("🚨 PANIC - All features disabled!")

# Global cheat instance
cheat = None

def initialize_cheat():
    """Initialize the auto-updating cheat"""
    global cheat
    if cheat is None and INTERNAL_MODE:
        cheat = AutoUpdatingCheat()
        return cheat
    return cheat

def get_cheat():
    """Get cheat instance"""
    return cheat

# Auto-initialize when injected
if INTERNAL_MODE:
    print("🚀 Auto-Updating BloodStrike Cheat injection detected...")
    initialize_cheat()
    print("✅ Cheat is now running with automatic offset management!")
    print("🎮 Controls:")
    print("   F1 - Toggle ESP")
    print("   F2 - Toggle Aimbot")
    print("   F3 - Toggle Auto-updates")
    print("   F4 - Force Update")
    print("   END - Panic")
else:
    print("❌ This script must be injected into BloodStrike's Python interpreter")

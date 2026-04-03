#!/usr/bin/env python3
"""
External BloodStrike Overlay with ImGui
Receives ESP data via UDP and displays with cool GUI
"""

import sys
import os
import json
import socket
import threading
import time
from typing import List, Dict, Any
import math

# ImGui and rendering imports
try:
    import pygame
    import imgui
    from imgui.integrations.pygame import PygameRenderer
    import OpenGL.GL as gl
    GUI_AVAILABLE = True
    print("✅ ImGui and rendering libraries loaded")
except ImportError as e:
    print(f"❌ GUI libraries missing: {e}")
    print("   Install with: pip install pygame PyOpenGL imgui")
    GUI_AVAILABLE = False

class PlayerData:
    """Enhanced player data structure for ESP"""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0  # 3D position
        self.hp = 100
        self.max_hp = 100
        self.armor = 0
        self.name = "Unknown"
        self.distance = 0
        self.is_enemy = True
        self.is_visible = True
        self.aimbot_target = False
        self.weapon = "Unknown"
        self.money = 0
        self.kills = 0
        self.deaths = 0
        self.is_shooting = False
        self.is_reloading = False
        self.is_aiming = False
        self.head_x = 0
        self.head_y = 0
        self.last_update = time.time()
        self.velocity_x = 0
        self.velocity_y = 0
        self.velocity_z = 0

class ExternalOverlay:
    """External overlay with ImGui GUI"""
    
    def __init__(self):
        if not GUI_AVAILABLE:
            print("❌ Cannot initialize overlay - missing GUI libraries")
            return
            
        # UDP receiver
        self.udp_port = 1337
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("127.0.0.1", self.udp_port))
        self.sock.settimeout(0.1)
        
        # Player data
        self.players: List[PlayerData] = []
        self.players_lock = threading.Lock()
        
        # Enhanced overlay settings
        self.width = 1920
        self.height = 1080
        self.show_esp = True
        self.show_menu = True
        self.show_stats = True
        self.show_skeleton = False
        self.show_head_tracer = False
        self.show_distance = True
        self.show_weapon = True
        self.show_health_bar = True
        self.show_armor_bar = True
        self.show_crosshair = False
        self.show_radar = False
        
        # ESP customization
        self.esp_box_color = (255, 0, 0)  # Red for enemies
        self.esp_friend_color = (0, 255, 0)  # Green for friends
        self.esp_text_color = (255, 255, 255)
        self.esp_visible_color = (255, 200, 0)  # Yellow for visible enemies
        self.esp_hidden_color = (255, 0, 0)  # Red for hidden enemies
        self.menu_bg_color = (20, 20, 30, 200)
        
        # ESP settings
        self.max_render_distance = 500
        self.box_thickness = 2
        self.skeleton_thickness = 1
        self.font_size = 14
        self.health_bar_height = 4
        self.armor_bar_height = 3
        
        # Aimbot settings
        self.aimbot_enabled = False
        self.aimbot_fov = 90
        self.aimbot_smooth = 10
        self.aimbot_bone = "head"  # head, chest, stomach
        self.aimbot_key = 2  # Right mouse button
        
        # Performance monitoring
        self.fps = 0
        self.frame_count = 0
        self.last_fps_time = time.time()
        self.render_time = 0
        self.network_latency = 0
        
        # Initialize pygame and ImGui
        self.init_gui()
        
        # Start UDP receiver thread
        self.udp_thread = threading.Thread(target=self.udp_receiver, daemon=True)
        self.udp_thread.start()
        
        print("✅ External overlay initialized")
        print("🎮 Controls:")
        print("   INSERT - Toggle Menu")
        print("   F1     - Toggle ESP")
        print("   F2     - Toggle Stats")
        print("   END    - Exit")
    
    def init_gui(self):
        """Initialize pygame and ImGui"""
        # Initialize pygame
        pygame.init()
        pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption("BloodStrike External Overlay")
        
        # Set window to be transparent and always on top
        # This would need platform-specific code
        
        # Initialize ImGui
        imgui.create_context()
        self.impl = PygameRenderer()
        
        # Set ImGui style
        self.setup_imgui_style()
    
    def setup_imgui_style(self):
        """Setup cool ImGui style"""
        style = imgui.get_style()
        style.window_rounding = 5.0
        style.frame_rounding = 3.0
        style.grab_rounding = 2.0
        style.scrollbar_rounding = 3.0
        
        # Dark theme with cool colors
        imgui.style_colors_dark()
        
        # Custom colors
        style.colors[imgui.IMGUI_COL_WINDOW_BG] = (0.1, 0.1, 0.15, 0.8)
        style.colors[imgui.IMGUI_COL_HEADER] = (0.2, 0.4, 0.8, 1.0)
        style.colors[imgui.IMGUI_COL_BUTTON] = (0.2, 0.6, 0.2, 1.0)
        style.colors[imgui.IMGUI_COL_BUTTON_HOVERED] = (0.3, 0.7, 0.3, 1.0)
        style.colors[imgui.IMGUI_COL_BUTTON_ACTIVE] = (0.1, 0.5, 0.1, 1.0)
    
    def udp_receiver(self):
        """Receive UDP data from internal cheat"""
        while True:
            try:
                data, addr = self.sock.recvfrom(4096)
                players_json = json.loads(data.decode())
                
                with self.players_lock:
                    self.players.clear()
                    for player_data in players_json:
                        player = PlayerData()
                        player.x = player_data.get('x', 0)
                        player.y = player_data.get('y', 0)
                        player.hp = player_data.get('hp', 100)
                        player.max_hp = player_data.get('max_hp', 100)
                        player.name = player_data.get('name', 'Unknown')
                        player.distance = player_data.get('distance', 0)
                        player.is_enemy = player_data.get('is_enemy', True)
                        player.last_update = time.time()
                        self.players.append(player)
                        
            except socket.timeout:
                continue
            except Exception as e:
                print(f"UDP receive error: {e}")
                continue
    
    def render_esp(self):
        """Enhanced ESP rendering with advanced features"""
        if not self.show_esp:
            return
            
        with self.players_lock:
            # Remove old players (timeout after 5 seconds)
            current_time = time.time()
            self.players = [p for p in self.players if current_time - p.last_update < 5.0]
            
            # Sort players by distance (closest first)
            self.players.sort(key=lambda p: p.distance)
            
            for player in self.players:
                # Skip if beyond render distance
                if player.distance > self.max_render_distance:
                    continue
                    
                # Enhanced box calculations based on distance
                base_width = 40
                base_height = 80
                distance_factor = max(0.5, min(2.0, 100 / max(player.distance, 1)))
                
                box_width = int(base_width * distance_factor)
                box_height = int(base_height * distance_factor)
                
                # Calculate box position
                box_x = int(player.x - box_width // 2)
                box_y = int(player.y - box_height // 2)
                
                # Choose color based on visibility and team
                if player.is_enemy:
                    color = self.esp_visible_color if player.is_visible else self.esp_hidden_color
                else:
                    color = self.esp_friend_color
                
                # Draw main box
                self.draw_rect(box_x, box_y, box_width, box_height, color, self.box_thickness)
                
                # Draw corner boxes (more professional look)
                corner_size = 10
                corner_thickness = 3
                # Top-left corner
                self.draw_rect(box_x, box_y, corner_size, corner_thickness, color, 0)
                self.draw_rect(box_x, box_y, corner_thickness, corner_size, color, 0)
                # Top-right corner
                self.draw_rect(box_x + box_width - corner_size, box_y, corner_size, corner_thickness, color, 0)
                self.draw_rect(box_x + box_width - corner_thickness, box_y, corner_thickness, corner_size, color, 0)
                # Bottom-left corner
                self.draw_rect(box_x, box_y + box_height - corner_thickness, corner_size, corner_thickness, color, 0)
                self.draw_rect(box_x, box_y + box_height - corner_size, corner_thickness, corner_size, color, 0)
                # Bottom-right corner
                self.draw_rect(box_x + box_width - corner_size, box_y + box_height - corner_thickness, corner_size, corner_thickness, color, 0)
                self.draw_rect(box_x + box_width - corner_thickness, box_y + box_height - corner_size, corner_thickness, corner_size, color, 0)
                
                # Draw health bar
                if self.show_health_bar and player.max_hp > 0:
                    health_percent = player.hp / player.max_hp
                    health_bar_height = int(box_height * health_percent)
                    
                    # Background
                    self.draw_rect(box_x - 8, box_y, 6, box_height, (0, 0, 0), 0)
                    
                    # Health bar with gradient colors
                    if health_percent > 0.6:
                        health_color = (0, 255, 0)
                    elif health_percent > 0.3:
                        health_color = (255, 255, 0)
                    else:
                        health_color = (255, 0, 0)
                    
                    self.draw_rect(box_x - 8, box_y + box_height - health_bar_height, 6, health_bar_height, health_color, 0)
                
                # Draw armor bar
                if self.show_armor_bar and player.armor > 0:
                    armor_percent = min(1.0, player.armor / 100)
                    armor_bar_height = int(box_height * armor_percent)
                    
                    # Background
                    self.draw_rect(box_x - 15, box_y, 6, box_height, (0, 0, 0), 0)
                    
                    # Armor bar (blue)
                    self.draw_rect(box_x - 15, box_y + box_height - armor_bar_height, 6, armor_bar_height, (0, 100, 255), 0)
                
                # Draw head dot
                if hasattr(player, 'head_x') and hasattr(player, 'head_y'):
                    head_size = max(3, int(5 * distance_factor))
                    self.draw_rect(int(player.head_x - head_size//2), int(player.head_y - head_size//2), head_size, head_size, (255, 0, 0), 0)
                
                # Draw skeleton lines
                if self.show_skeleton:
                    self.draw_skeleton(player, distance_factor)
                
                # Draw head tracer line
                if self.show_head_tracer and hasattr(player, 'head_x'):
                    self.draw_head_tracer(player)
                
                # Draw text information
                text_y = box_y - 20
                
                # Player name
                name_color = color if player.is_enemy else (0, 255, 0)
                self.draw_text(box_x, text_y, player.name, name_color)
                text_y -= 15
                
                # Distance
                if self.show_distance:
                    self.draw_text(box_x, text_y, f"[{int(player.distance)}m]", self.esp_text_color)
                    text_y -= 15
                
                # Weapon
                if self.show_weapon and player.weapon != "Unknown":
                    self.draw_text(box_x, text_y, player.weapon, (255, 200, 0))
                    text_y -= 15
                
                # Health info
                health_text = f"HP:{player.hp}"
                if player.armor > 0:
                    health_text += f" AR:{player.armor}"
                self.draw_text(box_x, text_y, health_text, (255, 255, 255))
                
                # Status indicators
                status_x = box_x + box_width + 5
                if player.is_shooting:
                    self.draw_text(status_x, box_y, "🔥", (255, 100, 0))
                    box_y += 15
                if player.is_reloading:
                    self.draw_text(status_x, box_y, "🔄", (255, 255, 0))
                    box_y += 15
                if player.is_aiming:
                    self.draw_text(status_x, box_y, "🎯", (0, 255, 0))
    
    def draw_menu(self):
        """Enhanced ImGui menu with comprehensive controls"""
        if not self.show_menu:
            return
            
        imgui.new_frame()
        
        # Main menu window
        imgui.set_next_window_size(350, 600, imgui.FIRST_USE_EVER)
        imgui.set_next_window_position(50, 50, imgui.FIRST_USE_EVER)
        
        expanded, opened = imgui.begin("🎯 BloodStrike External Cheat", True)
        
        if expanded:
            # Status section
            imgui.text("🔥 STATUS")
            imgui.text("Status: CONNECTED")
            imgui.text(f"FPS: {self.fps:.1f}")
            imgui.text(f"Render Time: {self.render_time:.2f}ms")
            imgui.separator()
            
            # Player statistics
            with self.players_lock:
                enemy_count = sum(1 for p in self.players if p.is_enemy)
                visible_count = sum(1 for p in self.players if p.is_visible)
                imgui.text("📊 PLAYER STATS")
                imgui.text(f"Total Players: {len(self.players)}")
                imgui.text(f"Enemies: {enemy_count}")
                imgui.text(f"Visible: {visible_count}")
            
            imgui.separator()
            
            # Main toggles
            imgui.text("⚙️ MAIN CONTROLS")
            
            if imgui.button("Toggle ESP [F1]"):
                self.show_esp = not self.show_esp
            
            imgui.same_line()
            if imgui.button("Toggle Menu [INSERT]"):
                self.show_menu = not self.show_menu
            
            if imgui.button("Toggle Stats [F2]"):
                self.show_stats = not self.show_stats
            
            imgui.same_line()
            if imgui.button("Exit [END]"):
                return False
            
            imgui.separator()
            
            # ESP Features
            imgui.text("👁️ ESP FEATURES")
            
            # ESP toggles
            changed, self.show_health_bar = imgui.checkbox("Health Bars", self.show_health_bar)
            changed, self.show_armor_bar = imgui.checkbox("Armor Bars", self.show_armor_bar)
            changed, self.show_distance = imgui.checkbox("Distance", self.show_distance)
            changed, self.show_weapon = imgui.checkbox("Weapon Info", self.show_weapon)
            changed, self.show_skeleton = imgui.checkbox("Skeleton", self.show_skeleton)
            changed, self.show_head_tracer = imgui.checkbox("Head Tracers", self.show_head_tracer)
            changed, self.show_crosshair = imgui.checkbox("Custom Crosshair", self.show_crosshair)
            changed, self.show_radar = imgui.checkbox("Radar", self.show_radar)
            
            imgui.separator()
            
            # ESP Settings
            imgui.text("🎨 ESP SETTINGS")
            
            # Render distance
            changed, self.max_render_distance = imgui.slider_int("Render Distance", self.max_render_distance, 100, 1000)
            
            # Box thickness
            changed, self.box_thickness = imgui.slider_int("Box Thickness", self.box_thickness, 1, 5)
            
            # Font size
            changed, self.font_size = imgui.slider_int("Font Size", self.font_size, 10, 20)
            
            # Color settings
            imgui.text("Colors:")
            
            changed, color = imgui.color_edit3("Enemy Visible", self.esp_visible_color)
            if changed:
                self.esp_visible_color = color
            
            changed, color = imgui.color_edit3("Enemy Hidden", self.esp_hidden_color)
            if changed:
                self.esp_hidden_color = color
            
            changed, color = imgui.color_edit3("Friend", self.esp_friend_color)
            if changed:
                self.esp_friend_color = color
            
            imgui.separator()
            
            # Aimbot settings
            imgui.text("🎯 AIMBOT")
            
            changed, self.aimbot_enabled = imgui.checkbox("Enable Aimbot", self.aimbot_enabled)
            
            if self.aimbot_enabled:
                changed, self.aimbot_fov = imgui.slider_float("Aimbot FOV", self.aimbot_fov, 10, 180)
                changed, self.aimbot_smooth = imgui.slider_float("Smoothness", self.aimbot_smooth, 1, 20)
                
                # Bone selection
                bones = ["head", "chest", "stomach"]
                current_bone_index = bones.index(self.aimbot_bone) if self.aimbot_bone in bones else 0
                changed, new_index = imgui.combo("Target Bone", current_bone_index, bones)
                if changed:
                    self.aimbot_bone = bones[new_index]
            
            imgui.separator()
            
            # Performance settings
            imgui.text("⚡ PERFORMANCE")
            imgui.text(f"Network Latency: {self.network_latency:.1f}ms")
            imgui.text(f"Active Players: {len(self.players)}")
            
            # Optimization toggles
            if imgui.button("Clear Old Players"):
                with self.players_lock:
                    current_time = time.time()
                    self.players = [p for p in self.players if current_time - p.last_update < 1.0]
            
            imgui.separator()
            
            # Player list (detailed)
            if len(self.players) > 0:
                imgui.text("👥 PLAYER LIST")
                
                with self.players_lock:
                    for i, player in enumerate(self.players[:8]):  # Show max 8 players
                        # Player header with color
                        if player.is_enemy:
                            color = (1.0, 0.2, 0.2, 1.0) if player.is_visible else (0.5, 0.1, 0.1, 1.0)
                        else:
                            color = (0.2, 1.0, 0.2, 1.0)
                        
                        imgui.text_colored(*color, f"{player.name}")
                        
                        # Player details
                        imgui.text(f"  Distance: {int(player.distance)}m")
                        imgui.text(f"  Health: {player.hp}/{player.max_hp}")
                        if player.armor > 0:
                            imgui.text(f"  Armor: {player.armor}")
                        if player.weapon != "Unknown":
                            imgui.text(f"  Weapon: {player.weapon}")
                        
                        # Status indicators
                        status_text = ""
                        if player.is_shooting:
                            status_text += "🔥 "
                        if player.is_reloading:
                            status_text += "🔄 "
                        if player.is_aiming:
                            status_text += "🎯 "
                        if status_text:
                            imgui.text(f"  Status: {status_text}")
                        
                        # Health bar
                        if player.max_hp > 0:
                            imgui.progress_bar(player.hp / player.max_hp, -1, 8)
                        
                        if i < min(7, len(self.players) - 1):
                            imgui.separator()
        
        imgui.end()
        
        # Enhanced stats window
        if self.show_stats:
            imgui.set_next_window_size(300, 250, imgui.FIRST_USE_EVER)
            imgui.set_next_window_position(self.width - 350, 50, imgui.FIRST_USE_EVER)
            
            expanded, opened = imgui.begin("📊 Performance Stats", True)
            
            if expanded:
                imgui.text("🔧 SYSTEM PERFORMANCE")
                imgui.text(f"FPS: {self.fps:.1f}")
                imgui.text(f"Render Time: {self.render_time:.2f}ms")
                imgui.text(f"Network Latency: {self.network_latency:.1f}ms")
                
                imgui.separator()
                
                imgui.text("📡 NETWORK STATUS")
                imgui.text(f"UDP Port: {self.udp_port}")
                imgui.text("Status: Connected")
                imgui.text("Protocol: UDP")
                
                imgui.separator()
                
                imgui.text("👥 TRACKING")
                with self.players_lock:
                    imgui.text(f"Players Tracked: {len(self.players)}")
                    enemy_count = sum(1 for p in self.players if p.is_enemy)
                    visible_count = sum(1 for p in self.players if p.is_visible)
                    imgui.text(f"Enemies: {enemy_count}")
                    imgui.text(f"Visible: {visible_count}")
                
                imgui.separator()
                
                imgui.text("⚙️ SETTINGS")
                imgui.text(f"Render Distance: {self.max_render_distance}m")
                imgui.text(f"ESP Enabled: {'Yes' if self.show_esp else 'No'}")
                imgui.text(f"Aimbot Enabled: {'Yes' if self.aimbot_enabled else 'No'}")
                
            imgui.end()
        
        imgui.render()
        self.impl.render(imgui.get_draw_data())
    
    def draw_rect(self, x, y, width, height, color, thickness):
        """Draw rectangle (placeholder - would use OpenGL)"""
        # This would be implemented with OpenGL calls
        pass
    
    def draw_text(self, x, y, text, color):
        """Draw text (placeholder - would use font rendering)"""
        # This would be implemented with text rendering
        pass
    
    def draw_skeleton(self, player, distance_factor):
        """Draw skeleton lines for player"""
        # This would draw connecting lines between bones
        # Head to chest, chest to arms, chest to legs, etc.
        # Implementation would use bone positions if available
        pass
    
    def draw_head_tracer(self, player):
        """Draw tracer line from crosshair to player head"""
        # This would draw a line from screen center to player head
        # Implementation would use OpenGL line drawing
        pass
    
    def draw_radar(self):
        """Draw mini-radar in corner of screen"""
        if not self.show_radar:
            return
            
        # Radar settings
        radar_size = 150
        radar_x = self.width - radar_size - 20
        radar_y = self.height - radar_size - 20
        
        # Draw radar background
        self.draw_rect(radar_x, radar_y, radar_size, radar_size, (0, 0, 0, 180), 0)
        
        # Draw radar border
        self.draw_rect(radar_x, radar_y, radar_size, radar_size, (255, 255, 255), 2)
        
        # Draw players on radar
        with self.players_lock:
            for player in self.players:
                if player.distance > self.max_render_distance:
                    continue
                    
                # Convert 3D position to 2D radar coordinates
                radar_scale = radar_size / (self.max_render_distance * 2)
                radar_player_x = radar_x + radar_size // 2 + int(player.x * radar_scale)
                radar_player_y = radar_y + radar_size // 2 + int(player.y * radar_scale)
                
                # Draw player dot
                color = self.esp_visible_color if player.is_visible else self.esp_hidden_color
                if not player.is_enemy:
                    color = self.esp_friend_color
                    
                self.draw_rect(radar_player_x - 2, radar_player_y - 2, 4, 4, color, 0)
    
    def draw_crosshair(self):
        """Draw custom crosshair"""
        if not self.show_crosshair:
            return
            
        center_x = self.width // 2
        center_y = self.height // 2
        crosshair_size = 10
        crosshair_thickness = 2
        
        # Draw crosshair lines
        self.draw_rect(center_x - crosshair_size, center_y - crosshair_thickness // 2, 
                      crosshair_size * 2, crosshair_thickness, (255, 255, 255), 0)
        self.draw_rect(center_x - crosshair_thickness // 2, center_y - crosshair_size, 
                      crosshair_thickness, crosshair_size * 2, (255, 255, 255), 0)
        
        # Draw center dot
        self.draw_rect(center_x - 1, center_y - 1, 2, 2, (255, 0, 0), 0)
    
    def handle_input(self):
        """Handle keyboard input"""
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            self.impl.process_event(event)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_INSERT:
                    self.show_menu = not self.show_menu
                elif event.key == pygame.K_F1:
                    self.show_esp = not self.show_esp
                elif event.key == pygame.K_F2:
                    self.show_stats = not self.show_stats
                elif event.key == pygame.K_END:
                    return False
        
        return True
    
    def update_fps(self):
        """Update FPS counter"""
        self.frame_count += 1
        current_time = time.time()
        
        if current_time - self.last_fps_time >= 1.0:
            self.fps = self.frame_count / (current_time - self.last_fps_time)
            self.frame_count = 0
            self.last_fps_time = current_time
    
    def run(self):
        """Main overlay loop"""
        if not GUI_AVAILABLE:
            return
            
        clock = pygame.time.Clock()
        running = True
        
        print("🎮 External overlay is running!")
        print("   Make sure the internal cheat is injected and sending data")
        
        while running:
            # Handle input
            running = self.handle_input()
            
            # Clear screen
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)
            
            # Draw ESP
            self.draw_esp()
            
            # Draw ImGui menu
            self.draw_menu()
            
            # Update display
            pygame.display.flip()
            
            # Update FPS
            self.update_fps()
            
            # Control frame rate
            clock.tick(60)
        
        # Cleanup
        self.sock.close()
        pygame.quit()
        print("Overlay closed")

def main():
    """Main entry point"""
    if not GUI_AVAILABLE:
        print("❌ Cannot start overlay - missing required libraries")
        print("   Install with: pip install pygame PyOpenGL imgui")
        return
    
    overlay = ExternalOverlay()
    overlay.run()

if __name__ == "__main__":
    main()

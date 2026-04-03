#!/usr/bin/env python3
"""
PROFESSIONAL PHANTOM STRIKE OVERLAY - Elite In-Game Menu System
Military-grade overlay with professional menu, ESP, aimbot integration, and skin changer
"""

import pygame
import sys
import time
import math
import random
from typing import List, Tuple, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
from collections import deque

# Initialize pygame
pygame.init()

# --- IMPORT PROFESSIONAL COMPONENTS ---
try:
    import importlib
    import real_aimbot_pro
    import ai_aimbot_pro
    import skin_changer_pro
    import offset_scanner_pro
    import anti_cheat_evasion_pro
    PROFESSIONAL_COMPONENTS_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Professional components not available: {e}")
    PROFESSIONAL_COMPONENTS_AVAILABLE = False

class MenuCategory(Enum):
    """Menu categories"""
    ESP = "ESP"
    AIMBOT = "Aimbot"
    MEMORY = "Memory"
    SKINS = "Skin Changer"
    OPTIONS = "Options"

@dataclass
class MenuItem:
    """Menu item configuration"""
    name: str
    enabled: bool = False
    value: Any = None
    min_val: float = 0
    max_val: float = 100
    step: float = 1
    item_type: str = "toggle"  # toggle, slider, button

class ProfessionalMenu:
    """Professional in-game menu system"""
    
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.visible = False
        self.current_category = MenuCategory.ESP
        self.selected_index = 0
        
        # Menu positioning
        self.menu_x = 50
        self.menu_y = 50
        self.menu_width = 400
        self.menu_height = 600
        
        # Colors
        self.bg_color = (20, 20, 30, 230)
        self.header_color = (40, 40, 60, 255)
        self.selected_color = (60, 60, 100, 255)
        self.text_color = (255, 255, 255)
        self.accent_color = (0, 255, 100)
        self.disabled_color = (100, 100, 100)
        
        # Fonts
        self.title_font = pygame.font.Font(None, 32)
        self.category_font = pygame.font.Font(None, 24)
        self.item_font = pygame.font.Font(None, 20)
        
        # Menu items by category
        self.menu_items = {
            MenuCategory.ESP: [
                MenuItem("Enable ESP", True, item_type="toggle"),
                MenuItem("Show Boxes", True, item_type="toggle"),
                MenuItem("Show Health Bars", True, item_type="toggle"),
                MenuItem("Show Armor Bars", True, item_type="toggle"),
                MenuItem("Show Distance", True, item_type="toggle"),
                MenuItem("Show Weapon", True, item_type="toggle"),
                MenuItem("Show Names", True, item_type="toggle"),
                MenuItem("Show Skeleton", False, item_type="toggle"),
                MenuItem("Max Distance", True, 500, 100, 1000, 50, "slider"),
                MenuItem("Box Thickness", True, 2, 1, 5, 1, "slider"),
            ],
            MenuCategory.AIMBOT: [
                MenuItem("Enable Aimbot", False, item_type="toggle"),
                MenuItem("Enable AI Aimbot", False, item_type="toggle"),
                MenuItem("Aim Key: RMB", True, item_type="toggle"),
                MenuItem("FOV", True, 90, 30, 180, 10, "slider"),
                MenuItem("Smoothness", True, 10, 1, 20, 1, "slider"),
                MenuItem("Target Bone: Head", True, item_type="toggle"),
                MenuItem("Prediction", True, item_type="toggle"),
                MenuItem("Human Aim", True, item_type="toggle"),
                MenuItem("Auto Fire", False, item_type="toggle"),
            ],
            MenuCategory.MEMORY: [
                MenuItem("Auto Scan Offsets", True, item_type="toggle"),
                MenuItem("Continuous Scanning", True, item_type="toggle"),
                MenuItem("Pattern Validation", True, item_type="toggle"),
                MenuItem("ML Prediction", True, item_type="toggle"),
                MenuItem("Scan Interval (s)", True, 5, 1, 30, 1, "slider"),
                MenuItem("Update Offsets", True, item_type="button"),
                MenuItem("Backup Offsets", True, item_type="button"),
            ],
            MenuCategory.SKINS: [
                MenuItem("Enable Skin Changer", False, item_type="toggle"),
                MenuItem("AK-47: Dragon Lore", False, item_type="toggle"),
                MenuItem("AWP: Fade", False, item_type="toggle"),
                MenuItem("Karambit: Fade", False, item_type="toggle"),
                MenuItem("USP-S: Fade", False, item_type="toggle"),
                MenuItem("M4A1-S: Howl", False, item_type="toggle"),
                MenuItem("StatTrak™", True, item_type="toggle"),
                MenuItem("Apply All Skins", True, item_type="button"),
                MenuItem("Save Inventory", True, item_type="button"),
            ],
            MenuCategory.OPTIONS: [
                MenuItem("Anti-Cheat Evasion", True, item_type="toggle"),
                MenuItem("Stealth Mode", True, item_type="toggle"),
                MenuItem("Process Cloaking", True, item_type="toggle"),
                MenuItem("Memory Encryption", True, item_type="toggle"),
                MenuItem("Network Stealth", True, item_type="toggle"),
                MenuItem("FPS Limit", True, 60, 30, 144, 15, "slider"),
                MenuItem("Show Stats", True, item_type="toggle"),
                MenuItem("Save Config", True, item_type="button"),
            ]
        }
    
    def toggle_menu(self):
        """Toggle menu visibility"""
        self.visible = not self.visible
    
    def handle_key(self, key):
        """Handle keyboard input"""
        if not self.visible:
            return
        
        items = self.menu_items[self.current_category]
        
        if key == pygame.K_UP:
            self.selected_index = (self.selected_index - 1) % len(items)
        elif key == pygame.K_DOWN:
            self.selected_index = (self.selected_index + 1) % len(items)
        elif key == pygame.K_LEFT:
            # Previous category
            categories = list(MenuCategory)
            current_idx = categories.index(self.current_category)
            self.current_category = categories[(current_idx - 1) % len(categories)]
            self.selected_index = 0
        elif key == pygame.K_RIGHT:
            # Next category
            categories = list(MenuCategory)
            current_idx = categories.index(self.current_category)
            self.current_category = categories[(current_idx + 1) % len(categories)]
            self.selected_index = 0
        elif key == pygame.K_RETURN or key == pygame.K_SPACE:
            # Toggle/activate selected item
            item = items[self.selected_index]
            if item.item_type == "toggle":
                item.enabled = not item.enabled
            elif item.item_type == "button":
                self.handle_button_action(item)
        elif key == pygame.K_a:
            # Decrease slider value
            item = items[self.selected_index]
            if item.item_type == "slider":
                item.value = max(item.min_val, item.value - item.step)
        elif key == pygame.K_d:
            # Increase slider value
            item = items[self.selected_index]
            if item.item_type == "slider":
                item.value = min(item.max_val, item.value + item.step)
    
    def handle_button_action(self, item: MenuItem):
        """Handle button actions"""
        if item.name == "Apply All Skins":
            print("🎨 Applying all selected skins...")
        elif item.name == "Save Inventory":
            print("💾 Saving skin inventory...")
        elif item.name == "Update Offsets":
            print("🔄 Updating offsets...")
        elif item.name == "Backup Offsets":
            print("💾 Backing up offsets...")
        elif item.name == "Save Config":
            print("💾 Saving configuration...")
    
    def draw(self, screen):
        """Draw professional menu"""
        if not self.visible:
            return
        
        # Create semi-transparent surface
        menu_surface = pygame.Surface((self.menu_width, self.menu_height), pygame.SRCALPHA)
        
        # Draw background
        pygame.draw.rect(menu_surface, self.bg_color, (0, 0, self.menu_width, self.menu_height))
        pygame.draw.rect(menu_surface, self.accent_color, (0, 0, self.menu_width, self.menu_height), 2)
        
        # Draw title
        title_text = self.title_font.render("PHANTOM STRIKE", True, self.accent_color)
        menu_surface.blit(title_text, (self.menu_width // 2 - title_text.get_width() // 2, 10))
        
        # Draw category tabs
        categories = list(MenuCategory)
        tab_width = self.menu_width // len(categories)
        for i, category in enumerate(categories):
            tab_x = i * tab_width
            tab_y = 50
            tab_color = self.header_color if category == self.current_category else (30, 30, 40, 200)
            
            pygame.draw.rect(menu_surface, tab_color, (tab_x, tab_y, tab_width, 30))
            pygame.draw.rect(menu_surface, self.accent_color if category == self.current_category else (60, 60, 80), 
                           (tab_x, tab_y, tab_width, 30), 1)
            
            cat_text = self.category_font.render(category.value, True, 
                                                self.accent_color if category == self.current_category else self.text_color)
            menu_surface.blit(cat_text, (tab_x + tab_width // 2 - cat_text.get_width() // 2, tab_y + 5))
        
        # Draw menu items
        items = self.menu_items[self.current_category]
        item_y = 100
        item_height = 35
        
        for i, item in enumerate(items):
            # Highlight selected item
            if i == self.selected_index:
                pygame.draw.rect(menu_surface, self.selected_color, 
                               (10, item_y, self.menu_width - 20, item_height))
            
            # Draw item name
            item_color = self.accent_color if item.enabled else self.disabled_color
            item_text = self.item_font.render(item.name, True, item_color)
            menu_surface.blit(item_text, (20, item_y + 8))
            
            # Draw item value/control
            if item.item_type == "toggle":
                toggle_text = "ON" if item.enabled else "OFF"
                toggle_color = self.accent_color if item.enabled else self.disabled_color
                value_text = self.item_font.render(toggle_text, True, toggle_color)
                menu_surface.blit(value_text, (self.menu_width - 60, item_y + 8))
            elif item.item_type == "slider":
                # Draw slider bar
                slider_x = self.menu_width - 150
                slider_width = 120
                slider_y = item_y + 15
                
                pygame.draw.rect(menu_surface, (60, 60, 80), (slider_x, slider_y, slider_width, 5))
                
                # Draw slider value
                slider_pos = (item.value - item.min_val) / (item.max_val - item.min_val)
                slider_fill_width = int(slider_width * slider_pos)
                pygame.draw.rect(menu_surface, self.accent_color, (slider_x, slider_y, slider_fill_width, 5))
                
                # Draw value text
                value_text = self.item_font.render(f"{int(item.value)}", True, self.text_color)
                menu_surface.blit(value_text, (slider_x + slider_width + 10, item_y + 8))
            elif item.item_type == "button":
                button_text = self.item_font.render("[ENTER]", True, self.accent_color)
                menu_surface.blit(button_text, (self.menu_width - 80, item_y + 8))
            
            item_y += item_height
        
        # Draw controls help
        help_y = self.menu_height - 80
        help_texts = [
            "↑↓ Navigate  ←→ Category  SPACE Toggle",
            "A/D Adjust Slider  ENTER Activate",
            "INSERT Close Menu"
        ]
        for i, help_text in enumerate(help_texts):
            help_render = self.item_font.render(help_text, True, (150, 150, 150))
            menu_surface.blit(help_render, (20, help_y + i * 20))
        
        # Blit menu to screen
        screen.blit(menu_surface, (self.menu_x, self.menu_y))

class PhantomStrikeOverlay:
    """Professional Phantom Strike overlay with in-game menu"""
    
    def __init__(self):
        # Get screen info
        info = pygame.display.Info()
        self.width = info.current_w
        self.height = info.current_h
        
        # Create window
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)
        pygame.display.set_caption("Phantom Strike Professional")
        
        # Set window to be transparent and always on top
        try:
            import ctypes
            hwnd = pygame.display.get_wm_info()['window']
            ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)
        except:
            pass
        
        # Initialize menu
        self.menu = ProfessionalMenu(self.width, self.height)
        
        # Initialize professional components
        self.real_aimbot = None
        self.ai_aimbot = None
        self.skin_changer = None
        self.offset_scanner = None
        self.anti_cheat = None
        
        if PROFESSIONAL_COMPONENTS_AVAILABLE:
            self.initialize_professional_components()
        
        # Demo ESP players
        self.players = []
        self.generate_demo_players()
        
        # Performance
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        
        print("✅ Phantom Strike Professional Overlay initialized")
        print(f"🎯 Screen: {self.width}x{self.height}")
        print("🔥 Press INSERT to toggle menu")
    
    def initialize_professional_components(self):
        """Initialize all professional components"""
        try:
            # Get instances from __main__
            import __main__
            
            if hasattr(__main__, 'professional_real_aimbot'):
                self.real_aimbot = __main__.professional_real_aimbot
                print("✅ Real Aimbot connected")
            
            if hasattr(__main__, 'professional_ai_aimbot'):
                self.ai_aimbot = __main__.professional_ai_aimbot
                print("✅ AI Aimbot connected")
            
            if hasattr(__main__, 'professional_skin_changer'):
                self.skin_changer = __main__.professional_skin_changer
                print("✅ Skin Changer connected")
            
            if hasattr(__main__, 'professional_offset_scanner'):
                self.offset_scanner = __main__.professional_offset_scanner
                print("✅ Offset Scanner connected")
            
            if hasattr(__main__, 'professional_anti_cheat_evasion'):
                self.anti_cheat = __main__.professional_anti_cheat_evasion
                print("✅ Anti-Cheat Evasion connected")
                
        except Exception as e:
            print(f"⚠️ Failed to connect professional components: {e}")
    
    def generate_demo_players(self):
        """Generate demo players for ESP demonstration"""
        self.players = []
        
        for i in range(12):
            angle = (i / 12.0) * 2 * math.pi
            distance = random.uniform(200, 600)
            
            x = math.cos(angle) * distance
            y = math.sin(angle) * distance
            z = random.uniform(-50, 100)
            
            player = {
                'id': i,
                'position': (x, y, z),
                'health': random.randint(20, 100),
                'max_health': 100,
                'armor': random.randint(0, 100),
                'team': random.choice([0, 1]),
                'name': f"Player_{i}",
                'weapon': random.choice(["AK-47", "M4A1", "AWP", "Desert Eagle"]),
                'distance': distance,
                'visible': True
            }
            
            self.players.append(player)
    
    def world_to_screen(self, world_pos: Tuple[float, float, float]) -> Tuple[int, int]:
        """Convert 3D world coordinates to 2D screen coordinates"""
        distance = math.sqrt(sum(p**2 for p in world_pos))
        
        if distance == 0:
            return (self.width // 2, self.height // 2)
        
        # Simple perspective projection
        fov = math.radians(90)
        scale = (self.height / 2) / math.tan(fov / 2)
        
        screen_x = int(self.width / 2 + (world_pos[0] * scale) / distance)
        screen_y = int(self.height / 2 - (world_pos[1] * scale) / distance)
        
        return (screen_x, screen_y)
    
    def draw_esp(self):
        """Draw ESP for players"""
        # Check if ESP is enabled in menu
        esp_enabled = self.menu.menu_items[MenuCategory.ESP][0].enabled
        if not esp_enabled:
            return
        
        show_boxes = self.menu.menu_items[MenuCategory.ESP][1].enabled
        show_health = self.menu.menu_items[MenuCategory.ESP][2].enabled
        show_armor = self.menu.menu_items[MenuCategory.ESP][3].enabled
        show_distance = self.menu.menu_items[MenuCategory.ESP][4].enabled
        show_weapon = self.menu.menu_items[MenuCategory.ESP][5].enabled
        show_names = self.menu.menu_items[MenuCategory.ESP][6].enabled
        
        font = pygame.font.Font(None, 18)
        
        for player in self.players:
            if not player['visible']:
                continue
            
            screen_x, screen_y = self.world_to_screen(player['position'])
            
            # Skip if off-screen
            if screen_x < 0 or screen_x > self.width or screen_y < 0 or screen_y > self.height:
                continue
            
            # Determine color based on team
            is_enemy = player['team'] == 0
            box_color = (255, 0, 0) if is_enemy else (0, 255, 0)
            
            # Draw box
            if show_boxes:
                box_width = 40
                box_height = 60
                box_x = screen_x - box_width // 2
                box_y = screen_y - box_height // 2
                
                pygame.draw.rect(self.screen, box_color, (box_x, box_y, box_width, box_height), 2)
            
            # Draw health bar
            if show_health:
                health_percent = player['health'] / player['max_health']
                health_bar_width = 40
                health_bar_height = 4
                health_bar_x = screen_x - health_bar_width // 2
                health_bar_y = screen_y - 35
                
                # Background
                pygame.draw.rect(self.screen, (60, 60, 60), 
                               (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
                # Health fill
                health_fill_width = int(health_bar_width * health_percent)
                health_color = (0, 255, 0) if health_percent > 0.5 else (255, 255, 0) if health_percent > 0.25 else (255, 0, 0)
                pygame.draw.rect(self.screen, health_color, 
                               (health_bar_x, health_bar_y, health_fill_width, health_bar_height))
            
            # Draw armor bar
            if show_armor and player['armor'] > 0:
                armor_percent = player['armor'] / 100
                armor_bar_width = 40
                armor_bar_height = 3
                armor_bar_x = screen_x - armor_bar_width // 2
                armor_bar_y = screen_y - 30
                
                armor_fill_width = int(armor_bar_width * armor_percent)
                pygame.draw.rect(self.screen, (0, 100, 255), 
                               (armor_bar_x, armor_bar_y, armor_fill_width, armor_bar_height))
            
            # Draw info text
            info_y = screen_y + 35
            
            if show_names:
                name_text = font.render(player['name'], True, (255, 255, 255))
                self.screen.blit(name_text, (screen_x - name_text.get_width() // 2, info_y))
                info_y += 15
            
            if show_weapon:
                weapon_text = font.render(player['weapon'], True, (200, 200, 200))
                self.screen.blit(weapon_text, (screen_x - weapon_text.get_width() // 2, info_y))
                info_y += 15
            
            if show_distance:
                distance_text = font.render(f"{int(player['distance'])}m", True, (255, 255, 0))
                self.screen.blit(distance_text, (screen_x - distance_text.get_width() // 2, info_y))
    
    def draw_crosshair(self):
        """Draw professional crosshair"""
        center_x = self.width // 2
        center_y = self.height // 2
        
        # Draw crosshair lines
        crosshair_size = 15
        crosshair_gap = 5
        crosshair_thickness = 2
        crosshair_color = (0, 255, 100)
        
        # Top
        pygame.draw.line(self.screen, crosshair_color, 
                        (center_x, center_y - crosshair_gap - crosshair_size), 
                        (center_x, center_y - crosshair_gap), crosshair_thickness)
        # Bottom
        pygame.draw.line(self.screen, crosshair_color, 
                        (center_x, center_y + crosshair_gap), 
                        (center_x, center_y + crosshair_gap + crosshair_size), crosshair_thickness)
        # Left
        pygame.draw.line(self.screen, crosshair_color, 
                        (center_x - crosshair_gap - crosshair_size, center_y), 
                        (center_x - crosshair_gap, center_y), crosshair_thickness)
        # Right
        pygame.draw.line(self.screen, crosshair_color, 
                        (center_x + crosshair_gap, center_y), 
                        (center_x + crosshair_gap + crosshair_size, center_y), crosshair_thickness)
        
        # Draw center dot
        pygame.draw.circle(self.screen, crosshair_color, (center_x, center_y), 2)
    
    def draw_stats(self):
        """Draw performance statistics"""
        show_stats = self.menu.menu_items[MenuCategory.OPTIONS][6].enabled
        if not show_stats:
            return
        
        font = pygame.font.Font(None, 20)
        stats_x = 10
        stats_y = 10
        
        stats = [
            f"FPS: {int(self.clock.get_fps())}",
            f"Players: {len(self.players)}",
            f"Menu: {'OPEN' if self.menu.visible else 'CLOSED'}",
        ]
        
        for i, stat in enumerate(stats):
            stat_text = font.render(stat, True, (0, 255, 100))
            self.screen.blit(stat_text, (stats_x, stats_y + i * 20))
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_INSERT:
                    self.menu.toggle_menu()
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
                else:
                    self.menu.handle_key(event.key)
    
    def run(self):
        """Main overlay loop"""
        while self.running:
            # Handle events
            self.handle_events()
            
            # Clear screen with transparency
            self.screen.fill((0, 0, 0, 0))
            
            # Draw ESP
            self.draw_esp()
            
            # Draw crosshair
            self.draw_crosshair()
            
            # Draw stats
            self.draw_stats()
            
            # Draw menu (always on top)
            self.menu.draw(self.screen)
            
            # Update display
            pygame.display.flip()
            
            # Cap FPS
            fps_limit = self.menu.menu_items[MenuCategory.OPTIONS][5].value
            self.clock.tick(int(fps_limit))
        
        pygame.quit()

def main():
    """Main entry point"""
    overlay = PhantomStrikeOverlay()
    overlay.run()

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
PROFESSIONAL PHANTOM STRIKE OVERLAY - Mouse-Driven Draggable Menu
Military-grade overlay with professional menu, ESP, aimbot integration, and skin changer
"""

import os
import sys
import subprocess

# Set SDL to use dummy audio to avoid pygame audio initialization issues
os.environ['SDL_AUDIODRIVER'] = 'dummy'

# Force X11 backend for SDL to work with XWayland on Fedora GNOME
# This ensures the overlay can be positioned and made transparent correctly
if os.environ.get('XDG_SESSION_TYPE') == 'wayland':
    os.environ['SDL_VIDEODRIVER'] = 'x11'
    print("🌐 Wayland detected, forcing SDL_VIDEODRIVER=x11 for XWayland compatibility")

import pygame
import time
import math
import random
from typing import List, Tuple, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
from collections import deque

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
    rect: pygame.Rect = None  # For mouse collision detection

class ProfessionalMenu:
    """Professional mouse-driven draggable menu system"""
    
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.visible = True  # Start visible
        self.current_category = MenuCategory.ESP
        self.selected_index = 0
        
        # Menu positioning (draggable)
        self.menu_x = 50
        self.menu_y = 50
        self.menu_width = 690
        self.menu_height = 470
        self.dragging = False
        self.drag_offset_x = 0
        self.drag_offset_y = 0
        
        # Colors (matching ImGui style)
        self.bg_color = (25, 25, 30, 240)
        self.header_color = (35, 35, 45, 255)
        self.selected_color = (70, 92, 120, 255)
        self.hover_color = (50, 50, 70, 255)
        self.text_color = (255, 255, 255)
        self.accent_color = (112, 146, 190)  # Main color from reference
        self.disabled_color = (100, 100, 100)
        self.border_color = (60, 60, 80)
        
        # Fonts
        self.title_font = pygame.font.Font(None, 36)
        self.category_font = pygame.font.Font(None, 22)
        self.item_font = pygame.font.Font(None, 18)
        self.small_font = pygame.font.Font(None, 14)
        
        # Mouse state
        self.mouse_pos = (0, 0)
        self.mouse_down = False
        self.dragging_slider = None
        
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
    
    def handle_mouse_down(self, pos):
        """Handle mouse button down"""
        self.mouse_down = True
        
        if not self.visible:
            return
        
        # Check if clicking on header (for dragging)
        header_rect = pygame.Rect(self.menu_x, self.menu_y, self.menu_width, 40)
        if header_rect.collidepoint(pos):
            self.dragging = True
            self.drag_offset_x = pos[0] - self.menu_x
            self.drag_offset_y = pos[1] - self.menu_y
            return
        
        # Check category tabs
        categories = list(MenuCategory)
        tab_width = (self.menu_width - 40) // len(categories)
        for i, category in enumerate(categories):
            tab_x = self.menu_x + 40 + i * tab_width
            tab_y = self.menu_y + 50
            tab_rect = pygame.Rect(tab_x, tab_y, tab_width, 35)
            
            if tab_rect.collidepoint(pos):
                self.current_category = category
                self.selected_index = 0
                return
        
        # Check menu items
        items = self.menu_items[self.current_category]
        item_y = self.menu_y + 100
        item_height = 35
        
        for i, item in enumerate(items):
            if item.rect and item.rect.collidepoint(pos):
                if item.item_type == "toggle":
                    item.enabled = not item.enabled
                elif item.item_type == "button":
                    self.handle_button_action(item)
                elif item.item_type == "slider":
                    self.dragging_slider = item
                return
    
    def handle_mouse_up(self, pos):
        """Handle mouse button up"""
        self.mouse_down = False
        self.dragging = False
        self.dragging_slider = None
    
    def handle_mouse_motion(self, pos):
        """Handle mouse motion"""
        self.mouse_pos = pos
        
        if self.dragging:
            self.menu_x = pos[0] - self.drag_offset_x
            self.menu_y = pos[1] - self.drag_offset_y
            
            # Keep menu on screen
            self.menu_x = max(0, min(self.menu_x, self.screen_width - self.menu_width))
            self.menu_y = max(0, min(self.menu_y, self.screen_height - self.menu_height))
        
        if self.dragging_slider:
            # Update slider value based on mouse position
            slider_x = self.menu_width - 160
            slider_width = 120
            relative_x = pos[0] - (self.menu_x + slider_x)
            slider_pos = max(0, min(1, relative_x / slider_width))
            
            value_range = self.dragging_slider.max_val - self.dragging_slider.min_val
            self.dragging_slider.value = self.dragging_slider.min_val + (slider_pos * value_range)
            self.dragging_slider.value = round(self.dragging_slider.value / self.dragging_slider.step) * self.dragging_slider.step
    
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
        """Draw professional menu with mouse support"""
        if not self.visible:
            return
        
        # Create semi-transparent surface
        menu_surface = pygame.Surface((self.menu_width, self.menu_height), pygame.SRCALPHA)
        
        # Draw main background
        pygame.draw.rect(menu_surface, self.bg_color, (0, 0, self.menu_width, self.menu_height))
        pygame.draw.rect(menu_surface, self.border_color, (0, 0, self.menu_width, self.menu_height), 2)
        
        # Draw header with gradient effect
        header_rect = pygame.Rect(0, 0, self.menu_width, 40)
        pygame.draw.rect(menu_surface, self.header_color, header_rect)
        pygame.draw.line(menu_surface, self.accent_color, (0, 40), (self.menu_width, 40), 2)
        
        # Draw title
        title_text = self.title_font.render("PHANTOM STRIKE", True, self.accent_color)
        menu_surface.blit(title_text, (20, 8))
        
        # Draw close button
        close_text = self.item_font.render("✕", True, self.text_color)
        menu_surface.blit(close_text, (self.menu_width - 30, 12))
        
        # Draw category tabs
        categories = list(MenuCategory)
        tab_width = (self.menu_width - 40) // len(categories)
        
        for i, category in enumerate(categories):
            tab_x = 40 + i * tab_width
            tab_y = 50
            
            # Check if mouse is hovering
            tab_rect = pygame.Rect(self.menu_x + tab_x, self.menu_y + tab_y, tab_width, 35)
            is_hover = tab_rect.collidepoint(self.mouse_pos)
            is_selected = category == self.current_category
            
            # Draw tab background
            if is_selected:
                tab_color = self.accent_color
                text_color = (255, 255, 255)
            elif is_hover:
                tab_color = self.hover_color
                text_color = self.text_color
            else:
                tab_color = (30, 30, 40, 200)
                text_color = (150, 150, 150)
            
            pygame.draw.rect(menu_surface, tab_color, (tab_x, tab_y, tab_width, 35))
            pygame.draw.rect(menu_surface, self.border_color, (tab_x, tab_y, tab_width, 35), 1)
            
            # Draw tab text
            cat_text = self.category_font.render(category.value, True, text_color)
            text_x = tab_x + tab_width // 2 - cat_text.get_width() // 2
            menu_surface.blit(cat_text, (text_x, tab_y + 8))
        
        # Draw menu items
        items = self.menu_items[self.current_category]
        item_y = 100
        item_height = 35
        
        for i, item in enumerate(items):
            # Create rect for collision detection
            item_rect = pygame.Rect(self.menu_x + 20, self.menu_y + item_y, self.menu_width - 40, item_height)
            item.rect = item_rect
            
            # Check if mouse is hovering
            is_hover = item_rect.collidepoint(self.mouse_pos)
            
            # Draw item background
            if is_hover:
                pygame.draw.rect(menu_surface, self.hover_color, (20, item_y, self.menu_width - 40, item_height))
            
            # Draw item name
            item_color = self.accent_color if item.enabled else self.disabled_color
            item_text = self.item_font.render(item.name, True, item_color)
            menu_surface.blit(item_text, (30, item_y + 10))
            
            # Draw item control
            if item.item_type == "toggle":
                # Draw toggle switch
                toggle_width = 40
                toggle_height = 20
                toggle_x = self.menu_width - 70
                toggle_y = item_y + 8
                
                # Background
                bg_color = self.accent_color if item.enabled else (60, 60, 70)
                pygame.draw.rect(menu_surface, bg_color, (toggle_x, toggle_y, toggle_width, toggle_height), border_radius=10)
                
                # Switch circle
                circle_x = toggle_x + (toggle_width - 16) if item.enabled else toggle_x + 8
                circle_y = toggle_y + 10
                pygame.draw.circle(menu_surface, (255, 255, 255), (circle_x, circle_y), 8)
                
            elif item.item_type == "slider":
                # Draw slider
                slider_x = self.menu_width - 160
                slider_width = 120
                slider_y = item_y + 15
                
                # Background track
                pygame.draw.rect(menu_surface, (60, 60, 80), (slider_x, slider_y, slider_width, 6), border_radius=3)
                
                # Filled track
                slider_pos = (item.value - item.min_val) / (item.max_val - item.min_val)
                slider_fill_width = int(slider_width * slider_pos)
                pygame.draw.rect(menu_surface, self.accent_color, (slider_x, slider_y, slider_fill_width, 6), border_radius=3)
                
                # Slider handle
                handle_x = slider_x + slider_fill_width
                handle_y = slider_y + 3
                pygame.draw.circle(menu_surface, (255, 255, 255), (handle_x, handle_y), 8)
                pygame.draw.circle(menu_surface, self.accent_color, (handle_x, handle_y), 6)
                
                # Value text
                value_text = self.small_font.render(f"{int(item.value)}", True, self.text_color)
                menu_surface.blit(value_text, (slider_x + slider_width + 10, item_y + 10))
                
            elif item.item_type == "button":
                # Draw button
                button_width = 80
                button_height = 25
                button_x = self.menu_width - 100
                button_y = item_y + 5
                
                button_color = self.accent_color if is_hover else (70, 70, 90)
                pygame.draw.rect(menu_surface, button_color, (button_x, button_y, button_width, button_height), border_radius=4)
                pygame.draw.rect(menu_surface, self.border_color, (button_x, button_y, button_width, button_height), 1, border_radius=4)
                
                button_text = self.small_font.render("ACTIVATE", True, self.text_color)
                text_x = button_x + button_width // 2 - button_text.get_width() // 2
                menu_surface.blit(button_text, (text_x, button_y + 6))
            
            item_y += item_height
        
        # Draw controls help at bottom
        help_y = self.menu_height - 30
        help_text = self.small_font.render("INSERT: Toggle Menu  |  Drag header to move  |  Click to interact", True, (120, 120, 120))
        menu_surface.blit(help_text, (20, help_y))
        
        # Blit menu to screen
        screen.blit(menu_surface, (self.menu_x, self.menu_y))

class PhantomStrikeOverlay:
    """Professional Phantom Strike overlay with mouse-driven menu"""
    
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Get screen info
        info = pygame.display.Info()
        self.width = info.current_w
        self.height = info.current_h
        
        print(f"🖥️  Screen: {self.width}x{self.height}")
        
        # Set environment for overlay positioning
        os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
        
        # Create transparent overlay window
        self.screen = pygame.display.set_mode(
            (self.width, self.height),
            pygame.NOFRAME | pygame.SRCALPHA | pygame.HWSURFACE | pygame.DOUBLEBUF
        )
        pygame.display.set_caption("Phantom Strike Professional")
        
        # Set window to be always on top and transparent
        self._setup_overlay_window()
        
        # Initialize menu
        self.menu = ProfessionalMenu(self.width, self.height)
    
    def _setup_overlay_window(self):
        """Configure window to be a proper game overlay"""
        try:
            time.sleep(0.5)  # Wait for window creation
            
            # Find our overlay window
            try:
                result = subprocess.run(
                    ['xdotool', 'search', '--name', 'Phantom Strike Professional'],
                    capture_output=True, text=True, timeout=2
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    window_id = result.stdout.strip().split('\n')[0]

                    # Make window always on top
                    subprocess.run(
                        ['wmctrl', '-i', '-r', window_id, '-b', 'add,above,sticky'],
                        capture_output=True, timeout=2
                    )

                    # Set window type to dock (prevents it from stealing focus)
                    subprocess.run(
                        ['xprop', '-id', window_id, '-f', '_NET_WM_WINDOW_TYPE', '32a',
                         '-set', '_NET_WM_WINDOW_TYPE', '_NET_WM_WINDOW_TYPE_DOCK'],
                        capture_output=True, timeout=2
                    )

                    # Try to make it skip taskbar
                    subprocess.run(
                        ['wmctrl', '-i', '-r', window_id, '-b', 'add,skip_taskbar,skip_pager'],
                        capture_output=True, timeout=2
                    )

                    print(f"✅ Overlay window {window_id} configured")
                    print("💡 Overlay is now on top of all windows")
                else:
                    print("⚠️  Could not find overlay window for configuration via xdotool")
            except FileNotFoundError:
                print("⚠️  xdotool or wmctrl not found. Please install them for best overlay experience.")
                
        except subprocess.TimeoutExpired:
            print("⚠️  Window setup timed out")
        except Exception as e:
            print(f"⚠️  Window setup: {e}")
        
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
        print("🔥 Press INSERT to toggle menu")
        print("🖱️  Click and drag header to move menu")
    
    def initialize_professional_components(self):
        """Initialize all professional components"""
        try:
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
        
        fov = math.radians(90)
        scale = (self.height / 2) / math.tan(fov / 2)
        
        screen_x = int(self.width / 2 + (world_pos[0] * scale) / distance)
        screen_y = int(self.height / 2 - (world_pos[1] * scale) / distance)
        
        return (screen_x, screen_y)
    
    def draw_esp(self):
        """Draw ESP for players"""
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
            
            if screen_x < 0 or screen_x > self.width or screen_y < 0 or screen_y > self.height:
                continue
            
            is_enemy = player['team'] == 0
            box_color = (255, 0, 0) if is_enemy else (0, 255, 0)
            
            if show_boxes:
                box_width = 40
                box_height = 60
                box_x = screen_x - box_width // 2
                box_y = screen_y - box_height // 2
                pygame.draw.rect(self.screen, box_color, (box_x, box_y, box_width, box_height), 2)
            
            if show_health:
                health_percent = player['health'] / player['max_health']
                health_bar_width = 40
                health_bar_height = 4
                health_bar_x = screen_x - health_bar_width // 2
                health_bar_y = screen_y - 35
                
                pygame.draw.rect(self.screen, (60, 60, 60), 
                               (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
                health_fill_width = int(health_bar_width * health_percent)
                health_color = (0, 255, 0) if health_percent > 0.5 else (255, 255, 0) if health_percent > 0.25 else (255, 0, 0)
                pygame.draw.rect(self.screen, health_color, 
                               (health_bar_x, health_bar_y, health_fill_width, health_bar_height))
            
            if show_armor and player['armor'] > 0:
                armor_percent = player['armor'] / 100
                armor_bar_width = 40
                armor_bar_height = 3
                armor_bar_x = screen_x - armor_bar_width // 2
                armor_bar_y = screen_y - 30
                
                armor_fill_width = int(armor_bar_width * armor_percent)
                pygame.draw.rect(self.screen, (0, 100, 255), 
                               (armor_bar_x, armor_bar_y, armor_fill_width, armor_bar_height))
            
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
        
        crosshair_size = 15
        crosshair_gap = 5
        crosshair_thickness = 2
        crosshair_color = (0, 255, 100)
        
        pygame.draw.line(self.screen, crosshair_color, 
                        (center_x, center_y - crosshair_gap - crosshair_size), 
                        (center_x, center_y - crosshair_gap), crosshair_thickness)
        pygame.draw.line(self.screen, crosshair_color, 
                        (center_x, center_y + crosshair_gap), 
                        (center_x, center_y + crosshair_gap + crosshair_size), crosshair_thickness)
        pygame.draw.line(self.screen, crosshair_color, 
                        (center_x - crosshair_gap - crosshair_size, center_y), 
                        (center_x - crosshair_gap, center_y), crosshair_thickness)
        pygame.draw.line(self.screen, crosshair_color, 
                        (center_x + crosshair_gap, center_y), 
                        (center_x + crosshair_gap + crosshair_size, center_y), crosshair_thickness)
        
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.menu.handle_mouse_down(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.menu.handle_mouse_up(event.pos)
            elif event.type == pygame.MOUSEMOTION:
                self.menu.handle_mouse_motion(event.pos)
    
    def run(self):
        """Main overlay loop"""
        while self.running:
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

#!/usr/bin/env python3
"""
BloodStrike Skin Changer GUI Integration
ImGui-based interface for skin changer functionality
"""

import sys
import os
from typing import Dict, List, Any, Optional

# Add paths
sys.path.insert(0, os.path.dirname(__file__))

try:
    import imgui
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False
    print("⚠ ImGui not available for skin changer GUI")

from skin_changer import get_skin_changer, WeaponType, SkinRarity, WeaponSkin

class SkinChangerGUI:
    """GUI for the skin changer system"""
    
    def __init__(self):
        self.skin_changer = get_skin_changer()
        self.show_skin_preview = False
        self.selected_weapon_id = None
        self.selected_skin_id = None
        self.search_filter = ""
        self.selected_rarity = None
        self.selected_weapon_type = None
        
        # GUI state
        self.weapon_list_open = True
        self.skin_list_open = True
        self.settings_open = True
        
        # Colors for rarity
        self.rarity_colors = {
            SkinRarity.COMMON: (0.5, 0.5, 0.5, 1.0),      # Gray
            SkinRarity.UNCOMMON: (0.3, 0.7, 0.3, 1.0),    # Green
            SkinRarity.RARE: (0.3, 0.3, 0.8, 1.0),        # Blue
            SkinRarity.EPIC: (0.6, 0.3, 0.8, 1.0),        # Purple
            SkinRarity.LEGENDARY: (0.9, 0.6, 0.1, 1.0),   # Orange
            SkinRarity.MYTHIC: (0.9, 0.1, 0.6, 1.0),      # Pink
        }
    
    def render_skin_changer_tab(self):
        """Render the skin changer tab"""
        if not GUI_AVAILABLE:
            return
        
        if imgui.begin_tab_item("Skin Changer")[0]:
            self.render_main_controls()
            imgui.separator()
            self.render_weapon_list()
            imgui.same_line()
            self.render_skin_selection()
            imgui.separator()
            self.render_skin_preview()
            imgui.end_tab_item()
    
    def render_main_controls(self):
        """Render main control toggles"""
        # Main toggle
        changed, self.skin_changer.enabled = imgui.checkbox("Skin Changer Enabled", self.skin_changer.enabled)
        if changed:
            self.skin_changer.toggle_skin_changer()
        
        imgui.same_line()
        
        # Auto-equip toggle
        changed, self.skin_changer.auto_equip = imgui.checkbox("Auto-Equip", self.skin_changer.auto_equip)
        if changed:
            self.skin_changer.save_skin_config()
        
        imgui.same_line()
        
        # Random skins toggle
        changed, self.skin_changer.random_skins = imgui.checkbox("Random Skins", self.skin_changer.random_skins)
        if changed:
            self.skin_changer.save_skin_config()
        
        # Status display
        status = self.skin_changer.get_status()
        imgui.text(f"Status: {status['equipped_skins']}/{status['weapons_in_inventory']} weapons skinned")
        
        # Force update button
        if imgui.button("Update Inventory"):
            self.skin_changer.update_weapon_inventory()
        
        imgui.same_line()
        
        # Save loadout button
        if imgui.button("Save Loadout"):
            self.skin_changer.save_skin_config()
        
        imgui.same_line()
        
        # Random all button
        if imgui.button("Random All Skins"):
            self.skin_changer.equip_random_skins()
    
    def render_weapon_list(self):
        """Render weapon inventory list"""
        if imgui.collapsing_header("Weapon Inventory", self.weapon_list_open)[1]:
            self.weapon_list_open = True
            
            # Update inventory if needed
            if len(self.skin_changer.weapon_inventory) == 0:
                self.skin_changer.update_weapon_inventory()
            
            # Search filter
            changed, self.search_filter = imgui.input_text("Search", self.search_filter, 256)
            
            # Weapon type filter
            weapon_types = ["All"] + [wt.value for wt in WeaponType]
            current_type_index = 0
            if self.selected_weapon_type:
                try:
                    current_type_index = weapon_types.index(self.selected_weapon_type.value)
                except:
                    current_type_index = 0
            
            changed, new_index = imgui.combo("Type", current_type_index, weapon_types)
            if changed:
                if new_index == 0:
                    self.selected_weapon_type = None
                else:
                    self.selected_weapon_type = WeaponType(weapon_types[new_index])
            
            # Weapon list
            if imgui.begin_child("WeaponList", (200, 300), True):
                for weapon_id, weapon_info in self.skin_changer.weapon_inventory.items():
                    # Apply filters
                    weapon_name = weapon_info['name']
                    if self.search_filter and self.search_filter.lower() not in weapon_name.lower():
                        continue
                    
                    weapon_type = self.skin_changer.get_weapon_type_from_name(weapon_name)
                    if self.selected_weapon_type and weapon_type != self.selected_weapon_type:
                        continue
                    
                    # Check if selected
                    is_selected = (self.selected_weapon_id == weapon_id)
                    
                    # Weapon name with current skin
                    display_name = weapon_name
                    current_skin_id = weapon_info.get('current_skin')
                    if current_skin_id:
                        skin = self.skin_changer.get_skin_by_id(current_skin_id)
                        if skin:
                            display_name = f"{weapon_name} [{skin.name}]"
                    
                    # Selectable weapon
                    clicked, _ = imgui.selectable(display_name, is_selected)
                    if clicked:
                        self.selected_weapon_id = weapon_id
                        self.selected_skin_id = current_skin_id
                    
                    # Context menu
                    if imgui.begin_popup_context_item(f"weapon_context_{weapon_id}"):
                        if imgui.menu_item("Clear Skin")[0]:
                            # Remove skin from weapon
                            if weapon_id in self.skin_changer.current_skins:
                                del self.skin_changer.current_skins[weapon_id]
                                weapon_info['current_skin'] = None
                                self.skin_changer.save_skin_config()
                        
                        if imgui.menu_item("Equip Random")[0]:
                            if weapon_type:
                                available_skins = self.skin_changer.get_weapon_skins(weapon_type)
                                if available_skins:
                                    import random
                                    random_skin = random.choice(available_skins)
                                    self.skin_changer.equip_skin(weapon_id, random_skin.id)
                        
                        imgui.end_popup()
            
            imgui.end_child()
        else:
            self.weapon_list_open = False
    
    def render_skin_selection(self):
        """Render skin selection panel"""
        if imgui.collapsing_header("Skin Selection", self.skin_list_open)[1]:
            self.skin_list_open = True
            
            if not self.selected_weapon_id:
                imgui.text("Select a weapon to view available skins")
                return
            
            # Get weapon info
            weapon_info = self.skin_changer.weapon_inventory.get(self.selected_weapon_id, {})
            weapon_name = weapon_info.get('name', 'Unknown Weapon')
            weapon_type = self.skin_changer.get_weapon_type_from_name(weapon_name)
            
            imgui.text(f"Skins for: {weapon_name}")
            
            if not weapon_type:
                imgui.text("Unknown weapon type")
                return
            
            # Rarity filter
            rarity_types = ["All"] + [sr.value for sr in SkinRarity]
            current_rarity_index = 0
            if self.selected_rarity:
                try:
                    current_rarity_index = rarity_types.index(self.selected_rarity.value)
                except:
                    current_rarity_index = 0
            
            changed, new_index = imgui.combo("Rarity", current_rarity_index, rarity_types)
            if changed:
                if new_index == 0:
                    self.selected_rarity = None
                else:
                    self.selected_rarity = SkinRarity(rarity_types[new_index])
            
            # Skin list
            available_skins = self.skin_changer.get_weapon_skins(weapon_type)
            
            if imgui.begin_child("SkinList", (300, 300), True):
                for skin in available_skins:
                    # Apply rarity filter
                    if self.selected_rarity and skin.rarity != self.selected_rarity:
                        continue
                    
                    # Check if selected
                    is_selected = (self.selected_skin_id == skin.id)
                    
                    # Skin name with rarity color
                    imgui.push_style_color(imgui.IMGUI_COL_TEXT, self.rarity_colors[skin.rarity])
                    
                    # Selectable skin
                    clicked, _ = imgui.selectable(f"{skin.name}##skin_{skin.id}", is_selected)
                    
                    imgui.pop_style_color()
                    
                    if clicked:
                        self.selected_skin_id = skin.id
                    
                    # Tooltip with skin info
                    if imgui.is_item_hovered():
                        imgui.begin_tooltip()
                        imgui.text(f"{skin.name}")
                        imgui.text(f"Rarity: {skin.rarity.value}")
                        imgui.text(f"{skin.description}")
                        imgui.separator()
                        
                        if imgui.button(f"Equip##equip_{skin.id}"):
                            self.skin_changer.equip_skin(self.selected_weapon_id, skin.id)
                            weapon_info['current_skin'] = skin.id
                        
                        imgui.end_tooltip()
                    
                    # Quick equip button
                    imgui.same_line()
                    if imgui.button(f"Equip##quick_equip_{skin.id}", (60, 20)):
                        self.skin_changer.equip_skin(self.selected_weapon_id, skin.id)
                        weapon_info['current_skin'] = skin.id
            
            imgui.end_child()
        else:
            self.skin_list_open = False
    
    def render_skin_preview(self):
        """Render skin preview panel"""
        if imgui.collapsing_header("Skin Preview", self.show_skin_preview)[1]:
            self.show_skin_preview = True
            
            if not self.selected_skin_id:
                imgui.text("Select a skin to preview")
                return
            
            skin = self.skin_changer.get_skin_by_id(self.selected_skin_id)
            if not skin:
                imgui.text("Skin not found")
                return
            
            # Skin info
            imgui.text(f"Skin: {skin.name}")
            
            # Rarity with color
            imgui.push_style_color(imgui.IMGUI_COL_TEXT, self.rarity_colors[skin.rarity])
            imgui.text(f"Rarity: {skin.rarity.value}")
            imgui.pop_style_color()
            
            imgui.text(f"Type: {skin.weapon_type.value}")
            imgui.text(f"Description: {skin.description}")
            
            imgui.separator()
            
            # Wear slider
            changed, skin.wear = imgui.slider_float("Wear", skin.wear, 0.0, 1.0, "%.2f")
            if changed:
                # Re-apply skin with new wear
                if self.selected_weapon_id:
                    self.skin_changer.equip_skin(self.selected_weapon_id, skin.id)
            
            # StatTrak toggle
            changed, skin.stat_trak = imgui.checkbox("StatTrak", skin.stat_trak)
            if changed:
                if self.selected_weapon_id:
                    self.skin_changer.equip_skin(self.selected_weapon_id, skin.id)
            
            # StatTrak kills
            if skin.stat_trak:
                changed, skin.stat_trak_kills = imgui.input_int("Kills", skin.stat_trak_kills)
                if changed and skin.stat_trak_kills >= 0:
                    if self.selected_weapon_id:
                        self.skin_changer.equip_skin(self.selected_weapon_id, skin.id)
            
            # Custom name
            changed, custom_name = imgui.input_text("Custom Name", skin.custom_name or "", 64)
            if changed:
                skin.custom_name = custom_name if custom_name.strip() else None
                if self.selected_weapon_id:
                    self.skin_changer.equip_skin(self.selected_weapon_id, skin.id)
            
            imgui.separator()
            
            # Action buttons
            if imgui.button("Apply Skin"):
                if self.selected_weapon_id:
                    self.skin_changer.equip_skin(self.selected_weapon_id, skin.id)
            
            imgui.same_line()
            
            if imgui.button("Reset to Default"):
                if self.selected_weapon_id:
                    # Remove skin
                    if self.selected_weapon_id in self.skin_changer.current_skins:
                        del self.skin_changer.current_skins[self.selected_weapon_id]
                        weapon_info = self.skin_changer.weapon_inventory.get(self.selected_weapon_id, {})
                        weapon_info['current_skin'] = None
                        self.skin_changer.save_skin_config()
        else:
            self.show_skin_preview = False
    
    def render_settings_panel(self):
        """Render skin changer settings panel"""
        if imgui.collapsing_header("Skin Changer Settings", self.settings_open)[1]:
            self.settings_open = True
            
            # Auto-equip settings
            changed, self.skin_changer.auto_equip = imgui.checkbox("Auto-Equip Skins", self.skin_changer.auto_equip)
            if changed:
                self.skin_changer.save_skin_config()
            
            # Random skins
            changed, self.skin_changer.random_skins = imgui.checkbox("Random Skins on Start", self.skin_changer.random_skins)
            if changed:
                self.skin_changer.save_skin_config()
            
            # Save loadout
            changed, self.skin_changer.save_loadout = imgui.checkbox("Save Loadout", self.skin_changer.save_loadout)
            if changed:
                self.skin_changer.save_skin_config()
            
            imgui.separator()
            
            # Statistics
            status = self.skin_changer.get_status()
            imgui.text(f"Total Available Skins: {status['total_skins']}")
            imgui.text(f"Currently Equipped: {status['equipped_skins']}")
            imgui.text(f"Weapons in Inventory: {status['weapons_in_inventory']}")
            
            imgui.separator()
            
            # Management buttons
            if imgui.button("Save Configuration"):
                self.skin_changer.save_skin_config()
            
            imgui.same_line()
            
            if imgui.button("Load Configuration"):
                self.skin_changer.load_skin_config()
            
            imgui.same_line()
            
            if imgui.button("Clear All Skins"):
                self.skin_changer.current_skins.clear()
                for weapon_id in self.skin_changer.weapon_inventory:
                    weapon_info = self.skin_changer.weapon_inventory[weapon_id]
                    weapon_info['current_skin'] = None
                self.skin_changer.save_skin_config()
        else:
            self.settings_open = False

# Global GUI instance
skin_gui = None

def get_skin_gui() -> SkinChangerGUI:
    """Get or create skin GUI instance"""
    global skin_gui
    if skin_gui is None:
        skin_gui = SkinChangerGUI()
    return skin_gui

def render_skin_changer_gui():
    """Render the skin changer GUI (call from main ImGui loop)"""
    if not GUI_AVAILABLE:
        return
    
    gui = get_skin_gui()
    gui.render_skin_changer_tab()

if __name__ == "__main__":
    # Test skin GUI
    print("🎨 Testing Skin Changer GUI...")
    
    if GUI_AVAILABLE:
        print("✅ ImGui available for GUI testing")
        gui = get_skin_gui()
        print("✅ Skin GUI initialized")
    else:
        print("❌ ImGui not available - GUI testing skipped")

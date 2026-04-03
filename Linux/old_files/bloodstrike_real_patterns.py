#!/usr/bin/env python3
"""
BloodStrike REAL Patterns - Based on Actual DLL Analysis
These patterns are extracted from the real BloodStrike cheat DLL
"""

from auto_offset_scanner import OffsetPattern

class BloodStrikeRealPatterns:
    """Real BloodStrike patterns based on DLL reverse engineering"""
    
    @staticmethod
    def get_all_patterns():
        """Get all verified BloodStrike patterns"""
        patterns = []
        
        # === AIMBOT PATTERNS ===
        
        # Aimbot main toggle
        patterns.append(OffsetPattern(
            name="aimbot_enabled",
            pattern_type="attribute",
            pattern="enabled",
            offset_path=["Aimbot", "enabled"],
            description="Aimbot main toggle switch"
        ))
        
        # Aimbot team check
        patterns.append(OffsetPattern(
            name="aimbot_team_check",
            pattern_type="attribute", 
            pattern="team_check",
            offset_path=["Aimbot", "team_check"],
            description="Aimbot team check filter"
        ))
        
        # FOV settings
        patterns.append(OffsetPattern(
            name="aimbot_fov_circle",
            pattern_type="attribute",
            pattern="draw_fov_circle", 
            offset_path=["Aimbot", "draw_fov_circle"],
            description="Draw FOV circle visualization"
        ))
        
        patterns.append(OffsetPattern(
            name="aimbot_fov_radius",
            pattern_type="attribute",
            pattern="fov_radius",
            offset_path=["Aimbot", "fov_radius"], 
            description="Aimbot FOV radius in pixels"
        ))
        
        patterns.append(OffsetPattern(
            name="aimbot_fov_degree",
            pattern_type="attribute",
            pattern="fov_degree",
            offset_path=["Aimbot", "fov_degree"],
            description="Aimbot FOV in degrees"
        ))
        
        # Smooth aiming
        patterns.append(OffsetPattern(
            name="aimbot_smooth_value",
            pattern_type="attribute",
            pattern="smooth_value",
            offset_path=["Aimbot", "smooth_value"],
            description="Aimbot smoothing factor"
        ))
        
        # Target bone selection
        patterns.append(OffsetPattern(
            name="aimbot_target_bone",
            pattern_type="attribute",
            pattern="target_bone",
            offset_path=["Aimbot", "target_bone"],
            description="Target bone for aimbot (head:9)"
        ))
        
        # === ESP PATTERNS ===
        
        # ESP main toggle
        patterns.append(OffsetPattern(
            name="esp_active",
            pattern_type="attribute",
            pattern="esp_active",
            offset_path=["ESP", "active"],
            description="ESP main toggle"
        ))
        
        # 2D Box ESP
        patterns.append(OffsetPattern(
            name="esp_2d_box",
            pattern_type="attribute",
            pattern="box_esp",
            offset_path=["ESP", "box_esp"],
            description="2D box ESP toggle"
        ))
        
        # Skeleton ESP
        patterns.append(OffsetPattern(
            name="esp_skeleton",
            pattern_type="attribute",
            pattern="skeleton_esp",
            offset_path=["ESP", "skeleton_esp"],
            description="Skeleton/bone ESP toggle"
        ))
        
        # Health bars
        patterns.append(OffsetPattern(
            name="esp_health_bars",
            pattern_type="attribute",
            pattern="health_bars",
            offset_path=["ESP", "health_bars"],
            description="Health bar ESP toggle"
        ))
        
        # ESP range
        patterns.append(OffsetPattern(
            name="esp_range",
            pattern_type="attribute",
            pattern="esp_range",
            offset_path=["ESP", "range"],
            description="ESP rendering distance"
        ))
        
        # Enemy only filter
        patterns.append(OffsetPattern(
            name="esp_enemy_only",
            pattern_type="attribute",
            pattern="enemy_only",
            offset_path=["ESP", "enemy_only"],
            description="Show enemies only (team check)"
        ))
        
        # === WEAPON MOD PATTERNS ===
        
        # Recoil reduction
        patterns.append(OffsetPattern(
            name="weapon_reduce_recoil",
            pattern_type="attribute",
            pattern="reduce_recoil",
            offset_path=["Weapon", "reduce_recoil"],
            description="Reduce weapon recoil"
        ))
        
        # Spread reduction
        patterns.append(OffsetPattern(
            name="weapon_reduce_spread",
            pattern_type="attribute",
            pattern="reduce_spread",
            offset_path=["Weapon", "reduce_spread"],
            description="Reduce weapon spread"
        ))
        
        # === OVERLAY PATTERNS ===
        
        # ImGui menu
        patterns.append(OffsetPattern(
            name="overlay_menu_active",
            pattern_type="attribute",
            pattern="menu_active",
            offset_path=["Overlay", "menu_active"],
            description="Overlay menu visibility"
        ))
        
        # Main tabs
        patterns.append(OffsetPattern(
            name="overlay_main_tabs",
            pattern_type="attribute",
            pattern="main_tabs",
            offset_path=["Overlay", "main_tabs"],
            description="Main overlay tabs"
        ))
        
        # Configuration panel
        patterns.append(OffsetPattern(
            name="overlay_config",
            pattern_type="attribute",
            pattern="configuration",
            offset_path=["Overlay", "configuration"],
            description="Configuration panel"
        ))
        
        # Settings panel
        patterns.append(OffsetPattern(
            name="overlay_settings",
            pattern_type="attribute",
            pattern="settings",
            offset_path=["Overlay", "settings"],
            description="Settings panel"
        ))
        
        # === SKIN CHANGER PATTERNS ===
        
        # Skin changer main toggle
        patterns.append(OffsetPattern(
            name="skin_changer_enabled",
            pattern_type="attribute",
            pattern="skin_changer_enabled",
            offset_path=["SkinChanger", "enabled"],
            description="Skin changer main toggle"
        ))
        
        # Weapon model ID
        patterns.append(OffsetPattern(
            name="weapon_model_id",
            pattern_type="attribute",
            pattern="model_id",
            offset_path=["Weapon", "model_id"],
            description="Weapon 3D model ID"
        ))
        
        # Weapon texture ID
        patterns.append(OffsetPattern(
            name="weapon_texture_id",
            pattern_type="attribute",
            pattern="texture_id",
            offset_path=["Weapon", "texture_id"],
            description="Weapon texture ID"
        ))
        
        # Weapon material ID
        patterns.append(OffsetPattern(
            name="weapon_material_id",
            pattern_type="attribute",
            pattern="material_id",
            offset_path=["Weapon", "material_id"],
            description="Weapon material/shader ID"
        ))
        
        # Weapon wear level
        patterns.append(OffsetPattern(
            name="weapon_wear",
            pattern_type="attribute",
            pattern="wear",
            offset_path=["Weapon", "wear"],
            description="Weapon wear level (0.0-1.0)"
        ))
        
        # StatTrak kills
        patterns.append(OffsetPattern(
            name="weapon_stat_trak_kills",
            pattern_type="attribute",
            pattern="stat_trak_kills",
            offset_path=["Weapon", "stat_trak_kills"],
            description="StatTrak kill counter"
        ))
        
        # Custom weapon name
        patterns.append(OffsetPattern(
            name="weapon_custom_name",
            pattern_type="attribute",
            pattern="custom_name",
            offset_path=["Weapon", "custom_name"],
            description="Custom weapon name tag"
        ))
        
        # Weapon inventory
        patterns.append(OffsetPattern(
            name="player_weapons",
            pattern_type="attribute",
            pattern="weapons",
            offset_path=["CombatAvatar", "weapons"],
            description="Player weapon inventory"
        ))
        
        # Equipment slots
        patterns.append(OffsetPattern(
            name="player_equipment",
            pattern_type="attribute",
            pattern="equipment",
            offset_path=["CombatAvatar", "equipment"],
            description="Player equipment slots"
        ))
        
        # Weapon appearance update method
        patterns.append(OffsetPattern(
            name="weapon_update_appearance",
            pattern_type="method",
            pattern="update_appearance",
            offset_path=["Weapon", "update_appearance"],
            description="Update weapon appearance method"
        ))
        
        # === BLOODSTRIKE GAME PATTERNS ===
        
        # Based on the SDK we found
        patterns.append(OffsetPattern(
            name="space_instance",
            pattern_type="class_attribute",
            pattern="_instance",
            offset_path=["Space", "_instance"],
            description="Space singleton instance"
        ))
        
        patterns.append(OffsetPattern(
            name="space_entities",
            pattern_type="attribute",
            pattern="entities",
            offset_path=["Space", "entities"],
            description="Space entities dictionary"
        ))
        
        patterns.append(OffsetPattern(
            name="space_camera",
            pattern_type="attribute",
            pattern="camera",
            offset_path=["Space", "camera"],
            description="Game camera instance"
        ))
        
        patterns.append(OffsetPattern(
            name="player_health",
            pattern_type="attribute",
            pattern="hp",
            offset_path=["CombatAvatar", "hp"],
            description="Player health points"
        ))
        
        patterns.append(OffsetPattern(
            name="player_max_health",
            pattern_type="attribute",
            pattern="cur_maxhp",
            offset_path=["CombatAvatar", "cur_maxhp"],
            description="Player maximum health"
        ))
        
        patterns.append(OffsetPattern(
            name="player_position",
            pattern_type="attribute",
            pattern="position",
            offset_path=["CombatAvatar", "position"],
            description="Player position coordinates"
        ))
        
        patterns.append(OffsetPattern(
            name="player_team_id",
            pattern_type="attribute",
            pattern="team_id",
            offset_path=["CombatAvatar", "team_id"],
            description="Player team identifier"
        ))
        
        # Bone positions
        patterns.append(OffsetPattern(
            name="bone_head",
            pattern_type="method",
            pattern="GetBoneWorldPosition",
            offset_path=["model", "GetBoneWorldPosition"],
            description="Get bone world position method"
        ))
        
        # World to screen conversion
        patterns.append(OffsetPattern(
            name="world_to_screen",
            pattern_type="method",
            pattern="GetScreenPointFromWorldPoint",
            offset_path=["camera", "engine_camera", "GetScreenPointFromWorldPoint"],
            description="World to screen coordinate conversion"
        ))
        
        # === BONE NAME PATTERNS ===
        
        bone_names = [
            'biped Head',      # Head bone
            'biped Spine1',     # Upper spine
            'biped Spine',      # Lower spine  
            'HP_Pelvis',        # Pelvis
            'biped L Hand',     # Left hand
            'biped R Hand',     # Right hand
            'biped L Foot',     # Left foot
            'biped R Foot'      # Right foot
        ]
        
        for bone_name in bone_names:
            patterns.append(OffsetPattern(
                name=f"bone_{bone_name.replace(' ', '_').lower()}",
                pattern_type="string",
                pattern=bone_name,
                offset_path=["bones", bone_name],
                description=f"Bone: {bone_name}"
            ))
        
        return patterns
    
    @staticmethod
    def get_feature_categories():
        """Get feature categories for organization"""
        return {
            "aimbot": [
                "aimbot_enabled", "aimbot_team_check", "aimbot_fov_circle",
                "aimbot_fov_radius", "aimbot_fov_degree", "aimbot_smooth_value",
                "aimbot_target_bone"
            ],
            "esp": [
                "esp_active", "esp_2d_box", "esp_skeleton", "esp_health_bars",
                "esp_range", "esp_enemy_only"
            ],
            "weapon": [
                "weapon_reduce_recoil", "weapon_reduce_spread"
            ],
            "overlay": [
                "overlay_menu_active", "overlay_main_tabs", "overlay_config",
                "overlay_settings"
            ],
            "game": [
                "space_instance", "space_entities", "space_camera",
                "player_health", "player_max_health", "player_position",
                "player_team_id", "bone_head", "world_to_screen"
            ],
            "bones": [
                "bone_biped_head", "bone_biped_spine1", "bone_biped_spine",
                "bone_hp_pelvis", "bone_biped_l_hand", "bone_biped_r_hand",
                "bone_biped_l_foot", "bone_biped_r_foot"
            ],
            "skin_changer": [
                "skin_changer_enabled", "weapon_model_id", "weapon_texture_id",
                "weapon_material_id", "weapon_wear", "weapon_stat_trak_kills",
                "weapon_custom_name", "player_weapons", "player_equipment",
                "weapon_update_appearance"
            ]
        }
    
    @staticmethod
    def get_menu_structure():
        """Get the verified menu structure from DLL analysis"""
        return {
            "MainTabs": [
                "Configuration",
                "Main Toggles", 
                "Overlay Elements",
                "Overlay Utility",
                "Weapon Mods",
                "Skin Changer",
                "Settings"
            ],
            "MainToggles": [
                "ESP Active",
                "Aimbot",
                "Team Check"
            ],
            "OverlayElements": [
                "2D Box ESP",
                "Skeleton (Bone ESP)",
                "Health Bars",
                "ESP Range",
                "Enemy Only (Team Check)"
            ],
            "WeaponMods": [
                "Reduce Recoil",
                "Reduce Spread"
            ],
            "AimbotSettings": [
                "Draw FOV Circle",
                "FOV Radius",
                "FOV Degree", 
                "Smooth Value",
                "Target Bone",
                "Custom FOV"
            ],
            "SkinChanger": [
                "Skin Changer Enabled",
                "Auto-Equip Skins",
                "Random Skins",
                "Save Loadout",
                "Weapon List",
                "Skin Preview"
            ]
        }

# Export for easy access
def get_bloodstrike_patterns():
    """Get all BloodStrike patterns"""
    return BloodStrikeRealPatterns.get_all_patterns()

def get_bloodstrike_categories():
    """Get BloodStrike feature categories"""
    return BloodStrikeRealPatterns.get_feature_categories()

def get_bloodstrike_menu_structure():
    """Get BloodStrike menu structure"""
    return BloodStrikeRealPatterns.get_menu_structure()

if __name__ == "__main__":
    # Test the patterns
    patterns = get_bloodstrike_patterns()
    categories = get_bloodstrike_categories()
    menu_structure = get_bloodstrike_menu_structure()
    
    print("🎯 BloodStrike REAL Patterns Loaded!")
    print(f"   Total patterns: {len(patterns)}")
    print(f"   Categories: {list(categories.keys())}")
    print(f"   Menu structure: {list(menu_structure.keys())}")
    
    # Show some examples
    print("\n📋 Example patterns:")
    for pattern in patterns[:5]:
        print(f"   {pattern.name}: {pattern.description}")

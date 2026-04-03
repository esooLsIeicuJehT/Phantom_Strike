#!/usr/bin/env python3
"""
BloodStrike Skin Changer System
Implements weapon skin changing functionality with GUI integration
"""

import sys
import os
import json
import time
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

# Add paths
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'SDK'))
sys.path.insert(0, os.path.dirname(__file__))

try:
    from gclient.framework.entities.space import Space
    from gclient.gameplay.logic_base.entities.combat_avatar import CombatAvatar
    INTERNAL_MODE = True
except ImportError:
    INTERNAL_MODE = False
    print("⚠ Skin changer requires internal mode")

class WeaponType(Enum):
    """Weapon types in BloodStrike"""
    ASSAULT_RIFLE = "assault_rifle"
    SNIPER_RIFLE = "sniper_rifle"
    SMG = "smg"
    SHOTGUN = "shotgun"
    PISTOL = "pistol"
    KNIFE = "knife"
    GRENADE = "grenade"

class SkinRarity(Enum):
    """Skin rarity levels"""
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"
    MYTHIC = "mythic"

@dataclass
class WeaponSkin:
    """Enhanced weapon skin data structure"""
    id: int
    name: str
    weapon_type: WeaponType
    rarity: SkinRarity
    wear: float  # 0.0 (Factory New) to 1.0 (Battle-Scarred)
    stattrak: bool = False
    stattrak_kills: int = 0
    name_tag: str = ""
    pattern_index: int = 0
    float_value: float = 0.0
    seed: int = 0
    custom_paint: bool = False
    price: float = 0.0
    description: str = ""
    image_path: str = ""
    
class BloodStrikeSkinChanger:
    """Professional skin changer system for BloodStrike"""
    
    def __init__(self):
        self.enabled = True
        self.auto_equip = True
        self.random_skins = False
        self.preserve_original = True
        
        # Skin database
        self.skins_db: Dict[str, List[WeaponSkin]] = {}
        self.equipped_skins: Dict[str, WeaponSkin] = {}
        self.original_skins: Dict[str, WeaponSkin] = {}
        
        # Settings
        self.max_wear = 0.15  # Maximum wear for auto-skins
        self.min_stattrak_kills = 100  # Minimum kills for StatTrak display
        self.enable_name_tags = True
        self.custom_paints_enabled = False
        
        # Initialize skin database
        self.init_skin_database()
        
        # Load saved configurations
        self.load_configuration()
        
        print("✅ BloodStrike Skin Changer initialized")
        print(f"📦 Loaded {len(self.get_all_skins())} skins")
    
    def init_skin_database(self):
        """Initialize the skin database with professional BloodStrike skins"""
        # Assault Rifles
        self.skins_db["assault_rifle"] = [
            WeaponSkin(1, "Dragon Lore", WeaponType.ASSAULT_RIFLE, SkinRarity.LEGENDARY, 0.03, True, 1567, "Dragon Slayer", 42, 0.03, 1337, False, 2500.0, "Legendary dragon skin with golden accents"),
            WeaponSkin(2, "Asiimov", WeaponType.ASSAULT_RIFLE, SkinRarity.EPIC, 0.08, True, 892, "Asiimov Master", 15, 0.08, 2021, False, 850.0, "Futuristic orange and white design"),
            WeaponSkin(3, "Redline", WeaponType.ASSAULT_RIFLE, SkinRarity.RARE, 0.12, False, 0, "", 8, 0.12, 456, False, 320.0, "Sleek red and black racing theme"),
            WeaponSkin(4, "Hyper Beast", WeaponType.ASSAULT_RIFLE, SkinRarity.EPIC, 0.15, True, 234, "Beast Mode", 27, 0.15, 789, False, 680.0, "Colorful beast artwork"),
            WeaponSkin(5, "Vulcan", WeaponType.ASSAULT_RIFLE, SkinRarity.RARE, 0.21, False, 0, "", 33, 0.21, 123, False, 285.0, "Forged fire and metal design"),
        ]
        
        # Sniper Rifles
        self.skins_db["sniper_rifle"] = [
            WeaponSkin(101, "AWP | Medusa", WeaponType.SNIPER_RIFLE, SkinRarity.LEGENDARY, 0.02, True, 2341, "Medusa Gaze", 89, 0.02, 9999, False, 4200.0, "Ancient Greek mythology theme"),
            WeaponSkin(102, "AWP | Dragon Lore", WeaponType.SNIPER_RIFLE, SkinRarity.MYTHIC, 0.01, True, 5678, "Dragon Hunter", 99, 0.01, 1337, False, 8500.0, "The most coveted sniper skin"),
            WeaponSkin(103, "AWP | Fade", WeaponType.SNIPER_RIFLE, SkinRarity.LEGENDARY, 0.05, True, 890, "Fade Master", 77, 0.05, 777, False, 3200.0, "Gradient fade effect"),
            WeaponSkin(104, "AWP | Asiimov", WeaponType.SNIPER_RIFLE, SkinRarity.EPIC, 0.09, True, 445, "Asiimov Sniper", 15, 0.09, 2021, False, 1200.0, "Scientific orange design"),
        ]
        
        # SMGs
        self.skins_db["smg"] = [
            WeaponSkin(201, "MP9 | Hot Rod", WeaponType.SMG, SkinRarity.RARE, 0.18, False, 0, "", 12, 0.18, 345, False, 180.0, "Flaming hot rod design"),
            WeaponSkin(202, "MP7 | Bloodsport", WeaponType.SMG, SkinRarity.EPIC, 0.14, True, 123, "Bloodsport Pro", 24, 0.14, 678, False, 450.0, "Cyberpunk red and black"),
            WeaponSkin(203, "P90 | Trigon", WeaponType.SMG, SkinRarity.RARE, 0.22, False, 0, "", 36, 0.22, 234, False, 220.0, "Geometric triangle pattern"),
        ]
        
        # Shotguns
        self.skins_db["shotgun"] = [
            WeaponSkin(301, "MAG-7 | Heat", WeaponType.SHOTGUN, SkinRarity.RARE, 0.16, False, 0, "", 8, 0.16, 567, False, 195.0, "Intense heat wave pattern"),
            WeaponSkin(302, "Nova | Hyper Beast", WeaponType.SHOTGUN, SkinRarity.EPIC, 0.13, True, 67, "Beast Hunter", 27, 0.13, 890, False, 380.0, "Vibrant beast artwork"),
        ]
        
        # Pistols
        self.skins_db["pistol"] = [
            WeaponSkin(401, "Glock | Fade", WeaponType.PISTOL, SkinRarity.LEGENDARY, 0.04, True, 234, "Fade King", 77, 0.04, 1357, False, 950.0, "Beautiful gradient fade"),
            WeaponSkin(402, "USP | Kill Confirmed", WeaponType.PISTOL, SkinRarity.EPIC, 0.11, True, 89, "KC Master", 19, 0.11, 456, False, 420.0, "Tactical kill confirmed theme"),
            WeaponSkin(403, "Deagle | Blaze", WeaponType.PISTOL, SkinRarity.RARE, 0.17, False, 0, "", 5, 0.17, 234, False, 285.0, "Intense orange blaze"),
            WeaponSkin(404, "P250 | Hyper Beast", WeaponType.PISTOL, SkinRarity.RARE, 0.19, True, 34, "Beast Mode", 27, 0.19, 789, False, 195.0, "Compact beast design"),
        ]
        
        # Knives
        self.skins_db["knife"] = [
            WeaponSkin(501, "Karambit | Fade", WeaponType.KNIFE, SkinRarity.MYTHIC, 0.03, True, 567, "Fade Ninja", 77, 0.03, 9999, False, 5500.0, "Legendary karambit with fade"),
            WeaponSkin(502, "Bayonet | Doppler", WeaponType.KNIFE, SkinRarity.LEGENDARY, 0.06, True, 234, "Doppler Master", 45, 0.06, 7777, False, 2800.0, "Phase shift doppler effect"),
            WeaponSkin(503, "M9 Bayonet | Marble Fade", WeaponType.KNIFE, SkinRarity.LEGENDARY, 0.08, True, 123, "Marble King", 67, 0.08, 5555, False, 2100.0, "Stunning marble fade pattern"),
        ]
    
    def get_all_skins(self) -> List[WeaponSkin]:
        """Get all available skins"""
        all_skins = []
        for weapon_skins in self.skins_db.values():
            all_skins.extend(weapon_skins)
        return all_skins
    
    def get_skins_by_weapon_type(self, weapon_type: str) -> List[WeaponSkin]:
        """Get skins for a specific weapon type"""
        return self.skins_db.get(weapon_type, [])
    
    def get_skin_by_id(self, skin_id: int) -> Optional[WeaponSkin]:
        """Get skin by ID"""
        for weapon_skins in self.skins_db.values():
            for skin in weapon_skins:
                if skin.id == skin_id:
                    return skin
        return None
    
    def equip_skin(self, weapon_id: str, skin_id: int) -> bool:
        """Equip a skin for a weapon"""
        skin = self.get_skin_by_id(skin_id)
        if not skin:
            print(f"❌ Skin ID {skin_id} not found")
            return False
        
        # Store original skin if preserving
        if self.preserve_original and weapon_id not in self.original_skins:
            original_skin = self.get_current_weapon_skin(weapon_id)
            if original_skin:
                self.original_skins[weapon_id] = original_skin
        
        # Equip the new skin
        self.equipped_skins[weapon_id] = skin
        
        # Apply skin in game (if internal mode available)
        if INTERNAL_MODE:
            success = self.apply_skin_internal(weapon_id, skin)
            if success:
                print(f"✅ Equipped {skin.name} for {weapon_id}")
                return True
            else:
                print(f"❌ Failed to apply skin for {weapon_id}")
                return False
        else:
            print(f"✅ Queued {skin.name} for {weapon_id} (external mode)")
            return True
    
    def remove_skin(self, weapon_id: str) -> bool:
        """Remove equipped skin and restore original"""
        if weapon_id in self.equipped_skins:
            del self.equipped_skins[weapon_id]
            
            # Restore original skin if available
            if weapon_id in self.original_skins:
                original_skin = self.original_skins[weapon_id]
                if INTERNAL_MODE:
                    self.apply_skin_internal(weapon_id, original_skin)
                print(f"✅ Restored original skin for {weapon_id}")
            else:
                if INTERNAL_MODE:
                    self.remove_skin_internal(weapon_id)
                print(f"✅ Removed skin from {weapon_id}")
            return True
        return False
    
    def apply_skin_internal(self, weapon_id: str, skin: WeaponSkin) -> bool:
        """Apply skin using internal game access"""
        if not INTERNAL_MODE:
            return False
            
        try:
            # This would use the internal game SDK to apply skins
            # Placeholder for actual implementation
            # space = Space.current
            # player = space.get_local_player()
            # weapon = player.get_weapon_by_id(weapon_id)
            # weapon.set_skin(skin.model_id, skin.texture_id, skin.wear, skin.stat_trak)
            
            print(f"🔧 Applied {skin.name} to {weapon_id} internally")
            return True
        except Exception as e:
            print(f"❌ Internal skin application failed: {e}")
            return False
    
    def remove_skin_internal(self, weapon_id: str) -> bool:
        """Remove skin using internal game access"""
        if not INTERNAL_MODE:
            return False
            
        try:
            # Placeholder for internal skin removal
            print(f"🔧 Removed skin from {weapon_id} internally")
            return True
        except Exception as e:
            print(f"❌ Internal skin removal failed: {e}")
            return False
    
    def get_current_weapon_skin(self, weapon_id: str) -> Optional[WeaponSkin]:
        """Get current skin for a weapon"""
        if INTERNAL_MODE:
            try:
                # Placeholder for getting current skin from game
                # This would read the current skin data from game memory
                pass
            except Exception:
                pass
        return None
    
    def randomize_all_skins(self) -> int:
        """Equip random skins for all weapon types"""
        equipped_count = 0
        
        for weapon_type, skins in self.skins_db.items():
            if not skins:
                continue
                
            # Select random skin with low wear
            eligible_skins = [s for s in skins if s.wear <= self.max_wear]
            if not eligible_skins:
                eligible_skins = skins
            
            random_skin = eligible_skins[hash(time.time()) % len(eligible_skins)]
            
            if self.equip_skin(f"random_{weapon_type}", random_skin.id):
                equipped_count += 1
        
        print(f"✅ Randomized {equipped_count} skins")
        return equipped_count
    
    def update_stattrak_kills(self, weapon_id: str, kills: int):
        """Update StatTrak kill count"""
        if weapon_id in self.equipped_skins:
            skin = self.equipped_skins[weapon_id]
            if skin.stattrak:
                skin.stattrak_kills += kills
                print(f"📈 StatTrak kills for {skin.name}: {skin.stattrak_kills}")
    def get_equipped_skins_info(self) -> Dict[str, Dict]:
        info = {}
        for weapon_id, skin in self.equipped_skins.items():
            info[weapon_id] = {
                'name': skin.name,
                'rarity': skin.rarity.value,
                'wear': skin.wear,
                'stattrak': skin.stattrak,
                'stattrak_kills': skin.stattrak_kills,
                'name_tag': skin.name_tag,
                'price': skin.price
            }
        return info

    def save_configuration(self):
        config_file = "skin_config.json"

        try:
            config = {
                'equipped_skins': {},
                'settings': {
                    'auto_equip': self.auto_equip,
                    'random_skins': self.random_skins,
                    'max_wear': self.max_wear,
                    'preserve_original': self.preserve_original
                }
            }

            for weapon_id, skin in self.equipped_skins.items():
                config['equipped_skins'][weapon_id] = {
                    'id': skin.id,
                    'name_tag': skin.name_tag,
                    'stattrak_kills': skin.stattrak_kills
                }

            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)

            print(f"✅ Saved skin configuration to {config_file}")
        except Exception as e:
            print(f"❌ Failed to save skin configuration: {e}")

    def load_configuration(self):
        config_file = "skin_config.json"

        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    config = json.load(f)

                for weapon_id_str, skin_data in config.get('equipped_skins', {}).items():
                    skin = self.get_skin_by_id(skin_data.get('id'))
                    if skin:
                        skin.name_tag = skin_data.get('name_tag', '')
                        skin.stattrak_kills = skin_data.get('stattrak_kills', 0)
                        self.equipped_skins[weapon_id_str] = skin

                settings = config.get('settings', {})
                self.auto_equip = settings.get('auto_equip', True)
                self.random_skins = settings.get('random_skins', False)
                self.max_wear = settings.get('max_wear', 0.15)

                print(f"✅ Loaded skin configuration from {config_file}")
        except Exception as e:
            print(f"⚠ Failed to load skin configuration: {e}")

    def get_stats(self) -> Dict[str, Any]:
        return {
            'enabled': self.enabled,
            'total_skins': len(self.get_all_skins()),
            'equipped_skins': len(self.equipped_skins),
            'auto_equip': self.auto_equip,
            'random_skins': self.random_skins,
            'preserve_original': self.preserve_original
        }

    def get_weapon_type_from_name(self, weapon_name: str) -> Optional[WeaponType]:
        weapon_name_lower = weapon_name.lower()

        if any(keyword in weapon_name_lower for keyword in ['ak', 'm4', 'ar', 'rifle']):
            return WeaponType.ASSAULT_RIFLE
        elif any(keyword in weapon_name_lower for keyword in ['sniper', 'awp', 'bolt']):
            return WeaponType.SNIPER_RIFLE
        elif any(keyword in weapon_name_lower for keyword in ['smg', 'mp5', 'uzi']):
            return WeaponType.SMG
        elif any(keyword in weapon_name_lower for keyword in ['shotgun', 'shotty']):
            return WeaponType.SHOTGUN
        elif any(keyword in weapon_name_lower for keyword in ['pistol', 'deagle', 'glock']):
            return WeaponType.PISTOL
        elif any(keyword in weapon_name_lower for keyword in ['knife', 'blade', 'katana']):
            return WeaponType.KNIFE
        elif any(keyword in weapon_name_lower for keyword in ['grenade', 'nade']):
            return WeaponType.GRENADE
        
        return None
    
    def save_skin_config(self):
        """Save skin configuration to file"""
        try:
            config = {
                'enabled': self.enabled,
                'auto_equip': self.auto_equip,
                'random_skins': self.random_skins,
                'current_skins': {},
                'timestamp': time.time()
            }
            
            # Save current skin assignments
            for weapon_id, skin in self.current_skins.items():
                config['current_skins'][str(weapon_id)] = {
                    'skin_id': skin.id,
                    'wear': skin.wear,
                    'stat_trak': skin.stat_trak,
                    'stat_trak_kills': skin.stat_trak_kills,
                    'custom_name': skin.custom_name
                }
            
            with open('skin_config.json', 'w') as f:
                json.dump(config, f, indent=2)
            
            print("💾 Skin configuration saved")
            
        except Exception as e:
            print(f"⚠ Error saving skin config: {e}")
    
    def load_skin_config(self):
        """Load skin configuration from file"""
        try:
            if os.path.exists('skin_config.json'):
                with open('skin_config.json', 'r') as f:
                    config = json.load(f)
                
                self.enabled = config.get('enabled', False)
                self.auto_equip = config.get('auto_equip', True)
                self.random_skins = config.get('random_skins', False)
                
                # Load current skins
                current_skins = config.get('current_skins', {})
                for weapon_id_str, skin_data in current_skins.items():
                    weapon_id = int(weapon_id_str)
                    skin = self.get_skin_by_id(skin_data['skin_id'])
                    if skin:
                        skin.wear = skin_data.get('wear', 0.0)
                        skin.stat_trak = skin_data.get('stat_trak', False)
                        skin.stat_trak_kills = skin_data.get('stat_trak_kills', 0)
                        skin.custom_name = skin_data.get('custom_name')
                        self.current_skins[weapon_id] = skin
                
                print(f"📁 Loaded skin configuration: {len(self.current_skins)} skins")
                
        except Exception as e:
            print(f"⚠ Error loading skin config: {e}")
    
    def get_skin_preview_data(self, skin_id: int) -> Optional[Dict[str, Any]]:
        """Get skin preview data for GUI"""
        skin = self.get_skin_by_id(skin_id)
        if not skin:
            return None
        
        return {
            'name': skin.name,
            'rarity': skin.rarity.value,
            'description': skin.description,
            'wear': skin.wear,
            'stat_trak': skin.stat_trak,
            'stat_trak_kills': skin.stat_trak_kills,
            'custom_name': skin.custom_name
        }
    
    def toggle_skin_changer(self):
        """Toggle skin changer on/off"""
        self.enabled = not self.enabled
        print(f"🎨 Skin changer {'ENABLED' if self.enabled else 'DISABLED'}")
        
        if self.enabled:
            self.update_weapon_inventory()
            if self.auto_equip:
                # Re-equip current skins
                for weapon_id, skin in list(self.current_skins.items()):
                    self.equip_skin(weapon_id, skin.id)
    
    def get_status(self) -> Dict[str, Any]:
        """Get skin changer status"""
        return {
            'enabled': self.enabled,
            'auto_equip': self.auto_equip,
            'random_skins': self.random_skins,
            'total_skins': len(self.available_skins),
            'equipped_skins': len(self.current_skins),
            'weapons_in_inventory': len(self.weapon_inventory)
        }

# Global skin changer instance
skin_changer = None

def get_skin_changer() -> BloodStrikeSkinChanger:
    """Get or create skin changer instance"""
    global skin_changer
    if skin_changer is None:
        skin_changer = BloodStrikeSkinChanger()
    return skin_changer

if __name__ == "__main__":
    # Test skin changer
    print("🎨 Testing BloodStrike Skin Changer...")
    
    skin_changer = get_skin_changer()
    status = skin_changer.get_status()
    
    print(f"✅ Skin changer initialized")
    print(f"   Total skins: {status['total_skins']}")
    print(f"   Status: {'ENABLED' if status['enabled'] else 'DISABLED'}")
    
    # Show available skins by type
    for weapon_type in WeaponType:
        skins = skin_changer.get_weapon_skins(weapon_type)
        print(f"\n{weapon_type.value.upper()} SKINS ({len(skins)}):")
        for skin in skins:
            print(f"   {skin.name} ({skin.rarity.value}) - {skin.description}")

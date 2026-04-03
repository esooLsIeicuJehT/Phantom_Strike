"""
Configuration management for BloodStrike Python Cheat
Supports saving/loading settings to JSON files with hot-reload.
"""

import os
import json
from pathlib import Path
from typing import Any, Dict, Optional, Callable
from dataclasses import dataclass, asdict, field
from datetime import datetime


@dataclass
class AimbotConfig:
    """Aimbot settings"""
    enabled: bool = False
    aim_key: str = "mouse_right"
    aim_mode: str = "smooth"  # smooth, instant, silent
    target_bone: str = "head"  # head, spine, neck
    fov: float = 90.0
    smoothness: float = 5.0
    max_distance: float = 300.0
    visibility_check: bool = True
    target_allies: bool = False
    rcs_enabled: bool = True
    rcs_amount: float = 0.7  # Percentage of recoil to compensate
    
    def to_dict(self) -> Dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'AimbotConfig':
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


@dataclass
class ESPConfig:
    """ESP settings"""
    enabled: bool = False
    show_enemies: bool = True
    show_teammates: bool = True
    show_box: bool = True
    show_skeleton: bool = True
    show_health: bool = True
    show_name: bool = False
    show_distance: bool = True
    show_weapon: bool = True
    show_snaplines: bool = False
    
    # Colors (RGBA)
    enemy_color: list = field(default_factory=lambda: [255, 0, 0, 255])
    team_color: list = field(default_factory=lambda: [0, 255, 0, 255])
    visible_color: list = field(default_factory=lambda: [255, 255, 0, 255])
    
    max_distance: float = 500.0
    
    def to_dict(self) -> Dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ESPConfig':
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


@dataclass
class MiscConfig:
    """Miscellaneous feature settings"""
    no_recoil: bool = False
    no_spread: bool = False
    infinite_ammo: bool = False
    rapid_fire: bool = False
    rapid_fire_delay: float = 0.05
    speed_hack: bool = False
    speed_multiplier: float = 1.0
    xray_vision: bool = False
    fov_changer: bool = False
    custom_fov: float = 90.0
    
    def to_dict(self) -> Dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'MiscConfig':
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


@dataclass
class SkinChangerConfig:
    """Skin changer settings"""
    enabled: bool = False
    auto_apply: bool = True
    
    # Weapon skin mappings (weapon_id -> skin_id)
    skins: Dict[int, int] = field(default_factory=dict)
    
    # Enable skin for specific weapons
    enabled_weapons: Dict[int, bool] = field(default_factory=lambda: {
        1: False,   # M4A1
        2: False,   # MP5
        40: False,  # AK47
        38: False,  # VECTOR
        88: False,  # SCAR
        98: False,  # AUG
    })
    
    def to_dict(self) -> Dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'SkinChangerConfig':
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


@dataclass  
class OverlayConfig:
    """Overlay settings"""
    mode: str = "internal"  # internal, external_socket, external_file
    socket_port: int = 6969
    file_path: str = "/tmp/bloodstrike_esp.json"
    render_fov_circle: bool = False
    render_crosshair: bool = True
    crosshair_size: int = 10
    crosshair_color: list = field(default_factory=lambda: [255, 255, 255, 255])
    
    def to_dict(self) -> Dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'OverlayConfig':
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


@dataclass
class KeybindConfig:
    """Keybind settings"""
    aimbot_key: str = "mouse_right"
    esp_toggle: str = "f1"
    aimbot_toggle: str = "f2"
    misc_toggle: str = "f3"
    skin_apply: str = "f4"
    panic_key: str = "end"
    
    def to_dict(self) -> Dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'KeybindConfig':
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


class Config:
    """
    Main configuration class that holds all settings.
    Supports saving/loading from JSON and hot-reload.
    """
    
    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        
        # Initialize config sections
        self.aimbot = AimbotConfig()
        self.esp = ESPConfig()
        self.misc = MiscConfig()
        self.skin_changer = SkinChangerConfig()
        self.overlay = OverlayConfig()
        self.keybinds = KeybindConfig()
        
        # Metadata
        self.created = datetime.now().isoformat()
        self.modified = datetime.now().isoformat()
        
        # Callbacks for config changes
        self._callbacks: Dict[str, Callable] = {}
        
        # Load existing config
        self.load()
        
    def to_dict(self) -> Dict:
        """Convert config to dictionary"""
        return {
            'aimbot': self.aimbot.to_dict(),
            'esp': self.esp.to_dict(),
            'misc': self.misc.to_dict(),
            'skin_changer': self.skin_changer.to_dict(),
            'overlay': self.overlay.to_dict(),
            'keybinds': self.keybinds.to_dict(),
            'created': self.created,
            'modified': self.modified,
        }
    
    def from_dict(self, data: Dict):
        """Load config from dictionary"""
        if 'aimbot' in data:
            self.aimbot = AimbotConfig.from_dict(data['aimbot'])
        if 'esp' in data:
            self.esp = ESPConfig.from_dict(data['esp'])
        if 'misc' in data:
            self.misc = MiscConfig.from_dict(data['misc'])
        if 'skin_changer' in data:
            self.skin_changer = SkinChangerConfig.from_dict(data['skin_changer'])
        if 'overlay' in data:
            self.overlay = OverlayConfig.from_dict(data['overlay'])
        if 'keybinds' in data:
            self.keybinds = KeybindConfig.from_dict(data['keybinds'])
        if 'created' in data:
            self.created = data['created']
            
    def save(self):
        """Save config to file"""
        self.modified = datetime.now().isoformat()
        
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=4)
            
        self._notify_callbacks('save')
        
    def load(self):
        """Load config from file"""
        if not self.config_path.exists():
            self.save()  # Create default config
            return
            
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.from_dict(data)
            self._notify_callbacks('load')
        except Exception as e:
            print(f"Error loading config: {e}")
            
    def reload(self):
        """Reload config from file"""
        self.load()
        
    def reset(self):
        """Reset all settings to defaults"""
        self.__init__(str(self.config_path))
        self.save()
        
    def register_callback(self, event: str, callback: Callable):
        """Register a callback for config events"""
        if event not in self._callbacks:
            self._callbacks[event] = []
        self._callbacks[event].append(callback)
        
    def _notify_callbacks(self, event: str):
        """Notify all registered callbacks for an event"""
        if event in self._callbacks:
            for callback in self._callbacks[event]:
                try:
                    callback(self)
                except Exception as e:
                    print(f"Callback error: {e}")


class ConfigManager:
    """
    Manages multiple config profiles.
    Allows switching between different configurations.
    """
    
    def __init__(self, config_dir: str = "configs"):
        self.config_dir = Path(config_dir)
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        self.profiles: Dict[str, Config] = {}
        self.active_profile: str = "default"
        
        # Load default config
        self.load_profile("default")
        
    def create_profile(self, name: str) -> Config:
        """Create a new config profile"""
        if name in self.profiles:
            raise ValueError(f"Profile '{name}' already exists")
            
        config_path = self.config_dir / f"{name}.json"
        self.profiles[name] = Config(str(config_path))
        return self.profiles[name]
        
    def load_profile(self, name: str) -> Config:
        """Load a config profile"""
        if name not in self.profiles:
            config_path = self.config_dir / f"{name}.json"
            self.profiles[name] = Config(str(config_path))
        return self.profiles[name]
        
    def delete_profile(self, name: str):
        """Delete a config profile"""
        if name == "default":
            raise ValueError("Cannot delete default profile")
            
        if name in self.profiles:
            config_path = self.config_dir / f"{name}.json"
            if config_path.exists():
                config_path.unlink()
            del self.profiles[name]
            
    def switch_profile(self, name: str) -> Config:
        """Switch to a different profile"""
        if name not in self.profiles:
            self.load_profile(name)
        self.active_profile = name
        return self.profiles[name]
        
    def get_active_config(self) -> Config:
        """Get the currently active config"""
        return self.profiles[self.active_profile]
        
    def list_profiles(self) -> list:
        """List all available profiles"""
        profiles = list(self.profiles.keys())
        
        # Also check for profile files not loaded
        for f in self.config_dir.glob("*.json"):
            name = f.stem
            if name not in profiles:
                profiles.append(name)
                
        return sorted(profiles)
        
    def duplicate_profile(self, source: str, dest: str) -> Config:
        """Duplicate a profile to a new name"""
        if source not in self.profiles:
            self.load_profile(source)
            
        source_config = self.profiles[source]
        new_config = self.create_profile(dest)
        
        new_config.from_dict(source_config.to_dict())
        new_config.save()
        
        return new_config
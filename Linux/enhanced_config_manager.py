#!/usr/bin/env python3
"""
Enhanced Configuration Manager for Phantom Strike
Advanced configuration with encryption, backup, and validation
"""

import os
import json
import time
import threading
import hashlib
import base64
import zlib
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, asdict
from enum import Enum
import shutil
import random
import string

class ConfigType(Enum):
    """Configuration types"""
    AIMBOT = "aimbot"
    ESP = "esp"
    SKINS = "skins"
    MISC = "misc"
    OVERLAY = "overlay"
    KEYBINDS = "keybinds"
    PROTECTION = "protection"
    PERFORMANCE = "performance"

@dataclass
class AimbotConfig:
    """Enhanced aimbot configuration"""
    enabled: bool = False
    aim_key: str = "mouse_right"
    aim_mode: str = "smooth"
    target_bone: str = "head"
    fov: float = 90.0
    smoothness: float = 5.0
    max_distance: float = 300.0
    visibility_check: bool = True
    target_allies: bool = False
    rcs_enabled: bool = True
    rcs_amount: float = 0.7
    
    # Advanced settings
    prediction_enabled: bool = True
    human_behavior: bool = True
    miss_simulation: bool = True
    body_shot_mix: float = 0.3
    reaction_time: float = 0.15
    aim_pace_control: bool = True
    flick_simulation: bool = True
    micro_adjustments: bool = True
    silent_aim: bool = False
    aim_desync: bool = True

@dataclass
class ESPConfig:
    """Enhanced ESP configuration"""
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
    show_head_tracer: bool = True
    show_velocity: bool = True
    show_prediction: bool = False
    show_radar: bool = True
    show_fov_circle: bool = True
    
    # Visual settings
    enemy_color: List[int] = None
    team_color: List[int] = None
    visible_color: List[int] = None
    hidden_color: List[int] = None
    max_distance: float = 800.0
    box_thickness: int = 2
    skeleton_thickness: int = 1
    font_size: int = 14
    box_style: str = "corner"
    fade_distance: float = 600.0
    warning_distance: float = 100.0
    
    def __post_init__(self):
        if self.enemy_color is None:
            self.enemy_color = [255, 0, 0, 255]
        if self.team_color is None:
            self.team_color = [0, 255, 0, 255]
        if self.visible_color is None:
            self.visible_color = [255, 255, 0, 255]
        if self.hidden_color is None:
            self.hidden_color = [255, 0, 0, 255]

@dataclass
class ProtectionConfig:
    """Anti-cheat protection configuration"""
    protection_level: str = "standard"
    memory_encryption: bool = True
    process_hiding: bool = True
    signature_rotation: bool = True
    behavioral_masking: bool = True
    timing_obfuscation: bool = True
    anti_screenshot: bool = True
    anti_memory_dump: bool = True
    dynamic_loading: bool = True
    runtime_patching: bool = True
    encrypted_communication: bool = True
    anti_forensics: bool = True
    stealth_mode: bool = False
    human_simulation: bool = True

@dataclass
class PerformanceConfig:
    """Performance optimization configuration"""
    fps_limit: int = 144
    render_optimization: bool = True
    culling_enabled: bool = True
    lod_enabled: bool = True
    async_rendering: bool = True
    batch_rendering: bool = True
    memory_pool: bool = True
    texture_cache: bool = True
    adaptive_quality: bool = True
    frame_skip: bool = False
    multithreading: bool = True
    gpu_acceleration: bool = True

class EnhancedConfigManager:
    """Enhanced configuration manager with advanced features"""
    
    def __init__(self):
        self.config_dir = "configs"
        self.backup_dir = "configs/backups"
        self.temp_dir = "configs/temp"
        
        # Create directories
        os.makedirs(self.config_dir, exist_ok=True)
        os.makedirs(self.backup_dir, exist_ok=True)
        os.makedirs(self.temp_dir, exist_ok=True)
        
        # Configuration objects
        self.aimbot_config = AimbotConfig()
        self.esp_config = ESPConfig()
        self.protection_config = ProtectionConfig()
        self.performance_config = PerformanceConfig()
        
        # Legacy config support
        self.misc_config = {}
        self.skin_config = {}
        self.overlay_config = {}
        self.keybinds_config = {}
        
        # Auto-save settings
        self.auto_save_enabled = True
        self.auto_save_interval = 300  # 5 minutes
        self.auto_save_thread = None
        self.last_save_time = time.time()
        
        # Encryption settings
        self.encryption_enabled = True
        self.encryption_key = self.generate_encryption_key()
        self.compression_enabled = True
        
        # Validation settings
        self.validate_configs = True
        self.backup_on_change = True
        self.max_backups = 10
        
        # Load configurations
        self.load_all_configurations()
        
        # Start auto-save
        if self.auto_save_enabled:
            self.start_auto_save()
        
        print("📋 Enhanced Configuration Manager initialized")
    
    def generate_encryption_key(self) -> bytes:
        """Generate random encryption key"""
        return os.urandom(32)
    
    def encrypt_config(self, data: str) -> str:
        """Encrypt configuration data"""
        if not self.encryption_enabled:
            return data
            
        try:
            # Compress data
            if self.compression_enabled:
                data = zlib.compress(data.encode())
            else:
                data = data.encode()
            
            # XOR encryption
            encrypted = bytearray()
            for i, byte in enumerate(data):
                encrypted.append(byte ^ self.encryption_key[i % len(self.encryption_key)])
            
            # Base64 encode
            return base64.b64encode(encrypted).decode()
        except Exception as e:
            print(f"❌ Config encryption failed: {e}")
            return data
    
    def decrypt_config(self, encrypted_data: str) -> str:
        """Decrypt configuration data"""
        if not self.encryption_enabled:
            return encrypted_data
            
        try:
            # Base64 decode
            encrypted = base64.b64decode(encrypted_data.encode())
            
            # XOR decryption
            decrypted = bytearray()
            for i, byte in enumerate(encrypted):
                decrypted.append(byte ^ self.encryption_key[i % len(self.encryption_key)])
            
            # Decompress data
            if self.compression_enabled:
                return zlib.decompress(decrypted).decode()
            else:
                return decrypted.decode()
        except Exception as e:
            print(f"❌ Config decryption failed: {e}")
            return encrypted_data
    
    def save_configuration(self, config_type: ConfigType, config_obj: Any) -> bool:
        """Save a specific configuration"""
        try:
            # Create backup if enabled
            if self.backup_on_change:
                self.create_backup(config_type)
            
            # Convert to dict
            config_data = asdict(config_obj) if hasattr(config_obj, '__dict__') else config_obj
            
            # Add metadata
            config_data['_metadata'] = {
                'saved_at': time.time(),
                'version': '2.0',
                'encrypted': self.encryption_enabled
            }
            
            # Serialize
            json_data = json.dumps(config_data, indent=2)
            
            # Encrypt
            if self.encryption_enabled:
                json_data = self.encrypt_config(json_data)
            
            # Save to file
            filename = f"{config_type.value}.json"
            filepath = os.path.join(self.config_dir, filename)
            
            with open(filepath, 'w') as f:
                f.write(json_data)
            
            self.last_save_time = time.time()
            print(f"💾 Saved {config_type.value} configuration")
            return True
            
        except Exception as e:
            print(f"❌ Failed to save {config_type.value} config: {e}")
            return False
    
    def load_configuration(self, config_type: ConfigType) -> Optional[Dict[str, Any]]:
        """Load a specific configuration"""
        try:
            filename = f"{config_type.value}.json"
            filepath = os.path.join(self.config_dir, filename)
            
            if not os.path.exists(filepath):
                print(f"⚠️ {config_type.value} config not found, using defaults")
                return None
            
            with open(filepath, 'r') as f:
                json_data = f.read()
            
            # Decrypt
            if self.encryption_enabled:
                json_data = self.decrypt_config(json_data)
            
            # Parse
            config_data = json.loads(json_data)
            
            # Remove metadata
            if '_metadata' in config_data:
                del config_data['_metadata']
            
            print(f"📁 Loaded {config_type.value} configuration")
            return config_data
            
        except Exception as e:
            print(f"❌ Failed to load {config_type.value} config: {e}")
            return None
    
    def create_backup(self, config_type: ConfigType) -> bool:
        """Create backup of configuration"""
        try:
            filename = f"{config_type.value}.json"
            filepath = os.path.join(self.config_dir, filename)
            
            if not os.path.exists(filepath):
                return False
            
            # Generate backup filename with timestamp
            timestamp = int(time.time())
            backup_filename = f"{config_type.value}_{timestamp}.json"
            backup_filepath = os.path.join(self.backup_dir, backup_filename)
            
            # Copy file
            shutil.copy2(filepath, backup_filepath)
            
            # Clean old backups
            self.clean_old_backups(config_type)
            
            print(f"📦 Created backup: {backup_filename}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to create backup: {e}")
            return False
    
    def clean_old_backups(self, config_type: ConfigType):
        """Clean old backup files"""
        try:
            pattern = f"{config_type.value}_*.json"
            backup_files = []
            
            for filename in os.listdir(self.backup_dir):
                if filename.startswith(f"{config_type.value}_") and filename.endswith(".json"):
                    filepath = os.path.join(self.backup_dir, filename)
                    backup_files.append((filepath, os.path.getmtime(filepath)))
            
            # Sort by modification time (newest first)
            backup_files.sort(key=lambda x: x[1], reverse=True)
            
            # Remove old backups
            for filepath, _ in backup_files[self.max_backups:]:
                os.remove(filepath)
                print(f"🗑️ Removed old backup: {os.path.basename(filepath)}")
                
        except Exception as e:
            print(f"❌ Failed to clean backups: {e}")
    
    def validate_configuration(self, config_type: ConfigType, config_data: Dict[str, Any]) -> bool:
        """Validate configuration data"""
        try:
            if config_type == ConfigType.AIMBOT:
                return self._validate_aimbot_config(config_data)
            elif config_type == ConfigType.ESP:
                return self._validate_esp_config(config_data)
            elif config_type == ConfigType.PROTECTION:
                return self._validate_protection_config(config_data)
            elif config_type == ConfigType.PERFORMANCE:
                return self._validate_performance_config(config_data)
            
            return True
            
        except Exception as e:
            print(f"❌ Configuration validation failed: {e}")
            return False
    
    def _validate_aimbot_config(self, config: Dict[str, Any]) -> bool:
        """Validate aimbot configuration"""
        required_fields = ['enabled', 'fov', 'smoothness', 'max_distance']
        
        for field in required_fields:
            if field not in config:
                print(f"❌ Missing aimbot config field: {field}")
                return False
        
        # Validate ranges
        if not (0 <= config['fov'] <= 360):
            print("❌ Invalid FOV value")
            return False
        
        if not (0 <= config['smoothness'] <= 20):
            print("❌ Invalid smoothness value")
            return False
        
        if not (0 <= config['max_distance'] <= 2000):
            print("❌ Invalid max_distance value")
            return False
        
        return True
    
    def _validate_esp_config(self, config: Dict[str, Any]) -> bool:
        """Validate ESP configuration"""
        required_fields = ['enabled', 'max_distance', 'box_thickness']
        
        for field in required_fields:
            if field not in config:
                print(f"❌ Missing ESP config field: {field}")
                return False
        
        # Validate color arrays
        color_fields = ['enemy_color', 'team_color', 'visible_color', 'hidden_color']
        for field in color_fields:
            if field in config and not isinstance(config[field], list):
                print(f"❌ Invalid color format for {field}")
                return False
        
        return True
    
    def _validate_protection_config(self, config: Dict[str, Any]) -> bool:
        """Validate protection configuration"""
        valid_levels = ['minimal', 'standard', 'aggressive', 'paranoid']
        
        if 'protection_level' in config and config['protection_level'] not in valid_levels:
            print(f"❌ Invalid protection level: {config['protection_level']}")
            return False
        
        return True
    
    def _validate_performance_config(self, config: Dict[str, Any]) -> bool:
        """Validate performance configuration"""
        if 'fps_limit' in config and not (30 <= config['fps_limit'] <= 360):
            print("❌ Invalid FPS limit value")
            return False
        
        return True
    
    def save_all_configurations(self) -> bool:
        """Save all configurations"""
        success = True
        
        # Save enhanced configs
        success &= self.save_configuration(ConfigType.AIMBOT, self.aimbot_config)
        success &= self.save_configuration(ConfigType.ESP, self.esp_config)
        success &= self.save_configuration(ConfigType.PROTECTION, self.protection_config)
        success &= self.save_configuration(ConfigType.PERFORMANCE, self.performance_config)
        
        # Save legacy configs
        success &= self.save_configuration(ConfigType.MISC, self.misc_config)
        success &= self.save_configuration(ConfigType.SKINS, self.skin_config)
        success &= self.save_configuration(ConfigType.OVERLAY, self.overlay_config)
        success &= self.save_configuration(ConfigType.KEYBINDS, self.keybinds_config)
        
        return success
    
    def load_all_configurations(self) -> bool:
        """Load all configurations"""
        success = True
        
        # Load enhanced configs
        aimbot_data = self.load_configuration(ConfigType.AIMBOT)
        if aimbot_data:
            if self.validate_configuration(ConfigType.AIMBOT, aimbot_data):
                self.aimbot_config = AimbotConfig(**aimbot_data)
        
        esp_data = self.load_configuration(ConfigType.ESP)
        if esp_data:
            if self.validate_configuration(ConfigType.ESP, esp_data):
                self.esp_config = ESPConfig(**esp_data)
        
        protection_data = self.load_configuration(ConfigType.PROTECTION)
        if protection_data:
            if self.validate_configuration(ConfigType.PROTECTION, protection_data):
                self.protection_config = ProtectionConfig(**protection_data)
        
        performance_data = self.load_configuration(ConfigType.PERFORMANCE)
        if performance_data:
            if self.validate_configuration(ConfigType.PERFORMANCE, performance_data):
                self.performance_config = PerformanceConfig(**performance_data)
        
        # Load legacy configs
        misc_data = self.load_configuration(ConfigType.MISC)
        if misc_data:
            self.misc_config = misc_data
        
        skin_data = self.load_configuration(ConfigType.SKINS)
        if skin_data:
            self.skin_config = skin_data
        
        overlay_data = self.load_configuration(ConfigType.OVERLAY)
        if overlay_data:
            self.overlay_config = overlay_data
        
        keybinds_data = self.load_configuration(ConfigType.KEYBINDS)
        if keybinds_data:
            self.keybinds_config = keybinds_data
        
        return success
    
    def start_auto_save(self):
        """Start auto-save thread"""
        if self.auto_save_thread is None or not self.auto_save_thread.is_alive():
            self.auto_save_thread = threading.Thread(target=self._auto_save_loop, daemon=True)
            self.auto_save_thread.start()
            print("⏰ Auto-save started")
    
    def stop_auto_save(self):
        """Stop auto-save thread"""
        self.auto_save_enabled = False
        if self.auto_save_thread:
            self.auto_save_thread.join(timeout=1.0)
            print("⏹️ Auto-save stopped")
    
    def _auto_save_loop(self):
        """Auto-save loop"""
        while self.auto_save_enabled:
            try:
                time.sleep(60)  # Check every minute
                
                if time.time() - self.last_save_time >= self.auto_save_interval:
                    self.save_all_configurations()
                    print("💾 Auto-saved configurations")
                    
            except Exception as e:
                print(f"❌ Auto-save error: {e}")
    
    def export_configuration(self, filepath: str) -> bool:
        """Export all configurations to a single file"""
        try:
            export_data = {
                'aimbot': asdict(self.aimbot_config),
                'esp': asdict(self.esp_config),
                'protection': asdict(self.protection_config),
                'performance': asdict(self.performance_config),
                'misc': self.misc_config,
                'skins': self.skin_config,
                'overlay': self.overlay_config,
                'keybinds': self.keybinds_config,
                '_export_metadata': {
                    'exported_at': time.time(),
                    'version': '2.0',
                    'encrypted': self.encryption_enabled
                }
            }
            
            json_data = json.dumps(export_data, indent=2)
            
            if self.encryption_enabled:
                json_data = self.encrypt_config(json_data)
            
            with open(filepath, 'w') as f:
                f.write(json_data)
            
            print(f"📤 Exported configuration to {filepath}")
            return True
            
        except Exception as e:
            print(f"❌ Export failed: {e}")
            return False
    
    def import_configuration(self, filepath: str, overwrite: bool = False) -> bool:
        """Import configuration from file"""
        try:
            with open(filepath, 'r') as f:
                json_data = f.read()
            
            if self.encryption_enabled:
                json_data = self.decrypt_config(json_data)
            
            import_data = json.loads(json_data)
            
            # Remove metadata
            if '_export_metadata' in import_data:
                del import_data['_export_metadata']
            
            # Validate and import each config
            if 'aimbot' in import_data:
                if self.validate_configuration(ConfigType.AIMBOT, import_data['aimbot']):
                    self.aimbot_config = AimbotConfig(**import_data['aimbot'])
            
            if 'esp' in import_data:
                if self.validate_configuration(ConfigType.ESP, import_data['esp']):
                    self.esp_config = ESPConfig(**import_data['esp'])
            
            if 'protection' in import_data:
                if self.validate_configuration(ConfigType.PROTECTION, import_data['protection']):
                    self.protection_config = ProtectionConfig(**import_data['protection'])
            
            if 'performance' in import_data:
                if self.validate_configuration(ConfigType.PERFORMANCE, import_data['performance']):
                    self.performance_config = PerformanceConfig(**import_data['performance'])
            
            # Import legacy configs
            if 'misc' in import_data:
                self.misc_config = import_data['misc']
            
            if 'skins' in import_data:
                self.skin_config = import_data['skins']
            
            if 'overlay' in import_data:
                self.overlay_config = import_data['overlay']
            
            if 'keybinds' in import_data:
                self.keybinds_config = import_data['keybinds']
            
            # Save imported configs
            if overwrite:
                self.save_all_configurations()
            
            print(f"📥 Imported configuration from {filepath}")
            return True
            
        except Exception as e:
            print(f"❌ Import failed: {e}")
            return False
    
    def reset_configuration(self, config_type: ConfigType) -> bool:
        """Reset configuration to defaults"""
        try:
            # Create backup before reset
            self.create_backup(config_type)
            
            if config_type == ConfigType.AIMBOT:
                self.aimbot_config = AimbotConfig()
            elif config_type == ConfigType.ESP:
                self.esp_config = ESPConfig()
            elif config_type == ConfigType.PROTECTION:
                self.protection_config = ProtectionConfig()
            elif config_type == ConfigType.PERFORMANCE:
                self.performance_config = PerformanceConfig()
            elif config_type == ConfigType.MISC:
                self.misc_config = {}
            elif config_type == ConfigType.SKINS:
                self.skin_config = {}
            elif config_type == ConfigType.OVERLAY:
                self.overlay_config = {}
            elif config_type == ConfigType.KEYBINDS:
                self.keybinds_config = {}
            
            # Save reset configuration
            self.save_configuration(config_type, getattr(self, f"{config_type.value}_config"))
            
            print(f"🔄 Reset {config_type.value} configuration to defaults")
            return True
            
        except Exception as e:
            print(f"❌ Reset failed: {e}")
            return False
    
    def get_configuration_summary(self) -> Dict[str, Any]:
        """Get summary of all configurations"""
        return {
            'aimbot': {
                'enabled': self.aimbot_config.enabled,
                'fov': self.aimbot_config.fov,
                'smoothness': self.aimbot_config.smoothness
            },
            'esp': {
                'enabled': self.esp_config.enabled,
                'max_distance': self.esp_config.max_distance,
                'box_style': self.esp_config.box_style
            },
            'protection': {
                'level': self.protection_config.protection_level,
                'stealth_mode': self.protection_config.stealth_mode
            },
            'performance': {
                'fps_limit': self.performance_config.fps_limit,
                'optimization': self.performance_config.render_optimization
            },
            'auto_save': {
                'enabled': self.auto_save_enabled,
                'interval': self.auto_save_interval,
                'last_save': self.last_save_time
            }
        }

# Compatibility with existing code
class BloodStrikeConfigManager(EnhancedConfigManager):
    """Backward compatible configuration manager"""
    pass

if __name__ == "__main__":
    # Test the enhanced configuration manager
    config_manager = EnhancedConfigManager()
    
    # Test saving and loading
    config_manager.save_all_configurations()
    
    # Get summary
    summary = config_manager.get_configuration_summary()
    print("Configuration Summary:")
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    print("✅ Enhanced Configuration Manager test completed!")

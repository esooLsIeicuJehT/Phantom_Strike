#!/usr/bin/env python3
"""
BloodStrike Configuration System
Comprehensive settings management and persistence
"""

import os
import sys
import json
import time
import hashlib
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, asdict
from enum import Enum
import threading
import pickle
import base64

class ConfigType(Enum):
    """Configuration file types"""
    MAIN = "main"
    AIMBOT = "aimbot"
    ESP = "esp"
    SKINS = "skins"
    PROTECTION = "protection"
    HOTKEYS = "hotkeys"
    PERFORMANCE = "performance"

class ConfigFormat(Enum):
    """Configuration file formats"""
    JSON = "json"
    BINARY = "binary"
    ENCRYPTED = "encrypted"

@dataclass
class AimbotConfig:
    """Aimbot configuration settings"""
    enabled: bool = True
    fov: float = 90.0
    smooth_factor: float = 10.0
    target_bone: str = "head"
    max_distance: float = 500.0
    reaction_time: float = 0.15
    aim_key: int = 2
    closest_target: bool = True
    lowest_health_first: bool = False
    threat_based: bool = True
    prediction_enabled: bool = True
    prediction_time: float = 0.1
    bullet_drop_compensation: bool = True
    lead_target: bool = True
    silent_aim: bool = False
    aim_punch: bool = False
    smooth_jitter: float = 0.2
    aim_speed: float = 2.0
    micro_corrections: bool = True
    aim_wobble: float = 0.5
    target_switch_delay: float = 0.1

@dataclass
class ESPConfig:
    """ESP configuration settings"""
    enabled: bool = True
    show_health_bar: bool = True
    show_armor_bar: bool = True
    show_distance: bool = True
    show_weapon: bool = True
    show_skeleton: bool = False
    show_head_tracer: bool = False
    show_crosshair: bool = False
    show_radar: bool = False
    max_render_distance: float = 500.0
    box_thickness: int = 2
    skeleton_thickness: int = 1
    font_size: int = 14
    health_bar_height: int = 4
    armor_bar_height: int = 3
    
    # ESP colors
    esp_visible_color: List[int] = None
    esp_hidden_color: List[int] = None
    esp_friend_color: List[int] = None
    esp_text_color: List[int] = None
    
    def __post_init__(self):
        if self.esp_visible_color is None:
            self.esp_visible_color = [255, 200, 0]
        if self.esp_hidden_color is None:
            self.esp_hidden_color = [255, 0, 0]
        if self.esp_friend_color is None:
            self.esp_friend_color = [0, 255, 0]
        if self.esp_text_color is None:
            self.esp_text_color = [255, 255, 255]

@dataclass
class SkinConfig:
    """Skin changer configuration"""
    enabled: bool = True
    auto_equip: bool = True
    random_skins: bool = False
    preserve_original: bool = True
    max_wear: float = 0.15
    min_stattrak_kills: int = 100
    enable_name_tags: bool = True
    custom_paints_enabled: bool = False
    equipped_skins: Dict[str, int] = None
    
    def __post_init__(self):
        if self.equipped_skins is None:
            self.equipped_skins = {}

@dataclass
class ProtectionConfig:
    """Anti-cheat protection configuration"""
    enabled: bool = True
    protection_level: str = "standard"
    stealth_mode: bool = False
    human_behavior: bool = True
    random_delays: bool = True
    network_monitoring: bool = True
    packet_filtering: bool = False
    connection_obfuscation: bool = False
    file_encryption: bool = True
    anti_debugging: bool = True
    anti_vm: bool = True
    anti_analysis: bool = True

@dataclass
class HotkeyConfig:
    """Hotkey configuration"""
    toggle_esp: int = 288  # F1
    toggle_aimbot: int = 289  # F2
    toggle_menu: int = 270  # INSERT
    toggle_stats: int = 286  # F5
    toggle_radar: int = 283  # F4
    toggle_skins: int = 285  # F6
    panic_mode: int = 279  # END
    reload_config: int = 290  # F7
    save_config: int = 291  # F8

@dataclass
class PerformanceConfig:
    """Performance optimization settings"""
    max_fps: int = 144
    render_distance: float = 1000.0
    update_frequency: float = 60.0
    network_timeout: float = 5.0
    cache_size: int = 1000
    thread_count: int = 4
    memory_limit: int = 2048  # MB
    gpu_acceleration: bool = True
    multithreading: bool = True
    lazy_loading: bool = True

@dataclass
class MainConfig:
    """Main configuration settings"""
    # General
    auto_start: bool = False
    minimize_to_tray: bool = True
    start_minimized: bool = False
    check_updates: bool = True
    auto_save: bool = True
    backup_configs: bool = True
    
    # Security
    encrypt_configs: bool = True
    password_protect: bool = False
    session_timeout: int = 3600  # 1 hour
    
    # Logging
    enable_logging: bool = True
    log_level: str = "INFO"
    max_log_size: int = 10  # MB
    log_retention_days: int = 7
    
    # Network
    udp_port: int = 1337
    tcp_port: int = 8080
    enable_web_interface: bool = False
    web_port: int = 8081
    web_password: str = ""

class BloodStrikeConfigManager:
    """Comprehensive configuration manager for BloodStrike cheat"""
    
    def __init__(self):
        self.config_dir = "configs"
        self.backup_dir = "backups"
        self.temp_dir = "temp"
        
        # Create directories
        self.create_directories()
        
        # Configuration objects
        self.main_config = MainConfig()
        self.aimbot_config = AimbotConfig()
        self.esp_config = ESPConfig()
        self.skin_config = SkinConfig()
        self.protection_config = ProtectionConfig()
        self.hotkey_config = HotkeyConfig()
        self.performance_config = PerformanceConfig()
        
        # File paths
        self.config_files = {
            ConfigType.MAIN: os.path.join(self.config_dir, "main_config.json"),
            ConfigType.AIMBOT: os.path.join(self.config_dir, "aimbot_config.json"),
            ConfigType.ESP: os.path.join(self.config_dir, "esp_config.json"),
            ConfigType.SKINS: os.path.join(self.config_dir, "skin_config.json"),
            ConfigType.PROTECTION: os.path.join(self.config_dir, "protection_config.json"),
            ConfigType.HOTKEYS: os.path.join(self.config_dir, "hotkey_config.json"),
            ConfigType.PERFORMANCE: os.path.join(self.config_dir, "performance_config.json")
        }
        
        # Encryption key (derived from system info)
        self.encryption_key = self.generate_encryption_key()
        
        # Thread lock for config operations
        self.config_lock = threading.Lock()
        
        # Auto-save timer
        self.auto_save_timer = None
        self.last_save_time = time.time()
        
        # Load all configurations
        self.load_all_configurations()
        
        print("🔧 BloodStrike Configuration Manager initialized")
        print(f"📁 Config directory: {self.config_dir}")
        print(f"🔐 Encryption: {'Enabled' if self.main_config.encrypt_configs else 'Disabled'}")
    
    def create_directories(self):
        """Create necessary directories"""
        directories = [self.config_dir, self.backup_dir, self.temp_dir]
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    def generate_encryption_key(self) -> str:
        """Generate encryption key from system information"""
        try:
            import platform
            import uuid
            
            # Get system-specific information
            system_info = f"{platform.system()}-{platform.node()}-{uuid.getnode()}"
            key = hashlib.sha256(system_info.encode()).hexdigest()
            return key[:32]  # Use first 32 characters
        except:
            return "bloodstrike_config_key_default"
    
    def encrypt_data(self, data: str) -> str:
        """Encrypt configuration data"""
        if not self.main_config.encrypt_configs:
            return data
        
        try:
            # Simple XOR encryption (for demonstration)
            key_bytes = self.encryption_key.encode()
            data_bytes = data.encode()
            encrypted_bytes = bytearray()
            
            for i, byte in enumerate(data_bytes):
                key_byte = key_bytes[i % len(key_bytes)]
                encrypted_bytes.append(byte ^ key_byte)
            
            return base64.b64encode(encrypted_bytes).decode()
        except Exception as e:
            print(f"❌ Encryption failed: {e}")
            return data
    
    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt configuration data"""
        if not self.main_config.encrypt_configs:
            return encrypted_data
        
        try:
            # Simple XOR decryption
            key_bytes = self.encryption_key.encode()
            encrypted_bytes = base64.b64decode(encrypted_data.encode())
            decrypted_bytes = bytearray()
            
            for i, byte in enumerate(encrypted_bytes):
                key_byte = key_bytes[i % len(key_bytes)]
                decrypted_bytes.append(byte ^ key_byte)
            
            return decrypted_bytes.decode()
        except Exception as e:
            print(f"❌ Decryption failed: {e}")
            return encrypted_data
    
    def save_configuration(self, config_type: ConfigType, config_format: ConfigFormat = ConfigFormat.JSON) -> bool:
        """Save a specific configuration"""
        with self.config_lock:
            try:
                # Get configuration object
                config_obj = self.get_config_object(config_type)
                if config_obj is None:
                    print(f"❌ Unknown configuration type: {config_type}")
                    return False
                
                # Convert to dictionary
                config_dict = asdict(config_obj)
                
                # Serialize based on format
                if config_format == ConfigFormat.JSON:
                    config_data = json.dumps(config_dict, indent=2)
                elif config_format == ConfigFormat.BINARY:
                    config_data = pickle.dumps(config_obj)
                    config_data = base64.b64encode(config_data).decode()
                elif config_format == ConfigFormat.ENCRYPTED:
                    config_data = json.dumps(config_dict, indent=2)
                    config_data = self.encrypt_data(config_data)
                else:
                    print(f"❌ Unknown format: {config_format}")
                    return False
                
                # Create backup if enabled
                if self.main_config.backup_configs:
                    self.create_backup(config_type)
                
                # Save to file
                file_path = self.config_files[config_type]
                if config_format == ConfigFormat.BINARY:
                    file_path = file_path.replace('.json', '.bin')
                elif config_format == ConfigFormat.ENCRYPTED:
                    file_path = file_path.replace('.json', '.enc')
                
                with open(file_path, 'w') as f:
                    f.write(config_data)
                
                self.last_save_time = time.time()
                print(f"✅ Saved {config_type.value} configuration")
                return True
                
            except Exception as e:
                print(f"❌ Failed to save {config_type.value} configuration: {e}")
                return False
    
    def load_configuration(self, config_type: ConfigType, config_format: ConfigFormat = ConfigFormat.JSON) -> bool:
        """Load a specific configuration"""
        with self.config_lock:
            try:
                # Determine file path
                file_path = self.config_files[config_type]
                if config_format == ConfigFormat.BINARY:
                    file_path = file_path.replace('.json', '.bin')
                elif config_format == ConfigFormat.ENCRYPTED:
                    file_path = file_path.replace('.json', '.enc')
                
                # Check if file exists
                if not os.path.exists(file_path):
                    print(f"⚠️ {config_type.value} configuration file not found, using defaults")
                    return False
                
                # Read file
                with open(file_path, 'r') as f:
                    config_data = f.read()
                
                # Deserialize based on format
                if config_format == ConfigFormat.JSON:
                    config_dict = json.loads(config_data)
                elif config_format == ConfigFormat.BINARY:
                    config_bytes = base64.b64decode(config_data.encode())
                    config_obj = pickle.loads(config_bytes)
                    self.set_config_object(config_type, config_obj)
                    return True
                elif config_format == ConfigFormat.ENCRYPTED:
                    config_data = self.decrypt_data(config_data)
                    config_dict = json.loads(config_data)
                else:
                    print(f"❌ Unknown format: {config_format}")
                    return False
                
                # Update configuration object
                config_obj = self.get_config_object(config_type)
                if config_obj:
                    for key, value in config_dict.items():
                        if hasattr(config_obj, key):
                            setattr(config_obj, key, value)
                
                print(f"✅ Loaded {config_type.value} configuration")
                return True
                
            except Exception as e:
                print(f"❌ Failed to load {config_type.value} configuration: {e}")
                return False
    
    def get_config_object(self, config_type: ConfigType):
        """Get configuration object by type"""
        config_map = {
            ConfigType.MAIN: self.main_config,
            ConfigType.AIMBOT: self.aimbot_config,
            ConfigType.ESP: self.esp_config,
            ConfigType.SKINS: self.skin_config,
            ConfigType.PROTECTION: self.protection_config,
            ConfigType.HOTKEYS: self.hotkey_config,
            ConfigType.PERFORMANCE: self.performance_config
        }
        return config_map.get(config_type)
    
    def set_config_object(self, config_type: ConfigType, config_obj):
        """Set configuration object by type"""
        if config_type == ConfigType.MAIN:
            self.main_config = config_obj
        elif config_type == ConfigType.AIMBOT:
            self.aimbot_config = config_obj
        elif config_type == ConfigType.ESP:
            self.esp_config = config_obj
        elif config_type == ConfigType.SKINS:
            self.skin_config = config_obj
        elif config_type == ConfigType.PROTECTION:
            self.protection_config = config_obj
        elif config_type == ConfigType.HOTKEYS:
            self.hotkey_config = config_obj
        elif config_type == ConfigType.PERFORMANCE:
            self.performance_config = config_obj
    
    def save_all_configurations(self) -> bool:
        """Save all configurations"""
        success_count = 0
        total_count = len(ConfigType)
        
        for config_type in ConfigType:
            if self.save_configuration(config_type):
                success_count += 1
        
        print(f"💾 Saved {success_count}/{total_count} configurations")
        return success_count == total_count
    
    def load_all_configurations(self) -> bool:
        """Load all configurations"""
        success_count = 0
        total_count = len(ConfigType)
        
        # Try different formats in order of preference
        formats = [ConfigFormat.ENCRYPTED, ConfigFormat.BINARY, ConfigFormat.JSON]
        
        for config_type in ConfigType:
            loaded = False
            for format_type in formats:
                if self.load_configuration(config_type, format_type):
                    loaded = True
                    break
            
            if loaded:
                success_count += 1
        
        print(f"📂 Loaded {success_count}/{total_count} configurations")
        return success_count > 0
    
    def create_backup(self, config_type: ConfigType) -> bool:
        """Create backup of configuration"""
        try:
            timestamp = int(time.time())
            backup_filename = f"{config_type.value}_backup_{timestamp}.json"
            backup_path = os.path.join(self.backup_dir, backup_filename)
            
            # Copy current config to backup
            import shutil
            shutil.copy2(self.config_files[config_type], backup_path)
            
            # Clean old backups (keep only last 10)
            self.cleanup_old_backups(config_type)
            
            print(f"💾 Created backup: {backup_filename}")
            return True
        except Exception as e:
            print(f"❌ Failed to create backup: {e}")
            return False
    
    def cleanup_old_backups(self, config_type: ConfigType):
        """Clean old backup files"""
        try:
            backup_pattern = f"{config_type.value}_backup_"
            backup_files = []
            
            for filename in os.listdir(self.backup_dir):
                if filename.startswith(backup_pattern) and filename.endswith('.json'):
                    backup_files.append(filename)
            
            # Sort by timestamp (newest first)
            backup_files.sort(reverse=True)
            
            # Keep only last 10 backups
            for old_backup in backup_files[10:]:
                old_path = os.path.join(self.backup_dir, old_backup)
                os.remove(old_path)
                
        except Exception as e:
            print(f"⚠️ Failed to cleanup old backups: {e}")
    
    def restore_backup(self, config_type: ConfigType, backup_timestamp: int) -> bool:
        """Restore configuration from backup"""
        try:
            backup_filename = f"{config_type.value}_backup_{backup_timestamp}.json"
            backup_path = os.path.join(self.backup_dir, backup_filename)
            
            if not os.path.exists(backup_path):
                print(f"❌ Backup file not found: {backup_filename}")
                return False
            
            # Create backup of current config first
            self.create_backup(config_type)
            
            # Restore from backup
            import shutil
            shutil.copy2(backup_path, self.config_files[config_type])
            
            # Load restored configuration
            self.load_configuration(config_type)
            
            print(f"✅ Restored {config_type.value} from backup")
            return True
        except Exception as e:
            print(f"❌ Failed to restore backup: {e}")
            return False
    
    def get_backup_list(self, config_type: ConfigType) -> List[Dict[str, Any]]:
        """Get list of available backups"""
        backups = []
        try:
            backup_pattern = f"{config_type.value}_backup_"
            
            for filename in os.listdir(self.backup_dir):
                if filename.startswith(backup_pattern) and filename.endswith('.json'):
                    # Extract timestamp from filename
                    timestamp_str = filename.replace(backup_pattern, '').replace('.json', '')
                    timestamp = int(timestamp_str)
                    
                    # Get file info
                    file_path = os.path.join(self.backup_dir, filename)
                    stat = os.stat(file_path)
                    
                    backups.append({
                        'filename': filename,
                        'timestamp': timestamp,
                        'date': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp)),
                        'size': stat.st_size
                    })
            
            # Sort by timestamp (newest first)
            backups.sort(key=lambda x: x['timestamp'], reverse=True)
            
        except Exception as e:
            print(f"⚠️ Failed to get backup list: {e}")
        
        return backups
    
    def export_configuration(self, export_path: str, config_types: List[ConfigType] = None) -> bool:
        """Export configurations to a single file"""
        try:
            if config_types is None:
                config_types = list(ConfigType)
            
            export_data = {
                'exported_at': time.time(),
                'version': '1.0',
                'configurations': {}
            }
            
            for config_type in config_types:
                config_obj = self.get_config_object(config_type)
                if config_obj:
                    export_data['configurations'][config_type.value] = asdict(config_obj)
            
            # Save export file
            with open(export_path, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            print(f"📤 Exported {len(config_types)} configurations to {export_path}")
            return True
        except Exception as e:
            print(f"❌ Failed to export configurations: {e}")
            return False
    
    def import_configuration(self, import_path: str, overwrite: bool = False) -> bool:
        """Import configurations from a file"""
        try:
            with open(import_path, 'r') as f:
                import_data = json.load(f)
            
            imported_count = 0
            
            for config_name, config_dict in import_data.get('configurations', {}).items():
                try:
                    config_type = ConfigType(config_name)
                    config_obj = self.get_config_object(config_type)
                    
                    if config_obj:
                        if overwrite:
                            # Overwrite all settings
                            for key, value in config_dict.items():
                                if hasattr(config_obj, key):
                                    setattr(config_obj, key, value)
                        else:
                            # Only update non-default values
                            for key, value in config_dict.items():
                                if hasattr(config_obj, key) and getattr(config_obj, key) != value:
                                    setattr(config_obj, key, value)
                        
                        # Save the updated configuration
                        self.save_configuration(config_type)
                        imported_count += 1
                        
                except ValueError:
                    print(f"⚠️ Unknown configuration type: {config_name}")
                    continue
            
            print(f"📥 Imported {imported_count} configurations from {import_path}")
            return imported_count > 0
        except Exception as e:
            print(f"❌ Failed to import configurations: {e}")
            return False
    
    def reset_configuration(self, config_type: ConfigType) -> bool:
        """Reset configuration to defaults"""
        try:
            # Create backup first
            self.create_backup(config_type)
            
            # Reset to defaults
            if config_type == ConfigType.MAIN:
                self.main_config = MainConfig()
            elif config_type == ConfigType.AIMBOT:
                self.aimbot_config = AimbotConfig()
            elif config_type == ConfigType.ESP:
                self.esp_config = ESPConfig()
            elif config_type == ConfigType.SKINS:
                self.skin_config = SkinConfig()
            elif config_type == ConfigType.PROTECTION:
                self.protection_config = ProtectionConfig()
            elif config_type == ConfigType.HOTKEYS:
                self.hotkey_config = HotkeyConfig()
            elif config_type == ConfigType.PERFORMANCE:
                self.performance_config = PerformanceConfig()
            
            # Save defaults
            self.save_configuration(config_type)
            
            print(f"🔄 Reset {config_type.value} configuration to defaults")
            return True
        except Exception as e:
            print(f"❌ Failed to reset configuration: {e}")
            return False
    
    def validate_configuration(self, config_type: ConfigType) -> Dict[str, Any]:
        """Validate configuration values"""
        validation_result = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        try:
            config_obj = self.get_config_object(config_type)
            if not config_obj:
                validation_result['valid'] = False
                validation_result['errors'].append(f"Unknown configuration type: {config_type}")
                return validation_result
            
            # Type-specific validation
            if config_type == ConfigType.AIMBOT:
                if self.aimbot_config.fov < 1 or self.aimbot_config.fov > 180:
                    validation_result['errors'].append("Aimbot FOV must be between 1 and 180")
                    validation_result['valid'] = False
                
                if self.aimbot_config.smooth_factor < 1 or self.aimbot_config.smooth_factor > 20:
                    validation_result['warnings'].append("Aimbot smooth factor should be between 1 and 20")
                
                if self.aimbot_config.max_distance < 0 or self.aimbot_config.max_distance > 10000:
                    validation_result['errors'].append("Max distance must be between 0 and 10000")
                    validation_result['valid'] = False
            
            elif config_type == ConfigType.ESP:
                if self.esp_config.max_render_distance < 0 or self.esp_config.max_render_distance > 10000:
                    validation_result['errors'].append("ESP render distance must be between 0 and 10000")
                    validation_result['valid'] = False
                
                if self.esp_config.box_thickness < 1 or self.esp_config.box_thickness > 10:
                    validation_result['warnings'].append("ESP box thickness should be between 1 and 10")
            
            elif config_type == ConfigType.SKINS:
                if self.skin_config.max_wear < 0 or self.skin_config.max_wear > 1:
                    validation_result['errors'].append("Max wear must be between 0 and 1")
                    validation_result['valid'] = False
            
            elif config_type == ConfigType.PROTECTION:
                valid_levels = ["minimal", "standard", "aggressive", "paranoid"]
                if self.protection_config.protection_level not in valid_levels:
                    validation_result['errors'].append(f"Protection level must be one of: {valid_levels}")
                    validation_result['valid'] = False
            
            elif config_type == ConfigType.PERFORMANCE:
                if self.performance_config.max_fps < 30 or self.performance_config.max_fps > 360:
                    validation_result['warnings'].append("Max FPS should be between 30 and 360")
                
                if self.performance_config.memory_limit < 512 or self.performance_config.memory_limit > 8192:
                    validation_result['warnings'].append("Memory limit should be between 512MB and 8GB")
            
        except Exception as e:
            validation_result['valid'] = False
            validation_result['errors'].append(f"Validation error: {e}")
        
        return validation_result
    
    def get_configuration_summary(self) -> Dict[str, Any]:
        """Get summary of all configurations"""
        summary = {
            'configs': {},
            'total_configs': len(ConfigType),
            'last_save_time': self.last_save_time,
            'encryption_enabled': self.main_config.encrypt_configs,
            'backup_enabled': self.main_config.backup_configs
        }
        
        for config_type in ConfigType:
            config_obj = self.get_config_object(config_type)
            if config_obj:
                config_dict = asdict(config_obj)
                
                # Count non-default values
                default_obj = self.get_default_config(config_type)
                default_dict = asdict(default_obj) if default_obj else {}
                
                non_default_count = 0
                for key, value in config_dict.items():
                    if key in default_dict and default_dict[key] != value:
                        non_default_count += 1
                
                summary['configs'][config_type.value] = {
                    'total_settings': len(config_dict),
                    'customized_settings': non_default_count,
                    'last_modified': getattr(config_obj, 'last_modified', 'Unknown')
                }
        
        return summary
    
    def get_default_config(self, config_type: ConfigType):
        """Get default configuration object"""
        defaults = {
            ConfigType.MAIN: MainConfig(),
            ConfigType.AIMBOT: AimbotConfig(),
            ConfigType.ESP: ESPConfig(),
            ConfigType.SKINS: SkinConfig(),
            ConfigType.PROTECTION: ProtectionConfig(),
            ConfigType.HOTKEYS: HotkeyConfig(),
            ConfigType.PERFORMANCE: PerformanceConfig()
        }
        return defaults.get(config_type)
    
    def start_auto_save(self):
        """Start auto-save timer"""
        if self.main_config.auto_save:
            def auto_save_worker():
                while True:
                    time.sleep(300)  # Save every 5 minutes
                    if self.main_config.auto_save:
                        self.save_all_configurations()
            
            if self.auto_save_timer is None:
                self.auto_save_timer = threading.Thread(target=auto_save_worker, daemon=True)
                self.auto_save_timer.start()
                print("⏰ Auto-save enabled")
    
    def stop_auto_save(self):
        """Stop auto-save timer"""
        self.auto_save_timer = None
        print("⏹️ Auto-save disabled")

# Main usage example
if __name__ == "__main__":
    # Initialize configuration manager
    config_manager = BloodStrikeConfigManager()
    
    # Save all configurations
    config_manager.save_all_configurations()
    
    # Get configuration summary
    summary = config_manager.get_configuration_summary()
    print("Configuration Summary:")
    for config_name, info in summary['configs'].items():
        print(f"  {config_name}: {info['customized_settings']}/{info['total_settings']} customized")
    
    # Validate configurations
    for config_type in ConfigType:
        validation = config_manager.validate_configuration(config_type)
        if not validation['valid']:
            print(f"❌ {config_type.value} validation failed: {validation['errors']}")
    
    # Export configurations
    config_manager.export_configuration("bloodstrike_config_export.json")
    
    print("🔧 BloodStrike Configuration System ready!")

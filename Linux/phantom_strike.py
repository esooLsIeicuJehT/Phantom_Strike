#!/usr/bin/env python3
"""
🎯 PHANTOM STRIKE - BloodStrike Professional Cheat Suite
Main launcher with integrated all beefed-up features
"""

import os
import sys
import time
import signal
import threading
import argparse
from typing import Dict, List, Any, Optional
import json

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Import all our beefed-up modules
try:
    from external_overlay_imgui import ExternalOverlay
    from ai_aimbot import AdvancedAIAimbot
    from skin_changer import BloodStrikeSkinChanger
    from anti_cheat_evasion import BloodStrikeAntiCheatEvasion, ProtectionLevel
    from config_manager import BloodStrikeConfigManager, ConfigType
    IMPORTS_AVAILABLE = True
    print("✅ All modules imported successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("⚠️ Running in demo mode - some features may be limited")
    IMPORTS_AVAILABLE = False

class PhantomStrikeLauncher:
    """Main launcher for Phantom Strike BloodStrike cheat"""
    
    def __init__(self):
        self.running = False
        self.debug_mode = False
        
        # Component instances
        self.overlay = None
        self.aimbot = None
        self.skin_changer = None
        self.anti_cheat = None
        self.config_manager = None
        
        # Performance monitoring
        self.start_time = time.time()
        self.frame_count = 0
        self.fps = 0
        self.last_fps_time = time.time()
        
        # Status tracking
        self.status = {
            'overlay': False,
            'aimbot': False,
            'skins': False,
            'protection': False,
            'config': False
        }
        
        # Initialize components
        self.initialize_components()
        
        print("🎯 Phantom Strike Launcher initialized")
    
    def initialize_components(self):
        """Initialize all cheat components"""
        try:
            # Configuration Manager (must be first)
            if IMPORTS_AVAILABLE:
                self.config_manager = BloodStrikeConfigManager()
                self.status['config'] = True
                print("📋 Configuration manager loaded")
            else:
                print("⚠️ Configuration manager not available")
            
            # Anti-Cheat Evasion (must be early)
            if IMPORTS_AVAILABLE and self.config_manager:
                protection_level = ProtectionLevel(self.config_manager.protection_config.protection_level)
                self.anti_cheat = BloodStrikeAntiCheatEvasion()
                self.anti_cheat.enable_protection(protection_level)
                self.status['protection'] = True
                print("🛡️ Anti-cheat evasion enabled")
            
            # AI Aimbot
            if IMPORTS_AVAILABLE and self.config_manager:
                self.aimbot = AdvancedAIAimbot()
                # Apply configuration
                aimbot_config = self.config_manager.aimbot_config
                self.aimbot.enabled = aimbot_config.enabled
                self.aimbot.fov = aimbot_config.fov
                self.aimbot.smooth_factor = aimbot_config.smooth_factor
                self.aimbot.target_bone = aimbot_config.target_bone
                self.aimbot.max_distance = aimbot_config.max_distance
                self.aimbot.reaction_time = aimbot_config.reaction_time
                self.aimbot.aim_key = aimbot_config.aim_key
                self.status['aimbot'] = True
                print("🎯 AI aimbot loaded")
            
            # Skin Changer
            if IMPORTS_AVAILABLE and self.config_manager:
                self.skin_changer = BloodStrikeSkinChanger()
                # Apply configuration
                skin_config = self.config_manager.skin_config
                self.skin_changer.enabled = skin_config.enabled
                self.skin_changer.auto_equip = skin_config.auto_equip
                self.skin_changer.random_skins = skin_config.random_skins
                self.skin_changer.preserve_original = skin_config.preserve_original
                self.skin_changer.max_wear = skin_config.max_wear
                self.status['skins'] = True
                print("🎨 Skin changer loaded")
            
            # External Overlay
            if IMPORTS_AVAILABLE and self.config_manager:
                self.overlay = ExternalOverlay()
                # Apply configuration
                esp_config = self.config_manager.esp_config
                self.overlay.show_esp = esp_config.enabled
                self.overlay.show_health_bar = esp_config.show_health_bar
                self.overlay.show_armor_bar = esp_config.show_armor_bar
                self.overlay.show_distance = esp_config.show_distance
                self.overlay.show_weapon = esp_config.show_weapon
                self.overlay.show_skeleton = esp_config.show_skeleton
                self.overlay.show_head_tracer = esp_config.show_head_tracer
                self.overlay.show_crosshair = esp_config.show_crosshair
                self.overlay.show_radar = esp_config.show_radar
                self.overlay.max_render_distance = esp_config.max_render_distance
                self.overlay.box_thickness = esp_config.box_thickness
                self.overlay.esp_visible_color = tuple(esp_config.esp_visible_color)
                self.overlay.esp_hidden_color = tuple(esp_config.esp_hidden_color)
                self.overlay.esp_friend_color = tuple(esp_config.esp_friend_color)
                self.overlay.esp_text_color = tuple(esp_config.esp_text_color)
                self.status['overlay'] = True
                print("👁️ External overlay loaded")
            
            print("✅ All components initialized successfully")
            
        except Exception as e:
            print(f"❌ Component initialization failed: {e}")
            self.cleanup()
            sys.exit(1)
    
    def start(self):
        """Start the cheat suite"""
        print("🚀 Starting Phantom Strike...")
        self.running = True
        
        try:
            # Start auto-save if enabled
            if self.config_manager and self.config_manager.main_config.auto_save:
                self.config_manager.start_auto_save()
            
            # Start main loop
            self.main_loop()
            
        except KeyboardInterrupt:
            print("\\n⚠️ Interrupted by user")
        except Exception as e:
            print(f"❌ Fatal error: {e}")
        finally:
            self.cleanup()
    
    def main_loop(self):
        """Main application loop"""
        print("🔄 Entering main loop...")
        
        while self.running:
            try:
                # Update performance metrics
                self.update_performance()
                
                # Process anti-cheat evasion
                if self.anti_cheat:
                    self.anti_cheat.check_detection_attempt()
                    if self.anti_cheat.random_delays:
                        self.anti_cheat.add_random_delay(0.001, 0.005)
                
                # Process aimbot
                if self.aimbot and self.aimbot.enabled:
                    # This would integrate with game memory reading
                    # For now, just simulate processing
                    pass
                
                # Process overlay rendering
                if self.overlay and self.overlay.show_esp:
                    # This would handle the overlay rendering
                    # For now, just simulate frame updates
                    self.frame_count += 1
                
                # Small sleep to prevent CPU overuse
                time.sleep(0.001)
                
            except Exception as e:
                if self.debug_mode:
                    print(f"⚠️ Main loop error: {e}")
                # Continue running even with errors
                continue
    
    def update_performance(self):
        """Update performance metrics"""
        current_time = time.time()
        
        # Calculate FPS
        if current_time - self.last_fps_time >= 1.0:
            self.fps = self.frame_count / (current_time - self.last_fps_time)
            self.frame_count = 0
            self.last_fps_time = current_time
            
            if self.debug_mode:
                print(f"📊 FPS: {self.fps:.1f}")
    
    def stop(self):
        """Stop the cheat suite"""
        print("🛑 Stopping Phantom Strike...")
        self.running = False
    
    def cleanup(self):
        """Clean up resources"""
        print("🧹 Cleaning up resources...")
        
        try:
            # Save configurations
            if self.config_manager:
                self.config_manager.save_all_configurations()
                self.config_manager.stop_auto_save()
            
            # Stop overlay
            if self.overlay:
                # Overlay cleanup would go here
                pass
            
            # Stop anti-cheat evasion
            if self.anti_cheat:
                self.anti_cheat.emergency_disable()
            
            # Save skin configuration
            if self.skin_changer:
                self.skin_changer.save_configuration()
            
            print("✅ Cleanup completed")
            
        except Exception as e:
            print(f"⚠️ Cleanup error: {e}")
    
    def get_status(self) -> Dict[str, Any]:
        """Get current status of all components"""
        status = {
            'running': self.running,
            'uptime': time.time() - self.start_time,
            'fps': self.fps,
            'components': self.status.copy(),
            'debug_mode': self.debug_mode
        }
        
        # Add component-specific status
        if self.aimbot:
            status['aimbot_stats'] = self.aimbot.get_stats()
        
        if self.skin_changer:
            status['skin_stats'] = self.skin_changer.get_stats()
        
        if self.anti_cheat:
            status['protection_status'] = self.anti_cheat.get_protection_status()
        
        if self.config_manager:
            status['config_summary'] = self.config_manager.get_configuration_summary()
        
        return status
    
    def print_status(self):
        """Print current status to console"""
        status = self.get_status()
        
        print("\\n" + "="*60)
        print("🎯 PHANTOM STRIKE STATUS")
        print("="*60)
        print(f"🟢 Running: {status['running']}")
        print(f"⏱️ Uptime: {status['uptime']:.1f}s")
        print(f"📊 FPS: {status['fps']:.1f}")
        print(f"🐛 Debug Mode: {status['debug_mode']}")
        
        print("\\n📦 Components:")
        for component, active in status['components'].items():
            status_icon = "✅" if active else "❌"
            print(f"  {status_icon} {component.title()}")
        
        # Component-specific stats
        if 'aimbot_stats' in status:
            aimbot = status['aimbot_stats']
            print(f"\\n🎯 Aimbot:")
            print(f"  Enabled: {aimbot['enabled']}")
            print(f"  Shots Fired: {aimbot['shots_fired']}")
            print(f"  Accuracy: {aimbot.get('accuracy', 0):.1f}%")
        
        if 'skin_stats' in status:
            skins = status['skin_stats']
            print(f"\\n🎨 Skins:")
            print(f"  Enabled: {skins['enabled']}")
            print(f"  Total Skins: {skins['total_skins']}")
            print(f"  Equipped: {skins['equipped_skins']}")
        
        if 'protection_status' in status:
            protection = status['protection_status']
            print(f"\\n🛡️ Protection:")
            print(f"  Enabled: {protection['enabled']}")
            print(f"  Level: {protection['protection_level']}")
            print(f"  Detection Attempts: {protection['detection_attempts']}")
        
        print("="*60)
    
    def handle_signal(self, signum, frame):
        """Handle system signals"""
        if signum == signal.SIGINT:
            print("\\n🛑 SIGINT received - shutting down...")
            self.stop()
        elif signum == signal.SIGTERM:
            print("\\n🛑 SIGTERM received - shutting down...")
            self.stop()
    
    def toggle_debug(self):
        """Toggle debug mode"""
        self.debug_mode = not self.debug_mode
        print(f"🐛 Debug mode: {'ON' if self.debug_mode else 'OFF'}")
    
    def emergency_stop(self):
        """Emergency stop all features"""
        print("🚨 EMERGENCY STOP ACTIVATED")
        self.running = False
        
        # Emergency disable all components
        if self.anti_cheat:
            self.anti_cheat.emergency_disable()
        
        if self.aimbot:
            self.aimbot.enabled = False
        
        if self.overlay:
            self.overlay.show_esp = False
        
        if self.skin_changer:
            self.skin_changer.enabled = False
        
        print("❌ All features disabled immediately")

def print_banner():
    """Print the Phantom Strike banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    🎯 PHANTOM STRIKE - BloodStrike Professional Cheat Suite   ║
║                                                              ║
║    🔥 Advanced Features:                                    ║
║       • AI-Powered Aimbot with Human Behavior                ║
║       • Professional ESP with 2D Boxes & Health Bars        ║
║       • Skin Changer with 25+ Weapon Skins                  ║
║       • Anti-Cheat Evasion System                            ║
║       • Configuration Management & Persistence               ║
║                                                              ║
║    🛡️ Protection:                                           ║
║       • Memory Encryption & Obfuscation                     ║
║       • Process Hiding & Anti-Debugging                     ║
║       • Human-Like Behavior Simulation                       ║
║       • Network Traffic Obfuscation                         ║
║                                                              ║
║    🎮 Controls:                                             ║
║       • F1 - Toggle ESP                                     ║
║       • F2 - Toggle Aimbot                                  ║
║       • INSERT - Toggle Menu                                ║
║       • END - Emergency Stop                                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)

def print_help():
    """Print help information"""
    help_text = """
🎯 PHANTOM STRIKE - Usage Guide

📋 Command Line Options:
    --help, -h          Show this help message
    --debug, -d         Enable debug mode
    --status, -s        Show status information
    --config <file>     Load configuration file
    --export <file>     Export current configuration
    --import <file>     Import configuration file
    --reset <type>      Reset configuration type
    --protection <level> Set protection level
    --emergency         Emergency stop all features

🎮 In-Game Controls:
    F1              Toggle ESP
    F2              Toggle Aimbot
    F3              Toggle AI Aimbot
    F4              Toggle Radar
    F5              Toggle Stats
    F6              Toggle Skins
    INSERT          Toggle Menu
    END             Emergency Stop

🛡️ Protection Levels:
    minimal         Basic protection only
    standard        Recommended for most users
    aggressive      Maximum protection
    paranoid       Ultimate stealth mode

📁 Configuration Files:
    configs/        Main configuration directory
    backups/        Configuration backups
    logs/           Log files

🔧 Supported Games:
    BloodStrike (Linux)

⚠️ Safety Notice:
    - Use responsibly and at your own risk
    - Follow all game terms of service
    - Keep software updated
    - Use in private matches only

For more information, check the documentation files.
"""
    print(help_text)

def main():
    """Main entry point"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Phantom Strike - BloodStrike Professional Cheat Suite')
    parser.add_argument('--debug', '-d', action='store_true', help='Enable debug mode')
    parser.add_argument('--status', '-s', action='store_true', help='Show status information')
    parser.add_argument('--config', help='Load configuration file')
    parser.add_argument('--export', help='Export current configuration')
    parser.add_argument('--import', help='Import configuration file')
    parser.add_argument('--reset', help='Reset configuration type')
    parser.add_argument('--protection', choices=['minimal', 'standard', 'aggressive', 'paranoid'], 
                       help='Set protection level')
    parser.add_argument('--emergency', action='store_true', help='Emergency stop all features')
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # Handle special commands
    if args.help or len(sys.argv) == 1:
        print_help()
        return
    
    if args.emergency:
        print("🚨 Emergency stop requested")
        # Find and kill any running instances
        try:
            import subprocess
            result = subprocess.run(['pkill', '-f', 'phantom_strike'], capture_output=True)
            if result.returncode == 0:
                print("✅ Emergency stop completed")
            else:
                print("⚠️ No running instances found")
        except:
            print("❌ Emergency stop failed")
        return
    
    # Initialize launcher
    launcher = PhantomStrikeLauncher()
    
    # Set debug mode
    if args.debug:
        launcher.toggle_debug()
    
    # Handle configuration operations
    if args.config and launcher.config_manager:
        print(f"📂 Loading configuration from: {args.config}")
        launcher.config_manager.import_configuration(args.config, overwrite=True)
    
    if args.export and launcher.config_manager:
        print(f"📤 Exporting configuration to: {args.export}")
        launcher.config_manager.export_configuration(args.export)
        return
    
    if args.import and launcher.config_manager:
        print(f"📥 Importing configuration from: {args.import}")
        launcher.config_manager.import_configuration(args.import)
    
    if args.reset and launcher.config_manager:
        try:
            config_type = ConfigType(args.reset)
            print(f"🔄 Resetting {args.reset} configuration")
            launcher.config_manager.reset_configuration(config_type)
        except ValueError:
            print(f"❌ Unknown configuration type: {args.reset}")
        return
    
    if args.protection and launcher.anti_cheat:
        print(f"🛡️ Setting protection level to: {args.protection}")
        protection_level = ProtectionLevel(args.protection)
        launcher.anti_cheat.enable_protection(protection_level)
    
    if args.status:
        launcher.print_status()
        return
    
    # Set up signal handlers
    signal.signal(signal.SIGINT, launcher.handle_signal)
    signal.signal(signal.SIGTERM, launcher.handle_signal)
    
    # Start the cheat suite
    try:
        launcher.start()
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        launcher.cleanup()
        sys.exit(1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Dynamic Offset Manager - Integrates with cheat and updates automatically
Manages offset persistence and automatic cheat updates
"""

import sys
import os
import json
import time
import threading
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime
import importlib
import inspect

from auto_offset_scanner import OffsetScanner, get_scanner, OffsetData

class DynamicOffsetManager:
    """Manages dynamic offsets and updates cheat automatically"""
    
    def __init__(self):
        self.scanner = get_scanner()
        self.cheat_modules = {}
        self.offset_callbacks = {}
        self.update_queue = []
        self.processing_updates = False
        
        # File paths
        self.config_file = "offset_config.json"
        self.cheat_config_file = "cheat_offset_config.json"
        
        # Load configuration
        self.load_config()
        
        # Register update callback
        self.scanner.update_callback = self.on_offset_updated
        
        # Start update processor
        self.start_update_processor()
        
        print("🔄 Dynamic offset manager initialized")
    
    def register_cheat_module(self, module_name: str, module_object: Any):
        """Register a cheat module for offset updates"""
        try:
            self.cheat_modules[module_name] = module_object
            print(f"📝 Registered cheat module: {module_name}")
            
            # Apply current offsets to this module
            self.apply_offsets_to_module(module_name, module_object)
            
        except Exception as e:
            print(f"⚠ Failed to register module {module_name}: {e}")
    
    def register_offset_callback(self, offset_name: str, callback: Callable[[Any], None]):
        """Register a callback for when an offset is updated"""
        if offset_name not in self.offset_callbacks:
            self.offset_callbacks[offset_name] = []
        self.offset_callbacks[offset_name].append(callback)
        print(f"🔔 Registered callback for offset: {offset_name}")
    
    def on_offset_updated(self, offset_name: str, offset_data: OffsetData):
        """Called when an offset is updated"""
        self.update_queue.append((offset_name, offset_data, time.time()))
    
    def start_update_processor(self):
        """Start background update processor"""
        self.update_thread = threading.Thread(target=self.process_updates, daemon=True)
        self.update_thread.start()
    
    def process_updates(self):
        """Process offset updates in background"""
        while True:
            try:
                if self.update_queue and not self.processing_updates:
                    self.processing_updates = True
                    
                    while self.update_queue:
                        offset_name, offset_data, update_time = self.update_queue.pop(0)
                        self.apply_offset_update(offset_name, offset_data)
                    
                    self.processing_updates = False
                
                time.sleep(0.1)  # Check every 100ms
                
            except Exception as e:
                print(f"⚠ Update processor error: {e}")
                self.processing_updates = False
    
    def apply_offset_update(self, offset_name: str, offset_data: OffsetData):
        """Apply offset update to all registered modules"""
        try:
            print(f"🔄 Applying update for {offset_name}")
            
            # Update all cheat modules
            for module_name, module_object in self.cheat_modules.items():
                self.apply_offset_to_module(module_name, module_object, offset_name, offset_data)
            
            # Call registered callbacks
            if offset_name in self.offset_callbacks:
                for callback in self.offset_callbacks[offset_name]:
                    try:
                        callback(offset_data.value)
                    except Exception as e:
                        print(f"⚠ Callback error for {offset_name}: {e}")
            
            # Save updated configuration
            self.save_config()
            
            print(f"✅ Successfully applied update for {offset_name}")
            
        except Exception as e:
            print(f"⚠ Failed to apply update for {offset_name}: {e}")
    
    def apply_offset_to_module(self, module_name: str, module_object: Any, 
                             offset_name: Optional[str] = None, offset_data: Optional[OffsetData] = None):
        """Apply offsets to a specific module"""
        try:
            if offset_name and offset_data:
                # Apply specific offset
                self._set_module_offset(module_object, offset_name, offset_data.value)
            else:
                # Apply all current offsets
                for name, data in self.scanner.found_offsets.items():
                    self._set_module_offset(module_object, name, data.value)
                    
        except Exception as e:
            print(f"⚠ Failed to apply offsets to {module_name}: {e}")
    
    def _set_module_offset(self, module_object: Any, offset_name: str, offset_value: Any):
        """Set offset in module object"""
        try:
            # Check if module has the offset attribute
            if hasattr(module_object, offset_name):
                setattr(module_object, offset_name, offset_value)
            else:
                # Try to set in nested objects
                if hasattr(module_object, '__dict__'):
                    for attr_name, attr_value in module_object.__dict__.items():
                        if hasattr(attr_value, offset_name):
                            setattr(attr_value, offset_name, offset_value)
                            break
                        
        except Exception as e:
            print(f"⚠ Failed to set offset {offset_name}: {e}")
    
    def create_offset_config(self) -> Dict[str, Any]:
        """Create configuration for current offsets"""
        config = {
            'timestamp': time.time(),
            'version': '1.0',
            'offsets': {},
            'patterns': {}
        }
        
        # Add found offsets
        for name, offset in self.scanner.found_offsets.items():
            config['offsets'][name] = {
                'type': offset.type,
                'value': str(offset.value),
                'confidence': offset.confidence,
                'verification_count': offset.verification_count
            }
        
        # Add pattern information
        for pattern in self.scanner.patterns:
            config['patterns'][pattern.name] = {
                'pattern_type': pattern.pattern_type,
                'pattern': str(pattern.pattern),
                'offset_path': pattern.offset_path,
                'success_rate': pattern.success_rate,
                'last_found': pattern.last_found
            }
        
        return config
    
    def save_config(self):
        """Save current configuration"""
        try:
            config = self.create_offset_config()
            
            # Save main config
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            # Create cheat-specific config
            cheat_config = self.create_cheat_config()
            with open(self.cheat_config_file, 'w') as f:
                json.dump(cheat_config, f, indent=2)
            
        except Exception as e:
            print(f"⚠ Failed to save config: {e}")
    
    def create_cheat_config(self) -> Dict[str, Any]:
        """Create cheat-specific configuration"""
        config = {
            'timestamp': time.time(),
            'auto_update': True,
            'confidence_threshold': self.scanner.confidence_threshold,
            'scan_interval': self.scanner.scan_interval,
            'offsets': {}
        }
        
        # Add offsets in cheat-friendly format
        for name, offset in self.scanner.found_offsets.items():
            config['offsets'][name] = {
                'value': offset.value,
                'type': offset.type,
                'confidence': offset.confidence,
                'last_verified': offset.timestamp
            }
        
        return config
    
    def load_config(self):
        """Load configuration from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                
                # Apply configuration
                if 'confidence_threshold' in config:
                    self.scanner.confidence_threshold = config['confidence_threshold']
                if 'scan_interval' in config:
                    self.scanner.scan_interval = config['scan_interval']
                
                print(f"📁 Loaded configuration from {config['timestamp']}")
                
        except Exception as e:
            print(f"⚠ Failed to load config: {e}")
    
    def reload_module_with_offsets(self, module_name: str):
        """Reload a module and reapply offsets"""
        try:
            if module_name in self.cheat_modules:
                module = self.cheat_modules[module_name]
                
                # Reload the module
                importlib.reload(module)
                
                # Reapply offsets
                self.apply_offsets_to_module(module_name, module)
                
                print(f"🔄 Reloaded module {module_name} with updated offsets")
                
        except Exception as e:
            print(f"⚠ Failed to reload module {module_name}: {e}")
    
    def get_module_offset_status(self, module_name: str) -> Dict[str, Any]:
        """Get offset status for a specific module"""
        status = {
            'module': module_name,
            'registered': module_name in self.cheat_modules,
            'offsets_applied': 0,
            'offsets_missing': 0,
            'details': {}
        }
        
        if module_name in self.cheat_modules:
            module = self.cheat_modules[module_name]
            
            for name, offset in self.scanner.found_offsets.items():
                if hasattr(module, name):
                    status['offsets_applied'] += 1
                    status['details'][name] = {
                        'applied': True,
                        'value': getattr(module, name),
                        'confidence': offset.confidence
                    }
                else:
                    status['offsets_missing'] += 1
                    status['details'][name] = {
                        'applied': False,
                        'confidence': offset.confidence
                    }
        
        return status
    
    def auto_update_cheat(self):
        """Automatically update all cheat components"""
        try:
            print("🔄 Starting automatic cheat update...")
            
            # Update all registered modules
            for module_name in self.cheat_modules:
                self.reload_module_with_offsets(module_name)
            
            # Verify all offsets
            verification_results = self.scanner.verify_offsets()
            
            # Report results
            success_count = sum(1 for success in verification_results.values() if success)
            total_count = len(verification_results)
            
            print(f"✅ Auto-update completed: {success_count}/{total_count} offsets verified")
            
            return success_count == total_count
            
        except Exception as e:
            print(f"⚠ Auto-update failed: {e}")
            return False
    
    def create_offset_monitor(self) -> 'OffsetMonitor':
        """Create an offset monitor GUI"""
        return OffsetMonitor(self)

class OffsetMonitor:
    """Monitor for offset status and updates"""
    
    def __init__(self, manager: DynamicOffsetManager):
        self.manager = manager
        self.running = False
        
    def start_monitoring(self):
        """Start monitoring in console"""
        self.running = True
        print("👁️  Starting offset monitor...")
        
        try:
            while self.running:
                self.print_status()
                time.sleep(5)
        except KeyboardInterrupt:
            self.stop_monitoring()
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.running = False
        print("🛑 Offset monitor stopped")
    
    def print_status(self):
        """Print current status"""
        print("\n" + "="*60)
        print(f"🔍 OFFSET MONITOR - {datetime.now().strftime('%H:%M:%S')}")
        print("="*60)
        
        # Scanner statistics
        stats = self.manager.scanner.get_statistics()
        print(f"📊 Scanner Stats:")
        print(f"   Scans: {stats['scan_count']}")
        print(f"   Found: {stats['patterns_found']}/{stats['total_patterns']}")
        print(f"   Success: {stats['success_rate']:.1%}")
        
        # Module status
        print(f"\n📝 Registered Modules: {len(self.manager.cheat_modules)}")
        for module_name in self.manager.cheat_modules:
            status = self.manager.get_module_offset_status(module_name)
            print(f"   {module_name}: {status['offsets_applied']} applied, {status['offsets_missing']} missing")
        
        # Recent updates
        if self.manager.update_queue:
            print(f"\n🔄 Pending Updates: {len(self.manager.update_queue)}")
        
        print("="*60)

# Global manager instance
manager = None

def get_manager() -> DynamicOffsetManager:
    """Get or create manager instance"""
    global manager
    if manager is None:
        manager = DynamicOffsetManager()
    return manager

def start_dynamic_manager():
    """Start the dynamic offset manager"""
    manager = get_manager()
    return manager

def register_cheat_module(module_name: str, module_object: Any):
    """Register a cheat module for dynamic updates"""
    manager = get_manager()
    manager.register_cheat_module(module_name, module_object)

def register_offset_callback(offset_name: str, callback: Callable[[Any], None]):
    """Register a callback for offset updates"""
    manager = get_manager()
    manager.register_offset_callback(offset_name, callback)

def auto_update_cheat():
    """Trigger automatic cheat update"""
    manager = get_manager()
    return manager.auto_update_cheat()

def start_monitor():
    """Start offset monitoring"""
    manager = get_manager()
    monitor = manager.create_offset_monitor()
    monitor.start_monitoring()

if __name__ == "__main__":
    # Test the dynamic manager
    print("🚀 Starting Dynamic Offset Manager...")
    manager = start_dynamic_manager()
    
    # Start monitoring
    monitor = manager.create_offset_monitor()
    monitor.start_monitoring()

#!/usr/bin/env python3
"""
Automatic Offset Scanner and Updater for BloodStrike
Continuously scans for patterns and updates offsets automatically
"""

import sys
import os
import json
import time
import pickle
import hashlib
import re
import gc
from typing import Dict, List, Tuple, Any, Optional, Callable
from dataclasses import dataclass, asdict
from datetime import datetime
import threading
import inspect

# Add game SDK path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'SDK'))

try:
    from gclient.framework.entities.space import Space
    from gclient.framework.util.story_tick import StoryTick
    from gclient.gameplay.logic_base.entities.combat_avatar import CombatAvatar
    INTERNAL_MODE = True
except ImportError:
    INTERNAL_MODE = False
    print("⚠ Auto scanner requires internal mode")

@dataclass
class OffsetPattern:
    """Pattern for finding offsets"""
    name: str
    pattern_type: str  # 'attribute', 'method', 'class', 'signature'
    pattern: Any
    offset_path: List[str]
    description: str
    confidence: float = 0.0
    last_found: Optional[float] = None
    scan_count: int = 0
    success_rate: float = 0.0

@dataclass
class OffsetData:
    """Stored offset data"""
    name: str
    value: Any
    type: str
    pattern_hash: str
    timestamp: float
    confidence: float
    verification_count: int = 0

class OffsetScanner:
    """Automatic offset scanner for BloodStrike"""
    
    def __init__(self):
        self.patterns: List[OffsetPattern] = []
        self.found_offsets: Dict[str, OffsetData] = {}
        self.scanning = False
        self.scan_interval = 5.0  # Scan every 5 seconds
        self.save_interval = 30.0  # Save every 30 seconds
        self.confidence_threshold = 0.7
        
        # File paths
        self.offsets_file = "offsets_database.json"
        self.patterns_file = "offset_patterns.json"
        self.backup_file = "offsets_backup.json"
        
        # Statistics
        self.scan_count = 0
        self.last_scan_time = 0
        self.pattern_matches = 0
        
        # Initialize patterns
        self.init_patterns()
        
        # Load existing data
        self.load_offsets()
        self.load_patterns()
        
        # Start background scanning
        if INTERNAL_MODE:
            self.start_scanning()
    
    def init_patterns(self):
        """Initialize offset patterns for BloodStrike"""
        
        # Load real BloodStrike patterns from DLL analysis
        try:
            from bloodstrike_real_patterns import get_bloodstrike_patterns
            real_patterns = get_bloodstrike_patterns()
            for pattern in real_patterns:
                self.patterns.append(pattern)
            print(f"🎯 Loaded {len(real_patterns)} verified BloodStrike patterns")
        except ImportError:
            print("⚠ Real patterns not available, using fallback patterns")
            self._init_fallback_patterns()
    
    def _init_fallback_patterns(self):
        """Fallback patterns if real patterns not available"""
        
        # CombatAvatar patterns
        self.add_pattern(OffsetPattern(
            name="health",
            pattern_type="attribute",
            pattern="hp",
            offset_path=["CombatAvatar", "hp"],
            description="Player health attribute"
        ))
        
        self.add_pattern(OffsetPattern(
            name="max_health",
            pattern_type="attribute", 
            pattern="cur_maxhp",
            offset_path=["CombatAvatar", "cur_maxhp"],
            description="Player max health attribute"
        ))
        
        self.add_pattern(OffsetPattern(
            name="position",
            pattern_type="attribute",
            pattern="position",
            offset_path=["CombatAvatar", "position"],
            description="Player position (x,y,z)"
        ))
        
        self.add_pattern(OffsetPattern(
            name="team_id",
            pattern_type="attribute",
            pattern="team_id",
            offset_path=["CombatAvatar", "team_id"],
            description="Player team identifier"
        ))
        
        # Space patterns
        self.add_pattern(OffsetPattern(
            name="space_instance",
            pattern_type="class_attribute",
            pattern="_instance",
            offset_path=["Space", "_instance"],
            description="Space singleton instance"
        ))
        
        self.add_pattern(OffsetPattern(
            name="space_entities",
            pattern_type="attribute",
            pattern="entities",
            offset_path=["Space", "entities"],
            description="Space entities dictionary"
        ))
        
        # Camera patterns
        self.add_pattern(OffsetPattern(
            name="camera",
            pattern_type="attribute",
            pattern="camera",
            offset_path=["Space", "camera"],
            description="Game camera instance"
        ))
        
        # Method patterns
        self.add_pattern(OffsetPattern(
            name="get_bone_position",
            pattern_type="method",
            pattern="GetBoneWorldPosition",
            offset_path=["CombatAvatar", "model", "GetBoneWorldPosition"],
            description="Get bone world position method"
        ))
        
        self.add_pattern(OffsetPattern(
            name="world_to_screen",
            pattern_type="method",
            pattern="GetScreenPointFromWorldPoint",
            offset_path=["camera", "engine_camera", "GetScreenPointFromWorldPoint"],
            description="World to screen conversion method"
        ))
        
        # Bone name patterns
        bone_names = ['biped Head', 'biped Spine1', 'biped Spine', 'HP_Pelvis', 
                     'biped L Hand', 'biped R Hand', 'biped L Foot', 'biped R Foot']
        
        for bone_name in bone_names:
            self.add_pattern(OffsetPattern(
                name=f"bone_{bone_name.replace(' ', '_').lower()}",
                pattern_type="string",
                pattern=bone_name,
                offset_path=["bones", bone_name],
                description=f"Bone: {bone_name}"
            ))
    
    def add_pattern(self, pattern: OffsetPattern):
        """Add a pattern to scan for"""
        self.patterns.append(pattern)
    
    def start_scanning(self):
        """Start background scanning"""
        self.scanning = True
        self.scan_thread = threading.Thread(target=self.scan_loop, daemon=True)
        self.save_thread = threading.Thread(target=self.save_loop, daemon=True)
        self.scan_thread.start()
        self.save_thread.start()
        print("🔍 Auto offset scanner started")
    
    def scan_loop(self):
        """Main scanning loop"""
        while self.scanning:
            try:
                self.perform_scan()
                time.sleep(self.scan_interval)
            except Exception as e:
                print(f"⚠ Scan error: {e}")
                time.sleep(self.scan_interval)
    
    def save_loop(self):
        """Periodic save loop"""
        while self.scanning:
            try:
                self.save_offsets()
                time.sleep(self.save_interval)
            except Exception as e:
                print(f"⚠ Save error: {e}")
                time.sleep(self.save_interval)
    
    def perform_scan(self):
        """Perform a full scan of all patterns"""
        if not INTERNAL_MODE:
            return
            
        self.last_scan_time = time.time()
        self.scan_count += 1
        
        try:
            # Get game objects
            space = getattr(Space, '_instance', None)
            if not space:
                return
            
            # Scan each pattern
            for pattern in self.patterns:
                self.scan_pattern(pattern, space)
            
            # Update statistics
            print(f"🔍 Scan #{self.scan_count}: {self.pattern_matches} patterns matched")
            
        except Exception as e:
            print(f"⚠ Scan error: {e}")
    
    def scan_pattern(self, pattern: OffsetPattern, space):
        """Scan for a specific pattern"""
        try:
            pattern.scan_count += 1
            found_value = None
            confidence = 0.0
            
            if pattern.pattern_type == "attribute":
                found_value, confidence = self.scan_attribute_pattern(pattern, space)
            elif pattern.pattern_type == "method":
                found_value, confidence = self.scan_method_pattern(pattern, space)
            elif pattern.pattern_type == "class_attribute":
                found_value, confidence = self.scan_class_attribute_pattern(pattern)
            elif pattern.pattern_type == "string":
                found_value, confidence = self.scan_string_pattern(pattern)
            
            if found_value is not None and confidence >= self.confidence_threshold:
                self.update_offset(pattern.name, found_value, pattern, confidence)
                pattern.last_found = time.time()
                pattern.success_rate = (pattern.success_rate * (pattern.scan_count - 1) + confidence) / pattern.scan_count
                self.pattern_matches += 1
                
        except Exception as e:
            print(f"⚠ Pattern scan error for {pattern.name}: {e}")
    
    def scan_attribute_pattern(self, pattern: OffsetPattern, space) -> Tuple[Any, float]:
        """Scan for attribute patterns"""
        try:
            # Look for pattern in entities
            if hasattr(space, 'entities'):
                for entity in space.entities.values():
                    if hasattr(entity, pattern.pattern):
                        value = getattr(entity, pattern.pattern)
                        return value, 0.9  # High confidence for direct attribute match
            
            # Look in space itself
            if hasattr(space, pattern.pattern):
                value = getattr(space, pattern.pattern)
                return value, 0.9
                
            # Look in camera
            camera = getattr(space, 'camera', None)
            if camera and hasattr(camera, pattern.pattern):
                value = getattr(camera, pattern.pattern)
                return value, 0.9
                
        except Exception:
            pass
        
        return None, 0.0
    
    def scan_method_pattern(self, pattern: OffsetPattern, space) -> Tuple[Any, float]:
        """Scan for method patterns"""
        try:
            # Look for methods in entities
            if hasattr(space, 'entities'):
                for entity in space.entities.values():
                    if hasattr(entity, 'model') and hasattr(entity.model, pattern.pattern):
                        method = getattr(entity.model, pattern.pattern)
                        if callable(method):
                            return method, 0.8
            
            # Look in camera
            camera = getattr(space, 'camera', None)
            if camera and hasattr(camera, 'engine_camera'):
                engine_camera = getattr(camera, 'engine_camera')
                if hasattr(engine_camera, pattern.pattern):
                    method = getattr(engine_camera, pattern.pattern)
                    if callable(method):
                        return method, 0.8
                        
        except Exception:
            pass
        
        return None, 0.0
    
    def scan_class_attribute_pattern(self, pattern: OffsetPattern) -> Tuple[Any, float]:
        """Scan for class-level attributes"""
        try:
            if pattern.pattern_path[0] == "Space":
                space_class = globals().get('Space')
                if space_class and hasattr(space_class, pattern.pattern):
                    value = getattr(space_class, pattern.pattern)
                    return value, 0.95  # Very high confidence for class attributes
                    
        except Exception:
            pass
        
        return None, 0.0
    
    def scan_string_pattern(self, pattern: OffsetPattern) -> Tuple[Any, float]:
        """Scan for string patterns (like bone names)"""
        try:
            # For bone names, we just return the string itself
            # The actual usage will be in method calls
            return pattern.pattern, 0.85
            
        except Exception:
            pass
        
        return None, 0.0
    
    def update_offset(self, name: str, value: Any, pattern: OffsetPattern, confidence: float):
        """Update or create offset data"""
        pattern_hash = self.calculate_pattern_hash(pattern)
        
        if name in self.found_offsets:
            # Update existing offset
            offset = self.found_offsets[name]
            offset.value = value
            offset.timestamp = time.time()
            offset.confidence = (offset.confidence + confidence) / 2
            offset.verification_count += 1
        else:
            # Create new offset
            self.found_offsets[name] = OffsetData(
                name=name,
                value=value,
                type=pattern.pattern_type,
                pattern_hash=pattern_hash,
                timestamp=time.time(),
                confidence=confidence,
                verification_count=1
            )
            print(f"✅ Found new offset: {name} (confidence: {confidence:.2f})")
    
    def calculate_pattern_hash(self, pattern: OffsetPattern) -> str:
        """Calculate hash for pattern verification"""
        pattern_str = f"{pattern.pattern_type}:{pattern.pattern}:{':'.join(pattern.offset_path)}"
        return hashlib.md5(pattern_str.encode()).hexdigest()
    
    def get_offset(self, name: str) -> Optional[OffsetData]:
        """Get offset data by name"""
        return self.found_offsets.get(name)
    
    def verify_offsets(self) -> Dict[str, bool]:
        """Verify all found offsets"""
        results = {}
        
        for name, offset in self.found_offsets.items():
            try:
                # Try to access the offset
                if offset.type == "attribute":
                    # Test if we can access the attribute
                    if hasattr(offset.value, '__call__'):
                        # It's callable, try calling with no args
                        offset.value()
                    results[name] = True
                elif offset.type == "method":
                    # Test if it's callable
                    results[name] = callable(offset.value)
                else:
                    results[name] = True
                    
            except Exception as e:
                print(f"⚠ Offset verification failed for {name}: {e}")
                results[name] = False
        
        return results
    
    def save_offsets(self):
        """Save offsets to file"""
        try:
            # Convert to serializable format
            serializable_data = {}
            for name, offset in self.found_offsets.items():
                serializable_data[name] = {
                    'name': offset.name,
                    'value': str(offset.value),  # Convert to string for serialization
                    'type': offset.type,
                    'pattern_hash': offset.pattern_hash,
                    'timestamp': offset.timestamp,
                    'confidence': offset.confidence,
                    'verification_count': offset.verification_count
                }
            
            # Save main file
            with open(self.offsets_file, 'w') as f:
                json.dump(serializable_data, f, indent=2)
            
            # Save backup
            with open(self.backup_file, 'w') as f:
                json.dump(serializable_data, f, indent=2)
            
            # Save patterns
            patterns_data = []
            for pattern in self.patterns:
                pattern_dict = asdict(pattern)
                # Convert non-serializable fields
                if hasattr(pattern.pattern, '__call__'):
                    pattern_dict['pattern'] = pattern.pattern.__name__
                patterns_data.append(pattern_dict)
            
            with open(self.patterns_file, 'w') as f:
                json.dump(patterns_data, f, indent=2)
            
        except Exception as e:
            print(f"⚠ Save error: {e}")
    
    def load_offsets(self):
        """Load offsets from file"""
        try:
            if os.path.exists(self.offsets_file):
                with open(self.offsets_file, 'r') as f:
                    data = json.load(f)
                
                for name, offset_data in data.items():
                    self.found_offsets[name] = OffsetData(**offset_data)
                
                print(f"📁 Loaded {len(self.found_offsets)} offsets from file")
                
        except Exception as e:
            print(f"⚠ Load error: {e}")
    
    def load_patterns(self):
        """Load patterns from file"""
        try:
            if os.path.exists(self.patterns_file):
                with open(self.patterns_file, 'r') as f:
                    patterns_data = json.load(f)
                
                # Merge with existing patterns
                for pattern_dict in patterns_data:
                    pattern = OffsetPattern(**pattern_dict)
                    if pattern.name not in [p.name for p in self.patterns]:
                        self.patterns.append(pattern)
                
        except Exception as e:
            print(f"⚠ Pattern load error: {e}")
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get scanner statistics"""
        return {
            'scan_count': self.scan_count,
            'last_scan_time': self.last_scan_time,
            'patterns_found': len(self.found_offsets),
            'total_patterns': len(self.patterns),
            'pattern_matches': self.pattern_matches,
            'success_rate': len(self.found_offsets) / max(len(self.patterns), 1)
        }
    
    def stop_scanning(self):
        """Stop scanning threads"""
        self.scanning = False
        self.save_offsets()
        print("🛑 Auto offset scanner stopped")

# Global scanner instance
scanner = None

def get_scanner() -> OffsetScanner:
    """Get or create scanner instance"""
    global scanner
    if scanner is None:
        scanner = OffsetScanner()
    return scanner

def start_auto_scanner():
    """Start the automatic offset scanner"""
    scanner = get_scanner()
    return scanner

def get_offset(name: str) -> Optional[Any]:
    """Get offset value by name"""
    scanner = get_scanner()
    offset = scanner.get_offset(name)
    return offset.value if offset else None

def verify_all_offsets() -> Dict[str, bool]:
    """Verify all found offsets"""
    scanner = get_scanner()
    return scanner.verify_offsets()

def print_offset_status():
    """Print current offset status"""
    scanner = get_scanner()
    stats = scanner.get_statistics()
    
    print("\n🔍 Offset Scanner Status:")
    print(f"   Scans performed: {stats['scan_count']}")
    print(f"   Patterns found: {stats['patterns_found']}/{stats['total_patterns']}")
    print(f"   Success rate: {stats['success_rate']:.1%}")
    print(f"   Last scan: {datetime.fromtimestamp(stats['last_scan_time']) if stats['last_scan_time'] else 'Never'}")
    
    print("\n📋 Found Offsets:")
    for name, offset in scanner.found_offsets.items():
        status = "✅" if offset.confidence > 0.8 else "⚠️" if offset.confidence > 0.5 else "❌"
        print(f"   {status} {name}: {offset.type} (confidence: {offset.confidence:.2f})")

if __name__ == "__main__":
    # Test the scanner
    if INTERNAL_MODE:
        print("🚀 Starting BloodStrike Auto Offset Scanner...")
        scanner = start_auto_scanner()
        
        try:
            while True:
                time.sleep(10)
                print_offset_status()
        except KeyboardInterrupt:
            scanner.stop_scanning()
    else:
        print("❌ Scanner requires internal mode (injected into BloodStrike)")

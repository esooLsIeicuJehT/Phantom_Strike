#!/usr/bin/env python3
"""
PHANTOM STRIKE - Windows Memory Scanner
Advanced memory scanning with pattern recognition
"""

import ctypes
import ctypes.wintypes
import struct
import time
from typing import Optional, List, Dict, Tuple

# Windows API constants
PROCESS_VM_READ = 0x0010
PROCESS_QUERY_INFORMATION = 0x0400
MEM_COMMIT = 0x1000
MEM_PRIVATE = 0x20000
MEM_IMAGE = 0x10000000
PAGE_READABLE = 0x01 | 0x02 | 0x04 | 0x08 | 0x10 | 0x80

class PhantomMemoryScanner:
    """Advanced memory scanner for PHANTOM STRIKE"""
    
    def __init__(self):
        self.process_handle = None
        self.process_id = None
        self.base_address = None
        self.memory_regions = []
        
    def attach_to_process(self, process_name: str) -> bool:
        """Attach to BloodStrike process"""
        try:
            # Find process
            self.process_id = self._find_process_id(process_name)
            if not self.process_id:
                print(f"❌ Process {process_name} not found")
                return False
            
            # Open process with required privileges
            self.process_handle = ctypes.windll.kernel32.OpenProcess(
                PROCESS_VM_READ | PROCESS_QUERY_INFORMATION,
                False,
                self.process_id
            )
            
            if not self.process_handle:
                print("❌ Failed to open process")
                return False
            
            # Get base address
            self.base_address = self._get_base_address()
            if not self.base_address:
                print("❌ Failed to get base address")
                return False
            
            # Enumerate memory regions
            self._enumerate_memory_regions()
            
            print(f"✅ Attached to process {process_name} (PID: {self.process_id})")
            print(f"📍 Base address: 0x{self.base_address:08X}")
            print(f"🗂️ Memory regions: {len(self.memory_regions)}")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to attach: {e}")
            return False
    
    def _find_process_id(self, process_name: str) -> Optional[int]:
        """Find process ID by name"""
        try:
            import psutil
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] and process_name.lower() in proc.info['name'].lower():
                    return proc.info['pid']
        except ImportError:
            # Fallback to Windows API
            return self._find_process_id_winapi(process_name)
        
        return None
    
    def _find_process_id_winapi(self, process_name: str) -> Optional[int]:
        """Find process ID using Windows API"""
        try:
            from ctypes import wintypes
            psapi = ctypes.windll.psapi
            
            # Enumerate processes
            process_ids = (ctypes.c_ulong * 1024)()
            bytes_returned = ctypes.c_ulong()
            
            if psapi.EnumProcesses(
                ctypes.byref(process_ids),
                ctypes.sizeof(process_ids),
                ctypes.byref(bytes_returned)
            ):
                count = bytes_returned.value // ctypes.sizeof(ctypes.c_ulong)
                
                for i in range(count):
                    pid = process_ids[i]
                    if pid == 0:
                        continue
                    
                    # Get process name
                    handle = ctypes.windll.kernel32.OpenProcess(
                        0x0400 | 0x0010, False, pid
                    )
                    if handle:
                        name = self._get_process_name_by_handle(handle)
                        ctypes.windll.kernel32.CloseHandle(handle)
                        
                        if name and process_name.lower() in name.lower():
                            return pid
        except Exception:
            pass
        
        return None
    
    def _get_process_name_by_handle(self, handle) -> Optional[str]:
        """Get process name from process handle"""
        try:
            buffer = ctypes.create_string_buffer(256)
            size = ctypes.windll.psapi.GetModuleBaseNameA(
                handle, None, buffer, 256
            )
            
            if size > 0:
                return buffer.value.decode('utf-8')
        except Exception:
            pass
        
        return None
    
    def _get_base_address(self) -> Optional[int]:
        """Get module base address"""
        try:
            from ctypes import wintypes
            psapi = ctypes.windll.psapi
            
            # Get module information
            modules = (ctypes.c_void_p * 1024)()
            bytes_needed = ctypes.c_ulong()
            
            if psapi.EnumProcessModulesEx(
                self.process_handle,
                ctypes.byref(modules),
                ctypes.sizeof(modules),
                ctypes.byref(bytes_needed),
                3  # LIST_MODULES_ALL
            ):
                # Get first module (main executable)
                module_handle = modules[0]
                base_address = ctypes.c_void_p()
                
                if psapi.GetModuleInformation(
                    self.process_handle,
                    module_handle,
                    ctypes.byref(base_address),
                    ctypes.sizeof(base_address)
                ):
                    return base_address.value
        except Exception:
            pass
        
        return None
    
    def _enumerate_memory_regions(self):
        """Enumerate readable memory regions"""
        try:
            from ctypes import wintypes
            
            # Memory Basic Information structure
            class MEMORY_BASIC_INFORMATION(ctypes.Structure):
                _fields_ = [
                    ('BaseAddress', ctypes.c_void_p),
                    ('AllocationBase', ctypes.c_void_p),
                    ('AllocationProtect', wintypes.DWORD),
                    ('RegionSize', ctypes.c_size_t),
                    ('State', wintypes.DWORD),
                    ('Protect', wintypes.DWORD),
                    ('Type', wintypes.DWORD),
                ]
            
            mbi = MEMORY_BASIC_INFORMATION()
            address = 0
            
            while ctypes.windll.kernel32.VirtualQueryEx(
                self.process_handle,
                ctypes.c_void_p(address),
                ctypes.byref(mbi),
                ctypes.sizeof(mbi)
            ):
                # Check if region is readable
                if (mbi.State == MEM_COMMIT and 
                    mbi.Protect & PAGE_READABLE and
                    mbi.RegionSize > 0):
                    
                    self.memory_regions.append({
                        'base': mbi.BaseAddress,
                        'size': mbi.RegionSize,
                        'protect': mbi.Protect,
                        'type': mbi.Type
                    })
                
                address = mbi.BaseAddress + mbi.RegionSize
                
                # Prevent infinite loop
                if address > 0x7FFFFFFF:
                    break
                    
        except Exception as e:
            print(f"⚠ Memory enumeration error: {e}")
    
    def scan_pattern(self, pattern: bytes, mask: str = None) -> List[int]:
        """Scan memory for byte pattern"""
        matches = []
        
        if not self.process_handle:
            print("❌ Not attached to process")
            return matches
        
        print(f"🔍 Scanning for pattern: {pattern[:20].hex()}...")
        
        for region in self.memory_regions:
            try:
                # Skip large regions to prevent timeouts
                if region['size'] > 0x10000000:  # 256MB
                    continue
                
                # Read memory region
                data = self._read_memory(region['base'], region['size'])
                if not data:
                    continue
                
                # Search for pattern
                for i in range(len(data) - len(pattern) + 1):
                    if self._pattern_matches(data[i:i+len(pattern)], pattern, mask):
                        address = region['base'] + i
                        matches.append(address)
                        print(f"✅ Found pattern at 0x{address:08X}")
                        
                        # Limit results to prevent spam
                        if len(matches) >= 10:
                            break
                
                if len(matches) >= 10:
                    break
                    
            except Exception as e:
                continue
        
        print(f"🎯 Pattern scan complete: {len(matches)} matches found")
        return matches
    
    def _pattern_matches(self, data: bytes, pattern: bytes, mask: str = None) -> bool:
        """Check if data matches pattern"""
        if len(data) != len(pattern):
            return False
        
        if mask is None:
            return data == pattern
        
        for i, (d, p) in enumerate(zip(data, pattern)):
            if mask[i] != '?' and d != p:
                return False
        
        return True
    
    def _read_memory(self, address: int, size: int) -> Optional[bytes]:
        """Read memory from process"""
        try:
            buffer = ctypes.create_string_buffer(size)
            bytes_read = ctypes.c_size_t()
            
            if ctypes.windll.kernel32.ReadProcessMemory(
                self.process_handle,
                ctypes.c_void_p(address),
                buffer,
                size,
                ctypes.byref(bytes_read)
            ):
                if bytes_read.value == size:
                    return buffer.raw
        except Exception:
            pass
        
        return None
    
    def read_int(self, address: int) -> Optional[int]:
        """Read 4-byte integer from memory"""
        data = self._read_memory(address, 4)
        if data:
            return struct.unpack('<I', data)[0]
        return None
    
    def read_float(self, address: int) -> Optional[float]:
        """Read 4-byte float from memory"""
        data = self._read_memory(address, 4)
        if data:
            return struct.unpack('<f', data)[0]
        return None
    
    def read_string(self, address: int, max_length: int = 256) -> Optional[str]:
        """Read null-terminated string from memory"""
        data = self._read_memory(address, max_length)
        if data:
            try:
                null_pos = data.find(b'\x00')
                if null_pos != -1:
                    data = data[:null_pos]
                return data.decode('utf-8')
            except UnicodeDecodeError:
                pass
        return None
    
    def scan_player_health(self) -> Dict[int, int]:
        """Scan for player health values"""
        health_values = {}
        
        # Common health patterns
        health_patterns = [
            b'\x64\x00\x00\x00',  # 100 health
            b'\x32\x00\x00\x00',  # 50 health
            b'\xC8\x00\x00\x00',  # 200 health
        ]
        
        for pattern in health_patterns:
            matches = self.scan_pattern(pattern)
            for address in matches:
                # Validate if this is actually health
                health = self.read_int(address)
                if health and 1 <= health <= 200:
                    health_values[address] = health
        
        print(f"❤️ Found {len(health_values)} potential health values")
        return health_values
    
    def scan_player_positions(self) -> Dict[int, Tuple[float, float, float]]:
        """Scan for player position vectors"""
        positions = {}
        
        # Scan for reasonable XYZ coordinates
        for region in self.memory_regions:
            try:
                data = self._read_memory(region['base'], region['size'])
                if not data:
                    continue
                
                # Look for float triples that could be positions
                for i in range(len(data) - 12):
                    try:
                        x = struct.unpack('<f', data[i:i+4])[0]
                        y = struct.unpack('<f', data[i+4:i+8])[0]
                        z = struct.unpack('<f', data[i+8:i+12])[0]
                        
                        # Check if coordinates are reasonable for game world
                        if (-10000 <= x <= 10000 and 
                            -10000 <= y <= 10000 and 
                            -1000 <= z <= 1000):
                            
                            address = region['base'] + i
                            positions[address] = (x, y, z)
                            
                            # Limit results
                            if len(positions) >= 50:
                                break
                    except:
                        continue
                
                if len(positions) >= 50:
                    break
                    
            except:
                continue
        
        print(f"📍 Found {len(positions)} potential position vectors")
        return positions
    
    def cleanup(self):
        """Clean up resources"""
        if self.process_handle:
            ctypes.windll.kernel32.CloseHandle(self.process_handle)
            self.process_handle = None
            print("✅ Memory scanner cleaned up")

# BloodStrike specific patterns
BLOODSTRIKE_PATTERNS = {
    'player_health': b'\x64\x00\x00\x00',
    'player_position': None,  # Will be scanned dynamically
    'weapon_id': b'\x01\x00\x00\x00',
    'team_id': b'\x00\x00\x00\x00',
}

def main():
    """Test memory scanner"""
    print("🔥 PHANTOM STRIKE - Windows Memory Scanner")
    print("=" * 50)
    
    scanner = PhantomMemoryScanner()
    
    # Attach to BloodStrike
    if scanner.attach_to_process("BloodStrike.exe"):
        try:
            # Scan for player health
            health_values = scanner.scan_player_health()
            print(f"\n❤️ Health values found: {len(health_values)}")
            
            # Scan for positions
            positions = scanner.scan_player_positions()
            print(f"📍 Position vectors found: {len(positions)}")
            
            # Test pattern scanning
            pattern_matches = scanner.scan_pattern(b'\x90\x90\x90\x90')
            print(f"🎯 NOP sleds found: {len(pattern_matches)}")
            
        finally:
            scanner.cleanup()
    else:
        print("❌ Failed to attach - make sure BloodStrike is running")

if __name__ == "__main__":
    main()

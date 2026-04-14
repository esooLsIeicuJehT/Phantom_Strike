"""
Memory operations for BloodStrike Python Cheat
Provides memory reading/writing utilities for Linux using /proc and ptrace.
"""

import os
import struct
import ctypes
import ctypes.util
from typing import Optional, List, Tuple, Any
from pathlib import Path


# Load libc for ptrace
libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

# ptrace constants
PTRACE_PEEKDATA = 3
PTRACE_POKEDATA = 5
PTRACE_ATTACH = 16
PTRACE_DETACH = 17
PTRACE_CONT = 7


class ProcessInfo:
    """Information about a process"""
    
    def __init__(self, pid: int):
        self.pid = pid
        self.name = ""
        self.path = ""
        self.base_address = 0
        self.module_size = 0
        self.maps: List[Tuple[int, int, str]] = []
        
        self._load_info()
        
    def _load_info(self):
        """Load process information from /proc"""
        proc_path = Path(f"/proc/{self.pid}")
        
        if not proc_path.exists():
            raise ValueError(f"Process {self.pid} not found")
            
        # Get process name
        try:
            with open(proc_path / "comm", "r") as f:
                self.name = f.read().strip()

            # For Proton/Wine, comm might be truncated or generic (e.g., "wine64-preloade")
            # Check cmdline for a better name
            with open(proc_path / "cmdline", "r") as f:
                cmdline = f.read().replace('\0', ' ').strip()
                if cmdline:
                    self.cmdline = cmdline
                    # If comm is generic or we find the target name in cmdline, use cmdline for identification
                    # But keep self.name as the primary short name
        except:
            self.cmdline = ""
            
        # Get executable path
        try:
            self.path = os.readlink(proc_path / "exe")
        except:
            pass
            
        # Parse memory maps
        self._parse_maps()
        
    def _parse_maps(self):
        """Parse /proc/pid/maps for memory regions"""
        maps_path = Path(f"/proc/{self.pid}/maps")
        
        if not maps_path.exists():
            return
            
        with open(maps_path, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) >= 5:
                    addr_range = parts[0]
                    perms = parts[1]
                    path = parts[-1] if len(parts) >= 6 else ""
                    
                    start, end = addr_range.split("-")
                    start = int(start, 16)
                    end = int(end, 16)
                    
                    self.maps.append((start, end, path))
                    
                    # Find base address (first executable region of main module)
                    if 'x' in perms and self.base_address == 0:
                        # Check if path contains process name or if it's a known game module
                        # For Proton, we often see the full Windows path in the mapping
                        name_match = self.name.lower() in path.lower()
                        cmdline_match = any(arg.lower() in path.lower() for arg in self.cmdline.split()) if hasattr(self, 'cmdline') else False

                        if name_match or cmdline_match or 'bloodstrike' in path.lower():
                            self.base_address = start
                            self.module_size = end - start
                            
    def find_module(self, name: str) -> Optional[Tuple[int, int]]:
        """Find a module's base address and size"""
        for start, end, path in self.maps:
            if name.lower() in path.lower():
                return (start, end - start)
        return None
        
    def get_all_regions(self) -> List[Tuple[int, int, str]]:
        """Get all memory regions"""
        return self.maps.copy()


class MemoryReader:
    """
    Memory reader class using /proc/mem for reading.
    Provides methods for reading various data types.
    """
    
    def __init__(self, pid: int):
        self.pid = pid
        self.process_info = ProcessInfo(pid)
        self._mem_file = None
        self._attached = False
        
    def open(self) -> bool:
        """Open the process memory file"""
        try:
            self._mem_file = open(f"/proc/{self.pid}/mem", "rb")
            return True
        except PermissionError:
            print("Permission denied. Try running as root.")
            return False
        except Exception as e:
            print(f"Error opening memory: {e}")
            return False
            
    def close(self):
        """Close the memory file"""
        if self._mem_file:
            self._mem_file.close()
            self._mem_file = None
            
    def attach(self) -> bool:
        """Attach to process using ptrace"""
        result = libc.ptrace(PTRACE_ATTACH, self.pid, 0, 0)
        if result == -1:
            errno = ctypes.get_errno()
            if errno != 0:
                print(f"ptrace attach failed: errno {errno}")
                return False
        self._attached = True
        return True
        
    def detach(self):
        """Detach from process"""
        if self._attached:
            libc.ptrace(PTRACE_DETACH, self.pid, 0, 0)
            self._attached = False
            
    def read_bytes(self, address: int, size: int) -> bytes:
        """Read raw bytes from memory"""
        if not self._mem_file:
            raise RuntimeError("Memory file not open")
            
        self._mem_file.seek(address)
        return self._mem_file.read(size)
        
    def read_int(self, address: int, signed: bool = True) -> int:
        """Read 4-byte integer"""
        data = self.read_bytes(address, 4)
        if signed:
            return struct.unpack('<i', data)[0]
        return struct.unpack('<I', data)[0]
        
    def read_long(self, address: int, signed: bool = True) -> int:
        """Read 8-byte integer"""
        data = self.read_bytes(address, 8)
        if signed:
            return struct.unpack('<q', data)[0]
        return struct.unpack('<Q', data)[0]
        
    def read_short(self, address: int, signed: bool = True) -> int:
        """Read 2-byte integer"""
        data = self.read_bytes(address, 2)
        if signed:
            return struct.unpack('<h', data)[0]
        return struct.unpack('<H', data)[0]
        
    def read_byte(self, address: int) -> int:
        """Read single byte"""
        data = self.read_bytes(address, 1)
        return struct.unpack('<B', data)[0]
        
    def read_float(self, address: int) -> float:
        """Read 4-byte float"""
        data = self.read_bytes(address, 4)
        return struct.unpack('<f', data)[0]
        
    def read_double(self, address: int) -> float:
        """Read 8-byte double"""
        data = self.read_bytes(address, 8)
        return struct.unpack('<d', data)[0]
        
    def read_string(self, address: int, max_length: int = 256) -> str:
        """Read null-terminated string"""
        data = self.read_bytes(address, max_length)
        null_pos = data.find(b'\x00')
        if null_pos >= 0:
            data = data[:null_pos]
        return data.decode('utf-8', errors='ignore')
        
    def read_vector3(self, address: int) -> Tuple[float, float, float]:
        """Read 3D vector (3 floats)"""
        x = self.read_float(address)
        y = self.read_float(address + 4)
        z = self.read_float(address + 8)
        return (x, y, z)
        
    def read_pointer(self, address: int) -> int:
        """Read pointer (8 bytes on 64-bit)"""
        return self.read_long(address, signed=False)
        
    def read_matrix(self, address: int, rows: int = 4, cols: int = 4) -> List[List[float]]:
        """Read a matrix (default 4x4)"""
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(self.read_float(address + (i * cols + j) * 4))
            matrix.append(row)
        return matrix
        
    def scan_pattern(self, pattern: bytes, mask: bytes = None, 
                     start: int = 0, end: int = 0) -> List[int]:
        """
        Scan memory for a pattern.
        pattern: bytes to search for (e.g., b'\x48\x89\x00\x00\x48')
        mask: 'x' for match, '?' for wildcard (e.g., b'xx??x')
        """
        results = []
        
        if start == 0:
            start = self.process_info.base_address
        if end == 0:
            end = start + self.process_info.module_size
            
        chunk_size = 0x10000
        current = start
        
        while current < end:
            try:
                chunk = self.read_bytes(current, min(chunk_size, end - current))
                
                for i in range(len(chunk) - len(pattern) + 1):
                    match = True
                    for j in range(len(pattern)):
                        if mask and mask[j] == ord('?'):
                            continue
                        if chunk[i + j] != pattern[j]:
                            match = False
                            break
                    if match:
                        results.append(current + i)
                        
                current += chunk_size
            except:
                current += chunk_size
                
        return results
    
    @staticmethod
    def find_process_by_name(name: str) -> Optional[int]:
        """Find process ID by name, improved for Proton/Wine"""
        name_lower = name.lower()
        for pid_dir in Path("/proc").iterdir():
            if not pid_dir.name.isdigit():
                continue
                
            try:
                # Check comm first (fast)
                with open(pid_dir / "comm", "r") as f:
                    proc_name = f.read().strip().lower()

                if name_lower in proc_name:
                    return int(pid_dir.name)

                # Check cmdline (better for Proton/Wine)
                with open(pid_dir / "cmdline", "r") as f:
                    cmdline = f.read().replace('\0', ' ').lower()
                    
                if name_lower in cmdline:
                    return int(pid_dir.name)
            except:
                pass
                
        return None


class MemoryWriter:
    """
    Memory writer class using ptrace for writing.
    Requires attaching to the process first.
    """
    
    def __init__(self, pid: int):
        self.pid = pid
        self._attached = False
        
    def attach(self) -> bool:
        """Attach to process using ptrace"""
        result = libc.ptrace(PTRACE_ATTACH, self.pid, 0, 0)
        if result == -1:
            errno = ctypes.get_errno()
            if errno != 0:
                print(f"ptrace attach failed: errno {errno}")
                return False
        self._attached = True
        return True
        
    def detach(self):
        """Detach from process"""
        if self._attached:
            libc.ptrace(PTRACE_DETACH, self.pid, 0, 0)
            self._attached = False
            
    def write_bytes(self, address: int, data: bytes) -> bool:
        """Write bytes to memory using ptrace (8 bytes at a time)"""
        if not self._attached:
            if not self.attach():
                return False
                
        # Align to word boundary
        aligned_addr = address & ~0x7
        offset = address - aligned_addr
        
        # Read original data
        original = libc.ptrace(PTRACE_PEEKDATA, self.pid, aligned_addr, 0)
        if original == -1:
            return False
            
        # Modify data
        original_bytes = bytearray(struct.pack('<Q', original))
        for i, b in enumerate(data):
            if offset + i < 8:
                original_bytes[offset + i] = b
            else:
                break
                
        # Write back if we have more than 8 bytes, continue with next word
        new_data = struct.unpack('<Q', bytes(original_bytes))[0]
        result = libc.ptrace(PTRACE_POKEDATA, self.pid, aligned_addr, new_data)
        
        if result == -1:
            return False
            
        # Handle remaining bytes
        if len(data) > 8 - offset:
            return self.write_bytes(address + (8 - offset), data[8 - offset:])
            
        return True
        
    def write_int(self, address: int, value: int) -> bool:
        """Write 4-byte integer"""
        return self.write_bytes(address, struct.pack('<i', value))
        
    def write_long(self, address: int, value: int) -> bool:
        """Write 8-byte integer"""
        return self.write_bytes(address, struct.pack('<q', value))
        
    def write_float(self, address: int, value: float) -> bool:
        """Write 4-byte float"""
        return self.write_bytes(address, struct.pack('<f', value))
        
    def write_byte(self, address: int, value: int) -> bool:
        """Write single byte"""
        return self.write_bytes(address, struct.pack('<B', value))
        
    def write_vector3(self, address: int, x: float, y: float, z: float) -> bool:
        """Write 3D vector"""
        data = struct.pack('<fff', x, y, z)
        return self.write_bytes(address, data)
        
    def nop_memory(self, address: int, size: int) -> bool:
        """NOP out memory region"""
        return self.write_bytes(address, b'\x90' * size)
        
    def hook_function(self, address: int, hook_address: int) -> bool:
        """Install a hook (x86_64 JMP instruction)"""
        # mov rax, hook_address
        # jmp rax
        hook_bytes = b'\x48\xB8' + struct.pack('<Q', hook_address) + b'\xFF\xE0'
        return self.write_bytes(address, hook_bytes)


def find_bloodstrike_pid() -> Optional[int]:
    """Find BloodStrike process ID"""
    return MemoryReader.find_process_by_name("bloodstrike")


def check_ptrace_scope() -> bool:
    """Check if ptrace_scope allows attaching"""
    try:
        with open("/proc/sys/kernel/yama/ptrace_scope", "r") as f:
            scope = int(f.read().strip())
            
        if scope == 0:
            return True
        elif scope == 1:
            # Need to be parent or have CAP_SYS_PTRACE
            return False
        else:
            # More restrictive
            return False
    except:
        return True  # File doesn't exist, assume unrestricted
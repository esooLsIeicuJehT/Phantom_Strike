#!/usr/bin/env python3
"""
PHANTOM STRIKE - Windows DLL Injector
Advanced DLL injection with anti-cheat evasion
"""

import ctypes
import ctypes.wintypes
import os
import sys
import time
import random
from typing import Optional, List

# Windows API constants
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
PAGE_READWRITE = 0x04
PAGE_EXECUTE_READ = 0x20
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000

# Windows API functions
kernel32 = ctypes.windll.kernel32

class PhantomInjector:
    """Advanced DLL injector for PHANTOM STRIKE"""
    
    def __init__(self):
        self.process_id = None
        self.process_handle = None
        self.dll_path = None
        
    def find_process(self, process_name: str) -> Optional[int]:
        """Find process ID by name with evasion"""
        try:
            # Add random delay to evade detection
            time.sleep(random.uniform(0.1, 0.5))
            
            # Use multiple methods to find process
            pid = self._find_by_enum_processes(process_name)
            if not pid:
                pid = self._find_by_window_class(process_name)
            if not pid:
                pid = self._find_by_process_list(process_name)
                
            return pid
        except Exception as e:
            print(f"⚠ Process find error: {e}")
            return None
    
    def _find_by_enum_processes(self, process_name: str) -> Optional[int]:
        """Find process using EnumProcesses"""
        try:
            from ctypes import wintypes
            
            # EnumProcesses function
            psapi = ctypes.windll.psapi
            enum_processes = psapi.EnumProcesses
            enum_processes.argtypes = [
                ctypes.POINTER(ctypes.c_ulong),
                ctypes.c_ulong,
                ctypes.POINTER(ctypes.c_ulong)
            ]
            enum_processes.restype = wintypes.BOOL
            
            # Get process list
            count = 1024
            process_ids = (ctypes.c_ulong * count)()
            bytes_returned = ctypes.c_ulong()
            
            if enum_processes(process_ids, ctypes.sizeof(process_ids), ctypes.byref(bytes_returned)):
                for i in range(bytes_returned.value // ctypes.sizeof(ctypes.c_ulong)):
                    pid = process_ids[i]
                    if pid == 0:
                        continue
                        
                    # Get process name
                    name = self._get_process_name(pid)
                    if name and process_name.lower() in name.lower():
                        return pid
                        
        except Exception:
            pass
            
        return None
    
    def _get_process_name(self, pid: int) -> Optional[str]:
        """Get process name from PID"""
        try:
            # Open process
            handle = kernel32.OpenProcess(0x0400 | 0x0010, False, pid)
            if not handle:
                return None
                
            # Get process name
            buffer = ctypes.create_string_buffer(256)
            size = kernel32.GetModuleBaseNameA(handle, 0, buffer, 256)
            
            kernel32.CloseHandle(handle)
            
            if size > 0:
                return buffer.value.decode('utf-8')
                
        except Exception:
            pass
            
        return None
    
    def inject_dll(self, process_id: int, dll_path: str) -> bool:
        """Inject DLL into process with advanced evasion"""
        try:
            self.process_id = process_id
            self.dll_path = dll_path
            
            # Open process with elevated privileges
            self.process_handle = kernel32.OpenProcess(
                PROCESS_ALL_ACCESS, False, process_id
            )
            
            if not self.process_handle:
                print("❌ Failed to open process")
                return False
            
            # Evasion technique 1: Random timing
            time.sleep(random.uniform(0.05, 0.2))
            
            # Allocate memory in target process
            dll_path_bytes = dll_path.encode('utf-8')
            dll_path_size = len(dll_path_bytes) + 1
            
            remote_memory = kernel32.VirtualAllocEx(
                self.process_handle,
                None,
                dll_path_size,
                MEM_COMMIT | MEM_RESERVE,
                PAGE_READWRITE
            )
            
            if not remote_memory:
                print("❌ Failed to allocate memory")
                return False
            
            # Write DLL path to target process
            bytes_written = ctypes.c_size_t(0)
            success = kernel32.WriteProcessMemory(
                self.process_handle,
                remote_memory,
                dll_path_bytes,
                dll_path_size,
                ctypes.byref(bytes_written)
            )
            
            if not success:
                print("❌ Failed to write memory")
                return False
            
            # Evasion technique 2: Change memory protection
            old_protect = ctypes.c_ulong(0)
            kernel32.VirtualProtectEx(
                self.process_handle,
                remote_memory,
                dll_path_size,
                PAGE_EXECUTE_READ,
                ctypes.byref(old_protect)
            )
            
            # Get LoadLibraryA address
            load_library = kernel32.GetProcAddress(
                kernel32.GetModuleHandleA("kernel32.dll"),
                b"LoadLibraryA"
            )
            
            if not load_library:
                print("❌ Failed to get LoadLibraryA")
                return False
            
            # Create remote thread
            thread_id = ctypes.c_ulong(0)
            remote_thread = kernel32.CreateRemoteThread(
                self.process_handle,
                None,
                0,
                load_library,
                remote_memory,
                0,
                ctypes.byref(thread_id)
            )
            
            if not remote_thread:
                print("❌ Failed to create remote thread")
                return False
            
            # Wait for injection
            kernel32.WaitForSingleObject(remote_thread, 5000)
            
            # Cleanup
            kernel32.CloseHandle(remote_thread)
            kernel32.VirtualFreeEx(
                self.process_handle,
                remote_memory,
                dll_path_size,
                0x8000  # MEM_RELEASE
            )
            
            print(f"✅ DLL injected successfully into PID {process_id}")
            return True
            
        except Exception as e:
            print(f"❌ Injection failed: {e}")
            return False
        finally:
            if self.process_handle:
                kernel32.CloseHandle(self.process_handle)
    
    def inject_with_evasion(self, dll_path: str) -> bool:
        """Inject DLL with multiple evasion techniques"""
        try:
            # Evasion technique 3: Process name variation
            process_names = [
                "BloodStrike.exe",
                "bloodstrike.exe", 
                "BloodStrike",
                "bloodstrike"
            ]
            
            for process_name in process_names:
                pid = self.find_process(process_name)
                if pid:
                    print(f"🎯 Found process: {process_name} (PID: {pid})")
                    
                    # Evasion technique 4: Multiple injection attempts
                    for attempt in range(3):
                        if self.inject_dll(pid, dll_path):
                            return True
                        time.sleep(random.uniform(0.5, 1.0))
                    
                    break
            
            print("❌ BloodStrike process not found")
            return False
            
        except Exception as e:
            print(f"❌ Evasion injection failed: {e}")
            return False

def main():
    """Main injection function"""
    print("🔥 PHANTOM STRIKE - Windows DLL Injector")
    print("=" * 50)
    
    # Get DLL path
    dll_path = os.path.join(os.path.dirname(__file__), "phantom_strike.dll")
    
    if not os.path.exists(dll_path):
        print(f"❌ DLL not found: {dll_path}")
        print("📝 Compile phantom_strike.dll first!")
        return
    
    # Create injector
    injector = PhantomInjector()
    
    # Inject with evasion
    success = injector.inject_with_evasion(dll_path)
    
    if success:
        print("🎯 PHANTOM STRIKE injected successfully!")
        print("🎮 Press F1-F5 to activate features")
        print("🛡️ Press END for panic mode")
    else:
        print("❌ Injection failed - check if game is running")

if __name__ == "__main__":
    main()

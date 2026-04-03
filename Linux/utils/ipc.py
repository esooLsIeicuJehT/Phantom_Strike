"""
IPC (Inter-Process Communication) utilities for BloodStrike Python Cheat
Provides communication between the game-embedded Python and external overlay.
"""

import os
import json
import socket
import struct
import threading
from typing import Optional, Callable, Dict, Any
from dataclasses import dataclass
from pathlib import Path


@dataclass
class IPCMessage:
    """IPC message structure"""
    type: str  # 'esp_data', 'aim_target', 'config', 'command'
    data: Dict[str, Any]
    
    def to_json(self) -> str:
        return json.dumps({'type': self.type, 'data': self.data})
    
    @classmethod
    def from_json(cls, json_str: str) -> 'IPCMessage':
        parsed = json.loads(json_str)
        return cls(type=parsed['type'], data=parsed['data'])


class IPCServer:
    """
    UDP server that receives ESP data from the game.
    Used by the external overlay to get player positions.
    """
    
    def __init__(self, host: str = "127.0.0.1", port: int = 6969):
        self.host = host
        self.port = port
        self.running = False
        self._socket: Optional[socket.socket] = None
        self._thread: Optional[threading.Thread] = None
        self._callbacks: Dict[str, Callable] = {}
        
    def start(self):
        """Start the IPC server"""
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.settimeout(1.0)
        self.running = True
        
        self._thread = threading.Thread(target=self._listen_loop, daemon=True)
        self._thread.start()
        
        print(f"IPC Server started on {self.host}:{self.port}")
        
    def stop(self):
        """Stop the IPC server"""
        self.running = False
        if self._socket:
            self._socket.close()
        if self._thread:
            self._thread.join(timeout=2)
            
    def register_callback(self, message_type: str, callback: Callable):
        """Register a callback for a specific message type"""
        self._callbacks[message_type] = callback
        
    def _listen_loop(self):
        """Main listen loop"""
        while self.running:
            try:
                data, addr = self._socket.recvfrom(65536)
                message_str = data.decode('utf-8')
                message = IPCMessage.from_json(message_str)
                
                if message.type in self._callbacks:
                    self._callbacks[message.type](message.data)
                elif '*' in self._callbacks:
                    self._callbacks['*'](message)
                    
            except socket.timeout:
                continue
            except Exception as e:
                if self.running:
                    print(f"IPC Server error: {e}")
                    
    def send_response(self, addr: tuple, response: Dict):
        """Send a response back to the client"""
        if self._socket:
            data = json.dumps(response).encode('utf-8')
            self._socket.sendto(data, addr)


class IPCClient:
    """
    UDP client that sends ESP data to external overlay.
    Used by the game-embedded Python to communicate with the overlay.
    """
    
    def __init__(self, host: str = "127.0.0.1", port: int = 6969):
        self.host = host
        self.port = port
        self._socket: Optional[socket.socket] = None
        
    def connect(self):
        """Create the UDP socket"""
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def disconnect(self):
        """Close the socket"""
        if self._socket:
            self._socket.close()
            self._socket = None
            
    def send(self, message: IPCMessage):
        """Send a message to the server"""
        if not self._socket:
            self.connect()
            
        data = message.to_json().encode('utf-8')
        self._socket.sendto(data, (self.host, self.port))
        
    def send_esp_data(self, players: list):
        """Send ESP data for all players"""
        self.send(IPCMessage(
            type='esp_data',
            data={'players': players}
        ))
        
    def send_aim_target(self, target_id: int, bone_pos: dict):
        """Send aim target information"""
        self.send(IPCMessage(
            type='aim_target',
            data={'target_id': target_id, 'bone_pos': bone_pos}
        ))
        
    def send_config(self, config: dict):
        """Send configuration update"""
        self.send(IPCMessage(
            type='config',
            data=config
        ))


class FileIPC:
    """
    File-based IPC for systems where UDP is not available.
    Writes ESP data to a file that the overlay reads.
    """
    
    def __init__(self, file_path: str = "/tmp/bloodstrike_esp.json"):
        self.file_path = Path(file_path)
        self._lock = threading.Lock()
        
    def write_data(self, data: Dict):
        """Write data to the IPC file"""
        with self._lock:
            try:
                with open(self.file_path, 'w') as f:
                    json.dump(data, f)
            except Exception as e:
                print(f"FileIPC write error: {e}")
                
    def read_data(self) -> Optional[Dict]:
        """Read data from the IPC file"""
        with self._lock:
            try:
                if self.file_path.exists():
                    with open(self.file_path, 'r') as f:
                        return json.load(f)
            except Exception as e:
                print(f"FileIPC read error: {e}")
        return None
        
    def clear(self):
        """Clear the IPC file"""
        with self._lock:
            if self.file_path.exists():
                self.file_path.unlink()


class SharedMemoryIPC:
    """
    Shared memory IPC for high-performance communication.
    Uses /dev/shm for fast data sharing.
    """
    
    def __init__(self, name: str = "bloodstrike_ipc", size: int = 65536):
        self.name = name
        self.size = size
        self.shm_path = Path(f"/dev/shm/{name}")
        self._fd = None
        self._mapped = None
        
    def create(self):
        """Create shared memory region"""
        try:
            import mmap
            
            self._fd = os.open(str(self.shm_path), os.O_CREAT | os.O_RDWR, 0o666)
            os.ftruncate(self._fd, self.size)
            self._mapped = mmap.mmap(self._fd, self.size)
            
        except Exception as e:
            print(f"SharedMemory create error: {e}")
            
    def write(self, data: bytes):
        """Write data to shared memory"""
        if self._mapped:
            # Write length prefix (4 bytes)
            length = len(data)
            self._mapped.seek(0)
            self._mapped.write(struct.pack('<I', length))
            self._mapped.write(data)
            
    def read(self) -> Optional[bytes]:
        """Read data from shared memory"""
        if self._mapped:
            self._mapped.seek(0)
            length_data = self._mapped.read(4)
            if len(length_data) == 4:
                length = struct.unpack('<I', length_data)[0]
                if length > 0 and length < self.size:
                    return self._mapped.read(length)
        return None
        
    def close(self):
        """Close and cleanup shared memory"""
        if self._mapped:
            self._mapped.close()
        if self._fd:
            os.close(self._fd)
        if self.shm_path.exists():
            self.shm_path.unlink()


class CommandInterface:
    """
    Command interface for external control.
    Allows sending commands to the cheat via file or socket.
    """
    
    def __init__(self, command_file: str = "/tmp/bloodstrike_cmd"):
        self.command_file = Path(command_file)
        self.running = False
        self._thread = None
        self._commands: Dict[str, Callable] = {}
        
    def register_command(self, name: str, handler: Callable):
        """Register a command handler"""
        self._commands[name] = handler
        
    def start(self):
        """Start listening for commands"""
        self.running = True
        self._thread = threading.Thread(target=self._watch_loop, daemon=True)
        self._thread.start()
        
    def stop(self):
        """Stop listening for commands"""
        self.running = False
        if self._thread:
            self._thread.join(timeout=1)
            
    def _watch_loop(self):
        """Watch for command file changes"""
        last_mtime = 0
        
        while self.running:
            try:
                if self.command_file.exists():
                    mtime = self.command_file.stat().st_mtime
                    if mtime > last_mtime:
                        last_mtime = mtime
                        self._process_commands()
            except Exception as e:
                pass
                
            import time
            time.sleep(0.1)
            
    def _process_commands(self):
        """Process commands from file"""
        try:
            with open(self.command_file, 'r') as f:
                content = f.read().strip()
                
            if content:
                commands = json.loads(content)
                for cmd in commands:
                    self._execute_command(cmd)
                    
            # Clear file after processing
            with open(self.command_file, 'w') as f:
                f.write('')
                
        except Exception as e:
            print(f"Command processing error: {e}")
            
    def _execute_command(self, cmd: Dict):
        """Execute a single command"""
        name = cmd.get('name')
        args = cmd.get('args', {})
        
        if name in self._commands:
            try:
                self._commands[name](**args)
            except Exception as e:
                print(f"Command execution error: {e}")
        else:
            print(f"Unknown command: {name}")
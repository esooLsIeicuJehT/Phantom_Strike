"""
ESP Overlay Window for BloodStrike Python Cheat
Transparent overlay that renders ESP on top of the game window.
Supports both X11 and Wayland on Fedora Linux.
"""

import sys
import time
import threading
from typing import Optional, Tuple, List
from dataclasses import dataclass

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
    from PyQt5.QtCore import Qt, QTimer, QPoint, QRect
    from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QBrush, QRegion
    PYQT_AVAILABLE = True
except ImportError:
    PYQT_AVAILABLE = False
    print("PyQt5 not installed. Install with: pip install PyQt5")

from ..features.esp import ESP, PlayerESPData
from ..core.sdk import BloodStrikeSDK


@dataclass
class OverlaySettings:
    """Settings for overlay rendering"""
    show_box: bool = True
    show_skeleton: bool = True
    show_health: bool = True
    show_name: bool = False
    show_distance: bool = True
    show_weapon: bool = False
    show_snaplines: bool = False
    
    # Colors (RGBA)
    enemy_color: Tuple[int, int, int, int] = (255, 0, 0, 255)
    team_color: Tuple[int, int, int, int] = (0, 255, 0, 255)
    visible_color: Tuple[int, int, int, int] = (255, 255, 0, 255)
    skeleton_color: Tuple[int, int, int, int] = (255, 255, 255, 255)
    
    # Box settings
    box_width: int = 2
    box_style: str = "full"  # full, corners, 2d, 3d
    
    # Font settings
    font_size: int = 10
    font_family: str = "Consolas"
    
    # Performance
    render_delay: float = 0.016  # ~60 FPS
    max_distance: float = 500.0  # Max ESP distance in meters


class OverlayWindow(QMainWindow if PYQT_AVAILABLE else object):
    """
    Transparent overlay window that renders ESP on top of the game.
    Uses window transparency and stays-on-top to overlay the game.
    """
    
    def __init__(self, esp: ESP, sdk: BloodStrikeSDK, settings: Optional[OverlaySettings] = None):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 is required for overlay rendering")
            
        super().__init__()
        
        self.esp = esp
        self.sdk = sdk
        self.settings = settings or OverlaySettings()
        
        # ESP data
        self.player_data: List[PlayerESPData] = []
        self.game_window_rect = QRect(0, 0, 1920, 1080)
        
        # Rendering state
        self.running = False
        self._overlay_thread = None
        
        # Setup window
        self._setup_window()
        
        # Update timer
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self._update_data)
        
    def _setup_window(self):
        """Setup the transparent overlay window"""
        # Window flags for overlay
        self.setWindowFlags(
            Qt.FramelessWindowHint |  # No border
            Qt.WindowStaysOnTopHint |  # Stay on top
            Qt.Tool |                  # No taskbar entry
            Qt.WindowTransparentForInput  # Click-through
        )
        
        # Enable transparency
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        
        # Set geometry to cover the game window
        self.setGeometry(0, 0, 1920, 1080)
        
        # Set window opacity
        self.setWindowOpacity(1.0)
        
        # Create central widget for painting
        self.central_widget = OverlayWidget(self)
        self.setCentralWidget(self.central_widget)
        
    def start(self):
        """Start the overlay rendering"""
        self.running = True
        self.show()
        self.update_timer.start(int(self.settings.render_delay * 1000))
        
    def stop(self):
        """Stop the overlay rendering"""
        self.running = False
        self.update_timer.stop()
        self.hide()
        
    def _update_data(self):
        """Update ESP data from the game"""
        if not self.running:
            return
            
        try:
            # Update game window position
            self._update_game_window()
            
            # Get ESP data
            self.player_data = self.esp.get_external_data()
            
            # Trigger repaint
            self.update()
            
        except Exception as e:
            print(f"Overlay update error: {e}")
            
    def _update_game_window(self):
        """Update the game window position and size"""
        try:
            # Try to find BloodStrike window
            import subprocess
            
            # Use xdotool to find window (X11)
            result = subprocess.run(
                ['xdotool', 'search', '--name', 'BloodStrike'],
                capture_output=True, text=True
            )
            
            if result.returncode == 0 and result.stdout.strip():
                window_id = result.stdout.strip().split('\n')[0]
                
                # Get window geometry
                geo_result = subprocess.run(
                    ['xdotool', 'getwindowgeometry', window_id],
                    capture_output=True, text=True
                )
                
                if geo_result.returncode == 0:
                    # Parse geometry: Position: 0,0 (screen: 0)
                    # Geometry: 1920x1080
                    lines = geo_result.stdout.strip().split('\n')
                    for line in lines:
                        if 'Position:' in line:
                            pos = line.split(':')[1].strip().split('(')[0]
                            x, y = map(int, pos.split(','))
                        elif 'Geometry:' in line:
                            size = line.split(':')[1].strip()
                            w, h = map(int, size.split('x'))
                            
                    self.game_window_rect = QRect(x, y, w, h)
                    self.setGeometry(self.game_window_rect)
                    
        except Exception as e:
            # Fallback to fullscreen
            pass
            
    def update_settings(self, settings: OverlaySettings):
        """Update overlay settings"""
        self.settings = settings
        self.update()


class OverlayWidget(QWidget if PYQT_AVAILABLE else object):
    """Widget that handles the actual ESP rendering"""
    
    def __init__(self, parent):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 is required")
            
        super().__init__(parent)
        self.overlay = parent
        
        # Setup font
        self.font = QFont(self.overlay.settings.font_family, self.overlay.settings.font_size)
        self.setFont(self.font)
        
    def paintEvent(self, event):
        """Paint the ESP overlay"""
        if not self.overlay.player_data:
            return
            
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(self.font)
        
        try:
            for player in self.overlay.player_data:
                if not player.is_valid:
                    continue
                    
                # Check distance
                if player.distance > self.overlay.settings.max_distance:
                    continue
                    
                self._draw_player(painter, player)
                
        except Exception as e:
            print(f"Paint error: {e}")
        finally:
            painter.end()
            
    def _draw_player(self, painter: QPainter, player: PlayerESPData):
        """Draw ESP for a single player"""
        settings = self.overlay.settings
        
        # Determine color based on team/visibility
        if player.is_visible:
            color = QColor(*settings.visible_color)
        elif player.is_teammate:
            color = QColor(*settings.team_color)
        else:
            color = QColor(*settings.enemy_color)
            
        # Draw box
        if settings.show_box:
            self._draw_box(painter, player, color)
            
        # Draw skeleton
        if settings.show_skeleton:
            self._draw_skeleton(painter, player)
            
        # Draw health bar
        if settings.show_health:
            self._draw_health_bar(painter, player)
            
        # Draw name
        if settings.show_name and player.name:
            self._draw_text(painter, player, player.name, 'top')
            
        # Draw distance
        if settings.show_distance:
            self._draw_text(painter, player, f"{player.distance:.0f}m", 'bottom')
            
        # Draw weapon
        if settings.show_weapon and player.weapon:
            self._draw_text(painter, player, player.weapon, 'bottom2')
            
        # Draw snapline
        if settings.show_snaplines:
            self._draw_snapline(painter, player, color)
            
    def _draw_box(self, painter: QPainter, player: PlayerESPData, color: QColor):
        """Draw ESP box around player"""
        settings = self.overlay.settings
        
        x, y = player.screen_pos
        w, h = player.box_width, player.box_height
        
        pen = QPen(color)
        pen.setWidth(settings.box_width)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        
        if settings.box_style == "full":
            painter.drawRect(int(x - w/2), int(y - h/2), int(w), int(h))
            
        elif settings.box_style == "corners":
            corner_len = min(w, h) * 0.3
            
            # Top-left corner
            painter.drawLine(int(x - w/2), int(y - h/2), 
                           int(x - w/2 + corner_len), int(y - h/2))
            painter.drawLine(int(x - w/2), int(y - h/2), 
                           int(x - w/2), int(y - h/2 + corner_len))
            
            # Top-right corner
            painter.drawLine(int(x + w/2), int(y - h/2), 
                           int(x + w/2 - corner_len), int(y - h/2))
            painter.drawLine(int(x + w/2), int(y - h/2), 
                           int(x + w/2), int(y - h/2 + corner_len))
            
            # Bottom-left corner
            painter.drawLine(int(x - w/2), int(y + h/2), 
                           int(x - w/2 + corner_len), int(y + h/2))
            painter.drawLine(int(x - w/2), int(y + h/2), 
                           int(x - w/2), int(y + h/2 - corner_len))
            
            # Bottom-right corner
            painter.drawLine(int(x + w/2), int(y + h/2), 
                           int(x + w/2 - corner_len), int(y + h/2))
            painter.drawLine(int(x + w/2), int(y + h/2), 
                           int(x + w/2), int(y + h/2 - corner_len))
            
        elif settings.box_style == "2d":
            painter.drawRect(int(x - w/2), int(y - h/2), int(w), int(h))
            
        elif settings.box_style == "3d":
            # 3D box rendering
            depth = w * 0.3
            self._draw_3d_box(painter, x, y, w, h, depth)
            
    def _draw_3d_box(self, painter: QPainter, x: float, y: float, 
                     w: float, h: float, depth: float):
        """Draw 3D box"""
        # Front face
        painter.drawRect(int(x - w/2), int(y - h/2), int(w), int(h))
        
        # Back face offset
        bx = x - w/2 + depth
        by = y - h/2 - depth
        
        # Connecting lines
        painter.drawLine(int(x - w/2), int(y - h/2), int(bx), int(by))
        painter.drawLine(int(x + w/2), int(y - h/2), int(bx + w), int(by))
        painter.drawLine(int(x - w/2), int(y + h/2), int(bx), int(by + h))
        painter.drawLine(int(x + w/2), int(y + h/2), int(bx + w), int(by + h))
        
        # Back face
        painter.drawRect(int(bx), int(by), int(w), int(h))
        
    def _draw_skeleton(self, painter: QPainter, player: PlayerESPData):
        """Draw player skeleton"""
        if not player.bones:
            return
            
        pen = QPen(QColor(*self.overlay.settings.skeleton_color))
        pen.setWidth(1)
        painter.setPen(pen)
        
        # Draw bone connections
        bone_connections = [
            ('head', 'neck'),
            ('neck', 'spine'),
            ('spine', 'pelvis'),
            ('neck', 'left_shoulder'),
            ('left_shoulder', 'left_elbow'),
            ('left_elbow', 'left_hand'),
            ('neck', 'right_shoulder'),
            ('right_shoulder', 'right_elbow'),
            ('right_elbow', 'right_hand'),
            ('pelvis', 'left_hip'),
            ('left_hip', 'left_knee'),
            ('left_knee', 'left_foot'),
            ('pelvis', 'right_hip'),
            ('right_hip', 'right_knee'),
            ('right_knee', 'right_foot'),
        ]
        
        for bone1, bone2 in bone_connections:
            if bone1 in player.bones and bone2 in player.bones:
                p1 = player.bones[bone1]
                p2 = player.bones[bone2]
                if p1 and p2:
                    painter.drawLine(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
                    
    def _draw_health_bar(self, painter: QPainter, player: PlayerESPData):
        """Draw health bar beside player"""
        x, y = player.screen_pos
        w, h = player.box_width, player.box_height
        
        bar_width = 4
        bar_height = h
        
        # Background
        painter.fillRect(int(x - w/2 - bar_width - 2), int(y - h/2), 
                        bar_width, bar_height, QColor(0, 0, 0, 150))
        
        # Health
        health_height = int(bar_height * (player.health / 100.0))
        health_color = QColor(
            int(255 * (1 - player.health / 100.0)),
            int(255 * (player.health / 100.0)),
            0
        )
        painter.fillRect(int(x - w/2 - bar_width - 2), 
                        int(y + h/2 - health_height),
                        bar_width, health_height, health_color)
        
    def _draw_text(self, painter: QPainter, player: PlayerESPData, 
                   text: str, position: str):
        """Draw text near player ESP"""
        x, y = player.screen_pos
        w, h = player.box_width, player.box_height
        
        if position == 'top':
            text_y = y - h/2 - 15
        elif position == 'bottom':
            text_y = y + h/2 + 5
        elif position == 'bottom2':
            text_y = y + h/2 + 18
        else:
            text_y = y
            
        painter.setPen(QColor(255, 255, 255, 255))
        painter.drawText(int(x - len(text) * 3), int(text_y), text)
        
    def _draw_snapline(self, painter: QPainter, player: PlayerESPData, color: QColor):
        """Draw snapline from screen bottom to player"""
        x, y = player.screen_pos
        
        screen_height = self.height()
        
        pen = QPen(color)
        pen.setWidth(1)
        painter.setPen(pen)
        
        painter.drawLine(int(x), int(screen_height), int(x), int(y))


class ExternalOverlay:
    """
    External overlay that communicates with the game via IPC.
    Used when running as a separate process from the game.
    """
    
    def __init__(self, host: str = "127.0.0.1", port: int = 6969):
        self.host = host
        self.port = port
        self.running = False
        self._socket = None
        
    def start(self):
        """Start receiving ESP data via UDP socket"""
        import socket
        
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind((self.host, self.port))
        self._socket.settimeout(1.0)
        self.running = True
        
        print(f"External overlay listening on {self.host}:{self.port}")
        
    def stop(self):
        """Stop the overlay"""
        self.running = False
        if self._socket:
            self._socket.close()
            
    def get_data(self) -> List[PlayerESPData]:
        """Get ESP data from the game"""
        if not self.running or not self._socket:
            return []
            
        try:
            data, _ = self._socket.recvfrom(65536)
            
            import json
            parsed = json.loads(data.decode())
            
            players = []
            for p in parsed.get('players', []):
                players.append(PlayerESPData(
                    entity_id=p.get('id', 0),
                    screen_pos=(p.get('x', 0), p.get('y', 0)),
                    box_width=p.get('w', 50),
                    box_height=p.get('h', 100),
                    health=p.get('health', 100),
                    is_teammate=p.get('team', False),
                    is_visible=p.get('visible', True),
                    distance=p.get('distance', 0),
                    name=p.get('name', ''),
                    weapon=p.get('weapon', ''),
                    bones=p.get('bones', {})
                ))
                
            return players
            
        except Exception as e:
            print(f"Error receiving ESP data: {e}")
            return []


def check_overlay_dependencies() -> bool:
    """Check if all dependencies for overlay are available"""
    dependencies = {
        'PyQt5': PYQT_AVAILABLE,
        'xdotool': False,
    }
    
    # Check for xdotool (X11 window management)
    try:
        import subprocess
        result = subprocess.run(['which', 'xdotool'], capture_output=True)
        dependencies['xdotool'] = result.returncode == 0
    except:
        pass
        
    missing = [k for k, v in dependencies.items() if not v]
    
    if missing:
        print(f"Missing dependencies: {', '.join(missing)}")
        print("\nInstall with:")
        if 'PyQt5' in missing:
            print("  pip install PyQt5")
        if 'xdotool' in missing:
            print("  sudo dnf install xdotool  # Fedora")
            print("  sudo apt install xdotool  # Ubuntu/Debian")
        return False
        
    return True
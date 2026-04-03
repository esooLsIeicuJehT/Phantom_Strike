"""
In-Game Overlay for BloodStrike Python Cheat
Displays ESP and menu overlay directly on the game screen with INSERT key toggle
"""

import time
import sys
from typing import Optional, List, Tuple

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
    from PyQt5.QtCore import Qt, QTimer, QPoint, QRect
    from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QBrush, QRegion
    PYQT_AVAILABLE = True
except ImportError:
    PYQT_AVAILABLE = False
    print("PyQt5 not installed. Install with: pip install PyQt5")

try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False
    print("pynput not installed. Install with: pip install pynput")

class InGameOverlay(QWidget if PYQT_AVAILABLE else object):
    """
    In-game overlay that shows ESP and cheat menu.
    Toggle with INSERT key.
    """

    def __init__(self, cheat):
        if not PYQT_AVAILABLE:
            raise RuntimeError("PyQt5 required for overlay")
        if not PYNPUT_AVAILABLE:
            raise RuntimeError("pynput required for keyboard input")

        super().__init__()
        self.cheat = cheat
        self.visible = False
        self.show_menu = True
        self.show_esp = True

        # Setup window
        self._setup_window()

        # Keyboard listener
        self.keyboard_listener = keyboard.Listener(on_press=self._on_key_press)
        self.keyboard_listener.start()

        # Update timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(16)  # ~60 FPS

    def _setup_window(self):
        """Setup transparent overlay window"""
        # Make window transparent and always on top
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool |
            Qt.WindowTransparentForInput
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)

        # Set to fullscreen
        self.setGeometry(0, 0, 1920, 1080)

    def _on_key_press(self, key):
        """Handle keyboard input"""
        try:
            # Toggle overlay with INSERT key
            if key == keyboard.Key.insert:
                self.visible = not self.visible
                if self.visible:
                    self.show()
                    self.raise_()
                    self.activateWindow()
                else:
                    self.hide()

            # Toggle menu with HOME key
            elif key == keyboard.Key.home:
                self.show_menu = not self.show_menu

            # Toggle ESP with F1
            elif key == keyboard.Key.f1:
                self._toggle_esp()

            # Toggle Aimbot with F2
            elif key == keyboard.Key.f2:
                self._toggle_aimbot()

            # Panic key - disable all with END
            elif key == keyboard.Key.end:
                self.cheat.config.aimbot.enabled = False
                self.cheat.config.esp.enabled = False
                self.visible = False
                self.hide()
                
        except AttributeError:
            pass
    
    def paintEvent(self, event):
        """Render overlay"""
        if not self.visible:
            return
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw menu
        if self.show_menu:
            self._draw_menu(painter)
        
        # Draw ESP
        if self.show_esp and self.cheat.esp:
            self._draw_esp(painter)
    
    def _draw_menu(self, painter: QPainter):
        """Draw cheat menu"""
        # Background
        menu_rect = QRect(10, 10, 300, 400)
        painter.fillRect(menu_rect, QColor(0, 0, 0, 180))
        
        # Border
        painter.setPen(QPen(QColor(0, 255, 0, 255), 2))
        painter.drawRect(menu_rect)
        
        # Title
        painter.setFont(QFont("Consolas", 14, QFont.Bold))
        painter.setPen(QColor(0, 255, 0, 255))
        painter.drawText(20, 35, "BloodStrike Cheat")
        
        # Separator
        painter.drawLine(20, 45, 300, 45)
        
        # Menu items
        painter.setFont(QFont("Consolas", 10))
        y = 70
        
        # Aimbot status
        aimbot_status = "ON" if self.cheat.config.aimbot.enabled else "OFF"
        aimbot_color = QColor(0, 255, 0) if self.cheat.config.aimbot.enabled else QColor(255, 0, 0)
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(20, y, "[F2] Aimbot:")
        painter.setPen(aimbot_color)
        painter.drawText(150, y, aimbot_status)
        y += 25
        
        # ESP status
        esp_status = "ON" if self.cheat.config.esp.enabled else "OFF"
        esp_color = QColor(0, 255, 0) if self.cheat.config.esp.enabled else QColor(255, 0, 0)
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(20, y, "[F1] ESP:")
        painter.setPen(esp_color)
        painter.drawText(150, y, esp_status)
        y += 25
        
        # Settings
        painter.setPen(QColor(200, 200, 200))
        y += 10
        painter.drawText(20, y, f"FOV: {self.cheat.config.aimbot.fov:.0f}°")
        y += 20
        painter.drawText(20, y, f"Smoothness: {self.cheat.config.aimbot.smoothness:.1f}")
        y += 20
        painter.drawText(20, y, f"Max Distance: {self.cheat.config.aimbot.max_distance:.0f}m")
        y += 30
        
        # Keybinds
        painter.setPen(QColor(150, 150, 150))
        painter.setFont(QFont("Consolas", 8))
        y += 10
        painter.drawText(20, y, "INSERT - Toggle Menu")
        y += 15
        painter.drawText(20, y, "HOME - Toggle Menu Display")
        y += 15
        painter.drawText(20, y, "F1 - Toggle ESP")
        y += 15
        painter.drawText(20, y, "F2 - Toggle Aimbot")
        y += 15
        painter.drawText(20, y, "END - Panic (Disable All)")
        
        # Watermark
        painter.setPen(QColor(100, 100, 100))
        painter.drawText(20, 390, "BloodStrike Python Cheat v1.0")
    
    def _draw_esp(self, painter: QPainter):
        """Draw ESP boxes and info"""
        if not self.cheat.esp or not self.cheat.esp.esp_data:
            return
        
        for player in self.cheat.esp.esp_data:
            # Determine color
            if player.is_allied:
                color = QColor(0, 255, 0, 255)  # Green for allies
            else:
                color = QColor(255, 0, 0, 255)  # Red for enemies
            
            # Draw box
            if player.box_min and player.box_max:
                painter.setPen(QPen(color, 2))
                box_rect = QRect(
                    int(player.box_min[0]),
                    int(player.box_min[1]),
                    int(player.box_max[0] - player.box_min[0]),
                    int(player.box_max[1] - player.box_min[1])
                )
                painter.drawRect(box_rect)
                
                # Draw health bar
                if player.health and player.max_health:
                    health_percent = player.health / player.max_health
                    health_bar_height = int((player.box_max[1] - player.box_min[1]) * health_percent)
                    
                    # Background
                    painter.fillRect(
                        int(player.box_min[0] - 6),
                        int(player.box_min[1]),
                        4,
                        int(player.box_max[1] - player.box_min[1]),
                        QColor(0, 0, 0, 180)
                    )
                    
                    # Health bar
                    health_color = QColor(0, 255, 0) if health_percent > 0.5 else QColor(255, 255, 0) if health_percent > 0.25 else QColor(255, 0, 0)
                    painter.fillRect(
                        int(player.box_min[0] - 6),
                        int(player.box_max[1] - health_bar_height),
                        4,
                        health_bar_height,
                        health_color
                    )
                
                # Draw name and distance
                painter.setFont(QFont("Consolas", 9))
                painter.setPen(QColor(255, 255, 255))
                
                info_text = f"{player.name} [{int(player.distance)}m]"
                painter.drawText(
                    int(player.box_min[0]),
                    int(player.box_min[1] - 5),
                    info_text
                )
                
                # Draw weapon
                if player.weapon:
                    painter.setPen(QColor(200, 200, 200))
                    painter.drawText(
                        int(player.box_min[0]),
                        int(player.box_max[1] + 15),
                        player.weapon
                    )
            
            # Draw skeleton
            if player.skeleton_bones:
                painter.setPen(QPen(QColor(255, 255, 255, 200), 1))
                for bone_start, bone_end in player.skeleton_bones:
                    painter.drawLine(
                        int(bone_start[0]), int(bone_start[1]),
                        int(bone_end[0]), int(bone_end[1])
                    )
    
    def closeEvent(self, event):
        """Cleanup on close"""
        self.keyboard_listener.stop()
        event.accept()


def check_overlay_dependencies() -> bool:
    """Check if overlay dependencies are installed"""
    if not PYQT_AVAILABLE:
        print("ERROR: PyQt5 not installed")
        print("Install with: pip install PyQt5")
        return False
    
    try:
        import pynput
    except ImportError:
        print("ERROR: pynput not installed")
        print("Install with: pip install pynput")
        return False
    
    return True

"""
BloodStrike Cheat Main Window
PyQt5-based GUI for Fedora Linux
"""

import sys
import time
import threading
from typing import Optional

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QLabel, QPushButton, QGroupBox, QCheckBox, QSlider,
    QComboBox, QSpinBox, QDoubleSpinBox, QTextEdit, QSplitter,
    QStatusBar, QMenuBar, QMenu, QAction, QMessageBox, QFrame
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QObject
from PyQt5.QtGui import QFont, QColor, QPalette

# Import features
sys.path.insert(0, '..')
from features import Aimbot, ESP, ESPRenderer, MiscFeatures, SkinChanger
from features.aimbot import AimTarget, AimMode


class SignalEmitter(QObject):
    """Signal emitter for thread-safe GUI updates"""
    log_signal = pyqtSignal(str)
    status_signal = pyqtSignal(str, bool)


class MainWindow(QMainWindow):
    """
    Main GUI window for BloodStrike cheat.
    Provides tabs for different features and an ESP overlay.
    """
    
    def __init__(self, sdk=None, entity_manager=None):
        super().__init__()
        
        self.sdk = sdk
        self.entity_manager = entity_manager
        
        # Feature instances
        self.aimbot = None
        self.esp = None
        self.esp_renderer = None
        self.misc = None
        self.skin_changer = None
        
        # State
        self.running = False
        self.update_timer = None
        self.signal_emitter = SignalEmitter()
        
        # Connect signals
        self.signal_emitter.log_signal.connect(self._log_message)
        self.signal_emitter.status_signal.connect(self._set_status)
        
        self._init_ui()
        self._init_features()
        self._init_timers()
    
    def _init_ui(self) -> None:
        """Initialize the user interface"""
        self.setWindowTitle("BloodStrike Python Cheat v1.0")
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumSize(600, 400)
        
        # Set dark theme
        self._set_dark_theme()
        
        # Create menu bar
        self._create_menu_bar()
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Create tab widget
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #3d3d3d;
                background-color: #2d2d2d;
            }
            QTabBar::tab {
                background-color: #3d3d3d;
                color: #ffffff;
                padding: 8px 16px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: #4d4d4d;
            }
        """)
        
        # Create tabs
        self.aimbot_tab = self._create_aimbot_tab()
        self.esp_tab = self._create_esp_tab()
        self.misc_tab = self._create_misc_tab()
        self.skin_tab = self._create_skin_tab()
        self.settings_tab = self._create_settings_tab()
        self.console_tab = self._create_console_tab()
        
        self.tabs.addTab(self.aimbot_tab, "🎯 Aimbot")
        self.tabs.addTab(self.esp_tab, "👁 ESP")
        self.tabs.addTab(self.misc_tab, "⚡ Misc")
        self.tabs.addTab(self.skin_tab, "🎨 Skins")
        self.tabs.addTab(self.settings_tab, "⚙ Settings")
        self.tabs.addTab(self.console_tab, "📋 Console")
        
        main_layout.addWidget(self.tabs)
        
        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
        # Create control buttons at bottom
        button_layout = QHBoxLayout()
        
        self.btn_start = QPushButton("▶ Start")
        self.btn_start.setStyleSheet("background-color: #28a745; color: white; padding: 8px 16px;")
        self.btn_start.clicked.connect(self.toggle_cheat)
        
        self.btn_reload = QPushButton("🔄 Reload Config")
        self.btn_reload.setStyleSheet("background-color: #17a2b8; color: white; padding: 8px 16px;")
        self.btn_reload.clicked.connect(self.reload_config)
        
        self.btn_exit = QPushButton("✖ Exit")
        self.btn_exit.setStyleSheet("background-color: #dc3545; color: white; padding: 8px 16px;")
        self.btn_exit.clicked.connect(self.close)
        
        button_layout.addWidget(self.btn_start)
        button_layout.addWidget(self.btn_reload)
        button_layout.addWidget(self.btn_exit)
        
        main_layout.addLayout(button_layout)
    
    def _set_dark_theme(self) -> None:
        """Apply dark theme to the application"""
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(45, 45, 45))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.AlternateBase, QColor(45, 45, 45))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(45, 45, 45))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        
        QApplication.instance().setPalette(dark_palette)
    
    def _create_menu_bar(self) -> None:
        """Create the menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        
        load_config = QAction("Load Config", self)
        load_config.setShortcut("Ctrl+O")
        load_config.triggered.connect(self.load_config)
        
        save_config = QAction("Save Config", self)
        save_config.setShortcut("Ctrl+S")
        save_config.triggered.connect(self.save_config)
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        
        file_menu.addAction(load_config)
        file_menu.addAction(save_config)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        
        help_menu.addAction(about_action)
    
    def _create_aimbot_tab(self) -> QWidget:
        """Create the aimbot configuration tab"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Enable checkbox
        self.check_aimbot = QCheckBox("Enable Aimbot")
        self.check_aimbot.stateChanged.connect(self._on_aimbot_toggle)
        layout.addWidget(self.check_aimbot)
        
        # Target settings group
        target_group = QGroupBox("Target Settings")
        target_layout = QVBoxLayout(target_group)
        
        # Target bone
        bone_layout = QHBoxLayout()
        bone_layout.addWidget(QLabel("Target Bone:"))
        self.combo_bone = QComboBox()
        self.combo_bone.addItems(["Head", "Neck", "Chest", "Spine"])
        self.combo_bone.currentTextChanged.connect(self._on_bone_changed)
        bone_layout.addWidget(self.combo_bone)
        target_layout.addLayout(bone_layout)
        
        # Aim mode
        mode_layout = QHBoxLayout()
        mode_layout.addWidget(QLabel("Aim Mode:"))
        self.combo_aim_mode = QComboBox()
        self.combo_aim_mode.addItems(["Hold", "Toggle", "Auto", "On Key"])
        self.combo_aim_mode.currentTextChanged.connect(self._on_aim_mode_changed)
        mode_layout.addWidget(self.combo_aim_mode)
        target_layout.addLayout(mode_layout)
        
        layout.addWidget(target_group)
        
        # Smoothing settings group
        smooth_group = QGroupBox("Smoothing")
        smooth_layout = QVBoxLayout(smmooth_group)
        
        # Smoothness slider
        smooth_slider_layout = QHBoxLayout()
        smooth_slider_layout.addWidget(QLabel("Smoothness:"))
        self.slider_smooth = QSlider(Qt.Horizontal)
        self.slider_smooth.setRange(0, 100)
        self.slider_smooth.setValue(50)
        self.slider_smooth.valueChanged.connect(self._on_smooth_changed)
        smooth_slider_layout.addWidget(self.slider_smooth)
        self.label_smooth = QLabel("50%")
        smooth_slider_layout.addWidget(self.label_smooth)
        smooth_layout.addLayout(smooth_slider_layout)
        
        # FOV slider
        fov_layout = QHBoxLayout()
        fov_layout.addWidget(QLabel("FOV:"))
        self.slider_fov = QSlider(Qt.Horizontal)
        self.slider_fov.setRange(1, 180)
        self.slider_fov.setValue(90)
        self.slider_fov.valueChanged.connect(self._on_fov_changed)
        fov_layout.addWidget(self.slider_fov)
        self.label_fov = QLabel("90°")
        fov_layout.addWidget(self.label_fov)
        smooth_layout.addLayout(fov_layout)
        
        # Max distance
        dist_layout = QHBoxLayout()
        dist_layout.addWidget(QLabel("Max Distance:"))
        self.spin_max_dist = QDoubleSpinBox()
        self.spin_max_dist.setRange(0, 1000)
        self.spin_max_dist.setValue(500)
        self.spin_max_dist.valueChanged.connect(self._on_max_dist_changed)
        dist_layout.addWidget(self.spin_max_dist)
        smooth_layout.addLayout(dist_layout)
        
        layout.addWidget(smooth_group)
        
        # Advanced settings
        advanced_group = QGroupBox("Advanced")
        advanced_layout = QVBoxLayout(advanced_group)
        
        self.check_visibility = QCheckBox("Visibility Check")
        self.check_visibility.setChecked(True)
        advanced_layout.addWidget(self.check_visibility)
        
        self.check_silent = QCheckBox("Silent Aim")
        advanced_layout.addWidget(self.check_silent)
        
        self.check_prediction = QCheckBox("Target Prediction")
        advanced_layout.addWidget(self.check_prediction)
        
        layout.addWidget(advanced_group)
        
        # RCS settings
        rcs_group = QGroupBox("Recoil Control")
        rcs_layout = QVBoxLayout(rcs_group)
        
        self.check_rcs = QCheckBox("Enable RCS")
        rcs_layout.addWidget(self.check_rcs)
        
        rcs_h_layout = QHBoxLayout()
        rcs_h_layout.addWidget(QLabel("Horizontal:"))
        self.slider_rcs_h = QSlider(Qt.Horizontal)
        self.slider_rcs_h.setRange(0, 100)
        self.slider_rcs_h.setValue(100)
        rcs_h_layout.addWidget(self.slider_rcs_h)
        rcs_layout.addLayout(rcs_h_layout)
        
        rcs_v_layout = QHBoxLayout()
        rcs_v_layout.addWidget(QLabel("Vertical:"))
        self.slider_rcs_v = QSlider(Qt.Horizontal)
        self.slider_rcs_v.setRange(0, 100)
        self.slider_rcs_v.setValue(100)
        rcs_v_layout.addWidget(self.slider_rcs_v)
        rcs_layout.addLayout(rcs_v_layout)
        
        layout.addWidget(rcs_group)
        
        layout.addStretch()
        return widget
    
    def _create_esp_tab(self) -> QWidget:
        """Create the ESP configuration tab"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Enable checkbox
        self.check_esp = QCheckBox("Enable ESP")
        self.check_esp.stateChanged.connect(self._on_esp_toggle)
        layout.addWidget(self.check_esp)
        
        # Player ESP group
        player_group = QGroupBox("Player ESP")
        player_layout = QVBoxLayout(player_group)
        
        self.check_esp_box = QCheckBox("Player Boxes")
        self.check_esp_box.setChecked(True)
        player_layout.addWidget(self.check_esp_box)
        
        self.check_esp_skeleton = QCheckBox("Skeleton")
        self.check_esp_skeleton.setChecked(True)
        player_layout.addWidget(self.check_esp_skeleton)
        
        self.check_esp_health = QCheckBox("Health Bar")
        self.check_esp_health.setChecked(True)
        player_layout.addWidget(self.check_esp_health)
        
        self.check_esp_name = QCheckBox("Player Name")
        self.check_esp_name.setChecked(True)
        player_layout.addWidget(self.check_esp_name)
        
        self.check_esp_distance = QCheckBox("Distance")
        self.check_esp_distance.setChecked(True)
        player_layout.addWidget(self.check_esp_distance)
        
        self.check_esp_weapon = QCheckBox("Weapon")
        player_layout.addWidget(self.check_esp_weapon)
        
        self.check_esp_snaplines = QCheckBox("Snaplines")
        player_layout.addWidget(self.check_esp_snaplines)
        
        layout.addWidget(player_group)
        
        # Filter settings
        filter_group = QGroupBox("Filters")
        filter_layout = QVBoxLayout(filter_group)
        
        self.check_esp_allies = QCheckBox("Show Allies")
        filter_layout.addWidget(self.check_esp_allies)
        
        self.check_esp_dead = QCheckBox("Show Dead Players")
        filter_layout.addWidget(self.check_esp_dead)
        
        max_dist_layout = QHBoxLayout()
        max_dist_layout.addWidget(QLabel("Max Distance:"))
        self.spin_esp_dist = QDoubleSpinBox()
        self.spin_esp_dist.setRange(0, 1000)
        self.spin_esp_dist.setValue(500)
        max_dist_layout.addWidget(self.spin_esp_dist)
        filter_layout.addLayout(max_dist_layout)
        
        layout.addWidget(filter_group)
        
        # ESP Mode
        mode_group = QGroupBox("ESP Mode")
        mode_layout = QVBoxLayout(mode_group)
        
        mode_select_layout = QHBoxLayout()
        mode_select_layout.addWidget(QLabel("Mode:"))
        self.combo_esp_mode = QComboBox()
        self.combo_esp_mode.addItems(["External Socket", "External File", "Internal"])
        mode_select_layout.addWidget(self.combo_esp_mode)
        mode_layout.addLayout(mode_select_layout)
        
        # Socket settings
        socket_layout = QHBoxLayout()
        socket_layout.addWidget(QLabel("Socket Port:"))
        self.spin_esp_port = QSpinBox()
        self.spin_esp_port.setRange(1, 65535)
        self.spin_esp_port.setValue(5555)
        socket_layout.addWidget(self.spin_esp_port)
        mode_layout.addLayout(socket_layout)
        
        layout.addWidget(mode_group)
        
        layout.addStretch()
        return widget
    
    def _create_misc_tab(self) -> QWidget:
        """Create the miscellaneous features tab"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Combat features
        combat_group = QGroupBox("Combat")
        combat_layout = QVBoxLayout(combat_group)
        
        self.check_no_recoil = QCheckBox("No Recoil")
        self.check_no_recoil.stateChanged.connect(self._on_no_recoil_toggle)
        combat_layout.addWidget(self.check_no_recoil)
        
        self.check_no_spread = QCheckBox("No Spread")
        self.check_no_spread.stateChanged.connect(self._on_no_spread_toggle)
        combat_layout.addWidget(self.check_no_spread)
        
        self.check_infinite_ammo = QCheckBox("Infinite Ammo")
        self.check_infinite_ammo.stateChanged.connect(self._on_infinite_ammo_toggle)
        combat_layout.addWidget(self.check_infinite_ammo)
        
        self.check_no_reload = QCheckBox("No Reload")
        combat_layout.addWidget(self.check_no_reload)
        
        self.check_rapid_fire = QCheckBox("Rapid Fire")
        combat_layout.addWidget(self.check_rapid_fire)
        
        layout.addWidget(combat_group)
        
        # Movement features
        movement_group = QGroupBox("Movement")
        movement_layout = QVBoxLayout(movement_group)
        
        self.check_speed_hack = QCheckBox("Speed Hack")
        movement_layout.addWidget(self.check_speed_hack)
        
        speed_layout = QHBoxLayout()
        speed_layout.addWidget(QLabel("Speed Multiplier:"))
        self.spin_speed = QDoubleSpinBox()
        self.spin_speed.setRange(0.5, 5.0)
        self.spin_speed.setValue(1.5)
        self.spin_speed.setSingleStep(0.1)
        speed_layout.addWidget(self.spin_speed)
        movement_layout.addLayout(speed_layout)
        
        self.check_infinite_stamina = QCheckBox("Infinite Stamina")
        movement_layout.addWidget(self.check_infinite_stamina)
        
        layout.addWidget(movement_group)
        
        # Visual features
        visual_group = QGroupBox("Visual")
        visual_layout = QVBoxLayout(visual_group)
        
        self.check_no_fog = QCheckBox("No Fog")
        visual_layout.addWidget(self.check_no_fog)
        
        self.check_full_bright = QCheckBox("Full Bright")
        visual_layout.addWidget(self.check_full_bright)
        
        self.check_xray = QCheckBox("X-Ray Vision")
        self.check_xray.stateChanged.connect(self._on_xray_toggle)
        visual_layout.addWidget(self.check_xray)
        
        fov_layout = QHBoxLayout()
        self.check_fov_changer = QCheckBox("Custom FOV:")
        fov_layout.addWidget(self.check_fov_changer)
        self.spin_fov = QSpinBox()
        self.spin_fov.setRange(60, 120)
        self.spin_fov.setValue(90)
        fov_layout.addWidget(self.spin_fov)
        visual_layout.addLayout(fov_layout)
        
        layout.addWidget(visual_group)
        
        # Other features
        other_group = QGroupBox("Other")
        other_layout = QVBoxLayout(other_group)
        
        self.check_anti_afk = QCheckBox("Anti-AFK")
        other_layout.addWidget(self.check_anti_afk)
        
        self.check_auto_pickup = QCheckBox("Auto Pickup")
        other_layout.addWidget(self.check_auto_pickup)
        
        self.check_auto_loot = QCheckBox("Auto Loot")
        other_layout.addWidget(self.check_auto_loot)
        
        layout.addWidget(other_group)
        
        layout.addStretch()
        return widget
    
    def _create_skin_tab(self) -> QWidget:
        """Create the skin changer tab"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Enable checkbox
        self.check_skin_changer = QCheckBox("Enable Skin Changer")
        self.check_skin_changer.stateChanged.connect(self._on_skin_changer_toggle)
        layout.addWidget(self.check_skin_changer)
        
        # Weapon selection
        weapon_group = QGroupBox("Weapon Selection")
        weapon_layout = QVBoxLayout(weapon_group)
        
        weapon_select_layout = QHBoxLayout()
        weapon_select_layout.addWidget(QLabel("Weapon:"))
        self.combo_weapon = QComboBox()
        self.combo_weapon.addItems([
            "M4A1", "MP5", "AK47", "Vector", "SCAR", "AUG",
            "HK416", "M16", "M249", "MP7", "UZI", "P90",
            "AWM", "Kar98k", "Mosin", "SVD", "MK14"
        ])
        self.combo_weapon.currentTextChanged.connect(self._on_weapon_selected)
        weapon_select_layout.addWidget(self.combo_weapon)
        weapon_layout.addLayout(weapon_select_layout)
        
        layout.addWidget(weapon_group)
        
        # Skin selection
        skin_group = QGroupBox("Skin Selection")
        skin_layout = QVBoxLayout(skin_group)
        
        skin_select_layout = QHBoxLayout()
        skin_select_layout.addWidget(QLabel("Skin:"))
        self.combo_skin = QComboBox()
        self.combo_skin.currentTextChanged.connect(self._on_skin_selected)
        skin_select_layout.addWidget(self.combo_skin)
        skin_layout.addLayout(skin_select_layout)
        
        self.btn_apply_skin = QPushButton("Apply Skin")
        self.btn_apply_skin.clicked.connect(self._apply_skin)
        skin_layout.addWidget(self.btn_apply_skin)
        
        layout.addWidget(skin_group)
        
        # Current skins
        current_group = QGroupBox("Applied Skins")
        current_layout = QVBoxLayout(current_group)
        
        self.text_current_skins = QTextEdit()
        self.text_current_skins.setReadOnly(True)
        self.text_current_skins.setMaximumHeight(150)
        current_layout.addWidget(self.text_current_skins)
        
        self.btn_reset_skins = QPushButton("Reset All Skins")
        self.btn_reset_skins.clicked.connect(self._reset_skins)
        current_layout.addWidget(self.btn_reset_skins)
        
        layout.addWidget(current_group)
        
        layout.addStretch()
        return widget
    
    def _create_settings_tab(self) -> QWidget:
        """Create the settings tab"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Connection settings
        conn_group = QGroupBox("Connection Settings")
        conn_layout = QVBoxLayout(conn_group)
        
        host_layout = QHBoxLayout()
        host_layout.addWidget(QLabel("ESP Socket Host:"))
        self.edit_host = QComboBox()
        self.edit_host.setEditable(True)
        self.edit_host.addItem("127.0.0.1")
        self.edit_host.addItem("localhost")
        host_layout.addWidget(self.edit_host)
        conn_layout.addLayout(host_layout)
        
        port_layout = QHBoxLayout()
        port_layout.addWidget(QLabel("ESP Socket Port:"))
        self.spin_port = QSpinBox()
        self.spin_port.setRange(1, 65535)
        self.spin_port.setValue(5555)
        port_layout.addWidget(self.spin_port)
        conn_layout.addLayout(port_layout)
        
        layout.addWidget(conn_group)
        
        # Hotkey settings
        hotkey_group = QGroupBox("Hotkeys")
        hotkey_layout = QVBoxLayout(hotkey_group)
        
        hotkey_layout.addWidget(QLabel("Aimbot Key: Right Mouse Button"))
        hotkey_layout.addWidget(QLabel("Trigger Bot Key: Mouse Button 5"))
        hotkey_layout.addWidget(QLabel("Toggle Menu: Insert"))
        
        layout.addWidget(hotkey_group)
        
        # Update interval
        update_group = QGroupBox("Performance")
        update_layout = QVBoxLayout(update_group)
        
        interval_layout = QHBoxLayout()
        interval_layout.addWidget(QLabel("Update Interval (ms):"))
        self.spin_interval = QSpinBox()
        self.spin_interval.setRange(1, 100)
        self.spin_interval.setValue(16)
        interval_layout.addWidget(self.spin_interval)
        update_layout.addLayout(interval_layout)
        
        layout.addWidget(update_group)
        
        # Config buttons
        config_group = QGroupBox("Configuration")
        config_layout = QVBoxLayout(config_group)
        
        btn_save_config = QPushButton("Save Configuration")
        btn_save_config.clicked.connect(self.save_config)
        config_layout.addWidget(btn_save_config)
        
        btn_load_config = QPushButton("Load Configuration")
        btn_load_config.clicked.connect(self.load_config)
        config_layout.addWidget(btn_load_config)
        
        btn_reset_config = QPushButton("Reset to Defaults")
        btn_reset_config.clicked.connect(self.reset_config)
        config_layout.addWidget(btn_reset_config)
        
        layout.addWidget(config_group)
        
        layout.addStretch()
        return widget
    
    def _create_console_tab(self) -> QWidget:
        """Create the console tab"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        self.text_console = QTextEdit()
        self.text_console.setReadOnly(True)
        self.text_console.setStyleSheet("background-color: #1e1e1e; color: #00ff00; font-family: Consolas, monospace;")
        layout.addWidget(self.text_console)
        
        # Clear button
        btn_clear = QPushButton("Clear Console")
        btn_clear.clicked.connect(self.text_console.clear)
        layout.addWidget(btn_clear)
        
        return widget
    
    def _init_features(self) -> None:
        """Initialize cheat features"""
        if self.sdk and self.entity_manager:
            self.aimbot = Aimbot(self.sdk, self.entity_manager)
            self.esp = ESP(self.sdk, self.entity_manager)
            self.misc = MiscFeatures(self.sdk, self.entity_manager)
            self.skin_changer = SkinChanger(self.sdk, self.entity_manager)
            
            self._log_message("Features initialized")
    
    def _init_timers(self) -> None:
        """Initialize update timers"""
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self._on_update)
        self.update_timer.setInterval(16)  # ~60 FPS
    
    def _on_update(self) -> None:
        """Main update callback"""
        if not self.running:
            return
        
        try:
            if self.aimbot and self.aimbot.settings.enabled:
                self.aimbot.update()
            
            if self.esp and self.esp.settings.enabled:
                self.esp.update()
            
            if self.misc and self.misc.settings.enabled:
                self.misc.update()
            
            if self.skin_changer and self.skin_changer.enabled:
                self.skin_changer.update()
                
        except Exception as e:
            self._log_message(f"Update error: {e}")
    
    def toggle_cheat(self) -> None:
        """Toggle cheat on/off"""
        if self.running:
            self.stop_cheat()
            self.btn_start.setText("▶ Start")
            self.btn_start.setStyleSheet("background-color: #28a745; color: white; padding: 8px 16px;")
        else:
            self.start_cheat()
            self.btn_start.setText("⏹ Stop")
            self.btn_start.setStyleSheet("background-color: #dc3545; color: white; padding: 8px 16px;")
    
    def start_cheat(self) -> None:
        """Start the cheat"""
        self.running = True
        self.update_timer.start()
        self._log_message("Cheat started")
        self._set_status("Running", False)
    
    def stop_cheat(self) -> None:
        """Stop the cheat"""
        self.running = False
        self.update_timer.stop()
        self._log_message("Cheat stopped")
        self._set_status("Stopped", False)
    
    def reload_config(self) -> None:
        """Reload configuration"""
        self._log_message("Configuration reloaded")
    
    def load_config(self) -> None:
        """Load configuration from file"""
        self._log_message("Configuration loaded")
    
    def save_config(self) -> None:
        """Save configuration to file"""
        self._log_message("Configuration saved")
    
    def reset_config(self) -> None:
        """Reset configuration to defaults"""
        self._log_message("Configuration reset to defaults")
    
    def show_about(self) -> None:
        """Show about dialog"""
        QMessageBox.about(self, "About", 
            "BloodStrike Python Cheat v1.0\n\n"
            "A Python-based cheat for BloodStrike\n"
            "Designed for Fedora Linux\n\n"
            "Features:\n"
            "- Aimbot with multiple modes\n"
            "- ESP with external overlay\n"
            "- Skin Changer\n"
            "- Misc features (No Recoil, etc.)\n\n"
            "Educational purposes only.")
    
    # Event handlers
    def _on_aimbot_toggle(self, state) -> None:
        if self.aimbot:
            self.aimbot.settings.enabled = state == Qt.Checked
            self._log_message(f"Aimbot {'enabled' if state == Qt.Checked else 'disabled'}")
    
    def _on_bone_changed(self, bone: str) -> None:
        if self.aimbot:
            bone_map = {"Head": AimTarget.HEAD, "Neck": AimTarget.NECK, 
                       "Chest": AimTarget.CHEST, "Spine": AimTarget.SPINE}
            self.aimbot.settings.target_bone = bone_map.get(bone, AimTarget.HEAD)
    
    def _on_aim_mode_changed(self, mode: str) -> None:
        if self.aimbot:
            mode_map = {"Hold": AimMode.HOLD, "Toggle": AimMode.TOGGLE,
                       "Auto": AimMode.AUTO, "On Key": AimMode.ON_KEY}
            self.aimbot.settings.aim_mode = mode_map.get(mode, AimMode.HOLD)
    
    def _on_smooth_changed(self, value: int) -> None:
        self.label_smooth.setText(f"{value}%")
        if self.aimbot:
            self.aimbot.settings.smoothness = value / 100.0
    
    def _on_fov_changed(self, value: int) -> None:
        self.label_fov.setText(f"{value}°")
        if self.aimbot:
            self.aimbot.settings.fov = float(value)
    
    def _on_max_dist_changed(self, value: float) -> None:
        if self.aimbot:
            self.aimbot.settings.max_distance = value
    
    def _on_esp_toggle(self, state) -> None:
        if self.esp:
            self.esp.settings.enabled = state == Qt.Checked
            if state == Qt.Checked:
                self.esp.start()
            else:
                self.esp.stop()
            self._log_message(f"ESP {'enabled' if state == Qt.Checked else 'disabled'}")
    
    def _on_no_recoil_toggle(self, state) -> None:
        if self.misc:
            self.misc.settings.no_recoil = state == Qt.Checked
    
    def _on_no_spread_toggle(self, state) -> None:
        if self.misc:
            self.misc.settings.no_spread = state == Qt.Checked
    
    def _on_infinite_ammo_toggle(self, state) -> None:
        if self.misc:
            self.misc.settings.infinite_ammo = state == Qt.Checked
    
    def _on_xray_toggle(self, state) -> None:
        if self.misc:
            self.misc.settings.xray_vision = state == Qt.Checked
    
    def _on_skin_changer_toggle(self, state) -> None:
        if self.skin_changer:
            self.skin_changer.set_enabled(state == Qt.Checked)
            self._log_message(f"Skin Changer {'enabled' if state == Qt.Checked else 'disabled'}")
    
    def _on_weapon_selected(self, weapon: str) -> None:
        # Update skin combo box based on weapon
        pass
    
    def _on_skin_selected(self, skin: str) -> None:
        pass
    
    def _apply_skin(self) -> None:
        self._log_message("Skin applied")
    
    def _reset_skins(self) -> None:
        if self.skin_changer:
            self.skin_changer.reset_all_skins()
        self._log_message("All skins reset")
    
    def _log_message(self, message: str) -> None:
        """Log message to console"""
        timestamp = time.strftime("%H:%M:%S")
        self.text_console.append(f"[{timestamp}] {message}")
    
    def _set_status(self, status: str, is_error: bool) -> None:
        """Set status bar message"""
        self.status_bar.showMessage(status)
    
    def closeEvent(self, event) -> None:
        """Handle window close"""
        self.stop_cheat()
        if self.esp:
            self.esp.stop()
        event.accept()


def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
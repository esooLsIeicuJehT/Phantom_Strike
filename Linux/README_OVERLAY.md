# 🎮 PHANTOM STRIKE OVERLAY - Setup Guide

## 🚀 **How to Launch the Overlay**

The overlay is designed to run **on top of your game window**. There are two ways to launch it:

### **Method 1: Standalone Launch (Current)**
```bash
./start.sh
```
This launches the overlay as a separate window. The overlay will be **always on top** of other windows.

### **Method 2: Game Overlay Launch (Recommended)**
```bash
./game_overlay_launcher.sh
```
This script:
1. Waits for BloodStrike to launch
2. Finds the game window
3. Positions the overlay on top of the game

---

## 🎯 **Adding to Steam (For In-Game Overlay)**

To make the overlay launch automatically with your game through Steam:

### **Option A: Add as Non-Steam Game**

1. **Open Steam** → Library → Add a Game → Add a Non-Steam Game
2. **Browse** to: `/home/jigga/Documents/GitHub/Phantom_Strike/Linux/game_overlay_launcher.sh`
3. **Add** the script to Steam
4. **Right-click** the game in Steam → Properties
5. **Set Launch Options** to:
   ```
   /home/jigga/Documents/GitHub/Phantom_Strike/Linux/game_overlay_launcher.sh
   ```

### **Option B: Launch with BloodStrike**

1. **Find BloodStrike** in your Steam library
2. **Right-click** → Properties → Launch Options
3. **Add** before the game command:
   ```
   /home/jigga/Documents/GitHub/Phantom_Strike/Linux/game_overlay_launcher.sh & %command%
   ```

This will launch the overlay script in the background, then launch the game.

---

## 🖱️ **Overlay Controls**

### **Mouse Controls:**
- **Click & Drag Header** - Move the menu anywhere on screen
- **Click Category Tabs** - Switch between ESP, Aimbot, Memory, Skins, Options
- **Click Toggles** - Enable/disable features
- **Click & Drag Sliders** - Adjust values (FOV, smoothness, etc.)
- **Click Buttons** - Activate actions

### **Keyboard:**
- **INSERT** - Toggle menu visibility
- **ESC** - Close overlay

---

## 🔧 **Troubleshooting**

### **Overlay appears in separate window:**
This is normal for the current setup. The overlay runs as an "always on top" window that stays above your game.

### **Overlay not visible:**
1. Press **INSERT** to toggle menu visibility
2. Check if the overlay window is minimized
3. Try running: `./game_overlay_launcher.sh`

### **Game doesn't detect overlay:**
The overlay is **external** and doesn't inject into the game process. It reads game memory externally and displays information on top.

### **Overlay blocks game input:**
The overlay is configured as a `DOCK` window type to minimize focus stealing. If it still blocks input:
- Toggle the menu off with **INSERT**
- Move the menu to a corner by dragging the header

---

## 📋 **Menu Categories**

1. **ESP** - Box ESP, health bars, armor, distance, weapons, names
2. **Aimbot** - Real/AI aimbot, FOV, smoothness, prediction
3. **Memory** - Auto scan offsets, continuous scanning, ML prediction
4. **Skins** - Enable skins, individual weapons, StatTrak™
5. **Options** - Anti-cheat evasion, stealth mode, FPS limit

---

## 🛠️ **Required Tools**

The overlay uses these Linux tools for window management:
- `xdotool` - Window detection and positioning
- `wmctrl` - Window manager control
- `xprop` - Window properties

Install if missing:
```bash
sudo apt install xdotool wmctrl x11-utils
```

---

## 💡 **Tips**

- **Drag the menu** by clicking and holding the header
- **Adjust transparency** in Options → FPS Limit (affects rendering)
- **Hide ESP** when not needed to improve performance
- **Save your config** using Options → Save Config

---

**Last Updated:** 2026-04-03  
**Version:** 3.0 Professional Mouse-Driven Menu

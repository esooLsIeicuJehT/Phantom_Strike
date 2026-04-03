# 🐧 PHANTOM STRIKE - LINUX VERSION

## 🔥 **Professional Gaming Cheat for Linux**

### **✨ Linux-Specific Features:**
- 🐍 **Python-Based Architecture** - Cross-platform compatibility
- 🎮 **OpenGL Overlay** - Hardware-accelerated rendering
- 🧠 **Advanced AI Aimbot** - Machine learning integration
- 🛡️ **Enhanced Anti-Detection** - Linux-specific evasion techniques
- ⚡ **High Performance** - Optimized for Linux systems

---

## 🚀 **QUICK START**

### **Prerequisites:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-pip python3-dev build-essential

# Fedora
sudo dnf install python3.11 python3.11-pip python3-devel gcc

# Arch Linux
sudo pacman -S python311 python-pip base-devel
```

### **Installation:**
```bash
# Navigate to Phantom Strike Linux directory
cd Phantom_Strike/Linux

# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run installation script (optional)
./linux_install.sh
```

### **Launch Options:**
```bash
# Option 1: Main launcher (recommended)
python3 phantom_strike.py

# Option 2: GUI control panel
python3 gui_main.py

# Option 3: External overlay only
python3 external_overlay_imgui.py
```

---

## 🎮 **CONTROLS & FEATURES**

### **Keyboard Controls:**
- **F1** - Toggle ESP
- **F2** - Toggle Aimbot  
- **F3** - Toggle AI Aimbot
- **F4** - Toggle Radar
- **F5** - Toggle Statistics
- **F6** - Toggle Skin Changer
- **INSERT** - Toggle Menu
- **END** - Emergency Stop

### **Mouse Controls:**
- **Right Mouse** - Aimbot activation (when configured)
- **Mouse Scroll** - Adjust settings in GUI
- **Left Click** - Select GUI options

---

## 🎯 **ENHANCED FEATURES**

### **🧠 Advanced AI Aimbot:**
- **Machine Learning Prediction** - Movement pattern analysis
- **Human Behavior Simulation** - Natural aiming movements
- **Advanced Ballistics** - Bullet drop and lead compensation
- **Multi-Target Tracking** - Simultaneous enemy tracking
- **Performance Statistics** - Accuracy and improvement tracking

### **👁️ Professional ESP System:**
- **Multiple Box Styles** - Corner, full, 3D boxes
- **Complete Skeleton Rendering** - Bone structure display
- **Real-time Health Bars** - HP and armor visualization
- **Velocity Indicators** - Movement speed and direction
- **Advanced Radar** - 360-degree threat awareness
- **Customizable Colors** - Personalized visual themes

### **🛡️ Enhanced Anti-Detection:**
- **Signature Rotation** - Dynamic pattern obfuscation
- **Behavioral Masking** - Human-like activity simulation
- **Memory Scrambling** - Background memory protection
- **Process Hiding** - Advanced concealment techniques
- **Anti-Forensics** - Trace elimination and log cleaning
- **Encrypted Communication** - Secure data transmission

### **⚙️ Advanced Configuration:**
- **Enhanced Config Manager** - Encryption and auto-backup
- **Performance Optimization** - FPS limiting and LOD systems
- **Multi-threading Support** - Parallel processing
- **GPU Acceleration** - Hardware optimization
- **Adaptive Quality** - Dynamic performance adjustment

---

## 📁 **FILE STRUCTURE**

```
Phantom_Strike/Linux/
├── 🐍 phantom_strike.py                    # Main launcher
├── 🖥️ gui_main.py                         # GUI control panel
├── 🖥️ external_overlay_imgui.py            # External overlay
├── 🧠 ai_aimbot.py                         # AI aimbot system
├── 🛡️ anti_cheat_evasion.py               # Anti-detection system
├── 🎨 skin_changer.py                      # Skin changer
├── 🔍 auto_offset_scanner.py               # Pattern scanner
├── 📋 enhanced_config_manager.py           # Configuration system
├── ⚙️ config.json                         # Main configuration
├── 📋 requirements.txt                     # Dependencies
├── 🚀 linux_install.sh                    # Install script
├── 📁 docs/                               # Documentation
├── 📁 core/                               # Core modules
├── 📁 features/                           # Feature modules
├── 📁 gui/                                # GUI components
├── 📁 utils/                              # Utilities
├── 📁 SDK/                                # Game SDK
└── 📁 venv/                               # Virtual environment
```

---

## 📋 **SYSTEM REQUIREMENTS**

### **Minimum Requirements:**
- **OS:** Ubuntu 18.04+, Fedora 30+, Arch Linux
- **Python:** 3.8-3.11 (3.12+ not compatible)
- **RAM:** 4GB minimum
- **GPU:** OpenGL 3.3+ compatible
- **CPU:** Dual-core 2.0GHz+
- **Storage:** 2GB free space

### **Recommended Requirements:**
- **OS:** Ubuntu 22.04+, Fedora 38+, Arch Linux
- **Python:** 3.11
- **RAM:** 8GB+ recommended
- **GPU:** Dedicated OpenGL 4.0+ graphics card
- **CPU:** Quad-core 3.0GHz+
- **Storage:** 5GB free space (for virtual environment)

### **Compatible Distributions:**
- ✅ Ubuntu 18.04, 20.04, 22.04
- ✅ Fedora 30, 35, 38
- ✅ Arch Linux (rolling)
- ✅ Debian 10, 11, 12
- ✅ Linux Mint 19, 20, 21
- ✅ openSUSE Leap 15.4+

---

## 🔧 **TROUBLESHOOTING**

### **Common Issues:**

#### **"Python command not found"**
```bash
# Install Python 3.11
sudo apt install python3.11 python3.11-venv

# Use python3.11 explicitly
python3.11 -m venv venv
source venv/bin/activate
```

#### **"OpenGL/PyGame errors"**
```bash
# Install graphics libraries
sudo apt install libgl1-mesa-dev libglu1-mesa-dev

# Update graphics drivers
sudo ubuntu-drivers autoinstall  # Ubuntu
sudo dnf update                  # Fedora
sudo pacman -Syu                 # Arch
```

#### **"Permission denied"**
```bash
# Make scripts executable
chmod +x linux_install.sh

# Run with proper permissions
./linux_install.sh
```

#### **"Import errors"**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Check Python version
python3 --version  # Should be 3.8-3.11
```

#### **"Overlay not showing"**
```bash
# Check OpenGL support
glxinfo | grep "OpenGL version"

# Test PyGame installation
python3 -c "import pygame; print('PyGame OK')"

# Run in windowed mode first
python3 external_overlay_imgui.py
```

---

## 🛡️ **LINUX-SPECIFIC SAFETY**

### **Process Security:**
- **User-level execution** - No root privileges required
- **Sandboxed environment** - Isolated from system processes
- **Memory protection** - Linux-specific memory security
- **Process hiding** - Advanced concealment techniques

### **File System Protection:**
- **Encrypted configs** - Secure configuration storage
- **Temporary file cleanup** - Automatic trace removal
- **Permission management** - Proper file access controls
- **Backup encryption** - Secure backup storage

### **Network Security:**
- **Encrypted communication** - Protected data transmission
- **Traffic obfuscation** - Network pattern masking
- **Protocol simulation** - Normal traffic appearance
- **Connection filtering** - Suspicious packet blocking

---

## ⚡ **PERFORMANCE OPTIMIZATION**

### **For Low-End Systems:**
```json
{
  "performance": {
    "fps_limit": 60,
    "render_optimization": true,
    "esp_max_distance": 300,
    "aimbot_fov": 90,
    "ai_enabled": false,
    "skeleton_esp": false,
    "radar_enabled": false
  }
}
```

### **For High-End Systems:**
```json
{
  "performance": {
    "fps_limit": 144,
    "render_optimization": true,
    "esp_max_distance": 800,
    "aimbot_fov": 120,
    "ai_enabled": true,
    "skeleton_esp": true,
    "radar_enabled": true,
    "prediction_trails": true
  }
}
```

### **Linux Optimization Commands:**
```bash
# Set process priority (lower = less CPU)
renice 10 $$

# Use performance governor (if available)
sudo cpupower frequency-set -g performance

# Optimize memory usage
echo 1 | sudo tee /proc/sys/vm/swappiness
```

---

## 🔄 **UPDATES & MAINTENANCE**

### **Auto-Update Features:**
- ✅ Pattern recognition updates
- ✅ Configuration backup and restore
- ✅ Dependency checking
- ✅ Performance optimization

### **Manual Updates:**
```bash
# Update dependencies
pip install --upgrade -r requirements.txt

# Update patterns (automatic)
python3 auto_offset_scanner.py --update

# Clean virtual environment
rm -rf venv/
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 📞 **SUPPORT**

### **Linux-Specific Issues:**
1. **Check distribution compatibility**
2. **Verify Python version (3.8-3.11)**
3. **Install graphics drivers**
4. **Check OpenGL support**
5. **Verify file permissions**

### **Debug Information:**
```bash
# System information
uname -a
python3 --version
glxinfo | grep OpenGL

# Phantom Strike status
python3 phantom_strike.py --status
python3 phantom_strike.py --debug
```

### **Log Files:**
- **Main log:** `logs/phantom_strike.log`
- **Error log:** `logs/errors.log`
- **Performance log:** `logs/performance.log`

---

## 🎯 **GETTING STARTED**

### **Quick Start Checklist:**
- [ ] Compatible Linux distribution
- [ ] Python 3.8-3.11 installed
- [ ] Graphics drivers updated
- [ ] Dependencies installed
- [ ] Virtual environment created
- [ ] Configuration reviewed
- [ ] Test launch successful

### **First Run:**
```bash
# 1. Navigate to directory
cd Phantom_Strike/Linux

# 2. Activate environment
source venv/bin/activate

# 3. Launch main program
python3 phantom_strike.py

# 4. Configure settings
# 5. Start game and enjoy!
```

---

**🐧 PHANTOM STRIKE LINUX - Professional Gaming Cheat**

*Last Updated: 2026-04-03*  
*Version: 2.0 Enhanced*  
*Platform: Linux (Ubuntu, Fedora, Arch, Debian)*  
*Status: Production Ready*  
*Python: 3.8-3.11*  
*Graphics: OpenGL 3.3+*

**Enjoy your enhanced Linux gaming experience!** 🚀

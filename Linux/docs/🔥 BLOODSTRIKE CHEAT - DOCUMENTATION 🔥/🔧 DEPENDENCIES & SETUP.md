# 🔧 DEPENDENCIES & COMPLETE SETUP GUIDE

## 📋 **BEFORE YOU START - CRITICAL PREREQUISITES**

### **⚠️ MUST READ - COMMON MISTAKES TO AVOID**

1. **❌ Don't skip Visual Studio Build Tools** - PyGame/OpenGL WILL fail
2. **❌ Don't use Python from Microsoft Store** - Use python.org version
3. **❌ Don't install to paths with spaces** - Use `C:\Cheat\` not `C:\My Cheat\`
4. **❌ Don't skip virtual environment** - Prevents conflicts
5. **❌ Don't run as admin unless necessary** - Security risk

---

## 🐍 **PYTHON INSTALLATION**

### **Step 1: Download Correct Python**
```bash
# Go to: https://www.python.org/downloads/
# Download Python 3.11 (recommended) or 3.8-3.10
# DO NOT use Python 3.12+ (compatibility issues)
```

### **Step 2: Install Properly**
```bash
# Run installer as Administrator
# CHECK these options:
# ✅ [x] Add Python to PATH
# ✅ [x] Install for all users
# ✅ [x] Associate .py files

# After installation, verify:
python --version    # Should show Python 3.11.x
pip --version       # Should show pip 23.x.x
```

### **Step 3: Configure Python**
```bash
# Upgrade pip to latest
python -m pip install --upgrade pip

# Install wheel for better package installation
pip install wheel

# Install setuptools
pip install setuptools
```

---

## 🛠️ **VISUAL STUDIO BUILD TOOLS (CRITICAL!)**

### **Why This is Required:**
- PyGame needs C++ compilers
- OpenGL requires build tools
- Many Python packages need compilation

### **Step 1: Download Build Tools**
```bash
# Go to: https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Download "Build Tools for Visual Studio 2022"
# File size: ~6MB (downloads additional components)
```

### **Step 2: Install Correct Components**
```bash
# Run installer as Administrator
# SELECT these workloads:
# ✅ [x] Desktop development with C++

# In "Individual components" tab, ensure:
# ✅ [x] MSVC v143 - VS 2022 C++ x64/x86 build tools
# ✅ [x] Windows 11 SDK (latest version)
# ✅ [x] C++ CMake tools for Visual Studio
```

### **Step 3: Verify Installation**
```bash
# Open Command Prompt as Administrator
# Test cl.exe (C++ compiler):
cl

# Should show Microsoft C++ Compiler version
# If not found, restart computer and try again
```

---

## 📦 **DEPENDENCY INSTALLATION**

### **Method 1: Automatic (Recommended)**
```bash
# Navigate to cheat directory
cd C:\BloodStrikeCheat

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Upgrade pip in virtual environment
python -m pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

### **Method 2: Manual Step-by-Step**
```bash
# Activate virtual environment first!
venv\Scripts\activate

# Install core gaming libraries
pip install pygame>=2.5.0
pip install PyOpenGL>=3.1.7
pip install PyOpenGL-accelerate>=3.1.7

# Install GUI framework
pip install imgui[full]>=2.0.0
pip install imgui[glfw]>=2.0.0

# Install machine learning
pip install scikit-learn>=1.3.0
pip install numpy>=1.24.0

# Install system utilities
pip install psutil>=5.9.0
pip install pynput>=1.7.0

# Install optional themes
pip install darkdetect>=0.8.0
```

### **Method 3: If You Have Issues**
```bash
# Try installing without version constraints
pip install pygame PyOpenGL PyOpenGL-accelerate
pip install imgui
pip install scikit-learn numpy
pip install psutil pynput

# If PyOpenGL fails, try:
pip install --upgrade pip setuptools wheel
pip install PyOpenGL --force-reinstall
```

---

## 🎯 **TESTING INSTALLATION**

### **Test 1: Basic Python Modules**
```bash
# Activate virtual environment
venv\Scripts\activate

# Test each module:
python -c "import pygame; print('✅ PyGame:', pygame.version.ver)"
python -c "import OpenGL; print('✅ OpenGL installed')"
python -c "import imgui; print('✅ ImGui installed')"
python -c "import sklearn; print('✅ Scikit-learn:', sklearn.__version__)"
python -c "import numpy; print('✅ NumPy:', numpy.__version__)"
```

### **Test 2: External Overlay**
```bash
# This is the most important test
python external_overlay_imgui.py

# EXPECTED RESULT:
# - Dark ImGui window appears
# - Shows "Waiting for data..."
# - No error messages
# - Can interact with interface

# IF IT FAILS:
# - Check pygame installation
# - Update graphics drivers
# - Run as administrator
```

### **Test 3: Individual Components**
```bash
# Test skin changer
python skin_changer.py

# Test AI aimbot
python ai_aimbot.py

# Test pattern recognition
python test_real_patterns.py
```

---

## ⚠️ **COMMON INSTALLATION PROBLEMS & SOLUTIONS**

### **Problem: "Microsoft Visual C++ 14.0 is required"**
```bash
# CAUSE: Missing Visual Studio Build Tools
# SOLUTION: Install Visual Studio Build Tools 2022
# See section above for detailed steps
```

### **Problem: "pygame.error: No available video device"**
```bash
# CAUSE: Graphics driver issues or headless environment
# SOLUTION 1: Update graphics drivers
# Download latest drivers from NVIDIA/AMD/Intel

# SOLUTION 2: Run with display
# Make sure you're not in SSH/tmux session

# SOLUTION 3: Reinstall PyGame
pip uninstall pygame
pip install pygame
```

### **Problem: "ImportError: DLL load failed"**
```bash
# CAUSE: Missing Visual C++ Redistributables
# SOLUTION 1: Install Visual C++ Redistributables
# Download from Microsoft website

# SOLUTION 2: Reinstall with specific version
pip install --force-reinstall pygame

# SOLUTION 3: Check Python architecture
# Make sure you're using 64-bit Python on 64-bit Windows
```

### **Problem: "OpenGL/GLFW errors"**
```bash
# CAUSE: Missing OpenGL support or drivers
# SOLUTION 1: Update graphics drivers
# SOLUTION 2: Install OpenGL runtime
# SOLUTION 3: Try different PyOpenGL version
pip install PyOpenGL==3.1.6
```

### **Problem: "Virtual environment activation fails"**
```bash
# CAUSE: Execution policy restrictions
# SOLUTION: Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate:
venv\Scripts\activate.ps1
```

### **Problem: "pip install fails with permissions error"**
```bash
# CAUSE: User permissions issue
# SOLUTION 1: Run as Administrator
# SOLUTION 2: Use user install
pip install --user package_name

# SOLUTION 3: Check Python path
where python
where pip
```

---

## 🔧 **ADVANCED CONFIGURATION**

### **Custom requirements.txt**
```txt
# Core gaming libraries
pygame>=2.5.0,<3.0.0
PyOpenGL>=3.1.7,<4.0.0
PyOpenGL-accelerate>=3.1.7,<4.0.0

# GUI framework
imgui[full]>=2.0.0,<3.0.0
imgui[glfw]>=2.0.0,<3.0.0
glfw>=2.6.0,<3.0.0

# Machine learning
scikit-learn>=1.3.0,<2.0.0
numpy>=1.24.0,<2.0.0
scipy>=1.10.0,<2.0.0

# System utilities
psutil>=5.9.0,<6.0.0
pynput>=1.7.0,<2.0.0

# Optional themes
darkdetect>=0.8.0,<1.0.0

# Development tools (optional)
pytest>=7.0.0,<8.0.0
black>=23.0.0,<24.0.0
```

### **Environment Variables (Optional)**
```bash
# Set these if you have issues
set PYTHONPATH=C:\BloodStrikeCheat
set PYGAME_HIDE_SUPPORT_PROMPT=1
set SDL_VIDEO_WINDOW_POS=center
```

### **Performance Optimization**
```bash
# Install optimized versions
pip install --pre pygame

# Use wheel cache
pip install --use-wheel --find-links https://download.lfd.uci.edu/pythonlibs/archived/

# For faster numpy
pip install intel-numpy
```

---

## 🖥️ **SYSTEM-SPECIFIC NOTES**

### **Windows 10/11:**
```bash
# Enable Developer Mode (optional)
# Settings > Update & Security > For developers > Developer Mode

# Disable Windows Defender Real-time Protection (temporary)
# Only if installation fails due to antivirus blocking
```

### **Laptops with Integrated Graphics:**
```bash
# Make sure Python uses dedicated GPU
# Set graphics preference for Python executable
# Control Panel > Graphics > Browse > python.exe
```

### **Multi-Monitor Setup:**
```bash
# Set primary monitor for overlay
# Windows Settings > Display > Set as primary display
```

---

## 🔄 **MAINTENANCE & UPDATES**

### **Update Dependencies:**
```bash
# Activate virtual environment
venv\Scripts\activate

# Update all packages
pip install --upgrade -r requirements.txt

# Update specific packages
pip install --upgrade pygame imgui scikit-learn
```

### **Clean Installation:**
```bash
# Remove old virtual environment
rmdir /s /q venv

# Create new one
python -m venv venv
venv\Scripts\activate

# Install fresh
pip install -r requirements.txt
```

### **Backup Configuration:**
```bash
# Save your settings
copy config.json config_backup.json
copy offsets_database.json offsets_backup.json
```

---

## 📞 **GETTING HELP**

### **Before Asking for Help:**
1. ✅ Read this entire guide
2. ✅ Try all troubleshooting steps
3. ✅ Check error messages carefully
4. ✅ Provide system information

### **Information to Include:**
```bash
# System info
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
python --version
pip --version

# Error messages (full text)
# What you were trying to do
# What happened instead
```

### **Self-Diagnosis Checklist:**
- [ ] Python 3.8-3.11 installed
- [ ] Visual Studio Build Tools installed
- [ ] Virtual environment created
- [ ] Dependencies installed without errors
- [ ] External overlay test passed
- [ ] No antivirus interference

---

## 🎯 **SUCCESS INDICATORS**

### **Installation Successful When:**
- ✅ All Python modules import without errors
- ✅ External overlay window appears
- ✅ No DLL load failures
- ✅ Virtual environment activates properly
- ✅ Requirements.txt installs cleanly

### **Ready to Use When:**
- ✅ External overlay shows ImGui interface
- ✅ Configuration files load correctly
- ✅ Debug mode shows no critical errors
- ✅ All test scripts run successfully

---

## 🏁 **FINAL VERIFICATION**

### **Run This Complete Test:**
```bash
# Activate environment
venv\Scripts\activate

# Test all components
echo "Testing Python modules..."
python -c "
import pygame, OpenGL, imgui, sklearn, numpy, psutil
print('✅ All core modules imported successfully')
"

echo "Testing external overlay..."
timeout 10 python external_overlay_imgui.py

echo "Testing cheat components..."
python skin_changer.py
python test_real_patterns.py

echo "Installation complete! 🎯"
```

**If all tests pass, you're ready to use the cheat!** 🚀

---

*Last Updated: 2026-04-03*  
*Windows 10/11 Compatible*  
*Python 3.8-3.11 Tested*

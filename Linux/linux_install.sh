#!/bin/bash
# PHANTOM STRIKE - Linux Installation Script
echo "🔥 PHANTOM STRIKE - Linux Installation"
echo "====================================="

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "🐍 Current Python version: $PYTHON_VERSION"

# Function to install Python 3.11
install_python311() {
    echo "📦 Installing Python 3.11..."
    
    # Ubuntu/Debian
    if command -v apt &> /dev/null; then
        sudo apt update
        sudo apt install -y python3.11 python3.11-venv python3.11-dev python3.11-pip
        
    # Fedora/RHEL/CentOS
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y python3.11 python3.11-pip
        
    # Arch Linux
    elif command -v pacman &> /dev/null; then
        sudo pacman -S python311
        
    else
        echo "❌ Unsupported Linux distribution"
        echo "Please install Python 3.11 manually"
        exit 1
    fi
    
    echo "✅ Python 3.11 installed"
}

# Check if Python 3.11 is available
if ! command -v python3.11 &> /dev/null; then
    echo "⚠️ Python 3.11 not found"
    read -p "Install Python 3.11? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        install_python311
    else
        echo "❌ Python 3.11 required for ImGui compatibility"
        exit 1
    fi
fi

# Create virtual environment
echo "📁 Creating virtual environment..."
python3.11 -m venv venv

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Test installation
echo "🧪 Testing installation..."
python -c "
import pygame
import OpenGL
import imgui
import sklearn
import numpy
print('✅ All dependencies installed successfully!')
"

echo "🎯 Installation complete!"
echo ""
echo "📝 Usage:"
echo "source venv/bin/activate"
echo "python external_overlay_imgui.py"
echo ""
echo "🎮 Controls: F1=ESP, F2=Aimbot, F3=AI, F4=Auto-Update, F5=Skins, END=Panic"

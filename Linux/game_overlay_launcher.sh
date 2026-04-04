#!/bin/bash
# Phantom Strike Game Overlay Launcher
# This script finds the game window and overlays the menu on top of it

cd "$(dirname "$0")"

# Activate virtual environment
source venv311/bin/activate

# Wait for game to launch
echo "🎮 Waiting for BloodStrike to launch..."
sleep 3

# Find the game window
GAME_WINDOW=$(xdotool search --name "BloodStrike" | head -1)

if [ -z "$GAME_WINDOW" ]; then
    echo "⚠️  Game window not found, trying alternative names..."
    GAME_WINDOW=$(xdotool search --name "bloodstrike" | head -1)
fi

if [ -z "$GAME_WINDOW" ]; then
    echo "⚠️  Game not detected, launching overlay anyway..."
else
    echo "✅ Found game window: $GAME_WINDOW"
    
    # Get game window position and size
    eval $(xdotool getwindowgeometry --shell $GAME_WINDOW)
    echo "📐 Game window: ${WIDTH}x${HEIGHT} at ${X},${Y}"
fi

# Launch the overlay
echo "🚀 Launching Phantom Strike Overlay..."
python3 phantom_strike_pro.py

echo "✅ Overlay closed"

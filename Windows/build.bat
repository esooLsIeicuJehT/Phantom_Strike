@echo off
echo 🔥 PHANTOM STRIKE - Windows DLL Build Script
echo ========================================

REM Check for Visual Studio Build Tools
where cl >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Visual Studio Build Tools not found!
    echo Please install Visual Studio Build Tools 2022
    echo Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/
    pause
    exit /b 1
)

echo ✅ Visual Studio Build Tools found

REM Set up Visual Studio environment
call "C:\Program Files\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat" 2>nul
if %ERRORLEVEL% NEQ 0 (
    call "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvars64.bat" 2>nul
)

if %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to set up Visual Studio environment
    pause
    exit /b 1
)

echo ✅ Visual Studio environment configured

REM Compile the DLL
echo 🔨 Compiling phantom_strike.dll...
cl /LD /EHsc /O2 /D_CRT_SECURE_NO_WARNINGS ^
   phantom_strike_fixed.cpp ^
   /Fe:phantom_strike.dll ^
   /link d3d11.lib dxgi.lib d2d1.lib dwrite.lib user32.lib gdi32.lib psapi.lib ^
   /OUT:phantom_strike.dll

if %ERRORLEVEL% NEQ 0 (
    echo ❌ Compilation failed!
    pause
    exit /b 1
)

echo ✅ Compilation successful!

REM Check if DLL was created
if exist phantom_strike.dll (
    echo 🎯 phantom_strike.dll created successfully!
    echo 📁 File size: 
    dir phantom_strike.dll | find "phantom_strike.dll"
) else (
    echo ❌ DLL file not found!
    pause
    exit /b 1
)

echo.
echo 🚀 PHANTOM STRIKE DLL is ready!
echo.
echo 📝 Usage:
echo 1. Run BloodStrike
echo 2. Execute: python dll_injector.py
echo 3. Press F1-F5 to activate features
echo.
echo 🎮 Controls:
echo F1 - Toggle ESP
echo F2 - Toggle Aimbot  
echo F3 - Toggle AI Aimbot
echo F4 - Toggle Auto Update
echo F5 - Toggle Skin Changer
echo END - Panic Mode
echo.

pause

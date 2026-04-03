cmake_minimum_required(VERSION 3.16)
project(PhantomStrike)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
find_package(DirectX REQUIRED)

# Add source files
set(SOURCES
    phantom_strike_fixed.cpp
)

# Create shared library (DLL)
add_library(PhantomStrike SHARED ${SOURCES})

# Link libraries
target_link_libraries(PhantomStrike
    d3d11
    dxgi
    d2d1
    dwrite
    user32
    gdi32
    psapi
)

# Set output directory
set_target_properties(PhantomStrike PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib
)

# Compiler-specific options
if(MSVC)
    target_compile_options(PhantomStrike PRIVATE
        /W3
        /EHsc
        /D_CRT_SECURE_NO_WARNINGS
    )
endif()

# Copy DLL to output directory
add_custom_command(
    TARGET PhantomStrike POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:PhantomStrike> ${CMAKE_BINARY_DIR}/phantom_strike.dll
)

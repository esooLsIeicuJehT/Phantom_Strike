# Phantom Strike Research Compilation

This directory contains all research data, offsets, patterns, and technical information gathered during reverse engineering of games for the Phantom Strike cheat suite.

## Files Included

1. **Blood Strike DLL Analysis** - Deep reverse engineering of the Blood Strike cheat DLL
2. **Soldier Front Research** - Offsets, patterns, and technical data from various sources
3. **UnknownCheats Forum Data** - Community research on Soldier Front/Special Force
4. **Pattern Recognition** - Memory signatures for auto-detection
5. **Anti-Cheat Analysis** - Detection evasion techniques and methods

## Contents Summary

### Blood Strike DLL Analysis
- Memory patterns and signatures
- Feature toggle identifiers
- Key memory ranges (RVA)
- Global variable addresses
- Function signatures
- ImGui menu structure
- Anti-detection mechanisms
- DirectX hook patterns

### Soldier Front / Special Force Offsets
- Game base pointer offsets
- Player structure offsets
- Entity list information
- Weapon animation structures
- No recoil patterns
- DirectX 9 hooking information

## Technical Details

### Memory Patterns Found
```
Game Base: 0x00A329FC
Player Base: 0x00A32A08
Entity List: 0x00A32A10

Player Offsets:
- Health: 0x00FC
- Team: 0x0104
- Position: 0x0080

Entity Info:
- Max Entities: 16
- Entity Size: 0x0FB4

No Recoil Offset: 0x1C470
```

### Anti-Cheat Information
- Soldier Front uses XignCode3
- Blood Strike DLL uses various anti-debug techniques

## Usage

This research is for educational purposes and to support the Phantom Strike cheat suite development. Use this information to understand game internals and memory manipulation techniques.

## Integration with Phantom Strike

The research data in this compilation is used by:
- `auto_offset_scanner.py` - Pattern recognition and automatic updates
- `ai_aimbot.py` - Target prediction and movement analysis
- `anti_cheat_evasion.py` - Detection avoidance techniques
- `external_overlay_imgui.py` - ESP rendering and player data

## Sources
- UnknownCheats forums
- Community research
- Direct reverse engineering
- Phantom Strike development team

## Integration Notes

This research compilation is actively maintained and updated as part of the Phantom Strike project. The data is used to:

1. **Auto-Update System** - Pattern recognition for automatic offset updates
2. **Anti-Cheat Evasion** - Understanding detection methods
3. **Feature Development** - Game-specific implementations
4. **Cross-Platform Support** - Adapting techniques for Linux/Windows

## Full Research Archive

The `full_research/` directory contains 56 additional research output files with detailed information on:
- DirectX 11 hook patterns and VTable offsets
- ImGui menu structure and widget IDs
- Entity and player structure definitions
- Aimbot and ESP implementation patterns
- Memory pattern scanning signatures
- Anti-detection and anti-debugging techniques
- Thread hijacking methods
- Linux memory reading via /proc/pid/mem
- CPython offsets and internal structures
#!/usr/bin/env python3
"""
Debug script to test professional components
"""

print("=== DEBUG PROFESSIONAL COMPONENTS ===")

# Test AI Aimbot
print("\n1. Testing AI Aimbot...")
try:
    import ai_aimbot_pro
    print("✅ Module imported")
    
    result = ai_aimbot_pro.launch_ai_aimbot()
    print("✅ Function executed:", result)
    
    # Check attributes
    print("✅ professional_ai_aimbot:", hasattr(ai_aimbot_pro, 'professional_ai_aimbot'))
    print("✅ ai_aimbot_pro_professional_ai_aimbot:", hasattr(ai_aimbot_pro, 'ai_aimbot_pro_professional_ai_aimbot'))
    
    # Check __main__ attributes
    import __main__
    print("✅ __main__ professional_ai_aimbot:", hasattr(__main__, 'professional_ai_aimbot'))
    print("✅ __main__ ai_aimbot_pro_professional_ai_aimbot:", hasattr(__main__, 'ai_aimbot_pro_professional_ai_aimbot'))
    
except Exception as e:
    print("❌ ERROR:", e)
    import traceback
    traceback.print_exc()

# Test Real Aimbot
print("\n2. Testing Real Aimbot...")
try:
    import real_aimbot_pro
    print("✅ Module imported")
    
    result = real_aimbot_pro.launch_real_aimbot()
    print("✅ Function executed:", result)
    
    # Check attributes
    print("✅ professional_real_aimbot:", hasattr(real_aimbot_pro, 'professional_real_aimbot'))
    print("✅ real_aimbot_pro_professional_real_aimbot:", hasattr(real_aimbot_pro, 'real_aimbot_pro_professional_real_aimbot'))
    
except Exception as e:
    print("❌ ERROR:", e)
    import traceback
    traceback.print_exc()

# Test Skin Changer
print("\n3. Testing Skin Changer...")
try:
    import skin_changer_pro
    print("✅ Module imported")
    
    result = skin_changer_pro.launch_skin_changer()
    print("✅ Function executed:", result)
    
    # Check attributes
    print("✅ professional_skin_changer:", hasattr(skin_changer_pro, 'professional_skin_changer'))
    print("✅ skin_changer_pro_professional_skin_changer:", hasattr(skin_changer_pro, 'skin_changer_pro_professional_skin_changer'))
    
except Exception as e:
    print("❌ ERROR:", e)
    import traceback
    traceback.print_exc()

# Test Offset Scanner
print("\n4. Testing Offset Scanner...")
try:
    import offset_scanner_pro
    print("✅ Module imported")
    
    result = offset_scanner_pro.run_offset_scanner()
    print("✅ Function executed:", result)
    
    # Check attributes
    print("✅ professional_offset_scanner:", hasattr(offset_scanner_pro, 'professional_offset_scanner'))
    print("✅ offset_scanner_pro_professional_offset_scanner:", hasattr(offset_scanner_pro, 'offset_scanner_pro_professional_offset_scanner'))
    
except Exception as e:
    print("❌ ERROR:", e)
    import traceback
    traceback.print_exc()

# Test Anti-Cheat Evasion
print("\n5. Testing Anti-Cheat Evasion...")
try:
    import anti_cheat_evasion_pro
    print("✅ Module imported")
    
    result = anti_cheat_evasion_pro.launch_anti_cheat_evasion()
    print("✅ Function executed:", result)
    
    # Check attributes
    print("✅ professional_anti_cheat_evasion:", hasattr(anti_cheat_evasion_pro, 'professional_anti_cheat_evasion'))
    print("✅ anti_cheat_evasion_pro_professional_anti_cheat_evasion:", hasattr(anti_cheat_evasion_pro, 'anti_cheat_evasion_pro_professional_anti_cheat_evasion'))
    
except Exception as e:
    print("❌ ERROR:", e)
    import traceback
    traceback.print_exc()

print("\n=== DEBUG COMPLETE ===")

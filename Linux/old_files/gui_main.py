import pygame
from pygame.locals import *
import imgui
from imgui.integrations.pygame import PygameRenderer

# --- IMPORTING YOUR WRAPPED SCRIPTS ---
try:
    import importlib
    import ai_aimbot_gui
    import skin_changer_wrapper
    import offset_scanner_wrapper
    import anti_cheat_evasion_wrapper
    WRAPPED_SCRIPTS_AVAILABLE = True
except ImportError as e:
    print(f"Missing wrapped script: {e}")
    WRAPPED_SCRIPTS_AVAILABLE = False

def main():
    pygame.init()
    # Use regular pygame surface instead of OpenGL
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("PHANTOM STRIKE :: REPOSITORY")

    imgui.create_context()
    renderer = PygameRenderer()
    
    clock = pygame.time.Clock()

    # Variables to track status
    log_messages = ["> System initialized - Ready for operations"]
    
    # Global instances for GUI access
    ai_aimbot_instance = None
    skin_changer_instance = None
    scanner_instance = None
    evasion_instance = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            renderer.process_event(event)

        # Get display size for ImGui
        display_size = pygame.display.get_surface().get_size()
        imgui.get_io().display_size = display_size
        
        imgui.new_frame()
        
        # --- THE CONTROL PANEL ---
        imgui.set_next_window_size(600, 500)
        imgui.begin("Phantom Strike Mainframe", True)

        imgui.text_colored("HACKER-NOIR OVERLAY ACTIVE", 0.0, 1.0, 0.8)
        imgui.separator()

        # --- BUTTON 1: AIMBOT ---
        if imgui.button("EXECUTE AIMBOT", 260, 40):
            if WRAPPED_SCRIPTS_AVAILABLE:
                try:
                    importlib.reload(ai_aimbot_gui)  # Re-reads the file from disk
                    result = ai_aimbot_gui.launch_ai_aimbot()
                    log_messages.append(f"> [RELOADED] {result}")
                except Exception as e:
                    log_messages.append(f"> [ERROR] AI Aimbot: {str(e)}")
            else:
                log_messages.append("> [ERROR] AI Aimbot wrapper not available")

        # --- BUTTON 2: SKIN CHANGER ---
        if imgui.button("RUN SKIN CHANGER", 260, 40):
            if WRAPPED_SCRIPTS_AVAILABLE:
                try:
                    importlib.reload(skin_changer_wrapper)
                    result = skin_changer_wrapper.launch_skin_changer()
                    log_messages.append(f"> [RELOADED] {result}")
                except Exception as e:
                    log_messages.append(f"> [ERROR] Skin Changer: {str(e)}")
            else:
                log_messages.append("> [ERROR] Skin Changer wrapper not available")

        # --- BUTTON 3: OFFSET SCANNER ---
        if imgui.button("SCAN OFFSETS", 260, 40):
            if WRAPPED_SCRIPTS_AVAILABLE:
                try:
                    importlib.reload(offset_scanner_wrapper)
                    result = offset_scanner_wrapper.run_offset_scanner()
                    log_messages.append(f"> [RELOADED] {result}")
                except Exception as e:
                    log_messages.append(f"> [ERROR] Offset Scanner: {str(e)}")
            else:
                log_messages.append("> [ERROR] Offset Scanner wrapper not available")
        
        # --- BUTTON 4: ANTI-CHEAT EVASION ---
        if imgui.button("ACTIVATE ANTI-CHEAT", 260, 40):
            if WRAPPED_SCRIPTS_AVAILABLE:
                try:
                    importlib.reload(anti_cheat_evasion_wrapper)
                    result = anti_cheat_evasion_wrapper.launch_anti_cheat_evasion()
                    log_messages.append(f"> [RELOADED] {result}")
                except Exception as e:
                    log_messages.append(f"> [ERROR] Anti-Cheat: {str(e)}")
            else:
                log_messages.append("> [ERROR] Anti-Cheat wrapper not available")

        imgui.spacing()
        imgui.text("Development Console:")
        imgui.begin_child("logs", 0, 150, border=True)
        
        # Display log messages (keep only last 10 messages)
        display_messages = log_messages[-10:] if len(log_messages) > 10 else log_messages
        for msg in display_messages:
            imgui.text(msg)
        
        # Auto-scroll to bottom
        if len(log_messages) > 0:
            imgui.set_scroll_here_y(1.0)
        
        imgui.end_child()

        imgui.end()

        # Render
        screen.fill((20, 20, 30))  # Dark background
        imgui.render()
        renderer.render(imgui.get_draw_data())
        pygame.display.flip()
        
        # Cap at 60 FPS
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
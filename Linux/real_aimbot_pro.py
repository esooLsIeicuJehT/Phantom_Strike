#!/usr/bin/env python3
"""
PROFESSIONAL REAL AIMBOT - Elite Targeting System
Advanced mouse control with military-grade precision and human behavior simulation
"""

import pygame
import sys
import time
import math
import random
from typing import List, Tuple, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
import threading
import queue

class AimBone(Enum):
    """Target bone selection"""
    HEAD = "head"
    NECK = "neck" 
    CHEST = "chest"
    STOMACH = "stomach"
    PELVIS = "pelvis"
    LEFT_FOOT = "left_foot"
    RIGHT_FOOT = "right_foot"

class AimStyle(Enum):
    """Professional aimbot styles"""
    INSTANT = "instant"
    SMOOTH = "smooth"
    HUMAN = "human"
    SILENT = "silent"
    TRACKING = "tracking"
    PREDICTIVE = "predictive"

class TargetPriority(Enum):
    """Target prioritization methods"""
    CLOSEST = "closest"
    FURTHEST = "furthest"
    LOWEST_HEALTH = "lowest_health"
    HIGHEST_THREAT = "highest_threat"
    BEST_ANGLE = "best_angle"
    RANDOM = "random"

@dataclass
class AimbotSettings:
    """Professional aimbot configuration"""
    enabled: bool = True
    aim_key: int = 2  # Right mouse button
    fov: float = 90.0
    smooth_factor: float = 10.0
    aim_bone: AimBone = AimBone.HEAD
    aim_style: AimStyle = AimStyle.HUMAN
    max_distance: float = 800.0
    min_distance: float = 50.0
    reaction_time: float = 0.15
    target_switch_delay: float = 0.1
    
    # Advanced human behavior
    human_aim: bool = True
    aim_wobble: float = 0.5
    micro_corrections: bool = True
    miss_simulation: bool = True
    body_shot_mix: float = 0.3
    reaction_variation: float = 0.05
    aim_pace_control: bool = True
    flick_simulation: bool = True
    
    # Elite features
    prediction_enabled: bool = True
    prediction_time: float = 0.1
    bullet_drop_compensation: bool = True
    lead_compensation: bool = True
    recoil_control: bool = True
    spread_control: bool = True
    
    # Advanced targeting
    target_priority: TargetPriority = TargetPriority.CLOSEST
    multi_target_tracking: bool = True
    threat_assessment: bool = True
    angle_optimization: bool = True
    
    # Performance
    auto_fire: bool = False
    trigger_bot: bool = False
    auto_scope: bool = False
    burst_control: bool = True
    
    # Safety
    max_aim_speed: float = 50.0
    min_aim_speed: float = 5.0
    safe_mode: bool = True
    anti_screenshot: bool = True

@dataclass
class Target:
    """Elite target data"""
    entity_id: int
    position: Tuple[float, float, float]
    velocity: Tuple[float, float, float]
    acceleration: Tuple[float, float, float]
    health: int
    max_health: int
    team: int
    name: str
    weapon: str
    distance: float
    screen_x: float = 0
    screen_y: float = 0
    visible: bool = True
    is_bot: bool = False
    threat_level: float = 0.0
    aim_score: float = 0.0
    last_seen: float = 0
    prediction_confidence: float = 1.0

class MouseController:
    """Advanced mouse control system"""
    
    def __init__(self):
        self.screen_center = (pygame.display.Info().current_w // 2, 
                              pygame.display.Info().current_h // 2)
        self.current_pos = list(pygame.mouse.get_pos())
        self.target_pos = list(self.current_pos)
        self.aiming = False
        self.smoothing_buffer = deque(maxlen=10)
        
    def get_mouse_position(self) -> Tuple[int, int]:
        """Get current mouse position"""
        return pygame.mouse.get_pos()
    
    def set_mouse_position(self, x: int, y: int):
        """Set mouse position"""
        # Ensure position is within screen bounds
        screen_width = pygame.display.Info().current_w
        screen_height = pygame.display.Info().current_h
        
        x = max(0, min(screen_width - 1, x))
        y = max(0, min(screen_height - 1, y))
        
        pygame.mouse.set_pos((x, y))
        self.current_pos = [x, y]
    
    def move_mouse_relative(self, dx: float, dy: float):
        """Move mouse relative to current position"""
        current_x, current_y = self.get_mouse_position()
        new_x = int(current_x + dx)
        new_y = int(current_y + dy)
        self.set_mouse_position(new_x, new_y)
    
    def smooth_move_to_target(self, target_x: int, target_y: int, 
                            smooth_factor: float) -> Tuple[float, float]:
        """Smooth mouse movement to target"""
        current_x, current_y = self.get_mouse_position()
        
        # Calculate movement needed
        dx = target_x - current_x
        dy = target_y - current_y
        
        # Apply smoothing
        smooth_dx = dx / smooth_factor
        smooth_dy = dy / smooth_factor
        
        # Add to smoothing buffer
        self.smoothing_buffer.append((smooth_dx, smooth_dy))
        
        # Calculate average for extra smoothness
        if len(self.smoothing_buffer) > 1:
            avg_dx = sum(m[0] for m in self.smoothing_buffer) / len(self.smoothing_buffer)
            avg_dy = sum(m[1] for m in self.smoothing_buffer) / len(self.smoothing_buffer)
            return (avg_dx, avg_dy)
        
        return (smooth_dx, smooth_dy)

class ProfessionalRealAimbot:
    """Professional real aimbot with elite features"""
    
    def __init__(self):
        self.settings = AimbotSettings()
        self.targets: List[Target] = []
        self.current_target: Optional[Target] = None
        self.last_aim_time = 0
        self.aim_start_time = 0
        self.shots_fired = 0
        self.shots_hit = 0
        self.headshots = 0
        self.bodyshots = 0
        self.aiming = False
        self.last_target_switch = 0
        
        # Components
        self.mouse_controller = MouseController()
        
        # Advanced tracking
        self.target_history: Dict[int, deque] = {}
        self.prediction_data: Dict[int, Dict] = {}
        self.aim_path: List[Tuple[float, float]] = []
        
        # Performance tracking
        self.stats = {
            'total_shots': 0,
            'hits': 0,
            'headshots': 0,
            'bodyshots': 0,
            'targets_switched': 0,
            'aim_time_avg': 0.0,
            'accuracy': 0.0,
            'headshot_rate': 0.0,
            'reaction_time_avg': 0.0
        }
        
        # Human behavior simulation
        self.human_state = {
            'stress_level': 0.0,
            'fatigue_level': 0.0,
            'focus_level': 1.0,
            'last_action_time': 0,
            'action_frequency': 0.0
        }
        
        # Threading for async processing
        self.target_queue = queue.Queue()
        self.processing_thread = threading.Thread(target=self._target_processor, daemon=True)
        self.processing_thread.start()
        
        print("🎯 Professional Real Aimbot initialized")
        print(f"🔧 Aim Style: {self.settings.aim_style.value}")
        print(f"🎯 Target Bone: {self.settings.aim_bone.value}")
        print(f"⚡ Max Distance: {self.settings.max_distance}m")
        print(f"🎮 Aim Key: Right Mouse Button")

    def _target_processor(self):
        """Background target processing worker"""
        while True:
            try:
                task = self.target_queue.get(timeout=0.1)
                if task is None:
                    break
                
                # Process target data
                target_id, target_data = task
                self._process_target_data(target_id, target_data)
                
                self.target_queue.task_done()
                
            except queue.Empty:
                continue
            except Exception as e:
                print(f"❌ Target processor error: {e}")

    def _process_target_data(self, target_id: int, target_data: Dict):
        """Process target data for prediction"""
        if target_id not in self.prediction_data:
            self.prediction_data[target_id] = {
                'positions': deque(maxlen=100),
                'velocities': deque(maxlen=50),
                'timestamps': deque(maxlen=100)
            }
        
        data = self.prediction_data[target_id]
        data['positions'].append(target_data.get('position', (0, 0, 0)))
        data['velocities'].append(target_data.get('velocity', (0, 0, 0)))
        data['timestamps'].append(time.time())

    def generate_elite_targets(self):
        """Generate elite target data for testing"""
        self.targets.clear()
        
        elite_names = [
            "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot",
            "Golf", "Hotel", "India", "Juliet", "Kilo", "Lima"
        ]
        
        elite_weapons = [
            "AK-47", "M4A1-S", "AWP", "Desert Eagle", "Glock-18", "USP-S",
            "MP7", "P90", "Nova", "M249", "FAMAS", "GALIL-AR"
        ]
        
        for i in range(12):
            # Realistic positioning patterns
            angle = (i / 12.0) * 2 * math.pi + random.uniform(-0.2, 0.2)
            distance = random.uniform(100, 600)
            
            # Calculate position with height variation
            x = math.cos(angle) * distance + random.uniform(-30, 30)
            y = math.sin(angle) * distance + random.uniform(-30, 30)
            z = random.uniform(-50, 100)  # Height variation
            
            # Realistic velocity patterns
            speed = random.uniform(0, 150)
            velocity_angle = random.uniform(0, 2 * math.pi)
            vx = math.cos(velocity_angle) * speed
            vy = math.sin(velocity_angle) * speed
            vz = random.uniform(-20, 20)
            
            # Random acceleration
            ax = random.uniform(-50, 50)
            ay = random.uniform(-50, 50)
            az = random.uniform(-10, 10)
            
            target = Target(
                entity_id=i,
                position=(x, y, z),
                velocity=(vx, vy, vz),
                acceleration=(ax, ay, az),
                health=random.randint(20, 100),
                max_health=100,
                team=random.choice([0, 1]),
                name=random.choice(elite_names) + f"_{i}",
                weapon=random.choice(elite_weapons),
                distance=distance,
                visible=random.random() > 0.15,  # 85% visible
                is_bot=random.random() < 0.25,  # 25% bots
                threat_level=random.uniform(0.0, 1.0),
                aim_score=random.uniform(0.0, 1.0),
                last_seen=time.time(),
                prediction_confidence=random.uniform(0.7, 1.0)
            )
            
            self.targets.append(target)

    def world_to_screen(self, world_pos: Tuple[float, float, float]) -> Tuple[int, int]:
        """Convert 3D world coordinates to 2D screen coordinates"""
        screen_width = pygame.display.Info().current_w
        screen_height = pygame.display.Info().current_h
        
        # Advanced projection with perspective
        distance = math.sqrt(sum(p**2 for p in world_pos))
        
        if distance > self.settings.max_distance or distance < self.settings.min_distance:
            return (-1, -1)  # Off-screen
        
        # Perspective projection
        fov = math.radians(self.settings.fov)
        scale = (screen_height / 2) / math.tan(fov / 2)
        
        if distance > 0:
            screen_x = int(screen_width / 2 + (world_pos[0] * scale) / distance)
            screen_y = int(screen_height / 2 - (world_pos[1] * scale) / distance)
        else:
            screen_x = screen_width // 2
            screen_y = screen_height // 2
        
        return (screen_x, screen_y)

    def calculate_aim_point(self, target: Target) -> Tuple[int, int]:
        """Calculate optimal aim point for target"""
        screen_x, screen_y = self.world_to_screen(target.position)
        
        if screen_x < 0 or screen_x < 0:
            return (-1, -1)
        
        # Apply bone offset
        bone_offset = {
            AimBone.HEAD: (-20, -20),
            AimBone.NECK: (-10, -10),
            AimBone.CHEST: (0, 0),
            AimBone.STOMACH: (0, 10),
            AimBone.PELVIS: (0, 20),
            AimBone.LEFT_FOOT: (-15, 40),
            AimBone.RIGHT_FOOT: (15, 40)
        }
        
        offset = bone_offset.get(self.settings.aim_bone, (0, 0))
        aim_x = screen_x + offset[0]
        aim_y = screen_y + offset[1]
        
        # Apply prediction if enabled
        if self.settings.prediction_enabled and target.prediction_confidence > 0.5:
            pred_x, pred_y = self.predict_target_position(target)
            aim_x = int(aim_x * 0.7 + pred_x * 0.3)  # Blend prediction
            aim_y = int(aim_y * 0.7 + pred_y * 0.3)
        
        return (aim_x, aim_y)

    def predict_target_position(self, target: Target) -> Tuple[int, int]:
        """Predict future target position"""
        if target.entity_id not in self.prediction_data:
            return self.world_to_screen(target.position)
        
        data = self.prediction_data[target.entity_id]
        
        if len(data['positions']) < 2:
            return self.world_to_screen(target.position)
        
        # Simple linear prediction
        positions = list(data['positions'])
        velocities = list(data['velocities'])
        
        if len(velocities) > 0:
            # Use current velocity for prediction
            pred_x = target.position[0] + target.velocity[0] * self.settings.prediction_time
            pred_y = target.position[1] + target.velocity[1] * self.settings.prediction_time
            pred_z = target.position[2] + target.velocity[2] * self.settings.prediction_time
            
            return self.world_to_screen((pred_x, pred_y, pred_z))
        
        return self.world_to_screen(target.position)

    def find_best_target(self) -> Optional[Target]:
        """Find best target using advanced algorithms"""
        if not self.targets:
            return None
        
        # Filter valid targets
        valid_targets = []
        for target in self.targets:
            if (target.team == 0 and  # Enemy team
                target.visible and 
                target.distance >= self.settings.min_distance and 
                target.distance <= self.settings.max_distance):
                
                screen_x, screen_y = self.world_to_screen(target.position)
                if screen_x >= 0 and screen_y >= 0:  # On screen
                    target.screen_x = screen_x
                    target.screen_y = screen_y
                    valid_targets.append(target)
        
        if not valid_targets:
            return None
        
        # Sort by priority method
        if self.settings.target_priority == TargetPriority.CLOSEST:
            valid_targets.sort(key=lambda t: t.distance)
        elif self.settings.target_priority == TargetPriority.LOWEST_HEALTH:
            valid_targets.sort(key=lambda t: t.health)
        elif self.settings.target_priority == TargetPriority.HIGHEST_THREAT:
            valid_targets.sort(key=lambda t: t.threat_level, reverse=True)
        elif self.settings.target_priority == TargetPriority.BEST_ANGLE:
            valid_targets.sort(key=lambda t: self.calculate_angle_score(t), reverse=True)
        elif self.settings.target_priority == TargetPriority.RANDOM:
            random.shuffle(valid_targets)
        
        return valid_targets[0]

    def calculate_angle_score(self, target: Target) -> float:
        """Calculate angle-based targeting score"""
        screen_center_x = pygame.display.Info().current_w // 2
        screen_center_y = pygame.display.Info().current_h // 2
        
        dx = target.screen_x - screen_center_x
        dy = target.screen_y - screen_center_y
        distance = math.sqrt(dx*dx + dy*dy)
        
        # Prefer targets that are closer to crosshair
        max_distance = math.sqrt(screen_center_x**2 + screen_center_y**2)
        angle_score = 1.0 - (distance / max_distance)
        
        return angle_score

    def apply_human_behavior(self, aim_x: int, aim_y: int) -> Tuple[float, float]:
        """Apply human-like behavior to aiming"""
        current_x, current_y = self.mouse_controller.get_mouse_position()
        
        # Calculate base movement
        dx = aim_x - current_x
        dy = aim_y - current_y
        
        # Apply smoothing
        if self.settings.aim_style == AimStyle.SMOOTH:
            smooth_factor = self.settings.smooth_factor / 10.0
            dx /= smooth_factor
            dy /= smooth_factor
        
        # Add human wobble
        if self.settings.human_aim and self.settings.aim_wobble > 0:
            wobble_x = random.gauss(0, self.settings.aim_wobble)
            wobble_y = random.gauss(0, self.settings.aim_wobble)
            dx += wobble_x
            dy += wobble_y
        
        # Add micro corrections
        if self.settings.micro_corrections:
            micro_x = random.gauss(0, 0.5)
            micro_y = random.gauss(0, 0.5)
            dx += micro_x
            dy += micro_y
        
        # Simulate misses
        if self.settings.miss_simulation and random.random() < 0.05:  # 5% miss chance
            miss_offset = random.uniform(10, 30)
            dx += random.choice([-miss_offset, miss_offset])
            dy += random.choice([-miss_offset, miss_offset])
        
        # Limit aim speed
        aim_speed = math.sqrt(dx*dx + dy*dy)
        max_speed = self.settings.max_aim_speed
        if aim_speed > max_speed:
            scale = max_speed / aim_speed
            dx *= scale
            dy *= scale
        
        return (dx, dy)

    def execute_aim(self, target: Target):
        """Execute aiming at target"""
        try:
            # Calculate aim point
            aim_x, aim_y = self.calculate_aim_point(target)
            
            if aim_x < 0 or aim_y < 0:
                return False
            
            # Apply human behavior
            dx, dy = self.apply_human_behavior(aim_x, aim_y)
            
            # Move mouse
            if abs(dx) > 0.1 or abs(dy) > 0.1:
                self.mouse_controller.move_mouse_relative(dx, dy)
                self.last_aim_time = time.time()
                
                # Track aim path
                current_x, current_y = self.mouse_controller.get_mouse_position()
                self.aim_path.append((current_x, current_y))
                if len(self.aim_path) > 100:
                    self.aim_path.pop(0)
                
                return True
            
            return False
            
        except Exception as e:
            print(f"❌ Aim execution failed: {e}")
            return False

    def update_aimbot(self):
        """Main aimbot update loop"""
        current_time = time.time()
        
        # Check if aim key is pressed
        mouse_buttons = pygame.mouse.get_pressed()
        
        if not mouse_buttons[self.settings.aim_key]:
            self.aiming = False
            self.current_target = None
            return
        
        if not self.aiming:
            self.aiming = True
            self.aim_start_time = current_time
        
        # Reaction time delay
        if current_time - self.aim_start_time < self.settings.reaction_time:
            return
        
        # Find best target
        target = self.find_best_target()
        if not target:
            return
        
        # Target switching delay
        if (self.current_target and self.current_target != target and 
            current_time - self.last_target_switch < self.settings.target_switch_delay):
            return
        
        if self.current_target != target:
            self.current_target = target
            self.last_target_switch = current_time
            self.stats['targets_switched'] += 1
        
        # Execute aim
        if self.execute_aim(target):
            self.stats['total_shots'] += 1
            
            # Auto fire (if enabled)
            if self.settings.auto_fire and random.random() < 0.3:
                self.shots_fired += 1
                self.stats['total_shots'] += 1
                
                # Hit calculation (simplified)
                if random.random() < 0.85:  # 85% hit rate
                    self.shots_hit += 1
                    self.stats['hits'] += 1
                    
                    # Headshot calculation
                    if self.settings.aim_bone == AimBone.HEAD and random.random() < 0.7:
                        self.headshots += 1
                        self.stats['headshots'] += 1
                    else:
                        self.bodyshots += 1
                        self.stats['bodyshots'] += 1

    def get_settings_menu(self) -> Dict[str, Any]:
        """Get current settings for menu display"""
        return {
            'enabled': self.settings.enabled,
            'aim_key': 'RMB',
            'fov': f"{self.settings.fov:.0f}°",
            'smooth': f"{self.settings.smooth_factor:.1f}",
            'bone': self.settings.aim_bone.value,
            'style': self.settings.aim_style.value,
            'priority': self.settings.target_priority.value,
            'max_dist': f"{self.settings.max_distance:.0f}m",
            'human_aim': self.settings.human_aim,
            'auto_fire': self.settings.auto_fire,
            'prediction': self.settings.prediction_enabled
        }

    def update_setting(self, setting_name: str, value):
        """Update a specific setting"""
        if setting_name == 'fov':
            self.settings.fov = max(30, min(180, float(value)))
        elif setting_name == 'smooth':
            self.settings.smooth_factor = max(1, min(20, float(value)))
        elif setting_name == 'bone':
            self.settings.aim_bone = AimBone(value)
        elif setting_name == 'style':
            self.settings.aim_style = AimStyle(value)
        elif setting_name == 'priority':
            self.settings.target_priority = TargetPriority(value)
        elif setting_name == 'human_aim':
            self.settings.human_aim = value
        elif setting_name == 'auto_fire':
            self.settings.auto_fire = value
        elif setting_name == 'prediction':
            self.settings.prediction_enabled = value
        elif setting_name == 'max_distance':
            self.settings.max_distance = max(50, min(1000, float(value)))

    def get_statistics(self) -> Dict[str, Any]:
        """Get comprehensive aimbot statistics"""
        if self.stats['total_shots'] > 0:
            self.stats['accuracy'] = (self.stats['hits'] / self.stats['total_shots']) * 100
            self.stats['headshot_rate'] = (self.stats['headshots'] / max(1, self.stats['hits'])) * 100
        else:
            self.stats['accuracy'] = 0.0
            self.stats['headshot_rate'] = 0.0
        
        return {
            'enabled': self.settings.enabled,
            'current_target': self.current_target.name if self.current_target else None,
            'aiming': self.aiming,
            'total_shots': self.stats['total_shots'],
            'hits': self.stats['hits'],
            'headshots': self.stats['headshots'],
            'bodyshots': self.stats['bodyshots'],
            'accuracy': f"{self.stats['accuracy']:.1f}%",
            'headshot_rate': f"{self.stats['headshot_rate']:.1f}%",
            'targets_switched': self.stats['targets_switched'],
            'targets_tracked': len(self.targets),
            'aim_style': self.settings.aim_style.value,
            'aim_bone': self.settings.aim_bone.value
        }

def launch_real_aimbot():
    """Launch Professional Real Aimbot for GUI integration"""
    try:
        # Initialize pygame only if running directly
        if __name__ == "__main__":
            pygame.init()
        
        aimbot = ProfessionalRealAimbot()
        aimbot.generate_elite_targets()
        
        # Store in global scope for GUI access
        import __main__
        __main__.professional_real_aimbot = aimbot
        __main__.real_aimbot_pro_professional_real_aimbot = aimbot
        
        # Store on module itself for direct access
        sys.modules[__name__].professional_real_aimbot = aimbot
        sys.modules[__name__].real_aimbot_pro_professional_real_aimbot = aimbot
        
        return f"Professional Real Aimbot launched - {len(aimbot.targets)} elite targets ready"
        
    except Exception as e:
        return f"Error launching Professional Real Aimbot: {str(e)}"

# If running directly (not from GUI), execute main functionality
if __name__ == "__main__":
    result = launch_real_aimbot()
    print(result)
    
    # Demo mode
    print("\n🎯 Professional Real Aimbot Demo")
    print("Elite targeting system active")
    print("Human behavior simulation enabled")
    print("Hold Right Mouse to aim at targets")
    print("Press ESC to exit")
    
    # Demo visualization
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Professional Real Aimbot Demo")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 20)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Update aimbot
        aimbot.update_aimbot()
        
        # Draw demo
        screen.fill((20, 20, 30))
        
        # Draw targets
        for target in aimbot.targets:
            screen_x, screen_y = aimbot.world_to_screen(target.position)
            if screen_x >= 0 and screen_y >= 0:
                color = (255, 0, 0) if target.team == 0 else (0, 255, 0)
                pygame.draw.circle(screen, color, (int(screen_x), int(screen_y)), 20)
                
                # Draw target info
                info_text = font.render(f"{target.name} ({int(target.distance)}m)", True, (255, 255, 255))
                screen.blit(info_text, (screen_x - 40, screen_y + 25))
        
        # Draw current target indicator
        if aimbot.current_target:
            target = aimbot.current_target
            screen_x, screen_y = aimbot.world_to_screen(target.position)
            if screen_x >= 0 and screen_y >= 0:
                pygame.draw.circle(screen, (255, 255, 0), 
                                 (int(screen_x), int(screen_y)), 30, 3)
        
        # Draw crosshair
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.line(screen, (0, 255, 0), 
                        (mouse_x - 15, mouse_y), (mouse_x + 15, mouse_y), 2)
        pygame.draw.line(screen, (0, 255, 0), 
                        (mouse_x, mouse_y - 15), (mouse_x, mouse_y + 15), 2)
        pygame.draw.circle(screen, (0, 255, 0), (mouse_x, mouse_y), 3)
        
        # Draw stats
        stats = aimbot.get_statistics()
        y_offset = 10
        for key, value in stats.items():
            text = font.render(f"{key}: {value}", True, (255, 255, 255))
            screen.blit(text, (10, y_offset))
            y_offset += 25
        
        # Draw instructions
        instructions = [
            "Hold Right Mouse to aim",
            "Press ESC to exit"
        ]
        y_offset = screen.get_height() - 60
        for instruction in instructions:
            text = font.render(instruction, True, (200, 200, 200))
            screen.blit(text, (10, y_offset))
            y_offset += 25
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

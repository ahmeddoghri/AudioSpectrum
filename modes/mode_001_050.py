"""
Audio Spectrum Visualization Modes 1-50
Auto-generated from audio_spectrum_creative.py
"""
from .base import BaseModeVisualizer
import numpy as np
import cv2


class Modes001_050(BaseModeVisualizer):
    """Visualization modes 1 through 50"""

    def __init__(self, visualizer):
        super().__init__(visualizer)
        # Mode-specific state initialization will be added here
        # This ensures backward compatibility with the original code

    def draw_mode_1_vinyl_grooves(self, frame, magnitudes):
        """Mode 1: Rotating vinyl record grooves"""
        # Update rotation
        avg_magnitude = np.mean(magnitudes)
        self.rotation_angle += 0.5 + avg_magnitude * 2

        # Draw concentric grooves that pulse with music
        num_grooves = 30
        max_thickness = 4

        for groove_idx in range(num_grooves):
            groove_progress = groove_idx / num_grooves
            base_radius = int(self.max_radius * 0.3 + groove_progress * self.max_radius * 0.6)

            # Get magnitude for this groove (map to frequency bands)
            mag_idx = int(groove_progress * len(magnitudes))
            magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

            # Radius varies with music
            radius_variation = int(magnitude * 8)
            radius = base_radius + radius_variation

            # Color: warm analog colors (amber/gold)
            hue = 30 + magnitude * 20  # Amber to gold range
            saturation = 180 + int(magnitude * 75)
            value = 150 + int(magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            # Thickness varies with magnitude
            thickness = max(1, int(magnitude * max_thickness))

            # Draw groove circle
            cv2.circle(frame, (self.center_x, self.center_y), radius, color,
                      thickness, lineType=cv2.LINE_AA)

        # Draw center label (like vinyl center)
        label_radius = int(self.max_radius * 0.2)
        cv2.circle(frame, (self.center_x, self.center_y), label_radius,
                  (200, 180, 140), 2, lineType=cv2.LINE_AA)

        # Add rotating marker line (like the vinyl groove indicator)
        angle_rad = np.deg2rad(self.rotation_angle)
        line_start = int(self.max_radius * 0.25)
        line_end = int(self.max_radius * 0.9)

        x1 = int(self.center_x + line_start * np.cos(angle_rad))
        y1 = int(self.center_y + line_start * np.sin(angle_rad))
        x2 = int(self.center_x + line_end * np.cos(angle_rad))
        y2 = int(self.center_y + line_end * np.sin(angle_rad))

        cv2.line(frame, (x1, y1), (x2, y2), (180, 160, 120), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_2_neon_rain(self, frame, magnitudes):
        """Mode 2: Neon droplets cascading down (cyberpunk lofi)"""
        # Spawn new rain particles based on magnitudes
        for i, magnitude in enumerate(magnitudes):
            if magnitude > 0.3 and np.random.random() < magnitude * 0.3:
                x = int((i / len(magnitudes)) * self.width)
                y = 0
                speed = 3 + magnitude * 15
                size = 2 + int(magnitude * 8)

                # Neon colors (cyan, magenta, pink)
                color_choice = i % 3
                if color_choice == 0:
                    color = (255, 255, 0)  # Cyan
                elif color_choice == 1:
                    color = (255, 0, 255)  # Magenta
                else:
                    color = (255, 100, 200)  # Pink

                self.rain_particles.append({
                    'x': x, 'y': y, 'speed': speed,
                    'size': size, 'color': color,
                    'trail_length': int(magnitude * 50)
                })

        # Update and draw rain particles
        new_particles = []
        for particle in self.rain_particles:
            particle['y'] += particle['speed']

            # Keep if still on screen
            if particle['y'] < self.height + 20:
                # Draw particle with trail
                trail_length = particle['trail_length']
                for t in range(trail_length):
                    trail_y = int(particle['y'] - t * 2)
                    if trail_y >= 0:
                        alpha = 1.0 - (t / trail_length)
                        trail_color = tuple(int(c * alpha) for c in particle['color'])
                        cv2.circle(frame, (particle['x'], trail_y),
                                 max(1, particle['size'] - t // 3),
                                 trail_color, -1, lineType=cv2.LINE_AA)

                # Glow effect
                cv2.circle(frame, (particle['x'], int(particle['y'])),
                          particle['size'] + 3,
                          tuple(int(c * 0.3) for c in particle['color']),
                          1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.rain_particles = new_particles

        return frame


    def draw_mode_3_jazzy_fireworks(self, frame, magnitudes):
        """Mode 3: Bursting particles from center (jazz energy) - ENHANCED VERSION"""
        avg_magnitude = np.mean(magnitudes)

        # MUCH MORE AGGRESSIVE spawning - spawn constantly and much more particles
        # Spawn from center constantly
        if avg_magnitude > 0.3:  # Lower threshold so fireworks happen more often
            # Base particles - always spawn a lot
            num_particles = int(150 + avg_magnitude * 250)  # Way more particles (150-400)

            for i in range(num_particles):
                angle = np.random.random() * 2 * np.pi
                # Higher speeds to fill entire screen
                speed = 5 + np.random.random() * 15 * (avg_magnitude + 0.5)

                # Rainbow colors for jazz energy
                hue = np.random.randint(0, 180)
                color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                self.firework_particles.append({
                    'x': self.center_x,
                    'y': self.center_y,
                    'vx': np.cos(angle) * speed,
                    'vy': np.sin(angle) * speed,
                    'color': color,
                    'life': 1.0,  # Longer life
                    'size': 4 + int(avg_magnitude * 8)  # Bigger particles
                })

        # Also spawn random secondary bursts from different positions
        if avg_magnitude > 0.5 and self.frame_counter % 5 == 0:
            # Create secondary burst points
            for burst in range(3):
                burst_angle = (burst / 3) * 2 * np.pi + self.frame_counter * 0.1
                burst_distance = self.max_radius * 0.4
                burst_x = self.center_x + int(np.cos(burst_angle) * burst_distance)
                burst_y = self.center_y + int(np.sin(burst_angle) * burst_distance)

                for i in range(50):
                    angle = np.random.random() * 2 * np.pi
                    speed = 3 + np.random.random() * 10

                    hue = np.random.randint(0, 180)
                    color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
                    color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                    color = tuple(int(c) for c in color_bgr)

                    self.firework_particles.append({
                        'x': burst_x,
                        'y': burst_y,
                        'vx': np.cos(angle) * speed,
                        'vy': np.sin(angle) * speed,
                        'color': color,
                        'life': 0.8,
                        'size': 3 + int(avg_magnitude * 6)
                    })

        # Update and draw particles
        new_particles = []
        for particle in self.firework_particles:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.008  # Slower decay so particles live longer and fill screen

            # Very slight gravity
            particle['vy'] += 0.05

            if particle['life'] > 0:
                alpha = particle['life']
                particle_color = tuple(int(c * alpha) for c in particle['color'])
                size = max(1, int(particle['size'] * alpha))

                # Main particle - bigger and brighter
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          size, particle_color, -1, lineType=cv2.LINE_AA)

                # Multi-layer glow for more visibility
                if alpha > 0.3:
                    # Outer glow
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                              size + 4, tuple(int(c * 0.3 * alpha) for c in particle_color),
                              1, lineType=cv2.LINE_AA)
                    # Inner bright glow
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                              size + 2, tuple(int(c * 0.6 * alpha) for c in particle_color),
                              -1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.firework_particles = new_particles

        return frame


    def draw_mode_4_retro_cassette(self, frame, magnitudes):
        """Mode 4: VU meters and cassette tape animation - REALISTIC VERSION"""
        # Update cassette reel rotation
        avg_magnitude = np.mean(magnitudes)
        self.cassette_reel_angle += 3 + avg_magnitude * 10

        # REALISTIC CASSETTE DIMENSIONS (wider, more authentic)
        cassette_width = int(self.width * 0.65)
        cassette_height = int(self.height * 0.35)
        cassette_x = self.center_x - cassette_width // 2
        cassette_y = self.center_y - cassette_height // 2

        # === CASSETTE BODY ===
        # Main outer shell (beige/tan plastic)
        cv2.rectangle(frame, (cassette_x, cassette_y),
                     (cassette_x + cassette_width, cassette_y + cassette_height),
                     (140, 130, 110), -1, lineType=cv2.LINE_AA)

        # Border/edge
        cv2.rectangle(frame, (cassette_x, cassette_y),
                     (cassette_x + cassette_width, cassette_y + cassette_height),
                     (100, 90, 70), 3, lineType=cv2.LINE_AA)

        # === LABEL AREA (top section) ===
        label_height = int(cassette_height * 0.25)
        cv2.rectangle(frame, (cassette_x + 20, cassette_y + 15),
                     (cassette_x + cassette_width - 20, cassette_y + label_height),
                     (220, 210, 200), -1, lineType=cv2.LINE_AA)
        cv2.rectangle(frame, (cassette_x + 20, cassette_y + 15),
                     (cassette_x + cassette_width - 20, cassette_y + label_height),
                     (180, 170, 160), 1, lineType=cv2.LINE_AA)

        # === WINDOW AREA (where you see the tape) ===
        window_y = cassette_y + label_height + 25
        window_height = int(cassette_height * 0.45)
        window_margin = 40

        # Dark transparent window
        cv2.rectangle(frame, (cassette_x + window_margin, window_y),
                     (cassette_x + cassette_width - window_margin, window_y + window_height),
                     (30, 25, 20), -1, lineType=cv2.LINE_AA)
        cv2.rectangle(frame, (cassette_x + window_margin, window_y),
                     (cassette_x + cassette_width - window_margin, window_y + window_height),
                     (80, 70, 60), 2, lineType=cv2.LINE_AA)

        # === TAPE REELS (much more detailed) ===
        reel_y = window_y + window_height // 2
        reel_outer_radius = 55
        reel_inner_radius = 15
        left_reel_x = cassette_x + cassette_width // 3
        right_reel_x = cassette_x + 2 * cassette_width // 3

        for reel_x in [left_reel_x, right_reel_x]:
            # Outer reel edge (dark)
            cv2.circle(frame, (reel_x, reel_y), reel_outer_radius,
                      (50, 45, 40), 2, lineType=cv2.LINE_AA)

            # Tape on reel (brown/black magnetic tape)
            tape_radius = int(reel_outer_radius * 0.85)
            cv2.circle(frame, (reel_x, reel_y), tape_radius,
                      (20, 15, 10), -1, lineType=cv2.LINE_AA)

            # Center hub (beige plastic)
            cv2.circle(frame, (reel_x, reel_y), reel_inner_radius,
                      (140, 130, 110), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (reel_x, reel_y), reel_inner_radius,
                      (100, 90, 70), 1, lineType=cv2.LINE_AA)

            # Rotating spokes (6 spokes for realism)
            for spoke in range(6):
                angle = np.deg2rad(self.cassette_reel_angle + spoke * 60)
                x1 = int(reel_x + reel_inner_radius * np.cos(angle))
                y1 = int(reel_y + reel_inner_radius * np.sin(angle))
                x2 = int(reel_x + tape_radius * 0.9 * np.cos(angle))
                y2 = int(reel_y + tape_radius * 0.9 * np.sin(angle))
                cv2.line(frame, (x1, y1), (x2, y2), (80, 70, 60), 2, lineType=cv2.LINE_AA)

            # Center dot
            cv2.circle(frame, (reel_x, reel_y), 4, (60, 50, 40), -1, lineType=cv2.LINE_AA)

        # === TAPE BETWEEN REELS (visible magnetic tape) ===
        tape_top_y = reel_y - reel_outer_radius + 5
        tape_bottom_y = reel_y + reel_outer_radius - 5
        tape_thickness = 8

        # Top tape section
        cv2.rectangle(frame, (left_reel_x + reel_outer_radius - 5, tape_top_y - tape_thickness),
                     (right_reel_x - reel_outer_radius + 5, tape_top_y),
                     (15, 10, 8), -1, lineType=cv2.LINE_AA)

        # Bottom tape section
        cv2.rectangle(frame, (left_reel_x + reel_outer_radius - 5, tape_bottom_y),
                     (right_reel_x - reel_outer_radius + 5, tape_bottom_y + tape_thickness),
                     (15, 10, 8), -1, lineType=cv2.LINE_AA)

        # === CASSETTE SCREWS (4 corners) ===
        screw_positions = [
            (cassette_x + 25, cassette_y + 25),
            (cassette_x + cassette_width - 25, cassette_y + 25),
            (cassette_x + 25, cassette_y + cassette_height - 25),
            (cassette_x + cassette_width - 25, cassette_y + cassette_height - 25)
        ]

        for screw_x, screw_y in screw_positions:
            cv2.circle(frame, (screw_x, screw_y), 6, (80, 70, 60), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (screw_x, screw_y), 6, (60, 50, 40), 1, lineType=cv2.LINE_AA)
            # Screw cross
            cv2.line(frame, (screw_x - 3, screw_y), (screw_x + 3, screw_y),
                    (40, 30, 25), 1, lineType=cv2.LINE_AA)
            cv2.line(frame, (screw_x, screw_y - 3), (screw_x, screw_y + 3),
                    (40, 30, 25), 1, lineType=cv2.LINE_AA)

        # === BOTTOM GRIP NOTCHES (authentic detail) ===
        notch_width = 30
        notch_height = 8
        notch_spacing = 15
        notch_y = cassette_y + cassette_height - notch_height - 5

        for i in range(5):
            notch_x = cassette_x + cassette_width // 2 - 2 * notch_width - 2 * notch_spacing + i * (notch_width + notch_spacing)
            cv2.rectangle(frame, (notch_x, notch_y),
                         (notch_x + notch_width, notch_y + notch_height),
                         (90, 80, 60), -1, lineType=cv2.LINE_AA)

        # === VINTAGE VU METERS (below cassette) ===
        vu_y = cassette_y + cassette_height + 100
        vu_width = cassette_width - 200
        vu_height = 35
        vu_x = self.center_x - vu_width // 2

        # Left and right channel VU meters
        num_segments = 40
        segment_width = vu_width // num_segments

        for channel in range(2):
            channel_y = vu_y + channel * 60

            # VU meter background/frame
            frame_padding = 5
            cv2.rectangle(frame,
                         (vu_x - frame_padding, channel_y - frame_padding),
                         (vu_x + vu_width + frame_padding, channel_y + vu_height + frame_padding),
                         (100, 90, 70), -1, lineType=cv2.LINE_AA)
            cv2.rectangle(frame,
                         (vu_x - frame_padding, channel_y - frame_padding),
                         (vu_x + vu_width + frame_padding, channel_y + vu_height + frame_padding),
                         (70, 60, 50), 2, lineType=cv2.LINE_AA)

            # Get magnitude for this channel (split frequencies)
            if channel == 0:
                channel_mag = np.mean(magnitudes[:len(magnitudes)//2])
            else:
                channel_mag = np.mean(magnitudes[len(magnitudes)//2:])

            active_segments = int(channel_mag * num_segments)

            for seg in range(num_segments):
                seg_x = vu_x + seg * segment_width

                # VINTAGE COLOR GRADIENT: green -> amber -> orange -> red
                segment_progress = seg / num_segments
                if segment_progress < 0.5:
                    color = (0, 200, 50)  # Green
                elif segment_progress < 0.7:
                    color = (0, 180, 200)  # Amber/yellow
                elif segment_progress < 0.85:
                    color = (0, 120, 255)  # Orange
                else:
                    color = (0, 60, 255)  # Red

                if seg < active_segments:
                    # Active segment - full brightness with glow
                    cv2.rectangle(frame, (seg_x + 1, channel_y),
                                (seg_x + segment_width - 2, channel_y + vu_height),
                                color, -1, lineType=cv2.LINE_AA)
                else:
                    # Inactive segment - very dim
                    dim_color = tuple(int(c * 0.15) for c in color)
                    cv2.rectangle(frame, (seg_x + 2, channel_y + 2),
                                (seg_x + segment_width - 2, channel_y + vu_height - 2),
                                dim_color, -1, lineType=cv2.LINE_AA)

            # Channel label (L/R)
            label = "L" if channel == 0 else "R"
            cv2.putText(frame, label, (vu_x - 35, channel_y + vu_height - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (150, 140, 120), 2, cv2.LINE_AA)

        return frame


    def draw_mode_5_soul_aura(self, frame, magnitudes):
        """Mode 5: Pulsing organic blob (soul/RnB vibe)"""
        # Create smooth organic shape with many points
        num_points = 60
        angle_step = 360 / num_points

        points = []
        for i in range(num_points):
            angle = np.deg2rad(i * angle_step)

            # Get magnitude for this angle section
            mag_idx = int((i / num_points) * len(magnitudes))
            magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

            # Base radius with organic variation
            base_variation = np.sin(i * 0.3 + self.frame_counter * 0.05) * 30
            magnitude_variation = magnitude * 150
            radius = self.max_radius * 0.5 + base_variation + magnitude_variation

            x = int(self.center_x + radius * np.cos(angle))
            y = int(self.center_y + radius * np.sin(angle))
            points.append([x, y])

        points = np.array(points, dtype=np.int32)

        # Draw multiple layers for depth and glow
        avg_magnitude = np.mean(magnitudes)

        # Outer glow layers (purple to pink gradient)
        for layer in range(5, 0, -1):
            layer_points = []
            expansion = layer * 15

            for point in points:
                # Expand from center
                dx = point[0] - self.center_x
                dy = point[1] - self.center_y
                scale = 1.0 + (expansion / np.sqrt(dx**2 + dy**2 + 1))

                x = int(self.center_x + dx * scale)
                y = int(self.center_y + dy * scale)
                layer_points.append([x, y])

            layer_points = np.array(layer_points, dtype=np.int32)

            # Color: deep purple to pink
            hue = 140 + layer * 5 + int(avg_magnitude * 20)  # Purple-pink range
            saturation = 200 + int(avg_magnitude * 55)
            value = 100 + int(avg_magnitude * 100) - layer * 15
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            alpha = 0.3 / layer
            color = tuple(int(c * alpha) for c in color)

            cv2.fillPoly(frame, [layer_points], color, lineType=cv2.LINE_AA)

        # Main aura body
        hue = 150 + int(avg_magnitude * 30)
        saturation = 220 + int(avg_magnitude * 35)
        value = 180 + int(avg_magnitude * 75)
        color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
        color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
        main_color = tuple(int(c) for c in color_bgr)

        cv2.fillPoly(frame, [points], main_color, lineType=cv2.LINE_AA)

        # Bright outline
        cv2.polylines(frame, [points], True, (255, 200, 255), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_6_frequency_flowers(self, frame, magnitudes):
        """Mode 6: Blooming flower petals (dreamy lofi)"""
        # Create flower petals around the circle
        num_petals = min(24, len(magnitudes))
        angle_step = 360 / num_petals

        for petal_idx in range(num_petals):
            angle = np.deg2rad(petal_idx * angle_step + self.frame_counter * 0.5)

            # Get magnitude for this petal
            mag_idx = int((petal_idx / num_petals) * len(magnitudes))
            magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

            # Petal size based on magnitude
            petal_length = 50 + magnitude * 150
            petal_width = 20 + magnitude * 40

            # Petal center position
            base_radius = self.max_radius * 0.4
            petal_base_x = int(self.center_x + base_radius * np.cos(angle))
            petal_base_y = int(self.center_y + base_radius * np.sin(angle))

            # Create petal shape (ellipse)
            # Petal tip position
            petal_tip_x = int(petal_base_x + petal_length * np.cos(angle))
            petal_tip_y = int(petal_base_y + petal_length * np.sin(angle))

            # Draw petal as filled ellipse
            # Color: pastel gradient (pink, lavender, yellow)
            hue = (petal_idx * 15 + self.frame_counter) % 180
            saturation = 100 + int(magnitude * 100)
            value = 200 + int(magnitude * 55)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            petal_color = tuple(int(c) for c in color_bgr)

            # Draw petal as rotated ellipse
            axes = (int(petal_width / 2), int(petal_length / 2))
            angle_deg = int(np.rad2deg(angle))

            petal_center_x = int((petal_base_x + petal_tip_x) / 2)
            petal_center_y = int((petal_base_y + petal_tip_y) / 2)

            cv2.ellipse(frame, (petal_center_x, petal_center_y), axes,
                       angle_deg, 0, 360, petal_color, -1, lineType=cv2.LINE_AA)

            # Petal outline
            cv2.ellipse(frame, (petal_center_x, petal_center_y), axes,
                       angle_deg, 0, 360, (255, 255, 255), 1, lineType=cv2.LINE_AA)

        # Draw flower center
        avg_magnitude = np.mean(magnitudes)
        center_radius = int(30 + avg_magnitude * 50)
        cv2.circle(frame, (self.center_x, self.center_y), center_radius,
                  (50, 200, 255), -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, (self.center_x, self.center_y), center_radius,
                  (100, 220, 255), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_7_electric_heartbeat(self, frame, magnitudes):
        """Mode 7: EKG-style waveform with glow (emotional jazz)"""
        # Draw waveform across the screen like an EKG monitor
        points = []

        y_baseline = self.center_y
        waveform_width = self.width - 100
        x_start = 50

        for i, magnitude in enumerate(magnitudes):
            x = int(x_start + (i / len(magnitudes)) * waveform_width)

            # Create heartbeat-like spikes
            # Dramatic peaks for strong frequencies
            if magnitude > 0.7:
                y_offset = -int(magnitude * 300)
            else:
                y_offset = -int(magnitude * 150)

            y = int(y_baseline + y_offset)
            points.append([x, y])

        # Add smooth interpolation for organic feel
        if len(points) > 1:
            points = np.array(points, dtype=np.int32)

            # Draw glow layers
            for glow in range(5, 0, -1):
                glow_color = (0, int(255 / glow), int(255 / glow))  # Cyan glow
                thickness = glow * 3
                alpha = 0.3
                glow_color = tuple(int(c * alpha) for c in glow_color)
                cv2.polylines(frame, [points], False, glow_color,
                            thickness, lineType=cv2.LINE_AA)

            # Main line (bright cyan/electric blue)
            cv2.polylines(frame, [points], False, (255, 255, 0),
                         3, lineType=cv2.LINE_AA)

            # Add small circles at peaks
            for i, point in enumerate(points):
                if i > 0 and i < len(points) - 1:
                    if point[1] < points[i-1][1] and point[1] < points[i+1][1]:
                        # This is a peak
                        cv2.circle(frame, tuple(point), 5, (255, 255, 255), -1,
                                 lineType=cv2.LINE_AA)
                        cv2.circle(frame, tuple(point), 8, (150, 255, 255), 1,
                                 lineType=cv2.LINE_AA)

        # Draw baseline
        cv2.line(frame, (x_start, y_baseline),
                (x_start + waveform_width, y_baseline),
                (100, 100, 100), 1, lineType=cv2.LINE_AA)

        # Grid lines (like EKG paper)
        for grid_x in range(x_start, x_start + waveform_width, 50):
            cv2.line(frame, (grid_x, y_baseline - 200),
                    (grid_x, y_baseline + 100),
                    (40, 40, 40), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_8_pixel_clouds(self, frame, magnitudes):
        """Mode 8: 8-bit style floating cloud particles (retro lofi)"""
        # Spawn pixel clouds based on magnitudes
        if self.frame_counter % 5 == 0:
            for i in range(0, len(magnitudes), 3):
                magnitude = magnitudes[i]
                if magnitude > 0.3:
                    # Random spawn position
                    x = np.random.randint(0, self.width)
                    y = np.random.randint(self.height // 3, 2 * self.height // 3)

                    # Pixel block size
                    pixel_size = 8 if magnitude < 0.6 else 12

                    # Pastel 8-bit colors
                    colors = [
                        (255, 200, 200),  # Pastel pink
                        (200, 255, 200),  # Pastel green
                        (200, 200, 255),  # Pastel blue
                        (255, 255, 200),  # Pastel yellow
                        (255, 200, 255),  # Pastel magenta
                    ]
                    color = colors[i % len(colors)]

                    self.pixel_clouds.append({
                        'x': x, 'y': y,
                        'vx': np.random.uniform(-1, 1),
                        'vy': np.random.uniform(-0.5, -2),  # Float upward
                        'size': pixel_size,
                        'color': color,
                        'life': 1.0
                    })

        # Update and draw pixel clouds
        new_clouds = []
        for cloud in self.pixel_clouds:
            cloud['x'] += cloud['vx']
            cloud['y'] += cloud['vy']
            cloud['life'] -= 0.01

            if cloud['life'] > 0 and 0 <= cloud['x'] < self.width:
                alpha = cloud['life']
                cloud_color = tuple(int(c * alpha) for c in cloud['color'])

                # Draw as pixelated square (no anti-aliasing for retro look)
                x = int(cloud['x'])
                y = int(cloud['y'])
                size = cloud['size']

                cv2.rectangle(frame, (x, y), (x + size, y + size),
                            cloud_color, -1)

                # Pixel outline
                cv2.rectangle(frame, (x, y), (x + size, y + size),
                            (255, 255, 255), 1)

                new_clouds.append(cloud)

        self.pixel_clouds = new_clouds

        return frame


    def draw_mode_9_liquid_mercury(self, frame, magnitudes):
        """Mode 9: Flowing metallic waves (smooth jazz/soul)"""
        # Create flowing wave with metallic sheen
        num_wave_points = 100

        wave_points_top = []
        wave_points_bottom = []

        for i in range(num_wave_points):
            x = int((i / num_wave_points) * self.width)

            # Get magnitude for this position
            mag_idx = int((i / num_wave_points) * len(magnitudes))
            magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

            # Multiple sine waves for organic flow
            wave1 = np.sin(i * 0.1 + self.frame_counter * 0.1) * 40
            wave2 = np.sin(i * 0.05 + self.frame_counter * 0.05) * 60
            wave_offset = wave1 + wave2 + magnitude * 100

            y_top = int(self.center_y + wave_offset)
            y_bottom = int(self.center_y + wave_offset + 80 + magnitude * 100)

            wave_points_top.append([x, y_top])
            wave_points_bottom.append([x, y_bottom])

        # Combine top and reversed bottom for filled shape
        wave_points_top = np.array(wave_points_top, dtype=np.int32)
        wave_points_bottom = np.array(wave_points_bottom, dtype=np.int32)
        all_points = np.concatenate([wave_points_top, wave_points_bottom[::-1]])

        # Draw metallic gradient (silver with highlights)
        # Base layer (dark silver)
        cv2.fillPoly(frame, [all_points], (120, 120, 120), lineType=cv2.LINE_AA)

        # Highlight layer (create metallic sheen)
        for i in range(len(wave_points_top) - 1):
            # Gradient based on position
            t = i / len(wave_points_top)
            shine = int(abs(np.sin(t * np.pi * 3 + self.frame_counter * 0.1)) * 100)

            line_color = (160 + shine, 160 + shine, 160 + shine)

            cv2.line(frame, tuple(wave_points_top[i]), tuple(wave_points_top[i + 1]),
                    line_color, 3, lineType=cv2.LINE_AA)

        # Reflective highlights (white streaks)
        avg_magnitude = np.mean(magnitudes)
        if avg_magnitude > 0.5:
            for streak in range(5):
                streak_x = int((streak / 5) * self.width)
                streak_idx = int((streak / 5) * len(wave_points_top))
                if streak_idx < len(wave_points_top):
                    streak_y = wave_points_top[streak_idx][1]
                    cv2.circle(frame, (streak_x, streak_y),
                              int(8 + avg_magnitude * 15),
                              (220, 220, 220), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_10_cosmic_dust(self, frame, magnitudes):
        """Mode 10: Swirling galaxy particles with trails (ambient lofi)"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn cosmic particles
        if self.frame_counter % 2 == 0:
            for i in range(int(avg_magnitude * 20 + 10)):
                # Random angle for spiral
                angle = np.random.random() * 2 * np.pi
                distance = np.random.random() * self.max_radius * 0.3

                x = self.center_x + distance * np.cos(angle)
                y = self.center_y + distance * np.sin(angle)

                # Orbital velocity (perpendicular to radius)
                orbital_speed = 0.5 + np.random.random() * 2
                vx = -np.sin(angle) * orbital_speed
                vy = np.cos(angle) * orbital_speed

                # Colors: deep space (blues, purples, whites)
                color_choice = np.random.random()
                if color_choice < 0.3:
                    color = (255, 200, 100)  # White-gold
                elif color_choice < 0.6:
                    color = (255, 100, 100)  # Blue
                else:
                    color = (200, 100, 200)  # Purple

                self.cosmic_particles.append({
                    'x': x, 'y': y,
                    'vx': vx, 'vy': vy,
                    'color': color,
                    'life': 1.0,
                    'size': 1 + int(np.random.random() * 3),
                    'trail': []
                })

        # Update and draw particles
        new_particles = []
        for particle in self.cosmic_particles:
            # Add current position to trail
            particle['trail'].append((int(particle['x']), int(particle['y'])))
            if len(particle['trail']) > 20:
                particle['trail'].pop(0)

            # Update position (spiral motion)
            dx = particle['x'] - self.center_x
            dy = particle['y'] - self.center_y
            distance = np.sqrt(dx**2 + dy**2)

            # Spiral outward slowly
            if distance > 0:
                angle = np.arctan2(dy, dx)
                angle += 0.02  # Rotation
                distance += 0.5  # Expand outward

                particle['x'] = self.center_x + distance * np.cos(angle)
                particle['y'] = self.center_y + distance * np.sin(angle)

            particle['life'] -= 0.005

            # Keep if alive and on screen
            if particle['life'] > 0 and distance < self.max_radius * 1.2:
                alpha = particle['life']

                # Draw trail
                for trail_idx, trail_pos in enumerate(particle['trail']):
                    trail_alpha = alpha * (trail_idx / len(particle['trail']))
                    trail_color = tuple(int(c * trail_alpha) for c in particle['color'])
                    trail_size = max(1, int(particle['size'] * trail_alpha))

                    cv2.circle(frame, trail_pos, trail_size, trail_color, -1,
                             lineType=cv2.LINE_AA)

                # Draw main particle with glow
                particle_color = tuple(int(c * alpha) for c in particle['color'])
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          particle['size'] + 1,
                          tuple(int(c * 0.4) for c in particle_color),
                          -1, lineType=cv2.LINE_AA)
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          particle['size'], particle_color, -1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.cosmic_particles = new_particles

        # Draw subtle center glow
        center_radius = int(20 + avg_magnitude * 40)
        for glow_layer in range(3, 0, -1):
            glow_color = (int(80 / glow_layer), int(60 / glow_layer), int(100 / glow_layer))
            cv2.circle(frame, (self.center_x, self.center_y),
                      center_radius + glow_layer * 10, glow_color, -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_11_quantum_strings(self, frame, magnitudes):
        """Mode 11: Vibrating quantum strings with interference patterns"""
        num_strings = 12

        for string_idx in range(num_strings):
            # Each string is a horizontal line that vibrates
            y_base = int((string_idx + 1) / (num_strings + 1) * self.height)

            points = []
            for x in range(0, self.width, 5):
                # Get magnitude for this position
                mag_idx = int((x / self.width) * len(magnitudes))
                magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

                # Multiple frequency components for interference
                wave1 = np.sin(x * 0.02 + self.frame_counter * 0.15 + string_idx) * magnitude * 80
                wave2 = np.sin(x * 0.05 + self.frame_counter * 0.1) * magnitude * 40
                wave3 = np.sin(x * 0.01 + self.frame_counter * 0.2 + string_idx * 0.5) * 20

                y = int(y_base + wave1 + wave2 + wave3)
                points.append([x, y])

            if len(points) > 1:
                points = np.array(points, dtype=np.int32)

                # Color shifts through rainbow based on string and magnitude
                avg_mag = magnitudes[string_idx * len(magnitudes) // num_strings] if string_idx < num_strings else 0.5
                hue = int((string_idx / num_strings) * 180)
                saturation = 200 + int(avg_mag * 55)
                value = 150 + int(avg_mag * 105)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                # Draw glowing string
                cv2.polylines(frame, [points], False,
                            tuple(int(c * 0.4) for c in color), 4, lineType=cv2.LINE_AA)
                cv2.polylines(frame, [points], False, color, 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_12_lava_lamp(self, frame, magnitudes):
        """Mode 12: Rising and morphing lava lamp blobs"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn new blobs
        if self.frame_counter % 20 == 0 or (avg_magnitude > 0.6 and self.frame_counter % 10 == 0):
            blob_x = np.random.randint(int(self.width * 0.2), int(self.width * 0.8))
            blob_y = self.height + 50
            blob_size = 40 + int(avg_magnitude * 80)

            # Warm lava colors (red, orange, yellow)
            hue = np.random.randint(0, 30)
            self.lava_blobs.append({
                'x': blob_x,
                'y': blob_y,
                'size': blob_size,
                'speed': 0.5 + np.random.random() * 1.5,
                'wobble': np.random.random() * 2 * np.pi,
                'hue': hue,
                'life': 1.0
            })

        # Update and draw blobs
        new_blobs = []
        for blob in self.lava_blobs:
            blob['y'] -= blob['speed']
            blob['wobble'] += 0.05
            blob['life'] -= 0.002

            # Horizontal wobble
            wobble_x = np.sin(blob['wobble']) * 30
            x = int(blob['x'] + wobble_x)
            y = int(blob['y'])

            if blob['life'] > 0 and y > -100:
                # Size varies with wobble
                current_size = int(blob['size'] * (1 + np.sin(blob['wobble'] * 2) * 0.2))

                # Draw blob with multiple layers for depth
                for layer in range(3, 0, -1):
                    layer_size = int(current_size * (1 + layer * 0.2))
                    alpha = blob['life'] * (0.3 / layer)

                    saturation = 200 + int(alpha * 55)
                    value = 150 + int(alpha * 105)
                    color_hsv = np.array([[[blob['hue'], saturation, value]]], dtype=np.uint8)
                    color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                    color = tuple(int(c * alpha) for c in color_bgr)

                    cv2.circle(frame, (x, y), layer_size, color, -1, lineType=cv2.LINE_AA)

                # Bright core
                core_color = (100, 180, 255)
                cv2.circle(frame, (x, y), int(current_size * 0.6), core_color, -1, lineType=cv2.LINE_AA)

                new_blobs.append(blob)

        self.lava_blobs = new_blobs
        return frame


    def draw_mode_13_dna_helix(self, frame, magnitudes):
        """Mode 13: Double helix DNA structure"""
        self.dna_rotation += 2

        # DNA backbone parameters
        num_points = 80
        helix_radius = 100
        helix_height = self.height - 200
        center_x = self.width // 2
        start_y = 100

        strand1_points = []
        strand2_points = []
        connections = []

        for i in range(num_points):
            progress = i / num_points
            y = int(start_y + progress * helix_height)

            # Get magnitude
            mag_idx = int(progress * len(magnitudes))
            magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

            # Helix calculations
            angle1 = (progress * 4 * np.pi + np.deg2rad(self.dna_rotation))
            angle2 = angle1 + np.pi

            # Radius varies with magnitude
            current_radius = helix_radius + magnitude * 50

            x1 = int(center_x + np.cos(angle1) * current_radius)
            x2 = int(center_x + np.cos(angle2) * current_radius)

            strand1_points.append([x1, y])
            strand2_points.append([x2, y])

            # Base pair connections every few points
            if i % 5 == 0:
                connections.append(([x1, y], [x2, y], magnitude))

        # Draw base pair connections (rungs)
        for conn in connections:
            p1, p2, mag = conn
            # Color based on magnitude (cyan to purple)
            hue = 90 + int(mag * 50)
            saturation = 200 + int(mag * 55)
            value = 150 + int(mag * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            cv2.line(frame, tuple(p1), tuple(p2), color, 2, lineType=cv2.LINE_AA)

        # Draw strands
        if len(strand1_points) > 1:
            strand1_points = np.array(strand1_points, dtype=np.int32)
            strand2_points = np.array(strand2_points, dtype=np.int32)

            # Strand 1 (blue-green)
            cv2.polylines(frame, [strand1_points], False, (255, 200, 0), 5, lineType=cv2.LINE_AA)
            cv2.polylines(frame, [strand1_points], False, (255, 255, 0), 2, lineType=cv2.LINE_AA)

            # Strand 2 (red-orange)
            cv2.polylines(frame, [strand2_points], False, (100, 100, 255), 5, lineType=cv2.LINE_AA)
            cv2.polylines(frame, [strand2_points], False, (150, 150, 255), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_14_lightning_strikes(self, frame, magnitudes):
        """Mode 14: Electric lightning bolts connecting peaks - AGGRESSIVE VERSION"""
        avg_magnitude = np.mean(magnitudes)

        # Find peaks in magnitudes - MUCH LOWER THRESHOLD
        peaks = []
        for i in range(1, len(magnitudes) - 1):
            if magnitudes[i] > 0.2 and magnitudes[i] > magnitudes[i-1] and magnitudes[i] > magnitudes[i+1]:  # Lowered from 0.5 to 0.2
                x = int((i / len(magnitudes)) * self.width)
                y = int(self.height - magnitudes[i] * self.height * 0.7)
                peaks.append((x, y, magnitudes[i]))

        # Generate lightning between peaks - MUCH MORE SENSITIVE
        if avg_magnitude > 0.15 and len(peaks) >= 2:  # Lowered from 0.4 to 0.15
            for i in range(0, len(peaks) - 1):
                if np.random.random() < 0.8:  # Increased from 0.3 to 0.8 (80% chance)
                    start = peaks[i]
                    end = peaks[i + 1]

                    # Create jagged lightning path
                    lightning_points = [start[:2]]
                    num_segments = 8

                    for seg in range(1, num_segments):
                        t = seg / num_segments
                        base_x = int(start[0] + (end[0] - start[0]) * t)
                        base_y = int(start[1] + (end[1] - start[1]) * t)

                        # Add randomness
                        offset_x = np.random.randint(-30, 30)
                        offset_y = np.random.randint(-30, 30)

                        lightning_points.append([base_x + offset_x, base_y + offset_y])

                    lightning_points.append(end[:2])
                    lightning_points = np.array(lightning_points, dtype=np.int32)

                    # Draw lightning with glow
                    intensity = (start[2] + end[2]) / 2

                    # Outer glow (blue-white)
                    cv2.polylines(frame, [lightning_points], False,
                                (255, 200, 100), 8, lineType=cv2.LINE_AA)
                    # Middle layer
                    cv2.polylines(frame, [lightning_points], False,
                                (255, 240, 180), 4, lineType=cv2.LINE_AA)
                    # Bright core
                    cv2.polylines(frame, [lightning_points], False,
                                (255, 255, 255), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_15_morphing_geometry(self, frame, magnitudes):
        """Mode 15: 3D wireframe shapes that morph"""
        avg_magnitude = np.mean(magnitudes)

        # Calculate vertices for a morphing polyhedron
        num_vertices = 8
        rotation_speed = 1 + avg_magnitude * 3
        self.rotation_angle += rotation_speed

        vertices_3d = []

        # Create vertices of a cube that morphs based on magnitude
        for i in range(num_vertices):
            angle_xy = (i / num_vertices) * 2 * np.pi
            angle_z = (i / 4) * np.pi

            # Get magnitude for this vertex
            mag_idx = int((i / num_vertices) * len(magnitudes))
            magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

            # 3D coordinates with magnitude influence
            radius = 200 + magnitude * 150
            x = np.cos(angle_xy + np.deg2rad(self.rotation_angle)) * radius
            y = np.sin(angle_xy + np.deg2rad(self.rotation_angle)) * radius
            z = np.cos(angle_z + np.deg2rad(self.rotation_angle * 0.7)) * radius

            vertices_3d.append([x, y, z])

        # Project to 2D
        vertices_2d = []
        for v in vertices_3d:
            # Simple perspective projection
            scale = 400 / (400 + v[2])
            x_2d = int(self.center_x + v[0] * scale)
            y_2d = int(self.center_y + v[1] * scale)
            vertices_2d.append([x_2d, y_2d])

        # Draw edges
        edge_pairs = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4),
                     (0,4), (1,5), (2,6), (3,7)]

        for edge_idx, (i, j) in enumerate(edge_pairs):
            if i < len(vertices_2d) and j < len(vertices_2d):
                p1 = tuple(vertices_2d[i])
                p2 = tuple(vertices_2d[j])

                # Color cycles through spectrum
                hue = int((edge_idx / len(edge_pairs)) * 180 + self.frame_counter) % 180
                saturation = 220
                value = 200 + int(avg_magnitude * 55)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                cv2.line(frame, p1, p2, color, 3, lineType=cv2.LINE_AA)

        # Draw vertices as glowing dots
        for v in vertices_2d:
            cv2.circle(frame, tuple(v), 8, (255, 255, 255), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, tuple(v), 12, (150, 150, 255), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_16_ink_drops(self, frame, magnitudes):
        """Mode 16: Organic ink dispersing in water"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn ink drops
        if avg_magnitude > 0.4 and self.frame_counter % 15 == 0:
            drop_x = np.random.randint(int(self.width * 0.3), int(self.width * 0.7))
            drop_y = np.random.randint(int(self.height * 0.3), int(self.height * 0.7))

            # Spawn many particles for each drop
            for i in range(int(avg_magnitude * 150 + 50)):
                angle = np.random.random() * 2 * np.pi
                speed = np.random.random() * 3

                # Ink colors (black, dark blue, purple)
                color_choice = np.random.random()
                if color_choice < 0.4:
                    color = (180, 120, 80)  # Dark blue
                elif color_choice < 0.7:
                    color = (150, 80, 120)  # Purple
                else:
                    color = (120, 120, 120)  # Gray

                self.ink_particles.append({
                    'x': drop_x,
                    'y': drop_y,
                    'vx': np.cos(angle) * speed,
                    'vy': np.sin(angle) * speed,
                    'color': color,
                    'life': 1.0,
                    'size': 2 + int(np.random.random() * 6)
                })

        # Update and draw ink particles
        new_particles = []
        for particle in self.ink_particles:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']

            # Slow down over time (like in water)
            particle['vx'] *= 0.98
            particle['vy'] *= 0.98

            particle['life'] -= 0.005

            if particle['life'] > 0:
                alpha = particle['life']
                particle_color = tuple(int(c * alpha) for c in particle['color'])

                # Draw with organic feel
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          particle['size'], particle_color, -1, lineType=cv2.LINE_AA)

                # Slight glow
                if alpha > 0.7:
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                              particle['size'] + 2,
                              tuple(int(c * 0.3) for c in particle_color),
                              1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.ink_particles = new_particles
        return frame


    def draw_mode_17_aurora_waves(self, frame, magnitudes):
        """Mode 17: Northern lights flowing ribbons"""
        # Create flowing aurora ribbons
        num_ribbons = 5

        for ribbon_idx in range(num_ribbons):
            ribbon_y_base = int((ribbon_idx + 1) / (num_ribbons + 1) * self.height)

            points_top = []
            points_bottom = []

            for x in range(0, self.width, 8):
                mag_idx = int((x / self.width) * len(magnitudes))
                magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

                # Flowing wave motion
                wave = np.sin(x * 0.01 + self.frame_counter * 0.05 + ribbon_idx * 0.5) * 60
                wave += np.sin(x * 0.005 + self.frame_counter * 0.03) * 40
                wave += magnitude * 80

                y_top = int(ribbon_y_base + wave - 20)
                y_bottom = int(ribbon_y_base + wave + 20)

                points_top.append([x, y_top])
                points_bottom.append([x, y_bottom])

            if len(points_top) > 1:
                # Combine for filled ribbon
                points_top = np.array(points_top, dtype=np.int32)
                points_bottom = np.array(points_bottom, dtype=np.int32)
                all_points = np.concatenate([points_top, points_bottom[::-1]])

                # Aurora colors (green, blue, purple gradient)
                hue = int(100 + ribbon_idx * 15 + self.frame_counter * 0.5) % 180
                saturation = 180 + int(np.mean(magnitudes) * 75)
                value = 120 + int(np.mean(magnitudes) * 100)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * 0.6) for c in color_bgr)

                # Draw semi-transparent ribbon
                cv2.fillPoly(frame, [all_points], color, lineType=cv2.LINE_AA)

                # Bright edge
                brighter_color = tuple(int(c * 1.3) for c in color)
                cv2.polylines(frame, [points_top], False, brighter_color, 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_18_fractal_bloom(self, frame, magnitudes):
        """Mode 18: Self-similar fractal patterns"""
        avg_magnitude = np.mean(magnitudes)

        # Draw multiple layers of fractals from center
        num_layers = 6

        for layer in range(num_layers):
            num_branches = 8
            layer_progress = layer / num_layers
            base_radius = 50 + layer * 80

            for branch_idx in range(num_branches):
                angle = (branch_idx / num_branches) * 2 * np.pi + self.frame_counter * 0.02

                # Get magnitude for this branch
                mag_idx = int((branch_idx / num_branches) * len(magnitudes))
                magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

                # Branch length based on magnitude
                branch_length = base_radius + magnitude * 100

                # Start point
                start_x = self.center_x
                start_y = self.center_y

                # Draw recursive branches
                for sub_branch in range(3):
                    sub_angle = angle + (sub_branch - 1) * 0.3
                    length_scale = 1.0 - sub_branch * 0.3

                    end_x = int(start_x + np.cos(sub_angle) * branch_length * length_scale)
                    end_y = int(start_y + np.sin(sub_angle) * branch_length * length_scale)

                    # Color based on layer and magnitude
                    hue = int((layer / num_layers) * 180 + magnitude * 40)
                    saturation = 200 + int(magnitude * 55)
                    value = 150 + int(magnitude * 105)
                    color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                    color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                    color = tuple(int(c) for c in color_bgr)

                    thickness = max(1, 4 - layer)
                    cv2.line(frame, (start_x, start_y), (end_x, end_y),
                            color, thickness, lineType=cv2.LINE_AA)

                    # Draw tip glow
                    if sub_branch == 2:
                        cv2.circle(frame, (end_x, end_y),
                                 int(4 + magnitude * 6), color, -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_19_plasma_storm(self, frame, magnitudes):
        """Mode 19: Swirling plasma vortex with tendrils"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn plasma tendrils
        if self.frame_counter % 3 == 0:
            for i in range(int(avg_magnitude * 5 + 2)):
                angle = np.random.random() * 2 * np.pi
                distance = np.random.random() * 50

                tendril_x = self.center_x + np.cos(angle) * distance
                tendril_y = self.center_y + np.sin(angle) * distance

                # Spiral outward velocity
                speed = 2 + np.random.random() * 4
                vx = np.cos(angle) * speed
                vy = np.sin(angle) * speed

                # Plasma colors (purple, cyan, magenta)
                hue = np.random.choice([130, 160, 90])

                self.plasma_tendrils.append({
                    'x': tendril_x,
                    'y': tendril_y,
                    'vx': vx,
                    'vy': vy,
                    'angle': angle,
                    'hue': hue,
                    'life': 1.0,
                    'trail': []
                })

        # Update and draw tendrils
        new_tendrils = []
        for tendril in self.plasma_tendrils:
            # Add to trail
            tendril['trail'].append((int(tendril['x']), int(tendril['y'])))
            if len(tendril['trail']) > 30:
                tendril['trail'].pop(0)

            # Spiral motion
            dx = tendril['x'] - self.center_x
            dy = tendril['y'] - self.center_y
            distance = np.sqrt(dx**2 + dy**2)

            if distance > 1:
                # Add rotation to velocity
                tangent_angle = np.arctan2(dy, dx) + np.pi / 2
                tangent_speed = 2 + avg_magnitude * 3
                tendril['vx'] += np.cos(tangent_angle) * 0.3
                tendril['vy'] += np.sin(tangent_angle) * 0.3

            tendril['x'] += tendril['vx']
            tendril['y'] += tendril['vy']
            tendril['life'] -= 0.01

            if tendril['life'] > 0 and distance < self.max_radius * 1.5:
                # Draw trail
                for trail_idx in range(len(tendril['trail']) - 1):
                    if trail_idx < len(tendril['trail']) - 1:
                        p1 = tendril['trail'][trail_idx]
                        p2 = tendril['trail'][trail_idx + 1]

                        trail_alpha = (trail_idx / len(tendril['trail'])) * tendril['life']

                        saturation = 220
                        value = int(150 + trail_alpha * 105)
                        color_hsv = np.array([[[tendril['hue'], saturation, value]]], dtype=np.uint8)
                        color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                        color = tuple(int(c * trail_alpha) for c in color_bgr)

                        thickness = max(1, int(3 * trail_alpha))
                        cv2.line(frame, p1, p2, color, thickness, lineType=cv2.LINE_AA)

                new_tendrils.append(tendril)

        self.plasma_tendrils = new_tendrils

        # Draw central vortex
        vortex_radius = int(30 + avg_magnitude * 50)
        for glow in range(5, 0, -1):
            glow_color = (int(180 / glow), int(100 / glow), int(200 / glow))
            cv2.circle(frame, (self.center_x, self.center_y),
                      vortex_radius + glow * 8, glow_color, -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_20_crystal_growth(self, frame, magnitudes):
        """Mode 20: Geometric crystals forming and shattering - AGGRESSIVE VERSION"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn crystals MUCH MORE FREQUENTLY on any audio activity
        if avg_magnitude > 0.15 and self.frame_counter % 3 == 0:  # Lowered from 0.5 to 0.15, every 3 frames instead of 10
            num_crystals = 5 + int(avg_magnitude * 8)  # 5-13 crystals (was fixed at 3)
            for i in range(num_crystals):
                # Spawn across entire screen
                crystal_x = self.center_x + np.random.randint(-400, 400)
                crystal_y = self.center_y + np.random.randint(-300, 300)

                num_sides = np.random.choice([5, 6, 7, 8, 10, 12])  # More variety
                size = 30 + int(avg_magnitude * 80)  # Larger crystals

                # Crystal colors (ice blue, white, cyan, purple)
                hue = np.random.choice([90, 100, 110, 120, 130])  # More color variety

                self.crystals.append({
                    'x': crystal_x,
                    'y': crystal_y,
                    'size': size,
                    'sides': num_sides,
                    'rotation': np.random.random() * 360,
                    'growth': 0.0,
                    'hue': hue,
                    'life': 1.0
                })

        # Update and draw crystals
        new_crystals = []
        for crystal in self.crystals:
            crystal['growth'] = min(1.0, crystal['growth'] + 0.08)  # Grow faster
            crystal['rotation'] += 2  # Rotate faster
            crystal['life'] -= 0.005  # Live longer (was 0.008)

            if crystal['life'] > 0:
                current_size = int(crystal['size'] * crystal['growth'])

                # Create polygon points
                points = []
                for i in range(crystal['sides']):
                    angle = (i / crystal['sides']) * 2 * np.pi + np.deg2rad(crystal['rotation'])
                    x = int(crystal['x'] + np.cos(angle) * current_size)
                    y = int(crystal['y'] + np.sin(angle) * current_size)
                    points.append([x, y])

                points = np.array(points, dtype=np.int32)

                # Color with transparency effect
                saturation = 150 + int(crystal['life'] * 105)
                value = 200 + int(crystal['life'] * 55)
                color_hsv = np.array([[[crystal['hue'], saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * crystal['life']) for c in color_bgr)

                # Draw crystal
                cv2.fillPoly(frame, [points], tuple(int(c * 0.4) for c in color), lineType=cv2.LINE_AA)
                cv2.polylines(frame, [points], True, color, 2, lineType=cv2.LINE_AA)

                # Bright center
                cv2.circle(frame, (int(crystal['x']), int(crystal['y'])),
                          int(current_size * 0.3), (255, 255, 255), -1, lineType=cv2.LINE_AA)

                new_crystals.append(crystal)

        self.crystals = new_crystals
        return frame


    def draw_mode_21_gravitational_lens(self, frame, magnitudes):
        """Mode 21: Spacetime warping and bending light"""
        avg_magnitude = np.mean(magnitudes)

        # Create grid of light sources that get warped by "gravity"
        grid_size = 40
        for i in range(grid_size):
            for j in range(grid_size):
                # Original grid position
                x_orig = int((i / grid_size) * self.width)
                y_orig = int((j / grid_size) * self.height)

                # Calculate gravitational warping from center
                dx = x_orig - self.center_x
                dy = y_orig - self.center_y
                distance = np.sqrt(dx**2 + dy**2) + 1

                # Warp strength based on magnitude
                warp_strength = avg_magnitude * 100000 / (distance**2)

                # Warp position
                x_warped = int(x_orig - dx * warp_strength / distance)
                y_warped = int(y_orig - dy * warp_strength / distance)

                # Draw warped grid points with color based on warping
                color_intensity = min(255, int(warp_strength * 50))
                color = (color_intensity, 150, 255 - color_intensity)

                if 0 <= x_warped < self.width and 0 <= y_warped < self.height:
                    cv2.circle(frame, (x_warped, y_warped), 2, color, -1, lineType=cv2.LINE_AA)

        # Draw central "black hole" or massive object
        central_radius = int(20 + avg_magnitude * 60)
        for glow in range(5, 0, -1):
            cv2.circle(frame, (self.center_x, self.center_y),
                      central_radius + glow * 10, (50, 30, 80), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_22_magnetic_fields(self, frame, magnitudes):
        """Mode 22: Iron filing patterns flowing with music"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn magnetic particles
        if self.frame_counter % 2 == 0:
            for i in range(int(avg_magnitude * 30 + 10)):
                particle_x = np.random.randint(0, self.width)
                particle_y = np.random.randint(0, self.height)

                self.magnetic_particles.append({
                    'x': particle_x,
                    'y': particle_y,
                    'vx': 0,
                    'vy': 0,
                    'life': 1.0
                })

        # Create magnetic poles based on frequency bands
        poles = []
        for i in range(4):
            angle = (i / 4) * 2 * np.pi + self.frame_counter * 0.02
            pole_distance = 200 + magnitudes[i * len(magnitudes) // 4] * 100
            pole_x = self.center_x + np.cos(angle) * pole_distance
            pole_y = self.center_y + np.sin(angle) * pole_distance
            pole_charge = 1 if i % 2 == 0 else -1
            poles.append((pole_x, pole_y, pole_charge))

        # Update particles based on magnetic field
        new_particles = []
        for particle in self.magnetic_particles:
            # Calculate force from each pole
            for pole_x, pole_y, charge in poles:
                dx = pole_x - particle['x']
                dy = pole_y - particle['y']
                distance = np.sqrt(dx**2 + dy**2) + 1

                force = charge * 0.5 / distance
                particle['vx'] += (dx / distance) * force
                particle['vy'] += (dy / distance) * force

            # Damping
            particle['vx'] *= 0.95
            particle['vy'] *= 0.95

            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.01

            if particle['life'] > 0 and 0 <= particle['x'] < self.width and 0 <= particle['y'] < self.height:
                # Draw particle (iron filing)
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          2, (100, 100, 100), -1, lineType=cv2.LINE_AA)
                new_particles.append(particle)

        self.magnetic_particles = new_particles

        # Draw poles
        for pole_x, pole_y, charge in poles:
            color = (0, 0, 255) if charge > 0 else (255, 0, 0)
            cv2.circle(frame, (int(pole_x), int(pole_y)), 15, color, -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_23_tribal_drums(self, frame, magnitudes):
        """Mode 23: Concentric shockwaves with ethnic patterns"""
        avg_magnitude = np.mean(magnitudes)

        # Generate shockwaves on strong beats
        if avg_magnitude > 0.5 and self.frame_counter % 8 == 0:
            self.tribal_shockwaves.append({
                'radius': 0,
                'max_radius': 400,
                'life': 1.0,
                'magnitude': avg_magnitude
            })

        # Update and draw shockwaves
        new_shockwaves = []
        for wave in self.tribal_shockwaves:
            wave['radius'] += 8
            wave['life'] -= 0.02

            if wave['life'] > 0 and wave['radius'] < wave['max_radius']:
                # Draw main shockwave ring
                alpha = wave['life']
                thickness = max(1, int(5 * alpha))

                # Earthy tribal colors (oranges, browns, reds)
                hue = 10 + int(wave['magnitude'] * 20)
                saturation = 200 + int(wave['magnitude'] * 55)
                value = 150 + int(wave['magnitude'] * 105)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * alpha) for c in color_bgr)

                cv2.circle(frame, (self.center_x, self.center_y),
                          int(wave['radius']), color, thickness, lineType=cv2.LINE_AA)

                # Add tribal pattern dots around the ring
                num_dots = 16
                for i in range(num_dots):
                    angle = (i / num_dots) * 2 * np.pi
                    dot_x = int(self.center_x + wave['radius'] * np.cos(angle))
                    dot_y = int(self.center_y + wave['radius'] * np.sin(angle))
                    cv2.circle(frame, (dot_x, dot_y), int(4 * alpha), color, -1, lineType=cv2.LINE_AA)

                new_shockwaves.append(wave)

        self.tribal_shockwaves = new_shockwaves

        # Draw central drum
        drum_radius = int(40 + avg_magnitude * 30)
        cv2.circle(frame, (self.center_x, self.center_y), drum_radius,
                  (50, 80, 120), -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, (self.center_x, self.center_y), drum_radius,
                  (100, 130, 160), 3, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_24_neon_cityscape(self, frame, magnitudes):
        """Mode 24: Scrolling city skyline with reactive buildings"""
        # Initialize buildings if not done
        if len(self.cityscape_buildings) == 0:
            for i in range(40):
                self.cityscape_buildings.append({
                    'x': i * 50,
                    'width': 40 + np.random.randint(0, 30),
                    'base_height': 100 + np.random.randint(0, 300),
                    'windows': np.random.randint(3, 8)
                })

        # Scroll buildings
        for building in self.cityscape_buildings:
            building['x'] -= 2
            if building['x'] < -50:
                building['x'] = self.width + 50
                building['width'] = 40 + np.random.randint(0, 30)
                building['base_height'] = 100 + np.random.randint(0, 300)

        # Draw buildings
        for i, building in enumerate(self.cityscape_buildings):
            mag_idx = i % len(magnitudes)
            magnitude = magnitudes[mag_idx]

            # Building height reacts to music
            height = int(building['base_height'] + magnitude * 100)
            building_y = self.height - height

            # Neon colors (cyan, pink, purple)
            hue = (i * 30 + self.frame_counter) % 180
            saturation = 220 + int(magnitude * 35)
            value = 150 + int(magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            # Draw building
            cv2.rectangle(frame, (int(building['x']), building_y),
                         (int(building['x'] + building['width']), self.height),
                         color, -1, lineType=cv2.LINE_AA)

            # Draw windows
            window_rows = int(height / 20)
            for row in range(window_rows):
                for col in range(building['windows']):
                    window_x = int(building['x'] + 5 + col * (building['width'] - 10) / building['windows'])
                    window_y = building_y + 10 + row * 20
                    window_brightness = 255 if magnitude > 0.5 else 150
                    cv2.rectangle(frame, (window_x, window_y),
                                (window_x + 3, window_y + 8),
                                (window_brightness, window_brightness, 100), -1)

        return frame


    def draw_mode_25_heartbeat_monitor(self, frame, magnitudes):
        """Mode 25: Medical monitor with vital signs"""
        # Add current average magnitude to history
        avg_magnitude = np.mean(magnitudes)
        self.heartbeat_history.append(avg_magnitude)
        if len(self.heartbeat_history) > 200:
            self.heartbeat_history.pop(0)

        # Draw monitor background
        monitor_x = 50
        monitor_y = self.center_y - 150
        monitor_width = self.width - 100
        monitor_height = 300

        # Dark monitor background
        cv2.rectangle(frame, (monitor_x, monitor_y),
                     (monitor_x + monitor_width, monitor_y + monitor_height),
                     (20, 30, 20), -1, lineType=cv2.LINE_AA)
        cv2.rectangle(frame, (monitor_x, monitor_y),
                     (monitor_x + monitor_width, monitor_y + monitor_height),
                     (0, 150, 0), 2, lineType=cv2.LINE_AA)

        # Draw grid
        for i in range(0, monitor_width, 30):
            cv2.line(frame, (monitor_x + i, monitor_y),
                    (monitor_x + i, monitor_y + monitor_height),
                    (0, 50, 0), 1, lineType=cv2.LINE_AA)
        for i in range(0, monitor_height, 30):
            cv2.line(frame, (monitor_x, monitor_y + i),
                    (monitor_x + monitor_width, monitor_y + i),
                    (0, 50, 0), 1, lineType=cv2.LINE_AA)

        # Draw heartbeat waveform
        if len(self.heartbeat_history) > 1:
            points = []
            for i, mag in enumerate(self.heartbeat_history):
                x = monitor_x + int((i / len(self.heartbeat_history)) * monitor_width)

                # Create ECG-style waveform
                if mag > 0.7:
                    y_offset = -int(mag * 200)
                else:
                    y_offset = -int(mag * 80)

                y = monitor_y + monitor_height // 2 + y_offset
                points.append([x, y])

            points = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [points], False, (0, 255, 0), 2, lineType=cv2.LINE_AA)

        # Draw BPM counter
        bpm = int(60 + avg_magnitude * 100)
        cv2.putText(frame, f"BPM: {bpm}", (monitor_x + 20, monitor_y + 40),
                   cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2, cv2.LINE_AA)

        return frame


    def draw_mode_26_ocean_depths(self, frame, magnitudes):
        """Mode 26: Deep sea bioluminescent creatures"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn bioluminescent creatures
        if self.frame_counter % 10 == 0 and avg_magnitude > 0.3:
            creature_x = np.random.randint(0, self.width)
            creature_y = np.random.randint(0, self.height)

            self.bioluminescent_creatures.append({
                'x': creature_x,
                'y': creature_y,
                'vx': np.random.uniform(-2, 2),
                'vy': np.random.uniform(-1, 1),
                'size': 10 + int(avg_magnitude * 30),
                'tentacles': 5 + int(avg_magnitude * 10),
                'life': 1.0,
                'phase': np.random.random() * 2 * np.pi
            })

        # Update and draw creatures
        new_creatures = []
        for creature in self.bioluminescent_creatures:
            creature['x'] += creature['vx']
            creature['y'] += creature['vy']
            creature['phase'] += 0.1
            creature['life'] -= 0.005

            if creature['life'] > 0:
                alpha = creature['life']

                # Draw creature body (jellyfish-like)
                body_color = (255, int(150 * alpha), int(100 * alpha))
                cv2.circle(frame, (int(creature['x']), int(creature['y'])),
                          creature['size'], body_color, -1, lineType=cv2.LINE_AA)

                # Draw tentacles
                for i in range(creature['tentacles']):
                    angle = (i / creature['tentacles']) * 2 * np.pi
                    tentacle_points = []
                    for seg in range(5):
                        wave = np.sin(creature['phase'] + seg * 0.5) * 10
                        seg_x = int(creature['x'] + np.cos(angle) * wave + np.cos(angle) * seg * 8)
                        seg_y = int(creature['y'] + creature['size'] + seg * 12)
                        tentacle_points.append([seg_x, seg_y])

                    if len(tentacle_points) > 1:
                        tentacle_points = np.array(tentacle_points, dtype=np.int32)
                        tentacle_color = tuple(int(c * alpha * 0.7) for c in body_color)
                        cv2.polylines(frame, [tentacle_points], False, tentacle_color, 2, lineType=cv2.LINE_AA)

                # Glow
                cv2.circle(frame, (int(creature['x']), int(creature['y'])),
                          creature['size'] + 10, tuple(int(c * 0.3 * alpha) for c in body_color),
                          -1, lineType=cv2.LINE_AA)

                new_creatures.append(creature)

        self.bioluminescent_creatures = new_creatures
        return frame


    def draw_mode_27_fire_dance(self, frame, magnitudes):
        """Mode 27: Realistic flames dancing to rhythm"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn fire particles from bottom
        if self.frame_counter % 2 == 0:
            num_particles = int(20 + avg_magnitude * 50)
            for i in range(num_particles):
                fire_x = self.center_x + np.random.randint(-150, 150)
                fire_y = self.height - 50

                self.fire_particles.append({
                    'x': fire_x,
                    'y': fire_y,
                    'vx': np.random.uniform(-1, 1),
                    'vy': -3 - np.random.random() * avg_magnitude * 8,
                    'life': 1.0,
                    'size': 3 + int(np.random.random() * 8)
                })

        # Update and draw fire
        new_particles = []
        for particle in self.fire_particles:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['vy'] += 0.1  # Slight upward curve
            particle['vx'] += np.random.uniform(-0.2, 0.2)
            particle['life'] -= 0.015

            if particle['life'] > 0 and particle['y'] > 0:
                alpha = particle['life']

                # Fire color gradient: white -> yellow -> orange -> red -> black
                if alpha > 0.8:
                    color = (255, 255, 255)  # White hot
                elif alpha > 0.6:
                    color = (100, 255, 255)  # Yellow
                elif alpha > 0.4:
                    color = (0, 180, 255)    # Orange
                else:
                    color = (0, 50, 200)     # Deep red

                particle_color = tuple(int(c * alpha) for c in color)

                # Draw particle
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          particle['size'], particle_color, -1, lineType=cv2.LINE_AA)

                # Glow
                if alpha > 0.5:
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                              particle['size'] + 4,
                              tuple(int(c * 0.3 * alpha) for c in color),
                              -1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.fire_particles = new_particles
        return frame


    def draw_mode_28_particle_collider(self, frame, magnitudes):
        """Mode 28: High-energy physics collision visualization"""
        avg_magnitude = np.mean(magnitudes)

        # Create particle collision on strong beats
        if avg_magnitude > 0.6 and self.frame_counter % 15 == 0:
            # Spawn particles from collision at center
            num_particles = int(50 + avg_magnitude * 100)
            for i in range(num_particles):
                angle = np.random.random() * 2 * np.pi
                speed = 5 + np.random.random() * 15

                self.collision_particles.append({
                    'x': self.center_x,
                    'y': self.center_y,
                    'vx': np.cos(angle) * speed,
                    'vy': np.sin(angle) * speed,
                    'life': 1.0,
                    'charge': np.random.choice([-1, 1]),
                    'trail': []
                })

        # Update particles
        new_particles = []
        for particle in self.collision_particles:
            particle['trail'].append((int(particle['x']), int(particle['y'])))
            if len(particle['trail']) > 15:
                particle['trail'].pop(0)

            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.012

            if particle['life'] > 0:
                alpha = particle['life']

                # Color based on charge (blue for negative, red for positive)
                if particle['charge'] > 0:
                    color = (0, 100, 255)  # Red
                else:
                    color = (255, 100, 0)  # Blue

                # Draw trail
                for trail_idx in range(len(particle['trail']) - 1):
                    p1 = particle['trail'][trail_idx]
                    p2 = particle['trail'][trail_idx + 1]
                    trail_alpha = (trail_idx / len(particle['trail'])) * alpha
                    trail_color = tuple(int(c * trail_alpha) for c in color)
                    cv2.line(frame, p1, p2, trail_color, 2, lineType=cv2.LINE_AA)

                # Draw particle
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          4, tuple(int(c * alpha) for c in color), -1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.collision_particles = new_particles

        # Draw collision center with energy rings
        if avg_magnitude > 0.5:
            for ring in range(3):
                radius = int(20 + ring * 15 + avg_magnitude * 30)
                cv2.circle(frame, (self.center_x, self.center_y), radius,
                          (180, 180, 255), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_29_rainbow_prism(self, frame, magnitudes):
        """Mode 29: Light refraction through rotating prism"""
        avg_magnitude = np.mean(magnitudes)
        self.prism_rotation += 1 + avg_magnitude * 3

        # Draw prism (triangle) at center
        prism_size = 100 + int(avg_magnitude * 100)
        prism_points = []
        for i in range(3):
            angle = np.deg2rad(self.prism_rotation + i * 120)
            x = int(self.center_x + np.cos(angle) * prism_size)
            y = int(self.center_y + np.sin(angle) * prism_size)
            prism_points.append([x, y])

        prism_points = np.array(prism_points, dtype=np.int32)
        cv2.fillPoly(frame, [prism_points], (200, 200, 220), lineType=cv2.LINE_AA)
        cv2.polylines(frame, [prism_points], True, (255, 255, 255), 3, lineType=cv2.LINE_AA)

        # Draw refracted rainbow beams
        num_beams = len(magnitudes)
        for i in range(min(num_beams, 30)):
            magnitude = magnitudes[i]
            if magnitude > 0.2:
                # Beam angle based on frequency (dispersion)
                base_angle = np.deg2rad(self.prism_rotation + 60)
                angle_spread = (i / num_beams - 0.5) * 60
                beam_angle = base_angle + np.deg2rad(angle_spread)

                # Beam length based on magnitude
                beam_length = 150 + magnitude * 300

                # Start from prism edge
                start_x = self.center_x + int(np.cos(base_angle) * prism_size)
                start_y = self.center_y + int(np.sin(base_angle) * prism_size)

                end_x = int(start_x + np.cos(beam_angle) * beam_length)
                end_y = int(start_y + np.sin(beam_angle) * beam_length)

                # Rainbow color
                hue = int((i / num_beams) * 180)
                saturation = 255
                value = 200 + int(magnitude * 55)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                # Draw beam with glow
                thickness = max(2, int(magnitude * 8))
                cv2.line(frame, (start_x, start_y), (end_x, end_y),
                        tuple(int(c * 0.4) for c in color), thickness + 4, lineType=cv2.LINE_AA)
                cv2.line(frame, (start_x, start_y), (end_x, end_y),
                        color, thickness, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_30_seismic_waves(self, frame, magnitudes):
        """Mode 30: Earthquake seismograph readings"""
        # Add current magnitudes to seismic history
        avg_magnitude = np.mean(magnitudes)
        self.seismic_readings.append(magnitudes.copy())
        if len(self.seismic_readings) > 150:
            self.seismic_readings.pop(0)

        # Draw seismograph paper background
        paper_margin = 50
        cv2.rectangle(frame, (paper_margin, paper_margin),
                     (self.width - paper_margin, self.height - paper_margin),
                     (240, 235, 220), -1, lineType=cv2.LINE_AA)

        # Draw grid lines
        for i in range(paper_margin, self.width - paper_margin, 40):
            cv2.line(frame, (i, paper_margin), (i, self.height - paper_margin),
                    (200, 195, 180), 1, lineType=cv2.LINE_AA)
        for i in range(paper_margin, self.height - paper_margin, 40):
            cv2.line(frame, (paper_margin, i), (self.width - paper_margin, i),
                    (200, 195, 180), 1, lineType=cv2.LINE_AA)

        # Draw seismic waveforms (3 channels: vertical, horizontal1, horizontal2)
        if len(self.seismic_readings) > 1:
            for channel in range(3):
                channel_y = paper_margin + 100 + channel * 250

                # Draw baseline
                cv2.line(frame, (paper_margin, channel_y),
                        (self.width - paper_margin, channel_y),
                        (150, 150, 150), 1, lineType=cv2.LINE_AA)

                # Draw waveform
                points = []
                for i, reading in enumerate(self.seismic_readings):
                    x = paper_margin + int((i / len(self.seismic_readings)) * (self.width - 2 * paper_margin))

                    # Different frequency ranges for each channel
                    if channel == 0:
                        mag = np.mean(reading[:len(reading)//3])
                    elif channel == 1:
                        mag = np.mean(reading[len(reading)//3:2*len(reading)//3])
                    else:
                        mag = np.mean(reading[2*len(reading)//3:])

                    y_offset = -int(mag * 100)
                    y = channel_y + y_offset
                    points.append([x, y])

                if len(points) > 1:
                    points = np.array(points, dtype=np.int32)
                    cv2.polylines(frame, [points], False, (30, 30, 30), 2, lineType=cv2.LINE_AA)

                # Channel label
                cv2.putText(frame, f"CH{channel+1}", (paper_margin + 10, channel_y - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (80, 80, 80), 2, cv2.LINE_AA)

        # Magnitude indicator
        magnitude_scale = avg_magnitude * 10
        cv2.putText(frame, f"M{magnitude_scale:.1f}", (self.width - 150, paper_margin + 40),
                   cv2.FONT_HERSHEY_SIMPLEX, 1.5, (200, 0, 0), 3, cv2.LINE_AA)

        return frame


    def draw_mode_31_origami_unfold(self, frame, magnitudes):
        """Mode 31: Paper folding and unfolding geometrically"""
        avg_magnitude = np.mean(magnitudes)

        # Create origami crane-like shape that unfolds with music
        num_segments = 8
        for seg_idx in range(num_segments):
            angle = (seg_idx / num_segments) * 2 * np.pi + self.frame_counter * 0.02

            # Get magnitude for this segment
            mag_idx = seg_idx % len(magnitudes)
            magnitude = magnitudes[mag_idx]

            # Fold angle based on magnitude (0 = folded, 1 = unfolded)
            fold_amount = 0.3 + magnitude * 0.7

            # Draw origami segments
            base_radius = 150
            inner_radius = base_radius * (1 - fold_amount)
            outer_radius = base_radius * fold_amount

            # Create folded paper shape
            points = []
            for i in range(4):
                sub_angle = angle + (i / 4) * (np.pi / 4)
                radius = inner_radius if i % 2 == 0 else outer_radius
                x = int(self.center_x + np.cos(sub_angle) * radius)
                y = int(self.center_y + np.sin(sub_angle) * radius)
                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            # Paper color (off-white to colored based on magnitude)
            hue = int(seg_idx * 22.5) % 180
            saturation = int(magnitude * 150)
            value = 220 + int(magnitude * 35)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            cv2.fillPoly(frame, [points], color, lineType=cv2.LINE_AA)
            cv2.polylines(frame, [points], True, (180, 180, 180), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_32_storm_clouds(self, frame, magnitudes):
        """Mode 32: Thunder and lightning in swirling clouds"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn storm particles
        if self.frame_counter % 3 == 0:
            for i in range(int(avg_magnitude * 20 + 10)):
                self.storm_particles.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height // 2),
                    'vx': np.random.uniform(-2, 2),
                    'vy': np.random.uniform(0.5, 2),
                    'size': 15 + int(np.random.random() * 40),
                    'life': 1.0
                })

        # Update and draw clouds
        new_particles = []
        for cloud in self.storm_particles:
            cloud['x'] += cloud['vx']
            cloud['y'] += cloud['vy']
            cloud['life'] -= 0.008

            if cloud['life'] > 0:
                alpha = cloud['life']
                # Dark storm cloud color
                cloud_color = (int(50 * alpha), int(50 * alpha), int(60 * alpha))

                cv2.circle(frame, (int(cloud['x']), int(cloud['y'])),
                          cloud['size'], cloud_color, -1, lineType=cv2.LINE_AA)

                new_particles.append(cloud)

        self.storm_particles = new_particles

        # Lightning strikes on strong beats
        if avg_magnitude > 0.7 and np.random.random() < 0.3:
            # Random lightning bolt
            strike_x = np.random.randint(100, self.width - 100)
            strike_y_start = 50
            strike_y_end = self.height - 50

            # Jagged lightning path
            lightning_points = [[strike_x, strike_y_start]]
            current_x = strike_x
            for y in range(strike_y_start, strike_y_end, 40):
                current_x += np.random.randint(-50, 50)
                lightning_points.append([current_x, y])
            lightning_points.append([current_x, strike_y_end])

            lightning_points = np.array(lightning_points, dtype=np.int32)

            # Draw lightning with glow
            cv2.polylines(frame, [lightning_points], False, (255, 255, 200), 8, lineType=cv2.LINE_AA)
            cv2.polylines(frame, [lightning_points], False, (255, 255, 255), 3, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_33_binary_matrix(self, frame, magnitudes):
        """Mode 33: Falling Matrix-style binary code"""
        # Initialize matrix columns if needed
        if len(self.matrix_columns) == 0:
            for i in range(50):
                self.matrix_columns.append({
                    'x': i * (self.width // 50),
                    'y': np.random.randint(-500, 0),
                    'speed': 5 + np.random.randint(0, 15),
                    'length': 10 + np.random.randint(0, 30),
                    'chars': [np.random.choice(['0', '1']) for _ in range(40)]
                })

        # Update and draw columns
        for col_idx, column in enumerate(self.matrix_columns):
            mag_idx = col_idx % len(magnitudes)
            magnitude = magnitudes[mag_idx]

            # Speed influenced by magnitude
            column['y'] += column['speed'] + int(magnitude * 10)

            if column['y'] > self.height + 100:
                column['y'] = -500
                column['chars'] = [np.random.choice(['0', '1']) for _ in range(40)]

            # Draw characters
            for char_idx in range(column['length']):
                char_y = int(column['y'] + char_idx * 20)
                if 0 <= char_y < self.height:
                    # Bright green for leading edge, fading behind
                    alpha = 1.0 - (char_idx / column['length'])
                    green_value = int(255 * alpha)

                    cv2.putText(frame, column['chars'][char_idx % len(column['chars'])],
                              (column['x'], char_y),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                              (0, green_value, 0), 2, cv2.LINE_AA)

        return frame


    def draw_mode_34_kaleidoscope(self, frame, magnitudes):
        """Mode 34: Symmetric mirrored patterns"""
        avg_magnitude = np.mean(magnitudes)
        self.kaleidoscope_rotation += 0.5 + avg_magnitude * 2

        # Number of symmetry sections
        num_sections = 8
        section_angle = 360 / num_sections

        # Create base pattern in one section
        pattern_elements = []
        for i in range(min(20, len(magnitudes))):
            magnitude = magnitudes[i]
            if magnitude > 0.3:
                # Element position within one section
                angle_in_section = (i / 20) * section_angle
                radius = 100 + magnitude * 250

                pattern_elements.append({
                    'angle': angle_in_section,
                    'radius': radius,
                    'size': int(5 + magnitude * 20),
                    'hue': int((i / 20) * 180)
                })

        # Mirror pattern across all sections
        for section in range(num_sections):
            section_rotation = section * section_angle + self.kaleidoscope_rotation

            for elem in pattern_elements:
                total_angle = section_rotation + elem['angle']
                x = int(self.center_x + np.cos(np.deg2rad(total_angle)) * elem['radius'])
                y = int(self.center_y + np.sin(np.deg2rad(total_angle)) * elem['radius'])

                # Color
                saturation = 255
                value = 255
                color_hsv = np.array([[[elem['hue'], saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                cv2.circle(frame, (x, y), elem['size'], color, -1, lineType=cv2.LINE_AA)
                cv2.circle(frame, (x, y), elem['size'] + 3,
                          tuple(int(c * 0.5) for c in color), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_35_laser_show(self, frame, magnitudes):
        """Mode 35: Concert laser beams and spotlights"""
        avg_magnitude = np.mean(magnitudes)

        # Update laser beams based on frequencies
        self.laser_beams = []
        for i in range(min(12, len(magnitudes))):
            magnitude = magnitudes[i * len(magnitudes) // 12]

            if magnitude > 0.4:
                # Laser beam from bottom corners
                if i % 2 == 0:
                    start_x = 0
                    start_y = self.height
                else:
                    start_x = self.width
                    start_y = self.height

                # Beam angle based on frequency
                angle = np.deg2rad(45 + i * 10 + self.frame_counter * 2)
                beam_length = 600 + magnitude * 400

                end_x = int(start_x + np.cos(angle) * beam_length)
                end_y = int(start_y - np.sin(angle) * beam_length)

                # Laser color (various neon colors)
                hue = (i * 30 + self.frame_counter) % 180
                saturation = 255
                value = 200 + int(magnitude * 55)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                self.laser_beams.append({
                    'start': (start_x, start_y),
                    'end': (end_x, end_y),
                    'color': color,
                    'thickness': max(2, int(magnitude * 8))
                })

        # Draw laser beams
        for laser in self.laser_beams:
            # Outer glow
            cv2.line(frame, laser['start'], laser['end'],
                    tuple(int(c * 0.3) for c in laser['color']),
                    laser['thickness'] + 6, lineType=cv2.LINE_AA)
            # Main beam
            cv2.line(frame, laser['start'], laser['end'],
                    laser['color'], laser['thickness'], lineType=cv2.LINE_AA)

        # Add smoke/haze effect (particles in laser beams)
        if avg_magnitude > 0.5:
            for laser in self.laser_beams:
                for t in np.arange(0.2, 1.0, 0.15):
                    smoke_x = int(laser['start'][0] + (laser['end'][0] - laser['start'][0]) * t)
                    smoke_y = int(laser['start'][1] + (laser['end'][1] - laser['start'][1]) * t)
                    cv2.circle(frame, (smoke_x, smoke_y), 20,
                              tuple(int(c * 0.2) for c in laser['color']),
                              -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_36_sandstorm(self, frame, magnitudes):
        """Mode 36: Desert sand particles in wind vortex"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn sand particles
        if self.frame_counter % 2 == 0:
            for i in range(int(30 + avg_magnitude * 70)):
                self.sand_particles.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'vx': np.random.uniform(-5, 5),
                    'vy': np.random.uniform(-3, 3),
                    'life': 1.0,
                    'size': 1 + int(np.random.random() * 3)
                })

        # Vortex center moves with music
        vortex_x = self.center_x + int(np.sin(self.frame_counter * 0.05) * 200)
        vortex_y = self.center_y + int(np.cos(self.frame_counter * 0.03) * 100)

        # Update sand particles
        new_particles = []
        for particle in self.sand_particles:
            # Attraction to vortex
            dx = vortex_x - particle['x']
            dy = vortex_y - particle['y']
            distance = np.sqrt(dx**2 + dy**2) + 1

            # Swirling motion
            angle = np.arctan2(dy, dx) + np.pi / 2
            force = (avg_magnitude + 0.3) * 50 / distance

            particle['vx'] += np.cos(angle) * force * 0.1
            particle['vy'] += np.sin(angle) * force * 0.1

            # Wind effect
            particle['vx'] += np.sin(self.frame_counter * 0.1) * 0.5

            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.01

            # Wrap around screen
            if particle['x'] < 0:
                particle['x'] = self.width
            if particle['x'] > self.width:
                particle['x'] = 0
            if particle['y'] < 0:
                particle['y'] = self.height
            if particle['y'] > self.height:
                particle['y'] = 0

            if particle['life'] > 0:
                alpha = particle['life']
                # Sandy brown colors
                sand_color = (int(140 * alpha), int(180 * alpha), int(220 * alpha))

                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          particle['size'], sand_color, -1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.sand_particles = new_particles

        # Draw vortex center
        vortex_radius = int(20 + avg_magnitude * 40)
        for glow in range(4, 0, -1):
            cv2.circle(frame, (vortex_x, vortex_y),
                      vortex_radius + glow * 10,
                      (int(100 / glow), int(120 / glow), int(80 / glow)),
                      -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_37_ice_shatter(self, frame, magnitudes):
        """Mode 37: Cracking and breaking ice surface"""
        avg_magnitude = np.mean(magnitudes)

        # Create crack on strong beats
        if avg_magnitude > 0.6 and self.frame_counter % 20 == 0:
            # Start crack from random point
            crack_start_x = np.random.randint(200, self.width - 200)
            crack_start_y = np.random.randint(200, self.height - 200)

            crack = {
                'segments': [[crack_start_x, crack_start_y]],
                'life': 1.0,
                'branches': []
            }

            # Generate crack segments
            current_x, current_y = crack_start_x, crack_start_y
            for seg in range(10):
                angle = np.random.uniform(0, 2 * np.pi)
                length = 30 + np.random.random() * 60
                current_x += int(np.cos(angle) * length)
                current_y += int(np.sin(angle) * length)
                crack['segments'].append([current_x, current_y])

                # Random branches
                if np.random.random() < 0.4:
                    branch_angle = angle + np.random.uniform(-np.pi/2, np.pi/2)
                    branch_x = current_x
                    branch_y = current_y
                    branch_points = [[branch_x, branch_y]]
                    for b in range(3):
                        branch_x += int(np.cos(branch_angle) * 40)
                        branch_y += int(np.sin(branch_angle) * 40)
                        branch_points.append([branch_x, branch_y])
                    crack['branches'].append(branch_points)

            self.ice_cracks.append(crack)

        # Draw ice cracks
        new_cracks = []
        for crack in self.ice_cracks:
            crack['life'] -= 0.005

            if crack['life'] > 0:
                alpha = crack['life']
                crack_color = (int(200 * alpha), int(230 * alpha), int(255 * alpha))

                # Draw main crack
                if len(crack['segments']) > 1:
                    segments = np.array(crack['segments'], dtype=np.int32)
                    cv2.polylines(frame, [segments], False, crack_color, 3, lineType=cv2.LINE_AA)
                    cv2.polylines(frame, [segments], False, (255, 255, 255), 1, lineType=cv2.LINE_AA)

                # Draw branches
                for branch in crack['branches']:
                    if len(branch) > 1:
                        branch_arr = np.array(branch, dtype=np.int32)
                        cv2.polylines(frame, [branch_arr], False, crack_color, 2, lineType=cv2.LINE_AA)

                new_cracks.append(crack)

        self.ice_cracks = new_cracks

        # Ice surface shimmer
        for i in range(20):
            shimmer_x = np.random.randint(0, self.width)
            shimmer_y = np.random.randint(0, self.height)
            cv2.circle(frame, (shimmer_x, shimmer_y), 2,
                      (220, 240, 255), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_38_cellular_division(self, frame, magnitudes):
        """Mode 38: Organic cells splitting and multiplying"""
        avg_magnitude = np.mean(magnitudes)

        # Initialize cells if empty
        if len(self.cells) == 0:
            for i in range(5):
                self.cells.append({
                    'x': np.random.randint(100, self.width - 100),
                    'y': np.random.randint(100, self.height - 100),
                    'size': 40 + np.random.randint(0, 40),
                    'life': 1.0,
                    'division_timer': 0,
                    'hue': np.random.randint(0, 180)
                })

        # Update cells
        new_cells = []
        for cell in self.cells:
            cell['division_timer'] += avg_magnitude * 5
            cell['life'] -= 0.002

            # Cell division on timer
            if cell['division_timer'] > 100 and cell['life'] > 0.5 and len(self.cells) < 20:
                # Create two daughter cells
                for i in range(2):
                    angle = np.random.random() * 2 * np.pi
                    offset = 30
                    new_cells.append({
                        'x': cell['x'] + np.cos(angle) * offset,
                        'y': cell['y'] + np.sin(angle) * offset,
                        'size': cell['size'] * 0.7,
                        'life': 1.0,
                        'division_timer': 0,
                        'hue': (cell['hue'] + np.random.randint(-10, 10)) % 180
                    })
                cell['life'] = 0  # Parent cell dies

            if cell['life'] > 0:
                # Pulsing size
                pulse = 1.0 + np.sin(self.frame_counter * 0.1 + cell['x']) * 0.2
                current_size = int(cell['size'] * pulse)

                # Cell color
                saturation = 180 + int(cell['life'] * 75)
                value = 150 + int(cell['life'] * 105)
                color_hsv = np.array([[[cell['hue'], saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                # Draw cell
                cv2.circle(frame, (int(cell['x']), int(cell['y'])),
                          current_size, color, -1, lineType=cv2.LINE_AA)
                cv2.circle(frame, (int(cell['x']), int(cell['y'])),
                          current_size, tuple(int(c * 1.3) for c in color), 2, lineType=cv2.LINE_AA)

                # Nucleus
                nucleus_size = int(current_size * 0.4)
                cv2.circle(frame, (int(cell['x']), int(cell['y'])),
                          nucleus_size, tuple(int(c * 0.6) for c in color), -1, lineType=cv2.LINE_AA)

                new_cells.append(cell)

        self.cells = new_cells
        return frame


    def draw_mode_39_neon_tubes(self, frame, magnitudes):
        """Mode 39: Glowing tube shapes bending and twisting"""
        # Create neon tubes that react to music
        num_tubes = 8

        for tube_idx in range(num_tubes):
            # Get magnitude for this tube
            mag_idx = tube_idx * len(magnitudes) // num_tubes
            magnitude = magnitudes[mag_idx]

            # Tube path
            points = []
            y_start = (tube_idx + 1) / (num_tubes + 1) * self.height

            for x in range(0, self.width, 20):
                # Sinusoidal bending based on magnitude
                wave1 = np.sin(x * 0.01 + self.frame_counter * 0.05 + tube_idx) * magnitude * 60
                wave2 = np.sin(x * 0.02 + self.frame_counter * 0.03) * 30
                y = int(y_start + wave1 + wave2)
                points.append([x, y])

            if len(points) > 1:
                points = np.array(points, dtype=np.int32)

                # Neon color
                hue = (tube_idx * 25 + self.frame_counter) % 180
                saturation = 255
                value = 180 + int(magnitude * 75)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                # Tube thickness based on magnitude
                thickness = max(4, int(6 + magnitude * 12))

                # Draw glow layers
                cv2.polylines(frame, [points], False,
                            tuple(int(c * 0.3) for c in color), thickness + 8, lineType=cv2.LINE_AA)
                cv2.polylines(frame, [points], False,
                            tuple(int(c * 0.6) for c in color), thickness + 4, lineType=cv2.LINE_AA)
                cv2.polylines(frame, [points], False, color, thickness, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_40_cosmic_strings(self, frame, magnitudes):
        """Mode 40: Universe-scale energy strings vibrating"""
        avg_magnitude = np.mean(magnitudes)

        # Draw cosmic string network
        num_strings = 6

        for string_idx in range(num_strings):
            # String endpoints
            angle1 = (string_idx / num_strings) * 2 * np.pi + self.frame_counter * 0.01
            angle2 = angle1 + np.pi + 0.3

            mag_idx = string_idx % len(magnitudes)
            magnitude = magnitudes[mag_idx]

            radius = 300 + magnitude * 200

            x1 = int(self.center_x + np.cos(angle1) * radius)
            y1 = int(self.center_y + np.sin(angle1) * radius)
            x2 = int(self.center_x + np.cos(angle2) * radius)
            y2 = int(self.center_y + np.sin(angle2) * radius)

            # Create vibrating string path
            num_segments = 20
            points = []
            for seg in range(num_segments + 1):
                t = seg / num_segments
                base_x = int(x1 + (x2 - x1) * t)
                base_y = int(y1 + (y2 - y1) * t)

                # Vibration perpendicular to string
                perpendicular_angle = angle1 + np.pi / 2
                vibration = np.sin(t * np.pi * 5 + self.frame_counter * 0.2) * magnitude * 50

                vib_x = int(base_x + np.cos(perpendicular_angle) * vibration)
                vib_y = int(base_y + np.sin(perpendicular_angle) * vibration)

                points.append([vib_x, vib_y])

            points = np.array(points, dtype=np.int32)

            # Cosmic energy color (purple/blue/white)
            hue = 120 + int(magnitude * 40)
            saturation = 200 + int(magnitude * 55)
            value = 180 + int(magnitude * 75)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            # Draw string with energy glow
            cv2.polylines(frame, [points], False,
                        tuple(int(c * 0.4) for c in color), 12, lineType=cv2.LINE_AA)
            cv2.polylines(frame, [points], False, color, 4, lineType=cv2.LINE_AA)
            cv2.polylines(frame, [points], False, (255, 255, 255), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_41_paint_splatter(self, frame, magnitudes):
        """Mode 41: Jackson Pollock drip painting style"""
        avg_magnitude = np.mean(magnitudes)

        # Create paint splatters on strong beats
        if avg_magnitude > 0.4 and self.frame_counter % 5 == 0:
            for i in range(int(avg_magnitude * 15 + 5)):
                splatter_x = np.random.randint(0, self.width)
                splatter_y = np.random.randint(0, self.height)

                # Paint drips from splatter point
                num_drips = int(10 + avg_magnitude * 30)
                for drip in range(num_drips):
                    angle = np.random.random() * 2 * np.pi
                    speed = np.random.random() * 8

                    # Random vibrant colors
                    hue = np.random.randint(0, 180)

                    self.paint_splatters.append({
                        'x': splatter_x,
                        'y': splatter_y,
                        'vx': np.cos(angle) * speed,
                        'vy': np.sin(angle) * speed + 2,  # Gravity
                        'hue': hue,
                        'life': 1.0,
                        'size': 2 + int(np.random.random() * 6),
                        'trail': []
                    })

        # Update paint
        new_splatters = []
        for paint in self.paint_splatters:
            paint['trail'].append((int(paint['x']), int(paint['y'])))
            if len(paint['trail']) > 25:
                paint['trail'].pop(0)

            paint['x'] += paint['vx']
            paint['y'] += paint['vy']
            paint['vy'] += 0.3  # Gravity
            paint['life'] -= 0.015

            if paint['life'] > 0 and 0 <= paint['x'] < self.width and 0 <= paint['y'] < self.height:
                alpha = paint['life']

                saturation = 220 + int(alpha * 35)
                value = 180 + int(alpha * 75)
                color_hsv = np.array([[[paint['hue'], saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * alpha) for c in color_bgr)

                # Draw trail
                for trail_idx in range(len(paint['trail']) - 1):
                    p1 = paint['trail'][trail_idx]
                    p2 = paint['trail'][trail_idx + 1]
                    trail_alpha = (trail_idx / len(paint['trail'])) * alpha
                    trail_color = tuple(int(c * trail_alpha) for c in color)
                    cv2.line(frame, p1, p2, trail_color, paint['size'], lineType=cv2.LINE_AA)

                new_splatters.append(paint)

        self.paint_splatters = new_splatters
        return frame


    def draw_mode_42_quantum_foam(self, frame, magnitudes):
        """Mode 42: Bubbling spacetime at quantum scale"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn quantum bubbles
        if self.frame_counter % 2 == 0:
            for i in range(int(avg_magnitude * 25 + 10)):
                self.quantum_bubbles.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'size': 5 + int(np.random.random() * 25),
                    'growth': np.random.uniform(0.5, 1.5),
                    'life': 1.0,
                    'phase': np.random.random() * 2 * np.pi
                })

        # Update bubbles
        new_bubbles = []
        for bubble in self.quantum_bubbles:
            bubble['size'] *= bubble['growth']
            bubble['phase'] += 0.15
            bubble['life'] -= 0.02

            if bubble['life'] > 0 and bubble['size'] < 80:
                alpha = bubble['life']

                # Quantum color shimmer
                hue = int((bubble['phase'] * 30 + self.frame_counter) % 180)
                saturation = 200 + int(alpha * 55)
                value = 150 + int(alpha * 105)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * alpha * 0.6) for c in color_bgr)

                # Draw bubble
                cv2.circle(frame, (int(bubble['x']), int(bubble['y'])),
                          int(bubble['size']), color, 2, lineType=cv2.LINE_AA)

                # Shimmer inside
                shimmer_size = int(bubble['size'] * 0.7)
                cv2.circle(frame, (int(bubble['x']), int(bubble['y'])),
                          shimmer_size, tuple(int(c * 0.3) for c in color), -1, lineType=cv2.LINE_AA)

                new_bubbles.append(bubble)

        self.quantum_bubbles = new_bubbles
        return frame


    def draw_mode_43_aztec_sun(self, frame, magnitudes):
        """Mode 43: Ancient Aztec calendar rotating and glowing"""
        avg_magnitude = np.mean(magnitudes)
        self.aztec_rotation += 0.5 + avg_magnitude * 2

        # Draw Aztec sun stone layers
        # Outer ring with symbols
        outer_radius = 350 + int(avg_magnitude * 100)
        num_symbols = 20

        for i in range(num_symbols):
            angle = np.deg2rad(self.aztec_rotation + i * (360 / num_symbols))
            x = int(self.center_x + np.cos(angle) * outer_radius)
            y = int(self.center_y + np.sin(angle) * outer_radius)

            # Symbol blocks
            symbol_size = 15 + int(avg_magnitude * 10)
            cv2.rectangle(frame, (x - symbol_size, y - symbol_size),
                         (x + symbol_size, y + symbol_size),
                         (50, 150, 200), -1, lineType=cv2.LINE_AA)
            cv2.rectangle(frame, (x - symbol_size, y - symbol_size),
                         (x + symbol_size, y + symbol_size),
                         (100, 180, 220), 2, lineType=cv2.LINE_AA)

        # Middle ring
        mid_radius = 250
        for ring_idx in range(3):
            radius = mid_radius - ring_idx * 40
            thickness = 8 + int(avg_magnitude * 12)

            # Golden/stone color
            hue = 15 + int(avg_magnitude * 15)
            saturation = 180 + int(avg_magnitude * 75)
            value = 150 + int(avg_magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            cv2.circle(frame, (self.center_x, self.center_y), radius,
                      color, thickness, lineType=cv2.LINE_AA)

        # Center sun face
        face_radius = 80 + int(avg_magnitude * 40)
        cv2.circle(frame, (self.center_x, self.center_y), face_radius,
                  (100, 180, 220), -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, (self.center_x, self.center_y), face_radius,
                  (150, 200, 240), 3, lineType=cv2.LINE_AA)

        # Sun rays
        num_rays = 12
        for ray in range(num_rays):
            angle = np.deg2rad(ray * (360 / num_rays) + self.aztec_rotation * 0.5)
            inner_r = face_radius + 10
            outer_r = face_radius + 60 + int(avg_magnitude * 40)

            x1 = int(self.center_x + np.cos(angle) * inner_r)
            y1 = int(self.center_y + np.sin(angle) * inner_r)
            x2 = int(self.center_x + np.cos(angle) * outer_r)
            y2 = int(self.center_y + np.sin(angle) * outer_r)

            cv2.line(frame, (x1, y1), (x2, y2), (120, 190, 230), 6, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_44_fiber_optics(self, frame, magnitudes):
        """Mode 44: Light traveling through fiber cables"""
        # Create fiber optic cables
        num_fibers = 12

        for fiber_idx in range(num_fibers):
            mag_idx = fiber_idx % len(magnitudes)
            magnitude = magnitudes[mag_idx]

            # Fiber path (curved)
            points = []
            y = (fiber_idx + 1) / (num_fibers + 1) * self.height

            for x in range(0, self.width, 15):
                curve = np.sin(x * 0.005 + fiber_idx) * 80
                points.append([x, int(y + curve)])

            if len(points) > 1:
                points = np.array(points, dtype=np.int32)

                # Draw fiber cable (dark)
                cv2.polylines(frame, [points], False, (40, 40, 40), 8, lineType=cv2.LINE_AA)

                # Light pulse traveling through
                if magnitude > 0.3:
                    pulse_position = (self.frame_counter * 30 + fiber_idx * 100) % self.width
                    pulse_idx = min(int(pulse_position / 15), len(points) - 1)

                    # Fiber color
                    hue = (fiber_idx * 30) % 180
                    saturation = 255
                    value = 200 + int(magnitude * 55)
                    color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                    color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                    color = tuple(int(c) for c in color_bgr)

                    # Draw light pulse
                    pulse_length = int(10 + magnitude * 30)
                    for i in range(max(0, pulse_idx - pulse_length), min(len(points), pulse_idx + pulse_length)):
                        distance = abs(i - pulse_idx)
                        pulse_alpha = 1.0 - (distance / pulse_length)

                        pulse_color = tuple(int(c * pulse_alpha) for c in color)
                        cv2.circle(frame, tuple(points[i]), 6, pulse_color, -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_45_tornado_funnel(self, frame, magnitudes):
        """Mode 45: Swirling debris in tornado vortex"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn debris
        if self.frame_counter % 2 == 0:
            for i in range(int(avg_magnitude * 40 + 20)):
                self.tornado_debris.append({
                    'x': self.center_x + np.random.randint(-100, 100),
                    'y': self.height,
                    'angle': np.random.random() * 2 * np.pi,
                    'height': 0,
                    'rotation_speed': np.random.uniform(0.1, 0.3),
                    'radius': 50 + np.random.random() * 200,
                    'life': 1.0,
                    'size': 3 + int(np.random.random() * 8)
                })

        # Update debris
        new_debris = []
        for debris in self.tornado_debris:
            debris['angle'] += debris['rotation_speed'] + avg_magnitude * 0.1
            debris['height'] += 4 + avg_magnitude * 6
            debris['radius'] *= 0.99  # Spiral inward
            debris['life'] -= 0.008

            # Calculate position in tornado spiral
            spiral_progress = debris['height'] / self.height
            current_radius = debris['radius'] * (1 - spiral_progress * 0.7)

            x = int(self.center_x + np.cos(debris['angle']) * current_radius)
            y = int(self.height - debris['height'])

            if debris['life'] > 0 and y > 0:
                alpha = debris['life']

                # Debris color (browns, grays)
                debris_colors = [(80, 90, 100), (60, 80, 90), (100, 110, 120)]
                color = debris_colors[int(debris['angle'] * 3) % len(debris_colors)]
                debris_color = tuple(int(c * alpha) for c in color)

                cv2.circle(frame, (x, y), debris['size'], debris_color, -1, lineType=cv2.LINE_AA)

                new_debris.append(debris)

        self.tornado_debris = new_debris

        # Draw tornado funnel outline
        funnel_points = []
        for h in range(0, self.height, 20):
            progress = h / self.height
            radius = 50 + progress * 300
            angle1 = self.frame_counter * 0.05 + progress * 2

            x1 = int(self.center_x + np.cos(angle1) * radius)
            y1 = self.height - h

            funnel_points.append([x1, y1])

        if len(funnel_points) > 1:
            funnel_points = np.array(funnel_points, dtype=np.int32)
            cv2.polylines(frame, [funnel_points], False, (80, 80, 80), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_46_hologram_glitch(self, frame, magnitudes):
        """Mode 46: Futuristic holographic projection errors"""
        avg_magnitude = np.mean(magnitudes)

        # Draw holographic grid
        grid_spacing = 50
        for x in range(0, self.width, grid_spacing):
            for y in range(0, self.height, grid_spacing):
                # Glitch offset based on magnitude
                if avg_magnitude > 0.5 and np.random.random() < avg_magnitude * 0.3:
                    offset_x = np.random.randint(-20, 20)
                    offset_y = np.random.randint(-20, 20)
                else:
                    offset_x = offset_y = 0

                cv2.circle(frame, (x + offset_x, y + offset_y), 2,
                          (0, 200, 255), -1, lineType=cv2.LINE_AA)

        # Holographic frequency bars that glitch
        num_bars = min(len(magnitudes), 40)
        for i in range(num_bars):
            magnitude = magnitudes[i]
            x = int((i / num_bars) * self.width)
            bar_height = int(magnitude * self.height * 0.6)

            # Random glitch displacement
            if avg_magnitude > 0.6 and np.random.random() < 0.2:
                glitch_offset = np.random.randint(-30, 30)
                rgb_split = 15
            else:
                glitch_offset = 0
                rgb_split = 0

            # RGB channel separation (glitch effect)
            # Red channel
            cv2.rectangle(frame, (x - rgb_split + glitch_offset, self.height - bar_height),
                         (x + 3 - rgb_split + glitch_offset, self.height),
                         (0, 0, 255), -1, lineType=cv2.LINE_AA)
            # Cyan channel
            cv2.rectangle(frame, (x + rgb_split + glitch_offset, self.height - bar_height),
                         (x + 3 + rgb_split + glitch_offset, self.height),
                         (255, 255, 0), -1, lineType=cv2.LINE_AA)
            # Green (main)
            cv2.rectangle(frame, (x + glitch_offset, self.height - bar_height),
                         (x + 3 + glitch_offset, self.height),
                         (0, 255, 0), -1, lineType=cv2.LINE_AA)

        # Scanlines
        for y in range(0, self.height, 4):
            cv2.line(frame, (0, y), (self.width, y), (0, 50, 50), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_47_starfield_warp(self, frame, magnitudes):
        """Mode 47: Stars streaking during hyperspace jump"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn stars
        if len(self.stars) < 200:
            for i in range(5):
                self.stars.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'z': np.random.uniform(0.1, 1.0),
                    'trail': []
                })

        # Update stars
        warp_speed = 5 + avg_magnitude * 20

        new_stars = []
        for star in self.stars:
            # Calculate position from center
            dx = star['x'] - self.center_x
            dy = star['y'] - self.center_y

            # Move away from center (warp effect)
            distance = np.sqrt(dx**2 + dy**2) + 1
            angle = np.arctan2(dy, dx)

            star['x'] += np.cos(angle) * warp_speed / star['z']
            star['y'] += np.sin(angle) * warp_speed / star['z']

            # Add to trail
            star['trail'].append((int(star['x']), int(star['y'])))
            if len(star['trail']) > int(15 / star['z']):
                star['trail'].pop(0)

            # Reset if off screen
            if star['x'] < -100 or star['x'] > self.width + 100 or star['y'] < -100 or star['y'] > self.height + 100:
                star['x'] = self.center_x + np.random.randint(-50, 50)
                star['y'] = self.center_y + np.random.randint(-50, 50)
                star['z'] = np.random.uniform(0.1, 1.0)
                star['trail'] = []
            else:
                # Draw star trail (motion blur)
                if len(star['trail']) > 1:
                    for trail_idx in range(len(star['trail']) - 1):
                        p1 = star['trail'][trail_idx]
                        p2 = star['trail'][trail_idx + 1]
                        trail_alpha = trail_idx / len(star['trail'])

                        # Star brightness based on depth
                        brightness = int(200 * (1 - star['z']) * trail_alpha)
                        color = (brightness, brightness, brightness + 55)

                        cv2.line(frame, p1, p2, color, max(1, int(3 / star['z'])), lineType=cv2.LINE_AA)

                # Draw star
                star_size = max(1, int(4 / star['z']))
                cv2.circle(frame, (int(star['x']), int(star['y'])),
                          star_size, (255, 255, 255), -1, lineType=cv2.LINE_AA)

                new_stars.append(star)

        self.stars = new_stars
        return frame


    def draw_mode_48_mandala_growth(self, frame, magnitudes):
        """Mode 48: Sacred geometry mandala forming"""
        avg_magnitude = np.mean(magnitudes)

        # Draw mandala layers from center outward
        num_layers = 10

        for layer_idx in range(num_layers):
            layer_progress = layer_idx / num_layers
            base_radius = 50 + layer_idx * 35

            # Radius varies with music
            layer_mag = magnitudes[layer_idx % len(magnitudes)]
            radius = base_radius + layer_mag * 50

            # Number of petals/elements increases with layer
            num_elements = 6 + layer_idx * 2

            for elem_idx in range(num_elements):
                angle = (elem_idx / num_elements) * 2 * np.pi + self.frame_counter * 0.01 * (layer_idx % 2 * 2 - 1)

                # Petal position
                x = int(self.center_x + np.cos(angle) * radius)
                y = int(self.center_y + np.sin(angle) * radius)

                # Petal size
                petal_size = int(10 + layer_mag * 25)

                # Sacred geometry colors (purples, golds, cyans)
                hue = int((layer_idx * 20 + elem_idx * 10 + self.frame_counter * 0.5) % 180)
                saturation = 200 + int(layer_mag * 55)
                value = 150 + int(layer_mag * 105)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                # Draw petal/element
                cv2.circle(frame, (x, y), petal_size, color, -1, lineType=cv2.LINE_AA)
                cv2.circle(frame, (x, y), petal_size + 2,
                          tuple(int(c * 1.3) for c in color), 1, lineType=cv2.LINE_AA)

                # Connect to center with lines
                if layer_idx % 2 == 0:
                    cv2.line(frame, (self.center_x, self.center_y), (x, y),
                            tuple(int(c * 0.3) for c in color), 1, lineType=cv2.LINE_AA)

        # Central dot
        cv2.circle(frame, (self.center_x, self.center_y),
                  15 + int(avg_magnitude * 20), (255, 255, 255), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_49_neon_sign_flicker(self, frame, magnitudes):
        """Mode 49: Vintage neon signs buzzing on/off"""
        avg_magnitude = np.mean(magnitudes)

        # Draw neon text that flickers
        signs = [
            {'text': 'AUDIO', 'y': 200, 'hue': 0},
            {'text': 'SPECTRUM', 'y': 350, 'hue': 120},
            {'text': 'LIVE', 'y': 500, 'hue': 160},
            {'text': 'MUSIC', 'y': 650, 'hue': 30}
        ]

        for sign_idx, sign in enumerate(signs):
            mag_idx = sign_idx % len(magnitudes)
            magnitude = magnitudes[mag_idx]

            # Flicker effect
            if magnitude > 0.7:
                flicker = 1.0
            elif np.random.random() < 0.1:
                flicker = np.random.uniform(0.3, 1.0)
            else:
                flicker = 0.8 + magnitude * 0.2

            if flicker > 0.2:
                # Neon color
                saturation = 255
                value = int(200 * flicker + magnitude * 55)
                color_hsv = np.array([[[sign['hue'], saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * flicker) for c in color_bgr)

                # Calculate text position (centered)
                text_size = cv2.getTextSize(sign['text'], cv2.FONT_HERSHEY_DUPLEX, 3, 8)[0]
                text_x = (self.width - text_size[0]) // 2

                # Draw glow layers
                for glow in range(5, 0, -1):
                    glow_color = tuple(int(c * 0.2 * flicker / glow) for c in color)
                    cv2.putText(frame, sign['text'], (text_x, sign['y']),
                              cv2.FONT_HERSHEY_DUPLEX, 3, glow_color, 8 + glow * 2, cv2.LINE_AA)

                # Main text
                cv2.putText(frame, sign['text'], (text_x, sign['y']),
                          cv2.FONT_HERSHEY_DUPLEX, 3, color, 8, cv2.LINE_AA)

        return frame


    def draw_mode_50_black_hole(self, frame, magnitudes):
        """Mode 50: Event horizon with gravitational lensing"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn particles around black hole
        if self.frame_counter % 2 == 0:
            for i in range(int(avg_magnitude * 30 + 15)):
                angle = np.random.random() * 2 * np.pi
                distance = 400 + np.random.random() * 200

                self.black_hole_particles.append({
                    'x': self.center_x + np.cos(angle) * distance,
                    'y': self.center_y + np.sin(angle) * distance,
                    'vx': 0,
                    'vy': 0,
                    'life': 1.0,
                    'hue': int(np.random.random() * 180)
                })

        # Update particles (gravitational pull)
        event_horizon_radius = 50 + avg_magnitude * 30

        new_particles = []
        for particle in self.black_hole_particles:
            # Calculate gravity
            dx = self.center_x - particle['x']
            dy = self.center_y - particle['y']
            distance = np.sqrt(dx**2 + dy**2) + 1

            # Strong gravity near event horizon
            gravity_force = 5000 / (distance ** 2)

            particle['vx'] += (dx / distance) * gravity_force
            particle['vy'] += (dy / distance) * gravity_force

            # Orbital velocity (tangential)
            orbital_angle = np.arctan2(dy, dx) + np.pi / 2
            orbital_speed = 50 / distance
            particle['vx'] += np.cos(orbital_angle) * orbital_speed
            particle['vy'] += np.sin(orbital_angle) * orbital_speed

            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.005

            # Check if not consumed by black hole
            if distance > event_horizon_radius and particle['life'] > 0:
                alpha = min(1.0, particle['life'])

                # Redshift effect (particles shift red near event horizon)
                proximity = 1.0 - (distance / 600)
                hue_shift = int(proximity * 30)
                final_hue = (particle['hue'] - hue_shift) % 180

                saturation = 220 + int(proximity * 35)
                value = 150 + int(proximity * 105)
                color_hsv = np.array([[[final_hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * alpha) for c in color_bgr)

                # Size based on distance (gravitational lensing)
                particle_size = max(2, int(8 / (distance / 100)))

                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          particle_size, color, -1, lineType=cv2.LINE_AA)

                # Accretion disk glow
                if distance < 200:
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                              particle_size + 3,
                              tuple(int(c * 0.4) for c in color), 1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.black_hole_particles = new_particles

        # Draw event horizon (black circle)
        cv2.circle(frame, (self.center_x, self.center_y),
                  int(event_horizon_radius), (0, 0, 0), -1, lineType=cv2.LINE_AA)

        # Event horizon glow
        for glow in range(4, 0, -1):
            glow_color = (int(20 / glow), int(10 / glow), int(30 / glow))
            cv2.circle(frame, (self.center_x, self.center_y),
                      int(event_horizon_radius) + glow * 8,
                      glow_color, 2, lineType=cv2.LINE_AA)

        return frame



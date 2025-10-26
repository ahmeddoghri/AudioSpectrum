"""
Audio Spectrum Visualization Modes 151-200
Auto-generated from audio_spectrum_creative.py
"""
from .base import BaseModeVisualizer
import numpy as np
import cv2


class Modes151_200(BaseModeVisualizer):
    """Visualization modes 151 through 200"""

    def __init__(self, visualizer):
        super().__init__(visualizer)
        # Mode-specific state initialization will be added here
        # This ensures backward compatibility with the original code

    def draw_mode_151_neon_halo_burst(self, frame, magnitudes):
        """Mode 151: Circular ring whose radius pulses with kick; emits radial spikes on snare"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:len(magnitudes)//2])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Main pulsing ring
        ring_radius = int(150 + bass * 200)
        glow_intensity = int(150 + bass * 105)

        # Draw glowing ring
        for thickness in range(5, 0, -1):
            alpha = glow_intensity * (thickness / 5)
            color = (int(alpha), int(alpha * 0.5), int(alpha * 1.2))
            cv2.circle(frame, (self.center_x, self.center_y), ring_radius, color, thickness, lineType=cv2.LINE_AA)

        # Emit radial spikes on snare (mid peaks)
        if mids > 0.6:
            spike_count = int(12 + treble * 12)
            for i in range(spike_count):
                angle = (i / spike_count) * 2 * np.pi
                spike_len = int(50 + mids * 100)
                x1 = int(self.center_x + np.cos(angle) * ring_radius)
                y1 = int(self.center_y + np.sin(angle) * ring_radius)
                x2 = int(self.center_x + np.cos(angle) * (ring_radius + spike_len))
                y2 = int(self.center_y + np.sin(angle) * (ring_radius + spike_len))
                cv2.line(frame, (x1, y1), (x2, y2), (255, 200, 100), 2, lineType=cv2.LINE_AA)

        # Glittery sparks for treble
        if treble > 0.5:
            spark_count = int(treble * 30)
            for _ in range(spark_count):
                angle = np.random.random() * 2 * np.pi
                dist = ring_radius + np.random.randint(-30, 30)
                sx = int(self.center_x + np.cos(angle) * dist)
                sy = int(self.center_y + np.sin(angle) * dist)
                cv2.circle(frame, (sx, sy), 2, (255, 255, 200), -1)

        return frame


    def draw_mode_152_twin_orbiters(self, frame, magnitudes):
        """Mode 152: Two dots orbit a center with elastic distance; trails draw lissajous figure"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Orbit parameters
        orbit_radius = 150 + bass * 100
        speed = self.frame_counter * 0.05

        # First orbiter
        x1 = int(self.center_x + np.cos(speed) * orbit_radius)
        y1 = int(self.center_y + np.sin(speed * 1.3) * orbit_radius * 0.8)

        # Second orbiter
        x2 = int(self.center_x + np.cos(speed + np.pi) * orbit_radius)
        y2 = int(self.center_y + np.sin((speed + np.pi) * 1.3) * orbit_radius * 0.8)

        # Store trail
        self.twin_orbiters.append(((x1, y1), (x2, y2)))
        if len(self.twin_orbiters) > 150:
            self.twin_orbiters.pop(0)

        # Draw trails
        for i, ((tx1, ty1), (tx2, ty2)) in enumerate(self.twin_orbiters):
            alpha = int((i / len(self.twin_orbiters)) * 255)
            thickness = 1 + int(mids * 3)
            cv2.circle(frame, (tx1, ty1), 2, (alpha, 100, 200), thickness)
            cv2.circle(frame, (tx2, ty2), 2, (200, alpha, 150), thickness)

        # Draw current orbiters
        cv2.circle(frame, (x1, y1), 8, (100, 200, 255), -1)
        cv2.circle(frame, (x2, y2), 8, (255, 100, 200), -1)

        return frame


    def draw_mode_153_bar_spiral_galaxy(self, frame, magnitudes):
        """Mode 153: Bars arranged in a spiral. Each bar length follows its band"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        self.bar_spiral_rotation += 0.02 + bass * 0.05

        num_bars = min(60, len(magnitudes))
        for i in range(num_bars):
            angle = (i / num_bars) * 4 * np.pi + self.bar_spiral_rotation
            distance = 50 + i * 8
            magnitude = magnitudes[i]
            bar_length = int(20 + magnitude * 100)

            x = int(self.center_x + np.cos(angle) * distance)
            y = int(self.center_y + np.sin(angle) * distance)

            angle_perp = angle + np.pi / 2
            x1 = int(x + np.cos(angle_perp) * bar_length)
            y1 = int(y + np.sin(angle_perp) * bar_length)

            hue = int((i / num_bars) * 180)
            color_hsv = np.array([[[hue, 255, int(200 + magnitude * 55)]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.line(frame, (x, y), (x1, y1), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_154_ribbon_wave(self, frame, magnitudes):
        """Mode 154: Wide ribbon undulates like cloth; bass lifts amplitude"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        segments = 80
        points_top = []
        points_bottom = []

        for i in range(segments):
            x = int(i * self.width / segments)
            amplitude = int(50 + bass * 100)
            wave = np.sin(i * 0.3 + self.frame_counter * 0.1) * amplitude
            edge_jitter = np.random.randint(-int(treble * 10), int(treble * 10) + 1)

            y_top = int(self.center_y - 30 + wave + edge_jitter)
            y_bottom = int(self.center_y + 30 + wave - edge_jitter)

            points_top.append((x, y_top))
            points_bottom.append((x, y_bottom))

        # Draw ribbon as filled polygon
        all_points = points_top + points_bottom[::-1]
        pts = np.array(all_points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.fillPoly(frame, [pts], (150, 100, 255))

        # Edge lines with shimmer
        for i in range(1, len(points_top)):
            cv2.line(frame, points_top[i-1], points_top[i], (255, 200, 255), 2, lineType=cv2.LINE_AA)
            cv2.line(frame, points_bottom[i-1], points_bottom[i], (255, 200, 255), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_155_voxel_city(self, frame, magnitudes):
        """Mode 155: 3D grid of extruded cubes like skyline; building heights react per frequency"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        grid_size = 8
        gap = 15
        start_x = self.center_x - (grid_size * gap) // 2
        start_y = self.center_y + 200

        for i in range(grid_size):
            for j in range(grid_size):
                idx = (i * grid_size + j) % len(magnitudes)
                height = int(magnitudes[idx] * 150)

                x = start_x + j * gap
                y_base = start_y - i * gap // 2

                # Draw simple isometric cube
                top_left = (x, y_base - height)
                top_right = (x + gap, y_base - height)
                bottom_left = (x, y_base)
                bottom_right = (x + gap, y_base)

                brightness = int(100 + magnitudes[idx] * 155)
                color = (brightness // 2, brightness // 2, brightness)

                cv2.rectangle(frame, top_left, bottom_right, color, -1)
                cv2.rectangle(frame, top_left, bottom_right, (255, 255, 255), 1, lineType=cv2.LINE_AA)

        # Fog breathes on beat
        if bass > 0.6:
            fog_overlay = np.zeros_like(frame, dtype=np.uint8)
            fog_overlay[:, :] = (50, 50, 50)
            frame = cv2.addWeighted(frame, 1.0, fog_overlay, bass * 0.3, 0)

        return frame


    def draw_mode_156_sunburst_dial(self, frame, magnitudes):
        """Mode 156: 360° radial meter with ticks; ticks bend outward on mids"""
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        tick_count = 60
        inner_radius = 120
        outer_radius = 200

        for i in range(tick_count):
            angle = (i / tick_count) * 2 * np.pi
            magnitude = magnitudes[min(i * len(magnitudes) // tick_count, len(magnitudes) - 1)]

            bend_amount = mids * 50
            effective_outer = outer_radius + int(magnitude * 100) + int(bend_amount)

            x1 = int(self.center_x + np.cos(angle) * inner_radius)
            y1 = int(self.center_y + np.sin(angle) * inner_radius)
            x2 = int(self.center_x + np.cos(angle) * effective_outer)
            y2 = int(self.center_y + np.sin(angle) * effective_outer)

            # Flicker tips on highs
            color = (200, 200, 255)
            if treble > 0.6 and i % 3 == 0:
                color = (255, 255, 255)
                cv2.circle(frame, (x2, y2), 4, color, -1)

            cv2.line(frame, (x1, y1), (x2, y2), color, 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_157_waterline_oscilloscope(self, frame, magnitudes):
        """Mode 157: Horizontal waveform floats like water surface"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Generate waveform points
        points = []
        swell = int(bass * 50)

        for i in range(len(magnitudes)):
            x = int(i * self.width / len(magnitudes))
            y = int(self.center_y + swell + magnitudes[i] * 100 - 50)
            points.append((x, y))

        # Draw water surface
        for i in range(1, len(points)):
            cv2.line(frame, points[i-1], points[i], (100, 200, 255), 2, lineType=cv2.LINE_AA)

        # Spawn foam particles on highs
        if treble > 0.5 and self.frame_counter % 2 == 0:
            for _ in range(int(treble * 5)):
                idx = np.random.randint(0, len(points))
                px, py = points[idx]
                self.waterline_surface.append({'x': px, 'y': py, 'life': 20})

        # Draw foam particles
        for particle in self.waterline_surface[:]:
            particle['y'] -= 1
            particle['life'] -= 1
            if particle['life'] > 0:
                alpha = particle['life'] / 20
                cv2.circle(frame, (particle['x'], particle['y']), 2, (int(255 * alpha), int(255 * alpha), 255), -1)

        self.waterline_surface = [p for p in self.waterline_surface if p['life'] > 0]

        return frame


    def draw_mode_158_laser_tunnel(self, frame, magnitudes):
        """Mode 158: Perspective tunnel of rings; ring scale follows kick"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        ring_count = 15
        hue_shift = int(treble * 180)

        for i in range(ring_count):
            z = i / ring_count
            scale = int(50 + z * 400 + bass * 100)
            thickness = max(1, int(5 * (1 - z)))

            hue = (hue_shift + i * 12) % 180
            color_hsv = np.array([[[hue, 255, 200]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (self.center_x, self.center_y), scale, tuple(map(int, color)), thickness, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_159_vector_field_sprites(self, frame, magnitudes):
        """Mode 159: Thousands of particles follow a noise flow; velocity multiplies on mids"""
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize particles
        if len(self.vector_field_particles) < 300:
            for _ in range(300 - len(self.vector_field_particles)):
                self.vector_field_particles.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'trail': []
                })

        # Update particles
        for particle in self.vector_field_particles:
            noise_x = np.sin(particle['x'] * 0.01 + self.frame_counter * 0.05) * (1 + mids * 2)
            noise_y = np.cos(particle['y'] * 0.01 + self.frame_counter * 0.05) * (1 + mids * 2)

            particle['x'] += noise_x
            particle['y'] += noise_y

            # Wrap around
            particle['x'] = particle['x'] % self.width
            particle['y'] = particle['y'] % self.height

            # Trail
            trail_length = int(5 + treble * 15)
            particle['trail'].append((int(particle['x']), int(particle['y'])))
            if len(particle['trail']) > trail_length:
                particle['trail'].pop(0)

            # Draw trail
            for i in range(1, len(particle['trail'])):
                alpha = int((i / len(particle['trail'])) * 255)
                cv2.line(frame, particle['trail'][i-1], particle['trail'][i], (alpha, alpha // 2, 255), 1)

        return frame


    def draw_mode_160_orbit_rings_meter(self, frame, magnitudes):
        """Mode 160: Nested orbits with dots; each ring maps to a band"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        ring_count = min(10, len(magnitudes) // 12)

        for i in range(ring_count):
            idx = i * (len(magnitudes) // ring_count)
            magnitude = magnitudes[idx]

            radius = 50 + i * 40
            eccentricity = magnitude * 0.5
            dot_size = int(5 + magnitude * 15)

            angle = self.frame_counter * 0.05 * (i + 1)
            x = int(self.center_x + np.cos(angle) * radius * (1 + eccentricity))
            y = int(self.center_y + np.sin(angle) * radius * (1 - eccentricity))

            # Draw orbit path
            cv2.ellipse(frame, (self.center_x, self.center_y), (int(radius * (1 + eccentricity)), int(radius * (1 - eccentricity))), 0, 0, 360, (100, 100, 150), 1, lineType=cv2.LINE_AA)

            # Draw dot
            hue = int((i / ring_count) * 180)
            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            cv2.circle(frame, (x, y), dot_size, tuple(map(int, color)), -1)

        return frame


    def draw_mode_161_stitch_bars(self, frame, magnitudes):
        """Mode 161: Stacked micro-bars like embroidered stitches"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        rows = 8
        cols = min(60, len(magnitudes))
        gap = self.width // (cols + 1)
        row_height = 15

        for row in range(rows):
            y = 100 + row * row_height
            for col in range(cols):
                x = gap * (col + 1)
                magnitude = magnitudes[col]
                density = int(magnitude * 10)

                # Wobble on beat
                wobble = int(np.sin(self.frame_counter * 0.1 + col * 0.5) * bass * 10)

                for d in range(density):
                    y_stitch = y + d * 2 + wobble
                    cv2.line(frame, (x - 3, y_stitch), (x + 3, y_stitch), (200, 150, 255), 1)

        return frame


    def draw_mode_162_aurora_curtain(self, frame, magnitudes):
        """Mode 162: Vertical curtains waving; bass widens curtain"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        curtain_count = 5

        for c in range(curtain_count):
            x_base = (c + 1) * self.width // (curtain_count + 1)
            width_mult = 1 + bass * 0.5

            points = []
            for y in range(0, self.height, 10):
                curl = int(np.sin(y * 0.05 + self.frame_counter * 0.1 + c) * mids * 30)
                x = int(x_base + curl * width_mult)
                points.append((x, y))

            # Draw curtain
            hue = int((c / curtain_count) * 180)
            color_hsv = np.array([[[hue, 200, 200]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            for i in range(1, len(points)):
                cv2.line(frame, points[i-1], points[i], tuple(map(int, color)), 3, lineType=cv2.LINE_AA)

        # Star-like flickers
        if treble > 0.6:
            for _ in range(int(treble * 10)):
                sx = np.random.randint(0, self.width)
                sy = np.random.randint(0, self.height)
                cv2.circle(frame, (sx, sy), 2, (255, 255, 200), -1)

        return frame


    def draw_mode_163_helix_bars_3d(self, frame, magnitudes):
        """Mode 163: Two helical rails of bars spinning"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        self.helix_bars_state += 0.05 + bass * 0.1

        bar_count = min(50, len(magnitudes))
        turns = 3

        for i in range(bar_count):
            t = i / bar_count
            angle = t * turns * 2 * np.pi + self.helix_bars_state

            x = int(self.center_x + np.cos(angle) * 150)
            y = int(100 + t * (self.height - 200))

            magnitude = magnitudes[i]
            bar_length = int(magnitude * 80)

            x1 = x - bar_length // 2
            x2 = x + bar_length // 2

            brightness = int(100 + magnitude * 155)
            color = (brightness, brightness // 2, brightness)

            cv2.line(frame, (x1, y), (x2, y), color, 3, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_164_polygon_heartbeat(self, frame, magnitudes):
        """Mode 164: Regular polygon in the center inflates on kicks"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        sides = 6
        scale = 100 + int(bass * 150)

        points = []
        for i in range(sides):
            angle = (i / sides) * 2 * np.pi
            x = int(self.center_x + np.cos(angle) * scale)
            y = int(self.center_y + np.sin(angle) * scale)
            points.append((x, y))

        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (255, 150, 150), 3, lineType=cv2.LINE_AA)

        # Concentric echo waves
        if bass > 0.5:
            for echo in range(1, 4):
                echo_scale = scale + echo * 30
                echo_points = []
                for i in range(sides):
                    angle = (i / sides) * 2 * np.pi
                    x = int(self.center_x + np.cos(angle) * echo_scale)
                    y = int(self.center_y + np.sin(angle) * echo_scale)
                    echo_points.append((x, y))

                echo_pts = np.array(echo_points, np.int32)
                echo_pts = echo_pts.reshape((-1, 1, 2))
                alpha = int(150 / echo)
                cv2.polylines(frame, [echo_pts], True, (alpha, alpha // 2, alpha // 2), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_165_confetti_impulse(self, frame, magnitudes):
        """Mode 165: On peaks, spawn confetti bursts"""
        peak_threshold = 0.7

        # Check for peaks
        for i, mag in enumerate(magnitudes):
            if mag > peak_threshold and np.random.random() < 0.1:
                # Spawn confetti
                hue = int((i / len(magnitudes)) * 180)
                for _ in range(20):
                    self.confetti_particles.append({
                        'x': self.center_x + np.random.randint(-50, 50),
                        'y': self.center_y + np.random.randint(-50, 50),
                        'vx': np.random.uniform(-5, 5),
                        'vy': np.random.uniform(-10, -2),
                        'hue': hue,
                        'life': 60
                    })

        # Update and draw confetti
        for particle in self.confetti_particles[:]:
            particle['vy'] += 0.3  # Gravity
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['vx'] *= 0.98  # Air drag
            particle['life'] -= 1

            if particle['life'] > 0:
                color_hsv = np.array([[[particle['hue'], 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                cv2.circle(frame, (int(particle['x']), int(particle['y'])), 3, tuple(map(int, color)), -1)

        self.confetti_particles = [p for p in self.confetti_particles if p['life'] > 0 and 0 <= p['y'] < self.height]

        return frame


    def draw_mode_166_wireframe_dome(self, frame, magnitudes):
        """Mode 166: Hemispherical mesh; vertices displace along normals"""
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        segments = 12

        for lat in range(segments // 2):
            for lon in range(segments):
                theta = (lat / (segments / 2)) * np.pi / 2
                phi = (lon / segments) * 2 * np.pi

                idx = (lat * segments + lon) % len(magnitudes)
                offset = int(magnitudes[idx] * 50)

                r = 200 + offset
                x = int(self.center_x + r * np.sin(theta) * np.cos(phi))
                y = int(self.center_y + 200 - r * np.cos(theta))
                z = int(r * np.sin(theta) * np.sin(phi))

                # Simple 3D to 2D projection
                x_2d = x + z // 2
                y_2d = y - z // 4

                if lat < segments // 2 - 1:
                    theta2 = ((lat + 1) / (segments / 2)) * np.pi / 2
                    r2 = 200 + int(magnitudes[((lat + 1) * segments + lon) % len(magnitudes)] * 50)
                    x2 = int(self.center_x + r2 * np.sin(theta2) * np.cos(phi))
                    y2 = int(self.center_y + 200 - r2 * np.cos(theta2))
                    z2 = int(r2 * np.sin(theta2) * np.sin(phi))
                    x2_2d = x2 + z2 // 2
                    y2_2d = y2 - z2 // 4

                    cv2.line(frame, (x_2d, y_2d), (x2_2d, y2_2d), (100, 150, 255), 1, lineType=cv2.LINE_AA)

                # Specular sparkle on highs
                if treble > 0.6 and idx % 3 == 0:
                    cv2.circle(frame, (x_2d, y_2d), 3, (255, 255, 255), -1)

        return frame


    def draw_mode_167_pulse_dashes(self, frame, magnitudes):
        """Mode 167: Circular dashed stroke; dash length oscillates with mids"""
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        dash_count = 60
        radius = 200
        dash_base_len = 20 + int(mids * 40)

        for i in range(dash_count):
            angle_start = (i / dash_count) * 2 * np.pi
            angle_end = angle_start + (dash_base_len / radius)

            x1 = int(self.center_x + np.cos(angle_start) * radius)
            y1 = int(self.center_y + np.sin(angle_start) * radius)
            x2 = int(self.center_x + np.cos(angle_end) * radius)
            y2 = int(self.center_y + np.sin(angle_end) * radius)

            # Tip glow on treble
            glow = 200
            if treble > 0.5 and i % 2 == 0:
                glow = 255
                cv2.circle(frame, (x2, y2), 5, (255, 255, 255), -1)

            cv2.line(frame, (x1, y1), (x2, y2), (glow, glow // 2, 255), 3, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_168_terrain_sweep(self, frame, magnitudes):
        """Mode 168: Scrolling heightmap like synthwave hills"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        row_count = 15

        # Shift existing rows
        for row in self.terrain_sweep_rows:
            row['y'] += 5

        # Remove off-screen rows
        self.terrain_sweep_rows = [r for r in self.terrain_sweep_rows if r['y'] < self.height]

        # Add new row
        if len(self.terrain_sweep_rows) < row_count:
            profile = [magnitudes[i % len(magnitudes)] for i in range(self.width // 10)]
            self.terrain_sweep_rows.insert(0, {'y': 0, 'profile': profile})

        # Draw terrain
        for row_idx, row in enumerate(self.terrain_sweep_rows):
            y_base = row['y']
            profile = row['profile']

            points = []
            for i, height in enumerate(profile):
                x = i * 10
                y = int(y_base + 200 - height * 150 - row_idx * 5)
                points.append((x, y))

            # Draw line
            for i in range(1, len(points)):
                hue = int((height / 1.0) * 180)
                color_hsv = np.array([[[hue, 255, 200]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                cv2.line(frame, points[i-1], points[i], tuple(map(int, color)), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_169_chromatic_bars_mirror(self, frame, magnitudes):
        """Mode 169: Mirrored bars with central symmetry; hue rotates"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        hue_offset = (self.frame_counter * 2) % 180
        bar_count = min(60, len(magnitudes))
        gap = 3
        bar_width = (self.width // 2) // bar_count - gap

        # Flash on kick
        if bass > 0.7 and self.frame_counter % 10 == 0:
            self.chromatic_bars_flash = 10

        flash_add = 0
        if self.chromatic_bars_flash > 0:
            flash_add = self.chromatic_bars_flash * 20
            self.chromatic_bars_flash -= 1

        for i in range(bar_count):
            magnitude = magnitudes[i]
            height = int(magnitude * (self.height // 2))

            x_left = self.center_x - i * (bar_width + gap) - bar_width
            x_right = self.center_x + i * (bar_width + gap)

            hue = (hue_offset + i * 3) % 180
            color_hsv = np.array([[[hue, 255, min(255, 200 + flash_add)]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Left bar
            cv2.rectangle(frame, (x_left, self.center_y - height), (x_left + bar_width, self.center_y), tuple(map(int, color)), -1)
            # Right bar
            cv2.rectangle(frame, (x_right, self.center_y - height), (x_right + bar_width, self.center_y), tuple(map(int, color)), -1)

        return frame


    def draw_mode_170_bubble_choir(self, frame, magnitudes):
        """Mode 170: Bubbles rise; size from band energy; pop on snare"""
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])

        # Spawn bubbles
        if self.frame_counter % 5 == 0:
            for i in range(0, len(magnitudes), 10):
                magnitude = magnitudes[i]
                if magnitude > 0.3:
                    self.bubble_choir_bubbles.append({
                        'x': np.random.randint(50, self.width - 50),
                        'y': self.height - 50,
                        'size': int(10 + magnitude * 40),
                        'vy': -2 - magnitude * 2,
                        'life': 100,
                        'popping': False
                    })

        # Update and draw bubbles
        for bubble in self.bubble_choir_bubbles[:]:
            bubble['y'] += bubble['vy']
            bubble['life'] -= 1

            # Pop on snare (mids spike)
            if mids > 0.7 and not bubble['popping']:
                bubble['popping'] = True
                bubble['pop_frame'] = 0

            if bubble['popping']:
                bubble['pop_frame'] += 1
                # Expanding rings
                ring_radius = bubble['size'] + bubble['pop_frame'] * 10
                alpha = max(0, 255 - bubble['pop_frame'] * 50)
                cv2.circle(frame, (int(bubble['x']), int(bubble['y'])), ring_radius, (alpha, alpha, 255), 2, lineType=cv2.LINE_AA)

                if bubble['pop_frame'] > 5:
                    bubble['life'] = 0
            else:
                # Draw bubble
                cv2.circle(frame, (int(bubble['x']), int(bubble['y'])), bubble['size'], (150, 200, 255), 2, lineType=cv2.LINE_AA)

        self.bubble_choir_bubbles = [b for b in self.bubble_choir_bubbles if b['life'] > 0]

        return frame


    def draw_mode_171_starfield_quantizer(self, frame, magnitudes):
        """Mode 171: Stars quantized to a grid; cell brightness follows local band"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        grid_size = 16
        cell_width = self.width // grid_size
        cell_height = self.height // grid_size

        for i in range(grid_size):
            for j in range(grid_size):
                idx = (i * grid_size + j) % len(magnitudes)
                brightness = int(magnitudes[idx] * 255)

                x = j * cell_width + cell_width // 2
                y = i * cell_height + cell_height // 2

                if brightness > 50:
                    size = max(1, brightness // 50)
                    cv2.circle(frame, (x, y), size, (brightness, brightness, brightness), -1)

        # Subtle rotation on beat
        if bass > 0.6:
            angle = bass * 2
            M = cv2.getRotationMatrix2D((self.center_x, self.center_y), angle, 1.0)
            frame = cv2.warpAffine(frame, M, (self.width, self.height))

        return frame


    def draw_mode_172_dna_ladder(self, frame, magnitudes):
        """Mode 172: Two sinusoid strands; rung length follows mids"""
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        strand_spacing = 100
        amplitude = 50

        points_left = []
        points_right = []

        for y in range(0, self.height, 5):
            t = y * 0.02 + self.frame_counter * 0.05
            x_left = int(self.center_x - strand_spacing // 2 + np.sin(t) * amplitude)
            x_right = int(self.center_x + strand_spacing // 2 + np.sin(t) * amplitude)

            points_left.append((x_left, y))
            points_right.append((x_right, y))

        # Draw strands
        for i in range(1, len(points_left)):
            cv2.line(frame, points_left[i-1], points_left[i], (100, 200, 255), 3, lineType=cv2.LINE_AA)
            cv2.line(frame, points_right[i-1], points_right[i], (255, 100, 200), 3, lineType=cv2.LINE_AA)

        # Draw rungs
        for i in range(0, len(points_left), 10):
            rung_length = int(strand_spacing * (0.5 + mids * 0.5))
            x_mid = (points_left[i][0] + points_right[i][0]) // 2
            y = points_left[i][1]

            cv2.line(frame, (x_mid - rung_length // 2, y), (x_mid + rung_length // 2, y), (200, 200, 200), 2, lineType=cv2.LINE_AA)

            # Sparks traverse on highs
            if treble > 0.5:
                spark_x = int(x_mid + np.sin(self.frame_counter * 0.2 + i) * rung_length // 2)
                cv2.circle(frame, (spark_x, y), 3, (255, 255, 100), -1)

        return frame


    def draw_mode_173_arc_meter_trio(self, frame, magnitudes):
        """Mode 173: Three concentric arcs for lows/mids/highs"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        values = [bass, mids, treble]
        colors = [(255, 100, 100), (100, 255, 100), (100, 100, 255)]

        for i, (value, color) in enumerate(zip(values, colors)):
            radius = 80 + i * 50
            thickness = int(10 + value * 20)
            sweep = int(value * 270)

            cv2.ellipse(frame, (self.center_x, self.center_y), (radius, radius), -90, 0, sweep, color, thickness, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_174_ink_splatter_scope(self, frame, magnitudes):
        """Mode 174: Oscilloscope line with ink-style splats at transients"""
        # Generate waveform
        points = []
        for i in range(len(magnitudes)):
            x = int(i * self.width / len(magnitudes))
            y = int(self.center_y + (magnitudes[i] - 0.5) * 200)
            points.append((x, y))

        # Draw waveform
        for i in range(1, len(points)):
            cv2.line(frame, points[i-1], points[i], (100, 100, 200), 2, lineType=cv2.LINE_AA)

            # Detect transients (sharp changes)
            if abs(magnitudes[i] - magnitudes[i-1]) > 0.3:
                # Spawn splat
                self.ink_splatter_splats.append({
                    'x': points[i][0],
                    'y': points[i][1],
                    'size': 20,
                    'life': 30
                })

        # Draw splats
        for splat in self.ink_splatter_splats[:]:
            splat['size'] += 2
            splat['life'] -= 1

            if splat['life'] > 0:
                alpha = int((splat['life'] / 30) * 255)
                cv2.circle(frame, (splat['x'], splat['y']), splat['size'], (alpha // 2, alpha // 2, alpha), 1, lineType=cv2.LINE_AA)

        self.ink_splatter_splats = [s for s in self.ink_splatter_splats if s['life'] > 0]

        return frame


    def draw_mode_175_hex_cell_bloom(self, frame, magnitudes):
        """Mode 175: Hex grid; cells bloom outward with frequency bucket"""
        # Initialize hex grid
        if not self.hex_cell_states:
            hex_size = 30
            rows = self.height // (hex_size * 2) + 2
            cols = self.width // (hex_size * 2) + 2

            for row in range(rows):
                for col in range(cols):
                    x = col * hex_size * 1.5
                    y = row * hex_size * np.sqrt(3)
                    if row % 2 == 1:
                        x += hex_size * 0.75

                    self.hex_cell_states.append({
                        'x': int(x),
                        'y': int(y),
                        'bloom': 0,
                        'idx': (row * cols + col) % len(magnitudes)
                    })

        # Update and draw cells
        for cell in self.hex_cell_states:
            magnitude = magnitudes[cell['idx']]
            cell['bloom'] = magnitude

            if cell['bloom'] > 0.2:
                size = int(15 + cell['bloom'] * 20)
                brightness = int(cell['bloom'] * 255)
                color = (brightness // 2, brightness, brightness // 2)

                # Draw hexagon (simplified as circle)
                cv2.circle(frame, (cell['x'], cell['y']), size, color, -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_176_event_horizon_lattice(self, frame, magnitudes):
        """Mode 176: Event Horizon Lattice - warped grid bends toward a black hole; streaks on transients"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        warp_strength = 0.3 + bass * 1.2

        rows = 16
        cols = 16
        for r in range(rows + 1):
            y = int(r * self.height / rows)
            prev_pt = None
            for c in range(cols + 1):
                x = int(c * self.width / cols)
                dx = x - self.center_x
                dy = y - self.center_y
                dist = max(1.0, np.hypot(dx, dy))
                pull = warp_strength * 20000.0 / dist
                px = int(x - dx / dist * pull)
                py = int(y - dy / dist * pull)
                if prev_pt is not None:
                    cv2.line(frame, prev_pt, (px, py), (60, 60, 90), 1, lineType=cv2.LINE_AA)
                prev_pt = (px, py)

        for c in range(cols + 1):
            x = int(c * self.width / cols)
            prev_pt = None
            for r in range(rows + 1):
                y = int(r * self.height / rows)
                dx = x - self.center_x
                dy = y - self.center_y
                dist = max(1.0, np.hypot(dx, dy))
                pull = warp_strength * 20000.0 / dist
                px = int(x - dx / dist * pull)
                py = int(y - dy / dist * pull)
                if prev_pt is not None:
                    cv2.line(frame, prev_pt, (px, py), (60, 60, 90), 1, lineType=cv2.LINE_AA)
                prev_pt = (px, py)

        # Time-dilation streaks on transients
        transient_indices = np.where(np.abs(np.diff(magnitudes)) > 0.25)[0]
        for idx in transient_indices[:20]:
            angle = (idx / len(magnitudes)) * 2 * np.pi
            r1 = int(self.max_radius * 0.2)
            r2 = int(self.max_radius * (0.6 + highs * 0.3))
            x1 = int(self.center_x + np.cos(angle) * r1)
            y1 = int(self.center_y + np.sin(angle) * r1)
            x2 = int(self.center_x + np.cos(angle) * r2)
            y2 = int(self.center_y + np.sin(angle) * r2)
            cv2.line(frame, (x1, y1), (x2, y2), (180, 180, 255), 1, lineType=cv2.LINE_AA)
        return frame


    def draw_mode_177_comet_conveyor(self, frame, magnitudes):
        """Mode 177: Comet Conveyor - endless belt carries comets; tails shear on treble"""
        energy = float(np.mean(magnitudes))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))

        belt_y = int(self.center_y + np.sin(self.frame_counter * 0.03) * 30)
        cv2.line(frame, (0, belt_y), (self.width, belt_y), (80, 80, 80), 2, lineType=cv2.LINE_AA)

        # Spawn
        if len(self.comet_conveyor_belt) < 40 and np.random.random() < 0.3:
            band_idx = np.random.randint(0, len(magnitudes))
            self.comet_conveyor_belt.append({
                'x': -20,
                'y': belt_y + np.random.randint(-20, 20),
                'vx': 4 + energy * 8,
                'size': int(4 + magnitudes[band_idx] * 18),
                'shear': highs * 20
            })

        # Update/draw
        for comet in self.comet_conveyor_belt[:]:
            comet['x'] += comet['vx']
            if comet['x'] > self.width + 40:
                self.comet_conveyor_belt.remove(comet)
                continue
            cv2.circle(frame, (int(comet['x']), int(comet['y'])), comet['size'], (255, 255, 200), -1)
            for t in range(1, 6):
                px = int(comet['x'] - t * comet['vx'] * 2)
                py = int(comet['y'] - t * comet['shear'] * 0.2)
                alpha = max(20, 200 - t * 35)
                cv2.circle(frame, (px, py), max(1, comet['size'] - t), (alpha, alpha, 180), -1)
        return frame


    def draw_mode_178_quantum_foam_micro(self, frame, magnitudes):
        """Mode 178: Quantum Foam Micro - foamy micro-bubbles pop; cascades on peaks"""
        energy = float(np.mean(magnitudes))
        peak = np.max(magnitudes) > 0.8

        # Spawn bubbles
        if len(self.foam_bubbles) < 200:
            for _ in range(3):
                self.foam_bubbles.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'r': np.random.randint(1, 5),
                    'life': np.random.randint(20, 80)
                })

        for b in self.foam_bubbles[:]:
            b['life'] -= 1
            b['r'] = max(1, b['r'] + (np.random.random() - 0.5) * 0.5)
            if peak and np.random.random() < 0.2 and len(self.foam_bubbles) < 300:
                # cascade: spawn smaller around (with limit check)
                for _ in range(2):  # Reduced from 3 to 2
                    self.foam_bubbles.append({'x': b['x']+np.random.randint(-6,6), 'y': b['y']+np.random.randint(-6,6), 'r': 1, 'life': 20})
            color = int(120 + energy * 135)
            cv2.circle(frame, (int(b['x']), int(b['y'])), int(b['r']), (color, color, 255), 1, lineType=cv2.LINE_AA)
            if b['life'] <= 0:
                self.foam_bubbles.remove(b)
        return frame


    def draw_mode_179_aurora_crown(self, frame, magnitudes):
        """Mode 179: Aurora Crown - polar aurora dome overhead; ribbons brighten by mids"""
        mids = float(np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]))
        ribbon_count = 8
        for i in range(ribbon_count):
            angle = (i / ribbon_count) * 2 * np.pi
            for r in range(60, 240, 10):
                x = int(self.center_x + np.cos(angle + np.sin(self.frame_counter*0.02+i)*0.2) * r)
                y = int(self.center_y - r * 0.6 + np.sin(i*0.7 + self.frame_counter*0.05) * 10)
                color = (int(80 + mids * 175), int(120 + mids * 135), 255)
                cv2.circle(frame, (x, y), 2, color, -1)
        return frame


    def draw_mode_180_asteroid_excavator(self, frame, magnitudes):
        """Mode 180: Asteroid Excavator - drill depth increases with bass; debris size follows highs"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        center = (self.center_x, self.center_y)
        cv2.circle(frame, center, 180, (60, 60, 60), -1)
        depth = int(bass * 120)
        cv2.line(frame, (self.center_x - 200, self.center_y - 100), (self.center_x - 40 - depth, self.center_y), (200, 200, 220), 3)
        # debris
        for _ in range(int(5 + highs * 25)):
            dx = np.random.randint(-180, -40)
            dy = np.random.randint(-10, 10)
            size = max(1, int(2 + highs * 6))
            cv2.circle(frame, (self.center_x + dx, self.center_y + dy), size, (180, 180, 180), -1)
        return frame


    def draw_mode_181_hyperloop_spectrotrain(self, frame, magnitudes):
        """Mode 181: Hyperloop Spectrotrain - car length scales to energy; station lights strobe"""
        energy = float(np.mean(magnitudes))
        y = self.center_y
        cv2.line(frame, (0, y+30), (self.width, y+30), (100,100,100), 4)
        car_count = 6
        base_x = int((self.frame_counter * (2 + energy*8)) % (self.width + 400)) - 200
        for i in range(car_count):
            cx = base_x - i * 70
            w = int(40 + energy * 80)
            cv2.rectangle(frame, (cx, y-20), (cx+w, y+20), (180, 200, 255), -1)
            for k in range(4):
                cv2.rectangle(frame, (cx+5+k*int(w/4), y-12), (cx+5+k*int(w/4)+10, y-2), (255, 255, 150), -1)
        if np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]) > 0.65:
            for sx in range(0, self.width, 60):
                cv2.circle(frame, (sx, y-40), 6, (255, 255, 200), -1)
        return frame


    def draw_mode_182_galactic_pinball(self, frame, magnitudes):
        """Mode 182: Galactic Pinball - bumpers map to bands; ball boosts on peaks"""
        if not self.pinball_entities:
            self.pinball_entities = [{ 'x': self.center_x, 'y': self.center_y, 'vx': 3, 'vy': -2 }]
        ball = self.pinball_entities[0]
        peak = np.max(magnitudes) > 0.8
        if peak:
            ball['vx'] *= 1.2
            ball['vy'] *= 1.2
        ball['x'] += ball['vx']
        ball['y'] += ball['vy']
        if ball['x']<10 or ball['x']>self.width-10: ball['vx']*=-1
        if ball['y']<10 or ball['y']>self.height-10: ball['vy']*=-1
        cv2.circle(frame, (int(ball['x']), int(ball['y'])), 6, (255, 255, 255), -1)
        # bumpers
        for i in range(10):
            angle = (i/10)*2*np.pi
            r = 220
            bx = int(self.center_x + np.cos(angle)*r)
            by = int(self.center_y + np.sin(angle)*r)
            mag = magnitudes[i*(len(magnitudes)//10)]
            size = int(8 + mag*18)
            cv2.circle(frame, (bx, by), size, (100, 150, 255), -1)
        return frame


    def draw_mode_183_nebula_inkblot(self, frame, magnitudes):
        """Mode 183: Nebula Inkblot - mirrored volumetric smoke; hue by dominant band"""
        dominant_idx = int(np.argmax(magnitudes))
        hue = int((dominant_idx / max(1, len(magnitudes)-1)) * 180)
        for _ in range(120):
            x = np.random.randint(0, self.center_x)
            y = np.random.randint(0, self.height)
            jitter = int(np.random.randn()*6)
            color_hsv = np.array([[[hue, 180, 200]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            cv2.circle(frame, (x, y+jitter), 3, tuple(map(int, color)), -1)
            cv2.circle(frame, (self.width-x, y+jitter), 3, tuple(map(int, color)), -1)
        return frame


    def draw_mode_184_satellite_telemetry_rings(self, frame, magnitudes):
        """Mode 184: Satellite Telemetry Rings - rippling rings with dashed spectrum"""
        energy = float(np.mean(magnitudes))
        ring_count = 5
        for i in range(ring_count):
            radius = int(60 + i*40 + (self.frame_counter*3 + i*15) % 40)
            dash_count = 48
            for d in range(dash_count):
                t = d/dash_count
                ang = t*2*np.pi
                idx = min(int(t*len(magnitudes)), len(magnitudes)-1)
                h = magnitudes[idx]
                x1 = int(self.center_x + np.cos(ang)*radius)
                y1 = int(self.center_y + np.sin(ang)*radius)
                x2 = int(self.center_x + np.cos(ang)*(radius+int(h*25)))
                y2 = int(self.center_y + np.sin(ang)*(radius+int(h*25)))
                cv2.line(frame, (x1,y1), (x2,y2), (120,120,200), 1, lineType=cv2.LINE_AA)
        if energy < 0.15 and self.frame_counter % 6 == 0:
            cv2.circle(frame, (np.random.randint(0,self.width), np.random.randint(0,self.height)), 2, (255,120,120), -1)
        return frame


    def draw_mode_185_wormhole_origami(self, frame, magnitudes):
        """Mode 185: Wormhole Origami - sheet folds into portal; depth by bass"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        folds = 10 + int(np.mean(magnitudes[3*len(magnitudes)//4:]) * 10)
        for i in range(folds):
            t = i/folds
            angle = t*np.pi
            r = int(200 + bass*120 * np.cos(angle))
            cv2.ellipse(frame, (self.center_x,self.center_y), (r,int(r*0.5)), 0, 0, 360, (160,160,255), 1, lineType=cv2.LINE_AA)
        return frame


    def draw_mode_186_holographic_jellyfish(self, frame, magnitudes):
        """Mode 186: Holographic Jellyfish - bell pulsates with lows; tentacles sparkle with highs"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        r = int(60 + bass*120)
        cv2.circle(frame, (self.center_x,self.center_y-60), r, (200,200,255), 2)
        for t in range(20):
            ang = (t/20)*np.pi
            x = int(self.center_x + np.cos(ang)*r*0.6)
            y = int(self.center_y-60 + np.sin(ang)*r*0.3)
            ty = y
            for k in range(8):
                nx = int(x + np.sin(self.frame_counter*0.08+k+t)*4)
                ny = int(ty + k*14)
                cv2.circle(frame,(nx,ny),1,(255,255,180),-1)
        for _ in range(int(highs*30)):
            cv2.circle(frame,(np.random.randint(self.center_x-r,self.center_x+r),np.random.randint(self.center_y-60,self.center_y+r)),1,(255,255,200),-1)
        return frame


    def draw_mode_187_moon_quarry_crane(self, frame, magnitudes):
        """Mode 187: Moon Quarry Crane - bins heights equal band magnitude; dust on kicks"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        bins = min(24, len(magnitudes))
        gap = self.width // (bins+2)
        for i in range(bins):
            h = int(magnitudes[i]*220)
            x = gap*(i+1)
            cv2.rectangle(frame,(x,self.center_y-h),(x+10,self.center_y),(180,180,220),-1)
        if bass>0.65:
            for _ in range(40):
                cv2.circle(frame,(np.random.randint(0,self.width), self.center_y-np.random.randint(0,80)),1,(220,220,220),-1)
        return frame


    def draw_mode_188_constellation_typoplot(self, frame, magnitudes):
        """Mode 188: Constellation TypoPlot - letters as stars; lines draw when band is hot"""
        cols = min(40, len(magnitudes))
        pts = []
        for i in range(cols):
            t = i/cols
            x = int(80 + t*(self.width-160))
            y = int(160 + np.sin(self.frame_counter*0.02 + t*6)*60)
            pts.append((x,y))
            cv2.circle(frame,(x,y),2,(200,200,255),-1)
        thr = 0.55
        for i in range(1, cols):
            if magnitudes[i]>thr:
                cv2.line(frame, pts[i-1], pts[i], (255,255,255), 1, lineType=cv2.LINE_AA)
        return frame


    def draw_mode_189_cryo_crystal_garden(self, frame, magnitudes):
        """Mode 189: Cryo Crystal Garden - crystals grow per frequency slice; flare on treble"""
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        slices = 18
        for i in range(slices):
            idx = min(int(i * len(magnitudes)/slices), len(magnitudes)-1)
            mag = magnitudes[idx]
            angle = (i/slices)*2*np.pi
            length = int(40 + mag*180)
            x1 = self.center_x
            y1 = self.center_y
            x2 = int(x1 + np.cos(angle)*length)
            y2 = int(y1 + np.sin(angle)*length)
            cv2.line(frame,(x1,y1),(x2,y2),(200,220,255),2, lineType=cv2.LINE_AA)
        if highs>0.6:
            cv2.circle(frame,(self.center_x,self.center_y),6,(255,255,255),-1)
        return frame


    def draw_mode_190_meteorite_blueprint(self, frame, magnitudes):
        """Mode 190: Meteorite Blueprint - technical UI; callouts to bands; red stamp on peaks"""
        for x in range(0,self.width,60):
            cv2.line(frame,(x,0),(x,self.height),(40,40,70),1)
        for y in range(0,self.height,60):
            cv2.line(frame,(0,y),(self.width,y),(40,40,70),1)
        for i in range(0, len(magnitudes), max(1,len(magnitudes)//20)):
            mag = magnitudes[i]
            x = 80 + int(i/len(magnitudes)*(self.width-160))
            y = self.center_y
            cv2.circle(frame,(x,y),4,(180,220,255),-1)
            cv2.line(frame,(x,y),(x,int(y-80-mag*120)),(120,180,255),1)
        if np.max(magnitudes)>0.85:
            cv2.rectangle(frame,(self.width-140,40),(self.width-40,100),(0,0,200),-1)
        return frame


    def draw_mode_191_lunar_tide_pool(self, frame, magnitudes):
        """Mode 191: Lunar Tide Pool - water level by bass; caustics sharpen with highs"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        level = int(self.center_y + 80 - bass*150)
        cv2.rectangle(frame,(0,level),(self.width,self.height),(120,160,220),-1)
        for x in range(0,self.width,10):
            y = level + int(np.sin(self.frame_counter*0.1 + x*0.05)* (6+highs*12))
            cv2.line(frame,(x,y),(x,y+3),(200,220,255),1)
        return frame


    def draw_mode_192_orbital_barcode_slicer(self, frame, magnitudes):
        """Mode 192: Orbital Barcode Slicer - rings slice vertical barcode; brightness per band"""
        bar_count = min(40, len(magnitudes))
        bar_w = max(2, self.width//(bar_count*2))
        for i in range(bar_count):
            h = int(magnitudes[i]*(self.height//2))
            x = int(self.center_x - bar_count*bar_w + i*2*bar_w)
            cv2.rectangle(frame,(x,self.center_y-h),(x+bar_w,self.center_y+h),(80,80,120),-1)
        ring_r = int(120 + (self.frame_counter*2 % 120))
        cv2.circle(frame,(self.center_x,self.center_y), ring_r,(180,180,255),2)
        return frame


    def draw_mode_193_satellite_swarm_flocking(self, frame, magnitudes):
        """Mode 193: Satellite Swarm Flocking - simple flock; thrust bursts on kick"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        if len(self.satellites_swarm) < 40:
            for _ in range(40 - len(self.satellites_swarm)):
                self.satellites_swarm.append({'x':np.random.randint(0,self.width),'y':np.random.randint(0,self.height),'vx':np.random.uniform(-1,1),'vy':np.random.uniform(-1,1)})
        for s in self.satellites_swarm:
            s['vx'] += (np.random.random()-0.5)*0.2
            s['vy'] += (np.random.random()-0.5)*0.2
            if bass>0.6:
                s['vx'] *= 1.1; s['vy'] *= 1.1
            s['x'] = (s['x'] + s['vx'])%self.width
            s['y'] = (s['y'] + s['vy'])%self.height
            cv2.circle(frame,(int(s['x']),int(s['y'])),2,(200,200,255),-1)
        return frame


    def draw_mode_194_astro_pulse_weave(self, frame, magnitudes):
        """Mode 194: Astro Pulse Weave - two opposing spiral waves; brightness sum of bands"""
        total = float(np.sum(magnitudes))
        for i in range(180):
            t = i/180
            ang = t*4*np.pi + self.frame_counter*0.02
            r = int(40 + t*260)
            x1 = int(self.center_x + np.cos(ang)*r)
            y1 = int(self.center_y + np.sin(ang)*r)
            x2 = int(self.center_x + np.cos(-ang)*r)
            y2 = int(self.center_y + np.sin(-ang)*r)
            color = min(255, int(80 + total*60))
            cv2.circle(frame,(x1,y1),1,(color, color, 255),-1)
            cv2.circle(frame,(x2,y2),1,(color, color, 255),-1)
        return frame


    def draw_mode_195_zero_g_paint_spheres(self, frame, magnitudes):
        """Mode 195: Zero-G Paint Spheres - spheres merge on peaks and split on highs"""
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        peak = np.max(magnitudes) > 0.85
        if len(self.paint_spheres) < 12:
            for _ in range(12 - len(self.paint_spheres)):
                self.paint_spheres.append({'x':np.random.randint(100,self.width-100),'y':np.random.randint(100,self.height-100),'r':np.random.randint(10,30)})
        if peak and len(self.paint_spheres)>1:
            a = self.paint_spheres.pop(); b = self.paint_spheres.pop()
            cx = int((a['x']+b['x'])/2); cy = int((a['y']+b['y'])/2)
            cr = int(min(80, a['r']+b['r']))
            self.paint_spheres.append({'x':cx,'y':cy,'r':cr})
        if highs>0.65 and len(self.paint_spheres)<20:
            self.paint_spheres.append({'x':np.random.randint(80,self.width-80),'y':np.random.randint(80,self.height-80),'r':12})
        for s in self.paint_spheres:
            cv2.circle(frame,(int(s['x']),int(s['y'])),int(s['r']),(160,200,255),-1)
        return frame


    def draw_mode_196_supernova_countdown(self, frame, magnitudes):
        """Mode 196: Supernova Countdown - star swells with energy; blasts at threshold"""
        self.supernova_state['energy'] += float(np.mean(magnitudes))*0.02
        threshold = 1.0
        if not self.supernova_state['blasting'] and self.supernova_state['energy']>threshold:
            self.supernova_state['blasting'] = True
            for i in range(80):
                ang = (i/80)*2*np.pi
                self.supernova_state['filaments'].append({'x':self.center_x,'y':self.center_y,'vx':np.cos(ang)*(2+np.random.random()*3),'vy':np.sin(ang)*(2+np.random.random()*3),'life':60})
        if not self.supernova_state['blasting']:
            r = int(40 + self.supernova_state['energy']*160)
            cv2.circle(frame,(self.center_x,self.center_y),r,(255,220,150),-1)
        else:
            for f in self.supernova_state['filaments'][:]:
                f['x'] += f['vx']; f['y'] += f['vy']; f['life'] -= 1
                cv2.circle(frame,(int(f['x']),int(f['y'])),1,(255,200,150),-1)
                if f['life']<=0:
                    self.supernova_state['filaments'].remove(f)
        return frame


    def draw_mode_197_martian_wind_harp(self, frame, magnitudes):
        """Mode 197: Martian Wind Harp - dunes as strings; ripples by mids; dust devils on snares"""
        mids = float(np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]))
        for y in range(200, self.height, 40):
            for x in range(0, self.width, 8):
                dy = int(np.sin(x*0.05 + self.frame_counter*0.08)*mids*20)
                frame[min(self.height-1,y+dy), min(self.width-1,x)] = (160,120,90)
        if mids>0.65:
            for _ in range(40):
                cv2.circle(frame,(np.random.randint(0,self.width),np.random.randint(200,self.height)),2,(200,180,150),-1)
        return frame


    def draw_mode_198_teleporting_bar_choir(self, frame, magnitudes):
        """Mode 198: Teleporting Bar Choir - bars pop at random radial positions; decay persists"""
        if self.frame_counter % max(1, int(8 - np.mean(magnitudes[3*len(magnitudes)//4:]) * 6)) == 0:
            idx = np.random.randint(0, len(magnitudes))
            angle = np.random.random()*2*np.pi
            radius = np.random.randint(40, self.max_radius)
            x = int(self.center_x + np.cos(angle)*radius)
            y = int(self.center_y + np.sin(angle)*radius)
            self.teleporting_bars.append({'x':x,'y':y,'h':int(30 + magnitudes[idx]*160),'life':50})
        for b in self.teleporting_bars[:]:
            cv2.line(frame,(b['x'],b['y']), (b['x'], b['y']-b['h']), (200,200,255), 2)
            b['life'] -= 1
            b['h'] = max(0, b['h']-2)
            if b['life']<=0: self.teleporting_bars.remove(b)
        return frame


    def draw_mode_199_cosmic_vinyl_halo(self, frame, magnitudes):
        """Mode 199: Cosmic Vinyl Halo - record edge-on; grooves shimmer with spectrum"""
        for i in range(12):
            r = 40 + i*12
            val = magnitudes[min(int(i/12*len(magnitudes)), len(magnitudes)-1)]
            cv2.ellipse(frame,(self.center_x,self.center_y),(r,int(r*0.1)),90,0,360,(80,80,80),1)
            cv2.ellipse(frame,(self.center_x,self.center_y),(r,int(r*0.1)),90,0,int(val*360),(160,160,255),2)
        return frame


    def draw_mode_200_photon_origination_chamber(self, frame, magnitudes):
        """Mode 200: Photon Origination Chamber - photons exit slits; rate per band bucket"""
        slit_count = 8
        for s in range(slit_count):
            x = int(self.center_x - 160 + s*(320//(slit_count-1)))
            cv2.line(frame,(x,self.center_y-60),(x,self.center_y+60),(120,120,150),2)
            idx = min(int(s/slit_count*len(magnitudes)), len(magnitudes)-1)
            rate = int(magnitudes[idx]*6)
            for _ in range(rate):
                px = x + np.random.randint(-2,2)
                py = self.center_y + np.random.randint(-2,2)
                cv2.circle(frame,(px,py-70),1,(255,255,200),-1)
        return frame



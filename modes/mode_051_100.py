"""
Audio Spectrum Visualization Modes 51-100
Auto-generated from audio_spectrum_creative.py
"""
from .base import BaseModeVisualizer
import numpy as np
import cv2


class Modes051_100(BaseModeVisualizer):
    """Visualization modes 51 through 100"""

    def __init__(self, visualizer):
        super().__init__(visualizer)
        # Mode-specific state initialization will be added here
        # This ensures backward compatibility with the original code

    def draw_mode_51_fractal_tree(self, frame, magnitudes):
        """Mode 51: Generative tree that grows - branches on bass, blooms on treble"""
        avg_magnitude = np.mean(magnitudes)
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Main trunk sway
        trunk_sway = int(np.sin(self.frame_counter * 0.1 + avg_magnitude) * 20)
        trunk_base = (self.center_x + trunk_sway, self.height - 50)
        trunk_top = (self.center_x + trunk_sway, self.center_y)

        # Draw main trunk with thickness based on volume
        trunk_thickness = int(10 + avg_magnitude * 15)
        cv2.line(frame, trunk_base, trunk_top, (40, 80, 40), trunk_thickness, lineType=cv2.LINE_AA)

        # Spawn branches on bass hits
        if bass > 0.3 and self.frame_counter % 8 == 0:
            angle = -np.pi/2 + (np.random.random() - 0.5) * np.pi/3
            self.fractal_tree_branches.append({
                'x': trunk_top[0], 'y': trunk_top[1],
                'angle': angle, 'length': 40 + bass * 60,
                'thickness': int(3 + bass * 8), 'generation': 0, 'life': 1.0
            })

        # Draw and update branches
        new_branches = []
        for branch in self.fractal_tree_branches:
            if branch['life'] > 0:
                end_x = int(branch['x'] + np.cos(branch['angle']) * branch['length'])
                end_y = int(branch['y'] + np.sin(branch['angle']) * branch['length'])

                alpha = branch['life']
                color = (int(50 * alpha), int(100 * alpha), int(50 * alpha))
                cv2.line(frame, (int(branch['x']), int(branch['y'])), (end_x, end_y),
                        color, branch['thickness'], lineType=cv2.LINE_AA)

                # Bloom flowers on treble
                if treble > 0.4 and branch['generation'] > 0:
                    bloom_size = int(3 + treble * 10)
                    bloom_color_hsv = np.array([[[int(treble * 180), 255, 255]]], dtype=np.uint8)
                    bloom_color = cv2.cvtColor(bloom_color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                    cv2.circle(frame, (end_x, end_y), bloom_size, tuple(map(int, bloom_color * alpha)), -1, lineType=cv2.LINE_AA)

                branch['life'] -= 0.003
                new_branches.append(branch)

        self.fractal_tree_branches = new_branches[:100]  # Limit
        return frame


    def draw_mode_52_cityscape_extrusion(self, frame, magnitudes):
        """Mode 52: 3D city blocks that extrude with frequency amplitude"""
        num_blocks = min(len(magnitudes), 40)
        block_width = self.width // num_blocks

        for i in range(num_blocks):
            magnitude = magnitudes[i] if i < len(magnitudes) else 0
            building_height = int(magnitude * self.height * 0.7)

            # 3D perspective
            base_y = self.height - 100
            top_y = base_y - building_height
            x_left = i * block_width + 5
            x_right = (i + 1) * block_width - 5

            # Building color based on beat
            hue = int((i / num_blocks) * 180)
            saturation = 180 + int(magnitude * 75)
            value = 100 + int(magnitude * 155)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw building
            cv2.rectangle(frame, (x_left, base_y), (x_right, top_y), tuple(map(int, color)), -1)

            # Emissive windows
            if magnitude > 0.3:
                num_windows = max(2, int(building_height / 30))
                for w in range(num_windows):
                    window_y = base_y - int((w + 0.5) * building_height / num_windows)
                    window_x = (x_left + x_right) // 2
                    window_brightness = int(255 * magnitude)
                    cv2.circle(frame, (window_x, window_y), 3, (window_brightness, window_brightness, 200), -1)

        return frame


    def draw_mode_53_gravity_well(self, frame, magnitudes):
        """Mode 53: Particles pulled toward pulsing bass center, pushed by treble shockwaves"""
        avg_magnitude = np.mean(magnitudes)
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Spawn particles at edges
        if self.frame_counter % 2 == 0:
            for _ in range(int(treble * 20 + 5)):
                angle = np.random.random() * 2 * np.pi
                edge_dist = min(self.width, self.height) // 2
                self.gravity_well_particles.append({
                    'x': self.center_x + np.cos(angle) * edge_dist,
                    'y': self.center_y + np.sin(angle) * edge_dist,
                    'vx': 0, 'vy': 0, 'hue': int(treble * 180)
                })

        # Black hole pulses with bass
        well_radius = int(30 + bass * 50)
        cv2.circle(frame, (self.center_x, self.center_y), well_radius, (255, 255, 255), -1, lineType=cv2.LINE_AA)

        # Bass shockwave push
        shockwave_force = bass * 500 if bass > 0.6 else 0

        new_particles = []
        for p in self.gravity_well_particles:
            dx = self.center_x - p['x']
            dy = self.center_y - p['y']
            dist = np.sqrt(dx**2 + dy**2) + 1

            # Gravitational pull
            pull_force = 200 / (dist**2)
            p['vx'] += (dx / dist) * pull_force
            p['vy'] += (dy / dist) * pull_force

            # Shockwave push
            if shockwave_force > 0 and dist < 200:
                p['vx'] -= (dx / dist) * shockwave_force
                p['vy'] -= (dy / dist) * shockwave_force

            p['x'] += p['vx']
            p['y'] += p['vy']

            if dist > well_radius and 0 < p['x'] < self.width and 0 < p['y'] < self.height:
                color_hsv = np.array([[[p['hue'], 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                cv2.circle(frame, (int(p['x']), int(p['y'])), 3, tuple(map(int, color)), -1)
                new_particles.append(p)

        self.gravity_well_particles = new_particles[:500]
        return frame


    def draw_mode_54_metaball_fluid(self, frame, magnitudes):
        """Mode 54: Lava lamp metaballs - size pulses with frequency amplitude"""
        num_balls = min(len(magnitudes), 15)

        # Update or create metaballs
        while len(self.metaballs) < num_balls:
            self.metaballs.append({
                'x': np.random.random() * self.width,
                'y': np.random.random() * self.height,
                'vx': (np.random.random() - 0.5) * 4,
                'vy': (np.random.random() - 0.5) * 4,
                'base_radius': 40 + np.random.random() * 40
            })

        avg_magnitude = np.mean(magnitudes)

        # Draw metaballs with glow
        for i, ball in enumerate(self.metaballs[:num_balls]):
            magnitude = magnitudes[i] if i < len(magnitudes) else avg_magnitude
            radius = int(ball['base_radius'] * (0.7 + magnitude * 0.8))

            # Update position with fluid-like motion
            ball['x'] += ball['vx']
            ball['y'] += ball['vy']

            # Bounce off walls
            if ball['x'] < radius or ball['x'] > self.width - radius:
                ball['vx'] *= -1
            if ball['y'] < radius or ball['y'] > self.height - radius:
                ball['vy'] *= -1

            # Color based on frequency
            hue = int((i / num_balls) * 180)
            saturation = 200 + int(magnitude * 55)
            value = 150 + int(magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw with gradient
            for r in range(radius, 0, -5):
                alpha = r / radius
                cv2.circle(frame, (int(ball['x']), int(ball['y'])), r,
                          tuple(int(c * alpha) for c in color), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_55_aurora_borealis(self, frame, magnitudes):
        """Mode 55: Northern lights curtains - low freq shapes, high freq shimmer"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        num_curtains = 5
        curtain_points = 60

        for curtain_idx in range(num_curtains):
            points = []
            base_y_offset = curtain_idx * 80 - 160

            for i in range(curtain_points):
                x = int((i / curtain_points) * self.width)
                # Low frequency controls main shape
                wave1 = np.sin(i * 0.15 + self.frame_counter * 0.05 + curtain_idx) * bass * 60
                wave2 = np.sin(i * 0.08 + self.frame_counter * 0.03) * bass * 40
                y = int(self.center_y + base_y_offset + wave1 + wave2)

                # High frequency shimmer
                shimmer = np.sin(i * 0.8 + self.frame_counter * 0.4) * treble * 20
                y += int(shimmer)

                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            # Aurora color (greenish with variation)
            hue = 60 + curtain_idx * 15
            saturation = 180 + int(treble * 75)
            value = 120 + int(bass * 135)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw curtain with thickness
            if len(points) > 1:
                cv2.polylines(frame, [points], False, tuple(map(int, color)), 3, lineType=cv2.LINE_AA)
                # Add glow
                cv2.polylines(frame, [points], False, tuple(int(c * 0.5) for c in color), 8, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_56_stained_glass(self, frame, magnitudes):
        """Mode 56: Stained glass window panes that glow with frequency"""
        rows, cols = 6, 10
        pane_width = self.width // cols
        pane_height = self.height // rows

        pane_idx = 0
        for row in range(rows):
            for col in range(cols):
                if pane_idx >= len(magnitudes):
                    break

                magnitude = magnitudes[pane_idx]

                x1 = col * pane_width + 2
                y1 = row * pane_height + 2
                x2 = (col + 1) * pane_width - 2
                y2 = (row + 1) * pane_height - 2

                # Stained glass color
                hue = int((pane_idx / len(magnitudes)) * 180)
                saturation = 255
                value = int(80 + magnitude * 175)  # Glow intensity
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                # Draw pane
                cv2.rectangle(frame, (x1, y1), (x2, y2), tuple(map(int, color)), -1)

                # Add glow effect
                if magnitude > 0.5:
                    glow_thickness = int(magnitude * 10)
                    glow_color = tuple(int(c * 1.2) for c in color)
                    cv2.rectangle(frame, (x1-glow_thickness, y1-glow_thickness),
                                (x2+glow_thickness, y2+glow_thickness), glow_color, glow_thickness, lineType=cv2.LINE_AA)

                pane_idx += 1

        return frame


    def draw_mode_57_neon_nerve_network(self, frame, magnitudes):
        """Mode 57: Neural network with pulsing nodes and synapse firings"""
        # Initialize nerve nodes if empty
        if len(self.nerve_nodes) == 0:
            num_nodes = 20
            for _ in range(num_nodes):
                self.nerve_nodes.append({
                    'x': np.random.randint(100, self.width - 100),
                    'y': np.random.randint(100, self.height - 100),
                    'pulse': 0, 'connections': []
                })
            # Create connections
            for i, node in enumerate(self.nerve_nodes):
                num_connections = np.random.randint(2, 5)
                for _ in range(num_connections):
                    target = np.random.randint(0, len(self.nerve_nodes))
                    if target != i:
                        node['connections'].append(target)

        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Update node pulses with bass
        for i, node in enumerate(self.nerve_nodes):
            if i < len(magnitudes):
                node['pulse'] = magnitudes[i]

        # Draw connections (synapses)
        for i, node in enumerate(self.nerve_nodes):
            for target_idx in node['connections']:
                target = self.nerve_nodes[target_idx]

                # Synapse fires with treble
                if treble > 0.5:
                    alpha = treble
                    color = (int(100 * alpha), int(200 * alpha), int(255 * alpha))
                    cv2.line(frame, (node['x'], node['y']), (target['x'], target['y']),
                            color, 2, lineType=cv2.LINE_AA)

        # Draw nodes
        for node in self.nerve_nodes:
            pulse_radius = int(10 + node['pulse'] * 25)
            cv2.circle(frame, (node['x'], node['y']), pulse_radius, (100, 255, 255), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (node['x'], node['y']), pulse_radius + 5, (50, 150, 200), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_58_glitch_artifact(self, frame, magnitudes):
        """Mode 58: Clean bars corrupted by glitch effects on transients"""
        avg_magnitude = np.mean(magnitudes)
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Draw clean bars first
        bar_width = self.width // len(magnitudes)
        for i, magnitude in enumerate(magnitudes):
            bar_height = int(magnitude * self.height * 0.7)
            x = i * bar_width
            y = self.height - bar_height

            color = (100, 200, 255)
            cv2.rectangle(frame, (x, y), (x + bar_width - 2, self.height), color, -1)

        # Apply glitch effects on strong transients
        if treble > 0.7:
            glitch_intensity = int((treble - 0.7) * 10)

            # Pixel sorting effect
            for _ in range(glitch_intensity):
                y_slice = np.random.randint(0, self.height - 50)
                slice_height = np.random.randint(10, 50)
                row = frame[y_slice:y_slice + slice_height, :]
                sorted_row = np.sort(row.view('i8'), axis=1).view(row.dtype)
                frame[y_slice:y_slice + slice_height, :] = sorted_row

            # Chromatic aberration
            shift = int(treble * 20)
            frame[:, :, 2] = np.roll(frame[:, :, 2], shift, axis=1)  # Red channel
            frame[:, :, 0] = np.roll(frame[:, :, 0], -shift, axis=1)  # Blue channel

        return frame


    def draw_mode_59_warp_tunnel(self, frame, magnitudes):
        """Mode 59: Hyperspace tunnel of rings - radius pulses with frequency"""
        avg_magnitude = np.mean(magnitudes)
        num_rings = 30

        for i in range(num_rings):
            depth = i / num_rings
            scale = 1 - depth * 0.9

            # Ring frequency index
            freq_idx = int(depth * len(magnitudes))
            if freq_idx >= len(magnitudes):
                freq_idx = len(magnitudes) - 1

            magnitude = magnitudes[freq_idx]
            radius = int(self.max_radius * scale * (0.5 + magnitude * 0.8))

            # Color based on depth and frequency
            hue = int((depth + self.frame_counter * 0.01) * 180) % 180
            saturation = 200 + int(magnitude * 55)
            value = int(150 * (1 - depth) + magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw ring
            thickness = int(2 + magnitude * 8)
            cv2.circle(frame, (self.center_x, self.center_y), radius, tuple(map(int, color)), thickness, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_60_conway_life(self, frame, magnitudes):
        """Mode 60: Conway's Game of Life modulated by audio"""
        grid_size = 40
        cell_width = self.width // grid_size
        cell_height = self.height // grid_size

        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize grid
        if len(self.cellular_automaton) == 0:
            self.cellular_automaton = np.random.randint(0, 2, (grid_size, grid_size))

        # Audio modulates birth/survival - low freq spawns, high freq increases survival
        if self.frame_counter % 3 == 0:
            new_grid = self.cellular_automaton.copy()

            for y in range(grid_size):
                for x in range(grid_size):
                    # Count neighbors
                    neighbors = 0
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            if dy == 0 and dx == 0:
                                continue
                            ny, nx = (y + dy) % grid_size, (x + dx) % grid_size
                            neighbors += self.cellular_automaton[ny, nx]

                    # Modified rules based on audio
                    if self.cellular_automaton[y, x] == 1:
                        # Survival: 2-3 neighbors (+ treble increases tolerance)
                        if neighbors < 2 - int(treble) or neighbors > 3 + int(treble * 2):
                            new_grid[y, x] = 0
                    else:
                        # Birth: 3 neighbors (bass spawns new cells randomly)
                        if neighbors == 3 or (bass > 0.6 and np.random.random() < bass * 0.1):
                            new_grid[y, x] = 1

            self.cellular_automaton = new_grid

        # Draw grid
        for y in range(grid_size):
            for x in range(grid_size):
                if self.cellular_automaton[y, x] == 1:
                    x1 = x * cell_width
                    y1 = y * cell_height
                    color = (100, 255, 100)
                    cv2.rectangle(frame, (x1, y1), (x1 + cell_width - 1, y1 + cell_height - 1), color, -1)

        return frame


    def draw_mode_61_ascii_art(self, frame, magnitudes):
        """Mode 61: ASCII art bars using text characters"""
        # Create text representation
        chars = ['.', '-', '=', '+', '*', '#', '@']
        bar_width = self.width // len(magnitudes)

        for i, magnitude in enumerate(magnitudes):
            bar_height = int(magnitude * 20)  # Number of chars high
            char_idx = min(int(magnitude * len(chars)), len(chars) - 1)
            char = chars[char_idx]

            # Draw vertical bar of characters
            x = int(i * bar_width + bar_width // 2)
            for row in range(bar_height):
                y = self.height - row * 30 - 30
                if y > 0:
                    brightness = int(200 + magnitude * 55)
                    cv2.putText(frame, char, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                              (brightness, brightness, brightness), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_62_rippling_water(self, frame, magnitudes):
        """Mode 62: Water surface with ripples from frequency raindrop sources"""
        # Each frequency acts as a ripple source
        for i, magnitude in enumerate(magnitudes):
            if magnitude > 0.4:
                # Source position along top
                x = int((i / len(magnitudes)) * self.width)
                y = int(self.height * 0.3)

                # Create ripple
                ripple_radius = int((self.frame_counter % 60) * magnitude * 8)
                alpha = 1.0 - (ripple_radius / 300)

                if alpha > 0:
                    color = (int(100 * alpha), int(150 * alpha), int(255 * alpha))
                    cv2.circle(frame, (x, y), ripple_radius, color, 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_63_terrain_flyover(self, frame, magnitudes):
        """Mode 63: 3D wireframe terrain generated from waveform"""
        # Generate terrain heightmap from audio
        terrain_width = 50
        terrain_depth = 30

        # Use magnitudes to create terrain
        terrain = np.zeros((terrain_depth, terrain_width))
        for x in range(terrain_width):
            freq_idx = int((x / terrain_width) * len(magnitudes))
            terrain[:, x] = magnitudes[freq_idx] * 200

        # Draw 3D wireframe terrain
        scale = 15
        offset_x = self.width // 2
        offset_y = self.height - 200

        for z in range(terrain_depth - 1):
            for x in range(terrain_width - 1):
                # Current point
                x1 = int(offset_x + (x - terrain_width // 2) * scale)
                y1 = int(offset_y - terrain[z, x] - z * 10)

                # Next points
                x2 = int(offset_x + (x + 1 - terrain_width // 2) * scale)
                y2 = int(offset_y - terrain[z, x + 1] - z * 10)

                x3 = int(offset_x + (x - terrain_width // 2) * scale)
                y3 = int(offset_y - terrain[z + 1, x] - (z + 1) * 10)

                # Draw lines
                depth_factor = 1 - z / terrain_depth
                color = (int(100 * depth_factor), int(200 * depth_factor), int(100 * depth_factor))
                cv2.line(frame, (x1, y1), (x2, y2), color, 1, lineType=cv2.LINE_AA)
                cv2.line(frame, (x1, y1), (x3, y3), color, 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_64_string_art(self, frame, magnitudes):
        """Mode 64: Points on circle with lines between - modulated by frequencies"""
        num_points = min(len(magnitudes), 36)
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Calculate point positions (modulated by low freq)
        points = []
        for i in range(num_points):
            angle = (i / num_points) * 2 * np.pi
            magnitude = magnitudes[i] if i < len(magnitudes) else 0
            radius = int(self.max_radius * 0.8 * (1 + bass * 0.3))

            # Position modulation
            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)
            points.append((x, y))

        # Draw lines between points (mids and treble control count and color)
        num_lines = int(mids * 50 + treble * 100)
        for _ in range(num_lines):
            idx1 = np.random.randint(0, len(points))
            idx2 = np.random.randint(0, len(points))

            if idx1 != idx2:
                hue = int(treble * 180)
                alpha = 0.3
                color_hsv = np.array([[[hue, 200, int(255 * alpha)]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                cv2.line(frame, points[idx1], points[idx2], tuple(map(int, color)), 1, lineType=cv2.LINE_AA)

        # Draw points
        for point in points:
            cv2.circle(frame, point, 4, (255, 255, 255), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_65_fire_embers(self, frame, magnitudes):
        """Mode 65: Central fire with sparks flying on treble hits"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Central fire (low-mid frequencies)
        fire_height = int(bass * 300 + 100)
        fire_width = 150

        for i in range(20):
            flame_x = int(self.center_x + (np.random.random() - 0.5) * fire_width)
            flame_y = int(self.height - 100 - np.random.random() * fire_height)
            flame_size = int(20 + bass * 30)

            # Fire color gradient
            hue = int(10 + np.random.random() * 20)  # Orange-yellow
            saturation = 255
            value = 200 + int(np.random.random() * 55)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (flame_x, flame_y), flame_size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        # Emit sparks/embers on treble hits
        if treble > 0.5:
            for _ in range(int(treble * 30)):
                self.ember_particles.append({
                    'x': self.center_x + (np.random.random() - 0.5) * 100,
                    'y': self.height - 150,
                    'vx': (np.random.random() - 0.5) * 8,
                    'vy': -np.random.random() * 15 - 5,
                    'life': 1.0
                })

        # Update and draw embers
        new_embers = []
        for ember in self.ember_particles:
            ember['x'] += ember['vx']
            ember['y'] += ember['vy']
            ember['vy'] += 0.5  # Gravity
            ember['life'] -= 0.015

            if ember['life'] > 0 and ember['y'] < self.height:
                alpha = ember['life']
                color = (int(100 * alpha), int(150 * alpha), int(255 * alpha))
                cv2.circle(frame, (int(ember['x']), int(ember['y'])), 3, color, -1, lineType=cv2.LINE_AA)
                new_embers.append(ember)

        self.ember_particles = new_embers
        return frame


    def draw_mode_66_radial_kaleidoscope(self, frame, magnitudes):
        """Mode 66: Radial kaleidoscope with mirrored segments"""
        num_segments = 8
        avg_magnitude = np.mean(magnitudes)

        # Create one segment
        segment_angle = 2 * np.pi / num_segments

        # Draw particles in one segment
        for i, magnitude in enumerate(magnitudes[:30]):
            if magnitude > 0.2:
                angle = (i / 30) * segment_angle
                distance = 100 + magnitude * 300

                x = int(self.center_x + np.cos(angle) * distance)
                y = int(self.center_y + np.sin(angle) * distance)

                hue = int((i / 30) * 180)
                color_hsv = np.array([[[hue, 255, int(255 * magnitude)]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                # Draw in all mirrored segments
                for seg in range(num_segments):
                    seg_angle = seg * segment_angle + self.frame_counter * 0.02
                    rot_x = int(self.center_x + np.cos(angle + seg_angle) * distance)
                    rot_y = int(self.center_y + np.sin(angle + seg_angle) * distance)

                    size = int(5 + magnitude * 15)
                    cv2.circle(frame, (rot_x, rot_y), size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        # Pulsing zoom
        zoom = 1 + avg_magnitude * 0.3

        return frame


    def draw_mode_67_pulsing_jellyfish(self, frame, magnitudes):
        """Mode 67: Translucent jellyfish - bell pulses with bass, tentacles are waveforms"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        # Jellyfish bell (pulses with bass)
        bell_radius = int(80 + bass * 70)
        bell_y = self.center_y - 100

        # Draw semi-transparent bell
        overlay = frame.copy()
        cv2.ellipse(overlay, (self.center_x, bell_y), (bell_radius, int(bell_radius * 0.7)),
                   0, 0, 180, (150, 100, 255), -1, lineType=cv2.LINE_AA)
        cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)

        # Tentacles (waveforms for high frequencies)
        num_tentacles = 8
        for t in range(num_tentacles):
            tentacle_x_offset = (t - num_tentacles // 2) * 30
            points = []

            # Each tentacle reacts to a frequency band
            freq_start = t * len(magnitudes) // num_tentacles
            freq_end = (t + 1) * len(magnitudes) // num_tentacles
            tentacle_freqs = magnitudes[freq_start:freq_end]

            for i, magnitude in enumerate(tentacle_freqs):
                x = self.center_x + tentacle_x_offset + int(np.sin(i * 0.5 + self.frame_counter * 0.1) * 15)
                y = bell_y + bell_radius // 2 + i * 8 + int(magnitude * 50)
                points.append([x, y])

            if len(points) > 1:
                points_np = np.array(points, dtype=np.int32)
                cv2.polylines(frame, [points_np], False, (200, 150, 255), 3, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_68_orbital_system(self, frame, magnitudes):
        """Mode 68: Central sun with orbiting planets (mid-freq) and moons (treble)"""
        avg_magnitude = np.mean(magnitudes)
        mids = magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Central sun pulses
        sun_radius = int(40 + avg_magnitude * 40)
        cv2.circle(frame, (self.center_x, self.center_y), sun_radius, (100, 200, 255), -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, (self.center_x, self.center_y), sun_radius + 10, (150, 220, 255), 2, lineType=cv2.LINE_AA)

        # Planets orbit
        num_planets = min(len(mids), 6)
        for i in range(num_planets):
            magnitude = mids[i] if i < len(mids) else 0
            orbit_radius = 120 + i * 70
            angle = self.frame_counter * 0.02 * (1 + i * 0.3)

            planet_x = int(self.center_x + np.cos(angle) * orbit_radius)
            planet_y = int(self.center_y + np.sin(angle) * orbit_radius)
            planet_size = int(10 + magnitude * 25)

            # Planet color
            hue = int((i / num_planets) * 180)
            color_hsv = np.array([[[hue, 200, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (planet_x, planet_y), planet_size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

            # Moon orbits planet (treble)
            if treble > 0.4:
                moon_angle = self.frame_counter * 0.1
                moon_distance = planet_size + 20
                moon_x = int(planet_x + np.cos(moon_angle) * moon_distance)
                moon_y = int(planet_y + np.sin(moon_angle) * moon_distance)
                moon_size = int(3 + treble * 8)

                cv2.circle(frame, (moon_x, moon_y), moon_size, (200, 200, 200), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_69_spectrum_cube(self, frame, magnitudes):
        """Mode 69: Rotating 3D cube with different visualizers on each face"""
        self.cube_rotation += 0.02
        cube_size = 200

        # Simple 3D cube projection
        angle_x = self.cube_rotation
        angle_y = self.cube_rotation * 0.7

        # Cube vertices
        vertices_3d = [
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
        ]

        # Rotate and project
        vertices_2d = []
        for vx, vy, vz in vertices_3d:
            # Rotate around Y
            x = vx * np.cos(angle_y) - vz * np.sin(angle_y)
            z = vx * np.sin(angle_y) + vz * np.cos(angle_y)

            # Rotate around X
            y = vy * np.cos(angle_x) - z * np.sin(angle_x)
            z = vy * np.sin(angle_x) + z * np.cos(angle_x)

            # Project to 2D
            scale = cube_size / (3 + z)
            x2d = int(self.center_x + x * scale)
            y2d = int(self.center_y + y * scale)
            vertices_2d.append((x2d, y2d))

        # Draw cube edges
        edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
        for start, end in edges:
            color = (100, 200, 255)
            cv2.line(frame, vertices_2d[start], vertices_2d[end], color, 2, lineType=cv2.LINE_AA)

        # Draw bars on front face
        avg_magnitude = np.mean(magnitudes)
        face_center = ((vertices_2d[0][0] + vertices_2d[2][0]) // 2,
                      (vertices_2d[0][1] + vertices_2d[2][1]) // 2)
        bar_length = int(30 + avg_magnitude * 50)
        cv2.line(frame, face_center, (face_center[0], face_center[1] - bar_length), (255, 200, 100), 3)

        return frame


    def draw_mode_70_typographic_flow(self, frame, magnitudes):
        """Mode 70: Floating words with size based on bass, waviness on treble"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Spawn new words
        if self.frame_counter % 30 == 0:
            words = ['MUSIC', 'FLOW', 'VIBE', 'SOUND', 'WAVE', 'PULSE', 'RHYTHM']
            word = np.random.choice(words)
            font_scale = 1.0 + bass * 2.0

            self.typography_words.append({
                'word': word,
                'x': np.random.randint(100, self.width - 200),
                'y': self.height + 50,
                'vy': -2 - bass * 3,
                'font_scale': font_scale,
                'life': 1.0
            })

        # Update and draw words
        new_words = []
        for word_obj in self.typography_words:
            word_obj['y'] += word_obj['vy']
            word_obj['life'] -= 0.005

            if word_obj['life'] > 0 and word_obj['y'] > -100:
                # Waviness from treble
                wobble_x = int(np.sin(self.frame_counter * 0.1 + word_obj['y'] * 0.01) * treble * 30)
                x = int(word_obj['x'] + wobble_x)
                y = int(word_obj['y'])

                alpha = word_obj['life']
                color = (int(255 * alpha), int(200 * alpha), int(100 * alpha))

                cv2.putText(frame, word_obj['word'], (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                          word_obj['font_scale'], color, 3, lineType=cv2.LINE_AA)

                new_words.append(word_obj)

        self.typography_words = new_words[:20]
        return frame


    def draw_mode_71_sonar_ping(self, frame, magnitudes):
        """Mode 71: Circular radar sweep with frequency blips"""
        # Rotating sweep line
        sweep_angle = (self.frame_counter * 0.05) % (2 * np.pi)
        sweep_end_x = int(self.center_x + np.cos(sweep_angle) * self.max_radius)
        sweep_end_y = int(self.center_y + np.sin(sweep_angle) * self.max_radius)

        # Draw sweep line
        cv2.line(frame, (self.center_x, self.center_y), (sweep_end_x, sweep_end_y),
                (100, 255, 100), 2, lineType=cv2.LINE_AA)

        # Draw concentric circles (radar grid)
        for ring in range(1, 6):
            radius = int(self.max_radius * ring / 5)
            cv2.circle(frame, (self.center_x, self.center_y), radius, (50, 100, 50), 1, lineType=cv2.LINE_AA)

        # Frequency blips appear on radar
        for i, magnitude in enumerate(magnitudes):
            if magnitude > 0.4:
                # Radial distance based on frequency (low=center, high=edge)
                distance = int((i / len(magnitudes)) * self.max_radius)
                angle = sweep_angle + (np.random.random() - 0.5) * 0.5

                blip_x = int(self.center_x + np.cos(angle) * distance)
                blip_y = int(self.center_y + np.sin(angle) * distance)

                blip_size = int(3 + magnitude * 12)
                brightness = int(200 + magnitude * 55)
                cv2.circle(frame, (blip_x, blip_y), blip_size, (brightness, 255, brightness), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_72_vu_meters(self, frame, magnitudes):
        """Mode 72: Retro analog VU meters with needle physics"""
        # Split audio into Left/Right (use first and second half)
        left_magnitude = np.mean(magnitudes[:len(magnitudes)//2])
        right_magnitude = np.mean(magnitudes[len(magnitudes)//2:])

        # Smooth needle movement with physics
        target_left = -60 + left_magnitude * 120  # Angle in degrees
        target_right = -60 + right_magnitude * 120

        # Apply smoothing and overshoot
        self.vu_needle_positions[0] += (target_left - self.vu_needle_positions[0]) * 0.3
        self.vu_needle_positions[1] += (target_right - self.vu_needle_positions[1]) * 0.3

        # Draw VU meters
        meter_width = 300
        meter_height = 200

        for idx, (label, needle_angle) in enumerate(zip(['L', 'R'], self.vu_needle_positions)):
            center_x = self.width // 4 + idx * self.width // 2
            center_y = self.center_y

            # Draw meter face
            cv2.ellipse(frame, (center_x, center_y), (meter_width//2, meter_height//2),
                       0, 180, 360, (50, 50, 50), -1)
            cv2.ellipse(frame, (center_x, center_y), (meter_width//2, meter_height//2),
                       0, 180, 360, (200, 200, 200), 3, lineType=cv2.LINE_AA)

            # Draw scale marks
            for angle in range(-60, 61, 10):
                mark_angle_rad = np.radians(180 - angle)
                start_r = meter_width // 2 - 20
                end_r = meter_width // 2 - 10
                mark_start = (int(center_x + np.cos(mark_angle_rad) * start_r),
                            int(center_y - np.sin(mark_angle_rad) * start_r))
                mark_end = (int(center_x + np.cos(mark_angle_rad) * end_r),
                          int(center_y - np.sin(mark_angle_rad) * end_r))
                cv2.line(frame, mark_start, mark_end, (200, 200, 200), 2, lineType=cv2.LINE_AA)

            # Draw needle
            needle_angle_rad = np.radians(180 - needle_angle)
            needle_end = (int(center_x + np.cos(needle_angle_rad) * (meter_width//2 - 30)),
                         int(center_y - np.sin(needle_angle_rad) * (meter_width//2 - 30)))

            cv2.line(frame, (center_x, center_y), needle_end, (255, 100, 100), 4, lineType=cv2.LINE_AA)
            cv2.circle(frame, (center_x, center_y), 10, (150, 150, 150), -1, lineType=cv2.LINE_AA)

            # Label
            cv2.putText(frame, label, (center_x - 15, center_y + 80), cv2.FONT_HERSHEY_SIMPLEX,
                       2.0, (200, 200, 200), 3, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_73_lightning_cloud(self, frame, magnitudes):
        """Mode 73: Storm cloud that rumbles with bass, lightning on treble"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Cloud shape (top of screen, expanding with bass)
        cloud_height = int(150 + bass * 100)

        for i in range(20):
            cloud_x = int(np.random.random() * self.width)
            cloud_y = int(np.random.random() * cloud_height)
            cloud_size = int(30 + bass * 50)

            alpha = 0.3
            color = (int(30 * alpha), int(30 * alpha), int(50 * alpha))
            cv2.circle(frame, (cloud_x, cloud_y), cloud_size, color, -1, lineType=cv2.LINE_AA)

        # Lightning bolts on strong treble
        if treble > 0.65:
            # Generate lightning bolt path
            start_x = np.random.randint(self.width // 4, 3 * self.width // 4)
            start_y = cloud_height

            x, y = start_x, start_y
            points = [(x, y)]

            # Jagged lightning path
            for _ in range(int(5 + treble * 10)):
                x += int((np.random.random() - 0.5) * 80)
                y += int(40 + np.random.random() * 60)
                points.append((x, y))

            # Draw lightning
            for i in range(len(points) - 1):
                brightness = int(200 + treble * 55)
                cv2.line(frame, points[i], points[i+1], (brightness, brightness, 255), 4, lineType=cv2.LINE_AA)
                # Glow
                cv2.line(frame, points[i], points[i+1], (100, 100, 200), 12, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_74_bouncing_balls(self, frame, magnitudes):
        """Mode 74: Physics-based bouncing balls, one per frequency bin"""
        # Initialize balls if needed
        if len(self.bouncing_balls) == 0:
            for i in range(min(len(magnitudes), 30)):
                self.bouncing_balls.append({
                    'x': (i / 30) * self.width,
                    'y': self.height - 50,
                    'vy': 0,
                    'color_hue': int((i / 30) * 180)
                })

        gravity = 0.8

        # Update and draw balls
        for i, ball in enumerate(self.bouncing_balls):
            if i >= len(magnitudes):
                break

            magnitude = magnitudes[i]

            # Bounce based on amplitude
            if ball['y'] >= self.height - 50:
                ball['vy'] = -magnitude * 30 - 5  # Bounce up

            # Apply gravity
            ball['vy'] += gravity
            ball['y'] += ball['vy']

            # Keep ball in bounds
            if ball['y'] > self.height - 50:
                ball['y'] = self.height - 50
                ball['vy'] *= -0.7  # Energy loss

            # Draw ball
            ball_size = int(10 + magnitude * 20)
            color_hsv = np.array([[[ball['color_hue'], 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (int(ball['x']), int(ball['y'])), ball_size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_75_liquid_ink(self, frame, magnitudes):
        """Mode 75: Ink drops falling into water - bass=dark blooms, treble=bright splatters"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Bass hits create large ink blooms
        if bass > 0.4 and self.frame_counter % 15 == 0:
            self.ink_blooms.append({
                'x': np.random.randint(200, self.width - 200),
                'y': 100,
                'radius': 10,
                'max_radius': 150 + bass * 200,
                'life': 1.0,
                'hue': int(bass * 60)
            })

        # Treble creates small bright splatters
        if treble > 0.5:
            for _ in range(int(treble * 10)):
                self.ink_blooms.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'radius': 5,
                    'max_radius': 20 + treble * 40,
                    'life': 1.0,
                    'hue': int(120 + treble * 60)
                })

        # Update and draw blooms
        new_blooms = []
        for bloom in self.ink_blooms:
            bloom['radius'] += 2
            bloom['life'] -= 0.01

            if bloom['life'] > 0 and bloom['radius'] < bloom['max_radius']:
                alpha = bloom['life']
                color_hsv = np.array([[[bloom['hue'], 200, int(255 * alpha)]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                cv2.circle(frame, (int(bloom['x']), int(bloom['y'])), int(bloom['radius']),
                          tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
                new_blooms.append(bloom)

        self.ink_blooms = new_blooms[:100]
        return frame


    def draw_mode_76_stereo_landscape(self, frame, magnitudes):
        """Mode 76: 3D perspective - left channel left mountain, right channel right mountain"""
        # Split into stereo channels
        left_mags = magnitudes[:len(magnitudes)//2]
        right_mags = magnitudes[len(magnitudes)//2:]

        # Draw left landscape
        left_points = []
        for i, mag in enumerate(left_mags):
            x = int((i / len(left_mags)) * (self.width // 2))
            y = int(self.height - 100 - mag * 300)
            left_points.append([x, y])

        if len(left_points) > 1:
            left_points.append([self.width // 2, self.height])
            left_points.append([0, self.height])
            pts = np.array(left_points, dtype=np.int32)
            cv2.fillPoly(frame, [pts], (100, 150, 255), lineType=cv2.LINE_AA)
            cv2.polylines(frame, [pts[:len(left_mags)]], False, (150, 200, 255), 3, lineType=cv2.LINE_AA)

        # Draw right landscape
        right_points = []
        for i, mag in enumerate(right_mags):
            x = int(self.width // 2 + (i / len(right_mags)) * (self.width // 2))
            y = int(self.height - 100 - mag * 300)
            right_points.append([x, y])

        if len(right_points) > 1:
            right_points.append([self.width, self.height])
            right_points.append([self.width // 2, self.height])
            pts = np.array(right_points, dtype=np.int32)
            cv2.fillPoly(frame, [pts], (255, 150, 100), lineType=cv2.LINE_AA)
            cv2.polylines(frame, [pts[:len(right_mags)]], False, (255, 200, 150), 3, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_77_ai_latent_walk(self, frame, magnitudes):
        """Mode 77: Abstract latent space visualization (simulated)"""
        avg_magnitude = np.mean(magnitudes)
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Simulate latent walk with morphing shapes
        self.latent_morph_state += avg_magnitude * 0.1

        num_shapes = 15
        for i in range(num_shapes):
            # Position influenced by latent state
            angle = (i / num_shapes) * 2 * np.pi + self.latent_morph_state
            radius = 100 + np.sin(self.latent_morph_state + i) * 200

            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)

            # Morphing size
            size = int(20 + bass * 40 + np.sin(self.latent_morph_state * 2 + i) * 20)

            # Dream-like colors
            hue = int((self.latent_morph_state * 50 + i * 12) % 180)
            saturation = 180 + int(treble * 75)
            value = 150 + int(avg_magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw with transparency effect
            cv2.circle(frame, (x, y), size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_78_pixel_storm(self, frame, magnitudes):
        """Mode 78: Blizzard of 8-bit pixels - wind direction from stereo, speed from volume"""
        avg_magnitude = np.mean(magnitudes)

        # Stereo pan (L/R balance)
        left_power = np.mean(magnitudes[:len(magnitudes)//2])
        right_power = np.mean(magnitudes[len(magnitudes)//2:])
        wind_direction = (right_power - left_power) * 5

        # Spawn pixels
        if self.frame_counter % 2 == 0:
            for _ in range(int(avg_magnitude * 30 + 10)):
                # Dominant frequency determines color
                dominant_freq_idx = np.argmax(magnitudes)
                hue = int((dominant_freq_idx / len(magnitudes)) * 180)

                self.pixel_storm.append({
                    'x': np.random.random() * self.width,
                    'y': 0,
                    'vx': wind_direction + (np.random.random() - 0.5) * 3,
                    'vy': 3 + avg_magnitude * 5,
                    'hue': hue,
                    'life': 1.0
                })

        # Update and draw pixels
        new_pixels = []
        for pixel in self.pixel_storm:
            pixel['x'] += pixel['vx']
            pixel['y'] += pixel['vy']
            pixel['life'] -= 0.01

            if pixel['life'] > 0 and 0 < pixel['y'] < self.height:
                color_hsv = np.array([[[pixel['hue'], 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                # 8-bit pixel (small rectangle)
                pixel_size = 4
                cv2.rectangle(frame,
                            (int(pixel['x']), int(pixel['y'])),
                            (int(pixel['x']) + pixel_size, int(pixel['y']) + pixel_size),
                            tuple(map(int, color)), -1)
                new_pixels.append(pixel)

        self.pixel_storm = new_pixels[:400]
        return frame


    def draw_mode_79_growing_vine(self, frame, magnitudes):
        """Mode 79: Vine grows across screen, sprouts leaves on beats"""
        avg_magnitude = np.mean(magnitudes)
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        # Grow vine if not complete
        if len(self.vine_segments) < 200:
            if len(self.vine_segments) == 0:
                self.vine_segments.append({'x': 100, 'y': self.height - 100, 'leaves': []})
            else:
                last = self.vine_segments[-1]
                # Vine meanders
                angle = -np.pi/6 + (np.random.random() - 0.5) * np.pi/4
                new_x = last['x'] + np.cos(angle) * 15
                new_y = last['y'] + np.sin(angle) * 15

                if 0 < new_x < self.width and 0 < new_y < self.height:
                    self.vine_segments.append({'x': new_x, 'y': new_y, 'leaves': []})

                    # Sprout leaf on beat
                    if bass > 0.5:
                        leaf_size = int(10 + bass * 30)
                        self.vine_segments[-1]['leaves'].append({
                            'offset_x': (np.random.random() - 0.5) * 20,
                            'offset_y': (np.random.random() - 0.5) * 20,
                            'size': leaf_size
                        })

        # Draw vine
        for i in range(len(self.vine_segments) - 1):
            seg = self.vine_segments[i]
            next_seg = self.vine_segments[i + 1]
            cv2.line(frame, (int(seg['x']), int(seg['y'])), (int(next_seg['x']), int(next_seg['y'])),
                    (50, 120, 50), 3, lineType=cv2.LINE_AA)

            # Draw leaves
            for leaf in seg['leaves']:
                leaf_x = int(seg['x'] + leaf['offset_x'])
                leaf_y = int(seg['y'] + leaf['offset_y'])
                cv2.circle(frame, (leaf_x, leaf_y), leaf['size'], (100, 255, 100), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_80_haunted_faces(self, frame, magnitudes):
        """Mode 80: Ghostly faces fade in/out with mid-range (vocals), eyes glow on bass"""
        mid_range = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        # Face opacity controlled by mid-range (vocals)
        self.haunted_face_alpha = mid_range

        if self.haunted_face_alpha > 0.2:
            # Draw ghostly faces
            num_faces = 3
            for i in range(num_faces):
                face_x = int((i + 1) * self.width // (num_faces + 1))
                face_y = int(self.height // 3 + np.sin(self.frame_counter * 0.05 + i) * 50)
                face_size = 80

                alpha = self.haunted_face_alpha * 0.5

                # Face circle
                color = (int(200 * alpha), int(200 * alpha), int(220 * alpha))
                cv2.circle(frame, (face_x, face_y), face_size, color, -1, lineType=cv2.LINE_AA)

                # Eyes (glow on bass)
                eye_glow = 255 if bass > 0.6 else 100
                eye_offset = 25
                cv2.circle(frame, (face_x - eye_offset, face_y - 20), 12, (eye_glow, eye_glow, 50), -1, lineType=cv2.LINE_AA)
                cv2.circle(frame, (face_x + eye_offset, face_y - 20), 12, (eye_glow, eye_glow, 50), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_81_connecting_constellations(self, frame, magnitudes):
        """Mode 81: Stars that shine and connect when frequency threshold passed"""
        # Initialize stars
        if len(self.constellation_stars) == 0:
            for i in range(len(magnitudes)):
                self.constellation_stars.append({
                    'x': np.random.randint(50, self.width - 50),
                    'y': np.random.randint(50, self.height - 50),
                    'shining': False,
                    'freq_idx': i
                })

        # Update star brightness based on frequency
        shining_stars = []
        for star in self.constellation_stars:
            if star['freq_idx'] < len(magnitudes):
                magnitude = magnitudes[star['freq_idx']]
                star['shining'] = magnitude > 0.5

                if star['shining']:
                    shining_stars.append(star)
                    # Draw bright star
                    brightness = int(200 + magnitude * 55)
                    cv2.circle(frame, (star['x'], star['y']), 5, (brightness, brightness, 255), -1, lineType=cv2.LINE_AA)
                    # Glow
                    cv2.circle(frame, (star['x'], star['y']), 10, (100, 100, 200), 1, lineType=cv2.LINE_AA)
                else:
                    # Dim star
                    cv2.circle(frame, (star['x'], star['y']), 2, (80, 80, 100), -1, lineType=cv2.LINE_AA)

        # Draw connections between shining stars
        for i, star1 in enumerate(shining_stars):
            for star2 in shining_stars[i+1:]:
                # Connect nearby shining stars
                dist = np.sqrt((star1['x'] - star2['x'])**2 + (star1['y'] - star2['y'])**2)
                if dist < 200:
                    cv2.line(frame, (star1['x'], star1['y']), (star2['x'], star2['y']),
                            (100, 100, 200), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_82_matrix_rain(self, frame, magnitudes):
        """Mode 82: Matrix-style falling characters - speed from volume, brightness from treble"""
        avg_magnitude = np.mean(magnitudes)
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize columns
        if len(self.matrix_rain) == 0:
            num_columns = 60
            for i in range(num_columns):
                self.matrix_rain.append({
                    'x': int((i / num_columns) * self.width),
                    'y': np.random.randint(-100, 0),
                    'speed': 3 + np.random.random() * 5,
                    'chars': []
                })

        # Update and draw columns
        for column in self.matrix_rain:
            # Speed modulated by volume
            column['y'] += int(column['speed'] * (1 + avg_magnitude))

            if column['y'] > self.height:
                column['y'] = -100

            # Draw falling characters
            num_chars = 15
            for i in range(num_chars):
                char_y = int(column['y'] - i * 20)
                if 0 < char_y < self.height:
                    # Brightness flash from treble
                    brightness = int(150 - i * 8 + treble * 105)
                    brightness = max(50, min(255, brightness))

                    char = chr(np.random.randint(33, 127))
                    cv2.putText(frame, char, (column['x'], char_y), cv2.FONT_HERSHEY_SIMPLEX,
                              0.5, (50, brightness, 50), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_83_voxel_world(self, frame, magnitudes):
        """Mode 83: 3D voxel grid with audio shockwave"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        # Shockwave emanates from center
        shockwave_radius = int((self.frame_counter % 100) * (1 + bass) * 5)

        # Draw voxel grid
        voxel_size = 40
        for x in range(0, self.width, voxel_size):
            for y in range(0, self.height, voxel_size):
                # Distance from center
                dist = np.sqrt((x - self.center_x)**2 + (y - self.center_y)**2)

                # Shockwave effect
                if abs(dist - shockwave_radius) < 30:
                    # Voxel affected by shockwave
                    color_intensity = int(200 + bass * 55)
                    color = (color_intensity, 100, 100)
                else:
                    color = (50, 50, 80)

                cv2.rectangle(frame, (x, y), (x + voxel_size - 2, y + voxel_size - 2), color, -1)
                cv2.rectangle(frame, (x, y), (x + voxel_size - 2, y + voxel_size - 2), (100, 100, 120), 1)

        return frame


    def draw_mode_84_dna_helix_rungs(self, frame, magnitudes):
        """Mode 84: DNA helix where rungs light up with frequency"""
        self.dna_rotation += 2

        # Draw double helix strands
        num_points = 100
        for i in range(num_points):
            z = i / num_points
            y = int(z * self.height)
            angle = z * 4 * np.pi + np.radians(self.dna_rotation)

            # Strand 1
            x1 = int(self.center_x + np.cos(angle) * 100)
            cv2.circle(frame, (x1, y), 5, (100, 150, 255), -1, lineType=cv2.LINE_AA)

            # Strand 2 (opposite)
            x2 = int(self.center_x + np.cos(angle + np.pi) * 100)
            cv2.circle(frame, (x2, y), 5, (100, 150, 255), -1, lineType=cv2.LINE_AA)

            # Rungs (light up based on frequency)
            if i % 5 == 0:
                freq_idx = int((i / num_points) * len(magnitudes))
                if freq_idx >= len(magnitudes):
                    freq_idx = len(magnitudes) - 1

                magnitude = magnitudes[freq_idx]
                if magnitude > 0.3:
                    brightness = int(100 + magnitude * 155)
                    rung_color = (brightness, brightness, 200)
                    thickness = int(2 + magnitude * 6)
                    cv2.line(frame, (x1, y), (x2, y), rung_color, thickness, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_85_audio_reactive_shader(self, frame, magnitudes):
        """Mode 85: Full-screen procedural shader effect"""
        avg_magnitude = np.mean(magnitudes)
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        self.shader_time += 0.05 + avg_magnitude * 0.1

        # Generate procedural pattern (simplified Perlin-like noise)
        for y in range(0, self.height, 4):
            for x in range(0, self.width, 4):
                # UV coordinates
                u = x / self.width
                v = y / self.height

                # Noise pattern
                noise_val = np.sin(u * 10 + self.shader_time + bass * 5) * np.cos(v * 10 + self.shader_time)
                noise_val += np.sin(np.sqrt(u*u + v*v) * 20 - self.shader_time * 2) * treble

                # Color mapping (clamp to valid uint8 range)
                hue = np.clip(int((noise_val * 0.5 + 0.5) * 180), 0, 179)
                saturation = np.clip(200 + int(treble * 55), 0, 255)
                value = np.clip(int((noise_val * 0.5 + 0.5) * 200 + bass * 55), 0, 255)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                cv2.rectangle(frame, (x, y), (x+4, y+4), tuple(map(int, color)), -1)

        return frame


    def draw_mode_86_spirograph(self, frame, magnitudes):
        """Mode 86: Spirograph pattern - radii controlled by frequencies"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Spirograph parameters modulated by audio
        R = 150 + bass * 100  # Outer wheel radius
        r = 50 + mids * 50  # Inner wheel radius
        d = 30 + treble * 40  # Pen distance

        # Draw spirograph
        points = []
        for t in np.linspace(0, 2 * np.pi * 5, 500):
            x = int(self.center_x + (R - r) * np.cos(t) + d * np.cos((R - r) / r * t))
            y = int(self.center_y + (R - r) * np.sin(t) - d * np.sin((R - r) / r * t))

            if 0 <= x < self.width and 0 <= y < self.height:
                points.append([x, y])

        if len(points) > 1:
            points = np.array(points, dtype=np.int32)

            # Color based on treble
            hue = int(treble * 180)
            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.polylines(frame, [points], False, tuple(map(int, color)), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_87_equalizer_tower(self, frame, magnitudes):
        """Mode 87: 3D tower of stacked glowing rings"""
        num_rings = min(len(magnitudes), 40)
        ring_height = self.height // num_rings

        for i, magnitude in enumerate(magnitudes[:num_rings]):
            y = self.height - (i + 1) * ring_height
            radius = int(magnitude * (self.width // 3))

            # Color gradient
            hue = int((i / num_rings) * 180)
            saturation = 200 + int(magnitude * 55)
            value = 150 + int(magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Ring thickness
            thickness = int(2 + magnitude * 10)

            cv2.circle(frame, (self.center_x, y), radius, tuple(map(int, color)), thickness, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_88_audio_driven_doodles(self, frame, magnitudes):
        """Mode 88: Generative doodle bot - bass=90° turns, treble=shakiness"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize path
        if len(self.doodle_path) == 0:
            self.doodle_path = [{'x': self.center_x, 'y': self.center_y, 'angle': 0}]

        # Current position
        current = self.doodle_path[-1]

        # Bass hit causes 90° turn
        if bass > 0.6 and len(self.doodle_path) % 10 == 0:
            current['angle'] += np.pi / 2

        # Move forward
        step_size = 5 + mids * 5
        shakiness = treble * 10
        new_x = current['x'] + np.cos(current['angle']) * step_size + (np.random.random() - 0.5) * shakiness
        new_y = current['y'] + np.sin(current['angle']) * step_size + (np.random.random() - 0.5) * shakiness

        # Keep in bounds
        new_x = np.clip(new_x, 50, self.width - 50)
        new_y = np.clip(new_y, 50, self.height - 50)

        self.doodle_path.append({'x': new_x, 'y': new_y, 'angle': current['angle']})

        # Limit path length
        if len(self.doodle_path) > 500:
            self.doodle_path = self.doodle_path[-500:]

        # Draw path
        for i in range(len(self.doodle_path) - 1):
            p1 = self.doodle_path[i]
            p2 = self.doodle_path[i + 1]

            # Color based on mids
            hue = int(mids * 180)
            alpha = (i / len(self.doodle_path))
            color_hsv = np.array([[[hue, 200, int(255 * alpha)]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.line(frame, (int(p1['x']), int(p1['y'])), (int(p2['x']), int(p2['y'])),
                    tuple(map(int, color)), 3, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_89_firework_show(self, frame, magnitudes):
        """Mode 89: Bass launches rockets, they explode at peak with mid-range color"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Launch rockets on bass hits
        if bass > 0.55 and self.frame_counter % 10 == 0:
            self.firework_rockets.append({
                'x': np.random.randint(self.width // 4, 3 * self.width // 4),
                'y': self.height - 50,
                'vy': -10 - bass * 8,
                'exploded': False,
                'particles': []
            })

        # Update rockets
        new_rockets = []
        for rocket in self.firework_rockets:
            if not rocket['exploded']:
                rocket['y'] += rocket['vy']
                rocket['vy'] += 0.3  # Gravity

                # Draw rocket trail
                cv2.circle(frame, (int(rocket['x']), int(rocket['y'])), 5, (200, 200, 255), -1, lineType=cv2.LINE_AA)

                # Explode at peak
                if rocket['vy'] > 0:
                    rocket['exploded'] = True
                    # Create particle burst
                    for _ in range(int(50 + mids * 100)):
                        angle = np.random.random() * 2 * np.pi
                        speed = 2 + np.random.random() * 8
                        rocket['particles'].append({
                            'x': rocket['x'],
                            'y': rocket['y'],
                            'vx': np.cos(angle) * speed,
                            'vy': np.sin(angle) * speed,
                            'life': 1.0
                        })

            # Update explosion particles
            if rocket['exploded']:
                new_particles = []
                for particle in rocket['particles']:
                    particle['x'] += particle['vx']
                    particle['y'] += particle['vy']
                    particle['vy'] += 0.2  # Gravity
                    particle['life'] -= 0.015

                    if particle['life'] > 0:
                        # Color from mids
                        hue = int(mids * 180)
                        alpha = particle['life']
                        color_hsv = np.array([[[hue, 255, int(255 * alpha)]]], dtype=np.uint8)
                        color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                        size = int(2 + treble * 6)
                        cv2.circle(frame, (int(particle['x']), int(particle['y'])), size,
                                  tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
                        new_particles.append(particle)

                rocket['particles'] = new_particles
                if len(rocket['particles']) > 0:
                    new_rockets.append(rocket)

            else:
                new_rockets.append(rocket)

        self.firework_rockets = new_rockets[:20]
        return frame


    def draw_mode_90_microscopic_view(self, frame, magnitudes):
        """Mode 90: Cells jiggle and divide based on frequency"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        avg_magnitude = np.mean(magnitudes)

        # Initialize cells
        if len(self.microscopic_cells) == 0:
            for i in range(10):
                self.microscopic_cells.append({
                    'x': np.random.random() * self.width,
                    'y': np.random.random() * self.height,
                    'radius': 30 + np.random.random() * 30,
                    'vx': (np.random.random() - 0.5) * 2,
                    'vy': (np.random.random() - 0.5) * 2,
                    'freq_idx': i % len(magnitudes)
                })

        # Update cells
        new_cells = []
        for cell in self.microscopic_cells:
            freq_idx = cell['freq_idx'] % len(magnitudes)
            magnitude = magnitudes[freq_idx]

            # Jiggle (agitation from overall volume)
            jiggle_x = (np.random.random() - 0.5) * avg_magnitude * 10
            jiggle_y = (np.random.random() - 0.5) * avg_magnitude * 10

            cell['x'] += cell['vx'] + jiggle_x
            cell['y'] += cell['vy'] + jiggle_y

            # Bounce off walls
            if cell['x'] < cell['radius'] or cell['x'] > self.width - cell['radius']:
                cell['vx'] *= -1
            if cell['y'] < cell['radius'] or cell['y'] > self.height - cell['radius']:
                cell['vy'] *= -1

            # Divide when amplitude is high
            if magnitude > 0.7 and len(new_cells) < 50 and np.random.random() < 0.05:
                # Create daughter cell
                new_cells.append({
                    'x': cell['x'] + 20,
                    'y': cell['y'] + 20,
                    'radius': cell['radius'] * 0.7,
                    'vx': -cell['vx'],
                    'vy': -cell['vy'],
                    'freq_idx': freq_idx
                })
                cell['radius'] *= 0.7

            # Draw cell
            hue = int((freq_idx / len(magnitudes)) * 180)
            saturation = 200 + int(magnitude * 55)
            value = 150 + int(magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (int(cell['x']), int(cell['y'])), int(cell['radius']),
                      tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(cell['x']), int(cell['y'])), int(cell['radius']),
                      (200, 200, 200), 2, lineType=cv2.LINE_AA)

            new_cells.append(cell)

        self.microscopic_cells = new_cells[:50]
        return frame


    def draw_mode_91_burning_paper(self, frame, magnitudes):
        """Mode 91: Spectrum bars as flames, embers on high freq, paper curls on bass"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Draw flame bars
        bar_width = self.width // len(magnitudes)
        for i, magnitude in enumerate(magnitudes):
            bar_height = int(magnitude * self.height * 0.7)
            x = i * bar_width
            y_base = self.height - 50

            # Flame effect (multiple layers)
            for layer in range(3):
                y_offset = layer * 15
                layer_height = bar_height - y_offset
                if layer_height > 0:
                    y = y_base - layer_height

                    # Flame color gradient
                    hue = 10 + layer * 5  # Yellow to red
                    saturation = 255
                    value = 200 - layer * 40
                    color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                    color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                    # Flickering width
                    flicker = int((np.random.random() - 0.5) * 5)
                    cv2.rectangle(frame, (x + flicker, y), (x + bar_width - 2 + flicker, y_base),
                                tuple(map(int, color)), -1)

        # Embers on treble
        if treble > 0.5:
            for _ in range(int(treble * 20)):
                ember_x = np.random.randint(0, self.width)
                ember_y = self.height - 50 - np.random.randint(0, 100)
                cv2.circle(frame, (ember_x, ember_y), 2, (100, 150, 255), -1)

        # Paper curl effect on bass (darken corners)
        if bass > 0.4:
            curl_alpha = bass * 0.5
            overlay = frame.copy()
            pts = np.array([[0, 0], [int(self.width * 0.2), 0],
                          [0, int(self.height * 0.2)]], dtype=np.int32)
            cv2.fillPoly(overlay, [pts], (20, 20, 10))
            cv2.addWeighted(overlay, curl_alpha, frame, 1 - curl_alpha, 0, frame)

        return frame


    def draw_mode_92_swarm_intelligence(self, frame, magnitudes):
        """Mode 92: Boid flocking - cohesion/separation modulated by audio"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize boids
        if len(self.swarm_boids) == 0:
            for _ in range(40):
                self.swarm_boids.append({
                    'x': np.random.random() * self.width,
                    'y': np.random.random() * self.height,
                    'vx': (np.random.random() - 0.5) * 4,
                    'vy': (np.random.random() - 0.5) * 4
                })

        # Boid rules modulated by audio
        cohesion_factor = 0.01 * (1 - bass)  # Bass scatters
        separation_factor = 0.5 + treble * 1.5  # Treble aligns
        alignment_factor = 0.05 + treble * 0.1

        for boid in self.swarm_boids:
            # Calculate forces
            cohesion_x, cohesion_y = 0, 0
            separation_x, separation_y = 0, 0
            alignment_vx, alignment_vy = 0, 0
            neighbors = 0

            for other in self.swarm_boids:
                if other is boid:
                    continue

                dx = other['x'] - boid['x']
                dy = other['y'] - boid['y']
                dist = np.sqrt(dx**2 + dy**2) + 0.1

                if dist < 100:
                    # Cohesion
                    cohesion_x += dx
                    cohesion_y += dy

                    # Alignment
                    alignment_vx += other['vx']
                    alignment_vy += other['vy']

                    neighbors += 1

                if dist < 30:
                    # Separation
                    separation_x -= dx / dist
                    separation_y -= dy / dist

            if neighbors > 0:
                cohesion_x /= neighbors
                cohesion_y /= neighbors
                alignment_vx /= neighbors
                alignment_vy /= neighbors

            # Apply forces
            boid['vx'] += cohesion_x * cohesion_factor + separation_x * separation_factor + alignment_vx * alignment_factor
            boid['vy'] += cohesion_y * cohesion_factor + separation_y * separation_factor + alignment_vy * alignment_factor

            # Limit speed
            speed = np.sqrt(boid['vx']**2 + boid['vy']**2)
            max_speed = 5 + treble * 5
            if speed > max_speed:
                boid['vx'] = (boid['vx'] / speed) * max_speed
                boid['vy'] = (boid['vy'] / speed) * max_speed

            # Update position
            boid['x'] += boid['vx']
            boid['y'] += boid['vy']

            # Wrap around
            boid['x'] = boid['x'] % self.width
            boid['y'] = boid['y'] % self.height

            # Draw boid
            cv2.circle(frame, (int(boid['x']), int(boid['y'])), 5, (100, 200, 255), -1, lineType=cv2.LINE_AA)

            # Draw velocity direction
            end_x = int(boid['x'] + boid['vx'] * 3)
            end_y = int(boid['y'] + boid['vy'] * 3)
            cv2.line(frame, (int(boid['x']), int(boid['y'])), (end_x, end_y), (150, 220, 255), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_93_pendulum_wave(self, frame, magnitudes):
        """Mode 93: Multiple pendulums with slightly different periods - force from frequency"""
        num_pendulums = min(len(magnitudes), 30)

        # Initialize pendulum angles
        if len(self.pendulum_angles) == 0:
            self.pendulum_angles = [0.0] * num_pendulums

        # Update and draw pendulums
        for i in range(num_pendulums):
            magnitude = magnitudes[i] if i < len(magnitudes) else 0

            # Period slightly different for each pendulum
            period = 0.05 + i * 0.001

            # Force from audio
            self.pendulum_angles[i] += period + magnitude * 0.1

            # Pendulum position
            x_base = int((i / num_pendulums) * self.width)
            y_base = 100

            pendulum_length = 200 + magnitude * 100
            x_end = int(x_base + np.sin(self.pendulum_angles[i]) * pendulum_length)
            y_end = int(y_base + pendulum_length)

            # Draw rod
            cv2.line(frame, (x_base, y_base), (x_end, y_end), (150, 150, 150), 2, lineType=cv2.LINE_AA)

            # Draw bob
            bob_size = int(5 + magnitude * 15)
            hue = int((i / num_pendulums) * 180)
            color_hsv = np.array([[[hue, 200, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (x_end, y_end), bob_size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_94_retro_scanlines(self, frame, magnitudes):
        """Mode 94: Waveform on old CRT with scanlines and static"""
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Draw waveform
        points = []
        for i, magnitude in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * self.width)
            y = int(self.center_y + (magnitude - 0.5) * self.height * 0.6)
            points.append([x, y])

        if len(points) > 1:
            points_np = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [points_np], False, (100, 255, 100), 3, lineType=cv2.LINE_AA)

        # Scanlines
        for y in range(0, self.height, 4):
            cv2.line(frame, (0, y), (self.width, y), (0, 0, 0), 1)

        # Static/noise increases with treble
        if treble > 0.3:
            noise_intensity = int(treble * 50)
            for _ in range(noise_intensity):
                x = np.random.randint(0, self.width)
                y = np.random.randint(0, self.height)
                brightness = np.random.randint(100, 255)
                cv2.circle(frame, (x, y), 1, (brightness, brightness, brightness), -1)

        # CRT flicker
        self.crt_flicker = (self.crt_flicker + treble * 10) % 20
        if self.crt_flicker > 18:
            frame = cv2.add(frame, np.full_like(frame, 20))

        return frame


    def draw_mode_95_pulsing_polygon(self, frame, magnitudes):
        """Mode 95: Central polygon with vertices pushed by frequency bands"""
        num_vertices = min(len(magnitudes), 12)

        # Calculate vertex positions
        vertices = []
        for i in range(num_vertices):
            angle = (i / num_vertices) * 2 * np.pi
            magnitude = magnitudes[i] if i < len(magnitudes) else 0

            # Bass affects main vertices
            base_radius = self.max_radius * 0.5
            pushed_radius = base_radius + magnitude * 200

            # Treble adds spikes between
            x = int(self.center_x + np.cos(angle) * pushed_radius)
            y = int(self.center_y + np.sin(angle) * pushed_radius)
            vertices.append([x, y])

        # Draw filled polygon
        if len(vertices) > 2:
            pts = np.array(vertices, dtype=np.int32)
            avg_magnitude = np.mean(magnitudes)

            hue = int(self.frame_counter * 2 % 180)
            saturation = 200 + int(avg_magnitude * 55)
            value = 150 + int(avg_magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.fillPoly(frame, [pts], tuple(map(int, color)), lineType=cv2.LINE_AA)
            cv2.polylines(frame, [pts], True, (255, 255, 255), 3, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_96_chromatic_orb(self, frame, magnitudes):
        """Mode 96: 3D sphere with chromatic shader and moving light source"""
        avg_magnitude = np.mean(magnitudes)
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        # Light source moves with stereo pan
        left = np.mean(magnitudes[:len(magnitudes)//2])
        right = np.mean(magnitudes[len(magnitudes)//2:])

        self.chromatic_orb_rotation += (right - left) * 0.1
        light_angle = self.chromatic_orb_rotation
        light_x = np.cos(light_angle)
        light_y = np.sin(light_angle)

        # Draw orb
        orb_radius = int(150 + bass * 50)

        for angle in np.linspace(0, 2 * np.pi, 60):
            for radius_factor in np.linspace(0, 1, 20):
                radius = int(orb_radius * radius_factor)

                x = int(self.center_x + np.cos(angle) * radius)
                y = int(self.center_y + np.sin(angle) * radius)

                # Lighting calculation
                dot = np.cos(angle) * light_x + np.sin(angle) * light_y
                brightness = max(0, dot) * 200 + 55

                # Chromatic color
                hue = int((angle / (2 * np.pi) + radius_factor + self.frame_counter * 0.01) * 180) % 180
                saturation = 200 + int(avg_magnitude * 55)
                value = int(brightness)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                cv2.circle(frame, (x, y), 3, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_97_textured_bars(self, frame, magnitudes):
        """Mode 97: Bars filled with scrolling animated texture"""
        bar_width = self.width // len(magnitudes)

        for i, magnitude in enumerate(magnitudes):
            bar_height = int(magnitude * self.height * 0.7)
            x = i * bar_width
            y = self.height - bar_height

            # Scrolling texture (simulated with pattern)
            for ty in range(y, self.height, 5):
                scroll_offset = int((self.frame_counter * magnitude * 2) % 10)
                pattern_y = (ty + scroll_offset) % 10

                if pattern_y < 5:
                    color = (100 + int(magnitude * 155), 150, 200)
                else:
                    color = (50, 100, 150)

                cv2.line(frame, (x, ty), (x + bar_width - 2, ty), color, 2)

        return frame


    def draw_mode_98_voronoi_tessellation(self, frame, magnitudes):
        """Mode 98: Voronoi diagram with cells pulsing and seed points moving"""
        num_seeds = min(len(magnitudes), 20)
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        # Update seed positions (moved by low frequencies)
        if len(self.voronoi_seeds) == 0:
            for _ in range(num_seeds):
                self.voronoi_seeds.append({
                    'x': np.random.random() * self.width,
                    'y': np.random.random() * self.height
                })

        for i, seed in enumerate(self.voronoi_seeds[:num_seeds]):
            magnitude = magnitudes[i] if i < len(magnitudes) else 0
            # Seeds move slightly
            seed['x'] += (np.random.random() - 0.5) * bass * 5
            seed['y'] += (np.random.random() - 0.5) * bass * 5
            # Keep in bounds
            seed['x'] = np.clip(seed['x'], 0, self.width)
            seed['y'] = np.clip(seed['y'], 0, self.height)

        # Draw Voronoi cells (simplified - sample points)
        for y in range(0, self.height, 5):
            for x in range(0, self.width, 5):
                # Find closest seed
                min_dist = float('inf')
                closest_idx = 0

                for i, seed in enumerate(self.voronoi_seeds[:num_seeds]):
                    dist = (x - seed['x'])**2 + (y - seed['y'])**2
                    if dist < min_dist:
                        min_dist = dist
                        closest_idx = i

                # Color based on closest seed and its magnitude
                magnitude = magnitudes[closest_idx] if closest_idx < len(magnitudes) else 0
                hue = int((closest_idx / num_seeds) * 180)
                saturation = 200 + int(magnitude * 55)
                value = 100 + int(magnitude * 155)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                cv2.rectangle(frame, (x, y), (x+5, y+5), tuple(map(int, color)), -1)

        # Draw seed points
        for seed in self.voronoi_seeds[:num_seeds]:
            cv2.circle(frame, (int(seed['x']), int(seed['y'])), 6, (255, 255, 255), -1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_99_shattering_glass(self, frame, magnitudes):
        """Mode 99: Glass pane with cracks appearing on beats"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Glass pane (semi-transparent overlay)
        overlay = frame.copy()
        cv2.rectangle(overlay, (100, 100), (self.width - 100, self.height - 100),
                     (200, 220, 240), -1)
        cv2.addWeighted(overlay, 0.3, frame, 0.7, 0, frame)

        # Create cracks on strong beats
        if bass > 0.65 and len(self.glass_cracks) < 50:
            crack_center = (self.center_x + int((np.random.random() - 0.5) * 200),
                          self.center_y + int((np.random.random() - 0.5) * 200))

            # Radiating crack lines
            num_lines = int(4 + bass * 8)
            for _ in range(num_lines):
                angle = np.random.random() * 2 * np.pi
                length = 50 + bass * 150

                end_x = int(crack_center[0] + np.cos(angle) * length)
                end_y = int(crack_center[1] + np.sin(angle) * length)

                self.glass_cracks.append({
                    'start': crack_center,
                    'end': (end_x, end_y),
                    'complexity': treble
                })

        # Draw cracks
        for crack in self.glass_cracks:
            thickness = int(1 + crack['complexity'] * 3)
            cv2.line(frame, crack['start'], crack['end'], (50, 50, 50), thickness, lineType=cv2.LINE_AA)

        # Screen shake on impact
        if bass > 0.7:
            shake_x = int((np.random.random() - 0.5) * bass * 20)
            shake_y = int((np.random.random() - 0.5) * bass * 20)
            M = np.float32([[1, 0, shake_x], [0, 1, shake_y]])
            frame = cv2.warpAffine(frame, M, (self.width, self.height))

        return frame


    def draw_mode_100_sunrise_sunset(self, frame, magnitudes):
        """Mode 100: Gradient sky with pulsing sun and glittering stars"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Sky gradient (color mapped to mid-range)
        sky_hue = int(20 + mids * 100)  # Blue to orange
        for y in range(self.height):
            gradient_factor = y / self.height
            saturation = int(200 - gradient_factor * 100)
            value = int(255 - gradient_factor * 100)

            color_hsv = np.array([[[sky_hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.line(frame, (0, y), (self.width, y), tuple(map(int, color)), 1)

        # Sun/Moon (pulses with bass)
        self.sun_position = int(self.height * 0.3 + np.sin(self.frame_counter * 0.02) * 50)
        sun_radius = int(60 + bass * 50)

        sun_color = (100, 200, 255) if mids < 0.5 else (50, 150, 255)
        cv2.circle(frame, (self.center_x, self.sun_position), sun_radius, sun_color, -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, (self.center_x, self.sun_position), sun_radius + 10,
                  tuple(int(c * 0.7) for c in sun_color), 3, lineType=cv2.LINE_AA)

        # Stars glitter on treble (visible when dark)
        if mids < 0.3:
            num_stars = int(treble * 50 + 10)
            for _ in range(num_stars):
                star_x = np.random.randint(0, self.width)
                star_y = np.random.randint(0, self.height // 2)
                brightness = int(200 + treble * 55)

                cv2.circle(frame, (star_x, star_y), 2, (brightness, brightness, brightness), -1, lineType=cv2.LINE_AA)

        return frame


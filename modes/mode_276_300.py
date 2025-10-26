"""
Audio Spectrum Visualization Modes 276-300
Creative new visualizations to complete the 300 mode collection
"""
from .base import BaseModeVisualizer
import numpy as np
import cv2


class Modes276_300(BaseModeVisualizer):
    """Visualization modes 276 through 300"""

    def __init__(self, visualizer):
        super().__init__(visualizer)

    def draw_mode_276_quantum_lattice(self, frame, magnitudes):
        """3D-looking quantum lattice that shifts with bass"""
        bass = self.get_bass(magnitudes)
        self.quantum_phase = getattr(self, 'quantum_phase', 0) + 0.02
        spacing = 40
        depth = int(10 + bass * 15)

        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                z_offset = int(depth * np.sin(self.quantum_phase + x*0.01 + y*0.01))
                color_val = int(140 + z_offset * 4)
                cv2.circle(frame, (x + z_offset, y + z_offset), 3, (color_val, 160, 255), -1)

                # Connect to neighbors
                if x + spacing < self.width:
                    cv2.line(frame, (x + z_offset, y + z_offset),
                            (x + spacing + z_offset, y + z_offset), (100, 120, 200), 1)
                if y + spacing < self.height:
                    cv2.line(frame, (x + z_offset, y + z_offset),
                            (x + z_offset, y + spacing + z_offset), (100, 120, 200), 1)
        return frame

    def draw_mode_277_prism_rays(self, frame, magnitudes):
        """Light rays splitting through a prism"""
        energy = self.get_energy(magnitudes)
        self.prism_angle = getattr(self, 'prism_angle', 0) + 0.01

        num_rays = 7
        colors = [(255, 100, 100), (255, 180, 100), (255, 255, 100), (100, 255, 100),
                  (100, 200, 255), (100, 100, 255), (200, 100, 255)]

        for i in range(num_rays):
            angle = self.prism_angle + (i - 3) * 0.15
            spread = int(80 + energy * 100)
            x1 = int(self.center_x + np.cos(angle) * 50)
            y1 = int(self.center_y + np.sin(angle) * 50)
            x2 = int(self.center_x + np.cos(angle) * spread)
            y2 = int(self.center_y + np.sin(angle) * spread)
            cv2.line(frame, (x1, y1), (x2, y2), colors[i], 2, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_278_liquid_nitrogen(self, frame, magnitudes):
        """Freezing and shattering effects"""
        highs = self.get_highs(magnitudes)
        if not hasattr(self, 'ice_cracks'):
            self.ice_cracks = []

        # Add new cracks when highs spike
        if highs > 0.7 and len(self.ice_cracks) < 100:
            for _ in range(3):
                x = np.random.randint(0, self.width)
                y = np.random.randint(0, self.height)
                angle = np.random.random() * 2 * np.pi
                self.ice_cracks.append({'x': x, 'y': y, 'angle': angle, 'length': 0, 'max_len': 40})

        # Grow and draw cracks
        for crack in self.ice_cracks[:]:
            if crack['length'] < crack['max_len']:
                crack['length'] += 0.5
            x1, y1 = crack['x'], crack['y']
            x2 = int(x1 + np.cos(crack['angle']) * crack['length'])
            y2 = int(y1 + np.sin(crack['angle']) * crack['length'])
            cv2.line(frame, (x1, y1), (x2, y2), (200, 240, 255), 1, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_279_silk_road_caravan(self, frame, magnitudes):
        """Moving lights across the screen like a caravan"""
        mids = self.get_mids(magnitudes)
        if not hasattr(self, 'caravan_lights'):
            self.caravan_lights = []
            for i in range(12):
                self.caravan_lights.append({
                    'x': -50 - i * 30,
                    'y': self.center_y + np.random.randint(-60, 60),
                    'speed': 1.2 + i * 0.1
                })

        for light in self.caravan_lights:
            light['x'] += light['speed'] * (1 + mids * 0.5)
            if light['x'] > self.width + 50:
                light['x'] = -50
                light['y'] = self.center_y + np.random.randint(-60, 60)

            # Draw light with glow
            x, y = int(light['x']), int(light['y'])
            cv2.circle(frame, (x, y), 8, (255, 200, 100), -1)
            cv2.circle(frame, (x, y), 14, (255, 180, 80), 2)
        return frame

    def draw_mode_280_steampunk_gears(self, frame, magnitudes):
        """Rotating mechanical gears"""
        bass = self.get_bass(magnitudes)
        self.gear_angle = getattr(self, 'gear_angle', 0) + 0.02 + bass * 0.03

        # Draw multiple interlocking gears
        gears = [
            {'x': self.center_x - 80, 'y': self.center_y, 'r': 60, 'teeth': 12},
            {'x': self.center_x + 80, 'y': self.center_y, 'r': 60, 'teeth': 12},
            {'x': self.center_x, 'y': self.center_y - 100, 'r': 50, 'teeth': 10}
        ]

        for i, gear in enumerate(gears):
            angle_offset = self.gear_angle * (-1 if i % 2 else 1)
            cv2.circle(frame, (gear['x'], gear['y']), gear['r'], (180, 140, 100), 2)

            for t in range(gear['teeth']):
                angle = angle_offset + (t / gear['teeth']) * 2 * np.pi
                x1 = int(gear['x'] + np.cos(angle) * gear['r'])
                y1 = int(gear['y'] + np.sin(angle) * gear['r'])
                x2 = int(gear['x'] + np.cos(angle) * (gear['r'] + 10))
                y2 = int(gear['y'] + np.sin(angle) * (gear['r'] + 10))
                cv2.line(frame, (x1, y1), (x2, y2), (200, 160, 120), 3)
        return frame

    def draw_mode_281_dragon_scales(self, frame, magnitudes):
        """Overlapping scale patterns like dragon skin"""
        energy = self.get_energy(magnitudes)
        self.scale_phase = getattr(self, 'scale_phase', 0) + 0.01

        scale_size = int(25 + energy * 15)
        for y in range(-scale_size, self.height + scale_size, scale_size):
            for x in range(-scale_size, self.width + scale_size, scale_size * 2):
                offset_x = x + (scale_size if (y // scale_size) % 2 else 0)
                pulse = int(10 * np.sin(self.scale_phase + x * 0.01 + y * 0.01))
                hue = int((x + y + self.frame_counter) % 180)
                color = self.hsv_to_bgr(hue, 200, 200 + pulse)
                cv2.ellipse(frame, (offset_x, y), (scale_size, scale_size // 2),
                           0, 0, 180, color, 2)
        return frame

    def draw_mode_282_time_dilation_grid(self, frame, magnitudes):
        """Warped spacetime grid"""
        bass = self.get_bass(magnitudes)
        self.time_phase = getattr(self, 'time_phase', 0) + 0.02

        warp_strength = 30 + bass * 40
        spacing = 30

        for y in range(0, self.height, spacing):
            points = []
            for x in range(0, self.width, 10):
                dx = x - self.center_x
                dy = y - self.center_y
                dist = np.sqrt(dx*dx + dy*dy)
                warp = warp_strength * np.sin(self.time_phase + dist * 0.02)
                points.append((x, int(y + warp)))

            for i in range(len(points) - 1):
                cv2.line(frame, points[i], points[i+1], (160, 180, 255), 1)

        for x in range(0, self.width, spacing):
            points = []
            for y in range(0, self.height, 10):
                dx = x - self.center_x
                dy = y - self.center_y
                dist = np.sqrt(dx*dx + dy*dy)
                warp = warp_strength * np.sin(self.time_phase + dist * 0.02)
                points.append((int(x + warp), y))

            for i in range(len(points) - 1):
                cv2.line(frame, points[i], points[i+1], (160, 180, 255), 1)
        return frame

    def draw_mode_283_fiber_bundle(self, frame, magnitudes):
        """Mathematical fiber bundle visualization"""
        if not hasattr(self, 'fiber_paths'):
            self.fiber_paths = []
            for i in range(8):
                path = []
                for t in range(100):
                    angle = (t / 100) * 4 * np.pi + i * 0.5
                    r = 80 + 40 * np.sin(3 * angle)
                    x = int(self.center_x + r * np.cos(angle))
                    y = int(self.center_y + r * np.sin(angle))
                    path.append((x, y))
                self.fiber_paths.append(path)

        self.fiber_offset = getattr(self, 'fiber_offset', 0) + 1
        for path in self.fiber_paths:
            offset_path = path[self.fiber_offset % len(path):] + path[:self.fiber_offset % len(path)]
            for i in range(len(offset_path) - 1):
                cv2.line(frame, offset_path[i], offset_path[i+1], (180, 200, 255), 2, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_284_moth_wing_shimmer(self, frame, magnitudes):
        """Iridescent shimmer patterns like moth wings"""
        highs = self.get_highs(magnitudes)
        self.shimmer_phase = getattr(self, 'shimmer_phase', 0) + 0.05

        for i in range(40):
            t = i / 40
            angle = t * np.pi * 2
            distance = 120 + highs * 80

            for side in [-1, 1]:
                x = int(self.center_x + side * np.cos(angle) * distance)
                y = int(self.center_y + np.sin(angle) * distance * 0.6)

                hue = int((self.shimmer_phase + t * 180) % 180)
                sat = int(150 + highs * 100)
                color = self.hsv_to_bgr(hue, sat, 255)
                cv2.circle(frame, (x, y), 4, color, -1)
        return frame

    def draw_mode_285_cathedral_rose(self, frame, magnitudes):
        """Rose window geometry like a cathedral"""
        self.rose_angle = getattr(self, 'rose_angle', 0) + 0.005
        bass = self.get_bass(magnitudes)

        num_petals = 12
        radius = int(100 + bass * 60)

        for i in range(num_petals):
            angle = self.rose_angle + (i / num_petals) * 2 * np.pi
            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)
            cv2.circle(frame, (x, y), 30, (200, 160, 220), 2)
            cv2.line(frame, (self.center_x, self.center_y), (x, y), (180, 140, 200), 1)

        cv2.circle(frame, (self.center_x, self.center_y), radius, (220, 180, 240), 2)
        cv2.circle(frame, (self.center_x, self.center_y), 40, (240, 200, 255), 2)
        return frame

    def draw_mode_286_neon_veins_pulse(self, frame, magnitudes):
        """Pulsing vein-like network"""
        if not hasattr(self, 'vein_network'):
            self.vein_network = []
            # Create branching structure
            self.vein_network.append({
                'x1': self.center_x, 'y1': self.height,
                'x2': self.center_x, 'y2': self.center_y
            })
            for _ in range(30):
                base = self.vein_network[np.random.randint(0, len(self.vein_network))]
                angle = np.random.uniform(-np.pi/3, np.pi/3)
                length = np.random.uniform(30, 80)
                x1, y1 = base['x2'], base['y2']
                x2 = int(x1 + np.cos(angle - np.pi/2) * length)
                y2 = int(y1 + np.sin(angle - np.pi/2) * length)
                self.vein_network.append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})

        energy = self.get_energy(magnitudes)
        pulse = int(50 + energy * 150)

        for vein in self.vein_network:
            thickness = np.random.randint(1, 3)
            cv2.line(frame, (vein['x1'], vein['y1']), (vein['x2'], vein['y2']),
                    (pulse, 255, pulse), thickness, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_287_glacial_crack(self, frame, magnitudes):
        """Spreading ice crack patterns"""
        highs = self.get_highs(magnitudes)
        if not hasattr(self, 'glacial_cracks'):
            self.glacial_cracks = [{
                'x': self.center_x,
                'y': self.center_y,
                'branches': []
            }]
            # Create initial branches
            for _ in range(6):
                angle = np.random.random() * 2 * np.pi
                self.glacial_cracks[0]['branches'].append({
                    'angle': angle,
                    'length': 0,
                    'max_length': np.random.uniform(80, 160)
                })

        # Grow branches
        for crack in self.glacial_cracks:
            for branch in crack['branches']:
                if branch['length'] < branch['max_length']:
                    branch['length'] += 0.8 + highs * 1.5

                x1, y1 = crack['x'], crack['y']
                x2 = int(x1 + np.cos(branch['angle']) * branch['length'])
                y2 = int(y1 + np.sin(branch['angle']) * branch['length'])
                cv2.line(frame, (x1, y1), (x2, y2), (220, 240, 255), 2, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_288_quantum_dots(self, frame, magnitudes):
        """Floating quantum dot particles"""
        if not hasattr(self, 'quantum_dots'):
            self.quantum_dots = []
            for _ in range(150):
                self.quantum_dots.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'vx': np.random.uniform(-0.5, 0.5),
                    'vy': np.random.uniform(-0.5, 0.5),
                    'hue': np.random.randint(0, 180)
                })

        energy = self.get_energy(magnitudes)

        for dot in self.quantum_dots:
            dot['x'] = (dot['x'] + dot['vx']) % self.width
            dot['y'] = (dot['y'] + dot['vy']) % self.height

            size = int(2 + energy * 4)
            brightness = int(150 + energy * 100)
            color = self.hsv_to_bgr(dot['hue'], 255, brightness)
            cv2.circle(frame, (int(dot['x']), int(dot['y'])), size, color, -1)
        return frame

    def draw_mode_289_origami_crane_flight(self, frame, magnitudes):
        """Geometric origami birds in flight"""
        if not hasattr(self, 'origami_cranes'):
            self.origami_cranes = []
            for _ in range(8):
                self.origami_cranes.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'angle': np.random.random() * 2 * np.pi,
                    'flap': 0
                })

        bass = self.get_bass(magnitudes)

        for crane in self.origami_cranes:
            crane['x'] = (crane['x'] + 2) % self.width
            crane['y'] = int(crane['y'] + 15 * np.sin(self.frame_counter * 0.05 + crane['angle']))
            crane['flap'] += 0.2 + bass * 0.3

            wing_span = int(20 + 10 * np.sin(crane['flap']))
            x, y = int(crane['x']), int(crane['y']) % self.height

            # Simple crane shape
            pts = np.array([
                [x, y],
                [x - wing_span, y + 10],
                [x, y + 5],
                [x + wing_span, y + 10]
            ], np.int32)
            cv2.polylines(frame, [pts], True, (220, 200, 180), 2)
        return frame

    def draw_mode_290_magma_chamber(self, frame, magnitudes):
        """Bubbling lava effects"""
        if not hasattr(self, 'magma_bubbles'):
            self.magma_bubbles = []

        bass = self.get_bass(magnitudes)

        # Spawn new bubbles
        if len(self.magma_bubbles) < 50 and np.random.random() < 0.3:
            self.magma_bubbles.append({
                'x': np.random.randint(0, self.width),
                'y': self.height,
                'vy': -1.0 - bass * 2.0,
                'size': np.random.randint(5, 20),
                'hue': np.random.randint(0, 30)
            })

        for bubble in self.magma_bubbles[:]:
            bubble['y'] += bubble['vy']
            if bubble['y'] < -bubble['size']:
                self.magma_bubbles.remove(bubble)
                continue

            color = self.hsv_to_bgr(bubble['hue'], 255, 255)
            cv2.circle(frame, (int(bubble['x']), int(bubble['y'])),
                      bubble['size'], color, -1)
            cv2.circle(frame, (int(bubble['x']), int(bubble['y'])),
                      bubble['size'], (255, 200, 100), 1)
        return frame

    def draw_mode_291_spider_web_dew(self, frame, magnitudes):
        """Dew drops on spider web"""
        if not hasattr(self, 'web_initialized'):
            self.web_lines = []
            # Radial lines
            for i in range(12):
                angle = (i / 12) * 2 * np.pi
                self.web_lines.append({
                    'x1': self.center_x,
                    'y1': self.center_y,
                    'x2': int(self.center_x + np.cos(angle) * 200),
                    'y2': int(self.center_y + np.sin(angle) * 200)
                })
            # Circular lines
            for r in range(40, 220, 30):
                for i in range(60):
                    angle1 = (i / 60) * 2 * np.pi
                    angle2 = ((i+1) / 60) * 2 * np.pi
                    self.web_lines.append({
                        'x1': int(self.center_x + np.cos(angle1) * r),
                        'y1': int(self.center_y + np.sin(angle1) * r),
                        'x2': int(self.center_x + np.cos(angle2) * r),
                        'y2': int(self.center_y + np.sin(angle2) * r)
                    })
            self.web_initialized = True

        # Draw web
        for line in self.web_lines:
            cv2.line(frame, (line['x1'], line['y1']), (line['x2'], line['y2']),
                    (200, 200, 220), 1, lineType=cv2.LINE_AA)

        # Draw dew drops
        highs = self.get_highs(magnitudes)
        self.dew_shimmer = getattr(self, 'dew_shimmer', 0) + 0.1
        for i in range(30):
            angle = (i / 30) * 2 * np.pi
            r = 100 + (i % 3) * 40
            x = int(self.center_x + np.cos(angle) * r)
            y = int(self.center_y + np.sin(angle) * r)
            brightness = int(180 + 75 * np.sin(self.dew_shimmer + i))
            cv2.circle(frame, (x, y), 4, (brightness, brightness, 255), -1)
        return frame

    def draw_mode_292_nebula_birth(self, frame, magnitudes):
        """Gas cloud formation"""
        if not hasattr(self, 'nebula_particles'):
            self.nebula_particles = []
            for _ in range(400):
                angle = np.random.random() * 2 * np.pi
                dist = np.random.exponential(80)
                self.nebula_particles.append({
                    'x': self.center_x + np.cos(angle) * dist,
                    'y': self.center_y + np.sin(angle) * dist,
                    'vx': np.cos(angle) * 0.3,
                    'vy': np.sin(angle) * 0.3,
                    'hue': np.random.randint(120, 160)
                })

        bass = self.get_bass(magnitudes)

        for particle in self.nebula_particles:
            # Pull towards center
            dx = self.center_x - particle['x']
            dy = self.center_y - particle['y']
            dist = np.sqrt(dx*dx + dy*dy) + 0.01
            particle['vx'] += (dx / dist) * 0.01 * (1 - bass)
            particle['vy'] += (dy / dist) * 0.01 * (1 - bass)

            # Push outward with bass
            particle['vx'] += (particle['x'] - self.center_x) * 0.001 * bass
            particle['vy'] += (particle['y'] - self.center_y) * 0.001 * bass

            particle['x'] += particle['vx']
            particle['y'] += particle['vy']

            if 0 <= particle['x'] < self.width and 0 <= particle['y'] < self.height:
                color = self.hsv_to_bgr(particle['hue'], 200, 200)
                frame[int(particle['y']), int(particle['x'])] = color
        return frame

    def draw_mode_293_circuit_board_live(self, frame, magnitudes):
        """Live electric circuit patterns"""
        if not hasattr(self, 'circuit_initialized'):
            self.circuit_paths = []
            # Create circuit-like paths
            for _ in range(20):
                x = np.random.randint(0, self.width)
                y = np.random.randint(0, self.height)
                path = [(x, y)]
                for _ in range(np.random.randint(3, 8)):
                    if np.random.random() < 0.5:
                        x += np.random.randint(-60, 60)
                    else:
                        y += np.random.randint(-60, 60)
                    x = max(0, min(self.width - 1, x))
                    y = max(0, min(self.height - 1, y))
                    path.append((x, y))
                self.circuit_paths.append({'path': path, 'pulse': np.random.random()})
            self.circuit_initialized = True

        energy = self.get_energy(magnitudes)

        for circuit in self.circuit_paths:
            circuit['pulse'] += 0.05
            brightness = int(100 + 155 * (0.5 + 0.5 * np.sin(circuit['pulse'])) * energy)

            for i in range(len(circuit['path']) - 1):
                cv2.line(frame, circuit['path'][i], circuit['path'][i+1],
                        (100, brightness, 100), 2)

            # Draw nodes
            for point in circuit['path']:
                cv2.circle(frame, point, 3, (100, 255, 100), -1)
        return frame

    def draw_mode_294_bioluminescent_tide(self, frame, magnitudes):
        """Glowing wave patterns"""
        self.tide_phase = getattr(self, 'tide_phase', 0) + 0.03
        mids = self.get_mids(magnitudes)

        for y_offset in range(5):
            y_base = self.center_y + y_offset * 40 - 80
            points = []
            for x in range(0, self.width, 5):
                y = int(y_base + 30 * np.sin(self.tide_phase + x * 0.02 + y_offset * 0.5))
                points.append((x, y))

            # Draw wave
            for i in range(len(points) - 1):
                brightness = int(180 + mids * 75)
                hue = int((self.tide_phase * 10 + y_offset * 30) % 180)
                color = self.hsv_to_bgr(hue, 200, brightness)
                cv2.line(frame, points[i], points[i+1], color, 2, lineType=cv2.LINE_AA)

            # Sparkles on wave
            if np.random.random() < 0.3:
                x = np.random.randint(0, self.width)
                y = int(y_base + 30 * np.sin(self.tide_phase + x * 0.02 + y_offset * 0.5))
                cv2.circle(frame, (x, y), 3, (255, 255, 255), -1)
        return frame

    def draw_mode_295_tesseract_projection(self, frame, magnitudes):
        """4D hypercube projection"""
        self.tesseract_angle = getattr(self, 'tesseract_angle', 0) + 0.02
        bass = self.get_bass(magnitudes)

        # 4D rotation matrix projection to 3D to 2D
        size = 80 + bass * 40

        # Inner cube
        inner_pts = [
            (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
            (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
        ]

        # Outer cube (4th dimension)
        outer_pts = [(x * 1.6, y * 1.6, z * 1.6) for x, y, z in inner_pts]

        def project(x, y, z):
            # Simple rotation
            x2 = x * np.cos(self.tesseract_angle) - z * np.sin(self.tesseract_angle)
            z2 = x * np.sin(self.tesseract_angle) + z * np.cos(self.tesseract_angle)
            return (int(self.center_x + x2 * size), int(self.center_y + y * size))

        inner_2d = [project(*p) for p in inner_pts]
        outer_2d = [project(*p) for p in outer_pts]

        # Draw edges
        edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4),
                (0,4), (1,5), (2,6), (3,7)]

        for i, j in edges:
            cv2.line(frame, inner_2d[i], inner_2d[j], (200, 180, 255), 2)
            cv2.line(frame, outer_2d[i], outer_2d[j], (180, 160, 235), 2)
            cv2.line(frame, inner_2d[i], outer_2d[i], (160, 140, 215), 1)
        return frame

    def draw_mode_296_frost_crystal_growth(self, frame, magnitudes):
        """Growing ice crystals"""
        if not hasattr(self, 'frost_crystals'):
            self.frost_crystals = []

        highs = self.get_highs(magnitudes)

        # Spawn new crystal
        if len(self.frost_crystals) < 10 and np.random.random() < 0.05:
            self.frost_crystals.append({
                'x': np.random.randint(0, self.width),
                'y': np.random.randint(0, self.height),
                'size': 0,
                'angle': np.random.random() * 2 * np.pi
            })

        for crystal in self.frost_crystals:
            crystal['size'] += 0.5 + highs * 1.5

            # Draw 6-fold symmetric crystal
            for i in range(6):
                angle = crystal['angle'] + (i / 6) * 2 * np.pi
                x1 = int(crystal['x'] + np.cos(angle) * crystal['size'] * 0.5)
                y1 = int(crystal['y'] + np.sin(angle) * crystal['size'] * 0.5)
                x2 = int(crystal['x'] + np.cos(angle) * crystal['size'])
                y2 = int(crystal['y'] + np.sin(angle) * crystal['size'])

                if 0 <= x2 < self.width and 0 <= y2 < self.height:
                    cv2.line(frame, (int(crystal['x']), int(crystal['y'])), (x2, y2),
                            (220, 240, 255), 2, lineType=cv2.LINE_AA)
                    # Branches
                    branch_angle = angle + np.pi / 6
                    x3 = int(x1 + np.cos(branch_angle) * crystal['size'] * 0.3)
                    y3 = int(y1 + np.sin(branch_angle) * crystal['size'] * 0.3)
                    cv2.line(frame, (x1, y1), (x3, y3), (200, 220, 255), 1, lineType=cv2.LINE_AA)

        # Remove large crystals
        self.frost_crystals = [c for c in self.frost_crystals if c['size'] < 100]
        return frame

    def draw_mode_297_sound_wave_interference(self, frame, magnitudes):
        """Wave interference patterns"""
        self.wave_phase = getattr(self, 'wave_phase', 0) + 0.05

        # Two wave sources
        sources = [
            (self.center_x - 100, self.center_y),
            (self.center_x + 100, self.center_y)
        ]

        for y in range(0, self.height, 4):
            for x in range(0, self.width, 4):
                # Calculate wave interference
                total_wave = 0
                for sx, sy in sources:
                    dx = x - sx
                    dy = y - sy
                    dist = np.sqrt(dx*dx + dy*dy)
                    total_wave += np.sin(self.wave_phase + dist * 0.05)

                # Map to color
                intensity = int(127 + 127 * (total_wave / 2))
                frame[y:y+4, x:x+4] = (intensity, 160, 255)
        return frame

    def draw_mode_298_holographic_fracture(self, frame, magnitudes):
        """Broken hologram effect"""
        self.holo_glitch = getattr(self, 'holo_glitch', 0)
        highs = self.get_highs(magnitudes)

        if highs > 0.6:
            self.holo_glitch = 20

        if self.holo_glitch > 0:
            self.holo_glitch -= 1
            # RGB split effect
            shift = np.random.randint(-5, 5)
            frame_shifted = np.roll(frame, shift, axis=1)
            frame[:, :, 0] = frame_shifted[:, :, 0]
            frame[:, :, 2] = np.roll(frame[:, :, 2], -shift, axis=1)

        # Scanlines
        for y in range(0, self.height, 4):
            cv2.line(frame, (0, y), (self.width, y), (20, 20, 20), 1)

        # Glitch bars
        if np.random.random() < 0.1:
            y = np.random.randint(0, self.height - 20)
            frame[y:y+5, :] = 255
        return frame

    def draw_mode_299_plasma_ball_arc(self, frame, magnitudes):
        """Electric plasma arcs"""
        if not hasattr(self, 'plasma_arcs'):
            self.plasma_arcs = []

        energy = self.get_energy(magnitudes)

        # Generate new arcs
        if len(self.plasma_arcs) < 15:
            angle1 = np.random.random() * 2 * np.pi
            angle2 = angle1 + np.random.uniform(-np.pi/2, np.pi/2)
            self.plasma_arcs.append({
                'angle1': angle1,
                'angle2': angle2,
                'life': 20
            })

        for arc in self.plasma_arcs[:]:
            arc['life'] -= 1
            if arc['life'] <= 0:
                self.plasma_arcs.remove(arc)
                continue

            # Draw arc as bezier-like curve
            radius = 100 + energy * 60
            x1 = int(self.center_x + np.cos(arc['angle1']) * radius)
            y1 = int(self.center_y + np.sin(arc['angle1']) * radius)
            x2 = int(self.center_x + np.cos(arc['angle2']) * radius)
            y2 = int(self.center_y + np.sin(arc['angle2']) * radius)

            # Multiple segments for arc effect
            steps = 10
            for i in range(steps):
                t1 = i / steps
                t2 = (i + 1) / steps
                # Quadratic curve through center
                xa = int((1-t1)**2 * x1 + 2*(1-t1)*t1 * self.center_x + t1**2 * x2)
                ya = int((1-t1)**2 * y1 + 2*(1-t1)*t1 * self.center_y + t1**2 * y2)
                xb = int((1-t2)**2 * x1 + 2*(1-t2)*t2 * self.center_x + t2**2 * x2)
                yb = int((1-t2)**2 * y1 + 2*(1-t2)*t2 * self.center_y + t2**2 * y2)

                brightness = int((arc['life'] / 20) * 255)
                cv2.line(frame, (xa, ya), (xb, yb), (brightness, 200, 255), 2, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_300_eternal_flame_dance(self, frame, magnitudes):
        """Flowing fire patterns"""
        if not hasattr(self, 'flame_particles'):
            self.flame_particles = []

        bass = self.get_bass(magnitudes)

        # Spawn particles at bottom
        if len(self.flame_particles) < 200:
            for _ in range(5):
                self.flame_particles.append({
                    'x': self.center_x + np.random.randint(-40, 40),
                    'y': self.height - 20,
                    'vx': np.random.uniform(-0.5, 0.5),
                    'vy': -2.0 - bass * 2.0,
                    'life': 100,
                    'hue': np.random.randint(0, 30)
                })

        for particle in self.flame_particles[:]:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 1
            particle['vy'] -= 0.02  # Acceleration upward

            if particle['life'] <= 0 or particle['y'] < 0:
                self.flame_particles.remove(particle)
                continue

            size = max(1, int(4 * (particle['life'] / 100)))
            brightness = int(255 * (particle['life'] / 100))
            color = self.hsv_to_bgr(particle['hue'], 255, brightness)

            cv2.circle(frame, (int(particle['x']), int(particle['y'])), size, color, -1)
        return frame

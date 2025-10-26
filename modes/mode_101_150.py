"""
Audio Spectrum Visualization Modes 101-150
Auto-generated from audio_spectrum_creative.py
"""
from .base import BaseModeVisualizer
import numpy as np
import cv2


class Modes101_150(BaseModeVisualizer):
    """Visualization modes 101 through 150"""

    def __init__(self, visualizer):
        super().__init__(visualizer)
        # Mode-specific state initialization will be added here
        # This ensures backward compatibility with the original code

    def draw_mode_101_neural_pulse(self, frame, magnitudes):
        """Mode 101: Neural network with pulsing nodes and lighting connections"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize neural network nodes
        if len(self.neural_nodes) == 0:
            for i in range(30):
                self.neural_nodes.append({
                    'x': np.random.randint(100, self.width - 100),
                    'y': np.random.randint(100, self.height - 100),
                    'layer': i % 3,  # 3 layers
                    'active': 0
                })

        # Update node activation based on frequency bands
        for i, node in enumerate(self.neural_nodes):
            if node['layer'] == 0:  # Bottom layer - bass
                node['active'] = bass
            elif node['layer'] == 1:  # Middle layer - mids
                node['active'] = mids
            else:  # Top layer - treble
                node['active'] = treble

        # Draw connections that flash with amplitude
        for i, node1 in enumerate(self.neural_nodes):
            for j, node2 in enumerate(self.neural_nodes[i+1:], i+1):
                if abs(node1['layer'] - node2['layer']) == 1:  # Connect adjacent layers
                    intensity = int((node1['active'] + node2['active']) * 127.5)
                    if intensity > 50:
                        color = (intensity, int(intensity * 0.5), intensity + 50)
                        thickness = 1 if intensity < 150 else 2
                        cv2.line(frame, (node1['x'], node1['y']), (node2['x'], node2['y']),
                                color, thickness, lineType=cv2.LINE_AA)

        # Draw pulsing nodes
        for node in self.neural_nodes:
            radius = int(8 + node['active'] * 20)
            hue = int(140 + node['layer'] * 30)  # Purple to cyan
            intensity = int(200 + node['active'] * 55)

            color_hsv = np.array([[[hue, 255, intensity]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (node['x'], node['y']), radius, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (node['x'], node['y']), radius + 3, (255, 255, 255), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_102_liquid_mercury(self, frame, magnitudes):
        """Mode 102: Metallic liquid that ripples with physics"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Spawn mercury droplets on high treble
        if treble > 0.5 and self.frame_counter % 3 == 0:
            self.liquid_mercury_particles.append({
                'x': np.random.randint(100, self.width - 100),
                'y': 100,
                'vx': np.random.uniform(-2, 2),
                'vy': 0,
                'radius': int(10 + treble * 20)
            })

        # Bass creates large waves
        wave_offset = int(bass * 50)

        # Update and draw mercury particles
        for particle in self.liquid_mercury_particles[:]:
            particle['vy'] += 0.5  # Gravity
            particle['y'] += particle['vy']
            particle['x'] += particle['vx']

            # Boundary bouncing
            if particle['y'] > self.height - 100:
                particle['vy'] *= -0.7
                particle['y'] = self.height - 100

            if particle['x'] < 50 or particle['x'] > self.width - 50:
                particle['vx'] *= -0.7

            # Draw with metallic shading
            cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                      particle['radius'], (200, 200, 200), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(particle['x']) - 5, int(particle['y']) - 5),
                      particle['radius'] // 3, (255, 255, 255), -1, lineType=cv2.LINE_AA)  # Highlight

        # Clean up old particles
        self.liquid_mercury_particles = [p for p in self.liquid_mercury_particles if p['y'] < self.height]

        # Mid-range creates surface ripples
        for i in range(int(mids * 5)):
            ripple_x = self.center_x + int(np.sin(self.frame_counter * 0.1 + i) * 200)
            ripple_y = self.height - 100
            ripple_radius = int(30 + i * 20 + mids * 30)
            cv2.circle(frame, (ripple_x, ripple_y), ripple_radius, (150, 150, 150), 2, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_103_cosmic_strings(self, frame, magnitudes):
        """Mode 103: Vibrating strings in space like guitar strings"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize strings
        if len(self.cosmic_strings) == 0:
            for i in range(12):
                self.cosmic_strings.append({
                    'y': 100 + i * (self.height - 200) // 12,
                    'frequency': i + 1,
                    'magnitude': 0
                })

        # Update string vibrations
        for i, string in enumerate(self.cosmic_strings):
            string['magnitude'] = magnitudes[min(i * 10, len(magnitudes) - 1)]

        # Draw vibrating strings
        for string in self.cosmic_strings:
            points = []
            amplitude = int(string['magnitude'] * 100)

            for x in range(0, self.width, 10):
                wave = np.sin(x * 0.02 * string['frequency'] + self.frame_counter * 0.1)
                y = string['y'] + int(wave * amplitude)
                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            # Gold and white glowing strings
            hue = 30  # Gold
            intensity = int(200 + string['magnitude'] * 55)

            color_hsv = np.array([[[hue, 200, intensity]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.polylines(frame, [points], False, tuple(map(int, color)), 2, lineType=cv2.LINE_AA)

            # Add glow
            cv2.polylines(frame, [points], False, (255, 255, 255), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_104_particle_swarm(self, frame, magnitudes):
        """Mode 104: Thousands of particles forming shapes"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Spawn particles
        if len(self.particle_swarm) < 1000:
            for _ in range(10):
                angle = np.random.random() * 2 * np.pi
                distance = np.random.random() * 200
                self.particle_swarm.append({
                    'x': self.center_x + np.cos(angle) * distance,
                    'y': self.center_y + np.sin(angle) * distance,
                    'vx': 0,
                    'vy': 0,
                    'trail': []
                })

        # Bass creates circular formations
        target_radius = 150 + bass * 200

        # Update particle positions
        for particle in self.particle_swarm:
            dx = self.center_x - particle['x']
            dy = self.center_y - particle['y']
            distance = np.sqrt(dx*dx + dy*dy)

            if distance > 0:
                angle = np.arctan2(dy, dx)

                # Bass = circular, treble = scatter
                if bass > 0.5:
                    target_x = self.center_x + np.cos(angle) * target_radius
                    target_y = self.center_y + np.sin(angle) * target_radius
                else:
                    target_x = self.center_x + np.cos(angle + treble * np.pi) * (distance + treble * 100)
                    target_y = self.center_y + np.sin(angle + treble * np.pi) * (distance + treble * 100)

                particle['vx'] = (target_x - particle['x']) * 0.05
                particle['vy'] = (target_y - particle['y']) * 0.05

            particle['x'] += particle['vx']
            particle['y'] += particle['vy']

            # Update trail
            particle['trail'].append((int(particle['x']), int(particle['y'])))
            if len(particle['trail']) > 5:
                particle['trail'].pop(0)

            # Velocity-based color
            velocity = np.sqrt(particle['vx']**2 + particle['vy']**2)
            hue = int(120 - min(velocity * 50, 120))  # Blue to red

            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw trail
            if len(particle['trail']) > 1:
                pts = np.array(particle['trail'], dtype=np.int32)
                cv2.polylines(frame, [pts], False, tuple(map(int, color)), 1, lineType=cv2.LINE_AA)

            # Draw particle
            cv2.circle(frame, (int(particle['x']), int(particle['y'])), 2, tuple(map(int, color)), -1)

        return frame


    def draw_mode_105_crystal_lattice(self, frame, magnitudes):
        """Mode 105: 3D crystal structure with pulsing nodes"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])

        # Initialize crystal lattice nodes
        if len(self.crystal_lattice_nodes) == 0:
            grid_size = 5
            spacing = min(self.width, self.height) // (grid_size + 1)
            for i in range(grid_size):
                for j in range(grid_size):
                    for k in range(grid_size):
                        self.crystal_lattice_nodes.append({
                            'x3d': (i - grid_size//2) * spacing,
                            'y3d': (j - grid_size//2) * spacing,
                            'z3d': (k - grid_size//2) * spacing,
                            'magnitude': 0
                        })

        # Rotation angle
        angle = self.frame_counter * 0.02

        # Draw connections and nodes
        for i, node in enumerate(self.crystal_lattice_nodes):
            # Update magnitude from frequencies
            node['magnitude'] = magnitudes[min(i * 2, len(magnitudes) - 1)]

            # 3D rotation and projection
            x = node['x3d']
            y = node['y3d'] * np.cos(angle) - node['z3d'] * np.sin(angle)
            z = node['y3d'] * np.sin(angle) + node['z3d'] * np.cos(angle)

            x_rot = x * np.cos(angle) - z * np.sin(angle)
            z_rot = x * np.sin(angle) + z * np.cos(angle)

            # Perspective projection
            scale = 300 / (300 + z_rot)
            x_2d = int(self.center_x + x_rot * scale)
            y_2d = int(self.center_y + y * scale)

            node['x2d'] = x_2d
            node['y2d'] = y_2d
            node['z2d'] = z_rot

            # Draw node
            radius = int(5 + node['magnitude'] * 15)
            hue = int((z_rot + 300) / 600 * 180)  # Rainbow based on depth

            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (x_2d, y_2d), radius, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (x_2d, y_2d), radius + 2, (255, 255, 255), 1, lineType=cv2.LINE_AA)

        # Draw connections between nearby nodes
        for i, node1 in enumerate(self.crystal_lattice_nodes):
            for node2 in self.crystal_lattice_nodes[i+1:i+10]:
                dist = np.sqrt((node1['x3d'] - node2['x3d'])**2 +
                             (node1['y3d'] - node2['y3d'])**2 +
                             (node1['z3d'] - node2['z3d'])**2)

                if dist < 250:  # Only connect nearby nodes
                    intensity = int((node1['magnitude'] + node2['magnitude']) * 127.5)
                    if intensity > 30:
                        cv2.line(frame, (node1['x2d'], node1['y2d']),
                                (node2['x2d'], node2['y2d']),
                                (intensity, intensity, intensity + 50), 1, lineType=cv2.LINE_AA)

        return frame


    def draw_mode_106_aurora_waves(self, frame, magnitudes):
        """Mode 106: Aurora borealis flowing curtains"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Multiple aurora curtains
        num_curtains = 5
        for curtain_idx in range(num_curtains):
            offset = curtain_idx * 50

            # Create flowing wave points
            for x in range(0, self.width, 15):
                wave1 = np.sin(x * 0.01 + self.frame_counter * 0.05 + offset) * bass * 100
                wave2 = np.sin(x * 0.02 + self.frame_counter * 0.03 + offset) * mids * 80
                y_base = self.height // 3 + curtain_idx * 30

                # Color shifts with mids
                hue = int(60 + mids * 60 + curtain_idx * 20)  # Green to purple to blue
                saturation = int(200 + treble * 55)

                color_hsv = np.array([[[hue, saturation, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                # Draw vertical curtain strands
                for y_offset in range(0, 200, 10):
                    y = int(y_base + wave1 + wave2 + y_offset)
                    if 0 <= y < self.height:
                        alpha = 1.0 - (y_offset / 200) * 0.7
                        cv2.circle(frame, (x, y), 8,
                                  tuple(int(c * alpha) for c in color), -1, lineType=cv2.LINE_AA)

                # Sparkle effects on treble
                if treble > 0.6 and np.random.random() < treble:
                    sparkle_y = int(y_base + wave1 + np.random.randint(0, 100))
                    if 0 <= sparkle_y < self.height:
                        cv2.circle(frame, (x, sparkle_y), 3, (255, 255, 255), -1)

        return frame


    def draw_mode_107_dna_helix(self, frame, magnitudes):
        """Mode 107: Rotating DNA double helix with pulsing base pairs"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Rotation speed increases with amplitude
        self.dna_helix_rotation += 0.02 + bass * 0.05

        # Draw double helix
        for z in range(0, self.height, 10):
            angle1 = z * 0.05 + self.dna_helix_rotation
            angle2 = angle1 + np.pi

            # Helix radius pulses with bass
            radius = 100 + bass * 50

            # Strand 1
            x1 = int(self.center_x + np.cos(angle1) * radius)
            y1 = z

            # Strand 2
            x2 = int(self.center_x + np.cos(angle2) * radius)
            y2 = z

            # Backbone color
            cv2.circle(frame, (x1, y1), 5, (255, 100, 100), -1, lineType=cv2.LINE_AA)  # Blue
            cv2.circle(frame, (x2, y2), 5, (100, 255, 100), -1, lineType=cv2.LINE_AA)  # Green

            # Base pairs connecting strands
            if z % 20 == 0:
                freq_idx = (z // 20) % len(magnitudes)
                magnitude = magnitudes[freq_idx]

                if magnitude > 0.3:
                    # Color based on frequency
                    if freq_idx < len(magnitudes) // 4:
                        color = (100, 100, 255)  # Red (bass)
                    elif freq_idx < 3 * len(magnitudes) // 4:
                        color = (100, 255, 255)  # Yellow (mids)
                    else:
                        color = (255, 100, 100)  # Blue (treble)

                    thickness = 2 if magnitude > 0.6 else 1
                    cv2.line(frame, (x1, y1), (x2, y2), color, thickness, lineType=cv2.LINE_AA)

                    # Base pair nodes
                    mid_x = (x1 + x2) // 2
                    mid_y = (y1 + y2) // 2
                    cv2.circle(frame, (mid_x, mid_y), int(3 + magnitude * 5), color, -1)

        return frame


    def draw_mode_108_fractal_bloom(self, frame, magnitudes):
        """Mode 108: Fractal flower blooming and contracting"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Number of fractal iterations based on treble
        iterations = int(3 + treble * 4)

        # Draw recursive petals
        def draw_fractal_petal(x, y, size, angle, depth):
            if depth <= 0 or size < 5:
                return

            # Petal color based on depth
            hue = int(300 - depth * 40) % 180  # Pink to orange
            saturation = int(200 + mids * 55)
            value = int(200 + bass * 55)

            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw petal
            petal_points = []
            for i in range(8):
                petal_angle = angle + (i / 8) * 2 * np.pi
                px = int(x + np.cos(petal_angle) * size)
                py = int(y + np.sin(petal_angle) * size)
                petal_points.append([px, py])

            petal_points = np.array(petal_points, dtype=np.int32)
            cv2.fillPoly(frame, [petal_points], tuple(map(int, color)), lineType=cv2.LINE_AA)

            # Recursive smaller petals
            for i in range(5):
                new_angle = angle + (i / 5) * 2 * np.pi
                new_x = int(x + np.cos(new_angle) * size * 0.6)
                new_y = int(y + np.sin(new_angle) * size * 0.6)
                draw_fractal_petal(new_x, new_y, size * 0.4, new_angle, depth - 1)

        # Blooming size controlled by bass
        bloom_size = int(80 + bass * 150)
        draw_fractal_petal(self.center_x, self.center_y, bloom_size, self.frame_counter * 0.05, iterations)

        return frame


    def draw_mode_109_circuit_board(self, frame, magnitudes):
        """Mode 109: Electronic circuit with flowing electricity"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Green PCB background
        frame[:] = (20, 50, 20)

        # Initialize circuit traces
        if len(self.circuit_board_traces) == 0:
            for i in range(20):
                self.circuit_board_traces.append({
                    'points': [(np.random.randint(0, self.width), np.random.randint(0, self.height))
                              for _ in range(10)],
                    'active': 0,
                    'freq_idx': i
                })

        # Draw traces and electricity
        for trace in self.circuit_board_traces:
            magnitude = magnitudes[min(trace['freq_idx'] * 6, len(magnitudes) - 1)]
            trace['active'] = magnitude

            # Draw trace path (golden)
            for i in range(len(trace['points']) - 1):
                cv2.line(frame, trace['points'][i], trace['points'][i + 1],
                        (50, 150, 200), 3, lineType=cv2.LINE_AA)

            # Electricity flows when active
            if magnitude > 0.4:
                flow_pos = int((self.frame_counter * 0.1) % len(trace['points']))

                # Blue electricity spark
                if flow_pos < len(trace['points']):
                    x, y = trace['points'][flow_pos]
                    intensity = int(200 + magnitude * 55)
                    cv2.circle(frame, (x, y), int(8 + magnitude * 10),
                              (intensity, intensity // 2, 0), -1, lineType=cv2.LINE_AA)

                    # Glow
                    cv2.circle(frame, (x, y), int(15 + magnitude * 15),
                              (intensity // 2, intensity // 4, 0), 2, lineType=cv2.LINE_AA)

        # Spark effects on high treble
        if treble > 0.7:
            for _ in range(int(treble * 10)):
                sx = np.random.randint(0, self.width)
                sy = np.random.randint(0, self.height)
                cv2.circle(frame, (sx, sy), 2, (255, 200, 100), -1)

        return frame


    def draw_mode_110_quantum_field(self, frame, magnitudes):
        """Mode 110: Quantum probability field with wave function collapse"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Spawn quantum particles
        if len(self.quantum_field_particles) < 500:
            for _ in range(5):
                self.quantum_field_particles.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'state': np.random.random(),  # Quantum state
                    'collapsed': False
                })

        # Audio causes wave function collapse
        collapse_threshold = 0.5 + mids * 0.4

        # Update and draw particles
        for particle in self.quantum_field_particles:
            # Quantum fluctuation
            particle['state'] += (np.random.random() - 0.5) * 0.1
            particle['state'] = max(0, min(1, particle['state']))

            # Collapse on high amplitude
            if mids > collapse_threshold and not particle['collapsed']:
                particle['collapsed'] = True
            elif mids < 0.3:
                particle['collapsed'] = False

            # Interference patterns
            wave_x = np.sin(particle['x'] * 0.02 + self.frame_counter * 0.1) * bass * 20
            wave_y = np.sin(particle['y'] * 0.02 + self.frame_counter * 0.1) * bass * 20

            draw_x = int(particle['x'] + wave_x)
            draw_y = int(particle['y'] + wave_y)

            # Heatmap color based on probability
            if particle['collapsed']:
                # Bright when collapsed
                hue = 0  # Red
                intensity = 255
                radius = 4
            else:
                # Ghosted when in superposition
                hue = int(120 * particle['state'])  # Blue to red
                intensity = int(100 + particle['state'] * 155)
                radius = 2

            color_hsv = np.array([[[hue, 255, intensity]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            if 0 <= draw_x < self.width and 0 <= draw_y < self.height:
                cv2.circle(frame, (draw_x, draw_y), radius, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_111_origami_unfold(self, frame, magnitudes):
        """Mode 111: Geometric origami folding rhythmically"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        fold_amount = bass * 0.8 + 0.2
        num_segments = 8
        
        for i in range(num_segments):
            angle = (i / num_segments) * 2 * np.pi + self.frame_counter * 0.02
            size = 150 * fold_amount
            
            x1 = int(self.center_x + np.cos(angle) * size)
            y1 = int(self.center_y + np.sin(angle) * size)
            x2 = int(self.center_x + np.cos(angle + 0.5) * size * 0.7)
            y2 = int(self.center_y + np.sin(angle + 0.5) * size * 0.7)
            
            hue = int((i / num_segments) * 180)
            color_hsv = np.array([[[hue, int(200 + mids * 55), 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            points = np.array([[self.center_x, self.center_y], [x1, y1], [x2, y2]], dtype=np.int32)
            cv2.fillPoly(frame, [points], tuple(map(int, color)), lineType=cv2.LINE_AA)
            cv2.polylines(frame, [points], True, (50, 50, 50), 2, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_112_galaxy_spiral(self, frame, magnitudes):
        """Mode 112: Spiral galaxy with pulsing stars"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if len(self.galaxy_spiral_stars) < 500:
            for _ in range(10):
                angle = np.random.random() * 2 * np.pi
                distance = np.random.random() * 300
                self.galaxy_spiral_stars.append({'angle': angle, 'distance': distance, 'brightness': np.random.random()})
        
        spiral_tightness = 0.3 + bass * 0.2
        rotation = self.frame_counter * 0.01
        
        for star in self.galaxy_spiral_stars:
            spiral_angle = star['angle'] + star['distance'] * spiral_tightness + rotation
            x = int(self.center_x + np.cos(spiral_angle) * star['distance'])
            y = int(self.center_y + np.sin(spiral_angle) * star['distance'])
            
            brightness = int((star['brightness'] + mids) * 127.5)
            hue = int(140 - star['distance'] / 3)
            color_hsv = np.array([[[hue, 255, brightness]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            if 0 <= x < self.width and 0 <= y < self.height:
                size = 1 if star['distance'] > 200 else 2
                cv2.circle(frame, (x, y), size, tuple(map(int, color)), -1)
        
        cv2.circle(frame, (self.center_x, self.center_y), int(20 + bass * 30), (255, 255, 200), -1, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_113_rubber_bands(self, frame, magnitudes):
        """Mode 113: Vibrating rubber bands with physics"""
        if len(self.rubber_bands) == 0:
            for i in range(10):
                self.rubber_bands.append({
                    'y': 100 + i * (self.height - 200) // 10,
                    'tension': 0
                })
        
        for i, band in enumerate(self.rubber_bands):
            magnitude = magnitudes[min(i * 12, len(magnitudes) - 1)]
            band['tension'] = magnitude
            
            points = []
            for x in range(0, self.width, 10):
                wave = np.sin(x * 0.05 + self.frame_counter * 0.15 * (i + 1)) * band['tension'] * 80
                points.append([x, int(band['y'] + wave)])
            
            hue = int(i * 18)
            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            pts = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [pts], False, tuple(map(int, color)), 3, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_114_ink_diffusion(self, frame, magnitudes):
        """Mode 114: Ink diffusing in water"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if bass > 0.6 and self.frame_counter % 10 == 0:
            self.ink_diffusion_particles.append({
                'x': self.center_x,
                'y': self.center_y,
                'vx': np.random.uniform(-5, 5),
                'vy': np.random.uniform(-5, 5),
                'life': 100,
                'hue': int(np.random.random() * 40 + 120)
            })
        
        for particle in self.ink_diffusion_particles[:]:
            particle['x'] += particle['vx'] + np.random.uniform(-treble * 2, treble * 2)
            particle['y'] += particle['vy'] + np.random.uniform(-treble * 2, treble * 2)
            particle['vx'] *= 0.98
            particle['vy'] *= 0.98
            particle['life'] -= 1
            
            if particle['life'] > 0:
                alpha = particle['life'] / 100
                color_hsv = np.array([[[particle['hue'], 255, int(200 * alpha)]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                size = int((1 - alpha) * 30 + 5)
                cv2.circle(frame, (int(particle['x']), int(particle['y'])), size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
        
        self.ink_diffusion_particles = [p for p in self.ink_diffusion_particles if p['life'] > 0]
        return frame


    def draw_mode_115_geometric_kaleidoscope(self, frame, magnitudes):
        """Mode 115: Rotating kaleidoscope with morphing shapes"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        self.geo_kaleidoscope_rotation += 0.02 + mids * 0.05
        num_segments = 8
        
        for seg in range(num_segments):
            angle_offset = (seg / num_segments) * 2 * np.pi
            
            for layer in range(3):
                size = (layer + 1) * 60 * (1 + bass * 0.5)
                num_sides = 3 + int(mids * 3)
                
                points = []
                for i in range(num_sides):
                    angle = angle_offset + self.geo_kaleidoscope_rotation + (i / num_sides) * 2 * np.pi
                    x = int(self.center_x + np.cos(angle) * size)
                    y = int(self.center_y + np.sin(angle) * size)
                    points.append([x, y])
                
                hue = int((seg * 22.5 + layer * 60) % 180)
                color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                pts = np.array(points, dtype=np.int32)
                cv2.polylines(frame, [pts], True, tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_116_lightning_storm(self, frame, magnitudes):
        """Mode 116: Lightning bolts with branching"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (30, 30, 40)
        
        if bass > 0.7 and np.random.random() < 0.3:
            start_x = np.random.randint(100, self.width - 100)
            self.lightning_bolts.append({'x': start_x, 'y': 0, 'life': 5, 'branches': []})
        
        for bolt in self.lightning_bolts[:]:
            bolt['life'] -= 1
            
            if bolt['life'] > 0:
                segments = 20
                prev_x, prev_y = bolt['x'], bolt['y']
                
                for seg in range(segments):
                    next_y = prev_y + self.height // segments
                    next_x = prev_x + np.random.randint(-30, 30)
                    
                    cv2.line(frame, (prev_x, prev_y), (next_x, next_y), (255, 255, 200), 2, lineType=cv2.LINE_AA)
                    cv2.line(frame, (prev_x, prev_y), (next_x, next_y), (150, 150, 255), 1, lineType=cv2.LINE_AA)
                    
                    if treble > 0.5 and np.random.random() < 0.2:
                        branch_x = next_x + np.random.randint(-80, 80)
                        branch_y = next_y + np.random.randint(20, 60)
                        cv2.line(frame, (next_x, next_y), (branch_x, branch_y), (200, 200, 255), 1, lineType=cv2.LINE_AA)
                    
                    prev_x, prev_y = next_x, next_y
        
        self.lightning_bolts = [b for b in self.lightning_bolts if b['life'] > 0]
        return frame


    def draw_mode_117_cellular_growth(self, frame, magnitudes):
        """Mode 117: Biological cell division and growth"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if len(self.cellular_growth_cells) == 0:
            self.cellular_growth_cells.append({'x': self.center_x, 'y': self.center_y, 'size': 50, 'gen': 0})
        
        if bass > 0.7 and len(self.cellular_growth_cells) < 50:
            for cell in list(self.cellular_growth_cells):
                if np.random.random() < 0.1:
                    angle = np.random.random() * 2 * np.pi
                    new_x = cell['x'] + np.cos(angle) * cell['size']
                    new_y = cell['y'] + np.sin(angle) * cell['size']
                    self.cellular_growth_cells.append({'x': new_x, 'y': new_y, 'size': 30, 'gen': cell['gen'] + 1})
        
        for cell in self.cellular_growth_cells:
            cell['size'] = 20 + bass * 30
            
            hue = int(60 + cell['gen'] * 20) % 180
            color_hsv = np.array([[[hue, 200, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            cv2.circle(frame, (int(cell['x']), int(cell['y'])), int(cell['size']), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(cell['x']), int(cell['y'])), int(cell['size'] * 0.5), tuple(map(int, color * 0.7)), -1, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_118_sound_ribbons(self, frame, magnitudes):
        """Mode 118: 3D ribbons twisting through space"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        num_ribbons = 5
        for ribbon_idx in range(num_ribbons):
            points = []
            for t in range(100):
                angle = t * 0.1 + self.frame_counter * 0.02 + ribbon_idx
                radius = 100 + np.sin(t * 0.1) * 50 * bass
                
                x = int(self.center_x + np.cos(angle) * radius)
                y = int(t * (self.height / 100))
                points.append([x, y])
            
            hue = int(ribbon_idx * 36) % 180
            color_hsv = np.array([[[hue, 255, int(200 + mids * 55)]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            pts = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [pts], False, tuple(map(int, color)), int(8 + bass * 10), lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_119_matrix_rain(self, frame, magnitudes):
        """Mode 119: Matrix code rain"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (0, 0, 0)
        
        if len(self.matrix_rain_columns) == 0:
            for x in range(0, self.width, 20):
                self.matrix_rain_columns.append({'x': x, 'y': np.random.randint(-100, 0), 'speed': 5 + np.random.randint(0, 10)})
        
        for col in self.matrix_rain_columns:
            col['speed'] = 5 + bass * 10
            col['y'] += col['speed']
            
            if col['y'] > self.height:
                col['y'] = -20
            
            for i in range(15):
                y_pos = int(col['y'] - i * 20)
                if 0 <= y_pos < self.height:
                    brightness = int(255 - i * 17)
                    if i == 0:
                        color = (brightness, brightness, brightness)
                    else:
                        color = (0, brightness, 0)
                    
                    char = chr(33 + np.random.randint(0, 94))
                    cv2.putText(frame, char, (col['x'], y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        
        if treble > 0.7:
            for _ in range(int(treble * 5)):
                x = np.random.randint(0, self.width)
                y = np.random.randint(0, self.height)
                cv2.putText(frame, chr(33 + np.random.randint(0, 94)), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        return frame


    def draw_mode_120_fire_mandala(self, frame, magnitudes):
        """Mode 120: Circular mandala made of flames"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        num_flames = int(20 + treble * 30)
        
        for i in range(num_flames):
            angle = (i / num_flames) * 2 * np.pi + self.frame_counter * 0.05
            radius = 100 + bass * 150
            
            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)
            
            flame_height = int(40 + bass * 60)
            for h in range(flame_height):
                offset = np.sin(h * 0.2 + self.frame_counter * 0.2) * 10
                flame_x = int(x + offset)
                flame_y = int(y - h)
                
                intensity = 1 - (h / flame_height)
                if h < flame_height * 0.3:
                    color = (255, int(255 * intensity), int(100 * intensity))
                elif h < flame_height * 0.6:
                    color = (int(255 * intensity), int(200 * intensity), 0)
                else:
                    color = (int(255 * intensity), 0, 0)
                
                if 0 <= flame_x < self.width and 0 <= flame_y < self.height:
                    cv2.circle(frame, (flame_x, flame_y), 3, color, -1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_121_tessellation_shift(self, frame, magnitudes):
        """Mode 121: Escher-style morphing tessellations"""
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        tile_size = int(40 + mids * 20)
        for y in range(0, self.height, tile_size):
            for x in range(0, self.width, tile_size):
                shift = int(self.frame_counter * mids) % 3
                hue = int((x + y) / 10 + self.frame_counter) % 180
                color_hsv = np.array([[[hue, 200, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                if shift == 0:
                    cv2.rectangle(frame, (x, y), (x + tile_size, y + tile_size), tuple(map(int, color)), -1)
                elif shift == 1:
                    pts = np.array([[x, y + tile_size], [x + tile_size // 2, y], [x + tile_size, y + tile_size]], dtype=np.int32)
                    cv2.fillPoly(frame, [pts], tuple(map(int, color)))
                else:
                    cv2.circle(frame, (x + tile_size // 2, y + tile_size // 2), tile_size // 2, tuple(map(int, color)), -1)
                
                cv2.rectangle(frame, (x, y), (x + tile_size, y + tile_size), (0, 0, 0), 1)
        
        return frame


    def draw_mode_122_seismic_waves(self, frame, magnitudes):
        """Mode 122: Seismograph readings with P-waves and S-waves"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        for wave_idx in range(3):
            y_pos = 100 + wave_idx * (self.height - 200) // 3
            points = []
            
            for x in range(self.width):
                if wave_idx == 0:
                    y = y_pos + int(bass * 80 * np.sin(x * 0.05 + self.frame_counter * 0.2))
                elif wave_idx == 1:
                    y = y_pos + int(mids * 60 * np.sin(x * 0.08 + self.frame_counter * 0.15))
                else:
                    y = y_pos + int(treble * 40 * np.sin(x * 0.1 + self.frame_counter * 0.25))
                
                points.append([x, y])
            
            colors = [(0, 100, 255), (0, 255, 100), (255, 100, 0)]
            pts = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [pts], False, colors[wave_idx], 2, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_123_neon_city(self, frame, magnitudes):
        """Mode 123: Cyberpunk city with pulsing lights"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (80, 40, 80)
        
        if len(self.neon_city_buildings) == 0:
            for i in range(15):
                self.neon_city_buildings.append({
                    'x': i * self.width // 15,
                    'base_height': np.random.randint(100, 400),
                    'width': self.width // 16
                })
        
        for building in self.neon_city_buildings:
            height = int(building['base_height'] * (1 + bass * 0.5))
            cv2.rectangle(frame, (building['x'], self.height - height), 
                         (building['x'] + building['width'], self.height), (40, 20, 60), -1)
            
            num_windows = int(height / 20)
            for win_y in range(num_windows):
                if np.random.random() < mids:
                    win_color = (255, 100, 255) if np.random.random() < 0.5 else (100, 255, 255)
                    win_actual_y = self.height - height + win_y * 20
                    cv2.rectangle(frame, (building['x'] + 2, win_actual_y + 2),
                                (building['x'] + building['width'] - 2, win_actual_y + 15),
                                win_color, -1)
        
        return frame


    def draw_mode_124_magnetic_field(self, frame, magnitudes):
        """Mode 124: Magnetic field lines with particle clustering"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        pole_n = (self.width // 3, self.center_y)
        pole_s = (2 * self.width // 3, self.center_y)
        
        for line_idx in range(int(20 + mids * 20)):
            angle = (line_idx / 20) * np.pi - np.pi / 2
            points = []
            
            for t in range(100):
                t_norm = t / 100
                x = int(pole_n[0] + (pole_s[0] - pole_n[0]) * t_norm + np.sin(angle + t * 0.1) * 100 * bass)
                y = int(pole_n[1] + np.cos(angle + t * 0.1) * 150 * (1 - abs(t_norm - 0.5) * 2))
                points.append([x, y])
            
            pts = np.array(points, dtype=np.int32)
            color = (255, 100, 100) if angle < 0 else (100, 100, 255)
            cv2.polylines(frame, [pts], False, color, 1, lineType=cv2.LINE_AA)
        
        cv2.circle(frame, pole_n, 20, (255, 100, 100), -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, pole_s, 20, (100, 100, 255), -1, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_125_bubble_fusion(self, frame, magnitudes):
        """Mode 125: Bubbles that float, merge, and pop"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if bass > 0.5 and len(self.bubble_fusion_bubbles) < 30:
            self.bubble_fusion_bubbles.append({
                'x': self.center_x + np.random.randint(-100, 100),
                'y': self.height - 50,
                'vx': np.random.uniform(-1, 1),
                'vy': -2 - bass * 3,
                'radius': int(20 + bass * 40)
            })
        
        for bubble in self.bubble_fusion_bubbles[:]:
            bubble['vy'] -= 0.1
            bubble['x'] += bubble['vx']
            bubble['y'] += bubble['vy']
            bubble['vx'] *= 0.99
            
            if bubble['y'] < 0 or treble > 0.8:
                self.bubble_fusion_bubbles.remove(bubble)
                continue
            
            hue = int((bubble['y'] / self.height) * 180)
            color_hsv = np.array([[[hue, 100, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            cv2.circle(frame, (int(bubble['x']), int(bubble['y'])), bubble['radius'], tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(bubble['x'] - bubble['radius'] // 3), int(bubble['y'] - bubble['radius'] // 3)),
                      bubble['radius'] // 4, (255, 255, 255), -1, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_126_tribal_drums(self, frame, magnitudes):
        """Mode 126: Tribal patterns pulsing like drum skins"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        
        num_rings = int(5 + bass * 10)
        for ring in range(num_rings):
            radius = int(50 + ring * 40 * (1 + bass * 0.3))
            
            num_symbols = 8
            for sym in range(num_symbols):
                angle = (sym / num_symbols) * 2 * np.pi + self.frame_counter * 0.02
                x = int(self.center_x + np.cos(angle) * radius)
                y = int(self.center_y + np.sin(angle) * radius)
                
                symbol_size = int(15 + bass * 10)
                pts = np.array([
                    [x, y - symbol_size],
                    [x + symbol_size, y],
                    [x, y + symbol_size],
                    [x - symbol_size, y]
                ], dtype=np.int32)
                
                color = (int(100 + bass * 155), int(70 + bass * 100), 30)
                cv2.fillPoly(frame, [pts], color, lineType=cv2.LINE_AA)
                cv2.polylines(frame, [pts], True, (0, 0, 0), 2, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_127_glass_shatter(self, frame, magnitudes):
        """Mode 127: Glass forming and shattering"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if bass > 0.7 and len(self.glass_shatter_fragments) == 0:
            for _ in range(30):
                self.glass_shatter_fragments.append({
                    'x': self.center_x + np.random.randint(-200, 200),
                    'y': self.center_y + np.random.randint(-200, 200),
                    'vx': np.random.uniform(-5, 5),
                    'vy': np.random.uniform(-5, 5),
                    'size': np.random.randint(20, 50),
                    'life': 30
                })
        
        if len(self.glass_shatter_fragments) > 0:
            for frag in self.glass_shatter_fragments[:]:
                frag['x'] += frag['vx']
                frag['y'] += frag['vy']
                frag['vy'] += 0.3
                frag['life'] -= 1
                
                if frag['life'] > 0:
                    alpha = frag['life'] / 30
                    color = (int(200 * alpha), int(220 * alpha), int(255 * alpha))
                    
                    pts = np.array([
                        [int(frag['x']), int(frag['y'] - frag['size'])],
                        [int(frag['x'] + frag['size']), int(frag['y'])],
                        [int(frag['x']), int(frag['y'] + frag['size'])],
                        [int(frag['x'] - frag['size']), int(frag['y'])]
                    ], dtype=np.int32)
                    
                    cv2.fillPoly(frame, [pts], color, lineType=cv2.LINE_AA)
                    cv2.polylines(frame, [pts], True, (150, 150, 150), 1, lineType=cv2.LINE_AA)
            
            self.glass_shatter_fragments = [f for f in self.glass_shatter_fragments if f['life'] > 0]
        else:
            cv2.rectangle(frame, (self.center_x - 200, self.center_y - 200),
                         (self.center_x + 200, self.center_y + 200),
                         (200, 220, 255), -1, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_128_bioluminescence(self, frame, magnitudes):
        """Mode 128: Deep ocean bioluminescent creatures"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (20, 10, 0)
        
        if len(self.bioluminescent_creatures) < 20:
            self.bioluminescent_creatures.append({
                'x': np.random.randint(0, self.width),
                'y': np.random.randint(0, self.height),
                'phase': np.random.random() * 2 * np.pi,
                'speed': np.random.uniform(0.5, 2)
            })
        
        for creature in self.bioluminescent_creatures:
            creature['x'] += np.sin(self.frame_counter * 0.02 + creature['phase']) * creature['speed']
            creature['y'] += np.cos(self.frame_counter * 0.03 + creature['phase']) * creature['speed'] * 0.5
            
            if creature['x'] < 0: creature['x'] = self.width
            if creature['x'] > self.width: creature['x'] = 0
            if creature['y'] < 0: creature['y'] = self.height
            if creature['y'] > self.height: creature['y'] = 0
            
            glow_intensity = int(150 + np.sin(self.frame_counter * 0.1 + creature['phase']) * 50 + bass * 55)
            
            hue = int(90 + mids * 60)
            color_hsv = np.array([[[hue, 255, glow_intensity]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            size = int(15 + bass * 20)
            cv2.circle(frame, (int(creature['x']), int(creature['y'])), size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(creature['x']), int(creature['y'])), size + 10, tuple(map(int, color * 0.5)), 2, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_129_sound_architecture(self, frame, magnitudes):
        """Mode 129: Impossible architecture constructing/deconstructing"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        build_progress = bass
        
        for level in range(5):
            y_base = self.height - level * 100
            block_width = 150 - level * 20
            
            if level * 0.2 < build_progress:
                x = self.center_x - block_width // 2
                y = int(y_base - (1 - build_progress) * 50)
                
                shadow_offset = 10
                cv2.rectangle(frame, (x + shadow_offset, y + shadow_offset),
                            (x + block_width + shadow_offset, y_base + shadow_offset),
                            (30, 30, 30), -1)
                
                gray_value = int(100 + mids * 155)
                cv2.rectangle(frame, (x, y), (x + block_width, y_base),
                            (gray_value, gray_value, gray_value), -1)
                cv2.rectangle(frame, (x, y), (x + block_width, y_base),
                            (50, 50, 50), 3)
        
        return frame


    def draw_mode_130_plasma_ball(self, frame, magnitudes):
        """Mode 130: Plasma globe with electrical tendrils"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        center_radius = int(60 + bass * 40)
        cv2.circle(frame, (self.center_x, self.center_y), center_radius, (100, 50, 100), -1, lineType=cv2.LINE_AA)
        
        num_arcs = int(5 + treble * 15)
        for arc_idx in range(num_arcs):
            angle = (arc_idx / num_arcs) * 2 * np.pi + self.frame_counter * 0.1
            
            current_x, current_y = self.center_x, self.center_y
            segments = 20
            
            for seg in range(segments):
                next_angle = angle + np.random.uniform(-0.5, 0.5)
                distance = center_radius + seg * 15
                
                next_x = int(self.center_x + np.cos(next_angle) * distance)
                next_y = int(self.center_y + np.sin(next_angle) * distance)
                
                hue = int(120 + seg * 5)
                intensity = int(255 - seg * 10)
                color_hsv = np.array([[[hue, 255, intensity]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                cv2.line(frame, (current_x, current_y), (next_x, next_y), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
                
                current_x, current_y = next_x, next_y
                angle = next_angle
        
        return frame

    def draw_mode_131_sand_mandala(self, frame, magnitudes):
        """Mode 131: Tibetan sand mandala forming grain by grain"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        num_sections = 8
        for section in range(num_sections):
            angle_offset = (section / num_sections) * 2 * np.pi
            
            for radius_level in range(int(5 + mids * 10)):
                radius = 30 + radius_level * 20
                num_grains = int(radius * 0.5)
                
                for grain in range(num_grains):
                    angle = angle_offset + (grain / num_grains) * (2 * np.pi / num_sections)
                    x = int(self.center_x + np.cos(angle) * radius)
                    y = int(self.center_y + np.sin(angle) * radius)
                    
                    colors = [(0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0)]
                    color = colors[radius_level % len(colors)]
                    
                    cv2.circle(frame, (x, y), 1, color, -1)
        
        return frame


    def draw_mode_132_laser_show(self, frame, magnitudes):
        """Mode 132: Concert laser beams sweeping and bouncing"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (10, 10, 10)
        
        num_beams = int(3 + treble * 7)
        for beam_idx in range(num_beams):
            angle = (beam_idx / num_beams) * np.pi + np.sin(self.frame_counter * 0.05 + beam_idx) * 0.5
            
            start_x = self.center_x
            start_y = self.height
            end_x = int(self.center_x + np.cos(angle) * self.width)
            end_y = int(self.height - abs(np.sin(angle)) * self.height)
            
            beam_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (0, 255, 255)]
            color = beam_colors[beam_idx % len(beam_colors)]
            
            intensity = bass
            actual_color = tuple(int(c * intensity) for c in color)
            
            cv2.line(frame, (start_x, start_y), (end_x, end_y), actual_color, 3, lineType=cv2.LINE_AA)
            cv2.line(frame, (start_x, start_y), (end_x, end_y), (255, 255, 255), 1, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_133_coral_reef(self, frame, magnitudes):
        """Mode 133: Growing coral reef with swaying polyps"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        frame[:] = (100, 50, 20)
        
        if len(self.coral_reef_polyps) < 30:
            self.coral_reef_polyps.append({
                'x': np.random.randint(50, self.width - 50),
                'y': self.height - np.random.randint(50, 200),
                'height': np.random.randint(40, 100),
                'hue': np.random.randint(0, 180),
                'phase': np.random.random() * 2 * np.pi
            })
        
        for coral in self.coral_reef_polyps:
            sway = np.sin(self.frame_counter * 0.05 + coral['phase']) * 20 * mids
            
            for h in range(coral['height']):
                x = int(coral['x'] + sway * (h / coral['height']))
                y = coral['y'] - h
                
                size = int(5 + (coral['height'] - h) / coral['height'] * 15 * (1 + bass * 0.3))
                
                color_hsv = np.array([[[coral['hue'], 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                if 0 <= x < self.width and 0 <= y < self.height:
                    cv2.circle(frame, (x, y), size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_134_wireframe_morph(self, frame, magnitudes):
        """Mode 134: 3D wireframe objects morphing between shapes"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        shape_type = int(self.frame_counter * 0.01) % 4
        angle = self.frame_counter * 0.03
        
        vertices_3d = []
        size = 150 + bass * 100
        
        if shape_type == 0:  # Cube
            for x in [-1, 1]:
                for y in [-1, 1]:
                    for z in [-1, 1]:
                        vertices_3d.append([x * size, y * size, z * size])
        elif shape_type == 1:  # Sphere
            for lat in range(-90, 90, 30):
                for lon in range(0, 360, 30):
                    x = size * np.cos(np.radians(lat)) * np.cos(np.radians(lon))
                    y = size * np.cos(np.radians(lat)) * np.sin(np.radians(lon))
                    z = size * np.sin(np.radians(lat))
                    vertices_3d.append([x, y, z])
        elif shape_type == 2:  # Pyramid
            vertices_3d = [[0, -size, 0], [size, size, size], [-size, size, size], [-size, size, -size], [size, size, -size]]
        else:  # Torus
            for u in range(0, 360, 30):
                for v in range(0, 360, 60):
                    R, r = size * 0.8, size * 0.3
                    x = (R + r * np.cos(np.radians(v))) * np.cos(np.radians(u))
                    y = (R + r * np.cos(np.radians(v))) * np.sin(np.radians(u))
                    z = r * np.sin(np.radians(v))
                    vertices_3d.append([x, y, z])
        
        vertices_2d = []
        for v in vertices_3d:
            x = v[0] * np.cos(angle) - v[2] * np.sin(angle)
            z = v[0] * np.sin(angle) + v[2] * np.cos(angle)
            y = v[1]
            
            scale = 300 / (300 + z)
            x_2d = int(self.center_x + x * scale)
            y_2d = int(self.center_y + y * scale)
            vertices_2d.append((x_2d, y_2d))
        
        for i, v1 in enumerate(vertices_2d):
            for v2 in vertices_2d[i+1:i+5]:
                hue = int(100 + mids * 80)
                color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                cv2.line(frame, v1, v2, tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_135_sound_garden(self, frame, magnitudes):
        """Mode 135: Abstract garden with blooming flowers"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if len(self.sound_garden_plants) < 15:
            self.sound_garden_plants.append({
                'x': np.random.randint(100, self.width - 100),
                'y': self.height - 50,
                'height': np.random.randint(80, 200),
                'bloom_size': 0,
                'hue': np.random.randint(0, 180)
            })
        
        for plant in self.sound_garden_plants:
            plant['bloom_size'] = bass * 40 + 10
            
            cv2.line(frame, (plant['x'], plant['y']), (plant['x'], plant['y'] - plant['height']),
                    (50, 150, 50), 3, lineType=cv2.LINE_AA)
            
            bloom_x = plant['x']
            bloom_y = plant['y'] - plant['height']
            
            for petal in range(8):
                angle = (petal / 8) * 2 * np.pi
                petal_x = int(bloom_x + np.cos(angle) * plant['bloom_size'])
                petal_y = int(bloom_y + np.sin(angle) * plant['bloom_size'])
                
                color_hsv = np.array([[[plant['hue'], 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                cv2.circle(frame, (petal_x, petal_y), int(plant['bloom_size'] * 0.5),
                          tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
            
            cv2.circle(frame, (bloom_x, bloom_y), int(plant['bloom_size'] * 0.3),
                      (255, 255, 100), -1, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_136_hologram_glitch(self, frame, magnitudes):
        """Mode 136: Glitching holographic interface"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (10, 10, 10)
        
        for panel_idx in range(5):
            panel_x = 100 + panel_idx * (self.width - 200) // 5
            panel_y = 100 + int(np.sin(self.frame_counter * 0.05 + panel_idx) * 30 * mids)
            panel_w = 100
            panel_h = 150
            
            if treble > 0.7 and np.random.random() < 0.3:
                glitch_offset = np.random.randint(-20, 20)
                panel_x += glitch_offset
                
                r_offset = np.random.randint(-5, 5)
                cv2.rectangle(frame, (panel_x + r_offset, panel_y), (panel_x + panel_w + r_offset, panel_y + panel_h), (255, 0, 0), 1)
                cv2.rectangle(frame, (panel_x - r_offset, panel_y), (panel_x + panel_w - r_offset, panel_y + panel_h), (0, 255, 255), 1)
            else:
                cv2.rectangle(frame, (panel_x, panel_y), (panel_x + panel_w, panel_y + panel_h), (0, 255, 255), 2, lineType=cv2.LINE_AA)
                
                for line_idx in range(5):
                    line_y = panel_y + 30 + line_idx * 20
                    cv2.line(frame, (panel_x + 10, line_y), (panel_x + panel_w - 10, line_y), (255, 150, 0), 1)
        
        if treble > 0.6:
            for _ in range(int(treble * 20)):
                scan_y = np.random.randint(0, self.height)
                cv2.line(frame, (0, scan_y), (self.width, scan_y), (100, 255, 255), 1)
        
        return frame


    def draw_mode_137_pendulum_wave(self, frame, magnitudes):
        """Mode 137: Multiple pendulums creating wave patterns"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        num_pendulums = 20
        for i in range(num_pendulums):
            x = 50 + i * (self.width - 100) // num_pendulums
            
            period = 1.0 + i * 0.05
            angle = np.sin(self.frame_counter * 0.05 * period) * (0.5 + bass * 0.5)
            
            length = 150 + mids * 100
            bob_x = int(x + np.sin(angle) * length)
            bob_y = int(100 + np.cos(angle) * length)
            
            cv2.line(frame, (x, 100), (bob_x, bob_y), (200, 200, 200), 1, lineType=cv2.LINE_AA)
            
            hue = int((i / num_pendulums) * 180)
            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            cv2.circle(frame, (bob_x, bob_y), 10, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_138_volcano_eruption(self, frame, magnitudes):
        """Mode 138: Volcano erupting with lava and ash"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        volcano_base = [(self.center_x - 200, self.height), (self.center_x + 200, self.height), (self.center_x, self.height - 200)]
        pts = np.array(volcano_base, dtype=np.int32)
        cv2.fillPoly(frame, [pts], (80, 60, 40), lineType=cv2.LINE_AA)
        
        if bass > 0.6:
            for _ in range(int(bass * 20)):
                self.volcano_lava_particles.append({
                    'x': self.center_x + np.random.randint(-20, 20),
                    'y': self.height - 200,
                    'vx': np.random.uniform(-3, 3),
                    'vy': -8 - bass * 5,
                    'life': 60
                })
        
        for particle in self.volcano_lava_particles[:]:
            particle['vy'] += 0.3
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 1
            
            if particle['life'] > 0:
                if particle['vy'] < 0:
                    color = (0, int(100 + particle['life'] * 2), 255)
                else:
                    color = (0, int(particle['life'] * 3), int(100 + particle['life'] * 2))
                
                if 0 <= particle['x'] < self.width and 0 <= particle['y'] < self.height:
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])), 4, color, -1)
        
        self.volcano_lava_particles = [p for p in self.volcano_lava_particles if p['life'] > 0 and p['y'] < self.height]
        
        return frame


    def draw_mode_139_butterfly_effect(self, frame, magnitudes):
        """Mode 139: Chaos theory Lorenz attractor"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        sigma, rho, beta = 10.0, 28.0, 8.0/3.0
        dt = 0.01
        
        if len(self.butterfly_attractor_trail) == 0:
            self.butterfly_attractor_trail = [[0.1, 0.0, 0.0]]
        
        x, y, z = self.butterfly_attractor_trail[-1]
        
        dx = sigma * (y - x) * (1 + bass * 0.5)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        
        x += dx * dt
        y += dy * dt
        z += dz * dt
        
        self.butterfly_attractor_trail.append([x, y, z])
        
        if len(self.butterfly_attractor_trail) > 500:
            self.butterfly_attractor_trail.pop(0)
        
        for i in range(1, len(self.butterfly_attractor_trail)):
            x1, y1, z1 = self.butterfly_attractor_trail[i-1]
            x2, y2, z2 = self.butterfly_attractor_trail[i]
            
            px1 = int(self.center_x + x1 * 10)
            py1 = int(self.center_y + z1 * 10)
            px2 = int(self.center_x + x2 * 10)
            py2 = int(self.center_y + z2 * 10)
            
            hue = int((i / len(self.butterfly_attractor_trail)) * 180)
            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            if 0 <= px1 < self.width and 0 <= py1 < self.height and 0 <= px2 < self.width and 0 <= py2 < self.height:
                cv2.line(frame, (px1, py1), (px2, py2), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_140_silk_weaving(self, frame, magnitudes):
        """Mode 140: Silk threads weaving patterns"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        grid_size = 20
        for i in range(0, self.width, grid_size):
            vertical_offset = int(np.sin(i * 0.05 + self.frame_counter * 0.1) * 30 * bass)
            
            hue = int((i / self.width) * 180)
            color_hsv = np.array([[[hue, int(150 + mids * 105), 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            cv2.line(frame, (i, vertical_offset), (i, self.height + vertical_offset), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
        
        for j in range(0, self.height, grid_size):
            horizontal_offset = int(np.sin(j * 0.05 + self.frame_counter * 0.1) * 30 * mids)
            
            hue = int(60 + (j / self.height) * 120)
            color_hsv = np.array([[[hue, int(150 + bass * 105), 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            cv2.line(frame, (horizontal_offset, j), (self.width + horizontal_offset, j), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_141_clock_gears(self, frame, magnitudes):
        """Mode 141: Interlocking clockwork gears turning"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        gears = [
            {'x': self.width // 3, 'y': self.center_y, 'radius': 80, 'teeth': 12, 'speed': 1},
            {'x': 2 * self.width // 3, 'y': self.center_y, 'radius': 60, 'teeth': 9, 'speed': -1.33},
            {'x': self.center_x, 'y': self.center_y - 100, 'radius': 50, 'teeth': 8, 'speed': 1.5}
        ]
        
        for gear in gears:
            rotation = (self.frame_counter * 0.05 * gear['speed'] * (1 + bass * 0.5))
            
            for tooth in range(gear['teeth']):
                angle = rotation + (tooth / gear['teeth']) * 2 * np.pi
                
                inner_x = int(gear['x'] + np.cos(angle) * gear['radius'] * 0.8)
                inner_y = int(gear['y'] + np.sin(angle) * gear['radius'] * 0.8)
                outer_x = int(gear['x'] + np.cos(angle) * gear['radius'])
                outer_y = int(gear['y'] + np.sin(angle) * gear['radius'])
                
                cv2.line(frame, (inner_x, inner_y), (outer_x, outer_y), (150, 100, 50), 3, lineType=cv2.LINE_AA)
            
            cv2.circle(frame, (gear['x'], gear['y']), int(gear['radius'] * 0.7), (180, 130, 70), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (gear['x'], gear['y']), int(gear['radius'] * 0.3), (50, 50, 50), -1, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_142_smoke_signals(self, frame, magnitudes):
        """Mode 142: Rising smoke plumes forming patterns"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if self.frame_counter % 3 == 0:
            self.smoke_signal_particles.append({
                'x': self.center_x + np.random.randint(-50, 50),
                'y': self.height - 100,
                'vx': np.random.uniform(-1, 1),
                'vy': -2 - mids * 2,
                'size': 10,
                'life': 100
            })
        
        for particle in self.smoke_signal_particles[:]:
            particle['x'] += particle['vx'] + np.sin(self.frame_counter * 0.1) * treble * 2
            particle['y'] += particle['vy']
            particle['vy'] -= 0.05
            particle['size'] += 0.5
            particle['life'] -= 1
            
            if particle['life'] > 0:
                alpha = particle['life'] / 100
                gray = int(180 * alpha)
                
                if 0 <= particle['x'] < self.width and 0 <= particle['y'] < self.height:
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])), int(particle['size']),
                              (gray, gray, gray), -1, lineType=cv2.LINE_AA)
        
        self.smoke_signal_particles = [p for p in self.smoke_signal_particles if p['life'] > 0]
        
        return frame


    def draw_mode_143_stained_glass(self, frame, magnitudes):
        """Mode 143: Glowing stained glass window"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        pane_size = 80
        for y in range(0, self.height, pane_size):
            for x in range(0, self.width, pane_size):
                hue = int((x + y) / 10) % 180
                brightness = int(150 + bass * 105)
                
                color_hsv = np.array([[[hue, 200, brightness]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                cv2.rectangle(frame, (x, y), (x + pane_size, y + pane_size), tuple(map(int, color)), -1)
                cv2.rectangle(frame, (x, y), (x + pane_size, y + pane_size), (30, 30, 30), 4)
                
                light_x = x + pane_size // 4
                light_y = y + pane_size // 4
                cv2.circle(frame, (light_x, light_y), pane_size // 6, (255, 255, 255), -1, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_144_string_theory(self, frame, magnitudes):
        """Mode 144: Theoretical strings vibrating in multiple dimensions"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        num_strings = 30
        for string_idx in range(num_strings):
            points = []
            
            for t in range(100):
                x = t * (self.width / 100)
                
                y = self.center_y
                for harmonic in range(5):
                    amplitude = (bass + mids + treble) / 3 * 50 / (harmonic + 1)
                    frequency = (harmonic + 1) * (string_idx + 1) * 0.05
                    y += np.sin(x * frequency + self.frame_counter * 0.1) * amplitude
                
                points.append([int(x), int(y)])
            
            hue = int((string_idx / num_strings) * 180)
            alpha = 0.3 + treble * 0.7
            color_hsv = np.array([[[hue, 255, int(255 * alpha)]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            pts = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [pts], False, tuple(map(int, color)), 1, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_145_paper_craft(self, frame, magnitudes):
        """Mode 145: Paper cutouts folding into 3D shapes"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        fold_progress = (np.sin(self.frame_counter * 0.05) + 1) / 2 * bass
        
        colors_pastel = [(255, 200, 200), (200, 255, 200), (200, 200, 255), (255, 255, 200)]
        
        for i in range(4):
            angle = (i / 4) * 2 * np.pi
            size = 100 * (1 + fold_progress)
            
            x1 = int(self.center_x + np.cos(angle) * size)
            y1 = int(self.center_y + np.sin(angle) * size)
            x2 = int(self.center_x + np.cos(angle + 0.5) * size * 0.7)
            y2 = int(self.center_y + np.sin(angle + 0.5) * size * 0.7)
            
            pts = np.array([[self.center_x, self.center_y], [x1, y1], [x2, y2]], dtype=np.int32)
            cv2.fillPoly(frame, [pts], colors_pastel[i], lineType=cv2.LINE_AA)
            
            shadow_offset = int(5 * fold_progress)
            pts_shadow = pts + np.array([shadow_offset, shadow_offset])
            cv2.fillPoly(frame, [pts_shadow], (150, 150, 150), lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_146_northern_lights(self, frame, magnitudes):
        """Mode 146: Realistic aurora borealis dancing"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (20, 20, 40)
        
        num_bands = 5
        for band in range(num_bands):
            y_base = 100 + band * 60
            
            for x in range(0, self.width, 10):
                wave1 = np.sin(x * 0.01 + self.frame_counter * 0.05 + band) * bass * 50
                wave2 = np.sin(x * 0.02 + self.frame_counter * 0.03) * mids * 30
                
                y = int(y_base + wave1 + wave2)
                
                hue = int(60 + mids * 60 + band * 10)
                brightness = int(200 + treble * 55)
                color_hsv = np.array([[[hue, 200, brightness]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                for y_offset in range(40):
                    alpha = 1.0 - (y_offset / 40)
                    if 0 <= y + y_offset < self.height:
                        cv2.circle(frame, (x, y + y_offset), 5, tuple(int(c * alpha) for c in color), -1, lineType=cv2.LINE_AA)
        
        for _ in range(50):
            sx = np.random.randint(0, self.width)
            sy = np.random.randint(0, self.height // 2)
            cv2.circle(frame, (sx, sy), 1, (255, 255, 255), -1)
        
        return frame


    def draw_mode_147_cellular_automata(self, frame, magnitudes):
        """Mode 147: Conway's Game of Life with audio triggers"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        cell_size = 10
        grid_w = self.width // cell_size
        grid_h = self.height // cell_size
        
        if len(self.cellular_automata_grid) == 0:
            self.cellular_automata_grid = [[np.random.randint(0, 2) for _ in range(grid_w)] for _ in range(grid_h)]
        
        if self.frame_counter % 5 == 0:
            new_grid = [[0 for _ in range(grid_w)] for _ in range(grid_h)]
            
            for y in range(grid_h):
                for x in range(grid_w):
                    neighbors = 0
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            if dy == 0 and dx == 0:
                                continue
                            ny, nx = (y + dy) % grid_h, (x + dx) % grid_w
                            neighbors += self.cellular_automata_grid[ny][nx]
                    
                    if self.cellular_automata_grid[y][x] == 1:
                        new_grid[y][x] = 1 if neighbors in [2, 3] else 0
                    else:
                        new_grid[y][x] = 1 if neighbors == 3 else 0
            
            if bass > 0.7:
                for _ in range(int(bass * 50)):
                    rx, ry = np.random.randint(0, grid_w), np.random.randint(0, grid_h)
                    new_grid[ry][rx] = 1
            
            self.cellular_automata_grid = new_grid
        
        for y in range(grid_h):
            for x in range(grid_w):
                if self.cellular_automata_grid[y][x] == 1:
                    color = (0, int(200 + mids * 55), 0)
                    cv2.rectangle(frame, (x * cell_size, y * cell_size),
                                ((x + 1) * cell_size, (y + 1) * cell_size), color, -1)
        
        return frame


    def draw_mode_148_dragon_curve(self, frame, magnitudes):
        """Mode 148: Fractal dragon curve growing"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        iterations = int(3 + bass * 8)
        
        def dragon_curve(order):
            if order == 0:
                return "F"
            else:
                prev = dragon_curve(order - 1)
                return prev + "L" + prev[::-1].replace("L", "temp").replace("R", "L").replace("temp", "R") + "R"
        
        curve = dragon_curve(min(iterations, 12))
        
        x, y = self.center_x, self.center_y
        angle = 0
        step = max(2, 300 // (2 ** min(iterations, 10)))
        
        points = [(x, y)]
        for command in curve:
            if command == "F":
                x += int(np.cos(np.radians(angle)) * step)
                y += int(np.sin(np.radians(angle)) * step)
                points.append((x, y))
            elif command == "L":
                angle -= 90
            elif command == "R":
                angle += 90
        
        for i in range(1, len(points)):
            hue = int((i / len(points)) * 180)
            color_hsv = np.array([[[hue, 255, int(200 + mids * 55)]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            if (0 <= points[i-1][0] < self.width and 0 <= points[i-1][1] < self.height and
                0 <= points[i][0] < self.width and 0 <= points[i][1] < self.height):
                cv2.line(frame, points[i-1], points[i], tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
        
        return frame


    def draw_mode_149_rain_circles(self, frame, magnitudes):
        """Mode 149: Concentric circles like raindrops"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if treble > 0.5 and self.frame_counter % 10 == 0:
            self.rain_circle_ripples.append({
                'x': np.random.randint(0, self.width),
                'y': np.random.randint(0, self.height),
                'radius': 0,
                'life': 60
            })
        
        for ripple in self.rain_circle_ripples[:]:
            ripple['radius'] += 3 + bass * 2
            ripple['life'] -= 1
            
            if ripple['life'] > 0:
                alpha = ripple['life'] / 60
                color = (int(100 * alpha), int(200 * alpha), int(255 * alpha))
                
                cv2.circle(frame, (ripple['x'], ripple['y']), int(ripple['radius']), color, 2, lineType=cv2.LINE_AA)
        
        self.rain_circle_ripples = [r for r in self.rain_circle_ripples if r['life'] > 0]
        
        return frame


    def draw_mode_150_fourier_epicycles(self, frame, magnitudes):
        """Mode 150: Rotating circles tracing Fourier series"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        num_circles = int(5 + treble * 10)
        
        x, y = self.center_x, self.center_y - 100
        
        for i in range(num_circles):
            magnitude = magnitudes[min(i * 8, len(magnitudes) - 1)]
            radius = int(20 + magnitude * 50 * (num_circles - i) / num_circles)
            speed = (i + 1) * 0.1 + bass * 0.1
            angle = self.frame_counter * speed
            
            next_x = x + int(np.cos(angle) * radius)
            next_y = y + int(np.sin(angle) * radius)
            
            hue = int((i / num_circles) * 180)
            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            cv2.circle(frame, (x, y), radius, tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
            cv2.line(frame, (x, y), (next_x, next_y), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
            cv2.circle(frame, (next_x, next_y), 5, tuple(map(int, color)), -1)
            
            x, y = next_x, next_y
        
        if len(self.fourier_epicycles) < 200:
            self.fourier_epicycles.append((x, y))
        else:
            self.fourier_epicycles.pop(0)
            self.fourier_epicycles.append((x, y))
        
        for i in range(1, len(self.fourier_epicycles)):
            cv2.line(frame, self.fourier_epicycles[i-1], self.fourier_epicycles[i], (255, 255, 255), 2, lineType=cv2.LINE_AA)

        return frame



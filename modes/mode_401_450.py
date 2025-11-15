"""
Audio Spectrum Visualization Modes 401-450
Science & Physics Category (Part 1)
"""
from .base import BaseModeVisualizer
import numpy as np
import cv2


class Modes401_450(BaseModeVisualizer):
    """Visualization modes 401 through 450 - Science & Physics"""

    def __init__(self, visualizer):
        super().__init__(visualizer)

    def draw_mode_401_atom_model(self, frame, magnitudes):
        """Mode 401: Atomic orbital model with electrons"""
        # Nucleus
        cv2.circle(frame, (self.center_x, self.center_y), 15, (200, 100, 100), -1)

        # Electron orbitals
        num_orbitals = 3
        for orbital in range(num_orbitals):
            radius = 60 + orbital * 80
            tilt = orbital * 30

            mag_idx = orbital * len(magnitudes) // num_orbitals
            mag = magnitudes[mag_idx]

            # Orbital path
            cv2.ellipse(frame, (self.center_x, self.center_y),
                       (radius, int(radius * 0.3)), tilt, 0, 360,
                       (100, 100, 200), 2)

            # Electrons
            num_electrons = orbital + 2
            for e in range(num_electrons):
                angle = (e / num_electrons) * 2 * np.pi + self.frame_count * 0.05 * (orbital + 1)

                ex = int(self.center_x + np.cos(angle) * radius * np.cos(np.deg2rad(tilt)))
                ey = int(self.center_y + np.sin(angle) * radius * 0.3)

                size = 5 + int(mag * 10)
                cv2.circle(frame, (ex, ey), size, (100, 200, 255), -1)

        return frame

    def draw_mode_402_double_helix(self, frame, magnitudes):
        """Mode 402: DNA double helix structure"""
        # Two spiraling strands
        for i, mag in enumerate(magnitudes):
            t = (i / len(magnitudes)) * 4 * np.pi + self.frame_count * 0.05

            radius = 100
            y = int((i / len(magnitudes)) * self.height)

            # Strand 1
            x1 = int(self.center_x + np.cos(t) * radius)
            color1 = self.hsv_to_bgr(120, 200, 200)
            cv2.circle(frame, (x1, y), 5, color1, -1)

            # Strand 2
            x2 = int(self.center_x + np.cos(t + np.pi) * radius)
            color2 = self.hsv_to_bgr(0, 200, 200)
            cv2.circle(frame, (x2, y), 5, color2, -1)

            # Base pairs (connecting rungs)
            if i % 5 == 0:
                cv2.line(frame, (x1, y), (x2, y), (150, 150, 150), 2)

        return frame

    def draw_mode_403_magnetic_field(self, frame, magnitudes):
        """Mode 403: Magnetic field lines"""
        # Two poles
        pole1_x = int(self.width * 0.3)
        pole2_x = int(self.width * 0.7)
        pole_y = self.center_y

        cv2.circle(frame, (pole1_x, pole_y), 20, (255, 100, 100), -1)  # N pole
        cv2.circle(frame, (pole2_x, pole_y), 20, (100, 100, 255), -1)  # S pole

        # Field lines
        for i, mag in enumerate(magnitudes[::3]):
            offset = (i - 20) * 15

            # Curved field lines
            points = []
            for t in np.linspace(0, 1, 30):
                x = pole1_x + t * (pole2_x - pole1_x)
                curve = np.sin(t * np.pi) * (100 + mag * 50 + offset)
                y = pole_y + curve

                points.append([int(x), int(y)])

            points = np.array(points, dtype=np.int32)

            for j in range(len(points) - 1):
                cv2.line(frame, tuple(points[j]), tuple(points[j + 1]), (150, 150, 200), 1)

        return frame

    def draw_mode_404_wave_interference(self, frame, magnitudes):
        """Mode 404: Wave interference patterns"""
        # Two wave sources
        source1 = (int(self.width * 0.4), self.center_y)
        source2 = (int(self.width * 0.6), self.center_y)

        bass = self.get_bass(magnitudes)

        # Draw interference pattern
        for y in range(0, self.height, 8):
            for x in range(0, self.width, 8):
                # Distance from each source
                d1 = np.sqrt((x - source1[0])**2 + (y - source1[1])**2)
                d2 = np.sqrt((x - source2[0])**2 + (y - source2[1])**2)

                # Wave equations
                wave1 = np.sin(d1 * 0.05 - self.frame_count * 0.1)
                wave2 = np.sin(d2 * 0.05 - self.frame_count * 0.1)

                # Interference
                amplitude = (wave1 + wave2) / 2
                brightness = int(127 + amplitude * 128 * bass)

                color = (brightness, brightness, brightness)
                cv2.circle(frame, (x, y), 3, color, -1)

        # Sources
        cv2.circle(frame, source1, 10, (255, 200, 100), -1)
        cv2.circle(frame, source2, 10, (255, 200, 100), -1)

        return frame

    def draw_mode_405_particle_accelerator(self, frame, magnitudes):
        """Mode 405: Particle accelerator ring"""
        energy = self.get_energy(magnitudes)

        # Accelerator ring
        cv2.circle(frame, (self.center_x, self.center_y), self.max_radius, (100, 100, 150), 5)

        # Particles moving at high speed
        num_particles = int(energy * 30)
        for i in range(num_particles):
            angle = (i / num_particles) * 2 * np.pi + self.frame_count * 0.2

            x = int(self.center_x + np.cos(angle) * self.max_radius)
            y = int(self.center_y + np.sin(angle) * self.max_radius)

            # Particle trail
            for j in range(5):
                trail_angle = angle - j * 0.1
                tx = int(self.center_x + np.cos(trail_angle) * self.max_radius)
                ty = int(self.center_y + np.sin(trail_angle) * self.max_radius)

                alpha = 255 - j * 50
                cv2.circle(frame, (tx, ty), 3, (alpha, alpha // 2, 0), -1)

        return frame

    def draw_mode_406_crystal_lattice(self, frame, magnitudes):
        """Mode 406: 3D crystal lattice structure"""
        spacing = 50

        for z in range(5):
            depth_factor = 1 - z * 0.15

            for y in range(0, self.height, spacing):
                for x in range(0, self.width, spacing):
                    idx = (x // spacing + y // spacing + z) % len(magnitudes)
                    mag = magnitudes[idx]

                    # 3D perspective
                    px = int(x * depth_factor + self.width * (1 - depth_factor) / 2)
                    py = int(y * depth_factor + self.height * (1 - depth_factor) / 2)

                    size = int(5 * depth_factor + mag * 10)
                    brightness = int(100 + mag * 155)

                    color = self.hsv_to_bgr(140, 200, brightness)
                    cv2.circle(frame, (px, py), size, color, -1)

                    # Bonds to adjacent atoms
                    if x < self.width - spacing:
                        px2 = int((x + spacing) * depth_factor + self.width * (1 - depth_factor) / 2)
                        cv2.line(frame, (px, py), (px2, py), (100, 100, 150), 1)

        return frame

    def draw_mode_407_electromagnetic_wave(self, frame, magnitudes):
        """Mode 407: Electromagnetic wave propagation"""
        for i, mag in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * self.width)

            # Electric field (vertical oscillation)
            e_amplitude = mag * 100
            e_y = int(self.center_y + np.sin(x * 0.02 + self.frame_count * 0.1) * e_amplitude)

            # Magnetic field (horizontal oscillation)
            m_amplitude = mag * 100
            m_offset = int(np.cos(x * 0.02 + self.frame_count * 0.1) * m_amplitude)

            # Draw E field
            cv2.circle(frame, (x, e_y), 3, (255, 100, 100), -1)
            cv2.line(frame, (x, self.center_y), (x, e_y), (255, 100, 100), 1)

            # Draw B field
            cv2.circle(frame, (x + m_offset, self.center_y), 3, (100, 100, 255), -1)
            cv2.line(frame, (x, self.center_y), (x + m_offset, self.center_y), (100, 100, 255), 1)

        return frame

    def draw_mode_408_quantum_tunneling(self, frame, magnitudes):
        """Mode 408: Quantum tunneling through barrier"""
        bass = self.get_bass(magnitudes)

        # Energy barrier
        barrier_x = self.center_x
        cv2.rectangle(frame, (barrier_x - 20, 0), (barrier_x + 20, self.height),
                     (150, 100, 100), -1)

        # Particle wave function
        for i, mag in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * self.width)

            # Wave function amplitude
            if x < barrier_x - 20:
                # Before barrier - incident + reflected
                amplitude = mag * 80
            elif x > barrier_x + 20:
                # After barrier - tunneled (reduced amplitude)
                amplitude = mag * 40 * bass
            else:
                # Inside barrier - exponential decay
                amplitude = mag * 60

            y1 = int(self.center_y - amplitude)
            y2 = int(self.center_y + amplitude)

            color = self.hsv_to_bgr(120, 200, 200)
            cv2.line(frame, (x, y1), (x, y2), color, 2)

        return frame

    def draw_mode_409_fission_reaction(self, frame, magnitudes):
        """Mode 409: Nuclear fission chain reaction"""
        bass = self.get_bass(magnitudes)

        # Central nucleus splitting
        if bass > 0.5:
            # Fragments flying apart
            for i in range(8):
                angle = (i / 8) * 2 * np.pi
                dist = bass * 150

                x = int(self.center_x + np.cos(angle) * dist)
                y = int(self.center_y + np.sin(angle) * dist)

                cv2.circle(frame, (x, y), 15, (255, 150, 100), -1)

                # Neutrons released
                for j in range(3):
                    n_angle = angle + (j - 1) * 0.3
                    n_dist = dist + 30
                    nx = int(self.center_x + np.cos(n_angle) * n_dist)
                    ny = int(self.center_y + np.sin(n_angle) * n_dist)

                    cv2.circle(frame, (nx, ny), 5, (200, 200, 255), -1)
        else:
            # Intact nucleus
            cv2.circle(frame, (self.center_x, self.center_y), 40, (200, 100, 100), -1)

        return frame

    def draw_mode_410_doppler_effect(self, frame, magnitudes):
        """Mode 410: Doppler effect wave compression"""
        # Moving source
        source_x = int(self.width * 0.3 + np.sin(self.frame_count * 0.05) * self.width * 0.2)
        source_y = self.center_y

        cv2.circle(frame, (source_x, source_y), 15, (255, 200, 100), -1)

        # Sound waves (compressed ahead, stretched behind)
        for i, mag in enumerate(magnitudes[::3]):
            radius = (self.frame_count + i * 10) % 200

            # Compression factor based on direction
            for angle in np.linspace(0, 2 * np.pi, 36):
                # Ahead of source (compressed)
                if np.cos(angle) > 0:
                    r = radius * 0.8
                # Behind source (stretched)
                else:
                    r = radius * 1.2

                x = int(source_x + np.cos(angle) * r)
                y = int(source_y + np.sin(angle) * r)

                cv2.circle(frame, (x, y), 2, (150, 150, 200), -1)

        return frame

    def draw_mode_411_gravity_well(self, frame, magnitudes):
        """Mode 411: Gravitational well spacetime curvature"""
        # Central mass
        cv2.circle(frame, (self.center_x, self.center_y), 25, (200, 200, 100), -1)

        # Spacetime grid warping
        grid_spacing = 40

        for i in range(0, self.height, grid_spacing):
            points = []
            for j in range(0, self.width, grid_spacing):
                # Distance from center
                dist = np.sqrt((j - self.center_x)**2 + (i - self.center_y)**2)

                # Warp based on distance (inverse square)
                warp = max(0, 100 - dist) * 0.3

                x = j
                y = int(i + warp)

                points.append([x, y])

            points = np.array(points, dtype=np.int32)
            for k in range(len(points) - 1):
                cv2.line(frame, tuple(points[k]), tuple(points[k + 1]), (100, 150, 200), 1)

        return frame

    def draw_mode_412_prism_spectrum(self, frame, magnitudes):
        """Mode 412: Light dispersing through prism"""
        # Prism
        prism_pts = np.array([
            [self.center_x, self.center_y - 80],
            [self.center_x - 60, self.center_y + 80],
            [self.center_x + 60, self.center_y + 80]
        ], dtype=np.int32)
        cv2.fillPoly(frame, [prism_pts], (180, 180, 200))

        # White light entering
        for i in range(20):
            y = int(self.center_y - 80 + i * 8)
            cv2.line(frame, (0, y), (self.center_x - 60, y), (255, 255, 255), 2)

        # Dispersed spectrum exiting
        for i, mag in enumerate(magnitudes[::5]):
            angle = -30 + i * 1.5  # Dispersion angle
            length = 200 + mag * 100

            rad = np.deg2rad(angle)
            x2 = int(self.center_x + 60 + np.cos(rad) * length)
            y2 = int(self.center_y + 80 + np.sin(rad) * length)

            hue = int((i / 24) * 180)
            color = self.hsv_to_bgr(hue, 255, 255)

            cv2.line(frame, (self.center_x + 60, self.center_y + 80), (x2, y2), color, 3)

        return frame

    def draw_mode_413_molecular_bonds(self, frame, magnitudes):
        """Mode 413: Molecular bonding and vibration"""
        # Molecule structure
        num_atoms = 8
        for i in range(num_atoms):
            angle = (i / num_atoms) * 2 * np.pi

            mag_idx = i * len(magnitudes) // num_atoms
            mag = magnitudes[mag_idx]

            # Bond vibration
            vibration = 1 + mag * 0.3
            dist = 120 * vibration

            x = int(self.center_x + np.cos(angle) * dist)
            y = int(self.center_y + np.sin(angle) * dist)

            # Atom
            cv2.circle(frame, (x, y), 20, (100, 150, 200), -1)

            # Bond to center
            cv2.line(frame, (self.center_x, self.center_y), (x, y), (150, 150, 150), 3)

            # Bond to next atom
            next_angle = ((i + 1) % num_atoms / num_atoms) * 2 * np.pi
            next_x = int(self.center_x + np.cos(next_angle) * dist)
            next_y = int(self.center_y + np.sin(next_angle) * dist)

            cv2.line(frame, (x, y), (next_x, next_y), (150, 150, 150), 2)

        # Center atom
        cv2.circle(frame, (self.center_x, self.center_y), 25, (200, 100, 150), -1)

        return frame

    def draw_mode_414_standing_wave(self, frame, magnitudes):
        """Mode 414: Standing wave with nodes and antinodes"""
        # Standing wave pattern
        num_harmonics = 4

        for harmonic in range(1, num_harmonics + 1):
            y_offset = int((harmonic / num_harmonics) * self.height * 0.8)

            for i, mag in enumerate(magnitudes):
                x = int((i / len(magnitudes)) * self.width)

                # Standing wave equation
                amplitude = mag * 50 * np.sin(harmonic * x * np.pi / self.width)
                amplitude *= np.cos(self.frame_count * 0.1)

                y = y_offset + int(amplitude)

                color = self.hsv_to_bgr(harmonic * 40, 200, 200)
                cv2.circle(frame, (x, y), 2, color, -1)

            # Nodes (points that don't move)
            for n in range(harmonic + 1):
                node_x = int((n / harmonic) * self.width)
                cv2.circle(frame, (node_x, y_offset), 8, (255, 100, 100), -1)

        return frame

    def draw_mode_415_brownian_motion(self, frame, magnitudes):
        """Mode 415: Brownian motion of particles"""
        energy = self.get_energy(magnitudes)

        # Random walk of particles
        num_particles = 30
        for i in range(num_particles):
            # Use pseudo-random but deterministic motion
            seed = i + self.frame_count

            x = int(self.width * 0.5 + np.sin(seed * 0.1) * 200 * energy)
            y = int(self.height * 0.5 + np.cos(seed * 0.13) * 200 * energy)

            # Trail
            for j in range(20):
                trail_seed = seed - j
                tx = int(self.width * 0.5 + np.sin(trail_seed * 0.1) * 200 * energy)
                ty = int(self.height * 0.5 + np.cos(trail_seed * 0.13) * 200 * energy)

                alpha = 255 - j * 12
                cv2.circle(frame, (tx, ty), 2, (alpha, alpha, alpha), -1)

            # Particle
            cv2.circle(frame, (x, y), 5, (200, 200, 255), -1)

        return frame

    def draw_mode_416_tesla_coil(self, frame, magnitudes):
        """Mode 416: Tesla coil electric arcs"""
        highs = self.get_highs(magnitudes)

        # Coil base
        coil_x = self.center_x
        coil_base = int(self.height * 0.8)
        cv2.rectangle(frame, (coil_x - 40, coil_base), (coil_x + 40, self.height),
                     (120, 100, 80), -1)

        # Coil windings
        for i in range(15):
            y = coil_base - i * 10
            cv2.ellipse(frame, (coil_x, y), (40, 8), 0, 0, 360, (150, 120, 100), 2)

        # Electric arcs
        if highs > 0.4:
            num_arcs = int(highs * 8)
            for arc in range(num_arcs):
                # Arc path
                x, y = coil_x, coil_base - 150

                for step in range(15):
                    x2 = x + int(np.random.random() * 60 - 30)
                    y2 = y - int(np.random.random() * 40)

                    cv2.line(frame, (x, y), (x2, y2), (200, 200, 255), 2)

                    x, y = x2, y2

        return frame

    def draw_mode_417_phase_transition(self, frame, magnitudes):
        """Mode 417: Phase transition (solid/liquid/gas)"""
        energy = self.get_energy(magnitudes)

        # Determine phase based on energy
        if energy < 0.33:
            # Solid - ordered lattice
            spacing = 40
            for y in range(0, self.height, spacing):
                for x in range(0, self.width, spacing):
                    cv2.circle(frame, (x, y), 8, (100, 150, 200), -1)

        elif energy < 0.66:
            # Liquid - particles close but mobile
            for i in range(100):
                x = int((i % 10) * self.width / 10 + np.sin(self.frame_count * 0.1 + i) * 20)
                y = int((i // 10) * self.height / 10 + np.cos(self.frame_count * 0.1 + i) * 20)

                cv2.circle(frame, (x, y), 10, (100, 200, 200), -1)

        else:
            # Gas - particles far apart, fast moving
            for i in range(40):
                angle = i * 0.5 + self.frame_count * 0.2
                dist = 50 + i * 15

                x = int(self.center_x + np.cos(angle) * dist)
                y = int(self.center_y + np.sin(angle) * dist)

                cv2.circle(frame, (x, y), 6, (200, 150, 100), -1)

        return frame

    def draw_mode_418_superconductor(self, frame, magnitudes):
        """Mode 418: Superconductor Meissner effect"""
        bass = self.get_bass(magnitudes)

        # Superconductor disc
        cv2.circle(frame, (self.center_x, self.center_y + 50), 80, (150, 150, 200), -1)

        # Levitating magnet
        levitation = int(bass * 100)
        magnet_y = self.center_y - 80 - levitation

        cv2.rectangle(frame, (self.center_x - 30, magnet_y - 15),
                     (self.center_x + 30, magnet_y + 15), (200, 100, 100), -1)

        # Expelled magnetic field lines
        for i in range(12):
            angle = (i / 12) * 2 * np.pi

            # Field lines curve around superconductor
            points = []
            for t in np.linspace(0, 1, 20):
                r = 120 + t * 100
                field_angle = angle + np.sin(t * np.pi) * 0.5

                x = int(self.center_x + np.cos(field_angle) * r)
                y = int(self.center_y + 50 + np.sin(field_angle) * r * 0.6)

                points.append([x, y])

            points = np.array(points, dtype=np.int32)
            for j in range(len(points) - 1):
                cv2.line(frame, tuple(points[j]), tuple(points[j + 1]), (150, 150, 255), 1)

        return frame

    def draw_mode_419_neuron_firing(self, frame, magnitudes):
        """Mode 419: Neuron action potential firing"""
        bass = self.get_bass(magnitudes)

        # Neuron body
        cv2.circle(frame, (self.center_x, self.center_y), 40, (200, 150, 200), -1)

        # Dendrites (inputs)
        for i in range(8):
            angle = (i / 8) * 2 * np.pi

            points = []
            for j in range(10):
                t = j / 10
                dist = 50 + t * 80
                branch_angle = angle + np.sin(j) * 0.3

                x = int(self.center_x + np.cos(branch_angle) * dist)
                y = int(self.center_y + np.sin(branch_angle) * dist)
                points.append([x, y])

            points = np.array(points, dtype=np.int32)
            for j in range(len(points) - 1):
                cv2.line(frame, tuple(points[j]), tuple(points[j + 1]), (150, 100, 150), 3)

        # Axon (output)
        axon_length = 200 + bass * 150
        axon_x = int(self.center_x + axon_length)

        cv2.line(frame, (self.center_x + 40, self.center_y),
                (axon_x, self.center_y), (180, 120, 180), 5)

        # Action potential pulse
        if bass > 0.5:
            pulse_x = int(self.center_x + 40 + (self.frame_count % 30) * 8)

            cv2.circle(frame, (pulse_x, self.center_y), 15, (255, 255, 100), -1)

        return frame

    def draw_mode_420_resonance_modes(self, frame, magnitudes):
        """Mode 420: Resonance modes of vibrating plate"""
        # Chladni plate patterns
        for y in range(0, self.height, 5):
            for x in range(0, self.width, 5):
                # Resonance pattern equations
                mode_x = np.sin(x * 0.02) * np.sin(y * 0.03)
                mode_y = np.cos(x * 0.03) * np.cos(y * 0.02)

                amplitude = mode_x * mode_y * np.cos(self.frame_count * 0.1)

                # Nodes (dark) and antinodes (bright)
                brightness = int(127 + amplitude * 128)

                color = (brightness, brightness, brightness)
                cv2.circle(frame, (x, y), 2, color, -1)

        return frame

    def draw_mode_421_fractal_diffusion(self, frame, magnitudes):
        """Mode 421: Diffusion-limited aggregation"""
        energy = self.get_energy(magnitudes)

        # Central seed
        cv2.circle(frame, (self.center_x, self.center_y), 5, (200, 200, 200), -1)

        # Particles aggregate in fractal pattern
        for i in range(int(energy * 100)):
            angle = (i / 100) * 2 * np.pi + np.random.random() * 0.5
            dist = 50 + i * 2 + np.random.random() * 30

            x = int(self.center_x + np.cos(angle) * dist)
            y = int(self.center_y + np.sin(angle) * dist)

            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            if mag > 0.2:
                size = 2 + int(mag * 5)
                cv2.circle(frame, (x, y), size, (180, 180, 200), -1)

        return frame

    def draw_mode_422_plasma_ball(self, frame, magnitudes):
        """Mode 422: Plasma ball electric tendrils"""
        # Central electrode
        cv2.circle(frame, (self.center_x, self.center_y), 20, (255, 255, 200), -1)

        # Plasma tendrils to edge
        for i, mag in enumerate(magnitudes[::3]):
            if mag > 0.3:
                angle = (i / 40) * 2 * np.pi

                # Tendril path with branching
                x, y = self.center_x, self.center_y

                for step in range(15):
                    angle += (np.random.random() - 0.5) * 0.5
                    step_dist = 15 + mag * 10

                    x2 = int(x + np.cos(angle) * step_dist)
                    y2 = int(y + np.sin(angle) * step_dist)

                    # Color shifts along tendril
                    hue = int(120 + step * 5)
                    color = self.hsv_to_bgr(hue, 255, 255)

                    cv2.line(frame, (x, y), (x2, y2), color, 2)

                    x, y = x2, y2

        return frame

    def draw_mode_423_coriolis_effect(self, frame, magnitudes):
        """Mode 423: Coriolis effect on rotating frame"""
        # Rotating reference frame
        rotation_speed = self.frame_count * 0.05

        # Object moving in straight line (inertial frame)
        for i, mag in enumerate(magnitudes[::4]):
            # Linear motion
            t = (self.frame_count + i * 5) % 100 / 100
            straight_x = int(t * self.width)
            straight_y = self.center_y

            # Apply rotation transformation
            rel_x = straight_x - self.center_x
            rel_y = straight_y - self.center_y

            rot_x = int(self.center_x + rel_x * np.cos(rotation_speed) - rel_y * np.sin(rotation_speed))
            rot_y = int(self.center_y + rel_x * np.sin(rotation_speed) + rel_y * np.cos(rotation_speed))

            # Appears to curve in rotating frame
            size = 3 + int(mag * 8)
            cv2.circle(frame, (rot_x, rot_y), size, (200, 150, 255), -1)

        # Rotating reference grid
        for i in range(8):
            angle = (i / 8) * 2 * np.pi + rotation_speed

            x = int(self.center_x + np.cos(angle) * self.max_radius)
            y = int(self.center_y + np.sin(angle) * self.max_radius)

            cv2.line(frame, (self.center_x, self.center_y), (x, y), (80, 80, 80), 1)

        return frame

    def draw_mode_424_photoelectric_effect(self, frame, magnitudes):
        """Mode 424: Photoelectric effect electron emission"""
        highs = self.get_highs(magnitudes)

        # Metal surface
        cv2.rectangle(frame, (0, self.center_y), (self.width, self.height),
                     (120, 120, 140), -1)

        # Incoming photons
        for i, mag in enumerate(magnitudes[::5]):
            x = int((i / 24) * self.width)
            y = int((self.frame_count + i * 10) % self.center_y)

            # Photon
            cv2.circle(frame, (x, y), 5, (255, 255, 100), -1)

            # If hits surface with sufficient energy
            if y > self.center_y - 20 and mag > 0.5:
                # Ejected electron
                electron_y = int(self.center_y - (self.frame_count + i * 10) % 100)

                if electron_y < self.center_y:
                    cv2.circle(frame, (x, electron_y), 4, (100, 200, 255), -1)

        return frame

    def draw_mode_425_lorenz_attractor(self, frame, magnitudes):
        """Mode 425: Lorenz attractor chaos theory"""
        # Lorenz system parameters
        sigma = 10.0
        rho = 28.0
        beta = 8.0 / 3.0
        dt = 0.01

        # Use magnitude to perturb initial conditions
        bass = self.get_bass(magnitudes)

        # Simplified Lorenz path
        for i in range(100):
            t = (self.frame_count + i) * dt
            x = np.sin(t * sigma) * 30 * (1 + bass)
            y = np.cos(t * rho) * 20
            z = np.sin(t * beta) * 25

            # Project 3D to 2D
            px = int(self.center_x + x + z * 0.5)
            py = int(self.center_y + y - z * 0.3)

            hue = int((i / 100) * 180)
            color = self.hsv_to_bgr(hue, 255, 200)

            cv2.circle(frame, (px, py), 2, color, -1)

        return frame

    def draw_mode_426_spin_precession(self, frame, magnitudes):
        """Mode 426: Quantum spin precession"""
        # Spin vector precessing around magnetic field
        for i, mag in enumerate(magnitudes[::8]):
            # Multiple spins
            offset_x = int((i / 15) * self.width)
            offset_y = int(self.height * 0.5)

            # Precession angle
            precession = self.frame_count * 0.1 + i

            # Spin vector
            radius = 30 + mag * 40
            x = int(offset_x + np.cos(precession) * radius)
            y = int(offset_y + np.sin(precession) * radius * 0.5)

            # Draw spin arrow
            cv2.line(frame, (offset_x, offset_y), (x, y), (200, 150, 255), 3)
            cv2.circle(frame, (x, y), 8, (255, 200, 200), -1)

            # Magnetic field direction (vertical)
            cv2.line(frame, (offset_x, offset_y - 50), (offset_x, offset_y + 50),
                    (100, 100, 200), 2)

        return frame

    def draw_mode_427_compton_scattering(self, frame, magnitudes):
        """Mode 427: Compton scattering of photons"""
        bass = self.get_bass(magnitudes)

        # Incoming photon
        photon_x = int((self.frame_count * 5) % self.width)
        cv2.line(frame, (0, self.center_y), (photon_x, self.center_y), (255, 255, 100), 3)

        # Target electron
        cv2.circle(frame, (self.center_x, self.center_y), 15, (100, 200, 255), -1)

        # If collision occurs
        if abs(photon_x - self.center_x) < 20:
            # Scattered photon (different wavelength)
            scatter_angle = 45 + bass * 30
            rad = np.deg2rad(scatter_angle)

            scatter_length = 200
            scatter_x = int(self.center_x + np.cos(rad) * scatter_length)
            scatter_y = int(self.center_y - np.sin(rad) * scatter_length)

            cv2.line(frame, (self.center_x, self.center_y), (scatter_x, scatter_y),
                    (200, 200, 100), 3)

            # Recoil electron
            recoil_angle = scatter_angle - 90
            recoil_rad = np.deg2rad(recoil_angle)

            recoil_x = int(self.center_x + np.cos(recoil_rad) * 80)
            recoil_y = int(self.center_y - np.sin(recoil_rad) * 80)

            cv2.line(frame, (self.center_x, self.center_y), (recoil_x, recoil_y),
                    (100, 255, 255), 3)

        return frame

    def draw_mode_428_ferrofluid(self, frame, magnitudes):
        """Mode 428: Ferrofluid spikes in magnetic field"""
        bass = self.get_bass(magnitudes)

        # Base fluid
        cv2.ellipse(frame, (self.center_x, self.center_y + 50),
                   (120, 40), 0, 0, 360, (40, 40, 40), -1)

        # Magnetic spikes
        num_spikes = 12
        for i in range(num_spikes):
            angle = (i / num_spikes) * np.pi - np.pi / 2

            mag_idx = i * len(magnitudes) // num_spikes
            mag = magnitudes[mag_idx]

            spike_height = 60 + mag * 120 * bass

            base_x = int(self.center_x + np.cos(angle) * 100)
            base_y = self.center_y + 50

            tip_x = int(base_x)
            tip_y = int(base_y - spike_height)

            # Spike shape (triangle)
            width = 15 + int(mag * 20)
            pts = np.array([
                [tip_x, tip_y],
                [base_x - width, base_y],
                [base_x + width, base_y]
            ], dtype=np.int32)

            cv2.fillPoly(frame, [pts], (60, 60, 60))

        return frame

    def draw_mode_429_sonoluminescence(self, frame, magnitudes):
        """Mode 429: Sonoluminescence bubble collapse"""
        bass = self.get_bass(magnitudes)

        # Bubble oscillation
        bubble_size = int(30 + np.sin(self.frame_count * 0.3) * 20 * bass)

        # Draw bubble
        cv2.circle(frame, (self.center_x, self.center_y), bubble_size, (100, 150, 200), -1)

        # At collapse point, emit light
        if bubble_size < 20 and bass > 0.6:
            # Light flash
            for i in range(5):
                flash_radius = 40 + i * 30
                alpha = 255 - i * 50

                cv2.circle(frame, (self.center_x, self.center_y), flash_radius,
                          (alpha, alpha, alpha), 2)

        return frame

    def draw_mode_430_cherenkov_radiation(self, frame, magnitudes):
        """Mode 430: Cherenkov radiation cone"""
        energy = self.get_energy(magnitudes)

        # Particle moving faster than light in medium
        particle_x = int((self.frame_count * 5 * energy) % self.width)
        particle_y = self.center_y

        cv2.circle(frame, (particle_x, particle_y), 10, (255, 200, 100), -1)

        # Cherenkov cone (shock wave)
        cone_angle = 30  # degrees

        for side in [-1, 1]:
            rad = np.deg2rad(cone_angle * side)

            # Cone extending backward
            for i in range(10):
                dist = i * 30
                x = int(particle_x - dist)
                y = int(particle_y + np.tan(rad) * dist)

                if 0 <= y < self.height:
                    alpha = 255 - i * 25
                    cv2.circle(frame, (x, y), 3, (0, alpha, alpha), -1)

        return frame

    def draw_mode_431_hall_effect(self, frame, magnitudes):
        """Mode 431: Hall effect charge separation"""
        bass = self.get_bass(magnitudes)

        # Conductor
        cv2.rectangle(frame, (int(self.width * 0.3), int(self.height * 0.3)),
                     (int(self.width * 0.7), int(self.height * 0.7)),
                     (150, 150, 150), -1)

        # Current flow (horizontal)
        for i in range(10):
            y = int(self.height * (0.35 + i * 0.04))
            cv2.line(frame, (int(self.width * 0.3), y), (int(self.width * 0.7), y),
                    (255, 200, 100), 2)

        # Magnetic field (into page) - represented by crosses
        for y in range(int(self.height * 0.35), int(self.height * 0.65), 30):
            for x in range(int(self.width * 0.35), int(self.width * 0.65), 30):
                cv2.line(frame, (x - 5, y - 5), (x + 5, y + 5), (200, 100, 100), 2)
                cv2.line(frame, (x - 5, y + 5), (x + 5, y - 5), (200, 100, 100), 2)

        # Hall voltage (charge separation)
        # Positive charges accumulate on top
        for i in range(int(bass * 10)):
            x = int(self.width * (0.35 + i * 0.035))
            y = int(self.height * 0.32)
            cv2.circle(frame, (x, y), 5, (255, 100, 100), -1)

        # Negative charges accumulate on bottom
        for i in range(int(bass * 10)):
            x = int(self.width * (0.35 + i * 0.035))
            y = int(self.height * 0.68)
            cv2.circle(frame, (x, y), 5, (100, 100, 255), -1)

        return frame

    def draw_mode_432_cymatics(self, frame, magnitudes):
        """Mode 432: Cymatic patterns from sound"""
        # Sound-induced patterns in medium
        for y in range(0, self.height, 8):
            for x in range(0, self.width, 8):
                # Multiple frequency modes
                pattern = 0
                for i, mag in enumerate(magnitudes[::10]):
                    freq = (i + 1) * 0.02
                    pattern += np.sin(x * freq) * np.cos(y * freq) * mag

                brightness = int(127 + pattern * 128)
                color = (brightness, brightness, brightness)

                cv2.circle(frame, (x, y), 3, color, -1)

        return frame

    def draw_mode_433_klein_bottle(self, frame, magnitudes):
        """Mode 433: Klein bottle topology"""
        # Parametric Klein bottle projection
        for i, mag in enumerate(magnitudes):
            u = (i / len(magnitudes)) * 2 * np.pi
            v = self.frame_count * 0.05

            # Klein bottle parametric equations (simplified)
            r = 100 + 50 * np.cos(v)
            x = r * np.cos(u)
            y = r * np.sin(u)
            z = 50 * np.sin(v)

            # Project to 2D
            px = int(self.center_x + x + z * 0.5)
            py = int(self.center_y + y * 0.7)

            size = 2 + int(mag * 6)
            hue = int((u / (2 * np.pi)) * 180)
            color = self.hsv_to_bgr(hue, 200, 200)

            cv2.circle(frame, (px, py), size, color, -1)

        return frame

    def draw_mode_434_raman_scattering(self, frame, magnitudes):
        """Mode 434: Raman spectroscopy energy levels"""
        # Incoming laser
        laser_x = int(self.width * 0.2)
        cv2.line(frame, (0, self.center_y), (laser_x, self.center_y), (0, 255, 0), 4)

        # Molecule energy levels
        levels = [
            (self.center_y + 100, "Ground"),
            (self.center_y, "Virtual"),
            (self.center_y + 80, "Vibrational")
        ]

        for y, label in levels:
            cv2.line(frame, (int(self.width * 0.3), y), (int(self.width * 0.7), y),
                    (200, 200, 200), 2)

        # Scattered light (different wavelengths)
        bass = self.get_bass(magnitudes)
        highs = self.get_highs(magnitudes)

        # Stokes (lower energy)
        if bass > 0.5:
            cv2.line(frame, (int(self.width * 0.5), self.center_y + 80),
                    (self.width, self.center_y + 80), (255, 100, 100), 3)

        # Anti-Stokes (higher energy)
        if highs > 0.5:
            cv2.line(frame, (int(self.width * 0.5), self.center_y + 100),
                    (self.width, self.center_y + 100), (100, 100, 255), 3)

        return frame

    def draw_mode_435_vortex_shedding(self, frame, magnitudes):
        """Mode 435: Von Kármán vortex street"""
        # Obstacle in flow
        obstacle_x = int(self.width * 0.3)
        cv2.circle(frame, (obstacle_x, self.center_y), 40, (150, 150, 150), -1)

        # Vortices shed alternately
        for i in range(8):
            phase = (self.frame_count + i * 20) % 200

            vortex_x = obstacle_x + phase
            # Alternating up and down
            vortex_y = self.center_y + (50 if i % 2 == 0 else -50)

            # Vortex rotation
            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            for j in range(12):
                angle = (j / 12) * 2 * np.pi + self.frame_count * 0.1 * (1 if i % 2 == 0 else -1)
                r = 20 + mag * 20

                vx = int(vortex_x + np.cos(angle) * r)
                vy = int(vortex_y + np.sin(angle) * r)

                cv2.circle(frame, (vx, vy), 2, (100, 150, 200), -1)

        return frame

    def draw_mode_436_polarization(self, frame, magnitudes):
        """Mode 436: Light polarization through filters"""
        # Unpolarized light
        for i in range(20):
            angle = (i / 20) * 2 * np.pi
            y = int(self.height * 0.3 + np.sin(angle) * 30)

            cv2.line(frame, (0, y), (int(self.width * 0.25), self.height * 0.3),
                    (255, 255, 100), 1)

        # First polarizer (vertical)
        cv2.rectangle(frame, (int(self.width * 0.25), int(self.height * 0.2)),
                     (int(self.width * 0.3), int(self.height * 0.4)),
                     (100, 100, 100), -1)

        # Vertically polarized light
        cv2.line(frame, (int(self.width * 0.3), self.height * 0.2),
                (int(self.width * 0.6), self.height * 0.2), (255, 255, 100), 2)
        cv2.line(frame, (int(self.width * 0.3), self.height * 0.4),
                (int(self.width * 0.6), self.height * 0.4), (255, 255, 100), 2)

        # Second polarizer (angle depends on bass)
        bass = self.get_bass(magnitudes)
        angle = bass * 90  # 0 to 90 degrees

        cv2.rectangle(frame, (int(self.width * 0.6), int(self.height * 0.2)),
                     (int(self.width * 0.65), int(self.height * 0.4)),
                     (100, 100, 100), -1)

        # Transmitted intensity (Malus's law)
        intensity = np.cos(np.deg2rad(angle))**2

        if intensity > 0.1:
            brightness = int(intensity * 255)
            cv2.line(frame, (int(self.width * 0.65), self.height * 0.3),
                    (self.width, self.height * 0.3), (brightness, brightness, 100), 3)

        return frame

    def draw_mode_437_higgs_field(self, frame, magnitudes):
        """Mode 437: Higgs field giving mass to particles"""
        energy = self.get_energy(magnitudes)

        # Higgs field (background)
        for y in range(0, self.height, 20):
            for x in range(0, self.width, 20):
                field_value = np.sin(x * 0.05) * np.cos(y * 0.05)
                brightness = int(100 + field_value * 50)

                cv2.circle(frame, (x, y), 3, (brightness, brightness, 150), -1)

        # Particles moving through field
        for i in range(int(energy * 15)):
            angle = i * 0.4 + self.frame_count * 0.05

            # Particles slow down (gain mass) in field
            slowdown = 1 + energy
            radius = 150 / slowdown

            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)

            # Size represents acquired mass
            size = int(5 + energy * 15)
            cv2.circle(frame, (x, y), size, (255, 200, 100), -1)

        return frame

    def draw_mode_438_bose_einstein(self, frame, magnitudes):
        """Mode 438: Bose-Einstein condensate formation"""
        bass = self.get_bass(magnitudes)

        # Temperature determines spread
        temperature = 1 - bass  # Low bass = low temperature

        if temperature < 0.3:
            # Condensed state - all particles in same location
            num_particles = 200
            for i in range(num_particles):
                # Very tight cluster
                x = int(self.center_x + np.random.normal(0, 20))
                y = int(self.center_y + np.random.normal(0, 20))

                cv2.circle(frame, (x, y), 2, (100, 200, 255), -1)

            # Quantum wavefunction
            for r in range(5):
                radius = 30 + r * 15
                cv2.circle(frame, (self.center_x, self.center_y), radius,
                          (100, 150, 255), 1)

        else:
            # Normal gas - spread out
            num_particles = 100
            for i in range(num_particles):
                spread = temperature * 200
                x = int(self.center_x + np.random.normal(0, spread))
                y = int(self.center_y + np.random.normal(0, spread))

                cv2.circle(frame, (x, y), 3, (200, 150, 100), -1)

        return frame

    def draw_mode_439_schrodinger_cat(self, frame, magnitudes):
        """Mode 439: Schrödinger's cat superposition"""
        bass = self.get_bass(magnitudes)

        # Box
        box_left = int(self.width * 0.25)
        box_right = int(self.width * 0.75)
        box_top = int(self.height * 0.25)
        box_bottom = int(self.height * 0.75)

        cv2.rectangle(frame, (box_left, box_top), (box_right, box_bottom),
                     (150, 150, 150), 3)

        # Superposition - both states
        if bass > 0.5:
            # Left side - alive
            cv2.circle(frame, (int(self.width * 0.4), self.center_y), 40,
                      (100, 255, 100), -1)
            cv2.putText(frame, "Alive", (int(self.width * 0.35), self.center_y + 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            # Right side - dead
            cv2.circle(frame, (int(self.width * 0.6), self.center_y), 40,
                      (255, 100, 100), -1)
            cv2.putText(frame, "Dead", (int(self.width * 0.57), self.center_y + 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            # Superposition symbol
            cv2.putText(frame, "+", (int(self.width * 0.48), self.center_y + 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

        else:
            # Collapsed state
            cv2.circle(frame, (self.center_x, self.center_y), 40,
                      (200, 200, 100), -1)
            cv2.putText(frame, "?", (self.center_x - 15, self.center_y + 15),
                       cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

        return frame

    def draw_mode_440_string_vibration(self, frame, magnitudes):
        """Mode 440: Vibrating string harmonics"""
        # Guitar string with different harmonics

        num_harmonics = 5
        for h in range(1, num_harmonics + 1):
            y_base = int((h / num_harmonics) * self.height * 0.8)

            points = []
            for i, mag in enumerate(magnitudes):
                x = int((i / len(magnitudes)) * self.width)

                # Harmonic equation
                amplitude = mag * 40 * np.sin(h * x * np.pi / self.width)
                amplitude *= np.sin(self.frame_count * 0.1 * h)

                y = y_base + int(amplitude)
                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            color = self.hsv_to_bgr(h * 30, 200, 200)
            for i in range(len(points) - 1):
                cv2.line(frame, tuple(points[i]), tuple(points[i + 1]), color, 2)

            # Fixed ends
            cv2.circle(frame, (0, y_base), 8, (255, 100, 100), -1)
            cv2.circle(frame, (self.width, y_base), 8, (255, 100, 100), -1)

        return frame

    def draw_mode_441_electron_cloud(self, frame, magnitudes):
        """Mode 441: Electron probability cloud"""
        # Quantum mechanical orbital
        energy = self.get_energy(magnitudes)

        # Density represents probability
        num_points = int(1000 * energy)

        for i in range(num_points):
            # Probability distribution (s-orbital approximation)
            r = abs(np.random.normal(0, 60))
            angle = np.random.random() * 2 * np.pi

            x = int(self.center_x + r * np.cos(angle))
            y = int(self.center_y + r * np.sin(angle))

            if 0 <= x < self.width and 0 <= y < self.height:
                cv2.circle(frame, (x, y), 1, (150, 200, 255), -1)

        # Nucleus
        cv2.circle(frame, (self.center_x, self.center_y), 8, (255, 200, 100), -1)

        return frame

    def draw_mode_442_thermoelectric(self, frame, magnitudes):
        """Mode 442: Thermoelectric Seebeck effect"""
        bass = self.get_bass(magnitudes)
        highs = self.get_highs(magnitudes)

        # Two different materials
        cv2.rectangle(frame, (int(self.width * 0.2), self.center_y - 30),
                     (int(self.width * 0.5), self.center_y + 30),
                     (200, 100, 100), -1)  # Material A

        cv2.rectangle(frame, (int(self.width * 0.5), self.center_y - 30),
                     (int(self.width * 0.8), self.center_y + 30),
                     (100, 100, 200), -1)  # Material B

        # Temperature gradient (hot to cold)
        # Hot end
        for i in range(int(bass * 20)):
            x = int(self.width * 0.2 - 30 + np.random.random() * 20)
            y = int(self.center_y + np.random.random() * 60 - 30)
            cv2.circle(frame, (x, y), 3, (255, 200, 100), -1)

        # Cold end
        for i in range(int(highs * 15)):
            x = int(self.width * 0.8 + 10 + np.random.random() * 20)
            y = int(self.center_y + np.random.random() * 60 - 30)
            cv2.circle(frame, (x, y), 3, (100, 200, 255), -1)

        # Generated voltage
        if bass > 0.4:
            cv2.putText(frame, f"V = {bass:.2f}", (int(self.width * 0.45), self.center_y - 50),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 100), 2)

        return frame

    def draw_mode_443_photon_entanglement(self, frame, magnitudes):
        """Mode 443: Quantum entangled photon pairs"""
        # Photon source
        cv2.circle(frame, (self.center_x, self.center_y), 20, (255, 255, 100), -1)

        # Entangled pairs moving apart
        separation = (self.frame_count * 3) % 300

        # Photon 1 (left)
        photon1_x = int(self.center_x - separation)
        photon1_y = self.center_y

        # Photon 2 (right)
        photon2_x = int(self.center_x + separation)
        photon2_y = self.center_y

        # Draw photons
        cv2.circle(frame, (photon1_x, photon1_y), 10, (255, 100, 100), -1)
        cv2.circle(frame, (photon2_x, photon2_y), 10, (100, 100, 255), -1)

        # Entanglement connection (spooky action at distance)
        cv2.line(frame, (photon1_x, photon1_y), (photon2_x, photon2_y),
                (200, 200, 255), 1, lineType=cv2.LINE_AA)

        # Spin correlation
        bass = self.get_bass(magnitudes)
        if bass > 0.5:
            # Both have same polarization
            cv2.line(frame, (photon1_x - 15, photon1_y - 15),
                    (photon1_x + 15, photon1_y + 15), (255, 255, 255), 2)
            cv2.line(frame, (photon2_x - 15, photon2_y - 15),
                    (photon2_x + 15, photon2_y + 15), (255, 255, 255), 2)

        return frame

    def draw_mode_444_superfluidity(self, frame, magnitudes):
        """Mode 444: Superfluid helium climbing walls"""
        bass = self.get_bass(magnitudes)

        # Container
        container_left = int(self.width * 0.3)
        container_right = int(self.width * 0.7)
        container_bottom = int(self.height * 0.8)

        cv2.line(frame, (container_left, container_bottom),
                (container_left, int(self.height * 0.5)), (150, 150, 150), 5)
        cv2.line(frame, (container_right, container_bottom),
                (container_right, int(self.height * 0.5)), (150, 150, 150), 5)
        cv2.line(frame, (container_left, container_bottom),
                (container_right, container_bottom), (150, 150, 150), 5)

        # Superfluid level
        fluid_level = int(self.height * 0.7)

        # Bulk fluid
        cv2.rectangle(frame, (container_left, fluid_level),
                     (container_right, container_bottom), (100, 180, 255), -1)

        # Superfluid film climbing walls (zero viscosity)
        if bass > 0.3:
            film_height = int(bass * 150)

            # Left wall
            for i in range(film_height):
                y = fluid_level - i
                cv2.circle(frame, (container_left - 2, y), 2, (150, 220, 255), -1)

            # Right wall
            for i in range(film_height):
                y = fluid_level - i
                cv2.circle(frame, (container_right + 2, y), 2, (150, 220, 255), -1)

        return frame

    def draw_mode_445_piezoelectric(self, frame, magnitudes):
        """Mode 445: Piezoelectric crystal stress/voltage"""
        bass = self.get_bass(magnitudes)

        # Crystal
        crystal_pts = np.array([
            [self.center_x, self.center_y - 80],
            [self.center_x - 60, self.center_y],
            [self.center_x, self.center_y + 80],
            [self.center_x + 60, self.center_y]
        ], dtype=np.int32)

        # Deformation based on bass
        deformation = int(bass * 20)
        crystal_pts[0][1] -= deformation  # Top compressed
        crystal_pts[2][1] += deformation  # Bottom extended

        cv2.fillPoly(frame, [crystal_pts], (150, 180, 200))

        # Charge separation (voltage generated)
        if bass > 0.4:
            # Positive charges on top
            for i in range(5):
                x = int(self.center_x - 30 + i * 15)
                y = int(self.center_y - 80 - deformation)
                cv2.circle(frame, (x, y), 5, (255, 100, 100), -1)
                cv2.putText(frame, "+", (x - 5, y + 5),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            # Negative charges on bottom
            for i in range(5):
                x = int(self.center_x - 30 + i * 15)
                y = int(self.center_y + 80 + deformation)
                cv2.circle(frame, (x, y), 5, (100, 100, 255), -1)
                cv2.putText(frame, "-", (x - 5, y + 5),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        return frame

    def draw_mode_446_zeeman_effect(self, frame, magnitudes):
        """Mode 446: Zeeman effect spectral line splitting"""
        # Without magnetic field - single spectral line
        cv2.line(frame, (int(self.width * 0.1), int(self.height * 0.3)),
                (int(self.width * 0.4), int(self.height * 0.3)),
                (255, 255, 100), 3)

        # With magnetic field - split lines
        bass = self.get_bass(magnitudes)
        splitting = int(bass * 30)

        # Center line
        cv2.line(frame, (int(self.width * 0.6), int(self.height * 0.3)),
                (int(self.width * 0.9), int(self.height * 0.3)),
                (255, 255, 100), 3)

        # Split lines
        cv2.line(frame, (int(self.width * 0.6), int(self.height * 0.3 - splitting)),
                (int(self.width * 0.9), int(self.height * 0.3 - splitting)),
                (255, 200, 100), 2)

        cv2.line(frame, (int(self.width * 0.6), int(self.height * 0.3 + splitting)),
                (int(self.width * 0.9), int(self.height * 0.3 + splitting)),
                (255, 200, 100), 2)

        # Magnetic field indicator
        cv2.putText(frame, "B = 0", (int(self.width * 0.2), int(self.height * 0.2)),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, f"B = {bass:.1f}T", (int(self.width * 0.7), int(self.height * 0.2)),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        return frame

    def draw_mode_447_cyclotron_motion(self, frame, magnitudes):
        """Mode 447: Charged particle in magnetic field"""
        # Magnetic field (perpendicular to screen)
        for y in range(50, self.height - 50, 40):
            for x in range(50, self.width - 50, 40):
                cv2.circle(frame, (x, y), 3, (150, 150, 200), -1)

        # Particle spiraling
        bass = self.get_bass(magnitudes)
        radius = 80 + bass * 80

        for i in range(20):
            angle = (self.frame_count * 0.1 + i * 0.3) % (2 * np.pi)

            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)

            size = 8 - i // 3
            alpha = 255 - i * 12

            cv2.circle(frame, (x, y), max(2, size), (alpha, alpha // 2, 255), -1)

        return frame

    def draw_mode_448_fusion_reactor(self, frame, magnitudes):
        """Mode 448: Tokamak fusion reactor plasma"""
        energy = self.get_energy(magnitudes)

        # Toroidal chamber
        cv2.ellipse(frame, (self.center_x, self.center_y), (self.max_radius, self.max_radius // 2),
                   0, 0, 360, (100, 100, 150), 5)

        # Hot plasma (confined by magnetic field)
        num_particles = int(energy * 150)
        for i in range(num_particles):
            angle = (i / num_particles) * 2 * np.pi + self.frame_count * 0.1

            # Toroidal path
            major_r = self.max_radius * 0.7
            minor_r = self.max_radius * 0.3

            x = int(self.center_x + (major_r + minor_r * np.cos(i * 5)) * np.cos(angle))
            y = int(self.center_y + (major_r + minor_r * np.cos(i * 5)) * np.sin(angle) * 0.5)

            # Temperature color (very hot)
            temp = energy * 255
            cv2.circle(frame, (x, y), 2, (int(temp), int(temp * 0.8), 255), -1)

        return frame

    def draw_mode_449_antimatter(self, frame, magnitudes):
        """Mode 449: Matter-antimatter annihilation"""
        bass = self.get_bass(magnitudes)

        # Matter particle (electron)
        matter_x = int(self.center_x - 50 - bass * 30)
        cv2.circle(frame, (matter_x, self.center_y), 15, (100, 200, 255), -1)
        cv2.putText(frame, "e-", (matter_x - 10, self.center_y + 5),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Antimatter particle (positron)
        antimatter_x = int(self.center_x + 50 + bass * 30)
        cv2.circle(frame, (antimatter_x, self.center_y), 15, (255, 200, 100), -1)
        cv2.putText(frame, "e+", (antimatter_x - 10, self.center_y + 5),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Annihilation (when they meet)
        if bass > 0.7:
            # Gamma rays produced
            for i in range(8):
                angle = (i / 8) * 2 * np.pi
                length = bass * 150

                x2 = int(self.center_x + np.cos(angle) * length)
                y2 = int(self.center_y + np.sin(angle) * length)

                cv2.line(frame, (self.center_x, self.center_y), (x2, y2),
                        (255, 255, 255), 3)

            # Energy release
            cv2.putText(frame, "E = mc²", (self.center_x - 40, self.center_y - 40),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 100), 2)

        return frame

    def draw_mode_450_hawking_radiation(self, frame, magnitudes):
        """Mode 450: Black hole Hawking radiation"""
        # Event horizon
        horizon_radius = 60
        cv2.circle(frame, (self.center_x, self.center_y), horizon_radius, (0, 0, 0), -1)
        cv2.circle(frame, (self.center_x, self.center_y), horizon_radius, (100, 100, 150), 2)

        # Quantum fluctuations near horizon
        energy = self.get_energy(magnitudes)

        for i in range(int(energy * 30)):
            angle = np.random.random() * 2 * np.pi
            dist = horizon_radius + np.random.random() * 40

            x = int(self.center_x + np.cos(angle) * dist)
            y = int(self.center_y + np.sin(angle) * dist)

            # Virtual particle pairs
            if np.random.random() > 0.5:
                # Escaping particle (Hawking radiation)
                cv2.circle(frame, (x, y), 3, (255, 255, 200), -1)
            else:
                # Falls into black hole
                cv2.circle(frame, (x, y), 3, (150, 150, 200), -1)

        # Accretion disk
        for i, mag in enumerate(magnitudes[::3]):
            angle = (i / 40) * 2 * np.pi + self.frame_count * 0.05
            radius = horizon_radius + 80 + i * 3

            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius * 0.4)

            hue = int((1 - i / 40) * 40)  # Hot to cool
            color = self.hsv_to_bgr(hue, 255, int(mag * 255))

            cv2.circle(frame, (x, y), 2 + int(mag * 5), color, -1)

        return frame

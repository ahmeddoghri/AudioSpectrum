"""
Audio Spectrum Visualization Modes 451-500
Science & Physics Category (Part 2)
"""
from .base import BaseModeVisualizer
import numpy as np
import cv2


class Modes451_500(BaseModeVisualizer):
    """Visualization modes 451 through 500 - Science & Physics"""

    def __init__(self, visualizer):
        super().__init__(visualizer)

    def draw_mode_451_heisenberg_uncertainty(self, frame, magnitudes):
        """Mode 451: Heisenberg uncertainty principle visualization"""
        bass = self.get_bass(magnitudes)

        # Precise position, uncertain momentum
        if bass < 0.5:
            x_uncertainty = 10
            p_uncertainty = 100
        else:
            # Precise momentum, uncertain position
            x_uncertainty = 100
            p_uncertainty = 10

        # Position distribution
        for i in range(50):
            x = int(self.center_x + np.random.normal(0, x_uncertainty))
            cv2.circle(frame, (x, int(self.height * 0.3)), 3, (255, 200, 200), -1)

        # Momentum distribution
        for i in range(50):
            px = int(self.center_x + np.random.normal(0, p_uncertainty))
            cv2.circle(frame, (px, int(self.height * 0.7)), 3, (200, 200, 255), -1)

        return frame

    def draw_mode_452_particle_decay(self, frame, magnitudes):
        """Mode 452: Radioactive particle decay chain"""
        energy = self.get_energy(magnitudes)

        # Parent particle
        cv2.circle(frame, (self.center_x, self.center_y - 100), 25, (200, 100, 100), -1)

        # Decay products
        if energy > 0.4:
            # Alpha particle
            cv2.circle(frame, (self.center_x - 80, self.center_y), 15, (255, 200, 100), -1)
            # Daughter nucleus
            cv2.circle(frame, (self.center_x + 80, self.center_y), 20, (100, 200, 100), -1)
            # Gamma ray
            cv2.line(frame, (self.center_x, self.center_y + 50),
                    (self.center_x, self.center_y + 150), (255, 255, 100), 3)

        return frame

    def draw_mode_453_laser_cavity(self, frame, magnitudes):
        """Mode 453: Laser optical cavity resonance"""
        # Mirrors
        cv2.line(frame, (100, 100), (100, self.height - 100), (200, 200, 200), 10)
        cv2.line(frame, (self.width - 100, 100), (self.width - 100, self.height - 100), (200, 200, 200), 10)

        # Photons bouncing
        for i, mag in enumerate(magnitudes[::5]):
            phase = (self.frame_count + i * 20) % 200

            if phase < 100:
                x = 100 + phase * (self.width - 200) / 100
            else:
                x = self.width - 100 - (phase - 100) * (self.width - 200) / 100

            y = int(self.center_y + np.sin(phase * 0.1) * 50)

            cv2.circle(frame, (int(x), y), 5, (255, int(mag * 255), 100), -1)

        return frame

    def draw_mode_454_dielectric_breakdown(self, frame, magnitudes):
        """Mode 454: Electric breakdown in dielectric"""
        highs = self.get_highs(magnitudes)

        if highs > 0.6:
            # Lightning-like breakdown path
            x, y = self.width // 2, 0

            for step in range(20):
                x2 = x + int(np.random.random() * 60 - 30)
                y2 = y + int(np.random.random() * 40 + 30)

                cv2.line(frame, (x, y), (x2, y2), (200, 220, 255), 3)
                x, y = x2, y2

                if y > self.height:
                    break

        return frame

    def draw_mode_455_casimir_effect(self, frame, magnitudes):
        """Mode 455: Casimir effect between plates"""
        # Two parallel plates
        plate1_x = int(self.width * 0.4)
        plate2_x = int(self.width * 0.6)

        cv2.rectangle(frame, (plate1_x - 10, 100), (plate1_x + 10, self.height - 100), (150, 150, 150), -1)
        cv2.rectangle(frame, (plate2_x - 10, 100), (plate2_x + 10, self.height - 100), (150, 150, 150), -1)

        bass = self.get_bass(magnitudes)

        # Virtual particles (more outside than inside)
        # Outside left
        for i in range(20):
            x = int(np.random.random() * (plate1_x - 50))
            y = int(np.random.random() * self.height)
            cv2.circle(frame, (x, y), 2, (200, 200, 255), -1)

        # Outside right
        for i in range(20):
            x = int(plate2_x + 50 + np.random.random() * (self.width - plate2_x - 50))
            y = int(np.random.random() * self.height)
            cv2.circle(frame, (x, y), 2, (200, 200, 255), -1)

        # Inside (fewer particles creates pressure difference)
        for i in range(5):
            x = int(plate1_x + np.random.random() * (plate2_x - plate1_x))
            y = int(np.random.random() * self.height)
            cv2.circle(frame, (x, y), 2, (255, 200, 200), -1)

        # Plates attracted (get closer)
        separation = int((plate2_x - plate1_x) * (1 - bass * 0.3))
        cv2.putText(frame, f"F = {bass:.2f}", (self.center_x - 30, 50),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        return frame

    def draw_mode_456_sonochemistry(self, frame, magnitudes):
        """Mode 456: Sonochemistry cavitation bubbles"""
        bass = self.get_bass(magnitudes)

        # Ultrasound creates bubbles
        for i in range(int(bass * 30)):
            x = int(np.random.random() * self.width)
            y = int(np.random.random() * self.height)

            # Bubble collapse creates hotspots
            if np.random.random() < bass:
                # Collapsing bubble with high temperature
                for r in range(5):
                    cv2.circle(frame, (x, y), 20 - r * 4, (255, 200 - r * 40, 100 - r * 20), 2)
            else:
                cv2.circle(frame, (x, y), 15, (100, 150, 200), 2)

        return frame

    def draw_mode_457_phonon_propagation(self, frame, magnitudes):
        """Mode 457: Phonons in crystal lattice"""
        spacing = 40

        for i, mag in enumerate(magnitudes[::3]):
            phase = (i / 40) * self.width

            for y in range(0, self.height, spacing):
                for x in range(0, self.width, spacing):
                    # Lattice vibration (phonon wave)
                    displacement = np.sin((x - phase) * 0.05) * mag * 15

                    px = int(x + displacement)
                    py = y

                    cv2.circle(frame, (px, py), 5, (150, 200, 200), -1)

        return frame

    def draw_mode_458_pair_production(self, frame, magnitudes):
        """Mode 458: Photon pair production"""
        energy = self.get_energy(magnitudes)

        if energy > 0.5:
            # High energy photon
            cv2.line(frame, (0, self.center_y), (self.center_x - 50, self.center_y),
                    (255, 255, 100), 4)

            # Produces electron-positron pair
            # Electron
            angle1 = 45
            x1 = int(self.center_x + np.cos(np.deg2rad(angle1)) * 100)
            y1 = int(self.center_y - np.sin(np.deg2rad(angle1)) * 100)
            cv2.line(frame, (self.center_x, self.center_y), (x1, y1), (100, 200, 255), 3)

            # Positron
            angle2 = -45
            x2 = int(self.center_x + np.cos(np.deg2rad(angle2)) * 100)
            y2 = int(self.center_y - np.sin(np.deg2rad(angle2)) * 100)
            cv2.line(frame, (self.center_x, self.center_y), (x2, y2), (255, 200, 100), 3)

        return frame

    def draw_mode_459_stefan_boltzmann(self, frame, magnitudes):
        """Mode 459: Stefan-Boltzmann radiation law"""
        bass = self.get_bass(magnitudes)

        # Temperature
        temperature = bass * 5000 + 1000

        # Blackbody
        cv2.circle(frame, (self.center_x, self.center_y), 60, (int(bass * 255), int(bass * 200), 100), -1)

        # Radiation (proportional to T^4)
        radiation = int((bass ** 4) * 100)

        for i in range(radiation):
            angle = np.random.random() * 2 * np.pi
            dist = 70 + np.random.random() * 150

            x = int(self.center_x + np.cos(angle) * dist)
            y = int(self.center_y + np.sin(angle) * dist)

            cv2.circle(frame, (x, y), 2, (255, 220, 150), -1)

        cv2.putText(frame, f"T = {int(temperature)}K", (self.center_x - 50, self.center_y + 100),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        return frame

    def draw_mode_460_eddy_currents(self, frame, magnitudes):
        """Mode 460: Eddy currents in conductor"""
        bass = self.get_bass(magnitudes)

        # Conductor plate
        cv2.rectangle(frame, (int(self.width * 0.3), int(self.height * 0.3)),
                     (int(self.width * 0.7), int(self.height * 0.7)),
                     (150, 150, 150), -1)

        # Moving magnet
        magnet_x = int(self.width * 0.3 + bass * (self.width * 0.4))
        cv2.rectangle(frame, (magnet_x - 20, int(self.height * 0.2)),
                     (magnet_x + 20, int(self.height * 0.3)), (200, 100, 100), -1)

        # Circular eddy currents
        for i in range(3):
            center_x = int(self.width * (0.4 + i * 0.15))

            for j in range(8):
                angle = (j / 8) * 2 * np.pi + self.frame_count * 0.1
                radius = 40

                x = int(center_x + np.cos(angle) * radius)
                y = int(self.center_y + np.sin(angle) * radius)

                cv2.circle(frame, (x, y), 3, (255, 200, 100), -1)

        return frame

    def draw_mode_461_wavefunction_collapse(self, frame, magnitudes):
        """Mode 461: Quantum wavefunction collapse on measurement"""
        bass = self.get_bass(magnitudes)

        if bass < 0.5:
            # Before measurement - spread out wavefunction
            for i, mag in enumerate(magnitudes):
                x = int((i / len(magnitudes)) * self.width)
                amplitude = mag * 100

                y1 = int(self.center_y - amplitude)
                y2 = int(self.center_y + amplitude)

                cv2.line(frame, (x, y1), (x, y2), (150, 200, 255), 1)
        else:
            # After measurement - collapsed to eigenstate
            x_pos = int(bass * self.width)
            cv2.line(frame, (x_pos, 0), (x_pos, self.height), (255, 200, 200), 5)
            cv2.circle(frame, (x_pos, self.center_y), 20, (255, 100, 100), -1)

        return frame

    def draw_mode_462_qed_feynman(self, frame, magnitudes):
        """Mode 462: QED Feynman diagram"""
        # Electron incoming
        cv2.line(frame, (100, self.center_y - 50), (self.center_x - 50, self.center_y),
                (100, 200, 255), 3)

        # Electron outgoing
        cv2.line(frame, (self.center_x + 50, self.center_y), (self.width - 100, self.center_y - 50),
                (100, 200, 255), 3)

        # Virtual photon exchange (wavy line)
        num_waves = 8
        points = []
        for i in range(num_waves + 1):
            x = self.center_x - 50 + i * 100 / num_waves
            y = self.center_y + np.sin(i * np.pi) * 20
            points.append([int(x), int(y)])

        points = np.array(points, dtype=np.int32)
        for i in range(len(points) - 1):
            cv2.line(frame, tuple(points[i]), tuple(points[i + 1]), (255, 255, 100), 2)

        # Vertices
        cv2.circle(frame, (self.center_x - 50, self.center_y), 8, (255, 200, 200), -1)
        cv2.circle(frame, (self.center_x + 50, self.center_y), 8, (255, 200, 200), -1)

        return frame

    def draw_mode_463_holography(self, frame, magnitudes):
        """Mode 463: Holographic interference pattern"""
        # Reference beam
        for i in range(0, self.height, 10):
            cv2.line(frame, (0, i), (self.width, i), (100, 100, 100), 1)

        # Object beam creates interference
        for i, mag in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * self.width)

            # Interference pattern
            for y in range(0, self.height, 5):
                interference = np.sin(x * 0.1) * np.cos(y * 0.1) * mag
                brightness = int(127 + interference * 128)

                cv2.circle(frame, (x, y), 2, (brightness, brightness, brightness), -1)

        return frame

    def draw_mode_464_metamaterial(self, frame, magnitudes):
        """Mode 464: Metamaterial negative refraction"""
        # Normal material (positive refraction)
        incident_angle = 30
        refract_angle = 20

        # Interface
        cv2.line(frame, (self.center_x, 0), (self.center_x, self.height), (200, 200, 200), 2)

        # Incident ray
        x1 = int(self.center_x - 100 * np.tan(np.deg2rad(incident_angle)))
        cv2.line(frame, (x1, 0), (self.center_x, self.center_y), (255, 255, 100), 3)

        # Negative refraction in metamaterial
        bass = self.get_bass(magnitudes)
        if bass > 0.5:
            # Negative index - ray bends wrong way
            x2 = int(self.center_x - 100 * np.tan(np.deg2rad(refract_angle)))
        else:
            # Positive index - normal refraction
            x2 = int(self.center_x + 100 * np.tan(np.deg2rad(refract_angle)))

        cv2.line(frame, (self.center_x, self.center_y), (x2, self.height), (255, 200, 100), 3)

        return frame

    def draw_mode_465_photodiode(self, frame, magnitudes):
        """Mode 465: Photodiode photocurrent generation"""
        highs = self.get_highs(magnitudes)

        # Photodiode
        cv2.rectangle(frame, (int(self.width * 0.4), int(self.height * 0.4)),
                     (int(self.width * 0.6), int(self.height * 0.6)),
                     (120, 120, 160), -1)

        # Incoming photons
        for i in range(int(highs * 20)):
            x = int(self.width * (0.45 + np.random.random() * 0.1))
            y = int((self.frame_count * 3 + i * 15) % (self.height * 0.4))

            cv2.circle(frame, (x, y), 5, (255, 255, 100), -1)

        # Generated electron-hole pairs
        current = int(highs * 100)

        for i in range(current):
            x = int(self.width * (0.4 + np.random.random() * 0.2))
            y = int(self.height * (0.4 + np.random.random() * 0.2))

            # Electrons
            cv2.circle(frame, (x, y), 2, (100, 200, 255), -1)

        cv2.putText(frame, f"I = {highs:.2f}A", (int(self.width * 0.45), int(self.height * 0.7)),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        return frame

    def draw_mode_466_bremsstrahlung(self, frame, magnitudes):
        """Mode 466: Bremsstrahlung X-ray emission"""
        bass = self.get_bass(magnitudes)

        # Electron beam
        electron_x = int((self.frame_count * 5) % (self.width * 0.6))
        cv2.line(frame, (0, self.center_y), (electron_x, self.center_y), (100, 200, 255), 3)

        # Target nucleus
        target_x = int(self.width * 0.6)
        cv2.circle(frame, (target_x, self.center_y), 25, (200, 100, 100), -1)

        # When electron passes near nucleus
        if abs(electron_x - target_x) < 50:
            # Electron deflects
            deflect_y = self.center_y + int(bass * 80)
            cv2.line(frame, (target_x, self.center_y), (self.width, deflect_y), (100, 200, 255), 3)

            # X-ray emitted
            for i in range(5):
                angle = -30 + i * 15
                rad = np.deg2rad(angle)
                length = 150

                x = int(target_x + np.cos(rad) * length)
                y = int(self.center_y - np.sin(rad) * length)

                cv2.line(frame, (target_x, self.center_y), (x, y), (200, 200, 255), 2)

        return frame

    def draw_mode_467_optogenetics(self, frame, magnitudes):
        """Mode 467: Optogenetics light-controlled neurons"""
        bass = self.get_bass(magnitudes)

        # Neuron
        cv2.circle(frame, (self.center_x, self.center_y), 40, (200, 150, 200), -1)

        # Light pulse
        if bass > 0.5:
            # Blue light activation
            for r in range(5):
                cv2.circle(frame, (self.center_x, self.center_y - 100), 30 + r * 20,
                          (100, 100, 255 - r * 50), 2)

            # Neuron fires
            cv2.circle(frame, (self.center_x, self.center_y), 45, (255, 255, 100), 3)

            # Action potential
            axon_x = self.center_x + 40 + int((self.frame_count % 30) * 8)
            cv2.circle(frame, (axon_x, self.center_y), 12, (255, 255, 100), -1)

        return frame

    def draw_mode_468_topological_insulator(self, frame, magnitudes):
        """Mode 468: Topological insulator edge states"""
        # Bulk (insulating)
        for y in range(100, self.height - 100, 30):
            for x in range(100, self.width - 100, 30):
                cv2.circle(frame, (x, y), 5, (100, 100, 150), -1)

        # Edge states (conducting)
        energy = self.get_energy(magnitudes)

        # Top edge
        for i in range(int(energy * 50)):
            x = int((i / 50) * self.width)
            phase = self.frame_count * 0.1 + i * 0.2

            if (int(phase) % 2) == 0:
                cv2.circle(frame, (x, 80), 4, (255, 200, 100), -1)

        # Bottom edge
        for i in range(int(energy * 50)):
            x = int((i / 50) * self.width)
            phase = self.frame_count * 0.1 - i * 0.2

            if (int(phase) % 2) == 0:
                cv2.circle(frame, (x, self.height - 80), 4, (255, 200, 100), -1)

        return frame

    def draw_mode_469_nernst_equation(self, frame, magnitudes):
        """Mode 469: Nernst equation ion concentration"""
        bass = self.get_bass(magnitudes)

        # Membrane
        cv2.line(frame, (self.center_x, 100), (self.center_x, self.height - 100), (150, 150, 150), 5)

        # High concentration side (left)
        for i in range(50):
            x = int(np.random.random() * (self.center_x - 100))
            y = int(np.random.random() * (self.height - 200) + 100)
            cv2.circle(frame, (x, y), 4, (255, 200, 100), -1)

        # Low concentration side (right)
        for i in range(10):
            x = int(self.center_x + 100 + np.random.random() * (self.width - self.center_x - 100))
            y = int(np.random.random() * (self.height - 200) + 100)
            cv2.circle(frame, (x, y), 4, (255, 200, 100), -1)

        # Voltage difference
        voltage = bass * 100
        cv2.putText(frame, f"V = {int(voltage)}mV", (self.center_x - 50, 50),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        return frame

    def draw_mode_470_mri_precession(self, frame, magnitudes):
        """Mode 470: MRI nuclear magnetic resonance"""
        # Magnetic field direction
        cv2.line(frame, (self.center_x, 0), (self.center_x, self.height), (100, 100, 200), 3)

        # Nuclear spins precessing
        for i, mag in enumerate(magnitudes[::5]):
            offset_y = int((i / 24) * self.height)

            angle = self.frame_count * 0.1 + i
            radius = 30 + mag * 30

            x = int(self.center_x + np.cos(angle) * radius)
            y = int(offset_y + np.sin(angle) * radius * 0.3)

            # Spin vector
            cv2.line(frame, (self.center_x, offset_y), (x, y), (255, 200, 200), 2)
            cv2.circle(frame, (x, y), 6, (255, 150, 150), -1)

        return frame

    # For brevity, creating more concise modes from 471-500
    def draw_mode_471_josephson_junction(self, frame, magnitudes):
        """Mode 471: Josephson junction supercurrent"""
        cv2.rectangle(frame, (int(self.width * 0.3), self.center_y - 40),
                     (int(self.width * 0.48), self.center_y + 40), (150, 180, 200), -1)
        cv2.rectangle(frame, (int(self.width * 0.52), self.center_y - 40),
                     (int(self.width * 0.7), self.center_y + 40), (150, 180, 200), -1)

        bass = self.get_bass(magnitudes)
        if bass > 0.4:
            for i in range(int(bass * 20)):
                x = int(self.width * (0.48 + np.random.random() * 0.04))
                y = int(self.center_y + np.random.random() * 80 - 40)
                cv2.circle(frame, (x, y), 3, (255, 200, 100), -1)
        return frame

    def draw_mode_472_liquid_crystal(self, frame, magnitudes):
        """Mode 472: Liquid crystal alignment"""
        spacing = 40
        bass = self.get_bass(magnitudes)
        angle_offset = bass * 90

        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                angle = np.deg2rad(angle_offset)
                x2 = int(x + np.cos(angle) * 20)
                y2 = int(y + np.sin(angle) * 20)
                cv2.line(frame, (x, y), (x2, y2), (150, 200, 255), 2)
        return frame

    def draw_mode_473_rydberg_atoms(self, frame, magnitudes):
        """Mode 473: Rydberg atoms with large orbitals"""
        for i, mag in enumerate(magnitudes[::10]):
            radius = 50 + i * 40 + mag * 60
            cv2.circle(frame, (self.center_x, self.center_y), int(radius),
                      (150, 150, 200), 2)
        cv2.circle(frame, (self.center_x, self.center_y), 10, (255, 200, 100), -1)
        return frame

    def draw_mode_474_cavity_qed(self, frame, magnitudes):
        """Mode 474: Cavity QED atom-photon coupling"""
        cv2.rectangle(frame, (200, 100), (self.width - 200, self.height - 100),
                     (120, 120, 140), 3)
        cv2.circle(frame, (self.center_x, self.center_y), 20, (200, 150, 200), -1)

        bass = self.get_bass(magnitudes)
        if bass > 0.5:
            for i in range(8):
                angle = (i / 8) * 2 * np.pi
                x = int(self.center_x + np.cos(angle + self.frame_count * 0.1) * 50)
                y = int(self.center_y + np.sin(angle + self.frame_count * 0.1) * 50)
                cv2.circle(frame, (x, y), 5, (255, 255, 100), -1)
        return frame

    def draw_mode_475_quantum_dots(self, frame, magnitudes):
        """Mode 475: Quantum dots emission"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            y = int(self.height * 0.7)

            cv2.circle(frame, (x, y), 8, (150, 150, 200), -1)

            if mag > 0.4:
                hue = int((i / 30) * 180)
                color = self.hsv_to_bgr(hue, 255, 255)

                for j in range(10):
                    py = int(y - j * 20 - (self.frame_count % 20))
                    if py > 0:
                        cv2.circle(frame, (x, py), 3, color, -1)
        return frame

    def draw_mode_476_soliton_wave(self, frame, magnitudes):
        """Mode 476: Soliton solitary wave"""
        phase = self.frame_count * 0.05

        for i, mag in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * self.width)

            # Soliton shape (sech function approximation)
            dist_from_center = abs(x - self.center_x - phase * 100) / 100
            amplitude = mag * 80 / (1 + dist_from_center**2)

            y = int(self.center_y - amplitude)
            cv2.circle(frame, (x, y), 3, (150, 200, 255), -1)

        # Water level
        cv2.line(frame, (0, self.center_y), (self.width, self.center_y), (100, 150, 200), 1)
        return frame

    def draw_mode_477_acoustic_levitation(self, frame, magnitudes):
        """Mode 477: Acoustic levitation standing wave"""
        # Sound emitter (bottom)
        cv2.rectangle(frame, (int(self.width * 0.3), self.height - 50),
                     (int(self.width * 0.7), self.height), (120, 120, 140), -1)

        # Standing wave nodes
        num_nodes = 5
        for i in range(num_nodes):
            y = int(self.height - 100 - i * 100)
            cv2.line(frame, (int(self.width * 0.3), y), (int(self.width * 0.7), y),
                    (180, 180, 180), 1)

        # Levitated particles at nodes
        bass = self.get_bass(magnitudes)
        for i in range(num_nodes):
            y = int(self.height - 100 - i * 100)
            x = int(self.width * (0.4 + np.sin(self.frame_count * 0.1) * 0.1))

            cv2.circle(frame, (x, y), 8, (255, int(bass * 200), 100), -1)
        return frame

    def draw_mode_478_mosfet_channel(self, frame, magnitudes):
        """Mode 478: MOSFET inversion channel"""
        # Gate
        cv2.rectangle(frame, (int(self.width * 0.3), int(self.height * 0.3)),
                     (int(self.width * 0.7), int(self.height * 0.35)),
                     (180, 180, 200), -1)

        bass = self.get_bass(magnitudes)

        # Channel (forms when gate voltage applied)
        if bass > 0.5:
            # Electron channel
            for i in range(int(bass * 50)):
                x = int(self.width * (0.3 + np.random.random() * 0.4))
                y = int(self.height * 0.37)
                cv2.circle(frame, (x, y), 2, (100, 200, 255), -1)

            cv2.putText(frame, "ON", (self.center_x - 20, self.center_y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (100, 255, 100), 2)
        else:
            cv2.putText(frame, "OFF", (self.center_x - 30, self.center_y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 100, 100), 2)
        return frame

    def draw_mode_479_spintronics(self, frame, magnitudes):
        """Mode 479: Spintronics spin current"""
        # Spin up electrons (left side)
        for i in range(20):
            x = int(self.width * (0.1 + i * 0.015))
            y = int(self.center_y + np.sin(i * 0.5) * 50)

            cv2.circle(frame, (x, y), 5, (255, 100, 100), -1)
            # Up arrow
            cv2.line(frame, (x, y), (x, y - 15), (255, 255, 255), 2)

        # Spin down electrons (right side)
        for i in range(20):
            x = int(self.width * (0.5 + i * 0.015))
            y = int(self.center_y + np.sin(i * 0.5) * 50)

            cv2.circle(frame, (x, y), 5, (100, 100, 255), -1)
            # Down arrow
            cv2.line(frame, (x, y), (x, y + 15), (255, 255, 255), 2)
        return frame

    def draw_mode_480_electrochemistry(self, frame, magnitudes):
        """Mode 480: Electrochemical cell redox reaction"""
        # Anode
        cv2.rectangle(frame, (int(self.width * 0.2), int(self.height * 0.3)),
                     (int(self.width * 0.3), int(self.height * 0.7)),
                     (200, 150, 100), -1)

        # Cathode
        cv2.rectangle(frame, (int(self.width * 0.7), int(self.height * 0.3)),
                     (int(self.width * 0.8), int(self.height * 0.7)),
                     (150, 150, 180), -1)

        # Ion flow in electrolyte
        bass = self.get_bass(magnitudes)
        for i in range(int(bass * 30)):
            phase = (self.frame_count + i * 10) % 100
            x = int(self.width * (0.3 + phase * 0.004))
            y = int(self.center_y + np.sin(phase * 0.1) * 100)

            cv2.circle(frame, (x, y), 4, (100, 200, 255), -1)
        return frame

    # Continuing with remaining modes 481-500 (more concise implementations)
    def draw_mode_481_langmuir_wave(self, frame, magnitudes):
        """Mode 481: Langmuir plasma oscillations"""
        for i, mag in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * self.width)
            y = int(self.center_y + np.sin(x * 0.05 + self.frame_count * 0.2) * mag * 80)
            cv2.circle(frame, (x, y), 3, (200, 150, 255), -1)
        return frame

    def draw_mode_482_bloch_sphere(self, frame, magnitudes):
        """Mode 482: Bloch sphere qubit state"""
        cv2.circle(frame, (self.center_x, self.center_y), self.max_radius // 2, (150, 150, 200), 2)
        bass = self.get_bass(magnitudes)
        theta = bass * np.pi
        phi = self.frame_count * 0.05

        x = int(self.center_x + self.max_radius // 2 * np.sin(theta) * np.cos(phi))
        y = int(self.center_y - self.max_radius // 2 * np.cos(theta))

        cv2.line(frame, (self.center_x, self.center_y), (x, y), (255, 200, 200), 3)
        cv2.circle(frame, (x, y), 10, (255, 100, 100), -1)
        return frame

    def draw_mode_483_curie_temperature(self, frame, magnitudes):
        """Mode 483: Curie temperature magnetic ordering"""
        bass = self.get_bass(magnitudes)
        spacing = 40

        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                if bass < 0.5:  # Below Curie temp - ordered
                    angle = 90
                else:  # Above Curie temp - random
                    angle = np.random.random() * 360

                rad = np.deg2rad(angle)
                x2 = int(x + np.cos(rad) * 15)
                y2 = int(y + np.sin(rad) * 15)
                cv2.line(frame, (x, y), (x2, y2), (200, 150, 200), 2)
        return frame

    def draw_mode_484_dyson_sphere(self, frame, magnitudes):
        """Mode 484: Dyson sphere energy collection"""
        # Central star
        cv2.circle(frame, (self.center_x, self.center_y), 40, (255, 255, 200), -1)

        # Sphere segments
        for i, mag in enumerate(magnitudes[::5]):
            angle = (i / 24) * 2 * np.pi
            radius = 120 + mag * 80

            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)

            cv2.circle(frame, (x, y), 15, (120, 120, 160), -1)
        return frame

    def draw_mode_485_graphene_lattice(self, frame, magnitudes):
        """Mode 485: Graphene hexagonal lattice"""
        spacing = 30
        for row in range(-1, self.height // spacing + 1):
            for col in range(-1, self.width // spacing + 1):
                x = col * spacing * 1.5
                y = row * spacing * np.sqrt(3)
                if col % 2:
                    y += spacing * np.sqrt(3) / 2

                cv2.circle(frame, (int(x), int(y)), 4, (100, 100, 100), -1)

                # Bonds
                for angle in [0, 60, 120]:
                    rad = np.deg2rad(angle)
                    x2 = int(x + np.cos(rad) * spacing)
                    y2 = int(y + np.sin(rad) * spacing)
                    cv2.line(frame, (int(x), int(y)), (x2, y2), (150, 150, 150), 1)
        return frame

    def draw_mode_486_memristor(self, frame, magnitudes):
        """Mode 486: Memristor resistance switching"""
        bass = self.get_bass(magnitudes)

        # Device
        cv2.rectangle(frame, (int(self.width * 0.4), int(self.height * 0.4)),
                     (int(self.width * 0.6), int(self.height * 0.6)),
                     (140, 140, 160), -1)

        # Internal state (oxygen vacancies position)
        vacancy_pos = bass * (self.width * 0.2)
        cv2.rectangle(frame, (int(self.width * 0.4), int(self.height * 0.4)),
                     (int(self.width * 0.4 + vacancy_pos), int(self.height * 0.6)),
                     (180, 120, 120), -1)

        cv2.putText(frame, f"R = {int((1 - bass) * 100)}Ω", (int(self.width * 0.42), int(self.height * 0.7)),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        return frame

    def draw_mode_487_quantum_hall(self, frame, magnitudes):
        """Mode 487: Quantum Hall effect edge states"""
        # Sample
        cv2.rectangle(frame, (200, 200), (self.width - 200, self.height - 200),
                     (120, 120, 160), 3)

        # Chiral edge states
        energy = self.get_energy(magnitudes)

        # Clockwise on top edge
        for i in range(int(energy * 30)):
            x = int(200 + (self.frame_count + i * 10) % (self.width - 400))
            cv2.circle(frame, (x, 195), 4, (255, 200, 100), -1)

        # Counter-clockwise on bottom edge
        for i in range(int(energy * 30)):
            x = int(self.width - 200 - (self.frame_count + i * 10) % (self.width - 400))
            cv2.circle(frame, (x, self.height - 195), 4, (100, 200, 255), -1)
        return frame

    def draw_mode_488_optomechanics(self, frame, magnitudes):
        """Mode 488: Cavity optomechanics"""
        # Optical cavity
        cv2.rectangle(frame, (int(self.width * 0.3), int(self.height * 0.3)),
                     (int(self.width * 0.7), int(self.height * 0.7)),
                     (140, 140, 160), 3)

        # Movable mirror
        bass = self.get_bass(magnitudes)
        mirror_x = int(self.width * (0.5 + bass * 0.1))

        cv2.line(frame, (mirror_x, int(self.height * 0.35)), (mirror_x, int(self.height * 0.65)),
                (200, 200, 220), 5)

        # Circulating photons
        for i in range(8):
            x = int(self.width * (0.35 + (self.frame_count + i * 20) % 100 * 0.003))
            cv2.circle(frame, (x, self.center_y), 5, (255, 255, 100), -1)
        return frame

    def draw_mode_489_exciton(self, frame, magnitudes):
        """Mode 489: Exciton electron-hole pair"""
        bass = self.get_bass(magnitudes)

        # Separation distance
        separation = 50 + bass * 100

        # Electron
        electron_x = int(self.center_x - separation)
        cv2.circle(frame, (electron_x, self.center_y), 15, (100, 200, 255), -1)
        cv2.putText(frame, "e-", (electron_x - 10, self.center_y + 5),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Hole
        hole_x = int(self.center_x + separation)
        cv2.circle(frame, (hole_x, self.center_y), 15, (255, 200, 100), -1)
        cv2.putText(frame, "h+", (hole_x - 10, self.center_y + 5),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Coulomb attraction
        cv2.line(frame, (electron_x, self.center_y), (hole_x, self.center_y),
                (200, 200, 255), 1, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_490_photonic_crystal(self, frame, magnitudes):
        """Mode 490: Photonic crystal band gap"""
        spacing = 50

        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                idx = ((y // spacing) * 20 + x // spacing) % len(magnitudes)
                mag = magnitudes[idx]

                # Periodic dielectric structure
                brightness = int(100 + mag * 155)
                cv2.circle(frame, (x, y), 20, (brightness, brightness, brightness), -1)
        return frame

    def draw_mode_491_skyrmion(self, frame, magnitudes):
        """Mode 491: Magnetic skyrmion texture"""
        # Topological spin texture
        for r in range(10):
            radius = 20 + r * 15

            for i in range(24):
                angle = (i / 24) * 2 * np.pi

                # Spin direction varies with radius
                spin_angle = angle + r * np.pi / 10

                x = int(self.center_x + np.cos(angle) * radius)
                y = int(self.center_y + np.sin(angle) * radius)

                x2 = int(x + np.cos(spin_angle) * 10)
                y2 = int(y + np.sin(spin_angle) * 10)

                hue = int((r / 10) * 180)
                color = self.hsv_to_bgr(hue, 200, 200)

                cv2.line(frame, (x, y), (x2, y2), color, 2)
        return frame

    def draw_mode_492_mott_insulator(self, frame, magnitudes):
        """Mode 492: Mott insulator transition"""
        spacing = 60
        bass = self.get_bass(magnitudes)

        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                cv2.circle(frame, (x, y), 12, (150, 150, 180), -1)

                # Exactly one electron per site (Mott state)
                cv2.circle(frame, (x, y), 5, (255, 200, 100), -1)

                # Cannot hop due to strong correlation
                if bass < 0.3:
                    cv2.circle(frame, (x, y), 20, (255, 100, 100), 2)
        return frame

    def draw_mode_493_squeezing(self, frame, magnitudes):
        """Mode 493: Quantum squeezing uncertainty"""
        bass = self.get_bass(magnitudes)

        # Coherent state (circular uncertainty)
        if bass < 0.5:
            cv2.ellipse(frame, (int(self.width * 0.3), self.center_y), (50, 50),
                       0, 0, 360, (200, 200, 255), 2)
        else:
            # Squeezed state (elliptical uncertainty)
            squeeze = 1 + bass * 2
            cv2.ellipse(frame, (int(self.width * 0.7), self.center_y),
                       (int(50 / squeeze), int(50 * squeeze)),
                       0, 0, 360, (255, 200, 200), 2)
        return frame

    def draw_mode_494_andreev_reflection(self, frame, magnitudes):
        """Mode 494: Andreev reflection at NS interface"""
        # Normal metal | Superconductor interface
        cv2.line(frame, (self.center_x, 0), (self.center_x, self.height), (200, 200, 200), 3)

        # Incoming electron
        cv2.line(frame, (100, self.center_y - 50), (self.center_x - 20, self.center_y - 50),
                (100, 200, 255), 3)

        # Reflected hole
        cv2.line(frame, (self.center_x - 20, self.center_y + 50), (100, self.center_y + 50),
                (255, 200, 100), 3)

        # Cooper pair in superconductor
        bass = self.get_bass(magnitudes)
        if bass > 0.4:
            cv2.line(frame, (self.center_x + 20, self.center_y - 10),
                    (self.width - 100, self.center_y - 10), (255, 255, 200), 3)
            cv2.line(frame, (self.center_x + 20, self.center_y + 10),
                    (self.width - 100, self.center_y + 10), (255, 255, 200), 3)
        return frame

    def draw_mode_495_casimir_polder(self, frame, magnitudes):
        """Mode 495: Casimir-Polder force on atom"""
        # Surface
        cv2.rectangle(frame, (0, self.height - 100), (self.width, self.height),
                     (150, 150, 150), -1)

        # Atom at varying height
        bass = self.get_bass(magnitudes)
        atom_y = int(self.height - 150 - bass * 200)

        cv2.circle(frame, (self.center_x, atom_y), 20, (200, 150, 200), -1)

        # Force arrow
        cv2.line(frame, (self.center_x, atom_y), (self.center_x, atom_y + 60),
                (255, 200, 100), 3)

        cv2.putText(frame, f"F ∝ 1/d⁴", (self.center_x + 40, atom_y),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        return frame

    def draw_mode_496_fano_resonance(self, frame, magnitudes):
        """Mode 496: Fano resonance asymmetric lineshape"""
        # Energy axis
        cv2.line(frame, (100, self.center_y), (self.width - 100, self.center_y),
                (200, 200, 200), 2)

        # Fano profile
        for i, mag in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * (self.width - 200) + 100)

            # Asymmetric Fano lineshape
            detuning = (i / len(magnitudes) - 0.5) * 4
            q = 2.0  # Fano parameter
            intensity = mag * ((q + detuning)**2) / (1 + detuning**2)

            y = int(self.center_y - intensity * 100)

            cv2.circle(frame, (x, y), 2, (200, 150, 255), -1)
        return frame

    def draw_mode_497_quantum_zeno(self, frame, magnitudes):
        """Mode 497: Quantum Zeno effect frequent measurement"""
        bass = self.get_bass(magnitudes)

        # Unobserved system (evolves)
        if bass < 0.3:
            phase = self.frame_count * 0.1
            x = int(self.width * (0.5 + 0.3 * np.cos(phase)))
            cv2.circle(frame, (x, int(self.height * 0.3)), 15, (150, 200, 255), -1)
        else:
            # Frequently observed (frozen)
            cv2.circle(frame, (int(self.width * 0.5), int(self.height * 0.3)), 15, (255, 200, 150), -1)

            # Measurement arrows
            for i in range(8):
                angle = (i / 8) * 2 * np.pi
                x1 = int(self.width * 0.5 + np.cos(angle) * 40)
                y1 = int(self.height * 0.3 + np.sin(angle) * 40)
                x2 = int(self.width * 0.5 + np.cos(angle) * 80)
                y2 = int(self.height * 0.3 + np.sin(angle) * 80)

                cv2.line(frame, (x1, y1), (x2, y2), (255, 200, 100), 2)
        return frame

    def draw_mode_498_rabi_oscillation(self, frame, magnitudes):
        """Mode 498: Rabi oscillation between states"""
        # Ground state population
        t = self.frame_count * 0.1
        bass = self.get_bass(magnitudes)
        omega_rabi = bass * 2

        pop_ground = (np.cos(omega_rabi * t / 2)**2)
        pop_excited = (np.sin(omega_rabi * t / 2)**2)

        # Ground state
        y_ground = int(self.height * 0.7)
        cv2.rectangle(frame, (int(self.width * 0.3), y_ground - 10),
                     (int(self.width * (0.3 + pop_ground * 0.4)), y_ground + 10),
                     (100, 200, 255), -1)

        # Excited state
        y_excited = int(self.height * 0.3)
        cv2.rectangle(frame, (int(self.width * 0.3), y_excited - 10),
                     (int(self.width * (0.3 + pop_excited * 0.4)), y_excited + 10),
                     (255, 200, 100), -1)

        cv2.line(frame, (int(self.width * 0.2), y_ground), (int(self.width * 0.8), y_ground),
                (200, 200, 200), 2)
        cv2.line(frame, (int(self.width * 0.2), y_excited), (int(self.width * 0.8), y_excited),
                (200, 200, 200), 2)
        return frame

    def draw_mode_499_aharonov_bohm(self, frame, magnitudes):
        """Mode 499: Aharonov-Bohm effect phase shift"""
        # Solenoid (enclosed magnetic flux)
        cv2.circle(frame, (self.center_x, self.center_y), 40, (150, 150, 200), -1)

        # Two electron paths (interference)
        # Upper path
        points_up = []
        for i in range(30):
            t = i / 30
            x = int(100 + t * (self.width - 200))
            y = int(self.center_y - 100 * np.sin(t * np.pi))
            points_up.append([x, y])

        points_up = np.array(points_up, dtype=np.int32)
        for i in range(len(points_up) - 1):
            cv2.line(frame, tuple(points_up[i]), tuple(points_up[i + 1]), (200, 200, 255), 2)

        # Lower path
        points_down = []
        for i in range(30):
            t = i / 30
            x = int(100 + t * (self.width - 200))
            y = int(self.center_y + 100 * np.sin(t * np.pi))
            points_down.append([x, y])

        points_down = np.array(points_down, dtype=np.int32)
        for i in range(len(points_down) - 1):
            cv2.line(frame, tuple(points_down[i]), tuple(points_down[i + 1]), (200, 200, 255), 2)

        # Phase difference due to enclosed flux
        bass = self.get_bass(magnitudes)
        cv2.putText(frame, f"Dphi = {bass * 2 * 3.14:.1f}", (self.center_x - 40, self.center_y + 80),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        return frame

    def draw_mode_500_berry_phase(self, frame, magnitudes):
        """Mode 500: Berry phase geometric phase"""
        # Parameter space loop
        num_points = 40

        for i in range(num_points):
            angle = (i / num_points) * 2 * np.pi + self.frame_count * 0.05

            # Cyclic evolution in parameter space
            radius = 100
            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)

            # State vector
            state_angle = 2 * angle  # Berry phase = solid angle
            sx = int(x + np.cos(state_angle) * 20)
            sy = int(y + np.sin(state_angle) * 20)

            cv2.line(frame, (x, y), (sx, sy), (200, 150, 255), 2)
            cv2.circle(frame, (x, y), 4, (255, 200, 200), -1)

        # Path in parameter space
        cv2.circle(frame, (self.center_x, self.center_y), 100, (150, 150, 200), 2)

        return frame

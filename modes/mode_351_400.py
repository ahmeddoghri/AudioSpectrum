"""
Audio Spectrum Visualization Modes 351-400
Nature & Organic Category (Part 2)
"""
from .base import BaseModeVisualizer
import numpy as np
import cv2


class Modes351_400(BaseModeVisualizer):
    """Visualization modes 351 through 400 - Nature & Organic"""

    def __init__(self, visualizer):
        super().__init__(visualizer)

    def draw_mode_351_rainbow_mist(self, frame, magnitudes):
        """Mode 351: Rainbow appearing in mist"""
        # Arc of rainbow
        for i, mag in enumerate(magnitudes):
            angle = np.pi - (i / len(magnitudes)) * np.pi
            radius_base = self.max_radius * 0.7

            for layer in range(7):  # 7 rainbow colors
                radius = int(radius_base + layer * 15)
                x = int(self.center_x + np.cos(angle) * radius)
                y = int(self.height - np.sin(angle) * radius)

                hue = int((layer / 7) * 180)
                color = self.hsv_to_bgr(hue, 200, int(mag * 255))

                cv2.circle(frame, (x, y), 4, color, -1)

        return frame

    def draw_mode_352_geode_crystals(self, frame, magnitudes):
        """Mode 352: Crystal formations inside geode"""
        # Outer geode shell
        cv2.circle(frame, (self.center_x, self.center_y), self.max_radius, (80, 70, 60), 20)

        # Inner crystals
        num_crystals = 24
        for i in range(num_crystals):
            angle = (i / num_crystals) * 2 * np.pi

            mag_idx = i * len(magnitudes) // num_crystals
            mag = magnitudes[mag_idx]

            dist = 50 + mag * 150
            x = int(self.center_x + np.cos(angle) * dist)
            y = int(self.center_y + np.sin(angle) * dist)

            # Crystal spike
            for j in range(int(mag * 20)):
                cx = int(x + np.cos(angle) * j * 3)
                cy = int(y + np.sin(angle) * j * 3)

                hue = (140 + j * 2) % 180
                color = self.hsv_to_bgr(hue, 200, 255)
                cv2.circle(frame, (cx, cy), 3, color, -1)

        return frame

    def draw_mode_353_snake_scales(self, frame, magnitudes):
        """Mode 353: Snake skin scale pattern"""
        scale_size = 20

        for row in range(0, self.height, scale_size):
            for col in range(0, self.width, scale_size):
                idx = ((row // scale_size) * 50 + col // scale_size) % len(magnitudes)
                mag = magnitudes[idx]

                if mag > 0.2:
                    # Scale shape
                    pts = []
                    for i in range(6):
                        angle = (i / 6) * 2 * np.pi
                        px = int(col + np.cos(angle) * scale_size * mag)
                        py = int(row + np.sin(angle) * scale_size * mag * 0.6)
                        pts.append([px, py])

                    pts = np.array(pts, dtype=np.int32)
                    hue = 80 + int(mag * 40)
                    color = self.hsv_to_bgr(hue, 200, 100 + int(mag * 155))
                    cv2.fillPoly(frame, [pts], color)

        return frame

    def draw_mode_354_whirlpool(self, frame, magnitudes):
        """Mode 354: Water spiraling into whirlpool"""
        for i, mag in enumerate(magnitudes):
            angle = (i / len(magnitudes)) * 4 * np.pi + self.frame_count * 0.1
            radius = (i / len(magnitudes)) * self.max_radius

            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)

            size = 2 + int(mag * 8)
            depth = int((1 - i / len(magnitudes)) * 255)
            color = self.hsv_to_bgr(120, 200, depth)

            cv2.circle(frame, (x, y), size, color, -1)

        return frame

    def draw_mode_355_owl_eyes(self, frame, magnitudes):
        """Mode 355: Owl eyes blinking"""
        bass = self.get_bass(magnitudes)

        # Two eyes
        for side in [-1, 1]:
            eye_x = int(self.center_x + side * 100)
            eye_y = self.center_y

            # Outer eye
            cv2.circle(frame, (eye_x, eye_y), 40, (100, 80, 60), -1)

            # Iris
            iris_size = int(20 + bass * 15)
            cv2.circle(frame, (eye_x, eye_y), iris_size, (30, 120, 180), -1)

            # Pupil
            pupil_size = int(10 + bass * 8)
            cv2.circle(frame, (eye_x, eye_y), pupil_size, (0, 0, 0), -1)

            # Highlight
            cv2.circle(frame, (eye_x - 5, eye_y - 5), 5, (255, 255, 255), -1)

        return frame

    def draw_mode_356_tornado_funnel(self, frame, magnitudes):
        """Mode 356: Tornado funnel with debris"""
        energy = self.get_energy(magnitudes)

        # Funnel shape
        for i in range(20):
            y = int((i / 20) * self.height)
            width = int(30 + (i / 20) * 200 * energy)

            for j in range(-width, width, 10):
                x = self.center_x + j + int(np.sin(self.frame_count * 0.2 + i) * 30)

                color = self.hsv_to_bgr(0, 0, 100 + int(energy * 100))
                cv2.circle(frame, (x, y), 5, color, -1)

        # Debris
        for i in range(int(energy * 40)):
            angle = self.frame_count * 0.3 + i
            radius = 50 + (self.frame_count + i * 10) % 300

            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.height - radius * 0.7)

            cv2.circle(frame, (x, y), 3, (80, 60, 40), -1)

        return frame

    def draw_mode_357_peacock_feathers(self, frame, magnitudes):
        """Mode 357: Peacock tail feather display"""
        num_feathers = 12
        for i in range(num_feathers):
            angle = (i / num_feathers) * np.pi - np.pi / 2

            mag_idx = i * len(magnitudes) // num_feathers
            mag = magnitudes[mag_idx]

            # Feather stem
            length = 100 + mag * 200
            x2 = int(self.center_x + np.cos(angle) * length)
            y2 = int(self.height - np.sin(angle) * length)

            cv2.line(frame, (self.center_x, self.height), (x2, y2), (40, 80, 40), 3)

            # Eye of feather
            eye_size = int(15 + mag * 25)
            cv2.circle(frame, (x2, y2), eye_size, (120, 180, 80), -1)
            cv2.circle(frame, (x2, y2), eye_size // 2, (0, 100, 200), -1)
            cv2.circle(frame, (x2, y2), eye_size // 4, (0, 0, 0), -1)

        return frame

    def draw_mode_358_jellyfish_pulse(self, frame, magnitudes):
        """Mode 358: Jellyfish pulsating"""
        bass = self.get_bass(magnitudes)

        # Bell
        pulse = 1.0 + bass * 0.3
        bell_width = int(80 * pulse)
        bell_height = int(60 * pulse)

        cv2.ellipse(frame, (self.center_x, self.center_y - 50),
                   (bell_width, bell_height), 0, 0, 180, (150, 100, 200), -1)

        # Tentacles
        num_tentacles = 8
        for i in range(num_tentacles):
            x_offset = int((i - num_tentacles / 2) * 20)
            x = self.center_x + x_offset

            for j, mag in enumerate(magnitudes[::4]):
                y = self.center_y + int(j * mag * 12)
                wave = int(np.sin(self.frame_count * 0.1 + i + j * 0.3) * mag * 15)

                color = self.hsv_to_bgr(140, 150, 150 + int(mag * 105))
                cv2.circle(frame, (x + wave, y), 3, color, -1)

        return frame

    def draw_mode_359_sand_ripples(self, frame, magnitudes):
        """Mode 359: Ripples in sand from wind"""
        for i in range(30):
            y = int((i / 30) * self.height)

            for j, mag in enumerate(magnitudes):
                x = int((j / len(magnitudes)) * self.width)
                ripple = int(np.sin(x * 0.05 + i * 0.3) * mag * 8)

                color = self.hsv_to_bgr(30, 100 + int(mag * 100), 180 + int(mag * 75))
                cv2.circle(frame, (x, y + ripple), 2, color, -1)

        return frame

    def draw_mode_360_bat_swarm(self, frame, magnitudes):
        """Mode 360: Bats swarming from cave"""
        energy = self.get_energy(magnitudes)

        for i in range(int(energy * 50)):
            phase = self.frame_count * 0.08 + i * 0.2

            x = int(self.center_x + np.sin(phase) * 200)
            y = int(self.center_y + np.cos(phase * 1.3) * 150)

            # Bat silhouette
            wing_span = 12
            cv2.line(frame, (x - wing_span, y), (x, y - 5), (20, 20, 20), 2)
            cv2.line(frame, (x, y - 5), (x + wing_span, y), (20, 20, 20), 2)

        return frame

    def draw_mode_361_tide_motion(self, frame, magnitudes):
        """Mode 361: Tidal motion advancing and retreating"""
        phase = np.sin(self.frame_count * 0.05)
        tide_level = int(self.height * (0.5 + phase * 0.3))

        # Water level
        for i, mag in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * self.width)

            wave = int(np.sin(x * 0.02 + self.frame_count * 0.15) * mag * 30)
            y = tide_level + wave

            # Foam
            if mag > 0.5:
                color = (255, 255, 255)
            else:
                color = self.hsv_to_bgr(120, 150, 150 + int(mag * 105))

            cv2.circle(frame, (x, y), 3 + int(mag * 6), color, -1)

        return frame

    def draw_mode_362_lichen_growth(self, frame, magnitudes):
        """Mode 362: Lichen spreading on rock"""
        # Random lichen colonies
        for i in range(150):
            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            if mag > 0.2:
                center_x = int(np.random.random() * self.width)
                center_y = int(np.random.random() * self.height)

                # Spread from center
                radius = int(5 + mag * 25)

                for j in range(int(mag * 30)):
                    angle = np.random.random() * 2 * np.pi
                    dist = np.random.random() * radius

                    x = int(center_x + np.cos(angle) * dist)
                    y = int(center_y + np.sin(angle) * dist)

                    hue = 50 + int(mag * 40)
                    color = self.hsv_to_bgr(hue, 180, 100 + int(mag * 100))
                    cv2.circle(frame, (x, y), 2, color, -1)

        return frame

    def draw_mode_363_eagle_soar(self, frame, magnitudes):
        """Mode 363: Eagle soaring in thermals"""
        # Thermal spirals
        for i in range(3):
            spiral_x = int(self.width * (0.3 + i * 0.2))
            spiral_y = int(self.height * 0.5)

            mag_idx = i * len(magnitudes) // 3
            mag = magnitudes[mag_idx]

            # Draw thermal current
            for j in range(20):
                angle = (j / 20) * 4 * np.pi + self.frame_count * 0.05
                radius = j * 15 + mag * 30

                x = int(spiral_x + np.cos(angle) * radius)
                y = int(spiral_y + np.sin(angle) * radius - j * 10)

                cv2.circle(frame, (x, y), 2, (200, 220, 240), -1)

        # Eagle
        eagle_angle = self.frame_count * 0.03
        eagle_radius = 150
        eagle_x = int(self.center_x + np.cos(eagle_angle) * eagle_radius)
        eagle_y = int(self.center_y + np.sin(eagle_angle) * eagle_radius)

        # Wings
        wing_size = 25
        cv2.line(frame, (eagle_x - wing_size, eagle_y), (eagle_x + wing_size, eagle_y), (40, 40, 40), 3)

        return frame

    def draw_mode_364_mangrove_roots(self, frame, magnitudes):
        """Mode 364: Mangrove root system"""
        # Multiple root arches
        num_roots = 10
        for i in range(num_roots):
            x_base = int((i / num_roots) * self.width)

            mag_idx = i * len(magnitudes) // num_roots
            mag = magnitudes[mag_idx]

            # Arch shape
            points = []
            for j in range(20):
                t = j / 20
                x = int(x_base + np.sin(t * np.pi) * mag * 50)
                y = int(self.height - t * self.height * 0.6)
                points.append([x, y])

            points = np.array(points, dtype=np.int32)
            color = self.hsv_to_bgr(30, 200, 80 + int(mag * 100))

            for j in range(len(points) - 1):
                cv2.line(frame, tuple(points[j]), tuple(points[j + 1]), color, 4)

        return frame

    def draw_mode_365_aurora_waves(self, frame, magnitudes):
        """Mode 365: Aurora borealis curtain waves"""
        for y in range(0, self.height // 2, 5):
            for i, mag in enumerate(magnitudes):
                x = int((i / len(magnitudes)) * self.width)

                wave1 = np.sin(x * 0.02 + y * 0.05 + self.frame_count * 0.1) * mag * 30
                wave2 = np.sin(x * 0.03 - y * 0.04 + self.frame_count * 0.08) * mag * 20

                y_pos = y + int(wave1 + wave2)

                # Layered colors (green to purple)
                hue = int(80 + y * 0.8 + mag * 40)
                color = self.hsv_to_bgr(hue, 255, int(mag * 255))

                cv2.circle(frame, (x, y_pos), 3, color, -1)

        return frame

    def draw_mode_366_dolphin_leap(self, frame, magnitudes):
        """Mode 366: Dolphins leaping from water"""
        bass = self.get_bass(magnitudes)

        if bass > 0.5:
            # Dolphin arc
            arc_points = []
            for i in range(30):
                t = i / 30
                x = int(self.width * 0.2 + t * self.width * 0.6)
                y = int(self.height * 0.7 - np.sin(t * np.pi) * bass * 200)
                arc_points.append([x, y])

            arc_points = np.array(arc_points, dtype=np.int32)

            for i in range(len(arc_points) - 1):
                cv2.line(frame, tuple(arc_points[i]), tuple(arc_points[i + 1]), (120, 120, 120), 5)

        # Water surface
        for i, mag in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * self.width)
            y = int(self.height * 0.7 + np.sin(x * 0.02 + self.frame_count * 0.1) * 10)

            cv2.circle(frame, (x, y), 2, (180, 140, 100), -1)

        return frame

    def draw_mode_367_tumbleweed_roll(self, frame, magnitudes):
        """Mode 367: Tumbleweed rolling across desert"""
        energy = self.get_energy(magnitudes)

        # Tumbleweed
        weed_x = int((self.frame_count * 3 * energy) % (self.width + 200) - 100)
        weed_y = int(self.height * 0.7)

        rotation = self.frame_count * 5

        # Draw spherical structure
        for i in range(20):
            angle = (i / 20) * 2 * np.pi + np.deg2rad(rotation)
            for j in range(10):
                latitude = (j / 10) * np.pi
                radius = 40 + energy * 20

                x = int(weed_x + np.cos(angle) * np.sin(latitude) * radius)
                y = int(weed_y + np.cos(latitude) * radius)

                cv2.circle(frame, (x, y), 1, (120, 100, 60), -1)

        return frame

    def draw_mode_368_coral_polyps(self, frame, magnitudes):
        """Mode 368: Coral polyps extending tentacles"""
        num_polyps = 20
        for i in range(num_polyps):
            px = int(np.random.random() * self.width)
            py = int(self.height * 0.7 + np.random.random() * self.height * 0.3)

            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            # Polyp body
            cv2.circle(frame, (px, py), 8, (100, 80, 120), -1)

            # Tentacles
            if mag > 0.3:
                for t in range(8):
                    angle = (t / 8) * 2 * np.pi + np.sin(self.frame_count * 0.1) * 0.3
                    length = 15 + mag * 25

                    tx = int(px + np.cos(angle) * length)
                    ty = int(py + np.sin(angle) * length)

                    cv2.line(frame, (px, py), (tx, ty), (120, 100, 140), 2)

        return frame

    def draw_mode_369_smoke_wisps(self, frame, magnitudes):
        """Mode 369: Smoke wisps rising"""
        for i, mag in enumerate(magnitudes):
            if mag > 0.25:
                base_x = int((i / len(magnitudes)) * self.width)

                for j in range(20):
                    y = self.height - j * 15
                    drift = int(np.sin(y * 0.05 + self.frame_count * 0.1) * mag * 30)
                    x = base_x + drift

                    alpha = 255 - j * 12
                    size = 3 + int(mag * 8)

                    color = (alpha // 2, alpha // 2, alpha // 2)
                    cv2.circle(frame, (x, y), size, color, -1)

        return frame

    def draw_mode_370_nautilus_shell(self, frame, magnitudes):
        """Mode 370: Nautilus shell spiral"""
        # Logarithmic spiral
        a = 5
        b = 0.15

        for i, mag in enumerate(magnitudes):
            theta = (i / len(magnitudes)) * 6 * np.pi
            r = a * np.exp(b * theta)

            x = int(self.center_x + r * np.cos(theta) * mag)
            y = int(self.center_y + r * np.sin(theta) * mag)

            size = 2 + int(mag * 8)
            hue = int((theta * 20) % 180)
            color = self.hsv_to_bgr(hue, 200, 200)

            cv2.circle(frame, (x, y), size, color, -1)

        # Chamber walls
        for i in range(8):
            theta = i * np.pi / 4
            r = a * np.exp(b * theta) * 5

            x = int(self.center_x + r * np.cos(theta))
            y = int(self.center_y + r * np.sin(theta))

            cv2.line(frame, (self.center_x, self.center_y), (x, y), (180, 160, 140), 2)

        return frame

    def draw_mode_371_wolf_howl(self, frame, magnitudes):
        """Mode 371: Wolf howling at moon with sound waves"""
        # Moon
        moon_x = int(self.width * 0.8)
        moon_y = int(self.height * 0.2)
        cv2.circle(frame, (moon_x, moon_y), 50, (200, 200, 180), -1)

        # Wolf silhouette
        wolf_x = int(self.width * 0.3)
        wolf_y = int(self.height * 0.7)

        # Simple wolf shape
        cv2.circle(frame, (wolf_x, wolf_y), 30, (40, 40, 40), -1)
        cv2.circle(frame, (wolf_x, wolf_y - 30), 20, (40, 40, 40), -1)

        # Howl sound waves
        bass = self.get_bass(magnitudes)
        if bass > 0.4:
            for i in range(5):
                radius = int(50 + i * 30 + (self.frame_count % 20) * 5)
                alpha = max(0, 200 - i * 40)

                cv2.ellipse(frame, (wolf_x + 20, wolf_y - 40), (radius, radius // 2),
                           45, 0, 180, (alpha, alpha, alpha), 2)

        return frame

    def draw_mode_372_seashell_patterns(self, frame, magnitudes):
        """Mode 372: Various seashell patterns"""
        num_shells = 8
        for i in range(num_shells):
            angle = (i / num_shells) * 2 * np.pi
            dist = 150

            sx = int(self.center_x + np.cos(angle) * dist)
            sy = int(self.center_y + np.sin(angle) * dist)

            mag_idx = i * len(magnitudes) // num_shells
            mag = magnitudes[mag_idx]

            # Spiral pattern
            for j in range(15):
                spiral_angle = (j / 15) * 2 * np.pi
                spiral_r = j * mag * 3

                x = int(sx + np.cos(spiral_angle) * spiral_r)
                y = int(sy + np.sin(spiral_angle) * spiral_r)

                hue = 20 + j * 8
                color = self.hsv_to_bgr(hue, 200, 200)
                cv2.circle(frame, (x, y), 2, color, -1)

        return frame

    def draw_mode_373_grass_blades(self, frame, magnitudes):
        """Mode 373: Individual grass blades swaying"""
        num_blades = 50
        for i in range(num_blades):
            x = int((i / num_blades) * self.width)

            mag_idx = i * len(magnitudes) // num_blades
            mag = magnitudes[mag_idx]

            # Blade curve
            points = []
            for j in range(15):
                t = j / 15
                blade_x = x + int(np.sin(self.frame_count * 0.08 + i + t) * mag * 20)
                blade_y = int(self.height - t * mag * 100)
                points.append([blade_x, blade_y])

            points = np.array(points, dtype=np.int32)
            color = self.hsv_to_bgr(70 + int(mag * 20), 200, 100 + int(mag * 100))

            for j in range(len(points) - 1):
                cv2.line(frame, tuple(points[j]), tuple(points[j + 1]), color, 2)

        return frame

    def draw_mode_374_stalactites(self, frame, magnitudes):
        """Mode 374: Cave stalactites and stalagmites"""
        # Stalactites from ceiling
        num_stalactites = 15
        for i in range(num_stalactites):
            x = int((i / num_stalactites) * self.width)

            mag_idx = i * len(magnitudes) // num_stalactites
            mag = magnitudes[mag_idx]

            length = int(mag * 150)
            width = int(15 + mag * 25)

            # Cone shape
            pts = np.array([
                [x, 0],
                [x - width, 0],
                [x, length],
                [x + width, 0]
            ], dtype=np.int32)

            color = self.hsv_to_bgr(30, 100, 120)
            cv2.fillPoly(frame, [pts], color)

        # Stalagmites from floor
        for i in range(num_stalactites):
            x = int((i / num_stalactites + 0.5 / num_stalactites) * self.width) % self.width

            mag_idx = (i + 5) % len(magnitudes)
            mag = magnitudes[mag_idx]

            length = int(mag * 120)
            width = int(12 + mag * 20)

            pts = np.array([
                [x, self.height],
                [x - width, self.height],
                [x, self.height - length],
                [x + width, self.height]
            ], dtype=np.int32)

            color = self.hsv_to_bgr(30, 100, 100)
            cv2.fillPoly(frame, [pts], color)

        return frame

    def draw_mode_375_amoeba_movement(self, frame, magnitudes):
        """Mode 375: Amoeba-like organic movement"""
        # Blob shape with pseudopods
        num_points = 20
        points = []

        for i in range(num_points):
            angle = (i / num_points) * 2 * np.pi

            mag_idx = i * len(magnitudes) // num_points
            mag = magnitudes[mag_idx]

            radius = 100 + mag * 100 + np.sin(self.frame_count * 0.1 + i) * 40

            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)
            points.append([x, y])

        points = np.array(points, dtype=np.int32)
        color = self.hsv_to_bgr(100, 200, 150)
        cv2.fillPoly(frame, [points], color)

        # Nucleus
        cv2.circle(frame, (self.center_x, self.center_y), 30, (120, 180, 120), -1)

        return frame

    def draw_mode_376_pine_needles(self, frame, magnitudes):
        """Mode 376: Pine needle clusters"""
        num_clusters = 12
        for i in range(num_clusters):
            angle = (i / num_clusters) * 2 * np.pi

            mag_idx = i * len(magnitudes) // num_clusters
            mag = magnitudes[mag_idx]

            dist = 80 + mag * 120
            cx = int(self.center_x + np.cos(angle) * dist)
            cy = int(self.center_y + np.sin(angle) * dist)

            # Needle bundle
            for n in range(8):
                needle_angle = angle + (n - 4) * 0.1
                length = 30 + mag * 40

                nx = int(cx + np.cos(needle_angle) * length)
                ny = int(cy + np.sin(needle_angle) * length)

                color = self.hsv_to_bgr(80, 200, 80 + int(mag * 100))
                cv2.line(frame, (cx, cy), (nx, ny), color, 1)

        return frame

    def draw_mode_377_water_droplet(self, frame, magnitudes):
        """Mode 377: Water droplet impact and splash"""
        bass = self.get_bass(magnitudes)

        # Droplet falling
        if bass > 0.4:
            drop_y = int((self.frame_count % 50) * 10)

            if drop_y < self.height * 0.7:
                cv2.circle(frame, (self.center_x, drop_y), 8, (180, 220, 255), -1)
            else:
                # Splash
                splash_phase = drop_y - self.height * 0.7
                for i in range(12):
                    angle = (i / 12) * 2 * np.pi
                    splash_dist = splash_phase * 2

                    sx = int(self.center_x + np.cos(angle) * splash_dist)
                    sy = int(self.height * 0.7 + np.sin(angle) * splash_dist * 0.5)

                    cv2.circle(frame, (sx, sy), 4, (180, 220, 255), -1)

        # Water surface
        for i, mag in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * self.width)
            y = int(self.height * 0.7)

            cv2.circle(frame, (x, y), 2, (140, 180, 200), -1)

        return frame

    def draw_mode_378_succulent_rosette(self, frame, magnitudes):
        """Mode 378: Succulent plant rosette pattern"""
        # Layers of leaves in spiral
        num_layers = 8
        for layer in range(num_layers):
            leaves_in_layer = 8 + layer * 2
            radius = 30 + layer * 25

            for i in range(leaves_in_layer):
                angle = (i / leaves_in_layer) * 2 * np.pi + layer * 0.3

                mag_idx = (layer * 10 + i) % len(magnitudes)
                mag = magnitudes[mag_idx]

                # Leaf shape (ellipse)
                lx = int(self.center_x + np.cos(angle) * radius)
                ly = int(self.center_y + np.sin(angle) * radius)

                leaf_size = int(15 + mag * 20)
                hue = 80 + layer * 10
                color = self.hsv_to_bgr(hue, 200, 120 + int(mag * 100))

                cv2.ellipse(frame, (lx, ly), (leaf_size, leaf_size // 2),
                           int(np.rad2deg(angle)), 0, 360, color, -1)

        return frame

    def draw_mode_379_salmon_upstream(self, frame, magnitudes):
        """Mode 379: Salmon swimming upstream"""
        energy = self.get_energy(magnitudes)

        # Water flow lines (downstream)
        for i in range(20):
            y = int((i / 20) * self.height)
            flow_x = int((self.frame_count * 5) % self.width)

            cv2.line(frame, (flow_x, y), (flow_x + 30, y), (120, 150, 180), 2)

        # Salmon (swimming upstream)
        num_salmon = int(energy * 8)
        for i in range(num_salmon):
            salmon_x = int(self.width - (self.frame_count * 3 + i * 100) % (self.width + 200))
            salmon_y = int(self.height * 0.5 + np.sin(i) * 100)

            # Fish body
            cv2.ellipse(frame, (salmon_x, salmon_y), (25, 10), 180, 0, 360, (180, 120, 100), -1)

            # Tail
            cv2.circle(frame, (salmon_x + 25, salmon_y), 8, (180, 120, 100), -1)

        return frame

    def draw_mode_380_cloud_formation(self, frame, magnitudes):
        """Mode 380: Clouds forming and dispersing"""
        # Multiple cloud layers
        for layer in range(3):
            y_base = int(self.height * (0.2 + layer * 0.15))

            for i, mag in enumerate(magnitudes[::2]):
                x = int((i / 60) * self.width)

                # Puffy cloud shape
                for j in range(int(mag * 10)):
                    cx = x + int(np.random.random() * 60 - 30)
                    cy = y_base + int(np.random.random() * 30 - 15)

                    size = 10 + int(mag * 20)
                    brightness = 180 + int(mag * 75)

                    cv2.circle(frame, (cx, cy), size, (brightness, brightness, brightness), -1)

        return frame

    def draw_mode_381_fox_tail(self, frame, magnitudes):
        """Mode 381: Fox tail swishing"""
        bass = self.get_bass(magnitudes)

        # Tail base
        base_x = int(self.width * 0.3)
        base_y = int(self.height * 0.7)

        # Tail curve
        points = []
        for i in range(20):
            t = i / 20
            swish = np.sin(self.frame_count * 0.15 + t * 2) * bass * 80

            x = int(base_x + t * 200 + swish)
            y = int(base_y - t * 100)
            points.append([x, y])

        points = np.array(points, dtype=np.int32)

        # Fluffy appearance
        for i in range(len(points) - 1):
            thickness = int(25 - i)
            cv2.line(frame, tuple(points[i]), tuple(points[i + 1]), (200, 140, 80), thickness)

        # White tip
        if len(points) > 0:
            cv2.circle(frame, tuple(points[-1]), 15, (255, 255, 255), -1)

        return frame

    def draw_mode_382_clover_field(self, frame, magnitudes):
        """Mode 382: Field of four-leaf clovers"""
        for i in range(40):
            cx = int(np.random.random() * self.width)
            cy = int(np.random.random() * self.height)

            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            if mag > 0.2:
                # Four leaves
                for leaf in range(4):
                    angle = (leaf / 4) * 2 * np.pi
                    leaf_dist = 10 + mag * 15

                    lx = int(cx + np.cos(angle) * leaf_dist)
                    ly = int(cy + np.sin(angle) * leaf_dist)

                    color = self.hsv_to_bgr(80, 200, 120 + int(mag * 100))
                    cv2.circle(frame, (lx, ly), 6, color, -1)

                # Stem
                cv2.circle(frame, (cx, cy), 3, (60, 100, 40), -1)

        return frame

    def draw_mode_383_geyser_field(self, frame, magnitudes):
        """Mode 383: Multiple geysers erupting"""
        for i, mag in enumerate(magnitudes[::8]):
            if mag > 0.5:
                x = int((i / 15) * self.width)
                height = int(mag * 200)

                # Steam column
                for j in range(int(height / 10)):
                    y = self.height - j * 10
                    spread = j * 3

                    for s in range(-spread, spread, 5):
                        sx = x + s + int(np.random.random() * 10 - 5)
                        brightness = 200 - j * 5

                        cv2.circle(frame, (sx, y), 4, (brightness, brightness, brightness), -1)

        return frame

    def draw_mode_384_insect_compound_eye(self, frame, magnitudes):
        """Mode 384: Compound eye of an insect"""
        # Hexagonal ommatidia
        hex_size = 12
        rows = self.height // (hex_size * 2)
        cols = self.width // (hex_size * 2)

        for row in range(rows):
            for col in range(cols):
                x = col * hex_size * 1.5
                y = row * hex_size * np.sqrt(3)

                if col % 2:
                    y += hex_size * np.sqrt(3) / 2

                # Distance from center for curvature effect
                dist = np.sqrt((x - self.center_x)**2 + (y - self.center_y)**2)

                if dist < self.max_radius:
                    idx = (row * cols + col) % len(magnitudes)
                    mag = magnitudes[idx]

                    # Each facet
                    hue = int((dist / self.max_radius) * 60)
                    brightness = int(100 + mag * 155)
                    color = self.hsv_to_bgr(hue, 200, brightness)

                    cv2.circle(frame, (int(x), int(y)), hex_size // 2, color, -1)

        return frame

    def draw_mode_385_moonflower_bloom(self, frame, magnitudes):
        """Mode 385: Moonflower blooming at night"""
        bass = self.get_bass(magnitudes)

        # Bloom open based on bass
        bloom_factor = bass

        # Petals
        num_petals = 6
        for i in range(num_petals):
            angle = (i / num_petals) * 2 * np.pi

            # Petal shape
            points = []
            for j in range(10):
                t = j / 10
                petal_angle = angle + (t - 0.5) * bloom_factor * 0.8
                petal_dist = 50 + t * 80 * bloom_factor

                x = int(self.center_x + np.cos(petal_angle) * petal_dist)
                y = int(self.center_y + np.sin(petal_angle) * petal_dist)
                points.append([x, y])

            points = np.array(points, dtype=np.int32)
            cv2.fillPoly(frame, [points], (200, 200, 250))

        # Center
        cv2.circle(frame, (self.center_x, self.center_y), 20, (255, 220, 100), -1)

        return frame

    def draw_mode_386_sand_dollar(self, frame, magnitudes):
        """Mode 386: Sand dollar pattern"""
        # Outer circle
        cv2.circle(frame, (self.center_x, self.center_y), self.max_radius // 2, (200, 190, 170), -1)
        cv2.circle(frame, (self.center_x, self.center_y), self.max_radius // 2, (180, 170, 150), 3)

        # Five-petal pattern
        for i in range(5):
            angle = (i / 5) * 2 * np.pi - np.pi / 2

            # Petal slot
            for j, mag in enumerate(magnitudes[::5]):
                dist = 20 + j * mag * 8
                x = int(self.center_x + np.cos(angle) * dist)
                y = int(self.center_y + np.sin(angle) * dist)

                cv2.circle(frame, (x, y), 3, (160, 150, 130), -1)

        return frame

    def draw_mode_387_glacier_crevasse(self, frame, magnitudes):
        """Mode 387: Deep crevasse in glacier"""
        # Ice walls
        for i, mag in enumerate(magnitudes):
            depth = (i / len(magnitudes)) * self.height

            # Left wall
            x1 = int(self.width * 0.3 + np.sin(depth * 0.01) * mag * 40)
            # Right wall
            x2 = int(self.width * 0.7 + np.sin(depth * 0.01 + np.pi) * mag * 40)

            y = int(depth)

            # Ice blue gradient
            brightness = 255 - int(depth / self.height * 100)
            color = self.hsv_to_bgr(120, 100, brightness)

            cv2.line(frame, (x1, y), (x2, y), color, 2)

        return frame

    def draw_mode_388_antler_growth(self, frame, magnitudes):
        """Mode 388: Deer antler branching pattern"""
        # Two antlers
        for side in [-1, 1]:
            base_x = int(self.center_x + side * 50)
            base_y = int(self.height * 0.6)

            def draw_branch(x, y, angle, depth, mag):
                if depth > 5:
                    return

                length = 40 - depth * 5
                rad = np.deg2rad(angle)

                x2 = int(x + np.cos(rad) * length)
                y2 = int(y - np.sin(rad) * length)

                thickness = max(1, 6 - depth)
                cv2.line(frame, (x, y), (x2, y2), (160, 140, 120), thickness)

                # Branch
                if mag > 0.3:
                    draw_branch(x2, y2, angle + 30 * side, depth + 1, mag * 0.8)
                    draw_branch(x2, y2, angle - 15 * side, depth + 1, mag * 0.7)

            bass = self.get_bass(magnitudes)
            draw_branch(base_x, base_y, 80, 0, bass)

        return frame

    def draw_mode_389_plume_worm(self, frame, magnitudes):
        """Mode 389: Feather duster worm plume"""
        # Central stem
        stem_x = self.center_x
        stem_y = self.height - 100

        cv2.line(frame, (stem_x, stem_y), (stem_x, self.height), (100, 80, 60), 8)

        # Radiating plume
        num_filaments = 24
        for i in range(num_filaments):
            angle = (i / num_filaments) * np.pi - np.pi

            mag_idx = i * len(magnitudes) // num_filaments
            mag = magnitudes[mag_idx]

            length = 80 + mag * 100

            # Filament curve
            points = []
            for j in range(15):
                t = j / 15
                dist = t * length
                curve = np.sin(t * np.pi) * 20

                fx = int(stem_x + (np.cos(angle) * dist + np.cos(angle + np.pi/2) * curve))
                fy = int(stem_y - np.sin(angle) * dist)
                points.append([fx, fy])

            points = np.array(points, dtype=np.int32)
            hue = 150 + i * 5
            color = self.hsv_to_bgr(hue, 200, 200)

            for j in range(len(points) - 1):
                cv2.line(frame, tuple(points[j]), tuple(points[j + 1]), color, 2)

        return frame

    def draw_mode_390_reed_marsh(self, frame, magnitudes):
        """Mode 390: Reeds swaying in marsh"""
        num_reeds = 30
        for i in range(num_reeds):
            x = int((i / num_reeds) * self.width)

            mag_idx = i * len(magnitudes) // num_reeds
            mag = magnitudes[mag_idx]

            # Reed height
            height = 150 + mag * 150
            sway = int(np.sin(self.frame_count * 0.08 + i) * mag * 30)

            # Draw reed
            cv2.line(frame, (x, self.height), (x + sway, int(self.height - height)),
                    (80, 120, 60), 3)

            # Seed head
            cv2.ellipse(frame, (x + sway, int(self.height - height)),
                       (8, 15), 0, 0, 360, (120, 100, 60), -1)

        return frame

    def draw_mode_391_beetle_shell(self, frame, magnitudes):
        """Mode 391: Iridescent beetle shell pattern"""
        # Oval shell
        cv2.ellipse(frame, (self.center_x, self.center_y),
                   (self.max_radius // 2, int(self.max_radius * 0.7)),
                   0, 0, 360, (40, 80, 40), -1)

        # Elytra line (wing case split)
        cv2.line(frame, (self.center_x, self.center_y - int(self.max_radius * 0.7)),
                (self.center_x, self.center_y + int(self.max_radius * 0.7)),
                (20, 40, 20), 3)

        # Iridescent spots
        for i, mag in enumerate(magnitudes[::3]):
            angle = (i / 40) * 2 * np.pi
            dist = (i / 40) * self.max_radius * 0.5

            x = int(self.center_x + np.cos(angle) * dist)
            y = int(self.center_y + np.sin(angle) * dist)

            if mag > 0.3:
                hue = (i * 15 + int(self.frame_count)) % 180
                color = self.hsv_to_bgr(hue, 255, int(mag * 255))
                cv2.circle(frame, (x, y), 5, color, -1)

        return frame

    def draw_mode_392_tide_anemone(self, frame, magnitudes):
        """Mode 392: Sea anemone in tidal zone"""
        bass = self.get_bass(magnitudes)

        # Base
        cv2.circle(frame, (self.center_x, self.center_y + 50), 40, (100, 60, 80), -1)

        # Tentacles
        num_tentacles = 20
        for i in range(num_tentacles):
            angle = (i / num_tentacles) * 2 * np.pi

            mag_idx = i * len(magnitudes) // num_tentacles
            mag = magnitudes[mag_idx]

            # Tentacle wave
            points = []
            for j in range(15):
                t = j / 15
                dist = 50 + t * (60 + mag * 80)

                wave = np.sin(self.frame_count * 0.1 + i + t * 3) * bass * 20
                tent_angle = angle + wave * 0.01

                x = int(self.center_x + np.cos(tent_angle) * dist)
                y = int(self.center_y + 50 - np.sin(tent_angle) * dist * 0.3)
                points.append([x, y])

            points = np.array(points, dtype=np.int32)
            hue = 140 + i * 8
            color = self.hsv_to_bgr(hue, 200, 180)

            for j in range(len(points) - 1):
                thickness = max(1, 5 - j // 3)
                cv2.line(frame, tuple(points[j]), tuple(points[j + 1]), color, thickness)

        return frame

    def draw_mode_393_earthquake_waves(self, frame, magnitudes):
        """Mode 393: Seismic waves propagating"""
        bass = self.get_bass(magnitudes)

        # Epicenter
        cv2.circle(frame, (self.center_x, self.center_y), 10, (150, 100, 80), -1)

        # Propagating waves
        for i in range(8):
            phase = (self.frame_count * 2 + i * 15) % 200
            radius = phase * 3

            intensity = max(0, 255 - phase * 2)

            if intensity > 0:
                # P-waves (faster)
                color = self.hsv_to_bgr(0, 200, intensity)
                cv2.circle(frame, (self.center_x, self.center_y), radius, color, 3)

                # S-waves (slower)
                s_radius = int(radius * 0.7)
                cv2.circle(frame, (self.center_x, self.center_y), s_radius, color, 2)

        # Ground displacement
        for i, mag in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * self.width)
            y_base = int(self.height * 0.8)

            displacement = int(np.sin(x * 0.02 + self.frame_count * 0.2) * bass * 30)
            y = y_base + displacement

            cv2.circle(frame, (x, y), 2, (120, 100, 80), -1)

        return frame

    def draw_mode_394_butterfly_lifecycle(self, frame, magnitudes):
        """Mode 394: Butterfly metamorphosis stages"""
        energy = self.get_energy(magnitudes)
        stage = int(energy * 4)

        # Stage 0: Egg
        if stage == 0:
            cv2.ellipse(frame, (self.center_x, self.center_y), (15, 20), 0, 0, 360, (200, 200, 180), -1)

        # Stage 1: Caterpillar
        elif stage == 1:
            for i in range(8):
                x = int(self.center_x - 80 + i * 20)
                y = self.center_y
                cv2.circle(frame, (x, y), 12, (80, 180, 80), -1)

        # Stage 2: Chrysalis
        elif stage == 2:
            cv2.ellipse(frame, (self.center_x, self.center_y), (25, 50), 0, 0, 360, (120, 180, 140), -1)

        # Stage 3: Butterfly
        else:
            wing_size = 50
            for side in [-1, 1]:
                # Upper wing
                cv2.ellipse(frame, (self.center_x + side * 30, self.center_y - 20),
                           (wing_size, wing_size), 0, 0, 360, (255, 150, 100), -1)
                # Lower wing
                cv2.ellipse(frame, (self.center_x + side * 30, self.center_y + 20),
                           (wing_size // 2, wing_size // 2), 0, 0, 360, (200, 100, 150), -1)

            # Body
            cv2.ellipse(frame, (self.center_x, self.center_y), (8, 40), 0, 0, 360, (40, 40, 40), -1)

        return frame

    def draw_mode_395_coconut_palm(self, frame, magnitudes):
        """Mode 395: Palm tree with coconuts"""
        # Trunk
        trunk_points = []
        for i in range(20):
            t = i / 20
            x = int(self.center_x + np.sin(i * 0.3) * 15)
            y = int(self.height - t * self.height * 0.7)
            trunk_points.append([x, y])

        trunk_points = np.array(trunk_points, dtype=np.int32)
        for i in range(len(trunk_points) - 1):
            cv2.line(frame, tuple(trunk_points[i]), tuple(trunk_points[i + 1]), (100, 80, 60), 20)

        # Fronds
        top_x, top_y = trunk_points[-1]
        num_fronds = 8

        for i in range(num_fronds):
            angle = (i / num_fronds) * 2 * np.pi

            mag_idx = i * len(magnitudes) // num_fronds
            mag = magnitudes[mag_idx]

            # Frond curve
            points = []
            for j in range(15):
                t = j / 15
                dist = t * (100 + mag * 80)
                curve = np.sin(t * np.pi) * 20

                fx = int(top_x + (np.cos(angle) * dist + np.cos(angle + np.pi/2) * curve))
                fy = int(top_y - np.sin(angle) * dist)
                points.append([fx, fy])

            points = np.array(points, dtype=np.int32)
            color = self.hsv_to_bgr(70, 200, 100)

            for j in range(len(points) - 1):
                cv2.line(frame, tuple(points[j]), tuple(points[j + 1]), color, 3)

        # Coconuts
        for i in range(4):
            angle = (i / 4) * 2 * np.pi
            cx = int(top_x + np.cos(angle) * 25)
            cy = int(top_y + np.sin(angle) * 25)

            cv2.circle(frame, (cx, cy), 12, (80, 60, 40), -1)

        return frame

    def draw_mode_396_frost_ferns(self, frame, magnitudes):
        """Mode 396: Frost fern patterns on window"""
        # Recursive fern pattern
        def draw_fern(x, y, angle, depth, mag):
            if depth > 6:
                return

            length = 30 - depth * 3
            rad = np.deg2rad(angle)

            x2 = int(x + np.cos(rad) * length)
            y2 = int(y + np.sin(rad) * length)

            cv2.line(frame, (x, y), (x2, y2), (200, 230, 255), 1)

            # Side branches
            if mag > 0.2:
                draw_fern(x2, y2, angle + 45, depth + 1, mag * 0.7)
                draw_fern(x2, y2, angle - 45, depth + 1, mag * 0.7)

        # Multiple fern starts
        for i in range(6):
            start_x = int((i / 6) * self.width)
            start_y = int(np.random.random() * self.height)

            mag_idx = i * len(magnitudes) // 6
            mag = magnitudes[mag_idx]

            if mag > 0.3:
                draw_fern(start_x, start_y, int(np.random.random() * 360), 0, mag)

        return frame

    def draw_mode_397_bioluminescent_bay(self, frame, magnitudes):
        """Mode 397: Bioluminescent organisms in bay"""
        for i, mag in enumerate(magnitudes):
            if mag > 0.25:
                x = int((i / len(magnitudes)) * self.width)
                y = int(self.height * 0.5 + np.sin(self.frame_count * 0.05 + i) * self.height * 0.3)

                # Glow effect
                glow_size = int(5 + mag * 15)
                intensity = int(mag * 255)

                # Outer glow
                cv2.circle(frame, (x, y), glow_size, (0, intensity // 3, intensity // 2), -1)
                # Inner bright
                cv2.circle(frame, (x, y), glow_size // 2, (0, intensity, intensity), -1)

        return frame

    def draw_mode_398_erosion_patterns(self, frame, magnitudes):
        """Mode 398: Water erosion creating patterns"""
        # Erosion channels
        num_channels = 8
        for i in range(num_channels):
            x = int((i / num_channels) * self.width)

            mag_idx = i * len(magnitudes) // num_channels
            mag = magnitudes[mag_idx]

            # Channel path
            points = []
            for j in range(30):
                t = j / 30
                y = int(t * self.height)

                meander = int(np.sin(j * 0.5) * mag * 50)
                cx = x + meander

                points.append([cx, y])

            points = np.array(points, dtype=np.int32)
            color = self.hsv_to_bgr(30, 150, 120)

            for j in range(len(points) - 1):
                thickness = max(1, int(mag * 8))
                cv2.line(frame, tuple(points[j]), tuple(points[j + 1]), color, thickness)

        return frame

    def draw_mode_399_hedge_maze(self, frame, magnitudes):
        """Mode 399: Hedge maze from above"""
        cell_size = 40

        for row in range(0, self.height, cell_size):
            for col in range(0, self.width, cell_size):
                idx = ((row // cell_size) * 20 + col // cell_size) % len(magnitudes)
                mag = magnitudes[idx]

                # Hedge walls based on magnitude
                if mag > 0.6:
                    # Vertical wall
                    cv2.rectangle(frame, (col, row), (col + 5, row + cell_size),
                                (40, 80, 40), -1)
                elif mag > 0.3:
                    # Horizontal wall
                    cv2.rectangle(frame, (col, row), (col + cell_size, row + 5),
                                (40, 80, 40), -1)

        return frame

    def draw_mode_400_water_lily_reflection(self, frame, magnitudes):
        """Mode 400: Water lily with mirror reflection"""
        # Water line
        water_y = self.height // 2

        # Lily (top half)
        num_petals = 8
        for i in range(num_petals):
            angle = (i / num_petals) * 2 * np.pi

            mag_idx = i * len(magnitudes) // num_petals
            mag = magnitudes[mag_idx]

            dist = 40 + mag * 50
            x = int(self.center_x + np.cos(angle) * dist)
            y = int(water_y - 50 + np.sin(angle) * dist * 0.5)

            # Petal
            size = 20 + int(mag * 25)
            color = self.hsv_to_bgr(160, 150, 255)
            cv2.ellipse(frame, (x, y), (size, size // 2),
                       int(np.rad2deg(angle)), 0, 360, color, -1)

            # Reflection (bottom half)
            y_reflect = water_y + (water_y - y)
            color_reflect = self.hsv_to_bgr(160, 150, 180)  # Darker
            cv2.ellipse(frame, (x, y_reflect), (size, size // 2),
                       int(np.rad2deg(angle)), 0, 360, color_reflect, -1)

        # Center
        cv2.circle(frame, (self.center_x, water_y - 50), 15, (255, 220, 100), -1)
        cv2.circle(frame, (self.center_x, water_y + 50), 15, (180, 160, 80), -1)

        # Water ripples
        for i in range(5):
            radius = 100 + i * 30
            cv2.ellipse(frame, (self.center_x, water_y), (radius, 10),
                       0, 0, 360, (120, 150, 180), 1)

        return frame

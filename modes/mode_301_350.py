"""
Audio Spectrum Visualization Modes 301-350
Nature & Organic Category (Part 1)
"""
from .base import BaseModeVisualizer
import numpy as np
import cv2


class Modes301_350(BaseModeVisualizer):
    """Visualization modes 301 through 350 - Nature & Organic"""

    def __init__(self, visualizer):
        super().__init__(visualizer)

    def draw_mode_301_forest_canopy(self, frame, magnitudes):
        """Mode 301: Tree canopy with swaying branches"""
        bass = self.get_bass(magnitudes)

        # Draw multiple tree branches from bottom
        num_trees = 12
        for i in range(num_trees):
            x = int((i / num_trees) * self.width)
            sway = int(np.sin(self.frame_count * 0.05 + i) * bass * 20)

            for j, mag in enumerate(magnitudes[::3]):
                y = self.height - int((j / 40) * self.height)
                branch_x = x + sway + int(mag * 30 * np.cos(j))
                color = self.hsv_to_bgr(30 + mag * 30, 200, 100 + int(mag * 155))
                cv2.circle(frame, (branch_x, y), 3 + int(mag * 8), color, -1)

        return frame

    def draw_mode_302_ocean_waves(self, frame, magnitudes):
        """Mode 302: Flowing ocean waves with foam"""
        # Multiple wave layers
        for layer in range(5):
            y_offset = int((layer / 5) * self.height)
            for i, mag in enumerate(magnitudes):
                x = int((i / len(magnitudes)) * self.width)
                wave = np.sin(x * 0.02 + self.frame_count * 0.1 + layer) * mag * 30
                y = y_offset + int(wave)

                color = self.hsv_to_bgr(100 + layer * 10, 150 - layer * 20, 150 + int(mag * 105))
                cv2.circle(frame, (x, y), 2 + int(mag * 6), color, -1)

        return frame

    def draw_mode_303_coral_reef(self, frame, magnitudes):
        """Mode 303: Coral formations with flowing tentacles"""
        num_corals = 15
        for i in range(num_corals):
            base_x = int((i / num_corals) * self.width)
            base_y = self.height - 50

            # Each coral sways
            for j in range(30):
                mag_idx = (i * 8 + j) % len(magnitudes)
                mag = magnitudes[mag_idx]

                sway = np.sin(self.frame_count * 0.08 + i + j * 0.1) * mag * 15
                x = int(base_x + sway)
                y = int(base_y - j * mag * 10)

                hue = (160 + i * 15) % 180
                color = self.hsv_to_bgr(hue, 200, 100 + int(mag * 155))
                cv2.circle(frame, (x, y), 2 + int(mag * 5), color, -1)

        return frame

    def draw_mode_304_butterfly_swarm(self, frame, magnitudes):
        """Mode 304: Butterflies dancing to music"""
        energy = self.get_energy(magnitudes)

        for i, mag in enumerate(magnitudes[::2]):
            if mag > 0.2:
                angle = self.frame_count * 0.1 + i * 0.5
                radius = 100 + mag * 200
                x = int(self.center_x + np.cos(angle) * radius)
                y = int(self.center_y + np.sin(angle) * radius)

                # Wing flutter
                wing_size = 5 + int(mag * 15)
                hue = (i * 7) % 180
                color = self.hsv_to_bgr(hue, 255, 200)

                cv2.ellipse(frame, (x, y), (wing_size, wing_size // 2),
                           int(angle * 10), 0, 360, color, -1)

        return frame

    def draw_mode_305_mountain_peaks(self, frame, magnitudes):
        """Mode 305: Mountain ranges responding to frequencies"""
        # Create mountain silhouette
        points = []
        for i, mag in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * self.width)
            y = int(self.height - mag * self.height * 0.7)
            points.append([x, y])

        points.append([self.width, self.height])
        points.append([0, self.height])
        points = np.array(points, dtype=np.int32)

        energy = self.get_energy(magnitudes)
        color = self.hsv_to_bgr(120, 100, 80 + int(energy * 120))
        cv2.fillPoly(frame, [points], color)

        # Snow caps on peaks
        for i, mag in enumerate(magnitudes):
            if mag > 0.6:
                x = int((i / len(magnitudes)) * self.width)
                y = int(self.height - mag * self.height * 0.7)
                cv2.circle(frame, (x, y), 8, (255, 255, 255), -1)

        return frame

    def draw_mode_306_fireflies(self, frame, magnitudes):
        """Mode 306: Fireflies glowing and flickering"""
        for i, mag in enumerate(magnitudes):
            if mag > 0.25:
                x = int(np.random.random() * self.width)
                y = int(np.random.random() * self.height)

                # Pulsing glow
                glow = int(mag * 255)
                size = 2 + int(mag * 8)

                cv2.circle(frame, (x, y), size + 4, (0, glow // 3, glow // 3), -1)
                cv2.circle(frame, (x, y), size, (0, glow, glow), -1)

        return frame

    def draw_mode_307_flower_bloom(self, frame, magnitudes):
        """Mode 307: Flowers blooming radially"""
        num_flowers = 8
        for f in range(num_flowers):
            angle_offset = (f / num_flowers) * 2 * np.pi
            flower_radius = 100 + f * 30

            for i, mag in enumerate(magnitudes[::4]):
                angle = angle_offset + (i / 30) * 2 * np.pi
                radius = flower_radius + mag * 50

                x = int(self.center_x + np.cos(angle) * radius)
                y = int(self.center_y + np.sin(angle) * radius)

                hue = (f * 25 + i * 5) % 180
                color = self.hsv_to_bgr(hue, 255, 200)
                cv2.circle(frame, (x, y), 3 + int(mag * 10), color, -1)

        return frame

    def draw_mode_308_rain_ripples(self, frame, magnitudes):
        """Mode 308: Rain creating ripples on water surface"""
        bass = self.get_bass(magnitudes)

        # Draw expanding ripples
        for i, mag in enumerate(magnitudes):
            if mag > 0.3:
                x = int((i / len(magnitudes)) * self.width)
                y = int(self.height * 0.3 + np.random.random() * self.height * 0.4)

                ripple_phase = (self.frame_count + i) % 50
                radius = int(ripple_phase * mag * 3)
                alpha = 255 - int(ripple_phase * 5)

                color = self.hsv_to_bgr(120, 150, alpha)
                cv2.circle(frame, (x, y), radius, color, 2)

        return frame

    def draw_mode_309_leaf_fall(self, frame, magnitudes):
        """Mode 309: Autumn leaves falling"""
        energy = self.get_energy(magnitudes)

        for i in range(int(energy * 50)):
            x = int(np.random.random() * self.width)
            y = int((self.frame_count * 2 + i * 10) % self.height)

            sway = int(np.sin(y * 0.1 + i) * 20)
            x = (x + sway) % self.width

            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            hue = 10 + int(mag * 30)  # Orange to red
            color = self.hsv_to_bgr(hue, 255, 200)

            # Leaf shape
            cv2.ellipse(frame, (x, y), (5, 8), int(self.frame_count + i), 0, 360, color, -1)

        return frame

    def draw_mode_310_tree_rings(self, frame, magnitudes):
        """Mode 310: Growth rings of a tree"""
        for i, mag in enumerate(magnitudes):
            radius = int((i / len(magnitudes)) * self.max_radius)
            thickness = max(1, int(mag * 8))

            hue = 20 + i % 40
            color = self.hsv_to_bgr(hue, 180, 120 + int(mag * 135))

            cv2.circle(frame, (self.center_x, self.center_y), radius, color, thickness)

        return frame

    def draw_mode_311_lightning_storm(self, frame, magnitudes):
        """Mode 311: Lightning bolts during storm"""
        highs = self.get_highs(magnitudes)

        if highs > 0.6:
            # Random lightning bolt
            x1 = int(np.random.random() * self.width)
            y1 = 0

            for _ in range(10):
                x2 = x1 + int(np.random.random() * 40 - 20)
                y2 = y1 + int(np.random.random() * 60 + 40)

                cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 200), 2)
                x1, y1 = x2, y2

                if y1 > self.height:
                    break

        return frame

    def draw_mode_312_pond_koi(self, frame, magnitudes):
        """Mode 312: Koi fish swimming in pond"""
        num_koi = 8
        for i in range(num_koi):
            angle = self.frame_count * 0.02 + i * 0.8
            radius = 100 + np.sin(self.frame_count * 0.05 + i) * 50

            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)

            mag_idx = i * len(magnitudes) // num_koi
            mag = magnitudes[mag_idx]

            # Fish body
            size = 15 + int(mag * 20)
            hue = (i * 40) % 180
            color = self.hsv_to_bgr(hue, 200, 255)

            cv2.ellipse(frame, (x, y), (size, size // 2), int(angle * 57), 0, 360, color, -1)

        return frame

    def draw_mode_313_moss_growth(self, frame, magnitudes):
        """Mode 313: Moss spreading organically"""
        for i in range(100):
            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            if mag > 0.2:
                x = int((np.random.random() * 0.8 + 0.1) * self.width)
                y = int((np.random.random() * 0.8 + 0.1) * self.height)

                spread = int(mag * 15)
                hue = 70 + int(mag * 20)
                color = self.hsv_to_bgr(hue, 200, 100 + int(mag * 100))

                cv2.circle(frame, (x, y), spread, color, -1)

        return frame

    def draw_mode_314_aurora_forest(self, frame, magnitudes):
        """Mode 314: Northern lights over forest"""
        # Aurora waves
        for y in range(0, self.height // 2, 10):
            for i, mag in enumerate(magnitudes):
                x = int((i / len(magnitudes)) * self.width)
                wave = np.sin(x * 0.02 + y * 0.05 + self.frame_count * 0.1) * mag * 20

                y_pos = y + int(wave)
                hue = (90 + y // 5) % 180
                color = self.hsv_to_bgr(hue, 200, int(mag * 255))

                cv2.circle(frame, (x, y_pos), 3, color, -1)

        # Forest silhouette
        for i in range(20):
            x = int((i / 20) * self.width)
            height = int(self.height * (0.3 + np.random.random() * 0.2))
            cv2.rectangle(frame, (x, self.height - height), (x + 30, self.height), (20, 20, 20), -1)

        return frame

    def draw_mode_315_dandelion_seeds(self, frame, magnitudes):
        """Mode 315: Dandelion seeds floating in wind"""
        energy = self.get_energy(magnitudes)

        for i in range(int(energy * 60)):
            x = int((self.frame_count * 1.5 + i * 20) % (self.width + 100) - 50)
            y = int(self.height * 0.3 + np.sin(x * 0.05 + i) * self.height * 0.3)

            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            # Draw seed with stem
            color = (200, 200, 200)
            cv2.circle(frame, (x, y), 2, color, -1)
            cv2.line(frame, (x, y), (x, y + 8), color, 1)

            # Fluffy top
            for j in range(6):
                angle = (j / 6) * 2 * np.pi
                fx = int(x + np.cos(angle) * 5)
                fy = int(y + np.sin(angle) * 5)
                cv2.line(frame, (x, y), (fx, fy), (220, 220, 220), 1)

        return frame

    def draw_mode_316_fern_fractals(self, frame, magnitudes):
        """Mode 316: Fractal fern patterns"""
        bass = self.get_bass(magnitudes)

        # Draw fern from bottom center
        x, y = self.center_x, self.height - 50
        angle = -90

        for i, mag in enumerate(magnitudes[::3]):
            length = 20 + mag * 40
            rad = np.deg2rad(angle)

            x2 = int(x + np.cos(rad) * length)
            y2 = int(y + np.sin(rad) * length)

            color = self.hsv_to_bgr(80 + int(mag * 40), 200, 150)
            cv2.line(frame, (int(x), int(y)), (x2, y2), color, 2)

            # Side branches
            for side in [-45, 45]:
                branch_angle = angle + side
                branch_rad = np.deg2rad(branch_angle)
                bx = int(x + np.cos(branch_rad) * length * 0.6)
                by = int(y + np.sin(branch_rad) * length * 0.6)
                cv2.line(frame, (int(x), int(y)), (bx, by), color, 1)

            x, y = x2, y2
            angle += np.sin(i) * mag * 20

        return frame

    def draw_mode_317_beehive_cells(self, frame, magnitudes):
        """Mode 317: Hexagonal honeycomb pattern"""
        hex_size = 30

        for row in range(-2, self.height // hex_size + 2):
            for col in range(-2, self.width // hex_size + 2):
                x = col * hex_size * 1.5
                y = row * hex_size * np.sqrt(3)

                if col % 2:
                    y += hex_size * np.sqrt(3) / 2

                # Map to magnitude
                idx = (row * 10 + col) % len(magnitudes)
                mag = magnitudes[idx]

                if mag > 0.2:
                    hue = 30 + int(mag * 30)
                    color = self.hsv_to_bgr(hue, 200, 100 + int(mag * 155))

                    # Draw hexagon
                    pts = []
                    for i in range(6):
                        angle = i * np.pi / 3
                        px = int(x + hex_size * np.cos(angle))
                        py = int(y + hex_size * np.sin(angle))
                        pts.append([px, py])

                    pts = np.array(pts, dtype=np.int32)
                    cv2.fillPoly(frame, [pts], color)

        return frame

    def draw_mode_318_wheat_field(self, frame, magnitudes):
        """Mode 318: Wheat swaying in wind"""
        for i in range(40):
            x = int((i / 40) * self.width)

            for j, mag in enumerate(magnitudes[::4]):
                y = self.height - int(j * mag * 15)
                sway = int(np.sin(self.frame_count * 0.1 + i * 0.5 + j) * 10)

                color = self.hsv_to_bgr(30 + int(mag * 20), 200, 150 + int(mag * 105))
                cv2.line(frame, (x + sway, self.height), (x + sway, y), color, 2)

        return frame

    def draw_mode_319_spider_web(self, frame, magnitudes):
        """Mode 319: Spider web with dew drops"""
        # Radial threads
        for i in range(12):
            angle = (i / 12) * 2 * np.pi
            x2 = int(self.center_x + np.cos(angle) * self.max_radius)
            y2 = int(self.center_y + np.sin(angle) * self.max_radius)
            cv2.line(frame, (self.center_x, self.center_y), (x2, y2), (200, 200, 200), 1)

        # Circular threads with dew
        for i, mag in enumerate(magnitudes[::3]):
            radius = int((i / 40) * self.max_radius)
            cv2.circle(frame, (self.center_x, self.center_y), radius, (180, 180, 180), 1)

            # Dew drops
            if mag > 0.4:
                angle = (i / 40) * 2 * np.pi
                x = int(self.center_x + np.cos(angle) * radius)
                y = int(self.center_y + np.sin(angle) * radius)

                size = 3 + int(mag * 8)
                cv2.circle(frame, (x, y), size, (180, 220, 255), -1)

        return frame

    def draw_mode_320_mushroom_spores(self, frame, magnitudes):
        """Mode 320: Mushroom spores floating"""
        energy = self.get_energy(magnitudes)

        for i in range(int(energy * 80)):
            x = int(np.random.random() * self.width)
            y = int((self.frame_count + i * 5) % self.height)

            drift = int(np.sin(y * 0.1 + i) * 30)
            x = (x + drift) % self.width

            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            size = 1 + int(mag * 4)
            hue = 20 + int(mag * 40)
            color = self.hsv_to_bgr(hue, 150, 200)

            cv2.circle(frame, (x, y), size, color, -1)

        return frame

    def draw_mode_321_bamboo_forest(self, frame, magnitudes):
        """Mode 321: Bamboo stalks swaying"""
        num_stalks = 15
        for i in range(num_stalks):
            x = int((i / num_stalks) * self.width)
            sway = int(np.sin(self.frame_count * 0.05 + i) * 15)

            mag_idx = i * len(magnitudes) // num_stalks
            mag = magnitudes[mag_idx]

            # Draw bamboo segments
            for j in range(8):
                y1 = self.height - j * 80
                y2 = y1 - 70

                color = self.hsv_to_bgr(70 + int(mag * 20), 200, 100 + int(mag * 100))
                cv2.line(frame, (x + sway, y1), (x + sway, y2), color, 6)

                # Segment joint
                cv2.circle(frame, (x + sway, y1), 8, (50, 80, 40), -1)

        return frame

    def draw_mode_322_tide_pools(self, frame, magnitudes):
        """Mode 322: Tide pools with sea life"""
        # Create pool circles
        num_pools = 6
        for i in range(num_pools):
            angle = (i / num_pools) * 2 * np.pi
            dist = self.max_radius * 0.5

            px = int(self.center_x + np.cos(angle) * dist)
            py = int(self.center_y + np.sin(angle) * dist)

            # Pool outline
            cv2.circle(frame, (px, py), 80, (100, 120, 60), 3)

            # Creatures in pool
            for j, mag in enumerate(magnitudes[i*10:(i+1)*10]):
                creature_angle = (j / 10) * 2 * np.pi + self.frame_count * 0.05
                cx = int(px + np.cos(creature_angle) * mag * 40)
                cy = int(py + np.sin(creature_angle) * mag * 40)

                color = self.hsv_to_bgr(120 + j * 10, 200, 200)
                cv2.circle(frame, (cx, cy), 3 + int(mag * 6), color, -1)

        return frame

    def draw_mode_323_vine_tendrils(self, frame, magnitudes):
        """Mode 323: Growing vine tendrils"""
        num_vines = 8
        for v in range(num_vines):
            x = int((v / num_vines) * self.width)
            y = self.height

            for i, mag in enumerate(magnitudes[::4]):
                curl = np.sin(i * 0.3 + self.frame_count * 0.05) * mag * 20
                x += int(curl)
                y -= int(mag * 15)

                if y < 0:
                    break

                color = self.hsv_to_bgr(80 + int(mag * 30), 200, 120 + int(mag * 135))
                cv2.circle(frame, (x, y), 2 + int(mag * 5), color, -1)

        return frame

    def draw_mode_324_crystal_cave(self, frame, magnitudes):
        """Mode 324: Crystalline cave formations"""
        num_crystals = 12
        for i in range(num_crystals):
            angle = (i / num_crystals) * 2 * np.pi
            base_dist = 100 + i * 20

            mag_idx = i * len(magnitudes) // num_crystals
            mag = magnitudes[mag_idx]

            dist = base_dist + mag * 80
            x = int(self.center_x + np.cos(angle) * dist)
            y = int(self.center_y + np.sin(angle) * dist)

            # Crystal shape (triangle)
            size = 15 + int(mag * 25)
            pts = np.array([
                [x, y - size],
                [x - size // 2, y + size // 2],
                [x + size // 2, y + size // 2]
            ], dtype=np.int32)

            hue = (140 + i * 15) % 180
            color = self.hsv_to_bgr(hue, 200, 200)
            cv2.fillPoly(frame, [pts], color)

        return frame

    def draw_mode_325_bird_murmuration(self, frame, magnitudes):
        """Mode 325: Flock of birds in murmuration"""
        energy = self.get_energy(magnitudes)
        num_birds = int(energy * 100)

        for i in range(num_birds):
            phase = self.frame_count * 0.05 + i * 0.1

            x = int(self.center_x + np.sin(phase) * 200 * np.cos(i))
            y = int(self.center_y + np.cos(phase) * 200 * np.sin(i))

            # Bird shape (simple V)
            size = 5
            color = (40, 40, 40)
            cv2.line(frame, (x - size, y), (x, y - size), color, 2)
            cv2.line(frame, (x, y - size), (x + size, y), color, 2)

        return frame

    def draw_mode_326_river_flow(self, frame, magnitudes):
        """Mode 326: River flowing with currents"""
        # Multiple flow lines
        for layer in range(8):
            y = int((layer / 8) * self.height)

            for i, mag in enumerate(magnitudes):
                x = int((i / len(magnitudes)) * self.width)
                flow = np.sin(x * 0.03 + self.frame_count * 0.1 + layer) * mag * 15

                y_pos = y + int(flow)
                color = self.hsv_to_bgr(110, 200 - layer * 20, 150 + int(mag * 105))

                cv2.circle(frame, (x, y_pos), 2 + int(mag * 4), color, -1)

        return frame

    def draw_mode_327_seed_pods(self, frame, magnitudes):
        """Mode 327: Seed pods bursting open"""
        num_pods = 10
        for i in range(num_pods):
            angle = (i / num_pods) * 2 * np.pi

            mag_idx = i * len(magnitudes) // num_pods
            mag = magnitudes[mag_idx]

            dist = 150 + mag * 100
            px = int(self.center_x + np.cos(angle) * dist)
            py = int(self.center_y + np.sin(angle) * dist)

            # Pod center
            cv2.circle(frame, (px, py), 10, (100, 80, 40), -1)

            # Seeds bursting out
            if mag > 0.4:
                for j in range(12):
                    seed_angle = (j / 12) * 2 * np.pi
                    sx = int(px + np.cos(seed_angle) * mag * 30)
                    sy = int(py + np.sin(seed_angle) * mag * 30)

                    cv2.circle(frame, (sx, sy), 3, (120, 100, 60), -1)

        return frame

    def draw_mode_328_algae_bloom(self, frame, magnitudes):
        """Mode 328: Algae blooming in water"""
        for i in range(150):
            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            if mag > 0.15:
                x = int(np.random.random() * self.width)
                y = int(np.random.random() * self.height)

                # Organic blob shape
                radius = 5 + int(mag * 15)
                hue = 70 + int(mag * 30)
                color = self.hsv_to_bgr(hue, 255, 120 + int(mag * 100))

                cv2.circle(frame, (x, y), radius, color, -1)

        return frame

    def draw_mode_329_cactus_spines(self, frame, magnitudes):
        """Mode 329: Cactus with radiating spines"""
        # Draw cactus body
        for i, mag in enumerate(magnitudes[::3]):
            y = int(self.height - (i / 40) * self.height * 0.8)
            width = 60 + int(mag * 40)

            color = self.hsv_to_bgr(80, 200, 80 + int(mag * 80))
            cv2.ellipse(frame, (self.center_x, y), (width, 30), 0, 0, 360, color, -1)

            # Spines
            for j in range(8):
                angle = (j / 8) * 2 * np.pi
                sx = int(self.center_x + width + np.cos(angle) * mag * 20)
                sy = int(y + np.sin(angle) * mag * 20)

                cv2.line(frame, (self.center_x, y), (sx, sy), (200, 200, 150), 1)

        return frame

    def draw_mode_330_snowflakes(self, frame, magnitudes):
        """Mode 330: Unique snowflakes falling"""
        energy = self.get_energy(magnitudes)

        for i in range(int(energy * 50)):
            x = int(np.random.random() * self.width)
            y = int((self.frame_count * 1.5 + i * 15) % self.height)

            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            size = 3 + int(mag * 10)

            # 6-fold symmetry
            for j in range(6):
                angle = (j / 6) * 2 * np.pi
                x2 = int(x + np.cos(angle) * size)
                y2 = int(y + np.sin(angle) * size)

                cv2.line(frame, (x, y), (x2, y2), (255, 255, 255), 1)

        return frame

    def draw_mode_331_lava_flow(self, frame, magnitudes):
        """Mode 331: Molten lava flowing"""
        for layer in range(6):
            y_offset = int(self.height * 0.3 + layer * 60)

            for i, mag in enumerate(magnitudes):
                x = int((i / len(magnitudes)) * self.width)
                flow = np.sin(x * 0.02 + self.frame_count * 0.15 - layer * 0.5) * mag * 25

                y = y_offset + int(flow)

                # Hot to cool gradient
                temp = 1.0 - (layer / 6)
                hue = int(temp * 20)
                color = self.hsv_to_bgr(hue, 255, int(150 + mag * 105))

                cv2.circle(frame, (x, y), 4 + int(mag * 8), color, -1)

        return frame

    def draw_mode_332_ice_crystals(self, frame, magnitudes):
        """Mode 332: Ice crystal formations"""
        num_crystals = 15
        for i in range(num_crystals):
            angle = (i / num_crystals) * 2 * np.pi + self.frame_count * 0.02

            mag_idx = i * len(magnitudes) // num_crystals
            mag = magnitudes[mag_idx]

            dist = 80 + mag * 150
            x = int(self.center_x + np.cos(angle) * dist)
            y = int(self.center_y + np.sin(angle) * dist)

            # Crystal branches
            for branch in range(6):
                branch_angle = angle + (branch / 6) * 2 * np.pi
                bx = int(x + np.cos(branch_angle) * mag * 40)
                by = int(y + np.sin(branch_angle) * mag * 40)

                cv2.line(frame, (x, y), (bx, by), (200, 240, 255), 2)

        return frame

    def draw_mode_333_pine_cones(self, frame, magnitudes):
        """Mode 333: Pine cone spiral patterns"""
        # Fibonacci spiral
        golden_angle = 137.5

        for i, mag in enumerate(magnitudes):
            angle = np.deg2rad(i * golden_angle)
            radius = np.sqrt(i) * 15

            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)

            size = 3 + int(mag * 8)
            hue = 20 + int(mag * 30)
            color = self.hsv_to_bgr(hue, 200, 120 + int(mag * 135))

            cv2.circle(frame, (x, y), size, color, -1)

        return frame

    def draw_mode_334_geyser_eruption(self, frame, magnitudes):
        """Mode 334: Geyser water erupting"""
        bass = self.get_bass(magnitudes)

        if bass > 0.5:
            # Main eruption column
            for i in range(20):
                y = self.height - i * 30
                spread = int(bass * 30)

                for j in range(-spread, spread, 5):
                    x = self.center_x + j

                    color = self.hsv_to_bgr(120, 150, 200)
                    cv2.circle(frame, (x, y), 5, color, -1)

        # Steam particles
        energy = self.get_energy(magnitudes)
        for i in range(int(energy * 40)):
            x = int(self.center_x + np.random.random() * 100 - 50)
            y = int(self.height - i * 10)

            cv2.circle(frame, (x, y), 3, (200, 200, 200), -1)

        return frame

    def draw_mode_335_pollen_cloud(self, frame, magnitudes):
        """Mode 335: Pollen drifting in air"""
        energy = self.get_energy(magnitudes)

        for i in range(int(energy * 100)):
            phase = self.frame_count * 0.02 + i * 0.1

            x = int((np.sin(phase) * 0.5 + 0.5) * self.width)
            y = int((np.cos(phase * 0.7) * 0.5 + 0.5) * self.height)

            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            size = 2 + int(mag * 5)
            color = self.hsv_to_bgr(40, 200, 200)

            cv2.circle(frame, (x, y), size, color, -1)

        return frame

    def draw_mode_336_desert_dunes(self, frame, magnitudes):
        """Mode 336: Sand dunes in wind"""
        # Multiple dune layers
        for layer in range(4):
            y_base = int(self.height * (0.4 + layer * 0.15))

            points = []
            for i, mag in enumerate(magnitudes):
                x = int((i / len(magnitudes)) * self.width)
                dune = np.sin(x * 0.01 + layer + self.frame_count * 0.02) * mag * 40
                y = y_base + int(dune)
                points.append([x, y])

            points.append([self.width, self.height])
            points.append([0, self.height])
            points = np.array(points, dtype=np.int32)

            hue = 25 + layer * 5
            color = self.hsv_to_bgr(hue, 100 - layer * 20, 180 - layer * 30)
            cv2.fillPoly(frame, [points], color)

        return frame

    def draw_mode_337_lily_pads(self, frame, magnitudes):
        """Mode 337: Water lilies on pond"""
        num_pads = 12
        for i in range(num_pads):
            angle = (i / num_pads) * 2 * np.pi + self.frame_count * 0.01

            mag_idx = i * len(magnitudes) // num_pads
            mag = magnitudes[mag_idx]

            dist = 100 + i * 30
            x = int(self.center_x + np.cos(angle) * dist)
            y = int(self.center_y + np.sin(angle) * dist)

            # Lily pad
            size = 20 + int(mag * 25)
            cv2.circle(frame, (x, y), size, (60, 120, 80), -1)
            cv2.circle(frame, (x, y), size, (40, 100, 60), 2)

            # Flower
            if mag > 0.5:
                flower_color = self.hsv_to_bgr(160, 200, 255)
                cv2.circle(frame, (x, y), 8, flower_color, -1)

        return frame

    def draw_mode_338_termite_mound(self, frame, magnitudes):
        """Mode 338: Termite mound structure"""
        # Central mound
        for i, mag in enumerate(magnitudes[::2]):
            y = int(self.height - (i / 60) * self.height * 0.7)
            width = 40 + int(mag * 60) - i

            if width > 5:
                color = self.hsv_to_bgr(20, 150, 100 + int(mag * 80))
                cv2.ellipse(frame, (self.center_x, y), (width, 15), 0, 0, 360, color, -1)

        # Tunnels/chambers
        for i in range(20):
            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            if mag > 0.4:
                x = int(self.center_x + np.random.randint(-50, 50))
                y = int(self.height * (0.3 + np.random.random() * 0.5))

                cv2.circle(frame, (x, y), 6, (40, 30, 20), -1)

        return frame

    def draw_mode_339_cherry_blossoms(self, frame, magnitudes):
        """Mode 339: Cherry blossom petals falling"""
        energy = self.get_energy(magnitudes)

        for i in range(int(energy * 60)):
            x = int((self.frame_count + i * 20) % self.width)
            y = int((self.frame_count * 0.8 + i * 15) % self.height)

            flutter = int(np.sin(y * 0.1 + i) * 25)
            x = (x + flutter) % self.width

            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            # Petal shape
            size = 6 + int(mag * 10)
            rotation = int(self.frame_count + i) % 360

            color = self.hsv_to_bgr(170, 100, 255)
            cv2.ellipse(frame, (x, y), (size, size // 2), rotation, 0, 360, color, -1)

        return frame

    def draw_mode_340_root_system(self, frame, magnitudes):
        """Mode 340: Underground root network"""
        # Start from center top
        x, y = self.center_x, 100

        def draw_root(x, y, angle, depth, mag):
            if depth > 8:
                return

            length = 30 + mag * 40
            rad = np.deg2rad(angle)

            x2 = int(x + np.cos(rad) * length)
            y2 = int(y + np.sin(rad) * length)

            thickness = max(1, 8 - depth)
            color = self.hsv_to_bgr(30, 200, 100 - depth * 10)

            cv2.line(frame, (int(x), int(y)), (x2, y2), color, thickness)

            # Branch
            if mag > 0.3:
                draw_root(x2, y2, angle - 30, depth + 1, mag * 0.8)
                draw_root(x2, y2, angle + 30, depth + 1, mag * 0.8)

        bass = self.get_bass(magnitudes)
        draw_root(x, y, 90, 0, bass)

        return frame

    def draw_mode_341_plankton_swarm(self, frame, magnitudes):
        """Mode 341: Bioluminescent plankton"""
        for i, mag in enumerate(magnitudes):
            if mag > 0.2:
                x = int((i / len(magnitudes)) * self.width)
                y = int(self.height * 0.3 + np.sin(self.frame_count * 0.1 + i) * self.height * 0.3)

                # Glow effect
                glow = int(mag * 255)
                size = 2 + int(mag * 6)

                cv2.circle(frame, (x, y), size + 3, (0, glow // 4, glow // 4), -1)
                cv2.circle(frame, (x, y), size, (0, glow, glow), -1)

        return frame

    def draw_mode_342_frost_patterns(self, frame, magnitudes):
        """Mode 342: Frost forming on glass"""
        # Dendritic patterns from edges
        for edge in range(4):
            if edge == 0:  # Top
                start_points = [(int(np.random.random() * self.width), 0) for _ in range(10)]
            elif edge == 1:  # Bottom
                start_points = [(int(np.random.random() * self.width), self.height) for _ in range(10)]
            elif edge == 2:  # Left
                start_points = [(0, int(np.random.random() * self.height)) for _ in range(10)]
            else:  # Right
                start_points = [(self.width, int(np.random.random() * self.height)) for _ in range(10)]

            for sp in start_points:
                for i, mag in enumerate(magnitudes[::5]):
                    if mag > 0.3:
                        angle = np.random.random() * 2 * np.pi
                        length = mag * 30

                        x2 = int(sp[0] + np.cos(angle) * length)
                        y2 = int(sp[1] + np.sin(angle) * length)

                        cv2.line(frame, sp, (x2, y2), (200, 230, 255), 1)

        return frame

    def draw_mode_343_ant_trails(self, frame, magnitudes):
        """Mode 343: Ant colony foraging trails"""
        # Pheromone trails
        for i in range(8):
            path_angle = (i / 8) * 2 * np.pi

            x, y = self.center_x, self.center_y

            for j, mag in enumerate(magnitudes[::3]):
                angle = path_angle + np.sin(j * 0.5) * mag
                distance = mag * 40

                x += np.cos(angle) * distance
                y += np.sin(angle) * distance

                if 0 < x < self.width and 0 < y < self.height:
                    color = self.hsv_to_bgr(0, 200, 100 + int(mag * 100))
                    cv2.circle(frame, (int(x), int(y)), 2, color, -1)

        return frame

    def draw_mode_344_seaweed_sway(self, frame, magnitudes):
        """Mode 344: Seaweed swaying underwater"""
        num_strands = 12
        for i in range(num_strands):
            x = int((i / num_strands) * self.width)

            for j, mag in enumerate(magnitudes[::3]):
                y = self.height - int(j * mag * 18)
                sway = int(np.sin(self.frame_count * 0.08 + i + j * 0.2) * mag * 25)

                color = self.hsv_to_bgr(80 + int(mag * 30), 200, 100 + int(mag * 100))
                cv2.circle(frame, (x + sway, y), 3 + int(mag * 6), color, -1)

        return frame

    def draw_mode_345_volcano_ash(self, frame, magnitudes):
        """Mode 345: Volcanic ash cloud"""
        bass = self.get_bass(magnitudes)

        # Ash plume
        for i in range(int(bass * 100)):
            spread = max(1, int((self.frame_count + i) * 2))
            x = int(self.center_x + np.random.randint(-spread, spread + 1))
            y = int(self.height - self.frame_count * 3 - i * 5) % self.height

            size = 2 + int(np.random.random() * 5)
            brightness = int(50 + np.random.random() * 80)

            cv2.circle(frame, (x, y), size, (brightness, brightness, brightness), -1)

        return frame

    def draw_mode_346_dragonfly_wings(self, frame, magnitudes):
        """Mode 346: Dragonfly wing patterns"""
        num_dragonflies = 6
        for i in range(num_dragonflies):
            angle = (i / num_dragonflies) * 2 * np.pi + self.frame_count * 0.05

            mag_idx = i * len(magnitudes) // num_dragonflies
            mag = magnitudes[mag_idx]

            dist = 150 + mag * 100
            x = int(self.center_x + np.cos(angle) * dist)
            y = int(self.center_y + np.sin(angle) * dist)

            # Four wings
            wing_size = 20 + int(mag * 20)
            for wing in range(4):
                wing_angle = angle + (wing / 4) * 2 * np.pi
                cv2.ellipse(frame, (x, y), (wing_size, wing_size // 2),
                           int(np.rad2deg(wing_angle)), 0, 360, (150, 180, 200), 1)

        return frame

    def draw_mode_347_pebble_ripples(self, frame, magnitudes):
        """Mode 347: Pebbles dropping in water"""
        for i, mag in enumerate(magnitudes):
            if mag > 0.5:
                x = int((i / len(magnitudes)) * self.width)
                y = int(self.height * 0.5)

                # Expanding ripples
                for r in range(5):
                    radius = int((self.frame_count % 30) * mag * 3 + r * 20)
                    alpha = max(0, 200 - radius * 2)

                    if alpha > 0:
                        color = self.hsv_to_bgr(120, 150, alpha)
                        cv2.circle(frame, (x, y), radius, color, 2)

        return frame

    def draw_mode_348_moss_tendrils(self, frame, magnitudes):
        """Mode 348: Moss growing on stone"""
        # Random moss patches
        for i in range(200):
            mag_idx = i % len(magnitudes)
            mag = magnitudes[mag_idx]

            if mag > 0.15:
                x = int(np.random.random() * self.width)
                y = int(np.random.random() * self.height)

                # Organic spread
                for j in range(int(mag * 10)):
                    ox = x + int(np.random.random() * 20 - 10)
                    oy = y + int(np.random.random() * 20 - 10)

                    size = 1 + int(mag * 4)
                    hue = 70 + int(mag * 20)
                    color = self.hsv_to_bgr(hue, 200, 80 + int(mag * 100))

                    cv2.circle(frame, (ox, oy), size, color, -1)

        return frame

    def draw_mode_349_starfish_arms(self, frame, magnitudes):
        """Mode 349: Starfish with moving arms"""
        # 5 arms
        for arm in range(5):
            base_angle = (arm / 5) * 2 * np.pi

            for i, mag in enumerate(magnitudes[::5]):
                angle = base_angle + np.sin(self.frame_count * 0.05 + i) * mag * 0.3
                dist = 50 + i * mag * 15

                x = int(self.center_x + np.cos(angle) * dist)
                y = int(self.center_y + np.sin(angle) * dist)

                size = 8 - int(i * 0.2)
                color = self.hsv_to_bgr(10 + int(mag * 30), 200, 200)

                cv2.circle(frame, (x, y), max(2, size), color, -1)

        return frame

    def draw_mode_350_venus_flytrap(self, frame, magnitudes):
        """Mode 350: Venus flytrap opening and closing"""
        bass = self.get_bass(magnitudes)

        # Two lobes
        open_angle = bass * 60  # Opens based on bass

        for lobe in [-1, 1]:
            points = []
            for i in range(20):
                angle = (i / 20) * np.pi + lobe * np.deg2rad(open_angle)
                radius = 80 + np.sin(i * 0.5) * 30

                x = int(self.center_x + np.cos(angle) * radius)
                y = int(self.center_y + np.sin(angle) * radius * lobe)
                points.append([x, y])

            points = np.array(points, dtype=np.int32)
            cv2.fillPoly(frame, [points], (60, 180, 80))

            # Trigger hairs
            for i in range(5):
                hx = int(self.center_x + np.random.randint(-30, 30))
                hy = int(self.center_y + lobe * 20)
                cv2.line(frame, (hx, hy), (hx, hy + lobe * 15), (100, 200, 100), 2)

        return frame

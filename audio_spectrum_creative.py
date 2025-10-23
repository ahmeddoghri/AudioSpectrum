#!/usr/bin/env python3
"""
Creative Audio Spectrum Visualizer - Lofi & Jazz Editions
Generates transparent videos with wild, creative audio spectrum animations
Perfect for lofi YouTube channels and K-pop/soul/jazz transformations

Visualization Modes:
  --mode 1: Vinyl Grooves - Rotating circular grooves like a vinyl record (perfect for lofi)
  --mode 2: Neon Rain - Vertical neon droplets cascading down (cyberpunk lofi aesthetic)
  --mode 3: Jazzy Fireworks - Bursting particles that explode from center (jazz energy)
  --mode 4: Retro Cassette - VU meters and tape reel animation (vintage lofi)
  --mode 5: Soul Aura - Pulsing organic blob with smooth edges (soul/RnB vibe)
  --mode 6: Frequency Flowers - Blooming petals that grow with music (dreamy lofi)
  --mode 7: Electric Heartbeat - EKG-style waveform with glow (emotional jazz)
  --mode 8: Pixel Clouds - 8-bit style floating cloud particles (retro lofi)
  --mode 9: Liquid Mercury - Flowing metallic waves (smooth jazz/soul)
  --mode 10: Cosmic Dust - Swirling galaxy particles with trails (ambient lofi)
  --mode 11: Quantum Strings - Vibrating strings with interference patterns (experimental)
  --mode 12: Lava Lamp - Rising and morphing organic blobs (psychedelic lofi)
  --mode 13: DNA Helix - Double helix structure that twists with music (scientific vibe)
  --mode 14: Lightning Strikes - Electric bolts connecting frequency peaks (intense energy)
  --mode 15: Morphing Geometry - Shifting 3D wireframe shapes (abstract modern)
  --mode 16: Ink Drops - Organic ink dispersing in water (artistic lofi)
  --mode 17: Aurora Waves - Northern lights-style flowing ribbons (ethereal ambient)
  --mode 18: Fractal Bloom - Self-similar patterns emerging from center (mathematical art)
  --mode 19: Plasma Storm - Swirling energy vortex with tendrils (chaotic energy)
  --mode 20: Crystal Growth - Geometric crystals forming and shattering (elegant minimalism)

Examples:
  # Vinyl grooves for lofi
python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode1.mov'  --mode 1

LOFI 
python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode2.mov'  --mode 2

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode3.mov'  --mode 3

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode4.mov'  --mode 4

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode5.mov'  --mode 5

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode6.mov'  --mode 6

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode7.mov'  --mode 7

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode8.mov'  --mode 8

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode9.mov'  --mode 9

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode10.mov'  --mode 10    

  
  
  # Soul aura for K-pop soul covers
  python audio_spectrum_creative.py input.mp3 output.mov --mode 5

  # Jazzy fireworks for upbeat tracks
  python audio_spectrum_creative.py input.mp3 output.mov --mode 3
"""

import sys
import numpy as np
import cv2
import librosa
import argparse
from pathlib import Path


class CreativeSpectrumVisualizer:
    def __init__(self, audio_path, output_path, width=1920, height=1080,
                 fps=30, num_bars=120, smoothing=0.7, mode=1):
        """
        Initialize the creative spectrum visualizer

        Args:
            audio_path: Path to input audio file
            output_path: Path to output video file
            width: Video width in pixels
            height: Video height in pixels
            fps: Frames per second
            num_bars: Number of frequency bars/elements
            smoothing: Smoothing factor (0-1) for animation
            mode: Visualization mode (1-10)
        """
        self.audio_path = audio_path
        self.output_path = output_path
        self.width = width
        self.height = height
        self.fps = fps
        self.num_bars = num_bars
        self.smoothing = smoothing
        self.mode = mode

        self.center_x = width // 2
        self.center_y = height // 2
        self.max_radius = min(width, height) // 2 - 40

        # For smoothing between frames
        self.prev_magnitudes = None

        # Mode-specific state
        self.rotation_angle = 0
        self.rain_particles = []
        self.firework_particles = []
        self.cassette_reel_angle = 0
        self.flower_petals = []
        self.pixel_clouds = []
        self.mercury_history = []
        self.cosmic_particles = []
        self.frame_counter = 0

    def load_audio(self):
        """Load and process audio file"""
        print(f"Loading audio from: {self.audio_path}")

        y, sr = librosa.load(self.audio_path, sr=None)
        self.sample_rate = sr
        self.duration = librosa.get_duration(y=y, sr=sr)

        print(f"Audio loaded: {self.duration:.2f}s, Sample rate: {sr}Hz")

        hop_length = int(sr / self.fps)
        n_fft = 2048

        stft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
        self.magnitude = np.abs(stft)

        self.magnitude_db = librosa.amplitude_to_db(self.magnitude, ref=np.max)
        self.magnitude_norm = (self.magnitude_db - self.magnitude_db.min()) / \
                              (self.magnitude_db.max() - self.magnitude_db.min())

        self.num_frames = self.magnitude_norm.shape[1]
        print(f"Processed {self.num_frames} frames")

        return y, sr

    def get_frequency_bands(self, frame_idx):
        """Extract frequency bands for a specific frame"""
        if frame_idx >= self.num_frames:
            frame_idx = self.num_frames - 1

        frame_magnitudes = self.magnitude_norm[:, frame_idx]
        total_freqs = len(frame_magnitudes)
        useful_freqs = int(total_freqs * 0.6)

        bar_magnitudes = []
        for i in range(self.num_bars):
            t = i / self.num_bars
            freq_pos = int(useful_freqs * (t ** 1.5))

            window_size = max(1, useful_freqs // (self.num_bars * 2))
            start_idx = max(0, freq_pos - window_size // 2)
            end_idx = min(useful_freqs, freq_pos + window_size // 2)

            if start_idx < end_idx:
                avg_magnitude = np.mean(frame_magnitudes[start_idx:end_idx])
            else:
                avg_magnitude = frame_magnitudes[freq_pos] if freq_pos < len(frame_magnitudes) else 0

            bar_magnitudes.append(avg_magnitude)

        bar_magnitudes = np.array(bar_magnitudes)

        if self.prev_magnitudes is not None:
            bar_magnitudes = (self.smoothing * self.prev_magnitudes +
                            (1 - self.smoothing) * bar_magnitudes)

        self.prev_magnitudes = bar_magnitudes.copy()

        return bar_magnitudes

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

    def draw_spectrum(self, frame, magnitudes):
        """Draw spectrum based on selected mode"""
        self.frame_counter += 1

        if self.mode == 1:
            return self.draw_mode_1_vinyl_grooves(frame, magnitudes)
        elif self.mode == 2:
            return self.draw_mode_2_neon_rain(frame, magnitudes)
        elif self.mode == 3:
            return self.draw_mode_3_jazzy_fireworks(frame, magnitudes)
        elif self.mode == 4:
            return self.draw_mode_4_retro_cassette(frame, magnitudes)
        elif self.mode == 5:
            return self.draw_mode_5_soul_aura(frame, magnitudes)
        elif self.mode == 6:
            return self.draw_mode_6_frequency_flowers(frame, magnitudes)
        elif self.mode == 7:
            return self.draw_mode_7_electric_heartbeat(frame, magnitudes)
        elif self.mode == 8:
            return self.draw_mode_8_pixel_clouds(frame, magnitudes)
        elif self.mode == 9:
            return self.draw_mode_9_liquid_mercury(frame, magnitudes)
        elif self.mode == 10:
            return self.draw_mode_10_cosmic_dust(frame, magnitudes)
        else:
            return self.draw_mode_1_vinyl_grooves(frame, magnitudes)

    def generate_video(self):
        """Generate the final video with transparent background"""
        print(f"Generating video: {self.output_path}")

        self.load_audio()

        temp_no_audio = str(Path(self.output_path).with_suffix('')) + '_temp_no_audio.mp4'
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        video_writer = cv2.VideoWriter(
            temp_no_audio, fourcc, self.fps,
            (self.width, self.height), True
        )

        if not video_writer.isOpened():
            raise RuntimeError("Failed to open video writer")

        total_frames = int(self.duration * self.fps)

        for frame_idx in range(total_frames):
            frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)

            audio_frame_idx = int(frame_idx * self.num_frames / total_frames)
            magnitudes = self.get_frequency_bands(audio_frame_idx)

            frame = self.draw_spectrum(frame, magnitudes)
            video_writer.write(frame)

            if (frame_idx + 1) % 30 == 0 or frame_idx == total_frames - 1:
                progress = (frame_idx + 1) / total_frames * 100
                print(f"Progress: {progress:.1f}% ({frame_idx + 1}/{total_frames} frames)")

        video_writer.release()
        print(f"\nVideo generation complete (silent): {temp_no_audio}")

        print("Adding audio and transparency...")
        import subprocess

        try:
            final_output = str(Path(self.output_path).with_suffix('.mov'))

            result = subprocess.run([
                'ffmpeg', '-y',
                '-i', temp_no_audio,
                '-i', self.audio_path,
                '-filter_complex',
                '[0:v]colorkey=0x000000:0.01:0.1[ckout];[ckout]format=yuva420p[video]',
                '-map', '[video]',
                '-map', '1:a',
                '-c:v', 'prores_ks',
                '-profile:v', '4444',
                '-c:a', 'aac',
                '-shortest',
                final_output
            ], capture_output=True, text=True)

            Path(temp_no_audio).unlink()

            if result.returncode == 0:
                self.output_path = final_output
                print(f"✓ Video with transparency and audio created successfully")
                print(f"✓ Output: {final_output}")
            else:
                print(f"Warning: Could not create transparent video. Creating standard video instead.")
                print(f"FFmpeg error: {result.stderr}")

                result = subprocess.run([
                    'ffmpeg', '-y',
                    '-i', temp_no_audio,
                    '-i', self.audio_path,
                    '-c:v', 'copy',
                    '-c:a', 'aac',
                    '-shortest',
                    final_output
                ], capture_output=True, text=True)

                Path(temp_no_audio).unlink()

                if result.returncode == 0:
                    print(f"✓ Standard video created: {final_output}")
                else:
                    print(f"Error: Could not create video")

        except FileNotFoundError:
            print("Error: ffmpeg not found. Please install ffmpeg:")
            print("  brew install ffmpeg")
            Path(temp_no_audio).unlink()
            raise
        except Exception as e:
            print(f"Error: Could not process video: {e}")
            if Path(temp_no_audio).exists():
                Path(temp_no_audio).unlink()
            raise

        print(f"Duration: {self.duration:.2f}s, Resolution: {self.width}x{self.height}, FPS: {self.fps}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate creative audio spectrum visualizations for lofi and jazz channels',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Vinyl grooves for lofi YouTube channel
  python audio_spectrum_creative.py input.mp3 output.mov --mode 1

  # Soul aura for K-pop soul/jazz covers
  python audio_spectrum_creative.py input.mp3 output.mov --mode 5

  # Neon rain for cyberpunk lofi
  python audio_spectrum_creative.py input.mp3 output.mov --mode 2

  # Electric heartbeat for emotional jazz
  python audio_spectrum_creative.py input.mp3 output.mov --mode 7
        """
    )

    parser.add_argument('input', help='Input audio file (.mp3 or .wav)')
    parser.add_argument('output', help='Output video file (.mov recommended)')
    parser.add_argument('--mode', type=int, choices=range(1, 11), default=1,
                       help='Visualization mode: 1=Vinyl Grooves, 2=Neon Rain, 3=Jazzy Fireworks, 4=Retro Cassette, 5=Soul Aura, 6=Frequency Flowers, 7=Electric Heartbeat, 8=Pixel Clouds, 9=Liquid Mercury, 10=Cosmic Dust')
    parser.add_argument('--width', type=int, default=1920, help='Video width (default: 1920)')
    parser.add_argument('--height', type=int, default=1080, help='Video height (default: 1080)')
    parser.add_argument('--fps', type=int, default=30, help='Frames per second (default: 30)')
    parser.add_argument('--num-bars', type=int, default=120, help='Number of frequency elements (default: 120)')
    parser.add_argument('--smoothing', type=float, default=0.7, help='Smoothing factor 0-1 (default: 0.7)')

    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)

    mode_names = {
        1: "Vinyl Grooves (lofi)",
        2: "Neon Rain (cyberpunk lofi)",
        3: "Jazzy Fireworks (jazz energy)",
        4: "Retro Cassette (vintage lofi)",
        5: "Soul Aura (soul/RnB)",
        6: "Frequency Flowers (dreamy lofi)",
        7: "Electric Heartbeat (emotional jazz)",
        8: "Pixel Clouds (retro lofi)",
        9: "Liquid Mercury (smooth jazz)",
        10: "Cosmic Dust (ambient lofi)"
    }
    print(f"Selected visualization mode: {args.mode} - {mode_names.get(args.mode, 'Unknown')}")

    visualizer = CreativeSpectrumVisualizer(
        audio_path=args.input,
        output_path=args.output,
        width=args.width,
        height=args.height,
        fps=args.fps,
        num_bars=args.num_bars,
        smoothing=args.smoothing,
        mode=args.mode
    )

    try:
        visualizer.generate_video()
        print("\nSuccess! Your creative audio spectrum video is ready.")
        print(f"Perfect for lofi and jazz/soul YouTube channels!")
    except Exception as e:
        print(f"\nError generating video: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

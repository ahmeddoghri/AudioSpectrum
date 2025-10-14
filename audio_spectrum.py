#!/usr/bin/env python3
"""
Circular Audio Spectrum Visualizer
Generates a transparent video with circular audio spectrum animation

Visualization Modes:
  --mode 1: Bars (default) - Classic radial bars extending from center
  --mode 2: Waves/Layers - Concentric circular waves that pulse with music
  --mode 3: Particles - Circular particle system with glow effects
  --mode 4: Waveform - Smooth continuous filled waveform
  --mode 5: Polygon - Dynamic morphing polygon shapes
  --mode 6: Spiral - Hypnotic spiral arms rotating with audio
  --mode 7: DNA Helix - Double helix strands wrapping around the center
  --mode 8: Kaleidoscope - Symmetrical mirrored patterns with radial symmetry
  --mode 9: Pulse Rings - Expanding concentric rings that burst from center
  --mode 10: Star Burst - Dynamic star with points that expand and contract

Examples:
  # YouTube regular - 1920x1080, auto for .mov
  python audio_spectrum.py '/Users/ahmeddoghri/Desktop/RÜFÜS DU SOL - New Sky (Lyrics).mp3' '/Users/ahmeddoghri/Desktop/output.mov'

  # YouTube Shorts - 1080x1920, auto for .mp4
  python audio_spectrum.py '/Users/ahmeddoghri/Desktop/RÜFÜS DU SOL - New Sky (Lyrics).mp3' '/Users/ahmeddoghri/Desktop/output.mp4'

  # With different visualization mode
  python audio_spectrum.py '/Users/ahmeddoghri/Desktop/RÜFÜS DU SOL - New Sky (Lyrics).mp3' '/Users/ahmeddoghri/Desktop/output.mov' --mode 6
"""

import sys
import numpy as np
import cv2
import librosa
import argparse
from pathlib import Path


class CircularSpectrumVisualizer:
    def __init__(self, audio_path, output_path, width=1080, height=1080,
                 fps=30, num_bars=120, color=(0, 255, 255), inner_radius=150,
                 bar_width_multiplier=1.5, smoothing=0.7, gradient=False,
                 gradient_color1=None, gradient_color2=None, mode=1):
        """
        Initialize the circular spectrum visualizer

        Args:
            audio_path: Path to input audio file (.mp3 or .wav)
            output_path: Path to output video file
            width: Video width in pixels
            height: Video height in pixels
            fps: Frames per second
            num_bars: Number of frequency bars around the circle
            color: RGB color tuple for the spectrum bars (used if gradient=False)
            inner_radius: Starting radius for the bars (center circle size)
            bar_width_multiplier: Controls bar thickness
            smoothing: Smoothing factor (0-1) for animation
            gradient: Enable gradient mode (left to right color transition)
            gradient_color1: Left side color (BGR format)
            gradient_color2: Right side color (BGR format)
            mode: Visualization mode (1-10)
        """
        self.audio_path = audio_path
        self.output_path = output_path
        self.width = width
        self.height = height
        self.fps = fps
        self.num_bars = num_bars
        self.color = color
        self.inner_radius = inner_radius
        self.bar_width_multiplier = bar_width_multiplier
        self.smoothing = smoothing
        self.gradient = gradient
        self.gradient_color1 = gradient_color1
        self.gradient_color2 = gradient_color2
        self.mode = mode

        self.center_x = width // 2
        self.center_y = height // 2
        self.max_radius = min(width, height) // 2 - 20

        # For smoothing between frames
        self.prev_magnitudes = None

    def load_audio(self):
        """Load and process audio file"""
        print(f"Loading audio from: {self.audio_path}")

        # Load audio file
        y, sr = librosa.load(self.audio_path, sr=None)
        self.sample_rate = sr
        self.duration = librosa.get_duration(y=y, sr=sr)

        print(f"Audio loaded: {self.duration:.2f}s, Sample rate: {sr}Hz")

        # Calculate STFT (Short-Time Fourier Transform)
        hop_length = int(sr / self.fps)
        n_fft = 2048

        stft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
        self.magnitude = np.abs(stft)

        # Convert to dB scale for better visualization
        self.magnitude_db = librosa.amplitude_to_db(self.magnitude, ref=np.max)

        # Normalize to 0-1 range
        self.magnitude_norm = (self.magnitude_db - self.magnitude_db.min()) / \
                              (self.magnitude_db.max() - self.magnitude_db.min())

        self.num_frames = self.magnitude_norm.shape[1]
        print(f"Processed {self.num_frames} frames")

        return y, sr

    def get_frequency_bands(self, frame_idx):
        """Extract frequency bands for a specific frame"""
        if frame_idx >= self.num_frames:
            frame_idx = self.num_frames - 1

        # Get magnitude for this frame
        frame_magnitudes = self.magnitude_norm[:, frame_idx]

        # Use logarithmic spacing for more perceptually accurate frequency distribution
        # This focuses more bars on lower frequencies where music has more energy
        total_freqs = len(frame_magnitudes)

        # Only use the lower 60% of frequencies (where most music energy is)
        # and distribute them across all bars
        useful_freqs = int(total_freqs * 0.6)

        bar_magnitudes = []
        for i in range(self.num_bars):
            # Logarithmic distribution: more bars for lower frequencies
            t = i / self.num_bars
            # Exponential mapping to focus on lower frequencies
            freq_pos = int(useful_freqs * (t ** 1.5))

            # Get a small window around this frequency
            window_size = max(1, useful_freqs // (self.num_bars * 2))
            start_idx = max(0, freq_pos - window_size // 2)
            end_idx = min(useful_freqs, freq_pos + window_size // 2)

            # Average the frequencies in this window
            if start_idx < end_idx:
                avg_magnitude = np.mean(frame_magnitudes[start_idx:end_idx])
            else:
                avg_magnitude = frame_magnitudes[freq_pos] if freq_pos < len(frame_magnitudes) else 0

            bar_magnitudes.append(avg_magnitude)

        bar_magnitudes = np.array(bar_magnitudes)

        # Apply smoothing between frames
        if self.prev_magnitudes is not None:
            bar_magnitudes = (self.smoothing * self.prev_magnitudes +
                             (1 - self.smoothing) * bar_magnitudes)

        self.prev_magnitudes = bar_magnitudes.copy()

        return bar_magnitudes

    def get_color_for_position(self, index, magnitude):
        """Get color for a given position with optional gradient and magnitude intensity"""
        angle_step = 360 / self.num_bars

        if self.gradient and self.gradient_color1 and self.gradient_color2:
            # Calculate gradient position based on angle
            angle_normalized = (index * angle_step) / 360.0

            # Create a smooth transition: left (0.5) to right (0 or 1)
            if angle_normalized <= 0.5:
                blend = 0.5 - angle_normalized
            else:
                blend = angle_normalized - 0.5

            blend = blend * 2  # Scale to 0-1 range

            # Interpolate between colors
            bar_color = (
                int(self.gradient_color1[0] * (1 - blend) + self.gradient_color2[0] * blend),
                int(self.gradient_color1[1] * (1 - blend) + self.gradient_color2[1] * blend),
                int(self.gradient_color1[2] * (1 - blend) + self.gradient_color2[2] * blend)
            )

            # Add brightness based on magnitude
            intensity = int(80 * magnitude)
            bar_color = (
                min(255, bar_color[0] + intensity),
                min(255, bar_color[1] + intensity),
                min(255, bar_color[2] + intensity)
            )
        else:
            # Single color mode with intensity
            intensity = int(255 * magnitude)
            bar_color = (
                min(255, self.color[0] + intensity // 3),
                min(255, self.color[1] + intensity // 3),
                min(255, self.color[2] + intensity // 3)
            )

        return bar_color

    def draw_center_circle(self, frame, magnitudes):
        """Draw a consistent center circle with subtle glow"""
        # Get average magnitude for center circle glow
        avg_magnitude = np.mean(magnitudes)

        # Base circle color (use gradient or single color)
        circle_color = (180, 180, 180)  # self.get_color_for_position(0, avg_magnitude * 0.5)

        # Draw outer glow ring (subtle)
        glow_color = tuple(int(c * 0.3) for c in circle_color)
        cv2.circle(frame, (self.center_x, self.center_y), self.inner_radius + 2,
                  glow_color, 1, lineType=cv2.LINE_AA)

        # Draw main center circle outline
        cv2.circle(frame, (self.center_x, self.center_y), self.inner_radius,
                  circle_color, 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_1_bars(self, frame, magnitudes):
        """Mode 1: Classic radial bars (original mode)"""
        angle_step = 360 / self.num_bars

        for i, magnitude in enumerate(magnitudes):
            angle = np.deg2rad(i * angle_step)

            # Calculate bar height
            min_bar_height = 5
            max_bar_height = self.max_radius - self.inner_radius
            bar_height = int(magnitude * max_bar_height)
            bar_height = max(min_bar_height, bar_height)

            # Calculate start and end points
            start_x = int(self.center_x + self.inner_radius * np.cos(angle))
            start_y = int(self.center_y + self.inner_radius * np.sin(angle))
            end_x = int(self.center_x + (self.inner_radius + bar_height) * np.cos(angle))
            end_y = int(self.center_y + (self.inner_radius + bar_height) * np.sin(angle))

            # Calculate bar thickness
            thickness = max(1, int(self.bar_width_multiplier * angle_step / 2))

            # Get color
            bar_color = self.get_color_for_position(i, magnitude)

            cv2.line(frame, (start_x, start_y), (end_x, end_y),
                    bar_color, thickness, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_2_waves(self, frame, magnitudes):
        """Mode 2: Concentric circular waves/layers"""
        num_layers = 5
        angle_step = 360 / self.num_bars

        for layer in range(num_layers):
            points = []
            layer_progress = layer / num_layers

            for i, magnitude in enumerate(magnitudes):
                angle = np.deg2rad(i * angle_step)

                # Each layer has a different base radius and responds to audio
                base_radius = self.inner_radius + (self.max_radius - self.inner_radius) * layer_progress
                wave_amplitude = magnitude * (self.max_radius - self.inner_radius) * 0.15
                radius = int(base_radius + wave_amplitude)

                x = int(self.center_x + radius * np.cos(angle))
                y = int(self.center_y + radius * np.sin(angle))
                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            # Get color for this layer (use average magnitude)
            avg_magnitude = np.mean(magnitudes)
            layer_color = self.get_color_for_position(layer * (self.num_bars // num_layers), avg_magnitude)

            # Make outer layers slightly transparent by reducing intensity
            alpha = 1.0 - (layer * 0.15)
            layer_color = tuple(int(c * alpha) for c in layer_color)

            # Draw the wave
            thickness = max(1, 3 - layer // 2)
            cv2.polylines(frame, [points], isClosed=True, color=layer_color,
                         thickness=thickness, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_3_particles(self, frame, magnitudes):
        """Mode 3: Particle rings with varying sizes"""
        angle_step = 360 / self.num_bars

        for i, magnitude in enumerate(magnitudes):
            angle = np.deg2rad(i * angle_step)

            # Calculate position
            max_bar_height = self.max_radius - self.inner_radius
            bar_height = int(magnitude * max_bar_height)
            radius = self.inner_radius + bar_height

            x = int(self.center_x + radius * np.cos(angle))
            y = int(self.center_y + radius * np.sin(angle))

            # Particle size based on magnitude
            particle_size = max(2, int(8 * magnitude + 2))

            # Get color
            particle_color = self.get_color_for_position(i, magnitude)

            # Draw circle particle
            cv2.circle(frame, (x, y), particle_size, particle_color, -1, lineType=cv2.LINE_AA)

            # Add a glow effect for high magnitudes
            if magnitude > 0.6:
                glow_size = particle_size + 3
                glow_color = tuple(int(c * 0.5) for c in particle_color)
                cv2.circle(frame, (x, y), glow_size, glow_color, 1, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_4_waveform(self, frame, magnitudes):
        """Mode 4: Radial waveform (smooth continuous wave)"""
        angle_step = 360 / self.num_bars
        points_outer = []
        points_inner = []

        for i, magnitude in enumerate(magnitudes):
            angle = np.deg2rad(i * angle_step)

            # Calculate radius based on magnitude
            max_bar_height = self.max_radius - self.inner_radius
            bar_height = int(magnitude * max_bar_height)
            radius = self.inner_radius + bar_height

            x = int(self.center_x + radius * np.cos(angle))
            y = int(self.center_y + radius * np.sin(angle))
            points_outer.append([x, y])

            # Inner point for filled area
            x_inner = int(self.center_x + self.inner_radius * np.cos(angle))
            y_inner = int(self.center_y + self.inner_radius * np.sin(angle))
            points_inner.append([x_inner, y_inner])

        points_outer = np.array(points_outer, dtype=np.int32)
        points_inner = np.array(points_inner, dtype=np.int32)

        # Create filled polygon between inner and outer waves
        # Combine outer and reversed inner points
        all_points = np.concatenate([points_outer, points_inner[::-1]])

        # Get average color
        avg_magnitude = np.mean(magnitudes)
        fill_color = self.get_color_for_position(0, avg_magnitude)
        # Reduce intensity for fill
        fill_color = tuple(int(c * 0.6) for c in fill_color)

        # Draw filled area
        cv2.fillPoly(frame, [all_points], fill_color, lineType=cv2.LINE_AA)

        # Draw outer outline with varying colors
        for i in range(len(points_outer)):
            next_i = (i + 1) % len(points_outer)
            line_color = self.get_color_for_position(i, magnitudes[i])
            cv2.line(frame, tuple(points_outer[i]), tuple(points_outer[next_i]),
                    line_color, 2, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_5_polygon(self, frame, magnitudes):
        """Mode 5: Dynamic polygon morph"""
        # Use fewer points for polygon effect
        polygon_points = 36
        step = self.num_bars // polygon_points
        angle_step = 360 / polygon_points

        points = []
        for i in range(polygon_points):
            angle = np.deg2rad(i * angle_step)

            # Get magnitude for this section (average nearby bars)
            mag_idx = i * step
            magnitude = np.mean(magnitudes[mag_idx:mag_idx + step]) if mag_idx < len(magnitudes) else magnitudes[-1]

            # Calculate radius
            max_bar_height = self.max_radius - self.inner_radius
            bar_height = int(magnitude * max_bar_height)
            radius = self.inner_radius + bar_height

            x = int(self.center_x + radius * np.cos(angle))
            y = int(self.center_y + radius * np.sin(angle))
            points.append([x, y])

        points = np.array(points, dtype=np.int32)

        # Draw multiple concentric polygons with different colors
        num_layers = 4
        for layer in range(num_layers):
            layer_progress = (layer + 1) / num_layers
            layer_points = []

            for i, point in enumerate(points):
                # Interpolate between center and outer point
                x = int(self.center_x + (point[0] - self.center_x) * layer_progress)
                y = int(self.center_y + (point[1] - self.center_y) * layer_progress)
                layer_points.append([x, y])

            layer_points = np.array(layer_points, dtype=np.int32)

            # Get color for this layer
            avg_magnitude = np.mean(magnitudes)
            layer_color = self.get_color_for_position(layer * 30, avg_magnitude)

            # Varying thickness and opacity
            thickness = max(1, 4 - layer)
            alpha = 0.6 + (layer * 0.1)
            layer_color = tuple(int(c * alpha) for c in layer_color)

            cv2.polylines(frame, [layer_points], isClosed=True, color=layer_color,
                         thickness=thickness, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_6_spiral(self, frame, magnitudes):
        """Mode 6: Hypnotic spiral arms"""
        num_arms = 5  # Number of spiral arms
        angle_step = 360 / self.num_bars

        for arm in range(num_arms):
            points = []
            arm_offset = (360 / num_arms) * arm

            for i, magnitude in enumerate(magnitudes):
                angle = np.deg2rad(i * angle_step + arm_offset)

                # Create spiral effect - radius increases with angle
                progress = i / self.num_bars
                max_bar_height = self.max_radius - self.inner_radius

                # Spiral outward effect
                spiral_radius = self.inner_radius + (progress * max_bar_height * 0.7)
                # Add magnitude variation
                radius_variation = magnitude * max_bar_height * 0.3
                radius = int(spiral_radius + radius_variation)

                x = int(self.center_x + radius * np.cos(angle))
                y = int(self.center_y + radius * np.sin(angle))
                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            # Get color for this arm
            avg_magnitude = np.mean(magnitudes)
            arm_color = self.get_color_for_position(arm * (self.num_bars // num_arms), avg_magnitude)

            # Draw spiral arm with varying thickness
            for i in range(len(points) - 1):
                thickness = max(1, int(3 - (i / len(points)) * 2))
                cv2.line(frame, tuple(points[i]), tuple(points[i + 1]),
                        arm_color, thickness, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_7_dna_helix(self, frame, magnitudes):
        """Mode 7: DNA double helix strands"""
        angle_step = 360 / self.num_bars
        max_bar_height = self.max_radius - self.inner_radius

        # Wave offset proportional to available space (10% of max height)
        wave_amplitude = max_bar_height * 0.1

        # Two strands
        for strand in range(2):
            points = []
            strand_phase = strand * np.pi  # 180 degree offset for second strand

            for i, magnitude in enumerate(magnitudes):
                angle = np.deg2rad(i * angle_step)

                # Create helix wave pattern
                progress = i / self.num_bars
                wave_offset = np.sin(progress * 4 * np.pi + strand_phase) * wave_amplitude

                base_radius = self.inner_radius + max_bar_height * 0.5
                radius_variation = magnitude * max_bar_height * 0.2
                radius = int(base_radius + wave_offset + radius_variation)

                x = int(self.center_x + radius * np.cos(angle))
                y = int(self.center_y + radius * np.sin(angle))
                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            # Color for strand
            avg_magnitude = np.mean(magnitudes)
            strand_color = self.get_color_for_position(strand * self.num_bars // 2, avg_magnitude)

            # Draw the strand
            cv2.polylines(frame, [points], isClosed=True, color=strand_color,
                         thickness=3, lineType=cv2.LINE_AA)

            # Draw connecting "rungs" between strands (every 10th bar)
            if strand == 1:
                for i in range(0, len(points), 10):
                    # Draw line to opposite strand
                    opposite_angle = np.deg2rad((i + self.num_bars // 2) * angle_step)

                    progress = i / self.num_bars
                    wave_offset_2 = np.sin(progress * 4 * np.pi) * wave_amplitude

                    magnitude_2 = magnitudes[(i + self.num_bars // 2) % len(magnitudes)]
                    base_radius = self.inner_radius + max_bar_height * 0.5
                    radius_2 = int(base_radius + wave_offset_2 + magnitude_2 * max_bar_height * 0.2)

                    x2 = int(self.center_x + radius_2 * np.cos(opposite_angle))
                    y2 = int(self.center_y + radius_2 * np.sin(opposite_angle))

                    rung_color = self.get_color_for_position(i, magnitudes[i])
                    rung_color = tuple(int(c * 0.5) for c in rung_color)
                    cv2.line(frame, tuple(points[i]), (x2, y2), rung_color, 1, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_8_kaleidoscope(self, frame, magnitudes):
        """Mode 8: Kaleidoscope with radial symmetry"""
        num_segments = 8  # Number of kaleidoscope segments
        segment_angle = 360 / num_segments
        angle_step = 360 / self.num_bars
        bars_per_segment = self.num_bars // num_segments

        for segment in range(num_segments):
            segment_offset = segment * segment_angle

            # Draw mirrored pattern in each segment
            for i in range(bars_per_segment):
                magnitude = magnitudes[i % len(magnitudes)]

                # Forward direction
                angle1 = np.deg2rad(segment_offset + (i * angle_step))
                # Mirrored direction
                angle2 = np.deg2rad(segment_offset + segment_angle - (i * angle_step))

                max_bar_height = self.max_radius - self.inner_radius
                bar_height = int(magnitude * max_bar_height)
                radius = self.inner_radius + bar_height

                # Forward point
                x1 = int(self.center_x + radius * np.cos(angle1))
                y1 = int(self.center_y + radius * np.sin(angle1))

                # Mirrored point
                x2 = int(self.center_x + radius * np.cos(angle2))
                y2 = int(self.center_y + radius * np.sin(angle2))

                # Get color
                bar_color = self.get_color_for_position(segment * bars_per_segment + i, magnitude)

                # Draw both mirrored elements
                inner_x1 = int(self.center_x + self.inner_radius * np.cos(angle1))
                inner_y1 = int(self.center_y + self.inner_radius * np.sin(angle1))
                inner_x2 = int(self.center_x + self.inner_radius * np.cos(angle2))
                inner_y2 = int(self.center_y + self.inner_radius * np.sin(angle2))

                thickness = max(1, int(self.bar_width_multiplier * segment_angle / bars_per_segment))
                cv2.line(frame, (inner_x1, inner_y1), (x1, y1), bar_color, thickness, lineType=cv2.LINE_AA)
                cv2.line(frame, (inner_x2, inner_y2), (x2, y2), bar_color, thickness, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_9_pulse_rings(self, frame, magnitudes):
        """Mode 9: Expanding pulse rings from center"""
        # Group magnitudes into rings
        num_rings = 12
        bars_per_ring = self.num_bars // num_rings
        max_bar_height = self.max_radius - self.inner_radius

        # Pulse expansion proportional to available space (8% of max height)
        max_pulse = max_bar_height * 0.08

        for ring_idx in range(num_rings):
            # Calculate average magnitude for this ring
            start_idx = ring_idx * bars_per_ring
            end_idx = start_idx + bars_per_ring
            ring_magnitude = np.mean(magnitudes[start_idx:end_idx])

            # Ring expands based on its position and magnitude
            ring_progress = ring_idx / num_rings
            base_radius = self.inner_radius + (ring_progress * max_bar_height)

            # Pulse effect - rings expand with magnitude (proportional)
            pulse_expansion = ring_magnitude * max_pulse
            radius = int(base_radius + pulse_expansion)

            # Get color for this ring
            ring_color = self.get_color_for_position(start_idx, ring_magnitude)

            # Thickness varies with magnitude
            thickness = max(1, int(2 + ring_magnitude * 5))

            # Make outer rings slightly more transparent
            alpha = 1.0 - (ring_progress * 0.3)
            ring_color = tuple(int(c * alpha) for c in ring_color)

            # Draw the ring
            cv2.circle(frame, (self.center_x, self.center_y), radius, ring_color,
                      thickness, lineType=cv2.LINE_AA)

            # Add glow for high magnitude rings
            if ring_magnitude > 0.7:
                glow_radius = radius + 3
                glow_color = tuple(int(c * 0.4) for c in ring_color)
                cv2.circle(frame, (self.center_x, self.center_y), glow_radius, glow_color,
                          1, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_10_star_burst(self, frame, magnitudes):
        """Mode 10: Dynamic star with expanding/contracting points"""
        num_points = 16  # Number of star points
        angle_step = 360 / num_points
        bars_per_point = self.num_bars // num_points

        star_points_outer = []
        star_points_inner = []

        for point_idx in range(num_points):
            angle = np.deg2rad(point_idx * angle_step)

            # Get average magnitude for this star point
            start_idx = point_idx * bars_per_point
            end_idx = start_idx + bars_per_point
            point_magnitude = np.mean(magnitudes[start_idx:end_idx])

            # Outer points (tips of star) - extend based on magnitude
            max_bar_height = self.max_radius - self.inner_radius
            bar_height = int(point_magnitude * max_bar_height)
            outer_radius = self.inner_radius + bar_height

            x_outer = int(self.center_x + outer_radius * np.cos(angle))
            y_outer = int(self.center_y + outer_radius * np.sin(angle))
            star_points_outer.append([x_outer, y_outer])

            # Inner points (between star tips) - smaller radius
            inner_angle = np.deg2rad((point_idx * angle_step) + (angle_step / 2))
            inner_magnitude = magnitudes[(start_idx + bars_per_point // 2) % len(magnitudes)]
            inner_radius = int(self.inner_radius + (inner_magnitude * max_bar_height * 0.4))

            x_inner = int(self.center_x + inner_radius * np.cos(inner_angle))
            y_inner = int(self.center_y + inner_radius * np.sin(inner_angle))
            star_points_inner.append([x_inner, y_inner])

        # Interleave outer and inner points to create star shape
        star_points = []
        for i in range(num_points):
            star_points.append(star_points_outer[i])
            star_points.append(star_points_inner[i])

        star_points = np.array(star_points, dtype=np.int32)

        # Draw filled star with gradient
        avg_magnitude = np.mean(magnitudes)
        fill_color = self.get_color_for_position(0, avg_magnitude)
        fill_color = tuple(int(c * 0.5) for c in fill_color)
        cv2.fillPoly(frame, [star_points], fill_color, lineType=cv2.LINE_AA)

        # Draw star outline with varying colors
        for i in range(len(star_points)):
            next_i = (i + 1) % len(star_points)
            segment_magnitude = magnitudes[(i * bars_per_point // 2) % len(magnitudes)]
            line_color = self.get_color_for_position(i * (self.num_bars // len(star_points)), segment_magnitude)

            cv2.line(frame, tuple(star_points[i]), tuple(star_points[next_i]),
                    line_color, 2, lineType=cv2.LINE_AA)

        # Add glow effect to star tips
        for i in range(0, len(star_points), 2):  # Only outer points
            point_magnitude = magnitudes[(i // 2 * bars_per_point) % len(magnitudes)]
            if point_magnitude > 0.6:
                glow_color = self.get_color_for_position(i * (self.num_bars // len(star_points)), point_magnitude)
                glow_color = tuple(int(c * 0.6) for c in glow_color)
                cv2.circle(frame, tuple(star_points[i]), 5, glow_color, -1, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_circular_spectrum(self, frame, magnitudes):
        """Draw the circular spectrum based on selected mode"""
        if self.mode == 1:
            return self.draw_mode_1_bars(frame, magnitudes)
        elif self.mode == 2:
            return self.draw_mode_2_waves(frame, magnitudes)
        elif self.mode == 3:
            return self.draw_mode_3_particles(frame, magnitudes)
        elif self.mode == 4:
            return self.draw_mode_4_waveform(frame, magnitudes)
        elif self.mode == 5:
            return self.draw_mode_5_polygon(frame, magnitudes)
        elif self.mode == 6:
            return self.draw_mode_6_spiral(frame, magnitudes)
        elif self.mode == 7:
            return self.draw_mode_7_dna_helix(frame, magnitudes)
        elif self.mode == 8:
            return self.draw_mode_8_kaleidoscope(frame, magnitudes)
        elif self.mode == 9:
            return self.draw_mode_9_pulse_rings(frame, magnitudes)
        elif self.mode == 10:
            return self.draw_mode_10_star_burst(frame, magnitudes)
        else:
            # Default to mode 1
            return self.draw_mode_1_bars(frame, magnitudes)

    def generate_video(self):
        """Generate the final video with transparent background"""
        print(f"Generating video: {self.output_path}")

        # Load audio
        self.load_audio()

        # Determine output format and codec based on file extension
        ext = Path(self.output_path).suffix.lower()

        # For transparency support, we'll create the video with WebM or MOV format
        # MP4 doesn't support alpha channel, so we'll use ffmpeg to create a proper transparent video

        # First, create a temporary video without transparency
        temp_no_audio = str(Path(self.output_path).with_suffix('')) + '_temp_no_audio.mp4'

        # Use mp4v codec for temporary file
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        # Create video writer
        video_writer = cv2.VideoWriter(
            temp_no_audio,
            fourcc,
            self.fps,
            (self.width, self.height),
            True
        )

        if not video_writer.isOpened():
            raise RuntimeError("Failed to open video writer")

        # Generate frames
        total_frames = int(self.duration * self.fps)

        for frame_idx in range(total_frames):
            # Create BGR frame (3 channels)
            frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)

            # Get frequency data for this frame
            audio_frame_idx = int(frame_idx * self.num_frames / total_frames)
            magnitudes = self.get_frequency_bands(audio_frame_idx)

            # Draw spectrum on the frame
            frame = self.draw_circular_spectrum(frame, magnitudes)

            # Write frame to video
            video_writer.write(frame)

            # Progress indicator
            if (frame_idx + 1) % 30 == 0 or frame_idx == total_frames - 1:
                progress = (frame_idx + 1) / total_frames * 100
                print(f"Progress: {progress:.1f}% ({frame_idx + 1}/{total_frames} frames)")

        video_writer.release()
        print(f"\nVideo generation complete (silent): {temp_no_audio}")

        # Now use ffmpeg to:
        # 1. Add audio
        # 2. Convert black pixels to transparent (using colorkey filter)
        # 3. Output to .mov with alpha channel
        print("Adding audio and transparency...")
        import subprocess

        try:
            # Always output to .mov since it supports transparency
            final_output = str(Path(self.output_path).with_suffix('.mov'))

            # Use ffmpeg to:
            # - Add audio
            # - Convert black (0,0,0) to transparent using colorkey filter
            # - Use ProRes 4444 codec which supports alpha channel
            result = subprocess.run([
                'ffmpeg', '-y',
                '-i', temp_no_audio,      # Video input
                '-i', self.audio_path,     # Audio input
                '-filter_complex',
                '[0:v]colorkey=0x000000:0.01:0.1[ckout];[ckout]format=yuva420p[video]',
                '-map', '[video]',         # Use filtered video
                '-map', '1:a',             # Use audio from second input
                '-c:v', 'prores_ks',       # ProRes codec with alpha support
                '-profile:v', '4444',      # ProRes 4444 profile (supports alpha)
                '-c:a', 'aac',             # AAC audio codec
                '-shortest',               # Match shortest stream
                final_output
            ], capture_output=True, text=True)

            # Clean up temp file
            Path(temp_no_audio).unlink()

            if result.returncode == 0:
                self.output_path = final_output
                print(f"✓ Video with transparency and audio created successfully")
                print(f"✓ Output: {final_output}")
            else:
                # Fallback: just add audio without transparency
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
        description='Generate circular audio spectrum visualization with transparent background',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # YouTube regular video (1920x1080, auto for .mov)
  python audio_spectrum.py input.mp3 output.mov

  # YouTube Shorts (1080x1920, auto for .mp4)
  python audio_spectrum.py input.mp3 output.mp4

  # With different visualization modes
  python audio_spectrum.py input.mp3 output.mov --mode 2
  python audio_spectrum.py input.mp3 output.mov --mode 3

  # Square format (1080x1080)
  python audio_spectrum.py song.wav video.mov --resolution square

  # Force Shorts format for .mov file
  python audio_spectrum.py audio.mp3 spectrum.mov --resolution shorts

  # Custom resolution (2000x2000)
  python audio_spectrum.py audio.mp3 spectrum.mov --resolution custom --width 2000 --height 2000

  # With color and bar customization
  python audio_spectrum.py audio.mp3 spectrum.mov --color 255 0 255 --num-bars 180 --no-gradient
        """
    )

    parser.add_argument('input', help='Input audio file (.mp3 or .wav)')
    parser.add_argument('output', help='Output video file (.mp4 or .mov recommended)')
    parser.add_argument('--mode', type=int, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default=1,
                       help='Visualization mode: 1=Bars (default), 2=Waves/Layers, 3=Particles, 4=Waveform, 5=Polygon, 6=Spiral, 7=DNA Helix, 8=Kaleidoscope, 9=Pulse Rings, 10=Star Burst')
    parser.add_argument('--resolution', type=str, choices=['square', 'shorts', 'hd', 'custom'],
                       default='auto',
                       help='Resolution preset: square (1080x1080), shorts (1080x1920 for YouTube Shorts), hd (1920x1080 for YouTube), custom (use --width/--height). Default: auto (.mov -> hd, .mp4 -> shorts)')
    parser.add_argument('--width', type=int, default=None, help='Video width (used with --resolution custom)')
    parser.add_argument('--height', type=int, default=None, help='Video height (used with --resolution custom)')
    parser.add_argument('--fps', type=int, default=30, help='Frames per second (default: 30)')
    parser.add_argument('--num-bars', type=int, default=120, help='Number of frequency bars (default: 120)')
    parser.add_argument('--color', nargs=3, type=int, default=[0, 255, 255],
                       metavar=('R', 'G', 'B'), help='RGB color for bars (used only with --no-gradient)')
    parser.add_argument('--no-gradient', action='store_true', help='Disable gradient mode (use single color)')
    parser.add_argument('--gradient-color1', nargs=3, type=int, default=[0, 180, 255],
                       metavar=('R', 'G', 'B'), help='Left side gradient color RGB (default: 0 180 255 = cyan)')
    parser.add_argument('--gradient-color2', nargs=3, type=int, default=[255, 0, 180],
                       metavar=('R', 'G', 'B'), help='Right side gradient color RGB (default: 255 0 180 = pink)')
    parser.add_argument('--inner-radius', type=int, default=150, help='Inner circle radius (default: 150)')
    parser.add_argument('--bar-width', type=float, default=1.5, help='Bar width multiplier (default: 1.5)')
    parser.add_argument('--smoothing', type=float, default=0.7, help='Smoothing factor 0-1 (default: 0.7)')

    args = parser.parse_args()

    # Validate input file
    if not Path(args.input).exists():
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)

    # Determine resolution based on preset or custom values
    resolution_presets = {
        'square': (1080, 1080),
        'shorts': (1080, 1920),
        'hd': (1920, 1080)
    }

    # Auto-detect resolution based on output file extension
    resolution = args.resolution
    if resolution == 'auto':
        ext = Path(args.output).suffix.lower()
        if ext == '.mov':
            resolution = 'hd'  # .mov -> 1920x1080 for YouTube regular videos
            print(f"Auto-detected resolution: hd (1920x1080) for .mov file")
        else:
            resolution = 'shorts'  # .mp4 -> 1080x1920 for YouTube Shorts
            print(f"Auto-detected resolution: shorts (1080x1920) for .mp4 file")

    if resolution == 'custom':
        if args.width is None or args.height is None:
            print("Error: --width and --height must be specified when using --resolution custom")
            sys.exit(1)
        width, height = args.width, args.height
    else:
        width, height = resolution_presets[resolution]
        if args.width is not None or args.height is not None:
            print(f"Warning: --width/--height ignored when using --resolution {resolution}")

    # Convert RGB to BGR for OpenCV
    color_bgr = (args.color[2], args.color[1], args.color[0])
    gradient_color1_bgr = (args.gradient_color1[2], args.gradient_color1[1], args.gradient_color1[0])
    gradient_color2_bgr = (args.gradient_color2[2], args.gradient_color2[1], args.gradient_color2[0])

    # Gradient is enabled by default unless --no-gradient is specified
    use_gradient = not args.no_gradient

    # Print selected mode
    mode_names = {
        1: "Bars (radial bars)",
        2: "Waves/Layers (concentric circular waves)",
        3: "Particles (particle rings with glow)",
        4: "Waveform (smooth continuous wave)",
        5: "Polygon (dynamic polygon morph)",
        6: "Spiral (hypnotic spiral arms)",
        7: "DNA Helix (double helix strands)",
        8: "Kaleidoscope (symmetrical mirrored patterns)",
        9: "Pulse Rings (expanding concentric rings)",
        10: "Star Burst (dynamic star points)"
    }
    print(f"Selected visualization mode: {args.mode} - {mode_names.get(args.mode, 'Unknown')}")

    # Create visualizer
    visualizer = CircularSpectrumVisualizer(
        audio_path=args.input,
        output_path=args.output,
        width=width,
        height=height,
        fps=args.fps,
        num_bars=args.num_bars,
        color=color_bgr,
        inner_radius=args.inner_radius,
        bar_width_multiplier=args.bar_width,
        smoothing=args.smoothing,
        gradient=use_gradient,
        gradient_color1=gradient_color1_bgr,
        gradient_color2=gradient_color2_bgr,
        mode=args.mode
    )

    # Generate video
    try:
        visualizer.generate_video()
        print("\nSuccess! Your circular audio spectrum video is ready.")
        print(f"Note: For true transparency in video editors, import the {args.output} file")
        print("      and enable 'preserve transparency' or use as a luma matte.")
    except Exception as e:
        print(f"\nError generating video: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

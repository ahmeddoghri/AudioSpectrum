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
    # Apple Design System - Minimal Color Palette (BGR format for OpenCV)
    PRIMARY_BLUE = (227, 113, 0)      # #0071e3 - vivid cool blue
    PRIMARY_ORANGE = (0, 122, 255)    # #ff7a00 - warm orange accent
    BG_SOFT_GRAY = (247, 245, 245)    # #f5f5f7 - soft neutral gray
    SURFACE_WHITE = (255, 255, 255)   # Pure white
    SURFACE_DARK = (16, 11, 11)       # #0b0b10 - deep slate
    TEXT_PRIMARY = (153, 153, 153)    # Muted gray for subtle elements
    TEXT_LIGHT = (255, 255, 255)      # White for dark backgrounds

    def __init__(self, audio_path, output_path, width=1080, height=1080,
                 fps=30, num_bars=72, color=None, inner_radius=180,
                 bar_width_multiplier=0.8, smoothing=0.85, gradient=True,
                 gradient_color1=None, gradient_color2=None, mode=1,
                 background_style='soft_gray'):
        """
        Initialize the circular spectrum visualizer with Apple minimalist design

        Args:
            audio_path: Path to input audio file (.mp3 or .wav)
            output_path: Path to output video file
            width: Video width in pixels
            height: Video height in pixels
            fps: Frames per second
            num_bars: Number of frequency bars (default: 72 for clean grid-like precision)
            color: RGB color tuple for the spectrum bars (default: PRIMARY_BLUE)
            inner_radius: Starting radius for the bars (default: 180 for more breathing room)
            bar_width_multiplier: Controls bar thickness (default: 0.8 for thinner, elegant bars)
            smoothing: Smoothing factor (0-1) for animation (default: 0.85 for fluid motion)
            gradient: Enable gradient mode (default: True)
            gradient_color1: Left side color (BGR format, default: PRIMARY_BLUE)
            gradient_color2: Right side color (BGR format, default: PRIMARY_ORANGE)
            mode: Visualization mode (1-10)
            background_style: Background style ('soft_gray', 'gradient', 'dark', 'transparent')
        """
        self.audio_path = audio_path
        self.output_path = output_path
        self.width = width
        self.height = height
        self.fps = fps
        self.num_bars = num_bars
        # Default to Apple PRIMARY_BLUE if no color specified
        self.color = color if color is not None else self.PRIMARY_BLUE
        self.inner_radius = inner_radius
        self.bar_width_multiplier = bar_width_multiplier
        self.smoothing = smoothing
        self.gradient = gradient
        # Default gradient: Apple blue to orange
        self.gradient_color1 = gradient_color1 if gradient_color1 is not None else self.PRIMARY_BLUE
        self.gradient_color2 = gradient_color2 if gradient_color2 is not None else self.PRIMARY_ORANGE
        self.mode = mode
        self.background_style = background_style

        self.center_x = width // 2
        self.center_y = height // 2
        self.max_radius = min(width, height) // 2 - 80  # 40% more padding for spacious minimalist look

        # For smoothing between frames
        self.prev_magnitudes = None

        # Animation frame counter for smooth effects
        self.frame_counter = 0

    @staticmethod
    def ease_out_cubic(t):
        """Apple-style cubic ease-out for smooth, natural deceleration"""
        return 1 - pow(1 - t, 3)

    @staticmethod
    def ease_in_out_cubic(t):
        """Apple-style cubic ease-in-out for balanced acceleration and deceleration"""
        return 4 * t * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 3) / 2

    @staticmethod
    def ease_out_expo(t):
        """Exponential ease-out for dramatic, premium deceleration"""
        return 1 if t == 1 else 1 - pow(2, -10 * t)

    def apply_saturation_reduction(self, color, reduction=0.3):
        """
        Reduce color saturation by specified amount for elegant, muted aesthetic

        Args:
            color: BGR color tuple
            reduction: Amount to reduce saturation (0-1), default 0.3 (30% reduction)

        Returns:
            Desaturated BGR color tuple
        """
        b, g, r = color
        # Convert to HSV for saturation control
        hsv = cv2.cvtColor(np.uint8([[[b, g, r]]]), cv2.COLOR_BGR2HSV)
        h, s, v = hsv[0][0]
        # Reduce saturation
        s = int(s * (1 - reduction))
        # Convert back to BGR
        bgr = cv2.cvtColor(np.uint8([[[h, s, v]]]), cv2.COLOR_HSV2BGR)
        return tuple(map(int, bgr[0][0]))

    def create_background(self):
        """
        Create Apple-inspired background with soft gradients and optional vignette

        Returns:
            Background frame with selected style
        """
        if self.background_style == 'transparent':
            # Pure black for transparency keying
            return np.zeros((self.height, self.width, 3), dtype=np.uint8)

        elif self.background_style == 'soft_gray':
            # Apple's soft neutral gray
            frame = np.full((self.height, self.width, 3), self.BG_SOFT_GRAY, dtype=np.uint8)
            # Add subtle vignette
            frame = self._apply_vignette(frame, strength=0.15)
            return frame

        elif self.background_style == 'gradient':
            # Subtle radial gradient from center
            frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
            center_y, center_x = self.center_y, self.center_x
            max_dist = np.sqrt(center_x**2 + center_y**2)

            for y in range(self.height):
                for x in range(self.width):
                    dist = np.sqrt((x - center_x)**2 + (y - center_y)**2)
                    t = min(dist / max_dist, 1.0)
                    # Smooth gradient from white to soft gray
                    for i in range(3):
                        frame[y, x, i] = int(self.SURFACE_WHITE[i] * (1 - t) + self.BG_SOFT_GRAY[i] * t)

            return frame

        elif self.background_style == 'dark':
            # Dark spotlight mode
            frame = np.full((self.height, self.width, 3), self.SURFACE_DARK, dtype=np.uint8)
            # Add soft vignette for focus
            frame = self._apply_vignette(frame, strength=0.3)
            return frame

        else:
            # Default to transparent
            return np.zeros((self.height, self.width, 3), dtype=np.uint8)

    def _apply_vignette(self, frame, strength=0.3):
        """
        Apply subtle vignette effect for edge darkening and focus

        Args:
            frame: Input frame
            strength: Vignette intensity (0-1), default 0.3

        Returns:
            Frame with vignette applied
        """
        rows, cols = frame.shape[:2]

        # Generate vignette mask
        kernel_x = cv2.getGaussianKernel(cols, cols * 0.35)
        kernel_y = cv2.getGaussianKernel(rows, rows * 0.35)
        kernel = kernel_y * kernel_x.T
        mask = kernel / kernel.max()

        # Apply vignette with specified strength
        vignette = np.ones_like(frame, dtype=np.float32)
        for i in range(3):
            vignette[:, :, i] = mask

        # Blend with strength parameter
        vignette = 1 - (1 - vignette) * strength

        return (frame * vignette).astype(np.uint8)

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
        """Get Apple-inspired minimalist color with sophisticated gradients and reduced saturation"""
        angle_step = 360 / self.num_bars

        if self.gradient and self.gradient_color1 and self.gradient_color2:
            # Calculate gradient position based on angle
            angle_normalized = (index * angle_step) / 360.0

            # Apple-style cubic ease-out for ultra-smooth color transitions
            blend = self.ease_out_cubic(angle_normalized)

            # Interpolate between colors with perceptual color mixing
            bar_color = (
                int(self.gradient_color1[0] * (1 - blend) + self.gradient_color2[0] * blend),
                int(self.gradient_color1[1] * (1 - blend) + self.gradient_color2[1] * blend),
                int(self.gradient_color1[2] * (1 - blend) + self.gradient_color2[2] * blend)
            )

            # Apple minimalist intensity: more subtle variation
            intensity_factor = 0.75 + (0.25 * magnitude)  # Subtle: 75-100%
            bar_color = (
                int(bar_color[0] * intensity_factor),
                int(bar_color[1] * intensity_factor),
                int(bar_color[2] * intensity_factor)
            )
        else:
            # Single color mode with Apple minimalist intensity
            base_intensity = 0.65 + (0.35 * magnitude * magnitude)  # Quadratic for smooth ramp
            bar_color = (
                int(self.color[0] * base_intensity),
                int(self.color[1] * base_intensity),
                int(self.color[2] * base_intensity)
            )

        # Apply 30% saturation reduction for elegant, muted Apple aesthetic
        bar_color = self.apply_saturation_reduction(bar_color, reduction=0.3)

        return bar_color

    def draw_center_circle(self, frame, magnitudes):
        """Draw Apple-minimalist center circle with subtle glow"""
        # Get average magnitude for reactive glow
        avg_magnitude = np.mean(magnitudes)

        # Apple muted color palette - using TEXT_PRIMARY for subtle elegance
        circle_color = self.TEXT_PRIMARY

        # Soft glow with Apple-style subtlety (fewer layers, more refined)
        glow_layers = 5  # Fewer layers for cleaner, more minimalist feel
        for i in range(glow_layers, 0, -1):
            # Exponential falloff for natural glow
            glow_alpha = 0.03 * (i / glow_layers) ** 2  # More subtle than before
            glow_radius = self.inner_radius + int(i * 2.5)
            glow_color = tuple(int(c * glow_alpha * (0.4 + 0.6 * avg_magnitude)) for c in circle_color)
            cv2.circle(frame, (self.center_x, self.center_y),
                      glow_radius, glow_color, 1, lineType=cv2.LINE_AA)

        # Minimal inner fill - very subtle
        inner_alpha = 0.08 + (0.06 * avg_magnitude)
        fill_color = tuple(int(c * inner_alpha) for c in circle_color)
        cv2.circle(frame, (self.center_x, self.center_y), self.inner_radius - 2,
                  fill_color, -1, lineType=cv2.LINE_AA)

        # Ultra-thin main stroke for refined Apple look
        stroke_intensity = 0.5 + 0.3 * avg_magnitude
        main_color = tuple(int(c * stroke_intensity) for c in circle_color)
        cv2.circle(frame, (self.center_x, self.center_y), self.inner_radius,
                  main_color, 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_1_bars(self, frame, magnitudes):
        """Mode 1: Apple-minimalist radial bars - thin, elegant, with soft glow"""
        angle_step = 360 / self.num_bars

        for i, magnitude in enumerate(magnitudes):
            angle = np.deg2rad(i * angle_step)

            # Apple-style cubic ease-out for smooth, natural motion
            min_bar_height = 2
            max_bar_height = self.max_radius - self.inner_radius
            # Use ease_out_cubic for premium Apple-quality animation
            eased = self.ease_out_cubic(magnitude)
            bar_height = int(eased * max_bar_height)
            bar_height = max(min_bar_height, bar_height)

            # Calculate positions
            start_x = int(self.center_x + self.inner_radius * np.cos(angle))
            start_y = int(self.center_y + self.inner_radius * np.sin(angle))
            end_x = int(self.center_x + (self.inner_radius + bar_height) * np.cos(angle))
            end_y = int(self.center_y + (self.inner_radius + bar_height) * np.sin(angle))

            # Thinner bars for Apple minimalist aesthetic (2px width)
            thickness = max(1, int(self.bar_width_multiplier * 2))

            # Get Apple-minimalist color with reduced saturation
            bar_color = self.get_color_for_position(i, magnitude)

            # Soft glow - Apple style (subtle, not aggressive)
            if magnitude > 0.2:
                # Single soft glow layer (5px blur)
                glow_color = tuple(int(c * 0.18) for c in bar_color)
                cv2.line(frame, (start_x, start_y), (end_x, end_y),
                        glow_color, thickness + 5, lineType=cv2.LINE_AA)

            # Main bar with antialiasing - single solid color
            cv2.line(frame, (start_x, start_y), (end_x, end_y),
                    bar_color, thickness, lineType=cv2.LINE_AA)

            # Rounded caps on bar ends (Apple aesthetic)
            if magnitude > 0.1:
                cap_radius = max(1, thickness // 2)
                cv2.circle(frame, (end_x, end_y), cap_radius,
                          bar_color, -1, lineType=cv2.LINE_AA)

        # Draw Apple-minimalist center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_2_waves(self, frame, magnitudes):
        """Mode 2: Apple-minimalist concentric waves - 3-4 thin strokes with high transparency"""
        num_layers = 3  # 3-4 layers maximum for cleaner look
        angle_step = 360 / self.num_bars

        for layer in range(num_layers):
            points = []
            layer_progress = (layer + 1) / (num_layers + 1)  # Distribute evenly

            for i, magnitude in enumerate(magnitudes):
                angle = np.deg2rad(i * angle_step)

                # Each layer has a different base radius and responds to audio
                base_radius = self.inner_radius + (self.max_radius - self.inner_radius) * layer_progress
                # Apple-style easing for gentle pulsing
                eased_magnitude = self.ease_out_cubic(magnitude)
                wave_amplitude = eased_magnitude * (self.max_radius - self.inner_radius) * 0.06  # More subtle
                radius = int(base_radius + wave_amplitude)

                x = int(self.center_x + radius * np.cos(angle))
                y = int(self.center_y + radius * np.sin(angle))
                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            # Get color for this layer
            avg_magnitude = np.mean(magnitudes)
            layer_color = self.get_color_for_position(layer * (self.num_bars // num_layers), avg_magnitude)

            # High transparency (30-50%) for elegant, layered look
            alpha = 0.45 - (layer * 0.1)
            layer_color = tuple(int(c * alpha) for c in layer_color)

            # Thin strokes (1-2px)
            thickness = 1 if layer > 0 else 2

            # Gentle pulsing - no aggressive glow
            cv2.polylines(frame, [points], isClosed=True, color=layer_color,
                         thickness=thickness, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_3_particles(self, frame, magnitudes):
        """Mode 3: Apple-minimalist particle system - smaller, lower opacity, soft blur"""
        angle_step = 360 / self.num_bars

        for i, magnitude in enumerate(magnitudes):
            angle = np.deg2rad(i * angle_step)

            # Apple-style easing for smooth, natural motion
            max_bar_height = self.max_radius - self.inner_radius
            eased = self.ease_out_cubic(magnitude)
            bar_height = int(eased * max_bar_height)
            radius = self.inner_radius + bar_height

            x = int(self.center_x + radius * np.cos(angle))
            y = int(self.center_y + radius * np.sin(angle))

            # Smaller particles (2-4px radius) for minimalist aesthetic
            particle_size = max(2, int(2 + 2 * magnitude))

            # Get Apple-minimalist color
            particle_color = self.get_color_for_position(i, magnitude)

            # Lower opacity (40-60%)
            opacity = 0.4 + (0.2 * magnitude)
            particle_color = tuple(int(c * opacity) for c in particle_color)

            # Soft blur - minimal bloom layers
            if magnitude > 0.25:
                bloom_layers = 3  # Fewer layers for subtlety
                for layer in range(bloom_layers, 0, -1):
                    # Soft falloff
                    bloom_alpha = 0.06 * (layer / bloom_layers) ** 2
                    bloom_size = particle_size + int(layer * 1.5)
                    bloom_color = tuple(int(c * bloom_alpha) for c in particle_color)
                    cv2.circle(frame, (x, y), bloom_size, bloom_color, -1, lineType=cv2.LINE_AA)

            # Main particle with soft rendering
            cv2.circle(frame, (x, y), particle_size, particle_color, -1, lineType=cv2.LINE_AA)

        # Draw Apple-minimalist center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_4_waveform(self, frame, magnitudes):
        """Mode 4: Apple-minimalist waveform - single smooth continuous line with 2px stroke"""
        angle_step = 360 / self.num_bars
        points_outer = []

        for i, magnitude in enumerate(magnitudes):
            angle = np.deg2rad(i * angle_step)

            # Apple-style easing for ultra-smooth curves
            max_bar_height = self.max_radius - self.inner_radius
            eased = self.ease_out_cubic(magnitude)
            bar_height = int(eased * max_bar_height)
            radius = self.inner_radius + bar_height

            x = int(self.center_x + radius * np.cos(angle))
            y = int(self.center_y + radius * np.sin(angle))
            points_outer.append([x, y])

        points_outer = np.array(points_outer, dtype=np.int32)

        # Get average color for the entire waveform
        avg_magnitude = np.mean(magnitudes)
        line_color = self.get_color_for_position(0, avg_magnitude)

        # Soft drop shadow beneath the line (Apple aesthetic)
        shadow_color = tuple(int(c * 0.12) for c in line_color)
        cv2.polylines(frame, [points_outer], isClosed=True, color=shadow_color,
                     thickness=6, lineType=cv2.LINE_AA)

        # Main line - elegant 2px stroke weight
        cv2.polylines(frame, [points_outer], isClosed=True, color=line_color,
                     thickness=2, lineType=cv2.LINE_AA)

        # Draw Apple-minimalist center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_5_polygon(self, frame, magnitudes):
        """Mode 5: Apple-minimalist morphing polygon - Clean, refined geometry"""
        # Fewer points for cleaner, more defined geometry
        polygon_points = 18  # Reduced for cleaner shapes
        step = self.num_bars // polygon_points
        angle_step = 360 / polygon_points

        points = []
        for i in range(polygon_points):
            angle = np.deg2rad(i * angle_step)

            # Get magnitude for this section with smooth averaging
            mag_idx = i * step
            magnitude = np.mean(magnitudes[mag_idx:mag_idx + step]) if mag_idx < len(magnitudes) else magnitudes[-1]

            # Apple-style easing for smooth motion
            max_bar_height = self.max_radius - self.inner_radius
            eased_magnitude = self.ease_out_cubic(magnitude)
            bar_height = int(eased_magnitude * max_bar_height)
            radius = self.inner_radius + bar_height

            x = int(self.center_x + radius * np.cos(angle))
            y = int(self.center_y + radius * np.sin(angle))
            points.append([x, y])

        points = np.array(points, dtype=np.int32)

        # Minimal concentric polygons (2 layers only)
        num_layers = 2
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

            # Thin strokes and high transparency
            thickness = 2 if layer == 1 else 1
            alpha = 0.55 - (layer * 0.15)
            layer_color = tuple(int(c * alpha) for c in layer_color)

            # Draw clean lines without glow
            cv2.polylines(frame, [layer_points], isClosed=True, color=layer_color,
                         thickness=thickness, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_6_spiral(self, frame, magnitudes):
        """Mode 6: Apple-minimalist spiral - Clean flowing curves"""
        num_arms = 3  # Fewer arms for cleaner, more minimal look
        angle_step = 360 / self.num_bars

        for arm in range(num_arms):
            points = []
            arm_offset = (360 / num_arms) * arm

            for i, magnitude in enumerate(magnitudes):
                angle = np.deg2rad(i * angle_step + arm_offset)

                # Create smooth spiral with Apple easing
                progress = i / self.num_bars
                max_bar_height = self.max_radius - self.inner_radius

                # Gentle spiral outward
                spiral_radius = self.inner_radius + (progress * max_bar_height * 0.7)
                # Apple-style easing for subtle magnitude variation
                eased_magnitude = self.ease_out_cubic(magnitude)
                radius_variation = eased_magnitude * max_bar_height * 0.2  # More subtle
                radius = int(spiral_radius + radius_variation)

                x = int(self.center_x + radius * np.cos(angle))
                y = int(self.center_y + radius * np.sin(angle))
                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            # Get color for this arm
            avg_magnitude = np.mean(magnitudes)
            arm_color = self.get_color_for_position(arm * (self.num_bars // num_arms), avg_magnitude)

            # Draw spiral with elegant tapering - no glow for minimalism
            for i in range(len(points) - 1):
                thickness = max(1, int(2 - (i / len(points)) * 0.8))  # Subtle taper

                # Main line only - clean Apple aesthetic
                cv2.line(frame, tuple(points[i]), tuple(points[i + 1]),
                        arm_color, thickness, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_7_dna_helix(self, frame, magnitudes):
        """Mode 7: Apple-minimalist DNA helix - Clean intertwined strands"""
        angle_step = 360 / self.num_bars
        max_bar_height = self.max_radius - self.inner_radius

        # More subtle wave for Apple minimalism
        wave_amplitude = max_bar_height * 0.06

        # Two strands
        for strand in range(2):
            points = []
            strand_phase = strand * np.pi

            for i, magnitude in enumerate(magnitudes):
                angle = np.deg2rad(i * angle_step)

                # Smooth helix pattern with Apple easing
                progress = i / self.num_bars
                wave_offset = np.sin(progress * 4 * np.pi + strand_phase) * wave_amplitude

                base_radius = self.inner_radius + max_bar_height * 0.5
                eased_magnitude = self.ease_out_cubic(magnitude)
                radius_variation = eased_magnitude * max_bar_height * 0.12  # More subtle
                radius = int(base_radius + wave_offset + radius_variation)

                x = int(self.center_x + radius * np.cos(angle))
                y = int(self.center_y + radius * np.sin(angle))
                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            # Get color for strand
            avg_magnitude = np.mean(magnitudes)
            strand_color = self.get_color_for_position(strand * self.num_bars // 2, avg_magnitude)

            # Thin strand line - no glow for minimalism
            cv2.polylines(frame, [points], isClosed=True, color=strand_color,
                         thickness=2, lineType=cv2.LINE_AA)

            # Fewer, more minimal connecting rungs
            if strand == 1:
                for i in range(0, len(points), 20):  # Fewer rungs
                    opposite_angle = np.deg2rad((i + self.num_bars // 2) * angle_step)

                    progress = i / self.num_bars
                    wave_offset_2 = np.sin(progress * 4 * np.pi) * wave_amplitude

                    magnitude_2 = magnitudes[(i + self.num_bars // 2) % len(magnitudes)]
                    eased_mag_2 = self.ease_out_cubic(magnitude_2)
                    base_radius = self.inner_radius + max_bar_height * 0.5
                    radius_2 = int(base_radius + wave_offset_2 + eased_mag_2 * max_bar_height * 0.12)

                    x2 = int(self.center_x + radius_2 * np.cos(opposite_angle))
                    y2 = int(self.center_y + radius_2 * np.sin(opposite_angle))

                    rung_color = self.get_color_for_position(i, magnitudes[i])
                    rung_color = tuple(int(c * 0.25) for c in rung_color)  # More subtle
                    cv2.line(frame, tuple(points[i]), (x2, y2), rung_color, 1, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_8_kaleidoscope(self, frame, magnitudes):
        """Mode 8: Apple-minimalist kaleidoscope - Clean radial symmetry"""
        num_segments = 6  # Clean hexagonal symmetry
        segment_angle = 360 / num_segments
        angle_step = 360 / self.num_bars
        bars_per_segment = self.num_bars // num_segments

        for segment in range(num_segments):
            segment_offset = segment * segment_angle

            # Draw elegant mirrored pattern
            for i in range(bars_per_segment):
                magnitude = magnitudes[i % len(magnitudes)]

                # Forward and mirrored directions
                angle1 = np.deg2rad(segment_offset + (i * angle_step))
                angle2 = np.deg2rad(segment_offset + segment_angle - (i * angle_step))

                max_bar_height = self.max_radius - self.inner_radius
                eased_magnitude = self.ease_out_cubic(magnitude)
                bar_height = int(eased_magnitude * max_bar_height)
                radius = self.inner_radius + bar_height

                # Forward point
                x1 = int(self.center_x + radius * np.cos(angle1))
                y1 = int(self.center_y + radius * np.sin(angle1))

                # Mirrored point
                x2 = int(self.center_x + radius * np.cos(angle2))
                y2 = int(self.center_y + radius * np.sin(angle2))

                # Get color
                bar_color = self.get_color_for_position(segment * bars_per_segment + i, magnitude)

                # Inner points
                inner_x1 = int(self.center_x + self.inner_radius * np.cos(angle1))
                inner_y1 = int(self.center_y + self.inner_radius * np.sin(angle1))
                inner_x2 = int(self.center_x + self.inner_radius * np.cos(angle2))
                inner_y2 = int(self.center_y + self.inner_radius * np.sin(angle2))

                # Thin lines for Apple minimalist aesthetic
                thickness = max(1, int(self.bar_width_multiplier * 1.5))

                # No glow - clean Apple aesthetic
                cv2.line(frame, (inner_x1, inner_y1), (x1, y1), bar_color, thickness, lineType=cv2.LINE_AA)
                cv2.line(frame, (inner_x2, inner_y2), (x2, y2), bar_color, thickness, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_9_pulse_rings(self, frame, magnitudes):
        """Mode 9: Apple-minimalist pulse rings - Clean concentric circles"""
        # Fewer rings for Apple minimalism
        num_rings = 6
        bars_per_ring = self.num_bars // num_rings
        max_bar_height = self.max_radius - self.inner_radius

        # More subtle pulse for Apple aesthetic
        max_pulse = max_bar_height * 0.04

        for ring_idx in range(num_rings):
            # Calculate average magnitude for this ring
            start_idx = ring_idx * bars_per_ring
            end_idx = start_idx + bars_per_ring
            ring_magnitude = np.mean(magnitudes[start_idx:end_idx])

            # Ring positioning
            ring_progress = (ring_idx + 1) / (num_rings + 1)
            base_radius = self.inner_radius + (ring_progress * max_bar_height)

            # Apple-style easing for smooth pulse
            eased_magnitude = self.ease_out_cubic(ring_magnitude)
            pulse_expansion = eased_magnitude * max_pulse
            radius = int(base_radius + pulse_expansion)

            # Get color
            ring_color = self.get_color_for_position(start_idx, ring_magnitude)

            # Thin, consistent line thickness
            thickness = 1

            # High transparency for layered look
            alpha = 0.5 - (ring_progress * 0.15)
            ring_color = tuple(int(c * alpha) for c in ring_color)

            # No glow - clean Apple aesthetic
            cv2.circle(frame, (self.center_x, self.center_y), radius, ring_color,
                      thickness, lineType=cv2.LINE_AA)

        # Draw center circle
        self.draw_center_circle(frame, magnitudes)

        return frame

    def draw_mode_10_star_burst(self, frame, magnitudes):
        """Mode 10: Apple-minimalist star burst - Clean geometric star"""
        num_points = 8  # Fewer points for cleaner, more minimal star
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

            # Outer points with Apple easing
            max_bar_height = self.max_radius - self.inner_radius
            eased_magnitude = self.ease_out_cubic(point_magnitude)
            bar_height = int(eased_magnitude * max_bar_height)
            outer_radius = self.inner_radius + bar_height

            x_outer = int(self.center_x + outer_radius * np.cos(angle))
            y_outer = int(self.center_y + outer_radius * np.sin(angle))
            star_points_outer.append([x_outer, y_outer])

            # Inner points with subtle variation
            inner_angle = np.deg2rad((point_idx * angle_step) + (angle_step / 2))
            inner_magnitude = magnitudes[(start_idx + bars_per_point // 2) % len(magnitudes)]
            eased_inner = self.ease_out_cubic(inner_magnitude)
            inner_radius = int(self.inner_radius + (eased_inner * max_bar_height * 0.3))

            x_inner = int(self.center_x + inner_radius * np.cos(inner_angle))
            y_inner = int(self.center_y + inner_radius * np.sin(inner_angle))
            star_points_inner.append([x_inner, y_inner])

        # Interleave outer and inner points
        star_points = []
        for i in range(num_points):
            star_points.append(star_points_outer[i])
            star_points.append(star_points_inner[i])

        star_points = np.array(star_points, dtype=np.int32)

        # Minimal fill - very subtle
        avg_magnitude = np.mean(magnitudes)
        fill_color = self.get_color_for_position(0, avg_magnitude)
        fill_color = tuple(int(c * 0.25) for c in fill_color)
        cv2.fillPoly(frame, [star_points], fill_color, lineType=cv2.LINE_AA)

        # Clean outline - no glow
        for i in range(len(star_points)):
            next_i = (i + 1) % len(star_points)
            segment_magnitude = magnitudes[(i * bars_per_point // 2) % len(magnitudes)]
            line_color = self.get_color_for_position(i * (self.num_bars // len(star_points)), segment_magnitude)

            # Thin main line only
            cv2.line(frame, tuple(star_points[i]), tuple(star_points[next_i]),
                    line_color, 1, lineType=cv2.LINE_AA)

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
            # Create frame with Apple-minimalist background
            frame = self.create_background()

            # Get frequency data for this frame
            audio_frame_idx = int(frame_idx * self.num_frames / total_frames)
            magnitudes = self.get_frequency_bands(audio_frame_idx)

            # Draw spectrum on the frame
            frame = self.draw_circular_spectrum(frame, magnitudes)

            # Apply final rendering optimizations for Apple aesthetic
            # Subtle blur for smoothness (0.5 sigma for very gentle effect)
            frame = cv2.GaussianBlur(frame, (3, 3), 0.5)

            # Increment frame counter for animations
            self.frame_counter += 1

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
    parser.add_argument('--num-bars', type=int, default=72, help='Number of frequency bars (default: 72 for clean Apple aesthetic)')
    parser.add_argument('--color', nargs=3, type=int, default=None,
                       metavar=('R', 'G', 'B'), help='RGB color for bars (default: Apple PRIMARY_BLUE #0071e3)')
    parser.add_argument('--no-gradient', action='store_true', help='Disable gradient mode (gradient enabled by default)')
    parser.add_argument('--gradient-color1', nargs=3, type=int, default=None,
                       metavar=('R', 'G', 'B'), help='Left side gradient color RGB (default: Apple PRIMARY_BLUE #0071e3)')
    parser.add_argument('--gradient-color2', nargs=3, type=int, default=None,
                       metavar=('R', 'G', 'B'), help='Right side gradient color RGB (default: Apple PRIMARY_ORANGE #ff7a00)')
    parser.add_argument('--inner-radius', type=int, default=180, help='Inner circle radius (default: 180 for more breathing room)')
    parser.add_argument('--bar-width', type=float, default=0.8, help='Bar width multiplier (default: 0.8 for thinner, elegant bars)')
    parser.add_argument('--smoothing', type=float, default=0.85, help='Smoothing factor 0-1 (default: 0.85 for fluid Apple motion)')
    parser.add_argument('--background', type=str, choices=['soft_gray', 'gradient', 'dark', 'transparent'],
                       default='soft_gray', help='Background style (default: soft_gray for Apple aesthetic)')

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

    # Convert RGB to BGR for OpenCV (handle None defaults for Apple colors)
    color_bgr = None
    if args.color is not None:
        color_bgr = (args.color[2], args.color[1], args.color[0])

    gradient_color1_bgr = None
    if args.gradient_color1 is not None:
        gradient_color1_bgr = (args.gradient_color1[2], args.gradient_color1[1], args.gradient_color1[0])

    gradient_color2_bgr = None
    if args.gradient_color2 is not None:
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

    # Create visualizer with Apple-minimalist design
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
        mode=args.mode,
        background_style=args.background
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

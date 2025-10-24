#!/usr/bin/env python3
"""
Image-Based Audio Spectrum Visualizer
Generates creative audio spectrum animations that are driven by an input image.
The image's colors, brightness, and structure influence the visual output.

Visualization Modes:
  --mode 1: Image Particles - Pixels from image explode and react to audio
  --mode 2: Color Wave - Image colors ripple outward in waves synced to music
  --mode 3: Pixel Fountain - Image pixels fountain up from bottom, height based on spectrum
  --mode 4: Image Shatter - Image breaks into shards that dance to frequencies
  --mode 5: Chromatic Rings - Concentric rings colored by image pixels
  --mode 6: Image Mosaic - Image tiles rearrange themselves rhythmically
  --mode 7: Spectrum Paint - Paint strokes using image colors
  --mode 8: Photo Prism - Image refracted through prism effect
  --mode 9: Pixel Vortex - Image pixels spiral into vortex
  --mode 10: Color Trails - Particles leave trails in image colors

Examples:
  python audio_spectrum_image.py input.wav output.mov --image photo.jpg --mode 1
  python audio_spectrum_image.py input.wav output.mov --image logo.png --mode 5 --width 1920 --height 1080
"""

import sys
import numpy as np
import cv2
import librosa
import argparse
from pathlib import Path
from typing import List, Tuple


class ImageSpectrumVisualizer:
    def __init__(self, audio_path, output_path, image_path, width=1920, height=1080,
                 fps=30, num_bars=120, smoothing=0.7, mode=1):
        """
        Initialize the image-based spectrum visualizer

        Args:
            audio_path: Path to input audio file
            output_path: Path to output video file
            image_path: Path to input image file
            width: Video width in pixels
            height: Video height in pixels
            fps: Frames per second
            num_bars: Number of frequency bars/elements
            smoothing: Smoothing factor (0-1) for animation
            mode: Visualization mode (1-10)
        """
        self.audio_path = audio_path
        self.output_path = output_path
        self.image_path = image_path
        self.width = width
        self.height = height
        self.fps = fps
        self.num_bars = num_bars
        self.smoothing = smoothing
        self.mode = mode

        self.center_x = width // 2
        self.center_y = height // 2

        # Load and resize the image to match output dimensions
        self.source_image = self._load_image()

        # For smoothing between frames
        self.prev_magnitudes = None

        # Mode-specific state
        self.particles = []
        self.shards = []
        self.fountain_particles = []
        self.mosaic_tiles = []
        self.paint_strokes = []
        self.vortex_particles = []
        self.trail_particles = []
        self.frame_counter = 0

    def _load_image(self):
        """Load and resize the input image"""
        img = cv2.imread(self.image_path, cv2.IMREAD_UNCHANGED)
        if img is None:
            raise ValueError(f"Could not load image: {self.image_path}")

        # Add alpha channel if not present
        if len(img.shape) == 2:  # Grayscale
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGRA)
        elif img.shape[2] == 3:  # BGR
            img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

        # Resize to match output dimensions
        img = cv2.resize(img, (self.width, self.height), interpolation=cv2.INTER_LANCZOS4)

        return img

    def _get_color_at(self, x, y):
        """Get color from source image at normalized coordinates (0-1)"""
        img_x = int(np.clip(x, 0, 1) * (self.width - 1))
        img_y = int(np.clip(y, 0, 1) * (self.height - 1))
        color = self.source_image[img_y, img_x]
        return tuple(map(int, color))

    def _get_color_at_pixel(self, x, y):
        """Get color from source image at pixel coordinates"""
        x = int(np.clip(x, 0, self.width - 1))
        y = int(np.clip(y, 0, self.height - 1))
        color = self.source_image[y, x]
        return tuple(map(int, color))

    def load_audio(self):
        """Load and process audio file"""
        print(f"Loading audio from {self.audio_path}...")
        y, sr = librosa.load(self.audio_path, sr=None)

        # Calculate duration
        duration = len(y) / sr
        total_frames = int(duration * self.fps)

        print(f"Audio duration: {duration:.2f}s, Sample rate: {sr}Hz")
        print(f"Generating {total_frames} frames at {self.fps}fps...")

        # Compute STFT
        hop_length = len(y) // total_frames
        if hop_length == 0:
            hop_length = 512

        D = np.abs(librosa.stft(y, hop_length=hop_length, n_fft=2048))

        # Convert to dB scale
        db = librosa.amplitude_to_db(D, ref=np.max)

        return db, total_frames, y, sr

    def render_mode_1_image_particles(self, frame, magnitudes):
        """Mode 1: Image Particles - Pixels explode and react to audio"""
        # Initialize particles if needed
        if len(self.particles) < 500:
            for _ in range(500 - len(self.particles)):
                x = np.random.randint(0, self.width)
                y = np.random.randint(0, self.height)
                color = self._get_color_at_pixel(x, y)
                vx = np.random.uniform(-2, 2)
                vy = np.random.uniform(-2, 2)
                self.particles.append({
                    'x': x, 'y': y, 'vx': vx, 'vy': vy,
                    'color': color, 'size': 3, 'life': 1.0
                })

        # Energy from audio
        energy = np.mean(magnitudes) / 100.0

        # Update and draw particles
        for particle in self.particles:
            # Apply audio energy as force
            force_scale = energy * 5
            particle['vx'] += np.random.uniform(-force_scale, force_scale)
            particle['vy'] += np.random.uniform(-force_scale, force_scale)

            # Damping
            particle['vx'] *= 0.95
            particle['vy'] *= 0.95

            # Update position
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']

            # Bounce off edges
            if particle['x'] < 0 or particle['x'] >= self.width:
                particle['vx'] *= -0.8
                particle['x'] = np.clip(particle['x'], 0, self.width - 1)
            if particle['y'] < 0 or particle['y'] >= self.height:
                particle['vy'] *= -0.8
                particle['y'] = np.clip(particle['y'], 0, self.height - 1)

            # Update color based on current position
            particle['color'] = self._get_color_at_pixel(particle['x'], particle['y'])

            # Draw particle with glow
            size = int(particle['size'] + energy * 3)
            cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                      size, particle['color'], -1, cv2.LINE_AA)

    def render_mode_2_color_wave(self, frame, magnitudes):
        """Mode 2: Color Wave - Image colors ripple outward synced to music"""
        energy = np.mean(magnitudes) / 100.0

        # Create expanding rings
        num_rings = 8
        for i in range(num_rings):
            phase = (self.frame_counter * 0.05 + i * 0.3) % (2 * np.pi)
            radius = int(100 + energy * 200 + i * 80 + np.sin(phase) * 50)

            if radius > 0 and radius < max(self.width, self.height):
                # Sample color from image at ring position
                angle_samples = 64
                for j in range(angle_samples):
                    angle = (j / angle_samples) * 2 * np.pi
                    x = int(self.center_x + radius * np.cos(angle))
                    y = int(self.center_y + radius * np.sin(angle))

                    if 0 <= x < self.width and 0 <= y < self.height:
                        # Get magnitude for this angle
                        mag_idx = int((j / angle_samples) * len(magnitudes))
                        mag = magnitudes[mag_idx] / 100.0

                        color = self._get_color_at_pixel(x, y)
                        thickness = int(5 + mag * 10)

                        # Draw segment
                        next_j = (j + 1) % angle_samples
                        next_angle = (next_j / angle_samples) * 2 * np.pi
                        x2 = int(self.center_x + radius * np.cos(next_angle))
                        y2 = int(self.center_y + radius * np.sin(next_angle))

                        cv2.line(frame, (x, y), (x2, y2), color, thickness, cv2.LINE_AA)

    def render_mode_3_pixel_fountain(self, frame, magnitudes):
        """Mode 3: Pixel Fountain - Image pixels fountain up, height based on spectrum"""
        # Spawn new fountain particles at bottom
        if self.frame_counter % 2 == 0:
            for i in range(20):
                x = np.random.randint(0, self.width)
                color = self._get_color_at_pixel(x, self.height - 1)

                mag_idx = int((x / self.width) * len(magnitudes))
                velocity = 5 + (magnitudes[mag_idx] / 100.0) * 20

                self.fountain_particles.append({
                    'x': x,
                    'y': self.height - 1,
                    'vx': np.random.uniform(-1, 1),
                    'vy': -velocity,
                    'color': color,
                    'life': 1.0
                })

        # Update and draw fountain particles
        particles_to_keep = []
        for particle in self.fountain_particles:
            particle['vy'] += 0.5  # Gravity
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.01

            if particle['life'] > 0 and particle['y'] < self.height:
                # Update color based on position
                if 0 <= particle['x'] < self.width and 0 <= particle['y'] < self.height:
                    particle['color'] = self._get_color_at_pixel(particle['x'], particle['y'])

                    # Draw with fade
                    alpha = int(particle['life'] * 255)
                    color = list(particle['color'])
                    color[3] = alpha

                    cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                              3, tuple(color), -1, cv2.LINE_AA)

                    particles_to_keep.append(particle)

        self.fountain_particles = particles_to_keep

    def render_mode_4_image_shatter(self, frame, magnitudes):
        """Mode 4: Image Shatter - Image breaks into shards that dance"""
        shard_size = 40
        energy = np.mean(magnitudes) / 100.0

        # Create shards if needed
        if len(self.shards) == 0:
            for y in range(0, self.height, shard_size):
                for x in range(0, self.width, shard_size):
                    self.shards.append({
                        'orig_x': x,
                        'orig_y': y,
                        'x': x,
                        'y': y,
                        'rotation': 0,
                        'phase': np.random.random() * 2 * np.pi
                    })

        # Update and draw shards
        for shard in self.shards:
            # Oscillate based on audio
            offset_x = np.sin(self.frame_counter * 0.1 + shard['phase']) * energy * 30
            offset_y = np.cos(self.frame_counter * 0.1 + shard['phase']) * energy * 30

            shard['x'] = shard['orig_x'] + offset_x
            shard['y'] = shard['orig_y'] + offset_y
            shard['rotation'] = energy * 15 * np.sin(self.frame_counter * 0.05 + shard['phase'])

            # Extract and rotate shard from source image
            x1 = max(0, min(int(shard['orig_x']), self.width - shard_size))
            y1 = max(0, min(int(shard['orig_y']), self.height - shard_size))
            x2 = min(x1 + shard_size, self.width)
            y2 = min(y1 + shard_size, self.height)

            shard_img = self.source_image[y1:y2, x1:x2].copy()

            # Rotate shard
            if shard_img.size > 0:
                M = cv2.getRotationMatrix2D(
                    (shard_img.shape[1] // 2, shard_img.shape[0] // 2),
                    shard['rotation'], 1.0
                )
                rotated = cv2.warpAffine(shard_img, M, (shard_img.shape[1], shard_img.shape[0]),
                                        flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT,
                                        borderValue=(0, 0, 0, 0))

                # Place shard on frame
                dest_x = int(shard['x'])
                dest_y = int(shard['y'])

                if 0 <= dest_x < self.width - rotated.shape[1] and 0 <= dest_y < self.height - rotated.shape[0]:
                    # Alpha blend
                    alpha = rotated[:, :, 3] / 255.0
                    for c in range(3):
                        frame[dest_y:dest_y + rotated.shape[0], dest_x:dest_x + rotated.shape[1], c] = \
                            frame[dest_y:dest_y + rotated.shape[0], dest_x:dest_x + rotated.shape[1], c] * (1 - alpha) + \
                            rotated[:, :, c] * alpha

    def render_mode_5_chromatic_rings(self, frame, magnitudes):
        """Mode 5: Chromatic Rings - Concentric rings colored by image pixels"""
        num_rings = min(len(magnitudes), 60)

        for i in range(num_rings):
            mag = magnitudes[i]
            radius = int(50 + i * 15 + (mag / 100.0) * 30)

            # Sample color from image in a circular pattern
            angle_for_color = (i / num_rings) * 2 * np.pi
            sample_x = 0.5 + 0.4 * np.cos(angle_for_color)
            sample_y = 0.5 + 0.4 * np.sin(angle_for_color)
            color = self._get_color_at(sample_x, sample_y)

            thickness = int(3 + (mag / 100.0) * 8)
            cv2.circle(frame, (self.center_x, self.center_y), radius, color, thickness, cv2.LINE_AA)

    def render_mode_6_image_mosaic(self, frame, magnitudes):
        """Mode 6: Image Mosaic - Image tiles rearrange rhythmically"""
        tile_size = 60
        energy = np.mean(magnitudes) / 100.0

        for y in range(0, self.height, tile_size):
            for x in range(0, self.width, tile_size):
                # Calculate tile offset based on audio and position
                tile_idx = (y // tile_size) * (self.width // tile_size) + (x // tile_size)
                mag_idx = tile_idx % len(magnitudes)

                offset_scale = magnitudes[mag_idx] / 100.0
                offset_x = np.sin(self.frame_counter * 0.1 + tile_idx * 0.1) * offset_scale * 20
                offset_y = np.cos(self.frame_counter * 0.1 + tile_idx * 0.1) * offset_scale * 20

                # Extract tile
                x1 = max(0, x)
                y1 = max(0, y)
                x2 = min(x + tile_size, self.width)
                y2 = min(y + tile_size, self.height)

                tile = self.source_image[y1:y2, x1:x2].copy()

                # Place tile at offset position
                dest_x = int(x + offset_x)
                dest_y = int(y + offset_y)

                if (0 <= dest_x < self.width - tile.shape[1] and
                    0 <= dest_y < self.height - tile.shape[0]):
                    # Alpha blend
                    alpha = tile[:, :, 3:4] / 255.0
                    frame[dest_y:dest_y + tile.shape[0], dest_x:dest_x + tile.shape[1], :3] = \
                        frame[dest_y:dest_y + tile.shape[0], dest_x:dest_x + tile.shape[1], :3] * (1 - alpha) + \
                        tile[:, :, :3] * alpha

    def render_mode_7_spectrum_paint(self, frame, magnitudes):
        """Mode 7: Spectrum Paint - Paint strokes using image colors"""
        # Add new paint strokes
        if self.frame_counter % 3 == 0:
            for i in range(10):
                angle = (i / 10) * 2 * np.pi
                mag_idx = int((i / 10) * len(magnitudes))
                distance = 100 + (magnitudes[mag_idx] / 100.0) * 300

                x = self.center_x + distance * np.cos(angle)
                y = self.center_y + distance * np.sin(angle)

                if 0 <= x < self.width and 0 <= y < self.height:
                    color = self._get_color_at_pixel(x, y)

                    self.paint_strokes.append({
                        'x': x, 'y': y,
                        'vx': np.cos(angle) * 2,
                        'vy': np.sin(angle) * 2,
                        'color': color,
                        'life': 1.0,
                        'thickness': int(5 + (magnitudes[mag_idx] / 100.0) * 10)
                    })

        # Update and draw strokes
        strokes_to_keep = []
        for stroke in self.paint_strokes:
            stroke['x'] += stroke['vx']
            stroke['y'] += stroke['vy']
            stroke['vx'] *= 0.98
            stroke['vy'] *= 0.98
            stroke['life'] -= 0.005

            if stroke['life'] > 0:
                color = list(stroke['color'])
                color[3] = int(stroke['life'] * 255)

                if 0 <= stroke['x'] < self.width and 0 <= stroke['y'] < self.height:
                    cv2.circle(frame, (int(stroke['x']), int(stroke['y'])),
                              stroke['thickness'], tuple(color), -1, cv2.LINE_AA)
                    strokes_to_keep.append(stroke)

        self.paint_strokes = strokes_to_keep

    def render_mode_8_photo_prism(self, frame, magnitudes):
        """Mode 8: Photo Prism - Image refracted through prism effect"""
        energy = np.mean(magnitudes) / 100.0

        # Create RGB separation effect
        offset = int(energy * 20)

        # Red channel shift
        if offset > 0:
            frame[:-offset, :-offset, 2] = self.source_image[offset:, offset:, 2]

        # Green channel (no shift)
        frame[:, :, 1] = self.source_image[:, :, 1]

        # Blue channel shift
        if offset > 0:
            frame[offset:, offset:, 0] = self.source_image[:-offset, :-offset, 0]

        # Add spectral rays
        for i in range(len(magnitudes)):
            if i % 5 == 0:
                mag = magnitudes[i] / 100.0
                angle = (i / len(magnitudes)) * 2 * np.pi

                length = int(mag * 200)
                x1 = self.center_x
                y1 = self.center_y
                x2 = int(x1 + length * np.cos(angle))
                y2 = int(y1 + length * np.sin(angle))

                # Get color from image
                sample_x = 0.5 + 0.3 * np.cos(angle)
                sample_y = 0.5 + 0.3 * np.sin(angle)
                color = self._get_color_at(sample_x, sample_y)

                cv2.line(frame, (x1, y1), (x2, y2), color, 2, cv2.LINE_AA)

    def render_mode_9_pixel_vortex(self, frame, magnitudes):
        """Mode 9: Pixel Vortex - Image pixels spiral into vortex"""
        # Initialize vortex particles
        if len(self.vortex_particles) < 1000:
            for _ in range(1000 - len(self.vortex_particles)):
                angle = np.random.random() * 2 * np.pi
                radius = np.random.random() * min(self.width, self.height) / 2

                x = self.center_x + radius * np.cos(angle)
                y = self.center_y + radius * np.sin(angle)

                self.vortex_particles.append({
                    'angle': angle,
                    'radius': radius,
                    'angular_vel': np.random.uniform(0.01, 0.05),
                    'color': self._get_color_at_pixel(x, y) if 0 <= x < self.width and 0 <= y < self.height else (128, 128, 128, 255)
                })

        energy = np.mean(magnitudes) / 100.0

        # Update and draw vortex
        for particle in self.vortex_particles:
            # Spiral inward/outward based on audio
            particle['radius'] += np.sin(self.frame_counter * 0.1) * energy * 2
            particle['radius'] = max(10, min(particle['radius'], min(self.width, self.height) / 2))

            # Rotate
            particle['angle'] += particle['angular_vel'] * (1 + energy)

            # Calculate position
            x = self.center_x + particle['radius'] * np.cos(particle['angle'])
            y = self.center_y + particle['radius'] * np.sin(particle['angle'])

            if 0 <= x < self.width and 0 <= y < self.height:
                # Update color from image
                particle['color'] = self._get_color_at_pixel(x, y)

                size = int(2 + energy * 3)
                cv2.circle(frame, (int(x), int(y)), size, particle['color'], -1, cv2.LINE_AA)

    def render_mode_10_color_trails(self, frame, magnitudes):
        """Mode 10: Color Trails - Particles leave trails in image colors"""
        # Spawn new particles
        if self.frame_counter % 2 == 0:
            for i in range(20):
                mag_idx = i % len(magnitudes)
                angle = (i / 20) * 2 * np.pi
                speed = 2 + (magnitudes[mag_idx] / 100.0) * 5

                self.trail_particles.append({
                    'x': self.center_x,
                    'y': self.center_y,
                    'vx': speed * np.cos(angle),
                    'vy': speed * np.sin(angle),
                    'trail': [],
                    'life': 1.0
                })

        # Update and draw particles with trails
        particles_to_keep = []
        for particle in self.trail_particles:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.005

            # Add to trail
            if 0 <= particle['x'] < self.width and 0 <= particle['y'] < self.height:
                color = self._get_color_at_pixel(particle['x'], particle['y'])
                particle['trail'].append((int(particle['x']), int(particle['y']), color))

            # Keep trail length manageable
            if len(particle['trail']) > 30:
                particle['trail'].pop(0)

            # Draw trail
            if particle['life'] > 0:
                for i, (tx, ty, tcolor) in enumerate(particle['trail']):
                    alpha = int((i / len(particle['trail'])) * particle['life'] * 255)
                    color = list(tcolor)
                    color[3] = alpha

                    cv2.circle(frame, (tx, ty), 3, tuple(color), -1, cv2.LINE_AA)

                particles_to_keep.append(particle)

        self.trail_particles = particles_to_keep

    def generate_frame(self, magnitudes):
        """Generate a single frame of visualization"""
        # Create transparent frame (BGRA)
        frame = np.zeros((self.height, self.width, 4), dtype=np.uint8)

        # Apply smoothing
        if self.prev_magnitudes is not None:
            magnitudes = (self.smoothing * self.prev_magnitudes +
                         (1 - self.smoothing) * magnitudes)
        self.prev_magnitudes = magnitudes.copy()

        # Render based on mode
        if self.mode == 1:
            self.render_mode_1_image_particles(frame, magnitudes)
        elif self.mode == 2:
            self.render_mode_2_color_wave(frame, magnitudes)
        elif self.mode == 3:
            self.render_mode_3_pixel_fountain(frame, magnitudes)
        elif self.mode == 4:
            self.render_mode_4_image_shatter(frame, magnitudes)
        elif self.mode == 5:
            self.render_mode_5_chromatic_rings(frame, magnitudes)
        elif self.mode == 6:
            self.render_mode_6_image_mosaic(frame, magnitudes)
        elif self.mode == 7:
            self.render_mode_7_spectrum_paint(frame, magnitudes)
        elif self.mode == 8:
            self.render_mode_8_photo_prism(frame, magnitudes)
        elif self.mode == 9:
            self.render_mode_9_pixel_vortex(frame, magnitudes)
        elif self.mode == 10:
            self.render_mode_10_color_trails(frame, magnitudes)
        else:
            raise ValueError(f"Invalid mode: {self.mode}. Choose 1-10.")

        self.frame_counter += 1
        return frame

    def create_visualization(self):
        """Main function to create the complete visualization"""
        # Load audio
        db_spectrum, total_frames, audio_data, sample_rate = self.load_audio()

        # Validate output file extension
        output_ext = Path(self.output_path).suffix.lower()
        if output_ext not in ['.mov', '.mp4', '.avi']:
            raise ValueError(f"Output file must be a video file (.mov, .mp4, or .avi), got: {output_ext}")

        # Setup video writer - try multiple codec options
        codecs_to_try = [
            ('avc1', 'H.264'),  # H.264 (widely supported)
            ('mp4v', 'MPEG-4'),  # MPEG-4
            ('XVID', 'Xvid'),    # Xvid
        ]

        out = None
        for fourcc_str, codec_name in codecs_to_try:
            fourcc = cv2.VideoWriter_fourcc(*fourcc_str)
            out = cv2.VideoWriter(
                self.output_path,
                fourcc,
                self.fps,
                (self.width, self.height),
                True
            )

            if out.isOpened():
                print(f"Using {codec_name} codec")
                break
            else:
                out.release()
                out = None

        if out is None or not out.isOpened():
            raise RuntimeError(f"Failed to open video writer for {self.output_path}. Try using .mp4 extension.")

        print(f"Rendering {total_frames} frames...")

        # Process each frame
        for frame_idx in range(total_frames):
            if frame_idx % 30 == 0:
                progress = (frame_idx / total_frames) * 100
                print(f"Progress: {progress:.1f}% ({frame_idx}/{total_frames} frames)")

            # Get frequency spectrum for this frame
            if frame_idx < db_spectrum.shape[1]:
                frame_spectrum = db_spectrum[:, frame_idx]
            else:
                frame_spectrum = db_spectrum[:, -1]

            # Normalize and select frequency bins
            spectrum_normalized = np.interp(
                frame_spectrum,
                (frame_spectrum.min(), frame_spectrum.max()),
                (0, 100)
            )

            # Select evenly spaced frequency bins
            indices = np.linspace(0, len(spectrum_normalized) - 1, self.num_bars, dtype=int)
            magnitudes = spectrum_normalized[indices]

            # Generate frame
            frame = self.generate_frame(magnitudes)

            # Convert BGRA to BGR for video writing (some codecs don't support alpha in VideoWriter)
            # We'll composite over black background
            bgr_frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
            alpha = frame[:, :, 3:4] / 255.0
            bgr_frame = frame[:, :, :3] * alpha + bgr_frame * (1 - alpha)
            bgr_frame = bgr_frame.astype(np.uint8)

            out.write(bgr_frame)

        out.release()
        print(f"\nVisualization complete! Saved to {self.output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate image-based audio spectrum visualizations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python audio_spectrum_image.py input.wav output.mov --image photo.jpg --mode 1
  python audio_spectrum_image.py input.wav output.mov --image logo.png --mode 5 --width 1280 --height 720

Modes:
  1: Image Particles - Pixels explode and react to audio
  2: Color Wave - Image colors ripple outward
  3: Pixel Fountain - Pixels fountain up from bottom
  4: Image Shatter - Image breaks into dancing shards
  5: Chromatic Rings - Concentric rings in image colors
  6: Image Mosaic - Tiles rearrange rhythmically
  7: Spectrum Paint - Paint strokes using image colors
  8: Photo Prism - Image refracted through prism
  9: Pixel Vortex - Pixels spiral into vortex
  10: Color Trails - Particles leave colorful trails
        """
    )

    parser.add_argument('audio_file', help='Input audio file path')
    parser.add_argument('output_file', help='Output video file path (.mov)')
    parser.add_argument('--image', required=True, help='Input image file path')
    parser.add_argument('--mode', type=int, default=1, choices=range(1, 11),
                       help='Visualization mode (1-10)')
    parser.add_argument('--width', type=int, default=1920,
                       help='Video width (default: 1920)')
    parser.add_argument('--height', type=int, default=1080,
                       help='Video height (default: 1080)')
    parser.add_argument('--fps', type=int, default=30,
                       help='Frames per second (default: 30)')
    parser.add_argument('--num-bars', type=int, default=120,
                       help='Number of frequency bars (default: 120)')
    parser.add_argument('--smoothing', type=float, default=0.7,
                       help='Smoothing factor 0-1 (default: 0.7)')

    args = parser.parse_args()

    # Validate input files
    if not Path(args.audio_file).exists():
        print(f"Error: Audio file not found: {args.audio_file}")
        sys.exit(1)

    if not Path(args.image).exists():
        print(f"Error: Image file not found: {args.image}")
        sys.exit(1)

    # Create visualizer and generate
    visualizer = ImageSpectrumVisualizer(
        audio_path=args.audio_file,
        output_path=args.output_file,
        image_path=args.image,
        width=args.width,
        height=args.height,
        fps=args.fps,
        num_bars=args.num_bars,
        smoothing=args.smoothing,
        mode=args.mode
    )

    visualizer.create_visualization()


if __name__ == '__main__':
    main()

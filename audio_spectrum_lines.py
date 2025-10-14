#!/usr/bin/env python3
"""
Line-Based Audio Spectrum Visualizer
Generates a transparent video with line-based audio spectrum animation

Visualization Modes:
  --mode 1: Classic Bars - Traditional vertical bars (default)
  --mode 2: Mirror Symmetry - Bars mirrored from center line
  --mode 3: Waterfall - Cascading bars with trail effect
  --mode 4: Converging Lines - Bars angle inward creating perspective
  --mode 5: Wave Morph - Smooth sine wave overlay on bars
  --mode 6: Staggered Pulse - Alternating heights with phase offset
  --mode 7: Geometric Tunnel - Bars create 3D depth illusion
  --mode 8: Dancing Ribbons - Flowing curved lines instead of straight bars
  --mode 9: Particle Stream - Dots instead of bars, flowing upward
  --mode 10: Glitch Art - Random horizontal offsets for digital glitch aesthetic

Examples:
  # Generate with default mode (Classic Bars)
  python audio_spectrum_lines.py '/Users/ahmeddoghri/Desktop/RÜFÜS DU SOL - New Sky (Lyrics).mp3' '/Users/ahmeddoghri/Desktop/output2.mov' --mode 2


  # With different visualization mode
  python audio_spectrum_lines.py input.mp3 output.mov --mode 2
  python audio_spectrum_lines.py input.mp3 output.mov --mode 5

  # Custom number of bars
  python audio_spectrum_lines.py audio.mp3 spectrum.mov --mode 3 --num-bars 80
  
  
  
  pick output_lines_mode7_Geometric_Tunnel.mov and  output_lines_mode8_Dancing_Ribbons
  honorable mentions 
  and output_lines_mode6_Staggered_Pulse.mov
  and output_lines_mode5_Wave_Morph.mov
"""

import sys
import numpy as np
import cv2
import librosa
import argparse
from pathlib import Path


class LineSpectrumVisualizer:
    def __init__(self, audio_path, output_path, width=1920, height=1080,
                 fps=30, num_bars=60, color=(255, 255, 255),
                 bar_spacing=10, smoothing=0.7, mode=1):
        """
        Initialize the line spectrum visualizer

        Args:
            audio_path: Path to input audio file (.mp3 or .wav)
            output_path: Path to output video file
            width: Video width in pixels
            height: Video height in pixels
            fps: Frames per second
            num_bars: Number of frequency bars
            color: RGB color tuple for the spectrum bars (default white)
            bar_spacing: Spacing between bars in pixels
            smoothing: Smoothing factor (0-1) for animation
            mode: Visualization mode (1-10)
        """
        self.audio_path = audio_path
        self.output_path = output_path
        self.width = width
        self.height = height
        self.fps = fps
        self.num_bars = num_bars
        self.color = color
        self.bar_spacing = bar_spacing
        self.smoothing = smoothing
        self.mode = mode

        # Calculate bar width based on available width and spacing
        total_spacing = (num_bars + 1) * bar_spacing
        available_width = width - total_spacing
        self.bar_width = max(2, available_width // num_bars)

        # Max bar height (leave some margin)
        self.max_bar_height = int(height * 0.8)
        self.center_y = height // 2

        # For smoothing between frames
        self.prev_magnitudes = None

        # For waterfall mode (mode 3)
        self.waterfall_history = []

        # For glitch mode (mode 10)
        self.glitch_offsets = None

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
        total_freqs = len(frame_magnitudes)

        # Only use the lower 60% of frequencies (where most music energy is)
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

    def draw_mode_1_classic_bars(self, frame, magnitudes):
        """Mode 1: Classic vertical bars"""
        for i, magnitude in enumerate(magnitudes):
            # Calculate bar position
            x = self.bar_spacing + i * (self.bar_width + self.bar_spacing)

            # Calculate bar height
            bar_height = int(magnitude * self.max_bar_height)
            bar_height = max(5, bar_height)

            # Draw bar from bottom up
            y_bottom = self.height - 50
            y_top = y_bottom - bar_height

            # Draw rectangle (filled bar)
            cv2.rectangle(frame, (x, y_top), (x + self.bar_width, y_bottom),
                         self.color, -1, lineType=cv2.LINE_AA)

            # Add subtle glow for high magnitudes
            if magnitude > 0.7:
                glow_rect = (x - 1, y_top - 2, self.bar_width + 2, bar_height + 2)
                cv2.rectangle(frame, (glow_rect[0], glow_rect[1]),
                            (glow_rect[0] + glow_rect[2], glow_rect[1] + glow_rect[3]),
                            tuple(int(c * 0.5) for c in self.color), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_2_mirror_symmetry(self, frame, magnitudes):
        """Mode 2: Bars mirrored from center line"""
        for i, magnitude in enumerate(magnitudes):
            x = self.bar_spacing + i * (self.bar_width + self.bar_spacing)
            bar_height = int(magnitude * self.max_bar_height * 0.5)
            bar_height = max(3, bar_height)

            # Top bar (mirrored up from center)
            y_center = self.center_y
            y_top = y_center - bar_height
            cv2.rectangle(frame, (x, y_top), (x + self.bar_width, y_center),
                         self.color, -1, lineType=cv2.LINE_AA)

            # Bottom bar (mirrored down from center)
            y_bottom = y_center + bar_height
            cv2.rectangle(frame, (x, y_center), (x + self.bar_width, y_bottom),
                         self.color, -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_3_waterfall(self, frame, magnitudes):
        """Mode 3: Cascading bars with trail effect"""
        # Add current magnitudes to history
        self.waterfall_history.append(magnitudes.copy())

        # Keep only last 10 frames for trail
        if len(self.waterfall_history) > 10:
            self.waterfall_history.pop(0)

        # Draw from oldest to newest (creates trail effect)
        for history_idx, hist_magnitudes in enumerate(self.waterfall_history):
            alpha = (history_idx + 1) / len(self.waterfall_history)
            trail_color = tuple(int(c * alpha) for c in self.color)

            # Offset each layer slightly
            y_offset = history_idx * 8

            for i, magnitude in enumerate(hist_magnitudes):
                x = self.bar_spacing + i * (self.bar_width + self.bar_spacing)
                bar_height = int(magnitude * self.max_bar_height * 0.8)
                bar_height = max(3, bar_height)

                y_bottom = self.height - 50 - y_offset
                y_top = y_bottom - bar_height

                cv2.rectangle(frame, (x, y_top), (x + self.bar_width, y_bottom),
                            trail_color, -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_4_converging_lines(self, frame, magnitudes):
        """Mode 4: Bars angle inward creating perspective"""
        for i, magnitude in enumerate(magnitudes):
            x = self.bar_spacing + i * (self.bar_width + self.bar_spacing)
            bar_height = int(magnitude * self.max_bar_height)
            bar_height = max(5, bar_height)

            # Calculate convergence angle
            center_x = self.width / 2
            distance_from_center = x - center_x
            angle_factor = distance_from_center / center_x * 0.3

            # Bottom points
            x1_bottom = x
            x2_bottom = x + self.bar_width
            y_bottom = self.height - 50

            # Top points (converge inward)
            x1_top = int(x - angle_factor * bar_height)
            x2_top = int(x + self.bar_width - angle_factor * bar_height)
            y_top = y_bottom - bar_height

            # Draw as polygon (trapezoid)
            points = np.array([
                [x1_bottom, y_bottom],
                [x2_bottom, y_bottom],
                [x2_top, y_top],
                [x1_top, y_top]
            ], dtype=np.int32)

            cv2.fillPoly(frame, [points], self.color, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_5_wave_morph(self, frame, magnitudes):
        """Mode 5: Smooth sine wave overlay on bars"""
        # Calculate wave offset based on average magnitude
        avg_magnitude = np.mean(magnitudes)
        wave_amplitude = avg_magnitude * 30

        for i, magnitude in enumerate(magnitudes):
            x = self.bar_spacing + i * (self.bar_width + self.bar_spacing)

            # Base bar height
            bar_height = int(magnitude * self.max_bar_height)
            bar_height = max(5, bar_height)

            # Add wave offset
            wave_offset = np.sin(i / self.num_bars * np.pi * 4) * wave_amplitude

            y_bottom = self.height - 50
            y_top = int(y_bottom - bar_height + wave_offset)

            # Draw bar
            cv2.rectangle(frame, (x, y_top), (x + self.bar_width, y_bottom),
                         self.color, -1, lineType=cv2.LINE_AA)

        # Draw smooth wave line on top
        wave_points = []
        for i, magnitude in enumerate(magnitudes):
            x = self.bar_spacing + i * (self.bar_width + self.bar_spacing) + self.bar_width // 2
            bar_height = int(magnitude * self.max_bar_height)
            wave_offset = np.sin(i / self.num_bars * np.pi * 4) * wave_amplitude
            y = int(self.height - 50 - bar_height + wave_offset)
            wave_points.append([x, y])

        if len(wave_points) > 1:
            wave_points = np.array(wave_points, dtype=np.int32)
            cv2.polylines(frame, [wave_points], False, self.color, 3, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_6_staggered_pulse(self, frame, magnitudes):
        """Mode 6: Alternating heights with phase offset"""
        for i, magnitude in enumerate(magnitudes):
            x = self.bar_spacing + i * (self.bar_width + self.bar_spacing)

            # Phase offset for staggered effect
            phase = (i % 3) * 0.3
            adjusted_magnitude = magnitude * (0.7 + phase)
            adjusted_magnitude = min(1.0, adjusted_magnitude)

            bar_height = int(adjusted_magnitude * self.max_bar_height)
            bar_height = max(5, bar_height)

            # Alternate between bottom-up and center-out
            if i % 2 == 0:
                # Bottom-up
                y_bottom = self.height - 50
                y_top = y_bottom - bar_height
            else:
                # Center-out
                y_top = self.center_y - bar_height // 2
                y_bottom = self.center_y + bar_height // 2

            cv2.rectangle(frame, (x, y_top), (x + self.bar_width, y_bottom),
                         self.color, -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_7_geometric_tunnel(self, frame, magnitudes):
        """Mode 7: Bars create 3D depth illusion"""
        # Draw multiple layers with decreasing size (perspective)
        num_layers = 5

        for layer in range(num_layers):
            layer_progress = layer / num_layers
            scale = 1.0 - (layer_progress * 0.6)
            alpha = 1.0 - (layer_progress * 0.5)
            layer_color = tuple(int(c * alpha) for c in self.color)

            # Layer offset (creates depth)
            y_offset = int(layer * 40)

            for i, magnitude in enumerate(magnitudes):
                # Scale bar width and spacing
                scaled_bar_width = int(self.bar_width * scale)
                scaled_spacing = int(self.bar_spacing * scale)

                # Center the scaled bars
                total_scaled_width = self.num_bars * (scaled_bar_width + scaled_spacing)
                x_offset = (self.width - total_scaled_width) // 2

                x = x_offset + i * (scaled_bar_width + scaled_spacing)

                bar_height = int(magnitude * self.max_bar_height * scale * 0.6)
                bar_height = max(2, bar_height)

                y_bottom = self.height - 50 - y_offset
                y_top = y_bottom - bar_height

                cv2.rectangle(frame, (x, y_top), (x + scaled_bar_width, y_bottom),
                            layer_color, -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_8_dancing_ribbons(self, frame, magnitudes):
        """Mode 8: Flowing curved lines instead of straight bars"""
        # Create smooth curves for each bar
        for i, magnitude in enumerate(magnitudes):
            x = self.bar_spacing + i * (self.bar_width + self.bar_spacing) + self.bar_width // 2
            bar_height = int(magnitude * self.max_bar_height)
            bar_height = max(10, bar_height)

            # Create wavy curve for each bar
            curve_points = []
            num_curve_points = 20

            for j in range(num_curve_points):
                y_progress = j / num_curve_points
                y = self.height - 50 - int(y_progress * bar_height)

                # Add wave motion
                wave_x = np.sin(y_progress * np.pi * 2 + i * 0.2) * 8
                curve_x = int(x + wave_x)

                curve_points.append([curve_x, y])

            if len(curve_points) > 1:
                curve_points = np.array(curve_points, dtype=np.int32)

                # Draw thick curve
                cv2.polylines(frame, [curve_points], False, self.color,
                            max(2, self.bar_width), lineType=cv2.LINE_AA)

        return frame

    def draw_mode_9_particle_stream(self, frame, magnitudes):
        """Mode 9: Dots instead of bars, flowing upward"""
        for i, magnitude in enumerate(magnitudes):
            x_center = self.bar_spacing + i * (self.bar_width + self.bar_spacing) + self.bar_width // 2
            bar_height = int(magnitude * self.max_bar_height)

            # Number of particles based on magnitude
            num_particles = max(3, int(magnitude * 15))

            for p in range(num_particles):
                y_progress = p / num_particles
                y = self.height - 50 - int(y_progress * bar_height)

                # Particle size varies with height
                particle_size = max(2, int(6 - y_progress * 4))

                # Add some horizontal variance
                x_variance = np.sin(y_progress * np.pi * 3 + i) * 5
                x = int(x_center + x_variance)

                # Fade particles at the top
                alpha = 1.0 - (y_progress * 0.5)
                particle_color = tuple(int(c * alpha) for c in self.color)

                cv2.circle(frame, (x, y), particle_size, particle_color, -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_10_glitch_art(self, frame, magnitudes):
        """Mode 10: Random horizontal offsets for digital glitch aesthetic"""
        # Regenerate glitch offsets occasionally for variety
        if self.glitch_offsets is None or np.random.random() < 0.1:
            self.glitch_offsets = np.random.randint(-20, 20, size=self.num_bars)

        for i, magnitude in enumerate(magnitudes):
            base_x = self.bar_spacing + i * (self.bar_width + self.bar_spacing)

            # Add glitch offset
            glitch_offset = self.glitch_offsets[i] if magnitude > 0.5 else 0
            x = base_x + glitch_offset

            bar_height = int(magnitude * self.max_bar_height)
            bar_height = max(5, bar_height)

            # Random segment breaks in tall bars
            if bar_height > 100 and magnitude > 0.6:
                # Draw in segments with gaps
                num_segments = 3
                segment_height = bar_height // num_segments

                for seg in range(num_segments):
                    seg_offset = np.random.randint(-10, 10)
                    seg_x = x + seg_offset

                    y_bottom = self.height - 50 - seg * segment_height
                    y_top = y_bottom - segment_height + 10

                    cv2.rectangle(frame, (seg_x, y_top), (seg_x + self.bar_width, y_bottom),
                                self.color, -1, lineType=cv2.LINE_AA)
            else:
                # Normal bar
                y_bottom = self.height - 50
                y_top = y_bottom - bar_height

                cv2.rectangle(frame, (x, y_top), (x + self.bar_width, y_bottom),
                            self.color, -1, lineType=cv2.LINE_AA)

        # Add horizontal glitch lines occasionally
        if np.random.random() < 0.05:
            y_glitch = np.random.randint(100, self.height - 100)
            cv2.line(frame, (0, y_glitch), (self.width, y_glitch),
                    self.color, 2, lineType=cv2.LINE_AA)

        return frame

    def draw_spectrum(self, frame, magnitudes):
        """Draw the spectrum based on selected mode"""
        if self.mode == 1:
            return self.draw_mode_1_classic_bars(frame, magnitudes)
        elif self.mode == 2:
            return self.draw_mode_2_mirror_symmetry(frame, magnitudes)
        elif self.mode == 3:
            return self.draw_mode_3_waterfall(frame, magnitudes)
        elif self.mode == 4:
            return self.draw_mode_4_converging_lines(frame, magnitudes)
        elif self.mode == 5:
            return self.draw_mode_5_wave_morph(frame, magnitudes)
        elif self.mode == 6:
            return self.draw_mode_6_staggered_pulse(frame, magnitudes)
        elif self.mode == 7:
            return self.draw_mode_7_geometric_tunnel(frame, magnitudes)
        elif self.mode == 8:
            return self.draw_mode_8_dancing_ribbons(frame, magnitudes)
        elif self.mode == 9:
            return self.draw_mode_9_particle_stream(frame, magnitudes)
        elif self.mode == 10:
            return self.draw_mode_10_glitch_art(frame, magnitudes)
        else:
            # Default to mode 1
            return self.draw_mode_1_classic_bars(frame, magnitudes)

    def generate_video(self):
        """Generate the final video with transparent background"""
        print(f"Generating video: {self.output_path}")

        # Load audio
        self.load_audio()

        # Create temporary video without audio
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
            # Create BGR frame (3 channels) - black background
            frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)

            # Get frequency data for this frame
            audio_frame_idx = int(frame_idx * self.num_frames / total_frames)
            magnitudes = self.get_frequency_bands(audio_frame_idx)

            # Draw spectrum on the frame
            frame = self.draw_spectrum(frame, magnitudes)

            # Write frame to video
            video_writer.write(frame)

            # Progress indicator
            if (frame_idx + 1) % 30 == 0 or frame_idx == total_frames - 1:
                progress = (frame_idx + 1) / total_frames * 100
                print(f"Progress: {progress:.1f}% ({frame_idx + 1}/{total_frames} frames)")

        video_writer.release()
        print(f"\nVideo generation complete (silent): {temp_no_audio}")

        # Use ffmpeg to add audio and transparency
        print("Adding audio and transparency...")
        import subprocess

        try:
            # Output to .mov with transparency
            final_output = str(Path(self.output_path).with_suffix('.mov'))

            # Use ffmpeg to add audio and convert black to transparent
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

            # Clean up temp file
            Path(temp_no_audio).unlink()

            if result.returncode == 0:
                self.output_path = final_output
                print(f"✓ Video with transparency and audio created successfully")
                print(f"✓ Output: {final_output}")
            else:
                print(f"Warning: Could not create transparent video. Creating standard video instead.")
                print(f"FFmpeg error: {result.stderr}")

                # Fallback: just add audio
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
        description='Generate line-based audio spectrum visualization with transparent background',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate with default mode (Classic Bars)
  python audio_spectrum_lines.py input.mp3 output.mov

  # With different visualization modes
  python audio_spectrum_lines.py input.mp3 output.mov --mode 2
  python audio_spectrum_lines.py input.mp3 output.mov --mode 5

  # Custom number of bars and spacing
  python audio_spectrum_lines.py audio.mp3 spectrum.mov --num-bars 80 --bar-spacing 8

  # Adjust smoothing for more responsive animation
  python audio_spectrum_lines.py audio.mp3 spectrum.mov --smoothing 0.5
        """
    )

    parser.add_argument('input', help='Input audio file (.mp3 or .wav)')
    parser.add_argument('output', help='Output video file (.mov recommended)')
    parser.add_argument('--mode', type=int, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default=1,
                       help='Visualization mode: 1=Classic Bars (default), 2=Mirror Symmetry, 3=Waterfall, 4=Converging Lines, 5=Wave Morph, 6=Staggered Pulse, 7=Geometric Tunnel, 8=Dancing Ribbons, 9=Particle Stream, 10=Glitch Art')
    parser.add_argument('--width', type=int, default=1920, help='Video width (default: 1920)')
    parser.add_argument('--height', type=int, default=1080, help='Video height (default: 1080)')
    parser.add_argument('--fps', type=int, default=30, help='Frames per second (default: 30)')
    parser.add_argument('--num-bars', type=int, default=60, help='Number of frequency bars (default: 60)')
    parser.add_argument('--bar-spacing', type=int, default=10, help='Spacing between bars (default: 10)')
    parser.add_argument('--smoothing', type=float, default=0.7, help='Smoothing factor 0-1 (default: 0.7)')

    args = parser.parse_args()

    # Validate input file
    if not Path(args.input).exists():
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)

    # Print selected mode
    mode_names = {
        1: "Classic Bars",
        2: "Mirror Symmetry",
        3: "Waterfall",
        4: "Converging Lines",
        5: "Wave Morph",
        6: "Staggered Pulse",
        7: "Geometric Tunnel",
        8: "Dancing Ribbons",
        9: "Particle Stream",
        10: "Glitch Art"
    }
    print(f"Selected visualization mode: {args.mode} - {mode_names.get(args.mode, 'Unknown')}")

    # White color in BGR format
    color_bgr = (255, 255, 255)

    # Create visualizer
    visualizer = LineSpectrumVisualizer(
        audio_path=args.input,
        output_path=args.output,
        width=args.width,
        height=args.height,
        fps=args.fps,
        num_bars=args.num_bars,
        color=color_bgr,
        bar_spacing=args.bar_spacing,
        smoothing=args.smoothing,
        mode=args.mode
    )

    # Generate video
    try:
        visualizer.generate_video()
        print("\nSuccess! Your line-based audio spectrum video is ready.")
        print(f"Note: For true transparency in video editors, import the {args.output} file")
        print("      and enable 'preserve transparency' or use as a luma matte.")
    except Exception as e:
        print(f"\nError generating video: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

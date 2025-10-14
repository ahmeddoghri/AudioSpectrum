#!/usr/bin/env python3
"""
Circular Audio Spectrum Visualizer
Generates a transparent video with circular audio spectrum animation

Example (YouTube regular - 1920x1080, auto for .mov):
python audio_spectrum.py '/Users/ahmeddoghri/Desktop/RÜFÜS DU SOL - New Sky (Lyrics).mp3' '/Users/ahmeddoghri/Desktop/output.mov'

Example (YouTube Shorts - 1080x1920, auto for .mp4):
python audio_spectrum.py '/Users/ahmeddoghri/Desktop/RÜFÜS DU SOL - New Sky (Lyrics).mp3' '/Users/ahmeddoghri/Desktop/output.mp4'

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
                 gradient_color1=None, gradient_color2=None):
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

    def draw_circular_spectrum(self, frame, magnitudes):
        """Draw the circular spectrum on a frame"""
        angle_step = 360 / self.num_bars

        for i, magnitude in enumerate(magnitudes):
            # Calculate angle for this bar (start from left, go clockwise)
            angle = np.deg2rad(i * angle_step)

            # Calculate bar height based on magnitude with minimum height
            min_bar_height = 5  # Minimum visible bar height
            max_bar_height = self.max_radius - self.inner_radius
            bar_height = int(magnitude * max_bar_height)
            bar_height = max(min_bar_height, bar_height)  # Ensure minimum visibility

            # Calculate start and end points of the bar
            start_x = int(self.center_x + self.inner_radius * np.cos(angle))
            start_y = int(self.center_y + self.inner_radius * np.sin(angle))

            end_x = int(self.center_x + (self.inner_radius + bar_height) * np.cos(angle))
            end_y = int(self.center_y + (self.inner_radius + bar_height) * np.sin(angle))

            # Calculate bar thickness
            thickness = max(1, int(self.bar_width_multiplier * angle_step / 2))

            # Determine bar color
            if self.gradient and self.gradient_color1 and self.gradient_color2:
                # Calculate gradient position based on angle
                # Left side (180°) = color1 (blue), Right side (0°/360°) = color2 (pink)
                # Normalize angle to 0-1 where 0.5 is left (180°) and 0/1 is right (0°/360°)
                angle_normalized = (i * angle_step) / 360.0

                # Create a smooth transition: left (0.5) to right (0 or 1)
                # Map so that 180° = 0 (full color1) and 0° = 1 (full color2)
                if angle_normalized <= 0.5:
                    # Top-left quadrant: 0 to 0.5 -> blend from 0.5 to 0
                    blend = 0.5 - angle_normalized
                else:
                    # Bottom-right quadrant: 0.5 to 1 -> blend from 0 to 0.5
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

            cv2.line(frame, (start_x, start_y), (end_x, end_y),
                    bar_color, thickness, lineType=cv2.LINE_AA)

        return frame

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
        # 3. Output to final format with alpha channel
        print("Adding audio and transparency...")
        import subprocess

        try:
            # Check if output should be .mov (supports alpha) or .webm (also supports alpha)
            # If user wants .mp4, we'll create .webm or .mov instead since MP4 doesn't support transparency
            if ext == '.mp4':
                print("Note: MP4 doesn't support transparency. Converting to .mov with alpha channel.")
                final_output = str(Path(self.output_path).with_suffix('.mov'))
            else:
                final_output = self.output_path

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
                    self.output_path
                ], capture_output=True, text=True)

                Path(temp_no_audio).unlink()

                if result.returncode == 0:
                    print(f"✓ Standard video created: {self.output_path}")
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
        gradient_color2=gradient_color2_bgr
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

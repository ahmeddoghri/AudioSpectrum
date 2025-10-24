#!/usr/bin/env python3
"""
Video Preview Generator for Audio Spectrum Visualizations
Generates 3-second video previews of all modes
"""

import subprocess
import sys
from pathlib import Path
import time

# Configuration
AUDIO_FILE = 'turkish-national-anthem.wav'  # Relative path for deployment
PREVIEWS_DIR = 'catalog/video_previews'  # Relative path for deployment

# Define all modes for each script
SCRIPTS = {
    'audio_spectrum': {
        'script': 'audio_spectrum.py',
        'modes': list(range(1, 11))
    },
    'audio_spectrum_lines': {
        'script': 'audio_spectrum_lines.py',
        'modes': list(range(1, 11))
    },
    'audio_spectrum_creative': {
        'script': 'audio_spectrum_creative.py',
        'modes': list(range(1, 101))  # NOW 100 MODES!
    }
}


def create_preview_audio():
    """Create a 4-second audio clip (6-10s) for faster preview generation"""
    temp_audio = Path(PREVIEWS_DIR) / 'preview_audio_4s.wav'

    print("Creating 4-second audio clip for previews (6-10 seconds)...")
    result = subprocess.run([
        'ffmpeg', '-y',
        '-i', AUDIO_FILE,
        '-ss', '00:00:06',  # Start at 6 seconds
        '-t', '4',  # 4 seconds duration (6-10s)
        temp_audio
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print(f"✗ Failed to create temp audio: {result.stderr}")
        return None

    print(f"✓ Created 4-second audio: {temp_audio}")
    return str(temp_audio)


def generate_preview_video(script_name, mode_num, preview_audio, output_dir):
    """Generate a 4-second preview video with small file size (480x480)"""
    output_video = output_dir / f"{Path(script_name).stem}_mode_{mode_num:03d}.mov"

    # Skip if already exists
    if output_video.exists():
        print(f"  ⚠ Preview already exists, skipping: {output_video.name}")
        return str(output_video)

    # Use smaller dimensions (480x480) for much smaller file sizes
    cmd = [
        'python',
        script_name,
        preview_audio,
        str(output_video),
        '--mode', str(mode_num),
        '--width', '480',
        '--height', '480'
    ]

    print(f"  Generating preview: {output_video.name}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0 and output_video.exists():
        print(f"  ✓ Generated: {output_video.name}")
        return str(output_video)
    else:
        print(f"  ✗ Failed to generate: {output_video.name}")
        if result.stderr:
            print(f"    Error: {result.stderr[:200]}")
        return None


def main():
    print("=" * 80)
    print("AUDIO SPECTRUM VIDEO PREVIEW GENERATOR")
    print("Generating 4-second video previews (480x480) for HTML viewer")
    print("=" * 80)
    print()

    # Create previews directory
    previews_dir = Path(PREVIEWS_DIR)
    previews_dir.mkdir(parents=True, exist_ok=True)

    # Check if audio file exists
    if not Path(AUDIO_FILE).exists():
        print(f"Error: Audio file not found: {AUDIO_FILE}")
        sys.exit(1)

    # Create 4-second audio clip (6-10s)
    preview_audio = create_preview_audio()
    if not preview_audio:
        print("Failed to create preview audio")
        sys.exit(1)

    print()

    # Total count
    total_modes = sum(len(info['modes']) for info in SCRIPTS.values())
    print(f"Total modes to process: {total_modes}")
    print()

    current = 0
    generated = 0
    skipped = 0

    # Process each script
    for script_key, script_info in SCRIPTS.items():
        script_name = script_info['script']
        modes = script_info['modes']

        print(f"\n{'='*80}")
        print(f"Processing: {script_name} ({len(modes)} modes)")
        print(f"{'='*80}\n")

        for mode_num in modes:
            current += 1
            print(f"[{current}/{total_modes}] Mode {mode_num}")

            result = generate_preview_video(script_name, mode_num, preview_audio, previews_dir)

            if result:
                if "already exists" not in result:
                    generated += 1
                else:
                    skipped += 1

            time.sleep(0.2)  # Small delay

    print("\n" + "=" * 80)
    print("VIDEO PREVIEW GENERATION COMPLETE!")
    print("=" * 80)
    print(f"\nPreviews saved to: {PREVIEWS_DIR}")
    print(f"Generated: {generated} new previews")
    print(f"Skipped: {skipped} existing previews")
    print(f"Total: {generated + skipped} preview videos")


if __name__ == '__main__':
    main()

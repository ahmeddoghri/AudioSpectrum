#!/usr/bin/env python3
"""
Catalog Generator for Audio Spectrum Visualizations
Generates screenshot images of all modes at peak audio levels
"""

import subprocess
import sys
from pathlib import Path
import time

# Configuration
AUDIO_FILE = 'turkish-national-anthem.wav'
CATALOG_DIR = 'catalog'

# Define all modes for each script
SCRIPTS = {
    'audio_spectrum': {
        'script': 'audio_spectrum.py',
        'modes': {
            1: 'Bars',
            2: 'Waves_Layers',
            3: 'Particles',
            4: 'Waveform',
            5: 'Polygon',
            6: 'Spiral',
            7: 'DNA_Helix',
            8: 'Kaleidoscope',
            9: 'Pulse_Rings',
            10: 'Star_Burst'
        }
    },
    'audio_spectrum_lines': {
        'script': 'audio_spectrum_lines.py',
        'modes': {
            1: 'Classic_Bars',
            2: 'Mirror_Symmetry',
            3: 'Waterfall',
            4: 'Converging_Lines',
            5: 'Wave_Morph',
            6: 'Staggered_Pulse',
            7: 'Geometric_Tunnel',
            8: 'Dancing_Ribbons',
            9: 'Particle_Stream',
            10: 'Glitch_Art'
        }
    },
    'audio_spectrum_creative': {
        'script': 'audio_spectrum_creative.py',
        'modes': {
            1: 'Vinyl_Grooves',
            2: 'Neon_Rain',
            3: 'Jazzy_Fireworks',
            4: 'Retro_Cassette',
            5: 'Soul_Aura',
            6: 'Frequency_Flowers',
            7: 'Electric_Heartbeat',
            8: 'Pixel_Clouds',
            9: 'Liquid_Mercury',
            10: 'Cosmic_Dust',
            11: 'Quantum_Strings',
            12: 'Lava_Lamp',
            13: 'DNA_Helix',
            14: 'Lightning_Strikes',
            15: 'Morphing_Geometry',
            16: 'Ink_Drops',
            17: 'Aurora_Waves',
            18: 'Fractal_Bloom',
            19: 'Plasma_Storm',
            20: 'Crystal_Growth',
            21: 'Gravitational_Lens',
            22: 'Magnetic_Fields',
            23: 'Tribal_Drums',
            24: 'Neon_Cityscape',
            25: 'Heartbeat_Monitor',
            26: 'Ocean_Depths',
            27: 'Fire_Dance',
            28: 'Particle_Collider',
            29: 'Rainbow_Prism',
            30: 'Seismic_Waves',
            31: 'Origami_Unfold',
            32: 'Storm_Clouds',
            33: 'Binary_Matrix',
            34: 'Kaleidoscope',
            35: 'Laser_Show',
            36: 'Sandstorm',
            37: 'Ice_Shatter',
            38: 'Cellular_Division',
            39: 'Neon_Tubes',
            40: 'Cosmic_Strings',
            41: 'Paint_Splatter',
            42: 'Quantum_Foam',
            43: 'Aztec_Sun',
            44: 'Fiber_Optics',
            45: 'Tornado_Funnel',
            46: 'Hologram_Glitch',
            47: 'Starfield_Warp',
            48: 'Mandala_Growth',
            49: 'Neon_Sign_Flicker',
            50: 'Black_Hole',
            51: 'Fractal_Tree',
            52: 'Cityscape_Extrusion',
            53: 'Gravity_Well',
            54: 'Metaball_Fluid',
            55: 'Aurora_Borealis',
            56: 'Stained_Glass',
            57: 'Neon_Nerve_Network',
            58: 'Glitch_Artifact',
            59: 'Warp_Tunnel',
            60: 'Conways_Life',
            61: 'ASCII_Art',
            62: 'Rippling_Water',
            63: 'Terrain_Flyover',
            64: 'String_Art',
            65: 'Fire_Embers',
            66: 'Radial_Kaleidoscope',
            67: 'Pulsing_Jellyfish',
            68: 'Orbital_System',
            69: 'Spectrum_Cube',
            70: 'Typographic_Flow',
            71: 'Sonar_Ping',
            72: 'VU_Meters',
            73: 'Lightning_Cloud',
            74: 'Bouncing_Balls',
            75: 'Liquid_Ink',
            76: 'Stereo_Landscape',
            77: 'AI_Latent_Walk',
            78: 'Pixel_Storm',
            79: 'Growing_Vine',
            80: 'Haunted_Faces',
            81: 'Connecting_Constellations',
            82: 'Matrix_Rain',
            83: 'Voxel_World',
            84: 'DNA_Helix_Rungs',
            85: 'Audio_Reactive_Shader',
            86: 'Spirograph',
            87: 'Equalizer_Tower',
            88: 'Audio_Driven_Doodles',
            89: 'Firework_Show',
            90: 'Microscopic_View',
            91: 'Burning_Paper',
            92: 'Swarm_Intelligence',
            93: 'Pendulum_Wave',
            94: 'Retro_Scanlines',
            95: 'Pulsing_Polygon',
            96: 'Chromatic_Orb',
            97: 'Textured_Bars',
            98: 'Voronoi_Tessellation',
            99: 'Shattering_Glass',
            100: 'Sunrise_Sunset'
        }
    }
}


def extract_screenshot_from_video(video_path, output_image, timestamp='00:00:03'):
    """Extract a single frame from video at specified timestamp"""
    try:
        result = subprocess.run([
            'ffmpeg', '-y',
            '-i', video_path,
            '-ss', timestamp,
            '-vframes', '1',
            '-q:v', '2',
            output_image
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"  ✓ Screenshot saved: {output_image}")
            return True
        else:
            print(f"  ✗ Failed to extract screenshot: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ✗ Error extracting screenshot: {e}")
        return False


def generate_short_video(script_name, mode_num, output_dir):
    """Generate a short 5-second video for screenshot extraction"""
    # Create a temporary 5-second audio clip for faster processing
    temp_audio = f'/tmp/temp_audio_5s.wav'

    print(f"  Creating 5-second audio clip...")
    result = subprocess.run([
        'ffmpeg', '-y',
        '-i', AUDIO_FILE,
        '-ss', '00:00:10',  # Start at 10 seconds (usually louder)
        '-t', '5',  # 5 seconds duration
        temp_audio
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print(f"  ✗ Failed to create temp audio: {result.stderr}")
        return None

    # Generate video
    temp_video = f'/tmp/temp_video_mode{mode_num}.mov'

    cmd = [
        'python',
        script_name,
        temp_audio,
        temp_video,
        '--mode', str(mode_num)
    ]

    print(f"  Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Clean up temp audio
    Path(temp_audio).unlink(missing_ok=True)

    if result.returncode == 0 and Path(temp_video).exists():
        return temp_video
    else:
        print(f"  ✗ Video generation failed")
        print(result.stderr)
        return None


def main():
    print("=" * 80)
    print("AUDIO SPECTRUM CATALOG GENERATOR")
    print("=" * 80)
    print()

    # Check if audio file exists
    if not Path(AUDIO_FILE).exists():
        print(f"Error: Audio file not found: {AUDIO_FILE}")
        sys.exit(1)

    # Total count
    total_modes = sum(len(info['modes']) for info in SCRIPTS.values())
    print(f"Total modes to process: {total_modes}")
    print()

    current = 0

    # Process each script
    for script_key, script_info in SCRIPTS.items():
        script_name = script_info['script']
        modes = script_info['modes']
        output_dir = Path(CATALOG_DIR) / script_key

        print(f"\n{'='*80}")
        print(f"Processing: {script_name} ({len(modes)} modes)")
        print(f"{'='*80}\n")

        # Process each mode
        for mode_num, mode_name in modes.items():
            current += 1
            print(f"\n[{current}/{total_modes}] Mode {mode_num}: {mode_name}")
            print("-" * 60)

            # Output image path
            output_image = output_dir / f"mode_{mode_num:02d}_{mode_name}.png"

            # Check if already exists
            if output_image.exists():
                print(f"  ⚠ Already exists, skipping: {output_image}")
                continue

            # Generate short video
            temp_video = generate_short_video(script_name, mode_num, output_dir)

            if temp_video:
                # Extract screenshot at 2.5 seconds (middle of the 5-second clip, peak moment)
                if extract_screenshot_from_video(temp_video, str(output_image), '00:00:02.5'):
                    print(f"  ✓ Completed: mode {mode_num}")

                # Clean up temp video
                Path(temp_video).unlink(missing_ok=True)
            else:
                print(f"  ✗ Failed to generate mode {mode_num}")

            # Small delay to prevent overwhelming the system
            time.sleep(0.5)

    print("\n" + "=" * 80)
    print("CATALOG GENERATION COMPLETE!")
    print("=" * 80)
    print(f"\nScreenshots saved to: {CATALOG_DIR}")
    print("\nFolder structure:")
    for script_key in SCRIPTS.keys():
        folder = Path(CATALOG_DIR) / script_key
        count = len(list(folder.glob("*.png"))) if folder.exists() else 0
        print(f"  {script_key}/  ({count} images)")


if __name__ == '__main__':
    main()

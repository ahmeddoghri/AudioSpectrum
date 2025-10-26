#!/usr/bin/env python3
"""
Unified Catalog Builder

Generates short preview videos for all visualizer modes and writes a local HTML
gallery page to browse and play them quickly.

- Discovers modes dynamically (by scanning source files) with safe fallbacks
  for classic/lines scripts.
- Creates a 4s preview audio slice to speed up generation.
- Renders previews to catalog/video_previews/*.webm (480x480) for fast browsing.
- Writes catalog/index.html that auto-loads all generated previews.
"""

import re
import sys
import json
import time
import shlex
import subprocess
from pathlib import Path
import os


# Configuration
AUDIO_FILE = Path('turkish-national-anthem.wav')
PREVIEWS_DIR = Path('catalog/video_previews')
OUTPUT_HTML = Path('catalog/index.html')

# Mode metadata - descriptions and tags for each mode
MODE_METADATA = {
    'audio_spectrum_creative': {
        1: {"name": "Vinyl Grooves", "desc": "Rotating circular grooves like a vinyl record", "tags": ["lofi", "retro"]},
        2: {"name": "Neon Rain", "desc": "Cyberpunk neon droplets cascading down", "tags": ["cyberpunk", "lofi"]},
        3: {"name": "Jazzy Fireworks", "desc": "Bursting particles from center", "tags": ["jazz", "explosive"]},
        4: {"name": "Retro Cassette", "desc": "VU meters and tape reel animation", "tags": ["vintage", "lofi"]},
        5: {"name": "Soul Aura", "desc": "Pulsing organic blob with soul vibes", "tags": ["soul", "rnb"]},
        6: {"name": "Frequency Flowers", "desc": "Blooming petals that grow with music", "tags": ["dreamy", "lofi"]},
        7: {"name": "Electric Heartbeat", "desc": "EKG-style waveform with emotional glow", "tags": ["emotional", "jazz"]},
        8: {"name": "Pixel Clouds", "desc": "8-bit style floating clouds", "tags": ["retro", "lofi"]},
        9: {"name": "Liquid Mercury", "desc": "Flowing metallic waves", "tags": ["smooth", "jazz"]},
        10: {"name": "Cosmic Dust", "desc": "Swirling galaxy particles with trails", "tags": ["ambient", "lofi"]},
        11: {"name": "Quantum Strings", "desc": "Vibrating strings with interference", "tags": ["experimental", "physics"]},
        12: {"name": "Lava Lamp", "desc": "Rising and morphing organic blobs", "tags": ["psychedelic", "lofi"]},
        13: {"name": "DNA Helix", "desc": "Double helix twisting with music", "tags": ["scientific", "bio"]},
        14: {"name": "Lightning Strikes", "desc": "Electric bolts connecting peaks", "tags": ["intense", "energy"]},
        15: {"name": "Morphing Geometry", "desc": "Shifting 3D wireframe shapes", "tags": ["abstract", "modern"]},
        16: {"name": "Ink Drops", "desc": "Organic ink dispersing in water", "tags": ["artistic", "lofi"]},
        17: {"name": "Aurora Waves", "desc": "Northern lights flowing ribbons", "tags": ["ethereal", "ambient"]},
        18: {"name": "Fractal Bloom", "desc": "Self-similar mathematical patterns", "tags": ["mathematical", "art"]},
        19: {"name": "Plasma Storm", "desc": "Swirling energy vortex", "tags": ["chaotic", "energy"]},
        20: {"name": "Crystal Growth", "desc": "Geometric crystals forming", "tags": ["elegant", "minimal"]},
        21: {"name": "Gravitational Lens", "desc": "Spacetime warping light", "tags": ["cosmic", "scifi"]},
        22: {"name": "Magnetic Fields", "desc": "Iron filing patterns", "tags": ["scientific", "art"]},
        23: {"name": "Tribal Drums", "desc": "Concentric ethnic shockwaves", "tags": ["world", "music"]},
        24: {"name": "Neon Cityscape", "desc": "Scrolling city with reactive buildings", "tags": ["synthwave", "urban"]},
        25: {"name": "Heartbeat Monitor", "desc": "Medical vital signs", "tags": ["dramatic", "tension"]},
        26: {"name": "Ocean Depths", "desc": "Bioluminescent creatures", "tags": ["underwater", "mystery"]},
        27: {"name": "Fire Dance", "desc": "Realistic flames dancing", "tags": ["primal", "energy"]},
        28: {"name": "Particle Collider", "desc": "High-energy physics", "tags": ["science", "physics"]},
        29: {"name": "Rainbow Prism", "desc": "Light refraction", "tags": ["optical", "colorful"]},
        30: {"name": "Seismic Waves", "desc": "Earthquake readings", "tags": ["geological", "drama"]},
        31: {"name": "Origami Unfold", "desc": "Paper geometric folding", "tags": ["japanese", "art"]},
        32: {"name": "Storm Clouds", "desc": "Thunder and lightning", "tags": ["epic", "weather"]},
        33: {"name": "Binary Matrix", "desc": "Matrix-style code", "tags": ["hacker", "cyber"]},
        34: {"name": "Kaleidoscope", "desc": "Mirrored symmetric patterns", "tags": ["psychedelic", "symmetry"]},
        35: {"name": "Laser Show", "desc": "Concert laser beams", "tags": ["edm", "concert"]},
        36: {"name": "Sandstorm", "desc": "Desert particles in wind", "tags": ["natural", "chaos"]},
        37: {"name": "Ice Shatter", "desc": "Cracking ice surface", "tags": ["dramatic", "tension"]},
        38: {"name": "Cellular Division", "desc": "Cells splitting", "tags": ["biology", "organic"]},
        39: {"name": "Neon Tubes", "desc": "Glowing tubes bending", "tags": ["futuristic", "minimal"]},
        40: {"name": "Cosmic Strings", "desc": "Universe-scale energy", "tags": ["theoretical", "physics"]},
        41: {"name": "Paint Splatter", "desc": "Pollock drip painting", "tags": ["abstract", "expressionism"]},
        42: {"name": "Quantum Foam", "desc": "Bubbling spacetime", "tags": ["extreme", "physics"]},
        43: {"name": "Aztec Sun", "desc": "Ancient calendar rotating", "tags": ["ancient", "civilization"]},
        44: {"name": "Fiber Optics", "desc": "Light through cables", "tags": ["tech", "modern"]},
        45: {"name": "Tornado Funnel", "desc": "Swirling debris vortex", "tags": ["natural", "disaster"]},
        46: {"name": "Hologram Glitch", "desc": "Futuristic projection errors", "tags": ["cyberpunk", "tech"]},
        47: {"name": "Starfield Warp", "desc": "Hyperspace jump", "tags": ["scifi", "space"]},
        48: {"name": "Mandala Growth", "desc": "Sacred geometry forming", "tags": ["spiritual", "art"]},
        49: {"name": "Neon Sign Flicker", "desc": "Vintage neon buzzing", "tags": ["retro", "urban"]},
        50: {"name": "Black Hole", "desc": "Event horizon lensing", "tags": ["cosmic", "destruction"]},
        51: {"name": "Fractal Tree", "desc": "Generative tree that grows with branches on bass, blooms on treble", "tags": ["hypnotic", "generative", "nature"], "new": True},
        52: {"name": "Cityscape Extrusion", "desc": "3D city blocks extruding with frequency", "tags": ["hypnotic", "3d", "urban"], "new": True},
        53: {"name": "Gravity Well", "desc": "Particles pulled by pulsing bass center, pushed by treble", "tags": ["hypnotic", "physics", "particles"], "new": True},
        54: {"name": "Metaball Fluid", "desc": "Lava lamp metaballs pulsing with frequencies", "tags": ["hypnotic", "fluid", "psychedelic"], "new": True},
        55: {"name": "Aurora Borealis", "desc": "Northern lights curtains with shimmering treble", "tags": ["hypnotic", "nature", "ethereal"], "new": True},
        56: {"name": "Stained Glass", "desc": "Glowing church window panes", "tags": ["hypnotic", "artistic", "glow"], "new": True},
        57: {"name": "Neon Nerve Network", "desc": "Neural synapses firing with music", "tags": ["hypnotic", "biological", "neon"], "new": True},
        58: {"name": "Glitch Artifact", "desc": "Datamosh corruption on transients", "tags": ["hypnotic", "glitch", "corrupt"], "new": True},
        59: {"name": "Warp Tunnel", "desc": "Hyperspace rings pulsing with depth", "tags": ["hypnotic", "scifi", "tunnel"], "new": True},
        60: {"name": "Conway's Life", "desc": "Cellular automaton modulated by audio", "tags": ["hypnotic", "algorithmic", "life"], "new": True},
        61: {"name": "ASCII Art", "desc": "Text character visualizer bars", "tags": ["hypnotic", "retro", "ascii"], "new": True},
        62: {"name": "Rippling Water", "desc": "Interference patterns from frequency raindrops", "tags": ["hypnotic", "water", "ripples"], "new": True},
        63: {"name": "Terrain Flyover", "desc": "3D wireframe landscape from waveform", "tags": ["hypnotic", "3d", "landscape"], "new": True},
        64: {"name": "String Art", "desc": "Geometric lines connecting points", "tags": ["hypnotic", "geometric", "lines"], "new": True},
        65: {"name": "Fire & Embers", "desc": "Central flames with sparks on treble", "tags": ["hypnotic", "fire", "primal"], "new": True},
        66: {"name": "Radial Kaleidoscope", "desc": "Mirrored segments with bass pulse", "tags": ["hypnotic", "kaleidoscope", "radial"], "new": True},
        67: {"name": "Pulsing Jellyfish", "desc": "Bell pulses with bass, tentacle waveforms", "tags": ["hypnotic", "aquatic", "organic"], "new": True},
        68: {"name": "Orbital System", "desc": "Sun with orbiting planets and moons", "tags": ["hypnotic", "space", "orbital"], "new": True},
        69: {"name": "Spectrum Cube", "desc": "Rotating 3D cube with visualizers on faces", "tags": ["hypnotic", "3d", "cube"], "new": True},
        70: {"name": "Typographic Flow", "desc": "Floating words with wavy treble", "tags": ["hypnotic", "typography", "words"], "new": True},
        71: {"name": "Sonar Ping", "desc": "Radar sweep with frequency blips", "tags": ["hypnotic", "radar", "sonar"], "new": True},
        72: {"name": "VU Meters", "desc": "Analog needle physics meters", "tags": ["hypnotic", "analog", "retro"], "new": True},
        73: {"name": "Lightning Cloud", "desc": "Storm cloud with treble lightning", "tags": ["hypnotic", "storm", "lightning"], "new": True},
        74: {"name": "Bouncing Balls", "desc": "Physics-based ball bouncing per frequency", "tags": ["hypnotic", "physics", "bouncing"], "new": True},
        75: {"name": "Liquid Ink", "desc": "Ink blooms in water - bass & treble", "tags": ["hypnotic", "ink", "liquid"], "new": True},
        76: {"name": "Stereo Landscape", "desc": "L/R channel mountains in 3D perspective", "tags": ["hypnotic", "stereo", "landscape"], "new": True},
        77: {"name": "AI Latent Walk", "desc": "Generative dream-like morphing", "tags": ["hypnotic", "ai", "generative"], "new": True},
        78: {"name": "Pixel Storm", "desc": "8-bit blizzard with stereo wind", "tags": ["hypnotic", "8bit", "storm"], "new": True},
        79: {"name": "Growing Vine", "desc": "Organic vine with leaves on beats", "tags": ["hypnotic", "organic", "growth"], "new": True},
        80: {"name": "Haunted Faces", "desc": "Ghostly faces with glowing eyes on bass", "tags": ["hypnotic", "spooky", "faces"], "new": True},
        81: {"name": "Connecting Constellations", "desc": "Stars that shine and connect", "tags": ["hypnotic", "stars", "network"], "new": True},
        82: {"name": "Matrix Rain", "desc": "Falling code with treble brightness", "tags": ["hypnotic", "matrix", "code"], "new": True},
        83: {"name": "Voxel World", "desc": "3D voxel shockwave emanating", "tags": ["hypnotic", "voxel", "3d"], "new": True},
        84: {"name": "DNA Helix Rungs", "desc": "Genetic code with glowing rungs", "tags": ["hypnotic", "dna", "biological"], "new": True},
        85: {"name": "Audio-Reactive Shader", "desc": "Procedural noise patterns", "tags": ["hypnotic", "shader", "procedural"], "new": True},
        86: {"name": "Spirograph", "desc": "Mathematical curves from frequencies", "tags": ["hypnotic", "spirograph", "curves"], "new": True},
        87: {"name": "Equalizer Tower", "desc": "Stacked glowing rings in 3D", "tags": ["hypnotic", "3d", "tower"], "new": True},
        88: {"name": "Audio-Driven Doodles", "desc": "Generative doodle bot art", "tags": ["hypnotic", "generative", "doodle"], "new": True},
        89: {"name": "Firework Show", "desc": "Bass launches rockets that explode", "tags": ["hypnotic", "fireworks", "explosive"], "new": True},
        90: {"name": "Microscopic View", "desc": "Cells jiggling and dividing", "tags": ["hypnotic", "microscopic", "cells"], "new": True},
        91: {"name": "Burning Paper", "desc": "Flame bars with embers and curling", "tags": ["hypnotic", "fire", "burning"], "new": True},
        92: {"name": "Swarm Intelligence", "desc": "Boid flocking with audio forces", "tags": ["hypnotic", "swarm", "flock"], "new": True},
        93: {"name": "Pendulum Wave", "desc": "Multiple pendulums with different periods", "tags": ["hypnotic", "pendulum", "wave"], "new": True},
        94: {"name": "Retro Scanlines", "desc": "CRT monitor with static", "tags": ["hypnotic", "crt", "retro"], "new": True},
        95: {"name": "Pulsing Polygon", "desc": "Central shape with pushed vertices", "tags": ["hypnotic", "polygon", "geometric"], "new": True},
        96: {"name": "Chromatic Orb", "desc": "3D sphere with moving light source", "tags": ["hypnotic", "3d", "chromatic"], "new": True},
        97: {"name": "Textured Bars", "desc": "Bars with scrolling animated patterns", "tags": ["hypnotic", "textured", "scrolling"], "new": True},
        98: {"name": "Voronoi Tessellation", "desc": "Cellular diagram with moving seeds", "tags": ["hypnotic", "voronoi", "tessellation"], "new": True},
        99: {"name": "Shattering Glass", "desc": "Glass pane cracking on beats", "tags": ["hypnotic", "glass", "shatter"], "new": True},
        100: {"name": "Sunrise/Sunset", "desc": "Gradient sky with pulsing sun and stars", "tags": ["hypnotic", "sky", "gradient"], "new": True}
    },
    'audio_spectrum': {
        1: {"name": "Bars", "desc": "Classic vertical bars", "tags": ["classic", "simple"]},
        2: {"name": "Waves & Layers", "desc": "Layered wave patterns", "tags": ["classic", "waves"]},
        3: {"name": "Particles", "desc": "Particle system", "tags": ["classic", "particles"]},
        4: {"name": "Waveform", "desc": "Traditional waveform", "tags": ["classic", "waveform"]},
        5: {"name": "Polygon", "desc": "Geometric polygon", "tags": ["classic", "geometric"]},
        6: {"name": "Spiral", "desc": "Spiral pattern", "tags": ["classic", "spiral"]},
        7: {"name": "DNA Helix", "desc": "Helix structure", "tags": ["classic", "dna"]},
        8: {"name": "Kaleidoscope", "desc": "Mirror symmetry", "tags": ["classic", "kaleidoscope"]},
        9: {"name": "Pulse Rings", "desc": "Pulsing rings", "tags": ["classic", "rings"]},
        10: {"name": "Star Burst", "desc": "Starburst effect", "tags": ["classic", "burst"]}
    },
    'audio_spectrum_lines': {
        1: {"name": "Classic Bars", "desc": "Traditional vertical bars", "tags": ["lines", "classic"]},
        2: {"name": "Mirror Symmetry", "desc": "Mirrored visualization", "tags": ["lines", "mirror"]},
        3: {"name": "Waterfall", "desc": "Cascading effect", "tags": ["lines", "waterfall"]},
        4: {"name": "Converging Lines", "desc": "Lines meeting at center", "tags": ["lines", "converging"]},
        5: {"name": "Wave Morph", "desc": "Morphing wave patterns", "tags": ["lines", "wave"]},
        6: {"name": "Staggered Pulse", "desc": "Offset pulsing bars", "tags": ["lines", "pulse"]},
        7: {"name": "Geometric Tunnel", "desc": "3D tunnel effect", "tags": ["lines", "3d"]},
        8: {"name": "Dancing Ribbons", "desc": "Flowing ribbons", "tags": ["lines", "ribbons"]},
        9: {"name": "Particle Stream", "desc": "Particle streams", "tags": ["lines", "particles"]},
        10: {"name": "Glitch Art", "desc": "Glitch aesthetic", "tags": ["lines", "glitch"]}
    }
}

# Source scripts
SCRIPTS = {
    'audio_spectrum': Path('audio_spectrum.py'),
    'audio_spectrum_lines': Path('audio_spectrum_lines.py'),
    'audio_spectrum_creative': Path('audio_spectrum_creative.py'),
}

# Fallback modes when discovery fails
FALLBACK_MODES = {
    'audio_spectrum': list(range(1, 11)),
    'audio_spectrum_lines': list(range(1, 11)),
    # Creative modes now go up to 300
    'audio_spectrum_creative': list(range(1, 301)),
}


def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, **kwargs)


def ensure_dirs() -> None:
    PREVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)


def create_preview_audio() -> str | None:
    """Create a 4-second audio clip (6-10s) for faster preview generation."""
    temp_audio = PREVIEWS_DIR / 'preview_audio_4s.wav'
    cmd = [
        'ffmpeg', '-y',
        '-i', str(AUDIO_FILE),
        '-ss', '00:00:06',
        '-t', '4',
        str(temp_audio)
    ]
    print(f"Creating preview audio: {' '.join(shlex.quote(x) for x in cmd)}")
    res = run(cmd)
    if res.returncode != 0:
        print(f"✗ Failed to create preview audio: {res.stderr[:200]}")
        return None
    print(f"✓ Created: {temp_audio}")
    return str(temp_audio)


def discover_modes(script_key: str, script_path: Path) -> list[int]:
    """Discover available modes by scanning for draw_mode_XXX functions.
    Falls back to predefined ranges when unspecified.
    """
    nums = set()

    # Scan main script
    try:
        src = script_path.read_text(encoding='utf-8', errors='ignore')
        nums.update(int(m.group(1)) for m in re.finditer(r"def\s+draw_mode_(\d+)_", src))
    except Exception:
        print(f"Warning: could not read {script_path}")

    # For audio_spectrum_creative, also scan modes/ directory
    if script_key == 'audio_spectrum_creative':
        modes_dir = Path('modes')
        if modes_dir.exists():
            for mode_file in modes_dir.glob('mode_*.py'):
                try:
                    src = mode_file.read_text(encoding='utf-8', errors='ignore')
                    nums.update(int(m.group(1)) for m in re.finditer(r"def\s+draw_mode_(\d+)_", src))
                except Exception:
                    pass

    if nums:
        modes = sorted(nums)
        print(f"Discovered {len(modes)} modes for {script_key}: {modes[0]}..{modes[-1]}")
        return modes

    print(f"No draw_mode_* found for {script_key}, using fallback")
    return FALLBACK_MODES.get(script_key, [])


def parse_mode_names(script_path: Path) -> dict[int, str]:
    """Parse mode names from function names like draw_mode_XXX_name_here."""
    result: dict[int, str] = {}

    # Parse from main script
    try:
        src = script_path.read_text(encoding='utf-8', errors='ignore')
        # Look for draw_mode_<num>_<name> patterns
        for m in re.finditer(r"def\s+draw_mode_(\d+)_([a-z_]+)", src):
            num = int(m.group(1))
            name = m.group(2).replace('_', ' ').title()
            result[num] = name
    except Exception:
        pass

    # For audio_spectrum_creative, also scan modes/ directory
    if script_path.stem == 'audio_spectrum_creative':
        modes_dir = Path('modes')
        if modes_dir.exists():
            for mode_file in modes_dir.glob('mode_*.py'):
                try:
                    src = mode_file.read_text(encoding='utf-8', errors='ignore')
                    for m in re.finditer(r"def\s+draw_mode_(\d+)_([a-z_]+)", src):
                        num = int(m.group(1))
                        name = m.group(2).replace('_', ' ').title()
                        result[num] = name
                except Exception:
                    pass

    return result


def generate_preview(script_path: Path, mode: int, preview_audio: str) -> str | None:
    out_name = f"{script_path.stem}_mode_{mode:03d}.mov"
    output_video = PREVIEWS_DIR / out_name
    if output_video.exists():
        print(f"  ⚠ Exists, skip: {out_name}")
        return str(output_video)

    cmd = [
        'python', str(script_path),
        preview_audio,
        str(output_video),
        '--mode', str(mode),
        '--width', '480',
        '--height', '480'
    ]
    print(f"  ▶ Generating {out_name}")
    env = os.environ.copy()
    env['AS_PREVIEW'] = '1'  # force fast preview path
    res = run(cmd, env=env)
    if res.returncode == 0 and output_video.exists():
        print(f"  ✓ Generated: {out_name}")
        return str(output_video)
    print(f"  ✗ Failed: {out_name}")
    if res.stderr:
        print(res.stderr[:400])
    return None


def scan_generated_previews() -> dict[str, list[dict]]:
    """Return mapping script_key -> list of {num, path, has_webm} for all previews found."""
    previews: dict[str, list[dict]] = {k: [] for k in SCRIPTS.keys()}

    # Scan for all video files (prefer webm, fallback to mov)
    seen = set()
    for ext in ['webm', 'mov']:
        for p in sorted(PREVIEWS_DIR.glob(f'*.{ext}')):
            m = re.match(r"(audio_spectrum(?:_lines|_creative)?)_mode_(\d{3})\.(webm|mov)$", p.name)
            if not m:
                continue
            script_stem = m.group(1)
            num = int(m.group(2))

            # Map stem to key in SCRIPTS
            key = 'audio_spectrum_creative' if script_stem == 'audio_spectrum_creative' else (
                'audio_spectrum_lines' if script_stem == 'audio_spectrum_lines' else 'audio_spectrum')

            # Create unique identifier
            unique_id = f"{key}_{num}"

            # Only add if not already seen, prefer webm
            if unique_id not in seen:
                # Check if webm exists
                webm_path = PREVIEWS_DIR / f"{script_stem}_mode_{num:03d}.webm"
                has_webm = webm_path.exists()

                previews[key].append({
                    'num': num,
                    'path': p.name,
                    'has_webm': has_webm
                })
                seen.add(unique_id)

    # Sort by mode number
    for key in previews:
        previews[key].sort(key=lambda d: d['num'])
    return previews


def write_html(previews: dict[str, list[dict]], names: dict[str, dict[int, str]]) -> None:
    total = sum(len(v) for v in previews.values())

    # Count by category
    creative_count = len(previews.get('audio_spectrum_creative', []))
    classic_count = len(previews.get('audio_spectrum', []))
    lines_count = len(previews.get('audio_spectrum_lines', []))
    hypnotic_count = len([p for p in previews.get('audio_spectrum_creative', []) if p['num'] >= 51 and p['num'] <= 100])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Audio Spectrum Visualizer - Video Preview Gallery</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            min-height: 100vh;
        }}

        .header {{
            text-align: center;
            padding: 40px 20px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 20px;
            margin-bottom: 40px;
            backdrop-filter: blur(10px);
        }}

        .header h1 {{
            font-size: 3em;
            margin-bottom: 10px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradient 3s ease infinite;
        }}

        @keyframes gradient {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        .header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}

        .stats {{
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 20px;
            flex-wrap: wrap;
        }}

        .stat {{
            background: rgba(255, 255, 255, 0.1);
            padding: 15px 30px;
            border-radius: 10px;
            backdrop-filter: blur(5px);
        }}

        .stat-number {{
            font-size: 2em;
            font-weight: bold;
            color: #4ecdc4;
        }}

        .filters {{
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }}

        .filter-btn {{
            background: rgba(255, 255, 255, 0.2);
            border: 2px solid rgba(255, 255, 255, 0.3);
            color: white;
            padding: 12px 25px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1em;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }}

        .filter-btn:hover {{
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
        }}

        .filter-btn.active {{
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            border-color: transparent;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }}

        .gallery {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 25px;
            padding: 20px;
        }}

        .preview-card {{
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            overflow: hidden;
            transition: all 0.3s ease;
            cursor: pointer;
            backdrop-filter: blur(10px);
            border: 2px solid transparent;
        }}

        .preview-card:hover {{
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5);
            border-color: rgba(78, 205, 196, 0.5);
        }}

        .video-container {{
            position: relative;
            width: 100%;
            padding-top: 56.25%;
            background: #000;
            overflow: hidden;
        }}

        .video-container video {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}

        .card-info {{
            padding: 20px;
        }}

        .mode-number {{
            display: inline-block;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
            margin-bottom: 10px;
        }}

        .mode-name {{
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 8px;
        }}

        .mode-desc {{
            opacity: 0.8;
            font-size: 0.95em;
            line-height: 1.4;
            margin-bottom: 8px;
        }}

        .search-box {{
            max-width: 600px;
            margin: 0 auto 30px;
        }}

        .search-box input {{
            width: 100%;
            padding: 15px 25px;
            border-radius: 30px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            background: rgba(255, 255, 255, 0.1);
            color: white;
            font-size: 1.1em;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }}

        .search-box input::placeholder {{
            color: rgba(255, 255, 255, 0.6);
        }}

        .search-box input:focus {{
            outline: none;
            border-color: #4ecdc4;
            background: rgba(255, 255, 255, 0.2);
        }}

        .tag {{
            display: inline-block;
            background: rgba(255, 255, 255, 0.15);
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.8em;
            margin-right: 5px;
            margin-top: 5px;
        }}

        .new-badge {{
            background: linear-gradient(45deg, #ff6b6b, #ee5a6f);
            color: white;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.75em;
            font-weight: bold;
            margin-left: 8px;
            animation: glow 2s ease-in-out infinite;
        }}

        @keyframes glow {{
            0%, 100% {{ box-shadow: 0 0 5px rgba(255, 107, 107, 0.5); }}
            50% {{ box-shadow: 0 0 20px rgba(255, 107, 107, 0.8), 0 0 30px rgba(255, 107, 107, 0.6); }}
        }}

        .hypnotic {{
            animation: pulse 2s ease-in-out infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.6; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1 class="hypnotic">🎵 Audio Spectrum Visualizer 🎵</h1>
        <p>Interactive Video Preview Gallery - Auto-Generated from Source</p>
        <div class="stats">
            <div class="stat">
                <div class="stat-number">{creative_count}</div>
                <div>Creative Modes</div>
            </div>
            <div class="stat">
                <div class="stat-number">{classic_count}</div>
                <div>Classic Modes</div>
            </div>
            <div class="stat">
                <div class="stat-number">{lines_count}</div>
                <div>Line Modes</div>
            </div>
            <div class="stat">
                <div class="stat-number">{total}</div>
                <div>Total Visualizations</div>
            </div>
        </div>
    </div>

    <div class="search-box">
        <input type="text" id="searchInput" placeholder="🔍 Search visualizations... (e.g., 'hypnotic', 'fractal', 'neon')">
    </div>

    <div class="filters">
        <button class="filter-btn active" data-filter="all">All ({total})</button>
        <button class="filter-btn" data-filter="creative">Creative ({creative_count}){' <span class="new-badge">HOT!</span>' if creative_count > 0 else ''}</button>
        <button class="filter-btn" data-filter="classic">Classic ({classic_count})</button>
        <button class="filter-btn" data-filter="lines">Lines ({lines_count})</button>
        <button class="filter-btn" data-filter="hypnotic">Hypnotic ({hypnotic_count}){' <span class="new-badge">NEW!</span>' if hypnotic_count > 0 else ''}</button>
    </div>

    <div class="gallery" id="gallery">
"""

    # Generate cards for each mode
    for key in ['audio_spectrum_creative', 'audio_spectrum', 'audio_spectrum_lines']:
        items = previews.get(key, [])
        for it in items:
            num = it['num']

            # Get metadata
            metadata = MODE_METADATA.get(key, {}).get(num, {})
            name = metadata.get('name', f"Mode {num}")
            desc = metadata.get('desc', '')
            tags = metadata.get('tags', [])
            is_new = metadata.get('new', False)

            # Determine filter category
            filter_class = key.replace('audio_spectrum_', '') if key != 'audio_spectrum' else 'classic'
            if key == 'audio_spectrum_creative' and num >= 51 and num <= 100:
                filter_class += ' hypnotic'

            # Get base path without extension
            base_name = it['path'].rsplit('.', 1)[0]

            # Determine video sources
            webm_src = f"video_previews/{base_name}.webm"
            mov_src = f"video_previews/{base_name}.mov"

            new_badge = '<span class="new-badge">NEW!</span>' if is_new else ''

            html += f"""
        <div class="preview-card" data-category="{filter_class}" data-searchable="{name.lower()} {desc.lower()} {' '.join(tags).lower()} mode{num}">
            <div class="video-container">
                <video loop muted playsinline preload="auto">
                    <source src="{webm_src}" type="video/webm">
                    <source src="{mov_src}" type="video/quicktime">
                    Your browser does not support the video tag.
                </video>
            </div>
            <div class="card-info">
                <div class="mode-number">Mode {num}{new_badge}</div>
                <div class="mode-name">{name}</div>
"""
            if desc:
                html += f'                <div class="mode-desc">{desc}</div>\n'
            if tags:
                html += '                <div>\n'
                for tag in tags:
                    html += f'                    <span class="tag">{tag}</span>\n'
                html += '                </div>\n'

            html += """            </div>
        </div>
"""

    html += """    </div>

    <script>
        // Wait for DOM to be ready
        document.addEventListener('DOMContentLoaded', function() {
            // Filter functionality
            const filterBtns = document.querySelectorAll('.filter-btn');
            const cards = document.querySelectorAll('.preview-card');
            const searchInput = document.getElementById('searchInput');
            const videos = document.querySelectorAll('video');

            console.log(`Initializing ${videos.length} videos...`);

            // Initialize videos with hover events
            videos.forEach((video, index) => {
                // Load video
                video.load();

                // Get the card container
                const card = video.closest('.preview-card');

                if (card) {
                    // Mouse enter - play video
                    card.addEventListener('mouseenter', function() {
                        const playPromise = video.play();

                        if (playPromise !== undefined) {
                            playPromise.catch(err => {
                                console.warn(`Video ${index} play failed:`, err.message);
                            });
                        }
                    });

                    // Mouse leave - pause and reset
                    card.addEventListener('mouseleave', function() {
                        video.pause();
                        video.currentTime = 0;
                    });
                }
            });

            console.log('Videos initialized successfully!');

            // Filter button handlers
            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    filterBtns.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    applyFilters();
                });
            });

            // Search input handler
            searchInput.addEventListener('input', () => {
                applyFilters();
            });

            function applyFilters() {
                const activeFilter = document.querySelector('.filter-btn.active').dataset.filter;
                const searchTerm = searchInput.value.toLowerCase();

                cards.forEach(card => {
                    const category = card.dataset.category;
                    const searchable = card.dataset.searchable;

                    let matchesFilter = activeFilter === 'all' || category.includes(activeFilter);
                    let matchesSearch = !searchTerm || searchable.includes(searchTerm);

                    if (matchesFilter && matchesSearch) {
                        card.style.display = '';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }
        });
    </script>
</body>
</html>
"""

    OUTPUT_HTML.write_text(html, encoding='utf-8')
    print(f"\n✓ Wrote HTML: {OUTPUT_HTML}")


def main() -> None:
    print("="*80)
    print("BUILD CATALOG: previews + HTML")
    print("="*80)

    # Checks
    ensure_dirs()
    if not AUDIO_FILE.exists():
        print(f"Error: Audio file not found: {AUDIO_FILE}")
        sys.exit(1)

    # Discover modes and names
    all_modes: dict[str, list[int]] = {}
    all_names: dict[str, dict[int, str]] = {}
    for key, path in SCRIPTS.items():
        modes = discover_modes(key, path)
        all_modes[key] = modes
        all_names[key] = parse_mode_names(path)

    # Create preview audio
    preview_audio = create_preview_audio()
    if not preview_audio:
        sys.exit(1)

    # Generate previews
    total = sum(len(v) for v in all_modes.values())
    done = 0
    for key, path in SCRIPTS.items():
        modes = all_modes[key]
        print(f"\n-- {path.name}: {len(modes)} modes")
        for m in modes:
            done += 1
            print(f"[{done}/{total}] {path.name} mode {m}")
            generate_preview(path, m, preview_audio)
            time.sleep(0.1)

    # Build HTML from generated previews
    previews = scan_generated_previews()
    write_html(previews, all_names)

    print("\nAll done.")


if __name__ == '__main__':
    main()



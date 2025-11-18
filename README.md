# Circular Audio Spectrum Visualizer

Generate stunning circular audio spectrum animations with transparent backgrounds, perfect for overlaying on videos in editing software.

## How to Run

### Web App (Recommended)

```bash
# Navigate to the web directory
cd web

# Option 1: Open directly in browser
open index.html

# Option 2: Use Python's built-in HTTP server
python3 -m http.server 8000
# Then visit http://localhost:8000 in your browser

# Option 3: Use Node's http-server (if installed)
npx http-server -p 8000
```

### Python Script (Command Line)

```bash
# Install dependencies
pip install -r requirements.txt

# Run with your audio file
python audio_spectrum.py input.mp3 output.mov
```

## Features

- Circular spectrum that radiates outward
- Transparent background for easy compositing
- Supports MP3 and WAV audio files
- Customizable colors, size, and animation parameters
- Smooth, responsive animation that maps exactly to your audio

## Installation

1. Install Python 3.8 or higher if you don't have it already

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install librosa numpy opencv-python scipy
```

## Quick Start

Basic usage with default settings (1080x1080, cyan color):

```bash
python audio_spectrum.py input.mp3 output.mov
```

Or with a WAV file:

```bash
python audio_spectrum.py input.wav output.mov
```

## Advanced Options

Customize your visualization:

```bash
python audio_spectrum.py input.mp3 output.mov \
  --width 1920 \
  --height 1080 \
  --color 255 0 255 \
  --num-bars 180 \
  --fps 60
```

### Available Options

- `--width`: Video width in pixels (default: 1080)
- `--height`: Video height in pixels (default: 1080)
- `--fps`: Frames per second (default: 30, try 60 for smoother animation)
- `--num-bars`: Number of frequency bars around the circle (default: 120)
- `--color R G B`: RGB color values 0-255 (default: 0 255 255 = cyan)
- `--inner-radius`: Size of the center circle in pixels (default: 150)
- `--bar-width`: Bar thickness multiplier (default: 1.5)
- `--smoothing`: Animation smoothing 0-1 (default: 0.7, higher = smoother)

### Example Presets

**Purple/Magenta for Burning Man aesthetic:**
```bash
python audio_spectrum.py input.mp3 output.mov --color 255 0 255
```

**High resolution with more bars:**
```bash
python audio_spectrum.py input.mp3 output.mov --width 1920 --height 1080 --num-bars 200
```

**Smaller center, larger spikes:**
```bash
python audio_spectrum.py input.mp3 output.mov --inner-radius 100
```

**Super smooth 60fps:**
```bash
python audio_spectrum.py input.mp3 output.mov --fps 60
```

## Using in Video Editors

### Output Format

The script outputs a `.mov` file which works best for transparency. The visualization is rendered with the spectrum visible against a black background.

### Applying as a Mask

**In Adobe Premiere Pro:**
1. Import your output.mov file
2. Place it on a track above your background
3. Go to Effect Controls > Opacity
4. Change Blend Mode to "Screen" or "Add" (removes black)
5. Or use "Track Matte Key" effect for more control

**In Final Cut Pro:**
1. Import your output.mov file
2. Place it above your background layer
3. Change Blend Mode to "Screen" or "Add"
4. Or use as a Luma Matte

**In DaVinci Resolve:**
1. Import your output.mov file
2. Place it above your background in the timeline
3. Change Composite Mode to "Screen" or "Add"
4. Or right-click > Composite Mode > Use as Matte

**In After Effects:**
1. Import your output.mov file
2. Use "Screen" or "Add" blend mode
3. Or use as a Luma Matte by selecting your background layer > Track Matte > Luma Matte

## Tips

- **Color matching**: Use `--color` to match the RGB values of your logo/brand colors
- **Performance**: Lower `--fps` to 24 if processing is slow; increase to 60 for ultra-smooth results
- **Density**: Increase `--num-bars` for more detail, decrease for a cleaner look
- **Reactivity**: Lower `--smoothing` (e.g., 0.3) for more reactive/jumpy animation, keep high (0.7-0.9) for smooth flow

## Troubleshooting

**"Failed to open video writer"**: Try using `.mov` as the output format, it has the best support.

**Black background not transparent in editor**: Use "Screen" or "Add" blend mode instead of "Normal"

**Audio and video out of sync**: Make sure your audio file is not corrupt and try with a different file

**Installation errors**: Make sure you have Python 3.8+ and try installing packages one at a time

## Technical Details

- Uses FFT (Fast Fourier Transform) to analyze audio frequencies
- Renders at the exact duration of your audio file
- Maps low frequencies to the first bars, high frequencies to the later bars
- Applies smoothing between frames for fluid animation
- Outputs standard video formats compatible with all major editing software

## License

Free to use for personal and commercial projects.

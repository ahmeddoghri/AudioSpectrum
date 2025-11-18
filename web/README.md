# Audio Spectrum Visualizer - Web App

A modern, minimalistic web application for creating stunning audio spectrum visualizations, built with Apple design principles.

## Features

- **Audio Upload**: Drag-and-drop or browse to upload MP3/WAV files (up to 50MB)
- **10 Visualization Modes**:
  - Circular Bars - Classic radial bars
  - Waves - Concentric waves
  - Particles - Glowing particle system
  - Smooth Waveform - Elegant line visualization
  - Neon Tubes - Minimal glowing tubes
  - Vinyl Grooves - Retro vinyl aesthetic
  - Soul Aura - Ethereal glowing aura
  - Liquid Mercury - Flowing metallic liquid
  - Aurora Waves - Northern lights inspired
  - Mandala Growth - Geometric patterns

- **Social Media Presets**:
  - Instagram Square (1080x1080)
  - Instagram Story (1080x1920)
  - TikTok/Reels (1080x1920)
  - YouTube (1920x1080)
  - YouTube Shorts (1080x1920)
  - Twitter (1280x720)
  - Custom dimensions

- **Advanced Settings**:
  - Color schemes (Apple Blue, Warm Orange, Monochrome, Custom)
  - Bar count (48-120)
  - Inner radius (100-250px)
  - Smoothing (0.5-0.95)
  - Background styles
  - Gradient toggle
  - FPS selection (24, 30, 60)

- **Real-time Preview**: See your visualization before generating
- **Client-side Processing**: All processing happens in your browser, no server required
- **Responsive Design**: Works on desktop, tablet, and mobile

## Tech Stack

- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Audio Processing**: Web Audio API
- **Visualization**: Canvas API
- **Video Encoding**: MediaRecorder API
- **Design**: Apple minimalist design system

## Getting Started

### Local Development

1. Simply open `index.html` in a modern web browser
2. Or use a local server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx http-server

# Using PHP
php -S localhost:8000
```

3. Navigate to `http://localhost:8000`

### Browser Requirements

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

Required APIs:
- Web Audio API
- Canvas API
- MediaRecorder API
- FileReader API

## Usage

1. **Upload Audio**: Click or drag-and-drop your audio file (MP3 or WAV)
2. **Choose Style**: Select from 10 visualization modes
3. **Select Format**: Pick a social media preset or custom dimensions
4. **Adjust Settings** (optional): Customize colors, bars, radius, etc.
5. **Preview**: Click "Play Preview" to see it in action
6. **Generate**: Click "Generate Video" to create your video
7. **Download**: Save your creation!

## File Structure

```
web/
├── index.html          # Main HTML structure
├── styles.css          # Apple-inspired styling
├── app.js             # Main application logic
├── constants.js       # Configuration and constants
├── utils.js           # Helper functions
├── audio-processor.js # Web Audio API handling
├── visualizer.js      # Visualization rendering
├── video-encoder.js   # Video generation
└── README.md          # This file
```

## Performance Tips

- **Audio Files**: Keep files under 50MB for best performance
- **Duration**: Longer audio files will take more time to process
- **Resolution**: Higher resolutions (4K) require more processing power
- **FPS**: 30 FPS is recommended for most use cases
- **Browser**: Chrome/Edge generally have better performance

## Deployment

### GitHub Pages

```bash
# Push to gh-pages branch
git subtree push --prefix web origin gh-pages
```

### Netlify

1. Drag and drop the `web` folder to Netlify
2. Or connect your GitHub repository

### Vercel

```bash
vercel deploy web
```

## Browser Compatibility

| Feature | Chrome | Firefox | Safari | Edge |
|---------|--------|---------|--------|------|
| Audio Upload | ✅ | ✅ | ✅ | ✅ |
| Visualization | ✅ | ✅ | ✅ | ✅ |
| Video Generation | ✅ | ✅ | ⚠️ | ✅ |
| Download | ✅ | ✅ | ✅ | ✅ |

⚠️ Safari: Video generation works but may have limitations with some formats

## Known Limitations

- Video output format is WebM (widely supported)
- Maximum file size: 50MB
- Processing time depends on audio duration and device performance
- Some features may be limited on mobile devices

## Future Enhancements

- [ ] Add more visualization modes
- [ ] Support for custom background images
- [ ] Text overlay support (song title, artist)
- [ ] Audio trimming
- [ ] Batch processing
- [ ] Theme toggle (light/dark mode)
- [ ] Export settings as JSON
- [ ] Gallery of example videos

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

MIT License - see LICENSE file for details

## Credits

Built with inspiration from Apple's minimalist design system.

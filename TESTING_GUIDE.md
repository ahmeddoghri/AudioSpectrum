# AudioSpectrum Visual Testing Framework

Automated visual testing framework for testing all visualization modes with parameter variations.

## What It Does

This framework:
- ✅ Tests all non-hidden visualization modes (~880 modes)
- ✅ Generates one video per mode with varied settings for coverage
- ✅ Captures screenshots of parameter variations (Step 4 settings)
- ✅ Tests: Bar Count, Inner Radius, Smoothing, Background, Gradient
- ✅ Can pause and resume testing (runs over multiple days if needed)
- ✅ Organizes results in folders per mode

## Installation

```bash
# Install dependencies
npm install

# Install Chromium browser for Playwright
npm run test:install
```

## Usage

### Start Testing

```bash
npm run test:visual
```

Or directly:

```bash
node visual-test-framework.js
```

### Resume Testing

The framework automatically tracks progress in `test-progress.json`. If you stop the script (Ctrl+C) and restart it, it will resume from where it left off.

### Stop Testing

Press `Ctrl+C` to stop. Progress is automatically saved.

## Output Structure

```
test-results/
├── mode_001_bars/
│   ├── video_1234567890.webm          # Generated video
│   ├── settings.json                   # Settings used for video
│   ├── param_barCount_50.png          # Min bar count
│   ├── param_barCount_100.png         # Mid bar count
│   ├── param_barCount_150.png         # Max bar count
│   ├── param_innerRadius_50.png       # Min inner radius
│   ├── param_innerRadius_150.png      # Mid inner radius
│   ├── param_innerRadius_250.png      # Max inner radius
│   ├── param_smoothing_0.5.png        # Min smoothing
│   ├── param_smoothing_0.75.png       # Mid smoothing
│   ├── param_smoothing_0.95.png       # Max smoothing
│   ├── param_background_soft_gray.png # Background variations
│   ├── param_background_white.png
│   ├── param_background_dark.png
│   ├── param_background_transparent.png
│   ├── param_gradient_enabled.png     # Gradient on
│   └── param_gradient_disabled.png    # Gradient off
├── mode_002_waves/
│   └── ... (same structure)
└── test-progress.json                  # Progress tracking
```

## Configuration

Edit the `CONFIG` object in `visual-test-framework.js` to customize:

- **Timeouts**: Adjust if video generation takes longer
- **Video Settings Variations**: Change which settings to cycle through
- **Parameters to Test**: Modify parameter values to test
- **Headless Mode**: Set `headless: true` to run in background

## Progress Tracking

The framework saves progress after each mode. The `test-progress.json` file contains:

```json
{
  "startedAt": "2024-01-01T00:00:00.000Z",
  "lastUpdated": "2024-01-01T01:00:00.000Z",
  "completedModes": ["mode_001_bars", "mode_002_waves"],
  "currentMode": "mode_003_particles",
  "stats": {
    "totalModes": 882,
    "completed": 2,
    "failed": 0,
    "skipped": 0
  }
}
```

## Reviewing Results

After testing, review the generated content:

1. **Videos**: Watch one video per mode to verify it generates correctly
2. **Parameter Screenshots**: Compare screenshots to verify each parameter affects the visualization
3. **Identify Issues**: If parameter screenshots look identical, that parameter doesn't affect that mode

### Finding Modes with Issues

Look for modes where:
- Screenshots for different parameter values look identical
- Error logs exist (`error.log` in mode folder)
- Video files are missing or corrupted

## Troubleshooting

### Browser Doesn't Launch
```bash
npm run test:install
```

### Video Generation Timeout
Increase timeout in CONFIG:
```javascript
timeouts: {
    videoGeneration: 600000, // 10 minutes
}
```

### Out of Disk Space
The framework can generate 10-20GB of data. Clean up `test-results/` periodically or test in batches.

### Mode Not Found
Some modes may be hidden or have different IDs. Check `web/constants.js` for the correct mode ID.

## Estimated Runtime

- **Per mode**: ~3-5 minutes (1-2 min video generation + 1-2 min screenshots)
- **Total for 880 modes**: ~50-70 hours
- **Recommended**: Run overnight for several nights

## Tips

1. **Run in batches**: Stop after 50-100 modes, review results, then continue
2. **Check disk space**: Monitor available space during long runs
3. **Review progress**: Check `test-progress.json` to see how many modes are left
4. **Test important modes first**: Edit the modes array to prioritize specific modes

## Files

- `visual-test-framework.js` - Main test script
- `test-audio-20s.wav` - 20-second audio sample used for all tests
- `test-progress.json` - Progress tracking (auto-generated)
- `test-results/` - Output directory (auto-generated)

## Support

If you encounter issues:
1. Check error logs in `test-results/[mode_name]/error.log`
2. Review browser console output in terminal
3. Try running one mode manually to debug

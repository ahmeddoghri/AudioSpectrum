# Quick Start Guide

## Setup (One-time)

```bash
# 1. Install dependencies
npm install

# 2. Install Chromium browser
npm run test:install
```

## Test Sample (Recommended First)

Test 3 modes to verify everything works:

```bash
npm run test:sample
```

This will create `test-results-sample/` with results for 3 modes.

## Run Full Test Suite

```bash
npm run test:visual
```

**Testing ~252 non-hidden modes will take ~15-20 hours.** It's designed to be stopped and resumed.

## Control Commands

```bash
# Stop testing
Ctrl+C

# Resume testing (just run again)
npm run test:visual

# Check progress
npm run test:status

# Clean all test results and start fresh
npm run test:clean
npm run test:visual
```

## What to Expect

### During Testing

You'll see output like:
```
[1/252] Testing: Classic Bars
----------------------------------------------------------------------
Selecting mode: Classic Bars (bars)
Configuring: apple_blue, square_1_1, 30fps, transparent bg
Generating video...
Video saved: test-results/bars_Classic_Bars/video_1234567890.webm
Capturing parameter variations...
  ✓ Bar Count: 50
  ✓ Bar Count: 100
  ✓ Bar Count: 150
  ✓ Inner Radius: 50
  ... etc ...
✅ Mode Classic Bars completed
```

### Output Structure

For each mode, you'll get:
- 1 video file (webm format)
- 14 parameter screenshots
- 1 settings.json (what settings were used for the video)

### Time Per Mode

- Video generation: 1-2 minutes
- Parameter screenshots: 1-2 minutes
- **Total per mode: 3-5 minutes**

### Total Time

- 252 modes × 4 minutes average = **~17 hours**
- Run over 2-3 nights

## Tips

1. **Test in batches**: Run for a few hours, stop, review some results, then continue
2. **Monitor disk space**: Can generate 5-10GB of data
3. **Review progress**: Check `test-progress.json` to see completion percentage
4. **Browser window**: The script opens a browser window - you can minimize it but don't close it

## Reviewing Results

After testing, review:

1. **Watch videos**: Verify mode generates correctly
2. **Compare parameter screenshots**: Check if parameters affect the visualization
   - If screenshots look identical for different values → parameter doesn't affect that mode
3. **Find broken modes**: Look for error.log files

## Troubleshooting

### "Cannot find module 'playwright'"
```bash
npm install
```

### "Browser not found"
```bash
npm run test:install
```

### Videos timeout
Edit `visual-test-framework.js`, increase timeout:
```javascript
timeouts: {
    videoGeneration: 600000, // 10 minutes
}
```

### Want to test specific modes only

Edit the script to filter modes:
```javascript
// In visual-test-framework.js main() function
const modesToTest = allModes.filter(mode =>
    mode.category === 'Classic' // Only Classic category
);
```

## Next Steps

1. Run sample test: `npm run test:sample`
2. Review sample results in `test-results-sample/`
3. If satisfied, run full test: `npm run test:visual`
4. Review results as they come in
5. Create a spreadsheet tracking which modes have issues

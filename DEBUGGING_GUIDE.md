# AudioSpectrum Debugging Guide

## Preview Canvas Location

### HTML (web/index.html)
- **Location**: Lines 344-365
- **Canvas Element**: `<canvas id="previewCanvas" width="400" height="400"></canvas>` (line 354)
- **Container**: `<div class="preview-canvas-container">` (line 353)
- **Section**: `<section class="section" id="preview-section">` (line 345)

### JavaScript (web/app.js)
- **Initialization**: Line 431 - `this.visualizer = new Visualizer(this.elements.previewCanvas, this.state.settings)`
- **Animation Start**: Line 1125 - `startPreviewAnimation()` method
- **Render Call**: Line 1160 - `this.visualizer.render(magnitudes)`

## Console Logs to Check

### Preview Animation Logs
Look for these in the browser console (F12 or Cmd+Option+I):

1. **When preview starts**:
   ```
   [Preview] Starting animation loop
   [Preview] Canvas dimensions: 400 x 400
   [Preview] Settings: {...}
   [Preview] First frame - magnitudes sample: [...]
   ```

2. **Visualizer initialization**:
   ```
   [Visualizer] First render - mode: circular_bars canvas: 400x400 isPreviewMode: true
   [Visualizer] Preview mode - baseInnerRadius: 180 maxRadius: 120 effectiveRadius: 42
   ```

### Video Generation Logs
When generating a video, look for:

1. **Video encoder logs**:
   ```
   [VideoEncoder] MediaRecorder stopped
   [VideoEncoder] Chunks collected: X
   [VideoEncoder] Total size: X bytes
   [VideoEncoder] Created blob: Blob {size: X, type: "video/webm"}
   [VideoEncoder] Blob size: X
   [VideoEncoder] Blob type: video/webm
   ```

2. **Download section logs**:
   ```
   [Download] Showing download section
   [Download] Generated video: Blob {size: X, type: "video/webm"}
   [Download] Video type: object
   [Download] Video size: X
   [Download] Is Blob: true
   [Download] Created video URL: blob:http://...
   ```

## Common Issues and Solutions

### Issue 1: Preview Canvas Shows Gray Screen

**Symptoms**:
- Canvas shows gray/white background
- No visualization bars or particles visible

**Check**:
1. Open browser console (F12)
2. Look for `[Preview]` and `[Visualizer]` logs
3. Check if animation loop started
4. Check if `effectiveRadius` is positive and less than `maxRadius`

**Expected Values**:
- `maxRadius`: ~120 (for 400x400 canvas)
- `effectiveRadius`: ~42 (35% of maxRadius)
- `isPreviewMode`: true

**If logs don't appear**: Animation may not be starting
**If effectiveRadius is wrong**: Check visualizer.js line 45-59

### Issue 2: createObjectURL Error

**Error Message**:
```
Failed to execute 'createObjectURL' on 'URL': Overload resolution failed
```

**Check**:
1. Look for `[Download]` logs in console
2. Check if `Is Blob: true`
3. Check if blob size > 0

**Common Causes**:
- Video blob is null or undefined
- Video blob is not a Blob object
- Video blob has size 0 (empty chunks)

**Solution**: Check the `[VideoEncoder]` logs to see if chunks were collected

### Issue 3: Preview Animation Not Updating

**Symptoms**:
- Canvas shows first frame but doesn't animate
- Changes to settings don't update preview

**Check**:
1. Is `previewAnimationId` being set?
2. Is `requestAnimationFrame` being called?
3. Are there any JavaScript errors?

**Debug**:
```javascript
// In browser console:
app.previewAnimationId  // Should be a number if animating
app.previewTime  // Should be increasing
```

## Manual Testing Checklist

### 1. Test Preview Animation
- [ ] Upload an audio file
- [ ] Check if preview canvas shows animated visualization
- [ ] Change color scheme - preview should update
- [ ] Change bar count - preview should update
- [ ] Try different modes - all should show animation

### 2. Test Video Generation
- [ ] Click "Generate Video"
- [ ] Wait for progress to complete
- [ ] Check console for `[VideoEncoder]` logs
- [ ] Verify blob size > 0
- [ ] Check if download section appears

### 3. Test Video Download
- [ ] Verify video preview plays in download section
- [ ] Click "Download Video"
- [ ] Verify file downloads successfully
- [ ] Open downloaded file - should play in video player

## Quick Fixes

### If Preview Doesn't Show:
```javascript
// In browser console, manually start animation:
app.startPreviewAnimation()
```

### If Canvas Dimensions Are Wrong:
```javascript
// Check canvas size:
console.log(app.elements.previewCanvas.width, app.elements.previewCanvas.height)

// Manually resize:
app.visualizer.updateDimensions(400, 400)
app.startPreviewAnimation()
```

### If createObjectURL Fails:
```javascript
// Check generated video:
console.log(app.state.generatedVideo)
console.log(app.state.generatedVideo instanceof Blob)
console.log(app.state.generatedVideo.size)
```

## Files Modified for Debugging

1. **web/app.js**:
   - Lines 1135-1137: Preview animation start logging
   - Lines 1350-1354: Download section validation logging
   - Lines 1156-1158: First frame magnitude logging

2. **web/visualizer.js**:
   - Lines 45-59: Effective radius calculation with logging
   - Lines 171-192: Render method with mode logging
   - Lines 3500-3506: Gradient creation with safety checks
   - Lines 4202-4208: Gradient creation with safety checks
   - Lines 98-103: Vignette gradient with safety checks

3. **web/video-encoder.js**:
   - Lines 177-186: MediaRecorder stop event with logging

## Browser Compatibility

### Tested On:
- Chrome/Edge: Full support
- Firefox: Full support
- Safari: May have MediaRecorder limitations

### Required APIs:
- Canvas 2D Context
- Web Audio API
- MediaRecorder API
- requestAnimationFrame
- URL.createObjectURL

## Performance Tips

### For Smooth Preview:
- Recommended bar count: 50-100 (not 150)
- Lower FPS for slower devices: 30fps instead of 60fps
- Disable preview animation during generation: Done automatically

### For Video Generation:
- Smaller resolution = faster encoding
- Lower FPS = faster encoding
- Progress updates may slow down encoding slightly

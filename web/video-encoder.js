/**
 * Audio Spectrum Visualizer - Video Encoder
 * Handles video generation and encoding using canvas frames
 */

class VideoEncoder {
    constructor() {
        this.isEncoding = false;
        this.isCancelled = false;
        this.frames = [];
        this.progress = 0;
        this.startTime = 0;

        // Callbacks
        this.onProgress = null;
        this.onComplete = null;
        this.onError = null;
    }

    /**
     * Generate video from audio and visualizer settings
     */
    async generateVideo(audioProcessor, visualizer, settings, previewStartTime = 0) {
        if (this.isEncoding) {
            throw new Error('Encoding already in progress');
        }

        this.isEncoding = true;
        this.isCancelled = false;
        this.frames = [];
        this.progress = 0;
        this.startTime = Date.now();

        console.log('[VideoEncoder] === Starting video generation ===');
        console.log('[VideoEncoder] Settings:', JSON.stringify(settings, null, 2));
        console.log('[VideoEncoder] Preview start time:', previewStartTime);

        try {
            // Update progress
            this.updateProgress('Processing audio...', 0);

            // Get audio info
            const audioInfo = audioProcessor.getInfo();
            const fullDuration = audioInfo.duration;

            // Proof of concept: limit to 15 seconds if song is longer
            // Full song will be available behind paywall
            const PREVIEW_DURATION = 15;
            const duration = fullDuration > PREVIEW_DURATION ? PREVIEW_DURATION : fullDuration;
            const isPreview = fullDuration > PREVIEW_DURATION;

            const fps = settings.fps || 30;
            const totalFrames = Math.floor(duration * fps);

            console.log('[VideoEncoder] Audio info:', audioInfo);
            console.log('[VideoEncoder] Full duration:', fullDuration, 'seconds');
            console.log('[VideoEncoder] Processing duration:', duration, 'seconds', isPreview ? '(preview mode)' : '(full)');
            console.log('[VideoEncoder] FPS:', fps);
            console.log('[VideoEncoder] Total frames:', totalFrames);

            // Update progress
            this.updateProgress('Rendering frames...', 5);

            // Create offscreen canvas for rendering
            const canvas = document.createElement('canvas');
            canvas.width = settings.width;
            canvas.height = settings.height;

            console.log('[VideoEncoder] Created offscreen canvas');
            console.log('[VideoEncoder] Canvas dimensions:', canvas.width, 'x', canvas.height);
            console.log('[VideoEncoder] Canvas element:', canvas);

            // Verify canvas context
            const testCtx = canvas.getContext('2d');
            console.log('[VideoEncoder] Canvas context:', testCtx);
            console.log('[VideoEncoder] Canvas context type:', typeof testCtx);

            // Create visualizer instance for rendering
            const offscreenVisualizer = new Visualizer(canvas, settings);
            console.log('[VideoEncoder] Created offscreen visualizer');

            // Reset audio processor smoothing
            audioProcessor.resetSmoothing();

            // Render all frames
            console.log('[VideoEncoder] Starting frame rendering loop');

            for (let frame = 0; frame < totalFrames; frame++) {
                if (this.isCancelled) {
                    throw new Error('Encoding cancelled');
                }

                // Calculate time with preview start offset
                const time = previewStartTime + (frame / fps);
                const progress = 5 + ((frame / totalFrames) * 85);

                if (frame === 0) {
                    console.log('[VideoEncoder] === Rendering first frame ===');
                    console.log('[VideoEncoder] Time (with offset):', time);
                    console.log('[VideoEncoder] Preview start time:', previewStartTime);
                }

                // Get magnitude spectrum for this time
                const magnitudes = await audioProcessor.getMagnitudeSpectrum(
                    time,
                    settings.numBars,
                    settings.smoothing
                );

                if (frame === 0) {
                    console.log('[VideoEncoder] Got magnitudes:', magnitudes);
                    console.log('[VideoEncoder] Magnitudes length:', magnitudes?.length);
                    console.log('[VideoEncoder] Sample values:', magnitudes?.slice(0, 5));
                }

                // Render frame
                if (frame === 0) {
                    console.log('[VideoEncoder] About to render first frame');
                    console.log('[VideoEncoder] Canvas before render - width:', canvas.width, 'height:', canvas.height);
                }

                offscreenVisualizer.render(magnitudes);

                if (frame === 0) {
                    console.log('[VideoEncoder] Frame rendered');
                    console.log('[VideoEncoder] Canvas after render - width:', canvas.width, 'height:', canvas.height);

                    // Check if anything was drawn
                    const imageData = testCtx.getImageData(0, 0, Math.min(10, canvas.width), Math.min(10, canvas.height));
                    const hasContent = imageData.data.some(v => v !== 0);
                    console.log('[VideoEncoder] Canvas has content:', hasContent);
                    console.log('[VideoEncoder] Sample pixel data:', imageData.data.slice(0, 20));
                }

                // Capture frame as blob
                if (frame === 0) {
                    console.log('[VideoEncoder] About to call toBlob');
                }

                const blob = await new Promise(resolve => {
                    canvas.toBlob(resolve, 'image/png');
                });

                if (frame === 0) {
                    console.log('[VideoEncoder] toBlob completed, blob:', blob);
                }

                // Validate blob before adding to frames
                if (!blob) {
                    console.error('[VideoEncoder] === toBlob returned null ===');
                    console.error('[VideoEncoder] Canvas state:');
                    console.error('[VideoEncoder]   - width:', canvas.width);
                    console.error('[VideoEncoder]   - height:', canvas.height);
                    console.error('[VideoEncoder]   - context:', testCtx);
                    console.error('[VideoEncoder]   - frame number:', frame);
                    throw new Error(`Failed to capture frame ${frame}: canvas.toBlob returned null`);
                }

                this.frames.push(blob);

                // Update progress every 10 frames
                if (frame % 10 === 0) {
                    const eta = this.calculateETA(frame, totalFrames);
                    this.updateProgress(`Rendering frames... (${frame}/${totalFrames})`, progress, eta);
                }

                // Allow browser to breathe
                if (frame % 30 === 0) {
                    await this.sleep(10);
                }
            }

            // Update progress
            this.updateProgress('Encoding video...', 90);

            // Create video using MediaRecorder API (simpler than FFmpeg.wasm)
            const videoBlob = await this.encodeFramesToVideo(this.frames, fps, audioProcessor.audioBuffer, settings, duration, previewStartTime);

            // Update progress
            this.updateProgress('Complete!', 100);

            // Clean up
            offscreenVisualizer.dispose();
            this.frames = [];
            this.isEncoding = false;

            // Call complete callback
            if (this.onComplete) {
                this.onComplete(videoBlob);
            }

            return videoBlob;

        } catch (error) {
            this.isEncoding = false;
            this.frames = [];

            if (this.onError && !this.isCancelled) {
                this.onError(error);
            }

            throw error;
        }
    }

    /**
     * Encode frames to video using Canvas + MediaRecorder
     * This is a simpler approach than FFmpeg.wasm for browser compatibility
     */
    async encodeFramesToVideo(frames, fps, audioBuffer, settings, duration, previewStartTime = 0) {
        return new Promise(async (resolve, reject) => {
            try {
                // Create canvas for playback
                const canvas = document.createElement('canvas');
                canvas.width = settings.width;
                canvas.height = settings.height;
                const ctx = canvas.getContext('2d');

                // Create media stream from canvas
                const stream = canvas.captureStream(fps);

                // Add audio track if available (trimmed to selected time range)
                if (audioBuffer) {
                    const audioContext = new (window.AudioContext || window.webkitAudioContext)();

                    // Calculate trimmed buffer parameters
                    const sampleRate = audioBuffer.sampleRate;
                    const fullDuration = audioBuffer.duration;
                    const limitedDuration = Math.min(duration, fullDuration);

                    let bufferToUse = audioBuffer;

                    // Create trimmed buffer from selected start time
                    if (limitedDuration < fullDuration || previewStartTime > 0) {
                        const numberOfChannels = audioBuffer.numberOfChannels;
                        const startSample = Math.floor(previewStartTime * sampleRate);
                        const trimmedLength = Math.floor(limitedDuration * sampleRate);

                        console.log('[VideoEncoder] Trimming audio:');
                        console.log('[VideoEncoder]   Start time:', previewStartTime, 's');
                        console.log('[VideoEncoder]   Duration:', limitedDuration, 's');
                        console.log('[VideoEncoder]   Start sample:', startSample);
                        console.log('[VideoEncoder]   Trimmed length:', trimmedLength);

                        bufferToUse = audioContext.createBuffer(
                            numberOfChannels,
                            trimmedLength,
                            sampleRate
                        );

                        // Copy audio data from selected position for each channel
                        for (let channel = 0; channel < numberOfChannels; channel++) {
                            const originalData = audioBuffer.getChannelData(channel);
                            const trimmedData = bufferToUse.getChannelData(channel);
                            // Copy from startSample to startSample + trimmedLength
                            trimmedData.set(originalData.slice(startSample, startSample + trimmedLength));
                        }
                    }

                    const source = audioContext.createBufferSource();
                    source.buffer = bufferToUse;

                    const dest = audioContext.createMediaStreamDestination();
                    source.connect(dest);

                    // Add audio track to stream
                    const audioTrack = dest.stream.getAudioTracks()[0];
                    if (audioTrack) {
                        stream.addTrack(audioTrack);
                    }

                    source.start(0);
                }

                // Set up media recorder
                const mediaRecorder = new MediaRecorder(stream, {
                    mimeType: 'video/webm;codecs=vp9',
                    videoBitsPerSecond: 8000000
                });

                const chunks = [];

                mediaRecorder.ondataavailable = (e) => {
                    if (e.data.size > 0) {
                        chunks.push(e.data);
                    }
                };

                mediaRecorder.onstop = () => {
                    console.log('[VideoEncoder] MediaRecorder stopped');
                    console.log('[VideoEncoder] Chunks collected:', chunks.length);
                    console.log('[VideoEncoder] Total size:', chunks.reduce((acc, chunk) => acc + chunk.size, 0));
                    const blob = new Blob(chunks, { type: 'video/webm' });
                    console.log('[VideoEncoder] Created blob:', blob);
                    console.log('[VideoEncoder] Blob size:', blob.size);
                    console.log('[VideoEncoder] Blob type:', blob.type);
                    resolve(blob);
                };

                mediaRecorder.onerror = (error) => {
                    reject(error);
                };

                // Start recording
                mediaRecorder.start();

                // Play back frames
                const frameDuration = 1000 / fps;
                for (let i = 0; i < frames.length; i++) {
                    if (this.isCancelled) {
                        mediaRecorder.stop();
                        reject(new Error('Encoding cancelled'));
                        return;
                    }

                    // Validate frame before creating object URL
                    if (!frames[i] || !(frames[i] instanceof Blob)) {
                        reject(new Error(`Invalid frame at index ${i}`));
                        return;
                    }

                    const img = await this.loadImage(URL.createObjectURL(frames[i]));
                    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

                    // Update progress during encoding (90% to 99%)
                    const encodingProgress = 90 + ((i / frames.length) * 9);
                    this.updateProgress(`Encoding video... (${i + 1}/${frames.length})`, encodingProgress);

                    await this.sleep(frameDuration);
                }

                // Stop recording
                mediaRecorder.stop();

            } catch (error) {
                reject(error);
            }
        });
    }

    /**
     * Alternative: Create animated WebM using frames (fallback method)
     */
    async createVideoFromFrames(frames, fps, audioBlob = null) {
        // For now, we'll return a simple implementation
        // In production, you might want to use FFmpeg.wasm here

        // Create a canvas animation
        const canvas = document.createElement('canvas');
        canvas.width = 1080;
        canvas.height = 1080;
        const ctx = canvas.getContext('2d');

        // Load first frame to get dimensions
        if (frames.length > 0) {
            // Validate first frame before creating object URL
            if (!frames[0] || !(frames[0] instanceof Blob)) {
                throw new Error('Invalid first frame: not a valid Blob');
            }
            const firstImg = await this.loadImage(URL.createObjectURL(frames[0]));
            canvas.width = firstImg.width;
            canvas.height = firstImg.height;
        }

        // Create video stream
        const stream = canvas.captureStream(fps);

        // Set up MediaRecorder
        const mimeType = MediaRecorder.isTypeSupported('video/webm;codecs=vp9')
            ? 'video/webm;codecs=vp9'
            : 'video/webm';

        const mediaRecorder = new MediaRecorder(stream, {
            mimeType: mimeType,
            videoBitsPerSecond: 5000000
        });

        const chunks = [];

        return new Promise((resolve, reject) => {
            mediaRecorder.ondataavailable = (e) => {
                if (e.data.size > 0) {
                    chunks.push(e.data);
                }
            };

            mediaRecorder.onstop = () => {
                const blob = new Blob(chunks, { type: mimeType });
                resolve(blob);
            };

            mediaRecorder.onerror = reject;

            mediaRecorder.start();

            // Render frames
            let frameIndex = 0;
            const interval = setInterval(async () => {
                if (frameIndex >= frames.length || this.isCancelled) {
                    clearInterval(interval);
                    setTimeout(() => mediaRecorder.stop(), 100);
                    return;
                }

                // Validate frame before creating object URL
                if (!frames[frameIndex] || !(frames[frameIndex] instanceof Blob)) {
                    clearInterval(interval);
                    mediaRecorder.stop();
                    reject(new Error(`Invalid frame at index ${frameIndex}`));
                    return;
                }

                const img = await this.loadImage(URL.createObjectURL(frames[frameIndex]));
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

                frameIndex++;
            }, 1000 / fps);
        });
    }

    /**
     * Load image from URL
     */
    loadImage(url) {
        return new Promise((resolve, reject) => {
            const img = new Image();
            img.onload = () => resolve(img);
            img.onerror = reject;
            img.src = url;
        });
    }

    /**
     * Sleep for specified milliseconds
     */
    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    /**
     * Update progress
     */
    updateProgress(status, percentage, eta = null) {
        this.progress = percentage;

        if (this.onProgress) {
            this.onProgress({
                status,
                percentage,
                eta
            });
        }
    }

    /**
     * Calculate estimated time remaining
     */
    calculateETA(currentFrame, totalFrames) {
        if (currentFrame === 0) return null;

        const elapsed = (Date.now() - this.startTime) / 1000; // seconds
        const framesPerSecond = currentFrame / elapsed;
        const remainingFrames = totalFrames - currentFrame;
        const remainingSeconds = remainingFrames / framesPerSecond;

        if (remainingSeconds < 60) {
            return `${Math.ceil(remainingSeconds)}s`;
        } else {
            const minutes = Math.floor(remainingSeconds / 60);
            const seconds = Math.ceil(remainingSeconds % 60);
            return `${minutes}m ${seconds}s`;
        }
    }

    /**
     * Cancel encoding
     */
    cancel() {
        this.isCancelled = true;
        this.isEncoding = false;
        this.frames = [];
    }

    /**
     * Set progress callback
     */
    setProgressCallback(callback) {
        this.onProgress = callback;
    }

    /**
     * Set complete callback
     */
    setCompleteCallback(callback) {
        this.onComplete = callback;
    }

    /**
     * Set error callback
     */
    setErrorCallback(callback) {
        this.onError = callback;
    }

    /**
     * Get current progress
     */
    getProgress() {
        return {
            percentage: this.progress,
            isEncoding: this.isEncoding
        };
    }
}

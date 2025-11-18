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
    async generateVideo(audioProcessor, visualizer, settings) {
        if (this.isEncoding) {
            throw new Error('Encoding already in progress');
        }

        this.isEncoding = true;
        this.isCancelled = false;
        this.frames = [];
        this.progress = 0;
        this.startTime = Date.now();

        try {
            // Update progress
            this.updateProgress('Processing audio...', 0);

            // Get audio info
            const audioInfo = audioProcessor.getInfo();
            const duration = audioInfo.duration;
            const fps = settings.fps || 30;
            const totalFrames = Math.floor(duration * fps);

            // Update progress
            this.updateProgress('Rendering frames...', 5);

            // Create offscreen canvas for rendering
            const canvas = document.createElement('canvas');
            canvas.width = settings.width;
            canvas.height = settings.height;

            // Create visualizer instance for rendering
            const offscreenVisualizer = new Visualizer(canvas, settings);

            // Reset audio processor smoothing
            audioProcessor.resetSmoothing();

            // Render all frames
            for (let frame = 0; frame < totalFrames; frame++) {
                if (this.isCancelled) {
                    throw new Error('Encoding cancelled');
                }

                const time = frame / fps;
                const progress = 5 + ((frame / totalFrames) * 85);

                // Get magnitude spectrum for this time
                const magnitudes = await audioProcessor.getMagnitudeSpectrum(
                    time,
                    settings.numBars,
                    settings.smoothing
                );

                // Render frame
                offscreenVisualizer.render(magnitudes);

                // Capture frame as blob
                const blob = await new Promise(resolve => {
                    canvas.toBlob(resolve, 'image/png');
                });

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
            const videoBlob = await this.encodeFramesToVideo(this.frames, fps, audioProcessor.audioBuffer, settings);

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
    async encodeFramesToVideo(frames, fps, audioBuffer, settings) {
        return new Promise(async (resolve, reject) => {
            try {
                // Create canvas for playback
                const canvas = document.createElement('canvas');
                canvas.width = settings.width;
                canvas.height = settings.height;
                const ctx = canvas.getContext('2d');

                // Create media stream from canvas
                const stream = canvas.captureStream(fps);

                // Add audio track if available
                if (audioBuffer) {
                    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
                    const source = audioContext.createBufferSource();
                    source.buffer = audioBuffer;

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
                    const blob = new Blob(chunks, { type: 'video/webm' });
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

                    const img = await this.loadImage(URL.createObjectURL(frames[i]));
                    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

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

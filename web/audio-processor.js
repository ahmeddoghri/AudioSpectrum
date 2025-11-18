/**
 * Audio Spectrum Visualizer - Audio Processor
 * Handles audio loading and frequency analysis using Web Audio API
 */

class AudioProcessor {
    constructor() {
        this.audioContext = null;
        this.analyser = null;
        this.audioBuffer = null;
        this.sourceNode = null;
        this.frequencyData = null;
        this.timeData = null;
        this.isPlaying = false;
        this.duration = 0;
        this.sampleRate = 44100;

        // Smoothing for visualization
        this.prevMagnitudes = null;
        this.smoothingFactor = AUDIO_CONFIG.smoothingTimeConstant;
    }

    /**
     * Initialize audio context
     */
    init() {
        if (!this.audioContext) {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            this.audioContext = new AudioContext();

            // Create analyser node
            this.analyser = this.audioContext.createAnalyser();
            this.analyser.fftSize = AUDIO_CONFIG.fftSize;
            this.analyser.smoothingTimeConstant = AUDIO_CONFIG.smoothingTimeConstant;
            this.analyser.minDecibels = AUDIO_CONFIG.minDecibels;
            this.analyser.maxDecibels = AUDIO_CONFIG.maxDecibels;

            // Initialize data arrays
            const bufferLength = this.analyser.frequencyBinCount;
            this.frequencyData = new Uint8Array(bufferLength);
            this.timeData = new Uint8Array(bufferLength);
        }
    }

    /**
     * Load audio file
     */
    async loadAudio(file) {
        this.init();

        try {
            // Read file as array buffer
            const arrayBuffer = await file.arrayBuffer();

            // Decode audio data
            this.audioBuffer = await this.audioContext.decodeAudioData(arrayBuffer);
            this.duration = this.audioBuffer.duration;
            this.sampleRate = this.audioBuffer.sampleRate;

            return {
                success: true,
                duration: this.duration,
                sampleRate: this.sampleRate,
                channels: this.audioBuffer.numberOfChannels
            };
        } catch (error) {
            console.error('Error loading audio:', error);
            throw new Error('Failed to decode audio file. Please ensure it\'s a valid MP3 or WAV file.');
        }
    }

    /**
     * Play audio for preview
     */
    play() {
        if (!this.audioBuffer || this.isPlaying) return;

        this.init();

        // Create source node
        this.sourceNode = this.audioContext.createBufferSource();
        this.sourceNode.buffer = this.audioBuffer;

        // Connect nodes
        this.sourceNode.connect(this.analyser);
        this.analyser.connect(this.audioContext.destination);

        // Start playback
        this.sourceNode.start(0);
        this.isPlaying = true;

        // Handle end of playback
        this.sourceNode.onended = () => {
            this.isPlaying = false;
        };
    }

    /**
     * Stop audio playback
     */
    stop() {
        if (this.sourceNode && this.isPlaying) {
            this.sourceNode.stop();
            this.sourceNode.disconnect();
            this.sourceNode = null;
            this.isPlaying = false;
        }
    }

    /**
     * Get frequency data (spectrum)
     */
    getFrequencyData() {
        if (!this.analyser) return null;

        this.analyser.getByteFrequencyData(this.frequencyData);
        return this.frequencyData;
    }

    /**
     * Get time domain data (waveform)
     */
    getTimeData() {
        if (!this.analyser) return null;

        this.analyser.getByteTimeDomainData(this.timeData);
        return this.timeData;
    }

    /**
     * Get smoothed magnitude spectrum for a specific time
     */
    async getMagnitudeSpectrum(time, numBars = 72, smoothing = 0.85) {
        if (!this.audioBuffer) return null;

        // Calculate the sample position
        const samplePosition = Math.floor(time * this.sampleRate);

        // Get channel data
        const channelData = this.audioBuffer.getChannelData(0);

        // Extract window of samples for FFT
        const fftSize = AUDIO_CONFIG.fftSize;
        const halfSize = fftSize / 2;
        const windowData = new Float32Array(fftSize);

        // Fill window with audio samples
        for (let i = 0; i < fftSize; i++) {
            const sampleIndex = samplePosition - halfSize + i;
            if (sampleIndex >= 0 && sampleIndex < channelData.length) {
                // Apply Hanning window
                const windowValue = 0.5 * (1 - Math.cos(2 * Math.PI * i / fftSize));
                windowData[i] = channelData[sampleIndex] * windowValue;
            }
        }

        // Perform FFT (using simple magnitude calculation)
        const magnitudes = this.calculateFFTMagnitudes(windowData, numBars);

        // Apply smoothing
        if (this.prevMagnitudes) {
            for (let i = 0; i < magnitudes.length; i++) {
                magnitudes[i] = this.prevMagnitudes[i] * smoothing + magnitudes[i] * (1 - smoothing);
            }
        }

        // Store for next frame
        this.prevMagnitudes = magnitudes.slice();

        return magnitudes;
    }

    /**
     * Calculate FFT magnitudes (simplified)
     */
    calculateFFTMagnitudes(data, numBars) {
        const fftSize = data.length;
        const magnitudes = new Float32Array(numBars);

        // Simple frequency grouping
        const samplesPerBar = Math.floor(fftSize / 2 / numBars);

        for (let i = 0; i < numBars; i++) {
            let sum = 0;
            const startIdx = i * samplesPerBar;
            const endIdx = Math.min(startIdx + samplesPerBar, fftSize / 2);

            for (let j = startIdx; j < endIdx; j++) {
                // Calculate magnitude using DFT-like approach
                let real = 0;
                let imag = 0;

                for (let k = 0; k < data.length; k++) {
                    const angle = -2 * Math.PI * j * k / fftSize;
                    real += data[k] * Math.cos(angle);
                    imag += data[k] * Math.sin(angle);
                }

                const magnitude = Math.sqrt(real * real + imag * imag);
                sum += magnitude;
            }

            magnitudes[i] = sum / samplesPerBar;
        }

        // Normalize
        const max = Math.max(...magnitudes);
        if (max > 0) {
            for (let i = 0; i < magnitudes.length; i++) {
                magnitudes[i] /= max;
            }
        }

        return magnitudes;
    }

    /**
     * Get magnitude spectrum using Web Audio API (for real-time preview)
     */
    getRealTimeMagnitudes(numBars = 72) {
        const frequencyData = this.getFrequencyData();
        if (!frequencyData) return null;

        const magnitudes = new Float32Array(numBars);
        const samplesPerBar = Math.floor(frequencyData.length / numBars);

        for (let i = 0; i < numBars; i++) {
            let sum = 0;
            const startIdx = i * samplesPerBar;
            const endIdx = Math.min(startIdx + samplesPerBar, frequencyData.length);

            for (let j = startIdx; j < endIdx; j++) {
                sum += frequencyData[j];
            }

            magnitudes[i] = sum / samplesPerBar / 255; // Normalize to 0-1
        }

        // Apply smoothing
        if (this.prevMagnitudes) {
            for (let i = 0; i < magnitudes.length; i++) {
                magnitudes[i] = this.prevMagnitudes[i] * this.smoothingFactor +
                               magnitudes[i] * (1 - this.smoothingFactor);
            }
        }

        this.prevMagnitudes = magnitudes.slice();

        return magnitudes;
    }

    /**
     * Calculate waveform data for visualization
     */
    async getWaveformData(width = 800) {
        if (!this.audioBuffer) return null;

        const channelData = this.audioBuffer.getChannelData(0);
        const samples = width;
        const blockSize = Math.floor(channelData.length / samples);
        const waveformData = [];

        for (let i = 0; i < samples; i++) {
            const blockStart = blockSize * i;
            let sum = 0;

            for (let j = 0; j < blockSize; j++) {
                sum += Math.abs(channelData[blockStart + j]);
            }

            waveformData.push(sum / blockSize);
        }

        return waveformData;
    }

    /**
     * Reset smoothing
     */
    resetSmoothing() {
        this.prevMagnitudes = null;
    }

    /**
     * Set smoothing factor
     */
    setSmoothingFactor(smoothing) {
        this.smoothingFactor = smoothing;
        if (this.analyser) {
            this.analyser.smoothingTimeConstant = smoothing;
        }
    }

    /**
     * Clean up resources
     */
    dispose() {
        this.stop();

        if (this.analyser) {
            this.analyser.disconnect();
            this.analyser = null;
        }

        if (this.audioContext && this.audioContext.state !== 'closed') {
            this.audioContext.close();
            this.audioContext = null;
        }

        this.audioBuffer = null;
        this.frequencyData = null;
        this.timeData = null;
        this.prevMagnitudes = null;
    }

    /**
     * Get audio info
     */
    getInfo() {
        if (!this.audioBuffer) return null;

        return {
            duration: this.duration,
            sampleRate: this.sampleRate,
            channels: this.audioBuffer.numberOfChannels,
            length: this.audioBuffer.length
        };
    }
}

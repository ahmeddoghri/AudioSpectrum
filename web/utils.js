/**
 * Audio Spectrum Visualizer - Utility Functions
 * Helper functions for the application
 */

class Utils {
    /**
     * Format bytes to human readable format
     */
    static formatBytes(bytes, decimals = 2) {
        if (bytes === 0) return '0 Bytes';

        const k = 1024;
        const dm = decimals < 0 ? 0 : decimals;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];

        const i = Math.floor(Math.log(bytes) / Math.log(k));

        return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }

    /**
     * Format seconds to MM:SS format
     */
    static formatTime(seconds) {
        const mins = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${mins}:${secs.toString().padStart(2, '0')}`;
    }

    /**
     * Validate file type and size
     */
    static validateFile(file) {
        const errors = [];

        // Check file type
        const validTypes = FILE_CONSTRAINTS.acceptedMimeTypes;
        if (!validTypes.includes(file.type)) {
            errors.push(`Invalid file type. Please upload ${FILE_CONSTRAINTS.acceptedFormats.join(', ')} files.`);
        }

        // Check file size
        const maxSize = FILE_CONSTRAINTS.maxSizeMB * 1024 * 1024;
        if (file.size > maxSize) {
            errors.push(`File size exceeds ${FILE_CONSTRAINTS.maxSizeMB}MB limit.`);
        }

        return {
            valid: errors.length === 0,
            errors
        };
    }

    /**
     * Show toast notification
     */
    static showToast(message, type = 'info', duration = 3000) {
        const toast = document.getElementById('toast');
        const toastMessage = document.getElementById('toastMessage');

        if (!toast || !toastMessage) return;

        toastMessage.textContent = message;
        toast.className = `toast ${type}`;
        toast.style.display = 'block';

        setTimeout(() => {
            toast.style.display = 'none';
        }, duration);
    }

    /**
     * Smooth scroll to element
     */
    static scrollToElement(elementId) {
        const element = document.getElementById(elementId);
        if (element) {
            element.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }

    /**
     * Debounce function calls
     */
    static debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    /**
     * Convert RGB to hex color
     */
    static rgbToHex(rgb) {
        const [r, g, b] = rgb;
        return '#' + [r, g, b].map(x => {
            const hex = x.toString(16);
            return hex.length === 1 ? '0' + hex : hex;
        }).join('');
    }

    /**
     * Convert hex to RGB color
     */
    static hexToRgb(hex) {
        const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? [
            parseInt(result[1], 16),
            parseInt(result[2], 16),
            parseInt(result[3], 16)
        ] : null;
    }

    /**
     * Linear interpolation between two values
     */
    static lerp(start, end, t) {
        return start * (1 - t) + end * t;
    }

    /**
     * Map value from one range to another
     */
    static mapRange(value, inMin, inMax, outMin, outMax) {
        return (value - inMin) * (outMax - outMin) / (inMax - inMin) + outMin;
    }

    /**
     * Clamp value between min and max
     */
    static clamp(value, min, max) {
        return Math.min(Math.max(value, min), max);
    }

    /**
     * Generate unique ID
     */
    static generateId() {
        return Date.now().toString(36) + Math.random().toString(36).substr(2);
    }

    /**
     * Create filename with timestamp
     */
    static createFilename(mode, extension = 'mp4', originalFilename = null) {
        const timestamp = new Date().getTime();

        // If original filename is provided, use its base name
        if (originalFilename) {
            // Remove the extension from the original filename
            const baseName = originalFilename.substring(0, originalFilename.lastIndexOf('.')) || originalFilename;
            return `${baseName}.${extension}`;
        }

        // Otherwise, use the mode-based naming
        const modeSlug = mode.replace(/\s+/g, '-').toLowerCase();
        return `audiospectrum-${modeSlug}-${timestamp}.${extension}`;
    }

    /**
     * Deep clone object
     */
    static deepClone(obj) {
        return JSON.parse(JSON.stringify(obj));
    }

    /**
     * Check if browser supports required APIs
     */
    static checkBrowserSupport() {
        const required = {
            audioContext: 'AudioContext' in window || 'webkitAudioContext' in window,
            canvas: 'HTMLCanvasElement' in window,
            webgl: (() => {
                try {
                    const canvas = document.createElement('canvas');
                    return !!(canvas.getContext('webgl') || canvas.getContext('experimental-webgl'));
                } catch (e) {
                    return false;
                }
            })(),
            fileReader: 'FileReader' in window,
            blob: 'Blob' in window,
            url: 'URL' in window
        };

        const unsupported = Object.entries(required)
            .filter(([key, value]) => !value)
            .map(([key]) => key);

        return {
            supported: unsupported.length === 0,
            unsupported
        };
    }

    /**
     * Download blob as file
     */
    static downloadBlob(blob, filename) {
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = filename;

        document.body.appendChild(a);
        a.click();

        // Clean up
        setTimeout(() => {
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }, 100);
    }

    /**
     * Load image from URL
     */
    static loadImage(url) {
        return new Promise((resolve, reject) => {
            const img = new Image();
            img.onload = () => resolve(img);
            img.onerror = reject;
            img.src = url;
        });
    }

    /**
     * Calculate waveform data for preview
     */
    static async calculateWaveform(audioBuffer, width = 800) {
        const rawData = audioBuffer.getChannelData(0);
        const samples = width;
        const blockSize = Math.floor(rawData.length / samples);
        const waveformData = [];

        for (let i = 0; i < samples; i++) {
            let blockStart = blockSize * i;
            let sum = 0;
            for (let j = 0; j < blockSize; j++) {
                sum += Math.abs(rawData[blockStart + j]);
            }
            waveformData.push(sum / blockSize);
        }

        return waveformData;
    }

    /**
     * Draw waveform on canvas
     */
    static drawWaveform(canvas, waveformData, color = COLORS.PRIMARY_BLUE) {
        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        // Set style
        ctx.fillStyle = `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
        ctx.globalAlpha = 0.8;

        // Draw bars
        const barWidth = width / waveformData.length;
        const middle = height / 2;

        waveformData.forEach((value, index) => {
            const barHeight = value * height;
            const x = index * barWidth;
            const y = middle - barHeight / 2;

            ctx.fillRect(x, y, barWidth - 1, barHeight);
        });
    }

    /**
     * Apply saturation reduction for elegant colors
     */
    static desaturateColor(rgb, reduction = 0.3) {
        const [r, g, b] = rgb;

        // Convert to HSL
        const rNorm = r / 255;
        const gNorm = g / 255;
        const bNorm = b / 255;

        const max = Math.max(rNorm, gNorm, bNorm);
        const min = Math.min(rNorm, gNorm, bNorm);
        const l = (max + min) / 2;

        let h, s;

        if (max === min) {
            h = s = 0;
        } else {
            const d = max - min;
            s = l > 0.5 ? d / (2 - max - min) : d / (max + min);

            switch (max) {
                case rNorm:
                    h = ((gNorm - bNorm) / d + (gNorm < bNorm ? 6 : 0)) / 6;
                    break;
                case gNorm:
                    h = ((bNorm - rNorm) / d + 2) / 6;
                    break;
                case bNorm:
                    h = ((rNorm - gNorm) / d + 4) / 6;
                    break;
            }
        }

        // Reduce saturation
        s = s * (1 - reduction);

        // Convert back to RGB
        const hue2rgb = (p, q, t) => {
            if (t < 0) t += 1;
            if (t > 1) t -= 1;
            if (t < 1/6) return p + (q - p) * 6 * t;
            if (t < 1/2) return q;
            if (t < 2/3) return p + (q - p) * (2/3 - t) * 6;
            return p;
        };

        let rNew, gNew, bNew;

        if (s === 0) {
            rNew = gNew = bNew = l;
        } else {
            const q = l < 0.5 ? l * (1 + s) : l + s - l * s;
            const p = 2 * l - q;
            rNew = hue2rgb(p, q, h + 1/3);
            gNew = hue2rgb(p, q, h);
            bNew = hue2rgb(p, q, h - 1/3);
        }

        return [
            Math.round(rNew * 255),
            Math.round(gNew * 255),
            Math.round(bNew * 255)
        ];
    }

    /**
     * Save settings to localStorage
     */
    static saveSettings(settings) {
        try {
            localStorage.setItem('audioSpectrumSettings', JSON.stringify(settings));
            return true;
        } catch (e) {
            console.error('Failed to save settings:', e);
            return false;
        }
    }

    /**
     * Load settings from localStorage
     */
    static loadSettings() {
        try {
            const saved = localStorage.getItem('audioSpectrumSettings');
            return saved ? JSON.parse(saved) : null;
        } catch (e) {
            console.error('Failed to load settings:', e);
            return null;
        }
    }
}

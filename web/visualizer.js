/**
 * Audio Spectrum Visualizer - Visualization Engine
 * Implements various visualization modes with Apple minimalist design
 */

class Visualizer {
    constructor(canvas, settings = {}) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.settings = { ...DEFAULT_SETTINGS, ...settings };

        this.centerX = canvas.width / 2;
        this.centerY = canvas.height / 2;
        this.maxRadius = Math.min(canvas.width, canvas.height) / 2 - 80;

        this.frameCounter = 0;
        this.animationId = null;
    }

    /**
     * Update canvas dimensions
     */
    updateDimensions(width, height) {
        this.canvas.width = width;
        this.canvas.height = height;
        this.centerX = width / 2;
        this.centerY = height / 2;
        this.maxRadius = Math.min(width, height) / 2 - 80;
    }

    /**
     * Update settings
     */
    updateSettings(newSettings) {
        this.settings = { ...this.settings, ...newSettings };
    }

    /**
     * Clear canvas
     */
    clear() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }

    /**
     * Draw background
     */
    drawBackground() {
        const bgStyle = BACKGROUND_STYLES[this.settings.background];
        const color = bgStyle.color;

        if (this.settings.background === 'transparent') {
            this.clear();
        } else {
            this.ctx.fillStyle = `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
            this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        }

        // Apply subtle vignette for non-transparent backgrounds
        if (this.settings.background !== 'transparent') {
            this.applyVignette(0.15);
        }
    }

    /**
     * Apply vignette effect
     */
    applyVignette(strength = 0.3) {
        const gradient = this.ctx.createRadialGradient(
            this.centerX, this.centerY, 0,
            this.centerX, this.centerY, this.maxRadius * 2
        );

        gradient.addColorStop(0, `rgba(0, 0, 0, 0)`);
        gradient.addColorStop(1, `rgba(0, 0, 0, ${strength})`);

        this.ctx.fillStyle = gradient;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    }

    /**
     * Get color for bar index
     */
    getColor(index, total) {
        const scheme = COLOR_SCHEMES[this.settings.colorScheme];

        if (!this.settings.gradient || !scheme.gradient) {
            const color = scheme.primary;
            return `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
        }

        // Create gradient
        const t = index / total;
        const color1 = scheme.primary;
        const color2 = scheme.secondary;

        const r = Math.round(Utils.lerp(color1[0], color2[0], t));
        const g = Math.round(Utils.lerp(color1[1], color2[1], t));
        const b = Math.round(Utils.lerp(color1[2], color2[2], t));

        return `rgb(${r}, ${g}, ${b})`;
    }

    /**
     * Apply easing function
     */
    ease(t) {
        return ANIMATION.easing.easeOutCubic(t);
    }

    /**
     * Render frame based on mode
     */
    render(magnitudes) {
        if (!magnitudes) return;

        this.drawBackground();

        const modeId = this.settings.mode;
        const mode = Object.values(VISUALIZATION_MODES).find(m => m.id === modeId);

        if (!mode) {
            this.renderCircularBars(magnitudes);
            return;
        }

        switch (modeId) {
            case 'circular_bars':
                this.renderCircularBars(magnitudes);
                break;
            case 'waves':
                this.renderWaves(magnitudes);
                break;
            case 'particles':
                this.renderParticles(magnitudes);
                break;
            case 'smooth_waveform':
                this.renderSmoothWaveform(magnitudes);
                break;
            case 'neon_tubes':
                this.renderNeonTubes(magnitudes);
                break;
            case 'vinyl_grooves':
                this.renderVinylGrooves(magnitudes);
                break;
            case 'soul_aura':
                this.renderSoulAura(magnitudes);
                break;
            case 'liquid_mercury':
                this.renderLiquidMercury(magnitudes);
                break;
            case 'aurora_waves':
                this.renderAuroraWaves(magnitudes);
                break;
            case 'mandala_growth':
                this.renderMandalaGrowth(magnitudes);
                break;
            default:
                this.renderCircularBars(magnitudes);
        }

        this.frameCounter++;
    }

    /**
     * Mode 1: Circular Bars
     */
    renderCircularBars(magnitudes) {
        const numBars = magnitudes.length;
        const angleStep = (Math.PI * 2) / numBars;
        const innerRadius = this.settings.innerRadius;
        const barWidthMultiplier = this.settings.barWidthMultiplier;

        // Enable shadow for depth
        this.ctx.shadowBlur = 15;
        this.ctx.shadowColor = 'rgba(0, 0, 0, 0.3)';

        for (let i = 0; i < numBars; i++) {
            const angle = i * angleStep - Math.PI / 2;
            const magnitude = magnitudes[i];
            const barLength = magnitude * this.maxRadius * 0.7;

            const x1 = this.centerX + Math.cos(angle) * innerRadius;
            const y1 = this.centerY + Math.sin(angle) * innerRadius;
            const x2 = this.centerX + Math.cos(angle) * (innerRadius + barLength);
            const y2 = this.centerY + Math.sin(angle) * (innerRadius + barLength);

            this.ctx.strokeStyle = this.getColor(i, numBars);
            this.ctx.lineWidth = angleStep * innerRadius * barWidthMultiplier;
            this.ctx.lineCap = 'round';

            this.ctx.beginPath();
            this.ctx.moveTo(x1, y1);
            this.ctx.lineTo(x2, y2);
            this.ctx.stroke();
        }

        // Reset shadow
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 2: Waves
     */
    renderWaves(magnitudes) {
        const numWaves = 5;
        const innerRadius = this.settings.innerRadius;

        this.ctx.shadowBlur = 20;
        this.ctx.shadowColor = 'rgba(0, 113, 227, 0.3)';

        for (let wave = 0; wave < numWaves; wave++) {
            const waveRadius = innerRadius + (wave * 40);
            const numPoints = magnitudes.length;
            const angleStep = (Math.PI * 2) / numPoints;

            this.ctx.beginPath();
            this.ctx.strokeStyle = this.getColor(wave * 20, 100);
            this.ctx.lineWidth = 3;
            this.ctx.lineCap = 'round';

            for (let i = 0; i <= numPoints; i++) {
                const angle = i * angleStep;
                const magnitude = magnitudes[i % numPoints];
                const radius = waveRadius + magnitude * 30;

                const x = this.centerX + Math.cos(angle) * radius;
                const y = this.centerY + Math.sin(angle) * radius;

                if (i === 0) {
                    this.ctx.moveTo(x, y);
                } else {
                    this.ctx.lineTo(x, y);
                }
            }

            this.ctx.closePath();
            this.ctx.stroke();
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 3: Particles
     */
    renderParticles(magnitudes) {
        const numBars = magnitudes.length;
        const angleStep = (Math.PI * 2) / numBars;
        const innerRadius = this.settings.innerRadius;

        this.ctx.shadowBlur = 25;

        for (let i = 0; i < numBars; i++) {
            const angle = i * angleStep;
            const magnitude = magnitudes[i];
            const distance = innerRadius + magnitude * this.maxRadius * 0.6;

            const x = this.centerX + Math.cos(angle) * distance;
            const y = this.centerY + Math.sin(angle) * distance;
            const size = 4 + magnitude * 8;

            const color = this.getColor(i, numBars);
            this.ctx.shadowColor = color;
            this.ctx.fillStyle = color;

            this.ctx.beginPath();
            this.ctx.arc(x, y, size, 0, Math.PI * 2);
            this.ctx.fill();
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 4: Smooth Waveform
     */
    renderSmoothWaveform(magnitudes) {
        const numPoints = magnitudes.length;
        const angleStep = (Math.PI * 2) / numPoints;
        const innerRadius = this.settings.innerRadius;

        // Draw filled waveform
        this.ctx.beginPath();

        for (let i = 0; i <= numPoints; i++) {
            const angle = i * angleStep;
            const magnitude = magnitudes[i % numPoints];
            const radius = innerRadius + magnitude * this.maxRadius * 0.5;

            const x = this.centerX + Math.cos(angle) * radius;
            const y = this.centerY + Math.sin(angle) * radius;

            if (i === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }

        this.ctx.closePath();

        // Create gradient fill
        const gradient = this.ctx.createRadialGradient(
            this.centerX, this.centerY, innerRadius,
            this.centerX, this.centerY, innerRadius + this.maxRadius * 0.5
        );

        const scheme = COLOR_SCHEMES[this.settings.colorScheme];
        const color1 = scheme.primary;
        const color2 = scheme.secondary;

        gradient.addColorStop(0, `rgba(${color1[0]}, ${color1[1]}, ${color1[2]}, 0.8)`);
        gradient.addColorStop(1, `rgba(${color2[0]}, ${color2[1]}, ${color2[2]}, 0.4)`);

        this.ctx.fillStyle = gradient;
        this.ctx.fill();

        // Draw outline
        this.ctx.strokeStyle = `rgb(${color1[0]}, ${color1[1]}, ${color1[2]})`;
        this.ctx.lineWidth = 2;
        this.ctx.stroke();
    }

    /**
     * Mode 5: Neon Tubes
     */
    renderNeonTubes(magnitudes) {
        const numBars = magnitudes.length;
        const angleStep = (Math.PI * 2) / numBars;
        const innerRadius = this.settings.innerRadius;

        // Glow effect
        this.ctx.shadowBlur = 30;

        for (let i = 0; i < numBars; i++) {
            const angle = i * angleStep - Math.PI / 2;
            const magnitude = magnitudes[i];
            const barLength = magnitude * this.maxRadius * 0.6;

            const x1 = this.centerX + Math.cos(angle) * innerRadius;
            const y1 = this.centerY + Math.sin(angle) * innerRadius;
            const x2 = this.centerX + Math.cos(angle) * (innerRadius + barLength);
            const y2 = this.centerY + Math.sin(angle) * (innerRadius + barLength);

            const color = this.getColor(i, numBars);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = 6;
            this.ctx.lineCap = 'round';

            this.ctx.beginPath();
            this.ctx.moveTo(x1, y1);
            this.ctx.lineTo(x2, y2);
            this.ctx.stroke();
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 6: Vinyl Grooves
     */
    renderVinylGrooves(magnitudes) {
        const numGrooves = 8;
        const innerRadius = this.settings.innerRadius - 50;

        this.ctx.strokeStyle = `rgba(${COLORS.TEXT_PRIMARY[0]}, ${COLORS.TEXT_PRIMARY[1]}, ${COLORS.TEXT_PRIMARY[2]}, 0.3)`;
        this.ctx.lineWidth = 1;

        // Draw concentric circles
        for (let i = 0; i < numGrooves; i++) {
            const radius = innerRadius + (i * 20);
            this.ctx.beginPath();
            this.ctx.arc(this.centerX, this.centerY, radius, 0, Math.PI * 2);
            this.ctx.stroke();
        }

        // Draw animated spectrum on grooves
        const numPoints = magnitudes.length;
        const angleStep = (Math.PI * 2) / numPoints;

        this.ctx.shadowBlur = 15;

        for (let i = 0; i < numPoints; i++) {
            const angle = i * angleStep;
            const magnitude = magnitudes[i];
            const radius = innerRadius + magnitude * 150;

            const x = this.centerX + Math.cos(angle) * radius;
            const y = this.centerY + Math.sin(angle) * radius;

            const color = this.getColor(i, numPoints);
            this.ctx.shadowColor = color;
            this.ctx.fillStyle = color;

            this.ctx.beginPath();
            this.ctx.arc(x, y, 2, 0, Math.PI * 2);
            this.ctx.fill();
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 7: Soul Aura
     */
    renderSoulAura(magnitudes) {
        const numLayers = 6;
        const innerRadius = this.settings.innerRadius;

        for (let layer = 0; layer < numLayers; layer++) {
            const alpha = 0.3 - (layer * 0.04);
            const layerRadius = innerRadius + (layer * 25);

            const numPoints = magnitudes.length;
            const angleStep = (Math.PI * 2) / numPoints;

            this.ctx.beginPath();

            for (let i = 0; i <= numPoints; i++) {
                const angle = i * angleStep;
                const magnitude = magnitudes[i % numPoints];
                const radius = layerRadius + magnitude * 80;

                const x = this.centerX + Math.cos(angle) * radius;
                const y = this.centerY + Math.sin(angle) * radius;

                if (i === 0) {
                    this.ctx.moveTo(x, y);
                } else {
                    this.ctx.lineTo(x, y);
                }
            }

            this.ctx.closePath();

            const scheme = COLOR_SCHEMES[this.settings.colorScheme];
            const color = scheme.primary;
            this.ctx.fillStyle = `rgba(${color[0]}, ${color[1]}, ${color[2]}, ${alpha})`;
            this.ctx.fill();
        }
    }

    /**
     * Mode 8: Liquid Mercury
     */
    renderLiquidMercury(magnitudes) {
        const numPoints = magnitudes.length;
        const angleStep = (Math.PI * 2) / numPoints;
        const innerRadius = this.settings.innerRadius;
        const time = this.frameCounter * 0.02;

        this.ctx.shadowBlur = 25;
        this.ctx.shadowColor = 'rgba(200, 200, 220, 0.5)';

        this.ctx.beginPath();

        for (let i = 0; i <= numPoints; i++) {
            const angle = i * angleStep;
            const magnitude = magnitudes[i % numPoints];
            const wave = Math.sin(angle * 3 + time) * 15;
            const radius = innerRadius + magnitude * this.maxRadius * 0.4 + wave;

            const x = this.centerX + Math.cos(angle) * radius;
            const y = this.centerY + Math.sin(angle) * radius;

            if (i === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }

        this.ctx.closePath();

        // Metallic gradient
        const gradient = this.ctx.createRadialGradient(
            this.centerX, this.centerY, innerRadius * 0.5,
            this.centerX, this.centerY, innerRadius + this.maxRadius * 0.4
        );

        gradient.addColorStop(0, 'rgba(240, 240, 250, 0.9)');
        gradient.addColorStop(0.5, 'rgba(180, 180, 200, 0.8)');
        gradient.addColorStop(1, 'rgba(120, 120, 140, 0.6)');

        this.ctx.fillStyle = gradient;
        this.ctx.fill();

        this.ctx.strokeStyle = 'rgba(200, 200, 220, 0.9)';
        this.ctx.lineWidth = 2;
        this.ctx.stroke();

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 9: Aurora Waves
     */
    renderAuroraWaves(magnitudes) {
        const numWaves = 4;
        const innerRadius = this.settings.innerRadius;
        const time = this.frameCounter * 0.01;

        for (let wave = 0; wave < numWaves; wave++) {
            const waveOffset = wave * 0.5;
            const numPoints = magnitudes.length;
            const angleStep = (Math.PI * 2) / numPoints;

            this.ctx.beginPath();

            for (let i = 0; i <= numPoints; i++) {
                const angle = i * angleStep;
                const magnitude = magnitudes[i % numPoints];
                const waveMod = Math.sin(angle * 2 + time + waveOffset) * 20;
                const radius = innerRadius + (wave * 30) + magnitude * 60 + waveMod;

                const x = this.centerX + Math.cos(angle) * radius;
                const y = this.centerY + Math.sin(angle) * radius;

                if (i === 0) {
                    this.ctx.moveTo(x, y);
                } else {
                    this.ctx.lineTo(x, y);
                }
            }

            this.ctx.closePath();

            const alpha = 0.3 - (wave * 0.05);
            const color = this.getColor(wave * 25, 100);
            const rgbMatch = color.match(/\d+/g);
            if (rgbMatch) {
                this.ctx.fillStyle = `rgba(${rgbMatch[0]}, ${rgbMatch[1]}, ${rgbMatch[2]}, ${alpha})`;
                this.ctx.fill();
            }
        }
    }

    /**
     * Mode 10: Mandala Growth
     */
    renderMandalaGrowth(magnitudes) {
        const symmetry = 8;
        const numBars = magnitudes.length / symmetry;
        const angleStep = (Math.PI * 2) / (numBars * symmetry);
        const innerRadius = this.settings.innerRadius;

        this.ctx.shadowBlur = 20;

        for (let sym = 0; sym < symmetry; sym++) {
            const symAngle = (Math.PI * 2 / symmetry) * sym;

            for (let i = 0; i < numBars; i++) {
                const angle = i * angleStep * symmetry + symAngle;
                const magnitude = magnitudes[i % magnitudes.length];
                const barLength = magnitude * this.maxRadius * 0.5;

                const x1 = this.centerX + Math.cos(angle) * innerRadius;
                const y1 = this.centerY + Math.sin(angle) * innerRadius;
                const x2 = this.centerX + Math.cos(angle) * (innerRadius + barLength);
                const y2 = this.centerY + Math.sin(angle) * (innerRadius + barLength);

                const color = this.getColor(i, numBars);
                this.ctx.shadowColor = color;
                this.ctx.strokeStyle = color;
                this.ctx.lineWidth = 3;
                this.ctx.lineCap = 'round';

                this.ctx.beginPath();
                this.ctx.moveTo(x1, y1);
                this.ctx.lineTo(x2, y2);
                this.ctx.stroke();
            }
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Generate preview frame
     */
    generatePreview(magnitudes) {
        if (!magnitudes) {
            // Generate demo data
            magnitudes = new Float32Array(this.settings.numBars);
            for (let i = 0; i < magnitudes.length; i++) {
                magnitudes[i] = Math.random() * 0.5 + 0.3;
            }
        }

        this.render(magnitudes);
    }

    /**
     * Dispose resources
     */
    dispose() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
            this.animationId = null;
        }
        this.clear();
    }
}

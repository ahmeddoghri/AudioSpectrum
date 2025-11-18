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

        // Check if we have a 3-color gradient
        if (scheme.tertiary && scheme.colorCount === 3) {
            const color1 = scheme.primary;
            const color2 = scheme.secondary;
            const color3 = scheme.tertiary;

            let r, g, b;

            if (t < 0.5) {
                // Interpolate between primary and secondary (first half)
                const t1 = t * 2; // Map 0-0.5 to 0-1
                r = Math.round(Utils.lerp(color1[0], color2[0], t1));
                g = Math.round(Utils.lerp(color1[1], color2[1], t1));
                b = Math.round(Utils.lerp(color1[2], color2[2], t1));
            } else {
                // Interpolate between secondary and tertiary (second half)
                const t2 = (t - 0.5) * 2; // Map 0.5-1 to 0-1
                r = Math.round(Utils.lerp(color2[0], color3[0], t2));
                g = Math.round(Utils.lerp(color2[1], color3[1], t2));
                b = Math.round(Utils.lerp(color2[2], color3[2], t2));
            }

            return `rgb(${r}, ${g}, ${b})`;
        } else {
            // 2-color gradient
            const color1 = scheme.primary;
            const color2 = scheme.secondary;

            const r = Math.round(Utils.lerp(color1[0], color2[0], t));
            const g = Math.round(Utils.lerp(color1[1], color2[1], t));
            const b = Math.round(Utils.lerp(color1[2], color2[2], t));

            return `rgb(${r}, ${g}, ${b})`;
        }
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
            // Classic Styles
            case 'circular_bars':
                this.renderCircularBars(magnitudes);
                break;
            case 'waves':
                this.renderWaves(magnitudes);
                break;
            case 'smooth_waveform':
                this.renderSmoothWaveform(magnitudes);
                break;
            case 'frequency_bars':
                this.renderFrequencyBars(magnitudes);
                break;
            case 'linear_spectrum':
                this.renderLinearSpectrum(magnitudes);
                break;

            // Particle Effects
            case 'particles':
                this.renderParticles(magnitudes);
                break;
            case 'fireworks':
                this.renderFireworks(magnitudes);
                break;
            case 'cosmic_dust':
                this.renderCosmicDust(magnitudes);
                break;
            case 'particle_rain':
                this.renderParticleRain(magnitudes);
                break;
            case 'snow_particles':
                this.renderSnowParticles(magnitudes);
                break;

            // Retro & Vintage
            case 'neon_tubes':
                this.renderNeonTubes(magnitudes);
                break;
            case 'vinyl_grooves':
                this.renderVinylGrooves(magnitudes);
                break;
            case 'retro_cassette':
                this.renderRetroCassette(magnitudes);
                break;
            case 'pixel_clouds':
                this.renderPixelClouds(magnitudes);
                break;
            case 'neon_cityscape':
                this.renderNeonCityscape(magnitudes);
                break;

            // Fluid & Organic
            case 'soul_aura':
                this.renderSoulAura(magnitudes);
                break;
            case 'liquid_mercury':
                this.renderLiquidMercury(magnitudes);
                break;
            case 'lava_lamp':
                this.renderLavaLamp(magnitudes);
                break;
            case 'ink_drops':
                this.renderInkDrops(magnitudes);
                break;
            case 'water_ripples':
                this.renderWaterRipples(magnitudes);
                break;

            // Nature & Ethereal
            case 'aurora_waves':
                this.renderAuroraWaves(magnitudes);
                break;
            case 'crystal_growth':
                this.renderCrystalGrowth(magnitudes);
                break;
            case 'frequency_flowers':
                this.renderFrequencyFlowers(magnitudes);
                break;
            case 'fire_dance':
                this.renderFireDance(magnitudes);
                break;
            case 'bioluminescence':
                this.renderBioluminescence(magnitudes);
                break;

            // Geometric & Mathematical
            case 'mandala_growth':
                this.renderMandalaGrowth(magnitudes);
                break;
            case 'kaleidoscope':
                this.renderKaleidoscope(magnitudes);
                break;
            case 'fractal_bloom':
                this.renderFractalBloom(magnitudes);
                break;
            case 'morphing_geometry':
                this.renderMorphingGeometry(magnitudes);
                break;
            case 'spiral_galaxy':
                this.renderSpiralGalaxy(magnitudes);
                break;

            // Scientific & Physics
            case 'dna_helix':
                this.renderDnaHelix(magnitudes);
                break;
            case 'quantum_strings':
                this.renderQuantumStrings(magnitudes);
                break;
            case 'magnetic_fields':
                this.renderMagneticFields(magnitudes);
                break;
            case 'gravitational_lens':
                this.renderGravitationalLens(magnitudes);
                break;
            case 'seismic_waves':
                this.renderSeismicWaves(magnitudes);
                break;

            // Tech & Futuristic
            case 'tunnel_vision':
                this.renderTunnelVision(magnitudes);
                break;
            case 'matrix_code':
                this.renderMatrixCode(magnitudes);
                break;
            case 'hologram_glitch':
                this.renderHologramGlitch(magnitudes);
                break;
            case 'circuit_board':
                this.renderCircuitBoard(magnitudes);
                break;
            case 'neural_network':
                this.renderNeuralNetwork(magnitudes);
                break;

            // Energy & Abstract
            case 'lightning_strikes':
                this.renderLightningStrikes(magnitudes);
                break;
            case 'plasma_storm':
                this.renderPlasmaStorm(magnitudes);
                break;
            case 'laser_show':
                this.renderLaserShow(magnitudes);
                break;
            case 'energy_pulses':
                this.renderEnergyPulses(magnitudes);
                break;
            case 'rainbow_prism':
                this.renderRainbowPrism(magnitudes);
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

        const scheme = COLOR_SCHEMES[this.settings.colorScheme];
        const color1 = scheme.primary;
        const color2 = scheme.secondary;

        this.ctx.shadowBlur = 25;
        this.ctx.shadowColor = `rgba(${color1[0]}, ${color1[1]}, ${color1[2]}, 0.5)`;

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

        // Fluid gradient using color scheme
        const gradient = this.ctx.createRadialGradient(
            this.centerX, this.centerY, innerRadius * 0.5,
            this.centerX, this.centerY, innerRadius + this.maxRadius * 0.4
        );

        gradient.addColorStop(0, `rgba(${color1[0]}, ${color1[1]}, ${color1[2]}, 0.9)`);
        gradient.addColorStop(0.5, `rgba(${Math.round((color1[0] + color2[0]) / 2)}, ${Math.round((color1[1] + color2[1]) / 2)}, ${Math.round((color1[2] + color2[2]) / 2)}, 0.8)`);
        gradient.addColorStop(1, `rgba(${color2[0]}, ${color2[1]}, ${color2[2]}, 0.6)`);

        this.ctx.fillStyle = gradient;
        this.ctx.fill();

        this.ctx.strokeStyle = `rgba(${color1[0]}, ${color1[1]}, ${color1[2]}, 0.9)`;
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
     * Mode 11: Frequency Bars
     */
    renderFrequencyBars(magnitudes) {
        const numBars = magnitudes.length;
        const barWidth = this.canvas.width / numBars;
        const centerY = this.canvas.height / 2;

        this.ctx.shadowBlur = 10;

        for (let i = 0; i < numBars; i++) {
            const barHeight = magnitudes[i] * this.canvas.height * 0.7;
            const x = i * barWidth;
            const y = centerY - barHeight / 2;

            const color = this.getColor(i, numBars);
            this.ctx.shadowColor = color;
            this.ctx.fillStyle = color;

            this.ctx.fillRect(x, y, barWidth * 0.8, barHeight);
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 12: Linear Spectrum
     */
    renderLinearSpectrum(magnitudes) {
        const numBars = magnitudes.length;
        const barWidth = this.canvas.width / numBars;
        const baseY = this.canvas.height * 0.75;

        this.ctx.shadowBlur = 12;

        for (let i = 0; i < numBars; i++) {
            const barHeight = magnitudes[i] * this.canvas.height * 0.6;
            const x = i * barWidth;
            const y = baseY - barHeight;

            const color = this.getColor(i, numBars);
            this.ctx.shadowColor = color;
            this.ctx.fillStyle = color;

            this.ctx.fillRect(x, y, barWidth * 0.9, barHeight);
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 13: Fireworks
     */
    renderFireworks(magnitudes) {
        const numBars = magnitudes.length;
        const angleStep = (Math.PI * 2) / numBars;

        this.ctx.shadowBlur = 30;

        for (let i = 0; i < numBars; i++) {
            const angle = i * angleStep;
            const magnitude = magnitudes[i];
            const distance = magnitude * this.maxRadius * 1.2;

            const x = this.centerX + Math.cos(angle) * distance;
            const y = this.centerY + Math.sin(angle) * distance;

            // Trail effect
            for (let t = 0; t < 3; t++) {
                const trailDist = distance * (0.5 + t * 0.2);
                const tx = this.centerX + Math.cos(angle) * trailDist;
                const ty = this.centerY + Math.sin(angle) * trailDist;
                const size = (3 - t) * magnitude * 3;

                const color = this.getColor(i, numBars);
                this.ctx.shadowColor = color;
                this.ctx.fillStyle = color;
                this.ctx.globalAlpha = 0.3 + t * 0.3;

                this.ctx.beginPath();
                this.ctx.arc(tx, ty, size, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 14: Cosmic Dust
     */
    renderCosmicDust(magnitudes) {
        const numParticles = magnitudes.length * 3;
        const time = this.frameCounter * 0.01;

        this.ctx.shadowBlur = 20;

        for (let i = 0; i < numParticles; i++) {
            const angle = (i / numParticles) * Math.PI * 2 + time;
            const magnitude = magnitudes[i % magnitudes.length];
            const spiral = i / numParticles;
            const distance = this.settings.innerRadius + spiral * this.maxRadius * 0.8 + magnitude * 50;

            const x = this.centerX + Math.cos(angle) * distance;
            const y = this.centerY + Math.sin(angle) * distance;
            const size = 2 + magnitude * 4;

            const color = this.getColor(i, numParticles);
            this.ctx.shadowColor = color;
            this.ctx.fillStyle = color;
            this.ctx.globalAlpha = 0.6 + magnitude * 0.4;

            this.ctx.beginPath();
            this.ctx.arc(x, y, size, 0, Math.PI * 2);
            this.ctx.fill();
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 15: Particle Rain
     */
    renderParticleRain(magnitudes) {
        const numBars = magnitudes.length;
        const barWidth = this.canvas.width / numBars;

        this.ctx.shadowBlur = 15;

        for (let i = 0; i < numBars; i++) {
            const magnitude = magnitudes[i];
            const numDrops = Math.floor(magnitude * 8);
            const x = i * barWidth + barWidth / 2;

            for (let d = 0; d < numDrops; d++) {
                const y = (d / numDrops) * this.canvas.height;
                const size = 2 + magnitude * 3;

                const color = this.getColor(i, numBars);
                this.ctx.shadowColor = color;
                this.ctx.fillStyle = color;
                this.ctx.globalAlpha = 0.4 + (d / numDrops) * 0.4;

                this.ctx.beginPath();
                this.ctx.arc(x, y, size, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 16: Snow Particles
     */
    renderSnowParticles(magnitudes) {
        const numFlakes = magnitudes.length * 2;
        const time = this.frameCounter * 0.005;

        this.ctx.shadowBlur = 10;

        for (let i = 0; i < numFlakes; i++) {
            const magnitude = magnitudes[i % magnitudes.length];
            const x = (i / numFlakes) * this.canvas.width + Math.sin(time + i) * 30;
            const y = ((time * 50 + i * 50) % this.canvas.height);
            const size = 1 + magnitude * 4;

            const color = this.getColor(i, numFlakes);
            this.ctx.shadowColor = color;
            this.ctx.fillStyle = color;
            this.ctx.globalAlpha = 0.5 + magnitude * 0.5;

            this.ctx.beginPath();
            this.ctx.arc(x, y, size, 0, Math.PI * 2);
            this.ctx.fill();
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 17: Retro Cassette
     */
    renderRetroCassette(magnitudes) {
        const centerY = this.canvas.height / 2;
        const barHeight = 100;
        const numBars = Math.min(magnitudes.length, 64);
        const barWidth = this.canvas.width * 0.6 / numBars;
        const startX = this.canvas.width * 0.2;

        // Draw VU meter background
        this.ctx.strokeStyle = this.getColor(0, numBars);
        this.ctx.lineWidth = 3;
        this.ctx.strokeRect(startX - 10, centerY - barHeight / 2 - 10, this.canvas.width * 0.6 + 20, barHeight + 20);

        // Draw bars
        for (let i = 0; i < numBars; i++) {
            const magnitude = magnitudes[i];
            const height = magnitude * barHeight;
            const x = startX + i * barWidth;
            const y = centerY - height / 2;

            const color = this.getColor(i, numBars);
            this.ctx.fillStyle = color;
            this.ctx.fillRect(x, y, barWidth * 0.8, height);
        }

        // Draw spinning reels
        const time = this.frameCounter * 0.1;
        const reel1X = this.canvas.width * 0.3;
        const reel2X = this.canvas.width * 0.7;
        const reelY = this.canvas.height * 0.3;
        const reelRadius = 40;

        for (const reelX of [reel1X, reel2X]) {
            this.ctx.strokeStyle = this.getColor(30, numBars);
            this.ctx.lineWidth = 3;
            this.ctx.beginPath();
            this.ctx.arc(reelX, reelY, reelRadius, 0, Math.PI * 2);
            this.ctx.stroke();

            // Spokes
            for (let s = 0; s < 6; s++) {
                const angle = (s / 6) * Math.PI * 2 + time;
                this.ctx.beginPath();
                this.ctx.moveTo(reelX, reelY);
                this.ctx.lineTo(reelX + Math.cos(angle) * reelRadius, reelY + Math.sin(angle) * reelRadius);
                this.ctx.stroke();
            }
        }
    }

    /**
     * Mode 18: Pixel Clouds
     */
    renderPixelClouds(magnitudes) {
        const pixelSize = 12;
        const numClouds = magnitudes.length / 2;
        const time = this.frameCounter * 0.02;

        for (let i = 0; i < numClouds; i++) {
            const magnitude = magnitudes[i % magnitudes.length];
            const x = ((i * 137.5 + time * 20) % this.canvas.width);
            const y = (i * 17) % this.canvas.height;
            const size = Math.floor(2 + magnitude * 5);

            const color = this.getColor(i, numClouds);
            this.ctx.fillStyle = color;

            // Draw pixelated cloud
            for (let px = 0; px < size; px++) {
                for (let py = 0; py < size; py++) {
                    if (Math.random() > 0.3) {
                        this.ctx.fillRect(x + px * pixelSize, y + py * pixelSize, pixelSize, pixelSize);
                    }
                }
            }
        }
    }

    /**
     * Mode 19: Neon Cityscape
     */
    renderNeonCityscape(magnitudes) {
        const numBuildings = magnitudes.length;
        const buildingWidth = this.canvas.width / numBuildings;
        const baseY = this.canvas.height * 0.9;

        this.ctx.shadowBlur = 25;

        for (let i = 0; i < numBuildings; i++) {
            const magnitude = magnitudes[i];
            const height = 50 + magnitude * this.canvas.height * 0.7;
            const x = i * buildingWidth;
            const y = baseY - height;

            const color = this.getColor(i, numBuildings);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = 2;

            // Building outline
            this.ctx.strokeRect(x + 2, y, buildingWidth - 4, height);

            // Windows
            const windowRows = Math.floor(height / 20);
            for (let w = 0; w < windowRows; w++) {
                if (magnitude > 0.3) {
                    this.ctx.fillStyle = color;
                    this.ctx.globalAlpha = 0.6;
                    this.ctx.fillRect(x + buildingWidth / 4, y + w * 20 + 5, buildingWidth / 4, 10);
                }
            }
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 20: Lava Lamp
     */
    renderLavaLamp(magnitudes) {
        const numBlobs = Math.min(magnitudes.length / 4, 12);
        const time = this.frameCounter * 0.01;

        this.ctx.shadowBlur = 30;

        for (let i = 0; i < numBlobs; i++) {
            const magnitude = magnitudes[i * 4] || magnitudes[i];
            const x = this.centerX + Math.sin(time + i * 2) * this.maxRadius * 0.5;
            const y = this.centerY + Math.cos(time * 0.7 + i * 1.5) * this.maxRadius * 0.6;
            const radius = 30 + magnitude * 80;

            const color = this.getColor(i * 8, numBlobs * 8);
            this.ctx.shadowColor = color;
            this.ctx.fillStyle = color;
            this.ctx.globalAlpha = 0.6;

            this.ctx.beginPath();
            this.ctx.arc(x, y, radius, 0, Math.PI * 2);
            this.ctx.fill();
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 21: Ink Drops
     */
    renderInkDrops(magnitudes) {
        const numDrops = Math.min(magnitudes.length / 3, 20);
        const time = this.frameCounter * 0.02;

        this.ctx.shadowBlur = 25;

        for (let i = 0; i < numDrops; i++) {
            const magnitude = magnitudes[i * 3] || magnitudes[i];
            const age = (time + i) % 10;
            const expansion = age / 10;

            const x = this.centerX + (Math.random() - 0.5) * 100;
            const y = this.centerY + (Math.random() - 0.5) * 100;
            const radius = expansion * magnitude * 100;

            const color = this.getColor(i * 4, numDrops * 4);
            this.ctx.shadowColor = color;
            this.ctx.fillStyle = color;
            this.ctx.globalAlpha = Math.max(0, 0.8 - expansion);

            this.ctx.beginPath();
            this.ctx.arc(x, y, radius, 0, Math.PI * 2);
            this.ctx.fill();

            // Tendrils
            for (let t = 0; t < 5; t++) {
                const angle = (t / 5) * Math.PI * 2 + i;
                const length = expansion * magnitude * 120;
                this.ctx.beginPath();
                this.ctx.moveTo(x, y);
                this.ctx.lineTo(x + Math.cos(angle) * length, y + Math.sin(angle) * length);
                this.ctx.strokeStyle = color;
                this.ctx.lineWidth = 2;
                this.ctx.stroke();
            }
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 22: Water Ripples
     */
    renderWaterRipples(magnitudes) {
        const numRipples = 8;
        const time = this.frameCounter * 0.05;

        this.ctx.shadowBlur = 15;

        for (let r = 0; r < numRipples; r++) {
            const phase = (time + r * 0.5) % 5;
            const radius = this.settings.innerRadius * 0.5 + phase * 60;

            const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
            const thickness = 1 + avgMagnitude * 3;

            const color = this.getColor(r * 10, numRipples * 10);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = thickness;
            this.ctx.globalAlpha = Math.max(0, 1 - phase / 5);

            this.ctx.beginPath();
            this.ctx.arc(this.centerX, this.centerY, radius, 0, Math.PI * 2);
            this.ctx.stroke();
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 23: Crystal Growth
     */
    renderCrystalGrowth(magnitudes) {
        const numCrystals = magnitudes.length;
        const angleStep = (Math.PI * 2) / numCrystals;
        const innerRadius = this.settings.innerRadius;

        this.ctx.shadowBlur = 20;

        for (let i = 0; i < numCrystals; i++) {
            const angle = i * angleStep;
            const magnitude = magnitudes[i];
            const length = magnitude * this.maxRadius * 0.6;

            const x1 = this.centerX + Math.cos(angle) * innerRadius;
            const y1 = this.centerY + Math.sin(angle) * innerRadius;
            const x2 = this.centerX + Math.cos(angle) * (innerRadius + length);
            const y2 = this.centerY + Math.sin(angle) * (innerRadius + length);

            const color = this.getColor(i, numCrystals);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;

            // Main crystal spike
            this.ctx.lineWidth = 4;
            this.ctx.beginPath();
            this.ctx.moveTo(x1, y1);
            this.ctx.lineTo(x2, y2);
            this.ctx.stroke();

            // Crystal branches
            if (magnitude > 0.4) {
                for (let b = 0; b < 3; b++) {
                    const branchAngle = angle + (Math.random() - 0.5) * 0.5;
                    const branchLength = length * (0.3 + Math.random() * 0.3);
                    const branchX = x1 + Math.cos(branchAngle) * branchLength;
                    const branchY = y1 + Math.sin(branchAngle) * branchLength;

                    this.ctx.lineWidth = 2;
                    this.ctx.beginPath();
                    this.ctx.moveTo(x1, y1);
                    this.ctx.lineTo(branchX, branchY);
                    this.ctx.stroke();
                }
            }
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 24: Frequency Flowers
     */
    renderFrequencyFlowers(magnitudes) {
        const numPetals = magnitudes.length;
        const angleStep = (Math.PI * 2) / numPetals;
        const innerRadius = this.settings.innerRadius;

        this.ctx.shadowBlur = 20;

        for (let i = 0; i < numPetals; i++) {
            const angle = i * angleStep;
            const magnitude = magnitudes[i];
            const petalLength = magnitude * this.maxRadius * 0.5;

            const color = this.getColor(i, numPetals);
            this.ctx.shadowColor = color;
            this.ctx.fillStyle = color;
            this.ctx.globalAlpha = 0.7;

            // Draw petal shape
            this.ctx.beginPath();
            const x1 = this.centerX + Math.cos(angle - 0.2) * innerRadius;
            const y1 = this.centerY + Math.sin(angle - 0.2) * innerRadius;
            const x2 = this.centerX + Math.cos(angle) * (innerRadius + petalLength);
            const y2 = this.centerY + Math.sin(angle) * (innerRadius + petalLength);
            const x3 = this.centerX + Math.cos(angle + 0.2) * innerRadius;
            const y3 = this.centerY + Math.sin(angle + 0.2) * innerRadius;

            this.ctx.moveTo(x1, y1);
            this.ctx.quadraticCurveTo(x2, y2, x3, y3);
            this.ctx.lineTo(this.centerX, this.centerY);
            this.ctx.closePath();
            this.ctx.fill();
        }

        // Draw center
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        this.ctx.fillStyle = this.getColor(0, numPetals);
        this.ctx.globalAlpha = 1;
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, innerRadius * 0.3 + avgMagnitude * 20, 0, Math.PI * 2);
        this.ctx.fill();

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 25: Fire Dance
     */
    renderFireDance(magnitudes) {
        const numFlames = magnitudes.length;
        const flameWidth = this.canvas.width / numFlames;
        const baseY = this.canvas.height * 0.8;

        this.ctx.shadowBlur = 30;

        for (let i = 0; i < numFlames; i++) {
            const magnitude = magnitudes[i];
            const x = i * flameWidth + flameWidth / 2;
            const height = magnitude * this.canvas.height * 0.6;

            const color = this.getColor(i, numFlames);
            this.ctx.shadowColor = color;

            // Draw flame shape
            this.ctx.beginPath();
            this.ctx.moveTo(x, baseY);

            for (let h = 0; h < height; h += 10) {
                const flicker = Math.sin(this.frameCounter * 0.1 + i + h * 0.1) * 5;
                const width = (1 - h / height) * flameWidth * 0.4;
                this.ctx.lineTo(x + flicker, baseY - h);
            }

            this.ctx.lineTo(x, baseY - height);
            this.ctx.lineTo(x, baseY);
            this.ctx.closePath();

            this.ctx.fillStyle = color;
            this.ctx.globalAlpha = 0.7;
            this.ctx.fill();
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 26: Ocean Bioluminescence
     */
    renderBioluminescence(magnitudes) {
        const numOrganisms = magnitudes.length * 2;
        const time = this.frameCounter * 0.01;

        this.ctx.shadowBlur = 25;

        for (let i = 0; i < numOrganisms; i++) {
            const magnitude = magnitudes[i % magnitudes.length];
            const swimPattern = Math.sin(time + i * 0.5) * 100;
            const x = ((i / numOrganisms) * this.canvas.width + swimPattern) % this.canvas.width;
            const y = (i * 17 % this.canvas.height);
            const size = 3 + magnitude * 8;
            const pulse = Math.sin(time * 2 + i) * 0.3 + 0.7;

            const color = this.getColor(i, numOrganisms);
            this.ctx.shadowColor = color;
            this.ctx.fillStyle = color;
            this.ctx.globalAlpha = pulse * magnitude;

            // Draw organism
            this.ctx.beginPath();
            this.ctx.arc(x, y, size, 0, Math.PI * 2);
            this.ctx.fill();

            // Trail
            for (let t = 1; t < 4; t++) {
                this.ctx.globalAlpha = (pulse * magnitude) / (t + 1);
                this.ctx.beginPath();
                this.ctx.arc(x - t * 8, y, size * (1 - t * 0.2), 0, Math.PI * 2);
                this.ctx.fill();
            }
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 27: Kaleidoscope
     */
    renderKaleidoscope(magnitudes) {
        const segments = 8;
        const numBars = magnitudes.length / segments;
        const angleStep = (Math.PI * 2) / segments;
        const innerRadius = this.settings.innerRadius;

        this.ctx.shadowBlur = 15;

        for (let seg = 0; seg < segments; seg++) {
            this.ctx.save();
            this.ctx.translate(this.centerX, this.centerY);
            this.ctx.rotate(seg * angleStep);

            for (let i = 0; i < numBars; i++) {
                const magnitude = magnitudes[Math.floor(i % magnitudes.length)];
                const barAngle = (i / numBars) * angleStep;
                const distance = innerRadius + magnitude * this.maxRadius * 0.5;

                const x = Math.cos(barAngle) * distance;
                const y = Math.sin(barAngle) * distance;
                const size = 3 + magnitude * 6;

                const color = this.getColor(i, numBars);
                this.ctx.shadowColor = color;
                this.ctx.fillStyle = color;

                this.ctx.beginPath();
                this.ctx.arc(x, y, size, 0, Math.PI * 2);
                this.ctx.fill();
            }

            this.ctx.restore();
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 28: Fractal Bloom
     */
    renderFractalBloom(magnitudes) {
        const depth = 4;
        const baseAngle = this.frameCounter * 0.01;

        this.ctx.shadowBlur = 15;

        const drawBranch = (x, y, angle, length, iteration, colorIndex) => {
            if (iteration >= depth) return;

            const magnitude = magnitudes[colorIndex % magnitudes.length];
            const endX = x + Math.cos(angle) * length;
            const endY = y + Math.sin(angle) * length;

            const color = this.getColor(colorIndex, magnitudes.length);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = (depth - iteration) * magnitude * 2;

            this.ctx.beginPath();
            this.ctx.moveTo(x, y);
            this.ctx.lineTo(endX, endY);
            this.ctx.stroke();

            const newLength = length * 0.7;
            drawBranch(endX, endY, angle - 0.5, newLength, iteration + 1, colorIndex + 1);
            drawBranch(endX, endY, angle + 0.5, newLength, iteration + 1, colorIndex + 2);
        };

        for (let i = 0; i < 6; i++) {
            const startAngle = baseAngle + (i / 6) * Math.PI * 2;
            drawBranch(this.centerX, this.centerY, startAngle, 80, 0, i * 10);
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 29: Morphing Geometry
     */
    renderMorphingGeometry(magnitudes) {
        const time = this.frameCounter * 0.02;
        const sides = 3 + Math.floor(Math.sin(time) * 3 + 4);
        const angleStep = (Math.PI * 2) / sides;
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const radius = this.settings.innerRadius + avgMagnitude * this.maxRadius * 0.4;

        this.ctx.shadowBlur = 20;

        // Main shape
        this.ctx.beginPath();
        for (let i = 0; i <= sides; i++) {
            const angle = i * angleStep + time;
            const magnitude = magnitudes[i % magnitudes.length];
            const r = radius + magnitude * 50;
            const x = this.centerX + Math.cos(angle) * r;
            const y = this.centerY + Math.sin(angle) * r;

            if (i === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }
        this.ctx.closePath();

        const color = this.getColor(Math.floor(time * 10), 100);
        this.ctx.shadowColor = color;
        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = 3;
        this.ctx.stroke();

        // Inner wireframe
        this.ctx.globalAlpha = 0.5;
        this.ctx.beginPath();
        for (let i = 0; i < sides; i++) {
            const angle = i * angleStep + time;
            const x = this.centerX + Math.cos(angle) * radius * 0.5;
            const y = this.centerY + Math.sin(angle) * radius * 0.5;

            this.ctx.moveTo(this.centerX, this.centerY);
            this.ctx.lineTo(x, y);
        }
        this.ctx.stroke();

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 30: Spiral Galaxy
     */
    renderSpiralGalaxy(magnitudes) {
        const numArms = 3;
        const particlesPerArm = magnitudes.length / numArms;
        const time = this.frameCounter * 0.01;

        this.ctx.shadowBlur = 20;

        for (let arm = 0; arm < numArms; arm++) {
            const armAngle = (arm / numArms) * Math.PI * 2;

            for (let i = 0; i < particlesPerArm; i++) {
                const t = i / particlesPerArm;
                const magnitude = magnitudes[Math.floor(arm * particlesPerArm + i) % magnitudes.length];
                const spiralAngle = armAngle + t * Math.PI * 4 + time;
                const distance = this.settings.innerRadius * 0.3 + t * this.maxRadius * 0.8;

                const x = this.centerX + Math.cos(spiralAngle) * distance;
                const y = this.centerY + Math.sin(spiralAngle) * distance;
                const size = 2 + magnitude * 5;

                const color = this.getColor(Math.floor(arm * particlesPerArm + i), magnitudes.length);
                this.ctx.shadowColor = color;
                this.ctx.fillStyle = color;
                this.ctx.globalAlpha = 0.6 + magnitude * 0.4;

                this.ctx.beginPath();
                this.ctx.arc(x, y, size, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 31: DNA Helix
     */
    renderDnaHelix(magnitudes) {
        const time = this.frameCounter * 0.05;
        const numPairs = magnitudes.length / 2;
        const spacing = this.canvas.height / numPairs;

        this.ctx.shadowBlur = 15;

        for (let i = 0; i < numPairs; i++) {
            const y = i * spacing + spacing / 2;
            const phase = i * 0.5 + time;
            const magnitude = magnitudes[i % magnitudes.length];

            const x1 = this.centerX + Math.sin(phase) * (100 + magnitude * 50);
            const x2 = this.centerX - Math.sin(phase) * (100 + magnitude * 50);

            const color = this.getColor(i, numPairs);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;

            // Base pair connection
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            this.ctx.moveTo(x1, y);
            this.ctx.lineTo(x2, y);
            this.ctx.stroke();

            // Nucleotides
            this.ctx.fillStyle = color;
            this.ctx.beginPath();
            this.ctx.arc(x1, y, 4 + magnitude * 4, 0, Math.PI * 2);
            this.ctx.fill();
            this.ctx.beginPath();
            this.ctx.arc(x2, y, 4 + magnitude * 4, 0, Math.PI * 2);
            this.ctx.fill();

            // Helix strands
            if (i > 0) {
                const prevY = (i - 1) * spacing + spacing / 2;
                const prevPhase = (i - 1) * 0.5 + time;
                const prevX1 = this.centerX + Math.sin(prevPhase) * (100 + magnitude * 50);
                const prevX2 = this.centerX - Math.sin(prevPhase) * (100 + magnitude * 50);

                this.ctx.lineWidth = 3;
                this.ctx.beginPath();
                this.ctx.moveTo(prevX1, prevY);
                this.ctx.lineTo(x1, y);
                this.ctx.stroke();
                this.ctx.beginPath();
                this.ctx.moveTo(prevX2, prevY);
                this.ctx.lineTo(x2, y);
                this.ctx.stroke();
            }
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 32: Quantum Strings
     */
    renderQuantumStrings(magnitudes) {
        const numStrings = Math.min(magnitudes.length / 2, 20);
        const time = this.frameCounter * 0.02;

        this.ctx.shadowBlur = 20;

        for (let s = 0; s < numStrings; s++) {
            const magnitude = magnitudes[s * 2 % magnitudes.length];
            const startX = (s / numStrings) * this.canvas.width;
            const numPoints = 50;

            const color = this.getColor(s, numStrings);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = 1 + magnitude * 2;

            this.ctx.beginPath();

            for (let i = 0; i < numPoints; i++) {
                const t = i / numPoints;
                const x = startX + (t * this.canvas.width);
                const y = this.centerY + Math.sin(t * Math.PI * 4 + time + s) * magnitude * 100;

                if (i === 0) {
                    this.ctx.moveTo(x, y);
                } else {
                    this.ctx.lineTo(x, y);
                }
            }

            this.ctx.stroke();
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 33: Magnetic Fields
     */
    renderMagneticFields(magnitudes) {
        const numLines = magnitudes.length / 2;

        this.ctx.shadowBlur = 10;

        for (let i = 0; i < numLines; i++) {
            const magnitude = magnitudes[i % magnitudes.length];
            const startY = (i / numLines) * this.canvas.height;

            const color = this.getColor(i, numLines);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = 1 + magnitude * 2;

            this.ctx.beginPath();

            const numPoints = 100;
            for (let p = 0; p < numPoints; p++) {
                const t = p / numPoints;
                const x = t * this.canvas.width;

                // Magnetic field curve
                const distFromCenter = Math.abs(startY - this.canvas.height / 2);
                const curve = Math.sin(t * Math.PI) * magnitude * (100 - distFromCenter * 0.3);
                const y = startY + curve;

                if (p === 0) {
                    this.ctx.moveTo(x, y);
                } else {
                    this.ctx.lineTo(x, y);
                }
            }

            this.ctx.stroke();
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 34: Gravitational Lens
     */
    renderGravitationalLens(magnitudes) {
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const numRings = 8;

        this.ctx.shadowBlur = 20;

        // Central mass
        const massRadius = 30 + avgMagnitude * 40;
        const color1 = this.getColor(0, numRings);
        this.ctx.shadowColor = color1;
        this.ctx.fillStyle = color1;
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, massRadius, 0, Math.PI * 2);
        this.ctx.fill();

        // Lensing rings
        for (let r = 0; r < numRings; r++) {
            const magnitude = magnitudes[r * (magnitudes.length / numRings)] || avgMagnitude;
            const baseRadius = this.settings.innerRadius + r * 40;

            const color = this.getColor(r * 10, numRings * 10);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = 2 + magnitude * 3;
            this.ctx.globalAlpha = 0.7;

            // Distorted ring
            this.ctx.beginPath();
            const numPoints = 100;
            for (let i = 0; i <= numPoints; i++) {
                const angle = (i / numPoints) * Math.PI * 2;
                const distortion = Math.sin(angle * 2) * magnitude * 20;
                const radius = baseRadius + distortion;

                const x = this.centerX + Math.cos(angle) * radius;
                const y = this.centerY + Math.sin(angle) * radius;

                if (i === 0) {
                    this.ctx.moveTo(x, y);
                } else {
                    this.ctx.lineTo(x, y);
                }
            }
            this.ctx.stroke();
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 35: Seismic Waves
     */
    renderSeismicWaves(magnitudes) {
        const centerY = this.canvas.height / 2;
        const numPoints = magnitudes.length;
        const spacing = this.canvas.width / numPoints;

        this.ctx.shadowBlur = 15;

        // Draw multiple seismic traces
        for (let trace = 0; trace < 3; trace++) {
            const yOffset = (trace - 1) * 100;
            const color = this.getColor(trace * 20, 60);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = 2;

            this.ctx.beginPath();

            for (let i = 0; i < numPoints; i++) {
                const x = i * spacing;
                const magnitude = magnitudes[i];
                const amplitude = magnitude * 80;
                const y = centerY + yOffset + (Math.random() - 0.5) * amplitude;

                if (i === 0) {
                    this.ctx.moveTo(x, y);
                } else {
                    this.ctx.lineTo(x, y);
                }
            }

            this.ctx.stroke();
        }

        // Draw grid
        this.ctx.strokeStyle = 'rgba(100, 100, 100, 0.2)';
        this.ctx.lineWidth = 1;
        for (let i = 0; i < 10; i++) {
            const y = (i / 10) * this.canvas.height;
            this.ctx.beginPath();
            this.ctx.moveTo(0, y);
            this.ctx.lineTo(this.canvas.width, y);
            this.ctx.stroke();
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 36: Tunnel Vision
     */
    renderTunnelVision(magnitudes) {
        const numRings = 20;
        const time = this.frameCounter * 0.05;

        this.ctx.shadowBlur = 25;

        for (let r = 0; r < numRings; r++) {
            const t = (r + time) % numRings;
            const radius = (t / numRings) * this.maxRadius * 1.5;
            const magnitude = magnitudes[r % magnitudes.length];

            const color = this.getColor(r, numRings);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = 3 + magnitude * 10;
            this.ctx.globalAlpha = 1 - (t / numRings);

            this.ctx.beginPath();
            this.ctx.arc(this.centerX, this.centerY, radius, 0, Math.PI * 2);
            this.ctx.stroke();
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 37: Matrix Code
     */
    renderMatrixCode(magnitudes) {
        const columns = Math.min(magnitudes.length, 60);
        const columnWidth = this.canvas.width / columns;
        const charHeight = 20;

        this.ctx.shadowBlur = 15;
        this.ctx.font = '14px monospace';

        for (let i = 0; i < columns; i++) {
            const magnitude = magnitudes[i];
            const numChars = Math.floor(magnitude * 30);

            const color = this.getColor(i, columns);
            this.ctx.shadowColor = color;

            for (let c = 0; c < numChars; c++) {
                const x = i * columnWidth + columnWidth / 2;
                const y = ((this.frameCounter * magnitude * 2 + c * charHeight) % this.canvas.height);
                const char = String.fromCharCode(0x30A0 + Math.floor(Math.random() * 96));

                const alpha = 1 - (c / numChars);
                this.ctx.fillStyle = color;
                this.ctx.globalAlpha = alpha * magnitude;
                this.ctx.fillText(char, x, y);
            }
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 38: Hologram Glitch
     */
    renderHologramGlitch(magnitudes) {
        const numBars = magnitudes.length;
        const angleStep = (Math.PI * 2) / numBars;
        const innerRadius = this.settings.innerRadius;
        const glitchIntensity = Math.max(...magnitudes);

        this.ctx.shadowBlur = 20;

        for (let i = 0; i < numBars; i++) {
            const angle = i * angleStep;
            const magnitude = magnitudes[i];

            // Glitch offset
            const glitchX = (Math.random() - 0.5) * glitchIntensity * 20;
            const glitchY = (Math.random() - 0.5) * glitchIntensity * 20;

            const barLength = magnitude * this.maxRadius * 0.6;
            const x1 = this.centerX + Math.cos(angle) * innerRadius + glitchX;
            const y1 = this.centerY + Math.sin(angle) * innerRadius + glitchY;
            const x2 = this.centerX + Math.cos(angle) * (innerRadius + barLength) + glitchX;
            const y2 = this.centerY + Math.sin(angle) * (innerRadius + barLength) + glitchY;

            const color = this.getColor(i, numBars);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = 3;
            this.ctx.globalAlpha = 0.6 + Math.random() * 0.4;

            this.ctx.beginPath();
            this.ctx.moveTo(x1, y1);
            this.ctx.lineTo(x2, y2);
            this.ctx.stroke();
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 39: Circuit Board
     */
    renderCircuitBoard(magnitudes) {
        const gridSize = 40;
        const cols = Math.floor(this.canvas.width / gridSize);
        const rows = Math.floor(this.canvas.height / gridSize);

        this.ctx.shadowBlur = 15;

        // Draw grid
        this.ctx.strokeStyle = this.getColor(0, magnitudes.length);
        this.ctx.lineWidth = 1;
        this.ctx.globalAlpha = 0.3;

        for (let x = 0; x < cols; x++) {
            for (let y = 0; y < rows; y++) {
                this.ctx.strokeRect(x * gridSize, y * gridSize, gridSize, gridSize);
            }
        }

        this.ctx.globalAlpha = 1;

        // Draw active paths
        const numPaths = Math.min(magnitudes.length / 2, cols);

        for (let i = 0; i < numPaths; i++) {
            const magnitude = magnitudes[i % magnitudes.length];
            if (magnitude < 0.3) continue;

            const x = (i % cols) * gridSize + gridSize / 2;
            const segments = Math.floor(magnitude * 10);

            const color = this.getColor(i, numPaths);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = 2;

            this.ctx.beginPath();
            this.ctx.moveTo(x, 0);

            let currentY = 0;
            for (let s = 0; s < segments; s++) {
                currentY += gridSize;
                if (currentY > this.canvas.height) break;

                const horizontalShift = (Math.random() > 0.5 ? 1 : -1) * gridSize;
                this.ctx.lineTo(x, currentY);
                this.ctx.lineTo(x + horizontalShift, currentY);
            }

            this.ctx.stroke();

            // Draw nodes
            this.ctx.fillStyle = color;
            this.ctx.beginPath();
            this.ctx.arc(x, 0, 4, 0, Math.PI * 2);
            this.ctx.fill();
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 40: Neural Network
     */
    renderNeuralNetwork(magnitudes) {
        const layers = 4;
        const nodesPerLayer = 8;
        const layerSpacing = this.canvas.width / (layers + 1);
        const nodeSpacing = this.canvas.height / (nodesPerLayer + 1);

        this.ctx.shadowBlur = 15;

        // Draw connections
        for (let l = 0; l < layers - 1; l++) {
            for (let n1 = 0; n1 < nodesPerLayer; n1++) {
                for (let n2 = 0; n2 < nodesPerLayer; n2++) {
                    const magnitude = magnitudes[(l * nodesPerLayer + n1) % magnitudes.length];

                    if (magnitude > 0.4) {
                        const x1 = (l + 1) * layerSpacing;
                        const y1 = (n1 + 1) * nodeSpacing;
                        const x2 = (l + 2) * layerSpacing;
                        const y2 = (n2 + 1) * nodeSpacing;

                        const color = this.getColor(l * nodesPerLayer + n1, magnitudes.length);
                        this.ctx.shadowColor = color;
                        this.ctx.strokeStyle = color;
                        this.ctx.lineWidth = magnitude * 2;
                        this.ctx.globalAlpha = magnitude * 0.6;

                        this.ctx.beginPath();
                        this.ctx.moveTo(x1, y1);
                        this.ctx.lineTo(x2, y2);
                        this.ctx.stroke();
                    }
                }
            }
        }

        this.ctx.globalAlpha = 1;

        // Draw nodes
        for (let l = 0; l < layers; l++) {
            for (let n = 0; n < nodesPerLayer; n++) {
                const x = (l + 1) * layerSpacing;
                const y = (n + 1) * nodeSpacing;
                const magnitude = magnitudes[(l * nodesPerLayer + n) % magnitudes.length];
                const size = 5 + magnitude * 10;

                const color = this.getColor(l * nodesPerLayer + n, magnitudes.length);
                this.ctx.shadowColor = color;
                this.ctx.fillStyle = color;

                this.ctx.beginPath();
                this.ctx.arc(x, y, size, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 41: Lightning Strikes
     */
    renderLightningStrikes(magnitudes) {
        const numBolts = magnitudes.length;

        this.ctx.shadowBlur = 25;

        for (let i = 0; i < numBolts; i++) {
            const magnitude = magnitudes[i];
            if (magnitude < 0.5) continue;

            const startX = (i / numBolts) * this.canvas.width;
            const startY = 0;
            const endY = this.canvas.height;

            const color = this.getColor(i, numBolts);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = 2 + magnitude * 4;

            this.ctx.beginPath();
            this.ctx.moveTo(startX, startY);

            let currentX = startX;
            let currentY = startY;
            const segments = 10 + Math.floor(magnitude * 10);

            for (let s = 0; s < segments; s++) {
                currentY += (endY - startY) / segments;
                currentX += (Math.random() - 0.5) * 40 * magnitude;

                this.ctx.lineTo(currentX, currentY);

                // Branch
                if (Math.random() > 0.7) {
                    const branchX = currentX + (Math.random() - 0.5) * 60;
                    const branchY = currentY + 40;
                    this.ctx.moveTo(currentX, currentY);
                    this.ctx.lineTo(branchX, branchY);
                    this.ctx.moveTo(currentX, currentY);
                }
            }

            this.ctx.stroke();
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 42: Plasma Storm
     */
    renderPlasmaStorm(magnitudes) {
        const time = this.frameCounter * 0.03;
        const numVortices = 3;

        this.ctx.shadowBlur = 30;

        for (let v = 0; v < numVortices; v++) {
            const vortexAngle = (v / numVortices) * Math.PI * 2 + time;
            const vortexDist = this.settings.innerRadius * 0.5;
            const vortexX = this.centerX + Math.cos(vortexAngle) * vortexDist;
            const vortexY = this.centerY + Math.sin(vortexAngle) * vortexDist;

            const numParticles = magnitudes.length / numVortices;

            for (let i = 0; i < numParticles; i++) {
                const magnitude = magnitudes[v * numParticles + i % magnitudes.length];
                const angle = (i / numParticles) * Math.PI * 2 + time * 2;
                const distance = magnitude * 100;

                const x = vortexX + Math.cos(angle) * distance;
                const y = vortexY + Math.sin(angle) * distance;
                const size = 2 + magnitude * 6;

                const color = this.getColor(v * numParticles + i, magnitudes.length);
                this.ctx.shadowColor = color;
                this.ctx.fillStyle = color;
                this.ctx.globalAlpha = 0.7;

                this.ctx.beginPath();
                this.ctx.arc(x, y, size, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 43: Laser Show
     */
    renderLaserShow(magnitudes) {
        const numLasers = Math.min(magnitudes.length / 2, 20);
        const time = this.frameCounter * 0.05;

        this.ctx.shadowBlur = 30;

        for (let i = 0; i < numLasers; i++) {
            const magnitude = magnitudes[i * 2 % magnitudes.length];
            if (magnitude < 0.3) continue;

            const angle = (i / numLasers) * Math.PI * 2 + time + magnitude;
            const length = this.maxRadius * 1.5;

            const x1 = this.centerX;
            const y1 = this.centerY;
            const x2 = this.centerX + Math.cos(angle) * length;
            const y2 = this.centerY + Math.sin(angle) * length;

            const color = this.getColor(i, numLasers);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = 3 + magnitude * 5;
            this.ctx.globalAlpha = 0.8;

            this.ctx.beginPath();
            this.ctx.moveTo(x1, y1);
            this.ctx.lineTo(x2, y2);
            this.ctx.stroke();

            // End glow
            this.ctx.fillStyle = color;
            this.ctx.beginPath();
            this.ctx.arc(x2, y2, 5 + magnitude * 10, 0, Math.PI * 2);
            this.ctx.fill();
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 44: Energy Pulses
     */
    renderEnergyPulses(magnitudes) {
        const numPulses = 6;
        const time = this.frameCounter * 0.1;

        this.ctx.shadowBlur = 25;

        for (let p = 0; p < numPulses; p++) {
            const phase = (time + p * 0.5) % 3;
            const radius = this.settings.innerRadius + phase * 100;
            const magnitude = magnitudes[p * (magnitudes.length / numPulses) % magnitudes.length];

            const color = this.getColor(p * 10, numPulses * 10);
            this.ctx.shadowColor = color;
            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = 3 + magnitude * 8;
            this.ctx.globalAlpha = Math.max(0, 1 - phase / 3);

            this.ctx.beginPath();
            this.ctx.arc(this.centerX, this.centerY, radius, 0, Math.PI * 2);
            this.ctx.stroke();
        }

        this.ctx.globalAlpha = 1;
        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 45: Rainbow Prism
     */
    renderRainbowPrism(magnitudes) {
        const numRays = magnitudes.length;
        const angleStep = (Math.PI * 2) / numRays;
        const innerRadius = this.settings.innerRadius * 0.5;

        this.ctx.shadowBlur = 20;

        for (let i = 0; i < numRays; i++) {
            const angle = i * angleStep;
            const magnitude = magnitudes[i];
            const length = magnitude * this.maxRadius * 0.8;

            const x1 = this.centerX + Math.cos(angle) * innerRadius;
            const y1 = this.centerY + Math.sin(angle) * innerRadius;
            const x2 = this.centerX + Math.cos(angle) * (innerRadius + length);
            const y2 = this.centerY + Math.sin(angle) * (innerRadius + length);

            // Create gradient for each ray
            const gradient = this.ctx.createLinearGradient(x1, y1, x2, y2);
            const color1 = this.getColor(i, numRays);
            const color2 = this.getColor((i + numRays / 6) % numRays, numRays);

            gradient.addColorStop(0, color1);
            gradient.addColorStop(1, color2);

            this.ctx.shadowColor = color1;
            this.ctx.strokeStyle = gradient;
            this.ctx.lineWidth = 4 + magnitude * 6;
            this.ctx.globalAlpha = 0.8;

            this.ctx.beginPath();
            this.ctx.moveTo(x1, y1);
            this.ctx.lineTo(x2, y2);
            this.ctx.stroke();
        }

        // Central prism
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        this.ctx.globalAlpha = 1;
        this.ctx.fillStyle = this.getColor(0, numRays);
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, innerRadius * 0.6 + avgMagnitude * 20, 0, Math.PI * 2);
        this.ctx.fill();

        this.ctx.globalAlpha = 1;
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

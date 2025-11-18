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

        // Mode-specific particle systems
        this.rainParticles = [];
        this.fireworkParticles = [];

        // Mode-specific state
        this.cassetteReelAngle = 0;
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
            case 'jazzy_fireworks':
                this.renderJazzyFireworks(magnitudes);
                break;
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
            case 'neon_rain':
                this.renderNeonRain(magnitudes);
                break;
            case 'neon_tubes':
                this.renderNeonTubes(magnitudes);
                break;
            case 'vinyl_grooves':
                this.renderVinylGrooves(magnitudes);
                break;
            case 'retro_cassette':
                this.renderRetroCassette(magnitudes);
                break;
            case 'retro_cassette_new':
                this.renderRetroCassetteNew(magnitudes);
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

            // Extended Modes (51-60)
            case 'fractal_tree':
                this.renderFractalTree(magnitudes);
                break;
            case 'cityscape_extrusion':
                this.renderCityscapeExtrusion(magnitudes);
                break;
            case 'gravity_well':
                this.renderGravityWell(magnitudes);
                break;
            case 'metaball_fluid':
                this.renderMetaballFluid(magnitudes);
                break;
            case 'aurora_borealis':
                this.renderAuroraBorealis(magnitudes);
                break;
            case 'stained_glass':
                this.renderStainedGlass(magnitudes);
                break;
            case 'glitch_artifact':
                this.renderGlitchArtifact(magnitudes);
                break;
            case 'warp_tunnel':
                this.renderWarpTunnel(magnitudes);
                break;
            case 'conway_life':
                this.renderConwayLife(magnitudes);
                break;

            // Extended Modes (61-70)
            case 'ascii_art':
                this.renderAsciiArt(magnitudes);
                break;
            case 'rippling_water':
                this.renderRipplingWater(magnitudes);
                break;
            case 'terrain_flyover':
                this.renderTerrainFlyover(magnitudes);
                break;
            case 'string_art':
                this.renderStringArt(magnitudes);
                break;
            case 'fire_embers':
                this.renderFireEmbers(magnitudes);
                break;
            case 'radial_kaleidoscope':
                this.renderRadialKaleidoscope(magnitudes);
                break;
            case 'pulsing_jellyfish':
                this.renderPulsingJellyfish(magnitudes);
                break;
            case 'orbital_system':
                this.renderOrbitalSystem(magnitudes);
                break;
            case 'spectrum_cube':
                this.renderSpectrumCube(magnitudes);
                break;
            case 'typographic_flow':
                this.renderTypographicFlow(magnitudes);
                break;
            case 'sonar_ping':
                this.renderSonarPing(magnitudes);
                break;
            case 'vu_meters':
                this.renderVUMeters(magnitudes);
                break;
            case 'lightning_cloud':
                this.renderLightningCloud(magnitudes);
                break;
            case 'bouncing_balls':
                this.renderBouncingBalls(magnitudes);
                break;
            case 'liquid_ink':
                this.renderLiquidInk(magnitudes);
                break;
            case 'stereo_landscape':
                this.renderStereoLandscape(magnitudes);
                break;
            case 'ai_latent_walk':
                this.renderAILatentWalk(magnitudes);
                break;
            case 'pixel_storm':
                this.renderPixelStorm(magnitudes);
                break;
            case 'growing_vine':
                this.renderGrowingVine(magnitudes);
                break;
            case 'haunted_faces':
                this.renderHauntedFaces(magnitudes);
                break;
            case 'connecting_constellations':
                this.renderConnectingConstellations(magnitudes);
                break;
            case 'matrix_rain':
                this.renderMatrixRain(magnitudes);
                break;
            case 'voxel_world':
                this.renderVoxelWorld(magnitudes);
                break;
            case 'dna_helix_rungs':
                this.renderDNAHelixRungs(magnitudes);
                break;
            case 'audio_reactive_shader':
                this.renderAudioReactiveShader(magnitudes);
                break;
            case 'spirograph':
                this.renderSpirograph(magnitudes);
                break;
            case 'equalizer_tower':
                this.renderEqualizerTower(magnitudes);
                break;
            case 'audio_driven_doodles':
                this.renderAudioDrivenDoodles(magnitudes);
                break;
            case 'firework_show':
                this.renderFireworkShow(magnitudes);
                break;
            case 'microscopic_view':
                this.renderMicroscopicView(magnitudes);
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
     * Jazzy Fireworks: Bursting particles from center with jazz energy
     */
    renderJazzyFireworks(magnitudes) {
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const particleCount = this.settings.jazzyFireworksParticleCount || 200;
        const speed = this.settings.jazzyFireworksSpeed || 10;
        const secondaryBursts = this.settings.jazzyFireworksSecondaryBursts || 3;

        // Spawn particles from center constantly when magnitude is high
        if (avgMagnitude > 0.3) {
            const numParticles = Math.floor(150 + avgMagnitude * (particleCount - 150));

            for (let i = 0; i < numParticles; i++) {
                const angle = Math.random() * Math.PI * 2;
                const particleSpeed = 5 + Math.random() * speed * (avgMagnitude + 0.5);

                // Rainbow colors for jazz energy
                const hue = Math.floor(Math.random() * 360);
                const color = this.hsvToRgb(hue, 100, 100);

                this.fireworkParticles.push({
                    x: this.centerX,
                    y: this.centerY,
                    vx: Math.cos(angle) * particleSpeed,
                    vy: Math.sin(angle) * particleSpeed,
                    color: color,
                    life: 1.0,
                    size: 4 + Math.floor(avgMagnitude * 8)
                });
            }
        }

        // Spawn secondary bursts from rotating positions
        if (avgMagnitude > 0.5 && this.frameCounter % 5 === 0) {
            for (let burst = 0; burst < secondaryBursts; burst++) {
                const burstAngle = (burst / secondaryBursts) * Math.PI * 2 + this.frameCounter * 0.1;
                const burstDistance = this.maxRadius * 0.4;
                const burstX = this.centerX + Math.cos(burstAngle) * burstDistance;
                const burstY = this.centerY + Math.sin(burstAngle) * burstDistance;

                for (let i = 0; i < 50; i++) {
                    const angle = Math.random() * Math.PI * 2;
                    const particleSpeed = 3 + Math.random() * 10;

                    const hue = Math.floor(Math.random() * 360);
                    const color = this.hsvToRgb(hue, 100, 100);

                    this.fireworkParticles.push({
                        x: burstX,
                        y: burstY,
                        vx: Math.cos(angle) * particleSpeed,
                        vy: Math.sin(angle) * particleSpeed,
                        color: color,
                        life: 0.8,
                        size: 3 + Math.floor(avgMagnitude * 6)
                    });
                }
            }
        }

        // Update and draw particles
        const newParticles = [];
        for (const particle of this.fireworkParticles) {
            particle.x += particle.vx;
            particle.y += particle.vy;
            particle.life -= 0.008;

            // Apply slight gravity
            particle.vy += 0.05;

            if (particle.life > 0) {
                const alpha = particle.life;
                const size = Math.max(1, Math.floor(particle.size * alpha));

                // Main particle
                this.ctx.fillStyle = `rgba(${particle.color[0]}, ${particle.color[1]}, ${particle.color[2]}, ${alpha})`;
                this.ctx.beginPath();
                this.ctx.arc(particle.x, particle.y, size, 0, Math.PI * 2);
                this.ctx.fill();

                // Multi-layer glow
                if (alpha > 0.3) {
                    // Outer glow
                    this.ctx.strokeStyle = `rgba(${particle.color[0]}, ${particle.color[1]}, ${particle.color[2]}, ${0.3 * alpha})`;
                    this.ctx.lineWidth = 1;
                    this.ctx.beginPath();
                    this.ctx.arc(particle.x, particle.y, size + 4, 0, Math.PI * 2);
                    this.ctx.stroke();

                    // Inner bright glow
                    this.ctx.fillStyle = `rgba(${particle.color[0]}, ${particle.color[1]}, ${particle.color[2]}, ${0.6 * alpha})`;
                    this.ctx.beginPath();
                    this.ctx.arc(particle.x, particle.y, size + 2, 0, Math.PI * 2);
                    this.ctx.fill();
                }

                newParticles.push(particle);
            }
        }

        this.fireworkParticles = newParticles;
        this.frameCounter++;
    }

    /**
     * Neon Rain: Cyberpunk neon droplets cascading down
     */
    renderNeonRain(magnitudes) {
        const numBars = magnitudes.length;
        const spawnRate = this.settings.neonRainSpawnRate || 0.3;
        const particleSize = this.settings.neonRainParticleSize || 5;
        const speed = this.settings.neonRainSpeed || 10;

        // Spawn new rain particles based on magnitudes
        for (let i = 0; i < numBars; i++) {
            const magnitude = magnitudes[i];
            if (magnitude > 0.3 && Math.random() < magnitude * spawnRate) {
                const x = (i / numBars) * this.canvas.width;
                const y = 0;
                const particleSpeed = 3 + magnitude * speed;
                const size = 2 + Math.floor(magnitude * particleSize);

                // Neon colors (cyan, magenta, pink)
                const colorChoice = i % 3;
                let color;
                if (colorChoice === 0) {
                    color = [0, 255, 255]; // Cyan
                } else if (colorChoice === 1) {
                    color = [255, 0, 255]; // Magenta
                } else {
                    color = [200, 100, 255]; // Pink
                }

                this.rainParticles.push({
                    x: x,
                    y: y,
                    speed: particleSpeed,
                    size: size,
                    color: color,
                    trailLength: Math.floor(magnitude * 50)
                });
            }
        }

        // Update and draw rain particles
        const newParticles = [];
        for (const particle of this.rainParticles) {
            particle.y += particle.speed;

            // Keep if still on screen
            if (particle.y < this.canvas.height + 20) {
                // Draw particle with trail
                const trailLength = particle.trailLength;
                for (let t = 0; t < trailLength; t++) {
                    const trailY = particle.y - t * 2;
                    if (trailY >= 0) {
                        const alpha = 1.0 - (t / trailLength);
                        const trailColor = `rgba(${particle.color[0]}, ${particle.color[1]}, ${particle.color[2]}, ${alpha})`;
                        const trailSize = Math.max(1, particle.size - Math.floor(t / 3));

                        this.ctx.fillStyle = trailColor;
                        this.ctx.beginPath();
                        this.ctx.arc(particle.x, trailY, trailSize, 0, Math.PI * 2);
                        this.ctx.fill();
                    }
                }

                // Glow effect
                this.ctx.fillStyle = `rgba(${particle.color[0]}, ${particle.color[1]}, ${particle.color[2]}, 0.3)`;
                this.ctx.beginPath();
                this.ctx.arc(particle.x, particle.y, particle.size + 3, 0, Math.PI * 2);
                this.ctx.fill();

                newParticles.push(particle);
            }
        }

        this.rainParticles = newParticles;
    }

    renderRetroCassetteNew(magnitudes) {
        // Get settings
        const reelSpeed = this.settings.retroCassetteReelSpeed || 5;
        const vuSensitivity = this.settings.retroCassetteVuSensitivity || 1;

        // Update cassette reel rotation
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        this.cassetteReelAngle += (3 + avgMagnitude * 10) * (reelSpeed / 5);

        // REALISTIC CASSETTE DIMENSIONS (wider, more authentic)
        const cassetteWidth = Math.floor(this.canvas.width * 0.65);
        const cassetteHeight = Math.floor(this.canvas.height * 0.35);
        const cassetteX = this.centerX - Math.floor(cassetteWidth / 2);
        const cassetteY = this.centerY - Math.floor(cassetteHeight / 2);

        // === CASSETTE BODY ===
        // Main outer shell (beige/tan plastic)
        this.ctx.fillStyle = 'rgb(140, 130, 110)';
        this.ctx.fillRect(cassetteX, cassetteY, cassetteWidth, cassetteHeight);

        // Border/edge
        this.ctx.strokeStyle = 'rgb(100, 90, 70)';
        this.ctx.lineWidth = 3;
        this.ctx.strokeRect(cassetteX, cassetteY, cassetteWidth, cassetteHeight);

        // === LABEL AREA (top section) ===
        const labelHeight = Math.floor(cassetteHeight * 0.25);
        this.ctx.fillStyle = 'rgb(220, 210, 200)';
        this.ctx.fillRect(cassetteX + 20, cassetteY + 15, cassetteWidth - 40, labelHeight - 15);
        this.ctx.strokeStyle = 'rgb(180, 170, 160)';
        this.ctx.lineWidth = 1;
        this.ctx.strokeRect(cassetteX + 20, cassetteY + 15, cassetteWidth - 40, labelHeight - 15);

        // === WINDOW AREA (where you see the tape) ===
        const windowY = cassetteY + labelHeight + 25;
        const windowHeight = Math.floor(cassetteHeight * 0.45);
        const windowMargin = 40;

        // Dark transparent window
        this.ctx.fillStyle = 'rgb(30, 25, 20)';
        this.ctx.fillRect(cassetteX + windowMargin, windowY, cassetteWidth - 2 * windowMargin, windowHeight);
        this.ctx.strokeStyle = 'rgb(80, 70, 60)';
        this.ctx.lineWidth = 2;
        this.ctx.strokeRect(cassetteX + windowMargin, windowY, cassetteWidth - 2 * windowMargin, windowHeight);

        // === TAPE REELS (much more detailed) ===
        const reelY = windowY + Math.floor(windowHeight / 2);
        const reelOuterRadius = 55;
        const reelInnerRadius = 15;
        const leftReelX = cassetteX + Math.floor(cassetteWidth / 3);
        const rightReelX = cassetteX + Math.floor(2 * cassetteWidth / 3);

        for (const reelX of [leftReelX, rightReelX]) {
            // Outer reel edge (dark)
            this.ctx.strokeStyle = 'rgb(50, 45, 40)';
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            this.ctx.arc(reelX, reelY, reelOuterRadius, 0, Math.PI * 2);
            this.ctx.stroke();

            // Tape on reel (brown/black magnetic tape)
            const tapeRadius = Math.floor(reelOuterRadius * 0.85);
            this.ctx.fillStyle = 'rgb(20, 15, 10)';
            this.ctx.beginPath();
            this.ctx.arc(reelX, reelY, tapeRadius, 0, Math.PI * 2);
            this.ctx.fill();

            // Center hub (beige plastic)
            this.ctx.fillStyle = 'rgb(140, 130, 110)';
            this.ctx.beginPath();
            this.ctx.arc(reelX, reelY, reelInnerRadius, 0, Math.PI * 2);
            this.ctx.fill();
            this.ctx.strokeStyle = 'rgb(100, 90, 70)';
            this.ctx.lineWidth = 1;
            this.ctx.stroke();

            // Rotating spokes (6 spokes for realism)
            this.ctx.strokeStyle = 'rgb(80, 70, 60)';
            this.ctx.lineWidth = 2;
            for (let spoke = 0; spoke < 6; spoke++) {
                const angle = (this.cassetteReelAngle + spoke * 60) * Math.PI / 180;
                const x1 = reelX + reelInnerRadius * Math.cos(angle);
                const y1 = reelY + reelInnerRadius * Math.sin(angle);
                const x2 = reelX + tapeRadius * 0.9 * Math.cos(angle);
                const y2 = reelY + tapeRadius * 0.9 * Math.sin(angle);
                this.ctx.beginPath();
                this.ctx.moveTo(x1, y1);
                this.ctx.lineTo(x2, y2);
                this.ctx.stroke();
            }

            // Center dot
            this.ctx.fillStyle = 'rgb(60, 50, 40)';
            this.ctx.beginPath();
            this.ctx.arc(reelX, reelY, 4, 0, Math.PI * 2);
            this.ctx.fill();
        }

        // === TAPE BETWEEN REELS (visible magnetic tape) ===
        const tapeTopY = reelY - reelOuterRadius + 5;
        const tapeBottomY = reelY + reelOuterRadius - 5;
        const tapeThickness = 8;

        this.ctx.fillStyle = 'rgb(15, 10, 8)';
        // Top tape section
        this.ctx.fillRect(
            leftReelX + reelOuterRadius - 5,
            tapeTopY - tapeThickness,
            rightReelX - leftReelX - 2 * (reelOuterRadius - 5),
            tapeThickness
        );
        // Bottom tape section
        this.ctx.fillRect(
            leftReelX + reelOuterRadius - 5,
            tapeBottomY,
            rightReelX - leftReelX - 2 * (reelOuterRadius - 5),
            tapeThickness
        );

        // === CASSETTE SCREWS (4 corners) ===
        const screwPositions = [
            [cassetteX + 25, cassetteY + 25],
            [cassetteX + cassetteWidth - 25, cassetteY + 25],
            [cassetteX + 25, cassetteY + cassetteHeight - 25],
            [cassetteX + cassetteWidth - 25, cassetteY + cassetteHeight - 25]
        ];

        for (const [screwX, screwY] of screwPositions) {
            this.ctx.fillStyle = 'rgb(80, 70, 60)';
            this.ctx.beginPath();
            this.ctx.arc(screwX, screwY, 6, 0, Math.PI * 2);
            this.ctx.fill();
            this.ctx.strokeStyle = 'rgb(60, 50, 40)';
            this.ctx.lineWidth = 1;
            this.ctx.stroke();

            // Screw cross
            this.ctx.strokeStyle = 'rgb(40, 30, 25)';
            this.ctx.lineWidth = 1;
            this.ctx.beginPath();
            this.ctx.moveTo(screwX - 3, screwY);
            this.ctx.lineTo(screwX + 3, screwY);
            this.ctx.stroke();
            this.ctx.beginPath();
            this.ctx.moveTo(screwX, screwY - 3);
            this.ctx.lineTo(screwX, screwY + 3);
            this.ctx.stroke();
        }

        // === BOTTOM GRIP NOTCHES (authentic detail) ===
        const notchWidth = 30;
        const notchHeight = 8;
        const notchSpacing = 15;
        const notchY = cassetteY + cassetteHeight - notchHeight - 5;

        this.ctx.fillStyle = 'rgb(90, 80, 60)';
        for (let i = 0; i < 5; i++) {
            const notchX = cassetteX + Math.floor(cassetteWidth / 2) - 2 * notchWidth - 2 * notchSpacing + i * (notchWidth + notchSpacing);
            this.ctx.fillRect(notchX, notchY, notchWidth, notchHeight);
        }

        // === VINTAGE VU METERS (below cassette) ===
        const vuY = cassetteY + cassetteHeight + 100;
        const vuWidth = cassetteWidth - 200;
        const vuHeight = 35;
        const vuX = this.centerX - Math.floor(vuWidth / 2);

        // Left and right channel VU meters
        const numSegments = 40;
        const segmentWidth = Math.floor(vuWidth / numSegments);

        for (let channel = 0; channel < 2; channel++) {
            const channelY = vuY + channel * 60;

            // VU meter background/frame
            const framePadding = 5;
            this.ctx.fillStyle = 'rgb(100, 90, 70)';
            this.ctx.fillRect(
                vuX - framePadding,
                channelY - framePadding,
                vuWidth + 2 * framePadding,
                vuHeight + 2 * framePadding
            );
            this.ctx.strokeStyle = 'rgb(70, 60, 50)';
            this.ctx.lineWidth = 2;
            this.ctx.strokeRect(
                vuX - framePadding,
                channelY - framePadding,
                vuWidth + 2 * framePadding,
                vuHeight + 2 * framePadding
            );

            // Get magnitude for this channel (split frequencies)
            let channelMag;
            if (channel === 0) {
                const leftHalf = magnitudes.slice(0, Math.floor(magnitudes.length / 2));
                channelMag = leftHalf.reduce((a, b) => a + b, 0) / leftHalf.length;
            } else {
                const rightHalf = magnitudes.slice(Math.floor(magnitudes.length / 2));
                channelMag = rightHalf.reduce((a, b) => a + b, 0) / rightHalf.length;
            }

            channelMag *= vuSensitivity;
            const activeSegments = Math.floor(channelMag * numSegments);

            for (let seg = 0; seg < numSegments; seg++) {
                const segX = vuX + seg * segmentWidth;

                // VINTAGE COLOR GRADIENT: green -> amber -> orange -> red
                const segmentProgress = seg / numSegments;
                let color;
                if (segmentProgress < 0.5) {
                    color = 'rgb(50, 200, 0)'; // Green
                } else if (segmentProgress < 0.7) {
                    color = 'rgb(200, 180, 0)'; // Amber/yellow
                } else if (segmentProgress < 0.85) {
                    color = 'rgb(255, 120, 0)'; // Orange
                } else {
                    color = 'rgb(255, 60, 0)'; // Red
                }

                if (seg < activeSegments) {
                    // Active segment - full brightness with glow
                    this.ctx.fillStyle = color;
                    this.ctx.fillRect(segX + 1, channelY, segmentWidth - 2, vuHeight);
                } else {
                    // Inactive segment - very dim
                    if (segmentProgress < 0.5) {
                        this.ctx.fillStyle = 'rgb(7, 30, 0)';
                    } else if (segmentProgress < 0.7) {
                        this.ctx.fillStyle = 'rgb(30, 27, 0)';
                    } else if (segmentProgress < 0.85) {
                        this.ctx.fillStyle = 'rgb(38, 18, 0)';
                    } else {
                        this.ctx.fillStyle = 'rgb(38, 9, 0)';
                    }
                    this.ctx.fillRect(segX + 2, channelY + 2, segmentWidth - 2, vuHeight - 4);
                }
            }

            // Channel label (L/R)
            const label = channel === 0 ? 'L' : 'R';
            this.ctx.fillStyle = 'rgb(150, 140, 120)';
            this.ctx.font = 'bold 20px Arial';
            this.ctx.fillText(label, vuX - 35, channelY + vuHeight - 10);
        }
    }

    renderSoulAura(magnitudes) {
        // Get settings
        const numPoints = this.settings.soulAuraNumPoints || 60;
        const baseRadius = this.settings.soulAuraBaseRadius || 0.5;
        const glowLayers = this.settings.soulAuraGlowLayers || 5;

        const angleStep = 360 / numPoints;
        const points = [];

        // Create smooth organic shape with many points
        for (let i = 0; i < numPoints; i++) {
            const angle = (i * angleStep) * Math.PI / 180;

            // Get magnitude for this angle section
            const magIdx = Math.floor((i / numPoints) * magnitudes.length);
            const magnitude = magnitudes[Math.min(magIdx, magnitudes.length - 1)];

            // Base radius with organic variation
            const baseVariation = Math.sin(i * 0.3 + this.frameCounter * 0.05) * 30;
            const magnitudeVariation = magnitude * 150;
            const radius = this.maxRadius * baseRadius + baseVariation + magnitudeVariation;

            const x = this.centerX + radius * Math.cos(angle);
            const y = this.centerY + radius * Math.sin(angle);
            points.push({ x, y });
        }

        // Calculate average magnitude for colors
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;

        // Draw multiple layers for depth and glow (outer glow layers - purple to pink gradient)
        for (let layer = glowLayers; layer > 0; layer--) {
            const expansion = layer * 15;
            const layerPoints = [];

            for (const point of points) {
                // Expand from center
                const dx = point.x - this.centerX;
                const dy = point.y - this.centerY;
                const dist = Math.sqrt(dx * dx + dy * dy);
                const scale = 1.0 + (expansion / (dist + 1));

                const x = this.centerX + dx * scale;
                const y = this.centerY + dy * scale;
                layerPoints.push({ x, y });
            }

            // Color: deep purple to pink
            const hue = 140 + layer * 5 + Math.floor(avgMagnitude * 20); // Purple-pink range
            const saturation = 200 + Math.floor(avgMagnitude * 55);
            const value = 100 + Math.floor(avgMagnitude * 100) - layer * 15;
            const rgb = this.hsvToRgb(hue, saturation / 255 * 100, value / 255 * 100);

            const alpha = 0.3 / layer;
            this.ctx.fillStyle = `rgba(${Math.floor(rgb[0] * alpha)}, ${Math.floor(rgb[1] * alpha)}, ${Math.floor(rgb[2] * alpha)}, ${alpha})`;

            // Draw filled polygon
            this.ctx.beginPath();
            this.ctx.moveTo(layerPoints[0].x, layerPoints[0].y);
            for (let i = 1; i < layerPoints.length; i++) {
                this.ctx.lineTo(layerPoints[i].x, layerPoints[i].y);
            }
            this.ctx.closePath();
            this.ctx.fill();
        }

        // Main aura body
        const mainHue = 150 + Math.floor(avgMagnitude * 30);
        const mainSaturation = 220 + Math.floor(avgMagnitude * 35);
        const mainValue = 180 + Math.floor(avgMagnitude * 75);
        const mainRgb = this.hsvToRgb(mainHue, mainSaturation / 255 * 100, mainValue / 255 * 100);

        this.ctx.fillStyle = `rgb(${mainRgb[0]}, ${mainRgb[1]}, ${mainRgb[2]})`;
        this.ctx.beginPath();
        this.ctx.moveTo(points[0].x, points[0].y);
        for (let i = 1; i < points.length; i++) {
            this.ctx.lineTo(points[i].x, points[i].y);
        }
        this.ctx.closePath();
        this.ctx.fill();

        // Bright outline
        this.ctx.strokeStyle = 'rgb(255, 200, 255)';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        this.ctx.moveTo(points[0].x, points[0].y);
        for (let i = 1; i < points.length; i++) {
            this.ctx.lineTo(points[i].x, points[i].y);
        }
        this.ctx.closePath();
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
        const innerRadius = Math.max(20, this.settings.innerRadius - 50);

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
     * Mode 46: Neon Rain (already implemented - keeping reference)
     */
    // renderNeonRain is already implemented above

    /**
     * Mode 47: Jazzy Fireworks (already implemented - keeping reference)
     */
    // renderJazzyFireworks is already implemented above

    /**
     * Mode 48: Retro Cassette New (already implemented - keeping reference)
     */
    // renderRetroCassetteNew is already implemented above

    /**
     * Mode 49: Soul Aura (already implemented - keeping reference)
     */
    // renderSoulAura is already implemented above

    /**
     * Mode 50: Frequency Flowers (migrated)
     */
    renderFrequencyFlowers(magnitudes) {
        const numPetals = Math.min(24, magnitudes.length);
        const angleStep = (Math.PI * 2) / numPetals;
        const time = this.frameCounter * 0.5;

        this.ctx.shadowBlur = 15;

        for (let i = 0; i < numPetals; i++) {
            const angle = i * angleStep + time * 0.01;
            const magnitude = magnitudes[Math.floor((i / numPetals) * magnitudes.length)];

            const petalLength = 50 + magnitude * 150;
            const petalWidth = 20 + magnitude * 40;
            const baseRadius = this.maxRadius * 0.4;

            const baseX = this.centerX + Math.cos(angle) * baseRadius;
            const baseY = this.centerY + Math.sin(angle) * baseRadius;

            const tipX = baseX + Math.cos(angle) * petalLength;
            const tipY = baseY + Math.sin(angle) * petalLength;

            const centerX = (baseX + tipX) / 2;
            const centerY = (baseY + tipY) / 2;

            // Pastel colors
            const hue = (i * 15 + this.frameCounter) % 360;
            const rgb = this.hsvToRgb(hue, 60 + magnitude * 40, 85 + magnitude * 15);
            const color = `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;

            this.ctx.fillStyle = color;
            this.ctx.shadowColor = color;

            this.ctx.save();
            this.ctx.translate(centerX, centerY);
            this.ctx.rotate(angle);
            this.ctx.beginPath();
            this.ctx.ellipse(0, 0, petalWidth / 2, petalLength / 2, 0, 0, Math.PI * 2);
            this.ctx.fill();
            this.ctx.restore();
        }

        // Flower center
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const centerRadius = 30 + avgMagnitude * 50;
        this.ctx.shadowBlur = 20;
        this.ctx.fillStyle = '#FFD93D';
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, centerRadius, 0, Math.PI * 2);
        this.ctx.fill();

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 51: Fractal Tree
     */
    renderFractalTree(magnitudes) {
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);

        // Trunk sway
        const trunkSway = Math.sin(this.frameCounter * 0.1 + avgMagnitude) * 20;
        const trunkBase = { x: this.centerX + trunkSway, y: this.canvas.height - 50 };
        const trunkTop = { x: this.centerX + trunkSway, y: this.centerY };

        // Draw trunk
        const trunkThickness = 10 + avgMagnitude * 15;
        this.ctx.strokeStyle = '#2D5016';
        this.ctx.lineWidth = trunkThickness;
        this.ctx.lineCap = 'round';
        this.ctx.beginPath();
        this.ctx.moveTo(trunkBase.x, trunkBase.y);
        this.ctx.lineTo(trunkTop.x, trunkTop.y);
        this.ctx.stroke();

        // Spawn branches on bass hits
        if (!this.fractalTreeBranches) this.fractalTreeBranches = [];
        if (bass > 0.3 && this.frameCounter % 8 === 0) {
            const angle = -Math.PI / 2 + (Math.random() - 0.5) * Math.PI / 3;
            this.fractalTreeBranches.push({
                x: trunkTop.x,
                y: trunkTop.y,
                angle: angle,
                length: 40 + bass * 60,
                thickness: 3 + bass * 8,
                generation: 0,
                life: 1.0
            });
        }

        // Update and draw branches
        this.fractalTreeBranches = this.fractalTreeBranches.filter(branch => {
            if (branch.life <= 0) return false;

            const endX = branch.x + Math.cos(branch.angle) * branch.length;
            const endY = branch.y + Math.sin(branch.angle) * branch.length;

            this.ctx.globalAlpha = branch.life;
            this.ctx.strokeStyle = `rgba(50, 100, 50, ${branch.life})`;
            this.ctx.lineWidth = branch.thickness;
            this.ctx.beginPath();
            this.ctx.moveTo(branch.x, branch.y);
            this.ctx.lineTo(endX, endY);
            this.ctx.stroke();

            // Bloom flowers on treble
            if (treble > 0.4 && branch.generation > 0) {
                const bloomSize = 3 + treble * 10;
                const hue = treble * 180;
                const rgb = this.hsvToRgb(hue, 100, 100);
                this.ctx.fillStyle = `rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, ${branch.life})`;
                this.ctx.beginPath();
                this.ctx.arc(endX, endY, bloomSize, 0, Math.PI * 2);
                this.ctx.fill();
            }

            branch.life -= 0.003;
            return true;
        }).slice(0, 100);

        this.ctx.globalAlpha = 1;
    }

    /**
     * Mode 52: Cityscape Extrusion
     */
    renderCityscapeExtrusion(magnitudes) {
        const numBlocks = Math.min(magnitudes.length, 40);
        const blockWidth = this.canvas.width / numBlocks;

        for (let i = 0; i < numBlocks; i++) {
            const magnitude = magnitudes[i] || 0;
            const buildingHeight = magnitude * this.canvas.height * 0.7;

            const baseY = this.canvas.height - 100;
            const topY = baseY - buildingHeight;
            const xLeft = i * blockWidth + 5;
            const xRight = (i + 1) * blockWidth - 5;

            // Building color
            const hue = (i / numBlocks) * 180;
            const rgb = this.hsvToRgb(hue, 70 + magnitude * 30, 40 + magnitude * 60);
            this.ctx.fillStyle = `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;
            this.ctx.fillRect(xLeft, topY, xRight - xLeft, baseY - topY);

            // Windows
            if (magnitude > 0.3) {
                const numWindows = Math.max(2, Math.floor(buildingHeight / 30));
                for (let w = 0; w < numWindows; w++) {
                    const windowY = baseY - ((w + 0.5) * buildingHeight / numWindows);
                    const windowX = (xLeft + xRight) / 2;
                    const brightness = 255 * magnitude;
                    this.ctx.fillStyle = `rgb(${brightness}, ${brightness}, 200)`;
                    this.ctx.beginPath();
                    this.ctx.arc(windowX, windowY, 3, 0, Math.PI * 2);
                    this.ctx.fill();
                }
            }
        }
    }

    /**
     * Mode 53: Gravity Well
     */
    renderGravityWell(magnitudes) {
        if (!this.gravityWellParticles) this.gravityWellParticles = [];

        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);

        // Spawn particles
        if (this.frameCounter % 2 === 0) {
            for (let i = 0; i < treble * 20 + 5; i++) {
                const angle = Math.random() * Math.PI * 2;
                const edgeDist = Math.min(this.canvas.width, this.canvas.height) / 2;
                this.gravityWellParticles.push({
                    x: this.centerX + Math.cos(angle) * edgeDist,
                    y: this.centerY + Math.sin(angle) * edgeDist,
                    vx: 0,
                    vy: 0,
                    hue: treble * 180
                });
            }
        }

        // Black hole
        const wellRadius = 30 + bass * 50;
        this.ctx.fillStyle = '#FFFFFF';
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, wellRadius, 0, Math.PI * 2);
        this.ctx.fill();

        // Update particles
        const shockwaveForce = bass > 0.6 ? bass * 500 : 0;

        this.gravityWellParticles = this.gravityWellParticles.filter(p => {
            const dx = this.centerX - p.x;
            const dy = this.centerY - p.y;
            const dist = Math.sqrt(dx * dx + dy * dy) + 1;

            // Gravity
            const pullForce = 200 / (dist * dist);
            p.vx += (dx / dist) * pullForce;
            p.vy += (dy / dist) * pullForce;

            // Shockwave
            if (shockwaveForce > 0 && dist < 200) {
                p.vx -= (dx / dist) * shockwaveForce;
                p.vy -= (dy / dist) * shockwaveForce;
            }

            p.x += p.vx;
            p.y += p.vy;

            if (dist > wellRadius && p.x >= 0 && p.x < this.canvas.width &&
                p.y >= 0 && p.y < this.canvas.height) {
                const rgb = this.hsvToRgb(p.hue, 100, 100);
                this.ctx.fillStyle = `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;
                this.ctx.beginPath();
                this.ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
                this.ctx.fill();
                return true;
            }
            return false;
        }).slice(0, 500);
    }

    /**
     * Mode 54: Metaball Fluid
     */
    renderMetaballFluid(magnitudes) {
        if (!this.metaballs) this.metaballs = [];

        const numBalls = Math.min(magnitudes.length, 15);
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;

        // Initialize metaballs
        while (this.metaballs.length < numBalls) {
            this.metaballs.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                vx: (Math.random() - 0.5) * 4,
                vy: (Math.random() - 0.5) * 4,
                baseRadius: 40 + Math.random() * 40
            });
        }

        // Draw metaballs
        for (let i = 0; i < Math.min(numBalls, this.metaballs.length); i++) {
            const ball = this.metaballs[i];
            const magnitude = magnitudes[i] || avgMagnitude;
            const radius = ball.baseRadius * (0.7 + magnitude * 0.8);

            // Update position
            ball.x += ball.vx;
            ball.y += ball.vy;

            // Bounce
            if (ball.x < radius || ball.x > this.canvas.width - radius) ball.vx *= -1;
            if (ball.y < radius || ball.y > this.canvas.height - radius) ball.vy *= -1;

            // Color
            const hue = (i / numBalls) * 180;
            const rgb = this.hsvToRgb(hue, 80 + magnitude * 20, 60 + magnitude * 40);

            // Draw with gradient
            for (let r = radius; r > 0; r -= 5) {
                const alpha = r / radius;
                this.ctx.fillStyle = `rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, ${alpha * 0.6})`;
                this.ctx.beginPath();
                this.ctx.arc(ball.x, ball.y, r, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }
    }

    /**
     * Mode 55: Aurora Borealis
     */
    renderAuroraBorealis(magnitudes) {
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);

        const numCurtains = 5;
        const curtainPoints = 60;

        for (let curtainIdx = 0; curtainIdx < numCurtains; curtainIdx++) {
            const points = [];
            const baseYOffset = curtainIdx * 80 - 160;

            for (let i = 0; i < curtainPoints; i++) {
                const x = (i / curtainPoints) * this.canvas.width;
                const wave1 = Math.sin(i * 0.15 + this.frameCounter * 0.05 + curtainIdx) * bass * 60;
                const wave2 = Math.sin(i * 0.08 + this.frameCounter * 0.03) * bass * 40;
                const shimmer = Math.sin(i * 0.8 + this.frameCounter * 0.4) * treble * 20;
                const y = this.centerY + baseYOffset + wave1 + wave2 + shimmer;

                points.push({ x, y });
            }

            const hue = 60 + curtainIdx * 15;
            const rgb = this.hsvToRgb(hue, 70 + treble * 30, 50 + bass * 50);
            this.ctx.strokeStyle = `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;
            this.ctx.lineWidth = 3;
            this.ctx.shadowBlur = 15;
            this.ctx.shadowColor = this.ctx.strokeStyle;

            this.ctx.beginPath();
            this.ctx.moveTo(points[0].x, points[0].y);
            for (let i = 1; i < points.length; i++) {
                this.ctx.lineTo(points[i].x, points[i].y);
            }
            this.ctx.stroke();
        }

        this.ctx.shadowBlur = 0;
    }

    /**
     * Mode 56: Stained Glass
     */
    renderStainedGlass(magnitudes) {
        const rows = 6, cols = 10;
        const paneWidth = this.canvas.width / cols;
        const paneHeight = this.canvas.height / rows;

        let paneIdx = 0;
        for (let row = 0; row < rows; row++) {
            for (let col = 0; col < cols; col++) {
                if (paneIdx >= magnitudes.length) break;

                const magnitude = magnitudes[paneIdx];
                const x1 = col * paneWidth + 2;
                const y1 = row * paneHeight + 2;
                const x2 = (col + 1) * paneWidth - 2;
                const y2 = (row + 1) * paneHeight - 2;

                const hue = (paneIdx / magnitudes.length) * 180;
                const rgb = this.hsvToRgb(hue, 100, 30 + magnitude * 70);
                this.ctx.fillStyle = `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;
                this.ctx.fillRect(x1, y1, x2 - x1, y2 - y1);

                if (magnitude > 0.5) {
                    this.ctx.shadowBlur = magnitude * 20;
                    this.ctx.shadowColor = `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;
                    this.ctx.fillRect(x1, y1, x2 - x1, y2 - y1);
                    this.ctx.shadowBlur = 0;
                }

                paneIdx++;
            }
        }
    }

    /**
     * Mode 57: Neural Network
     */
    renderNeuralNetwork(magnitudes) {
        if (!this.nerveNodes || this.nerveNodes.length === 0) {
            this.nerveNodes = [];
            const numNodes = 20;
            for (let i = 0; i < numNodes; i++) {
                this.nerveNodes.push({
                    x: 100 + Math.random() * (this.canvas.width - 200),
                    y: 100 + Math.random() * (this.canvas.height - 200),
                    pulse: 0,
                    connections: []
                });
            }
            // Create connections
            this.nerveNodes.forEach((node, i) => {
                const numConnections = 2 + Math.floor(Math.random() * 3);
                for (let j = 0; j < numConnections; j++) {
                    const target = Math.floor(Math.random() * numNodes);
                    if (target !== i) node.connections.push(target);
                }
            });
        }

        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);

        // Update pulses
        this.nerveNodes.forEach((node, i) => {
            if (i < magnitudes.length) node.pulse = magnitudes[i];
        });

        // Draw connections
        this.ctx.strokeStyle = `rgba(100, 200, 255, ${treble * 0.8})`;
        this.ctx.lineWidth = 2;
        this.nerveNodes.forEach(node => {
            node.connections.forEach(targetIdx => {
                const target = this.nerveNodes[targetIdx];
                if (treble > 0.5) {
                    this.ctx.beginPath();
                    this.ctx.moveTo(node.x, node.y);
                    this.ctx.lineTo(target.x, target.y);
                    this.ctx.stroke();
                }
            });
        });

        // Draw nodes
        this.nerveNodes.forEach(node => {
            const radius = 10 + node.pulse * 25;
            this.ctx.fillStyle = `rgba(100, 255, 255, ${0.6 + node.pulse * 0.4})`;
            this.ctx.beginPath();
            this.ctx.arc(node.x, node.y, radius, 0, Math.PI * 2);
            this.ctx.fill();
        });
    }

    /**
     * Mode 58: Glitch Artifact
     */
    renderGlitchArtifact(magnitudes) {
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);

        // Draw clean bars
        const barWidth = this.canvas.width / magnitudes.length;
        magnitudes.forEach((magnitude, i) => {
            const barHeight = magnitude * this.canvas.height * 0.7;
            const x = i * barWidth;
            const y = this.canvas.height - barHeight;

            this.ctx.fillStyle = '#64C8FF';
            this.ctx.fillRect(x, y, barWidth - 2, barHeight);
        });

        // Apply glitch on strong transients
        if (treble > 0.7) {
            const imageData = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);
            const shift = Math.floor(treble * 20);

            // Simple chromatic aberration simulation
            for (let y = 0; y < this.canvas.height; y += 10) {
                const rowData = this.ctx.getImageData(0, y, this.canvas.width, 1);
                this.ctx.putImageData(rowData, shift, y);
            }
        }
    }

    /**
     * Mode 59: Warp Tunnel
     */
    renderWarpTunnel(magnitudes) {
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const numRings = 30;

        for (let i = 0; i < numRings; i++) {
            const depth = i / numRings;
            const scale = 1 - depth * 0.9;
            const freqIdx = Math.floor(depth * magnitudes.length);
            const magnitude = magnitudes[Math.min(freqIdx, magnitudes.length - 1)];
            const radius = this.maxRadius * scale * (0.5 + magnitude * 0.8);

            const hue = ((depth + this.frameCounter * 0.01) * 180) % 180;
            const rgb = this.hsvToRgb(hue, 80 + magnitude * 20, Math.floor(60 * (1 - depth) + magnitude * 40));
            this.ctx.strokeStyle = `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;
            this.ctx.lineWidth = 2 + magnitude * 8;

            this.ctx.beginPath();
            this.ctx.arc(this.centerX, this.centerY, radius, 0, Math.PI * 2);
            this.ctx.stroke();
        }
    }

    /**
     * Mode 60: Conway's Game of Life
     */
    renderConwayLife(magnitudes) {
        const gridSize = 40;
        const cellWidth = this.canvas.width / gridSize;
        const cellHeight = this.canvas.height / gridSize;

        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);

        if (!this.cellularAutomaton || this.cellularAutomaton.length === 0) {
            this.cellularAutomaton = [];
            for (let y = 0; y < gridSize; y++) {
                this.cellularAutomaton[y] = [];
                for (let x = 0; x < gridSize; x++) {
                    this.cellularAutomaton[y][x] = Math.random() > 0.5 ? 1 : 0;
                }
            }
        }

        if (this.frameCounter % 3 === 0) {
            const newGrid = this.cellularAutomaton.map(row => [...row]);

            for (let y = 0; y < gridSize; y++) {
                for (let x = 0; x < gridSize; x++) {
                    let neighbors = 0;
                    for (let dy = -1; dy <= 1; dy++) {
                        for (let dx = -1; dx <= 1; dx++) {
                            if (dy === 0 && dx === 0) continue;
                            const ny = (y + dy + gridSize) % gridSize;
                            const nx = (x + dx + gridSize) % gridSize;
                            neighbors += this.cellularAutomaton[ny][nx];
                        }
                    }

                    if (this.cellularAutomaton[y][x] === 1) {
                        if (neighbors < 2 || neighbors > 3) newGrid[y][x] = 0;
                    } else {
                        if (neighbors === 3 || (bass > 0.6 && Math.random() < bass * 0.1)) {
                            newGrid[y][x] = 1;
                        }
                    }
                }
            }

            this.cellularAutomaton = newGrid;
        }

        // Draw grid
        this.ctx.fillStyle = '#64FF64';
        for (let y = 0; y < gridSize; y++) {
            for (let x = 0; x < gridSize; x++) {
                if (this.cellularAutomaton[y][x] === 1) {
                    this.ctx.fillRect(x * cellWidth, y * cellHeight, cellWidth - 1, cellHeight - 1);
                }
            }
        }
    }

    /**
     * Mode 61: ASCII Art Bars
     */
    renderAsciiArt(magnitudes) {
        const chars = ['.', '-', '=', '+', '*', '#', '@'];
        const barWidth = this.canvas.width / magnitudes.length;

        this.ctx.font = '20px monospace';
        this.ctx.textAlign = 'center';

        for (let i = 0; i < magnitudes.length; i++) {
            const magnitude = magnitudes[i];
            const barHeight = Math.floor(magnitude * 20);
            const charIdx = Math.min(Math.floor(magnitude * chars.length), chars.length - 1);
            const char = chars[charIdx];

            const x = i * barWidth + barWidth / 2;
            for (let row = 0; row < barHeight; row++) {
                const y = this.canvas.height - row * 30 - 30;
                if (y > 0) {
                    const brightness = 200 + magnitude * 55;
                    this.ctx.fillStyle = `rgb(${brightness}, ${brightness}, ${brightness})`;
                    this.ctx.fillText(char, x, y);
                }
            }
        }
    }

    /**
     * Mode 62: Rippling Water
     */
    renderRipplingWater(magnitudes) {
        for (let i = 0; i < magnitudes.length; i++) {
            const magnitude = magnitudes[i];
            if (magnitude > 0.4) {
                const x = (i / magnitudes.length) * this.canvas.width;
                const y = this.canvas.height * 0.3;

                const rippleRadius = ((this.frameCounter % 60) * magnitude * 8);
                const alpha = 1.0 - (rippleRadius / 300);

                if (alpha > 0) {
                    this.ctx.strokeStyle = `rgba(100, 150, 255, ${alpha})`;
                    this.ctx.lineWidth = 2;
                    this.ctx.beginPath();
                    this.ctx.arc(x, y, rippleRadius, 0, Math.PI * 2);
                    this.ctx.stroke();
                }
            }
        }
    }

    /**
     * Mode 63: Terrain Flyover
     */
    renderTerrainFlyover(magnitudes) {
        const terrainWidth = 50;
        const terrainDepth = 30;
        const scale = 15;
        const offsetX = this.canvas.width / 2;
        const offsetY = this.canvas.height - 200;

        for (let z = 0; z < terrainDepth - 1; z++) {
            for (let x = 0; x < terrainWidth - 1; x++) {
                const freqIdx = Math.floor((x / terrainWidth) * magnitudes.length);
                const height = magnitudes[Math.min(freqIdx, magnitudes.length - 1)] * 200;

                const x1 = offsetX + (x - terrainWidth / 2) * scale;
                const y1 = offsetY - height - z * 10;

                const x2 = offsetX + (x + 1 - terrainWidth / 2) * scale;
                const y2 = offsetY - height - z * 10;

                const x3 = offsetX + (x - terrainWidth / 2) * scale;
                const y3 = offsetY - height - (z + 1) * 10;

                const depthFactor = 1 - z / terrainDepth;
                const color = `rgb(${100 * depthFactor}, ${200 * depthFactor}, ${100 * depthFactor})`;

                this.ctx.strokeStyle = color;
                this.ctx.lineWidth = 1;
                this.ctx.beginPath();
                this.ctx.moveTo(x1, y1);
                this.ctx.lineTo(x2, y2);
                this.ctx.stroke();

                this.ctx.beginPath();
                this.ctx.moveTo(x1, y1);
                this.ctx.lineTo(x3, y3);
                this.ctx.stroke();
            }
        }
    }

    /**
     * Mode 64: String Art
     */
    renderStringArt(magnitudes) {
        const numPoints = Math.min(magnitudes.length, 36);
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);
        const mids = magnitudes.slice(Math.floor(magnitudes.length / 4), Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 2);
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);

        // Calculate points
        const points = [];
        for (let i = 0; i < numPoints; i++) {
            const angle = (i / numPoints) * Math.PI * 2;
            const radius = this.maxRadius * 0.8 * (1 + bass * 0.3);
            const x = this.centerX + Math.cos(angle) * radius;
            const y = this.centerY + Math.sin(angle) * radius;
            points.push({ x, y });
        }

        // Draw lines
        const numLines = mids * 50 + treble * 100;
        const hue = treble * 180;
        const rgb = this.hsvToRgb(hue, 80, 60);

        this.ctx.strokeStyle = `rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, 0.3)`;
        this.ctx.lineWidth = 1;

        for (let i = 0; i < numLines; i++) {
            const idx1 = Math.floor(Math.random() * points.length);
            const idx2 = Math.floor(Math.random() * points.length);
            if (idx1 !== idx2) {
                this.ctx.beginPath();
                this.ctx.moveTo(points[idx1].x, points[idx1].y);
                this.ctx.lineTo(points[idx2].x, points[idx2].y);
                this.ctx.stroke();
            }
        }

        // Draw points
        this.ctx.fillStyle = '#FFFFFF';
        points.forEach(point => {
            this.ctx.beginPath();
            this.ctx.arc(point.x, point.y, 4, 0, Math.PI * 2);
            this.ctx.fill();
        });
    }

    /**
     * Mode 65: Fire Embers
     */
    renderFireEmbers(magnitudes) {
        if (!this.emberParticles) this.emberParticles = [];

        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / (magnitudes.length / 4);

        // Central fire
        const fireHeight = bass * 300 + 100;
        const fireWidth = 150;

        for (let i = 0; i < 20; i++) {
            const flameX = this.centerX + (Math.random() - 0.5) * fireWidth;
            const flameY = this.canvas.height - 100 - Math.random() * fireHeight;
            const flameSize = 20 + bass * 30;

            const hue = 10 + Math.random() * 20;
            const rgb = this.hsvToRgb(hue, 100, 78 + Math.random() * 22);
            this.ctx.fillStyle = `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;
            this.ctx.beginPath();
            this.ctx.arc(flameX, flameY, flameSize, 0, Math.PI * 2);
            this.ctx.fill();
        }

        // Emit embers on treble
        if (treble > 0.5) {
            for (let i = 0; i < treble * 30; i++) {
                this.emberParticles.push({
                    x: this.centerX + (Math.random() - 0.5) * 100,
                    y: this.canvas.height - 150,
                    vx: (Math.random() - 0.5) * 8,
                    vy: -Math.random() * 15 - 5,
                    life: 1.0
                });
            }
        }

        // Update embers
        this.emberParticles = this.emberParticles.filter(ember => {
            ember.x += ember.vx;
            ember.y += ember.vy;
            ember.vy += 0.5; // Gravity
            ember.life -= 0.015;

            if (ember.life > 0 && ember.y < this.canvas.height) {
                const alpha = ember.life;
                this.ctx.fillStyle = `rgba(100, 150, 255, ${alpha})`;
                this.ctx.beginPath();
                this.ctx.arc(ember.x, ember.y, 3, 0, Math.PI * 2);
                this.ctx.fill();
                return true;
            }
            return false;
        });
    }

    /**
     * Mode 66: Radial Kaleidoscope
     */
    renderRadialKaleidoscope(magnitudes) {
        const numSegments = 8;
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const segmentAngle = (Math.PI * 2) / numSegments;

        // Draw particles in mirrored segments
        for (let i = 0; i < Math.min(magnitudes.length, 30); i++) {
            const magnitude = magnitudes[i];
            if (magnitude > 0.2) {
                const angle = (i / 30) * segmentAngle;
                const distance = 100 + magnitude * 300;

                const hue = (i / 30) * 360;
                const [r, g, b] = this.hsvToRgb(hue, 1.0, magnitude);

                // Draw in all mirrored segments
                for (let seg = 0; seg < numSegments; seg++) {
                    const segAngle = seg * segmentAngle + this.frameCounter * 0.02;
                    const rotX = this.centerX + Math.cos(angle + segAngle) * distance;
                    const rotY = this.centerY + Math.sin(angle + segAngle) * distance;

                    const size = 5 + magnitude * 15;
                    this.ctx.fillStyle = `rgb(${r}, ${g}, ${b})`;
                    this.ctx.beginPath();
                    this.ctx.arc(rotX, rotY, size, 0, Math.PI * 2);
                    this.ctx.fill();
                }
            }
        }
    }

    /**
     * Mode 67: Pulsing Jellyfish
     */
    renderPulsingJellyfish(magnitudes) {
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);

        // Jellyfish bell (pulses with bass)
        const bellRadius = 80 + bass * 70;
        const bellY = this.centerY - 100;

        // Draw semi-transparent bell
        this.ctx.globalAlpha = 0.6;
        this.ctx.fillStyle = 'rgba(150, 100, 255, 0.6)';
        this.ctx.beginPath();
        this.ctx.ellipse(this.centerX, bellY, bellRadius, bellRadius * 0.7, 0, 0, Math.PI);
        this.ctx.fill();
        this.ctx.globalAlpha = 1.0;

        // Tentacles (waveforms for frequencies)
        const numTentacles = 8;
        for (let t = 0; t < numTentacles; t++) {
            const tentacleXOffset = (t - numTentacles / 2) * 30;
            const freqStart = Math.floor(t * magnitudes.length / numTentacles);
            const freqEnd = Math.floor((t + 1) * magnitudes.length / numTentacles);
            const tentacleFreqs = magnitudes.slice(freqStart, freqEnd);

            this.ctx.beginPath();
            this.ctx.strokeStyle = 'rgba(200, 150, 255, 0.8)';
            this.ctx.lineWidth = 3;

            tentacleFreqs.forEach((magnitude, i) => {
                const x = this.centerX + tentacleXOffset + Math.sin(i * 0.5 + this.frameCounter * 0.1) * 15;
                const y = bellY + bellRadius / 2 + i * 8 + magnitude * 50;

                if (i === 0) {
                    this.ctx.moveTo(x, y);
                } else {
                    this.ctx.lineTo(x, y);
                }
            });

            this.ctx.stroke();
        }
    }

    /**
     * Mode 68: Orbital System
     */
    renderOrbitalSystem(magnitudes) {
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const mids = magnitudes.slice(Math.floor(magnitudes.length / 4), Math.floor(3 * magnitudes.length / 4));
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);

        // Central sun pulses
        const sunRadius = 40 + avgMagnitude * 40;
        this.ctx.fillStyle = 'rgb(100, 200, 255)';
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, sunRadius, 0, Math.PI * 2);
        this.ctx.fill();

        this.ctx.strokeStyle = 'rgb(150, 220, 255)';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, sunRadius + 10, 0, Math.PI * 2);
        this.ctx.stroke();

        // Planets orbit
        const numPlanets = Math.min(mids.length, 6);
        for (let i = 0; i < numPlanets; i++) {
            const magnitude = i < mids.length ? mids[i] : 0;
            const orbitRadius = 120 + i * 70;
            const angle = this.frameCounter * 0.02 * (1 + i * 0.3);

            const planetX = this.centerX + Math.cos(angle) * orbitRadius;
            const planetY = this.centerY + Math.sin(angle) * orbitRadius;
            const planetSize = 10 + magnitude * 25;

            // Planet color
            const hue = (i / numPlanets) * 360;
            const [r, g, b] = this.hsvToRgb(hue, 0.8, 1.0);

            this.ctx.fillStyle = `rgb(${r}, ${g}, ${b})`;
            this.ctx.beginPath();
            this.ctx.arc(planetX, planetY, planetSize, 0, Math.PI * 2);
            this.ctx.fill();

            // Moon orbits planet (treble)
            if (treble > 0.4) {
                const moonAngle = this.frameCounter * 0.1;
                const moonDistance = planetSize + 20;
                const moonX = planetX + Math.cos(moonAngle) * moonDistance;
                const moonY = planetY + Math.sin(moonAngle) * moonDistance;
                const moonSize = 3 + treble * 8;

                this.ctx.fillStyle = 'rgb(200, 200, 200)';
                this.ctx.beginPath();
                this.ctx.arc(moonX, moonY, moonSize, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }
    }

    /**
     * Mode 69: Spectrum Cube
     */
    renderSpectrumCube(magnitudes) {
        if (!this.cubeRotation) this.cubeRotation = 0;
        this.cubeRotation += 0.02;

        const cubeSize = 200;
        const angleX = this.cubeRotation;
        const angleY = this.cubeRotation * 0.7;

        // Cube vertices
        const vertices3D = [
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
        ];

        // Rotate and project
        const vertices2D = vertices3D.map(([vx, vy, vz]) => {
            // Rotate around Y
            let x = vx * Math.cos(angleY) - vz * Math.sin(angleY);
            let z = vx * Math.sin(angleY) + vz * Math.cos(angleY);

            // Rotate around X
            const y = vy * Math.cos(angleX) - z * Math.sin(angleX);
            z = vy * Math.sin(angleX) + z * Math.cos(angleX);

            // Project to 2D
            const scale = cubeSize / (3 + z);
            const x2d = this.centerX + x * scale;
            const y2d = this.centerY + y * scale;

            return [x2d, y2d];
        });

        // Draw cube edges
        const edges = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]];
        this.ctx.strokeStyle = 'rgb(100, 200, 255)';
        this.ctx.lineWidth = 2;

        edges.forEach(([start, end]) => {
            this.ctx.beginPath();
            this.ctx.moveTo(vertices2D[start][0], vertices2D[start][1]);
            this.ctx.lineTo(vertices2D[end][0], vertices2D[end][1]);
            this.ctx.stroke();
        });

        // Draw bars on front face
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const faceCenterX = (vertices2D[0][0] + vertices2D[2][0]) / 2;
        const faceCenterY = (vertices2D[0][1] + vertices2D[2][1]) / 2;
        const barLength = 30 + avgMagnitude * 50;

        this.ctx.strokeStyle = 'rgb(255, 200, 100)';
        this.ctx.lineWidth = 3;
        this.ctx.beginPath();
        this.ctx.moveTo(faceCenterX, faceCenterY);
        this.ctx.lineTo(faceCenterX, faceCenterY - barLength);
        this.ctx.stroke();
    }

    /**
     * Mode 70: Typographic Flow
     */
    renderTypographicFlow(magnitudes) {
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);

        // Initialize word particles
        if (!this.wordParticles) this.wordParticles = [];

        // Spawn new words
        if (this.frameCounter % 30 === 0) {
            const words = ['MUSIC', 'FLOW', 'VIBE', 'SOUND', 'WAVE', 'PULSE', 'RHYTHM'];
            const word = words[Math.floor(Math.random() * words.length)];
            this.wordParticles.push({
                word: word,
                x: Math.random() * this.canvas.width,
                y: this.canvas.height + 50,
                vy: -2 - Math.random() * 2,
                life: 1.0
            });
        }

        // Update and draw words
        this.wordParticles = this.wordParticles.filter(particle => {
            particle.y += particle.vy;
            particle.life -= 0.01;

            if (particle.life > 0 && particle.y > -100) {
                const size = 20 + bass * 40;
                const waviness = treble * 20;
                const offsetX = Math.sin(particle.y * 0.02 + this.frameCounter * 0.1) * waviness;

                this.ctx.save();
                this.ctx.font = `${size}px Arial`;
                this.ctx.fillStyle = `rgba(100, 200, 255, ${particle.life})`;
                this.ctx.fillText(particle.word, particle.x + offsetX, particle.y);
                this.ctx.restore();

                return true;
            }
            return false;
        });
    }

    /**
     * Mode 71: Sonar Ping
     */
    renderSonarPing(magnitudes) {
        // Rotating sweep line
        const sweepAngle = (this.frameCounter * 0.05) % (Math.PI * 2);
        const sweepEndX = this.centerX + Math.cos(sweepAngle) * this.maxRadius;
        const sweepEndY = this.centerY + Math.sin(sweepAngle) * this.maxRadius;

        // Draw sweep line
        this.ctx.strokeStyle = 'rgb(100, 255, 100)';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        this.ctx.moveTo(this.centerX, this.centerY);
        this.ctx.lineTo(sweepEndX, sweepEndY);
        this.ctx.stroke();

        // Draw concentric circles (radar grid)
        this.ctx.strokeStyle = 'rgb(50, 100, 50)';
        this.ctx.lineWidth = 1;
        for (let ring = 1; ring <= 5; ring++) {
            const radius = (this.maxRadius * ring) / 5;
            this.ctx.beginPath();
            this.ctx.arc(this.centerX, this.centerY, radius, 0, Math.PI * 2);
            this.ctx.stroke();
        }

        // Frequency blips appear on radar
        magnitudes.forEach((magnitude, i) => {
            if (magnitude > 0.4) {
                const distance = (i / magnitudes.length) * this.maxRadius;
                const angle = sweepAngle + (Math.random() - 0.5) * 0.5;

                const blipX = this.centerX + Math.cos(angle) * distance;
                const blipY = this.centerY + Math.sin(angle) * distance;

                const blipSize = 3 + magnitude * 12;
                const brightness = 200 + magnitude * 55;

                this.ctx.fillStyle = `rgb(${brightness}, 255, ${brightness})`;
                this.ctx.beginPath();
                this.ctx.arc(blipX, blipY, blipSize, 0, Math.PI * 2);
                this.ctx.fill();
            }
        });
    }

    /**
     * Mode 72: VU Meters
     */
    renderVUMeters(magnitudes) {
        // Split audio into Left/Right
        const leftMagnitude = magnitudes.slice(0, Math.floor(magnitudes.length / 2))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 2);
        const rightMagnitude = magnitudes.slice(Math.floor(magnitudes.length / 2))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 2);

        // Initialize needle positions
        if (!this.vuNeedlePositions) this.vuNeedlePositions = [-60, -60];

        // Smooth needle movement
        const targetLeft = -60 + leftMagnitude * 120;
        const targetRight = -60 + rightMagnitude * 120;

        this.vuNeedlePositions[0] += (targetLeft - this.vuNeedlePositions[0]) * 0.3;
        this.vuNeedlePositions[1] += (targetRight - this.vuNeedlePositions[1]) * 0.3;

        // Draw VU meters
        const meterWidth = 300;
        const meterHeight = 200;

        ['L', 'R'].forEach((label, idx) => {
            const centerX = this.canvas.width / 4 + idx * this.canvas.width / 2;
            const centerY = this.centerY;
            const needleAngle = this.vuNeedlePositions[idx];

            // Draw meter face
            this.ctx.fillStyle = 'rgb(50, 50, 50)';
            this.ctx.beginPath();
            this.ctx.ellipse(centerX, centerY, meterWidth / 2, meterHeight / 2, 0, Math.PI, 2 * Math.PI);
            this.ctx.fill();

            this.ctx.strokeStyle = 'rgb(200, 200, 200)';
            this.ctx.lineWidth = 3;
            this.ctx.beginPath();
            this.ctx.ellipse(centerX, centerY, meterWidth / 2, meterHeight / 2, 0, Math.PI, 2 * Math.PI);
            this.ctx.stroke();

            // Draw scale marks
            for (let angle = -60; angle <= 60; angle += 10) {
                const markAngleRad = (Math.PI - angle * Math.PI / 180);
                const startR = meterWidth / 2 - 20;
                const endR = meterWidth / 2 - 10;

                this.ctx.strokeStyle = 'rgb(200, 200, 200)';
                this.ctx.lineWidth = 2;
                this.ctx.beginPath();
                this.ctx.moveTo(centerX + Math.cos(markAngleRad) * startR,
                               centerY - Math.sin(markAngleRad) * startR);
                this.ctx.lineTo(centerX + Math.cos(markAngleRad) * endR,
                               centerY - Math.sin(markAngleRad) * endR);
                this.ctx.stroke();
            }

            // Draw needle
            const needleAngleRad = (Math.PI - needleAngle * Math.PI / 180);
            this.ctx.strokeStyle = 'rgb(255, 100, 100)';
            this.ctx.lineWidth = 4;
            this.ctx.beginPath();
            this.ctx.moveTo(centerX, centerY);
            this.ctx.lineTo(centerX + Math.cos(needleAngleRad) * (meterWidth / 2 - 30),
                           centerY - Math.sin(needleAngleRad) * (meterWidth / 2 - 30));
            this.ctx.stroke();

            this.ctx.fillStyle = 'rgb(150, 150, 150)';
            this.ctx.beginPath();
            this.ctx.arc(centerX, centerY, 10, 0, Math.PI * 2);
            this.ctx.fill();

            // Label
            this.ctx.fillStyle = 'rgb(200, 200, 200)';
            this.ctx.font = '32px Arial';
            this.ctx.fillText(label, centerX - 15, centerY + 80);
        });
    }

    /**
     * Mode 73: Lightning Cloud
     */
    renderLightningCloud(magnitudes) {
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);

        // Cloud shape
        const cloudHeight = 150 + bass * 100;

        this.ctx.globalAlpha = 0.3;
        for (let i = 0; i < 20; i++) {
            const cloudX = Math.random() * this.canvas.width;
            const cloudY = Math.random() * cloudHeight;
            const cloudSize = 30 + bass * 50;

            this.ctx.fillStyle = 'rgb(30, 30, 50)';
            this.ctx.beginPath();
            this.ctx.arc(cloudX, cloudY, cloudSize, 0, Math.PI * 2);
            this.ctx.fill();
        }
        this.ctx.globalAlpha = 1.0;

        // Lightning bolts on strong treble
        if (treble > 0.65) {
            const startX = Math.random() * (this.canvas.width / 2) + this.canvas.width / 4;
            const startY = cloudHeight;

            let x = startX;
            let y = startY;
            const points = [[x, y]];

            // Jagged lightning path
            for (let i = 0; i < 5 + treble * 10; i++) {
                x += (Math.random() - 0.5) * 80;
                y += 40 + Math.random() * 60;
                points.push([x, y]);
            }

            // Draw lightning (glow first, then bright line)
            this.ctx.lineWidth = 12;
            this.ctx.strokeStyle = 'rgba(100, 100, 200, 0.6)';
            this.ctx.beginPath();
            points.forEach((point, i) => {
                if (i === 0) this.ctx.moveTo(point[0], point[1]);
                else this.ctx.lineTo(point[0], point[1]);
            });
            this.ctx.stroke();

            const brightness = 200 + treble * 55;
            this.ctx.lineWidth = 4;
            this.ctx.strokeStyle = `rgb(${brightness}, ${brightness}, 255)`;
            this.ctx.beginPath();
            points.forEach((point, i) => {
                if (i === 0) this.ctx.moveTo(point[0], point[1]);
                else this.ctx.lineTo(point[0], point[1]);
            });
            this.ctx.stroke();
        }
    }

    /**
     * Mode 74: Bouncing Balls
     */
    renderBouncingBalls(magnitudes) {
        // Initialize balls
        if (!this.bouncingBalls) {
            this.bouncingBalls = [];
            for (let i = 0; i < Math.min(magnitudes.length, 30); i++) {
                this.bouncingBalls.push({
                    x: (i / 30) * this.canvas.width,
                    y: this.canvas.height - 50,
                    vy: 0,
                    colorHue: (i / 30) * 360
                });
            }
        }

        const gravity = 0.8;

        // Update and draw balls
        this.bouncingBalls.forEach((ball, i) => {
            if (i >= magnitudes.length) return;

            const magnitude = magnitudes[i];

            // Bounce based on amplitude
            if (ball.y >= this.canvas.height - 50) {
                ball.vy = -magnitude * 30 - 5;
            }

            // Apply gravity
            ball.vy += gravity;
            ball.y += ball.vy;

            // Keep ball in bounds
            if (ball.y > this.canvas.height - 50) {
                ball.y = this.canvas.height - 50;
                ball.vy *= -0.7;
            }

            // Draw ball
            const ballSize = 10 + magnitude * 20;
            const [r, g, b] = this.hsvToRgb(ball.colorHue, 1.0, 1.0);

            this.ctx.fillStyle = `rgb(${r}, ${g}, ${b})`;
            this.ctx.beginPath();
            this.ctx.arc(ball.x, ball.y, ballSize, 0, Math.PI * 2);
            this.ctx.fill();
        });
    }

    /**
     * Mode 75: Liquid Ink
     */
    renderLiquidInk(magnitudes) {
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);

        // Initialize blooms
        if (!this.inkBlooms) this.inkBlooms = [];

        // Bass hits create large ink blooms
        if (bass > 0.4 && this.frameCounter % 15 === 0) {
            this.inkBlooms.push({
                x: Math.random() * (this.canvas.width - 400) + 200,
                y: 100,
                radius: 10,
                maxRadius: 150 + bass * 200,
                life: 1.0,
                hue: bass * 60
            });
        }

        // Treble creates small bright splatters
        if (treble > 0.5) {
            for (let i = 0; i < treble * 10; i++) {
                this.inkBlooms.push({
                    x: Math.random() * this.canvas.width,
                    y: Math.random() * this.canvas.height,
                    radius: 5,
                    maxRadius: 20 + treble * 40,
                    life: 1.0,
                    hue: 120 + treble * 60
                });
            }
        }

        // Update and draw blooms
        this.inkBlooms = this.inkBlooms.filter(bloom => {
            bloom.radius += 2;
            bloom.life -= 0.01;

            if (bloom.life > 0 && bloom.radius < bloom.maxRadius) {
                const [r, g, b] = this.hsvToRgb(bloom.hue, 0.8, bloom.life);

                this.ctx.strokeStyle = `rgba(${r}, ${g}, ${b}, ${bloom.life})`;
                this.ctx.lineWidth = 2;
                this.ctx.beginPath();
                this.ctx.arc(bloom.x, bloom.y, bloom.radius, 0, Math.PI * 2);
                this.ctx.stroke();

                return true;
            }
            return false;
        });

        // Limit blooms
        if (this.inkBlooms.length > 100) {
            this.inkBlooms = this.inkBlooms.slice(-100);
        }
    }

    renderStereoLandscape(magnitudes) {
        // Mode 76: 3D perspective - left channel left mountain, right channel right mountain
        const midpoint = Math.floor(magnitudes.length / 2);
        const leftMags = magnitudes.slice(0, midpoint);
        const rightMags = magnitudes.slice(midpoint);

        // Draw left landscape
        this.ctx.beginPath();
        this.ctx.moveTo(0, this.canvas.height);

        for (let i = 0; i < leftMags.length; i++) {
            const x = (i / leftMags.length) * (this.canvas.width / 2);
            const y = this.canvas.height - 100 - leftMags[i] * 300;
            this.ctx.lineTo(x, y);
        }

        this.ctx.lineTo(this.canvas.width / 2, this.canvas.height);
        this.ctx.lineTo(0, this.canvas.height);
        this.ctx.fillStyle = 'rgba(100, 150, 255, 0.7)';
        this.ctx.fill();

        // Left landscape outline
        this.ctx.beginPath();
        for (let i = 0; i < leftMags.length; i++) {
            const x = (i / leftMags.length) * (this.canvas.width / 2);
            const y = this.canvas.height - 100 - leftMags[i] * 300;
            if (i === 0) this.ctx.moveTo(x, y);
            else this.ctx.lineTo(x, y);
        }
        this.ctx.strokeStyle = 'rgba(150, 200, 255, 1)';
        this.ctx.lineWidth = 3;
        this.ctx.stroke();

        // Draw right landscape
        this.ctx.beginPath();
        this.ctx.moveTo(this.canvas.width / 2, this.canvas.height);

        for (let i = 0; i < rightMags.length; i++) {
            const x = this.canvas.width / 2 + (i / rightMags.length) * (this.canvas.width / 2);
            const y = this.canvas.height - 100 - rightMags[i] * 300;
            this.ctx.lineTo(x, y);
        }

        this.ctx.lineTo(this.canvas.width, this.canvas.height);
        this.ctx.lineTo(this.canvas.width / 2, this.canvas.height);
        this.ctx.fillStyle = 'rgba(255, 150, 100, 0.7)';
        this.ctx.fill();

        // Right landscape outline
        this.ctx.beginPath();
        for (let i = 0; i < rightMags.length; i++) {
            const x = this.canvas.width / 2 + (i / rightMags.length) * (this.canvas.width / 2);
            const y = this.canvas.height - 100 - rightMags[i] * 300;
            if (i === 0) this.ctx.moveTo(x, y);
            else this.ctx.lineTo(x, y);
        }
        this.ctx.strokeStyle = 'rgba(255, 200, 150, 1)';
        this.ctx.lineWidth = 3;
        this.ctx.stroke();
    }

    renderAILatentWalk(magnitudes) {
        // Mode 77: Abstract latent space visualization (simulated)
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);

        // Initialize latent state
        if (this.latentMorphState === undefined) this.latentMorphState = 0;
        this.latentMorphState += avgMagnitude * 0.1;

        const numShapes = 15;
        for (let i = 0; i < numShapes; i++) {
            // Position influenced by latent state
            const angle = (i / numShapes) * Math.PI * 2 + this.latentMorphState;
            const radius = 100 + Math.sin(this.latentMorphState + i) * 200;

            const x = this.canvas.width / 2 + Math.cos(angle) * radius;
            const y = this.canvas.height / 2 + Math.sin(angle) * radius;

            // Morphing size
            const size = 20 + bass * 40 + Math.sin(this.latentMorphState * 2 + i) * 20;

            // Dream-like colors
            const hue = (this.latentMorphState * 50 + i * 12) % 360;
            const saturation = 70 + treble * 30;
            const value = 60 + avgMagnitude * 40;

            const [r, g, b] = this.hsvToRgb(hue, saturation / 100, value / 100);

            // Draw with glow effect
            this.ctx.fillStyle = `rgba(${r}, ${g}, ${b}, 0.7)`;
            this.ctx.beginPath();
            this.ctx.arc(x, y, size, 0, Math.PI * 2);
            this.ctx.fill();
        }
    }

    renderPixelStorm(magnitudes) {
        // Mode 78: Blizzard of 8-bit pixels - wind direction from stereo, speed from volume
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;

        // Stereo pan (L/R balance)
        const midpoint = Math.floor(magnitudes.length / 2);
        const leftPower = magnitudes.slice(0, midpoint).reduce((a, b) => a + b, 0) / midpoint;
        const rightPower = magnitudes.slice(midpoint).reduce((a, b) => a + b, 0) / (magnitudes.length - midpoint);
        const windDirection = (rightPower - leftPower) * 5;

        // Initialize pixel storm
        if (!this.pixelStorm) this.pixelStorm = [];

        // Spawn pixels
        if (this.frameCounter % 2 === 0) {
            const numPixels = Math.floor(avgMagnitude * 30 + 10);
            for (let i = 0; i < numPixels; i++) {
                // Dominant frequency determines color
                const dominantFreqIdx = magnitudes.indexOf(Math.max(...magnitudes));
                const hue = (dominantFreqIdx / magnitudes.length) * 360;

                this.pixelStorm.push({
                    x: Math.random() * this.canvas.width,
                    y: 0,
                    vx: windDirection + (Math.random() - 0.5) * 3,
                    vy: 3 + avgMagnitude * 5,
                    hue: hue,
                    life: 1.0
                });
            }
        }

        // Update and draw pixels
        this.pixelStorm = this.pixelStorm.filter(pixel => {
            pixel.x += pixel.vx;
            pixel.y += pixel.vy;
            pixel.life -= 0.01;

            if (pixel.life > 0 && pixel.y < this.canvas.height) {
                const [r, g, b] = this.hsvToRgb(pixel.hue / 360, 1, 1);

                // 8-bit pixel (small rectangle)
                this.ctx.fillStyle = `rgb(${r}, ${g}, ${b})`;
                this.ctx.fillRect(Math.floor(pixel.x), Math.floor(pixel.y), 4, 4);

                return true;
            }
            return false;
        });

        // Limit particle count
        if (this.pixelStorm.length > 400) {
            this.pixelStorm = this.pixelStorm.slice(-400);
        }
    }

    renderGrowingVine(magnitudes) {
        // Mode 79: Vine grows across screen, sprouts leaves on beats
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);

        // Initialize vine
        if (!this.vineSegments) this.vineSegments = [];

        // Grow vine if not complete
        if (this.vineSegments.length < 200) {
            if (this.vineSegments.length === 0) {
                this.vineSegments.push({x: 100, y: this.canvas.height - 100, leaves: []});
            } else {
                const last = this.vineSegments[this.vineSegments.length - 1];
                // Vine meanders
                const angle = -Math.PI / 6 + (Math.random() - 0.5) * Math.PI / 4;
                const newX = last.x + Math.cos(angle) * 15;
                const newY = last.y + Math.sin(angle) * 15;

                if (newX > 0 && newX < this.canvas.width && newY > 0 && newY < this.canvas.height) {
                    const newSegment = {x: newX, y: newY, leaves: []};
                    this.vineSegments.push(newSegment);

                    // Sprout leaf on beat
                    if (bass > 0.5) {
                        const leafSize = 10 + bass * 30;
                        newSegment.leaves.push({
                            offsetX: (Math.random() - 0.5) * 20,
                            offsetY: (Math.random() - 0.5) * 20,
                            size: leafSize
                        });
                    }
                }
            }
        }

        // Draw vine
        this.ctx.strokeStyle = 'rgb(50, 120, 50)';
        this.ctx.lineWidth = 3;
        this.ctx.beginPath();
        for (let i = 0; i < this.vineSegments.length - 1; i++) {
            const seg = this.vineSegments[i];
            const nextSeg = this.vineSegments[i + 1];
            if (i === 0) {
                this.ctx.moveTo(seg.x, seg.y);
            }
            this.ctx.lineTo(nextSeg.x, nextSeg.y);
        }
        this.ctx.stroke();

        // Draw leaves
        for (const seg of this.vineSegments) {
            for (const leaf of seg.leaves) {
                const leafX = seg.x + leaf.offsetX;
                const leafY = seg.y + leaf.offsetY;
                this.ctx.fillStyle = 'rgb(100, 255, 100)';
                this.ctx.beginPath();
                this.ctx.arc(leafX, leafY, leaf.size, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }
    }

    renderHauntedFaces(magnitudes) {
        // Mode 80: Ghostly faces fade in/out with mid-range (vocals), eyes glow on bass
        const midRange = magnitudes.slice(Math.floor(magnitudes.length / 4), Math.floor(3 * magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 2);
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4))
            .reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);

        // Face opacity controlled by mid-range (vocals)
        const faceAlpha = midRange;

        if (faceAlpha > 0.2) {
            // Draw ghostly faces
            const numFaces = 3;
            for (let i = 0; i < numFaces; i++) {
                const faceX = ((i + 1) * this.canvas.width) / (numFaces + 1);
                const faceY = this.canvas.height / 3 + Math.sin(this.frameCounter * 0.05 + i) * 50;
                const faceSize = 80;

                const alpha = faceAlpha * 0.5;

                // Face circle
                this.ctx.fillStyle = `rgba(200, 200, 220, ${alpha})`;
                this.ctx.beginPath();
                this.ctx.arc(faceX, faceY, faceSize, 0, Math.PI * 2);
                this.ctx.fill();

                // Eyes (glow on bass)
                const eyeGlow = bass > 0.6 ? 255 : 100;
                const eyeOffset = 25;

                // Left eye
                this.ctx.fillStyle = `rgb(${eyeGlow}, ${eyeGlow}, 50)`;
                this.ctx.beginPath();
                this.ctx.arc(faceX - eyeOffset, faceY - 20, 12, 0, Math.PI * 2);
                this.ctx.fill();

                // Right eye
                this.ctx.beginPath();
                this.ctx.arc(faceX + eyeOffset, faceY - 20, 12, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }
    }

    renderConnectingConstellations(magnitudes) {
        // Mode 81: Stars that connect when their frequencies pass threshold
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;

        // Initialize stars
        if (!this.constellationStars) {
            this.constellationStars = [];
            const numStars = 50;
            for (let i = 0; i < numStars; i++) {
                this.constellationStars.push({
                    x: Math.random() * this.canvas.width,
                    y: Math.random() * this.canvas.height,
                    freqIdx: Math.floor(Math.random() * magnitudes.length),
                    shining: false,
                    baseSize: 2 + Math.random() * 3
                });
            }
        }

        // Clear with fade
        this.ctx.fillStyle = 'rgba(0, 0, 20, 0.2)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Update stars based on their frequency
        for (const star of this.constellationStars) {
            const magnitude = magnitudes[star.freqIdx];
            star.shining = magnitude > 0.5;

            const brightness = star.shining ? 255 : 100;
            const size = star.shining ? star.baseSize * (1 + magnitude) : star.baseSize;

            // Draw star
            this.ctx.fillStyle = `rgb(${brightness}, ${brightness}, 255)`;
            this.ctx.beginPath();
            this.ctx.arc(star.x, star.y, size, 0, Math.PI * 2);
            this.ctx.fill();
        }

        // Connect nearby shining stars
        this.ctx.strokeStyle = 'rgba(100, 100, 200, 0.4)';
        this.ctx.lineWidth = 1;
        for (let i = 0; i < this.constellationStars.length; i++) {
            const star1 = this.constellationStars[i];
            if (!star1.shining) continue;

            for (let j = i + 1; j < this.constellationStars.length; j++) {
                const star2 = this.constellationStars[j];
                if (!star2.shining) continue;

                const dx = star2.x - star1.x;
                const dy = star2.y - star1.y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < 200) {
                    this.ctx.beginPath();
                    this.ctx.moveTo(star1.x, star1.y);
                    this.ctx.lineTo(star2.x, star2.y);
                    this.ctx.stroke();
                }
            }
        }
    }

    renderMatrixRain(magnitudes) {
        // Mode 82: Falling Matrix-style characters with audio-reactive speed
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const treble = magnitudes.slice(Math.floor(magnitudes.length * 0.75)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.25);

        // Initialize columns
        if (!this.matrixColumns) {
            this.matrixColumns = [];
            const numColumns = Math.floor(this.canvas.width / 20);
            for (let i = 0; i < numColumns; i++) {
                this.matrixColumns.push({
                    x: i * 20,
                    y: -Math.random() * this.canvas.height,
                    speed: 2 + Math.random() * 3,
                    chars: []
                });
            }
        }

        // Clear with fade for trail effect
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Update and draw columns
        this.ctx.font = '16px monospace';
        for (const column of this.matrixColumns) {
            // Speed modulated by volume
            column.y += column.speed * (1 + avgMagnitude);

            // Reset when off screen
            if (column.y > this.canvas.height + 200) {
                column.y = -100;
            }

            // Draw trail of characters
            const trailLength = 20;
            for (let i = 0; i < trailLength; i++) {
                const charY = column.y - i * 16;
                if (charY < 0 || charY > this.canvas.height) continue;

                // Brightness fades towards tail, treble adds flash
                const brightness = 150 - i * 8 + treble * 105;
                const char = String.fromCharCode(33 + Math.floor(Math.random() * 94));

                this.ctx.fillStyle = `rgb(50, ${Math.max(0, Math.min(255, brightness))}, 50)`;
                this.ctx.fillText(char, column.x, charY);
            }
        }
    }

    renderVoxelWorld(magnitudes) {
        // Mode 83: 3D voxel grid with audio shockwave
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length * 0.25)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.25);

        this.ctx.fillStyle = 'rgb(10, 10, 30)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // 3D grid parameters
        const gridSize = 8;
        const voxelSize = 30;
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;

        // Shockwave radius from bass
        const shockwave = bass * 300;

        // Draw voxel grid with 3D perspective
        for (let x = 0; x < gridSize; x++) {
            for (let z = 0; z < gridSize; z++) {
                const worldX = (x - gridSize / 2) * voxelSize;
                const worldZ = (z - gridSize / 2) * voxelSize;

                // Distance from center for shockwave
                const dist = Math.sqrt(worldX * worldX + worldZ * worldZ);

                // Height based on frequency and distance from shockwave
                const freqIdx = Math.floor(((x + z * gridSize) / (gridSize * gridSize)) * magnitudes.length);
                const magnitude = magnitudes[freqIdx];
                const shockwaveEffect = Math.max(0, 1 - Math.abs(dist - shockwave) / 50);
                const height = (magnitude + shockwaveEffect) * 100;

                // 3D to 2D projection (simple isometric)
                const screenX = centerX + worldX - worldZ * 0.5;
                const screenY = centerY + worldZ * 0.5 - height;

                // Color based on height
                const hue = (height / 100) * 120;
                const color = this.hsvToRgb(hue / 360, 0.8, 0.9);

                // Draw voxel as diamond shape
                this.ctx.fillStyle = `rgb(${color.r}, ${color.g}, ${color.b})`;
                this.ctx.beginPath();
                this.ctx.moveTo(screenX, screenY);
                this.ctx.lineTo(screenX + voxelSize / 2, screenY + voxelSize / 4);
                this.ctx.lineTo(screenX, screenY + voxelSize / 2);
                this.ctx.lineTo(screenX - voxelSize / 2, screenY + voxelSize / 4);
                this.ctx.closePath();
                this.ctx.fill();
            }
        }
    }

    renderDNAHelixRungs(magnitudes) {
        // Mode 84: DNA double helix with rungs lighting up per frequency
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;

        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        const numRungs = 40;
        const helixRadius = 100;
        const centerX = this.canvas.width / 2;

        for (let i = 0; i < numRungs; i++) {
            const t = (i / numRungs) * Math.PI * 4 + this.frameCounter * 0.02;
            const y = (i / numRungs) * this.canvas.height;

            // Left strand
            const x1 = centerX + Math.cos(t) * helixRadius;
            // Right strand
            const x2 = centerX + Math.cos(t + Math.PI) * helixRadius;

            // Strand beads
            this.ctx.fillStyle = 'rgba(100, 150, 255, 0.8)';
            this.ctx.beginPath();
            this.ctx.arc(x1, y, 8, 0, Math.PI * 2);
            this.ctx.fill();

            this.ctx.fillStyle = 'rgba(255, 100, 150, 0.8)';
            this.ctx.beginPath();
            this.ctx.arc(x2, y, 8, 0, Math.PI * 2);
            this.ctx.fill();

            // Rung connecting strands (lit by frequency)
            const freqIdx = Math.floor((i / numRungs) * magnitudes.length);
            const magnitude = magnitudes[freqIdx];

            if (magnitude > 0.3) {
                const brightness = magnitude * 255;
                this.ctx.strokeStyle = `rgba(${brightness}, 255, ${brightness}, ${magnitude})`;
                this.ctx.lineWidth = 3;
                this.ctx.beginPath();
                this.ctx.moveTo(x1, y);
                this.ctx.lineTo(x2, y);
                this.ctx.stroke();
            }
        }
    }

    renderAudioReactiveShader(magnitudes) {
        // Mode 85: Procedural shader-like effect with audio modulation
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length * 0.25)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.25);
        const treble = magnitudes.slice(Math.floor(magnitudes.length * 0.75)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.25);

        // Pixel-based shader effect
        const imageData = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);
        const data = imageData.data;

        const time = this.frameCounter * 0.01;
        const scale = 0.02 + avgMagnitude * 0.02;

        for (let y = 0; y < this.canvas.height; y += 2) {
            for (let x = 0; x < this.canvas.width; x += 2) {
                const idx = (y * this.canvas.width + x) * 4;

                // Normalized coordinates
                const nx = x / this.canvas.width - 0.5;
                const ny = y / this.canvas.height - 0.5;

                // Distance from center
                const dist = Math.sqrt(nx * nx + ny * ny);

                // Procedural pattern
                const wave1 = Math.sin(nx * 10 * scale + time + bass * 5) * 0.5 + 0.5;
                const wave2 = Math.cos(ny * 10 * scale + time + treble * 5) * 0.5 + 0.5;
                const pattern = wave1 * wave2;

                // Radial influence
                const radialEffect = 1 - dist;

                // Color based on pattern and audio
                const r = pattern * 255 * (1 + bass);
                const g = (1 - pattern) * 255 * avgMagnitude;
                const b = Math.sin(dist * 20 + time) * 127 + 128;

                data[idx] = Math.min(255, r * radialEffect);
                data[idx + 1] = Math.min(255, g * radialEffect);
                data[idx + 2] = Math.min(255, b * radialEffect * (1 + treble));
                data[idx + 3] = 255;
            }
        }

        this.ctx.putImageData(imageData, 0, 0);
    }

    renderSpirograph(magnitudes) {
        // Mode 86: Spirograph pattern - radii controlled by frequencies
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length * 0.25)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.25);
        const mids = magnitudes.slice(Math.floor(magnitudes.length * 0.25), Math.floor(magnitudes.length * 0.75)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.5);
        const treble = magnitudes.slice(Math.floor(magnitudes.length * 0.75)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.25);

        // Clear with fade
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Spirograph parameters modulated by audio
        const R = 150 + bass * 100;  // Outer wheel radius
        const r = 50 + mids * 50;    // Inner wheel radius
        const d = 30 + treble * 40;  // Pen distance

        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;

        // Draw spirograph
        this.ctx.beginPath();
        let firstPoint = true;

        for (let t = 0; t < Math.PI * 10; t += 0.02) {
            const x = centerX + (R - r) * Math.cos(t) + d * Math.cos((R - r) / r * t);
            const y = centerY + (R - r) * Math.sin(t) - d * Math.sin((R - r) / r * t);

            if (x >= 0 && x < this.canvas.width && y >= 0 && y < this.canvas.height) {
                if (firstPoint) {
                    this.ctx.moveTo(x, y);
                    firstPoint = false;
                } else {
                    this.ctx.lineTo(x, y);
                }
            }
        }

        // Color based on treble
        const hue = treble * 360;
        const color = this.hsvToRgb(hue, 100, 100);
        this.ctx.strokeStyle = `rgb(${color.r}, ${color.g}, ${color.b})`;
        this.ctx.lineWidth = 2;
        this.ctx.stroke();
    }

    renderEqualizerTower(magnitudes) {
        // Mode 87: 3D tower of stacked glowing rings
        this.ctx.fillStyle = 'rgb(0, 0, 0)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        const numRings = Math.min(magnitudes.length, 40);
        const ringHeight = this.canvas.height / numRings;
        const centerX = this.canvas.width / 2;

        for (let i = 0; i < numRings; i++) {
            const magnitude = magnitudes[i];
            const y = this.canvas.height - (i + 1) * ringHeight;
            const radius = magnitude * (this.canvas.width / 3);

            // Color gradient
            const hue = (i / numRings) * 120;
            const saturation = 80 + magnitude * 20;
            const value = 60 + magnitude * 40;
            const color = this.hsvToRgb(hue, saturation, value);

            // Ring thickness
            const thickness = 2 + magnitude * 10;

            this.ctx.strokeStyle = `rgb(${color.r}, ${color.g}, ${color.b})`;
            this.ctx.lineWidth = thickness;
            this.ctx.beginPath();
            this.ctx.arc(centerX, y, radius, 0, Math.PI * 2);
            this.ctx.stroke();
        }
    }

    renderAudioDrivenDoodles(magnitudes) {
        // Mode 88: Generative doodle bot - bass=90° turns, treble=shakiness
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length * 0.25)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.25);
        const mids = magnitudes.slice(Math.floor(magnitudes.length * 0.25), Math.floor(magnitudes.length * 0.75)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.5);
        const treble = magnitudes.slice(Math.floor(magnitudes.length * 0.75)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.25);

        // Initialize path
        if (!this.doodlePath) {
            this.doodlePath = [{
                x: this.canvas.width / 2,
                y: this.canvas.height / 2,
                angle: 0
            }];
            this.doodleCounter = 0;
        }

        this.doodleCounter++;

        // Clear with fade
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Current position
        const current = this.doodlePath[this.doodlePath.length - 1];

        // Bass hit causes 90° turn
        if (bass > 0.6 && this.doodleCounter % 10 === 0) {
            current.angle += Math.PI / 2;
        }

        // Move forward
        const stepSize = 5 + mids * 5;
        const shakiness = treble * 10;
        let newX = current.x + Math.cos(current.angle) * stepSize + (Math.random() - 0.5) * shakiness;
        let newY = current.y + Math.sin(current.angle) * stepSize + (Math.random() - 0.5) * shakiness;

        // Keep in bounds
        newX = Math.max(50, Math.min(this.canvas.width - 50, newX));
        newY = Math.max(50, Math.min(this.canvas.height - 50, newY));

        this.doodlePath.push({ x: newX, y: newY, angle: current.angle });

        // Limit path length
        if (this.doodlePath.length > 500) {
            this.doodlePath = this.doodlePath.slice(-500);
        }

        // Draw path
        for (let i = 0; i < this.doodlePath.length - 1; i++) {
            const p1 = this.doodlePath[i];
            const p2 = this.doodlePath[i + 1];

            // Color based on mids
            const hue = mids * 360;
            const alpha = i / this.doodlePath.length;
            const color = this.hsvToRgb(hue, 80, alpha * 100);

            this.ctx.strokeStyle = `rgb(${color.r}, ${color.g}, ${color.b})`;
            this.ctx.lineWidth = 3;
            this.ctx.beginPath();
            this.ctx.moveTo(p1.x, p1.y);
            this.ctx.lineTo(p2.x, p2.y);
            this.ctx.stroke();
        }
    }

    renderFireworkShow(magnitudes) {
        // Mode 89: Bass launches rockets, they explode at peak with mid-range color
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length * 0.25)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.25);
        const mids = magnitudes.slice(Math.floor(magnitudes.length * 0.25), Math.floor(magnitudes.length * 0.75)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.5);
        const treble = magnitudes.slice(Math.floor(magnitudes.length * 0.75)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.25);

        // Initialize rockets array
        if (!this.fireworkRockets) {
            this.fireworkRockets = [];
        }

        // Clear with fade
        this.ctx.fillStyle = 'rgba(0, 0, 10, 0.15)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Launch rockets on bass hits
        if (bass > 0.55 && this.frameCounter % 10 === 0) {
            this.fireworkRockets.push({
                x: Math.random() * (this.canvas.width / 2) + this.canvas.width / 4,
                y: this.canvas.height - 50,
                vy: -10 - bass * 8,
                exploded: false,
                particles: []
            });
        }

        // Update rockets
        const newRockets = [];
        for (const rocket of this.fireworkRockets) {
            if (!rocket.exploded) {
                rocket.y += rocket.vy;
                rocket.vy += 0.3;  // Gravity

                // Draw rocket trail
                this.ctx.fillStyle = 'rgb(200, 200, 255)';
                this.ctx.beginPath();
                this.ctx.arc(rocket.x, rocket.y, 5, 0, Math.PI * 2);
                this.ctx.fill();

                // Explode at peak
                if (rocket.vy > 0) {
                    rocket.exploded = true;
                    // Create particle burst
                    const numParticles = 50 + mids * 100;
                    for (let i = 0; i < numParticles; i++) {
                        const angle = Math.random() * 2 * Math.PI;
                        const speed = 2 + Math.random() * 8;
                        rocket.particles.push({
                            x: rocket.x,
                            y: rocket.y,
                            vx: Math.cos(angle) * speed,
                            vy: Math.sin(angle) * speed,
                            life: 1.0
                        });
                    }
                }
            }

            // Update explosion particles
            if (rocket.exploded) {
                const newParticles = [];
                for (const particle of rocket.particles) {
                    particle.x += particle.vx;
                    particle.y += particle.vy;
                    particle.vy += 0.2;  // Gravity
                    particle.life -= 0.015;

                    if (particle.life > 0) {
                        // Color from mids
                        const hue = mids * 360;
                        const color = this.hsvToRgb(hue, 100, particle.life * 100);

                        const size = 2 + treble * 6;
                        this.ctx.fillStyle = `rgb(${color.r}, ${color.g}, ${color.b})`;
                        this.ctx.beginPath();
                        this.ctx.arc(particle.x, particle.y, size, 0, Math.PI * 2);
                        this.ctx.fill();

                        newParticles.push(particle);
                    }
                }

                rocket.particles = newParticles;
                if (rocket.particles.length > 0) {
                    newRockets.push(rocket);
                }
            } else {
                newRockets.push(rocket);
            }
        }

        this.fireworkRockets = newRockets.slice(0, 20);
    }

    renderMicroscopicView(magnitudes) {
        // Mode 90: Cells jiggle and divide based on frequency
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length * 0.25)).reduce((a, b) => a + b, 0) / (magnitudes.length * 0.25);
        const avgMagnitude = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;

        // Initialize cells
        if (!this.microscopicCells) {
            this.microscopicCells = [];
            for (let i = 0; i < 10; i++) {
                this.microscopicCells.push({
                    x: Math.random() * this.canvas.width,
                    y: Math.random() * this.canvas.height,
                    radius: 30 + Math.random() * 30,
                    vx: (Math.random() - 0.5) * 2,
                    vy: (Math.random() - 0.5) * 2,
                    freqIdx: i % magnitudes.length
                });
            }
        }

        // Clear
        this.ctx.fillStyle = 'rgb(240, 240, 250)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Update cells
        const newCells = [];
        for (const cell of this.microscopicCells) {
            const freqIdx = cell.freqIdx % magnitudes.length;
            const magnitude = magnitudes[freqIdx];

            // Jiggle (agitation from overall volume)
            const jiggleX = (Math.random() - 0.5) * avgMagnitude * 10;
            const jiggleY = (Math.random() - 0.5) * avgMagnitude * 10;

            cell.x += cell.vx + jiggleX;
            cell.y += cell.vy + jiggleY;

            // Bounce off walls
            if (cell.x < cell.radius || cell.x > this.canvas.width - cell.radius) {
                cell.vx *= -1;
            }
            if (cell.y < cell.radius || cell.y > this.canvas.height - cell.radius) {
                cell.vy *= -1;
            }

            // Divide when amplitude is high
            if (magnitude > 0.7 && newCells.length < 50 && Math.random() < 0.05) {
                // Create daughter cell
                newCells.push({
                    x: cell.x + 20,
                    y: cell.y + 20,
                    radius: cell.radius * 0.7,
                    vx: -cell.vx,
                    vy: -cell.vy,
                    freqIdx: freqIdx
                });
                cell.radius *= 0.7;
            }

            // Draw cell
            const hue = (freqIdx / magnitudes.length) * 120;
            const saturation = 80 + magnitude * 20;
            const value = 60 + magnitude * 40;
            const color = this.hsvToRgb(hue, saturation, value);

            this.ctx.fillStyle = `rgb(${color.r}, ${color.g}, ${color.b})`;
            this.ctx.beginPath();
            this.ctx.arc(cell.x, cell.y, cell.radius, 0, Math.PI * 2);
            this.ctx.fill();

            this.ctx.strokeStyle = 'rgb(200, 200, 200)';
            this.ctx.lineWidth = 2;
            this.ctx.stroke();

            newCells.push(cell);
        }

        this.microscopicCells = newCells.slice(0, 50);
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
    /**
     * Convert HSV to RGB
     * @param {number} h - Hue (0-360)
     * @param {number} s - Saturation (0-100)
     * @param {number} v - Value (0-100)
     * @returns {Array} RGB array [r, g, b] (0-255)
     */
    hsvToRgb(h, s, v) {
        h = h / 360;
        s = s / 100;
        v = v / 100;

        let r, g, b;
        const i = Math.floor(h * 6);
        const f = h * 6 - i;
        const p = v * (1 - s);
        const q = v * (1 - f * s);
        const t = v * (1 - (1 - f) * s);

        switch (i % 6) {
            case 0: r = v; g = t; b = p; break;
            case 1: r = q; g = v; b = p; break;
            case 2: r = p; g = v; b = t; break;
            case 3: r = p; g = q; b = v; break;
            case 4: r = t; g = p; b = v; break;
            case 5: r = v; g = p; b = q; break;
        }

        return [
            Math.round(r * 255),
            Math.round(g * 255),
            Math.round(b * 255)
        ];
    }

    dispose() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
            this.animationId = null;
        }
        this.clear();
    }
}

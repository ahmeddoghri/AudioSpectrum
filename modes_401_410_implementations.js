// Complete JavaScript implementations for modes 401-410
// These will replace the placeholder implementations in visualizer.js

// Mode 401: Atom Model - Atomic orbital model with electrons
function render401AtomModel_IMPL(magnitudes) {
    const params = this.settings.parameters || {};
    const intensity = params.intensity || 1;
    const speed = params.speed || 1;
    const complexity = params.complexity || 5;

    const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4)).reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);

    this.frameCounter = (this.frameCounter || 0) + speed;

    // Nucleus
    this.ctx.fillStyle = this.getColor(0, 3);
    this.ctx.beginPath();
    this.ctx.arc(this.centerX, this.centerY, 15 * intensity, 0, Math.PI * 2);
    this.ctx.fill();

    // Electron orbitals
    const numOrbitals = Math.min(3, Math.floor(complexity / 2));
    for (let orbital = 0; orbital < numOrbitals; orbital++) {
        const radius = 60 + orbital * 80;
        const tilt = orbital * 30;

        const magIdx = Math.floor(orbital * magnitudes.length / numOrbitals);
        const mag = magnitudes[magIdx];

        // Orbital path (ellipse)
        this.ctx.strokeStyle = this.getColor(orbital, numOrbitals);
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        this.ctx.ellipse(this.centerX, this.centerY, radius, radius * 0.3, tilt * Math.PI / 180, 0, Math.PI * 2);
        this.ctx.stroke();

        // Electrons
        const numElectrons = orbital + 2;
        for (let e = 0; e < numElectrons; e++) {
            const angle = (e / numElectrons) * 2 * Math.PI + this.frameCounter * 0.05 * (orbital + 1);

            const ex = this.centerX + Math.cos(angle) * radius * Math.cos(tilt * Math.PI / 180);
            const ey = this.centerY + Math.sin(angle) * radius * 0.3;

            const size = 5 + mag * 10 * intensity;
            this.ctx.fillStyle = this.getColor(e, numElectrons);
            this.ctx.beginPath();
            this.ctx.arc(ex, ey, size, 0, Math.PI * 2);
            this.ctx.fill();
        }
    }
}

// Mode 402: Double Helix - DNA double helix structure
function render402DoubleHelix_IMPL(magnitudes) {
    const params = this.settings.parameters || {};
    const intensity = params.intensity || 1;
    const speed = params.speed || 1;
    const complexity = params.complexity || 5;

    this.frameCounter = (this.frameCounter || 0) + speed;

    // Two spiraling strands
    for (let i = 0; i < magnitudes.length; i++) {
        const mag = magnitudes[i];
        const t = (i / magnitudes.length) * 4 * Math.PI + this.frameCounter * 0.05;

        const radius = 100 * intensity;
        const y = (i / magnitudes.length) * this.canvas.height;

        // Strand 1
        const x1 = this.centerX + Math.cos(t) * radius;
        this.ctx.fillStyle = this.getColor(0, 2);
        this.ctx.beginPath();
        this.ctx.arc(x1, y, 5, 0, Math.PI * 2);
        this.ctx.fill();

        // Strand 2
        const x2 = this.centerX + Math.cos(t + Math.PI) * radius;
        this.ctx.fillStyle = this.getColor(1, 2);
        this.ctx.beginPath();
        this.ctx.arc(x2, y, 5, 0, Math.PI * 2);
        this.ctx.fill();

        // Base pairs (connecting rungs)
        if (i % 5 === 0) {
            this.ctx.strokeStyle = `rgba(150, 150, 150, ${0.5 + mag * 0.5})`;
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            this.ctx.moveTo(x1, y);
            this.ctx.lineTo(x2, y);
            this.ctx.stroke();
        }
    }
}

// Mode 403: Magnetic Field - Magnetic field lines
function render403MagneticField_IMPL(magnitudes) {
    const params = this.settings.parameters || {};
    const intensity = params.intensity || 1;
    const speed = params.speed || 1;

    // Two poles
    const pole1X = this.canvas.width * 0.3;
    const pole2X = this.canvas.width * 0.7;
    const poleY = this.centerY;

    // N pole
    this.ctx.fillStyle = `rgb(255, 100, 100)`;
    this.ctx.beginPath();
    this.ctx.arc(pole1X, poleY, 20 * intensity, 0, Math.PI * 2);
    this.ctx.fill();

    // S pole
    this.ctx.fillStyle = `rgb(100, 100, 255)`;
    this.ctx.beginPath();
    this.ctx.arc(pole2X, poleY, 20 * intensity, 0, Math.PI * 2);
    this.ctx.fill();

    // Field lines
    const step = Math.max(1, Math.floor(magnitudes.length / 15));
    for (let i = 0; i < magnitudes.length; i += step) {
        const mag = magnitudes[i];
        const offset = (i / step - 10) * 15;

        // Curved field line
        this.ctx.beginPath();
        this.ctx.strokeStyle = this.getColor(i, magnitudes.length);
        this.ctx.lineWidth = 1 + mag * 2;

        for (let t = 0; t <= 1; t += 0.03) {
            const x = pole1X + t * (pole2X - pole1X);
            const curve = Math.sin(t * Math.PI) * (100 + mag * 50 * intensity + offset);
            const y = poleY + curve;

            if (t === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }
        this.ctx.stroke();
    }
}

// Mode 404: Wave Interference - Wave interference patterns
function render404WaveInterference_IMPL(magnitudes) {
    const params = this.settings.parameters || {};
    const intensity = params.intensity || 1;
    const speed = params.speed || 1;

    this.frameCounter = (this.frameCounter || 0) + speed;

    const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4)).reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);

    // Two wave sources
    const source1 = {x: this.canvas.width * 0.4, y: this.centerY};
    const source2 = {x: this.canvas.width * 0.6, y: this.centerY};

    // Draw interference pattern
    for (let y = 0; y < this.canvas.height; y += 8) {
        for (let x = 0; x < this.canvas.width; x += 8) {
            // Distance from each source
            const d1 = Math.sqrt((x - source1.x) ** 2 + (y - source1.y) ** 2);
            const d2 = Math.sqrt((x - source2.x) ** 2 + (y - source2.y) ** 2);

            // Wave equations
            const wave1 = Math.sin(d1 * 0.05 - this.frameCounter * 0.1);
            const wave2 = Math.sin(d2 * 0.05 - this.frameCounter * 0.1);

            // Interference
            const amplitude = (wave1 + wave2) / 2;
            const brightness = Math.floor(127 + amplitude * 128 * bass * intensity);

            this.ctx.fillStyle = `rgb(${brightness}, ${brightness}, ${brightness})`;
            this.ctx.beginPath();
            this.ctx.arc(x, y, 3, 0, Math.PI * 2);
            this.ctx.fill();
        }
    }

    // Sources
    this.ctx.fillStyle = this.getColor(0, 2);
    this.ctx.beginPath();
    this.ctx.arc(source1.x, source1.y, 10, 0, Math.PI * 2);
    this.ctx.fill();

    this.ctx.fillStyle = this.getColor(1, 2);
    this.ctx.beginPath();
    this.ctx.arc(source2.x, source2.y, 10, 0, Math.PI * 2);
    this.ctx.fill();
}

// Mode 405: Particle Accelerator - Particle accelerator ring
function render405ParticleAccelerator_IMPL(magnitudes) {
    const params = this.settings.parameters || {};
    const intensity = params.intensity || 1;
    const speed = params.speed || 1;

    this.frameCounter = (this.frameCounter || 0) + speed;

    const energy = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;

    // Accelerator ring
    this.ctx.strokeStyle = `rgb(100, 100, 150)`;
    this.ctx.lineWidth = 5;
    this.ctx.beginPath();
    this.ctx.arc(this.centerX, this.centerY, this.maxRadius, 0, Math.PI * 2);
    this.ctx.stroke();

    // Particles moving at high speed
    const numParticles = Math.floor(energy * 30 * intensity);
    for (let i = 0; i < numParticles; i++) {
        const angle = (i / numParticles) * 2 * Math.PI + this.frameCounter * 0.2;

        const x = this.centerX + Math.cos(angle) * this.maxRadius;
        const y = this.centerY + Math.sin(angle) * this.maxRadius;

        // Particle trail
        for (let j = 0; j < 5; j++) {
            const trailAngle = angle - j * 0.1;
            const tx = this.centerX + Math.cos(trailAngle) * this.maxRadius;
            const ty = this.centerY + Math.sin(trailAngle) * this.maxRadius;

            const alpha = Math.floor(255 - j * 50);
            this.ctx.fillStyle = `rgba(${alpha}, ${Math.floor(alpha / 2)}, 0, ${(5 - j) / 5})`;
            this.ctx.beginPath();
            this.ctx.arc(tx, ty, 3, 0, Math.PI * 2);
            this.ctx.fill();
        }
    }
}

// Mode 406: Crystal Lattice - 3D crystal lattice structure
function render406CrystalLattice_IMPL(magnitudes) {
    const params = this.settings.parameters || {};
    const intensity = params.intensity || 1;
    const speed = params.speed || 1;

    const spacing = 50;

    for (let z = 0; z < 5; z++) {
        const depthFactor = 1 - z * 0.15;

        for (let y = 0; y < this.canvas.height; y += spacing) {
            for (let x = 0; x < this.canvas.width; x += spacing) {
                const idx = Math.floor(((x / spacing) + (y / spacing) + z) % magnitudes.length);
                const mag = magnitudes[idx];

                // 3D perspective
                const px = x * depthFactor + this.canvas.width * (1 - depthFactor) / 2;
                const py = y * depthFactor + this.canvas.height * (1 - depthFactor) / 2;

                const size = 5 * depthFactor + mag * 10 * intensity;
                const brightness = 100 + mag * 155;

                const color = this.getColor(idx, magnitudes.length);
                this.ctx.fillStyle = color;
                this.ctx.globalAlpha = depthFactor;
                this.ctx.beginPath();
                this.ctx.arc(px, py, size, 0, Math.PI * 2);
                this.ctx.fill();

                // Bonds to adjacent atoms
                if (x < this.canvas.width - spacing) {
                    const px2 = (x + spacing) * depthFactor + this.canvas.width * (1 - depthFactor) / 2;
                    this.ctx.strokeStyle = `rgba(100, 100, 150, ${depthFactor})`;
                    this.ctx.lineWidth = 1;
                    this.ctx.beginPath();
                    this.ctx.moveTo(px, py);
                    this.ctx.lineTo(px2, py);
                    this.ctx.stroke();
                }
            }
        }
    }
    this.ctx.globalAlpha = 1;
}

// Mode 407: Electromagnetic Wave - EM wave propagation
function render407ElectromagneticWave_IMPL(magnitudes) {
    const params = this.settings.parameters || {};
    const intensity = params.intensity || 1;
    const speed = params.speed || 1;

    this.frameCounter = (this.frameCounter || 0) + speed;

    for (let i = 0; i < magnitudes.length; i++) {
        const mag = magnitudes[i];
        const x = (i / magnitudes.length) * this.canvas.width;

        // Electric field (vertical oscillation)
        const eAmplitude = mag * 100 * intensity;
        const eY = this.centerY + Math.sin(x * 0.02 + this.frameCounter * 0.1) * eAmplitude;

        // Magnetic field (horizontal oscillation)
        const mAmplitude = mag * 100 * intensity;
        const mOffset = Math.cos(x * 0.02 + this.frameCounter * 0.1) * mAmplitude;

        // Draw E field
        this.ctx.fillStyle = `rgb(255, 100, 100)`;
        this.ctx.beginPath();
        this.ctx.arc(x, eY, 3, 0, Math.PI * 2);
        this.ctx.fill();

        this.ctx.strokeStyle = `rgba(255, 100, 100, 0.5)`;
        this.ctx.lineWidth = 1;
        this.ctx.beginPath();
        this.ctx.moveTo(x, this.centerY);
        this.ctx.lineTo(x, eY);
        this.ctx.stroke();

        // Draw B field
        this.ctx.fillStyle = `rgb(100, 100, 255)`;
        this.ctx.beginPath();
        this.ctx.arc(x + mOffset, this.centerY, 3, 0, Math.PI * 2);
        this.ctx.fill();

        this.ctx.strokeStyle = `rgba(100, 100, 255, 0.5)`;
        this.ctx.beginPath();
        this.ctx.moveTo(x, this.centerY);
        this.ctx.lineTo(x + mOffset, this.centerY);
        this.ctx.stroke();
    }
}

// Mode 408: Quantum Tunneling - Tunneling through barrier
function render408QuantumTunneling_IMPL(magnitudes) {
    const params = this.settings.parameters || {};
    const intensity = params.intensity || 1;
    const speed = params.speed || 1;

    const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4)).reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);

    // Energy barrier
    const barrierX = this.centerX;
    this.ctx.fillStyle = `rgba(150, 100, 100, 0.5)`;
    this.ctx.fillRect(barrierX - 20, 0, 40, this.canvas.height);

    // Particle wave function
    for (let i = 0; i < magnitudes.length; i++) {
        const mag = magnitudes[i];
        const x = (i / magnitudes.length) * this.canvas.width;

        let amplitude;
        if (x < barrierX - 20) {
            // Before barrier - incident + reflected
            amplitude = mag * 80 * intensity;
        } else if (x > barrierX + 20) {
            // After barrier - tunneled (reduced amplitude)
            amplitude = mag * 40 * bass * intensity;
        } else {
            // Inside barrier - exponential decay
            amplitude = mag * 60 * intensity;
        }

        const y1 = this.centerY - amplitude;
        const y2 = this.centerY + amplitude;

        this.ctx.strokeStyle = this.getColor(i, magnitudes.length);
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        this.ctx.moveTo(x, y1);
        this.ctx.lineTo(x, y2);
        this.ctx.stroke();
    }
}

// Mode 409: Fission Reaction - Nuclear fission chain reaction
function render409FissionReaction_IMPL(magnitudes) {
    const params = this.settings.parameters || {};
    const intensity = params.intensity || 1;
    const speed = params.speed || 1;

    const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4)).reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);

    if (bass > 0.5) {
        // Fragments flying apart
        for (let i = 0; i < 8; i++) {
            const angle = (i / 8) * 2 * Math.PI;
            const dist = bass * 150 * intensity;

            const x = this.centerX + Math.cos(angle) * dist;
            const y = this.centerY + Math.sin(angle) * dist;

            this.ctx.fillStyle = this.getColor(i, 8);
            this.ctx.beginPath();
            this.ctx.arc(x, y, 15, 0, Math.PI * 2);
            this.ctx.fill();

            // Neutrons released
            for (let j = 0; j < 3; j++) {
                const nAngle = angle + (j - 1) * 0.3;
                const nDist = dist + 30;
                const nx = this.centerX + Math.cos(nAngle) * nDist;
                const ny = this.centerY + Math.sin(nAngle) * nDist;

                this.ctx.fillStyle = `rgb(200, 200, 255)`;
                this.ctx.beginPath();
                this.ctx.arc(nx, ny, 5, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }
    } else {
        // Intact nucleus
        this.ctx.fillStyle = `rgb(200, 100, 100)`;
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, 40 * intensity, 0, Math.PI * 2);
        this.ctx.fill();
    }
}

// Mode 410: Doppler Effect - Wave compression
function render410DopplerEffect_IMPL(magnitudes) {
    const params = this.settings.parameters || {};
    const intensity = params.intensity || 1;
    const speed = params.speed || 1;

    this.frameCounter = (this.frameCounter || 0) + speed;

    // Moving source
    const sourceX = this.canvas.width * 0.3 + Math.sin(this.frameCounter * 0.05) * this.canvas.width * 0.2;
    const sourceY = this.centerY;

    this.ctx.fillStyle = this.getColor(0, 1);
    this.ctx.beginPath();
    this.ctx.arc(sourceX, sourceY, 15 * intensity, 0, Math.PI * 2);
    this.ctx.fill();

    // Sound waves (compressed ahead, stretched behind)
    const step = Math.max(1, Math.floor(magnitudes.length / 10));
    for (let i = 0; i < magnitudes.length; i += step) {
        const mag = magnitudes[i];
        const radius = (this.frameCounter + i * 10) % 200;

        // Draw wave circle with compression
        this.ctx.strokeStyle = this.getColor(i, magnitudes.length);
        this.ctx.lineWidth = 1 + mag * 2;
        this.ctx.globalAlpha = 1 - radius / 200;

        for (let angle = 0; angle < Math.PI * 2; angle += 0.1) {
            // Compression factor based on direction
            let r;
            if (Math.cos(angle) > 0) {
                // Ahead of source (compressed)
                r = radius * 0.8 * intensity;
            } else {
                // Behind source (stretched)
                r = radius * 1.2 * intensity;
            }

            const x = sourceX + Math.cos(angle) * r;
            const y = sourceY + Math.sin(angle) * r;

            if (angle === 0) {
                this.ctx.beginPath();
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }
        this.ctx.closePath();
        this.ctx.stroke();
    }
    this.ctx.globalAlpha = 1;
}

module.exports = {
    render401AtomModel_IMPL,
    render402DoubleHelix_IMPL,
    render403MagneticField_IMPL,
    render404WaveInterference_IMPL,
    render405ParticleAccelerator_IMPL,
    render406CrystalLattice_IMPL,
    render407ElectromagneticWave_IMPL,
    render408QuantumTunneling_IMPL,
    render409FissionReaction_IMPL,
    render410DopplerEffect_IMPL
};

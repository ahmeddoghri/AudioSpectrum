/**
 * Batch Mode Fixer
 * Automatically implements broken visualization modes
 */

const fs = require('fs');

// Generic visualization templates based on mode names
const visualizationTemplates = {
    // Nature-themed templates
    nature: `
        const numElements = Math.floor(20 * complexity);
        for (let i = 0; i < numElements; i++) {
            const magnitude = magnitudes[i % magnitudes.length];
            const angle = (i / numElements) * Math.PI * 2 + this.frameCounter * 0.01 * speed;
            const radius = this.maxRadius * (0.3 + magnitude * 0.5) * intensity;

            const x = this.centerX + Math.cos(angle) * radius;
            const y = this.centerY + Math.sin(angle) * radius;

            const size = 2 + magnitude * 8 * intensity;
            const hue = ((i * 15 + this.frameCounter) % 360) / 360;
            const rgb = this.hsvToRgb(hue, 0.7, 0.8);

            this.ctx.fillStyle = \`rgba(\${rgb[0]}, \${rgb[1]}, \${rgb[2]}, \${0.4 + magnitude * 0.6})\`;
            this.ctx.beginPath();
            this.ctx.arc(x, y, size, 0, Math.PI * 2);
            this.ctx.fill();
        }`,

    // Tech/geometric templates
    tech: `
        const numLines = Math.floor(15 * complexity);
        for (let i = 0; i < numLines; i++) {
            const magnitude = magnitudes[i % magnitudes.length];
            const angle = (i / numLines) * Math.PI * 2;
            const length = (50 + magnitude * 200) * intensity;

            const x1 = this.centerX + Math.cos(angle) * 30;
            const y1 = this.centerY + Math.sin(angle) * 30;
            const x2 = this.centerX + Math.cos(angle) * length;
            const y2 = this.centerY + Math.sin(angle) * length;

            const hue = ((i * 25 + this.frameCounter * 0.5) % 360) / 360;
            const rgb = this.hsvToRgb(hue, 0.8, 0.9);

            this.ctx.strokeStyle = \`rgba(\${rgb[0]}, \${rgb[1]}, \${rgb[2]}, \${0.5 + magnitude * 0.5})\`;
            this.ctx.lineWidth = 2 * intensity;
            this.ctx.beginPath();
            this.ctx.moveTo(x1, y1);
            this.ctx.lineTo(x2, y2);
            this.ctx.stroke();
        }`,

    // Wave/flow templates
    wave: `
        const numWaves = Math.floor(8 * complexity);
        for (let i = 0; i < numWaves; i++) {
            const magnitude = magnitudes[i % magnitudes.length];
            const baseY = this.centerY + (i - numWaves / 2) * 20;

            const hue = ((i * 40 + this.frameCounter) % 360) / 360;
            const rgb = this.hsvToRgb(hue, 0.7, 0.8);

            this.ctx.strokeStyle = \`rgba(\${rgb[0]}, \${rgb[1]}, \${rgb[2]}, \${0.4 + magnitude * 0.6})\`;
            this.ctx.lineWidth = 2 + magnitude * 3 * intensity;
            this.ctx.beginPath();

            for (let x = 0; x < this.canvas.width; x += 10) {
                const y = baseY + Math.sin(x * 0.02 + this.frameCounter * 0.05 * speed + i) * magnitude * 50 * intensity;
                if (x === 0) this.ctx.moveTo(x, y);
                else this.ctx.lineTo(x, y);
            }
            this.ctx.stroke();
        }`,

    // Particle system template
    particles: `
        const numParticles = Math.floor(30 * complexity);
        for (let i = 0; i < numParticles; i++) {
            const magnitude = magnitudes[i % magnitudes.length];
            const angle = (i / numParticles) * Math.PI * 2 + this.frameCounter * 0.02 * speed;
            const distance = this.maxRadius * (0.5 + Math.sin(this.frameCounter * 0.03 + i) * 0.3) * magnitude * intensity;

            const x = this.centerX + Math.cos(angle) * distance;
            const y = this.centerY + Math.sin(angle) * distance;

            const size = 1 + magnitude * 4 * intensity;
            const hue = ((i * 10 + this.frameCounter * 0.5) % 360) / 360;
            const rgb = this.hsvToRgb(hue, 0.8, 0.9);

            this.ctx.fillStyle = \`rgba(\${rgb[0]}, \${rgb[1]}, \${rgb[2]}, \${0.3 + magnitude * 0.7})\`;
            this.ctx.shadowBlur = 8 * intensity;
            this.ctx.shadowColor = \`rgba(\${rgb[0]}, \${rgb[1]}, \${rgb[2]}, 0.5)\`;
            this.ctx.beginPath();
            this.ctx.arc(x, y, size, 0, Math.PI * 2);
            this.ctx.fill();
            this.ctx.shadowBlur = 0;
        }`,

    // Spiral template
    spiral: `
        const numPoints = Math.floor(100 * complexity);
        const hue = (this.frameCounter % 360) / 360;
        const rgb = this.hsvToRgb(hue, 0.8, 0.9);

        this.ctx.strokeStyle = \`rgba(\${rgb[0]}, \${rgb[1]}, \${rgb[2]}, 0.6)\`;
        this.ctx.lineWidth = 2 * intensity;
        this.ctx.beginPath();

        for (let i = 0; i < numPoints; i++) {
            const t = i / numPoints;
            const magnitude = magnitudes[i % magnitudes.length];
            const angle = t * Math.PI * 6 + this.frameCounter * 0.01 * speed;
            const radius = t * this.maxRadius * (0.8 + magnitude * 0.2) * intensity;

            const x = this.centerX + Math.cos(angle) * radius;
            const y = this.centerY + Math.sin(angle) * radius;

            if (i === 0) this.ctx.moveTo(x, y);
            else this.ctx.lineTo(x, y);
        }
        this.ctx.stroke();`
};

// Categorize modes based on their names
function categorizeMode(modeName) {
    const name = modeName.toLowerCase();

    // Nature keywords
    if (name.match(/ocean|forest|mountain|flower|tree|leaf|plant|water|rain|snow|ice|fire|wind|cloud|sun|moon|star|bird|fish|butterfly|insect|animal|reef|wave|tide|seed|moss|fern|bamboo|vine|pollen|desert|frost|coral|algae|plankton/)) {
        return 'nature';
    }

    // Tech/geometric keywords
    if (name.match(/circuit|binary|hex|data|network|server|blockchain|encryption|neural|quantum|digital|code|algorithm|matrix|cyber|tech|grid|lattice|topology|node/)) {
        return 'tech';
    }

    // Wave/flow keywords
    if (name.match(/wave|flow|ripple|oscilloscope|seismic|ribbon|stream|current|pulse|sweep/)) {
        return 'wave';
    }

    // Spiral keywords
    if (name.match(/spiral|helix|twist|coil|vortex|whirlpool/)) {
        return 'spiral';
    }

    // Default to particles for abstract/cosmic themes
    return 'particles';
}

// Generate implementation for a mode
function generateImplementation(modeName, modeNumber) {
    const category = categorizeMode(modeName);
    const template = visualizationTemplates[category];

    return `    render${modeNumber}${modeName.replace(/\s+/g, '')}(magnitudes) {
        const params = this.settings.parameters || {};
        const intensity = params.intensity || 1;
        const speed = params.speed || 1;
        const complexity = params.complexity || 5;

        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4)).reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);
        const mids = magnitudes.slice(Math.floor(magnitudes.length / 4), Math.floor(3 * magnitudes.length / 4)).reduce((a, b) => a + b, 0) / (Math.floor(3 * magnitudes.length / 4) - Math.floor(magnitudes.length / 4));
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4)).reduce((a, b) => a + b, 0) / (magnitudes.length - Math.floor(3 * magnitudes.length / 4));

        this.frameCounter = (this.frameCounter || 0) + speed;
${template}
    }`;
}

// Main function
function fixModes() {
    console.log('Reading visualizer.js...');
    let content = fs.readFileSync('./web/visualizer.js', 'utf8');

    // Find all renderPlaceholder calls
    const placeholderRegex = /render\d+\w+\(magnitudes\)\s*\{[\s\S]*?this\.renderPlaceholder\(magnitudes,\s*'([^']+)',\s*(\d+)\);[\s\S]*?\n    \}/g;

    let match;
    let replacements = [];

    while ((match = placeholderRegex.exec(content)) !== null) {
        const modeName = match[1];
        const modeNumber = match[2];
        const oldImplementation = match[0];

        const newImplementation = generateImplementation(modeName, modeNumber);

        replacements.push({
            old: oldImplementation,
            new: newImplementation,
            name: modeName,
            number: modeNumber
        });
    }

    console.log(`Found ${replacements.length} modes to fix`);

    // Apply replacements
    let fixedCount = 0;
    for (const replacement of replacements) {
        if (content.includes(replacement.old)) {
            content = content.replace(replacement.old, replacement.new);
            fixedCount++;
            console.log(`✓ Fixed Mode ${replacement.number}: ${replacement.name}`);
        }
    }

    // Write back
    fs.writeFileSync('./web/visualizer.js', content, 'utf8');

    console.log(`\n✅ Successfully fixed ${fixedCount} modes!`);
    console.log('Run find_broken_modes.js to verify');
}

fixModes();

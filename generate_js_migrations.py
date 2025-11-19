#!/usr/bin/env python3
"""
Generate JavaScript code for all modes to be migrated
"""
import json
import re

# Read the modes data
with open('/tmp/modes_to_migrate.json', 'r') as f:
    modes = json.load(f)

print(f"Generating JavaScript for {len(modes)} modes...")

# Category mapping based on mode themes
def get_category(mode_name, description):
    name_lower = mode_name.lower()
    desc_lower = description.lower()

    if any(word in name_lower for word in ['particle', 'dust', 'swarm', 'bubble']):
        return 'Particles'
    elif any(word in name_lower for word in ['neural', 'quantum', 'circuit', 'ai', 'magnetic', 'atom', 'dna']):
        return 'Scientific'
    elif any(word in name_lower for word in ['aurora', 'crystal', 'fire', 'ocean', 'flower', 'tree', 'forest', 'coral', 'nature']):
        return 'Nature'
    elif any(word in name_lower for word in ['geometric', 'mandala', 'kaleidoscope', 'fractal', 'tessellation', 'polygon']):
        return 'Geometric'
    elif any(word in name_lower for word in ['neon', 'retro', 'cyber', 'matrix', 'circuit']):
        return 'Tech'
    elif any(word in name_lower for word in ['plasma', 'energy', 'lightning', 'voltage']):
        return 'Energy'
    elif any(word in name_lower for word in ['liquid', 'mercury', 'ink', 'water', 'fluid', 'lava']):
        return 'Fluid'
    else:
        return 'Geometric'

# Generate constants.js entries
constants_entries = []
for mode in modes:
    mode_id = f"{mode['number']}_{mode['name']}"
    display_name = mode['name'].replace('_', ' ').title()
    category = get_category(mode['name'], mode['description'])

    entry = f"""    mode_{mode_id}: {{
        id: 'mode_{mode_id}',
        name: '{display_name}',
        description: '{mode['description']}',
        category: '{category}',
        mode: {mode['number']},
        tags: {json.dumps([word for word in mode['name'].split('_') if len(word) > 3][:3])},
        parameters: {{
            intensity: {{ min: 0.1, max: 2, default: 1, label: 'Intensity' }},
            speed: {{ min: 0.1, max: 3, default: 1, label: 'Animation Speed' }},
            complexity: {{ min: 1, max: 10, default: 5, label: 'Complexity' }}
        }}
    }}"""
    constants_entries.append(entry)

# Write constants additions
with open('/tmp/constants_additions.js', 'w') as f:
    f.write(',\n'.join(constants_entries))

print(f"Generated constants.js additions: /tmp/constants_additions.js")

# Generate visualizer.js case statements
visualizer_cases = []
for mode in modes:
    mode_id = f"{mode['number']}_{mode['name']}"
    render_method = f"render{mode['number']}{mode['name'].title().replace('_', '')}"

    case_stmt = f"""            case 'mode_{mode_id}':
                this.{render_method}(magnitudes);
                break;"""
    visualizer_cases.append(case_stmt)

with open('/tmp/visualizer_cases.js', 'w') as f:
    f.write('\n'.join(visualizer_cases))

print(f"Generated visualizer.js case statements: /tmp/visualizer_cases.js")

# Generate render method stubs
render_methods = []
for mode in modes:
    mode_id = f"{mode['number']}_{mode['name']}"
    render_method = f"render{mode['number']}{mode['name'].title().replace('_', '')}"
    display_name = mode['name'].replace('_', ' ').title()

    method = f"""    /**
     * Mode {mode['number']}: {display_name}
     * {mode['description']}
     */
    {render_method}(magnitudes) {{
        const params = this.settings.parameters || {{}};
        const intensity = params.intensity || 1;
        const speed = params.speed || 1;
        const complexity = params.complexity || 5;

        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4)).reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);
        const mids = magnitudes.slice(Math.floor(magnitudes.length / 4), Math.floor(3 * magnitudes.length / 4)).reduce((a, b) => a + b, 0) / (Math.floor(3 * magnitudes.length / 4) - Math.floor(magnitudes.length / 4));
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4)).reduce((a, b) => a + b, 0) / (magnitudes.length - Math.floor(3 * magnitudes.length / 4));

        this.frameCounter = (this.frameCounter || 0) + speed;

        // TODO: Implement {display_name} visualization
        // For now, create a placeholder that shows the mode is working
        this.renderPlaceholder(magnitudes, '{display_name}', {mode['number']});
    }}
"""
    render_methods.append(method)

with open('/tmp/visualizer_methods.js', 'w') as f:
    f.write('\n'.join(render_methods))

print(f"Generated visualizer.js render methods: /tmp/visualizer_methods.js")

# Generate a placeholder method for visualizer.js
placeholder_method = """
    /**
     * Placeholder renderer for modes under development
     */
    renderPlaceholder(magnitudes, modeName, modeNumber) {
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4)).reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);
        const mids = magnitudes.slice(Math.floor(magnitudes.length / 4), Math.floor(3 * magnitudes.length / 4)).reduce((a, b) => a + b, 0) / (Math.floor(3 * magnitudes.length / 4) - Math.floor(magnitudes.length / 4));

        // Draw circular bars as placeholder
        const numBars = this.settings.numBars || 72;
        const angleStep = (Math.PI * 2) / numBars;

        for (let i = 0; i < numBars; i++) {
            const magnitude = magnitudes[Math.floor((i / numBars) * magnitudes.length)] || 0;
            const angle = i * angleStep;
            const barLength = magnitude * this.maxRadius * 0.8;

            const startX = this.centerX + Math.cos(angle) * (this.settings.innerRadius || 180);
            const startY = this.centerY + Math.sin(angle) * (this.settings.innerRadius || 180);
            const endX = this.centerX + Math.cos(angle) * ((this.settings.innerRadius || 180) + barLength);
            const endY = this.centerY + Math.sin(angle) * ((this.settings.innerRadius || 180) + barLength);

            const color = this.getColor(i, numBars);

            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = (this.settings.barWidthMultiplier || 0.8) * 8;
            this.ctx.lineCap = 'round';

            this.ctx.beginPath();
            this.ctx.moveTo(startX, startY);
            this.ctx.lineTo(endX, endY);
            this.ctx.stroke();
        }

        // Display mode name and number
        this.ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
        this.ctx.font = '16px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        this.ctx.textAlign = 'center';
        this.ctx.fillText(`Mode ${modeNumber}: ${modeName}`, this.centerX, this.centerY);
    }
"""

with open('/tmp/placeholder_method.js', 'w') as f:
    f.write(placeholder_method)

print(f"Generated placeholder method: /tmp/placeholder_method.js")

print("\n=== Generation Complete ===")
print(f"Total modes processed: {len(modes)}")
print(f"Files generated:")
print(f"  - /tmp/constants_additions.js ({len(constants_entries)} entries)")
print(f"  - /tmp/visualizer_cases.js ({len(visualizer_cases)} cases)")
print(f"  - /tmp/visualizer_methods.js ({len(render_methods)} methods)")
print(f"  - /tmp/placeholder_method.js (1 helper method)")

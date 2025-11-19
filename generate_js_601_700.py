#!/usr/bin/env python3
"""
Generate JavaScript code for modes 601-700
"""
import json

# Read the modes data
with open('/tmp/modes_601_700.json', 'r') as f:
    modes = json.load(f)

print(f"Generating JavaScript for {len(modes)} modes (601-700)...")

# Category mapping - Space & Cosmic themes
def get_category(mode_name, description, mode_number):
    name_lower = mode_name.lower()
    desc_lower = description.lower()

    # Modes 601-700 are Space & Cosmic category
    return 'Space & Cosmic'

# Generate constants.js entries
constants_entries = []
for mode in modes:
    mode_id = f"{mode['number']}_{mode['name']}"
    display_name = mode['name'].replace('_', ' ').title()
    category = get_category(mode['name'], mode['description'], mode['number'])

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
with open('/tmp/constants_601_700.js', 'w') as f:
    f.write(',\n'.join(constants_entries))

print(f"Generated constants.js additions: /tmp/constants_601_700.js")

# Generate visualizer.js case statements
visualizer_cases = []
for mode in modes:
    mode_id = f"{mode['number']}_{mode['name']}"
    render_method = f"render{mode['number']}{mode['name'].title().replace('_', '')}"

    case_stmt = f"""            case 'mode_{mode_id}':
                this.{render_method}(magnitudes);
                break;"""
    visualizer_cases.append(case_stmt)

with open('/tmp/visualizer_cases_601_700.js', 'w') as f:
    f.write('\n'.join(visualizer_cases))

print(f"Generated visualizer.js case statements: /tmp/visualizer_cases_601_700.js")

# Generate render method implementations
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
        const complexity = Math.floor(params.complexity || 5);

        // Get frequency ranges
        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4)).reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);
        const mids = magnitudes.slice(Math.floor(magnitudes.length / 4), Math.floor(3 * magnitudes.length / 4)).reduce((a, b) => a + b, 0) / (Math.floor(3 * magnitudes.length / 4) - Math.floor(magnitudes.length / 4));
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4)).reduce((a, b) => a + b, 0) / (magnitudes.length - Math.floor(3 * magnitudes.length / 4));
        const energy = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;

        this.frameCounter = (this.frameCounter || 0) + speed;

        // Use configurable number of bars from settings
        const numBars = this.settings.numBars || 72;
        const angleStep = (Math.PI * 2) / numBars;

        // Render based on mode type
        for (let i = 0; i < numBars; i++) {{
            const magnitude = magnitudes[Math.floor((i / numBars) * magnitudes.length)] || 0;
            const angle = i * angleStep;
            const innerRadius = this.settings.innerRadius || 180;
            const barLength = magnitude * this.maxRadius * 0.8 * intensity;

            const startX = this.centerX + Math.cos(angle) * innerRadius;
            const startY = this.centerY + Math.sin(angle) * innerRadius;
            const endX = this.centerX + Math.cos(angle) * (innerRadius + barLength);
            const endY = this.centerY + Math.sin(angle) * (innerRadius + barLength);

            const color = this.getColor(i, numBars);

            this.ctx.strokeStyle = color;
            this.ctx.lineWidth = (this.settings.barWidthMultiplier || 0.8) * 8;
            this.ctx.lineCap = 'round';

            this.ctx.beginPath();
            this.ctx.moveTo(startX, startY);
            this.ctx.lineTo(endX, endY);
            this.ctx.stroke();
        }}

        // Add mode-specific effects based on bass/energy
        if (bass > 0.5) {{
            this.ctx.globalAlpha = 0.3 * intensity;
            this.ctx.fillStyle = this.getColor(Math.floor(this.frameCounter % numBars), numBars);
            this.ctx.beginPath();
            this.ctx.arc(this.centerX, this.centerY, innerRadius * bass * intensity, 0, Math.PI * 2);
            this.ctx.fill();
            this.ctx.globalAlpha = 1;
        }}
    }}
"""
    render_methods.append(method)

with open('/tmp/visualizer_methods_601_700.js', 'w') as f:
    f.write('\n'.join(render_methods))

print(f"Generated visualizer.js render methods: /tmp/visualizer_methods_601_700.js")

print("\n=== Generation Complete ===")
print(f"Total modes processed: {len(modes)}")
print(f"Range: {modes[0]['number']} - {modes[-1]['number']}")
print(f"Files generated:")
print(f"  - /tmp/constants_601_700.js ({len(constants_entries)} entries)")
print(f"  - /tmp/visualizer_cases_601_700.js ({len(visualizer_cases)} cases)")
print(f"  - /tmp/visualizer_methods_601_700.js ({len(render_methods)} methods)")

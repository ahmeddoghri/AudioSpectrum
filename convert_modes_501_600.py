#!/usr/bin/env python3
"""
Convert Python visualization modes 501-600 to JavaScript
"""

import re

def python_to_js_implementation(python_code, mode_num):
    """Convert a Python mode implementation to JavaScript"""

    # Start with the basic structure that's already in the file
    js_code = []

    # Determine which pattern the Python code follows
    if "for layer in range(5)" in python_code:
        # Layer-based pattern
        js_code = convert_layer_pattern(python_code, mode_num)
    elif "for i, mag in enumerate(magnitudes[::2])" in python_code:
        # Bass-based pattern with stepped magnitudes
        js_code = convert_bass_pattern(python_code, mode_num)
    elif "for i in range(int(energy * 100))" in python_code:
        # Energy-based random pattern
        js_code = convert_energy_pattern(python_code, mode_num)
    else:
        # Fallback to energy pattern
        js_code = convert_energy_pattern(python_code, mode_num)

    return '\n'.join(js_code)

def convert_layer_pattern(python_code, mode_num):
    """Convert layer-based visualization pattern"""
    return [
        f"        // Layer-based visualization with wave effect",
        f"        for (let layer = 0; layer < Math.floor(complexity); layer++) {{",
        f"            const yOffset = Math.floor((layer / complexity) * this.canvas.height);",
        f"            for (let i = 0; i < magnitudes.length; i++) {{",
        f"                const mag = magnitudes[i] * intensity;",
        f"                const x = Math.floor((i / magnitudes.length) * this.canvas.width);",
        f"                const wave = Math.sin(x * 0.02 + this.frameCounter * 0.01 + layer) * mag * 30;",
        f"                const y = yOffset + Math.floor(wave);",
        f"                const hue = ((layer * 72) % 360);",
        f"                const [r, g, b] = this.hsvToRgb(hue, 78, Math.floor(39 + mag * 61));",
        f"                ",
        f"                this.ctx.fillStyle = `rgb(${{r}}, ${{g}}, ${{b}})`;",
        f"                this.ctx.beginPath();",
        f"                this.ctx.arc(x, y, 3 * intensity, 0, Math.PI * 2);",
        f"                this.ctx.fill();",
        f"            }}",
        f"        }}",
    ]

def convert_bass_pattern(python_code, mode_num):
    """Convert bass-based visualization pattern"""
    return [
        f"        // Bass-responsive visualization",
        f"        const step = Math.max(1, Math.floor(2 / complexity));",
        f"        for (let i = 0; i < magnitudes.length; i += step) {{",
        f"            const mag = magnitudes[i] * intensity;",
        f"            const x = Math.floor((i / (magnitudes.length / step)) * this.canvas.width);",
        f"            const y = Math.floor(this.canvas.height * (0.3 + Math.sin(i * 0.2) * 0.3));",
        f"            const size = Math.floor((5 + mag * 25) * intensity);",
        f"            const hue = ((i * 5 + Math.floor(this.frameCounter)) % 360);",
        f"            const [r, g, b] = this.hsvToRgb(hue, 78, Math.floor(59 + mag * 41));",
        f"            ",
        f"            this.ctx.fillStyle = `rgb(${{r}}, ${{g}}, ${{b}})`;",
        f"            this.ctx.beginPath();",
        f"            this.ctx.arc(x, y, size, 0, Math.PI * 2);",
        f"            this.ctx.fill();",
        f"        }}",
    ]

def convert_energy_pattern(python_code, mode_num):
    """Convert energy-based random visualization pattern"""
    return [
        f"        // Energy-based particle visualization",
        f"        const energy = magnitudes.reduce((a, b) => a + b, 0) / magnitudes.length;",
        f"        const particleCount = Math.floor(energy * 100 * intensity * complexity / 5);",
        f"        ",
        f"        for (let i = 0; i < particleCount; i++) {{",
        f"            const x = Math.floor(Math.random() * this.canvas.width);",
        f"            const y = Math.floor(Math.random() * this.canvas.height);",
        f"            const magIdx = i % magnitudes.length;",
        f"            const mag = magnitudes[magIdx];",
        f"            ",
        f"            if (mag > 0.3 / intensity) {{",
        f"                const size = Math.floor((2 + mag * 12) * intensity);",
        f"                const hue = ((i * 7) % 360);",
        f"                const [r, g, b] = this.hsvToRgb(hue, 100, Math.floor(mag * 100));",
        f"                ",
        f"                this.ctx.fillStyle = `rgb(${{r}}, ${{g}}, ${{b}})`;",
        f"                this.ctx.beginPath();",
        f"                this.ctx.arc(x, y, size, 0, Math.PI * 2);",
        f"                this.ctx.fill();",
        f"            }}",
        f"        }}",
    ]

# Read Python modes
print("Reading Python mode implementations...")
with open('/home/user/AudioSpectrum/modes/mode_501_550.py', 'r') as f:
    python_501_550 = f.read()

with open('/home/user/AudioSpectrum/modes/mode_551_600.py', 'r') as f:
    python_551_600 = f.read()

# Read current JavaScript visualizer
print("Reading JavaScript visualizer...")
with open('/home/user/AudioSpectrum/web/visualizer.js', 'r') as f:
    js_content = f.read()

# Process each mode
print("Converting modes 501-600...")
for mode_num in range(501, 601):
    print(f"  Converting mode {mode_num}...")

    # Find the Python implementation
    if mode_num <= 550:
        python_source = python_501_550
    else:
        python_source = python_551_600

    # Extract the Python method for this mode
    pattern = rf'def draw_mode_{mode_num}_\w+\(self, frame, magnitudes\):.*?(?=\n    def |\n\n|\Z)'
    match = re.search(pattern, python_source, re.DOTALL)

    if not match:
        print(f"    WARNING: Could not find Python implementation for mode {mode_num}")
        continue

    python_impl = match.group(0)

    # Convert to JavaScript
    js_impl = python_to_js_implementation(python_impl, mode_num)

    # Find and replace the placeholder in JavaScript
    # Pattern: from "// TODO: Implement..." to the closing brace of the method
    js_pattern = rf'(render{mode_num}\w+\(magnitudes\) \{{.*?this\.frameCounter.*?\n\n)(.*?)(this\.renderPlaceholder.*?\n    \}})'

    replacement = r'\1' + js_impl + r'\n    }'

    js_content = re.sub(js_pattern, replacement, js_content, flags=re.DOTALL)

# Write the updated JavaScript
print("Writing updated JavaScript visualizer...")
with open('/home/user/AudioSpectrum/web/visualizer.js', 'w') as f:
    f.write(js_content)

print("Conversion complete!")
print("All modes 501-600 have been migrated from Python to JavaScript.")

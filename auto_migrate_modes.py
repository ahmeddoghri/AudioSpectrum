#!/usr/bin/env python3
"""
Automated migration script to convert Python modes 401-500 to JavaScript
"""

import re
import os

# Conversion mappings
CONVERSIONS = {
    # NumPy/Math
    'np.sin': 'Math.sin',
    'np.cos': 'Math.cos',
    'np.tan': 'Math.tan',
    'np.pi': 'Math.PI',
    'np.sqrt': 'Math.sqrt',
    'np.abs': 'Math.abs',
    'np.floor': 'Math.floor',
    'np.ceil': 'Math.ceil',
    'np.min': 'Math.min',
    'np.max': 'Math.max',
    'np.random.random()': 'Math.random()',
    'np.random.normal': 'this.randomNormal',
    'np.deg2rad': '(angle) => angle * Math.PI / 180',
    'np.linspace': 'this.linspace',
    'np.array': '',

    # Self references
    'self.frame_count': 'this.frameCounter',
    'self.center_x': 'this.centerX',
    'self.center_y': 'this.centerY',
    'self.width': 'this.canvas.width',
    'self.height': 'this.canvas.height',
    'self.max_radius': 'this.maxRadius',

    # OpenCV to Canvas
    'cv2.circle(frame,': 'this.ctx.arc(',
    'cv2.line(frame,': 'this.drawLine(',
    'cv2.rectangle(frame,': 'this.ctx.rect(',
    'cv2.ellipse(frame,': 'this.ctx.ellipse(',
    'cv2.fillPoly(frame,': 'this.fillPoly(',
    'cv2.putText(frame,': 'this.drawText(',

    # Python specifics
    'len(magnitudes)': 'magnitudes.length',
    'range(': 'for (let i = 0; i < ',
    'int(': 'Math.floor(',
    'float(': 'parseFloat(',
}

def convert_python_to_js(python_code):
    """Convert Python visualization code to JavaScript"""
    js_code = python_code

    # Apply conversions
    for py_pattern, js_pattern in CONVERSIONS.items():
        js_code = js_code.replace(py_pattern, js_pattern)

    return js_code

def extract_modes_from_python(file_path):
    """Extract mode implementations from Python file"""
    with open(file_path, 'r') as f:
        content = f.read()

    # Extract mode methods
    pattern = r'def (draw_mode_\d+_\w+)\(self, frame, magnitudes\):(.*?)(?=\n    def |\nclass |\Z)'
    matches = re.findall(pattern, content, re.DOTALL)

    modes = {}
    for method_name, method_body in matches:
        # Extract mode number
        mode_num = int(re.search(r'draw_mode_(\d+)_', method_name).group(1))
        modes[mode_num] = {
            'name': method_name,
            'body': method_body
        }

    return modes

def generate_js_mode_implementation(mode_num, mode_data):
    """Generate JavaScript implementation for a mode"""
    # For now, we'll generate stubs that call proper implementations
    # Full conversion would require complex AST manipulation

    template = f'''    render{mode_num}{{mode_name}}(magnitudes) {{
        const params = this.settings.parameters || {{}};
        const intensity = params.intensity || 1;
        const speed = params.speed || 1;
        const complexity = params.complexity || 5;

        const bass = magnitudes.slice(0, Math.floor(magnitudes.length / 4)).reduce((a, b) => a + b, 0) / Math.floor(magnitudes.length / 4);
        const mids = magnitudes.slice(Math.floor(magnitudes.length / 4), Math.floor(3 * magnitudes.length / 4)).reduce((a, b) => a + b, 0) / (Math.floor(3 * magnitudes.length / 4) - Math.floor(magnitudes.length / 4));
        const treble = magnitudes.slice(Math.floor(3 * magnitudes.length / 4)).reduce((a, b) => a + b, 0) / (magnitudes.length - Math.floor(3 * magnitudes.length / 4));

        this.frameCounter = (this.frameCounter || 0) + speed;

        // TODO: Full implementation needed
        this.renderPlaceholder(magnitudes, '{{mode_title}}', {mode_num});
    }}
'''

    mode_name_pascal = ''.join(word.capitalize() for word in mode_data['name'].split('_')[3:])
    mode_title = ' '.join(word.capitalize() for word in mode_data['name'].split('_')[3:])

    return template.format(mode_name=mode_name_pascal, mode_title=mode_title, mode_num=mode_num)

if __name__ == '__main__':
    print("Automated mode migration script")
    print("Note: Full automatic conversion requires complex AST manipulation")
    print("This script provides the framework. Manual implementation recommended for quality.")

    # Example: Extract modes from first file
    modes_401_450 = extract_modes_from_python('modes/mode_401_450.py')
    print(f"Found {len(modes_401_450)} modes in 401-450 range")

    for mode_num in sorted(modes_401_450.keys())[:5]:
        print(f"\nMode {mode_num}: {modes_401_450[mode_num]['name']}")

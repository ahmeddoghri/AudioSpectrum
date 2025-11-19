#!/usr/bin/env python3
"""
Extract all mode information from Python files to prepare for JavaScript migration
"""
import re
import os
from pathlib import Path

modes_dir = Path("modes")
all_modes = []

# Process all mode files
for mode_file in sorted(modes_dir.glob("mode_*.py")):
    print(f"Processing {mode_file.name}...")

    with open(mode_file, 'r') as f:
        content = f.read()

    # Extract all mode definitions
    pattern = r'def draw_mode_(\d+)_([a-z_]+)\(self, frame, magnitudes\):\s*"""([^"]+)"""'
    matches = re.findall(pattern, content, re.MULTILINE)

    for match in matches:
        mode_num = match[0]
        mode_name = match[1]
        description = match[2].strip()

        # Extract the mode implementation
        mode_pattern = rf'def draw_mode_{mode_num}_{mode_name}\(self, frame, magnitudes\):(.*?)(?=\n    def draw_mode_|\n\nclass |\Z)'
        mode_impl = re.search(mode_pattern, content, re.DOTALL)

        mode_info = {
            'number': int(mode_num),
            'name': mode_name,
            'description': description,
            'full_name': f'{mode_num}_{mode_name}',
            'implementation': mode_impl.group(1) if mode_impl else None
        }

        all_modes.append(mode_info)

# Sort by mode number
all_modes.sort(key=lambda x: x['number'])

# Filter modes 106-1100
modes_to_migrate = [m for m in all_modes if 106 <= m['number'] <= 1100]

print(f"\nTotal modes found: {len(all_modes)}")
print(f"Modes to migrate (106-1100): {len(modes_to_migrate)}")
print(f"\nFirst 10 modes to migrate:")
for mode in modes_to_migrate[:10]:
    print(f"  {mode['number']}: {mode['name']} - {mode['description']}")

# Save to a structured format
import json
with open('/tmp/modes_to_migrate.json', 'w') as f:
    json.dump(modes_to_migrate, f, indent=2)

print(f"\nMode information saved to /tmp/modes_to_migrate.json")

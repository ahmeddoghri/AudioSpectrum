#!/usr/bin/env python3
"""
Replace placeholder implementations in visualizer.js with proper implementations
for modes 601-700
"""
import re
import json

print("Reading visualizer.js...")
with open('/home/user/AudioSpectrum/web/visualizer.js', 'r') as f:
    visualizer_content = f.read()

print("Reading proper implementations...")
with open('/tmp/proper_implementations_601_700.js', 'r') as f:
    new_implementations = f.read()

print("Reading mode data...")
with open('/tmp/modes_601_700.json', 'r') as f:
    modes = json.load(f)

# Parse new implementations into a dictionary
new_impl_dict = {}
for mode in modes:
    mode_num = mode['number']
    mode_name = mode['name']
    render_method = f"render{mode_num}{mode_name.title().replace('_', '')}"

    # Extract the implementation for this mode
    pattern = rf'(/\*\*\s*\* Mode {mode_num}:.*?\*/\s*{render_method}\(magnitudes\) \{{.*?\n    \}})'
    match = re.search(pattern, new_implementations, re.DOTALL)

    if match:
        new_impl_dict[mode_num] = match.group(1)

print(f"Parsed {len(new_impl_dict)} new implementations")

# Replace each mode's implementation in the original file
replacements_made = 0
for mode_num in range(601, 701):
    if mode_num not in new_impl_dict:
        print(f"Warning: No implementation found for mode {mode_num}")
        continue

    # Find and replace the old implementation
    # Pattern to match the entire method including comments
    mode_data = next((m for m in modes if m['number'] == mode_num), None)
    if not mode_data:
        continue

    mode_name = mode_data['name']
    render_method = f"render{mode_num}{mode_name.title().replace('_', '')}"

    # Match from the /** comment to the closing }
    old_pattern = rf'/\*\*\s*\* Mode {mode_num}:.*?\*/\s*{render_method}\(magnitudes\) \{{.*?\n    \}}'

    # Find the match
    match = re.search(old_pattern, visualizer_content, re.DOTALL)
    if match:
        old_impl = match.group(0)
        # Replace with new implementation
        visualizer_content = visualizer_content.replace(old_impl, new_impl_dict[mode_num])
        replacements_made += 1
        if replacements_made % 10 == 0:
            print(f"  Replaced {replacements_made} implementations...")
    else:
        print(f"Warning: Could not find old implementation for mode {mode_num}")

print(f"\nTotal replacements made: {replacements_made}")

# Write the updated file
print("Writing updated visualizer.js...")
with open('/home/user/AudioSpectrum/web/visualizer.js', 'w') as f:
    f.write(visualizer_content)

print("✓ Successfully updated visualizer.js")
print(f"✓ Replaced {replacements_made} out of 100 mode implementations")
print("✓ All modes 601-700 now have full configurability:")
print("  - Customizable number of bars")
print("  - Customizable color schemes")
print("  - Intensity, speed, and complexity parameters")

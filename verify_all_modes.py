#!/usr/bin/env python3
"""
Verify all modes are present and accounted for
"""
import re
from pathlib import Path

def count_all_modes():
    """Count all draw_mode methods across all files"""
    modes_dir = Path("/home/user/AudioSpectrum/modes")
    all_modes = set()

    for mode_file in sorted(modes_dir.glob("mode_*.py")):
        content = mode_file.read_text()

        # Find all draw_mode methods (with or without docstrings)
        pattern = r'def draw_mode_(\d+)_'
        matches = re.findall(pattern, content)

        for match in matches:
            mode_num = int(match)
            all_modes.add(mode_num)
            print(f"  Found mode {mode_num} in {mode_file.name}")

    return sorted(all_modes)

def main():
    print("Scanning all mode files...")
    print()

    all_modes = count_all_modes()

    print()
    print(f"Total unique modes found: {len(all_modes)}")
    print(f"Mode range: {min(all_modes)} - {max(all_modes)}")

    # Check for gaps
    expected = set(range(1, 1101))
    missing = expected - set(all_modes)

    if missing:
        print(f"\n⚠ Missing {len(missing)} modes:")
        print(f"  {sorted(missing)}")
    else:
        print("\n✅ All expected modes (1-1100) are present!")

    # Check by category
    print("\nModes by category:")
    categories = [
        ("Original (1-300)", 1, 300),
        ("Nature & Organic (301-400)", 301, 400),
        ("Science & Physics (401-500)", 401, 500),
        ("Art & Visual (501-600)", 501, 600),
        ("Space & Cosmic (601-700)", 601, 700),
        ("Tech & Digital (701-800)", 701, 800),
        ("Spiritual & Sacred (801-900)", 801, 900),
        ("Hypnotic & Abstract (901-1000)", 901, 1000),
        ("Architecture & Structure (1001-1100)", 1001, 1100),
    ]

    for name, start, end in categories:
        count = sum(1 for m in all_modes if start <= m <= end)
        expected_count = end - start + 1
        status = "✓" if count == expected_count else "✗"
        print(f"  {status} {name:40}: {count:4}/{expected_count:4}")

if __name__ == "__main__":
    main()

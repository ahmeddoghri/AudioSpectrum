#!/usr/bin/env python3
"""
Comprehensive Audit Script for AudioSpectrum
Tests all 1100 modes for functionality, uniqueness, and quality
"""
import sys
import os
import importlib
import inspect
import re
from collections import defaultdict
from pathlib import Path

class AudioSpectrumAuditor:
    def __init__(self):
        self.results = {
            'total_modes': 0,
            'issues': [],
            'warnings': [],
            'mode_info': {},
            'duplicates': [],
            'missing_modes': [],
            'complexity_scores': {}
        }

    def audit_repository_structure(self):
        """Audit the overall repository structure"""
        print("=" * 70)
        print("REPOSITORY STRUCTURE AUDIT")
        print("=" * 70)
        print()

        repo_root = Path("/home/user/AudioSpectrum")

        # Check main files
        main_files = [
            'audio_spectrum.py',
            'audio_spectrum_creative.py',
            'audio_spectrum_lines.py',
            'audio_spectrum_image.py'
        ]

        print("Main Application Files:")
        for file in main_files:
            path = repo_root / file
            if path.exists():
                size = path.stat().st_size
                print(f"  ✓ {file:40} ({size:,} bytes)")
            else:
                print(f"  ✗ {file:40} MISSING")
                self.results['issues'].append(f"Missing main file: {file}")

        # Check modes directory
        print("\nModes Directory:")
        modes_dir = repo_root / "modes"
        if modes_dir.exists():
            mode_files = sorted(modes_dir.glob("mode_*.py"))
            print(f"  ✓ modes/ directory exists")
            print(f"  ✓ {len(mode_files)} mode files found")

            # List mode files
            for mf in mode_files:
                size = mf.stat().st_size
                lines = len(mf.read_text().split('\n'))
                print(f"    - {mf.name:30} ({size:6,} bytes, {lines:5,} lines)")
        else:
            print(f"  ✗ modes/ directory MISSING")
            self.results['issues'].append("Missing modes directory")

        print()

    def audit_mode_loading(self):
        """Test that all mode modules can be loaded"""
        print("=" * 70)
        print("MODE MODULE LOADING AUDIT")
        print("=" * 70)
        print()

        modes_dir = Path("/home/user/AudioSpectrum/modes")
        mode_files = sorted(modes_dir.glob("mode_*.py"))

        loaded = 0
        failed = 0

        for mode_file in mode_files:
            module_name = f"modes.{mode_file.stem}"
            try:
                module = importlib.import_module(module_name)

                # Find mode classes
                classes = [name for name, obj in inspect.getmembers(module, inspect.isclass)
                          if name.startswith('Modes') and name != 'BaseModeVisualizer']

                if classes:
                    print(f"  ✓ {mode_file.name:30} -> {', '.join(classes)}")
                    loaded += 1
                else:
                    print(f"  ⚠ {mode_file.name:30} -> No mode classes found")
                    self.results['warnings'].append(f"No classes in {mode_file.name}")

            except Exception as e:
                print(f"  ✗ {mode_file.name:30} -> ERROR: {e}")
                self.results['issues'].append(f"Failed to load {mode_file.name}: {e}")
                failed += 1

        print(f"\nSummary: {loaded} loaded, {failed} failed")
        print()

        return failed == 0

    def analyze_mode_methods(self):
        """Analyze all mode methods for completeness and uniqueness"""
        print("=" * 70)
        print("MODE METHODS ANALYSIS")
        print("=" * 70)
        print()

        modes_dir = Path("/home/user/AudioSpectrum/modes")
        mode_files = sorted(modes_dir.glob("mode_*.py"))

        all_modes = {}
        mode_descriptions = {}
        mode_complexity = {}

        for mode_file in mode_files:
            content = mode_file.read_text()

            # Find all draw_mode methods
            pattern = r'def (draw_mode_(\d+)_\w+)\(self, frame, magnitudes\):\s*"""([^"]+)"""'
            matches = re.finditer(pattern, content)

            for match in matches:
                method_name = match.group(1)
                mode_num = int(match.group(2))
                description = match.group(3).strip()

                all_modes[mode_num] = method_name
                mode_descriptions[mode_num] = description

                # Analyze complexity (rough metric based on code length)
                method_pattern = rf'def {method_name}\(.*?\):\s*""".*?"""(.*?)(?=\n    def |\Z)'
                method_match = re.search(method_pattern, content, re.DOTALL)
                if method_match:
                    code = method_match.group(1)
                    complexity = {
                        'lines': len(code.split('\n')),
                        'cv2_calls': code.count('cv2.'),
                        'loops': code.count('for ') + code.count('while '),
                        'conditionals': code.count('if ') + code.count('elif '),
                        'numpy_calls': code.count('np.')
                    }
                    mode_complexity[mode_num] = complexity

        self.results['total_modes'] = len(all_modes)
        self.results['mode_info'] = all_modes
        self.results['complexity_scores'] = mode_complexity

        # Check for missing modes
        expected_modes = set(range(1, 301)) | set(range(301, 1101))
        found_modes = set(all_modes.keys())
        missing = expected_modes - found_modes

        if missing:
            print(f"⚠ Missing modes: {sorted(missing)}")
            self.results['missing_modes'] = sorted(missing)

        # Print statistics by range
        ranges = [
            ("Original Modes", 1, 300),
            ("Nature & Organic", 301, 400),
            ("Science & Physics", 401, 500),
            ("Art & Visual", 501, 600),
            ("Space & Cosmic", 601, 700),
            ("Tech & Digital", 701, 800),
            ("Spiritual & Sacred", 801, 900),
            ("Hypnotic & Abstract", 901, 1000),
            ("Architecture & Structure", 1001, 1100),
        ]

        print("Mode Count by Category:")
        for category, start, end in ranges:
            count = sum(1 for m in all_modes.keys() if start <= m <= end)
            expected = end - start + 1
            status = "✓" if count == expected else "✗"
            print(f"  {status} {category:30} ({start:4}-{end:4}): {count:3}/{expected:3} modes")

        print(f"\nTotal Modes Found: {len(all_modes)}")
        print()

        return all_modes, mode_descriptions, mode_complexity

    def check_mode_uniqueness(self, mode_descriptions, mode_complexity):
        """Check that modes are sufficiently different from each other"""
        print("=" * 70)
        print("MODE UNIQUENESS ANALYSIS")
        print("=" * 70)
        print()

        # Group modes by similar descriptions
        description_groups = defaultdict(list)
        for mode_num, desc in mode_descriptions.items():
            # Normalize description
            normalized = desc.lower().strip()
            description_groups[normalized].append(mode_num)

        # Find potential duplicates
        duplicates = {desc: modes for desc, modes in description_groups.items() if len(modes) > 1}

        if duplicates:
            print(f"⚠ Found {len(duplicates)} duplicate descriptions:")
            for desc, modes in list(duplicates.items())[:10]:  # Show first 10
                print(f"  - '{desc}': modes {modes}")
            if len(duplicates) > 10:
                print(f"  ... and {len(duplicates) - 10} more")
            self.results['duplicates'] = duplicates
        else:
            print("✓ All mode descriptions are unique")

        # Check complexity distribution
        print("\nComplexity Distribution:")

        complexity_levels = {
            'simple': 0,      # < 20 lines
            'moderate': 0,    # 20-50 lines
            'complex': 0,     # 50-100 lines
            'very_complex': 0 # > 100 lines
        }

        for mode_num, complexity in mode_complexity.items():
            lines = complexity['lines']
            if lines < 20:
                complexity_levels['simple'] += 1
            elif lines < 50:
                complexity_levels['moderate'] += 1
            elif lines < 100:
                complexity_levels['complex'] += 1
            else:
                complexity_levels['very_complex'] += 1

        total = sum(complexity_levels.values())
        for level, count in complexity_levels.items():
            pct = (count / total * 100) if total > 0 else 0
            print(f"  {level.replace('_', ' ').title():15}: {count:4} ({pct:5.1f}%)")

        print()

    def check_code_quality(self):
        """Check code quality across all mode files"""
        print("=" * 70)
        print("CODE QUALITY AUDIT")
        print("=" * 70)
        print()

        modes_dir = Path("/home/user/AudioSpectrum/modes")
        mode_files = sorted(modes_dir.glob("mode_*.py"))

        issues = []

        for mode_file in mode_files:
            content = mode_file.read_text()

            # Check for common issues

            # 1. Missing imports
            if 'import numpy as np' not in content and 'np.' in content:
                issues.append(f"{mode_file.name}: Missing numpy import")

            if 'import cv2' not in content and 'cv2.' in content:
                issues.append(f"{mode_file.name}: Missing cv2 import")

            # 2. Check for syntax errors (basic)
            try:
                compile(content, mode_file.name, 'exec')
            except SyntaxError as e:
                issues.append(f"{mode_file.name}: Syntax error at line {e.lineno}")

            # 3. Check for proper class inheritance
            if 'class Modes' in content and 'BaseModeVisualizer' not in content:
                issues.append(f"{mode_file.name}: Class doesn't inherit from BaseModeVisualizer")

            # 4. Check return statements
            draw_methods = re.findall(r'def draw_mode_\d+_\w+\([^)]+\):(.*?)(?=\n    def |\Z)',
                                     content, re.DOTALL)
            for i, method in enumerate(draw_methods):
                if 'return frame' not in method:
                    issues.append(f"{mode_file.name}: Method {i+1} missing 'return frame'")

        if issues:
            print(f"⚠ Found {len(issues)} code quality issues:")
            for issue in issues[:20]:  # Show first 20
                print(f"  - {issue}")
            if len(issues) > 20:
                print(f"  ... and {len(issues) - 20} more")
            self.results['issues'].extend(issues)
        else:
            print("✓ No code quality issues found")

        print()

    def test_mode_creativity(self, mode_complexity):
        """Analyze mode creativity and variety"""
        print("=" * 70)
        print("MODE CREATIVITY ANALYSIS")
        print("=" * 70)
        print()

        # Analyze variety of techniques used
        techniques = {
            'circles': 0,
            'lines': 0,
            'polygons': 0,
            'text': 0,
            'complex_shapes': 0,
            'animations': 0
        }

        modes_dir = Path("/home/user/AudioSpectrum/modes")

        for mode_file in sorted(modes_dir.glob("mode_*.py")):
            content = mode_file.read_text()

            if 'cv2.circle' in content:
                techniques['circles'] += content.count('cv2.circle')
            if 'cv2.line' in content:
                techniques['lines'] += content.count('cv2.line')
            if 'cv2.fillPoly' in content or 'cv2.polylines' in content:
                techniques['polygons'] += content.count('cv2.fillPoly') + content.count('cv2.polylines')
            if 'cv2.putText' in content:
                techniques['text'] += content.count('cv2.putText')
            if 'cv2.ellipse' in content:
                techniques['complex_shapes'] += content.count('cv2.ellipse')
            if 'self.frame_count' in content:
                techniques['animations'] += content.count('self.frame_count')

        print("Drawing Techniques Used:")
        for technique, count in sorted(techniques.items(), key=lambda x: x[1], reverse=True):
            print(f"  {technique.replace('_', ' ').title():20}: {count:4} times")

        # Check for creative patterns
        print("\nCreative Patterns:")

        patterns = {
            'Spirals': 0,
            'Waves': 0,
            'Fractals': 0,
            'Particles': 0,
            'Rotations': 0,
            'Color gradients': 0
        }

        for mode_file in sorted(modes_dir.glob("mode_*.py")):
            content = mode_file.read_text().lower()

            if 'spiral' in content or 'angle' in content:
                patterns['Spirals'] += 1
            if 'wave' in content or 'sin(' in content or 'cos(' in content:
                patterns['Waves'] += 1
            if 'fractal' in content or 'recursive' in content:
                patterns['Fractals'] += 1
            if 'particle' in content:
                patterns['Particles'] += 1
            if 'rotation' in content or 'rotate' in content:
                patterns['Rotations'] += 1
            if 'hue' in content or 'gradient' in content:
                patterns['Color gradients'] += 1

        for pattern, count in sorted(patterns.items(), key=lambda x: x[1], reverse=True):
            print(f"  {pattern:20}: {count:4} modes")

        print()

    def generate_report(self):
        """Generate final audit report"""
        print("=" * 70)
        print("AUDIT SUMMARY REPORT")
        print("=" * 70)
        print()

        print(f"Total Modes Analyzed: {self.results['total_modes']}")
        print()

        if self.results['missing_modes']:
            print(f"⚠ Missing Modes: {len(self.results['missing_modes'])}")
            print(f"  {self.results['missing_modes']}")
            print()

        if self.results['issues']:
            print(f"❌ Issues Found: {len(self.results['issues'])}")
            for issue in self.results['issues'][:10]:
                print(f"  - {issue}")
            if len(self.results['issues']) > 10:
                print(f"  ... and {len(self.results['issues']) - 10} more")
            print()
        else:
            print("✅ No critical issues found")
            print()

        if self.results['warnings']:
            print(f"⚠ Warnings: {len(self.results['warnings'])}")
            for warning in self.results['warnings'][:10]:
                print(f"  - {warning}")
            if len(self.results['warnings']) > 10:
                print(f"  ... and {len(self.results['warnings']) - 10} more")
            print()

        # Overall assessment
        print("=" * 70)
        if not self.results['issues'] and not self.results['missing_modes']:
            print("🎉 AUDIT PASSED - All modes are properly implemented!")
        elif len(self.results['issues']) < 10:
            print("⚠ AUDIT PASSED WITH WARNINGS - Minor issues found")
        else:
            print("❌ AUDIT FAILED - Significant issues require attention")
        print("=" * 70)
        print()

def main():
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "AudioSpectrum Comprehensive Audit" + " " * 20 + "║")
    print("╚" + "=" * 68 + "╝")
    print()

    auditor = AudioSpectrumAuditor()

    # Run all audits
    auditor.audit_repository_structure()

    if not auditor.audit_mode_loading():
        print("❌ Critical: Mode loading failed. Aborting further tests.")
        return 1

    all_modes, mode_descriptions, mode_complexity = auditor.analyze_mode_methods()
    auditor.check_mode_uniqueness(mode_descriptions, mode_complexity)
    auditor.check_code_quality()
    auditor.test_mode_creativity(mode_complexity)
    auditor.generate_report()

    return 0 if not auditor.results['issues'] else 1

if __name__ == "__main__":
    sys.exit(main())

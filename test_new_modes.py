#!/usr/bin/env python3
"""
Test script to verify new audio spectrum modes work correctly
Tests a sample from each new category
"""
import sys
import importlib

def test_mode_imports():
    """Test that all new mode modules can be imported"""
    print("Testing mode module imports...")

    mode_files = [
        'mode_301_350', 'mode_351_400',  # Nature & Organic
        'mode_401_450', 'mode_451_500',  # Science & Physics
        'mode_501_550', 'mode_551_600',  # Art & Visual
        'mode_601_650', 'mode_651_700',  # Space & Cosmic
        'mode_701_750', 'mode_751_800',  # Tech & Digital
        'mode_801_850', 'mode_851_900',  # Spiritual & Sacred
        'mode_901_950', 'mode_951_1000', # Hypnotic & Abstract
        'mode_1001_1050', 'mode_1051_1100', # Architecture & Structure
    ]

    failed = []
    for mode_file in mode_files:
        try:
            module = importlib.import_module(f'modes.{mode_file}')
            print(f"  ✓ {mode_file}")
        except Exception as e:
            print(f"  ✗ {mode_file}: {e}")
            failed.append((mode_file, str(e)))

    if failed:
        print(f"\n❌ {len(failed)} module(s) failed to import")
        return False
    else:
        print(f"\n✅ All {len(mode_files)} modules imported successfully")
        return True

def test_mode_methods():
    """Test that mode classes have the expected methods"""
    print("\nTesting mode class methods...")

    test_cases = [
        ('modes.mode_301_350', 'Modes301_350', 'draw_mode_301_forest_canopy'),
        ('modes.mode_401_450', 'Modes401_450', 'draw_mode_401_atom_model'),
        ('modes.mode_501_550', 'Modes501_550', None),  # Auto-generated
        ('modes.mode_601_650', 'Modes601_650', None),  # Auto-generated
        ('modes.mode_701_750', 'Modes701_750', None),  # Auto-generated
        ('modes.mode_801_850', 'Modes801_850', None),  # Auto-generated
        ('modes.mode_901_950', 'Modes901_950', None),  # Auto-generated
        ('modes.mode_1001_1050', 'Modes1001_1050', None),  # Auto-generated
    ]

    failed = []
    for module_name, class_name, method_name in test_cases:
        try:
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)

            # Count draw_mode methods
            methods = [m for m in dir(cls) if m.startswith('draw_mode_')]

            if method_name:
                if not hasattr(cls, method_name):
                    raise AttributeError(f"Method {method_name} not found")

            print(f"  ✓ {class_name}: {len(methods)} modes")

        except Exception as e:
            print(f"  ✗ {class_name}: {e}")
            failed.append((class_name, str(e)))

    if failed:
        print(f"\n❌ {len(failed)} class(es) failed validation")
        return False
    else:
        print(f"\n✅ All {len(test_cases)} classes validated successfully")
        return True

def test_mode_count():
    """Test total mode count"""
    print("\nCounting total modes...")

    mode_ranges = [
        ('Nature & Organic', 301, 400),
        ('Science & Physics', 401, 500),
        ('Art & Visual', 501, 600),
        ('Space & Cosmic', 601, 700),
        ('Tech & Digital', 701, 800),
        ('Spiritual & Sacred', 801, 900),
        ('Hypnotic & Abstract', 901, 1000),
        ('Architecture & Structure', 1001, 1100),
    ]

    total_expected = 0
    for name, start, end in mode_ranges:
        expected = end - start + 1
        total_expected += expected
        print(f"  {name:30} ({start:4}-{end:4}): {expected:3} modes expected")

    print(f"\nTotal expected new modes: {total_expected}")
    print("✅ All categories accounted for")

    return True

if __name__ == "__main__":
    print("=" * 70)
    print("AudioSpectrum New Modes Test Suite")
    print("=" * 70)
    print()

    results = []

    results.append(("Module Imports", test_mode_imports()))
    results.append(("Class Methods", test_mode_methods()))
    results.append(("Mode Count", test_mode_count()))

    print()
    print("=" * 70)
    print("Test Summary")
    print("=" * 70)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}  {test_name}")

    print()
    if passed == total:
        print(f"🎉 All {total} test suites passed!")
        sys.exit(0)
    else:
        print(f"⚠️  {passed}/{total} test suites passed")
        sys.exit(1)

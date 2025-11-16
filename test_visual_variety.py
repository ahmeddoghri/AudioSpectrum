#!/usr/bin/env python3
"""
Test visual variety by generating sample frames from different modes
Tests that modes produce visually distinct outputs
"""
import sys
import numpy as np
import cv2
from audio_spectrum_creative import CreativeSpectrumVisualizer
import random

def generate_test_magnitudes():
    """Generate realistic test magnitude data"""
    # Simulate frequency magnitudes with some variation
    magnitudes = []

    # Bass frequencies (low, higher amplitude)
    magnitudes.extend([random.uniform(0.6, 0.9) for _ in range(30)])

    # Mid frequencies (moderate amplitude)
    magnitudes.extend([random.uniform(0.3, 0.6) for _ in range(50)])

    # High frequencies (lower amplitude, more variation)
    magnitudes.extend([random.uniform(0.1, 0.4) for _ in range(40)])

    return np.array(magnitudes)

def test_mode_output(mode_num, visualizer, test_name=""):
    """Test a single mode and return frame"""
    try:
        # Generate test magnitudes
        magnitudes = generate_test_magnitudes()

        # Create blank frame (1920x1080, 3 channels, black)
        frame = np.zeros((visualizer.height, visualizer.width, 3), dtype=np.uint8)

        # Get mode method
        from modes import get_mode_method
        mode_method = get_mode_method(mode_num)

        if mode_method is None:
            return None, f"Mode {mode_num} not found"

        # Draw the visualization
        result_frame = mode_method(frame, magnitudes)

        # Check if frame was modified (not all black)
        if np.sum(result_frame) == 0:
            return None, f"Mode {mode_num} produced blank frame"

        return result_frame, None

    except Exception as e:
        return None, f"Mode {mode_num} error: {str(e)}"

def calculate_frame_diversity(frames):
    """Calculate how different frames are from each other"""
    if len(frames) < 2:
        return 0.0

    differences = []
    for i in range(len(frames)):
        for j in range(i + 1, len(frames)):
            # Calculate absolute difference between frames
            diff = np.abs(frames[i].astype(float) - frames[j].astype(float))
            avg_diff = np.mean(diff)
            differences.append(avg_diff)

    return np.mean(differences)

def main():
    print("=" * 70)
    print("Visual Variety Test - Testing Sample Modes from Each Category")
    print("=" * 70)
    print()

    # Create visualizer
    print("Initializing visualizer...")
    # Use dummy paths since we're just testing frame generation
    visualizer = CreativeSpectrumVisualizer("dummy.mp3", "dummy.mp4")

    # Initialize frame counter for modes that use animation
    visualizer.frame_count = 0
    visualizer.frame_counter = 0

    print("✓ Visualizer created")
    print()

    # Test modes from each category
    test_categories = [
        ("Nature & Organic", [305, 325, 345, 365, 385]),
        ("Science & Physics", [410, 430, 450, 470, 490]),
        ("Art & Visual", [510, 530, 550, 570, 590]),
        ("Space & Cosmic", [610, 630, 650, 670, 690]),
        ("Tech & Digital", [710, 730, 750, 770, 790]),
        ("Spiritual & Sacred", [810, 830, 850, 870, 890]),
        ("Hypnotic & Abstract", [910, 930, 950, 970, 990]),
        ("Architecture & Structure", [1010, 1030, 1050, 1070, 1090]),
    ]

    all_frames = []
    results = []

    for category_name, mode_nums in test_categories:
        print(f"Testing {category_name}...")
        category_frames = []
        successes = 0
        failures = 0

        for mode_num in mode_nums:
            frame, error = test_mode_output(mode_num, visualizer, category_name)

            if error:
                print(f"  ✗ Mode {mode_num}: {error}")
                failures += 1
            else:
                print(f"  ✓ Mode {mode_num}: Generated successfully")
                category_frames.append(frame)
                all_frames.append(frame)
                successes += 1

        # Calculate diversity within category
        if len(category_frames) > 1:
            diversity = calculate_frame_diversity(category_frames)
            print(f"  → Diversity score: {diversity:.2f}")
        else:
            diversity = 0.0

        results.append({
            'category': category_name,
            'successes': successes,
            'failures': failures,
            'diversity': diversity
        })

        print()

    # Overall statistics
    print("=" * 70)
    print("VISUAL VARIETY TEST RESULTS")
    print("=" * 70)
    print()

    total_success = sum(r['successes'] for r in results)
    total_failure = sum(r['failures'] for r in results)
    total_tested = total_success + total_failure

    print(f"Modes Tested: {total_tested}")
    print(f"Successful: {total_success}")
    print(f"Failed: {total_failure}")
    print(f"Success Rate: {(total_success/total_tested*100):.1f}%")
    print()

    print("Category Diversity Scores:")
    for result in results:
        status = "✓" if result['failures'] == 0 else "⚠"
        print(f"  {status} {result['category']:30}: {result['diversity']:6.2f} ({result['successes']}/{result['successes']+result['failures']} modes)")

    # Overall diversity
    if len(all_frames) > 1:
        overall_diversity = calculate_frame_diversity(all_frames)
        print(f"\nOverall Diversity Score: {overall_diversity:.2f}")

        if overall_diversity > 30:
            print("✅ Excellent diversity - modes are visually distinct")
        elif overall_diversity > 20:
            print("✓ Good diversity - modes show good variation")
        elif overall_diversity > 10:
            print("⚠ Moderate diversity - some modes may be similar")
        else:
            print("⚠ Low diversity - modes may be too similar")

    print()
    print("=" * 70)

    if total_failure == 0:
        print("🎉 All tested modes work correctly!")
        return 0
    else:
        print(f"⚠ {total_failure} mode(s) had issues")
        return 1

if __name__ == "__main__":
    sys.exit(main())

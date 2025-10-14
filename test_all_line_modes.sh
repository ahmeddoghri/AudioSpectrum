#!/bin/bash

# Test all 10 line-based visualization modes
# This script generates a video for each mode with the same audio input

AUDIO_FILE="/Users/ahmeddoghri/Desktop/RÜFÜS DU SOL - New Sky (Lyrics).mp3"
OUTPUT_DIR="/Users/ahmeddoghri/Desktop"

echo "Testing all 10 line-based visualization modes..."
echo "========================================"

# Check if audio file exists
if [ ! -f "$AUDIO_FILE" ]; then
    echo "Error: Audio file not found at: $AUDIO_FILE"
    exit 1
fi

# Array of mode names for better output
declare -a mode_names=(
    "Classic_Bars"
    "Mirror_Symmetry"
    "Waterfall"
    "Converging_Lines"
    "Wave_Morph"
    "Staggered_Pulse"
    "Geometric_Tunnel"
    "Dancing_Ribbons"
    "Particle_Stream"
    "Glitch_Art"
)

# Loop through all 10 modes
for mode in {1..10}; do
    mode_name="${mode_names[$mode-1]}"
    output_file="${OUTPUT_DIR}/output_lines_mode${mode}_${mode_name}.mov"

    echo ""
    echo "Processing Mode $mode: $mode_name"
    echo "Output: $output_file"
    echo "----------------------------------------"

    python audio_spectrum_lines.py "$AUDIO_FILE" "$output_file" --mode $mode

    if [ $? -eq 0 ]; then
        echo "✓ Mode $mode completed successfully"
    else
        echo "✗ Mode $mode failed"
    fi
done

echo ""
echo "========================================"
echo "All line-based modes processed!"
echo "Check the output files in: $OUTPUT_DIR"
echo ""
echo "Files created:"
ls -lh "${OUTPUT_DIR}"/output_lines_mode*.mov 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'

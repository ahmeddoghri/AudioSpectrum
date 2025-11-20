/**
 * Automated Mode Migration Helper
 *
 * This script helps migrate visualization modes from Python to JavaScript
 * by finding broken modes and their Python implementations.
 */

const fs = require('fs');
const path = require('path');

// Find all broken modes
function findBrokenModes() {
    const visualizerContent = fs.readFileSync('./web/visualizer.js', 'utf8');
    const placeholderRegex = /this\.renderPlaceholder\(magnitudes,\s*'([^']+)',\s*(\d+)\);/g;
    const matches = [];
    let match;

    while ((match = placeholderRegex.exec(visualizerContent)) !== null) {
        matches.push({
            name: match[1],
            modeNumber: parseInt(match[2])
        });
    }

    return matches.sort((a, b) => a.modeNumber - b.modeNumber);
}

// Find Python file for a mode number
function findPythonFile(modeNumber) {
    const ranges = [
        { start: 1, end: 50, file: 'modes/mode_001_050.py' },
        { start: 51, end: 100, file: 'modes/mode_051_100.py' },
        { start: 101, end: 150, file: 'modes/mode_101_150.py' },
        { start: 151, end: 200, file: 'modes/mode_151_200.py' },
        { start: 201, end: 225, file: 'modes/mode_201_225.py' },
        { start: 226, end: 275, file: 'modes/mode_226_275.py' },
        { start: 276, end: 300, file: 'modes/mode_276_300.py' },
        { start: 301, end: 350, file: 'modes/mode_301_350.py' },
        { start: 351, end: 400, file: 'modes/mode_351_400.py' },
        { start: 401, end: 450, file: 'modes/mode_401_450.py' },
        { start: 451, end: 500, file: 'modes/mode_451_500.py' },
        { start: 501, end: 550, file: 'modes/mode_501_550.py' },
        { start: 551, end: 600, file: 'modes/mode_551_600.py' },
        { start: 601, end: 650, file: 'modes/mode_601_650.py' },
        { start: 651, end: 700, file: 'modes/mode_651_700.py' },
        { start: 701, end: 750, file: 'modes/mode_701_750.py' },
        { start: 751, end: 800, file: 'modes/mode_751_800.py' }
    ];

    for (const range of ranges) {
        if (modeNumber >= range.start && modeNumber <= range.end) {
            return range.file;
        }
    }

    return null;
}

// Extract Python implementation for a specific mode
function extractPythonImplementation(modeNumber) {
    const pythonFile = findPythonFile(modeNumber);

    if (!pythonFile || !fs.existsSync(pythonFile)) {
        return null;
    }

    const content = fs.readFileSync(pythonFile, 'utf8');

    // Search for the function definition
    const functionPattern = new RegExp(
        `def draw_mode_${modeNumber}_[^(]+\\(self, frame, magnitudes\\):[\\s\\S]*?(?=\\n    def |\\nclass |$)`,
        'g'
    );

    const match = content.match(functionPattern);

    if (match && match[0]) {
        return match[0];
    }

    return null;
}

// Main function
function main() {
    console.log('\n=== Automated Mode Migration Helper ===\n');

    const brokenModes = findBrokenModes();
    console.log(`Found ${brokenModes.length} broken modes\n`);

    // Example: Show first 10 broken modes with their Python implementations
    const modesToShow = brokenModes.slice(0, 10);

    console.log('First 10 broken modes:\n');

    for (const mode of modesToShow) {
        console.log(`\n${'='.repeat(70)}`);
        console.log(`Mode ${mode.modeNumber}: ${mode.name}`);
        console.log('='.repeat(70));

        const pythonFile = findPythonFile(mode.modeNumber);
        console.log(`Python file: ${pythonFile || 'NOT FOUND'}`);

        if (pythonFile) {
            const implementation = extractPythonImplementation(mode.modeNumber);
            if (implementation) {
                // Show first 20 lines of implementation
                const lines = implementation.split('\n').slice(0, 20);
                console.log('\nPython Implementation (first 20 lines):');
                console.log(lines.join('\n'));
                console.log('\n... (truncated)');
            } else {
                console.log('Could not extract implementation');
            }
        }
    }

    console.log(`\n\n✅ To fix a mode:`);
    console.log(`1. Find the Python implementation in the file shown above`);
    console.log(`2. Convert cv2/numpy calls to Canvas API calls`);
    console.log(`3. Replace the renderPlaceholder() call in web/visualizer.js`);
    console.log(`4. Test in the browser\n`);

    // Generate a priority list
    console.log('\n=== Priority Modes to Fix ===\n');
    console.log('Based on category distribution:');

    const byCategory = {};
    brokenModes.forEach(mode => {
        const range = Math.floor(mode.modeNumber / 100) * 100;
        const key = `${range}-${range + 99}`;
        if (!byCategory[key]) byCategory[key] = 0;
        byCategory[key]++;
    });

    Object.entries(byCategory).forEach(([range, count]) => {
        console.log(`  ${range}: ${count} modes`);
    });
}

main();

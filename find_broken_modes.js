/**
 * Script to find all visualization modes that are using renderPlaceholder
 * (indicating they weren't properly migrated from Python to JavaScript)
 */

const fs = require('fs');

// Read the visualizer.js file
const visualizerContent = fs.readFileSync('./web/visualizer.js', 'utf8');

// Find all occurrences of renderPlaceholder
const placeholderRegex = /this\.renderPlaceholder\(magnitudes,\s*'([^']+)',\s*(\d+)\);/g;
const matches = [];
let match;

while ((match = placeholderRegex.exec(visualizerContent)) !== null) {
    matches.push({
        name: match[1],
        modeNumber: parseInt(match[2])
    });
}

// Sort by mode number
matches.sort((a, b) => a.modeNumber - b.modeNumber);

console.log(`\n========================================`);
console.log(`BROKEN MODES REPORT`);
console.log(`========================================\n`);
console.log(`Found ${matches.length} modes using placeholder implementation:\n`);

// Group modes by ranges for easier viewing
const ranges = {
    '100-199': matches.filter(m => m.modeNumber >= 100 && m.modeNumber < 200),
    '200-299': matches.filter(m => m.modeNumber >= 200 && m.modeNumber < 300),
    '300-399': matches.filter(m => m.modeNumber >= 300 && m.modeNumber < 400),
    '400-499': matches.filter(m => m.modeNumber >= 400 && m.modeNumber < 500),
    '500+': matches.filter(m => m.modeNumber >= 500)
};

for (const [range, modes] of Object.entries(ranges)) {
    if (modes.length > 0) {
        console.log(`\n${range}: ${modes.length} modes`);
        console.log('─'.repeat(50));
        modes.forEach(mode => {
            console.log(`  Mode ${mode.modeNumber}: ${mode.name}`);
        });
    }
}

// Write detailed report to file
const reportContent = `BROKEN MODES REPORT
Generated: ${new Date().toISOString()}

Total broken modes: ${matches.length}

DETAILED LIST:
${matches.map(m => `Mode ${m.modeNumber}: ${m.name}`).join('\n')}

EXPLANATION:
These modes all call renderPlaceholder() which renders a generic circular bars
visualization instead of their unique implementation. This occurred during the
migration from Python to JavaScript where the implementations were not completed.

IMPACT:
Multiple modes with different names and descriptions will look identical,
causing confusion for users.

RECOMMENDATION:
Each mode needs its unique render implementation based on its description
in the constants.js file.
`;

fs.writeFileSync('./broken_modes_report.txt', reportContent);
console.log(`\n\n✅ Detailed report saved to: broken_modes_report.txt\n`);

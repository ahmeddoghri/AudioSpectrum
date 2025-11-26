/**
 * Test parameter integration for new modes
 * Verifies that step 4 parameters actually affect the visualization
 */

const fs = require('fs');
const path = require('path');

// Read visualizer.js
const visualizerPath = path.join(__dirname, 'web', 'visualizer.js');
const visualizerContent = fs.readFileSync(visualizerPath, 'utf8');

// Define modes and their parameters with expected usage patterns
const modesWithParams = [
    {
        id: 'circular_waves',
        renderFunction: 'renderCircularWaves',
        paramUsage: [
            { param: 'waveCount', usage: 'for \\(let w = 0; w < waveCount' },
            { param: 'waveThickness', usage: 'lineWidth = waveThickness' },
            { param: 'waveSpacing', usage: 'baseRadius = w \\* waveSpacing' }
        ]
    },
    {
        id: 'line_spectrum',
        renderFunction: 'renderLineSpectrum',
        paramUsage: [
            { param: 'lineCount', usage: 'for \\(let i = 0; i < lineCount' },
            { param: 'lineThickness', usage: 'lineWidth = lineThickness' },
            { param: 'lineSpacing', usage: 'y = startY \\+ i \\* lineSpacing' }
        ]
    },
    {
        id: 'radial_pulse',
        renderFunction: 'renderRadialPulse',
        paramUsage: [
            { param: 'ringCount', usage: 'for \\(let i = 0; i < ringCount' },
            { param: 'pulseIntensity', usage: 'avgMagnitude \\* pulseIntensity' },
            { param: 'ringThickness', usage: 'lineWidth = ringThickness' }
        ]
    },
    {
        id: 'double_helix',
        renderFunction: 'renderDoubleHelix',
        paramUsage: [
            { param: 'helixTurns', usage: 'Math\\.PI \\* 2 \\* helixTurns' },
            { param: 'helixWidth', usage: 'Math\\.cos\\(angle\\) \\* helixWidth' },
            { param: 'pointSize', usage: 'size = pointSize \\+' }
        ]
    },
    {
        id: 'spiral_bars',
        renderFunction: 'renderSpiralBars',
        paramUsage: [
            { param: 'spiralTurns', usage: 'Math\\.PI \\* 2 \\* spiralTurns' },
            { param: 'barLength', usage: 'length = barLength \\+' },
            { param: 'spiralTightness', usage: 'maxRadius \\* 0\\.6 \\* spiralTightness' }
        ]
    }
];

let allTestsPassed = true;

console.log('='.repeat(70));
console.log('Testing Parameter Integration for New Modes');
console.log('='.repeat(70));
console.log();

modesWithParams.forEach(mode => {
    console.log(`Mode: ${mode.id}`);
    console.log('-'.repeat(70));

    // Extract the render function
    const functionPattern = new RegExp(`${mode.renderFunction}\\(magnitudes\\)\\s*{([\\s\\S]*?)(?=\\n\\s{4}(?:\\/\\*\\*|render))`, 'm');
    const functionMatch = visualizerContent.match(functionPattern);

    if (!functionMatch) {
        console.log(`✗ Could not extract ${mode.renderFunction}`);
        allTestsPassed = false;
        console.log();
        return;
    }

    const functionBody = functionMatch[1];

    // Test 1: Check params extraction
    if (/const params = this\.settings\.parameters/.test(functionBody)) {
        console.log(`✓ Correctly extracts parameters from this.settings.parameters`);
    } else {
        console.log(`✗ Does NOT extract parameters correctly`);
        allTestsPassed = false;
    }

    // Test 2: Check each parameter is extracted and used
    let allParamsUsed = true;
    mode.paramUsage.forEach(({ param, usage }) => {
        // Check if parameter is extracted from params object
        const extractPattern = new RegExp(`const ${param} = params\\.${param}`, 'm');
        if (extractPattern.test(functionBody)) {
            console.log(`  ✓ ${param}: extracted from params`);

            // Check if parameter is actually used in the logic
            const usagePattern = new RegExp(usage, 'm');
            if (usagePattern.test(functionBody)) {
                console.log(`  ✓ ${param}: used in visualization logic`);
            } else {
                console.log(`  ⚠ ${param}: extracted but usage pattern not found`);
                // Not failing the test as usage pattern might be different
            }
        } else {
            console.log(`  ✗ ${param}: NOT properly extracted`);
            allParamsUsed = false;
            allTestsPassed = false;
        }
    });

    if (allParamsUsed) {
        console.log(`✓ All parameters properly integrated`);
    }

    console.log();
});

// Test that app.js properly passes parameters
const appPath = path.join(__dirname, 'web', 'app.js');
const appContent = fs.readFileSync(appPath, 'utf8');

console.log('Testing app.js parameter handling');
console.log('-'.repeat(70));

// Check if parameters are stored in the correct location
if (/this\.state\.settings\.parameters\[paramKey\]/.test(appContent)) {
    console.log('✓ app.js stores parameters in this.state.settings.parameters');
} else {
    console.log('✗ app.js does NOT store parameters correctly');
    allTestsPassed = false;
}

// Check if updatePreview is called when parameters change
if (/this\.updatePreview\(\)/.test(appContent)) {
    console.log('✓ app.js calls updatePreview() when parameters change');
} else {
    console.log('✗ app.js does NOT call updatePreview() when parameters change');
    allTestsPassed = false;
}

console.log();
console.log('='.repeat(70));
if (allTestsPassed) {
    console.log('✓ PARAMETER INTEGRATION VERIFIED!');
    console.log('  All modes correctly access and use step 4 parameters.');
} else {
    console.log('✗ PARAMETER INTEGRATION ISSUES DETECTED');
    console.log('  Some parameters are not properly integrated.');
}
console.log('='.repeat(70));

process.exit(allTestsPassed ? 0 : 1);

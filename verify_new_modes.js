/**
 * Verification script for new classic modes
 * This script checks that all 5 new modes are properly defined and implemented
 */

const fs = require('fs');
const path = require('path');

// Read constants.js
const constantsPath = path.join(__dirname, 'web', 'constants.js');
const constantsContent = fs.readFileSync(constantsPath, 'utf8');

// Read visualizer.js
const visualizerPath = path.join(__dirname, 'web', 'visualizer.js');
const visualizerContent = fs.readFileSync(visualizerPath, 'utf8');

// Define the expected modes
const expectedModes = [
    {
        id: 'circular_waves',
        name: 'Circular Waves',
        mode: 861,
        renderFunction: 'renderCircularWaves',
        parameters: ['waveCount', 'waveThickness', 'waveSpacing']
    },
    {
        id: 'line_spectrum',
        name: 'Line Spectrum',
        mode: 862,
        renderFunction: 'renderLineSpectrum',
        parameters: ['lineCount', 'lineThickness', 'lineSpacing']
    },
    {
        id: 'radial_pulse',
        name: 'Radial Pulse',
        mode: 863,
        renderFunction: 'renderRadialPulse',
        parameters: ['ringCount', 'pulseIntensity', 'ringThickness']
    },
    {
        id: 'double_helix',
        name: 'Double Helix',
        mode: 864,
        renderFunction: 'renderDoubleHelix',
        parameters: ['helixTurns', 'helixWidth', 'pointSize']
    },
    {
        id: 'spiral_bars',
        name: 'Spiral Bars',
        mode: 865,
        renderFunction: 'renderSpiralBars',
        parameters: ['spiralTurns', 'barLength', 'spiralTightness']
    }
];

let allTestsPassed = true;

console.log('='.repeat(60));
console.log('Verifying New Classic Modes Implementation');
console.log('='.repeat(60));
console.log();

expectedModes.forEach(mode => {
    console.log(`Testing mode: ${mode.name} (${mode.id})`);
    console.log('-'.repeat(60));

    // Test 1: Check if mode is defined in constants.js
    const modeDefinitionPattern = new RegExp(`${mode.id}:\\s*{[\\s\\S]*?id:\\s*['"]${mode.id}['"][\\s\\S]*?mode:\\s*${mode.mode}`, 'm');
    if (modeDefinitionPattern.test(constantsContent)) {
        console.log(`✓ Mode definition found in constants.js`);
    } else {
        console.log(`✗ Mode definition NOT found in constants.js`);
        allTestsPassed = false;
    }

    // Test 2: Check if all parameters are defined
    let allParamsFound = true;
    mode.parameters.forEach(param => {
        const paramPattern = new RegExp(`${param}:\\s*{[^}]*min:[^}]*max:[^}]*default:[^}]*label:`, 'm');
        if (!paramPattern.test(constantsContent)) {
            console.log(`✗ Parameter ${param} NOT properly defined`);
            allParamsFound = false;
            allTestsPassed = false;
        }
    });
    if (allParamsFound) {
        console.log(`✓ All ${mode.parameters.length} parameters defined correctly`);
    }

    // Test 3: Check if case statement exists in visualizer.js
    const casePattern = new RegExp(`case\\s+['"]${mode.id}['"]:[\\s\\S]*?this\\.${mode.renderFunction}\\(magnitudes\\)`, 'm');
    if (casePattern.test(visualizerContent)) {
        console.log(`✓ Case statement found in visualizer.js`);
    } else {
        console.log(`✗ Case statement NOT found in visualizer.js`);
        allTestsPassed = false;
    }

    // Test 4: Check if render function is implemented
    const renderFunctionPattern = new RegExp(`${mode.renderFunction}\\(magnitudes\\)\\s*{[\\s\\S]{100,}`, 'm');
    if (renderFunctionPattern.test(visualizerContent)) {
        console.log(`✓ Render function ${mode.renderFunction} implemented`);
    } else {
        console.log(`✗ Render function ${mode.renderFunction} NOT implemented`);
        allTestsPassed = false;
    }

    // Test 5: Check if render function accesses parameters
    const renderFunctionStartPattern = new RegExp(`${mode.renderFunction}\\(magnitudes\\)\\s*{([\\s\\S]{0,500}?)(?=\\n\\s{4}(?:render|\\*\\*\\*))`);
    const renderFunctionMatch = visualizerContent.match(renderFunctionStartPattern);
    if (renderFunctionMatch) {
        const functionBody = renderFunctionMatch[1];
        const accessesParams = /const params = this\.settings\.parameters/.test(functionBody);
        const usesParams = mode.parameters.some(param => new RegExp(`params\\.${param}`).test(functionBody));

        if (accessesParams && usesParams) {
            console.log(`✓ Render function correctly accesses parameters`);
        } else {
            console.log(`✗ Render function does NOT properly access parameters`);
            allTestsPassed = false;
        }
    }

    console.log();
});

console.log('='.repeat(60));
if (allTestsPassed) {
    console.log('✓ All tests PASSED! All 5 new modes are properly implemented.');
} else {
    console.log('✗ Some tests FAILED. Please review the implementation.');
}
console.log('='.repeat(60));

process.exit(allTestsPassed ? 0 : 1);

#!/usr/bin/env node

/**
 * Verification script to ensure all 45 modes are properly implemented
 */

const fs = require('fs');
const path = require('path');

// Read files
const constantsContent = fs.readFileSync(path.join(__dirname, 'constants.js'), 'utf8');
const visualizerContent = fs.readFileSync(path.join(__dirname, 'visualizer.js'), 'utf8');

// Extract mode IDs from constants.js
const modeMatches = constantsContent.match(/\b\w+:\s*\{[\s\S]*?id:\s*'(\w+)'/g);
const definedModes = [];

if (modeMatches) {
    modeMatches.forEach(match => {
        const idMatch = match.match(/id:\s*'(\w+)'/);
        if (idMatch) {
            definedModes.push(idMatch[1]);
        }
    });
}

// Extract case statements from visualizer.js
const caseMatches = visualizerContent.match(/case\s+'(\w+)':/g);
const implementedCases = [];

if (caseMatches) {
    caseMatches.forEach(match => {
        const caseMatch = match.match(/case\s+'(\w+)':/);
        if (caseMatch) {
            implementedCases.push(caseMatch[1]);
        }
    });
}

// Extract render methods from visualizer.js
const renderMatches = visualizerContent.match(/render\w+\(magnitudes\)/g);
const renderMethods = [];

if (renderMatches) {
    renderMatches.forEach(match => {
        const methodMatch = match.match(/render(\w+)\(/);
        if (methodMatch) {
            renderMethods.push(methodMatch[1]);
        }
    });
}

// Report
console.log('='.repeat(60));
console.log('AUDIO SPECTRUM VISUALIZATION MODES - VERIFICATION REPORT');
console.log('='.repeat(60));
console.log('');

console.log(`✓ Modes defined in constants.js: ${definedModes.length}`);
console.log(`✓ Case statements in visualizer.js: ${implementedCases.length}`);
console.log(`✓ Render methods in visualizer.js: ${renderMethods.length}`);
console.log('');

// Check for missing implementations
const missingImplementations = definedModes.filter(mode => !implementedCases.includes(mode));
if (missingImplementations.length > 0) {
    console.log('⚠️  MISSING IMPLEMENTATIONS:');
    missingImplementations.forEach(mode => console.log(`   - ${mode}`));
    console.log('');
}

// Check for undefined modes
const undefinedModes = implementedCases.filter(mode => !definedModes.includes(mode) && mode !== 'default');
if (undefinedModes.length > 0) {
    console.log('⚠️  IMPLEMENTED BUT NOT DEFINED:');
    undefinedModes.forEach(mode => console.log(`   - ${mode}`));
    console.log('');
}

// List all modes by category
console.log('MODES BY CATEGORY:');
console.log('-'.repeat(60));

const categories = {
    Classic: [],
    Particles: [],
    Retro: [],
    Fluid: [],
    Nature: [],
    Geometric: [],
    Scientific: [],
    Tech: [],
    Energy: []
};

const modeBlockMatches = constantsContent.match(/(\w+):\s*\{[^}]*id:\s*'(\w+)'[^}]*category:\s*'(\w+)'[^}]*\}/g);

if (modeBlockMatches) {
    modeBlockMatches.forEach(block => {
        const idMatch = block.match(/id:\s*'(\w+)'/);
        const categoryMatch = block.match(/category:\s*'(\w+)'/);
        const nameMatch = block.match(/name:\s*'([^']+)'/);

        if (idMatch && categoryMatch && nameMatch) {
            const category = categoryMatch[1];
            const id = idMatch[1];
            const name = nameMatch[1];
            const implemented = implementedCases.includes(id);

            if (categories[category]) {
                categories[category].push({
                    id,
                    name,
                    implemented
                });
            }
        }
    });
}

Object.keys(categories).forEach(category => {
    const modes = categories[category];
    if (modes.length > 0) {
        console.log(`\n${category} (${modes.length} modes):`);
        modes.forEach(mode => {
            const status = mode.implemented ? '✓' : '✗';
            console.log(`  ${status} ${mode.name} (${mode.id})`);
        });
    }
});

console.log('');
console.log('='.repeat(60));

// Summary
const totalDefined = definedModes.length;
const totalImplemented = implementedCases.filter(c => c !== 'default').length;
const successRate = ((totalImplemented / totalDefined) * 100).toFixed(1);

console.log(`SUMMARY:`);
console.log(`  Total Modes Defined: ${totalDefined}`);
console.log(`  Total Modes Implemented: ${totalImplemented}`);
console.log(`  Success Rate: ${successRate}%`);

if (missingImplementations.length === 0 && totalDefined === 45) {
    console.log('');
    console.log('✅ ALL 45 MODES ARE PROPERLY IMPLEMENTED!');
} else if (missingImplementations.length > 0) {
    console.log('');
    console.log(`❌ ${missingImplementations.length} modes are missing implementations`);
}

console.log('='.repeat(60));

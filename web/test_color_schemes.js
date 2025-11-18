#!/usr/bin/env node

/**
 * Automated test to verify all color schemes work with all visualization modes
 */

const fs = require('fs');
const path = require('path');

// Load constants
const constantsPath = path.join(__dirname, 'constants.js');
const constantsContent = fs.readFileSync(constantsPath, 'utf8');

// Parse modes and color schemes
function extractModes() {
    const modes = [];
    const modeBlockMatches = constantsContent.match(/(\w+):\s*\{[^}]*id:\s*'(\w+)'[^}]*name:\s*'([^']+)'[^}]*category:\s*'(\w+)'[^}]*\}/g);

    if (modeBlockMatches) {
        modeBlockMatches.forEach(block => {
            const idMatch = block.match(/id:\s*'(\w+)'/);
            const nameMatch = block.match(/name:\s*'([^']+)'/);
            const categoryMatch = block.match(/category:\s*'(\w+)'/);

            if (idMatch && nameMatch && categoryMatch) {
                modes.push({
                    id: idMatch[1],
                    name: nameMatch[1],
                    category: categoryMatch[1]
                });
            }
        });
    }

    return modes;
}

function extractColorSchemes() {
    const schemes = [];
    const schemeMatches = constantsContent.match(/(\w+):\s*\{[^}]*name:\s*'([^']+)'[^}]*primary:/g);

    if (schemeMatches) {
        schemeMatches.forEach(match => {
            const idMatch = match.match(/^(\w+):/);
            const nameMatch = match.match(/name:\s*'([^']+)'/);

            if (idMatch && nameMatch) {
                schemes.push({
                    id: idMatch[1],
                    name: nameMatch[1]
                });
            }
        });
    }

    return schemes;
}

// Verify color scheme compatibility
function verifyColorSchemeUsage(modeId) {
    const visualizerPath = path.join(__dirname, 'visualizer.js');
    const visualizerContent = fs.readFileSync(visualizerPath, 'utf8');

    // Find the render method for this mode
    const methodName = modeId.split('_').map((word, i) =>
        i === 0 ? word : word.charAt(0).toUpperCase() + word.slice(1)
    ).join('');

    const methodPattern = new RegExp(`render${methodName.charAt(0).toUpperCase() + methodName.slice(1)}\\(magnitudes\\)[\\s\\S]*?(?=render\\w+\\(magnitudes\\)|generatePreview|$)`, 'i');
    const methodMatch = visualizerContent.match(methodPattern);

    if (!methodMatch) {
        return { hasMethod: false, usesGetColor: false, usesColorScheme: false };
    }

    const methodBody = methodMatch[0];

    // Check if method uses getColor or directly accesses COLOR_SCHEMES
    const usesGetColor = /this\.getColor\(/.test(methodBody);
    const usesColorScheme = /COLOR_SCHEMES\[this\.settings\.colorScheme\]/.test(methodBody);
    const hasHardcodedColors = /rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+/.test(methodBody);

    return {
        hasMethod: true,
        usesGetColor,
        usesColorScheme,
        hasHardcodedColors,
        supportsColors: usesGetColor || usesColorScheme
    };
}

// Main test
console.log('='.repeat(70));
console.log('COLOR SCHEME COMPATIBILITY TEST');
console.log('='.repeat(70));
console.log('');

const modes = extractModes();
const colorSchemes = extractColorSchemes();

console.log(`Testing ${modes.length} modes with ${colorSchemes.length} color schemes`);
console.log(`Total combinations to test: ${modes.length * colorSchemes.length}`);
console.log('');

// Test results
const results = {
    total: modes.length,
    fullSupport: 0,
    partialSupport: 0,
    noSupport: 0,
    byCategory: {}
};

console.log('TESTING MODE COLOR SUPPORT:');
console.log('-'.repeat(70));

modes.forEach(mode => {
    const verification = verifyColorSchemeUsage(mode.id);

    let status = '❌ No Support';
    let supportLevel = 'none';

    if (verification.supportsColors && !verification.hasHardcodedColors) {
        status = '✅ Full Support';
        supportLevel = 'full';
        results.fullSupport++;
    } else if (verification.supportsColors && verification.hasHardcodedColors) {
        status = '⚠️  Partial Support';
        supportLevel = 'partial';
        results.partialSupport++;
    } else {
        results.noSupport++;
    }

    // Track by category
    if (!results.byCategory[mode.category]) {
        results.byCategory[mode.category] = {
            total: 0,
            full: 0,
            partial: 0,
            none: 0
        };
    }

    results.byCategory[mode.category].total++;
    results.byCategory[mode.category][supportLevel]++;

    console.log(`${status} | ${mode.name.padEnd(30)} | ${mode.category.padEnd(12)} | ${verification.usesGetColor ? 'getColor' : verification.usesColorScheme ? 'direct' : 'none'}`);
});

console.log('');
console.log('='.repeat(70));
console.log('SUMMARY BY CATEGORY:');
console.log('-'.repeat(70));

Object.keys(results.byCategory).forEach(category => {
    const stats = results.byCategory[category];
    const percentage = ((stats.full / stats.total) * 100).toFixed(0);
    console.log(`${category.padEnd(15)} | ${stats.total} modes | ✅ ${stats.full} | ⚠️  ${stats.partial} | ❌ ${stats.none} | ${percentage}% full support`);
});

console.log('');
console.log('='.repeat(70));
console.log('OVERALL STATISTICS:');
console.log('-'.repeat(70));
console.log(`Total Modes: ${results.total}`);
console.log(`✅ Full Color Support: ${results.fullSupport} (${((results.fullSupport / results.total) * 100).toFixed(1)}%)`);
console.log(`⚠️  Partial Color Support: ${results.partialSupport} (${((results.partialSupport / results.total) * 100).toFixed(1)}%)`);
console.log(`❌ No Color Support: ${results.noSupport} (${((results.noSupport / results.total) * 100).toFixed(1)}%)`);
console.log('');

console.log('COLOR SCHEMES AVAILABLE:');
console.log('-'.repeat(70));
colorSchemes.forEach((scheme, i) => {
    console.log(`${(i + 1).toString().padStart(2)}. ${scheme.name} (${scheme.id})`);
});

console.log('');
console.log('='.repeat(70));

if (results.fullSupport === results.total) {
    console.log('🎉 SUCCESS! ALL MODES HAVE FULL COLOR SCHEME SUPPORT!');
} else if (results.fullSupport + results.partialSupport === results.total) {
    console.log(`✅ All modes support colors, but ${results.partialSupport} have hardcoded values`);
} else {
    console.log(`⚠️  WARNING: ${results.noSupport} modes do not support color customization`);
}

console.log('='.repeat(70));

// Exit with appropriate code
process.exit(results.noSupport > 0 ? 1 : 0);

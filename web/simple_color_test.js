#!/usr/bin/env node

/**
 * Simple color scheme test - directly checks for getColor usage
 */

const fs = require('fs');
const path = require('path');

const visualizerContent = fs.readFileSync(path.join(__dirname, 'visualizer.js'), 'utf8');

// Find all render methods
const renderMethods = [];
const methodMatches = visualizerContent.matchAll(/render(\w+)\(magnitudes\)\s*\{([\s\S]*?)(?=\n\s{4}\/\*\*|\n\s{4}generatePreview)/g);

for (const match of methodMatches) {
    const methodName = match[1];
    const methodBody = match[2];
    const usesGetColor = /this\.getColor\(/.test(methodBody);
    const usesScheme = /COLOR_SCHEMES\[this\.settings\.colorScheme\]/.test(methodBody);

    renderMethods.push({
        name: `render${methodName}`,
        usesGetColor,
        usesScheme,
        hasColorSupport: usesGetColor || usesScheme
    });
}

console.log('='.repeat(70));
console.log('SIMPLE COLOR SUPPORT TEST');
console.log('='.repeat(70));
console.log('');

console.log(`Found ${renderMethods.length} render methods\n`);

let supported = 0;
let notSupported = 0;

renderMethods.forEach(method => {
    const status = method.hasColorSupport ? '✅' : '❌';
    const impl = method.usesGetColor ? 'getColor()' : method.usesScheme ? 'COLOR_SCHEMES' : 'none';

    console.log(`${status} ${method.name.padEnd(35)} | ${impl}`);

    if (method.hasColorSupport) {
        supported++;
    } else {
        notSupported++;
    }
});

console.log('');
console.log('='.repeat(70));
console.log(`✅ Color Support: ${supported}/${renderMethods.length}`);
console.log(`❌ No Support: ${notSupported}/${renderMethods.length}`);
console.log(`Success Rate: ${((supported / renderMethods.length) * 100).toFixed(1)}%`);
console.log('='.repeat(70));

if (supported === renderMethods.length) {
    console.log('🎉 ALL RENDER METHODS USE COLOR SCHEMES!');
} else {
    console.log(`⚠️  ${notSupported} methods need color scheme support`);
}

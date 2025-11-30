#!/usr/bin/env node

/**
 * Quick test script to verify the framework works
 * Tests only 3 modes to validate setup
 */

const { AudioSpectrumTester, loadModes, ProgressTracker } = require('./visual-test-framework');
const path = require('path');
const fs = require('fs');

const CONFIG = {
    baseUrl: `file://${path.join(__dirname, 'web', 'index.html')}`,
    audioFile: path.join(__dirname, 'test-audio-20s.wav'),
    outputDir: path.join(__dirname, 'test-results-sample'),
    progressFile: path.join(__dirname, 'test-progress-sample.json'),

    timeouts: {
        navigation: 30000,
        videoGeneration: 300000,
        preview: 5000,
        settingsUpdate: 2000
    },

    videoSettings: {
        colorSchemes: ['apple_blue', 'sunset', 'ocean'],
        formats: ['square_1_1', 'vertical_9_16', 'landscape_16_9_hd'],
        fps: [30],
        backgrounds: ['transparent', 'dark']
    },

    parametersToTest: {
        barCount: [50, 100, 150],
        innerRadius: [50, 150, 250],
        smoothing: [0.5, 0.75, 0.95],
        background: ['soft_gray', 'white', 'dark', 'transparent'],
        enableGradient: [true, false]
    }
};

async function main() {
    console.log('='.repeat(70));
    console.log('AudioSpectrum Visual Testing Framework - SAMPLE TEST');
    console.log('='.repeat(70));
    console.log('');
    console.log('This will test 3 modes to verify the framework works correctly.');
    console.log('');

    // Load modes
    const allModes = loadModes();

    // Test only first 3 non-hidden modes
    const modesToTest = allModes.slice(0, 3);

    console.log(`Testing ${modesToTest.length} modes:`);
    modesToTest.forEach((mode, i) => {
        console.log(`  ${i + 1}. ${mode.name} (${mode.category})`);
    });
    console.log('');

    // Create output directory
    if (!fs.existsSync(CONFIG.outputDir)) {
        fs.mkdirSync(CONFIG.outputDir, { recursive: true });
    }

    const progressTracker = new ProgressTracker(CONFIG.progressFile);
    progressTracker.setTotalModes(modesToTest.length);

    const tester = new AudioSpectrumTester(CONFIG, progressTracker);

    try {
        await tester.init();

        for (let i = 0; i < modesToTest.length; i++) {
            const mode = modesToTest[i];

            console.log(`\n[${i + 1}/${modesToTest.length}] Testing: ${mode.name}`);
            console.log('-'.repeat(70));

            await tester.testMode(mode, i);
        }

        console.log('');
        console.log('='.repeat(70));
        console.log('✅ Sample test complete!');
        console.log(`Results saved to: ${CONFIG.outputDir}`);
        console.log('');
        console.log('If this worked correctly, you can run the full test with:');
        console.log('  npm run test:visual');
        console.log('='.repeat(70));

    } catch (error) {
        console.error('Fatal error:', error);
    } finally {
        await tester.close();
    }
}

if (require.main === module) {
    main().catch(console.error);
}

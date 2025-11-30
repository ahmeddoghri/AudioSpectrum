#!/usr/bin/env node

/**
 * AudioSpectrum Visual Testing Framework
 *
 * Tests all non-hidden modes with various parameter combinations
 * Generates videos and parameter variation screenshots for manual review
 *
 * Features:
 * - Resume capability (tracks progress in progress.json)
 * - Tests all Step 4 parameters at min/mid/max values
 * - Organized output: test-results/[mode_name]/
 * - Can run over multiple days
 */

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

// ============================================================================
// CONFIGURATION
// ============================================================================

const CONFIG = {
    baseUrl: `file://${path.join(__dirname, 'web', 'index.html')}`,
    audioFile: path.join(__dirname, 'test-audio-20s.wav'),
    outputDir: path.join(__dirname, 'test-results'),
    progressFile: path.join(__dirname, 'test-progress.json'),

    // Timeouts (in milliseconds)
    timeouts: {
        navigation: 30000,
        videoGeneration: 300000, // 5 minutes max per video
        preview: 5000,
        settingsUpdate: 2000
    },

    // Video settings variations (will cycle through for coverage)
    videoSettings: {
        colorSchemes: ['apple_blue', 'sunset', 'ocean', 'neon', 'fire'],
        formats: ['square_1_1', 'vertical_9_16', 'landscape_16_9_hd'],
        fps: [24, 30, 60],
        backgrounds: ['transparent', 'dark', 'white']
    },

    // Parameters to test (Step 4 - Advanced Settings)
    parametersToTest: {
        barCount: [50, 100, 150],
        innerRadius: [50, 150, 250],
        smoothing: [0.5, 0.75, 0.95],
        background: ['soft_gray', 'white', 'dark', 'transparent'],
        enableGradient: [true, false]
    }
};

// ============================================================================
// PROGRESS TRACKING
// ============================================================================

class ProgressTracker {
    constructor(progressFile) {
        this.progressFile = progressFile;
        this.progress = this.load();
    }

    load() {
        if (fs.existsSync(this.progressFile)) {
            try {
                return JSON.parse(fs.readFileSync(this.progressFile, 'utf8'));
            } catch (err) {
                console.warn('Failed to load progress file, starting fresh');
            }
        }
        return {
            startedAt: new Date().toISOString(),
            lastUpdated: new Date().toISOString(),
            completedModes: [],
            currentMode: null,
            stats: {
                totalModes: 0,
                completed: 0,
                failed: 0,
                skipped: 0
            }
        };
    }

    save() {
        this.progress.lastUpdated = new Date().toISOString();
        fs.writeFileSync(this.progressFile, JSON.stringify(this.progress, null, 2));
    }

    isModeCompleted(modeId) {
        return this.progress.completedModes.includes(modeId);
    }

    markModeCompleted(modeId, success = true) {
        if (!this.progress.completedModes.includes(modeId)) {
            this.progress.completedModes.push(modeId);
        }
        if (success) {
            this.progress.stats.completed++;
        } else {
            this.progress.stats.failed++;
        }
        this.save();
    }

    setCurrentMode(modeId) {
        this.progress.currentMode = modeId;
        this.save();
    }

    setTotalModes(count) {
        this.progress.stats.totalModes = count;
        this.save();
    }
}

// ============================================================================
// MODE LOADER
// ============================================================================

function loadModes() {
    const constantsPath = path.join(__dirname, 'web', 'constants.js');
    const content = fs.readFileSync(constantsPath, 'utf8');

    // Extract HIDDEN_MODES array
    const hiddenModesMatch = content.match(/const HIDDEN_MODES = \[([\s\S]*?)\];/);
    const hiddenModes = new Set();

    if (hiddenModesMatch) {
        const hiddenList = hiddenModesMatch[1];
        const matches = hiddenList.match(/'([^']+)'/g);
        if (matches) {
            matches.forEach(m => hiddenModes.add(m.replace(/'/g, '')));
        }
    }

    // Extract all modes
    const modes = [];
    const modeRegex = /(\w+):\s*\{[^}]*id:\s*'([^']+)'[^}]*name:\s*'([^']+)'[^}]*category:\s*'([^']+)'[^}]*\}/g;

    let match;
    while ((match = modeRegex.exec(content)) !== null) {
        const [, key, id, name, category] = match;

        // Only include non-hidden modes
        if (!hiddenModes.has(id) && !hiddenModes.has(key)) {
            modes.push({ key, id, name, category });
        }
    }

    console.log(`Loaded ${modes.length} non-hidden modes (${hiddenModes.size} hidden)`);
    return modes;
}

// ============================================================================
// BROWSER AUTOMATION
// ============================================================================

class AudioSpectrumTester {
    constructor(config, progressTracker) {
        this.config = config;
        this.progress = progressTracker;
        this.browser = null;
        this.page = null;
        this.settingsVariationIndex = 0;
    }

    async init() {
        console.log('Launching browser...');
        this.browser = await chromium.launch({
            headless: false, // Set to true for background execution
            downloadsPath: this.config.outputDir
        });

        const context = await this.browser.newContext({
            acceptDownloads: true,
            viewport: { width: 1920, height: 1080 }
        });

        this.page = await context.newPage();

        // Enable console logging for debugging
        this.page.on('console', msg => {
            if (msg.type() === 'error') {
                console.error('[Browser Error]', msg.text());
            }
        });
    }

    async navigateAndUploadAudio() {
        console.log('Navigating to app...');
        await this.page.goto(this.config.baseUrl, {
            waitUntil: 'networkidle',
            timeout: this.config.timeouts.navigation
        });

        console.log('Uploading audio file...');

        // Click "Get Started" if hero section is visible
        const heroBtn = await this.page.$('#heroGetStarted');
        if (heroBtn && await heroBtn.isVisible()) {
            await heroBtn.click();
            await this.page.waitForTimeout(500);
        }

        // Upload audio file
        const fileInput = await this.page.$('#audioInput');
        await fileInput.setInputFiles(this.config.audioFile);

        // Wait for file to be processed
        await this.page.waitForSelector('#fileInfo', {
            state: 'visible',
            timeout: 10000
        });

        console.log('Audio uploaded successfully');
        await this.page.waitForTimeout(2000);
    }

    async selectMode(mode) {
        console.log(`Selecting mode: ${mode.name} (${mode.id})`);

        // Make sure mode section is visible
        const modeSection = await this.page.$('#mode-section');
        if (!(await modeSection.isVisible())) {
            await this.page.waitForSelector('#mode-section', {
                state: 'visible',
                timeout: 5000
            });
        }

        // Search for the mode to make it visible
        const searchBox = await this.page.$('#modeSearch');
        await searchBox.fill(mode.name);
        await this.page.waitForTimeout(500);

        // Click the mode card
        const modeCard = await this.page.$(`[data-mode="${mode.id}"]`);
        if (!modeCard) {
            throw new Error(`Mode card not found: ${mode.id}`);
        }

        await modeCard.click();
        await this.page.waitForTimeout(1000);

        // Clear search
        await searchBox.fill('');
    }

    async configureVideoSettings(settingsIndex) {
        const settings = this.config.videoSettings;

        // Cycle through variations for coverage
        const colorScheme = settings.colorSchemes[settingsIndex % settings.colorSchemes.length];
        const format = settings.formats[settingsIndex % settings.formats.length];
        const fps = settings.fps[settingsIndex % settings.fps.length];
        const background = settings.backgrounds[settingsIndex % settings.backgrounds.length];

        console.log(`Configuring: ${colorScheme}, ${format}, ${fps}fps, ${background} bg`);

        // Wait for format section
        await this.page.waitForSelector('#format-section', {
            state: 'visible',
            timeout: 5000
        });

        // Select format
        const formatChip = await this.page.$(`[data-format="${format}"]`);
        if (formatChip) {
            await formatChip.click();
            await this.page.waitForTimeout(500);
        }

        // Select FPS
        const fpsChip = await this.page.$(`[data-fps="${fps}"]`);
        if (fpsChip) {
            await fpsChip.click();
            await this.page.waitForTimeout(500);
        }

        // Expand advanced settings
        await this.page.waitForSelector('#settings-section', {
            state: 'visible',
            timeout: 5000
        });

        const settingsToggle = await this.page.$('#settingsToggle');
        const isExpanded = await this.page.$eval('#settingsContent',
            el => el.style.display !== 'none'
        );

        if (!isExpanded) {
            await settingsToggle.click();
            await this.page.waitForTimeout(500);
        }

        // Set color scheme
        await this.page.selectOption('#colorScheme', colorScheme);
        await this.page.waitForTimeout(500);

        // Set background
        await this.page.selectOption('#background', background);
        await this.page.waitForTimeout(500);

        return { colorScheme, format, fps, background };
    }

    async generateAndDownloadVideo(mode, outputPath) {
        console.log('Generating video...');

        // Scroll to generate section
        await this.page.waitForSelector('#generate-section', {
            state: 'visible',
            timeout: 5000
        });

        // Click generate button
        const generateBtn = await this.page.$('#generateBtn');
        await generateBtn.click();

        // Wait for video generation to complete
        await this.page.waitForSelector('#download-section', {
            state: 'visible',
            timeout: this.config.timeouts.videoGeneration
        });

        console.log('Video generated, downloading...');

        // Set up download handler
        const downloadPromise = this.page.waitForEvent('download', {
            timeout: 30000
        });

        // Click download button
        const downloadBtn = await this.page.$('#downloadBtn');
        await downloadBtn.click();

        // Wait for download
        const download = await downloadPromise;
        const downloadPath = path.join(outputPath, `video_${Date.now()}.webm`);
        await download.saveAs(downloadPath);

        console.log(`Video saved: ${downloadPath}`);
        return downloadPath;
    }

    async captureParameterVariations(mode, outputPath) {
        console.log('Capturing parameter variations...');

        const params = this.config.parametersToTest;
        const screenshots = [];

        // Make sure we're at preview section and settings are visible
        await this.page.waitForSelector('#preview-section', {
            state: 'visible',
            timeout: 5000
        });

        const settingsToggle = await this.page.$('#settingsToggle');
        const isExpanded = await this.page.$eval('#settingsContent',
            el => el.style.display !== 'none'
        );

        if (!isExpanded) {
            await settingsToggle.click();
            await this.page.waitForTimeout(500);
        }

        // Test Bar Count
        for (const value of params.barCount) {
            await this.page.fill('#barCount', value.toString());
            await this.page.waitForTimeout(this.config.timeouts.settingsUpdate);

            const screenshotPath = path.join(outputPath, `param_barCount_${value}.png`);
            await this.page.locator('#previewCanvas').screenshot({
                path: screenshotPath
            });
            screenshots.push(screenshotPath);
            console.log(`  ✓ Bar Count: ${value}`);
        }

        // Reset to default
        await this.page.fill('#barCount', '100');
        await this.page.waitForTimeout(500);

        // Test Inner Radius
        for (const value of params.innerRadius) {
            await this.page.fill('#innerRadius', value.toString());
            await this.page.waitForTimeout(this.config.timeouts.settingsUpdate);

            const screenshotPath = path.join(outputPath, `param_innerRadius_${value}.png`);
            await this.page.locator('#previewCanvas').screenshot({
                path: screenshotPath
            });
            screenshots.push(screenshotPath);
            console.log(`  ✓ Inner Radius: ${value}`);
        }

        // Reset to default
        await this.page.fill('#innerRadius', '100');
        await this.page.waitForTimeout(500);

        // Test Smoothing
        for (const value of params.smoothing) {
            await this.page.fill('#smoothing', value.toString());
            await this.page.waitForTimeout(this.config.timeouts.settingsUpdate);

            const screenshotPath = path.join(outputPath, `param_smoothing_${value}.png`);
            await this.page.locator('#previewCanvas').screenshot({
                path: screenshotPath
            });
            screenshots.push(screenshotPath);
            console.log(`  ✓ Smoothing: ${value}`);
        }

        // Reset to default
        await this.page.fill('#smoothing', '0.85');
        await this.page.waitForTimeout(500);

        // Test Background
        for (const value of params.background) {
            await this.page.selectOption('#background', value);
            await this.page.waitForTimeout(this.config.timeouts.settingsUpdate);

            const screenshotPath = path.join(outputPath, `param_background_${value}.png`);
            await this.page.locator('#previewCanvas').screenshot({
                path: screenshotPath
            });
            screenshots.push(screenshotPath);
            console.log(`  ✓ Background: ${value}`);
        }

        // Reset to default
        await this.page.selectOption('#background', 'transparent');
        await this.page.waitForTimeout(500);

        // Test Enable Gradient
        for (const value of params.enableGradient) {
            const checkbox = await this.page.$('#enableGradient');
            const isChecked = await checkbox.isChecked();

            if (isChecked !== value) {
                await checkbox.click();
                await this.page.waitForTimeout(this.config.timeouts.settingsUpdate);
            }

            const screenshotPath = path.join(outputPath, `param_gradient_${value ? 'enabled' : 'disabled'}.png`);
            await this.page.locator('#previewCanvas').screenshot({
                path: screenshotPath
            });
            screenshots.push(screenshotPath);
            console.log(`  ✓ Gradient: ${value}`);
        }

        console.log(`Captured ${screenshots.length} parameter variation screenshots`);
        return screenshots;
    }

    async testMode(mode, modeIndex) {
        const modeFolder = path.join(
            this.config.outputDir,
            `${mode.id}_${mode.name.replace(/[^a-zA-Z0-9]/g, '_')}`
        );

        // Create mode folder
        if (!fs.existsSync(modeFolder)) {
            fs.mkdirSync(modeFolder, { recursive: true });
        }

        try {
            this.progress.setCurrentMode(mode.id);

            // Navigate and upload audio (only on first mode)
            if (modeIndex === 0 || !(await this.page.$('#fileInfo'))) {
                await this.navigateAndUploadAudio();
            } else {
                // Just reload the page to reset state
                await this.page.reload({ waitUntil: 'networkidle' });
                await this.page.waitForTimeout(2000);
            }

            // Select the mode
            await this.selectMode(mode);

            // Configure video settings with variation
            const settings = await this.configureVideoSettings(this.settingsVariationIndex++);

            // Save settings info
            const settingsInfo = {
                mode: mode,
                videoSettings: settings,
                timestamp: new Date().toISOString()
            };
            fs.writeFileSync(
                path.join(modeFolder, 'settings.json'),
                JSON.stringify(settingsInfo, null, 2)
            );

            // Generate and download video
            await this.generateAndDownloadVideo(mode, modeFolder);

            // Reset for parameter testing - reload page
            await this.page.reload({ waitUntil: 'networkidle' });
            await this.page.waitForTimeout(2000);

            // Re-upload audio and select mode with default settings
            await this.navigateAndUploadAudio();
            await this.selectMode(mode);

            // Use default settings for parameter testing
            await this.page.waitForSelector('#format-section', {
                state: 'visible',
                timeout: 5000
            });

            // Click through to preview with defaults
            const formatChip = await this.page.$('[data-format="square_1_1"]');
            if (formatChip) await formatChip.click();
            await this.page.waitForTimeout(500);

            // Capture parameter variations
            await this.captureParameterVariations(mode, modeFolder);

            // Mark as completed
            this.progress.markModeCompleted(mode.id, true);

            console.log(`✅ Mode ${mode.name} completed\n`);

        } catch (error) {
            console.error(`❌ Failed to test mode ${mode.name}:`, error.message);

            // Save error log
            fs.writeFileSync(
                path.join(modeFolder, 'error.log'),
                `Error: ${error.message}\n\nStack: ${error.stack}\n\nTimestamp: ${new Date().toISOString()}`
            );

            this.progress.markModeCompleted(mode.id, false);
        }
    }

    async close() {
        if (this.browser) {
            await this.browser.close();
        }
    }
}

// ============================================================================
// MAIN
// ============================================================================

async function main() {
    console.log('='.repeat(70));
    console.log('AudioSpectrum Visual Testing Framework');
    console.log('='.repeat(70));
    console.log('');

    // Load modes
    const allModes = loadModes();
    const progressTracker = new ProgressTracker(CONFIG.progressFile);
    progressTracker.setTotalModes(allModes.length);

    // Filter out already completed modes
    const modesToTest = allModes.filter(mode => !progressTracker.isModeCompleted(mode.id));

    console.log(`Total modes: ${allModes.length}`);
    console.log(`Completed: ${progressTracker.progress.stats.completed}`);
    console.log(`Remaining: ${modesToTest.length}`);
    console.log('');

    if (modesToTest.length === 0) {
        console.log('🎉 All modes have been tested!');
        return;
    }

    // Create output directory
    if (!fs.existsSync(CONFIG.outputDir)) {
        fs.mkdirSync(CONFIG.outputDir, { recursive: true });
    }

    // Initialize tester
    const tester = new AudioSpectrumTester(CONFIG, progressTracker);

    try {
        await tester.init();

        // Test each mode
        for (let i = 0; i < modesToTest.length; i++) {
            const mode = modesToTest[i];
            const overallIndex = allModes.indexOf(mode);

            console.log(`\n[${ overallIndex + 1}/${allModes.length}] Testing: ${mode.name}`);
            console.log('-'.repeat(70));

            await tester.testMode(mode, i);

            // Save progress after each mode
            progressTracker.save();
        }

        console.log('');
        console.log('='.repeat(70));
        console.log('✅ Testing complete!');
        console.log(`Results saved to: ${CONFIG.outputDir}`);
        console.log('='.repeat(70));

    } catch (error) {
        console.error('Fatal error:', error);
    } finally {
        await tester.close();
    }
}

// Handle interruption gracefully
process.on('SIGINT', () => {
    console.log('\n\nReceived interrupt signal. Saving progress...');
    process.exit(0);
});

// Run
if (require.main === module) {
    main().catch(console.error);
}

module.exports = { AudioSpectrumTester, loadModes, ProgressTracker };

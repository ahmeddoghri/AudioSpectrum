/**
 * Audio Spectrum Visualizer - Main Application
 * Coordinates all components and handles user interactions
 */

class AudioSpectrumApp {
    constructor() {
        // Core components
        this.audioProcessor = new AudioProcessor();
        this.visualizer = null;
        this.videoEncoder = new VideoEncoder();

        // Application state
        this.state = {
            audioFile: null,
            audioLoaded: false,
            selectedMode: DEFAULT_SETTINGS.mode,
            selectedFormat: DEFAULT_SETTINGS.format,
            settings: { ...DEFAULT_SETTINGS },
            isGenerating: false,
            generatedVideo: null
        };

        // DOM elements
        this.elements = {};

        // Initialize
        this.init();
    }

    /**
     * Initialize application
     */
    init() {
        // Check browser support
        const support = Utils.checkBrowserSupport();
        if (!support.supported) {
            Utils.showToast(
                `Your browser doesn't support required features: ${support.unsupported.join(', ')}`,
                'error',
                5000
            );
            return;
        }

        // Cache DOM elements
        this.cacheElements();

        // Set up event listeners
        this.setupEventListeners();

        // Initialize UI
        this.initializeUI();

        // Load saved settings
        this.loadSavedSettings();
    }

    /**
     * Cache DOM elements
     */
    cacheElements() {
        // Navigation
        this.elements.nav = document.getElementById('nav');

        // Hero
        this.elements.heroGetStarted = document.getElementById('heroGetStarted');

        // Upload section
        this.elements.uploadSection = document.getElementById('upload-section');
        this.elements.dropzone = document.getElementById('dropzone');
        this.elements.audioInput = document.getElementById('audioInput');
        this.elements.selectFileBtn = document.getElementById('selectFileBtn');
        this.elements.fileInfo = document.getElementById('fileInfo');
        this.elements.fileName = document.getElementById('fileName');
        this.elements.fileDuration = document.getElementById('fileDuration');
        this.elements.fileSize = document.getElementById('fileSize');
        this.elements.clearFileBtn = document.getElementById('clearFileBtn');
        this.elements.waveformCanvas = document.getElementById('waveformCanvas');

        // Mode section
        this.elements.modeSection = document.getElementById('mode-section');
        this.elements.modeGrid = document.getElementById('modeGrid');

        // Format section
        this.elements.formatSection = document.getElementById('format-section');
        this.elements.formatChips = document.getElementById('formatChips');
        this.elements.customFormat = document.getElementById('customFormat');
        this.elements.customWidth = document.getElementById('customWidth');
        this.elements.customHeight = document.getElementById('customHeight');
        this.elements.fpsChips = document.getElementById('fpsChips');

        // Settings section
        this.elements.settingsSection = document.getElementById('settings-section');
        this.elements.settingsToggle = document.getElementById('settingsToggle');
        this.elements.settingsContent = document.getElementById('settingsContent');
        this.elements.colorScheme = document.getElementById('colorScheme');
        this.elements.customColorPicker = document.getElementById('customColorPicker');
        this.elements.customColor = document.getElementById('customColor');
        this.elements.barCount = document.getElementById('barCount');
        this.elements.barCountValue = document.getElementById('barCountValue');
        this.elements.innerRadius = document.getElementById('innerRadius');
        this.elements.innerRadiusValue = document.getElementById('innerRadiusValue');
        this.elements.smoothing = document.getElementById('smoothing');
        this.elements.smoothingValue = document.getElementById('smoothingValue');
        this.elements.background = document.getElementById('background');
        this.elements.enableGradient = document.getElementById('enableGradient');

        // Preview section
        this.elements.previewSection = document.getElementById('preview-section');
        this.elements.previewCanvas = document.getElementById('previewCanvas');
        this.elements.previewPlayBtn = document.getElementById('previewPlayBtn');

        // Generate section
        this.elements.generateSection = document.getElementById('generate-section');
        this.elements.generateBtn = document.getElementById('generateBtn');
        this.elements.progressContainer = document.getElementById('progressContainer');
        this.elements.progressStatus = document.getElementById('progressStatus');
        this.elements.progressPercentage = document.getElementById('progressPercentage');
        this.elements.progressFill = document.getElementById('progressFill');
        this.elements.progressTime = document.getElementById('progressTime');
        this.elements.cancelBtn = document.getElementById('cancelBtn');

        // Download section
        this.elements.downloadSection = document.getElementById('download-section');
        this.elements.videoPreview = document.getElementById('videoPreview');
        this.elements.downloadSize = document.getElementById('downloadSize');
        this.elements.downloadDuration = document.getElementById('downloadDuration');
        this.elements.downloadFormat = document.getElementById('downloadFormat');
        this.elements.downloadBtn = document.getElementById('downloadBtn');
        this.elements.createAnotherBtn = document.getElementById('createAnotherBtn');
    }

    /**
     * Set up event listeners
     */
    setupEventListeners() {
        // Hero
        this.elements.heroGetStarted.addEventListener('click', () => {
            Utils.scrollToElement('upload-section');
        });

        // Navigation scroll effect
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                this.elements.nav.classList.add('scrolled');
            } else {
                this.elements.nav.classList.remove('scrolled');
            }
        });

        // File upload
        this.elements.selectFileBtn.addEventListener('click', () => {
            this.elements.audioInput.click();
        });

        this.elements.audioInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) {
                this.handleFileUpload(file);
            }
        });

        // Drag and drop
        this.elements.dropzone.addEventListener('dragover', (e) => {
            e.preventDefault();
            this.elements.dropzone.classList.add('dragover');
        });

        this.elements.dropzone.addEventListener('dragleave', () => {
            this.elements.dropzone.classList.remove('dragover');
        });

        this.elements.dropzone.addEventListener('drop', (e) => {
            e.preventDefault();
            this.elements.dropzone.classList.remove('dragover');

            const file = e.dataTransfer.files[0];
            if (file) {
                this.handleFileUpload(file);
            }
        });

        // Clear file
        this.elements.clearFileBtn.addEventListener('click', () => {
            this.clearFile();
        });

        // FPS selector
        const fpsButtons = this.elements.fpsChips.querySelectorAll('.chip');
        fpsButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                fpsButtons.forEach(b => b.classList.remove('chip-selected'));
                btn.classList.add('chip-selected');
                this.state.settings.fps = parseInt(btn.dataset.fps);
            });
        });

        // Settings accordion
        this.elements.settingsToggle.addEventListener('click', () => {
            const isOpen = this.elements.settingsToggle.classList.toggle('open');
            this.elements.settingsContent.style.display = isOpen ? 'block' : 'none';
        });

        // Color scheme selector
        this.elements.colorScheme.addEventListener('change', (e) => {
            this.state.settings.colorScheme = e.target.value;
            this.elements.customColorPicker.style.display =
                e.target.value === 'custom' ? 'block' : 'none';
            this.updatePreview();
        });

        // Custom color
        this.elements.customColor.addEventListener('change', (e) => {
            const rgb = Utils.hexToRgb(e.target.value);
            if (rgb) {
                COLOR_SCHEMES.custom.primary = rgb;
                this.updatePreview();
            }
        });

        // Sliders
        this.elements.barCount.addEventListener('input', (e) => {
            this.elements.barCountValue.textContent = e.target.value;
            this.state.settings.numBars = parseInt(e.target.value);
            this.debouncedUpdatePreview();
        });

        this.elements.innerRadius.addEventListener('input', (e) => {
            this.elements.innerRadiusValue.textContent = e.target.value;
            this.state.settings.innerRadius = parseInt(e.target.value);
            this.debouncedUpdatePreview();
        });

        this.elements.smoothing.addEventListener('input', (e) => {
            this.elements.smoothingValue.textContent = e.target.value;
            this.state.settings.smoothing = parseFloat(e.target.value);
            this.debouncedUpdatePreview();
        });

        // Background selector
        this.elements.background.addEventListener('change', (e) => {
            this.state.settings.background = e.target.value;
            this.updatePreview();
        });

        // Gradient toggle
        this.elements.enableGradient.addEventListener('change', (e) => {
            this.state.settings.gradient = e.target.checked;
            this.updatePreview();
        });

        // Preview play
        this.elements.previewPlayBtn.addEventListener('click', () => {
            this.playPreview();
        });

        // Generate video
        this.elements.generateBtn.addEventListener('click', () => {
            this.generateVideo();
        });

        // Cancel generation
        this.elements.cancelBtn.addEventListener('click', () => {
            this.cancelGeneration();
        });

        // Download video
        this.elements.downloadBtn.addEventListener('click', () => {
            this.downloadVideo();
        });

        // Create another
        this.elements.createAnotherBtn.addEventListener('click', () => {
            this.resetApp();
        });
    }

    /**
     * Initialize UI
     */
    initializeUI() {
        // Populate mode grid
        this.populateModeGrid();

        // Populate format chips
        this.populateFormatChips();

        // Initialize preview canvas
        this.visualizer = new Visualizer(this.elements.previewCanvas, this.state.settings);

        // Create debounced update preview function
        this.debouncedUpdatePreview = Utils.debounce(() => this.updatePreview(), 300);
    }

    /**
     * Populate mode grid
     */
    populateModeGrid() {
        Object.values(VISUALIZATION_MODES).forEach(mode => {
            const card = document.createElement('div');
            card.className = 'mode-card';
            card.dataset.mode = mode.id;

            card.innerHTML = `
                <div class="mode-preview">
                    <canvas width="280" height="280"></canvas>
                </div>
                <h3 class="mode-name">${mode.name}</h3>
                <p class="mode-description">${mode.description}</p>
                <button class="btn btn-secondary">
                    <span>Select</span>
                    <svg class="checkmark" width="16" height="16" viewBox="0 0 16 16" fill="none">
                        <path d="M3 8L6 11L13 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </button>
            `;

            card.addEventListener('click', () => {
                this.selectMode(mode.id);
            });

            this.elements.modeGrid.appendChild(card);

            // Generate preview for this mode
            this.generateModePreview(card.querySelector('canvas'), mode.id);
        });
    }

    /**
     * Generate mode preview
     */
    generateModePreview(canvas, modeId) {
        const tempSettings = {
            ...DEFAULT_SETTINGS,
            mode: modeId,
            numBars: 48
        };

        const tempVisualizer = new Visualizer(canvas, tempSettings);

        // Generate demo magnitudes
        const magnitudes = new Float32Array(48);
        for (let i = 0; i < magnitudes.length; i++) {
            magnitudes[i] = 0.3 + Math.random() * 0.4 + Math.sin(i * 0.2) * 0.2;
        }

        tempVisualizer.render(magnitudes);
    }

    /**
     * Populate format chips
     */
    populateFormatChips() {
        Object.entries(FORMAT_PRESETS).forEach(([key, preset]) => {
            const chip = document.createElement('button');
            chip.className = 'chip';
            chip.dataset.format = key;
            chip.innerHTML = `
                <span>${preset.name}</span>
                <small>${preset.aspectRatio}</small>
            `;

            chip.addEventListener('click', () => {
                this.selectFormat(key);
            });

            this.elements.formatChips.appendChild(chip);
        });
    }

    /**
     * Handle file upload
     */
    async handleFileUpload(file) {
        // Validate file
        const validation = Utils.validateFile(file);
        if (!validation.valid) {
            Utils.showToast(validation.errors[0], 'error');
            return;
        }

        try {
            // Show loading state
            Utils.showToast('Loading audio file...', 'info');

            // Load audio
            const audioInfo = await this.audioProcessor.loadAudio(file);

            // Update state
            this.state.audioFile = file;
            this.state.audioLoaded = true;

            // Update UI
            this.elements.dropzone.style.display = 'none';
            this.elements.fileInfo.style.display = 'block';
            this.elements.fileName.textContent = file.name;
            this.elements.fileDuration.textContent = Utils.formatTime(audioInfo.duration);
            this.elements.fileSize.textContent = Utils.formatBytes(file.size);

            // Generate waveform
            const waveformData = await this.audioProcessor.getWaveformData(800);
            Utils.drawWaveform(this.elements.waveformCanvas, waveformData);

            // Show next sections
            this.elements.modeSection.style.display = 'block';
            this.elements.formatSection.style.display = 'block';
            this.elements.settingsSection.style.display = 'block';
            this.elements.previewSection.style.display = 'block';
            this.elements.generateSection.style.display = 'block';

            // Update preview
            this.updatePreview();

            Utils.showToast('Audio loaded successfully!', 'success');

        } catch (error) {
            console.error('Error loading audio:', error);
            Utils.showToast(error.message || 'Failed to load audio file', 'error');
        }
    }

    /**
     * Clear file
     */
    clearFile() {
        this.audioProcessor.dispose();
        this.audioProcessor = new AudioProcessor();

        this.state.audioFile = null;
        this.state.audioLoaded = false;

        this.elements.audioInput.value = '';
        this.elements.dropzone.style.display = 'block';
        this.elements.fileInfo.style.display = 'none';

        // Hide sections
        this.elements.modeSection.style.display = 'none';
        this.elements.formatSection.style.display = 'none';
        this.elements.settingsSection.style.display = 'none';
        this.elements.previewSection.style.display = 'none';
        this.elements.generateSection.style.display = 'none';
    }

    /**
     * Select visualization mode
     */
    selectMode(modeId) {
        this.state.selectedMode = modeId;
        this.state.settings.mode = modeId;

        // Update UI
        const cards = this.elements.modeGrid.querySelectorAll('.mode-card');
        cards.forEach(card => {
            if (card.dataset.mode === modeId) {
                card.classList.add('selected');
            } else {
                card.classList.remove('selected');
            }
        });

        // Update preview
        this.updatePreview();

        // Scroll to format section
        setTimeout(() => {
            Utils.scrollToElement('format-section');
        }, 300);
    }

    /**
     * Select format
     */
    selectFormat(formatKey) {
        this.state.selectedFormat = formatKey;
        const preset = FORMAT_PRESETS[formatKey];

        // Update settings
        this.state.settings.width = preset.width;
        this.state.settings.height = preset.height;

        // Update UI
        const chips = this.elements.formatChips.querySelectorAll('.chip');
        chips.forEach(chip => {
            if (chip.dataset.format === formatKey) {
                chip.classList.add('chip-selected');
            } else {
                chip.classList.remove('chip-selected');
            }
        });

        // Show/hide custom format inputs
        this.elements.customFormat.style.display =
            formatKey === 'custom' ? 'flex' : 'none';

        if (formatKey === 'custom') {
            this.elements.customWidth.value = preset.width;
            this.elements.customHeight.value = preset.height;
        }

        // Update preview canvas dimensions
        this.updatePreviewDimensions();
    }

    /**
     * Update preview dimensions
     */
    updatePreviewDimensions() {
        const aspectRatio = this.state.settings.width / this.state.settings.height;
        const maxSize = 400;

        let canvasWidth, canvasHeight;

        if (aspectRatio > 1) {
            // Landscape
            canvasWidth = maxSize;
            canvasHeight = maxSize / aspectRatio;
        } else {
            // Portrait or square
            canvasHeight = maxSize;
            canvasWidth = maxSize * aspectRatio;
        }

        this.elements.previewCanvas.width = canvasWidth;
        this.elements.previewCanvas.height = canvasHeight;

        this.visualizer.updateDimensions(canvasWidth, canvasHeight);
        this.updatePreview();
    }

    /**
     * Update preview
     */
    updatePreview() {
        if (!this.visualizer) return;

        this.visualizer.updateSettings(this.state.settings);

        // Generate demo magnitudes or use real-time data
        const magnitudes = new Float32Array(this.state.settings.numBars);
        for (let i = 0; i < magnitudes.length; i++) {
            magnitudes[i] = 0.3 + Math.random() * 0.4 + Math.sin(i * 0.2 + Date.now() * 0.001) * 0.2;
        }

        this.visualizer.render(magnitudes);
    }

    /**
     * Play preview with audio
     */
    playPreview() {
        if (!this.state.audioLoaded) {
            Utils.showToast('Please upload an audio file first', 'warning');
            return;
        }

        if (this.audioProcessor.isPlaying) {
            this.audioProcessor.stop();
            this.elements.previewPlayBtn.innerHTML = `
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                    <path d="M4 2L12 8L4 14Z" fill="currentColor"/>
                </svg>
                Play Preview
            `;
            return;
        }

        // Play audio
        this.audioProcessor.play();
        this.elements.previewPlayBtn.innerHTML = `
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <rect x="4" y="2" width="3" height="12" fill="currentColor"/>
                <rect x="9" y="2" width="3" height="12" fill="currentColor"/>
            </svg>
            Pause
        `;

        // Animate preview
        const animate = () => {
            if (this.audioProcessor.isPlaying) {
                const magnitudes = this.audioProcessor.getRealTimeMagnitudes(this.state.settings.numBars);
                if (magnitudes) {
                    this.visualizer.render(magnitudes);
                }
                requestAnimationFrame(animate);
            } else {
                this.elements.previewPlayBtn.innerHTML = `
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                        <path d="M4 2L12 8L4 14Z" fill="currentColor"/>
                    </svg>
                    Play Preview
                `;
            }
        };

        animate();
    }

    /**
     * Generate video
     */
    async generateVideo() {
        if (!this.state.audioLoaded) {
            Utils.showToast('Please upload an audio file first', 'warning');
            return;
        }

        if (!this.state.selectedMode) {
            Utils.showToast('Please select a visualization mode', 'warning');
            return;
        }

        try {
            this.state.isGenerating = true;

            // Update UI
            this.elements.generateBtn.style.display = 'none';
            this.elements.progressContainer.style.display = 'block';

            // Set up video encoder callbacks
            this.videoEncoder.setProgressCallback((progress) => {
                this.elements.progressStatus.textContent = progress.status;
                this.elements.progressPercentage.textContent = `${Math.round(progress.percentage)}%`;
                this.elements.progressFill.style.width = `${progress.percentage}%`;

                if (progress.eta) {
                    this.elements.progressTime.textContent = `Estimated time: ${progress.eta}`;
                }
            });

            this.videoEncoder.setCompleteCallback((videoBlob) => {
                this.state.generatedVideo = videoBlob;
                this.showDownloadSection();
            });

            this.videoEncoder.setErrorCallback((error) => {
                console.error('Video generation error:', error);
                Utils.showToast(error.message || 'Failed to generate video', 'error');
                this.resetGenerateSection();
            });

            // Get custom dimensions if custom format is selected
            if (this.state.selectedFormat === 'custom') {
                this.state.settings.width = parseInt(this.elements.customWidth.value);
                this.state.settings.height = parseInt(this.elements.customHeight.value);
            }

            // Generate video
            await this.videoEncoder.generateVideo(
                this.audioProcessor,
                this.visualizer,
                this.state.settings
            );

        } catch (error) {
            console.error('Error generating video:', error);
            Utils.showToast(error.message || 'Failed to generate video', 'error');
            this.resetGenerateSection();
        }
    }

    /**
     * Cancel video generation
     */
    cancelGeneration() {
        this.videoEncoder.cancel();
        this.resetGenerateSection();
        Utils.showToast('Video generation cancelled', 'info');
    }

    /**
     * Reset generate section
     */
    resetGenerateSection() {
        this.state.isGenerating = false;
        this.elements.generateBtn.style.display = 'block';
        this.elements.progressContainer.style.display = 'none';
        this.elements.progressFill.style.width = '0%';
    }

    /**
     * Show download section
     */
    showDownloadSection() {
        this.resetGenerateSection();

        // Show download section
        this.elements.downloadSection.style.display = 'block';

        // Set video preview
        const videoUrl = URL.createObjectURL(this.state.generatedVideo);
        this.elements.videoPreview.src = videoUrl;

        // Update file info
        this.elements.downloadSize.textContent = Utils.formatBytes(this.state.generatedVideo.size);
        this.elements.downloadDuration.textContent = Utils.formatTime(this.audioProcessor.duration);
        this.elements.downloadFormat.textContent = 'WebM';

        // Scroll to download section
        setTimeout(() => {
            Utils.scrollToElement('download-section');
        }, 300);

        Utils.showToast('Video generated successfully!', 'success');
    }

    /**
     * Download video
     */
    downloadVideo() {
        if (!this.state.generatedVideo) return;

        const filename = Utils.createFilename(this.state.selectedMode, 'webm');
        Utils.downloadBlob(this.state.generatedVideo, filename);

        Utils.showToast('Download started!', 'success');
    }

    /**
     * Reset app
     */
    resetApp() {
        // Clean up
        this.audioProcessor.dispose();
        this.audioProcessor = new AudioProcessor();

        if (this.state.generatedVideo) {
            URL.revokeObjectURL(this.elements.videoPreview.src);
        }

        // Reset state
        this.state = {
            audioFile: null,
            audioLoaded: false,
            selectedMode: DEFAULT_SETTINGS.mode,
            selectedFormat: DEFAULT_SETTINGS.format,
            settings: { ...DEFAULT_SETTINGS },
            isGenerating: false,
            generatedVideo: null
        };

        // Reset UI
        this.elements.audioInput.value = '';
        this.elements.dropzone.style.display = 'block';
        this.elements.fileInfo.style.display = 'none';
        this.elements.modeSection.style.display = 'none';
        this.elements.formatSection.style.display = 'none';
        this.elements.settingsSection.style.display = 'none';
        this.elements.previewSection.style.display = 'none';
        this.elements.generateSection.style.display = 'none';
        this.elements.downloadSection.style.display = 'none';

        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });

        Utils.showToast('Ready for a new project!', 'success');
    }

    /**
     * Load saved settings
     */
    loadSavedSettings() {
        const saved = Utils.loadSettings();
        if (saved) {
            this.state.settings = { ...this.state.settings, ...saved };

            // Update UI elements
            this.elements.colorScheme.value = saved.colorScheme || DEFAULT_SETTINGS.colorScheme;
            this.elements.barCount.value = saved.numBars || DEFAULT_SETTINGS.numBars;
            this.elements.barCountValue.textContent = saved.numBars || DEFAULT_SETTINGS.numBars;
            this.elements.innerRadius.value = saved.innerRadius || DEFAULT_SETTINGS.innerRadius;
            this.elements.innerRadiusValue.textContent = saved.innerRadius || DEFAULT_SETTINGS.innerRadius;
            this.elements.smoothing.value = saved.smoothing || DEFAULT_SETTINGS.smoothing;
            this.elements.smoothingValue.textContent = saved.smoothing || DEFAULT_SETTINGS.smoothing;
            this.elements.background.value = saved.background || DEFAULT_SETTINGS.background;
            this.elements.enableGradient.checked = saved.gradient !== undefined ? saved.gradient : DEFAULT_SETTINGS.gradient;
        }
    }

    /**
     * Save current settings
     */
    saveSettings() {
        Utils.saveSettings(this.state.settings);
    }
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.app = new AudioSpectrumApp();
});

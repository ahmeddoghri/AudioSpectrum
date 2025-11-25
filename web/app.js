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
            generatedVideo: null,
            downloadFormat: 'webm' // Default download format
        };

        // DOM elements
        this.elements = {};

        // Preview animation state
        this.previewAnimationId = null;
        this.previewTime = 0;

        // Preview selection window state
        this.previewSelectionState = {
            startTime: 0,
            duration: 15,
            isDragging: false,
            dragStartX: 0,
            windowStartX: 0
        };

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
        this.elements.waveformProgress = document.getElementById('waveformProgress');
        this.elements.waveformContainer = document.getElementById('waveformContainer');
        this.elements.waveformCursor = document.getElementById('waveformCursor');
        this.elements.waveformSelectionWindow = document.getElementById('waveformSelectionWindow');
        this.elements.audioElement = document.getElementById('audioElement');
        this.elements.playButton = document.getElementById('playButton');
        this.elements.currentTime = document.getElementById('currentTime');
        this.elements.totalTime = document.getElementById('totalTime');
        this.elements.volumeSlider = document.getElementById('volumeSlider');

        // Mode section
        this.elements.modeSection = document.getElementById('mode-section');
        this.elements.modeGrid = document.getElementById('modeGrid');
        this.elements.modeSearch = document.getElementById('modeSearch');
        this.elements.clearSearch = document.getElementById('clearSearch');
        this.elements.categoryFilter = document.getElementById('categoryFilter');
        this.elements.visibleModeCount = document.getElementById('visibleModeCount');
        this.elements.noModesMessage = document.getElementById('noModesMessage');
        this.elements.resetFilters = document.getElementById('resetFilters');

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
        this.elements.gradientColors = document.getElementById('gradientColors');
        this.elements.gradientColor1 = document.getElementById('gradientColor1');
        this.elements.gradientColor2 = document.getElementById('gradientColor2');
        this.elements.gradientColor3 = document.getElementById('gradientColor3');
        this.elements.gradientColor3Group = document.getElementById('gradientColor3Group');
        this.elements.gradientPreview = document.getElementById('gradientPreview');
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
        this.elements.downloadFormatDisplay = document.getElementById('downloadFormatDisplay');
        this.elements.downloadFormatChips = document.getElementById('downloadFormatChips');
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

        // Audio player controls
        this.elements.playButton.addEventListener('click', () => {
            this.togglePlayback();
        });

        this.elements.audioElement.addEventListener('timeupdate', () => {
            this.updatePlaybackProgress();
        });

        this.elements.audioElement.addEventListener('ended', () => {
            this.handleAudioEnded();
        });

        this.elements.volumeSlider.addEventListener('input', (e) => {
            this.updateVolume(e.target.value / 100);
        });

        // Waveform interaction
        this.elements.waveformContainer.addEventListener('click', (e) => {
            this.handleWaveformClick(e);
        });

        this.elements.waveformContainer.addEventListener('mousemove', (e) => {
            this.handleWaveformHover(e);
        });

        this.elements.waveformContainer.addEventListener('mouseleave', () => {
            this.elements.waveformCursor.style.opacity = '0';
        });

        // Selection window dragging
        this.elements.waveformSelectionWindow.addEventListener('mousedown', (e) => {
            this.handleSelectionWindowDragStart(e);
        });

        document.addEventListener('mousemove', (e) => {
            this.handleSelectionWindowDrag(e);
        });

        document.addEventListener('mouseup', () => {
            this.handleSelectionWindowDragEnd();
        });

        // Mode search and filter
        this.elements.modeSearch.addEventListener('input', (e) => {
            const searchTerm = e.target.value;
            this.elements.clearSearch.style.display = searchTerm ? 'flex' : 'none';
            this.filterModes();
        });

        this.elements.clearSearch.addEventListener('click', () => {
            this.elements.modeSearch.value = '';
            this.elements.clearSearch.style.display = 'none';
            this.filterModes();
        });

        this.elements.categoryFilter.addEventListener('change', () => {
            this.filterModes();
        });

        this.elements.resetFilters.addEventListener('click', () => {
            this.elements.modeSearch.value = '';
            this.elements.categoryFilter.value = 'classic';
            this.elements.clearSearch.style.display = 'none';
            this.filterModes();
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
            const scheme = e.target.value;
            this.state.settings.colorScheme = scheme;

            // Show/hide gradient color pickers based on scheme
            const schemeData = COLOR_SCHEMES[scheme];
            if (schemeData && schemeData.customizable) {
                this.elements.gradientColors.style.display = 'flex';

                // Initialize color pickers with scheme colors
                this.elements.gradientColor1.value = Utils.rgbToHex(schemeData.primary);
                this.elements.gradientColor2.value = Utils.rgbToHex(schemeData.secondary);

                // Show 3rd color picker for 3-color gradients
                if (schemeData.colorCount === 3) {
                    this.elements.gradientColor3Group.style.display = 'flex';
                    this.elements.gradientColor3.value = Utils.rgbToHex(schemeData.tertiary);
                } else {
                    this.elements.gradientColor3Group.style.display = 'none';
                }
                this.updateGradientPreview();
            } else {
                this.elements.gradientColors.style.display = 'none';
            }

            this.updatePreview();
        });

        // Gradient color pickers
        this.elements.gradientColor1.addEventListener('input', (e) => {
            const rgb = Utils.hexToRgb(e.target.value);
            if (rgb) {
                const scheme = this.state.settings.colorScheme;
                const schemeData = COLOR_SCHEMES[scheme];
                if (schemeData && schemeData.customizable) {
                    COLOR_SCHEMES[scheme].primary = rgb;
                }
                this.updateGradientPreview();
                this.updatePreview();
            }
        });

        this.elements.gradientColor2.addEventListener('input', (e) => {
            const rgb = Utils.hexToRgb(e.target.value);
            if (rgb) {
                const scheme = this.state.settings.colorScheme;
                const schemeData = COLOR_SCHEMES[scheme];
                if (schemeData && schemeData.customizable) {
                    COLOR_SCHEMES[scheme].secondary = rgb;
                }
                this.updateGradientPreview();
                this.updatePreview();
            }
        });

        this.elements.gradientColor3.addEventListener('input', (e) => {
            const rgb = Utils.hexToRgb(e.target.value);
            if (rgb) {
                const scheme = this.state.settings.colorScheme;
                const schemeData = COLOR_SCHEMES[scheme];
                if (schemeData && schemeData.customizable && schemeData.colorCount === 3) {
                    COLOR_SCHEMES[scheme].tertiary = rgb;
                }
                this.updateGradientPreview();
                this.updatePreview();
            }
        });

        // Custom color
        if (this.elements.customColor) {
            this.elements.customColor.addEventListener('change', (e) => {
                const rgb = Utils.hexToRgb(e.target.value);
                if (rgb) {
                    COLOR_SCHEMES.custom.primary = rgb;
                    this.updatePreview();
                }
            });
        }

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

        // Download format selector
        const downloadFormatButtons = this.elements.downloadFormatChips.querySelectorAll('.chip');
        downloadFormatButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                downloadFormatButtons.forEach(b => b.classList.remove('chip-selected'));
                btn.classList.add('chip-selected');
                this.state.downloadFormat = btn.dataset.format;
                this.updateDownloadFormatDisplay();
            });
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

        // Initialize preview canvas first (needed before selectFormat)
        this.visualizer = new Visualizer(this.elements.previewCanvas, this.state.settings);

        // Initialize format dimensions from default settings
        this.selectFormat(this.state.selectedFormat);

        // Create debounced update preview function
        this.debouncedUpdatePreview = Utils.debounce(() => this.updatePreview(), 300);
    }

    /**
     * Populate mode grid
     */
    populateModeGrid() {
        Object.values(VISUALIZATION_MODES)
            .filter(mode => !HIDDEN_MODES.includes(mode.id))
            .forEach(mode => {
            const card = document.createElement('div');
            card.className = 'mode-card';
            card.dataset.mode = mode.id;
            card.dataset.category = mode.category.toLowerCase();
            card.dataset.name = mode.name.toLowerCase();
            card.dataset.description = mode.description.toLowerCase();
            card.dataset.tags = mode.tags.join(' ').toLowerCase();

            card.innerHTML = `
                <div class="mode-preview">
                    <canvas width="280" height="280"></canvas>
                </div>
                <div class="mode-category-badge">${mode.category}</div>
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

            const canvas = card.querySelector('canvas');

            // Add hover animation
            let animationId = null;
            let hoverVisualizer = null;

            card.addEventListener('mouseenter', () => {
                // Create a visualizer for this mode
                const tempSettings = {
                    ...DEFAULT_SETTINGS,
                    mode: mode.id,
                    numBars: 48,
                    // Use small settings for 280x280 preview canvas
                    innerRadius: 50,  // Adjusted for better visibility in preview
                    barWidthMultiplier: 1.0
                };
                hoverVisualizer = new Visualizer(canvas, tempSettings);

                // Start animation loop
                let animationTime = 0;
                const animate = () => {
                    // Generate animated magnitudes that change over time
                    const magnitudes = new Float32Array(48);
                    for (let i = 0; i < magnitudes.length; i++) {
                        // Create smooth animated values with controlled range for preview
                        const value =
                            0.25 +
                            Math.sin(animationTime * 0.02 + i * 0.15) * 0.15 +
                            Math.sin(animationTime * 0.03 + i * 0.08) * 0.12 +
                            Math.cos(animationTime * 0.015 + i * 0.1) * 0.1;
                        // Clamp to safe range for 280x280 canvas
                        magnitudes[i] = Math.min(Math.max(value, 0.15), 0.65);
                    }

                    hoverVisualizer.render(magnitudes);
                    animationTime++;
                    animationId = requestAnimationFrame(animate);
                };

                animate();
            });

            card.addEventListener('mouseleave', () => {
                // Stop animation
                if (animationId) {
                    cancelAnimationFrame(animationId);
                    animationId = null;
                }

                // Restore static preview
                this.generateModePreview(canvas, mode.id);
                hoverVisualizer = null;
            });

            // Generate initial static preview for this mode
            this.generateModePreview(canvas, mode.id);

            this.elements.modeGrid.appendChild(card);
        });

        // Initial count update
        this.updateModeCount();
    }

    /**
     * Filter modes based on search and category
     */
    filterModes() {
        const searchTerm = this.elements.modeSearch.value.toLowerCase().trim();
        const selectedCategory = this.elements.categoryFilter.value;

        const cards = this.elements.modeGrid.querySelectorAll('.mode-card');
        let visibleCount = 0;

        cards.forEach(card => {
            const name = card.dataset.name;
            const description = card.dataset.description;
            const category = card.dataset.category;
            const tags = card.dataset.tags;

            // Check search match
            const searchMatch = !searchTerm ||
                                name.includes(searchTerm) ||
                                description.includes(searchTerm) ||
                                tags.includes(searchTerm);

            // Check category match
            const categoryMatch = selectedCategory === 'all' ||
                                  category === selectedCategory;

            // Show/hide card based on filters
            if (searchMatch && categoryMatch) {
                card.style.display = 'block';
                visibleCount++;
            } else {
                card.style.display = 'none';
            }
        });

        // Update count and show/hide no results message
        this.updateModeCount(visibleCount);

        if (visibleCount === 0) {
            this.elements.noModesMessage.style.display = 'flex';
            this.elements.modeGrid.style.display = 'none';
        } else {
            this.elements.noModesMessage.style.display = 'none';
            this.elements.modeGrid.style.display = 'grid';
        }
    }

    /**
     * Update mode count display
     */
    updateModeCount(count) {
        if (count === undefined) {
            const allModes = Object.values(VISUALIZATION_MODES);
            const visibleModes = allModes.filter(mode => !HIDDEN_MODES.includes(mode.id));
            count = visibleModes.length;
        }
        this.elements.visibleModeCount.textContent = count;
    }

    /**
     * Generate mode preview
     */
    generateModePreview(canvas, modeId) {
        const tempSettings = {
            ...DEFAULT_SETTINGS,
            mode: modeId,
            numBars: 48,
            // Use settings for preview canvas (280x280) to ensure full visibility
            innerRadius: 50,  // Match hover animation settings
            barWidthMultiplier: 1.0
        };

        const tempVisualizer = new Visualizer(canvas, tempSettings);

        // Generate demo magnitudes with controlled values for preview
        const magnitudes = new Float32Array(48);
        for (let i = 0; i < magnitudes.length; i++) {
            const value = 0.25 + Math.random() * 0.25 + Math.sin(i * 0.2) * 0.12;
            // Clamp to safe range matching animation
            magnitudes[i] = Math.min(Math.max(value, 0.15), 0.65);
        }

        tempVisualizer.render(magnitudes);
    }

    /**
     * Animate mode preview on hover
     */
    animateModePreview(canvas, modeId, setAnimationId) {
        const tempSettings = {
            ...DEFAULT_SETTINGS,
            mode: modeId,
            numBars: 48,
            // Use settings for preview canvas (280x280) to ensure full visibility
            innerRadius: 50,  // Match static preview settings
            barWidthMultiplier: 1.0
        };

        const tempVisualizer = new Visualizer(canvas, tempSettings);
        let time = 0;

        const animate = () => {
            time += 0.05;

            // Generate animated magnitudes with controlled values for preview
            const magnitudes = new Float32Array(48);
            for (let i = 0; i < magnitudes.length; i++) {
                // Create smooth wave motion with multiple frequencies
                const wave1 = Math.sin(i * 0.2 + time) * 0.1;
                const wave2 = Math.sin(i * 0.1 + time * 1.5) * 0.08;
                const wave3 = Math.sin(i * 0.3 + time * 0.7) * 0.05;
                const base = 0.3;
                const randomness = Math.sin(i * 0.15 + time * 2) * 0.04;

                const value = base + wave1 + wave2 + wave3 + randomness;
                // Clamp to safe range for 280x280 canvas
                magnitudes[i] = Math.min(Math.max(value, 0.15), 0.65);
            }

            tempVisualizer.render(magnitudes);

            const id = requestAnimationFrame(animate);
            setAnimationId(id);
        };

        animate();
    }

    /**
     * Populate format chips
     */
    populateFormatChips() {
        Object.entries(FORMAT_PRESETS).forEach(([key, preset]) => {
            const chip = document.createElement('button');
            chip.className = 'format-chip';
            chip.dataset.format = key;

            // Create aspect ratio visual indicator
            const aspectIcon = this.createAspectRatioIcon(preset);

            chip.innerHTML = `
                ${aspectIcon}
                <div class="format-chip-content">
                    <div class="format-chip-name">${preset.name}</div>
                    <div class="format-chip-dimensions">${preset.width} × ${preset.height}</div>
                </div>
            `;

            chip.addEventListener('click', () => {
                this.selectFormat(key);
            });

            this.elements.formatChips.appendChild(chip);
        });
    }

    /**
     * Create aspect ratio icon (visual rectangle)
     */
    createAspectRatioIcon(preset) {
        if (preset.isCustom) {
            return `
                <div class="aspect-ratio-icon custom">
                    <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
                        <rect x="12" y="12" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" rx="4"/>
                        <text x="24" y="30" text-anchor="middle" fill="currentColor" font-size="16" font-weight="600">?</text>
                    </svg>
                </div>
            `;
        }

        const aspectRatio = preset.width / preset.height;
        let rectWidth, rectHeight;
        const maxSize = 40;

        if (aspectRatio >= 1) {
            // Landscape or square
            rectWidth = maxSize;
            rectHeight = maxSize / aspectRatio;
        } else {
            // Portrait
            rectHeight = maxSize;
            rectWidth = maxSize * aspectRatio;
        }

        return `
            <div class="aspect-ratio-icon">
                <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
                    <rect
                        x="${(48 - rectWidth) / 2}"
                        y="${(48 - rectHeight) / 2}"
                        width="${rectWidth}"
                        height="${rectHeight}"
                        fill="currentColor"
                        opacity="0.2"
                        stroke="currentColor"
                        stroke-width="2"
                        rx="2"
                    />
                </svg>
            </div>
        `;
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
            this.waveformData = waveformData; // Store for later use
            this.drawWaveform(waveformData);

            // Set up HTML5 audio element
            const audioURL = URL.createObjectURL(file);
            this.elements.audioElement.src = audioURL;
            this.elements.audioElement.volume = 0.8;
            this.elements.totalTime.textContent = Utils.formatTime(audioInfo.duration);

            // Show/hide selection window based on audio duration
            this.updateSelectionWindowVisibility();

            // Show next sections
            this.elements.modeSection.style.display = 'block';
            this.elements.formatSection.style.display = 'block';
            this.elements.settingsSection.style.display = 'block';
            this.elements.previewSection.style.display = 'block';
            this.elements.generateSection.style.display = 'block';

            // Apply the Classic filter by default
            this.filterModes();

            // Update preview
            this.updatePreview();

            // Automatically select the classic audiospectrum mode (circular_bars)
            // Pass false to prevent auto-scrolling to format section
            this.selectMode('circular_bars', false);

            // Scroll to mode section so user sees step 2
            setTimeout(() => {
                Utils.scrollToElement('mode-section');
            }, 300);

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
        // Stop playback
        if (this.elements.audioElement) {
            this.elements.audioElement.pause();
            this.elements.audioElement.src = '';
        }

        // Stop preview animation
        this.stopPreviewAnimation();

        this.audioProcessor.dispose();
        this.audioProcessor = new AudioProcessor();

        this.state.audioFile = null;
        this.state.audioLoaded = false;
        this.waveformData = null;

        this.elements.audioInput.value = '';
        this.elements.dropzone.style.display = 'block';
        this.elements.fileInfo.style.display = 'none';

        // Reset play button
        this.updatePlayButtonState(false);

        // Hide sections
        this.elements.modeSection.style.display = 'none';
        this.elements.formatSection.style.display = 'none';
        this.elements.settingsSection.style.display = 'none';
        this.elements.previewSection.style.display = 'none';
        this.elements.generateSection.style.display = 'none';
    }

    /**
     * Draw waveform on canvas
     */
    drawWaveform(waveformData) {
        const canvas = this.elements.waveformCanvas;
        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        // Set style
        ctx.fillStyle = `rgb(${COLORS.PRIMARY_BLUE[0]}, ${COLORS.PRIMARY_BLUE[1]}, ${COLORS.PRIMARY_BLUE[2]})`;
        ctx.globalAlpha = 0.6;

        // Draw bars
        const barWidth = width / waveformData.length;
        const middle = height / 2;

        waveformData.forEach((value, index) => {
            const barHeight = value * height * 0.9;
            const x = index * barWidth;
            const y = middle - barHeight / 2;

            ctx.fillRect(x, y, Math.max(barWidth - 1, 1), barHeight);
        });
    }

    /**
     * Draw waveform progress
     */
    drawWaveformProgress(progress) {
        const canvas = this.elements.waveformProgress;
        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        if (!this.waveformData) return;

        // Calculate how many bars to draw based on progress
        const progressWidth = width * progress;
        const barWidth = width / this.waveformData.length;
        const middle = height / 2;

        // Set style for progress
        ctx.fillStyle = `rgb(${COLORS.PRIMARY_BLUE[0]}, ${COLORS.PRIMARY_BLUE[1]}, ${COLORS.PRIMARY_BLUE[2]})`;
        ctx.globalAlpha = 1.0;

        this.waveformData.forEach((value, index) => {
            const x = index * barWidth;

            // Only draw if within progress
            if (x < progressWidth) {
                const barHeight = value * height * 0.9;
                const y = middle - barHeight / 2;
                ctx.fillRect(x, y, Math.max(barWidth - 1, 1), barHeight);
            }
        });
    }

    /**
     * Toggle playback
     */
    togglePlayback() {
        if (!this.state.audioLoaded) return;

        if (this.elements.audioElement.paused) {
            this.elements.audioElement.play();
            this.updatePlayButtonState(true);
        } else {
            this.elements.audioElement.pause();
            this.updatePlayButtonState(false);
        }
    }

    /**
     * Update play button state
     */
    updatePlayButtonState(isPlaying) {
        const playIcon = this.elements.playButton.querySelector('.play-icon');
        const pauseIcon = this.elements.playButton.querySelector('.pause-icon');

        if (isPlaying) {
            playIcon.style.display = 'none';
            pauseIcon.style.display = 'block';
        } else {
            playIcon.style.display = 'block';
            pauseIcon.style.display = 'none';
        }
    }

    /**
     * Update playback progress
     */
    updatePlaybackProgress() {
        const currentTime = this.elements.audioElement.currentTime;
        const duration = this.elements.audioElement.duration;

        if (!isNaN(duration) && duration > 0) {
            const progress = currentTime / duration;

            // Update time display
            this.elements.currentTime.textContent = Utils.formatTime(currentTime);

            // Update waveform progress
            this.drawWaveformProgress(progress);
        }
    }

    /**
     * Handle audio ended
     */
    handleAudioEnded() {
        this.updatePlayButtonState(false);
        this.elements.audioElement.currentTime = 0;
        this.drawWaveformProgress(0);
    }

    /**
     * Update volume
     */
    updateVolume(volume) {
        this.elements.audioElement.volume = volume;

        // Update slider background
        const percentage = volume * 100;
        this.elements.volumeSlider.style.background =
            `linear-gradient(to right, var(--color-primary) 0%, var(--color-primary) ${percentage}%, #d2d2d7 ${percentage}%, #d2d2d7 100%)`;
    }

    /**
     * Handle waveform click for seeking
     */
    handleWaveformClick(e) {
        if (!this.state.audioLoaded) return;

        const rect = this.elements.waveformContainer.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const percentage = x / rect.width;

        const duration = this.elements.audioElement.duration;
        if (!isNaN(duration)) {
            this.elements.audioElement.currentTime = duration * percentage;
        }
    }

    /**
     * Handle waveform hover for cursor
     */
    handleWaveformHover(e) {
        const rect = this.elements.waveformContainer.getBoundingClientRect();
        const x = e.clientX - rect.left;

        this.elements.waveformCursor.style.left = `${x}px`;
        this.elements.waveformCursor.style.opacity = '1';
    }

    /**
     * Show or hide the selection window based on audio duration
     */
    updateSelectionWindowVisibility() {
        const audioInfo = this.audioProcessor.getInfo();
        if (!audioInfo) return;

        const PREVIEW_DURATION = 15;
        const shouldShow = audioInfo.duration > PREVIEW_DURATION;

        if (shouldShow) {
            this.elements.waveformSelectionWindow.style.display = 'block';
            this.updateSelectionWindowPosition();
        } else {
            this.elements.waveformSelectionWindow.style.display = 'none';
        }
    }

    /**
     * Update selection window position based on current state
     */
    updateSelectionWindowPosition() {
        const audioInfo = this.audioProcessor.getInfo();
        if (!audioInfo) return;

        const rect = this.elements.waveformContainer.getBoundingClientRect();
        const totalDuration = audioInfo.duration;
        const PREVIEW_DURATION = 15;

        // Calculate width as percentage of total waveform
        const widthPercentage = (PREVIEW_DURATION / totalDuration) * 100;
        this.elements.waveformSelectionWindow.style.width = `${widthPercentage}%`;

        // Calculate left position based on start time
        const leftPercentage = (this.previewSelectionState.startTime / totalDuration) * 100;
        this.elements.waveformSelectionWindow.style.left = `${leftPercentage}%`;
    }

    /**
     * Handle selection window drag start
     */
    handleSelectionWindowDragStart(e) {
        e.preventDefault();
        e.stopPropagation();

        this.previewSelectionState.isDragging = true;
        this.previewSelectionState.dragStartX = e.clientX;

        const rect = this.elements.waveformSelectionWindow.getBoundingClientRect();
        const containerRect = this.elements.waveformContainer.getBoundingClientRect();
        this.previewSelectionState.windowStartX = rect.left - containerRect.left;
    }

    /**
     * Handle selection window drag
     */
    handleSelectionWindowDrag(e) {
        if (!this.previewSelectionState.isDragging) return;

        e.preventDefault();

        const audioInfo = this.audioProcessor.getInfo();
        if (!audioInfo) return;

        const containerRect = this.elements.waveformContainer.getBoundingClientRect();
        const deltaX = e.clientX - this.previewSelectionState.dragStartX;
        const newX = this.previewSelectionState.windowStartX + deltaX;

        // Calculate boundaries
        const windowWidth = this.elements.waveformSelectionWindow.offsetWidth;
        const maxX = containerRect.width - windowWidth;

        // Constrain within bounds
        const constrainedX = Math.max(0, Math.min(newX, maxX));

        // Update start time based on position
        const totalDuration = audioInfo.duration;
        const PREVIEW_DURATION = 15;
        const maxStartTime = totalDuration - PREVIEW_DURATION;

        this.previewSelectionState.startTime = (constrainedX / containerRect.width) * totalDuration;
        this.previewSelectionState.startTime = Math.max(0, Math.min(this.previewSelectionState.startTime, maxStartTime));

        // Update visual position
        this.updateSelectionWindowPosition();
    }

    /**
     * Handle selection window drag end
     */
    handleSelectionWindowDragEnd() {
        if (this.previewSelectionState.isDragging) {
            this.previewSelectionState.isDragging = false;

            // Log the selected time range for debugging
            const endTime = this.previewSelectionState.startTime + this.previewSelectionState.duration;
            console.log(`[Preview Selection] Selected time range: ${this.previewSelectionState.startTime.toFixed(2)}s - ${endTime.toFixed(2)}s`);
        }
    }

    /**
     * Select visualization mode
     */
    selectMode(modeId, autoScroll = true) {
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

        // Update dynamic parameters for this mode
        this.updateDynamicParameters(modeId);

        // Update preview
        this.updatePreview();

        // Scroll to format section only if autoScroll is enabled
        if (autoScroll) {
            setTimeout(() => {
                Utils.scrollToElement('format-section');
            }, 300);
        }
    }

    /**
     * Update dynamic parameters based on selected mode
     */
    updateDynamicParameters(modeId) {
        const mode = VISUALIZATION_MODES[modeId];
        if (!mode || !mode.parameters) {
            // No custom parameters for this mode, hide all mode-specific settings
            return;
        }

        // TODO: Dynamically show/hide parameter controls based on mode.parameters
        // For now, we'll implement this in the next iteration
        console.log(`Mode ${modeId} has custom parameters:`, mode.parameters);
    }

    /**
     * Select format
     */
    selectFormat(formatKey) {
        const preset = FORMAT_PRESETS[formatKey];

        // Safety check for invalid format keys
        if (!preset) {
            console.error(`Invalid format key: ${formatKey}. Falling back to square_1_1.`);
            // Recursively call with fallback
            this.selectFormat('square_1_1');
            return;
        }

        this.state.selectedFormat = formatKey;

        // Update settings
        this.state.settings.width = preset.width;
        this.state.settings.height = preset.height;

        // Update UI
        const chips = this.elements.formatChips.querySelectorAll('.format-chip');
        chips.forEach(chip => {
            if (chip.dataset.format === formatKey) {
                chip.classList.add('format-chip-selected');
            } else {
                chip.classList.remove('format-chip-selected');
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
     * Update preview (called when settings change)
     */
    updatePreview() {
        if (!this.visualizer) return;

        this.visualizer.updateSettings(this.state.settings);

        // If preview animation is already running, it will pick up the new settings
        // Otherwise, start the animation
        if (!this.previewAnimationId) {
            this.startPreviewAnimation();
        }
    }

    /**
     * Start continuous preview animation
     */
    startPreviewAnimation() {
        // Stop any existing animation
        this.stopPreviewAnimation();

        // Ensure visualizer is initialized
        if (!this.visualizer) {
            console.error('[Preview] Visualizer not initialized');
            return;
        }

        console.log('[Preview] Starting animation loop');
        console.log('[Preview] Canvas dimensions:', this.elements.previewCanvas.width, 'x', this.elements.previewCanvas.height);
        console.log('[Preview] Settings:', JSON.stringify(this.state.settings, null, 2));

        const animate = () => {
            try {
                // Generate animated demo magnitudes
                const magnitudes = new Float32Array(this.state.settings.numBars);

                for (let i = 0; i < magnitudes.length; i++) {
                    // Create smooth, animated waves
                    const wave1 = Math.sin(this.previewTime * 0.02 + i * 0.1) * 0.2;
                    const wave2 = Math.sin(this.previewTime * 0.03 - i * 0.08) * 0.15;
                    const wave3 = Math.cos(this.previewTime * 0.015 + i * 0.12) * 0.1;
                    const base = 0.3;
                    const randomness = Math.sin(i * 0.15 + this.previewTime * 0.05) * 0.05;

                    const value = base + wave1 + wave2 + wave3 + randomness;
                    magnitudes[i] = Math.min(Math.max(value, 0.1), 0.9);
                }

                if (this.previewTime === 0) {
                    console.log('[Preview] First frame - magnitudes sample:', magnitudes.slice(0, 5));
                }

                this.visualizer.render(magnitudes);
                this.previewTime++;

                this.previewAnimationId = requestAnimationFrame(animate);
            } catch (error) {
                console.error('[Preview] Error in preview animation:', error);
                console.error('[Preview] Stack trace:', error.stack);
                this.stopPreviewAnimation();
            }
        };

        animate();
    }

    /**
     * Stop preview animation
     */
    stopPreviewAnimation() {
        if (this.previewAnimationId) {
            cancelAnimationFrame(this.previewAnimationId);
            this.previewAnimationId = null;
        }
    }

    /**
     * Update gradient preview
     */
    updateGradientPreview() {
        const color1 = this.elements.gradientColor1.value;
        const color2 = this.elements.gradientColor2.value;
        const color3 = this.elements.gradientColor3.value;

        const scheme = this.state.settings.colorScheme;
        const schemeData = COLOR_SCHEMES[scheme];

        if (schemeData && schemeData.colorCount === 3) {
            this.elements.gradientPreview.style.background =
                `linear-gradient(to right, ${color1}, ${color2}, ${color3})`;
        } else {
            this.elements.gradientPreview.style.background =
                `linear-gradient(to right, ${color1}, ${color2})`;
        }
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
            // Restart the demo animation
            this.startPreviewAnimation();
            return;
        }

        // Stop the demo animation when playing real audio
        this.stopPreviewAnimation();

        // Play audio
        this.audioProcessor.play();
        this.elements.previewPlayBtn.innerHTML = `
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <rect x="4" y="2" width="3" height="12" fill="currentColor"/>
                <rect x="9" y="2" width="3" height="12" fill="currentColor"/>
            </svg>
            Pause
        `;

        // Animate preview with real audio
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
                // Restart the demo animation after audio stops
                this.startPreviewAnimation();
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

            // Check if this will be a preview (15-second limit for songs longer than 15s)
            const audioInfo = this.audioProcessor.getInfo();
            const PREVIEW_DURATION = 15;
            if (audioInfo && audioInfo.duration > PREVIEW_DURATION) {
                const startTime = this.previewSelectionState.startTime;
                const endTime = startTime + PREVIEW_DURATION;
                Utils.showToast(`Generating ${PREVIEW_DURATION}-second preview (${startTime.toFixed(1)}s - ${endTime.toFixed(1)}s)`, 'info', 4000);
            }

            // Generate video with selected time range
            await this.videoEncoder.generateVideo(
                this.audioProcessor,
                this.visualizer,
                this.state.settings,
                this.previewSelectionState.startTime
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

        console.log('[Download] Showing download section');
        console.log('[Download] Generated video:', this.state.generatedVideo);
        console.log('[Download] Video type:', typeof this.state.generatedVideo);
        console.log('[Download] Video size:', this.state.generatedVideo?.size);
        console.log('[Download] Is Blob:', this.state.generatedVideo instanceof Blob);

        // Validate generated video
        if (!this.state.generatedVideo) {
            console.error('[Download] No generated video available');
            Utils.showToast('No video available to download', 'error');
            return;
        }

        if (!(this.state.generatedVideo instanceof Blob)) {
            console.error('[Download] Generated video is not a Blob');
            Utils.showToast('Invalid video format', 'error');
            return;
        }

        if (this.state.generatedVideo.size === 0) {
            console.error('[Download] Generated video is empty');
            Utils.showToast('Generated video is empty', 'error');
            return;
        }

        // Show download section
        this.elements.downloadSection.style.display = 'block';

        try {
            // Set video preview
            const videoUrl = URL.createObjectURL(this.state.generatedVideo);
            console.log('[Download] Created video URL:', videoUrl);
            this.elements.videoPreview.src = videoUrl;

            // Reset download format to WebM
            this.state.downloadFormat = 'webm';
            const downloadFormatButtons = this.elements.downloadFormatChips.querySelectorAll('.chip');
            downloadFormatButtons.forEach(btn => {
                if (btn.dataset.format === 'webm') {
                    btn.classList.add('chip-selected');
                } else {
                    btn.classList.remove('chip-selected');
                }
            });

            // Update file info
            this.elements.downloadSize.textContent = Utils.formatBytes(this.state.generatedVideo.size);
            this.elements.downloadDuration.textContent = Utils.formatTime(this.audioProcessor.duration);
            this.updateDownloadFormatDisplay();

            // Scroll to download section
            setTimeout(() => {
                Utils.scrollToElement('download-section');
            }, 300);

            Utils.showToast('Video generated successfully!', 'success');
        } catch (error) {
            console.error('[Download] Error creating video URL:', error);
            Utils.showToast('Failed to create download preview: ' + error.message, 'error');
        }
    }

    /**
     * Update download format display
     */
    updateDownloadFormatDisplay() {
        const formatNames = {
            'webm': 'WebM (VP9)',
            'mp4': 'H.264 MP4',
            'mov': 'MOV'
        };

        this.elements.downloadFormatDisplay.textContent = formatNames[this.state.downloadFormat] || 'WebM';
    }

    /**
     * Download video
     */
    downloadVideo() {
        if (!this.state.generatedVideo) return;

        // Use selected download format
        const extension = this.state.downloadFormat;

        // Get original audio filename if available
        const originalFilename = this.state.audioFile ? this.state.audioFile.name : null;
        const filename = Utils.createFilename(this.state.selectedMode, extension, originalFilename);

        Utils.downloadBlob(this.state.generatedVideo, filename);

        // Show appropriate message based on format
        if (extension === 'webm') {
            Utils.showToast('Download started!', 'success');
        } else {
            Utils.showToast(`Downloaded as .${extension}. Note: Video is encoded as WebM. You may need to convert it for full compatibility.`, 'info', 5000);
        }
    }

    /**
     * Reset app
     */
    resetApp() {
        // Clean up
        this.audioProcessor.dispose();
        this.audioProcessor = new AudioProcessor();

        // Stop preview animation
        this.stopPreviewAnimation();

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
            generatedVideo: null,
            downloadFormat: 'webm'
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

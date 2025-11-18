/**
 * Audio Spectrum Visualizer - Constants
 * Configuration and constants for the application
 */

// Apple Design System Colors (RGB format)
const COLORS = {
    PRIMARY_BLUE: [0, 113, 227],
    PRIMARY_ORANGE: [255, 122, 0],
    BG_SOFT_GRAY: [245, 245, 247],
    SURFACE_WHITE: [255, 255, 255],
    SURFACE_DARK: [11, 11, 16],
    TEXT_PRIMARY: [153, 153, 153],
    TEXT_LIGHT: [255, 255, 255],
    SUCCESS: [52, 199, 89],
    ERROR: [255, 59, 48],
    WARNING: [255, 204, 0],
    INFO: [94, 92, 230]
};

// Color Schemes for visualization
const COLOR_SCHEMES = {
    apple_blue: {
        name: 'Apple Blue',
        primary: COLORS.PRIMARY_BLUE,
        secondary: COLORS.PRIMARY_ORANGE,
        gradient: true
    },
    warm_orange: {
        name: 'Warm Orange',
        primary: COLORS.PRIMARY_ORANGE,
        secondary: [255, 149, 0],
        gradient: true
    },
    monochrome_white: {
        name: 'Monochrome White',
        primary: COLORS.TEXT_LIGHT,
        secondary: [200, 200, 200],
        gradient: false
    },
    custom: {
        name: 'Custom',
        primary: COLORS.PRIMARY_BLUE,
        secondary: COLORS.PRIMARY_ORANGE,
        gradient: true
    }
};

// Background Styles
const BACKGROUND_STYLES = {
    soft_gray: {
        name: 'Soft Gray',
        color: COLORS.BG_SOFT_GRAY
    },
    white: {
        name: 'White',
        color: COLORS.SURFACE_WHITE
    },
    dark: {
        name: 'Dark',
        color: COLORS.SURFACE_DARK
    },
    transparent: {
        name: 'Transparent',
        color: [0, 0, 0]
    }
};

// Video Format Presets
const FORMAT_PRESETS = {
    instagram_square: {
        name: 'Instagram Square',
        width: 1080,
        height: 1080,
        aspectRatio: '1:1',
        description: 'Perfect for Instagram feed posts'
    },
    instagram_story: {
        name: 'Instagram Story',
        width: 1080,
        height: 1920,
        aspectRatio: '9:16',
        description: 'Vertical format for Stories'
    },
    tiktok: {
        name: 'TikTok/Reels',
        width: 1080,
        height: 1920,
        aspectRatio: '9:16',
        description: 'Vertical format for TikTok and Reels'
    },
    youtube: {
        name: 'YouTube',
        width: 1920,
        height: 1080,
        aspectRatio: '16:9',
        description: 'Standard landscape video'
    },
    youtube_shorts: {
        name: 'YouTube Shorts',
        width: 1080,
        height: 1920,
        aspectRatio: '9:16',
        description: 'Vertical format for Shorts'
    },
    twitter: {
        name: 'Twitter',
        width: 1280,
        height: 720,
        aspectRatio: '16:9',
        description: 'Optimized for Twitter'
    },
    custom: {
        name: 'Custom',
        width: 1920,
        height: 1080,
        aspectRatio: 'Custom',
        description: 'Set your own dimensions'
    }
};

// FPS Options
const FPS_OPTIONS = [24, 30, 60];

// Visualization Modes
const VISUALIZATION_MODES = {
    circular_bars: {
        id: 'circular_bars',
        name: 'Circular Bars',
        description: 'Classic radial bars extending from center',
        mode: 1
    },
    waves: {
        id: 'waves',
        name: 'Waves',
        description: 'Concentric waves that pulse with music',
        mode: 2
    },
    particles: {
        id: 'particles',
        name: 'Particles',
        description: 'Glowing particle system',
        mode: 3
    },
    smooth_waveform: {
        id: 'smooth_waveform',
        name: 'Smooth Waveform',
        description: 'Elegant continuous waveform',
        mode: 4
    },
    neon_tubes: {
        id: 'neon_tubes',
        name: 'Neon Tubes',
        description: 'Minimal glowing tubes',
        mode: 5
    },
    vinyl_grooves: {
        id: 'vinyl_grooves',
        name: 'Vinyl Grooves',
        description: 'Retro vinyl record aesthetic',
        mode: 6
    },
    soul_aura: {
        id: 'soul_aura',
        name: 'Soul Aura',
        description: 'Ethereal glowing aura',
        mode: 7
    },
    liquid_mercury: {
        id: 'liquid_mercury',
        name: 'Liquid Mercury',
        description: 'Flowing metallic liquid',
        mode: 8
    },
    aurora_waves: {
        id: 'aurora_waves',
        name: 'Aurora Waves',
        description: 'Northern lights inspired',
        mode: 9
    },
    mandala_growth: {
        id: 'mandala_growth',
        name: 'Mandala Growth',
        description: 'Geometric mandala patterns',
        mode: 10
    }
};

// Default Settings
const DEFAULT_SETTINGS = {
    numBars: 72,
    innerRadius: 180,
    smoothing: 0.85,
    barWidthMultiplier: 0.8,
    gradient: true,
    colorScheme: 'apple_blue',
    background: 'soft_gray',
    fps: 30,
    format: 'instagram_square',
    mode: 'circular_bars'
};

// Audio Processing
const AUDIO_CONFIG = {
    fftSize: 2048,
    smoothingTimeConstant: 0.85,
    minDecibels: -90,
    maxDecibels: -10
};

// File Constraints
const FILE_CONSTRAINTS = {
    maxSizeMB: 50,
    acceptedFormats: ['.mp3', '.wav'],
    acceptedMimeTypes: ['audio/mpeg', 'audio/wav', 'audio/mp3']
};

// Animation
const ANIMATION = {
    easing: {
        easeOutCubic: t => 1 - Math.pow(1 - t, 3),
        easeInOutCubic: t => t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2,
        easeOutExpo: t => t === 1 ? 1 : 1 - Math.pow(2, -10 * t)
    },
    duration: {
        fast: 120,
        base: 200,
        slow: 300
    }
};

// Export all constants
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        COLORS,
        COLOR_SCHEMES,
        BACKGROUND_STYLES,
        FORMAT_PRESETS,
        FPS_OPTIONS,
        VISUALIZATION_MODES,
        DEFAULT_SETTINGS,
        AUDIO_CONFIG,
        FILE_CONSTRAINTS,
        ANIMATION
    };
}

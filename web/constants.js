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
    sunset: {
        name: 'Sunset',
        primary: [255, 94, 77],
        secondary: [255, 158, 68],
        gradient: true
    },
    ocean: {
        name: 'Ocean',
        primary: [0, 119, 182],
        secondary: [0, 180, 216],
        gradient: true
    },
    forest: {
        name: 'Forest',
        primary: [46, 125, 50],
        secondary: [124, 179, 66],
        gradient: true
    },
    purple_haze: {
        name: 'Purple Haze',
        primary: [123, 31, 162],
        secondary: [186, 104, 200],
        gradient: true
    },
    neon: {
        name: 'Neon',
        primary: [233, 30, 99],
        secondary: [3, 218, 198],
        gradient: true
    },
    fire: {
        name: 'Fire',
        primary: [244, 67, 54],
        secondary: [255, 235, 59],
        gradient: true
    },
    gradient_2: {
        name: 'Gradient (2 Colors)',
        primary: COLORS.PRIMARY_BLUE,
        secondary: COLORS.PRIMARY_ORANGE,
        gradient: true,
        customizable: true,
        colorCount: 2
    },
    gradient_3: {
        name: 'Gradient (3 Colors)',
        primary: COLORS.PRIMARY_BLUE,
        secondary: COLORS.PRIMARY_ORANGE,
        tertiary: [124, 179, 66],
        gradient: true,
        customizable: true,
        colorCount: 3
    },
    super_custom: {
        name: 'Super Custom',
        primary: COLORS.PRIMARY_BLUE,
        secondary: COLORS.PRIMARY_ORANGE,
        tertiary: [124, 179, 66],
        gradient: true,
        customizable: true,
        colorCount: 3,
        progressControl: true
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

// Video Format Presets (Rationalized to combine duplicates)
const FORMAT_PRESETS = {
    square_1_1: {
        name: 'Square (Instagram Feed)',
        width: 1080,
        height: 1080,
        aspectRatio: '1:1',
        description: 'Instagram posts, profile videos'
    },
    vertical_9_16: {
        name: '9:16 (Stories/Shorts/Reels)',
        width: 1080,
        height: 1920,
        aspectRatio: '9:16',
        description: 'Instagram Stories, TikTok, YouTube Shorts, Reels'
    },
    landscape_16_9_hd: {
        name: '16:9 HD (YouTube)',
        width: 1920,
        height: 1080,
        aspectRatio: '16:9',
        description: 'YouTube, Vimeo, standard HD video'
    },
    landscape_16_9_720p: {
        name: '16:9 720p (Twitter)',
        width: 1280,
        height: 720,
        aspectRatio: '16:9',
        description: 'Twitter, LinkedIn, Facebook'
    },
    vertical_4_5: {
        name: '4:5 (Instagram Portrait)',
        width: 1080,
        height: 1350,
        aspectRatio: '4:5',
        description: 'Instagram portrait posts'
    },
    landscape_21_9: {
        name: '21:9 (Cinematic)',
        width: 2560,
        height: 1080,
        aspectRatio: '21:9',
        description: 'Ultrawide cinematic format'
    },
    custom: {
        name: 'Custom',
        width: 1920,
        height: 1080,
        aspectRatio: 'Custom',
        description: 'Set your own dimensions',
        isCustom: true
    }
};

// FPS Options
const FPS_OPTIONS = [24, 30, 60];

// Visualization Modes with Categories
const VISUALIZATION_MODES = {
    // Classic Styles
    circular_bars: {
        id: 'circular_bars',
        name: 'Circular Bars',
        description: 'Classic radial bars extending from center',
        category: 'Classic',
        mode: 1,
        tags: ['radial', 'bars', 'classic']
    },
    waves: {
        id: 'waves',
        name: 'Waves',
        description: 'Concentric waves that pulse with music',
        category: 'Classic',
        mode: 2,
        tags: ['waves', 'pulse', 'smooth']
    },
    smooth_waveform: {
        id: 'smooth_waveform',
        name: 'Smooth Waveform',
        description: 'Elegant continuous waveform',
        category: 'Classic',
        mode: 4,
        tags: ['waveform', 'smooth', 'elegant']
    },
    frequency_bars: {
        id: 'frequency_bars',
        name: 'Frequency Bars',
        description: 'Traditional frequency spectrum bars',
        category: 'Classic',
        mode: 11,
        tags: ['bars', 'spectrum', 'traditional']
    },
    linear_spectrum: {
        id: 'linear_spectrum',
        name: 'Linear Spectrum',
        description: 'Horizontal frequency bars',
        category: 'Classic',
        mode: 12,
        tags: ['linear', 'horizontal', 'clean']
    },

    // Particle Effects
    particles: {
        id: 'particles',
        name: 'Particles',
        description: 'Glowing particle system',
        category: 'Particles',
        mode: 3,
        tags: ['particles', 'glow', 'dynamic']
    },
    fireworks: {
        id: 'fireworks',
        name: 'Fireworks',
        description: 'Exploding particles from center',
        category: 'Particles',
        mode: 13,
        tags: ['particles', 'explosive', 'celebration']
    },
    cosmic_dust: {
        id: 'cosmic_dust',
        name: 'Cosmic Dust',
        description: 'Swirling galaxy particles with trails',
        category: 'Particles',
        mode: 14,
        tags: ['space', 'particles', 'trails']
    },
    particle_rain: {
        id: 'particle_rain',
        name: 'Particle Rain',
        description: 'Cascading particles from above',
        category: 'Particles',
        mode: 15,
        tags: ['particles', 'cascade', 'rain']
    },
    snow_particles: {
        id: 'snow_particles',
        name: 'Snow Particles',
        description: 'Gentle falling snowflakes',
        category: 'Particles',
        mode: 16,
        tags: ['particles', 'snow', 'gentle']
    },

    // Retro & Vintage
    vinyl_grooves: {
        id: 'vinyl_grooves',
        name: 'Vinyl Grooves',
        description: 'Rotating vinyl record aesthetic',
        category: 'Retro',
        mode: 6,
        tags: ['vintage', 'vinyl', 'rotation']
    },
    neon_tubes: {
        id: 'neon_tubes',
        name: 'Neon Tubes',
        description: 'Minimal glowing neon tubes',
        category: 'Retro',
        mode: 5,
        tags: ['neon', 'minimal', 'glow']
    },
    retro_cassette: {
        id: 'retro_cassette',
        name: 'Retro Cassette',
        description: 'VU meters and tape reel animation',
        category: 'Retro',
        mode: 17,
        tags: ['vintage', 'cassette', 'analog']
    },
    pixel_clouds: {
        id: 'pixel_clouds',
        name: 'Pixel Clouds',
        description: '8-bit style floating clouds',
        category: 'Retro',
        mode: 18,
        tags: ['pixel', '8bit', 'retro']
    },
    neon_cityscape: {
        id: 'neon_cityscape',
        name: 'Neon Cityscape',
        description: 'Synthwave city with reactive buildings',
        category: 'Retro',
        mode: 19,
        tags: ['synthwave', 'city', 'neon']
    },

    // Fluid & Organic
    liquid_mercury: {
        id: 'liquid_mercury',
        name: 'Liquid Mercury',
        description: 'Flowing metallic liquid',
        category: 'Fluid',
        mode: 8,
        tags: ['fluid', 'metallic', 'smooth']
    },
    soul_aura: {
        id: 'soul_aura',
        name: 'Soul Aura',
        description: 'Pulsing organic ethereal glow',
        category: 'Fluid',
        mode: 7,
        tags: ['organic', 'glow', 'ethereal']
    },
    lava_lamp: {
        id: 'lava_lamp',
        name: 'Lava Lamp',
        description: 'Rising and morphing organic blobs',
        category: 'Fluid',
        mode: 20,
        tags: ['organic', 'psychedelic', 'fluid']
    },
    ink_drops: {
        id: 'ink_drops',
        name: 'Ink Drops',
        description: 'Organic ink dispersing in water',
        category: 'Fluid',
        mode: 21,
        tags: ['artistic', 'fluid', 'organic']
    },
    water_ripples: {
        id: 'water_ripples',
        name: 'Water Ripples',
        description: 'Interference patterns from frequency drops',
        category: 'Fluid',
        mode: 22,
        tags: ['water', 'ripples', 'interference']
    },

    // Nature & Ethereal
    aurora_waves: {
        id: 'aurora_waves',
        name: 'Aurora Waves',
        description: 'Northern lights flowing ribbons',
        category: 'Nature',
        mode: 9,
        tags: ['ethereal', 'nature', 'lights']
    },
    crystal_growth: {
        id: 'crystal_growth',
        name: 'Crystal Growth',
        description: 'Geometric crystals forming',
        category: 'Nature',
        mode: 23,
        tags: ['geometric', 'crystals', 'elegant']
    },
    frequency_flowers: {
        id: 'frequency_flowers',
        name: 'Frequency Flowers',
        description: 'Blooming petals that grow with music',
        category: 'Nature',
        mode: 24,
        tags: ['organic', 'flowers', 'bloom']
    },
    fire_dance: {
        id: 'fire_dance',
        name: 'Fire Dance',
        description: 'Realistic flames dancing to rhythm',
        category: 'Nature',
        mode: 25,
        tags: ['fire', 'primal', 'energy']
    },
    bioluminescence: {
        id: 'bioluminescence',
        name: 'Ocean Bioluminescence',
        description: 'Glowing underwater creatures',
        category: 'Nature',
        mode: 26,
        tags: ['underwater', 'glow', 'organic']
    },

    // Geometric & Mathematical
    mandala_growth: {
        id: 'mandala_growth',
        name: 'Mandala Growth',
        description: 'Sacred geometric mandala patterns',
        category: 'Geometric',
        mode: 10,
        tags: ['geometric', 'sacred', 'symmetry']
    },
    kaleidoscope: {
        id: 'kaleidoscope',
        name: 'Kaleidoscope',
        description: 'Mirrored symmetric patterns',
        category: 'Geometric',
        mode: 27,
        tags: ['symmetric', 'mirrored', 'psychedelic']
    },
    fractal_bloom: {
        id: 'fractal_bloom',
        name: 'Fractal Bloom',
        description: 'Self-similar mathematical patterns',
        category: 'Geometric',
        mode: 28,
        tags: ['fractal', 'mathematical', 'complex']
    },
    morphing_geometry: {
        id: 'morphing_geometry',
        name: 'Morphing Geometry',
        description: 'Shifting 3D wireframe shapes',
        category: 'Geometric',
        mode: 29,
        tags: ['3d', 'wireframe', 'abstract']
    },
    spiral_galaxy: {
        id: 'spiral_galaxy',
        name: 'Spiral Galaxy',
        description: 'Rotating spiral arms with particles',
        category: 'Geometric',
        mode: 30,
        tags: ['spiral', 'rotation', 'space']
    },

    // Scientific & Physics
    dna_helix: {
        id: 'dna_helix',
        name: 'DNA Helix',
        description: 'Double helix twisting with music',
        category: 'Scientific',
        mode: 31,
        tags: ['biology', 'helix', 'scientific']
    },
    quantum_strings: {
        id: 'quantum_strings',
        name: 'Quantum Strings',
        description: 'Vibrating strings with interference',
        category: 'Scientific',
        mode: 32,
        tags: ['physics', 'quantum', 'strings']
    },
    magnetic_fields: {
        id: 'magnetic_fields',
        name: 'Magnetic Fields',
        description: 'Iron filing pattern visualization',
        category: 'Scientific',
        mode: 33,
        tags: ['physics', 'magnetic', 'patterns']
    },
    gravitational_lens: {
        id: 'gravitational_lens',
        name: 'Gravitational Lens',
        description: 'Spacetime warping light',
        category: 'Scientific',
        mode: 34,
        tags: ['physics', 'gravity', 'space']
    },
    seismic_waves: {
        id: 'seismic_waves',
        name: 'Seismic Waves',
        description: 'Earthquake seismograph readings',
        category: 'Scientific',
        mode: 35,
        tags: ['geological', 'waves', 'dramatic']
    },

    // Tech & Futuristic
    tunnel_vision: {
        id: 'tunnel_vision',
        name: 'Tunnel Vision',
        description: 'Hyperspace tunnel with depth',
        category: 'Tech',
        mode: 36,
        tags: ['scifi', 'tunnel', 'depth']
    },
    matrix_code: {
        id: 'matrix_code',
        name: 'Matrix Code',
        description: 'Cascading digital rain code',
        category: 'Tech',
        mode: 37,
        tags: ['cyber', 'code', 'digital']
    },
    hologram_glitch: {
        id: 'hologram_glitch',
        name: 'Hologram Glitch',
        description: 'Futuristic projection with glitch effects',
        category: 'Tech',
        mode: 38,
        tags: ['hologram', 'glitch', 'futuristic']
    },
    circuit_board: {
        id: 'circuit_board',
        name: 'Circuit Board',
        description: 'Electronic pathways lighting up',
        category: 'Tech',
        mode: 39,
        tags: ['electronic', 'circuit', 'tech']
    },
    neural_network: {
        id: 'neural_network',
        name: 'Neural Network',
        description: 'AI synapses firing with music',
        category: 'Tech',
        mode: 40,
        tags: ['ai', 'neural', 'connections']
    },

    // Energy & Abstract
    lightning_strikes: {
        id: 'lightning_strikes',
        name: 'Lightning Strikes',
        description: 'Electric bolts connecting peaks',
        category: 'Energy',
        mode: 41,
        tags: ['electric', 'energy', 'intense']
    },
    plasma_storm: {
        id: 'plasma_storm',
        name: 'Plasma Storm',
        description: 'Swirling energy vortex',
        category: 'Energy',
        mode: 42,
        tags: ['chaotic', 'energy', 'vortex']
    },
    laser_show: {
        id: 'laser_show',
        name: 'Laser Show',
        description: 'Concert-style laser beams',
        category: 'Energy',
        mode: 43,
        tags: ['laser', 'concert', 'edm']
    },
    energy_pulses: {
        id: 'energy_pulses',
        name: 'Energy Pulses',
        description: 'Radiating shockwaves from center',
        category: 'Energy',
        mode: 44,
        tags: ['pulse', 'radial', 'waves']
    },
    rainbow_prism: {
        id: 'rainbow_prism',
        name: 'Rainbow Prism',
        description: 'Light refraction spectrum',
        category: 'Energy',
        mode: 45,
        tags: ['rainbow', 'spectrum', 'colorful']
    }
};

// Mode Categories for filtering
const MODE_CATEGORIES = {
    all: 'All Modes',
    classic: 'Classic',
    particles: 'Particles',
    retro: 'Retro',
    fluid: 'Fluid',
    nature: 'Nature',
    geometric: 'Geometric',
    scientific: 'Scientific',
    tech: 'Tech',
    energy: 'Energy'
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

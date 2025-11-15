#!/usr/bin/env python3
"""
Creative Audio Spectrum Visualizer - HYPNOTIC EDITION (100 Modes!)
Generates transparent videos with wild, creative audio spectrum animations
Perfect for lofi YouTube channels and K-pop/soul/jazz transformations

NOW WITH 100 HYPNOTIC VISUALIZATION MODES!
Modes 1-50: Original creative visualizations
Modes 51-100: NEW! Inspired by fractals, physics, nature, and hypnotic patterns




Visualization Modes:
  --mode 1: Vinyl Grooves - Rotating circular grooves like a vinyl record (perfect for lofi)
  --mode 2: Neon Rain - Vertical neon droplets cascading down (cyberpunk lofi aesthetic)
  --mode 3: Jazzy Fireworks - Bursting particles that explode from center (jazz energy)
  --mode 4: Retro Cassette - VU meters and tape reel animation (vintage lofi)
  --mode 5: Soul Aura - Pulsing organic blob with smooth edges (soul/RnB vibe)
  --mode 6: Frequency Flowers - Blooming petals that grow with music (dreamy lofi)
  --mode 7: Electric Heartbeat - EKG-style waveform with glow (emotional jazz)
  --mode 8: Pixel Clouds - 8-bit style floating cloud particles (retro lofi)
  --mode 9: Liquid Mercury - Flowing metallic waves (smooth jazz/soul)
  --mode 10: Cosmic Dust - Swirling galaxy particles with trails (ambient lofi)
  --mode 11: Quantum Strings - Vibrating strings with interference patterns (experimental)
  --mode 12: Lava Lamp - Rising and morphing organic blobs (psychedelic lofi)
  --mode 13: DNA Helix - Double helix structure that twists with music (scientific vibe)
  --mode 14: Lightning Strikes - Electric bolts connecting frequency peaks (intense energy)
  --mode 15: Morphing Geometry - Shifting 3D wireframe shapes (abstract modern)
  --mode 16: Ink Drops - Organic ink dispersing in water (artistic lofi)
  --mode 17: Aurora Waves - Northern lights-style flowing ribbons (ethereal ambient)
  --mode 18: Fractal Bloom - Self-similar patterns emerging from center (mathematical art)
  --mode 19: Plasma Storm - Swirling energy vortex with tendrils (chaotic energy)
  --mode 20: Crystal Growth - Geometric crystals forming and shattering (elegant minimalism)
  --mode 21: Gravitational Lens - Spacetime warping and bending light (cosmic sci-fi)
  --mode 22: Magnetic Fields - Iron filing patterns flowing with music (scientific art)
  --mode 23: Tribal Drums - Concentric shockwaves with ethnic patterns (world music)
  --mode 24: Neon Cityscape - Scrolling city skyline with reactive buildings (synthwave)
  --mode 25: Heartbeat Monitor - Medical monitor with vital signs (dramatic tension)
  --mode 26: Ocean Depths - Deep sea bioluminescent creatures (underwater mystery)
  --mode 27: Fire Dance - Realistic flames dancing to rhythm (primal energy)
  --mode 28: Particle Collider - High-energy physics collision visualization (science)
  --mode 29: Rainbow Prism - Light refraction through rotating prism (optical physics)
  --mode 30: Seismic Waves - Earthquake seismograph readings (geological drama)
  --mode 31: Origami Unfold - Paper folding and unfolding geometrically (Japanese art)
  --mode 32: Storm Clouds - Thunder and lightning in swirling clouds (epic weather)
  --mode 33: Binary Matrix - Falling Matrix-style binary code (hacker aesthetic)
  --mode 34: Kaleidoscope - Symmetric mirrored patterns (psychedelic symmetry)
  --mode 35: Laser Show - Concert laser beams and spotlights (EDM concert)
  --mode 36: Sandstorm - Desert sand particles in wind vortex (natural chaos)
  --mode 37: Ice Shatter - Cracking and breaking ice surface (dramatic tension)
  --mode 38: Cellular Division - Organic cells splitting and multiplying (biology)
  --mode 39: Neon Tubes - Glowing tube shapes bending and twisting (futuristic minimal)
  --mode 40: Cosmic Strings - Universe-scale energy strings vibrating (theoretical physics)
  --mode 41: Paint Splatter - Jackson Pollock drip painting style (abstract expressionism)
  --mode 42: Quantum Foam - Bubbling spacetime at quantum scale (extreme physics)
  --mode 43: Aztec Sun - Ancient Aztec calendar rotating and glowing (ancient civilization)
  --mode 44: Fiber Optics - Light traveling through fiber cables (tech aesthetic)
  --mode 45: Tornado Funnel - Swirling debris in tornado vortex (natural disaster)
  --mode 46: Hologram Glitch - Futuristic holographic projection errors (cyberpunk tech)
  --mode 47: Starfield Warp - Stars streaking during hyperspace jump (sci-fi space travel)
  --mode 48: Mandala Growth - Sacred geometry mandala forming (spiritual art)
  --mode 49: Neon Sign Flicker - Vintage neon signs buzzing on/off (retro urban)
  --mode 50: Black Hole - Event horizon with gravitational lensing (cosmic destruction)

Examples:
  # Vinyl grooves for lofi
python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode1.mov'  --mode 1

LOFI 
python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode2.mov'  --mode 2

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode3.mov'  --mode 3

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode4.mov'  --mode 4

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode5.mov'  --mode 5

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode6.mov'  --mode 6

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode7.mov'  --mode 7

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode8.mov'  --mode 8

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode9.mov'  --mode 9

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode10.mov'  --mode 10

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode11.mov'  --mode 11

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode12.mov'  --mode 12

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode13.mov'  --mode 13

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode14.mov'  --mode 14

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode15.mov'  --mode 15

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode16.mov'  --mode 16

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode17.mov'  --mode 17

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode18.mov'  --mode 18

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode19.mov'  --mode 19

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode20.mov'  --mode 20

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode21.mov'  --mode 21

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode22.mov'  --mode 22

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode23.mov'  --mode 23

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode24.mov'  --mode 24

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode25.mov'  --mode 25

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode26.mov'  --mode 26

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode27.mov'  --mode 27

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode28.mov'  --mode 28

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode29.mov'  --mode 29

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode30.mov'  --mode 30

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode31.mov'  --mode 31

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode32.mov'  --mode 32

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode33.mov'  --mode 33

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode34.mov'  --mode 34

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode35.mov'  --mode 35

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode36.mov'  --mode 36

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode37.mov'  --mode 37

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode38.mov'  --mode 38

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode39.mov'  --mode 39

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode40.mov'  --mode 40

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode41.mov'  --mode 41

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode42.mov'  --mode 42

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode43.mov'  --mode 43

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode44.mov'  --mode 44

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode45.mov'  --mode 45

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode46.mov'  --mode 46

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode47.mov'  --mode 47

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode48.mov'  --mode 48

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode49.mov'  --mode 49

python audio_spectrum_creative.py '/Users/ahmeddoghri/Desktop/turkish-national-anthem.wav' '/Users/ahmeddoghri/Desktop/turkish-national-anthem-mode50.mov'  --mode 50


  # Soul aura for K-pop soul covers
  python audio_spectrum_creative.py input.mp3 output.mov --mode 5

  # Jazzy fireworks for upbeat tracks
  python audio_spectrum_creative.py input.mp3 output.mov --mode 3
"""

import sys
import os
import numpy as np
import cv2
import librosa
import argparse
from pathlib import Path

# Import mode registry for modular visualization modes
from modes import register_modes, get_mode_method


class CreativeSpectrumVisualizer:
    def __init__(self, audio_path, output_path, width=1920, height=1080,
                 fps=30, num_bars=120, smoothing=0.7, mode=1):
        """
        Initialize the creative spectrum visualizer

        Args:
            audio_path: Path to input audio file
            output_path: Path to output video file
            width: Video width in pixels
            height: Video height in pixels
            fps: Frames per second
            num_bars: Number of frequency bars/elements
            smoothing: Smoothing factor (0-1) for animation
            mode: Visualization mode (1-20)
        """
        self.audio_path = audio_path
        self.output_path = output_path
        self.width = width
        self.height = height
        self.fps = fps
        self.num_bars = num_bars
        self.smoothing = smoothing
        self.mode = mode

        self.center_x = width // 2
        self.center_y = height // 2
        self.max_radius = min(width, height) // 2 - 50  # More padding for minimalist look

        # For smoothing between frames
        self.prev_magnitudes = None

        # Mode-specific state
        self.rotation_angle = 0
        self.rain_particles = []
        self.firework_particles = []
        self.cassette_reel_angle = 0
        self.flower_petals = []
        self.pixel_clouds = []
        self.mercury_history = []
        self.cosmic_particles = []
        self.frame_counter = 0

        # New modes 11-20 state
        self.quantum_strings = []
        self.lava_blobs = []
        self.dna_rotation = 0
        self.lightning_bolts = []
        self.geometry_vertices = []
        self.ink_particles = []
        self.aurora_ribbons = []
        self.fractal_layers = []
        self.plasma_tendrils = []
        self.crystals = []

        # Modes 21-50 state
        self.gravitational_objects = []
        self.magnetic_particles = []
        self.tribal_shockwaves = []
        self.cityscape_buildings = []
        self.heartbeat_history = []
        self.bioluminescent_creatures = []
        self.fire_particles = []
        self.collision_particles = []
        self.prism_rotation = 0
        self.seismic_readings = []
        self.origami_folds = []
        self.storm_particles = []
        self.matrix_columns = []
        self.kaleidoscope_rotation = 0
        self.laser_beams = []
        self.sand_particles = []
        self.ice_cracks = []
        self.cells = []
        self.neon_tubes = []
        self.cosmic_string_segments = []
        self.paint_splatters = []
        self.quantum_bubbles = []
        self.aztec_rotation = 0
        self.fiber_pulses = []
        self.tornado_debris = []
        self.hologram_errors = []
        self.stars = []
        self.mandala_layers = []
        self.neon_signs = []
        self.black_hole_particles = []

        # Modes 51-100 state - HYPNOTIC EDITION
        self.fractal_tree_branches = []
        self.city_blocks = []
        self.gravity_well_particles = []
        self.metaballs = []
        self.aurora_curtains = []
        self.stained_glass_panes = []
        self.nerve_nodes = []
        self.glitch_blocks = []
        self.warp_rings = []
        self.cellular_automaton = []
        self.ascii_chars = []
        self.water_ripples = []
        self.terrain_height = []
        self.string_art_points = []
        self.ember_particles = []
        self.kaleidoscope_segments = []
        self.jellyfish_tentacles = []
        self.orbital_bodies = []
        self.cube_rotation = 0
        self.typography_words = []
        self.sonar_blips = []
        self.vu_needle_positions = [0, 0]
        self.lightning_cloud = []
        self.bouncing_balls = []
        self.ink_blooms = []
        self.stereo_landscape_left = []
        self.stereo_landscape_right = []
        self.latent_morph_state = 0
        self.pixel_storm = []
        self.vine_segments = []
        self.haunted_face_alpha = 0
        self.constellation_stars = []
        self.matrix_rain = []
        self.voxel_grid = []
        self.dna_helix_rungs = []
        self.shader_time = 0
        self.spirograph_trail = []
        self.eq_tower_rings = []
        self.doodle_path = []
        self.firework_rockets = []
        self.microscopic_cells = []
        self.burning_paper = []
        self.swarm_boids = []
        self.pendulum_angles = []
        self.crt_flicker = 0
        self.pulsing_polygon_vertices = []
        self.chromatic_orb_rotation = 0
        self.textured_bar_scroll = []
        self.voronoi_seeds = []
        self.glass_cracks = []
        self.sun_position = 0

        # Modes 101-150 state - ULTIMATE HYPNOTIC EDITION
        self.neural_nodes = []
        self.neural_connections = []
        self.liquid_mercury_particles = []
        self.cosmic_strings = []
        self.particle_swarm = []
        self.crystal_lattice_nodes = []
        self.aurora_wave_points = []
        self.dna_helix_rotation = 0
        self.fractal_bloom_petals = []
        self.circuit_board_traces = []
        self.quantum_field_particles = []
        self.origami_fold_state = 0
        self.galaxy_spiral_stars = []
        self.rubber_bands = []
        self.ink_diffusion_particles = []
        self.geo_kaleidoscope_rotation = 0
        self.lightning_bolts = []
        self.cellular_growth_cells = []
        self.sound_ribbons = []
        self.matrix_rain_columns = []
        self.fire_mandala_flames = []
        self.tessellation_state = 0
        self.seismic_wave_data = []
        self.neon_city_buildings = []
        self.magnetic_field_lines = []
        self.bubble_fusion_bubbles = []
        self.tribal_drum_patterns = []
        self.glass_shatter_fragments = []
        self.bioluminescent_creatures = []
        self.sound_architecture_blocks = []
        self.plasma_ball_arcs = []
        self.sand_mandala_grains = []
        self.laser_show_beams = []
        self.coral_reef_polyps = []
        self.wireframe_morph_vertices = []
        self.sound_garden_plants = []
        self.hologram_glitch_panels = []
        self.pendulum_wave_pendulums = []
        self.volcano_lava_particles = []
        self.butterfly_attractor_trail = []
        self.silk_weaving_threads = []
        self.clock_gears = []
        self.smoke_signal_particles = []
        self.stained_glass_rays = []
        self.string_theory_strings = []
        self.paper_craft_folds = []
        self.aurora_sky_bands = []
        self.cellular_automata_grid = []
        self.dragon_curve_points = []
        self.rain_circle_ripples = []
        self.fourier_epicycles = []

        # Modes 151-200 state - ULTIMATE CREATIVE HYPNOTIC EDITION
        self.neon_halo_rings = []
        self.twin_orbiters = []
        self.bar_spiral_rotation = 0
        self.ribbon_wave_points = []
        self.voxel_city_grid = []
        self.sunburst_ticks = []
        self.waterline_surface = []
        self.laser_tunnel_rings = []
        self.vector_field_particles = []
        self.orbit_ring_dots = []
        self.stitch_bars_grid = []
        self.aurora_curtain_points = []
        self.helix_bars_state = 0
        self.polygon_echo_waves = []
        self.confetti_particles = []
        self.wireframe_dome_vertices = []
        self.pulse_dashes = []
        self.terrain_sweep_rows = []
        self.chromatic_bars_flash = 0
        self.bubble_choir_bubbles = []
        self.starfield_grid_cells = []
        self.dna_ladder_rungs = []
        self.arc_meter_values = [0, 0, 0]
        self.ink_splatter_splats = []
        self.hex_cell_states = []
        self.sonic_orbit_satellites = []
        self.liquid_bar_velocities = []
        self.clockwork_gears_state = []
        self.petal_resonator_petals = []
        self.kaleido_scope_rotation = 0
        self.runway_lights_sweep = 0
        self.constellation_points = []
        self.quake_grid_tiles = []
        self.sonic_rain_streaks = []
        self.halo_typo_glow = 0
        self.wormhole_depth_particles = []
        self.fractal_leaves_branches = []
        self.tape_analyzer_reels = 0
        self.slinky_circle_coils = []
        self.meteor_swarm_meteors = []
        self.piano_roll_bars = []
        self.ring_rainbows_state = []
        self.origami_fan_angle = 0
        self.circuit_pulse_nodes = []
        self.sphere_harmonics_points = []
        self.split_screen_flash = 0
        self.equalizer_rings_sectors = []
        self.liquid_bokeh_circles = []
        self.gooey_droplets = []
        self.arcade_histogram_palette = 0
        # setB modes 176-200
        self.serpentine_chain_segments = []
        self.pendulum_array_pendulums = []
        self.hologram_pyramid_rotation = 0
        self.sonic_snow_flakes = []
        self.rail_scanner_position = 0
        self.nebula_fog_density = []
        self.tri_arc_weave_state = []
        self.pixel_fountain_pixels = []
        self.time_ruler_markers = []
        self.moire_rings_offset = 0
        self.comet_wheel_comets = []
        self.sliced_donut_tilt = 0
        self.crosshair_pulse_spacing = 0
        self.sonar_sweep_angle = 0
        self.paper_strip_bends = []
        self.ripple_grid_emitters = []
        self.orbit_text_kerning = 0
        self.triangulated_points = []
        self.slinky_stairs_heights = []
        self.orbital_rings_flung = []
        self.hatching_shader_density = 0
        self.spectrum_curtain_state = 0
        self.spiral_sand_grains = []
        self.iso_bars_cube_rotation = 0
        self.spectrum_waterfall_columns = []
        self.magnetic_lines_field = []
        self.tiled_portals_grid = []
        self.crown_peaks_spikes = []
        self.silhouette_aura_sparks = []
        self.sine_quilt_tiles = []
        self.radial_barcode_rotation = 0
        self.drum_orbit_markers_list = []
        self.spline_comet_path = []
        self.crystal_shards_pieces = []
        self.metaball_ring_blobs = []
        self.bezier_bouquet_stems = []
        self.pulse_grid_columns = []
        self.stacked_ribbons_layers = []
        self.compass_needles_angles = []
        self.rippled_donut_waveform = []
        self.neon_spirograph_path = []
        self.gated_squares_grid = []
        self.strobe_lattice_state = 0
        self.sand_pendulum_trail = []
        self.tornado_columns_twist = 0
        self.led_matrix_glyphs = []
        self.chromatic_beads_positions = []
        self.echo_circles_rings = []
        self.stacked_area_bands_state = []
        self.laser_lattice_3d_grid = []
        self.polygon_shimmer_clock_ticks = []
        self.feather_plume_strands = []

        # Modes 201-225 state - NEW CREATIVE SET
        self.event_horizon_grid = []
        self.comet_conveyor_belt = []
        self.foam_bubbles = []
        self.aurora_crown_ribbons = []
        self.asteroid_dust = []
        self.hyperloop_cars = []
        self.pinball_entities = []
        self.inkblot_noise = 0
        self.telemetry_rings = []
        self.wormhole_folds = []
        self.jellyfish_tentacles_holo = []
        self.moon_crane_bins = []
        self.constellation_letters = []
        self.cryo_crystals = []
        self.blueprint_callouts = []
        self.tide_caustics = []
        self.barcode_slicer_bars = []
        self.satellites_swarm = []
        self.pulse_weave_phase = 0.0
        self.paint_spheres = []
        self.supernova_state = { 'energy': 0.0, 'blasting': False, 'filaments': [] }
        self.martian_harp_strings = []
        self.teleporting_bars = []
        self.vinyl_halo_grooves = []
        self.photon_slits = []
        self.meteor_net_nodes = []
        self.space_hose_droplets = []
        self.horizon_monoliths = []
        self.slingshot_probes = []
        self.solar_notches = []
        self.tesseract_edges = []
        self.postcard_tiles = []
        self.cosmic_braille_dots = []
        self.harpoon_line = []
        self.galaxy_ticker_chars = []
        self.antimatter_chessboard = []
        self.star_nursery_stations = []
        self.magnetar_lines = []
        self.zero_kelvin_diamonds = []
        self.time_garden_planets = []
        self.ribbon_printer_points = []
        self.dark_matter_drops = []
        self.meteor_choir_cones = []
        self.folded_map_folds = []
        self.ion_thruster_particles = []
        self.dominoes_tiles = []
        self.suit_hud_state = { 'flash': 0 }
        self.pulsar_beam_angle = 0.0
        self.astro_terrarium_entities = []
        self.spark_curtain_particles = []
        self.transit_plot_points = []
        self.cryo_pod_mist = []
        self.boomerangs = []
        self.solar_sails = []
        self.dark_nebula_mask = []

        # Modes 226-275 state - HYPNOTIC SET D
        self.phyllotaxis_angle = 137.5
        self.phyllotaxis_breath = 0.0
        self.mandala_weave_phase = 0.0
        self.lissajous_t = 0.0
        self.lotus_phase = 0.0
        self.hypno_pendula = []
        self.moire_angle_a = 0.0
        self.moire_angle_b = 0.0
        self.shepard_zoom = 1.0
        self.plasma_shift = 0.0
        self.pulse_timer = 0
        self.serpents_trail = []
        self.orb_choir = []
        self.sufi_spin_angle = 0.0
        self.helmholtz_phase = 0.0
        self.slinky_depth = 0.0
        self.fern_points = []
        self.binaural_phase_l = 0.0
        self.binaural_phase_r = 0.0
        self.chakric_phase = 0.0
        self.hypersphere_phase = 0.0
        self.phi_kaleidos_phase = 0.0
        self.cycloid_phase = 0.0
        self.ocean_swell = 0.0
        self.harmonograph_t = 0.0
        self.ink_veins = []
        self.breath_vortex = 0.0
        self.meteor_carousel = []
        self.ripple_glass_phase = 0.0
        self.theta_lanterns = []
        self.iso_weave_phase = 0.0
        self.orbiting_eye_angle = 0.0
        self.ribbon_stair_phase = 0.0
        self.toroidal_flow = 0.0
        self.hypno_shell_twist = 0.0
        self.tide_clock_phase = 0.0
        self.kaleidofish_school = []
        self.compass_wave_phase = 0.0
        self.glacial_bloom = []
        self.helix_lanterns = []
        self.soft_grid_phase = 0.0
        self.ripple_dome_phase = 0.0
        self.spirocloud_traces = []
        self.mosaic_cells = []
        self.bamboo_stalks = []
        self.nesting_circles_phase = 0.0
        self.paper_cranes = []
        self.pulse_hologrid_phase = 0.0
        self.ribbon_canopy = []
        self.auroral_gate_phase = 0.0
        self.satin_ladder_phase = 0.0
        self.opaline_orb_t = 0.0
        self.quilt_loom_phase = 0.0

        # Register all visualization modes from the modes/ directory
        register_modes(self)

    def load_audio(self):
        """Load and process audio file"""
        print(f"Loading audio from: {self.audio_path}")

        y, sr = librosa.load(self.audio_path, sr=None)
        self.sample_rate = sr
        self.duration = librosa.get_duration(y=y, sr=sr)

        print(f"Audio loaded: {self.duration:.2f}s, Sample rate: {sr}Hz")

        hop_length = int(sr / self.fps)
        n_fft = 2048

        stft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)
        self.magnitude = np.abs(stft)

        self.magnitude_db = librosa.amplitude_to_db(self.magnitude, ref=np.max)
        self.magnitude_norm = (self.magnitude_db - self.magnitude_db.min()) / \
                              (self.magnitude_db.max() - self.magnitude_db.min())

        self.num_frames = self.magnitude_norm.shape[1]
        print(f"Processed {self.num_frames} frames")

        return y, sr

    def get_frequency_bands(self, frame_idx):
        """Extract frequency bands for a specific frame"""
        if frame_idx >= self.num_frames:
            frame_idx = self.num_frames - 1

        frame_magnitudes = self.magnitude_norm[:, frame_idx]
        total_freqs = len(frame_magnitudes)
        useful_freqs = int(total_freqs * 0.6)

        bar_magnitudes = []
        for i in range(self.num_bars):
            t = i / self.num_bars
            freq_pos = int(useful_freqs * (t ** 1.5))

            window_size = max(1, useful_freqs // (self.num_bars * 2))
            start_idx = max(0, freq_pos - window_size // 2)
            end_idx = min(useful_freqs, freq_pos + window_size // 2)

            if start_idx < end_idx:
                avg_magnitude = np.mean(frame_magnitudes[start_idx:end_idx])
            else:
                avg_magnitude = frame_magnitudes[freq_pos] if freq_pos < len(frame_magnitudes) else 0

            bar_magnitudes.append(avg_magnitude)

        bar_magnitudes = np.array(bar_magnitudes)

        if self.prev_magnitudes is not None:
            bar_magnitudes = (self.smoothing * self.prev_magnitudes +
                            (1 - self.smoothing) * bar_magnitudes)

        self.prev_magnitudes = bar_magnitudes.copy()

        return bar_magnitudes

    def get_apple_style_color(self, hue, magnitude, saturation_multiplier=0.6, value_multiplier=0.85):
        """
        Convert vibrant colors to Apple-style minimalist aesthetic

        Args:
            hue: Base hue (0-180 in OpenCV HSV)
            magnitude: Audio magnitude (0-1)
            saturation_multiplier: Reduce saturation for muted colors
            value_multiplier: Adjust brightness

        Returns:
            BGR color tuple with minimalist aesthetic
        """
        # Reduce saturation for more muted, elegant colors
        saturation = int(100 + magnitude * 80 * saturation_multiplier)
        saturation = min(180, saturation)

        # Softer value range for minimalist look
        value = int(180 + magnitude * 75 * value_multiplier)
        value = min(240, value)

        color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
        color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

        return tuple(int(c) for c in color_bgr)

    def apply_elegant_glow(self, frame, x, y, color, size, intensity=0.3):
        """
        Apply subtle glow effect for depth - Apple style

        Args:
            frame: Frame to draw on
            x, y: Position
            color: Base color
            size: Glow size
            intensity: Glow intensity (0-1)
        """
        glow_color = tuple(int(c * intensity) for c in color)
        cv2.circle(frame, (x, y), size + 4, glow_color, -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, (x, y), size + 2, tuple(int(c * intensity * 1.5) for c in color),
                  -1, lineType=cv2.LINE_AA)

    def draw_mode_1_vinyl_grooves(self, frame, magnitudes):
        """Mode 1: Rotating vinyl record grooves"""
        # Update rotation
        avg_magnitude = np.mean(magnitudes)
        self.rotation_angle += 0.5 + avg_magnitude * 2

        # Draw concentric grooves that pulse with music
        num_grooves = 30
        max_thickness = 4

        for groove_idx in range(num_grooves):
            groove_progress = groove_idx / num_grooves
            base_radius = int(self.max_radius * 0.3 + groove_progress * self.max_radius * 0.6)

            # Get magnitude for this groove (map to frequency bands)
            mag_idx = int(groove_progress * len(magnitudes))
            magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

            # Radius varies with music
            radius_variation = int(magnitude * 8)
            radius = base_radius + radius_variation

            # Color: warm analog colors (amber/gold)
            hue = 30 + magnitude * 20  # Amber to gold range
            saturation = 180 + int(magnitude * 75)
            value = 150 + int(magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            # Thickness varies with magnitude
            thickness = max(1, int(magnitude * max_thickness))

            # Draw groove circle
            cv2.circle(frame, (self.center_x, self.center_y), radius, color,
                      thickness, lineType=cv2.LINE_AA)

        # Draw center label (like vinyl center)
        label_radius = int(self.max_radius * 0.2)
        cv2.circle(frame, (self.center_x, self.center_y), label_radius,
                  (200, 180, 140), 2, lineType=cv2.LINE_AA)

        # Add rotating marker line (like the vinyl groove indicator)
        angle_rad = np.deg2rad(self.rotation_angle)
        line_start = int(self.max_radius * 0.25)
        line_end = int(self.max_radius * 0.9)

        x1 = int(self.center_x + line_start * np.cos(angle_rad))
        y1 = int(self.center_y + line_start * np.sin(angle_rad))
        x2 = int(self.center_x + line_end * np.cos(angle_rad))
        y2 = int(self.center_y + line_end * np.sin(angle_rad))

        cv2.line(frame, (x1, y1), (x2, y2), (180, 160, 120), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_226_golden_phyllotaxis_bloom(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        self.phyllotaxis_breath = 0.98*self.phyllotaxis_breath + 0.02*(0.8 + bass*0.6)
        dot_count = 1200
        angle_deg = self.phyllotaxis_angle
        scale = 2.0 * self.phyllotaxis_breath
        jitter = highs * 2.0
        for i in range(dot_count):
            a = np.radians(i*angle_deg)
            r = scale*np.sqrt(i)
            x = int(self.center_x + (r*np.cos(a)) + np.random.uniform(-jitter, jitter))
            y = int(self.center_y + (r*np.sin(a)) + np.random.uniform(-jitter, jitter))
            if 0 <= x < self.width and 0 <= y < self.height:
                frame[y, x] = (150, 180, 255)
        return frame

    def draw_mode_227_breathing_mandala_weave(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        tempo = float(np.mean(magnitudes))
        self.mandala_weave_phase += 0.01 + tempo*0.02
        segments = 12
        radius = int(120 + bass*120)
        for i in range(segments):
            ang = (i/segments)*2*np.pi + self.mandala_weave_phase
            x1 = int(self.center_x + np.cos(ang)*radius)
            y1 = int(self.center_y + np.sin(ang)*radius)
            ang2 = ang + np.pi/segments
            x2 = int(self.center_x + np.cos(ang2)*radius)
            y2 = int(self.center_y + np.sin(ang2)*radius)
            cv2.line(frame,(x1,y1),(x2,y2),(200,180,255),2, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_228_infinite_tunnel_lissajous(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        mids = float(np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]))
        self.lissajous_t += 0.02
        for i in range(100):
            t = self.lissajous_t + i*0.1
            x = int(self.center_x + (120 + bass*100)*np.sin(t*1.0))
            y = int(self.center_y + (80 + mids*80)*np.sin(t*1.3))
            s = max(1, 6 - i//20)
            cv2.circle(frame,(x,y),s,(160,160,200),-1)
        return frame

    def draw_mode_229_lotus_bloom_cascade(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        rings = 8
        self.lotus_phase += 0.02
        for r in range(rings):
            phase = self.lotus_phase - r*0.1
            rad = int(40 + r*22 + bass*60*np.sin(phase))
            petals = 10
            for p in range(petals):
                ang = (p/petals)*2*np.pi
                x = int(self.center_x + np.cos(ang)*rad)
                y = int(self.center_y + np.sin(ang)*rad)
                color = (180, 200, 255)
                if highs>0.6 and p%3==0:
                    color = (220, 220, 255)
                cv2.circle(frame,(x,y),2,color,-1)
        return frame

    def draw_mode_230_orbital_hypno_pendula(self, frame, magnitudes):
        tempo = float(np.mean(magnitudes))
        count = 24
        if not self.hypno_pendula:
            for i in range(count):
                self.hypno_pendula.append({'phase':i*0.2})
        for i, p in enumerate(self.hypno_pendula):
            p['phase'] += 0.02 + tempo*0.02
            ang = p['phase']
            r = 160
            x = int(self.center_x + np.cos(ang+i*0.1)*r)
            y = int(self.center_y + np.sin(ang+i*0.1)*r)
            cv2.circle(frame,(x,y),3,(200,200,255),-1)
        return frame

    def draw_mode_231_moire_breathing_nets(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        self.moire_angle_a += 0.01
        self.moire_angle_b -= 0.012
        scale = 1.0 + bass*0.3
        step = 24
        for y in range(0, self.height, step):
            x1 = int(self.center_x + np.cos(self.moire_angle_a)*scale*(y-self.center_y))
            cv2.line(frame,(0,y),(self.width,y),(80,80,120),1)
            if 0 <= x1 < self.width:
                frame[y, x1] = (120, 120, 200)
        for x in range(0, self.width, step):
            y1 = int(self.center_y + np.sin(self.moire_angle_b)*scale*(x-self.center_x))
            cv2.line(frame,(x,0),(x,self.height),(80,80,120),1)
            if 0 <= y1 < self.height:
                frame[y1, x] = (120, 120, 200)
        return frame

    def draw_mode_232_spiral_shepard_rings(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        self.shepard_zoom *= 1.0 + (bass-0.5)*0.002
        for i in range(12):
            r = int((i+1)*20*self.shepard_zoom) % 240
            cv2.circle(frame,(self.center_x,self.center_y),r,(140,140,200),1)
        return frame

    def draw_mode_233_velvet_plasma_pool(self, frame, magnitudes):
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        self.plasma_shift += 0.01
        for y in range(0, self.height, 4):
            for x in range(0, self.width, 4):
                v = np.sin(x*0.01 + self.plasma_shift) + np.cos(y*0.01 - self.plasma_shift)
                c = int(120 + 40*v + highs*50)
                frame[y:y+4, x:x+4] = (c, c, 200)
        return frame

    def draw_mode_234_radial_pulse_cathedral(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        self.pulse_timer += 1
        if self.pulse_timer % int(max(5, 30 - bass*20)) == 0:
            for r in range(30, 260, 20):
                cv2.circle(frame,(self.center_x,self.center_y),r,(160,160,220),1)
        return frame

    def draw_mode_235_s_curve_serpents(self, frame, magnitudes):
        mids = float(np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]))
        amp = 60 + int(mids*120)
        points = []
        for t in range(0, 360, 4):
            x = int(self.center_x + t - 180)
            y = int(self.center_y + np.sin((t/30)+self.frame_counter*0.05)*amp)
            points.append((x,y))
        for i in range(1,len(points)):
            cv2.line(frame, points[i-1], points[i], (200,180,255), 2, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_236_orb_choir_orbitals(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        if not self.orb_choir:
            for i in range(20):
                self.orb_choir.append({'ang':i*0.3})
        for i, o in enumerate(self.orb_choir):
            o['ang'] += 0.01
            a = o['ang']
            r = 120 + int(bass*80)
            x = int(self.center_x + np.cos(a+i*0.1)*r)
            y = int(self.center_y + np.sin(a+i*0.13)*r*0.8)
            cv2.circle(frame,(x,y),3,(180,200,255),-1)
        return frame

    def draw_mode_237_sufi_spin_carpet(self, frame, magnitudes):
        self.sufi_spin_angle += 0.01
        for i in range(12):
            ang = self.sufi_spin_angle + i*0.5
            x1 = int(self.center_x + np.cos(ang)*180)
            y1 = int(self.center_y + np.sin(ang)*180)
            cv2.line(frame,(self.center_x,self.center_y),(x1,y1),(160,160,220),1)
        return frame

    def draw_mode_238_helmholtz_rings(self, frame, magnitudes):
        tempo = float(np.mean(magnitudes))
        self.helmholtz_phase += 0.01 + tempo*0.01
        for i in range(12):
            r = int(40 + i*16 + np.sin(self.helmholtz_phase + i*0.2)*12)
            cv2.circle(frame,(self.center_x,self.center_y),r,(180,180,240),1)
        return frame

    def draw_mode_239_hypno_slinky_stairwell(self, frame, magnitudes):
        self.slinky_depth += 0.6
        for i in range(40):
            t = (self.slinky_depth + i*12) % (self.height+80)
            y = int(t - 40)
            x = int(self.center_x + (i-20)*6)
            cv2.rectangle(frame,(x-20,y-6),(x+20,y+6),(120,120,180),1)
        return frame

    def draw_mode_240_fractal_fern_drift(self, frame, magnitudes):
        if len(self.fern_points) < 4000:
            x, y = 0.0, 0.0
            for _ in range(1000):
                r = np.random.random()
                if r < 0.01:
                    x, y = 0.0, 0.16*y
                elif r < 0.86:
                    x, y = 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
                elif r < 0.93:
                    x, y = 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
                else:
                    x, y = -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44
                self.fern_points.append((x,y))
        for px, py in self.fern_points[::10]:
            sx = int(self.center_x + px*60)
            sy = int(self.height-80 - py*60)
            if 0 <= sx < self.width and 0 <= sy < self.height:
                frame[sy, sx] = (160, 200, 160)
        return frame

    def draw_mode_241_binaural_circles(self, frame, magnitudes):
        left = float(np.mean(magnitudes[:len(magnitudes)//8]))
        right = float(np.mean(magnitudes[len(magnitudes)//8:len(magnitudes)//4]))
        self.binaural_phase_l += 0.02 + left*0.02
        self.binaural_phase_r += 0.021 + right*0.02
        rl = int(80 + np.sin(self.binaural_phase_l)*30)
        rr = int(80 + np.sin(self.binaural_phase_r)*30)
        cv2.circle(frame,(self.center_x-80,self.center_y),rl,(180,180,240),2)
        cv2.circle(frame,(self.center_x+80,self.center_y),rr,(180,180,240),2)
        return frame

    def draw_mode_242_auric_chakric_wheel(self, frame, magnitudes):
        self.chakric_phase += 0.01
        for i, ry in enumerate(range(self.center_y-180, self.center_y+220, 60)):
            r = int(30 + np.sin(self.chakric_phase + i*0.3)*20)
            cv2.circle(frame,(self.center_x, ry), r, (160,160,220), 2)
        return frame

    def draw_mode_243_hypersphere_ribbon(self, frame, magnitudes):
        self.hypersphere_phase += 0.02
        for i in range(120):
            t = i/120 * 2*np.pi
            x = int(self.center_x + 160*np.cos(t)*np.cos(self.hypersphere_phase))
            y = int(self.center_y + 90*np.sin(t)*np.sin(self.hypersphere_phase))
            frame[y, x] = (180, 180, 255)
        return frame

    def draw_mode_244_phi_step_kaleidos(self, frame, magnitudes):
        self.phi_kaleidos_phase += 0.02
        seg = 8
        for i in range(seg):
            ang = self.phi_kaleidos_phase + i*(2*np.pi/seg)
            x = int(self.center_x + np.cos(ang)*180)
            y = int(self.center_y + np.sin(ang)*180)
            cv2.line(frame,(self.center_x,self.center_y),(x,y),(160,160,220),1)
        return frame

    def draw_mode_245_silk_ribbon_cycloid(self, frame, magnitudes):
        self.cycloid_phase += 0.02
        for t in np.linspace(0, 4*np.pi, 200):
            x = int(self.center_x + 120*(np.cos(t) + 0.5*np.cos(2*t+self.cycloid_phase)))
            y = int(self.center_y + 80*(np.sin(t) - 0.5*np.sin(2*t+self.cycloid_phase)))
            if 0 <= x < self.width and 0 <= y < self.height:
                frame[y, x] = (200, 180, 255)
        return frame

    def draw_mode_246_oceanic_breather(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        self.ocean_swell = 0.98*self.ocean_swell + 0.02*(bass*60)
        for x in range(0, self.width, 6):
            y = int(self.center_y + np.sin(x*0.02 + self.frame_counter*0.04)* (20 + self.ocean_swell))
            cv2.line(frame,(x,y),(x,y+2),(160,200,255),1)
        return frame

    def draw_mode_247_zen_sand_harmonograph(self, frame, magnitudes):
        self.harmonograph_t += 0.02
        for t in np.linspace(0, 4*np.pi, 200):
            x = int(self.center_x + 140*np.sin(2*t + self.harmonograph_t))
            y = int(self.center_y + 100*np.sin(3*t))
            frame[y, x] = (200, 200, 255)
        return frame

    def draw_mode_248_magnetic_ink_veins(self, frame, magnitudes):
        if len(self.ink_veins) < 400:
            for _ in range(20):
                self.ink_veins.append({'x':np.random.randint(0,self.width),'y':np.random.randint(0,self.height)})
        for v in self.ink_veins:
            v['x'] = (v['x'] + np.random.randint(-1,2)) % self.width
            v['y'] = (v['y'] + np.random.randint(-1,2)) % self.height
            frame[int(v['y']), int(v['x'])] = (180, 200, 220)
        return frame

    def draw_mode_249_breath_linked_vortex(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        self.breath_vortex = 0.98*self.breath_vortex + 0.02*(120 + bass*160)
        for a in np.linspace(0, 2*np.pi, 180):
            r = int(self.breath_vortex * (a/(2*np.pi)))
            x = int(self.center_x + np.cos(a)*r)
            y = int(self.center_y + np.sin(a)*r)
            frame[y, x] = (180, 180, 240)
        return frame

    def draw_mode_250_slow_meteor_carousel(self, frame, magnitudes):
        if not self.meteor_carousel:
            for i in range(18):
                self.meteor_carousel.append({'a':i*(2*np.pi/18)})
        for m in self.meteor_carousel:
            m['a'] += 0.005
            x = int(self.center_x + 160*np.cos(m['a']))
            y = int(self.center_y + 160*np.sin(m['a']))
            cv2.circle(frame,(x,y),2,(200,200,255),-1)
        return frame

    def draw_mode_251_ripple_glass_cathedral(self, frame, magnitudes):
        self.ripple_glass_phase += 0.02
        for y in range(0, self.height, 8):
            for x in range(0, self.width, 8):
                dx = int(2*np.sin(self.ripple_glass_phase + y*0.05))
                dy = int(2*np.cos(self.ripple_glass_phase + x*0.05))
                xx = min(self.width-1, max(0, x+dx))
                yy = min(self.height-1, max(0, y+dy))
                frame[y:y+8, x:x+8] = frame[yy:yy+8, xx:xx+8]
        return frame

    def draw_mode_252_theta_lantern_field(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        if len(self.theta_lanterns) < 40 and np.random.random()<0.3:
            self.theta_lanterns.append({'x':np.random.randint(40,self.width-40),'y':self.height+20,'vy':-1.0 - bass*1.5,'p':np.random.random()*2*np.pi})
        for lan in self.theta_lanterns[:]:
            lan['y'] += lan['vy']
            if lan['y'] < -40:
                self.theta_lanterns.remove(lan)
                continue
            r = int(10 + (np.sin(self.frame_counter*0.1 + lan['p'])+1)*4)
            cv2.circle(frame,(int(lan['x']),int(lan['y'])),r,(200,180,140),-1)
        return frame

    def draw_mode_253_isochromatic_weaves(self, frame, magnitudes):
        self.iso_weave_phase += 0.01
        for i in range(0,self.width,20):
            y = int(self.center_y + np.sin(i*0.03 + self.iso_weave_phase)*40)
            cv2.line(frame,(i,y-10),(i,y+10),(200,180,255),1)
        for j in range(0,self.height,20):
            x = int(self.center_x + np.cos(j*0.03 + self.iso_weave_phase)*40)
            cv2.line(frame,(x-10,j),(x+10,j),(180,200,255),1)
        return frame

    def draw_mode_254_orbiting_eye(self, frame, magnitudes):
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        self.orbiting_eye_angle += 0.01
        r = int(60 + bass*60)
        cv2.circle(frame,(self.center_x,self.center_y), r, (160,160,220), 2)
        x = int(self.center_x + np.cos(self.orbiting_eye_angle)*r)
        y = int(self.center_y + np.sin(self.orbiting_eye_angle)*r)
        cv2.circle(frame,(x,y),4,(220,220,255),-1)
        return frame

    def draw_mode_255_endless_ribbon_stair(self, frame, magnitudes):
        self.ribbon_stair_phase += 0.01
        for i in range(40):
            t = i/40
            x = int(self.center_x + (t-0.5)*300)
            y = int(self.center_y + np.sin(self.ribbon_stair_phase + t*6)*60)
            cv2.rectangle(frame,(x-6,y-20),(x+6,y+20),(160,160,220),1)
        return frame

    def draw_mode_256_glassy_toroidal_river(self, frame, magnitudes):
        self.toroidal_flow += 0.01
        for i in range(160):
            t = i/160
            ang = t*2*np.pi
            x = int(self.center_x + 160*np.cos(ang))
            y = int(self.center_y + 80*np.sin(ang) + np.sin(self.toroidal_flow+t*8)*6)
            frame[y, x] = (180, 200, 230)
        return frame

    def draw_mode_257_low_poly_hypno_shell(self, frame, magnitudes):
        self.hypno_shell_twist += 0.01
        for i in range(60):
            t = i/60
            r = int(40 + t*200)
            ang = self.hypno_shell_twist + t*6*np.pi
            x = int(self.center_x + np.cos(ang)*r)
            y = int(self.center_y + np.sin(ang)*r)
            cv2.circle(frame,(x,y),2,(200,200,240),-1)
        return frame

    def draw_mode_258_tide_clock_halo(self, frame, magnitudes):
        self.tide_clock_phase += 0.01
        r = int(120 + np.sin(self.tide_clock_phase)*20)
        cv2.circle(frame,(self.center_x,self.center_y),r,(160,160,220),2)
        ang = self.tide_clock_phase
        x = int(self.center_x + np.cos(ang)*r)
        y = int(self.center_y + np.sin(ang)*r)
        cv2.circle(frame,(x,y),4,(220,220,255),-1)
        return frame

    def draw_mode_259_morphic_kaleidofish(self, frame, magnitudes):
        if len(self.kaleidofish_school) < 50:
            for _ in range(50 - len(self.kaleidofish_school)):
                self.kaleidofish_school.append({'x':np.random.randint(0,self.width),'y':np.random.randint(0,self.height),'vx':np.random.uniform(-1,1),'vy':np.random.uniform(-1,1)})
        for f in self.kaleidofish_school:
            f['x'] = (f['x'] + f['vx']) % self.width
            f['y'] = (f['y'] + f['vy']) % self.height
            frame[int(f['y']), int(f['x'])] = (200, 200, 255)
        return frame

    def draw_mode_260_zen_compass_waves(self, frame, magnitudes):
        self.compass_wave_phase += 0.01
        for i in range(8):
            ang = i*(np.pi/4)
            for r in range(40, 220, 20):
                x = int(self.center_x + np.cos(ang + self.compass_wave_phase)*r)
                y = int(self.center_y + np.sin(ang + self.compass_wave_phase)*r)
                cv2.circle(frame,(x,y),2,(180,180,230),-1)
        return frame

    def draw_mode_261_glacial_bloom(self, frame, magnitudes):
        if len(self.glacial_bloom) < 200:
            for _ in range(10):
                self.glacial_bloom.append({'x':self.center_x,'y':self.center_y,'vx':np.random.uniform(-1,1),'vy':np.random.uniform(-1,1),'life':200})
        for g in self.glacial_bloom[:]:
            g['x'] += g['vx']; g['y'] += g['vy']; g['life'] -= 1
            cv2.circle(frame,(int(g['x']),int(g['y'])),1,(200,220,255),-1)
            if g['life']<=0: self.glacial_bloom.remove(g)
        return frame

    def draw_mode_262_double_helix_lanterns(self, frame, magnitudes):
        if len(self.helix_lanterns) < 80:
            for i in range(80):
                self.helix_lanterns.append({'t':i*0.1})
        for h in self.helix_lanterns:
            h['t'] += 0.01
            x = int(self.center_x + 120*np.cos(h['t']))
            y = int(100 + (h['t']%(2*np.pi))/(2*np.pi) * (self.height-200))
            cv2.circle(frame,(x,y),2,(220,200,160),-1)
            x2 = int(self.center_x - 120*np.cos(h['t']))
            cv2.circle(frame,(x2,y),2,(220,200,160),-1)
        return frame

    def draw_mode_263_soft_grid_phase_slide(self, frame, magnitudes):
        self.soft_grid_phase += 0.01
        step = 30
        for y in range(0,self.height,step):
            for x in range(0,self.width,step):
                xx = x + int(4*np.sin(self.soft_grid_phase + y*0.05))
                yy = y + int(4*np.cos(self.soft_grid_phase + x*0.05))
                cv2.circle(frame,(xx,yy),1,(160,160,220),-1)
        return frame

    def draw_mode_264_ripple_dome_observatory(self, frame, magnitudes):
        self.ripple_dome_phase += 0.02
        for r in range(40, 260, 12):
            jitter = int(4*np.sin(self.ripple_dome_phase + r*0.05))
            cv2.circle(frame,(self.center_x,self.center_y), r+jitter, (160,160,230), 1)
        return frame

    def draw_mode_265_ethereal_spirocloud(self, frame, magnitudes):
        if len(self.spirocloud_traces) < 200:
            t = self.frame_counter*0.02
            x = int(self.center_x + 120*np.cos(2*t) + 40*np.cos(6*t))
            y = int(self.center_y + 80*np.sin(3*t) + 30*np.sin(5*t))
            self.spirocloud_traces.append((x,y))
        else:
            self.spirocloud_traces.pop(0)
        for i in range(1,len(self.spirocloud_traces)):
            a = int(i/len(self.spirocloud_traces)*200 + 55)
            cv2.line(frame,self.spirocloud_traces[i-1],self.spirocloud_traces[i],(a,a,255),1)
        return frame

    def draw_mode_266_mosaic_drizzle(self, frame, magnitudes):
        if not self.mosaic_cells:
            rows, cols = 18, 18
            for r in range(rows):
                for c in range(cols):
                    self.mosaic_cells.append({'r':r,'c':c,'val':np.random.randint(120,200)})
        for cell in self.mosaic_cells:
            if np.random.random()<0.01:
                cell['val'] = min(255, max(80, cell['val'] + np.random.randint(-5,6)))
            x = int(cell['c']*self.width/18)
            y = int(cell['r']*self.height/18)
            w = self.width//18
            h = self.height//18
            frame[y:y+h, x:x+w] = (cell['val'], cell['val'], 220)
        return frame

    def draw_mode_267_whispering_bamboo(self, frame, magnitudes):
        if not self.bamboo_stalks:
            for x in range(60, self.width, 60):
                self.bamboo_stalks.append({'x':x,'o':np.random.random()*6.28})
        for b in self.bamboo_stalks:
            sway = int(10*np.sin(self.frame_counter*0.03 + b['o']))
            cv2.line(frame,(b['x']+sway, self.height-40),(b['x']+sway, 160),(120,180,120),3)
        return frame

    def draw_mode_268_nesting_circles_flow(self, frame, magnitudes):
        self.nesting_circles_phase += 0.02
        for i in range(10):
            r = int(30 + i*18 + np.sin(self.nesting_circles_phase + i)*8)
            cv2.circle(frame,(self.center_x,self.center_y),r,(160,160,220),1)
        return frame

    def draw_mode_269_drifting_paper_cranes(self, frame, magnitudes):
        if not self.paper_cranes:
            for _ in range(24):
                self.paper_cranes.append({'x':np.random.randint(0,self.width),'y':np.random.randint(0,self.height),'vx':np.random.uniform(-0.6,0.6),'vy':np.random.uniform(-0.3,0.0)})
        for c in self.paper_cranes:
            c['x'] = (c['x'] + c['vx']) % self.width
            c['y'] = (c['y'] + c['vy']) % self.height
            cv2.circle(frame,(int(c['x']),int(c['y'])),2,(220,220,240),-1)
        return frame

    def draw_mode_270_pulse_weave_hologrid(self, frame, magnitudes):
        self.pulse_hologrid_phase += 0.02
        for i in range(0,self.width,24):
            y = int(self.center_y + np.sin(self.pulse_hologrid_phase + i*0.05)*40)
            cv2.line(frame,(i,y-6),(i,y+6),(160,160,230),1)
        for j in range(0,self.height,24):
            x = int(self.center_x + np.cos(self.pulse_hologrid_phase + j*0.05)*40)
            cv2.line(frame,(x-6,j),(x+6,j),(160,160,230),1)
        return frame

    def draw_mode_271_serene_ribbon_canopy(self, frame, magnitudes):
        if not self.ribbon_canopy:
            for i in range(140):
                self.ribbon_canopy.append({'x':np.random.randint(0,self.width),'y':np.random.randint(-self.height,0)})
        for r in self.ribbon_canopy:
            r['y'] += 1
            if r['y'] > self.height:
                r['y'] = -np.random.randint(0,self.height)
            cv2.line(frame,(r['x'],r['y']),(r['x'],r['y']+8),(180,180,230),1)
        return frame

    def draw_mode_272_auroral_veil_gate(self, frame, magnitudes):
        self.auroral_gate_phase += 0.02
        for i in range(8):
            ang = i*(2*np.pi/8)
            for r in range(60, 220, 20):
                x = int(self.center_x + np.cos(ang + self.auroral_gate_phase)*r)
                y = int(self.center_y + np.sin(ang + self.auroral_gate_phase)*r)
                frame[y, x] = (180, 200, 255)
        return frame

    def draw_mode_273_satin_spiral_ladder(self, frame, magnitudes):
        self.satin_ladder_phase += 0.01
        for i in range(80):
            t = i/80
            ang = self.satin_ladder_phase + t*4*np.pi
            x = int(self.center_x + np.cos(ang)*140)
            y = int(self.center_y + np.sin(ang)*100)
            cv2.line(frame,(x-6,y),(x+6,y),(200,200,250),1)
        return frame

    def draw_mode_274_opaline_orb_drifter(self, frame, magnitudes):
        self.opaline_orb_t += 0.01
        x = int(self.center_x + np.sin(self.opaline_orb_t)*40)
        y = int(self.center_y - 30 + np.cos(self.opaline_orb_t*0.7)*20)
        cv2.circle(frame,(x,y), 60, (180, 200, 240), 2)
        return frame

    def draw_mode_275_hypno_quilt_loom(self, frame, magnitudes):
        self.quilt_loom_phase += 0.02
        step = 20
        for y in range(200, self.height-200, step):
            for x in range(100, self.width-100, step):
                if (x//step + y//step) % 2 == 0:
                    xx = int(x + 4*np.sin(self.quilt_loom_phase + y*0.05))
                    yy = int(y + 4*np.cos(self.quilt_loom_phase + x*0.05))
                    cv2.circle(frame,(xx,yy),1,(200,200,255),-1)
        return frame

    def draw_mode_176_event_horizon_lattice(self, frame, magnitudes):
        """Mode 176: Event Horizon Lattice - warped grid bends toward a black hole; streaks on transients"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        warp_strength = 0.3 + bass * 1.2

        rows = 16
        cols = 16
        for r in range(rows + 1):
            y = int(r * self.height / rows)
            prev_pt = None
            for c in range(cols + 1):
                x = int(c * self.width / cols)
                dx = x - self.center_x
                dy = y - self.center_y
                dist = max(1.0, np.hypot(dx, dy))
                pull = warp_strength * 20000.0 / dist
                px = int(x - dx / dist * pull)
                py = int(y - dy / dist * pull)
                if prev_pt is not None:
                    cv2.line(frame, prev_pt, (px, py), (60, 60, 90), 1, lineType=cv2.LINE_AA)
                prev_pt = (px, py)

        for c in range(cols + 1):
            x = int(c * self.width / cols)
            prev_pt = None
            for r in range(rows + 1):
                y = int(r * self.height / rows)
                dx = x - self.center_x
                dy = y - self.center_y
                dist = max(1.0, np.hypot(dx, dy))
                pull = warp_strength * 20000.0 / dist
                px = int(x - dx / dist * pull)
                py = int(y - dy / dist * pull)
                if prev_pt is not None:
                    cv2.line(frame, prev_pt, (px, py), (60, 60, 90), 1, lineType=cv2.LINE_AA)
                prev_pt = (px, py)

        # Time-dilation streaks on transients
        transient_indices = np.where(np.abs(np.diff(magnitudes)) > 0.25)[0]
        for idx in transient_indices[:20]:
            angle = (idx / len(magnitudes)) * 2 * np.pi
            r1 = int(self.max_radius * 0.2)
            r2 = int(self.max_radius * (0.6 + highs * 0.3))
            x1 = int(self.center_x + np.cos(angle) * r1)
            y1 = int(self.center_y + np.sin(angle) * r1)
            x2 = int(self.center_x + np.cos(angle) * r2)
            y2 = int(self.center_y + np.sin(angle) * r2)
            cv2.line(frame, (x1, y1), (x2, y2), (180, 180, 255), 1, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_177_comet_conveyor(self, frame, magnitudes):
        """Mode 177: Comet Conveyor - endless belt carries comets; tails shear on treble"""
        energy = float(np.mean(magnitudes))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))

        belt_y = int(self.center_y + np.sin(self.frame_counter * 0.03) * 30)
        cv2.line(frame, (0, belt_y), (self.width, belt_y), (80, 80, 80), 2, lineType=cv2.LINE_AA)

        # Spawn
        if len(self.comet_conveyor_belt) < 40 and np.random.random() < 0.3:
            band_idx = np.random.randint(0, len(magnitudes))
            self.comet_conveyor_belt.append({
                'x': -20,
                'y': belt_y + np.random.randint(-20, 20),
                'vx': 4 + energy * 8,
                'size': int(4 + magnitudes[band_idx] * 18),
                'shear': highs * 20
            })

        # Update/draw
        for comet in self.comet_conveyor_belt[:]:
            comet['x'] += comet['vx']
            if comet['x'] > self.width + 40:
                self.comet_conveyor_belt.remove(comet)
                continue
            cv2.circle(frame, (int(comet['x']), int(comet['y'])), comet['size'], (255, 255, 200), -1)
            for t in range(1, 6):
                px = int(comet['x'] - t * comet['vx'] * 2)
                py = int(comet['y'] - t * comet['shear'] * 0.2)
                alpha = max(20, 200 - t * 35)
                cv2.circle(frame, (px, py), max(1, comet['size'] - t), (alpha, alpha, 180), -1)
        return frame

    def draw_mode_178_quantum_foam_micro(self, frame, magnitudes):
        """Mode 178: Quantum Foam Micro - foamy micro-bubbles pop; cascades on peaks"""
        energy = float(np.mean(magnitudes))
        peak = np.max(magnitudes) > 0.8

        # Spawn bubbles
        if len(self.foam_bubbles) < 200:
            for _ in range(3):
                self.foam_bubbles.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'r': np.random.randint(1, 5),
                    'life': np.random.randint(20, 80)
                })

        for b in self.foam_bubbles[:]:
            b['life'] -= 1
            b['r'] = max(1, b['r'] + (np.random.random() - 0.5) * 0.5)
            if peak and np.random.random() < 0.2:
                # cascade: spawn smaller around
                for _ in range(3):
                    self.foam_bubbles.append({'x': b['x']+np.random.randint(-6,6), 'y': b['y']+np.random.randint(-6,6), 'r': 1, 'life': 20})
            color = int(120 + energy * 135)
            cv2.circle(frame, (int(b['x']), int(b['y'])), int(b['r']), (color, color, 255), 1, lineType=cv2.LINE_AA)
            if b['life'] <= 0:
                self.foam_bubbles.remove(b)
        return frame

    def draw_mode_179_aurora_crown(self, frame, magnitudes):
        """Mode 179: Aurora Crown - polar aurora dome overhead; ribbons brighten by mids"""
        mids = float(np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]))
        ribbon_count = 8
        for i in range(ribbon_count):
            angle = (i / ribbon_count) * 2 * np.pi
            for r in range(60, 240, 10):
                x = int(self.center_x + np.cos(angle + np.sin(self.frame_counter*0.02+i)*0.2) * r)
                y = int(self.center_y - r * 0.6 + np.sin(i*0.7 + self.frame_counter*0.05) * 10)
                color = (int(80 + mids * 175), int(120 + mids * 135), 255)
                cv2.circle(frame, (x, y), 2, color, -1)
        return frame

    def draw_mode_180_asteroid_excavator(self, frame, magnitudes):
        """Mode 180: Asteroid Excavator - drill depth increases with bass; debris size follows highs"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        center = (self.center_x, self.center_y)
        cv2.circle(frame, center, 180, (60, 60, 60), -1)
        depth = int(bass * 120)
        cv2.line(frame, (self.center_x - 200, self.center_y - 100), (self.center_x - 40 - depth, self.center_y), (200, 200, 220), 3)
        # debris
        for _ in range(int(5 + highs * 25)):
            dx = np.random.randint(-180, -40)
            dy = np.random.randint(-10, 10)
            size = max(1, int(2 + highs * 6))
            cv2.circle(frame, (self.center_x + dx, self.center_y + dy), size, (180, 180, 180), -1)
        return frame

    def draw_mode_181_hyperloop_spectrotrain(self, frame, magnitudes):
        """Mode 181: Hyperloop Spectrotrain - car length scales to energy; station lights strobe"""
        energy = float(np.mean(magnitudes))
        y = self.center_y
        cv2.line(frame, (0, y+30), (self.width, y+30), (100,100,100), 4)
        car_count = 6
        base_x = int((self.frame_counter * (2 + energy*8)) % (self.width + 400)) - 200
        for i in range(car_count):
            cx = base_x - i * 70
            w = int(40 + energy * 80)
            cv2.rectangle(frame, (cx, y-20), (cx+w, y+20), (180, 200, 255), -1)
            for k in range(4):
                cv2.rectangle(frame, (cx+5+k*int(w/4), y-12), (cx+5+k*int(w/4)+10, y-2), (255, 255, 150), -1)
        if np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]) > 0.65:
            for sx in range(0, self.width, 60):
                cv2.circle(frame, (sx, y-40), 6, (255, 255, 200), -1)
        return frame

    def draw_mode_182_galactic_pinball(self, frame, magnitudes):
        """Mode 182: Galactic Pinball - bumpers map to bands; ball boosts on peaks"""
        if not self.pinball_entities:
            self.pinball_entities = [{ 'x': self.center_x, 'y': self.center_y, 'vx': 3, 'vy': -2 }]
        ball = self.pinball_entities[0]
        peak = np.max(magnitudes) > 0.8
        if peak:
            ball['vx'] *= 1.2
            ball['vy'] *= 1.2
        ball['x'] += ball['vx']
        ball['y'] += ball['vy']
        if ball['x']<10 or ball['x']>self.width-10: ball['vx']*=-1
        if ball['y']<10 or ball['y']>self.height-10: ball['vy']*=-1
        cv2.circle(frame, (int(ball['x']), int(ball['y'])), 6, (255, 255, 255), -1)
        # bumpers
        for i in range(10):
            angle = (i/10)*2*np.pi
            r = 220
            bx = int(self.center_x + np.cos(angle)*r)
            by = int(self.center_y + np.sin(angle)*r)
            mag = magnitudes[i*(len(magnitudes)//10)]
            size = int(8 + mag*18)
            cv2.circle(frame, (bx, by), size, (100, 150, 255), -1)
        return frame

    def draw_mode_183_nebula_inkblot(self, frame, magnitudes):
        """Mode 183: Nebula Inkblot - mirrored volumetric smoke; hue by dominant band"""
        dominant_idx = int(np.argmax(magnitudes))
        hue = int((dominant_idx / max(1, len(magnitudes)-1)) * 180)
        for _ in range(120):
            x = np.random.randint(0, self.center_x)
            y = np.random.randint(0, self.height)
            jitter = int(np.random.randn()*6)
            color_hsv = np.array([[[hue, 180, 200]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            cv2.circle(frame, (x, y+jitter), 3, tuple(map(int, color)), -1)
            cv2.circle(frame, (self.width-x, y+jitter), 3, tuple(map(int, color)), -1)
        return frame

    def draw_mode_184_satellite_telemetry_rings(self, frame, magnitudes):
        """Mode 184: Satellite Telemetry Rings - rippling rings with dashed spectrum"""
        energy = float(np.mean(magnitudes))
        ring_count = 5
        for i in range(ring_count):
            radius = int(60 + i*40 + (self.frame_counter*3 + i*15) % 40)
            dash_count = 48
            for d in range(dash_count):
                t = d/dash_count
                ang = t*2*np.pi
                idx = min(int(t*len(magnitudes)), len(magnitudes)-1)
                h = magnitudes[idx]
                x1 = int(self.center_x + np.cos(ang)*radius)
                y1 = int(self.center_y + np.sin(ang)*radius)
                x2 = int(self.center_x + np.cos(ang)*(radius+int(h*25)))
                y2 = int(self.center_y + np.sin(ang)*(radius+int(h*25)))
                cv2.line(frame, (x1,y1), (x2,y2), (120,120,200), 1, lineType=cv2.LINE_AA)
        if energy < 0.15 and self.frame_counter % 6 == 0:
            cv2.circle(frame, (np.random.randint(0,self.width), np.random.randint(0,self.height)), 2, (255,120,120), -1)
        return frame

    def draw_mode_185_wormhole_origami(self, frame, magnitudes):
        """Mode 185: Wormhole Origami - sheet folds into portal; depth by bass"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        folds = 10 + int(np.mean(magnitudes[3*len(magnitudes)//4:]) * 10)
        for i in range(folds):
            t = i/folds
            angle = t*np.pi
            r = int(200 + bass*120 * np.cos(angle))
            cv2.ellipse(frame, (self.center_x,self.center_y), (r,int(r*0.5)), 0, 0, 360, (160,160,255), 1, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_186_holographic_jellyfish(self, frame, magnitudes):
        """Mode 186: Holographic Jellyfish - bell pulsates with lows; tentacles sparkle with highs"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        r = int(60 + bass*120)
        cv2.circle(frame, (self.center_x,self.center_y-60), r, (200,200,255), 2)
        for t in range(20):
            ang = (t/20)*np.pi
            x = int(self.center_x + np.cos(ang)*r*0.6)
            y = int(self.center_y-60 + np.sin(ang)*r*0.3)
            ty = y
            for k in range(8):
                nx = int(x + np.sin(self.frame_counter*0.08+k+t)*4)
                ny = int(ty + k*14)
                cv2.circle(frame,(nx,ny),1,(255,255,180),-1)
        for _ in range(int(highs*30)):
            cv2.circle(frame,(np.random.randint(self.center_x-r,self.center_x+r),np.random.randint(self.center_y-60,self.center_y+r)),1,(255,255,200),-1)
        return frame

    def draw_mode_187_moon_quarry_crane(self, frame, magnitudes):
        """Mode 187: Moon Quarry Crane - bins heights equal band magnitude; dust on kicks"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        bins = min(24, len(magnitudes))
        gap = self.width // (bins+2)
        for i in range(bins):
            h = int(magnitudes[i]*220)
            x = gap*(i+1)
            cv2.rectangle(frame,(x,self.center_y-h),(x+10,self.center_y),(180,180,220),-1)
        if bass>0.65:
            for _ in range(40):
                cv2.circle(frame,(np.random.randint(0,self.width), self.center_y-np.random.randint(0,80)),1,(220,220,220),-1)
        return frame

    def draw_mode_188_constellation_typoplot(self, frame, magnitudes):
        """Mode 188: Constellation TypoPlot - letters as stars; lines draw when band is hot"""
        cols = min(40, len(magnitudes))
        pts = []
        for i in range(cols):
            t = i/cols
            x = int(80 + t*(self.width-160))
            y = int(160 + np.sin(self.frame_counter*0.02 + t*6)*60)
            pts.append((x,y))
            cv2.circle(frame,(x,y),2,(200,200,255),-1)
        thr = 0.55
        for i in range(1, cols):
            if magnitudes[i]>thr:
                cv2.line(frame, pts[i-1], pts[i], (255,255,255), 1, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_189_cryo_crystal_garden(self, frame, magnitudes):
        """Mode 189: Cryo Crystal Garden - crystals grow per frequency slice; flare on treble"""
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        slices = 18
        for i in range(slices):
            idx = min(int(i * len(magnitudes)/slices), len(magnitudes)-1)
            mag = magnitudes[idx]
            angle = (i/slices)*2*np.pi
            length = int(40 + mag*180)
            x1 = self.center_x
            y1 = self.center_y
            x2 = int(x1 + np.cos(angle)*length)
            y2 = int(y1 + np.sin(angle)*length)
            cv2.line(frame,(x1,y1),(x2,y2),(200,220,255),2, lineType=cv2.LINE_AA)
        if highs>0.6:
            cv2.circle(frame,(self.center_x,self.center_y),6,(255,255,255),-1)
        return frame

    def draw_mode_190_meteorite_blueprint(self, frame, magnitudes):
        """Mode 190: Meteorite Blueprint - technical UI; callouts to bands; red stamp on peaks"""
        for x in range(0,self.width,60):
            cv2.line(frame,(x,0),(x,self.height),(40,40,70),1)
        for y in range(0,self.height,60):
            cv2.line(frame,(0,y),(self.width,y),(40,40,70),1)
        for i in range(0, len(magnitudes), max(1,len(magnitudes)//20)):
            mag = magnitudes[i]
            x = 80 + int(i/len(magnitudes)*(self.width-160))
            y = self.center_y
            cv2.circle(frame,(x,y),4,(180,220,255),-1)
            cv2.line(frame,(x,y),(x,int(y-80-mag*120)),(120,180,255),1)
        if np.max(magnitudes)>0.85:
            cv2.rectangle(frame,(self.width-140,40),(self.width-40,100),(0,0,200),-1)
        return frame

    def draw_mode_191_lunar_tide_pool(self, frame, magnitudes):
        """Mode 191: Lunar Tide Pool - water level by bass; caustics sharpen with highs"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        level = int(self.center_y + 80 - bass*150)
        cv2.rectangle(frame,(0,level),(self.width,self.height),(120,160,220),-1)
        for x in range(0,self.width,10):
            y = level + int(np.sin(self.frame_counter*0.1 + x*0.05)* (6+highs*12))
            cv2.line(frame,(x,y),(x,y+3),(200,220,255),1)
        return frame

    def draw_mode_192_orbital_barcode_slicer(self, frame, magnitudes):
        """Mode 192: Orbital Barcode Slicer - rings slice vertical barcode; brightness per band"""
        bar_count = min(40, len(magnitudes))
        bar_w = max(2, self.width//(bar_count*2))
        for i in range(bar_count):
            h = int(magnitudes[i]*(self.height//2))
            x = int(self.center_x - bar_count*bar_w + i*2*bar_w)
            cv2.rectangle(frame,(x,self.center_y-h),(x+bar_w,self.center_y+h),(80,80,120),-1)
        ring_r = int(120 + (self.frame_counter*2 % 120))
        cv2.circle(frame,(self.center_x,self.center_y), ring_r,(180,180,255),2)
        return frame

    def draw_mode_193_satellite_swarm_flocking(self, frame, magnitudes):
        """Mode 193: Satellite Swarm Flocking - simple flock; thrust bursts on kick"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        if len(self.satellites_swarm) < 40:
            for _ in range(40 - len(self.satellites_swarm)):
                self.satellites_swarm.append({'x':np.random.randint(0,self.width),'y':np.random.randint(0,self.height),'vx':np.random.uniform(-1,1),'vy':np.random.uniform(-1,1)})
        for s in self.satellites_swarm:
            s['vx'] += (np.random.random()-0.5)*0.2
            s['vy'] += (np.random.random()-0.5)*0.2
            if bass>0.6:
                s['vx'] *= 1.1; s['vy'] *= 1.1
            s['x'] = (s['x'] + s['vx'])%self.width
            s['y'] = (s['y'] + s['vy'])%self.height
            cv2.circle(frame,(int(s['x']),int(s['y'])),2,(200,200,255),-1)
        return frame

    def draw_mode_194_astro_pulse_weave(self, frame, magnitudes):
        """Mode 194: Astro Pulse Weave - two opposing spiral waves; brightness sum of bands"""
        total = float(np.sum(magnitudes))
        for i in range(180):
            t = i/180
            ang = t*4*np.pi + self.frame_counter*0.02
            r = int(40 + t*260)
            x1 = int(self.center_x + np.cos(ang)*r)
            y1 = int(self.center_y + np.sin(ang)*r)
            x2 = int(self.center_x + np.cos(-ang)*r)
            y2 = int(self.center_y + np.sin(-ang)*r)
            color = min(255, int(80 + total*60))
            cv2.circle(frame,(x1,y1),1,(color, color, 255),-1)
            cv2.circle(frame,(x2,y2),1,(color, color, 255),-1)
        return frame

    def draw_mode_195_zero_g_paint_spheres(self, frame, magnitudes):
        """Mode 195: Zero-G Paint Spheres - spheres merge on peaks and split on highs"""
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        peak = np.max(magnitudes) > 0.85
        if len(self.paint_spheres) < 12:
            for _ in range(12 - len(self.paint_spheres)):
                self.paint_spheres.append({'x':np.random.randint(100,self.width-100),'y':np.random.randint(100,self.height-100),'r':np.random.randint(10,30)})
        if peak and len(self.paint_spheres)>1:
            a = self.paint_spheres.pop(); b = self.paint_spheres.pop()
            cx = int((a['x']+b['x'])/2); cy = int((a['y']+b['y'])/2)
            cr = int(min(80, a['r']+b['r']))
            self.paint_spheres.append({'x':cx,'y':cy,'r':cr})
        if highs>0.65 and len(self.paint_spheres)<20:
            self.paint_spheres.append({'x':np.random.randint(80,self.width-80),'y':np.random.randint(80,self.height-80),'r':12})
        for s in self.paint_spheres:
            cv2.circle(frame,(int(s['x']),int(s['y'])),int(s['r']),(160,200,255),-1)
        return frame

    def draw_mode_196_supernova_countdown(self, frame, magnitudes):
        """Mode 196: Supernova Countdown - star swells with energy; blasts at threshold"""
        self.supernova_state['energy'] += float(np.mean(magnitudes))*0.02
        threshold = 1.0
        if not self.supernova_state['blasting'] and self.supernova_state['energy']>threshold:
            self.supernova_state['blasting'] = True
            for i in range(80):
                ang = (i/80)*2*np.pi
                self.supernova_state['filaments'].append({'x':self.center_x,'y':self.center_y,'vx':np.cos(ang)*(2+np.random.random()*3),'vy':np.sin(ang)*(2+np.random.random()*3),'life':60})
        if not self.supernova_state['blasting']:
            r = int(40 + self.supernova_state['energy']*160)
            cv2.circle(frame,(self.center_x,self.center_y),r,(255,220,150),-1)
        else:
            for f in self.supernova_state['filaments'][:]:
                f['x'] += f['vx']; f['y'] += f['vy']; f['life'] -= 1
                cv2.circle(frame,(int(f['x']),int(f['y'])),1,(255,200,150),-1)
                if f['life']<=0:
                    self.supernova_state['filaments'].remove(f)
        return frame

    def draw_mode_197_martian_wind_harp(self, frame, magnitudes):
        """Mode 197: Martian Wind Harp - dunes as strings; ripples by mids; dust devils on snares"""
        mids = float(np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]))
        for y in range(200, self.height, 40):
            for x in range(0, self.width, 8):
                dy = int(np.sin(x*0.05 + self.frame_counter*0.08)*mids*20)
                frame[min(self.height-1,y+dy), min(self.width-1,x)] = (160,120,90)
        if mids>0.65:
            for _ in range(40):
                cv2.circle(frame,(np.random.randint(0,self.width),np.random.randint(200,self.height)),2,(200,180,150),-1)
        return frame

    def draw_mode_198_teleporting_bar_choir(self, frame, magnitudes):
        """Mode 198: Teleporting Bar Choir - bars pop at random radial positions; decay persists"""
        if self.frame_counter % max(1, int(8 - np.mean(magnitudes[3*len(magnitudes)//4:]) * 6)) == 0:
            idx = np.random.randint(0, len(magnitudes))
            angle = np.random.random()*2*np.pi
            radius = np.random.randint(40, self.max_radius)
            x = int(self.center_x + np.cos(angle)*radius)
            y = int(self.center_y + np.sin(angle)*radius)
            self.teleporting_bars.append({'x':x,'y':y,'h':int(30 + magnitudes[idx]*160),'life':50})
        for b in self.teleporting_bars[:]:
            cv2.line(frame,(b['x'],b['y']), (b['x'], b['y']-b['h']), (200,200,255), 2)
            b['life'] -= 1
            b['h'] = max(0, b['h']-2)
            if b['life']<=0: self.teleporting_bars.remove(b)
        return frame

    def draw_mode_199_cosmic_vinyl_halo(self, frame, magnitudes):
        """Mode 199: Cosmic Vinyl Halo - record edge-on; grooves shimmer with spectrum"""
        for i in range(12):
            r = 40 + i*12
            val = magnitudes[min(int(i/12*len(magnitudes)), len(magnitudes)-1)]
            cv2.ellipse(frame,(self.center_x,self.center_y),(r,int(r*0.1)),90,0,360,(80,80,80),1)
            cv2.ellipse(frame,(self.center_x,self.center_y),(r,int(r*0.1)),90,0,int(val*360),(160,160,255),2)
        return frame

    def draw_mode_200_photon_origination_chamber(self, frame, magnitudes):
        """Mode 200: Photon Origination Chamber - photons exit slits; rate per band bucket"""
        slit_count = 8
        for s in range(slit_count):
            x = int(self.center_x - 160 + s*(320//(slit_count-1)))
            cv2.line(frame,(x,self.center_y-60),(x,self.center_y+60),(120,120,150),2)
            idx = min(int(s/slit_count*len(magnitudes)), len(magnitudes)-1)
            rate = int(magnitudes[idx]*6)
            for _ in range(rate):
                px = x + np.random.randint(-2,2)
                py = self.center_y + np.random.randint(-2,2)
                cv2.circle(frame,(px,py-70),1,(255,255,200),-1)
        return frame

    def draw_mode_201_meteor_net(self, frame, magnitudes):
        """Mode 201: Meteor Net - hex net catches meteors; nodes glow by band"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        size = 24
        for y in range(100, self.height-100, size):
            for x in range(80, self.width-80, size):
                idx = ((x+y)//size) % len(magnitudes)
                glow = int(80 + magnitudes[idx]*175)
                cv2.circle(frame,(x,y),3,(glow,glow,255),-1)
        if np.max(magnitudes)>0.9:
            cv2.circle(frame,(self.center_x,self.center_y),int(80 + bass*140),(255,255,255),1)
        return frame

    def draw_mode_202_deep_space_garden_hose(self, frame, magnitudes):
        """Mode 202: Deep-Space Garden Hose - spray pressure by amplitude; droplets chime on highs"""
        amp = float(np.mean(magnitudes))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        for i in range(int(30 + amp*120)):
            ang = -np.pi/6 + np.random.random()*np.pi/3
            r = 10 + np.random.random()* (120 + amp*200)
            x = int(self.center_x + np.cos(ang)*r)
            y = int(self.center_y + np.sin(ang)*r)
            cv2.circle(frame,(x,y),1,(200,200,255),-1)
        if highs>0.6:
            for _ in range(8):
                cv2.circle(frame,(np.random.randint(self.center_x-80,self.center_x+80), np.random.randint(self.center_y-80,self.center_y+80)),1,(255,255,200),-1)
        return frame

    def draw_mode_203_horizon_monoliths(self, frame, magnitudes):
        """Mode 203: Horizon Monoliths - distant monoliths rise with band; shadow sweeps on kicks"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        base_y = self.height-80
        count = min(20, len(magnitudes))
        gap = self.width//(count+1)
        for i in range(count):
            h = int(magnitudes[i]*220)
            x = gap*(i+1)
            cv2.rectangle(frame,(x, base_y-h),(x+10, base_y),(80,80,120),-1)
        if bass>0.7:
            cv2.rectangle(frame,(0,base_y-10),(self.width,base_y),(30,30,30),-1)
        return frame

    def draw_mode_204_gravity_slingshot_trails(self, frame, magnitudes):
        """Mode 204: Gravity Slingshot Trails - probes slingshot around planet; trail length by highs"""
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        for i in range(10):
            ang = self.frame_counter*0.02 + i*0.6
            r = 120 + i*6
            x = int(self.center_x + np.cos(ang)*r)
            y = int(self.center_y + np.sin(ang)*r)
            for t in range(int(10 + highs*30)):
                px = int(self.center_x + np.cos(ang - t*0.02)*r)
                py = int(self.center_y + np.sin(ang - t*0.02)*r)
                cv2.circle(frame,(px,py),1,(140,140,255),-1)
            cv2.circle(frame,(x,y),2,(255,255,255),-1)
        return frame

    def draw_mode_205_solar_flare_notches(self, frame, magnitudes):
        """Mode 205: Solar Flare Notches - solar disc with notch flares per bin"""
        cv2.circle(frame,(self.center_x,self.center_y),120,(200,180,140),-1)
        bins = len(magnitudes)
        for i in range(0,bins, max(1,bins//60)):
            ang = (i/bins)*2*np.pi
            flare = int(magnitudes[i]*100)
            x1 = int(self.center_x + np.cos(ang)*120)
            y1 = int(self.center_y + np.sin(ang)*120)
            x2 = int(self.center_x + np.cos(ang)*(120+flare))
            y2 = int(self.center_y + np.sin(ang)*(120+flare))
            cv2.line(frame,(x1,y1),(x2,y2),(255,220,180),2, lineType=cv2.LINE_AA)
        return frame

    def draw_mode_206_tesseract_window(self, frame, magnitudes):
        """Mode 206: Tesseract Window - 4D cube projection; face alpha by band energy"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        size = int(80 + bass*80)
        for dz in (-1,1):
            for dy in (-1,1):
                for dx in (-1,1):
                    x = self.center_x + dx*size
                    y = self.center_y + dy*size
                    cv2.circle(frame,(x+dz*20,y+dz*10),2,(200,200,255),-1)
        for a in range(0,360,30):
            x1 = int(self.center_x + np.cos(np.radians(a))*size)
            y1 = int(self.center_y + np.sin(np.radians(a))*size)
            x2 = int(self.center_x + np.cos(np.radians(a+30))*size)
            y2 = int(self.center_y + np.sin(np.radians(a+30))*size)
            cv2.line(frame,(x1,y1),(x2,y2),(180,180,255),1)
        return frame

    def draw_mode_207_interstellar_postcards(self, frame, magnitudes):
        """Mode 207: Interstellar Postcards - tiles flip; each hosts tiny spectrum motif"""
        rows, cols = 3, 4
        tile_w = self.width//(cols+1)
        tile_h = self.height//(rows+1)
        for r in range(rows):
            for c in range(cols):
                x = (c+1)*tile_w - tile_w//2
                y = (r+1)*tile_h - tile_h//2
                cv2.rectangle(frame,(x-60,y-40),(x+60,y+40),(220,220,220),2)
                for k in range(8):
                    idx = (k*len(magnitudes)//8)
                    h = int(magnitudes[idx]*30)
                    cv2.line(frame,(x-50+k*12,y+20),(x-50+k*12,y+20-h),(150,200,255),2)
        return frame

    def draw_mode_208_cosmic_braille(self, frame, magnitudes):
        """Mode 208: Cosmic Braille - raised dots scroll; dot height by band"""
        for i in range(min(40,len(magnitudes))):
            x = int((i/40)*self.width)
            y = int(self.center_y + np.sin(self.frame_counter*0.05 + i)*40)
            size = max(1,int(1 + magnitudes[i]*6))
            cv2.circle(frame,(x,y),size,(200,200,255),-1)
        return frame

    def draw_mode_209_stellar_harpoon(self, frame, magnitudes):
        """Mode 209: Stellar Harpoon - line tension by amplitude; vibrato with highs"""
        amp = float(np.mean(magnitudes))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        length = int(80 + amp*260)
        wiggle = int(highs*20)
        x2 = int(self.center_x + length)
        y2 = int(self.center_y + np.sin(self.frame_counter*0.2)*wiggle)
        cv2.line(frame,(self.center_x,self.center_y),(x2,y2),(220,220,255),2)
        return frame

    def draw_mode_210_galaxy_ticker_tape(self, frame, magnitudes):
        """Mode 210: Galaxy Ticker Tape - ticker snakes; character scale by band"""
        for i in range(min(30,len(magnitudes))):
            x = int((self.frame_counter*2 + i*20) % (self.width+60)) - 60
            y = int(self.center_y + np.sin(i*0.3 + self.frame_counter*0.05)*40)
            s = int(6 + magnitudes[i]*16)
            cv2.rectangle(frame,(x,y),(x+s,y+s),(200,200,255),-1)
        return frame

    def draw_mode_211_antimatter_chess(self, frame, magnitudes):
        """Mode 211: Antimatter Chess - pieces phase in/out; height maps to band"""
        size = 40
        for r in range(8):
            for c in range(8):
                x = c*size+160
                y = r*size+160
                color = (40,40,60) if (r+c)%2==0 else (20,20,30)
                cv2.rectangle(frame,(x,y),(x+size,y+size),color,-1)
        for i in range(16):
            idx = i*(len(magnitudes)//16)
            h = int(magnitudes[idx]*30)
            x = 160 + (i%8)*size + 10
            y = 160 + (i//8)*size + 10
            cv2.rectangle(frame,(x,y-h),(x+20,y),(200,200,255),-1)
        return frame

    def draw_mode_212_star_nursery_conveyor(self, frame, magnitudes):
        """Mode 212: Star Nursery Conveyor - progression speed from energy"""
        energy = float(np.mean(magnitudes))
        for i in range(6):
            x = int((self.frame_counter*(2+energy*8) + i*140) % (self.width+160)) - 80
            for s in range(3):
                r = 8 + s*6
                cv2.circle(frame,(x, 220+s*40), r, (180,180,255), 2)
        return frame

    def draw_mode_213_magnetar_lines(self, frame, magnitudes):
        """Mode 213: Magnetar Lines - field lines whip; gamma flashes on transients"""
        for i in range(30):
            ang = i/30*2*np.pi
            k = np.sin(self.frame_counter*0.05 + i)*40
            x1 = int(self.center_x + np.cos(ang)*80)
            y1 = int(self.center_y + np.sin(ang)*80)
            x2 = int(self.center_x + np.cos(ang)*(180+k))
            y2 = int(self.center_y + np.sin(ang)*(180+k))
            cv2.line(frame,(x1,y1),(x2,y2),(160,200,255),1)
        if np.max(np.abs(np.diff(magnitudes)))>0.4:
            cv2.rectangle(frame,(0,0),(self.width,self.height),(255,255,255),1)
        return frame

    def draw_mode_214_zero_kelvin_diamonds(self, frame, magnitudes):
        """Mode 214: Zero-Kelvin Diamonds - refracted beams thickness tracks bands; spin with tempo"""
        angle = self.frame_counter*0.02
        for i in range(6):
            t = i/6
            r = int(40 + t*160)
            x = int(self.center_x + np.cos(angle+t*2*np.pi)*r)
            y = int(self.center_y + np.sin(angle+t*2*np.pi)*r)
            cv2.polylines(frame,[np.array([(x,y-10),(x+10,y),(x,y+10),(x-10,y)],np.int32)],True,(200,220,255),2)
        return frame

    def draw_mode_215_orbital_time_garden(self, frame, magnitudes):
        """Mode 215: Orbital Time Garden - planets are clock markers; orbits expand with bass"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        for h in range(12):
            ang = h/12*2*np.pi - np.pi/2
            r = int(120 + bass*60)
            x = int(self.center_x + np.cos(ang)*r)
            y = int(self.center_y + np.sin(ang)*r)
            cv2.circle(frame,(x,y),6,(200,200,255),-1)
        return frame

    def draw_mode_216_subspace_ribbon_printer(self, frame, magnitudes):
        """Mode 216: Subspace Ribbon Printer - ribbon thickness equals summed band energy at slice"""
        total = float(np.sum(magnitudes))
        y = int(120 + (self.frame_counter % (self.height-240)))
        thickness = int(4 + total*8)
        cv2.line(frame,(60,y),(self.width-60,y),(200,200,255),thickness)
        return frame

    def draw_mode_217_dark_matter_drizzle(self, frame, magnitudes):
        """Mode 217: Dark-Matter Drizzle - invisible drizzle reveals when bands exceed threshold"""
        thr = 0.5
        for i in range(len(magnitudes)):
            if magnitudes[i] > thr and np.random.random()<0.2:
                x = np.random.randint(0,self.width)
                y = np.random.randint(0,self.height)
                cv2.circle(frame,(x,y),1,(200,200,255),-1)
        if np.max(magnitudes)>0.9:
            cv2.circle(frame,(self.center_x,self.center_y),100,(100,100,100),1)
        return frame

    def draw_mode_218_meteor_choir_cones(self, frame, magnitudes):
        """Mode 218: Meteor Choir Cones - cone aperture by band; inner rings harmonics"""
        count = 8
        for i in range(count):
            idx = i*(len(magnitudes)//count)
            mag = magnitudes[idx]
            ang = (i/count)*2*np.pi
            x = int(self.center_x + np.cos(ang)*80)
            y = int(self.center_y + np.sin(ang)*80)
            rad = int(20 + mag*40)
            cv2.circle(frame,(x,y),rad,(200,200,255),1)
            cv2.circle(frame,(x,y),rad//2,(160,160,255),1)
        return frame

    def draw_mode_219_folded_galaxy_map(self, frame, magnitudes):
        """Mode 219: Folded Galaxy Map - folds reveal bar clusters; refolds during breakdown"""
        phase = (np.sin(self.frame_counter*0.03)+1)/2
        cols = 12
        for i in range(cols):
            x = int(80 + i*(self.width-160)/cols)
            h = int(magnitudes[min(i,len(magnitudes)-1)]*200*phase)
            cv2.rectangle(frame,(x,self.center_y-h),(x+6,self.center_y+h),(200,200,255),-1)
        return frame

    def draw_mode_220_ion_thruster_plume(self, frame, magnitudes):
        """Mode 220: Ion Thruster Plume - plume length maps to amplitude; shock diamonds on peaks"""
        amp = float(np.mean(magnitudes))
        length = int(60 + amp*260)
        base = (120, self.center_y)
        cv2.rectangle(frame,(base[0]-10,base[1]-10),(base[0],base[1]+10),(180,180,200),-1)
        for i in range(10):
            y = base[1] - 20 + i*4
            cv2.line(frame,(base[0],y),(base[0]+length,y),(200,220,255),1)
        if np.max(magnitudes)>0.85:
            for i in range(5):
                x = base[0] + int(length*(i+1)/6)
                cv2.circle(frame,(x,base[1]),3,(255,255,255),-1)
        return frame

    def draw_mode_221_cosmic_dominoes(self, frame, magnitudes):
        """Mode 221: Cosmic Dominoes - curved domino line; fall rate by energy; tiles display local bars"""
        energy = float(np.mean(magnitudes))
        n = 20
        for i in range(n):
            t = i/n
            ang = t*np.pi
            x = int(120 + t*(self.width-240))
            y = int(self.center_y + np.sin(ang)*60)
            tilt = int(np.sin(self.frame_counter*0.02 + t*6)*energy*30)
            pts = np.array([(x-10,y-20),(x+10,y-20+tilt),(x+10,y+20+tilt),(x-10,y+20)],np.int32)
            cv2.polylines(frame,[pts],True,(200,200,255),2)
        return frame

    def draw_mode_222_spacesuit_hud(self, frame, magnitudes):
        """Mode 222: Spacesuit HUD - HUD overlays with spectrum wedges; warning flashes on peaks"""
        wedges = 24
        for i in range(wedges):
            t = i/wedges
            idx = min(int(t*len(magnitudes)), len(magnitudes)-1)
            h = int(magnitudes[idx]*80)
            ang1 = int(t*360)
            ang2 = ang1 + 6
            cv2.ellipse(frame,(self.center_x,self.center_y),(200,200),-90,ang1,ang2,(150,200,255),2)
            cv2.ellipse(frame,(self.center_x,self.center_y),(200+h,200+h),-90,ang1,ang2,(200,220,255),2)
        if np.max(magnitudes)>0.9:
            cv2.circle(frame,(self.center_x,self.center_y),10,(0,0,255),-1)
        return frame

    def draw_mode_223_pulsar_barcode_beam(self, frame, magnitudes):
        """Mode 223: Pulsar Barcode Beam - rotating beam; bar lengths by band; bloom on peaks"""
        angle = (self.frame_counter*2) % 360
        bars = 48
        for i in range(bars):
            t = i/bars
            idx = min(int(t*len(magnitudes)), len(magnitudes)-1)
            r = int(60 + magnitudes[idx]*200)
            ang = np.radians(angle) + t*2*np.pi
            x = int(self.center_x + np.cos(ang)*r)
            y = int(self.center_y + np.sin(ang)*r)
            cv2.circle(frame,(x,y),1,(200,200,255),-1)
        if np.max(magnitudes)>0.85:
            cv2.circle(frame,(self.center_x,self.center_y),40,(255,255,255),1)
        return frame

    def draw_mode_224_astro_terrarium(self, frame, magnitudes):
        """Mode 224: Astro Terrarium - micro planet ecosystem; eruptions on kicks; biolume with highs"""
        bass = float(np.mean(magnitudes[:len(magnitudes)//4]))
        highs = float(np.mean(magnitudes[3*len(magnitudes)//4:]))
        cv2.circle(frame,(self.center_x,self.center_y+60),90,(80,120,80),-1)
        if bass>0.7:
            for _ in range(30):
                x = self.center_x + np.random.randint(-60,60)
                y = self.center_y + 60 - np.random.randint(0,60)
                cv2.circle(frame,(x,y),2,(160,80,60),-1)
        for _ in range(int(highs*40)):
            cv2.circle(frame,(np.random.randint(self.center_x-80,self.center_x+80), np.random.randint(self.center_y-20,self.center_y+120)),1,(120,220,200),-1)
        return frame

    def draw_mode_225_micrometeor_spark_curtain(self, frame, magnitudes):
        """Mode 225: Micrometeor Spark Curtain - diagonal sparks; density with amplitude"""
        amp = float(np.mean(magnitudes))
        density = int(40 + amp*200)
        for _ in range(density):
            x = np.random.randint(0,self.width)
            y = np.random.randint(0,self.height)
            dx = 6; dy = 12
            cv2.line(frame,(x,y),(x+dx,y+dy),(200,200,255),1)
        return frame

    def draw_mode_2_neon_rain(self, frame, magnitudes):
        """Mode 2: Neon droplets cascading down (cyberpunk lofi)"""
        # Spawn new rain particles based on magnitudes
        for i, magnitude in enumerate(magnitudes):
            if magnitude > 0.3 and np.random.random() < magnitude * 0.3:
                x = int((i / len(magnitudes)) * self.width)
                y = 0
                speed = 3 + magnitude * 15
                size = 2 + int(magnitude * 8)

                # Neon colors (cyan, magenta, pink)
                color_choice = i % 3
                if color_choice == 0:
                    color = (255, 255, 0)  # Cyan
                elif color_choice == 1:
                    color = (255, 0, 255)  # Magenta
                else:
                    color = (255, 100, 200)  # Pink

                self.rain_particles.append({
                    'x': x, 'y': y, 'speed': speed,
                    'size': size, 'color': color,
                    'trail_length': int(magnitude * 50)
                })

        # Update and draw rain particles
        new_particles = []
        for particle in self.rain_particles:
            particle['y'] += particle['speed']

            # Keep if still on screen
            if particle['y'] < self.height + 20:
                # Draw particle with trail
                trail_length = particle['trail_length']
                for t in range(trail_length):
                    trail_y = int(particle['y'] - t * 2)
                    if trail_y >= 0:
                        alpha = 1.0 - (t / trail_length)
                        trail_color = tuple(int(c * alpha) for c in particle['color'])
                        cv2.circle(frame, (particle['x'], trail_y),
                                 max(1, particle['size'] - t // 3),
                                 trail_color, -1, lineType=cv2.LINE_AA)

                # Glow effect
                cv2.circle(frame, (particle['x'], int(particle['y'])),
                          particle['size'] + 3,
                          tuple(int(c * 0.3) for c in particle['color']),
                          1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.rain_particles = new_particles

        return frame

    def draw_mode_3_jazzy_fireworks(self, frame, magnitudes):
        """Mode 3: Bursting particles from center (jazz energy) - ENHANCED VERSION"""
        avg_magnitude = np.mean(magnitudes)

        # MUCH MORE AGGRESSIVE spawning - spawn constantly and much more particles
        # Spawn from center constantly
        if avg_magnitude > 0.3:  # Lower threshold so fireworks happen more often
            # Base particles - always spawn a lot
            num_particles = int(150 + avg_magnitude * 250)  # Way more particles (150-400)

            for i in range(num_particles):
                angle = np.random.random() * 2 * np.pi
                # Higher speeds to fill entire screen
                speed = 5 + np.random.random() * 15 * (avg_magnitude + 0.5)

                # Rainbow colors for jazz energy
                hue = np.random.randint(0, 180)
                color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                self.firework_particles.append({
                    'x': self.center_x,
                    'y': self.center_y,
                    'vx': np.cos(angle) * speed,
                    'vy': np.sin(angle) * speed,
                    'color': color,
                    'life': 1.0,  # Longer life
                    'size': 4 + int(avg_magnitude * 8)  # Bigger particles
                })

        # Also spawn random secondary bursts from different positions
        if avg_magnitude > 0.5 and self.frame_counter % 5 == 0:
            # Create secondary burst points
            for burst in range(3):
                burst_angle = (burst / 3) * 2 * np.pi + self.frame_counter * 0.1
                burst_distance = self.max_radius * 0.4
                burst_x = self.center_x + int(np.cos(burst_angle) * burst_distance)
                burst_y = self.center_y + int(np.sin(burst_angle) * burst_distance)

                for i in range(50):
                    angle = np.random.random() * 2 * np.pi
                    speed = 3 + np.random.random() * 10

                    hue = np.random.randint(0, 180)
                    color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
                    color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                    color = tuple(int(c) for c in color_bgr)

                    self.firework_particles.append({
                        'x': burst_x,
                        'y': burst_y,
                        'vx': np.cos(angle) * speed,
                        'vy': np.sin(angle) * speed,
                        'color': color,
                        'life': 0.8,
                        'size': 3 + int(avg_magnitude * 6)
                    })

        # Update and draw particles
        new_particles = []
        for particle in self.firework_particles:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.008  # Slower decay so particles live longer and fill screen

            # Very slight gravity
            particle['vy'] += 0.05

            if particle['life'] > 0:
                alpha = particle['life']
                particle_color = tuple(int(c * alpha) for c in particle['color'])
                size = max(1, int(particle['size'] * alpha))

                # Main particle - bigger and brighter
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          size, particle_color, -1, lineType=cv2.LINE_AA)

                # Multi-layer glow for more visibility
                if alpha > 0.3:
                    # Outer glow
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                              size + 4, tuple(int(c * 0.3 * alpha) for c in particle_color),
                              1, lineType=cv2.LINE_AA)
                    # Inner bright glow
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                              size + 2, tuple(int(c * 0.6 * alpha) for c in particle_color),
                              -1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.firework_particles = new_particles

        return frame

    def draw_mode_4_retro_cassette(self, frame, magnitudes):
        """Mode 4: VU meters and cassette tape animation - REALISTIC VERSION"""
        # Update cassette reel rotation
        avg_magnitude = np.mean(magnitudes)
        self.cassette_reel_angle += 3 + avg_magnitude * 10

        # REALISTIC CASSETTE DIMENSIONS (wider, more authentic)
        cassette_width = int(self.width * 0.65)
        cassette_height = int(self.height * 0.35)
        cassette_x = self.center_x - cassette_width // 2
        cassette_y = self.center_y - cassette_height // 2

        # === CASSETTE BODY ===
        # Main outer shell (beige/tan plastic)
        cv2.rectangle(frame, (cassette_x, cassette_y),
                     (cassette_x + cassette_width, cassette_y + cassette_height),
                     (140, 130, 110), -1, lineType=cv2.LINE_AA)

        # Border/edge
        cv2.rectangle(frame, (cassette_x, cassette_y),
                     (cassette_x + cassette_width, cassette_y + cassette_height),
                     (100, 90, 70), 3, lineType=cv2.LINE_AA)

        # === LABEL AREA (top section) ===
        label_height = int(cassette_height * 0.25)
        cv2.rectangle(frame, (cassette_x + 20, cassette_y + 15),
                     (cassette_x + cassette_width - 20, cassette_y + label_height),
                     (220, 210, 200), -1, lineType=cv2.LINE_AA)
        cv2.rectangle(frame, (cassette_x + 20, cassette_y + 15),
                     (cassette_x + cassette_width - 20, cassette_y + label_height),
                     (180, 170, 160), 1, lineType=cv2.LINE_AA)

        # === WINDOW AREA (where you see the tape) ===
        window_y = cassette_y + label_height + 25
        window_height = int(cassette_height * 0.45)
        window_margin = 40

        # Dark transparent window
        cv2.rectangle(frame, (cassette_x + window_margin, window_y),
                     (cassette_x + cassette_width - window_margin, window_y + window_height),
                     (30, 25, 20), -1, lineType=cv2.LINE_AA)
        cv2.rectangle(frame, (cassette_x + window_margin, window_y),
                     (cassette_x + cassette_width - window_margin, window_y + window_height),
                     (80, 70, 60), 2, lineType=cv2.LINE_AA)

        # === TAPE REELS (much more detailed) ===
        reel_y = window_y + window_height // 2
        reel_outer_radius = 55
        reel_inner_radius = 15
        left_reel_x = cassette_x + cassette_width // 3
        right_reel_x = cassette_x + 2 * cassette_width // 3

        for reel_x in [left_reel_x, right_reel_x]:
            # Outer reel edge (dark)
            cv2.circle(frame, (reel_x, reel_y), reel_outer_radius,
                      (50, 45, 40), 2, lineType=cv2.LINE_AA)

            # Tape on reel (brown/black magnetic tape)
            tape_radius = int(reel_outer_radius * 0.85)
            cv2.circle(frame, (reel_x, reel_y), tape_radius,
                      (20, 15, 10), -1, lineType=cv2.LINE_AA)

            # Center hub (beige plastic)
            cv2.circle(frame, (reel_x, reel_y), reel_inner_radius,
                      (140, 130, 110), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (reel_x, reel_y), reel_inner_radius,
                      (100, 90, 70), 1, lineType=cv2.LINE_AA)

            # Rotating spokes (6 spokes for realism)
            for spoke in range(6):
                angle = np.deg2rad(self.cassette_reel_angle + spoke * 60)
                x1 = int(reel_x + reel_inner_radius * np.cos(angle))
                y1 = int(reel_y + reel_inner_radius * np.sin(angle))
                x2 = int(reel_x + tape_radius * 0.9 * np.cos(angle))
                y2 = int(reel_y + tape_radius * 0.9 * np.sin(angle))
                cv2.line(frame, (x1, y1), (x2, y2), (80, 70, 60), 2, lineType=cv2.LINE_AA)

            # Center dot
            cv2.circle(frame, (reel_x, reel_y), 4, (60, 50, 40), -1, lineType=cv2.LINE_AA)

        # === TAPE BETWEEN REELS (visible magnetic tape) ===
        tape_top_y = reel_y - reel_outer_radius + 5
        tape_bottom_y = reel_y + reel_outer_radius - 5
        tape_thickness = 8

        # Top tape section
        cv2.rectangle(frame, (left_reel_x + reel_outer_radius - 5, tape_top_y - tape_thickness),
                     (right_reel_x - reel_outer_radius + 5, tape_top_y),
                     (15, 10, 8), -1, lineType=cv2.LINE_AA)

        # Bottom tape section
        cv2.rectangle(frame, (left_reel_x + reel_outer_radius - 5, tape_bottom_y),
                     (right_reel_x - reel_outer_radius + 5, tape_bottom_y + tape_thickness),
                     (15, 10, 8), -1, lineType=cv2.LINE_AA)

        # === CASSETTE SCREWS (4 corners) ===
        screw_positions = [
            (cassette_x + 25, cassette_y + 25),
            (cassette_x + cassette_width - 25, cassette_y + 25),
            (cassette_x + 25, cassette_y + cassette_height - 25),
            (cassette_x + cassette_width - 25, cassette_y + cassette_height - 25)
        ]

        for screw_x, screw_y in screw_positions:
            cv2.circle(frame, (screw_x, screw_y), 6, (80, 70, 60), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (screw_x, screw_y), 6, (60, 50, 40), 1, lineType=cv2.LINE_AA)
            # Screw cross
            cv2.line(frame, (screw_x - 3, screw_y), (screw_x + 3, screw_y),
                    (40, 30, 25), 1, lineType=cv2.LINE_AA)
            cv2.line(frame, (screw_x, screw_y - 3), (screw_x, screw_y + 3),
                    (40, 30, 25), 1, lineType=cv2.LINE_AA)

        # === BOTTOM GRIP NOTCHES (authentic detail) ===
        notch_width = 30
        notch_height = 8
        notch_spacing = 15
        notch_y = cassette_y + cassette_height - notch_height - 5

        for i in range(5):
            notch_x = cassette_x + cassette_width // 2 - 2 * notch_width - 2 * notch_spacing + i * (notch_width + notch_spacing)
            cv2.rectangle(frame, (notch_x, notch_y),
                         (notch_x + notch_width, notch_y + notch_height),
                         (90, 80, 60), -1, lineType=cv2.LINE_AA)

        # === VINTAGE VU METERS (below cassette) ===
        vu_y = cassette_y + cassette_height + 100
        vu_width = cassette_width - 200
        vu_height = 35
        vu_x = self.center_x - vu_width // 2

        # Left and right channel VU meters
        num_segments = 40
        segment_width = vu_width // num_segments

        for channel in range(2):
            channel_y = vu_y + channel * 60

            # VU meter background/frame
            frame_padding = 5
            cv2.rectangle(frame,
                         (vu_x - frame_padding, channel_y - frame_padding),
                         (vu_x + vu_width + frame_padding, channel_y + vu_height + frame_padding),
                         (100, 90, 70), -1, lineType=cv2.LINE_AA)
            cv2.rectangle(frame,
                         (vu_x - frame_padding, channel_y - frame_padding),
                         (vu_x + vu_width + frame_padding, channel_y + vu_height + frame_padding),
                         (70, 60, 50), 2, lineType=cv2.LINE_AA)

            # Get magnitude for this channel (split frequencies)
            if channel == 0:
                channel_mag = np.mean(magnitudes[:len(magnitudes)//2])
            else:
                channel_mag = np.mean(magnitudes[len(magnitudes)//2:])

            active_segments = int(channel_mag * num_segments)

            for seg in range(num_segments):
                seg_x = vu_x + seg * segment_width

                # VINTAGE COLOR GRADIENT: green -> amber -> orange -> red
                segment_progress = seg / num_segments
                if segment_progress < 0.5:
                    color = (0, 200, 50)  # Green
                elif segment_progress < 0.7:
                    color = (0, 180, 200)  # Amber/yellow
                elif segment_progress < 0.85:
                    color = (0, 120, 255)  # Orange
                else:
                    color = (0, 60, 255)  # Red

                if seg < active_segments:
                    # Active segment - full brightness with glow
                    cv2.rectangle(frame, (seg_x + 1, channel_y),
                                (seg_x + segment_width - 2, channel_y + vu_height),
                                color, -1, lineType=cv2.LINE_AA)
                else:
                    # Inactive segment - very dim
                    dim_color = tuple(int(c * 0.15) for c in color)
                    cv2.rectangle(frame, (seg_x + 2, channel_y + 2),
                                (seg_x + segment_width - 2, channel_y + vu_height - 2),
                                dim_color, -1, lineType=cv2.LINE_AA)

            # Channel label (L/R)
            label = "L" if channel == 0 else "R"
            cv2.putText(frame, label, (vu_x - 35, channel_y + vu_height - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (150, 140, 120), 2, cv2.LINE_AA)

        return frame

    def draw_mode_5_soul_aura(self, frame, magnitudes):
        """Mode 5: Pulsing organic blob (soul/RnB vibe)"""
        # Create smooth organic shape with many points
        num_points = 60
        angle_step = 360 / num_points

        points = []
        for i in range(num_points):
            angle = np.deg2rad(i * angle_step)

            # Get magnitude for this angle section
            mag_idx = int((i / num_points) * len(magnitudes))
            magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

            # Base radius with organic variation
            base_variation = np.sin(i * 0.3 + self.frame_counter * 0.05) * 30
            magnitude_variation = magnitude * 150
            radius = self.max_radius * 0.5 + base_variation + magnitude_variation

            x = int(self.center_x + radius * np.cos(angle))
            y = int(self.center_y + radius * np.sin(angle))
            points.append([x, y])

        points = np.array(points, dtype=np.int32)

        # Draw multiple layers for depth and glow
        avg_magnitude = np.mean(magnitudes)

        # Outer glow layers (purple to pink gradient)
        for layer in range(5, 0, -1):
            layer_points = []
            expansion = layer * 15

            for point in points:
                # Expand from center
                dx = point[0] - self.center_x
                dy = point[1] - self.center_y
                scale = 1.0 + (expansion / np.sqrt(dx**2 + dy**2 + 1))

                x = int(self.center_x + dx * scale)
                y = int(self.center_y + dy * scale)
                layer_points.append([x, y])

            layer_points = np.array(layer_points, dtype=np.int32)

            # Color: deep purple to pink
            hue = 140 + layer * 5 + int(avg_magnitude * 20)  # Purple-pink range
            saturation = 200 + int(avg_magnitude * 55)
            value = 100 + int(avg_magnitude * 100) - layer * 15
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            alpha = 0.3 / layer
            color = tuple(int(c * alpha) for c in color)

            cv2.fillPoly(frame, [layer_points], color, lineType=cv2.LINE_AA)

        # Main aura body
        hue = 150 + int(avg_magnitude * 30)
        saturation = 220 + int(avg_magnitude * 35)
        value = 180 + int(avg_magnitude * 75)
        color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
        color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
        main_color = tuple(int(c) for c in color_bgr)

        cv2.fillPoly(frame, [points], main_color, lineType=cv2.LINE_AA)

        # Bright outline
        cv2.polylines(frame, [points], True, (255, 200, 255), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_6_frequency_flowers(self, frame, magnitudes):
        """Mode 6: Blooming flower petals (dreamy lofi)"""
        # Create flower petals around the circle
        num_petals = min(24, len(magnitudes))
        angle_step = 360 / num_petals

        for petal_idx in range(num_petals):
            angle = np.deg2rad(petal_idx * angle_step + self.frame_counter * 0.5)

            # Get magnitude for this petal
            mag_idx = int((petal_idx / num_petals) * len(magnitudes))
            magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

            # Petal size based on magnitude
            petal_length = 50 + magnitude * 150
            petal_width = 20 + magnitude * 40

            # Petal center position
            base_radius = self.max_radius * 0.4
            petal_base_x = int(self.center_x + base_radius * np.cos(angle))
            petal_base_y = int(self.center_y + base_radius * np.sin(angle))

            # Create petal shape (ellipse)
            # Petal tip position
            petal_tip_x = int(petal_base_x + petal_length * np.cos(angle))
            petal_tip_y = int(petal_base_y + petal_length * np.sin(angle))

            # Draw petal as filled ellipse
            # Color: pastel gradient (pink, lavender, yellow)
            hue = (petal_idx * 15 + self.frame_counter) % 180
            saturation = 100 + int(magnitude * 100)
            value = 200 + int(magnitude * 55)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            petal_color = tuple(int(c) for c in color_bgr)

            # Draw petal as rotated ellipse
            axes = (int(petal_width / 2), int(petal_length / 2))
            angle_deg = int(np.rad2deg(angle))

            petal_center_x = int((petal_base_x + petal_tip_x) / 2)
            petal_center_y = int((petal_base_y + petal_tip_y) / 2)

            cv2.ellipse(frame, (petal_center_x, petal_center_y), axes,
                       angle_deg, 0, 360, petal_color, -1, lineType=cv2.LINE_AA)

            # Petal outline
            cv2.ellipse(frame, (petal_center_x, petal_center_y), axes,
                       angle_deg, 0, 360, (255, 255, 255), 1, lineType=cv2.LINE_AA)

        # Draw flower center
        avg_magnitude = np.mean(magnitudes)
        center_radius = int(30 + avg_magnitude * 50)
        cv2.circle(frame, (self.center_x, self.center_y), center_radius,
                  (50, 200, 255), -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, (self.center_x, self.center_y), center_radius,
                  (100, 220, 255), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_7_electric_heartbeat(self, frame, magnitudes):
        """Mode 7: EKG-style waveform with glow (emotional jazz)"""
        # Draw waveform across the screen like an EKG monitor
        points = []

        y_baseline = self.center_y
        waveform_width = self.width - 100
        x_start = 50

        for i, magnitude in enumerate(magnitudes):
            x = int(x_start + (i / len(magnitudes)) * waveform_width)

            # Create heartbeat-like spikes
            # Dramatic peaks for strong frequencies
            if magnitude > 0.7:
                y_offset = -int(magnitude * 300)
            else:
                y_offset = -int(magnitude * 150)

            y = int(y_baseline + y_offset)
            points.append([x, y])

        # Add smooth interpolation for organic feel
        if len(points) > 1:
            points = np.array(points, dtype=np.int32)

            # Draw glow layers
            for glow in range(5, 0, -1):
                glow_color = (0, int(255 / glow), int(255 / glow))  # Cyan glow
                thickness = glow * 3
                alpha = 0.3
                glow_color = tuple(int(c * alpha) for c in glow_color)
                cv2.polylines(frame, [points], False, glow_color,
                            thickness, lineType=cv2.LINE_AA)

            # Main line (bright cyan/electric blue)
            cv2.polylines(frame, [points], False, (255, 255, 0),
                         3, lineType=cv2.LINE_AA)

            # Add small circles at peaks
            for i, point in enumerate(points):
                if i > 0 and i < len(points) - 1:
                    if point[1] < points[i-1][1] and point[1] < points[i+1][1]:
                        # This is a peak
                        cv2.circle(frame, tuple(point), 5, (255, 255, 255), -1,
                                 lineType=cv2.LINE_AA)
                        cv2.circle(frame, tuple(point), 8, (150, 255, 255), 1,
                                 lineType=cv2.LINE_AA)

        # Draw baseline
        cv2.line(frame, (x_start, y_baseline),
                (x_start + waveform_width, y_baseline),
                (100, 100, 100), 1, lineType=cv2.LINE_AA)

        # Grid lines (like EKG paper)
        for grid_x in range(x_start, x_start + waveform_width, 50):
            cv2.line(frame, (grid_x, y_baseline - 200),
                    (grid_x, y_baseline + 100),
                    (40, 40, 40), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_8_pixel_clouds(self, frame, magnitudes):
        """Mode 8: 8-bit style floating cloud particles (retro lofi)"""
        # Spawn pixel clouds based on magnitudes
        if self.frame_counter % 5 == 0:
            for i in range(0, len(magnitudes), 3):
                magnitude = magnitudes[i]
                if magnitude > 0.3:
                    # Random spawn position
                    x = np.random.randint(0, self.width)
                    y = np.random.randint(self.height // 3, 2 * self.height // 3)

                    # Pixel block size
                    pixel_size = 8 if magnitude < 0.6 else 12

                    # Pastel 8-bit colors
                    colors = [
                        (255, 200, 200),  # Pastel pink
                        (200, 255, 200),  # Pastel green
                        (200, 200, 255),  # Pastel blue
                        (255, 255, 200),  # Pastel yellow
                        (255, 200, 255),  # Pastel magenta
                    ]
                    color = colors[i % len(colors)]

                    self.pixel_clouds.append({
                        'x': x, 'y': y,
                        'vx': np.random.uniform(-1, 1),
                        'vy': np.random.uniform(-0.5, -2),  # Float upward
                        'size': pixel_size,
                        'color': color,
                        'life': 1.0
                    })

        # Update and draw pixel clouds
        new_clouds = []
        for cloud in self.pixel_clouds:
            cloud['x'] += cloud['vx']
            cloud['y'] += cloud['vy']
            cloud['life'] -= 0.01

            if cloud['life'] > 0 and 0 <= cloud['x'] < self.width:
                alpha = cloud['life']
                cloud_color = tuple(int(c * alpha) for c in cloud['color'])

                # Draw as pixelated square (no anti-aliasing for retro look)
                x = int(cloud['x'])
                y = int(cloud['y'])
                size = cloud['size']

                cv2.rectangle(frame, (x, y), (x + size, y + size),
                            cloud_color, -1)

                # Pixel outline
                cv2.rectangle(frame, (x, y), (x + size, y + size),
                            (255, 255, 255), 1)

                new_clouds.append(cloud)

        self.pixel_clouds = new_clouds

        return frame

    def draw_mode_9_liquid_mercury(self, frame, magnitudes):
        """Mode 9: Flowing metallic waves (smooth jazz/soul)"""
        # Create flowing wave with metallic sheen
        num_wave_points = 100

        wave_points_top = []
        wave_points_bottom = []

        for i in range(num_wave_points):
            x = int((i / num_wave_points) * self.width)

            # Get magnitude for this position
            mag_idx = int((i / num_wave_points) * len(magnitudes))
            magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

            # Multiple sine waves for organic flow
            wave1 = np.sin(i * 0.1 + self.frame_counter * 0.1) * 40
            wave2 = np.sin(i * 0.05 + self.frame_counter * 0.05) * 60
            wave_offset = wave1 + wave2 + magnitude * 100

            y_top = int(self.center_y + wave_offset)
            y_bottom = int(self.center_y + wave_offset + 80 + magnitude * 100)

            wave_points_top.append([x, y_top])
            wave_points_bottom.append([x, y_bottom])

        # Combine top and reversed bottom for filled shape
        wave_points_top = np.array(wave_points_top, dtype=np.int32)
        wave_points_bottom = np.array(wave_points_bottom, dtype=np.int32)
        all_points = np.concatenate([wave_points_top, wave_points_bottom[::-1]])

        # Draw metallic gradient (silver with highlights)
        # Base layer (dark silver)
        cv2.fillPoly(frame, [all_points], (120, 120, 120), lineType=cv2.LINE_AA)

        # Highlight layer (create metallic sheen)
        for i in range(len(wave_points_top) - 1):
            # Gradient based on position
            t = i / len(wave_points_top)
            shine = int(abs(np.sin(t * np.pi * 3 + self.frame_counter * 0.1)) * 100)

            line_color = (160 + shine, 160 + shine, 160 + shine)

            cv2.line(frame, tuple(wave_points_top[i]), tuple(wave_points_top[i + 1]),
                    line_color, 3, lineType=cv2.LINE_AA)

        # Reflective highlights (white streaks)
        avg_magnitude = np.mean(magnitudes)
        if avg_magnitude > 0.5:
            for streak in range(5):
                streak_x = int((streak / 5) * self.width)
                streak_idx = int((streak / 5) * len(wave_points_top))
                if streak_idx < len(wave_points_top):
                    streak_y = wave_points_top[streak_idx][1]
                    cv2.circle(frame, (streak_x, streak_y),
                              int(8 + avg_magnitude * 15),
                              (220, 220, 220), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_10_cosmic_dust(self, frame, magnitudes):
        """Mode 10: Swirling galaxy particles with trails (ambient lofi)"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn cosmic particles
        if self.frame_counter % 2 == 0:
            for i in range(int(avg_magnitude * 20 + 10)):
                # Random angle for spiral
                angle = np.random.random() * 2 * np.pi
                distance = np.random.random() * self.max_radius * 0.3

                x = self.center_x + distance * np.cos(angle)
                y = self.center_y + distance * np.sin(angle)

                # Orbital velocity (perpendicular to radius)
                orbital_speed = 0.5 + np.random.random() * 2
                vx = -np.sin(angle) * orbital_speed
                vy = np.cos(angle) * orbital_speed

                # Colors: deep space (blues, purples, whites)
                color_choice = np.random.random()
                if color_choice < 0.3:
                    color = (255, 200, 100)  # White-gold
                elif color_choice < 0.6:
                    color = (255, 100, 100)  # Blue
                else:
                    color = (200, 100, 200)  # Purple

                self.cosmic_particles.append({
                    'x': x, 'y': y,
                    'vx': vx, 'vy': vy,
                    'color': color,
                    'life': 1.0,
                    'size': 1 + int(np.random.random() * 3),
                    'trail': []
                })

        # Update and draw particles
        new_particles = []
        for particle in self.cosmic_particles:
            # Add current position to trail
            particle['trail'].append((int(particle['x']), int(particle['y'])))
            if len(particle['trail']) > 20:
                particle['trail'].pop(0)

            # Update position (spiral motion)
            dx = particle['x'] - self.center_x
            dy = particle['y'] - self.center_y
            distance = np.sqrt(dx**2 + dy**2)

            # Spiral outward slowly
            if distance > 0:
                angle = np.arctan2(dy, dx)
                angle += 0.02  # Rotation
                distance += 0.5  # Expand outward

                particle['x'] = self.center_x + distance * np.cos(angle)
                particle['y'] = self.center_y + distance * np.sin(angle)

            particle['life'] -= 0.005

            # Keep if alive and on screen
            if particle['life'] > 0 and distance < self.max_radius * 1.2:
                alpha = particle['life']

                # Draw trail
                for trail_idx, trail_pos in enumerate(particle['trail']):
                    trail_alpha = alpha * (trail_idx / len(particle['trail']))
                    trail_color = tuple(int(c * trail_alpha) for c in particle['color'])
                    trail_size = max(1, int(particle['size'] * trail_alpha))

                    cv2.circle(frame, trail_pos, trail_size, trail_color, -1,
                             lineType=cv2.LINE_AA)

                # Draw main particle with glow
                particle_color = tuple(int(c * alpha) for c in particle['color'])
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          particle['size'] + 1,
                          tuple(int(c * 0.4) for c in particle_color),
                          -1, lineType=cv2.LINE_AA)
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          particle['size'], particle_color, -1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.cosmic_particles = new_particles

        # Draw subtle center glow
        center_radius = int(20 + avg_magnitude * 40)
        for glow_layer in range(3, 0, -1):
            glow_color = (int(80 / glow_layer), int(60 / glow_layer), int(100 / glow_layer))
            cv2.circle(frame, (self.center_x, self.center_y),
                      center_radius + glow_layer * 10, glow_color, -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_11_quantum_strings(self, frame, magnitudes):
        """Mode 11: Vibrating quantum strings with interference patterns"""
        num_strings = 12

        for string_idx in range(num_strings):
            # Each string is a horizontal line that vibrates
            y_base = int((string_idx + 1) / (num_strings + 1) * self.height)

            points = []
            for x in range(0, self.width, 5):
                # Get magnitude for this position
                mag_idx = int((x / self.width) * len(magnitudes))
                magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

                # Multiple frequency components for interference
                wave1 = np.sin(x * 0.02 + self.frame_counter * 0.15 + string_idx) * magnitude * 80
                wave2 = np.sin(x * 0.05 + self.frame_counter * 0.1) * magnitude * 40
                wave3 = np.sin(x * 0.01 + self.frame_counter * 0.2 + string_idx * 0.5) * 20

                y = int(y_base + wave1 + wave2 + wave3)
                points.append([x, y])

            if len(points) > 1:
                points = np.array(points, dtype=np.int32)

                # Color shifts through rainbow based on string and magnitude
                avg_mag = magnitudes[string_idx * len(magnitudes) // num_strings] if string_idx < num_strings else 0.5
                hue = int((string_idx / num_strings) * 180)
                saturation = 200 + int(avg_mag * 55)
                value = 150 + int(avg_mag * 105)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                # Draw glowing string
                cv2.polylines(frame, [points], False,
                            tuple(int(c * 0.4) for c in color), 4, lineType=cv2.LINE_AA)
                cv2.polylines(frame, [points], False, color, 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_12_lava_lamp(self, frame, magnitudes):
        """Mode 12: Rising and morphing lava lamp blobs"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn new blobs
        if self.frame_counter % 20 == 0 or (avg_magnitude > 0.6 and self.frame_counter % 10 == 0):
            blob_x = np.random.randint(int(self.width * 0.2), int(self.width * 0.8))
            blob_y = self.height + 50
            blob_size = 40 + int(avg_magnitude * 80)

            # Warm lava colors (red, orange, yellow)
            hue = np.random.randint(0, 30)
            self.lava_blobs.append({
                'x': blob_x,
                'y': blob_y,
                'size': blob_size,
                'speed': 0.5 + np.random.random() * 1.5,
                'wobble': np.random.random() * 2 * np.pi,
                'hue': hue,
                'life': 1.0
            })

        # Update and draw blobs
        new_blobs = []
        for blob in self.lava_blobs:
            blob['y'] -= blob['speed']
            blob['wobble'] += 0.05
            blob['life'] -= 0.002

            # Horizontal wobble
            wobble_x = np.sin(blob['wobble']) * 30
            x = int(blob['x'] + wobble_x)
            y = int(blob['y'])

            if blob['life'] > 0 and y > -100:
                # Size varies with wobble
                current_size = int(blob['size'] * (1 + np.sin(blob['wobble'] * 2) * 0.2))

                # Draw blob with multiple layers for depth
                for layer in range(3, 0, -1):
                    layer_size = int(current_size * (1 + layer * 0.2))
                    alpha = blob['life'] * (0.3 / layer)

                    saturation = 200 + int(alpha * 55)
                    value = 150 + int(alpha * 105)
                    color_hsv = np.array([[[blob['hue'], saturation, value]]], dtype=np.uint8)
                    color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                    color = tuple(int(c * alpha) for c in color_bgr)

                    cv2.circle(frame, (x, y), layer_size, color, -1, lineType=cv2.LINE_AA)

                # Bright core
                core_color = (100, 180, 255)
                cv2.circle(frame, (x, y), int(current_size * 0.6), core_color, -1, lineType=cv2.LINE_AA)

                new_blobs.append(blob)

        self.lava_blobs = new_blobs
        return frame

    def draw_mode_13_dna_helix(self, frame, magnitudes):
        """Mode 13: Double helix DNA structure"""
        self.dna_rotation += 2

        # DNA backbone parameters
        num_points = 80
        helix_radius = 100
        helix_height = self.height - 200
        center_x = self.width // 2
        start_y = 100

        strand1_points = []
        strand2_points = []
        connections = []

        for i in range(num_points):
            progress = i / num_points
            y = int(start_y + progress * helix_height)

            # Get magnitude
            mag_idx = int(progress * len(magnitudes))
            magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

            # Helix calculations
            angle1 = (progress * 4 * np.pi + np.deg2rad(self.dna_rotation))
            angle2 = angle1 + np.pi

            # Radius varies with magnitude
            current_radius = helix_radius + magnitude * 50

            x1 = int(center_x + np.cos(angle1) * current_radius)
            x2 = int(center_x + np.cos(angle2) * current_radius)

            strand1_points.append([x1, y])
            strand2_points.append([x2, y])

            # Base pair connections every few points
            if i % 5 == 0:
                connections.append(([x1, y], [x2, y], magnitude))

        # Draw base pair connections (rungs)
        for conn in connections:
            p1, p2, mag = conn
            # Color based on magnitude (cyan to purple)
            hue = 90 + int(mag * 50)
            saturation = 200 + int(mag * 55)
            value = 150 + int(mag * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            cv2.line(frame, tuple(p1), tuple(p2), color, 2, lineType=cv2.LINE_AA)

        # Draw strands
        if len(strand1_points) > 1:
            strand1_points = np.array(strand1_points, dtype=np.int32)
            strand2_points = np.array(strand2_points, dtype=np.int32)

            # Strand 1 (blue-green)
            cv2.polylines(frame, [strand1_points], False, (255, 200, 0), 5, lineType=cv2.LINE_AA)
            cv2.polylines(frame, [strand1_points], False, (255, 255, 0), 2, lineType=cv2.LINE_AA)

            # Strand 2 (red-orange)
            cv2.polylines(frame, [strand2_points], False, (100, 100, 255), 5, lineType=cv2.LINE_AA)
            cv2.polylines(frame, [strand2_points], False, (150, 150, 255), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_14_lightning_strikes(self, frame, magnitudes):
        """Mode 14: Electric lightning bolts connecting peaks - AGGRESSIVE VERSION"""
        avg_magnitude = np.mean(magnitudes)

        # Find peaks in magnitudes - MUCH LOWER THRESHOLD
        peaks = []
        for i in range(1, len(magnitudes) - 1):
            if magnitudes[i] > 0.2 and magnitudes[i] > magnitudes[i-1] and magnitudes[i] > magnitudes[i+1]:  # Lowered from 0.5 to 0.2
                x = int((i / len(magnitudes)) * self.width)
                y = int(self.height - magnitudes[i] * self.height * 0.7)
                peaks.append((x, y, magnitudes[i]))

        # Generate lightning between peaks - MUCH MORE SENSITIVE
        if avg_magnitude > 0.15 and len(peaks) >= 2:  # Lowered from 0.4 to 0.15
            for i in range(0, len(peaks) - 1):
                if np.random.random() < 0.8:  # Increased from 0.3 to 0.8 (80% chance)
                    start = peaks[i]
                    end = peaks[i + 1]

                    # Create jagged lightning path
                    lightning_points = [start[:2]]
                    num_segments = 8

                    for seg in range(1, num_segments):
                        t = seg / num_segments
                        base_x = int(start[0] + (end[0] - start[0]) * t)
                        base_y = int(start[1] + (end[1] - start[1]) * t)

                        # Add randomness
                        offset_x = np.random.randint(-30, 30)
                        offset_y = np.random.randint(-30, 30)

                        lightning_points.append([base_x + offset_x, base_y + offset_y])

                    lightning_points.append(end[:2])
                    lightning_points = np.array(lightning_points, dtype=np.int32)

                    # Draw lightning with glow
                    intensity = (start[2] + end[2]) / 2

                    # Outer glow (blue-white)
                    cv2.polylines(frame, [lightning_points], False,
                                (255, 200, 100), 8, lineType=cv2.LINE_AA)
                    # Middle layer
                    cv2.polylines(frame, [lightning_points], False,
                                (255, 240, 180), 4, lineType=cv2.LINE_AA)
                    # Bright core
                    cv2.polylines(frame, [lightning_points], False,
                                (255, 255, 255), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_15_morphing_geometry(self, frame, magnitudes):
        """Mode 15: 3D wireframe shapes that morph"""
        avg_magnitude = np.mean(magnitudes)

        # Calculate vertices for a morphing polyhedron
        num_vertices = 8
        rotation_speed = 1 + avg_magnitude * 3
        self.rotation_angle += rotation_speed

        vertices_3d = []

        # Create vertices of a cube that morphs based on magnitude
        for i in range(num_vertices):
            angle_xy = (i / num_vertices) * 2 * np.pi
            angle_z = (i / 4) * np.pi

            # Get magnitude for this vertex
            mag_idx = int((i / num_vertices) * len(magnitudes))
            magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

            # 3D coordinates with magnitude influence
            radius = 200 + magnitude * 150
            x = np.cos(angle_xy + np.deg2rad(self.rotation_angle)) * radius
            y = np.sin(angle_xy + np.deg2rad(self.rotation_angle)) * radius
            z = np.cos(angle_z + np.deg2rad(self.rotation_angle * 0.7)) * radius

            vertices_3d.append([x, y, z])

        # Project to 2D
        vertices_2d = []
        for v in vertices_3d:
            # Simple perspective projection
            scale = 400 / (400 + v[2])
            x_2d = int(self.center_x + v[0] * scale)
            y_2d = int(self.center_y + v[1] * scale)
            vertices_2d.append([x_2d, y_2d])

        # Draw edges
        edge_pairs = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4),
                     (0,4), (1,5), (2,6), (3,7)]

        for edge_idx, (i, j) in enumerate(edge_pairs):
            if i < len(vertices_2d) and j < len(vertices_2d):
                p1 = tuple(vertices_2d[i])
                p2 = tuple(vertices_2d[j])

                # Color cycles through spectrum
                hue = int((edge_idx / len(edge_pairs)) * 180 + self.frame_counter) % 180
                saturation = 220
                value = 200 + int(avg_magnitude * 55)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                cv2.line(frame, p1, p2, color, 3, lineType=cv2.LINE_AA)

        # Draw vertices as glowing dots
        for v in vertices_2d:
            cv2.circle(frame, tuple(v), 8, (255, 255, 255), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, tuple(v), 12, (150, 150, 255), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_16_ink_drops(self, frame, magnitudes):
        """Mode 16: Organic ink dispersing in water"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn ink drops
        if avg_magnitude > 0.4 and self.frame_counter % 15 == 0:
            drop_x = np.random.randint(int(self.width * 0.3), int(self.width * 0.7))
            drop_y = np.random.randint(int(self.height * 0.3), int(self.height * 0.7))

            # Spawn many particles for each drop
            for i in range(int(avg_magnitude * 150 + 50)):
                angle = np.random.random() * 2 * np.pi
                speed = np.random.random() * 3

                # Ink colors (black, dark blue, purple)
                color_choice = np.random.random()
                if color_choice < 0.4:
                    color = (180, 120, 80)  # Dark blue
                elif color_choice < 0.7:
                    color = (150, 80, 120)  # Purple
                else:
                    color = (120, 120, 120)  # Gray

                self.ink_particles.append({
                    'x': drop_x,
                    'y': drop_y,
                    'vx': np.cos(angle) * speed,
                    'vy': np.sin(angle) * speed,
                    'color': color,
                    'life': 1.0,
                    'size': 2 + int(np.random.random() * 6)
                })

        # Update and draw ink particles
        new_particles = []
        for particle in self.ink_particles:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']

            # Slow down over time (like in water)
            particle['vx'] *= 0.98
            particle['vy'] *= 0.98

            particle['life'] -= 0.005

            if particle['life'] > 0:
                alpha = particle['life']
                particle_color = tuple(int(c * alpha) for c in particle['color'])

                # Draw with organic feel
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          particle['size'], particle_color, -1, lineType=cv2.LINE_AA)

                # Slight glow
                if alpha > 0.7:
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                              particle['size'] + 2,
                              tuple(int(c * 0.3) for c in particle_color),
                              1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.ink_particles = new_particles
        return frame

    def draw_mode_17_aurora_waves(self, frame, magnitudes):
        """Mode 17: Northern lights flowing ribbons"""
        # Create flowing aurora ribbons
        num_ribbons = 5

        for ribbon_idx in range(num_ribbons):
            ribbon_y_base = int((ribbon_idx + 1) / (num_ribbons + 1) * self.height)

            points_top = []
            points_bottom = []

            for x in range(0, self.width, 8):
                mag_idx = int((x / self.width) * len(magnitudes))
                magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

                # Flowing wave motion
                wave = np.sin(x * 0.01 + self.frame_counter * 0.05 + ribbon_idx * 0.5) * 60
                wave += np.sin(x * 0.005 + self.frame_counter * 0.03) * 40
                wave += magnitude * 80

                y_top = int(ribbon_y_base + wave - 20)
                y_bottom = int(ribbon_y_base + wave + 20)

                points_top.append([x, y_top])
                points_bottom.append([x, y_bottom])

            if len(points_top) > 1:
                # Combine for filled ribbon
                points_top = np.array(points_top, dtype=np.int32)
                points_bottom = np.array(points_bottom, dtype=np.int32)
                all_points = np.concatenate([points_top, points_bottom[::-1]])

                # Aurora colors (green, blue, purple gradient)
                hue = int(100 + ribbon_idx * 15 + self.frame_counter * 0.5) % 180
                saturation = 180 + int(np.mean(magnitudes) * 75)
                value = 120 + int(np.mean(magnitudes) * 100)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * 0.6) for c in color_bgr)

                # Draw semi-transparent ribbon
                cv2.fillPoly(frame, [all_points], color, lineType=cv2.LINE_AA)

                # Bright edge
                brighter_color = tuple(int(c * 1.3) for c in color)
                cv2.polylines(frame, [points_top], False, brighter_color, 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_18_fractal_bloom(self, frame, magnitudes):
        """Mode 18: Self-similar fractal patterns"""
        avg_magnitude = np.mean(magnitudes)

        # Draw multiple layers of fractals from center
        num_layers = 6

        for layer in range(num_layers):
            num_branches = 8
            layer_progress = layer / num_layers
            base_radius = 50 + layer * 80

            for branch_idx in range(num_branches):
                angle = (branch_idx / num_branches) * 2 * np.pi + self.frame_counter * 0.02

                # Get magnitude for this branch
                mag_idx = int((branch_idx / num_branches) * len(magnitudes))
                magnitude = magnitudes[min(mag_idx, len(magnitudes) - 1)]

                # Branch length based on magnitude
                branch_length = base_radius + magnitude * 100

                # Start point
                start_x = self.center_x
                start_y = self.center_y

                # Draw recursive branches
                for sub_branch in range(3):
                    sub_angle = angle + (sub_branch - 1) * 0.3
                    length_scale = 1.0 - sub_branch * 0.3

                    end_x = int(start_x + np.cos(sub_angle) * branch_length * length_scale)
                    end_y = int(start_y + np.sin(sub_angle) * branch_length * length_scale)

                    # Color based on layer and magnitude
                    hue = int((layer / num_layers) * 180 + magnitude * 40)
                    saturation = 200 + int(magnitude * 55)
                    value = 150 + int(magnitude * 105)
                    color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                    color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                    color = tuple(int(c) for c in color_bgr)

                    thickness = max(1, 4 - layer)
                    cv2.line(frame, (start_x, start_y), (end_x, end_y),
                            color, thickness, lineType=cv2.LINE_AA)

                    # Draw tip glow
                    if sub_branch == 2:
                        cv2.circle(frame, (end_x, end_y),
                                 int(4 + magnitude * 6), color, -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_19_plasma_storm(self, frame, magnitudes):
        """Mode 19: Swirling plasma vortex with tendrils"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn plasma tendrils
        if self.frame_counter % 3 == 0:
            for i in range(int(avg_magnitude * 5 + 2)):
                angle = np.random.random() * 2 * np.pi
                distance = np.random.random() * 50

                tendril_x = self.center_x + np.cos(angle) * distance
                tendril_y = self.center_y + np.sin(angle) * distance

                # Spiral outward velocity
                speed = 2 + np.random.random() * 4
                vx = np.cos(angle) * speed
                vy = np.sin(angle) * speed

                # Plasma colors (purple, cyan, magenta)
                hue = np.random.choice([130, 160, 90])

                self.plasma_tendrils.append({
                    'x': tendril_x,
                    'y': tendril_y,
                    'vx': vx,
                    'vy': vy,
                    'angle': angle,
                    'hue': hue,
                    'life': 1.0,
                    'trail': []
                })

        # Update and draw tendrils
        new_tendrils = []
        for tendril in self.plasma_tendrils:
            # Add to trail
            tendril['trail'].append((int(tendril['x']), int(tendril['y'])))
            if len(tendril['trail']) > 30:
                tendril['trail'].pop(0)

            # Spiral motion
            dx = tendril['x'] - self.center_x
            dy = tendril['y'] - self.center_y
            distance = np.sqrt(dx**2 + dy**2)

            if distance > 1:
                # Add rotation to velocity
                tangent_angle = np.arctan2(dy, dx) + np.pi / 2
                tangent_speed = 2 + avg_magnitude * 3
                tendril['vx'] += np.cos(tangent_angle) * 0.3
                tendril['vy'] += np.sin(tangent_angle) * 0.3

            tendril['x'] += tendril['vx']
            tendril['y'] += tendril['vy']
            tendril['life'] -= 0.01

            if tendril['life'] > 0 and distance < self.max_radius * 1.5:
                # Draw trail
                for trail_idx in range(len(tendril['trail']) - 1):
                    if trail_idx < len(tendril['trail']) - 1:
                        p1 = tendril['trail'][trail_idx]
                        p2 = tendril['trail'][trail_idx + 1]

                        trail_alpha = (trail_idx / len(tendril['trail'])) * tendril['life']

                        saturation = 220
                        value = int(150 + trail_alpha * 105)
                        color_hsv = np.array([[[tendril['hue'], saturation, value]]], dtype=np.uint8)
                        color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                        color = tuple(int(c * trail_alpha) for c in color_bgr)

                        thickness = max(1, int(3 * trail_alpha))
                        cv2.line(frame, p1, p2, color, thickness, lineType=cv2.LINE_AA)

                new_tendrils.append(tendril)

        self.plasma_tendrils = new_tendrils

        # Draw central vortex
        vortex_radius = int(30 + avg_magnitude * 50)
        for glow in range(5, 0, -1):
            glow_color = (int(180 / glow), int(100 / glow), int(200 / glow))
            cv2.circle(frame, (self.center_x, self.center_y),
                      vortex_radius + glow * 8, glow_color, -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_20_crystal_growth(self, frame, magnitudes):
        """Mode 20: Geometric crystals forming and shattering - AGGRESSIVE VERSION"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn crystals MUCH MORE FREQUENTLY on any audio activity
        if avg_magnitude > 0.15 and self.frame_counter % 3 == 0:  # Lowered from 0.5 to 0.15, every 3 frames instead of 10
            num_crystals = 5 + int(avg_magnitude * 8)  # 5-13 crystals (was fixed at 3)
            for i in range(num_crystals):
                # Spawn across entire screen
                crystal_x = self.center_x + np.random.randint(-400, 400)
                crystal_y = self.center_y + np.random.randint(-300, 300)

                num_sides = np.random.choice([5, 6, 7, 8, 10, 12])  # More variety
                size = 30 + int(avg_magnitude * 80)  # Larger crystals

                # Crystal colors (ice blue, white, cyan, purple)
                hue = np.random.choice([90, 100, 110, 120, 130])  # More color variety

                self.crystals.append({
                    'x': crystal_x,
                    'y': crystal_y,
                    'size': size,
                    'sides': num_sides,
                    'rotation': np.random.random() * 360,
                    'growth': 0.0,
                    'hue': hue,
                    'life': 1.0
                })

        # Update and draw crystals
        new_crystals = []
        for crystal in self.crystals:
            crystal['growth'] = min(1.0, crystal['growth'] + 0.08)  # Grow faster
            crystal['rotation'] += 2  # Rotate faster
            crystal['life'] -= 0.005  # Live longer (was 0.008)

            if crystal['life'] > 0:
                current_size = int(crystal['size'] * crystal['growth'])

                # Create polygon points
                points = []
                for i in range(crystal['sides']):
                    angle = (i / crystal['sides']) * 2 * np.pi + np.deg2rad(crystal['rotation'])
                    x = int(crystal['x'] + np.cos(angle) * current_size)
                    y = int(crystal['y'] + np.sin(angle) * current_size)
                    points.append([x, y])

                points = np.array(points, dtype=np.int32)

                # Color with transparency effect
                saturation = 150 + int(crystal['life'] * 105)
                value = 200 + int(crystal['life'] * 55)
                color_hsv = np.array([[[crystal['hue'], saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * crystal['life']) for c in color_bgr)

                # Draw crystal
                cv2.fillPoly(frame, [points], tuple(int(c * 0.4) for c in color), lineType=cv2.LINE_AA)
                cv2.polylines(frame, [points], True, color, 2, lineType=cv2.LINE_AA)

                # Bright center
                cv2.circle(frame, (int(crystal['x']), int(crystal['y'])),
                          int(current_size * 0.3), (255, 255, 255), -1, lineType=cv2.LINE_AA)

                new_crystals.append(crystal)

        self.crystals = new_crystals
        return frame

    def draw_mode_21_gravitational_lens(self, frame, magnitudes):
        """Mode 21: Spacetime warping and bending light"""
        avg_magnitude = np.mean(magnitudes)

        # Create grid of light sources that get warped by "gravity"
        grid_size = 40
        for i in range(grid_size):
            for j in range(grid_size):
                # Original grid position
                x_orig = int((i / grid_size) * self.width)
                y_orig = int((j / grid_size) * self.height)

                # Calculate gravitational warping from center
                dx = x_orig - self.center_x
                dy = y_orig - self.center_y
                distance = np.sqrt(dx**2 + dy**2) + 1

                # Warp strength based on magnitude
                warp_strength = avg_magnitude * 100000 / (distance**2)

                # Warp position
                x_warped = int(x_orig - dx * warp_strength / distance)
                y_warped = int(y_orig - dy * warp_strength / distance)

                # Draw warped grid points with color based on warping
                color_intensity = min(255, int(warp_strength * 50))
                color = (color_intensity, 150, 255 - color_intensity)

                if 0 <= x_warped < self.width and 0 <= y_warped < self.height:
                    cv2.circle(frame, (x_warped, y_warped), 2, color, -1, lineType=cv2.LINE_AA)

        # Draw central "black hole" or massive object
        central_radius = int(20 + avg_magnitude * 60)
        for glow in range(5, 0, -1):
            cv2.circle(frame, (self.center_x, self.center_y),
                      central_radius + glow * 10, (50, 30, 80), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_22_magnetic_fields(self, frame, magnitudes):
        """Mode 22: Iron filing patterns flowing with music"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn magnetic particles
        if self.frame_counter % 2 == 0:
            for i in range(int(avg_magnitude * 30 + 10)):
                particle_x = np.random.randint(0, self.width)
                particle_y = np.random.randint(0, self.height)

                self.magnetic_particles.append({
                    'x': particle_x,
                    'y': particle_y,
                    'vx': 0,
                    'vy': 0,
                    'life': 1.0
                })

        # Create magnetic poles based on frequency bands
        poles = []
        for i in range(4):
            angle = (i / 4) * 2 * np.pi + self.frame_counter * 0.02
            pole_distance = 200 + magnitudes[i * len(magnitudes) // 4] * 100
            pole_x = self.center_x + np.cos(angle) * pole_distance
            pole_y = self.center_y + np.sin(angle) * pole_distance
            pole_charge = 1 if i % 2 == 0 else -1
            poles.append((pole_x, pole_y, pole_charge))

        # Update particles based on magnetic field
        new_particles = []
        for particle in self.magnetic_particles:
            # Calculate force from each pole
            for pole_x, pole_y, charge in poles:
                dx = pole_x - particle['x']
                dy = pole_y - particle['y']
                distance = np.sqrt(dx**2 + dy**2) + 1

                force = charge * 0.5 / distance
                particle['vx'] += (dx / distance) * force
                particle['vy'] += (dy / distance) * force

            # Damping
            particle['vx'] *= 0.95
            particle['vy'] *= 0.95

            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.01

            if particle['life'] > 0 and 0 <= particle['x'] < self.width and 0 <= particle['y'] < self.height:
                # Draw particle (iron filing)
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          2, (100, 100, 100), -1, lineType=cv2.LINE_AA)
                new_particles.append(particle)

        self.magnetic_particles = new_particles

        # Draw poles
        for pole_x, pole_y, charge in poles:
            color = (0, 0, 255) if charge > 0 else (255, 0, 0)
            cv2.circle(frame, (int(pole_x), int(pole_y)), 15, color, -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_23_tribal_drums(self, frame, magnitudes):
        """Mode 23: Concentric shockwaves with ethnic patterns"""
        avg_magnitude = np.mean(magnitudes)

        # Generate shockwaves on strong beats
        if avg_magnitude > 0.5 and self.frame_counter % 8 == 0:
            self.tribal_shockwaves.append({
                'radius': 0,
                'max_radius': 400,
                'life': 1.0,
                'magnitude': avg_magnitude
            })

        # Update and draw shockwaves
        new_shockwaves = []
        for wave in self.tribal_shockwaves:
            wave['radius'] += 8
            wave['life'] -= 0.02

            if wave['life'] > 0 and wave['radius'] < wave['max_radius']:
                # Draw main shockwave ring
                alpha = wave['life']
                thickness = max(1, int(5 * alpha))

                # Earthy tribal colors (oranges, browns, reds)
                hue = 10 + int(wave['magnitude'] * 20)
                saturation = 200 + int(wave['magnitude'] * 55)
                value = 150 + int(wave['magnitude'] * 105)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * alpha) for c in color_bgr)

                cv2.circle(frame, (self.center_x, self.center_y),
                          int(wave['radius']), color, thickness, lineType=cv2.LINE_AA)

                # Add tribal pattern dots around the ring
                num_dots = 16
                for i in range(num_dots):
                    angle = (i / num_dots) * 2 * np.pi
                    dot_x = int(self.center_x + wave['radius'] * np.cos(angle))
                    dot_y = int(self.center_y + wave['radius'] * np.sin(angle))
                    cv2.circle(frame, (dot_x, dot_y), int(4 * alpha), color, -1, lineType=cv2.LINE_AA)

                new_shockwaves.append(wave)

        self.tribal_shockwaves = new_shockwaves

        # Draw central drum
        drum_radius = int(40 + avg_magnitude * 30)
        cv2.circle(frame, (self.center_x, self.center_y), drum_radius,
                  (50, 80, 120), -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, (self.center_x, self.center_y), drum_radius,
                  (100, 130, 160), 3, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_24_neon_cityscape(self, frame, magnitudes):
        """Mode 24: Scrolling city skyline with reactive buildings"""
        # Initialize buildings if not done
        if len(self.cityscape_buildings) == 0:
            for i in range(40):
                self.cityscape_buildings.append({
                    'x': i * 50,
                    'width': 40 + np.random.randint(0, 30),
                    'base_height': 100 + np.random.randint(0, 300),
                    'windows': np.random.randint(3, 8)
                })

        # Scroll buildings
        for building in self.cityscape_buildings:
            building['x'] -= 2
            if building['x'] < -50:
                building['x'] = self.width + 50
                building['width'] = 40 + np.random.randint(0, 30)
                building['base_height'] = 100 + np.random.randint(0, 300)

        # Draw buildings
        for i, building in enumerate(self.cityscape_buildings):
            mag_idx = i % len(magnitudes)
            magnitude = magnitudes[mag_idx]

            # Building height reacts to music
            height = int(building['base_height'] + magnitude * 100)
            building_y = self.height - height

            # Neon colors (cyan, pink, purple)
            hue = (i * 30 + self.frame_counter) % 180
            saturation = 220 + int(magnitude * 35)
            value = 150 + int(magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            # Draw building
            cv2.rectangle(frame, (int(building['x']), building_y),
                         (int(building['x'] + building['width']), self.height),
                         color, -1, lineType=cv2.LINE_AA)

            # Draw windows
            window_rows = int(height / 20)
            for row in range(window_rows):
                for col in range(building['windows']):
                    window_x = int(building['x'] + 5 + col * (building['width'] - 10) / building['windows'])
                    window_y = building_y + 10 + row * 20
                    window_brightness = 255 if magnitude > 0.5 else 150
                    cv2.rectangle(frame, (window_x, window_y),
                                (window_x + 3, window_y + 8),
                                (window_brightness, window_brightness, 100), -1)

        return frame

    def draw_mode_25_heartbeat_monitor(self, frame, magnitudes):
        """Mode 25: Medical monitor with vital signs"""
        # Add current average magnitude to history
        avg_magnitude = np.mean(magnitudes)
        self.heartbeat_history.append(avg_magnitude)
        if len(self.heartbeat_history) > 200:
            self.heartbeat_history.pop(0)

        # Draw monitor background
        monitor_x = 50
        monitor_y = self.center_y - 150
        monitor_width = self.width - 100
        monitor_height = 300

        # Dark monitor background
        cv2.rectangle(frame, (monitor_x, monitor_y),
                     (monitor_x + monitor_width, monitor_y + monitor_height),
                     (20, 30, 20), -1, lineType=cv2.LINE_AA)
        cv2.rectangle(frame, (monitor_x, monitor_y),
                     (monitor_x + monitor_width, monitor_y + monitor_height),
                     (0, 150, 0), 2, lineType=cv2.LINE_AA)

        # Draw grid
        for i in range(0, monitor_width, 30):
            cv2.line(frame, (monitor_x + i, monitor_y),
                    (monitor_x + i, monitor_y + monitor_height),
                    (0, 50, 0), 1, lineType=cv2.LINE_AA)
        for i in range(0, monitor_height, 30):
            cv2.line(frame, (monitor_x, monitor_y + i),
                    (monitor_x + monitor_width, monitor_y + i),
                    (0, 50, 0), 1, lineType=cv2.LINE_AA)

        # Draw heartbeat waveform
        if len(self.heartbeat_history) > 1:
            points = []
            for i, mag in enumerate(self.heartbeat_history):
                x = monitor_x + int((i / len(self.heartbeat_history)) * monitor_width)

                # Create ECG-style waveform
                if mag > 0.7:
                    y_offset = -int(mag * 200)
                else:
                    y_offset = -int(mag * 80)

                y = monitor_y + monitor_height // 2 + y_offset
                points.append([x, y])

            points = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [points], False, (0, 255, 0), 2, lineType=cv2.LINE_AA)

        # Draw BPM counter
        bpm = int(60 + avg_magnitude * 100)
        cv2.putText(frame, f"BPM: {bpm}", (monitor_x + 20, monitor_y + 40),
                   cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2, cv2.LINE_AA)

        return frame

    def draw_mode_26_ocean_depths(self, frame, magnitudes):
        """Mode 26: Deep sea bioluminescent creatures"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn bioluminescent creatures
        if self.frame_counter % 10 == 0 and avg_magnitude > 0.3:
            creature_x = np.random.randint(0, self.width)
            creature_y = np.random.randint(0, self.height)

            self.bioluminescent_creatures.append({
                'x': creature_x,
                'y': creature_y,
                'vx': np.random.uniform(-2, 2),
                'vy': np.random.uniform(-1, 1),
                'size': 10 + int(avg_magnitude * 30),
                'tentacles': 5 + int(avg_magnitude * 10),
                'life': 1.0,
                'phase': np.random.random() * 2 * np.pi
            })

        # Update and draw creatures
        new_creatures = []
        for creature in self.bioluminescent_creatures:
            creature['x'] += creature['vx']
            creature['y'] += creature['vy']
            creature['phase'] += 0.1
            creature['life'] -= 0.005

            if creature['life'] > 0:
                alpha = creature['life']

                # Draw creature body (jellyfish-like)
                body_color = (255, int(150 * alpha), int(100 * alpha))
                cv2.circle(frame, (int(creature['x']), int(creature['y'])),
                          creature['size'], body_color, -1, lineType=cv2.LINE_AA)

                # Draw tentacles
                for i in range(creature['tentacles']):
                    angle = (i / creature['tentacles']) * 2 * np.pi
                    tentacle_points = []
                    for seg in range(5):
                        wave = np.sin(creature['phase'] + seg * 0.5) * 10
                        seg_x = int(creature['x'] + np.cos(angle) * wave + np.cos(angle) * seg * 8)
                        seg_y = int(creature['y'] + creature['size'] + seg * 12)
                        tentacle_points.append([seg_x, seg_y])

                    if len(tentacle_points) > 1:
                        tentacle_points = np.array(tentacle_points, dtype=np.int32)
                        tentacle_color = tuple(int(c * alpha * 0.7) for c in body_color)
                        cv2.polylines(frame, [tentacle_points], False, tentacle_color, 2, lineType=cv2.LINE_AA)

                # Glow
                cv2.circle(frame, (int(creature['x']), int(creature['y'])),
                          creature['size'] + 10, tuple(int(c * 0.3 * alpha) for c in body_color),
                          -1, lineType=cv2.LINE_AA)

                new_creatures.append(creature)

        self.bioluminescent_creatures = new_creatures
        return frame

    def draw_mode_27_fire_dance(self, frame, magnitudes):
        """Mode 27: Realistic flames dancing to rhythm"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn fire particles from bottom
        if self.frame_counter % 2 == 0:
            num_particles = int(20 + avg_magnitude * 50)
            for i in range(num_particles):
                fire_x = self.center_x + np.random.randint(-150, 150)
                fire_y = self.height - 50

                self.fire_particles.append({
                    'x': fire_x,
                    'y': fire_y,
                    'vx': np.random.uniform(-1, 1),
                    'vy': -3 - np.random.random() * avg_magnitude * 8,
                    'life': 1.0,
                    'size': 3 + int(np.random.random() * 8)
                })

        # Update and draw fire
        new_particles = []
        for particle in self.fire_particles:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['vy'] += 0.1  # Slight upward curve
            particle['vx'] += np.random.uniform(-0.2, 0.2)
            particle['life'] -= 0.015

            if particle['life'] > 0 and particle['y'] > 0:
                alpha = particle['life']

                # Fire color gradient: white -> yellow -> orange -> red -> black
                if alpha > 0.8:
                    color = (255, 255, 255)  # White hot
                elif alpha > 0.6:
                    color = (100, 255, 255)  # Yellow
                elif alpha > 0.4:
                    color = (0, 180, 255)    # Orange
                else:
                    color = (0, 50, 200)     # Deep red

                particle_color = tuple(int(c * alpha) for c in color)

                # Draw particle
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          particle['size'], particle_color, -1, lineType=cv2.LINE_AA)

                # Glow
                if alpha > 0.5:
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                              particle['size'] + 4,
                              tuple(int(c * 0.3 * alpha) for c in color),
                              -1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.fire_particles = new_particles
        return frame

    def draw_mode_28_particle_collider(self, frame, magnitudes):
        """Mode 28: High-energy physics collision visualization"""
        avg_magnitude = np.mean(magnitudes)

        # Create particle collision on strong beats
        if avg_magnitude > 0.6 and self.frame_counter % 15 == 0:
            # Spawn particles from collision at center
            num_particles = int(50 + avg_magnitude * 100)
            for i in range(num_particles):
                angle = np.random.random() * 2 * np.pi
                speed = 5 + np.random.random() * 15

                self.collision_particles.append({
                    'x': self.center_x,
                    'y': self.center_y,
                    'vx': np.cos(angle) * speed,
                    'vy': np.sin(angle) * speed,
                    'life': 1.0,
                    'charge': np.random.choice([-1, 1]),
                    'trail': []
                })

        # Update particles
        new_particles = []
        for particle in self.collision_particles:
            particle['trail'].append((int(particle['x']), int(particle['y'])))
            if len(particle['trail']) > 15:
                particle['trail'].pop(0)

            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.012

            if particle['life'] > 0:
                alpha = particle['life']

                # Color based on charge (blue for negative, red for positive)
                if particle['charge'] > 0:
                    color = (0, 100, 255)  # Red
                else:
                    color = (255, 100, 0)  # Blue

                # Draw trail
                for trail_idx in range(len(particle['trail']) - 1):
                    p1 = particle['trail'][trail_idx]
                    p2 = particle['trail'][trail_idx + 1]
                    trail_alpha = (trail_idx / len(particle['trail'])) * alpha
                    trail_color = tuple(int(c * trail_alpha) for c in color)
                    cv2.line(frame, p1, p2, trail_color, 2, lineType=cv2.LINE_AA)

                # Draw particle
                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          4, tuple(int(c * alpha) for c in color), -1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.collision_particles = new_particles

        # Draw collision center with energy rings
        if avg_magnitude > 0.5:
            for ring in range(3):
                radius = int(20 + ring * 15 + avg_magnitude * 30)
                cv2.circle(frame, (self.center_x, self.center_y), radius,
                          (180, 180, 255), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_29_rainbow_prism(self, frame, magnitudes):
        """Mode 29: Light refraction through rotating prism"""
        avg_magnitude = np.mean(magnitudes)
        self.prism_rotation += 1 + avg_magnitude * 3

        # Draw prism (triangle) at center
        prism_size = 100 + int(avg_magnitude * 100)
        prism_points = []
        for i in range(3):
            angle = np.deg2rad(self.prism_rotation + i * 120)
            x = int(self.center_x + np.cos(angle) * prism_size)
            y = int(self.center_y + np.sin(angle) * prism_size)
            prism_points.append([x, y])

        prism_points = np.array(prism_points, dtype=np.int32)
        cv2.fillPoly(frame, [prism_points], (200, 200, 220), lineType=cv2.LINE_AA)
        cv2.polylines(frame, [prism_points], True, (255, 255, 255), 3, lineType=cv2.LINE_AA)

        # Draw refracted rainbow beams
        num_beams = len(magnitudes)
        for i in range(min(num_beams, 30)):
            magnitude = magnitudes[i]
            if magnitude > 0.2:
                # Beam angle based on frequency (dispersion)
                base_angle = np.deg2rad(self.prism_rotation + 60)
                angle_spread = (i / num_beams - 0.5) * 60
                beam_angle = base_angle + np.deg2rad(angle_spread)

                # Beam length based on magnitude
                beam_length = 150 + magnitude * 300

                # Start from prism edge
                start_x = self.center_x + int(np.cos(base_angle) * prism_size)
                start_y = self.center_y + int(np.sin(base_angle) * prism_size)

                end_x = int(start_x + np.cos(beam_angle) * beam_length)
                end_y = int(start_y + np.sin(beam_angle) * beam_length)

                # Rainbow color
                hue = int((i / num_beams) * 180)
                saturation = 255
                value = 200 + int(magnitude * 55)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                # Draw beam with glow
                thickness = max(2, int(magnitude * 8))
                cv2.line(frame, (start_x, start_y), (end_x, end_y),
                        tuple(int(c * 0.4) for c in color), thickness + 4, lineType=cv2.LINE_AA)
                cv2.line(frame, (start_x, start_y), (end_x, end_y),
                        color, thickness, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_30_seismic_waves(self, frame, magnitudes):
        """Mode 30: Earthquake seismograph readings"""
        # Add current magnitudes to seismic history
        avg_magnitude = np.mean(magnitudes)
        self.seismic_readings.append(magnitudes.copy())
        if len(self.seismic_readings) > 150:
            self.seismic_readings.pop(0)

        # Draw seismograph paper background
        paper_margin = 50
        cv2.rectangle(frame, (paper_margin, paper_margin),
                     (self.width - paper_margin, self.height - paper_margin),
                     (240, 235, 220), -1, lineType=cv2.LINE_AA)

        # Draw grid lines
        for i in range(paper_margin, self.width - paper_margin, 40):
            cv2.line(frame, (i, paper_margin), (i, self.height - paper_margin),
                    (200, 195, 180), 1, lineType=cv2.LINE_AA)
        for i in range(paper_margin, self.height - paper_margin, 40):
            cv2.line(frame, (paper_margin, i), (self.width - paper_margin, i),
                    (200, 195, 180), 1, lineType=cv2.LINE_AA)

        # Draw seismic waveforms (3 channels: vertical, horizontal1, horizontal2)
        if len(self.seismic_readings) > 1:
            for channel in range(3):
                channel_y = paper_margin + 100 + channel * 250

                # Draw baseline
                cv2.line(frame, (paper_margin, channel_y),
                        (self.width - paper_margin, channel_y),
                        (150, 150, 150), 1, lineType=cv2.LINE_AA)

                # Draw waveform
                points = []
                for i, reading in enumerate(self.seismic_readings):
                    x = paper_margin + int((i / len(self.seismic_readings)) * (self.width - 2 * paper_margin))

                    # Different frequency ranges for each channel
                    if channel == 0:
                        mag = np.mean(reading[:len(reading)//3])
                    elif channel == 1:
                        mag = np.mean(reading[len(reading)//3:2*len(reading)//3])
                    else:
                        mag = np.mean(reading[2*len(reading)//3:])

                    y_offset = -int(mag * 100)
                    y = channel_y + y_offset
                    points.append([x, y])

                if len(points) > 1:
                    points = np.array(points, dtype=np.int32)
                    cv2.polylines(frame, [points], False, (30, 30, 30), 2, lineType=cv2.LINE_AA)

                # Channel label
                cv2.putText(frame, f"CH{channel+1}", (paper_margin + 10, channel_y - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (80, 80, 80), 2, cv2.LINE_AA)

        # Magnitude indicator
        magnitude_scale = avg_magnitude * 10
        cv2.putText(frame, f"M{magnitude_scale:.1f}", (self.width - 150, paper_margin + 40),
                   cv2.FONT_HERSHEY_SIMPLEX, 1.5, (200, 0, 0), 3, cv2.LINE_AA)

        return frame

    def draw_mode_31_origami_unfold(self, frame, magnitudes):
        """Mode 31: Paper folding and unfolding geometrically"""
        avg_magnitude = np.mean(magnitudes)

        # Create origami crane-like shape that unfolds with music
        num_segments = 8
        for seg_idx in range(num_segments):
            angle = (seg_idx / num_segments) * 2 * np.pi + self.frame_counter * 0.02

            # Get magnitude for this segment
            mag_idx = seg_idx % len(magnitudes)
            magnitude = magnitudes[mag_idx]

            # Fold angle based on magnitude (0 = folded, 1 = unfolded)
            fold_amount = 0.3 + magnitude * 0.7

            # Draw origami segments
            base_radius = 150
            inner_radius = base_radius * (1 - fold_amount)
            outer_radius = base_radius * fold_amount

            # Create folded paper shape
            points = []
            for i in range(4):
                sub_angle = angle + (i / 4) * (np.pi / 4)
                radius = inner_radius if i % 2 == 0 else outer_radius
                x = int(self.center_x + np.cos(sub_angle) * radius)
                y = int(self.center_y + np.sin(sub_angle) * radius)
                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            # Paper color (off-white to colored based on magnitude)
            hue = int(seg_idx * 22.5) % 180
            saturation = int(magnitude * 150)
            value = 220 + int(magnitude * 35)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            cv2.fillPoly(frame, [points], color, lineType=cv2.LINE_AA)
            cv2.polylines(frame, [points], True, (180, 180, 180), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_32_storm_clouds(self, frame, magnitudes):
        """Mode 32: Thunder and lightning in swirling clouds"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn storm particles
        if self.frame_counter % 3 == 0:
            for i in range(int(avg_magnitude * 20 + 10)):
                self.storm_particles.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height // 2),
                    'vx': np.random.uniform(-2, 2),
                    'vy': np.random.uniform(0.5, 2),
                    'size': 15 + int(np.random.random() * 40),
                    'life': 1.0
                })

        # Update and draw clouds
        new_particles = []
        for cloud in self.storm_particles:
            cloud['x'] += cloud['vx']
            cloud['y'] += cloud['vy']
            cloud['life'] -= 0.008

            if cloud['life'] > 0:
                alpha = cloud['life']
                # Dark storm cloud color
                cloud_color = (int(50 * alpha), int(50 * alpha), int(60 * alpha))

                cv2.circle(frame, (int(cloud['x']), int(cloud['y'])),
                          cloud['size'], cloud_color, -1, lineType=cv2.LINE_AA)

                new_particles.append(cloud)

        self.storm_particles = new_particles

        # Lightning strikes on strong beats
        if avg_magnitude > 0.7 and np.random.random() < 0.3:
            # Random lightning bolt
            strike_x = np.random.randint(100, self.width - 100)
            strike_y_start = 50
            strike_y_end = self.height - 50

            # Jagged lightning path
            lightning_points = [[strike_x, strike_y_start]]
            current_x = strike_x
            for y in range(strike_y_start, strike_y_end, 40):
                current_x += np.random.randint(-50, 50)
                lightning_points.append([current_x, y])
            lightning_points.append([current_x, strike_y_end])

            lightning_points = np.array(lightning_points, dtype=np.int32)

            # Draw lightning with glow
            cv2.polylines(frame, [lightning_points], False, (255, 255, 200), 8, lineType=cv2.LINE_AA)
            cv2.polylines(frame, [lightning_points], False, (255, 255, 255), 3, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_33_binary_matrix(self, frame, magnitudes):
        """Mode 33: Falling Matrix-style binary code"""
        # Initialize matrix columns if needed
        if len(self.matrix_columns) == 0:
            for i in range(50):
                self.matrix_columns.append({
                    'x': i * (self.width // 50),
                    'y': np.random.randint(-500, 0),
                    'speed': 5 + np.random.randint(0, 15),
                    'length': 10 + np.random.randint(0, 30),
                    'chars': [np.random.choice(['0', '1']) for _ in range(40)]
                })

        # Update and draw columns
        for col_idx, column in enumerate(self.matrix_columns):
            mag_idx = col_idx % len(magnitudes)
            magnitude = magnitudes[mag_idx]

            # Speed influenced by magnitude
            column['y'] += column['speed'] + int(magnitude * 10)

            if column['y'] > self.height + 100:
                column['y'] = -500
                column['chars'] = [np.random.choice(['0', '1']) for _ in range(40)]

            # Draw characters
            for char_idx in range(column['length']):
                char_y = int(column['y'] + char_idx * 20)
                if 0 <= char_y < self.height:
                    # Bright green for leading edge, fading behind
                    alpha = 1.0 - (char_idx / column['length'])
                    green_value = int(255 * alpha)

                    cv2.putText(frame, column['chars'][char_idx % len(column['chars'])],
                              (column['x'], char_y),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                              (0, green_value, 0), 2, cv2.LINE_AA)

        return frame

    def draw_mode_34_kaleidoscope(self, frame, magnitudes):
        """Mode 34: Symmetric mirrored patterns"""
        avg_magnitude = np.mean(magnitudes)
        self.kaleidoscope_rotation += 0.5 + avg_magnitude * 2

        # Number of symmetry sections
        num_sections = 8
        section_angle = 360 / num_sections

        # Create base pattern in one section
        pattern_elements = []
        for i in range(min(20, len(magnitudes))):
            magnitude = magnitudes[i]
            if magnitude > 0.3:
                # Element position within one section
                angle_in_section = (i / 20) * section_angle
                radius = 100 + magnitude * 250

                pattern_elements.append({
                    'angle': angle_in_section,
                    'radius': radius,
                    'size': int(5 + magnitude * 20),
                    'hue': int((i / 20) * 180)
                })

        # Mirror pattern across all sections
        for section in range(num_sections):
            section_rotation = section * section_angle + self.kaleidoscope_rotation

            for elem in pattern_elements:
                total_angle = section_rotation + elem['angle']
                x = int(self.center_x + np.cos(np.deg2rad(total_angle)) * elem['radius'])
                y = int(self.center_y + np.sin(np.deg2rad(total_angle)) * elem['radius'])

                # Color
                saturation = 255
                value = 255
                color_hsv = np.array([[[elem['hue'], saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                cv2.circle(frame, (x, y), elem['size'], color, -1, lineType=cv2.LINE_AA)
                cv2.circle(frame, (x, y), elem['size'] + 3,
                          tuple(int(c * 0.5) for c in color), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_35_laser_show(self, frame, magnitudes):
        """Mode 35: Concert laser beams and spotlights"""
        avg_magnitude = np.mean(magnitudes)

        # Update laser beams based on frequencies
        self.laser_beams = []
        for i in range(min(12, len(magnitudes))):
            magnitude = magnitudes[i * len(magnitudes) // 12]

            if magnitude > 0.4:
                # Laser beam from bottom corners
                if i % 2 == 0:
                    start_x = 0
                    start_y = self.height
                else:
                    start_x = self.width
                    start_y = self.height

                # Beam angle based on frequency
                angle = np.deg2rad(45 + i * 10 + self.frame_counter * 2)
                beam_length = 600 + magnitude * 400

                end_x = int(start_x + np.cos(angle) * beam_length)
                end_y = int(start_y - np.sin(angle) * beam_length)

                # Laser color (various neon colors)
                hue = (i * 30 + self.frame_counter) % 180
                saturation = 255
                value = 200 + int(magnitude * 55)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                self.laser_beams.append({
                    'start': (start_x, start_y),
                    'end': (end_x, end_y),
                    'color': color,
                    'thickness': max(2, int(magnitude * 8))
                })

        # Draw laser beams
        for laser in self.laser_beams:
            # Outer glow
            cv2.line(frame, laser['start'], laser['end'],
                    tuple(int(c * 0.3) for c in laser['color']),
                    laser['thickness'] + 6, lineType=cv2.LINE_AA)
            # Main beam
            cv2.line(frame, laser['start'], laser['end'],
                    laser['color'], laser['thickness'], lineType=cv2.LINE_AA)

        # Add smoke/haze effect (particles in laser beams)
        if avg_magnitude > 0.5:
            for laser in self.laser_beams:
                for t in np.arange(0.2, 1.0, 0.15):
                    smoke_x = int(laser['start'][0] + (laser['end'][0] - laser['start'][0]) * t)
                    smoke_y = int(laser['start'][1] + (laser['end'][1] - laser['start'][1]) * t)
                    cv2.circle(frame, (smoke_x, smoke_y), 20,
                              tuple(int(c * 0.2) for c in laser['color']),
                              -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_36_sandstorm(self, frame, magnitudes):
        """Mode 36: Desert sand particles in wind vortex"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn sand particles
        if self.frame_counter % 2 == 0:
            for i in range(int(30 + avg_magnitude * 70)):
                self.sand_particles.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'vx': np.random.uniform(-5, 5),
                    'vy': np.random.uniform(-3, 3),
                    'life': 1.0,
                    'size': 1 + int(np.random.random() * 3)
                })

        # Vortex center moves with music
        vortex_x = self.center_x + int(np.sin(self.frame_counter * 0.05) * 200)
        vortex_y = self.center_y + int(np.cos(self.frame_counter * 0.03) * 100)

        # Update sand particles
        new_particles = []
        for particle in self.sand_particles:
            # Attraction to vortex
            dx = vortex_x - particle['x']
            dy = vortex_y - particle['y']
            distance = np.sqrt(dx**2 + dy**2) + 1

            # Swirling motion
            angle = np.arctan2(dy, dx) + np.pi / 2
            force = (avg_magnitude + 0.3) * 50 / distance

            particle['vx'] += np.cos(angle) * force * 0.1
            particle['vy'] += np.sin(angle) * force * 0.1

            # Wind effect
            particle['vx'] += np.sin(self.frame_counter * 0.1) * 0.5

            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.01

            # Wrap around screen
            if particle['x'] < 0:
                particle['x'] = self.width
            if particle['x'] > self.width:
                particle['x'] = 0
            if particle['y'] < 0:
                particle['y'] = self.height
            if particle['y'] > self.height:
                particle['y'] = 0

            if particle['life'] > 0:
                alpha = particle['life']
                # Sandy brown colors
                sand_color = (int(140 * alpha), int(180 * alpha), int(220 * alpha))

                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          particle['size'], sand_color, -1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.sand_particles = new_particles

        # Draw vortex center
        vortex_radius = int(20 + avg_magnitude * 40)
        for glow in range(4, 0, -1):
            cv2.circle(frame, (vortex_x, vortex_y),
                      vortex_radius + glow * 10,
                      (int(100 / glow), int(120 / glow), int(80 / glow)),
                      -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_37_ice_shatter(self, frame, magnitudes):
        """Mode 37: Cracking and breaking ice surface"""
        avg_magnitude = np.mean(magnitudes)

        # Create crack on strong beats
        if avg_magnitude > 0.6 and self.frame_counter % 20 == 0:
            # Start crack from random point
            crack_start_x = np.random.randint(200, self.width - 200)
            crack_start_y = np.random.randint(200, self.height - 200)

            crack = {
                'segments': [[crack_start_x, crack_start_y]],
                'life': 1.0,
                'branches': []
            }

            # Generate crack segments
            current_x, current_y = crack_start_x, crack_start_y
            for seg in range(10):
                angle = np.random.uniform(0, 2 * np.pi)
                length = 30 + np.random.random() * 60
                current_x += int(np.cos(angle) * length)
                current_y += int(np.sin(angle) * length)
                crack['segments'].append([current_x, current_y])

                # Random branches
                if np.random.random() < 0.4:
                    branch_angle = angle + np.random.uniform(-np.pi/2, np.pi/2)
                    branch_x = current_x
                    branch_y = current_y
                    branch_points = [[branch_x, branch_y]]
                    for b in range(3):
                        branch_x += int(np.cos(branch_angle) * 40)
                        branch_y += int(np.sin(branch_angle) * 40)
                        branch_points.append([branch_x, branch_y])
                    crack['branches'].append(branch_points)

            self.ice_cracks.append(crack)

        # Draw ice cracks
        new_cracks = []
        for crack in self.ice_cracks:
            crack['life'] -= 0.005

            if crack['life'] > 0:
                alpha = crack['life']
                crack_color = (int(200 * alpha), int(230 * alpha), int(255 * alpha))

                # Draw main crack
                if len(crack['segments']) > 1:
                    segments = np.array(crack['segments'], dtype=np.int32)
                    cv2.polylines(frame, [segments], False, crack_color, 3, lineType=cv2.LINE_AA)
                    cv2.polylines(frame, [segments], False, (255, 255, 255), 1, lineType=cv2.LINE_AA)

                # Draw branches
                for branch in crack['branches']:
                    if len(branch) > 1:
                        branch_arr = np.array(branch, dtype=np.int32)
                        cv2.polylines(frame, [branch_arr], False, crack_color, 2, lineType=cv2.LINE_AA)

                new_cracks.append(crack)

        self.ice_cracks = new_cracks

        # Ice surface shimmer
        for i in range(20):
            shimmer_x = np.random.randint(0, self.width)
            shimmer_y = np.random.randint(0, self.height)
            cv2.circle(frame, (shimmer_x, shimmer_y), 2,
                      (220, 240, 255), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_38_cellular_division(self, frame, magnitudes):
        """Mode 38: Organic cells splitting and multiplying"""
        avg_magnitude = np.mean(magnitudes)

        # Initialize cells if empty
        if len(self.cells) == 0:
            for i in range(5):
                self.cells.append({
                    'x': np.random.randint(100, self.width - 100),
                    'y': np.random.randint(100, self.height - 100),
                    'size': 40 + np.random.randint(0, 40),
                    'life': 1.0,
                    'division_timer': 0,
                    'hue': np.random.randint(0, 180)
                })

        # Update cells
        new_cells = []
        for cell in self.cells:
            cell['division_timer'] += avg_magnitude * 5
            cell['life'] -= 0.002

            # Cell division on timer
            if cell['division_timer'] > 100 and cell['life'] > 0.5 and len(self.cells) < 20:
                # Create two daughter cells
                for i in range(2):
                    angle = np.random.random() * 2 * np.pi
                    offset = 30
                    new_cells.append({
                        'x': cell['x'] + np.cos(angle) * offset,
                        'y': cell['y'] + np.sin(angle) * offset,
                        'size': cell['size'] * 0.7,
                        'life': 1.0,
                        'division_timer': 0,
                        'hue': (cell['hue'] + np.random.randint(-10, 10)) % 180
                    })
                cell['life'] = 0  # Parent cell dies

            if cell['life'] > 0:
                # Pulsing size
                pulse = 1.0 + np.sin(self.frame_counter * 0.1 + cell['x']) * 0.2
                current_size = int(cell['size'] * pulse)

                # Cell color
                saturation = 180 + int(cell['life'] * 75)
                value = 150 + int(cell['life'] * 105)
                color_hsv = np.array([[[cell['hue'], saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                # Draw cell
                cv2.circle(frame, (int(cell['x']), int(cell['y'])),
                          current_size, color, -1, lineType=cv2.LINE_AA)
                cv2.circle(frame, (int(cell['x']), int(cell['y'])),
                          current_size, tuple(int(c * 1.3) for c in color), 2, lineType=cv2.LINE_AA)

                # Nucleus
                nucleus_size = int(current_size * 0.4)
                cv2.circle(frame, (int(cell['x']), int(cell['y'])),
                          nucleus_size, tuple(int(c * 0.6) for c in color), -1, lineType=cv2.LINE_AA)

                new_cells.append(cell)

        self.cells = new_cells
        return frame

    def draw_mode_39_neon_tubes(self, frame, magnitudes):
        """Mode 39: Glowing tube shapes bending and twisting"""
        # Create neon tubes that react to music
        num_tubes = 8

        for tube_idx in range(num_tubes):
            # Get magnitude for this tube
            mag_idx = tube_idx * len(magnitudes) // num_tubes
            magnitude = magnitudes[mag_idx]

            # Tube path
            points = []
            y_start = (tube_idx + 1) / (num_tubes + 1) * self.height

            for x in range(0, self.width, 20):
                # Sinusoidal bending based on magnitude
                wave1 = np.sin(x * 0.01 + self.frame_counter * 0.05 + tube_idx) * magnitude * 60
                wave2 = np.sin(x * 0.02 + self.frame_counter * 0.03) * 30
                y = int(y_start + wave1 + wave2)
                points.append([x, y])

            if len(points) > 1:
                points = np.array(points, dtype=np.int32)

                # Neon color
                hue = (tube_idx * 25 + self.frame_counter) % 180
                saturation = 255
                value = 180 + int(magnitude * 75)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                # Tube thickness based on magnitude
                thickness = max(4, int(6 + magnitude * 12))

                # Draw glow layers
                cv2.polylines(frame, [points], False,
                            tuple(int(c * 0.3) for c in color), thickness + 8, lineType=cv2.LINE_AA)
                cv2.polylines(frame, [points], False,
                            tuple(int(c * 0.6) for c in color), thickness + 4, lineType=cv2.LINE_AA)
                cv2.polylines(frame, [points], False, color, thickness, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_40_cosmic_strings(self, frame, magnitudes):
        """Mode 40: Universe-scale energy strings vibrating"""
        avg_magnitude = np.mean(magnitudes)

        # Draw cosmic string network
        num_strings = 6

        for string_idx in range(num_strings):
            # String endpoints
            angle1 = (string_idx / num_strings) * 2 * np.pi + self.frame_counter * 0.01
            angle2 = angle1 + np.pi + 0.3

            mag_idx = string_idx % len(magnitudes)
            magnitude = magnitudes[mag_idx]

            radius = 300 + magnitude * 200

            x1 = int(self.center_x + np.cos(angle1) * radius)
            y1 = int(self.center_y + np.sin(angle1) * radius)
            x2 = int(self.center_x + np.cos(angle2) * radius)
            y2 = int(self.center_y + np.sin(angle2) * radius)

            # Create vibrating string path
            num_segments = 20
            points = []
            for seg in range(num_segments + 1):
                t = seg / num_segments
                base_x = int(x1 + (x2 - x1) * t)
                base_y = int(y1 + (y2 - y1) * t)

                # Vibration perpendicular to string
                perpendicular_angle = angle1 + np.pi / 2
                vibration = np.sin(t * np.pi * 5 + self.frame_counter * 0.2) * magnitude * 50

                vib_x = int(base_x + np.cos(perpendicular_angle) * vibration)
                vib_y = int(base_y + np.sin(perpendicular_angle) * vibration)

                points.append([vib_x, vib_y])

            points = np.array(points, dtype=np.int32)

            # Cosmic energy color (purple/blue/white)
            hue = 120 + int(magnitude * 40)
            saturation = 200 + int(magnitude * 55)
            value = 180 + int(magnitude * 75)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            # Draw string with energy glow
            cv2.polylines(frame, [points], False,
                        tuple(int(c * 0.4) for c in color), 12, lineType=cv2.LINE_AA)
            cv2.polylines(frame, [points], False, color, 4, lineType=cv2.LINE_AA)
            cv2.polylines(frame, [points], False, (255, 255, 255), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_41_paint_splatter(self, frame, magnitudes):
        """Mode 41: Jackson Pollock drip painting style"""
        avg_magnitude = np.mean(magnitudes)

        # Create paint splatters on strong beats
        if avg_magnitude > 0.4 and self.frame_counter % 5 == 0:
            for i in range(int(avg_magnitude * 15 + 5)):
                splatter_x = np.random.randint(0, self.width)
                splatter_y = np.random.randint(0, self.height)

                # Paint drips from splatter point
                num_drips = int(10 + avg_magnitude * 30)
                for drip in range(num_drips):
                    angle = np.random.random() * 2 * np.pi
                    speed = np.random.random() * 8

                    # Random vibrant colors
                    hue = np.random.randint(0, 180)

                    self.paint_splatters.append({
                        'x': splatter_x,
                        'y': splatter_y,
                        'vx': np.cos(angle) * speed,
                        'vy': np.sin(angle) * speed + 2,  # Gravity
                        'hue': hue,
                        'life': 1.0,
                        'size': 2 + int(np.random.random() * 6),
                        'trail': []
                    })

        # Update paint
        new_splatters = []
        for paint in self.paint_splatters:
            paint['trail'].append((int(paint['x']), int(paint['y'])))
            if len(paint['trail']) > 25:
                paint['trail'].pop(0)

            paint['x'] += paint['vx']
            paint['y'] += paint['vy']
            paint['vy'] += 0.3  # Gravity
            paint['life'] -= 0.015

            if paint['life'] > 0 and 0 <= paint['x'] < self.width and 0 <= paint['y'] < self.height:
                alpha = paint['life']

                saturation = 220 + int(alpha * 35)
                value = 180 + int(alpha * 75)
                color_hsv = np.array([[[paint['hue'], saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * alpha) for c in color_bgr)

                # Draw trail
                for trail_idx in range(len(paint['trail']) - 1):
                    p1 = paint['trail'][trail_idx]
                    p2 = paint['trail'][trail_idx + 1]
                    trail_alpha = (trail_idx / len(paint['trail'])) * alpha
                    trail_color = tuple(int(c * trail_alpha) for c in color)
                    cv2.line(frame, p1, p2, trail_color, paint['size'], lineType=cv2.LINE_AA)

                new_splatters.append(paint)

        self.paint_splatters = new_splatters
        return frame

    def draw_mode_42_quantum_foam(self, frame, magnitudes):
        """Mode 42: Bubbling spacetime at quantum scale"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn quantum bubbles
        if self.frame_counter % 2 == 0:
            for i in range(int(avg_magnitude * 25 + 10)):
                self.quantum_bubbles.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'size': 5 + int(np.random.random() * 25),
                    'growth': np.random.uniform(0.5, 1.5),
                    'life': 1.0,
                    'phase': np.random.random() * 2 * np.pi
                })

        # Update bubbles
        new_bubbles = []
        for bubble in self.quantum_bubbles:
            bubble['size'] *= bubble['growth']
            bubble['phase'] += 0.15
            bubble['life'] -= 0.02

            if bubble['life'] > 0 and bubble['size'] < 80:
                alpha = bubble['life']

                # Quantum color shimmer
                hue = int((bubble['phase'] * 30 + self.frame_counter) % 180)
                saturation = 200 + int(alpha * 55)
                value = 150 + int(alpha * 105)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * alpha * 0.6) for c in color_bgr)

                # Draw bubble
                cv2.circle(frame, (int(bubble['x']), int(bubble['y'])),
                          int(bubble['size']), color, 2, lineType=cv2.LINE_AA)

                # Shimmer inside
                shimmer_size = int(bubble['size'] * 0.7)
                cv2.circle(frame, (int(bubble['x']), int(bubble['y'])),
                          shimmer_size, tuple(int(c * 0.3) for c in color), -1, lineType=cv2.LINE_AA)

                new_bubbles.append(bubble)

        self.quantum_bubbles = new_bubbles
        return frame

    def draw_mode_43_aztec_sun(self, frame, magnitudes):
        """Mode 43: Ancient Aztec calendar rotating and glowing"""
        avg_magnitude = np.mean(magnitudes)
        self.aztec_rotation += 0.5 + avg_magnitude * 2

        # Draw Aztec sun stone layers
        # Outer ring with symbols
        outer_radius = 350 + int(avg_magnitude * 100)
        num_symbols = 20

        for i in range(num_symbols):
            angle = np.deg2rad(self.aztec_rotation + i * (360 / num_symbols))
            x = int(self.center_x + np.cos(angle) * outer_radius)
            y = int(self.center_y + np.sin(angle) * outer_radius)

            # Symbol blocks
            symbol_size = 15 + int(avg_magnitude * 10)
            cv2.rectangle(frame, (x - symbol_size, y - symbol_size),
                         (x + symbol_size, y + symbol_size),
                         (50, 150, 200), -1, lineType=cv2.LINE_AA)
            cv2.rectangle(frame, (x - symbol_size, y - symbol_size),
                         (x + symbol_size, y + symbol_size),
                         (100, 180, 220), 2, lineType=cv2.LINE_AA)

        # Middle ring
        mid_radius = 250
        for ring_idx in range(3):
            radius = mid_radius - ring_idx * 40
            thickness = 8 + int(avg_magnitude * 12)

            # Golden/stone color
            hue = 15 + int(avg_magnitude * 15)
            saturation = 180 + int(avg_magnitude * 75)
            value = 150 + int(avg_magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            color = tuple(int(c) for c in color_bgr)

            cv2.circle(frame, (self.center_x, self.center_y), radius,
                      color, thickness, lineType=cv2.LINE_AA)

        # Center sun face
        face_radius = 80 + int(avg_magnitude * 40)
        cv2.circle(frame, (self.center_x, self.center_y), face_radius,
                  (100, 180, 220), -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, (self.center_x, self.center_y), face_radius,
                  (150, 200, 240), 3, lineType=cv2.LINE_AA)

        # Sun rays
        num_rays = 12
        for ray in range(num_rays):
            angle = np.deg2rad(ray * (360 / num_rays) + self.aztec_rotation * 0.5)
            inner_r = face_radius + 10
            outer_r = face_radius + 60 + int(avg_magnitude * 40)

            x1 = int(self.center_x + np.cos(angle) * inner_r)
            y1 = int(self.center_y + np.sin(angle) * inner_r)
            x2 = int(self.center_x + np.cos(angle) * outer_r)
            y2 = int(self.center_y + np.sin(angle) * outer_r)

            cv2.line(frame, (x1, y1), (x2, y2), (120, 190, 230), 6, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_44_fiber_optics(self, frame, magnitudes):
        """Mode 44: Light traveling through fiber cables"""
        # Create fiber optic cables
        num_fibers = 12

        for fiber_idx in range(num_fibers):
            mag_idx = fiber_idx % len(magnitudes)
            magnitude = magnitudes[mag_idx]

            # Fiber path (curved)
            points = []
            y = (fiber_idx + 1) / (num_fibers + 1) * self.height

            for x in range(0, self.width, 15):
                curve = np.sin(x * 0.005 + fiber_idx) * 80
                points.append([x, int(y + curve)])

            if len(points) > 1:
                points = np.array(points, dtype=np.int32)

                # Draw fiber cable (dark)
                cv2.polylines(frame, [points], False, (40, 40, 40), 8, lineType=cv2.LINE_AA)

                # Light pulse traveling through
                if magnitude > 0.3:
                    pulse_position = (self.frame_counter * 30 + fiber_idx * 100) % self.width
                    pulse_idx = min(int(pulse_position / 15), len(points) - 1)

                    # Fiber color
                    hue = (fiber_idx * 30) % 180
                    saturation = 255
                    value = 200 + int(magnitude * 55)
                    color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                    color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                    color = tuple(int(c) for c in color_bgr)

                    # Draw light pulse
                    pulse_length = int(10 + magnitude * 30)
                    for i in range(max(0, pulse_idx - pulse_length), min(len(points), pulse_idx + pulse_length)):
                        distance = abs(i - pulse_idx)
                        pulse_alpha = 1.0 - (distance / pulse_length)

                        pulse_color = tuple(int(c * pulse_alpha) for c in color)
                        cv2.circle(frame, tuple(points[i]), 6, pulse_color, -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_45_tornado_funnel(self, frame, magnitudes):
        """Mode 45: Swirling debris in tornado vortex"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn debris
        if self.frame_counter % 2 == 0:
            for i in range(int(avg_magnitude * 40 + 20)):
                self.tornado_debris.append({
                    'x': self.center_x + np.random.randint(-100, 100),
                    'y': self.height,
                    'angle': np.random.random() * 2 * np.pi,
                    'height': 0,
                    'rotation_speed': np.random.uniform(0.1, 0.3),
                    'radius': 50 + np.random.random() * 200,
                    'life': 1.0,
                    'size': 3 + int(np.random.random() * 8)
                })

        # Update debris
        new_debris = []
        for debris in self.tornado_debris:
            debris['angle'] += debris['rotation_speed'] + avg_magnitude * 0.1
            debris['height'] += 4 + avg_magnitude * 6
            debris['radius'] *= 0.99  # Spiral inward
            debris['life'] -= 0.008

            # Calculate position in tornado spiral
            spiral_progress = debris['height'] / self.height
            current_radius = debris['radius'] * (1 - spiral_progress * 0.7)

            x = int(self.center_x + np.cos(debris['angle']) * current_radius)
            y = int(self.height - debris['height'])

            if debris['life'] > 0 and y > 0:
                alpha = debris['life']

                # Debris color (browns, grays)
                debris_colors = [(80, 90, 100), (60, 80, 90), (100, 110, 120)]
                color = debris_colors[int(debris['angle'] * 3) % len(debris_colors)]
                debris_color = tuple(int(c * alpha) for c in color)

                cv2.circle(frame, (x, y), debris['size'], debris_color, -1, lineType=cv2.LINE_AA)

                new_debris.append(debris)

        self.tornado_debris = new_debris

        # Draw tornado funnel outline
        funnel_points = []
        for h in range(0, self.height, 20):
            progress = h / self.height
            radius = 50 + progress * 300
            angle1 = self.frame_counter * 0.05 + progress * 2

            x1 = int(self.center_x + np.cos(angle1) * radius)
            y1 = self.height - h

            funnel_points.append([x1, y1])

        if len(funnel_points) > 1:
            funnel_points = np.array(funnel_points, dtype=np.int32)
            cv2.polylines(frame, [funnel_points], False, (80, 80, 80), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_46_hologram_glitch(self, frame, magnitudes):
        """Mode 46: Futuristic holographic projection errors"""
        avg_magnitude = np.mean(magnitudes)

        # Draw holographic grid
        grid_spacing = 50
        for x in range(0, self.width, grid_spacing):
            for y in range(0, self.height, grid_spacing):
                # Glitch offset based on magnitude
                if avg_magnitude > 0.5 and np.random.random() < avg_magnitude * 0.3:
                    offset_x = np.random.randint(-20, 20)
                    offset_y = np.random.randint(-20, 20)
                else:
                    offset_x = offset_y = 0

                cv2.circle(frame, (x + offset_x, y + offset_y), 2,
                          (0, 200, 255), -1, lineType=cv2.LINE_AA)

        # Holographic frequency bars that glitch
        num_bars = min(len(magnitudes), 40)
        for i in range(num_bars):
            magnitude = magnitudes[i]
            x = int((i / num_bars) * self.width)
            bar_height = int(magnitude * self.height * 0.6)

            # Random glitch displacement
            if avg_magnitude > 0.6 and np.random.random() < 0.2:
                glitch_offset = np.random.randint(-30, 30)
                rgb_split = 15
            else:
                glitch_offset = 0
                rgb_split = 0

            # RGB channel separation (glitch effect)
            # Red channel
            cv2.rectangle(frame, (x - rgb_split + glitch_offset, self.height - bar_height),
                         (x + 3 - rgb_split + glitch_offset, self.height),
                         (0, 0, 255), -1, lineType=cv2.LINE_AA)
            # Cyan channel
            cv2.rectangle(frame, (x + rgb_split + glitch_offset, self.height - bar_height),
                         (x + 3 + rgb_split + glitch_offset, self.height),
                         (255, 255, 0), -1, lineType=cv2.LINE_AA)
            # Green (main)
            cv2.rectangle(frame, (x + glitch_offset, self.height - bar_height),
                         (x + 3 + glitch_offset, self.height),
                         (0, 255, 0), -1, lineType=cv2.LINE_AA)

        # Scanlines
        for y in range(0, self.height, 4):
            cv2.line(frame, (0, y), (self.width, y), (0, 50, 50), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_47_starfield_warp(self, frame, magnitudes):
        """Mode 47: Stars streaking during hyperspace jump"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn stars
        if len(self.stars) < 200:
            for i in range(5):
                self.stars.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'z': np.random.uniform(0.1, 1.0),
                    'trail': []
                })

        # Update stars
        warp_speed = 5 + avg_magnitude * 20

        new_stars = []
        for star in self.stars:
            # Calculate position from center
            dx = star['x'] - self.center_x
            dy = star['y'] - self.center_y

            # Move away from center (warp effect)
            distance = np.sqrt(dx**2 + dy**2) + 1
            angle = np.arctan2(dy, dx)

            star['x'] += np.cos(angle) * warp_speed / star['z']
            star['y'] += np.sin(angle) * warp_speed / star['z']

            # Add to trail
            star['trail'].append((int(star['x']), int(star['y'])))
            if len(star['trail']) > int(15 / star['z']):
                star['trail'].pop(0)

            # Reset if off screen
            if star['x'] < -100 or star['x'] > self.width + 100 or star['y'] < -100 or star['y'] > self.height + 100:
                star['x'] = self.center_x + np.random.randint(-50, 50)
                star['y'] = self.center_y + np.random.randint(-50, 50)
                star['z'] = np.random.uniform(0.1, 1.0)
                star['trail'] = []
            else:
                # Draw star trail (motion blur)
                if len(star['trail']) > 1:
                    for trail_idx in range(len(star['trail']) - 1):
                        p1 = star['trail'][trail_idx]
                        p2 = star['trail'][trail_idx + 1]
                        trail_alpha = trail_idx / len(star['trail'])

                        # Star brightness based on depth
                        brightness = int(200 * (1 - star['z']) * trail_alpha)
                        color = (brightness, brightness, brightness + 55)

                        cv2.line(frame, p1, p2, color, max(1, int(3 / star['z'])), lineType=cv2.LINE_AA)

                # Draw star
                star_size = max(1, int(4 / star['z']))
                cv2.circle(frame, (int(star['x']), int(star['y'])),
                          star_size, (255, 255, 255), -1, lineType=cv2.LINE_AA)

                new_stars.append(star)

        self.stars = new_stars
        return frame

    def draw_mode_48_mandala_growth(self, frame, magnitudes):
        """Mode 48: Sacred geometry mandala forming"""
        avg_magnitude = np.mean(magnitudes)

        # Draw mandala layers from center outward
        num_layers = 10

        for layer_idx in range(num_layers):
            layer_progress = layer_idx / num_layers
            base_radius = 50 + layer_idx * 35

            # Radius varies with music
            layer_mag = magnitudes[layer_idx % len(magnitudes)]
            radius = base_radius + layer_mag * 50

            # Number of petals/elements increases with layer
            num_elements = 6 + layer_idx * 2

            for elem_idx in range(num_elements):
                angle = (elem_idx / num_elements) * 2 * np.pi + self.frame_counter * 0.01 * (layer_idx % 2 * 2 - 1)

                # Petal position
                x = int(self.center_x + np.cos(angle) * radius)
                y = int(self.center_y + np.sin(angle) * radius)

                # Petal size
                petal_size = int(10 + layer_mag * 25)

                # Sacred geometry colors (purples, golds, cyans)
                hue = int((layer_idx * 20 + elem_idx * 10 + self.frame_counter * 0.5) % 180)
                saturation = 200 + int(layer_mag * 55)
                value = 150 + int(layer_mag * 105)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c) for c in color_bgr)

                # Draw petal/element
                cv2.circle(frame, (x, y), petal_size, color, -1, lineType=cv2.LINE_AA)
                cv2.circle(frame, (x, y), petal_size + 2,
                          tuple(int(c * 1.3) for c in color), 1, lineType=cv2.LINE_AA)

                # Connect to center with lines
                if layer_idx % 2 == 0:
                    cv2.line(frame, (self.center_x, self.center_y), (x, y),
                            tuple(int(c * 0.3) for c in color), 1, lineType=cv2.LINE_AA)

        # Central dot
        cv2.circle(frame, (self.center_x, self.center_y),
                  15 + int(avg_magnitude * 20), (255, 255, 255), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_49_neon_sign_flicker(self, frame, magnitudes):
        """Mode 49: Vintage neon signs buzzing on/off"""
        avg_magnitude = np.mean(magnitudes)

        # Draw neon text that flickers
        signs = [
            {'text': 'AUDIO', 'y': 200, 'hue': 0},
            {'text': 'SPECTRUM', 'y': 350, 'hue': 120},
            {'text': 'LIVE', 'y': 500, 'hue': 160},
            {'text': 'MUSIC', 'y': 650, 'hue': 30}
        ]

        for sign_idx, sign in enumerate(signs):
            mag_idx = sign_idx % len(magnitudes)
            magnitude = magnitudes[mag_idx]

            # Flicker effect
            if magnitude > 0.7:
                flicker = 1.0
            elif np.random.random() < 0.1:
                flicker = np.random.uniform(0.3, 1.0)
            else:
                flicker = 0.8 + magnitude * 0.2

            if flicker > 0.2:
                # Neon color
                saturation = 255
                value = int(200 * flicker + magnitude * 55)
                color_hsv = np.array([[[sign['hue'], saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * flicker) for c in color_bgr)

                # Calculate text position (centered)
                text_size = cv2.getTextSize(sign['text'], cv2.FONT_HERSHEY_DUPLEX, 3, 8)[0]
                text_x = (self.width - text_size[0]) // 2

                # Draw glow layers
                for glow in range(5, 0, -1):
                    glow_color = tuple(int(c * 0.2 * flicker / glow) for c in color)
                    cv2.putText(frame, sign['text'], (text_x, sign['y']),
                              cv2.FONT_HERSHEY_DUPLEX, 3, glow_color, 8 + glow * 2, cv2.LINE_AA)

                # Main text
                cv2.putText(frame, sign['text'], (text_x, sign['y']),
                          cv2.FONT_HERSHEY_DUPLEX, 3, color, 8, cv2.LINE_AA)

        return frame

    def draw_mode_50_black_hole(self, frame, magnitudes):
        """Mode 50: Event horizon with gravitational lensing"""
        avg_magnitude = np.mean(magnitudes)

        # Spawn particles around black hole
        if self.frame_counter % 2 == 0:
            for i in range(int(avg_magnitude * 30 + 15)):
                angle = np.random.random() * 2 * np.pi
                distance = 400 + np.random.random() * 200

                self.black_hole_particles.append({
                    'x': self.center_x + np.cos(angle) * distance,
                    'y': self.center_y + np.sin(angle) * distance,
                    'vx': 0,
                    'vy': 0,
                    'life': 1.0,
                    'hue': int(np.random.random() * 180)
                })

        # Update particles (gravitational pull)
        event_horizon_radius = 50 + avg_magnitude * 30

        new_particles = []
        for particle in self.black_hole_particles:
            # Calculate gravity
            dx = self.center_x - particle['x']
            dy = self.center_y - particle['y']
            distance = np.sqrt(dx**2 + dy**2) + 1

            # Strong gravity near event horizon
            gravity_force = 5000 / (distance ** 2)

            particle['vx'] += (dx / distance) * gravity_force
            particle['vy'] += (dy / distance) * gravity_force

            # Orbital velocity (tangential)
            orbital_angle = np.arctan2(dy, dx) + np.pi / 2
            orbital_speed = 50 / distance
            particle['vx'] += np.cos(orbital_angle) * orbital_speed
            particle['vy'] += np.sin(orbital_angle) * orbital_speed

            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.005

            # Check if not consumed by black hole
            if distance > event_horizon_radius and particle['life'] > 0:
                alpha = min(1.0, particle['life'])

                # Redshift effect (particles shift red near event horizon)
                proximity = 1.0 - (distance / 600)
                hue_shift = int(proximity * 30)
                final_hue = (particle['hue'] - hue_shift) % 180

                saturation = 220 + int(proximity * 35)
                value = 150 + int(proximity * 105)
                color_hsv = np.array([[[final_hue, saturation, value]]], dtype=np.uint8)
                color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                color = tuple(int(c * alpha) for c in color_bgr)

                # Size based on distance (gravitational lensing)
                particle_size = max(2, int(8 / (distance / 100)))

                cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                          particle_size, color, -1, lineType=cv2.LINE_AA)

                # Accretion disk glow
                if distance < 200:
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                              particle_size + 3,
                              tuple(int(c * 0.4) for c in color), 1, lineType=cv2.LINE_AA)

                new_particles.append(particle)

        self.black_hole_particles = new_particles

        # Draw event horizon (black circle)
        cv2.circle(frame, (self.center_x, self.center_y),
                  int(event_horizon_radius), (0, 0, 0), -1, lineType=cv2.LINE_AA)

        # Event horizon glow
        for glow in range(4, 0, -1):
            glow_color = (int(20 / glow), int(10 / glow), int(30 / glow))
            cv2.circle(frame, (self.center_x, self.center_y),
                      int(event_horizon_radius) + glow * 8,
                      glow_color, 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_51_fractal_tree(self, frame, magnitudes):
        """Mode 51: Generative tree that grows - branches on bass, blooms on treble"""
        avg_magnitude = np.mean(magnitudes)
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Main trunk sway
        trunk_sway = int(np.sin(self.frame_counter * 0.1 + avg_magnitude) * 20)
        trunk_base = (self.center_x + trunk_sway, self.height - 50)
        trunk_top = (self.center_x + trunk_sway, self.center_y)

        # Draw main trunk with thickness based on volume
        trunk_thickness = int(10 + avg_magnitude * 15)
        cv2.line(frame, trunk_base, trunk_top, (40, 80, 40), trunk_thickness, lineType=cv2.LINE_AA)

        # Spawn branches on bass hits
        if bass > 0.3 and self.frame_counter % 8 == 0:
            angle = -np.pi/2 + (np.random.random() - 0.5) * np.pi/3
            self.fractal_tree_branches.append({
                'x': trunk_top[0], 'y': trunk_top[1],
                'angle': angle, 'length': 40 + bass * 60,
                'thickness': int(3 + bass * 8), 'generation': 0, 'life': 1.0
            })

        # Draw and update branches
        new_branches = []
        for branch in self.fractal_tree_branches:
            if branch['life'] > 0:
                end_x = int(branch['x'] + np.cos(branch['angle']) * branch['length'])
                end_y = int(branch['y'] + np.sin(branch['angle']) * branch['length'])

                alpha = branch['life']
                color = (int(50 * alpha), int(100 * alpha), int(50 * alpha))
                cv2.line(frame, (int(branch['x']), int(branch['y'])), (end_x, end_y),
                        color, branch['thickness'], lineType=cv2.LINE_AA)

                # Bloom flowers on treble
                if treble > 0.4 and branch['generation'] > 0:
                    bloom_size = int(3 + treble * 10)
                    bloom_color_hsv = np.array([[[int(treble * 180), 255, 255]]], dtype=np.uint8)
                    bloom_color = cv2.cvtColor(bloom_color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                    cv2.circle(frame, (end_x, end_y), bloom_size, tuple(map(int, bloom_color * alpha)), -1, lineType=cv2.LINE_AA)

                branch['life'] -= 0.003
                new_branches.append(branch)

        self.fractal_tree_branches = new_branches[:100]  # Limit
        return frame

    def draw_mode_52_cityscape_extrusion(self, frame, magnitudes):
        """Mode 52: 3D city blocks that extrude with frequency amplitude"""
        num_blocks = min(len(magnitudes), 40)
        block_width = self.width // num_blocks

        for i in range(num_blocks):
            magnitude = magnitudes[i] if i < len(magnitudes) else 0
            building_height = int(magnitude * self.height * 0.7)

            # 3D perspective
            base_y = self.height - 100
            top_y = base_y - building_height
            x_left = i * block_width + 5
            x_right = (i + 1) * block_width - 5

            # Building color based on beat
            hue = int((i / num_blocks) * 180)
            saturation = 180 + int(magnitude * 75)
            value = 100 + int(magnitude * 155)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw building
            cv2.rectangle(frame, (x_left, base_y), (x_right, top_y), tuple(map(int, color)), -1)

            # Emissive windows
            if magnitude > 0.3:
                num_windows = max(2, int(building_height / 30))
                for w in range(num_windows):
                    window_y = base_y - int((w + 0.5) * building_height / num_windows)
                    window_x = (x_left + x_right) // 2
                    window_brightness = int(255 * magnitude)
                    cv2.circle(frame, (window_x, window_y), 3, (window_brightness, window_brightness, 200), -1)

        return frame

    def draw_mode_53_gravity_well(self, frame, magnitudes):
        """Mode 53: Particles pulled toward pulsing bass center, pushed by treble shockwaves"""
        avg_magnitude = np.mean(magnitudes)
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Spawn particles at edges
        if self.frame_counter % 2 == 0:
            for _ in range(int(treble * 20 + 5)):
                angle = np.random.random() * 2 * np.pi
                edge_dist = min(self.width, self.height) // 2
                self.gravity_well_particles.append({
                    'x': self.center_x + np.cos(angle) * edge_dist,
                    'y': self.center_y + np.sin(angle) * edge_dist,
                    'vx': 0, 'vy': 0, 'hue': int(treble * 180)
                })

        # Black hole pulses with bass
        well_radius = int(30 + bass * 50)
        cv2.circle(frame, (self.center_x, self.center_y), well_radius, (255, 255, 255), -1, lineType=cv2.LINE_AA)

        # Bass shockwave push
        shockwave_force = bass * 500 if bass > 0.6 else 0

        new_particles = []
        for p in self.gravity_well_particles:
            dx = self.center_x - p['x']
            dy = self.center_y - p['y']
            dist = np.sqrt(dx**2 + dy**2) + 1

            # Gravitational pull
            pull_force = 200 / (dist**2)
            p['vx'] += (dx / dist) * pull_force
            p['vy'] += (dy / dist) * pull_force

            # Shockwave push
            if shockwave_force > 0 and dist < 200:
                p['vx'] -= (dx / dist) * shockwave_force
                p['vy'] -= (dy / dist) * shockwave_force

            p['x'] += p['vx']
            p['y'] += p['vy']

            if dist > well_radius and 0 < p['x'] < self.width and 0 < p['y'] < self.height:
                color_hsv = np.array([[[p['hue'], 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                cv2.circle(frame, (int(p['x']), int(p['y'])), 3, tuple(map(int, color)), -1)
                new_particles.append(p)

        self.gravity_well_particles = new_particles[:500]
        return frame

    def draw_mode_54_metaball_fluid(self, frame, magnitudes):
        """Mode 54: Lava lamp metaballs - size pulses with frequency amplitude"""
        num_balls = min(len(magnitudes), 15)

        # Update or create metaballs
        while len(self.metaballs) < num_balls:
            self.metaballs.append({
                'x': np.random.random() * self.width,
                'y': np.random.random() * self.height,
                'vx': (np.random.random() - 0.5) * 4,
                'vy': (np.random.random() - 0.5) * 4,
                'base_radius': 40 + np.random.random() * 40
            })

        avg_magnitude = np.mean(magnitudes)

        # Draw metaballs with glow
        for i, ball in enumerate(self.metaballs[:num_balls]):
            magnitude = magnitudes[i] if i < len(magnitudes) else avg_magnitude
            radius = int(ball['base_radius'] * (0.7 + magnitude * 0.8))

            # Update position with fluid-like motion
            ball['x'] += ball['vx']
            ball['y'] += ball['vy']

            # Bounce off walls
            if ball['x'] < radius or ball['x'] > self.width - radius:
                ball['vx'] *= -1
            if ball['y'] < radius or ball['y'] > self.height - radius:
                ball['vy'] *= -1

            # Color based on frequency
            hue = int((i / num_balls) * 180)
            saturation = 200 + int(magnitude * 55)
            value = 150 + int(magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw with gradient
            for r in range(radius, 0, -5):
                alpha = r / radius
                cv2.circle(frame, (int(ball['x']), int(ball['y'])), r,
                          tuple(int(c * alpha) for c in color), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_55_aurora_borealis(self, frame, magnitudes):
        """Mode 55: Northern lights curtains - low freq shapes, high freq shimmer"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        num_curtains = 5
        curtain_points = 60

        for curtain_idx in range(num_curtains):
            points = []
            base_y_offset = curtain_idx * 80 - 160

            for i in range(curtain_points):
                x = int((i / curtain_points) * self.width)
                # Low frequency controls main shape
                wave1 = np.sin(i * 0.15 + self.frame_counter * 0.05 + curtain_idx) * bass * 60
                wave2 = np.sin(i * 0.08 + self.frame_counter * 0.03) * bass * 40
                y = int(self.center_y + base_y_offset + wave1 + wave2)

                # High frequency shimmer
                shimmer = np.sin(i * 0.8 + self.frame_counter * 0.4) * treble * 20
                y += int(shimmer)

                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            # Aurora color (greenish with variation)
            hue = 60 + curtain_idx * 15
            saturation = 180 + int(treble * 75)
            value = 120 + int(bass * 135)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw curtain with thickness
            if len(points) > 1:
                cv2.polylines(frame, [points], False, tuple(map(int, color)), 3, lineType=cv2.LINE_AA)
                # Add glow
                cv2.polylines(frame, [points], False, tuple(int(c * 0.5) for c in color), 8, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_56_stained_glass(self, frame, magnitudes):
        """Mode 56: Stained glass window panes that glow with frequency"""
        rows, cols = 6, 10
        pane_width = self.width // cols
        pane_height = self.height // rows

        pane_idx = 0
        for row in range(rows):
            for col in range(cols):
                if pane_idx >= len(magnitudes):
                    break

                magnitude = magnitudes[pane_idx]

                x1 = col * pane_width + 2
                y1 = row * pane_height + 2
                x2 = (col + 1) * pane_width - 2
                y2 = (row + 1) * pane_height - 2

                # Stained glass color
                hue = int((pane_idx / len(magnitudes)) * 180)
                saturation = 255
                value = int(80 + magnitude * 175)  # Glow intensity
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                # Draw pane
                cv2.rectangle(frame, (x1, y1), (x2, y2), tuple(map(int, color)), -1)

                # Add glow effect
                if magnitude > 0.5:
                    glow_thickness = int(magnitude * 10)
                    glow_color = tuple(int(c * 1.2) for c in color)
                    cv2.rectangle(frame, (x1-glow_thickness, y1-glow_thickness),
                                (x2+glow_thickness, y2+glow_thickness), glow_color, glow_thickness, lineType=cv2.LINE_AA)

                pane_idx += 1

        return frame

    def draw_mode_57_neon_nerve_network(self, frame, magnitudes):
        """Mode 57: Neural network with pulsing nodes and synapse firings"""
        # Initialize nerve nodes if empty
        if len(self.nerve_nodes) == 0:
            num_nodes = 20
            for _ in range(num_nodes):
                self.nerve_nodes.append({
                    'x': np.random.randint(100, self.width - 100),
                    'y': np.random.randint(100, self.height - 100),
                    'pulse': 0, 'connections': []
                })
            # Create connections
            for i, node in enumerate(self.nerve_nodes):
                num_connections = np.random.randint(2, 5)
                for _ in range(num_connections):
                    target = np.random.randint(0, len(self.nerve_nodes))
                    if target != i:
                        node['connections'].append(target)

        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Update node pulses with bass
        for i, node in enumerate(self.nerve_nodes):
            if i < len(magnitudes):
                node['pulse'] = magnitudes[i]

        # Draw connections (synapses)
        for i, node in enumerate(self.nerve_nodes):
            for target_idx in node['connections']:
                target = self.nerve_nodes[target_idx]

                # Synapse fires with treble
                if treble > 0.5:
                    alpha = treble
                    color = (int(100 * alpha), int(200 * alpha), int(255 * alpha))
                    cv2.line(frame, (node['x'], node['y']), (target['x'], target['y']),
                            color, 2, lineType=cv2.LINE_AA)

        # Draw nodes
        for node in self.nerve_nodes:
            pulse_radius = int(10 + node['pulse'] * 25)
            cv2.circle(frame, (node['x'], node['y']), pulse_radius, (100, 255, 255), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (node['x'], node['y']), pulse_radius + 5, (50, 150, 200), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_58_glitch_artifact(self, frame, magnitudes):
        """Mode 58: Clean bars corrupted by glitch effects on transients"""
        avg_magnitude = np.mean(magnitudes)
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Draw clean bars first
        bar_width = self.width // len(magnitudes)
        for i, magnitude in enumerate(magnitudes):
            bar_height = int(magnitude * self.height * 0.7)
            x = i * bar_width
            y = self.height - bar_height

            color = (100, 200, 255)
            cv2.rectangle(frame, (x, y), (x + bar_width - 2, self.height), color, -1)

        # Apply glitch effects on strong transients
        if treble > 0.7:
            glitch_intensity = int((treble - 0.7) * 10)

            # Pixel sorting effect
            for _ in range(glitch_intensity):
                y_slice = np.random.randint(0, self.height - 50)
                slice_height = np.random.randint(10, 50)
                row = frame[y_slice:y_slice + slice_height, :]
                sorted_row = np.sort(row.view('i8'), axis=1).view(row.dtype)
                frame[y_slice:y_slice + slice_height, :] = sorted_row

            # Chromatic aberration
            shift = int(treble * 20)
            frame[:, :, 2] = np.roll(frame[:, :, 2], shift, axis=1)  # Red channel
            frame[:, :, 0] = np.roll(frame[:, :, 0], -shift, axis=1)  # Blue channel

        return frame

    def draw_mode_59_warp_tunnel(self, frame, magnitudes):
        """Mode 59: Hyperspace tunnel of rings - radius pulses with frequency"""
        avg_magnitude = np.mean(magnitudes)
        num_rings = 30

        for i in range(num_rings):
            depth = i / num_rings
            scale = 1 - depth * 0.9

            # Ring frequency index
            freq_idx = int(depth * len(magnitudes))
            if freq_idx >= len(magnitudes):
                freq_idx = len(magnitudes) - 1

            magnitude = magnitudes[freq_idx]
            radius = int(self.max_radius * scale * (0.5 + magnitude * 0.8))

            # Color based on depth and frequency
            hue = int((depth + self.frame_counter * 0.01) * 180) % 180
            saturation = 200 + int(magnitude * 55)
            value = int(150 * (1 - depth) + magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw ring
            thickness = int(2 + magnitude * 8)
            cv2.circle(frame, (self.center_x, self.center_y), radius, tuple(map(int, color)), thickness, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_60_conway_life(self, frame, magnitudes):
        """Mode 60: Conway's Game of Life modulated by audio"""
        grid_size = 40
        cell_width = self.width // grid_size
        cell_height = self.height // grid_size

        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize grid
        if len(self.cellular_automaton) == 0:
            self.cellular_automaton = np.random.randint(0, 2, (grid_size, grid_size))

        # Audio modulates birth/survival - low freq spawns, high freq increases survival
        if self.frame_counter % 3 == 0:
            new_grid = self.cellular_automaton.copy()

            for y in range(grid_size):
                for x in range(grid_size):
                    # Count neighbors
                    neighbors = 0
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            if dy == 0 and dx == 0:
                                continue
                            ny, nx = (y + dy) % grid_size, (x + dx) % grid_size
                            neighbors += self.cellular_automaton[ny, nx]

                    # Modified rules based on audio
                    if self.cellular_automaton[y, x] == 1:
                        # Survival: 2-3 neighbors (+ treble increases tolerance)
                        if neighbors < 2 - int(treble) or neighbors > 3 + int(treble * 2):
                            new_grid[y, x] = 0
                    else:
                        # Birth: 3 neighbors (bass spawns new cells randomly)
                        if neighbors == 3 or (bass > 0.6 and np.random.random() < bass * 0.1):
                            new_grid[y, x] = 1

            self.cellular_automaton = new_grid

        # Draw grid
        for y in range(grid_size):
            for x in range(grid_size):
                if self.cellular_automaton[y, x] == 1:
                    x1 = x * cell_width
                    y1 = y * cell_height
                    color = (100, 255, 100)
                    cv2.rectangle(frame, (x1, y1), (x1 + cell_width - 1, y1 + cell_height - 1), color, -1)

        return frame

    def draw_mode_61_ascii_art(self, frame, magnitudes):
        """Mode 61: ASCII art bars using text characters"""
        # Create text representation
        chars = ['.', '-', '=', '+', '*', '#', '@']
        bar_width = self.width // len(magnitudes)

        for i, magnitude in enumerate(magnitudes):
            bar_height = int(magnitude * 20)  # Number of chars high
            char_idx = min(int(magnitude * len(chars)), len(chars) - 1)
            char = chars[char_idx]

            # Draw vertical bar of characters
            x = int(i * bar_width + bar_width // 2)
            for row in range(bar_height):
                y = self.height - row * 30 - 30
                if y > 0:
                    brightness = int(200 + magnitude * 55)
                    cv2.putText(frame, char, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                              (brightness, brightness, brightness), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_62_rippling_water(self, frame, magnitudes):
        """Mode 62: Water surface with ripples from frequency raindrop sources"""
        # Each frequency acts as a ripple source
        for i, magnitude in enumerate(magnitudes):
            if magnitude > 0.4:
                # Source position along top
                x = int((i / len(magnitudes)) * self.width)
                y = int(self.height * 0.3)

                # Create ripple
                ripple_radius = int((self.frame_counter % 60) * magnitude * 8)
                alpha = 1.0 - (ripple_radius / 300)

                if alpha > 0:
                    color = (int(100 * alpha), int(150 * alpha), int(255 * alpha))
                    cv2.circle(frame, (x, y), ripple_radius, color, 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_63_terrain_flyover(self, frame, magnitudes):
        """Mode 63: 3D wireframe terrain generated from waveform"""
        # Generate terrain heightmap from audio
        terrain_width = 50
        terrain_depth = 30

        # Use magnitudes to create terrain
        terrain = np.zeros((terrain_depth, terrain_width))
        for x in range(terrain_width):
            freq_idx = int((x / terrain_width) * len(magnitudes))
            terrain[:, x] = magnitudes[freq_idx] * 200

        # Draw 3D wireframe terrain
        scale = 15
        offset_x = self.width // 2
        offset_y = self.height - 200

        for z in range(terrain_depth - 1):
            for x in range(terrain_width - 1):
                # Current point
                x1 = int(offset_x + (x - terrain_width // 2) * scale)
                y1 = int(offset_y - terrain[z, x] - z * 10)

                # Next points
                x2 = int(offset_x + (x + 1 - terrain_width // 2) * scale)
                y2 = int(offset_y - terrain[z, x + 1] - z * 10)

                x3 = int(offset_x + (x - terrain_width // 2) * scale)
                y3 = int(offset_y - terrain[z + 1, x] - (z + 1) * 10)

                # Draw lines
                depth_factor = 1 - z / terrain_depth
                color = (int(100 * depth_factor), int(200 * depth_factor), int(100 * depth_factor))
                cv2.line(frame, (x1, y1), (x2, y2), color, 1, lineType=cv2.LINE_AA)
                cv2.line(frame, (x1, y1), (x3, y3), color, 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_64_string_art(self, frame, magnitudes):
        """Mode 64: Points on circle with lines between - modulated by frequencies"""
        num_points = min(len(magnitudes), 36)
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Calculate point positions (modulated by low freq)
        points = []
        for i in range(num_points):
            angle = (i / num_points) * 2 * np.pi
            magnitude = magnitudes[i] if i < len(magnitudes) else 0
            radius = int(self.max_radius * 0.8 * (1 + bass * 0.3))

            # Position modulation
            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)
            points.append((x, y))

        # Draw lines between points (mids and treble control count and color)
        num_lines = int(mids * 50 + treble * 100)
        for _ in range(num_lines):
            idx1 = np.random.randint(0, len(points))
            idx2 = np.random.randint(0, len(points))

            if idx1 != idx2:
                hue = int(treble * 180)
                alpha = 0.3
                color_hsv = np.array([[[hue, 200, int(255 * alpha)]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                cv2.line(frame, points[idx1], points[idx2], tuple(map(int, color)), 1, lineType=cv2.LINE_AA)

        # Draw points
        for point in points:
            cv2.circle(frame, point, 4, (255, 255, 255), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_65_fire_embers(self, frame, magnitudes):
        """Mode 65: Central fire with sparks flying on treble hits"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Central fire (low-mid frequencies)
        fire_height = int(bass * 300 + 100)
        fire_width = 150

        for i in range(20):
            flame_x = int(self.center_x + (np.random.random() - 0.5) * fire_width)
            flame_y = int(self.height - 100 - np.random.random() * fire_height)
            flame_size = int(20 + bass * 30)

            # Fire color gradient
            hue = int(10 + np.random.random() * 20)  # Orange-yellow
            saturation = 255
            value = 200 + int(np.random.random() * 55)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (flame_x, flame_y), flame_size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        # Emit sparks/embers on treble hits
        if treble > 0.5:
            for _ in range(int(treble * 30)):
                self.ember_particles.append({
                    'x': self.center_x + (np.random.random() - 0.5) * 100,
                    'y': self.height - 150,
                    'vx': (np.random.random() - 0.5) * 8,
                    'vy': -np.random.random() * 15 - 5,
                    'life': 1.0
                })

        # Update and draw embers
        new_embers = []
        for ember in self.ember_particles:
            ember['x'] += ember['vx']
            ember['y'] += ember['vy']
            ember['vy'] += 0.5  # Gravity
            ember['life'] -= 0.015

            if ember['life'] > 0 and ember['y'] < self.height:
                alpha = ember['life']
                color = (int(100 * alpha), int(150 * alpha), int(255 * alpha))
                cv2.circle(frame, (int(ember['x']), int(ember['y'])), 3, color, -1, lineType=cv2.LINE_AA)
                new_embers.append(ember)

        self.ember_particles = new_embers
        return frame

    def draw_mode_66_radial_kaleidoscope(self, frame, magnitudes):
        """Mode 66: Radial kaleidoscope with mirrored segments"""
        num_segments = 8
        avg_magnitude = np.mean(magnitudes)

        # Create one segment
        segment_angle = 2 * np.pi / num_segments

        # Draw particles in one segment
        for i, magnitude in enumerate(magnitudes[:30]):
            if magnitude > 0.2:
                angle = (i / 30) * segment_angle
                distance = 100 + magnitude * 300

                x = int(self.center_x + np.cos(angle) * distance)
                y = int(self.center_y + np.sin(angle) * distance)

                hue = int((i / 30) * 180)
                color_hsv = np.array([[[hue, 255, int(255 * magnitude)]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                # Draw in all mirrored segments
                for seg in range(num_segments):
                    seg_angle = seg * segment_angle + self.frame_counter * 0.02
                    rot_x = int(self.center_x + np.cos(angle + seg_angle) * distance)
                    rot_y = int(self.center_y + np.sin(angle + seg_angle) * distance)

                    size = int(5 + magnitude * 15)
                    cv2.circle(frame, (rot_x, rot_y), size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        # Pulsing zoom
        zoom = 1 + avg_magnitude * 0.3

        return frame

    def draw_mode_67_pulsing_jellyfish(self, frame, magnitudes):
        """Mode 67: Translucent jellyfish - bell pulses with bass, tentacles are waveforms"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        # Jellyfish bell (pulses with bass)
        bell_radius = int(80 + bass * 70)
        bell_y = self.center_y - 100

        # Draw semi-transparent bell
        overlay = frame.copy()
        cv2.ellipse(overlay, (self.center_x, bell_y), (bell_radius, int(bell_radius * 0.7)),
                   0, 0, 180, (150, 100, 255), -1, lineType=cv2.LINE_AA)
        cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)

        # Tentacles (waveforms for high frequencies)
        num_tentacles = 8
        for t in range(num_tentacles):
            tentacle_x_offset = (t - num_tentacles // 2) * 30
            points = []

            # Each tentacle reacts to a frequency band
            freq_start = t * len(magnitudes) // num_tentacles
            freq_end = (t + 1) * len(magnitudes) // num_tentacles
            tentacle_freqs = magnitudes[freq_start:freq_end]

            for i, magnitude in enumerate(tentacle_freqs):
                x = self.center_x + tentacle_x_offset + int(np.sin(i * 0.5 + self.frame_counter * 0.1) * 15)
                y = bell_y + bell_radius // 2 + i * 8 + int(magnitude * 50)
                points.append([x, y])

            if len(points) > 1:
                points_np = np.array(points, dtype=np.int32)
                cv2.polylines(frame, [points_np], False, (200, 150, 255), 3, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_68_orbital_system(self, frame, magnitudes):
        """Mode 68: Central sun with orbiting planets (mid-freq) and moons (treble)"""
        avg_magnitude = np.mean(magnitudes)
        mids = magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Central sun pulses
        sun_radius = int(40 + avg_magnitude * 40)
        cv2.circle(frame, (self.center_x, self.center_y), sun_radius, (100, 200, 255), -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, (self.center_x, self.center_y), sun_radius + 10, (150, 220, 255), 2, lineType=cv2.LINE_AA)

        # Planets orbit
        num_planets = min(len(mids), 6)
        for i in range(num_planets):
            magnitude = mids[i] if i < len(mids) else 0
            orbit_radius = 120 + i * 70
            angle = self.frame_counter * 0.02 * (1 + i * 0.3)

            planet_x = int(self.center_x + np.cos(angle) * orbit_radius)
            planet_y = int(self.center_y + np.sin(angle) * orbit_radius)
            planet_size = int(10 + magnitude * 25)

            # Planet color
            hue = int((i / num_planets) * 180)
            color_hsv = np.array([[[hue, 200, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (planet_x, planet_y), planet_size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

            # Moon orbits planet (treble)
            if treble > 0.4:
                moon_angle = self.frame_counter * 0.1
                moon_distance = planet_size + 20
                moon_x = int(planet_x + np.cos(moon_angle) * moon_distance)
                moon_y = int(planet_y + np.sin(moon_angle) * moon_distance)
                moon_size = int(3 + treble * 8)

                cv2.circle(frame, (moon_x, moon_y), moon_size, (200, 200, 200), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_69_spectrum_cube(self, frame, magnitudes):
        """Mode 69: Rotating 3D cube with different visualizers on each face"""
        self.cube_rotation += 0.02
        cube_size = 200

        # Simple 3D cube projection
        angle_x = self.cube_rotation
        angle_y = self.cube_rotation * 0.7

        # Cube vertices
        vertices_3d = [
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
        ]

        # Rotate and project
        vertices_2d = []
        for vx, vy, vz in vertices_3d:
            # Rotate around Y
            x = vx * np.cos(angle_y) - vz * np.sin(angle_y)
            z = vx * np.sin(angle_y) + vz * np.cos(angle_y)

            # Rotate around X
            y = vy * np.cos(angle_x) - z * np.sin(angle_x)
            z = vy * np.sin(angle_x) + z * np.cos(angle_x)

            # Project to 2D
            scale = cube_size / (3 + z)
            x2d = int(self.center_x + x * scale)
            y2d = int(self.center_y + y * scale)
            vertices_2d.append((x2d, y2d))

        # Draw cube edges
        edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
        for start, end in edges:
            color = (100, 200, 255)
            cv2.line(frame, vertices_2d[start], vertices_2d[end], color, 2, lineType=cv2.LINE_AA)

        # Draw bars on front face
        avg_magnitude = np.mean(magnitudes)
        face_center = ((vertices_2d[0][0] + vertices_2d[2][0]) // 2,
                      (vertices_2d[0][1] + vertices_2d[2][1]) // 2)
        bar_length = int(30 + avg_magnitude * 50)
        cv2.line(frame, face_center, (face_center[0], face_center[1] - bar_length), (255, 200, 100), 3)

        return frame

    def draw_mode_70_typographic_flow(self, frame, magnitudes):
        """Mode 70: Floating words with size based on bass, waviness on treble"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Spawn new words
        if self.frame_counter % 30 == 0:
            words = ['MUSIC', 'FLOW', 'VIBE', 'SOUND', 'WAVE', 'PULSE', 'RHYTHM']
            word = np.random.choice(words)
            font_scale = 1.0 + bass * 2.0

            self.typography_words.append({
                'word': word,
                'x': np.random.randint(100, self.width - 200),
                'y': self.height + 50,
                'vy': -2 - bass * 3,
                'font_scale': font_scale,
                'life': 1.0
            })

        # Update and draw words
        new_words = []
        for word_obj in self.typography_words:
            word_obj['y'] += word_obj['vy']
            word_obj['life'] -= 0.005

            if word_obj['life'] > 0 and word_obj['y'] > -100:
                # Waviness from treble
                wobble_x = int(np.sin(self.frame_counter * 0.1 + word_obj['y'] * 0.01) * treble * 30)
                x = int(word_obj['x'] + wobble_x)
                y = int(word_obj['y'])

                alpha = word_obj['life']
                color = (int(255 * alpha), int(200 * alpha), int(100 * alpha))

                cv2.putText(frame, word_obj['word'], (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                          word_obj['font_scale'], color, 3, lineType=cv2.LINE_AA)

                new_words.append(word_obj)

        self.typography_words = new_words[:20]
        return frame

    def draw_mode_71_sonar_ping(self, frame, magnitudes):
        """Mode 71: Circular radar sweep with frequency blips"""
        # Rotating sweep line
        sweep_angle = (self.frame_counter * 0.05) % (2 * np.pi)
        sweep_end_x = int(self.center_x + np.cos(sweep_angle) * self.max_radius)
        sweep_end_y = int(self.center_y + np.sin(sweep_angle) * self.max_radius)

        # Draw sweep line
        cv2.line(frame, (self.center_x, self.center_y), (sweep_end_x, sweep_end_y),
                (100, 255, 100), 2, lineType=cv2.LINE_AA)

        # Draw concentric circles (radar grid)
        for ring in range(1, 6):
            radius = int(self.max_radius * ring / 5)
            cv2.circle(frame, (self.center_x, self.center_y), radius, (50, 100, 50), 1, lineType=cv2.LINE_AA)

        # Frequency blips appear on radar
        for i, magnitude in enumerate(magnitudes):
            if magnitude > 0.4:
                # Radial distance based on frequency (low=center, high=edge)
                distance = int((i / len(magnitudes)) * self.max_radius)
                angle = sweep_angle + (np.random.random() - 0.5) * 0.5

                blip_x = int(self.center_x + np.cos(angle) * distance)
                blip_y = int(self.center_y + np.sin(angle) * distance)

                blip_size = int(3 + magnitude * 12)
                brightness = int(200 + magnitude * 55)
                cv2.circle(frame, (blip_x, blip_y), blip_size, (brightness, 255, brightness), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_72_vu_meters(self, frame, magnitudes):
        """Mode 72: Retro analog VU meters with needle physics"""
        # Split audio into Left/Right (use first and second half)
        left_magnitude = np.mean(magnitudes[:len(magnitudes)//2])
        right_magnitude = np.mean(magnitudes[len(magnitudes)//2:])

        # Smooth needle movement with physics
        target_left = -60 + left_magnitude * 120  # Angle in degrees
        target_right = -60 + right_magnitude * 120

        # Apply smoothing and overshoot
        self.vu_needle_positions[0] += (target_left - self.vu_needle_positions[0]) * 0.3
        self.vu_needle_positions[1] += (target_right - self.vu_needle_positions[1]) * 0.3

        # Draw VU meters
        meter_width = 300
        meter_height = 200

        for idx, (label, needle_angle) in enumerate(zip(['L', 'R'], self.vu_needle_positions)):
            center_x = self.width // 4 + idx * self.width // 2
            center_y = self.center_y

            # Draw meter face
            cv2.ellipse(frame, (center_x, center_y), (meter_width//2, meter_height//2),
                       0, 180, 360, (50, 50, 50), -1)
            cv2.ellipse(frame, (center_x, center_y), (meter_width//2, meter_height//2),
                       0, 180, 360, (200, 200, 200), 3, lineType=cv2.LINE_AA)

            # Draw scale marks
            for angle in range(-60, 61, 10):
                mark_angle_rad = np.radians(180 - angle)
                start_r = meter_width // 2 - 20
                end_r = meter_width // 2 - 10
                mark_start = (int(center_x + np.cos(mark_angle_rad) * start_r),
                            int(center_y - np.sin(mark_angle_rad) * start_r))
                mark_end = (int(center_x + np.cos(mark_angle_rad) * end_r),
                          int(center_y - np.sin(mark_angle_rad) * end_r))
                cv2.line(frame, mark_start, mark_end, (200, 200, 200), 2, lineType=cv2.LINE_AA)

            # Draw needle
            needle_angle_rad = np.radians(180 - needle_angle)
            needle_end = (int(center_x + np.cos(needle_angle_rad) * (meter_width//2 - 30)),
                         int(center_y - np.sin(needle_angle_rad) * (meter_width//2 - 30)))

            cv2.line(frame, (center_x, center_y), needle_end, (255, 100, 100), 4, lineType=cv2.LINE_AA)
            cv2.circle(frame, (center_x, center_y), 10, (150, 150, 150), -1, lineType=cv2.LINE_AA)

            # Label
            cv2.putText(frame, label, (center_x - 15, center_y + 80), cv2.FONT_HERSHEY_SIMPLEX,
                       2.0, (200, 200, 200), 3, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_73_lightning_cloud(self, frame, magnitudes):
        """Mode 73: Storm cloud that rumbles with bass, lightning on treble"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Cloud shape (top of screen, expanding with bass)
        cloud_height = int(150 + bass * 100)

        for i in range(20):
            cloud_x = int(np.random.random() * self.width)
            cloud_y = int(np.random.random() * cloud_height)
            cloud_size = int(30 + bass * 50)

            alpha = 0.3
            color = (int(30 * alpha), int(30 * alpha), int(50 * alpha))
            cv2.circle(frame, (cloud_x, cloud_y), cloud_size, color, -1, lineType=cv2.LINE_AA)

        # Lightning bolts on strong treble
        if treble > 0.65:
            # Generate lightning bolt path
            start_x = np.random.randint(self.width // 4, 3 * self.width // 4)
            start_y = cloud_height

            x, y = start_x, start_y
            points = [(x, y)]

            # Jagged lightning path
            for _ in range(int(5 + treble * 10)):
                x += int((np.random.random() - 0.5) * 80)
                y += int(40 + np.random.random() * 60)
                points.append((x, y))

            # Draw lightning
            for i in range(len(points) - 1):
                brightness = int(200 + treble * 55)
                cv2.line(frame, points[i], points[i+1], (brightness, brightness, 255), 4, lineType=cv2.LINE_AA)
                # Glow
                cv2.line(frame, points[i], points[i+1], (100, 100, 200), 12, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_74_bouncing_balls(self, frame, magnitudes):
        """Mode 74: Physics-based bouncing balls, one per frequency bin"""
        # Initialize balls if needed
        if len(self.bouncing_balls) == 0:
            for i in range(min(len(magnitudes), 30)):
                self.bouncing_balls.append({
                    'x': (i / 30) * self.width,
                    'y': self.height - 50,
                    'vy': 0,
                    'color_hue': int((i / 30) * 180)
                })

        gravity = 0.8

        # Update and draw balls
        for i, ball in enumerate(self.bouncing_balls):
            if i >= len(magnitudes):
                break

            magnitude = magnitudes[i]

            # Bounce based on amplitude
            if ball['y'] >= self.height - 50:
                ball['vy'] = -magnitude * 30 - 5  # Bounce up

            # Apply gravity
            ball['vy'] += gravity
            ball['y'] += ball['vy']

            # Keep ball in bounds
            if ball['y'] > self.height - 50:
                ball['y'] = self.height - 50
                ball['vy'] *= -0.7  # Energy loss

            # Draw ball
            ball_size = int(10 + magnitude * 20)
            color_hsv = np.array([[[ball['color_hue'], 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (int(ball['x']), int(ball['y'])), ball_size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_75_liquid_ink(self, frame, magnitudes):
        """Mode 75: Ink drops falling into water - bass=dark blooms, treble=bright splatters"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Bass hits create large ink blooms
        if bass > 0.4 and self.frame_counter % 15 == 0:
            self.ink_blooms.append({
                'x': np.random.randint(200, self.width - 200),
                'y': 100,
                'radius': 10,
                'max_radius': 150 + bass * 200,
                'life': 1.0,
                'hue': int(bass * 60)
            })

        # Treble creates small bright splatters
        if treble > 0.5:
            for _ in range(int(treble * 10)):
                self.ink_blooms.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'radius': 5,
                    'max_radius': 20 + treble * 40,
                    'life': 1.0,
                    'hue': int(120 + treble * 60)
                })

        # Update and draw blooms
        new_blooms = []
        for bloom in self.ink_blooms:
            bloom['radius'] += 2
            bloom['life'] -= 0.01

            if bloom['life'] > 0 and bloom['radius'] < bloom['max_radius']:
                alpha = bloom['life']
                color_hsv = np.array([[[bloom['hue'], 200, int(255 * alpha)]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                cv2.circle(frame, (int(bloom['x']), int(bloom['y'])), int(bloom['radius']),
                          tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
                new_blooms.append(bloom)

        self.ink_blooms = new_blooms[:100]
        return frame

    def draw_mode_76_stereo_landscape(self, frame, magnitudes):
        """Mode 76: 3D perspective - left channel left mountain, right channel right mountain"""
        # Split into stereo channels
        left_mags = magnitudes[:len(magnitudes)//2]
        right_mags = magnitudes[len(magnitudes)//2:]

        # Draw left landscape
        left_points = []
        for i, mag in enumerate(left_mags):
            x = int((i / len(left_mags)) * (self.width // 2))
            y = int(self.height - 100 - mag * 300)
            left_points.append([x, y])

        if len(left_points) > 1:
            left_points.append([self.width // 2, self.height])
            left_points.append([0, self.height])
            pts = np.array(left_points, dtype=np.int32)
            cv2.fillPoly(frame, [pts], (100, 150, 255), lineType=cv2.LINE_AA)
            cv2.polylines(frame, [pts[:len(left_mags)]], False, (150, 200, 255), 3, lineType=cv2.LINE_AA)

        # Draw right landscape
        right_points = []
        for i, mag in enumerate(right_mags):
            x = int(self.width // 2 + (i / len(right_mags)) * (self.width // 2))
            y = int(self.height - 100 - mag * 300)
            right_points.append([x, y])

        if len(right_points) > 1:
            right_points.append([self.width, self.height])
            right_points.append([self.width // 2, self.height])
            pts = np.array(right_points, dtype=np.int32)
            cv2.fillPoly(frame, [pts], (255, 150, 100), lineType=cv2.LINE_AA)
            cv2.polylines(frame, [pts[:len(right_mags)]], False, (255, 200, 150), 3, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_77_ai_latent_walk(self, frame, magnitudes):
        """Mode 77: Abstract latent space visualization (simulated)"""
        avg_magnitude = np.mean(magnitudes)
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Simulate latent walk with morphing shapes
        self.latent_morph_state += avg_magnitude * 0.1

        num_shapes = 15
        for i in range(num_shapes):
            # Position influenced by latent state
            angle = (i / num_shapes) * 2 * np.pi + self.latent_morph_state
            radius = 100 + np.sin(self.latent_morph_state + i) * 200

            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)

            # Morphing size
            size = int(20 + bass * 40 + np.sin(self.latent_morph_state * 2 + i) * 20)

            # Dream-like colors
            hue = int((self.latent_morph_state * 50 + i * 12) % 180)
            saturation = 180 + int(treble * 75)
            value = 150 + int(avg_magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw with transparency effect
            cv2.circle(frame, (x, y), size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_78_pixel_storm(self, frame, magnitudes):
        """Mode 78: Blizzard of 8-bit pixels - wind direction from stereo, speed from volume"""
        avg_magnitude = np.mean(magnitudes)

        # Stereo pan (L/R balance)
        left_power = np.mean(magnitudes[:len(magnitudes)//2])
        right_power = np.mean(magnitudes[len(magnitudes)//2:])
        wind_direction = (right_power - left_power) * 5

        # Spawn pixels
        if self.frame_counter % 2 == 0:
            for _ in range(int(avg_magnitude * 30 + 10)):
                # Dominant frequency determines color
                dominant_freq_idx = np.argmax(magnitudes)
                hue = int((dominant_freq_idx / len(magnitudes)) * 180)

                self.pixel_storm.append({
                    'x': np.random.random() * self.width,
                    'y': 0,
                    'vx': wind_direction + (np.random.random() - 0.5) * 3,
                    'vy': 3 + avg_magnitude * 5,
                    'hue': hue,
                    'life': 1.0
                })

        # Update and draw pixels
        new_pixels = []
        for pixel in self.pixel_storm:
            pixel['x'] += pixel['vx']
            pixel['y'] += pixel['vy']
            pixel['life'] -= 0.01

            if pixel['life'] > 0 and 0 < pixel['y'] < self.height:
                color_hsv = np.array([[[pixel['hue'], 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                # 8-bit pixel (small rectangle)
                pixel_size = 4
                cv2.rectangle(frame,
                            (int(pixel['x']), int(pixel['y'])),
                            (int(pixel['x']) + pixel_size, int(pixel['y']) + pixel_size),
                            tuple(map(int, color)), -1)
                new_pixels.append(pixel)

        self.pixel_storm = new_pixels[:400]
        return frame

    def draw_mode_79_growing_vine(self, frame, magnitudes):
        """Mode 79: Vine grows across screen, sprouts leaves on beats"""
        avg_magnitude = np.mean(magnitudes)
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        # Grow vine if not complete
        if len(self.vine_segments) < 200:
            if len(self.vine_segments) == 0:
                self.vine_segments.append({'x': 100, 'y': self.height - 100, 'leaves': []})
            else:
                last = self.vine_segments[-1]
                # Vine meanders
                angle = -np.pi/6 + (np.random.random() - 0.5) * np.pi/4
                new_x = last['x'] + np.cos(angle) * 15
                new_y = last['y'] + np.sin(angle) * 15

                if 0 < new_x < self.width and 0 < new_y < self.height:
                    self.vine_segments.append({'x': new_x, 'y': new_y, 'leaves': []})

                    # Sprout leaf on beat
                    if bass > 0.5:
                        leaf_size = int(10 + bass * 30)
                        self.vine_segments[-1]['leaves'].append({
                            'offset_x': (np.random.random() - 0.5) * 20,
                            'offset_y': (np.random.random() - 0.5) * 20,
                            'size': leaf_size
                        })

        # Draw vine
        for i in range(len(self.vine_segments) - 1):
            seg = self.vine_segments[i]
            next_seg = self.vine_segments[i + 1]
            cv2.line(frame, (int(seg['x']), int(seg['y'])), (int(next_seg['x']), int(next_seg['y'])),
                    (50, 120, 50), 3, lineType=cv2.LINE_AA)

            # Draw leaves
            for leaf in seg['leaves']:
                leaf_x = int(seg['x'] + leaf['offset_x'])
                leaf_y = int(seg['y'] + leaf['offset_y'])
                cv2.circle(frame, (leaf_x, leaf_y), leaf['size'], (100, 255, 100), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_80_haunted_faces(self, frame, magnitudes):
        """Mode 80: Ghostly faces fade in/out with mid-range (vocals), eyes glow on bass"""
        mid_range = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        # Face opacity controlled by mid-range (vocals)
        self.haunted_face_alpha = mid_range

        if self.haunted_face_alpha > 0.2:
            # Draw ghostly faces
            num_faces = 3
            for i in range(num_faces):
                face_x = int((i + 1) * self.width // (num_faces + 1))
                face_y = int(self.height // 3 + np.sin(self.frame_counter * 0.05 + i) * 50)
                face_size = 80

                alpha = self.haunted_face_alpha * 0.5

                # Face circle
                color = (int(200 * alpha), int(200 * alpha), int(220 * alpha))
                cv2.circle(frame, (face_x, face_y), face_size, color, -1, lineType=cv2.LINE_AA)

                # Eyes (glow on bass)
                eye_glow = 255 if bass > 0.6 else 100
                eye_offset = 25
                cv2.circle(frame, (face_x - eye_offset, face_y - 20), 12, (eye_glow, eye_glow, 50), -1, lineType=cv2.LINE_AA)
                cv2.circle(frame, (face_x + eye_offset, face_y - 20), 12, (eye_glow, eye_glow, 50), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_81_connecting_constellations(self, frame, magnitudes):
        """Mode 81: Stars that shine and connect when frequency threshold passed"""
        # Initialize stars
        if len(self.constellation_stars) == 0:
            for i in range(len(magnitudes)):
                self.constellation_stars.append({
                    'x': np.random.randint(50, self.width - 50),
                    'y': np.random.randint(50, self.height - 50),
                    'shining': False,
                    'freq_idx': i
                })

        # Update star brightness based on frequency
        shining_stars = []
        for star in self.constellation_stars:
            if star['freq_idx'] < len(magnitudes):
                magnitude = magnitudes[star['freq_idx']]
                star['shining'] = magnitude > 0.5

                if star['shining']:
                    shining_stars.append(star)
                    # Draw bright star
                    brightness = int(200 + magnitude * 55)
                    cv2.circle(frame, (star['x'], star['y']), 5, (brightness, brightness, 255), -1, lineType=cv2.LINE_AA)
                    # Glow
                    cv2.circle(frame, (star['x'], star['y']), 10, (100, 100, 200), 1, lineType=cv2.LINE_AA)
                else:
                    # Dim star
                    cv2.circle(frame, (star['x'], star['y']), 2, (80, 80, 100), -1, lineType=cv2.LINE_AA)

        # Draw connections between shining stars
        for i, star1 in enumerate(shining_stars):
            for star2 in shining_stars[i+1:]:
                # Connect nearby shining stars
                dist = np.sqrt((star1['x'] - star2['x'])**2 + (star1['y'] - star2['y'])**2)
                if dist < 200:
                    cv2.line(frame, (star1['x'], star1['y']), (star2['x'], star2['y']),
                            (100, 100, 200), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_82_matrix_rain(self, frame, magnitudes):
        """Mode 82: Matrix-style falling characters - speed from volume, brightness from treble"""
        avg_magnitude = np.mean(magnitudes)
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize columns
        if len(self.matrix_rain) == 0:
            num_columns = 60
            for i in range(num_columns):
                self.matrix_rain.append({
                    'x': int((i / num_columns) * self.width),
                    'y': np.random.randint(-100, 0),
                    'speed': 3 + np.random.random() * 5,
                    'chars': []
                })

        # Update and draw columns
        for column in self.matrix_rain:
            # Speed modulated by volume
            column['y'] += int(column['speed'] * (1 + avg_magnitude))

            if column['y'] > self.height:
                column['y'] = -100

            # Draw falling characters
            num_chars = 15
            for i in range(num_chars):
                char_y = int(column['y'] - i * 20)
                if 0 < char_y < self.height:
                    # Brightness flash from treble
                    brightness = int(150 - i * 8 + treble * 105)
                    brightness = max(50, min(255, brightness))

                    char = chr(np.random.randint(33, 127))
                    cv2.putText(frame, char, (column['x'], char_y), cv2.FONT_HERSHEY_SIMPLEX,
                              0.5, (50, brightness, 50), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_83_voxel_world(self, frame, magnitudes):
        """Mode 83: 3D voxel grid with audio shockwave"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        # Shockwave emanates from center
        shockwave_radius = int((self.frame_counter % 100) * (1 + bass) * 5)

        # Draw voxel grid
        voxel_size = 40
        for x in range(0, self.width, voxel_size):
            for y in range(0, self.height, voxel_size):
                # Distance from center
                dist = np.sqrt((x - self.center_x)**2 + (y - self.center_y)**2)

                # Shockwave effect
                if abs(dist - shockwave_radius) < 30:
                    # Voxel affected by shockwave
                    color_intensity = int(200 + bass * 55)
                    color = (color_intensity, 100, 100)
                else:
                    color = (50, 50, 80)

                cv2.rectangle(frame, (x, y), (x + voxel_size - 2, y + voxel_size - 2), color, -1)
                cv2.rectangle(frame, (x, y), (x + voxel_size - 2, y + voxel_size - 2), (100, 100, 120), 1)

        return frame

    def draw_mode_84_dna_helix_rungs(self, frame, magnitudes):
        """Mode 84: DNA helix where rungs light up with frequency"""
        self.dna_rotation += 2

        # Draw double helix strands
        num_points = 100
        for i in range(num_points):
            z = i / num_points
            y = int(z * self.height)
            angle = z * 4 * np.pi + np.radians(self.dna_rotation)

            # Strand 1
            x1 = int(self.center_x + np.cos(angle) * 100)
            cv2.circle(frame, (x1, y), 5, (100, 150, 255), -1, lineType=cv2.LINE_AA)

            # Strand 2 (opposite)
            x2 = int(self.center_x + np.cos(angle + np.pi) * 100)
            cv2.circle(frame, (x2, y), 5, (100, 150, 255), -1, lineType=cv2.LINE_AA)

            # Rungs (light up based on frequency)
            if i % 5 == 0:
                freq_idx = int((i / num_points) * len(magnitudes))
                if freq_idx >= len(magnitudes):
                    freq_idx = len(magnitudes) - 1

                magnitude = magnitudes[freq_idx]
                if magnitude > 0.3:
                    brightness = int(100 + magnitude * 155)
                    rung_color = (brightness, brightness, 200)
                    thickness = int(2 + magnitude * 6)
                    cv2.line(frame, (x1, y), (x2, y), rung_color, thickness, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_85_audio_reactive_shader(self, frame, magnitudes):
        """Mode 85: Full-screen procedural shader effect"""
        avg_magnitude = np.mean(magnitudes)
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        self.shader_time += 0.05 + avg_magnitude * 0.1

        # Generate procedural pattern (simplified Perlin-like noise)
        for y in range(0, self.height, 4):
            for x in range(0, self.width, 4):
                # UV coordinates
                u = x / self.width
                v = y / self.height

                # Noise pattern
                noise_val = np.sin(u * 10 + self.shader_time + bass * 5) * np.cos(v * 10 + self.shader_time)
                noise_val += np.sin(np.sqrt(u*u + v*v) * 20 - self.shader_time * 2) * treble

                # Color mapping (clamp to valid uint8 range)
                hue = np.clip(int((noise_val * 0.5 + 0.5) * 180), 0, 179)
                saturation = np.clip(200 + int(treble * 55), 0, 255)
                value = np.clip(int((noise_val * 0.5 + 0.5) * 200 + bass * 55), 0, 255)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                cv2.rectangle(frame, (x, y), (x+4, y+4), tuple(map(int, color)), -1)

        return frame

    def draw_mode_86_spirograph(self, frame, magnitudes):
        """Mode 86: Spirograph pattern - radii controlled by frequencies"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Spirograph parameters modulated by audio
        R = 150 + bass * 100  # Outer wheel radius
        r = 50 + mids * 50  # Inner wheel radius
        d = 30 + treble * 40  # Pen distance

        # Draw spirograph
        points = []
        for t in np.linspace(0, 2 * np.pi * 5, 500):
            x = int(self.center_x + (R - r) * np.cos(t) + d * np.cos((R - r) / r * t))
            y = int(self.center_y + (R - r) * np.sin(t) - d * np.sin((R - r) / r * t))

            if 0 <= x < self.width and 0 <= y < self.height:
                points.append([x, y])

        if len(points) > 1:
            points = np.array(points, dtype=np.int32)

            # Color based on treble
            hue = int(treble * 180)
            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.polylines(frame, [points], False, tuple(map(int, color)), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_87_equalizer_tower(self, frame, magnitudes):
        """Mode 87: 3D tower of stacked glowing rings"""
        num_rings = min(len(magnitudes), 40)
        ring_height = self.height // num_rings

        for i, magnitude in enumerate(magnitudes[:num_rings]):
            y = self.height - (i + 1) * ring_height
            radius = int(magnitude * (self.width // 3))

            # Color gradient
            hue = int((i / num_rings) * 180)
            saturation = 200 + int(magnitude * 55)
            value = 150 + int(magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Ring thickness
            thickness = int(2 + magnitude * 10)

            cv2.circle(frame, (self.center_x, y), radius, tuple(map(int, color)), thickness, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_88_audio_driven_doodles(self, frame, magnitudes):
        """Mode 88: Generative doodle bot - bass=90° turns, treble=shakiness"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize path
        if len(self.doodle_path) == 0:
            self.doodle_path = [{'x': self.center_x, 'y': self.center_y, 'angle': 0}]

        # Current position
        current = self.doodle_path[-1]

        # Bass hit causes 90° turn
        if bass > 0.6 and len(self.doodle_path) % 10 == 0:
            current['angle'] += np.pi / 2

        # Move forward
        step_size = 5 + mids * 5
        shakiness = treble * 10
        new_x = current['x'] + np.cos(current['angle']) * step_size + (np.random.random() - 0.5) * shakiness
        new_y = current['y'] + np.sin(current['angle']) * step_size + (np.random.random() - 0.5) * shakiness

        # Keep in bounds
        new_x = np.clip(new_x, 50, self.width - 50)
        new_y = np.clip(new_y, 50, self.height - 50)

        self.doodle_path.append({'x': new_x, 'y': new_y, 'angle': current['angle']})

        # Limit path length
        if len(self.doodle_path) > 500:
            self.doodle_path = self.doodle_path[-500:]

        # Draw path
        for i in range(len(self.doodle_path) - 1):
            p1 = self.doodle_path[i]
            p2 = self.doodle_path[i + 1]

            # Color based on mids
            hue = int(mids * 180)
            alpha = (i / len(self.doodle_path))
            color_hsv = np.array([[[hue, 200, int(255 * alpha)]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.line(frame, (int(p1['x']), int(p1['y'])), (int(p2['x']), int(p2['y'])),
                    tuple(map(int, color)), 3, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_89_firework_show(self, frame, magnitudes):
        """Mode 89: Bass launches rockets, they explode at peak with mid-range color"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Launch rockets on bass hits
        if bass > 0.55 and self.frame_counter % 10 == 0:
            self.firework_rockets.append({
                'x': np.random.randint(self.width // 4, 3 * self.width // 4),
                'y': self.height - 50,
                'vy': -10 - bass * 8,
                'exploded': False,
                'particles': []
            })

        # Update rockets
        new_rockets = []
        for rocket in self.firework_rockets:
            if not rocket['exploded']:
                rocket['y'] += rocket['vy']
                rocket['vy'] += 0.3  # Gravity

                # Draw rocket trail
                cv2.circle(frame, (int(rocket['x']), int(rocket['y'])), 5, (200, 200, 255), -1, lineType=cv2.LINE_AA)

                # Explode at peak
                if rocket['vy'] > 0:
                    rocket['exploded'] = True
                    # Create particle burst
                    for _ in range(int(50 + mids * 100)):
                        angle = np.random.random() * 2 * np.pi
                        speed = 2 + np.random.random() * 8
                        rocket['particles'].append({
                            'x': rocket['x'],
                            'y': rocket['y'],
                            'vx': np.cos(angle) * speed,
                            'vy': np.sin(angle) * speed,
                            'life': 1.0
                        })

            # Update explosion particles
            if rocket['exploded']:
                new_particles = []
                for particle in rocket['particles']:
                    particle['x'] += particle['vx']
                    particle['y'] += particle['vy']
                    particle['vy'] += 0.2  # Gravity
                    particle['life'] -= 0.015

                    if particle['life'] > 0:
                        # Color from mids
                        hue = int(mids * 180)
                        alpha = particle['life']
                        color_hsv = np.array([[[hue, 255, int(255 * alpha)]]], dtype=np.uint8)
                        color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                        size = int(2 + treble * 6)
                        cv2.circle(frame, (int(particle['x']), int(particle['y'])), size,
                                  tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
                        new_particles.append(particle)

                rocket['particles'] = new_particles
                if len(rocket['particles']) > 0:
                    new_rockets.append(rocket)

            else:
                new_rockets.append(rocket)

        self.firework_rockets = new_rockets[:20]
        return frame

    def draw_mode_90_microscopic_view(self, frame, magnitudes):
        """Mode 90: Cells jiggle and divide based on frequency"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        avg_magnitude = np.mean(magnitudes)

        # Initialize cells
        if len(self.microscopic_cells) == 0:
            for i in range(10):
                self.microscopic_cells.append({
                    'x': np.random.random() * self.width,
                    'y': np.random.random() * self.height,
                    'radius': 30 + np.random.random() * 30,
                    'vx': (np.random.random() - 0.5) * 2,
                    'vy': (np.random.random() - 0.5) * 2,
                    'freq_idx': i % len(magnitudes)
                })

        # Update cells
        new_cells = []
        for cell in self.microscopic_cells:
            freq_idx = cell['freq_idx'] % len(magnitudes)
            magnitude = magnitudes[freq_idx]

            # Jiggle (agitation from overall volume)
            jiggle_x = (np.random.random() - 0.5) * avg_magnitude * 10
            jiggle_y = (np.random.random() - 0.5) * avg_magnitude * 10

            cell['x'] += cell['vx'] + jiggle_x
            cell['y'] += cell['vy'] + jiggle_y

            # Bounce off walls
            if cell['x'] < cell['radius'] or cell['x'] > self.width - cell['radius']:
                cell['vx'] *= -1
            if cell['y'] < cell['radius'] or cell['y'] > self.height - cell['radius']:
                cell['vy'] *= -1

            # Divide when amplitude is high
            if magnitude > 0.7 and len(new_cells) < 50 and np.random.random() < 0.05:
                # Create daughter cell
                new_cells.append({
                    'x': cell['x'] + 20,
                    'y': cell['y'] + 20,
                    'radius': cell['radius'] * 0.7,
                    'vx': -cell['vx'],
                    'vy': -cell['vy'],
                    'freq_idx': freq_idx
                })
                cell['radius'] *= 0.7

            # Draw cell
            hue = int((freq_idx / len(magnitudes)) * 180)
            saturation = 200 + int(magnitude * 55)
            value = 150 + int(magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (int(cell['x']), int(cell['y'])), int(cell['radius']),
                      tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(cell['x']), int(cell['y'])), int(cell['radius']),
                      (200, 200, 200), 2, lineType=cv2.LINE_AA)

            new_cells.append(cell)

        self.microscopic_cells = new_cells[:50]
        return frame

    def draw_mode_91_burning_paper(self, frame, magnitudes):
        """Mode 91: Spectrum bars as flames, embers on high freq, paper curls on bass"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Draw flame bars
        bar_width = self.width // len(magnitudes)
        for i, magnitude in enumerate(magnitudes):
            bar_height = int(magnitude * self.height * 0.7)
            x = i * bar_width
            y_base = self.height - 50

            # Flame effect (multiple layers)
            for layer in range(3):
                y_offset = layer * 15
                layer_height = bar_height - y_offset
                if layer_height > 0:
                    y = y_base - layer_height

                    # Flame color gradient
                    hue = 10 + layer * 5  # Yellow to red
                    saturation = 255
                    value = 200 - layer * 40
                    color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                    color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                    # Flickering width
                    flicker = int((np.random.random() - 0.5) * 5)
                    cv2.rectangle(frame, (x + flicker, y), (x + bar_width - 2 + flicker, y_base),
                                tuple(map(int, color)), -1)

        # Embers on treble
        if treble > 0.5:
            for _ in range(int(treble * 20)):
                ember_x = np.random.randint(0, self.width)
                ember_y = self.height - 50 - np.random.randint(0, 100)
                cv2.circle(frame, (ember_x, ember_y), 2, (100, 150, 255), -1)

        # Paper curl effect on bass (darken corners)
        if bass > 0.4:
            curl_alpha = bass * 0.5
            overlay = frame.copy()
            pts = np.array([[0, 0], [int(self.width * 0.2), 0],
                          [0, int(self.height * 0.2)]], dtype=np.int32)
            cv2.fillPoly(overlay, [pts], (20, 20, 10))
            cv2.addWeighted(overlay, curl_alpha, frame, 1 - curl_alpha, 0, frame)

        return frame

    def draw_mode_92_swarm_intelligence(self, frame, magnitudes):
        """Mode 92: Boid flocking - cohesion/separation modulated by audio"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize boids
        if len(self.swarm_boids) == 0:
            for _ in range(40):
                self.swarm_boids.append({
                    'x': np.random.random() * self.width,
                    'y': np.random.random() * self.height,
                    'vx': (np.random.random() - 0.5) * 4,
                    'vy': (np.random.random() - 0.5) * 4
                })

        # Boid rules modulated by audio
        cohesion_factor = 0.01 * (1 - bass)  # Bass scatters
        separation_factor = 0.5 + treble * 1.5  # Treble aligns
        alignment_factor = 0.05 + treble * 0.1

        for boid in self.swarm_boids:
            # Calculate forces
            cohesion_x, cohesion_y = 0, 0
            separation_x, separation_y = 0, 0
            alignment_vx, alignment_vy = 0, 0
            neighbors = 0

            for other in self.swarm_boids:
                if other is boid:
                    continue

                dx = other['x'] - boid['x']
                dy = other['y'] - boid['y']
                dist = np.sqrt(dx**2 + dy**2) + 0.1

                if dist < 100:
                    # Cohesion
                    cohesion_x += dx
                    cohesion_y += dy

                    # Alignment
                    alignment_vx += other['vx']
                    alignment_vy += other['vy']

                    neighbors += 1

                if dist < 30:
                    # Separation
                    separation_x -= dx / dist
                    separation_y -= dy / dist

            if neighbors > 0:
                cohesion_x /= neighbors
                cohesion_y /= neighbors
                alignment_vx /= neighbors
                alignment_vy /= neighbors

            # Apply forces
            boid['vx'] += cohesion_x * cohesion_factor + separation_x * separation_factor + alignment_vx * alignment_factor
            boid['vy'] += cohesion_y * cohesion_factor + separation_y * separation_factor + alignment_vy * alignment_factor

            # Limit speed
            speed = np.sqrt(boid['vx']**2 + boid['vy']**2)
            max_speed = 5 + treble * 5
            if speed > max_speed:
                boid['vx'] = (boid['vx'] / speed) * max_speed
                boid['vy'] = (boid['vy'] / speed) * max_speed

            # Update position
            boid['x'] += boid['vx']
            boid['y'] += boid['vy']

            # Wrap around
            boid['x'] = boid['x'] % self.width
            boid['y'] = boid['y'] % self.height

            # Draw boid
            cv2.circle(frame, (int(boid['x']), int(boid['y'])), 5, (100, 200, 255), -1, lineType=cv2.LINE_AA)

            # Draw velocity direction
            end_x = int(boid['x'] + boid['vx'] * 3)
            end_y = int(boid['y'] + boid['vy'] * 3)
            cv2.line(frame, (int(boid['x']), int(boid['y'])), (end_x, end_y), (150, 220, 255), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_93_pendulum_wave(self, frame, magnitudes):
        """Mode 93: Multiple pendulums with slightly different periods - force from frequency"""
        num_pendulums = min(len(magnitudes), 30)

        # Initialize pendulum angles
        if len(self.pendulum_angles) == 0:
            self.pendulum_angles = [0.0] * num_pendulums

        # Update and draw pendulums
        for i in range(num_pendulums):
            magnitude = magnitudes[i] if i < len(magnitudes) else 0

            # Period slightly different for each pendulum
            period = 0.05 + i * 0.001

            # Force from audio
            self.pendulum_angles[i] += period + magnitude * 0.1

            # Pendulum position
            x_base = int((i / num_pendulums) * self.width)
            y_base = 100

            pendulum_length = 200 + magnitude * 100
            x_end = int(x_base + np.sin(self.pendulum_angles[i]) * pendulum_length)
            y_end = int(y_base + pendulum_length)

            # Draw rod
            cv2.line(frame, (x_base, y_base), (x_end, y_end), (150, 150, 150), 2, lineType=cv2.LINE_AA)

            # Draw bob
            bob_size = int(5 + magnitude * 15)
            hue = int((i / num_pendulums) * 180)
            color_hsv = np.array([[[hue, 200, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (x_end, y_end), bob_size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_94_retro_scanlines(self, frame, magnitudes):
        """Mode 94: Waveform on old CRT with scanlines and static"""
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Draw waveform
        points = []
        for i, magnitude in enumerate(magnitudes):
            x = int((i / len(magnitudes)) * self.width)
            y = int(self.center_y + (magnitude - 0.5) * self.height * 0.6)
            points.append([x, y])

        if len(points) > 1:
            points_np = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [points_np], False, (100, 255, 100), 3, lineType=cv2.LINE_AA)

        # Scanlines
        for y in range(0, self.height, 4):
            cv2.line(frame, (0, y), (self.width, y), (0, 0, 0), 1)

        # Static/noise increases with treble
        if treble > 0.3:
            noise_intensity = int(treble * 50)
            for _ in range(noise_intensity):
                x = np.random.randint(0, self.width)
                y = np.random.randint(0, self.height)
                brightness = np.random.randint(100, 255)
                cv2.circle(frame, (x, y), 1, (brightness, brightness, brightness), -1)

        # CRT flicker
        self.crt_flicker = (self.crt_flicker + treble * 10) % 20
        if self.crt_flicker > 18:
            frame = cv2.add(frame, np.full_like(frame, 20))

        return frame

    def draw_mode_95_pulsing_polygon(self, frame, magnitudes):
        """Mode 95: Central polygon with vertices pushed by frequency bands"""
        num_vertices = min(len(magnitudes), 12)

        # Calculate vertex positions
        vertices = []
        for i in range(num_vertices):
            angle = (i / num_vertices) * 2 * np.pi
            magnitude = magnitudes[i] if i < len(magnitudes) else 0

            # Bass affects main vertices
            base_radius = self.max_radius * 0.5
            pushed_radius = base_radius + magnitude * 200

            # Treble adds spikes between
            x = int(self.center_x + np.cos(angle) * pushed_radius)
            y = int(self.center_y + np.sin(angle) * pushed_radius)
            vertices.append([x, y])

        # Draw filled polygon
        if len(vertices) > 2:
            pts = np.array(vertices, dtype=np.int32)
            avg_magnitude = np.mean(magnitudes)

            hue = int(self.frame_counter * 2 % 180)
            saturation = 200 + int(avg_magnitude * 55)
            value = 150 + int(avg_magnitude * 105)
            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.fillPoly(frame, [pts], tuple(map(int, color)), lineType=cv2.LINE_AA)
            cv2.polylines(frame, [pts], True, (255, 255, 255), 3, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_96_chromatic_orb(self, frame, magnitudes):
        """Mode 96: 3D sphere with chromatic shader and moving light source"""
        avg_magnitude = np.mean(magnitudes)
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        # Light source moves with stereo pan
        left = np.mean(magnitudes[:len(magnitudes)//2])
        right = np.mean(magnitudes[len(magnitudes)//2:])

        self.chromatic_orb_rotation += (right - left) * 0.1
        light_angle = self.chromatic_orb_rotation
        light_x = np.cos(light_angle)
        light_y = np.sin(light_angle)

        # Draw orb
        orb_radius = int(150 + bass * 50)

        for angle in np.linspace(0, 2 * np.pi, 60):
            for radius_factor in np.linspace(0, 1, 20):
                radius = int(orb_radius * radius_factor)

                x = int(self.center_x + np.cos(angle) * radius)
                y = int(self.center_y + np.sin(angle) * radius)

                # Lighting calculation
                dot = np.cos(angle) * light_x + np.sin(angle) * light_y
                brightness = max(0, dot) * 200 + 55

                # Chromatic color
                hue = int((angle / (2 * np.pi) + radius_factor + self.frame_counter * 0.01) * 180) % 180
                saturation = 200 + int(avg_magnitude * 55)
                value = int(brightness)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                cv2.circle(frame, (x, y), 3, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_97_textured_bars(self, frame, magnitudes):
        """Mode 97: Bars filled with scrolling animated texture"""
        bar_width = self.width // len(magnitudes)

        for i, magnitude in enumerate(magnitudes):
            bar_height = int(magnitude * self.height * 0.7)
            x = i * bar_width
            y = self.height - bar_height

            # Scrolling texture (simulated with pattern)
            for ty in range(y, self.height, 5):
                scroll_offset = int((self.frame_counter * magnitude * 2) % 10)
                pattern_y = (ty + scroll_offset) % 10

                if pattern_y < 5:
                    color = (100 + int(magnitude * 155), 150, 200)
                else:
                    color = (50, 100, 150)

                cv2.line(frame, (x, ty), (x + bar_width - 2, ty), color, 2)

        return frame

    def draw_mode_98_voronoi_tessellation(self, frame, magnitudes):
        """Mode 98: Voronoi diagram with cells pulsing and seed points moving"""
        num_seeds = min(len(magnitudes), 20)
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        # Update seed positions (moved by low frequencies)
        if len(self.voronoi_seeds) == 0:
            for _ in range(num_seeds):
                self.voronoi_seeds.append({
                    'x': np.random.random() * self.width,
                    'y': np.random.random() * self.height
                })

        for i, seed in enumerate(self.voronoi_seeds[:num_seeds]):
            magnitude = magnitudes[i] if i < len(magnitudes) else 0
            # Seeds move slightly
            seed['x'] += (np.random.random() - 0.5) * bass * 5
            seed['y'] += (np.random.random() - 0.5) * bass * 5
            # Keep in bounds
            seed['x'] = np.clip(seed['x'], 0, self.width)
            seed['y'] = np.clip(seed['y'], 0, self.height)

        # Draw Voronoi cells (simplified - sample points)
        for y in range(0, self.height, 5):
            for x in range(0, self.width, 5):
                # Find closest seed
                min_dist = float('inf')
                closest_idx = 0

                for i, seed in enumerate(self.voronoi_seeds[:num_seeds]):
                    dist = (x - seed['x'])**2 + (y - seed['y'])**2
                    if dist < min_dist:
                        min_dist = dist
                        closest_idx = i

                # Color based on closest seed and its magnitude
                magnitude = magnitudes[closest_idx] if closest_idx < len(magnitudes) else 0
                hue = int((closest_idx / num_seeds) * 180)
                saturation = 200 + int(magnitude * 55)
                value = 100 + int(magnitude * 155)
                color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                cv2.rectangle(frame, (x, y), (x+5, y+5), tuple(map(int, color)), -1)

        # Draw seed points
        for seed in self.voronoi_seeds[:num_seeds]:
            cv2.circle(frame, (int(seed['x']), int(seed['y'])), 6, (255, 255, 255), -1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_99_shattering_glass(self, frame, magnitudes):
        """Mode 99: Glass pane with cracks appearing on beats"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Glass pane (semi-transparent overlay)
        overlay = frame.copy()
        cv2.rectangle(overlay, (100, 100), (self.width - 100, self.height - 100),
                     (200, 220, 240), -1)
        cv2.addWeighted(overlay, 0.3, frame, 0.7, 0, frame)

        # Create cracks on strong beats
        if bass > 0.65 and len(self.glass_cracks) < 50:
            crack_center = (self.center_x + int((np.random.random() - 0.5) * 200),
                          self.center_y + int((np.random.random() - 0.5) * 200))

            # Radiating crack lines
            num_lines = int(4 + bass * 8)
            for _ in range(num_lines):
                angle = np.random.random() * 2 * np.pi
                length = 50 + bass * 150

                end_x = int(crack_center[0] + np.cos(angle) * length)
                end_y = int(crack_center[1] + np.sin(angle) * length)

                self.glass_cracks.append({
                    'start': crack_center,
                    'end': (end_x, end_y),
                    'complexity': treble
                })

        # Draw cracks
        for crack in self.glass_cracks:
            thickness = int(1 + crack['complexity'] * 3)
            cv2.line(frame, crack['start'], crack['end'], (50, 50, 50), thickness, lineType=cv2.LINE_AA)

        # Screen shake on impact
        if bass > 0.7:
            shake_x = int((np.random.random() - 0.5) * bass * 20)
            shake_y = int((np.random.random() - 0.5) * bass * 20)
            M = np.float32([[1, 0, shake_x], [0, 1, shake_y]])
            frame = cv2.warpAffine(frame, M, (self.width, self.height))

        return frame

    def draw_mode_100_sunrise_sunset(self, frame, magnitudes):
        """Mode 100: Gradient sky with pulsing sun and glittering stars"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Sky gradient (color mapped to mid-range)
        sky_hue = int(20 + mids * 100)  # Blue to orange
        for y in range(self.height):
            gradient_factor = y / self.height
            saturation = int(200 - gradient_factor * 100)
            value = int(255 - gradient_factor * 100)

            color_hsv = np.array([[[sky_hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.line(frame, (0, y), (self.width, y), tuple(map(int, color)), 1)

        # Sun/Moon (pulses with bass)
        self.sun_position = int(self.height * 0.3 + np.sin(self.frame_counter * 0.02) * 50)
        sun_radius = int(60 + bass * 50)

        sun_color = (100, 200, 255) if mids < 0.5 else (50, 150, 255)
        cv2.circle(frame, (self.center_x, self.sun_position), sun_radius, sun_color, -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, (self.center_x, self.sun_position), sun_radius + 10,
                  tuple(int(c * 0.7) for c in sun_color), 3, lineType=cv2.LINE_AA)

        # Stars glitter on treble (visible when dark)
        if mids < 0.3:
            num_stars = int(treble * 50 + 10)
            for _ in range(num_stars):
                star_x = np.random.randint(0, self.width)
                star_y = np.random.randint(0, self.height // 2)
                brightness = int(200 + treble * 55)

                cv2.circle(frame, (star_x, star_y), 2, (brightness, brightness, brightness), -1, lineType=cv2.LINE_AA)

        return frame
    def draw_mode_101_neural_pulse(self, frame, magnitudes):
        """Mode 101: Neural network with pulsing nodes and lighting connections"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize neural network nodes
        if len(self.neural_nodes) == 0:
            for i in range(30):
                self.neural_nodes.append({
                    'x': np.random.randint(100, self.width - 100),
                    'y': np.random.randint(100, self.height - 100),
                    'layer': i % 3,  # 3 layers
                    'active': 0
                })

        # Update node activation based on frequency bands
        for i, node in enumerate(self.neural_nodes):
            if node['layer'] == 0:  # Bottom layer - bass
                node['active'] = bass
            elif node['layer'] == 1:  # Middle layer - mids
                node['active'] = mids
            else:  # Top layer - treble
                node['active'] = treble

        # Draw connections that flash with amplitude
        for i, node1 in enumerate(self.neural_nodes):
            for j, node2 in enumerate(self.neural_nodes[i+1:], i+1):
                if abs(node1['layer'] - node2['layer']) == 1:  # Connect adjacent layers
                    intensity = int((node1['active'] + node2['active']) * 127.5)
                    if intensity > 50:
                        color = (intensity, int(intensity * 0.5), intensity + 50)
                        thickness = 1 if intensity < 150 else 2
                        cv2.line(frame, (node1['x'], node1['y']), (node2['x'], node2['y']),
                                color, thickness, lineType=cv2.LINE_AA)

        # Draw pulsing nodes
        for node in self.neural_nodes:
            radius = int(8 + node['active'] * 20)
            hue = int(140 + node['layer'] * 30)  # Purple to cyan
            intensity = int(200 + node['active'] * 55)

            color_hsv = np.array([[[hue, 255, intensity]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (node['x'], node['y']), radius, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (node['x'], node['y']), radius + 3, (255, 255, 255), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_102_liquid_mercury(self, frame, magnitudes):
        """Mode 102: Metallic liquid that ripples with physics"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Spawn mercury droplets on high treble
        if treble > 0.5 and self.frame_counter % 3 == 0:
            self.liquid_mercury_particles.append({
                'x': np.random.randint(100, self.width - 100),
                'y': 100,
                'vx': np.random.uniform(-2, 2),
                'vy': 0,
                'radius': int(10 + treble * 20)
            })

        # Bass creates large waves
        wave_offset = int(bass * 50)

        # Update and draw mercury particles
        for particle in self.liquid_mercury_particles[:]:
            particle['vy'] += 0.5  # Gravity
            particle['y'] += particle['vy']
            particle['x'] += particle['vx']

            # Boundary bouncing
            if particle['y'] > self.height - 100:
                particle['vy'] *= -0.7
                particle['y'] = self.height - 100

            if particle['x'] < 50 or particle['x'] > self.width - 50:
                particle['vx'] *= -0.7

            # Draw with metallic shading
            cv2.circle(frame, (int(particle['x']), int(particle['y'])),
                      particle['radius'], (200, 200, 200), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(particle['x']) - 5, int(particle['y']) - 5),
                      particle['radius'] // 3, (255, 255, 255), -1, lineType=cv2.LINE_AA)  # Highlight

        # Clean up old particles
        self.liquid_mercury_particles = [p for p in self.liquid_mercury_particles if p['y'] < self.height]

        # Mid-range creates surface ripples
        for i in range(int(mids * 5)):
            ripple_x = self.center_x + int(np.sin(self.frame_counter * 0.1 + i) * 200)
            ripple_y = self.height - 100
            ripple_radius = int(30 + i * 20 + mids * 30)
            cv2.circle(frame, (ripple_x, ripple_y), ripple_radius, (150, 150, 150), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_103_cosmic_strings(self, frame, magnitudes):
        """Mode 103: Vibrating strings in space like guitar strings"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize strings
        if len(self.cosmic_strings) == 0:
            for i in range(12):
                self.cosmic_strings.append({
                    'y': 100 + i * (self.height - 200) // 12,
                    'frequency': i + 1,
                    'magnitude': 0
                })

        # Update string vibrations
        for i, string in enumerate(self.cosmic_strings):
            string['magnitude'] = magnitudes[min(i * 10, len(magnitudes) - 1)]

        # Draw vibrating strings
        for string in self.cosmic_strings:
            points = []
            amplitude = int(string['magnitude'] * 100)

            for x in range(0, self.width, 10):
                wave = np.sin(x * 0.02 * string['frequency'] + self.frame_counter * 0.1)
                y = string['y'] + int(wave * amplitude)
                points.append([x, y])

            points = np.array(points, dtype=np.int32)

            # Gold and white glowing strings
            hue = 30  # Gold
            intensity = int(200 + string['magnitude'] * 55)

            color_hsv = np.array([[[hue, 200, intensity]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.polylines(frame, [points], False, tuple(map(int, color)), 2, lineType=cv2.LINE_AA)

            # Add glow
            cv2.polylines(frame, [points], False, (255, 255, 255), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_104_particle_swarm(self, frame, magnitudes):
        """Mode 104: Thousands of particles forming shapes"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Spawn particles
        if len(self.particle_swarm) < 1000:
            for _ in range(10):
                angle = np.random.random() * 2 * np.pi
                distance = np.random.random() * 200
                self.particle_swarm.append({
                    'x': self.center_x + np.cos(angle) * distance,
                    'y': self.center_y + np.sin(angle) * distance,
                    'vx': 0,
                    'vy': 0,
                    'trail': []
                })

        # Bass creates circular formations
        target_radius = 150 + bass * 200

        # Update particle positions
        for particle in self.particle_swarm:
            dx = self.center_x - particle['x']
            dy = self.center_y - particle['y']
            distance = np.sqrt(dx*dx + dy*dy)

            if distance > 0:
                angle = np.arctan2(dy, dx)

                # Bass = circular, treble = scatter
                if bass > 0.5:
                    target_x = self.center_x + np.cos(angle) * target_radius
                    target_y = self.center_y + np.sin(angle) * target_radius
                else:
                    target_x = self.center_x + np.cos(angle + treble * np.pi) * (distance + treble * 100)
                    target_y = self.center_y + np.sin(angle + treble * np.pi) * (distance + treble * 100)

                particle['vx'] = (target_x - particle['x']) * 0.05
                particle['vy'] = (target_y - particle['y']) * 0.05

            particle['x'] += particle['vx']
            particle['y'] += particle['vy']

            # Update trail
            particle['trail'].append((int(particle['x']), int(particle['y'])))
            if len(particle['trail']) > 5:
                particle['trail'].pop(0)

            # Velocity-based color
            velocity = np.sqrt(particle['vx']**2 + particle['vy']**2)
            hue = int(120 - min(velocity * 50, 120))  # Blue to red

            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw trail
            if len(particle['trail']) > 1:
                pts = np.array(particle['trail'], dtype=np.int32)
                cv2.polylines(frame, [pts], False, tuple(map(int, color)), 1, lineType=cv2.LINE_AA)

            # Draw particle
            cv2.circle(frame, (int(particle['x']), int(particle['y'])), 2, tuple(map(int, color)), -1)

        return frame

    def draw_mode_105_crystal_lattice(self, frame, magnitudes):
        """Mode 105: 3D crystal structure with pulsing nodes"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])

        # Initialize crystal lattice nodes
        if len(self.crystal_lattice_nodes) == 0:
            grid_size = 5
            spacing = min(self.width, self.height) // (grid_size + 1)
            for i in range(grid_size):
                for j in range(grid_size):
                    for k in range(grid_size):
                        self.crystal_lattice_nodes.append({
                            'x3d': (i - grid_size//2) * spacing,
                            'y3d': (j - grid_size//2) * spacing,
                            'z3d': (k - grid_size//2) * spacing,
                            'magnitude': 0
                        })

        # Rotation angle
        angle = self.frame_counter * 0.02

        # Draw connections and nodes
        for i, node in enumerate(self.crystal_lattice_nodes):
            # Update magnitude from frequencies
            node['magnitude'] = magnitudes[min(i * 2, len(magnitudes) - 1)]

            # 3D rotation and projection
            x = node['x3d']
            y = node['y3d'] * np.cos(angle) - node['z3d'] * np.sin(angle)
            z = node['y3d'] * np.sin(angle) + node['z3d'] * np.cos(angle)

            x_rot = x * np.cos(angle) - z * np.sin(angle)
            z_rot = x * np.sin(angle) + z * np.cos(angle)

            # Perspective projection
            scale = 300 / (300 + z_rot)
            x_2d = int(self.center_x + x_rot * scale)
            y_2d = int(self.center_y + y * scale)

            node['x2d'] = x_2d
            node['y2d'] = y_2d
            node['z2d'] = z_rot

            # Draw node
            radius = int(5 + node['magnitude'] * 15)
            hue = int((z_rot + 300) / 600 * 180)  # Rainbow based on depth

            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (x_2d, y_2d), radius, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (x_2d, y_2d), radius + 2, (255, 255, 255), 1, lineType=cv2.LINE_AA)

        # Draw connections between nearby nodes
        for i, node1 in enumerate(self.crystal_lattice_nodes):
            for node2 in self.crystal_lattice_nodes[i+1:i+10]:
                dist = np.sqrt((node1['x3d'] - node2['x3d'])**2 +
                             (node1['y3d'] - node2['y3d'])**2 +
                             (node1['z3d'] - node2['z3d'])**2)

                if dist < 250:  # Only connect nearby nodes
                    intensity = int((node1['magnitude'] + node2['magnitude']) * 127.5)
                    if intensity > 30:
                        cv2.line(frame, (node1['x2d'], node1['y2d']),
                                (node2['x2d'], node2['y2d']),
                                (intensity, intensity, intensity + 50), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_106_aurora_waves(self, frame, magnitudes):
        """Mode 106: Aurora borealis flowing curtains"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Multiple aurora curtains
        num_curtains = 5
        for curtain_idx in range(num_curtains):
            offset = curtain_idx * 50

            # Create flowing wave points
            for x in range(0, self.width, 15):
                wave1 = np.sin(x * 0.01 + self.frame_counter * 0.05 + offset) * bass * 100
                wave2 = np.sin(x * 0.02 + self.frame_counter * 0.03 + offset) * mids * 80
                y_base = self.height // 3 + curtain_idx * 30

                # Color shifts with mids
                hue = int(60 + mids * 60 + curtain_idx * 20)  # Green to purple to blue
                saturation = int(200 + treble * 55)

                color_hsv = np.array([[[hue, saturation, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

                # Draw vertical curtain strands
                for y_offset in range(0, 200, 10):
                    y = int(y_base + wave1 + wave2 + y_offset)
                    if 0 <= y < self.height:
                        alpha = 1.0 - (y_offset / 200) * 0.7
                        cv2.circle(frame, (x, y), 8,
                                  tuple(int(c * alpha) for c in color), -1, lineType=cv2.LINE_AA)

                # Sparkle effects on treble
                if treble > 0.6 and np.random.random() < treble:
                    sparkle_y = int(y_base + wave1 + np.random.randint(0, 100))
                    if 0 <= sparkle_y < self.height:
                        cv2.circle(frame, (x, sparkle_y), 3, (255, 255, 255), -1)

        return frame

    def draw_mode_107_dna_helix(self, frame, magnitudes):
        """Mode 107: Rotating DNA double helix with pulsing base pairs"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Rotation speed increases with amplitude
        self.dna_helix_rotation += 0.02 + bass * 0.05

        # Draw double helix
        for z in range(0, self.height, 10):
            angle1 = z * 0.05 + self.dna_helix_rotation
            angle2 = angle1 + np.pi

            # Helix radius pulses with bass
            radius = 100 + bass * 50

            # Strand 1
            x1 = int(self.center_x + np.cos(angle1) * radius)
            y1 = z

            # Strand 2
            x2 = int(self.center_x + np.cos(angle2) * radius)
            y2 = z

            # Backbone color
            cv2.circle(frame, (x1, y1), 5, (255, 100, 100), -1, lineType=cv2.LINE_AA)  # Blue
            cv2.circle(frame, (x2, y2), 5, (100, 255, 100), -1, lineType=cv2.LINE_AA)  # Green

            # Base pairs connecting strands
            if z % 20 == 0:
                freq_idx = (z // 20) % len(magnitudes)
                magnitude = magnitudes[freq_idx]

                if magnitude > 0.3:
                    # Color based on frequency
                    if freq_idx < len(magnitudes) // 4:
                        color = (100, 100, 255)  # Red (bass)
                    elif freq_idx < 3 * len(magnitudes) // 4:
                        color = (100, 255, 255)  # Yellow (mids)
                    else:
                        color = (255, 100, 100)  # Blue (treble)

                    thickness = 2 if magnitude > 0.6 else 1
                    cv2.line(frame, (x1, y1), (x2, y2), color, thickness, lineType=cv2.LINE_AA)

                    # Base pair nodes
                    mid_x = (x1 + x2) // 2
                    mid_y = (y1 + y2) // 2
                    cv2.circle(frame, (mid_x, mid_y), int(3 + magnitude * 5), color, -1)

        return frame

    def draw_mode_108_fractal_bloom(self, frame, magnitudes):
        """Mode 108: Fractal flower blooming and contracting"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Number of fractal iterations based on treble
        iterations = int(3 + treble * 4)

        # Draw recursive petals
        def draw_fractal_petal(x, y, size, angle, depth):
            if depth <= 0 or size < 5:
                return

            # Petal color based on depth
            hue = int(300 - depth * 40) % 180  # Pink to orange
            saturation = int(200 + mids * 55)
            value = int(200 + bass * 55)

            color_hsv = np.array([[[hue, saturation, value]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Draw petal
            petal_points = []
            for i in range(8):
                petal_angle = angle + (i / 8) * 2 * np.pi
                px = int(x + np.cos(petal_angle) * size)
                py = int(y + np.sin(petal_angle) * size)
                petal_points.append([px, py])

            petal_points = np.array(petal_points, dtype=np.int32)
            cv2.fillPoly(frame, [petal_points], tuple(map(int, color)), lineType=cv2.LINE_AA)

            # Recursive smaller petals
            for i in range(5):
                new_angle = angle + (i / 5) * 2 * np.pi
                new_x = int(x + np.cos(new_angle) * size * 0.6)
                new_y = int(y + np.sin(new_angle) * size * 0.6)
                draw_fractal_petal(new_x, new_y, size * 0.4, new_angle, depth - 1)

        # Blooming size controlled by bass
        bloom_size = int(80 + bass * 150)
        draw_fractal_petal(self.center_x, self.center_y, bloom_size, self.frame_counter * 0.05, iterations)

        return frame

    def draw_mode_109_circuit_board(self, frame, magnitudes):
        """Mode 109: Electronic circuit with flowing electricity"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Green PCB background
        frame[:] = (20, 50, 20)

        # Initialize circuit traces
        if len(self.circuit_board_traces) == 0:
            for i in range(20):
                self.circuit_board_traces.append({
                    'points': [(np.random.randint(0, self.width), np.random.randint(0, self.height))
                              for _ in range(10)],
                    'active': 0,
                    'freq_idx': i
                })

        # Draw traces and electricity
        for trace in self.circuit_board_traces:
            magnitude = magnitudes[min(trace['freq_idx'] * 6, len(magnitudes) - 1)]
            trace['active'] = magnitude

            # Draw trace path (golden)
            for i in range(len(trace['points']) - 1):
                cv2.line(frame, trace['points'][i], trace['points'][i + 1],
                        (50, 150, 200), 3, lineType=cv2.LINE_AA)

            # Electricity flows when active
            if magnitude > 0.4:
                flow_pos = int((self.frame_counter * 0.1) % len(trace['points']))

                # Blue electricity spark
                if flow_pos < len(trace['points']):
                    x, y = trace['points'][flow_pos]
                    intensity = int(200 + magnitude * 55)
                    cv2.circle(frame, (x, y), int(8 + magnitude * 10),
                              (intensity, intensity // 2, 0), -1, lineType=cv2.LINE_AA)

                    # Glow
                    cv2.circle(frame, (x, y), int(15 + magnitude * 15),
                              (intensity // 2, intensity // 4, 0), 2, lineType=cv2.LINE_AA)

        # Spark effects on high treble
        if treble > 0.7:
            for _ in range(int(treble * 10)):
                sx = np.random.randint(0, self.width)
                sy = np.random.randint(0, self.height)
                cv2.circle(frame, (sx, sy), 2, (255, 200, 100), -1)

        return frame

    def draw_mode_110_quantum_field(self, frame, magnitudes):
        """Mode 110: Quantum probability field with wave function collapse"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Spawn quantum particles
        if len(self.quantum_field_particles) < 500:
            for _ in range(5):
                self.quantum_field_particles.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'state': np.random.random(),  # Quantum state
                    'collapsed': False
                })

        # Audio causes wave function collapse
        collapse_threshold = 0.5 + mids * 0.4

        # Update and draw particles
        for particle in self.quantum_field_particles:
            # Quantum fluctuation
            particle['state'] += (np.random.random() - 0.5) * 0.1
            particle['state'] = max(0, min(1, particle['state']))

            # Collapse on high amplitude
            if mids > collapse_threshold and not particle['collapsed']:
                particle['collapsed'] = True
            elif mids < 0.3:
                particle['collapsed'] = False

            # Interference patterns
            wave_x = np.sin(particle['x'] * 0.02 + self.frame_counter * 0.1) * bass * 20
            wave_y = np.sin(particle['y'] * 0.02 + self.frame_counter * 0.1) * bass * 20

            draw_x = int(particle['x'] + wave_x)
            draw_y = int(particle['y'] + wave_y)

            # Heatmap color based on probability
            if particle['collapsed']:
                # Bright when collapsed
                hue = 0  # Red
                intensity = 255
                radius = 4
            else:
                # Ghosted when in superposition
                hue = int(120 * particle['state'])  # Blue to red
                intensity = int(100 + particle['state'] * 155)
                radius = 2

            color_hsv = np.array([[[hue, 255, intensity]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            if 0 <= draw_x < self.width and 0 <= draw_y < self.height:
                cv2.circle(frame, (draw_x, draw_y), radius, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)

        return frame
    def draw_mode_111_origami_unfold(self, frame, magnitudes):
        """Mode 111: Geometric origami folding rhythmically"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        fold_amount = bass * 0.8 + 0.2
        num_segments = 8
        
        for i in range(num_segments):
            angle = (i / num_segments) * 2 * np.pi + self.frame_counter * 0.02
            size = 150 * fold_amount
            
            x1 = int(self.center_x + np.cos(angle) * size)
            y1 = int(self.center_y + np.sin(angle) * size)
            x2 = int(self.center_x + np.cos(angle + 0.5) * size * 0.7)
            y2 = int(self.center_y + np.sin(angle + 0.5) * size * 0.7)
            
            hue = int((i / num_segments) * 180)
            color_hsv = np.array([[[hue, int(200 + mids * 55), 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            points = np.array([[self.center_x, self.center_y], [x1, y1], [x2, y2]], dtype=np.int32)
            cv2.fillPoly(frame, [points], tuple(map(int, color)), lineType=cv2.LINE_AA)
            cv2.polylines(frame, [points], True, (50, 50, 50), 2, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_112_galaxy_spiral(self, frame, magnitudes):
        """Mode 112: Spiral galaxy with pulsing stars"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if len(self.galaxy_spiral_stars) < 500:
            for _ in range(10):
                angle = np.random.random() * 2 * np.pi
                distance = np.random.random() * 300
                self.galaxy_spiral_stars.append({'angle': angle, 'distance': distance, 'brightness': np.random.random()})
        
        spiral_tightness = 0.3 + bass * 0.2
        rotation = self.frame_counter * 0.01
        
        for star in self.galaxy_spiral_stars:
            spiral_angle = star['angle'] + star['distance'] * spiral_tightness + rotation
            x = int(self.center_x + np.cos(spiral_angle) * star['distance'])
            y = int(self.center_y + np.sin(spiral_angle) * star['distance'])
            
            brightness = int((star['brightness'] + mids) * 127.5)
            hue = int(140 - star['distance'] / 3)
            color_hsv = np.array([[[hue, 255, brightness]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            if 0 <= x < self.width and 0 <= y < self.height:
                size = 1 if star['distance'] > 200 else 2
                cv2.circle(frame, (x, y), size, tuple(map(int, color)), -1)
        
        cv2.circle(frame, (self.center_x, self.center_y), int(20 + bass * 30), (255, 255, 200), -1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_113_rubber_bands(self, frame, magnitudes):
        """Mode 113: Vibrating rubber bands with physics"""
        if len(self.rubber_bands) == 0:
            for i in range(10):
                self.rubber_bands.append({
                    'y': 100 + i * (self.height - 200) // 10,
                    'tension': 0
                })
        
        for i, band in enumerate(self.rubber_bands):
            magnitude = magnitudes[min(i * 12, len(magnitudes) - 1)]
            band['tension'] = magnitude
            
            points = []
            for x in range(0, self.width, 10):
                wave = np.sin(x * 0.05 + self.frame_counter * 0.15 * (i + 1)) * band['tension'] * 80
                points.append([x, int(band['y'] + wave)])
            
            hue = int(i * 18)
            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            pts = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [pts], False, tuple(map(int, color)), 3, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_114_ink_diffusion(self, frame, magnitudes):
        """Mode 114: Ink diffusing in water"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if bass > 0.6 and self.frame_counter % 10 == 0:
            self.ink_diffusion_particles.append({
                'x': self.center_x,
                'y': self.center_y,
                'vx': np.random.uniform(-5, 5),
                'vy': np.random.uniform(-5, 5),
                'life': 100,
                'hue': int(np.random.random() * 40 + 120)
            })
        
        for particle in self.ink_diffusion_particles[:]:
            particle['x'] += particle['vx'] + np.random.uniform(-treble * 2, treble * 2)
            particle['y'] += particle['vy'] + np.random.uniform(-treble * 2, treble * 2)
            particle['vx'] *= 0.98
            particle['vy'] *= 0.98
            particle['life'] -= 1
            
            if particle['life'] > 0:
                alpha = particle['life'] / 100
                color_hsv = np.array([[[particle['hue'], 255, int(200 * alpha)]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                size = int((1 - alpha) * 30 + 5)
                cv2.circle(frame, (int(particle['x']), int(particle['y'])), size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
        
        self.ink_diffusion_particles = [p for p in self.ink_diffusion_particles if p['life'] > 0]
        return frame

    def draw_mode_115_geometric_kaleidoscope(self, frame, magnitudes):
        """Mode 115: Rotating kaleidoscope with morphing shapes"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        self.geo_kaleidoscope_rotation += 0.02 + mids * 0.05
        num_segments = 8
        
        for seg in range(num_segments):
            angle_offset = (seg / num_segments) * 2 * np.pi
            
            for layer in range(3):
                size = (layer + 1) * 60 * (1 + bass * 0.5)
                num_sides = 3 + int(mids * 3)
                
                points = []
                for i in range(num_sides):
                    angle = angle_offset + self.geo_kaleidoscope_rotation + (i / num_sides) * 2 * np.pi
                    x = int(self.center_x + np.cos(angle) * size)
                    y = int(self.center_y + np.sin(angle) * size)
                    points.append([x, y])
                
                hue = int((seg * 22.5 + layer * 60) % 180)
                color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                pts = np.array(points, dtype=np.int32)
                cv2.polylines(frame, [pts], True, tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_116_lightning_storm(self, frame, magnitudes):
        """Mode 116: Lightning bolts with branching"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (30, 30, 40)
        
        if bass > 0.7 and np.random.random() < 0.3:
            start_x = np.random.randint(100, self.width - 100)
            self.lightning_bolts.append({'x': start_x, 'y': 0, 'life': 5, 'branches': []})
        
        for bolt in self.lightning_bolts[:]:
            bolt['life'] -= 1
            
            if bolt['life'] > 0:
                segments = 20
                prev_x, prev_y = bolt['x'], bolt['y']
                
                for seg in range(segments):
                    next_y = prev_y + self.height // segments
                    next_x = prev_x + np.random.randint(-30, 30)
                    
                    cv2.line(frame, (prev_x, prev_y), (next_x, next_y), (255, 255, 200), 2, lineType=cv2.LINE_AA)
                    cv2.line(frame, (prev_x, prev_y), (next_x, next_y), (150, 150, 255), 1, lineType=cv2.LINE_AA)
                    
                    if treble > 0.5 and np.random.random() < 0.2:
                        branch_x = next_x + np.random.randint(-80, 80)
                        branch_y = next_y + np.random.randint(20, 60)
                        cv2.line(frame, (next_x, next_y), (branch_x, branch_y), (200, 200, 255), 1, lineType=cv2.LINE_AA)
                    
                    prev_x, prev_y = next_x, next_y
        
        self.lightning_bolts = [b for b in self.lightning_bolts if b['life'] > 0]
        return frame

    def draw_mode_117_cellular_growth(self, frame, magnitudes):
        """Mode 117: Biological cell division and growth"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if len(self.cellular_growth_cells) == 0:
            self.cellular_growth_cells.append({'x': self.center_x, 'y': self.center_y, 'size': 50, 'gen': 0})
        
        if bass > 0.7 and len(self.cellular_growth_cells) < 50:
            for cell in list(self.cellular_growth_cells):
                if np.random.random() < 0.1:
                    angle = np.random.random() * 2 * np.pi
                    new_x = cell['x'] + np.cos(angle) * cell['size']
                    new_y = cell['y'] + np.sin(angle) * cell['size']
                    self.cellular_growth_cells.append({'x': new_x, 'y': new_y, 'size': 30, 'gen': cell['gen'] + 1})
        
        for cell in self.cellular_growth_cells:
            cell['size'] = 20 + bass * 30
            
            hue = int(60 + cell['gen'] * 20) % 180
            color_hsv = np.array([[[hue, 200, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            cv2.circle(frame, (int(cell['x']), int(cell['y'])), int(cell['size']), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(cell['x']), int(cell['y'])), int(cell['size'] * 0.5), tuple(map(int, color * 0.7)), -1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_118_sound_ribbons(self, frame, magnitudes):
        """Mode 118: 3D ribbons twisting through space"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        num_ribbons = 5
        for ribbon_idx in range(num_ribbons):
            points = []
            for t in range(100):
                angle = t * 0.1 + self.frame_counter * 0.02 + ribbon_idx
                radius = 100 + np.sin(t * 0.1) * 50 * bass
                
                x = int(self.center_x + np.cos(angle) * radius)
                y = int(t * (self.height / 100))
                points.append([x, y])
            
            hue = int(ribbon_idx * 36) % 180
            color_hsv = np.array([[[hue, 255, int(200 + mids * 55)]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            pts = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [pts], False, tuple(map(int, color)), int(8 + bass * 10), lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_119_matrix_rain(self, frame, magnitudes):
        """Mode 119: Matrix code rain"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (0, 0, 0)
        
        if len(self.matrix_rain_columns) == 0:
            for x in range(0, self.width, 20):
                self.matrix_rain_columns.append({'x': x, 'y': np.random.randint(-100, 0), 'speed': 5 + np.random.randint(0, 10)})
        
        for col in self.matrix_rain_columns:
            col['speed'] = 5 + bass * 10
            col['y'] += col['speed']
            
            if col['y'] > self.height:
                col['y'] = -20
            
            for i in range(15):
                y_pos = int(col['y'] - i * 20)
                if 0 <= y_pos < self.height:
                    brightness = int(255 - i * 17)
                    if i == 0:
                        color = (brightness, brightness, brightness)
                    else:
                        color = (0, brightness, 0)
                    
                    char = chr(33 + np.random.randint(0, 94))
                    cv2.putText(frame, char, (col['x'], y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        
        if treble > 0.7:
            for _ in range(int(treble * 5)):
                x = np.random.randint(0, self.width)
                y = np.random.randint(0, self.height)
                cv2.putText(frame, chr(33 + np.random.randint(0, 94)), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        return frame

    def draw_mode_120_fire_mandala(self, frame, magnitudes):
        """Mode 120: Circular mandala made of flames"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        num_flames = int(20 + treble * 30)
        
        for i in range(num_flames):
            angle = (i / num_flames) * 2 * np.pi + self.frame_counter * 0.05
            radius = 100 + bass * 150
            
            x = int(self.center_x + np.cos(angle) * radius)
            y = int(self.center_y + np.sin(angle) * radius)
            
            flame_height = int(40 + bass * 60)
            for h in range(flame_height):
                offset = np.sin(h * 0.2 + self.frame_counter * 0.2) * 10
                flame_x = int(x + offset)
                flame_y = int(y - h)
                
                intensity = 1 - (h / flame_height)
                if h < flame_height * 0.3:
                    color = (255, int(255 * intensity), int(100 * intensity))
                elif h < flame_height * 0.6:
                    color = (int(255 * intensity), int(200 * intensity), 0)
                else:
                    color = (int(255 * intensity), 0, 0)
                
                if 0 <= flame_x < self.width and 0 <= flame_y < self.height:
                    cv2.circle(frame, (flame_x, flame_y), 3, color, -1, lineType=cv2.LINE_AA)
        
        return frame
    def draw_mode_121_tessellation_shift(self, frame, magnitudes):
        """Mode 121: Escher-style morphing tessellations"""
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        tile_size = int(40 + mids * 20)
        for y in range(0, self.height, tile_size):
            for x in range(0, self.width, tile_size):
                shift = int(self.frame_counter * mids) % 3
                hue = int((x + y) / 10 + self.frame_counter) % 180
                color_hsv = np.array([[[hue, 200, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                if shift == 0:
                    cv2.rectangle(frame, (x, y), (x + tile_size, y + tile_size), tuple(map(int, color)), -1)
                elif shift == 1:
                    pts = np.array([[x, y + tile_size], [x + tile_size // 2, y], [x + tile_size, y + tile_size]], dtype=np.int32)
                    cv2.fillPoly(frame, [pts], tuple(map(int, color)))
                else:
                    cv2.circle(frame, (x + tile_size // 2, y + tile_size // 2), tile_size // 2, tuple(map(int, color)), -1)
                
                cv2.rectangle(frame, (x, y), (x + tile_size, y + tile_size), (0, 0, 0), 1)
        
        return frame

    def draw_mode_122_seismic_waves(self, frame, magnitudes):
        """Mode 122: Seismograph readings with P-waves and S-waves"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        for wave_idx in range(3):
            y_pos = 100 + wave_idx * (self.height - 200) // 3
            points = []
            
            for x in range(self.width):
                if wave_idx == 0:
                    y = y_pos + int(bass * 80 * np.sin(x * 0.05 + self.frame_counter * 0.2))
                elif wave_idx == 1:
                    y = y_pos + int(mids * 60 * np.sin(x * 0.08 + self.frame_counter * 0.15))
                else:
                    y = y_pos + int(treble * 40 * np.sin(x * 0.1 + self.frame_counter * 0.25))
                
                points.append([x, y])
            
            colors = [(0, 100, 255), (0, 255, 100), (255, 100, 0)]
            pts = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [pts], False, colors[wave_idx], 2, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_123_neon_city(self, frame, magnitudes):
        """Mode 123: Cyberpunk city with pulsing lights"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (80, 40, 80)
        
        if len(self.neon_city_buildings) == 0:
            for i in range(15):
                self.neon_city_buildings.append({
                    'x': i * self.width // 15,
                    'base_height': np.random.randint(100, 400),
                    'width': self.width // 16
                })
        
        for building in self.neon_city_buildings:
            height = int(building['base_height'] * (1 + bass * 0.5))
            cv2.rectangle(frame, (building['x'], self.height - height), 
                         (building['x'] + building['width'], self.height), (40, 20, 60), -1)
            
            num_windows = int(height / 20)
            for win_y in range(num_windows):
                if np.random.random() < mids:
                    win_color = (255, 100, 255) if np.random.random() < 0.5 else (100, 255, 255)
                    win_actual_y = self.height - height + win_y * 20
                    cv2.rectangle(frame, (building['x'] + 2, win_actual_y + 2),
                                (building['x'] + building['width'] - 2, win_actual_y + 15),
                                win_color, -1)
        
        return frame

    def draw_mode_124_magnetic_field(self, frame, magnitudes):
        """Mode 124: Magnetic field lines with particle clustering"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        pole_n = (self.width // 3, self.center_y)
        pole_s = (2 * self.width // 3, self.center_y)
        
        for line_idx in range(int(20 + mids * 20)):
            angle = (line_idx / 20) * np.pi - np.pi / 2
            points = []
            
            for t in range(100):
                t_norm = t / 100
                x = int(pole_n[0] + (pole_s[0] - pole_n[0]) * t_norm + np.sin(angle + t * 0.1) * 100 * bass)
                y = int(pole_n[1] + np.cos(angle + t * 0.1) * 150 * (1 - abs(t_norm - 0.5) * 2))
                points.append([x, y])
            
            pts = np.array(points, dtype=np.int32)
            color = (255, 100, 100) if angle < 0 else (100, 100, 255)
            cv2.polylines(frame, [pts], False, color, 1, lineType=cv2.LINE_AA)
        
        cv2.circle(frame, pole_n, 20, (255, 100, 100), -1, lineType=cv2.LINE_AA)
        cv2.circle(frame, pole_s, 20, (100, 100, 255), -1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_125_bubble_fusion(self, frame, magnitudes):
        """Mode 125: Bubbles that float, merge, and pop"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if bass > 0.5 and len(self.bubble_fusion_bubbles) < 30:
            self.bubble_fusion_bubbles.append({
                'x': self.center_x + np.random.randint(-100, 100),
                'y': self.height - 50,
                'vx': np.random.uniform(-1, 1),
                'vy': -2 - bass * 3,
                'radius': int(20 + bass * 40)
            })
        
        for bubble in self.bubble_fusion_bubbles[:]:
            bubble['vy'] -= 0.1
            bubble['x'] += bubble['vx']
            bubble['y'] += bubble['vy']
            bubble['vx'] *= 0.99
            
            if bubble['y'] < 0 or treble > 0.8:
                self.bubble_fusion_bubbles.remove(bubble)
                continue
            
            hue = int((bubble['y'] / self.height) * 180)
            color_hsv = np.array([[[hue, 100, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            cv2.circle(frame, (int(bubble['x']), int(bubble['y'])), bubble['radius'], tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(bubble['x'] - bubble['radius'] // 3), int(bubble['y'] - bubble['radius'] // 3)),
                      bubble['radius'] // 4, (255, 255, 255), -1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_126_tribal_drums(self, frame, magnitudes):
        """Mode 126: Tribal patterns pulsing like drum skins"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        
        num_rings = int(5 + bass * 10)
        for ring in range(num_rings):
            radius = int(50 + ring * 40 * (1 + bass * 0.3))
            
            num_symbols = 8
            for sym in range(num_symbols):
                angle = (sym / num_symbols) * 2 * np.pi + self.frame_counter * 0.02
                x = int(self.center_x + np.cos(angle) * radius)
                y = int(self.center_y + np.sin(angle) * radius)
                
                symbol_size = int(15 + bass * 10)
                pts = np.array([
                    [x, y - symbol_size],
                    [x + symbol_size, y],
                    [x, y + symbol_size],
                    [x - symbol_size, y]
                ], dtype=np.int32)
                
                color = (int(100 + bass * 155), int(70 + bass * 100), 30)
                cv2.fillPoly(frame, [pts], color, lineType=cv2.LINE_AA)
                cv2.polylines(frame, [pts], True, (0, 0, 0), 2, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_127_glass_shatter(self, frame, magnitudes):
        """Mode 127: Glass forming and shattering"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if bass > 0.7 and len(self.glass_shatter_fragments) == 0:
            for _ in range(30):
                self.glass_shatter_fragments.append({
                    'x': self.center_x + np.random.randint(-200, 200),
                    'y': self.center_y + np.random.randint(-200, 200),
                    'vx': np.random.uniform(-5, 5),
                    'vy': np.random.uniform(-5, 5),
                    'size': np.random.randint(20, 50),
                    'life': 30
                })
        
        if len(self.glass_shatter_fragments) > 0:
            for frag in self.glass_shatter_fragments[:]:
                frag['x'] += frag['vx']
                frag['y'] += frag['vy']
                frag['vy'] += 0.3
                frag['life'] -= 1
                
                if frag['life'] > 0:
                    alpha = frag['life'] / 30
                    color = (int(200 * alpha), int(220 * alpha), int(255 * alpha))
                    
                    pts = np.array([
                        [int(frag['x']), int(frag['y'] - frag['size'])],
                        [int(frag['x'] + frag['size']), int(frag['y'])],
                        [int(frag['x']), int(frag['y'] + frag['size'])],
                        [int(frag['x'] - frag['size']), int(frag['y'])]
                    ], dtype=np.int32)
                    
                    cv2.fillPoly(frame, [pts], color, lineType=cv2.LINE_AA)
                    cv2.polylines(frame, [pts], True, (150, 150, 150), 1, lineType=cv2.LINE_AA)
            
            self.glass_shatter_fragments = [f for f in self.glass_shatter_fragments if f['life'] > 0]
        else:
            cv2.rectangle(frame, (self.center_x - 200, self.center_y - 200),
                         (self.center_x + 200, self.center_y + 200),
                         (200, 220, 255), -1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_128_bioluminescence(self, frame, magnitudes):
        """Mode 128: Deep ocean bioluminescent creatures"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (20, 10, 0)
        
        if len(self.bioluminescent_creatures) < 20:
            self.bioluminescent_creatures.append({
                'x': np.random.randint(0, self.width),
                'y': np.random.randint(0, self.height),
                'phase': np.random.random() * 2 * np.pi,
                'speed': np.random.uniform(0.5, 2)
            })
        
        for creature in self.bioluminescent_creatures:
            creature['x'] += np.sin(self.frame_counter * 0.02 + creature['phase']) * creature['speed']
            creature['y'] += np.cos(self.frame_counter * 0.03 + creature['phase']) * creature['speed'] * 0.5
            
            if creature['x'] < 0: creature['x'] = self.width
            if creature['x'] > self.width: creature['x'] = 0
            if creature['y'] < 0: creature['y'] = self.height
            if creature['y'] > self.height: creature['y'] = 0
            
            glow_intensity = int(150 + np.sin(self.frame_counter * 0.1 + creature['phase']) * 50 + bass * 55)
            
            hue = int(90 + mids * 60)
            color_hsv = np.array([[[hue, 255, glow_intensity]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            size = int(15 + bass * 20)
            cv2.circle(frame, (int(creature['x']), int(creature['y'])), size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (int(creature['x']), int(creature['y'])), size + 10, tuple(map(int, color * 0.5)), 2, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_129_sound_architecture(self, frame, magnitudes):
        """Mode 129: Impossible architecture constructing/deconstructing"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        build_progress = bass
        
        for level in range(5):
            y_base = self.height - level * 100
            block_width = 150 - level * 20
            
            if level * 0.2 < build_progress:
                x = self.center_x - block_width // 2
                y = int(y_base - (1 - build_progress) * 50)
                
                shadow_offset = 10
                cv2.rectangle(frame, (x + shadow_offset, y + shadow_offset),
                            (x + block_width + shadow_offset, y_base + shadow_offset),
                            (30, 30, 30), -1)
                
                gray_value = int(100 + mids * 155)
                cv2.rectangle(frame, (x, y), (x + block_width, y_base),
                            (gray_value, gray_value, gray_value), -1)
                cv2.rectangle(frame, (x, y), (x + block_width, y_base),
                            (50, 50, 50), 3)
        
        return frame

    def draw_mode_130_plasma_ball(self, frame, magnitudes):
        """Mode 130: Plasma globe with electrical tendrils"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        center_radius = int(60 + bass * 40)
        cv2.circle(frame, (self.center_x, self.center_y), center_radius, (100, 50, 100), -1, lineType=cv2.LINE_AA)
        
        num_arcs = int(5 + treble * 15)
        for arc_idx in range(num_arcs):
            angle = (arc_idx / num_arcs) * 2 * np.pi + self.frame_counter * 0.1
            
            current_x, current_y = self.center_x, self.center_y
            segments = 20
            
            for seg in range(segments):
                next_angle = angle + np.random.uniform(-0.5, 0.5)
                distance = center_radius + seg * 15
                
                next_x = int(self.center_x + np.cos(next_angle) * distance)
                next_y = int(self.center_y + np.sin(next_angle) * distance)
                
                hue = int(120 + seg * 5)
                intensity = int(255 - seg * 10)
                color_hsv = np.array([[[hue, 255, intensity]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                cv2.line(frame, (current_x, current_y), (next_x, next_y), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
                
                current_x, current_y = next_x, next_y
                angle = next_angle
        
        return frame
    def draw_mode_131_sand_mandala(self, frame, magnitudes):
        """Mode 131: Tibetan sand mandala forming grain by grain"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        num_sections = 8
        for section in range(num_sections):
            angle_offset = (section / num_sections) * 2 * np.pi
            
            for radius_level in range(int(5 + mids * 10)):
                radius = 30 + radius_level * 20
                num_grains = int(radius * 0.5)
                
                for grain in range(num_grains):
                    angle = angle_offset + (grain / num_grains) * (2 * np.pi / num_sections)
                    x = int(self.center_x + np.cos(angle) * radius)
                    y = int(self.center_y + np.sin(angle) * radius)
                    
                    colors = [(0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0)]
                    color = colors[radius_level % len(colors)]
                    
                    cv2.circle(frame, (x, y), 1, color, -1)
        
        return frame

    def draw_mode_132_laser_show(self, frame, magnitudes):
        """Mode 132: Concert laser beams sweeping and bouncing"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (10, 10, 10)
        
        num_beams = int(3 + treble * 7)
        for beam_idx in range(num_beams):
            angle = (beam_idx / num_beams) * np.pi + np.sin(self.frame_counter * 0.05 + beam_idx) * 0.5
            
            start_x = self.center_x
            start_y = self.height
            end_x = int(self.center_x + np.cos(angle) * self.width)
            end_y = int(self.height - abs(np.sin(angle)) * self.height)
            
            beam_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (0, 255, 255)]
            color = beam_colors[beam_idx % len(beam_colors)]
            
            intensity = bass
            actual_color = tuple(int(c * intensity) for c in color)
            
            cv2.line(frame, (start_x, start_y), (end_x, end_y), actual_color, 3, lineType=cv2.LINE_AA)
            cv2.line(frame, (start_x, start_y), (end_x, end_y), (255, 255, 255), 1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_133_coral_reef(self, frame, magnitudes):
        """Mode 133: Growing coral reef with swaying polyps"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        frame[:] = (100, 50, 20)
        
        if len(self.coral_reef_polyps) < 30:
            self.coral_reef_polyps.append({
                'x': np.random.randint(50, self.width - 50),
                'y': self.height - np.random.randint(50, 200),
                'height': np.random.randint(40, 100),
                'hue': np.random.randint(0, 180),
                'phase': np.random.random() * 2 * np.pi
            })
        
        for coral in self.coral_reef_polyps:
            sway = np.sin(self.frame_counter * 0.05 + coral['phase']) * 20 * mids
            
            for h in range(coral['height']):
                x = int(coral['x'] + sway * (h / coral['height']))
                y = coral['y'] - h
                
                size = int(5 + (coral['height'] - h) / coral['height'] * 15 * (1 + bass * 0.3))
                
                color_hsv = np.array([[[coral['hue'], 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                if 0 <= x < self.width and 0 <= y < self.height:
                    cv2.circle(frame, (x, y), size, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_134_wireframe_morph(self, frame, magnitudes):
        """Mode 134: 3D wireframe objects morphing between shapes"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        shape_type = int(self.frame_counter * 0.01) % 4
        angle = self.frame_counter * 0.03
        
        vertices_3d = []
        size = 150 + bass * 100
        
        if shape_type == 0:  # Cube
            for x in [-1, 1]:
                for y in [-1, 1]:
                    for z in [-1, 1]:
                        vertices_3d.append([x * size, y * size, z * size])
        elif shape_type == 1:  # Sphere
            for lat in range(-90, 90, 30):
                for lon in range(0, 360, 30):
                    x = size * np.cos(np.radians(lat)) * np.cos(np.radians(lon))
                    y = size * np.cos(np.radians(lat)) * np.sin(np.radians(lon))
                    z = size * np.sin(np.radians(lat))
                    vertices_3d.append([x, y, z])
        elif shape_type == 2:  # Pyramid
            vertices_3d = [[0, -size, 0], [size, size, size], [-size, size, size], [-size, size, -size], [size, size, -size]]
        else:  # Torus
            for u in range(0, 360, 30):
                for v in range(0, 360, 60):
                    R, r = size * 0.8, size * 0.3
                    x = (R + r * np.cos(np.radians(v))) * np.cos(np.radians(u))
                    y = (R + r * np.cos(np.radians(v))) * np.sin(np.radians(u))
                    z = r * np.sin(np.radians(v))
                    vertices_3d.append([x, y, z])
        
        vertices_2d = []
        for v in vertices_3d:
            x = v[0] * np.cos(angle) - v[2] * np.sin(angle)
            z = v[0] * np.sin(angle) + v[2] * np.cos(angle)
            y = v[1]
            
            scale = 300 / (300 + z)
            x_2d = int(self.center_x + x * scale)
            y_2d = int(self.center_y + y * scale)
            vertices_2d.append((x_2d, y_2d))
        
        for i, v1 in enumerate(vertices_2d):
            for v2 in vertices_2d[i+1:i+5]:
                hue = int(100 + mids * 80)
                color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                cv2.line(frame, v1, v2, tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_135_sound_garden(self, frame, magnitudes):
        """Mode 135: Abstract garden with blooming flowers"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if len(self.sound_garden_plants) < 15:
            self.sound_garden_plants.append({
                'x': np.random.randint(100, self.width - 100),
                'y': self.height - 50,
                'height': np.random.randint(80, 200),
                'bloom_size': 0,
                'hue': np.random.randint(0, 180)
            })
        
        for plant in self.sound_garden_plants:
            plant['bloom_size'] = bass * 40 + 10
            
            cv2.line(frame, (plant['x'], plant['y']), (plant['x'], plant['y'] - plant['height']),
                    (50, 150, 50), 3, lineType=cv2.LINE_AA)
            
            bloom_x = plant['x']
            bloom_y = plant['y'] - plant['height']
            
            for petal in range(8):
                angle = (petal / 8) * 2 * np.pi
                petal_x = int(bloom_x + np.cos(angle) * plant['bloom_size'])
                petal_y = int(bloom_y + np.sin(angle) * plant['bloom_size'])
                
                color_hsv = np.array([[[plant['hue'], 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                cv2.circle(frame, (petal_x, petal_y), int(plant['bloom_size'] * 0.5),
                          tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
            
            cv2.circle(frame, (bloom_x, bloom_y), int(plant['bloom_size'] * 0.3),
                      (255, 255, 100), -1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_136_hologram_glitch(self, frame, magnitudes):
        """Mode 136: Glitching holographic interface"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (10, 10, 10)
        
        for panel_idx in range(5):
            panel_x = 100 + panel_idx * (self.width - 200) // 5
            panel_y = 100 + int(np.sin(self.frame_counter * 0.05 + panel_idx) * 30 * mids)
            panel_w = 100
            panel_h = 150
            
            if treble > 0.7 and np.random.random() < 0.3:
                glitch_offset = np.random.randint(-20, 20)
                panel_x += glitch_offset
                
                r_offset = np.random.randint(-5, 5)
                cv2.rectangle(frame, (panel_x + r_offset, panel_y), (panel_x + panel_w + r_offset, panel_y + panel_h), (255, 0, 0), 1)
                cv2.rectangle(frame, (panel_x - r_offset, panel_y), (panel_x + panel_w - r_offset, panel_y + panel_h), (0, 255, 255), 1)
            else:
                cv2.rectangle(frame, (panel_x, panel_y), (panel_x + panel_w, panel_y + panel_h), (0, 255, 255), 2, lineType=cv2.LINE_AA)
                
                for line_idx in range(5):
                    line_y = panel_y + 30 + line_idx * 20
                    cv2.line(frame, (panel_x + 10, line_y), (panel_x + panel_w - 10, line_y), (255, 150, 0), 1)
        
        if treble > 0.6:
            for _ in range(int(treble * 20)):
                scan_y = np.random.randint(0, self.height)
                cv2.line(frame, (0, scan_y), (self.width, scan_y), (100, 255, 255), 1)
        
        return frame

    def draw_mode_137_pendulum_wave(self, frame, magnitudes):
        """Mode 137: Multiple pendulums creating wave patterns"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        num_pendulums = 20
        for i in range(num_pendulums):
            x = 50 + i * (self.width - 100) // num_pendulums
            
            period = 1.0 + i * 0.05
            angle = np.sin(self.frame_counter * 0.05 * period) * (0.5 + bass * 0.5)
            
            length = 150 + mids * 100
            bob_x = int(x + np.sin(angle) * length)
            bob_y = int(100 + np.cos(angle) * length)
            
            cv2.line(frame, (x, 100), (bob_x, bob_y), (200, 200, 200), 1, lineType=cv2.LINE_AA)
            
            hue = int((i / num_pendulums) * 180)
            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            cv2.circle(frame, (bob_x, bob_y), 10, tuple(map(int, color)), -1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_138_volcano_eruption(self, frame, magnitudes):
        """Mode 138: Volcano erupting with lava and ash"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        volcano_base = [(self.center_x - 200, self.height), (self.center_x + 200, self.height), (self.center_x, self.height - 200)]
        pts = np.array(volcano_base, dtype=np.int32)
        cv2.fillPoly(frame, [pts], (80, 60, 40), lineType=cv2.LINE_AA)
        
        if bass > 0.6:
            for _ in range(int(bass * 20)):
                self.volcano_lava_particles.append({
                    'x': self.center_x + np.random.randint(-20, 20),
                    'y': self.height - 200,
                    'vx': np.random.uniform(-3, 3),
                    'vy': -8 - bass * 5,
                    'life': 60
                })
        
        for particle in self.volcano_lava_particles[:]:
            particle['vy'] += 0.3
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 1
            
            if particle['life'] > 0:
                if particle['vy'] < 0:
                    color = (0, int(100 + particle['life'] * 2), 255)
                else:
                    color = (0, int(particle['life'] * 3), int(100 + particle['life'] * 2))
                
                if 0 <= particle['x'] < self.width and 0 <= particle['y'] < self.height:
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])), 4, color, -1)
        
        self.volcano_lava_particles = [p for p in self.volcano_lava_particles if p['life'] > 0 and p['y'] < self.height]
        
        return frame

    def draw_mode_139_butterfly_effect(self, frame, magnitudes):
        """Mode 139: Chaos theory Lorenz attractor"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        sigma, rho, beta = 10.0, 28.0, 8.0/3.0
        dt = 0.01
        
        if len(self.butterfly_attractor_trail) == 0:
            self.butterfly_attractor_trail = [[0.1, 0.0, 0.0]]
        
        x, y, z = self.butterfly_attractor_trail[-1]
        
        dx = sigma * (y - x) * (1 + bass * 0.5)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        
        x += dx * dt
        y += dy * dt
        z += dz * dt
        
        self.butterfly_attractor_trail.append([x, y, z])
        
        if len(self.butterfly_attractor_trail) > 500:
            self.butterfly_attractor_trail.pop(0)
        
        for i in range(1, len(self.butterfly_attractor_trail)):
            x1, y1, z1 = self.butterfly_attractor_trail[i-1]
            x2, y2, z2 = self.butterfly_attractor_trail[i]
            
            px1 = int(self.center_x + x1 * 10)
            py1 = int(self.center_y + z1 * 10)
            px2 = int(self.center_x + x2 * 10)
            py2 = int(self.center_y + z2 * 10)
            
            hue = int((i / len(self.butterfly_attractor_trail)) * 180)
            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            if 0 <= px1 < self.width and 0 <= py1 < self.height and 0 <= px2 < self.width and 0 <= py2 < self.height:
                cv2.line(frame, (px1, py1), (px2, py2), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_140_silk_weaving(self, frame, magnitudes):
        """Mode 140: Silk threads weaving patterns"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        grid_size = 20
        for i in range(0, self.width, grid_size):
            vertical_offset = int(np.sin(i * 0.05 + self.frame_counter * 0.1) * 30 * bass)
            
            hue = int((i / self.width) * 180)
            color_hsv = np.array([[[hue, int(150 + mids * 105), 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            cv2.line(frame, (i, vertical_offset), (i, self.height + vertical_offset), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
        
        for j in range(0, self.height, grid_size):
            horizontal_offset = int(np.sin(j * 0.05 + self.frame_counter * 0.1) * 30 * mids)
            
            hue = int(60 + (j / self.height) * 120)
            color_hsv = np.array([[[hue, int(150 + bass * 105), 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            cv2.line(frame, (horizontal_offset, j), (self.width + horizontal_offset, j), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_141_clock_gears(self, frame, magnitudes):
        """Mode 141: Interlocking clockwork gears turning"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        gears = [
            {'x': self.width // 3, 'y': self.center_y, 'radius': 80, 'teeth': 12, 'speed': 1},
            {'x': 2 * self.width // 3, 'y': self.center_y, 'radius': 60, 'teeth': 9, 'speed': -1.33},
            {'x': self.center_x, 'y': self.center_y - 100, 'radius': 50, 'teeth': 8, 'speed': 1.5}
        ]
        
        for gear in gears:
            rotation = (self.frame_counter * 0.05 * gear['speed'] * (1 + bass * 0.5))
            
            for tooth in range(gear['teeth']):
                angle = rotation + (tooth / gear['teeth']) * 2 * np.pi
                
                inner_x = int(gear['x'] + np.cos(angle) * gear['radius'] * 0.8)
                inner_y = int(gear['y'] + np.sin(angle) * gear['radius'] * 0.8)
                outer_x = int(gear['x'] + np.cos(angle) * gear['radius'])
                outer_y = int(gear['y'] + np.sin(angle) * gear['radius'])
                
                cv2.line(frame, (inner_x, inner_y), (outer_x, outer_y), (150, 100, 50), 3, lineType=cv2.LINE_AA)
            
            cv2.circle(frame, (gear['x'], gear['y']), int(gear['radius'] * 0.7), (180, 130, 70), -1, lineType=cv2.LINE_AA)
            cv2.circle(frame, (gear['x'], gear['y']), int(gear['radius'] * 0.3), (50, 50, 50), -1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_142_smoke_signals(self, frame, magnitudes):
        """Mode 142: Rising smoke plumes forming patterns"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if self.frame_counter % 3 == 0:
            self.smoke_signal_particles.append({
                'x': self.center_x + np.random.randint(-50, 50),
                'y': self.height - 100,
                'vx': np.random.uniform(-1, 1),
                'vy': -2 - mids * 2,
                'size': 10,
                'life': 100
            })
        
        for particle in self.smoke_signal_particles[:]:
            particle['x'] += particle['vx'] + np.sin(self.frame_counter * 0.1) * treble * 2
            particle['y'] += particle['vy']
            particle['vy'] -= 0.05
            particle['size'] += 0.5
            particle['life'] -= 1
            
            if particle['life'] > 0:
                alpha = particle['life'] / 100
                gray = int(180 * alpha)
                
                if 0 <= particle['x'] < self.width and 0 <= particle['y'] < self.height:
                    cv2.circle(frame, (int(particle['x']), int(particle['y'])), int(particle['size']),
                              (gray, gray, gray), -1, lineType=cv2.LINE_AA)
        
        self.smoke_signal_particles = [p for p in self.smoke_signal_particles if p['life'] > 0]
        
        return frame

    def draw_mode_143_stained_glass(self, frame, magnitudes):
        """Mode 143: Glowing stained glass window"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        pane_size = 80
        for y in range(0, self.height, pane_size):
            for x in range(0, self.width, pane_size):
                hue = int((x + y) / 10) % 180
                brightness = int(150 + bass * 105)
                
                color_hsv = np.array([[[hue, 200, brightness]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                cv2.rectangle(frame, (x, y), (x + pane_size, y + pane_size), tuple(map(int, color)), -1)
                cv2.rectangle(frame, (x, y), (x + pane_size, y + pane_size), (30, 30, 30), 4)
                
                light_x = x + pane_size // 4
                light_y = y + pane_size // 4
                cv2.circle(frame, (light_x, light_y), pane_size // 6, (255, 255, 255), -1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_144_string_theory(self, frame, magnitudes):
        """Mode 144: Theoretical strings vibrating in multiple dimensions"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        num_strings = 30
        for string_idx in range(num_strings):
            points = []
            
            for t in range(100):
                x = t * (self.width / 100)
                
                y = self.center_y
                for harmonic in range(5):
                    amplitude = (bass + mids + treble) / 3 * 50 / (harmonic + 1)
                    frequency = (harmonic + 1) * (string_idx + 1) * 0.05
                    y += np.sin(x * frequency + self.frame_counter * 0.1) * amplitude
                
                points.append([int(x), int(y)])
            
            hue = int((string_idx / num_strings) * 180)
            alpha = 0.3 + treble * 0.7
            color_hsv = np.array([[[hue, 255, int(255 * alpha)]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            pts = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [pts], False, tuple(map(int, color)), 1, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_145_paper_craft(self, frame, magnitudes):
        """Mode 145: Paper cutouts folding into 3D shapes"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        fold_progress = (np.sin(self.frame_counter * 0.05) + 1) / 2 * bass
        
        colors_pastel = [(255, 200, 200), (200, 255, 200), (200, 200, 255), (255, 255, 200)]
        
        for i in range(4):
            angle = (i / 4) * 2 * np.pi
            size = 100 * (1 + fold_progress)
            
            x1 = int(self.center_x + np.cos(angle) * size)
            y1 = int(self.center_y + np.sin(angle) * size)
            x2 = int(self.center_x + np.cos(angle + 0.5) * size * 0.7)
            y2 = int(self.center_y + np.sin(angle + 0.5) * size * 0.7)
            
            pts = np.array([[self.center_x, self.center_y], [x1, y1], [x2, y2]], dtype=np.int32)
            cv2.fillPoly(frame, [pts], colors_pastel[i], lineType=cv2.LINE_AA)
            
            shadow_offset = int(5 * fold_progress)
            pts_shadow = pts + np.array([shadow_offset, shadow_offset])
            cv2.fillPoly(frame, [pts_shadow], (150, 150, 150), lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_146_northern_lights(self, frame, magnitudes):
        """Mode 146: Realistic aurora borealis dancing"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        frame[:] = (20, 20, 40)
        
        num_bands = 5
        for band in range(num_bands):
            y_base = 100 + band * 60
            
            for x in range(0, self.width, 10):
                wave1 = np.sin(x * 0.01 + self.frame_counter * 0.05 + band) * bass * 50
                wave2 = np.sin(x * 0.02 + self.frame_counter * 0.03) * mids * 30
                
                y = int(y_base + wave1 + wave2)
                
                hue = int(60 + mids * 60 + band * 10)
                brightness = int(200 + treble * 55)
                color_hsv = np.array([[[hue, 200, brightness]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                
                for y_offset in range(40):
                    alpha = 1.0 - (y_offset / 40)
                    if 0 <= y + y_offset < self.height:
                        cv2.circle(frame, (x, y + y_offset), 5, tuple(int(c * alpha) for c in color), -1, lineType=cv2.LINE_AA)
        
        for _ in range(50):
            sx = np.random.randint(0, self.width)
            sy = np.random.randint(0, self.height // 2)
            cv2.circle(frame, (sx, sy), 1, (255, 255, 255), -1)
        
        return frame

    def draw_mode_147_cellular_automata(self, frame, magnitudes):
        """Mode 147: Conway's Game of Life with audio triggers"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        cell_size = 10
        grid_w = self.width // cell_size
        grid_h = self.height // cell_size
        
        if len(self.cellular_automata_grid) == 0:
            self.cellular_automata_grid = [[np.random.randint(0, 2) for _ in range(grid_w)] for _ in range(grid_h)]
        
        if self.frame_counter % 5 == 0:
            new_grid = [[0 for _ in range(grid_w)] for _ in range(grid_h)]
            
            for y in range(grid_h):
                for x in range(grid_w):
                    neighbors = 0
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            if dy == 0 and dx == 0:
                                continue
                            ny, nx = (y + dy) % grid_h, (x + dx) % grid_w
                            neighbors += self.cellular_automata_grid[ny][nx]
                    
                    if self.cellular_automata_grid[y][x] == 1:
                        new_grid[y][x] = 1 if neighbors in [2, 3] else 0
                    else:
                        new_grid[y][x] = 1 if neighbors == 3 else 0
            
            if bass > 0.7:
                for _ in range(int(bass * 50)):
                    rx, ry = np.random.randint(0, grid_w), np.random.randint(0, grid_h)
                    new_grid[ry][rx] = 1
            
            self.cellular_automata_grid = new_grid
        
        for y in range(grid_h):
            for x in range(grid_w):
                if self.cellular_automata_grid[y][x] == 1:
                    color = (0, int(200 + mids * 55), 0)
                    cv2.rectangle(frame, (x * cell_size, y * cell_size),
                                ((x + 1) * cell_size, (y + 1) * cell_size), color, -1)
        
        return frame

    def draw_mode_148_dragon_curve(self, frame, magnitudes):
        """Mode 148: Fractal dragon curve growing"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        
        iterations = int(3 + bass * 8)
        
        def dragon_curve(order):
            if order == 0:
                return "F"
            else:
                prev = dragon_curve(order - 1)
                return prev + "L" + prev[::-1].replace("L", "temp").replace("R", "L").replace("temp", "R") + "R"
        
        curve = dragon_curve(min(iterations, 12))
        
        x, y = self.center_x, self.center_y
        angle = 0
        step = max(2, 300 // (2 ** min(iterations, 10)))
        
        points = [(x, y)]
        for command in curve:
            if command == "F":
                x += int(np.cos(np.radians(angle)) * step)
                y += int(np.sin(np.radians(angle)) * step)
                points.append((x, y))
            elif command == "L":
                angle -= 90
            elif command == "R":
                angle += 90
        
        for i in range(1, len(points)):
            hue = int((i / len(points)) * 180)
            color_hsv = np.array([[[hue, 255, int(200 + mids * 55)]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            if (0 <= points[i-1][0] < self.width and 0 <= points[i-1][1] < self.height and
                0 <= points[i][0] < self.width and 0 <= points[i][1] < self.height):
                cv2.line(frame, points[i-1], points[i], tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
        
        return frame

    def draw_mode_149_rain_circles(self, frame, magnitudes):
        """Mode 149: Concentric circles like raindrops"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        if treble > 0.5 and self.frame_counter % 10 == 0:
            self.rain_circle_ripples.append({
                'x': np.random.randint(0, self.width),
                'y': np.random.randint(0, self.height),
                'radius': 0,
                'life': 60
            })
        
        for ripple in self.rain_circle_ripples[:]:
            ripple['radius'] += 3 + bass * 2
            ripple['life'] -= 1
            
            if ripple['life'] > 0:
                alpha = ripple['life'] / 60
                color = (int(100 * alpha), int(200 * alpha), int(255 * alpha))
                
                cv2.circle(frame, (ripple['x'], ripple['y']), int(ripple['radius']), color, 2, lineType=cv2.LINE_AA)
        
        self.rain_circle_ripples = [r for r in self.rain_circle_ripples if r['life'] > 0]
        
        return frame

    def draw_mode_150_fourier_epicycles(self, frame, magnitudes):
        """Mode 150: Rotating circles tracing Fourier series"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])
        
        num_circles = int(5 + treble * 10)
        
        x, y = self.center_x, self.center_y - 100
        
        for i in range(num_circles):
            magnitude = magnitudes[min(i * 8, len(magnitudes) - 1)]
            radius = int(20 + magnitude * 50 * (num_circles - i) / num_circles)
            speed = (i + 1) * 0.1 + bass * 0.1
            angle = self.frame_counter * speed
            
            next_x = x + int(np.cos(angle) * radius)
            next_y = y + int(np.sin(angle) * radius)
            
            hue = int((i / num_circles) * 180)
            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            
            cv2.circle(frame, (x, y), radius, tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
            cv2.line(frame, (x, y), (next_x, next_y), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)
            cv2.circle(frame, (next_x, next_y), 5, tuple(map(int, color)), -1)
            
            x, y = next_x, next_y
        
        if len(self.fourier_epicycles) < 200:
            self.fourier_epicycles.append((x, y))
        else:
            self.fourier_epicycles.pop(0)
            self.fourier_epicycles.append((x, y))
        
        for i in range(1, len(self.fourier_epicycles)):
            cv2.line(frame, self.fourier_epicycles[i-1], self.fourier_epicycles[i], (255, 255, 255), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_151_neon_halo_burst(self, frame, magnitudes):
        """Mode 151: Circular ring whose radius pulses with kick; emits radial spikes on snare"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:len(magnitudes)//2])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Main pulsing ring
        ring_radius = int(150 + bass * 200)
        glow_intensity = int(150 + bass * 105)

        # Draw glowing ring
        for thickness in range(5, 0, -1):
            alpha = glow_intensity * (thickness / 5)
            color = (int(alpha), int(alpha * 0.5), int(alpha * 1.2))
            cv2.circle(frame, (self.center_x, self.center_y), ring_radius, color, thickness, lineType=cv2.LINE_AA)

        # Emit radial spikes on snare (mid peaks)
        if mids > 0.6:
            spike_count = int(12 + treble * 12)
            for i in range(spike_count):
                angle = (i / spike_count) * 2 * np.pi
                spike_len = int(50 + mids * 100)
                x1 = int(self.center_x + np.cos(angle) * ring_radius)
                y1 = int(self.center_y + np.sin(angle) * ring_radius)
                x2 = int(self.center_x + np.cos(angle) * (ring_radius + spike_len))
                y2 = int(self.center_y + np.sin(angle) * (ring_radius + spike_len))
                cv2.line(frame, (x1, y1), (x2, y2), (255, 200, 100), 2, lineType=cv2.LINE_AA)

        # Glittery sparks for treble
        if treble > 0.5:
            spark_count = int(treble * 30)
            for _ in range(spark_count):
                angle = np.random.random() * 2 * np.pi
                dist = ring_radius + np.random.randint(-30, 30)
                sx = int(self.center_x + np.cos(angle) * dist)
                sy = int(self.center_y + np.sin(angle) * dist)
                cv2.circle(frame, (sx, sy), 2, (255, 255, 200), -1)

        return frame

    def draw_mode_152_twin_orbiters(self, frame, magnitudes):
        """Mode 152: Two dots orbit a center with elastic distance; trails draw lissajous figure"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Orbit parameters
        orbit_radius = 150 + bass * 100
        speed = self.frame_counter * 0.05

        # First orbiter
        x1 = int(self.center_x + np.cos(speed) * orbit_radius)
        y1 = int(self.center_y + np.sin(speed * 1.3) * orbit_radius * 0.8)

        # Second orbiter
        x2 = int(self.center_x + np.cos(speed + np.pi) * orbit_radius)
        y2 = int(self.center_y + np.sin((speed + np.pi) * 1.3) * orbit_radius * 0.8)

        # Store trail
        self.twin_orbiters.append(((x1, y1), (x2, y2)))
        if len(self.twin_orbiters) > 150:
            self.twin_orbiters.pop(0)

        # Draw trails
        for i, ((tx1, ty1), (tx2, ty2)) in enumerate(self.twin_orbiters):
            alpha = int((i / len(self.twin_orbiters)) * 255)
            thickness = 1 + int(mids * 3)
            cv2.circle(frame, (tx1, ty1), 2, (alpha, 100, 200), thickness)
            cv2.circle(frame, (tx2, ty2), 2, (200, alpha, 150), thickness)

        # Draw current orbiters
        cv2.circle(frame, (x1, y1), 8, (100, 200, 255), -1)
        cv2.circle(frame, (x2, y2), 8, (255, 100, 200), -1)

        return frame

    def draw_mode_153_bar_spiral_galaxy(self, frame, magnitudes):
        """Mode 153: Bars arranged in a spiral. Each bar length follows its band"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        self.bar_spiral_rotation += 0.02 + bass * 0.05

        num_bars = min(60, len(magnitudes))
        for i in range(num_bars):
            angle = (i / num_bars) * 4 * np.pi + self.bar_spiral_rotation
            distance = 50 + i * 8
            magnitude = magnitudes[i]
            bar_length = int(20 + magnitude * 100)

            x = int(self.center_x + np.cos(angle) * distance)
            y = int(self.center_y + np.sin(angle) * distance)

            angle_perp = angle + np.pi / 2
            x1 = int(x + np.cos(angle_perp) * bar_length)
            y1 = int(y + np.sin(angle_perp) * bar_length)

            hue = int((i / num_bars) * 180)
            color_hsv = np.array([[[hue, 255, int(200 + magnitude * 55)]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.line(frame, (x, y), (x1, y1), tuple(map(int, color)), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_154_ribbon_wave(self, frame, magnitudes):
        """Mode 154: Wide ribbon undulates like cloth; bass lifts amplitude"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        segments = 80
        points_top = []
        points_bottom = []

        for i in range(segments):
            x = int(i * self.width / segments)
            amplitude = int(50 + bass * 100)
            wave = np.sin(i * 0.3 + self.frame_counter * 0.1) * amplitude
            edge_jitter = np.random.randint(-int(treble * 10), int(treble * 10) + 1)

            y_top = int(self.center_y - 30 + wave + edge_jitter)
            y_bottom = int(self.center_y + 30 + wave - edge_jitter)

            points_top.append((x, y_top))
            points_bottom.append((x, y_bottom))

        # Draw ribbon as filled polygon
        all_points = points_top + points_bottom[::-1]
        pts = np.array(all_points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.fillPoly(frame, [pts], (150, 100, 255))

        # Edge lines with shimmer
        for i in range(1, len(points_top)):
            cv2.line(frame, points_top[i-1], points_top[i], (255, 200, 255), 2, lineType=cv2.LINE_AA)
            cv2.line(frame, points_bottom[i-1], points_bottom[i], (255, 200, 255), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_155_voxel_city(self, frame, magnitudes):
        """Mode 155: 3D grid of extruded cubes like skyline; building heights react per frequency"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        grid_size = 8
        gap = 15
        start_x = self.center_x - (grid_size * gap) // 2
        start_y = self.center_y + 200

        for i in range(grid_size):
            for j in range(grid_size):
                idx = (i * grid_size + j) % len(magnitudes)
                height = int(magnitudes[idx] * 150)

                x = start_x + j * gap
                y_base = start_y - i * gap // 2

                # Draw simple isometric cube
                top_left = (x, y_base - height)
                top_right = (x + gap, y_base - height)
                bottom_left = (x, y_base)
                bottom_right = (x + gap, y_base)

                brightness = int(100 + magnitudes[idx] * 155)
                color = (brightness // 2, brightness // 2, brightness)

                cv2.rectangle(frame, top_left, bottom_right, color, -1)
                cv2.rectangle(frame, top_left, bottom_right, (255, 255, 255), 1, lineType=cv2.LINE_AA)

        # Fog breathes on beat
        if bass > 0.6:
            fog_overlay = np.zeros_like(frame, dtype=np.uint8)
            fog_overlay[:, :] = (50, 50, 50)
            frame = cv2.addWeighted(frame, 1.0, fog_overlay, bass * 0.3, 0)

        return frame

    def draw_mode_156_sunburst_dial(self, frame, magnitudes):
        """Mode 156: 360° radial meter with ticks; ticks bend outward on mids"""
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        tick_count = 60
        inner_radius = 120
        outer_radius = 200

        for i in range(tick_count):
            angle = (i / tick_count) * 2 * np.pi
            magnitude = magnitudes[min(i * len(magnitudes) // tick_count, len(magnitudes) - 1)]

            bend_amount = mids * 50
            effective_outer = outer_radius + int(magnitude * 100) + int(bend_amount)

            x1 = int(self.center_x + np.cos(angle) * inner_radius)
            y1 = int(self.center_y + np.sin(angle) * inner_radius)
            x2 = int(self.center_x + np.cos(angle) * effective_outer)
            y2 = int(self.center_y + np.sin(angle) * effective_outer)

            # Flicker tips on highs
            color = (200, 200, 255)
            if treble > 0.6 and i % 3 == 0:
                color = (255, 255, 255)
                cv2.circle(frame, (x2, y2), 4, color, -1)

            cv2.line(frame, (x1, y1), (x2, y2), color, 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_157_waterline_oscilloscope(self, frame, magnitudes):
        """Mode 157: Horizontal waveform floats like water surface"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Generate waveform points
        points = []
        swell = int(bass * 50)

        for i in range(len(magnitudes)):
            x = int(i * self.width / len(magnitudes))
            y = int(self.center_y + swell + magnitudes[i] * 100 - 50)
            points.append((x, y))

        # Draw water surface
        for i in range(1, len(points)):
            cv2.line(frame, points[i-1], points[i], (100, 200, 255), 2, lineType=cv2.LINE_AA)

        # Spawn foam particles on highs
        if treble > 0.5 and self.frame_counter % 2 == 0:
            for _ in range(int(treble * 5)):
                idx = np.random.randint(0, len(points))
                px, py = points[idx]
                self.waterline_surface.append({'x': px, 'y': py, 'life': 20})

        # Draw foam particles
        for particle in self.waterline_surface[:]:
            particle['y'] -= 1
            particle['life'] -= 1
            if particle['life'] > 0:
                alpha = particle['life'] / 20
                cv2.circle(frame, (particle['x'], particle['y']), 2, (int(255 * alpha), int(255 * alpha), 255), -1)

        self.waterline_surface = [p for p in self.waterline_surface if p['life'] > 0]

        return frame

    def draw_mode_158_laser_tunnel(self, frame, magnitudes):
        """Mode 158: Perspective tunnel of rings; ring scale follows kick"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        ring_count = 15
        hue_shift = int(treble * 180)

        for i in range(ring_count):
            z = i / ring_count
            scale = int(50 + z * 400 + bass * 100)
            thickness = max(1, int(5 * (1 - z)))

            hue = (hue_shift + i * 12) % 180
            color_hsv = np.array([[[hue, 255, 200]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            cv2.circle(frame, (self.center_x, self.center_y), scale, tuple(map(int, color)), thickness, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_159_vector_field_sprites(self, frame, magnitudes):
        """Mode 159: Thousands of particles follow a noise flow; velocity multiplies on mids"""
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        # Initialize particles
        if len(self.vector_field_particles) < 300:
            for _ in range(300 - len(self.vector_field_particles)):
                self.vector_field_particles.append({
                    'x': np.random.randint(0, self.width),
                    'y': np.random.randint(0, self.height),
                    'trail': []
                })

        # Update particles
        for particle in self.vector_field_particles:
            noise_x = np.sin(particle['x'] * 0.01 + self.frame_counter * 0.05) * (1 + mids * 2)
            noise_y = np.cos(particle['y'] * 0.01 + self.frame_counter * 0.05) * (1 + mids * 2)

            particle['x'] += noise_x
            particle['y'] += noise_y

            # Wrap around
            particle['x'] = particle['x'] % self.width
            particle['y'] = particle['y'] % self.height

            # Trail
            trail_length = int(5 + treble * 15)
            particle['trail'].append((int(particle['x']), int(particle['y'])))
            if len(particle['trail']) > trail_length:
                particle['trail'].pop(0)

            # Draw trail
            for i in range(1, len(particle['trail'])):
                alpha = int((i / len(particle['trail'])) * 255)
                cv2.line(frame, particle['trail'][i-1], particle['trail'][i], (alpha, alpha // 2, 255), 1)

        return frame

    def draw_mode_160_orbit_rings_meter(self, frame, magnitudes):
        """Mode 160: Nested orbits with dots; each ring maps to a band"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        ring_count = min(10, len(magnitudes) // 12)

        for i in range(ring_count):
            idx = i * (len(magnitudes) // ring_count)
            magnitude = magnitudes[idx]

            radius = 50 + i * 40
            eccentricity = magnitude * 0.5
            dot_size = int(5 + magnitude * 15)

            angle = self.frame_counter * 0.05 * (i + 1)
            x = int(self.center_x + np.cos(angle) * radius * (1 + eccentricity))
            y = int(self.center_y + np.sin(angle) * radius * (1 - eccentricity))

            # Draw orbit path
            cv2.ellipse(frame, (self.center_x, self.center_y), (int(radius * (1 + eccentricity)), int(radius * (1 - eccentricity))), 0, 0, 360, (100, 100, 150), 1, lineType=cv2.LINE_AA)

            # Draw dot
            hue = int((i / ring_count) * 180)
            color_hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
            cv2.circle(frame, (x, y), dot_size, tuple(map(int, color)), -1)

        return frame

    def draw_mode_161_stitch_bars(self, frame, magnitudes):
        """Mode 161: Stacked micro-bars like embroidered stitches"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        rows = 8
        cols = min(60, len(magnitudes))
        gap = self.width // (cols + 1)
        row_height = 15

        for row in range(rows):
            y = 100 + row * row_height
            for col in range(cols):
                x = gap * (col + 1)
                magnitude = magnitudes[col]
                density = int(magnitude * 10)

                # Wobble on beat
                wobble = int(np.sin(self.frame_counter * 0.1 + col * 0.5) * bass * 10)

                for d in range(density):
                    y_stitch = y + d * 2 + wobble
                    cv2.line(frame, (x - 3, y_stitch), (x + 3, y_stitch), (200, 150, 255), 1)

        return frame

    def draw_mode_162_aurora_curtain(self, frame, magnitudes):
        """Mode 162: Vertical curtains waving; bass widens curtain"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        curtain_count = 5

        for c in range(curtain_count):
            x_base = (c + 1) * self.width // (curtain_count + 1)
            width_mult = 1 + bass * 0.5

            points = []
            for y in range(0, self.height, 10):
                curl = int(np.sin(y * 0.05 + self.frame_counter * 0.1 + c) * mids * 30)
                x = int(x_base + curl * width_mult)
                points.append((x, y))

            # Draw curtain
            hue = int((c / curtain_count) * 180)
            color_hsv = np.array([[[hue, 200, 200]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            for i in range(1, len(points)):
                cv2.line(frame, points[i-1], points[i], tuple(map(int, color)), 3, lineType=cv2.LINE_AA)

        # Star-like flickers
        if treble > 0.6:
            for _ in range(int(treble * 10)):
                sx = np.random.randint(0, self.width)
                sy = np.random.randint(0, self.height)
                cv2.circle(frame, (sx, sy), 2, (255, 255, 200), -1)

        return frame

    def draw_mode_163_helix_bars_3d(self, frame, magnitudes):
        """Mode 163: Two helical rails of bars spinning"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        self.helix_bars_state += 0.05 + bass * 0.1

        bar_count = min(50, len(magnitudes))
        turns = 3

        for i in range(bar_count):
            t = i / bar_count
            angle = t * turns * 2 * np.pi + self.helix_bars_state

            x = int(self.center_x + np.cos(angle) * 150)
            y = int(100 + t * (self.height - 200))

            magnitude = magnitudes[i]
            bar_length = int(magnitude * 80)

            x1 = x - bar_length // 2
            x2 = x + bar_length // 2

            brightness = int(100 + magnitude * 155)
            color = (brightness, brightness // 2, brightness)

            cv2.line(frame, (x1, y), (x2, y), color, 3, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_164_polygon_heartbeat(self, frame, magnitudes):
        """Mode 164: Regular polygon in the center inflates on kicks"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        sides = 6
        scale = 100 + int(bass * 150)

        points = []
        for i in range(sides):
            angle = (i / sides) * 2 * np.pi
            x = int(self.center_x + np.cos(angle) * scale)
            y = int(self.center_y + np.sin(angle) * scale)
            points.append((x, y))

        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (255, 150, 150), 3, lineType=cv2.LINE_AA)

        # Concentric echo waves
        if bass > 0.5:
            for echo in range(1, 4):
                echo_scale = scale + echo * 30
                echo_points = []
                for i in range(sides):
                    angle = (i / sides) * 2 * np.pi
                    x = int(self.center_x + np.cos(angle) * echo_scale)
                    y = int(self.center_y + np.sin(angle) * echo_scale)
                    echo_points.append((x, y))

                echo_pts = np.array(echo_points, np.int32)
                echo_pts = echo_pts.reshape((-1, 1, 2))
                alpha = int(150 / echo)
                cv2.polylines(frame, [echo_pts], True, (alpha, alpha // 2, alpha // 2), 1, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_165_confetti_impulse(self, frame, magnitudes):
        """Mode 165: On peaks, spawn confetti bursts"""
        peak_threshold = 0.7

        # Check for peaks
        for i, mag in enumerate(magnitudes):
            if mag > peak_threshold and np.random.random() < 0.1:
                # Spawn confetti
                hue = int((i / len(magnitudes)) * 180)
                for _ in range(20):
                    self.confetti_particles.append({
                        'x': self.center_x + np.random.randint(-50, 50),
                        'y': self.center_y + np.random.randint(-50, 50),
                        'vx': np.random.uniform(-5, 5),
                        'vy': np.random.uniform(-10, -2),
                        'hue': hue,
                        'life': 60
                    })

        # Update and draw confetti
        for particle in self.confetti_particles[:]:
            particle['vy'] += 0.3  # Gravity
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['vx'] *= 0.98  # Air drag
            particle['life'] -= 1

            if particle['life'] > 0:
                color_hsv = np.array([[[particle['hue'], 255, 255]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                cv2.circle(frame, (int(particle['x']), int(particle['y'])), 3, tuple(map(int, color)), -1)

        self.confetti_particles = [p for p in self.confetti_particles if p['life'] > 0 and 0 <= p['y'] < self.height]

        return frame

    def draw_mode_166_wireframe_dome(self, frame, magnitudes):
        """Mode 166: Hemispherical mesh; vertices displace along normals"""
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        segments = 12

        for lat in range(segments // 2):
            for lon in range(segments):
                theta = (lat / (segments / 2)) * np.pi / 2
                phi = (lon / segments) * 2 * np.pi

                idx = (lat * segments + lon) % len(magnitudes)
                offset = int(magnitudes[idx] * 50)

                r = 200 + offset
                x = int(self.center_x + r * np.sin(theta) * np.cos(phi))
                y = int(self.center_y + 200 - r * np.cos(theta))
                z = int(r * np.sin(theta) * np.sin(phi))

                # Simple 3D to 2D projection
                x_2d = x + z // 2
                y_2d = y - z // 4

                if lat < segments // 2 - 1:
                    theta2 = ((lat + 1) / (segments / 2)) * np.pi / 2
                    r2 = 200 + int(magnitudes[((lat + 1) * segments + lon) % len(magnitudes)] * 50)
                    x2 = int(self.center_x + r2 * np.sin(theta2) * np.cos(phi))
                    y2 = int(self.center_y + 200 - r2 * np.cos(theta2))
                    z2 = int(r2 * np.sin(theta2) * np.sin(phi))
                    x2_2d = x2 + z2 // 2
                    y2_2d = y2 - z2 // 4

                    cv2.line(frame, (x_2d, y_2d), (x2_2d, y2_2d), (100, 150, 255), 1, lineType=cv2.LINE_AA)

                # Specular sparkle on highs
                if treble > 0.6 and idx % 3 == 0:
                    cv2.circle(frame, (x_2d, y_2d), 3, (255, 255, 255), -1)

        return frame

    def draw_mode_167_pulse_dashes(self, frame, magnitudes):
        """Mode 167: Circular dashed stroke; dash length oscillates with mids"""
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        dash_count = 60
        radius = 200
        dash_base_len = 20 + int(mids * 40)

        for i in range(dash_count):
            angle_start = (i / dash_count) * 2 * np.pi
            angle_end = angle_start + (dash_base_len / radius)

            x1 = int(self.center_x + np.cos(angle_start) * radius)
            y1 = int(self.center_y + np.sin(angle_start) * radius)
            x2 = int(self.center_x + np.cos(angle_end) * radius)
            y2 = int(self.center_y + np.sin(angle_end) * radius)

            # Tip glow on treble
            glow = 200
            if treble > 0.5 and i % 2 == 0:
                glow = 255
                cv2.circle(frame, (x2, y2), 5, (255, 255, 255), -1)

            cv2.line(frame, (x1, y1), (x2, y2), (glow, glow // 2, 255), 3, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_168_terrain_sweep(self, frame, magnitudes):
        """Mode 168: Scrolling heightmap like synthwave hills"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        row_count = 15

        # Shift existing rows
        for row in self.terrain_sweep_rows:
            row['y'] += 5

        # Remove off-screen rows
        self.terrain_sweep_rows = [r for r in self.terrain_sweep_rows if r['y'] < self.height]

        # Add new row
        if len(self.terrain_sweep_rows) < row_count:
            profile = [magnitudes[i % len(magnitudes)] for i in range(self.width // 10)]
            self.terrain_sweep_rows.insert(0, {'y': 0, 'profile': profile})

        # Draw terrain
        for row_idx, row in enumerate(self.terrain_sweep_rows):
            y_base = row['y']
            profile = row['profile']

            points = []
            for i, height in enumerate(profile):
                x = i * 10
                y = int(y_base + 200 - height * 150 - row_idx * 5)
                points.append((x, y))

            # Draw line
            for i in range(1, len(points)):
                hue = int((height / 1.0) * 180)
                color_hsv = np.array([[[hue, 255, 200]]], dtype=np.uint8)
                color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
                cv2.line(frame, points[i-1], points[i], tuple(map(int, color)), 2, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_169_chromatic_bars_mirror(self, frame, magnitudes):
        """Mode 169: Mirrored bars with central symmetry; hue rotates"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        hue_offset = (self.frame_counter * 2) % 180
        bar_count = min(60, len(magnitudes))
        gap = 3
        bar_width = (self.width // 2) // bar_count - gap

        # Flash on kick
        if bass > 0.7 and self.frame_counter % 10 == 0:
            self.chromatic_bars_flash = 10

        flash_add = 0
        if self.chromatic_bars_flash > 0:
            flash_add = self.chromatic_bars_flash * 20
            self.chromatic_bars_flash -= 1

        for i in range(bar_count):
            magnitude = magnitudes[i]
            height = int(magnitude * (self.height // 2))

            x_left = self.center_x - i * (bar_width + gap) - bar_width
            x_right = self.center_x + i * (bar_width + gap)

            hue = (hue_offset + i * 3) % 180
            color_hsv = np.array([[[hue, 255, min(255, 200 + flash_add)]]], dtype=np.uint8)
            color = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]

            # Left bar
            cv2.rectangle(frame, (x_left, self.center_y - height), (x_left + bar_width, self.center_y), tuple(map(int, color)), -1)
            # Right bar
            cv2.rectangle(frame, (x_right, self.center_y - height), (x_right + bar_width, self.center_y), tuple(map(int, color)), -1)

        return frame

    def draw_mode_170_bubble_choir(self, frame, magnitudes):
        """Mode 170: Bubbles rise; size from band energy; pop on snare"""
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])

        # Spawn bubbles
        if self.frame_counter % 5 == 0:
            for i in range(0, len(magnitudes), 10):
                magnitude = magnitudes[i]
                if magnitude > 0.3:
                    self.bubble_choir_bubbles.append({
                        'x': np.random.randint(50, self.width - 50),
                        'y': self.height - 50,
                        'size': int(10 + magnitude * 40),
                        'vy': -2 - magnitude * 2,
                        'life': 100,
                        'popping': False
                    })

        # Update and draw bubbles
        for bubble in self.bubble_choir_bubbles[:]:
            bubble['y'] += bubble['vy']
            bubble['life'] -= 1

            # Pop on snare (mids spike)
            if mids > 0.7 and not bubble['popping']:
                bubble['popping'] = True
                bubble['pop_frame'] = 0

            if bubble['popping']:
                bubble['pop_frame'] += 1
                # Expanding rings
                ring_radius = bubble['size'] + bubble['pop_frame'] * 10
                alpha = max(0, 255 - bubble['pop_frame'] * 50)
                cv2.circle(frame, (int(bubble['x']), int(bubble['y'])), ring_radius, (alpha, alpha, 255), 2, lineType=cv2.LINE_AA)

                if bubble['pop_frame'] > 5:
                    bubble['life'] = 0
            else:
                # Draw bubble
                cv2.circle(frame, (int(bubble['x']), int(bubble['y'])), bubble['size'], (150, 200, 255), 2, lineType=cv2.LINE_AA)

        self.bubble_choir_bubbles = [b for b in self.bubble_choir_bubbles if b['life'] > 0]

        return frame

    def draw_mode_171_starfield_quantizer(self, frame, magnitudes):
        """Mode 171: Stars quantized to a grid; cell brightness follows local band"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])

        grid_size = 16
        cell_width = self.width // grid_size
        cell_height = self.height // grid_size

        for i in range(grid_size):
            for j in range(grid_size):
                idx = (i * grid_size + j) % len(magnitudes)
                brightness = int(magnitudes[idx] * 255)

                x = j * cell_width + cell_width // 2
                y = i * cell_height + cell_height // 2

                if brightness > 50:
                    size = max(1, brightness // 50)
                    cv2.circle(frame, (x, y), size, (brightness, brightness, brightness), -1)

        # Subtle rotation on beat
        if bass > 0.6:
            angle = bass * 2
            M = cv2.getRotationMatrix2D((self.center_x, self.center_y), angle, 1.0)
            frame = cv2.warpAffine(frame, M, (self.width, self.height))

        return frame

    def draw_mode_172_dna_ladder(self, frame, magnitudes):
        """Mode 172: Two sinusoid strands; rung length follows mids"""
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        strand_spacing = 100
        amplitude = 50

        points_left = []
        points_right = []

        for y in range(0, self.height, 5):
            t = y * 0.02 + self.frame_counter * 0.05
            x_left = int(self.center_x - strand_spacing // 2 + np.sin(t) * amplitude)
            x_right = int(self.center_x + strand_spacing // 2 + np.sin(t) * amplitude)

            points_left.append((x_left, y))
            points_right.append((x_right, y))

        # Draw strands
        for i in range(1, len(points_left)):
            cv2.line(frame, points_left[i-1], points_left[i], (100, 200, 255), 3, lineType=cv2.LINE_AA)
            cv2.line(frame, points_right[i-1], points_right[i], (255, 100, 200), 3, lineType=cv2.LINE_AA)

        # Draw rungs
        for i in range(0, len(points_left), 10):
            rung_length = int(strand_spacing * (0.5 + mids * 0.5))
            x_mid = (points_left[i][0] + points_right[i][0]) // 2
            y = points_left[i][1]

            cv2.line(frame, (x_mid - rung_length // 2, y), (x_mid + rung_length // 2, y), (200, 200, 200), 2, lineType=cv2.LINE_AA)

            # Sparks traverse on highs
            if treble > 0.5:
                spark_x = int(x_mid + np.sin(self.frame_counter * 0.2 + i) * rung_length // 2)
                cv2.circle(frame, (spark_x, y), 3, (255, 255, 100), -1)

        return frame

    def draw_mode_173_arc_meter_trio(self, frame, magnitudes):
        """Mode 173: Three concentric arcs for lows/mids/highs"""
        bass = np.mean(magnitudes[:len(magnitudes)//4])
        mids = np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4])
        treble = np.mean(magnitudes[3*len(magnitudes)//4:])

        values = [bass, mids, treble]
        colors = [(255, 100, 100), (100, 255, 100), (100, 100, 255)]

        for i, (value, color) in enumerate(zip(values, colors)):
            radius = 80 + i * 50
            thickness = int(10 + value * 20)
            sweep = int(value * 270)

            cv2.ellipse(frame, (self.center_x, self.center_y), (radius, radius), -90, 0, sweep, color, thickness, lineType=cv2.LINE_AA)

        return frame

    def draw_mode_174_ink_splatter_scope(self, frame, magnitudes):
        """Mode 174: Oscilloscope line with ink-style splats at transients"""
        # Generate waveform
        points = []
        for i in range(len(magnitudes)):
            x = int(i * self.width / len(magnitudes))
            y = int(self.center_y + (magnitudes[i] - 0.5) * 200)
            points.append((x, y))

        # Draw waveform
        for i in range(1, len(points)):
            cv2.line(frame, points[i-1], points[i], (100, 100, 200), 2, lineType=cv2.LINE_AA)

            # Detect transients (sharp changes)
            if abs(magnitudes[i] - magnitudes[i-1]) > 0.3:
                # Spawn splat
                self.ink_splatter_splats.append({
                    'x': points[i][0],
                    'y': points[i][1],
                    'size': 20,
                    'life': 30
                })

        # Draw splats
        for splat in self.ink_splatter_splats[:]:
            splat['size'] += 2
            splat['life'] -= 1

            if splat['life'] > 0:
                alpha = int((splat['life'] / 30) * 255)
                cv2.circle(frame, (splat['x'], splat['y']), splat['size'], (alpha // 2, alpha // 2, alpha), 1, lineType=cv2.LINE_AA)

        self.ink_splatter_splats = [s for s in self.ink_splatter_splats if s['life'] > 0]

        return frame

    def draw_mode_175_hex_cell_bloom(self, frame, magnitudes):
        """Mode 175: Hex grid; cells bloom outward with frequency bucket"""
        # Initialize hex grid
        if not self.hex_cell_states:
            hex_size = 30
            rows = self.height // (hex_size * 2) + 2
            cols = self.width // (hex_size * 2) + 2

            for row in range(rows):
                for col in range(cols):
                    x = col * hex_size * 1.5
                    y = row * hex_size * np.sqrt(3)
                    if row % 2 == 1:
                        x += hex_size * 0.75

                    self.hex_cell_states.append({
                        'x': int(x),
                        'y': int(y),
                        'bloom': 0,
                        'idx': (row * cols + col) % len(magnitudes)
                    })

        # Update and draw cells
        for cell in self.hex_cell_states:
            magnitude = magnitudes[cell['idx']]
            cell['bloom'] = magnitude

            if cell['bloom'] > 0.2:
                size = int(15 + cell['bloom'] * 20)
                brightness = int(cell['bloom'] * 255)
                color = (brightness // 2, brightness, brightness // 2)

                # Draw hexagon (simplified as circle)
                cv2.circle(frame, (cell['x'], cell['y']), size, color, -1, lineType=cv2.LINE_AA)

        return frame

    def draw_spectrum(self, frame, magnitudes):
        """Draw spectrum based on selected mode using dynamic dispatch"""
        self.frame_counter += 1

        # Get mode method from registry
        mode_method = get_mode_method(self.mode)
        if mode_method:
            return mode_method(frame, magnitudes)
        else:
            # Fallback: simple bars if mode not found
            print(f"Warning: Mode {self.mode} not found, using fallback")
            for i in range(min(self.num_bars, len(magnitudes))):
                height = int(magnitudes[i] * self.height * 0.8)
                x = int((i + 0.5) * self.width / self.num_bars)
                cv2.rectangle(frame, (x - 5, self.height - height),
                            (x + 5, self.height), (100, 150, 255), -1)
            return frame

    def generate_video(self):
        """Generate the final video with transparent background"""
        print(f"Generating video: {self.output_path}")

        self.load_audio()

        temp_no_audio = str(Path(self.output_path).with_suffix('')) + '_temp_no_audio.mp4'
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        video_writer = cv2.VideoWriter(
            temp_no_audio, fourcc, self.fps,
            (self.width, self.height), True
        )

        if not video_writer.isOpened():
            raise RuntimeError("Failed to open video writer")

        total_frames = int(self.duration * self.fps)

        for frame_idx in range(total_frames):
            frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)

            audio_frame_idx = int(frame_idx * self.num_frames / total_frames)
            magnitudes = self.get_frequency_bands(audio_frame_idx)

            frame = self.draw_spectrum(frame, magnitudes)
            video_writer.write(frame)

            if (frame_idx + 1) % 30 == 0 or frame_idx == total_frames - 1:
                progress = (frame_idx + 1) / total_frames * 100
                print(f"Progress: {progress:.1f}% ({frame_idx + 1}/{total_frames} frames)")

        video_writer.release()
        print(f"\nVideo generation complete (silent): {temp_no_audio}")

        print("Adding audio and finalizing...")
        import subprocess

        try:
            # Fast preview path: skip transparency/prores when AS_PREVIEW=1
            if os.getenv('AS_PREVIEW') == '1':
                final_output = str(Path(self.output_path))
                result = subprocess.run([
                    'ffmpeg', '-y',
                    '-i', temp_no_audio,
                    '-i', self.audio_path,
                    '-c:v', 'libx264',
                    '-preset', 'veryfast',
                    '-crf', '23',
                    '-c:a', 'aac',
                    '-shortest',
                    final_output
                ], capture_output=True, text=True)

                Path(temp_no_audio).unlink(missing_ok=True)

                if result.returncode == 0:
                    self.output_path = final_output
                    print(f"✓ Preview video created: {final_output}")
                    return
                else:
                    print(f"Warning: Preview mux failed, falling back to transparency path")

            final_output = str(Path(self.output_path).with_suffix('.mov'))

            result = subprocess.run([
                'ffmpeg', '-y',
                '-i', temp_no_audio,
                '-i', self.audio_path,
                '-filter_complex',
                '[0:v]colorkey=0x000000:0.01:0.1[ckout];[ckout]format=yuva420p[video]',
                '-map', '[video]',
                '-map', '1:a',
                '-c:v', 'prores_ks',
                '-profile:v', '4444',
                '-c:a', 'aac',
                '-shortest',
                final_output
            ], capture_output=True, text=True)

            Path(temp_no_audio).unlink(missing_ok=True)

            if result.returncode == 0:
                self.output_path = final_output
                print(f"✓ Video with transparency and audio created successfully")
                print(f"✓ Output: {final_output}")
            else:
                print(f"Warning: Could not create transparent video. Creating standard video instead.")
                print(f"FFmpeg error: {result.stderr}")

                result = subprocess.run([
                    'ffmpeg', '-y',
                    '-i', temp_no_audio,
                    '-i', self.audio_path,
                    '-c:v', 'copy',
                    '-c:a', 'aac',
                    '-shortest',
                    final_output
                ], capture_output=True, text=True)

                Path(temp_no_audio).unlink(missing_ok=True)

                if result.returncode == 0:
                    print(f"✓ Standard video created: {final_output}")
                else:
                    print(f"Error: Could not create video")

        except FileNotFoundError:
            print("Error: ffmpeg not found. Please install ffmpeg:")
            print("  brew install ffmpeg")
            Path(temp_no_audio).unlink()
            raise
        except Exception as e:
            print(f"Error: Could not process video: {e}")
            if Path(temp_no_audio).exists():
                Path(temp_no_audio).unlink()
            raise

        print(f"Duration: {self.duration:.2f}s, Resolution: {self.width}x{self.height}, FPS: {self.fps}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate creative audio spectrum visualizations for lofi and jazz channels',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Vinyl grooves for lofi YouTube channel
  python audio_spectrum_creative.py input.mp3 output.mov --mode 1

  # Soul aura for K-pop soul/jazz covers
  python audio_spectrum_creative.py input.mp3 output.mov --mode 5

  # Neon rain for cyberpunk lofi
  python audio_spectrum_creative.py input.mp3 output.mov --mode 2

  # Electric heartbeat for emotional jazz
  python audio_spectrum_creative.py input.mp3 output.mov --mode 7
        """
    )

    parser.add_argument('input', help='Input audio file (.mp3 or .wav)')
    parser.add_argument('output', help='Output video file (.mov recommended)')
    parser.add_argument('--mode', type=int, choices=range(1, 301), default=1,
                       help='Visualization mode (1-300). Use --help for full list.')
    parser.add_argument('--width', type=int, default=720, help='Video width (default: 720 for square format)')
    parser.add_argument('--height', type=int, default=720, help='Video height (default: 720 for square format)')
    parser.add_argument('--fps', type=int, default=30, help='Frames per second (default: 30)')
    parser.add_argument('--num-bars', type=int, default=120, help='Number of frequency elements (default: 120)')
    parser.add_argument('--smoothing', type=float, default=0.7, help='Smoothing factor 0-1 (default: 0.7)')

    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)

    mode_names = {
        1: "Vinyl Grooves (lofi)",
        2: "Neon Rain (cyberpunk lofi)",
        3: "Jazzy Fireworks (jazz energy)",
        4: "Retro Cassette (vintage lofi)",
        5: "Soul Aura (soul/RnB)",
        6: "Frequency Flowers (dreamy lofi)",
        7: "Electric Heartbeat (emotional jazz)",
        8: "Pixel Clouds (retro lofi)",
        9: "Liquid Mercury (smooth jazz)",
        10: "Cosmic Dust (ambient lofi)",
        11: "Quantum Strings (experimental)",
        12: "Lava Lamp (psychedelic lofi)",
        13: "DNA Helix (scientific vibe)",
        14: "Lightning Strikes (intense energy)",
        15: "Morphing Geometry (abstract modern)",
        16: "Ink Drops (artistic lofi)",
        17: "Aurora Waves (ethereal ambient)",
        18: "Fractal Bloom (mathematical art)",
        19: "Plasma Storm (chaotic energy)",
        20: "Crystal Growth (elegant minimalism)",
        21: "Gravitational Lens (cosmic sci-fi)",
        22: "Magnetic Fields (scientific art)",
        23: "Tribal Drums (world music)",
        24: "Neon Cityscape (synthwave)",
        25: "Heartbeat Monitor (dramatic tension)",
        26: "Ocean Depths (underwater mystery)",
        27: "Fire Dance (primal energy)",
        28: "Particle Collider (science)",
        29: "Rainbow Prism (optical physics)",
        30: "Seismic Waves (geological drama)",
        31: "Origami Unfold (Japanese art)",
        32: "Storm Clouds (epic weather)",
        33: "Binary Matrix (hacker aesthetic)",
        34: "Kaleidoscope (psychedelic symmetry)",
        35: "Laser Show (EDM concert)",
        36: "Sandstorm (natural chaos)",
        37: "Ice Shatter (dramatic tension)",
        38: "Cellular Division (biology)",
        39: "Neon Tubes (futuristic minimal)",
        40: "Cosmic Strings (theoretical physics)",
        41: "Paint Splatter (abstract expressionism)",
        42: "Quantum Foam (extreme physics)",
        43: "Aztec Sun (ancient civilization)",
        44: "Fiber Optics (tech aesthetic)",
        45: "Tornado Funnel (natural disaster)",
        46: "Hologram Glitch (cyberpunk tech)",
        47: "Starfield Warp (sci-fi space travel)",
        48: "Mandala Growth (spiritual art)",
        49: "Neon Sign Flicker (retro urban)",
        50: "Black Hole (cosmic destruction)",
        51: "Fractal Tree (generative growth)",
        52: "Cityscape Extrusion (3D buildings)",
        53: "Gravity Well (particle physics)",
        54: "Metaball Fluid (lava lamp)",
        55: "Aurora Borealis (northern lights)",
        56: "Stained Glass (glowing panes)",
        57: "Neon Nerve Network (neural synapses)",
        58: "Glitch Artifact (datamosh corruption)",
        59: "Warp Tunnel (hyperspace travel)",
        60: "Conway's Life (cellular automaton)",
        61: "ASCII Art (text visualizer)",
        62: "Rippling Water (interference patterns)",
        63: "Terrain Flyover (3D landscape)",
        64: "String Art (geometric lines)",
        65: "Fire & Embers (primal flames)",
        66: "Radial Kaleidoscope (mirrored symmetry)",
        67: "Pulsing Jellyfish (aquatic organism)",
        68: "Orbital System (planets & moons)",
        69: "Spectrum Cube (rotating 3D)",
        70: "Typographic Flow (floating words)",
        71: "Sonar Ping (radar sweep)",
        72: "VU Meters (analog needles)",
        73: "Lightning Cloud (storm strikes)",
        74: "Bouncing Balls (physics simulation)",
        75: "Liquid Ink (water dispersion)",
        76: "Stereo Landscape (L/R mountains)",
        77: "AI Latent Walk (generative dream)",
        78: "Pixel Storm (8-bit blizzard)",
        79: "Growing Vine (organic spread)",
        80: "Haunted Faces (ghostly vocals)",
        81: "Connecting Constellations (star network)",
        82: "Matrix Rain (falling code)",
        83: "Voxel World (3D shockwave)",
        84: "DNA Helix Rungs (genetic code)",
        85: "Audio-Reactive Shader (procedural noise)",
        86: "Spirograph (mathematical curves)",
        87: "Equalizer Tower (stacked rings)",
        88: "Audio-Driven Doodles (generative art)",
        89: "Firework Show (explosive bursts)",
        90: "Microscopic View (cellular division)",
        91: "Burning Paper (flame bars)",
        92: "Swarm Intelligence (boid flocking)",
        93: "Pendulum Wave (hypnotic dance)",
        94: "Retro Scanlines (CRT monitor)",
        95: "Pulsing Polygon (morphing shape)",
        96: "Chromatic Orb (3D sphere shader)",
        97: "Textured Bars (scrolling patterns)",
        98: "Voronoi Tessellation (cellular diagram)",
        99: "Shattering Glass (cracking pane)",
        100: "Sunrise/Sunset (gradient sky)",
        151: "Neon Halo Burst",
        152: "Twin Orbiters",
        153: "Bar Spiral Galaxy",
        154: "Ribbon Wave",
        155: "Voxel City",
        156: "Sunburst Dial",
        157: "Waterline Oscilloscope",
        158: "Laser Tunnel",
        159: "Vector Field Sprites",
        160: "Orbit Rings Meter",
        161: "Stitch Bars",
        162: "Aurora Curtain",
        163: "Helix Bars 3D",
        164: "Polygon Heartbeat",
        165: "Confetti Impulse",
        166: "Wireframe Dome",
        167: "Pulse Dashes",
        168: "Terrain Sweep",
        169: "Chromatic Bars Mirror",
        170: "Bubble Choir",
        171: "Starfield Quantizer",
        172: "DNA Ladder",
        173: "Arc Meter Trio",
        174: "Ink Splatter Scope",
        175: "Hex Cell Bloom",
        176: "Event Horizon Lattice",
        177: "Comet Conveyor",
        178: "Quantum Foam Micro",
        179: "Aurora Crown",
        180: "Asteroid Excavator",
        181: "Hyperloop Spectrotrain",
        182: "Galactic Pinball",
        183: "Nebula Inkblot",
        184: "Satellite Telemetry Rings",
        185: "Wormhole Origami",
        186: "Holographic Jellyfish",
        187: "Moon Quarry Crane",
        188: "Constellation TypoPlot",
        189: "Cryo Crystal Garden",
        190: "Meteorite Blueprint",
        191: "Lunar Tide Pool",
        192: "Orbital Barcode Slicer",
        193: "Satellite Swarm Flocking",
        194: "Astro Pulse Weave",
        195: "Zero-G Paint Spheres",
        196: "Supernova Countdown",
        197: "Martian Wind Harp",
        198: "Teleporting Bar Choir",
        199: "Cosmic Vinyl Halo",
        200: "Photon Origination Chamber",
        201: "Meteor Net",
        202: "Deep-Space Garden Hose",
        203: "Horizon Monoliths",
        204: "Gravity Slingshot Trails",
        205: "Solar Flare Notches",
        206: "Tesseract Window",
        207: "Interstellar Postcards",
        208: "Cosmic Braille",
        209: "Stellar Harpoon",
        210: "Galaxy Ticker Tape",
        211: "Antimatter Chess",
        212: "Star Nursery Conveyor",
        213: "Magnetar Lines",
        214: "Zero-Kelvin Diamonds",
        215: "Orbital Time Garden",
        216: "Subspace Ribbon Printer",
        217: "Dark-Matter Drizzle",
        218: "Meteor Choir Cones",
        219: "Folded Galaxy Map",
        220: "Ion Thruster Plume",
        221: "Cosmic Dominoes",
        222: "Spacesuit HUD",
        223: "Pulsar Barcode Beam",
        224: "Astro Terrarium",
        225: "Micrometeor Spark Curtain"
        ,226: "Golden Phyllotaxis Bloom"
        ,227: "Breathing Mandala Weave"
        ,228: "Infinite Tunnel Lissajous"
        ,229: "Lotus Bloom Cascade"
        ,230: "Orbital Hypno-Pendula"
        ,231: "Moire Breathing Nets"
        ,232: "Spiral Shepard Rings"
        ,233: "Velvet Plasma Pool"
        ,234: "Radial Pulse Cathedral"
        ,235: "S-Curve Serpents"
        ,236: "Orb Choir Orbitals"
        ,237: "Sufi Spin Carpet"
        ,238: "Helmholtz Rings"
        ,239: "Hypno Slinky Stairwell"
        ,240: "Fractal Fern Drift"
        ,241: "Binaural Circles"
        ,242: "Auric Chakric Wheel"
        ,243: "Hypersphere Ribbon"
        ,244: "Phi Step Kaleidos"
        ,245: "Silk Ribbon Cycloid"
        ,246: "Oceanic Breather"
        ,247: "Zen Sand Harmonograph"
        ,248: "Magnetic Ink Veins"
        ,249: "Breath-Linked Vortex"
        ,250: "Slow Meteor Carousel"
        ,251: "Ripple-Glass Cathedral"
        ,252: "Theta Lantern Field"
        ,253: "Isochromatic Weaves"
        ,254: "Orbiting Eye"
        ,255: "Endless Ribbon Stair"
        ,256: "Glassy Toroidal River"
        ,257: "Low-Poly Hypno-Shell"
        ,258: "Tide Clock Halo"
        ,259: "Morphic Kaleidofish"
        ,260: "Zen Compass Waves"
        ,261: "Glacial Bloom"
        ,262: "Double Helix Lanterns"
        ,263: "Soft-Grid Phase Slide"
        ,264: "Ripple Dome Observatory"
        ,265: "Ethereal Spirocloud"
        ,266: "Mosaic Drizzle"
        ,267: "Whispering Bamboo"
        ,268: "Nesting Circles Flow"
        ,269: "Drifting Paper Cranes"
        ,270: "Pulse-Weave Hologrid"
        ,271: "Serene Ribbon Canopy"
        ,272: "Auroral Veil Gate"
        ,273: "Satin Spiral Ladder"
        ,274: "Opaline Orb Drifter"
        ,275: "Hypno Quilt Loom"
    }
    print(f"Selected visualization mode: {args.mode} - {mode_names.get(args.mode, 'Unknown')}")

    visualizer = CreativeSpectrumVisualizer(
        audio_path=args.input,
        output_path=args.output,
        width=args.width,
        height=args.height,
        fps=args.fps,
        num_bars=args.num_bars,
        smoothing=args.smoothing,
        mode=args.mode
    )

    try:
        visualizer.generate_video()
        print("\nSuccess! Your creative audio spectrum video is ready.")
        print(f"Perfect for lofi and jazz/soul YouTube channels!")
    except Exception as e:
        print(f"\nError generating video: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

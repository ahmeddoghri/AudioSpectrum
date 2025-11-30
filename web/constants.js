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

// ========================================
// HIDDEN MODES - Temporarily hide problematic modes from frontend
// ========================================
// To hide a mode: Add its mode ID to this array
// Example: 'mode_990_abstract_concrete'
// To find a mode's ID: Search for the mode name in this file and copy its 'id' field
const HIDDEN_MODES = [
    // Add mode IDs here to hide them from the frontend
    // Example: 'mode_990_abstract_concrete',
    'mode_125_bubble_fusion',
    'mode_170_bubble_choir',
    'mode_193_satellite_swarm_flocking',
    'mode_304_butterfly_swarm',
    'mode_341_plankton_swarm',
    'vu_meters',
    'mode_114_ink_diffusion',
    'mode_157_waterline_oscilloscope',
    'mode_174_ink_splatter_scope',
    'mode_400_water_lily_reflection',
    'mode_400_water_lily_reflection',
    'mode_428_ferrofluid',
    'mode_444_superfluidity',
    'mode_120_fire_mandala',
    'mode_133_coral_reef',
    'mode_179_aurora_crown',
    'mode_189_cryo_crystal_garden',
    'mode_296_frost_crystal_growth',
    'mode_301_forest_canopy',
    'mode_302_ocean_waves',
    'mode_303_coral_reef',
    'mode_306_fireflies',
    'mode_307_flower_bloom',
    'mode_310_tree_rings',
    'mode_314_aurora_forest',
    'mode_321_bamboo_forest',
    'mode_324_crystal_cave',
    'mode_332_ice_crystals',
    'mode_352_geode_crystals',
    'mode_365_aurora_waves',
    'mode_368_coral_polyps',
    'mode_385_moonflower_bloom',
    'mode_406_crystal_lattice',
    'mode_472_liquid_crystal',
    'mode_490_photonic_crystal',
    'mode_570_street_art',
    'mode_715_digital_signature',
    'mode_745_random_forest',
    'mode_746_decision_tree',
    'mode_810_flower_of_life',
    // Hidden Geometric modes
    'mode_108_fractal_bloom',
    'mode_115_geometric_kaleidoscope',
    'mode_137_pendulum_wave',
    'mode_153_bar_spiral_galaxy',
    'mode_566_kaleidoscope_art',
    'mode_1000_mechanical_living',
    'mode_111_origami_unfold',
    'mode_112_galaxy_spiral',
    'mode_113_rubber_bands',
    'mode_117_cellular_growth',
    'mode_118_sound_ribbons',
    'mode_121_tessellation_shift',
    'mode_122_seismic_waves',
    'mode_126_tribal_drums',
    'mode_127_glass_shatter',
    'mode_128_bioluminescence',
    'mode_129_sound_architecture',
    'mode_131_sand_mandala',
    'mode_132_laser_show',
    'mode_134_wireframe_morph',
    'mode_135_sound_garden',
    'mode_136_hologram_glitch',
    'mode_138_volcano_eruption',
    'mode_139_butterfly_effect',
    'mode_140_silk_weaving',
    'mode_141_clock_gears',
    'mode_142_smoke_signals',
    'mode_144_string_theory',
    'mode_145_paper_craft',
    'mode_146_northern_lights',
    'mode_147_cellular_automata',
    'mode_148_dragon_curve',
    'mode_150_fourier_epicycles',
    'mode_152_twin_orbiters',
    'mode_154_ribbon_wave',
    'mode_155_voxel_city',
    'mode_156_sunburst_dial',
    'mode_158_laser_tunnel',
    'mode_159_vector_field_sprites',
    'mode_160_orbit_rings_meter',
    'mode_161_stitch_bars',
    'mode_164_polygon_heartbeat',
    'mode_165_confetti_impulse',
    'mode_166_wireframe_dome',
    'mode_167_pulse_dashes',
    'mode_169_chromatic_bars_mirror',
    'mode_171_starfield_quantizer',
    'mode_173_arc_meter_trio',
    'mode_175_hex_cell_bloom',
    'mode_176_event_horizon_lattice',
    'mode_177_comet_conveyor',
    'mode_180_asteroid_excavator',
    'mode_182_galactic_pinball',
    'mode_184_satellite_telemetry_rings',
    'mode_185_wormhole_origami',
    'mode_186_holographic_jellyfish',
    'mode_187_moon_quarry_crane',
    'mode_188_constellation_typoplot',
    'mode_190_meteorite_blueprint',
    'mode_191_lunar_tide_pool',
    'mode_192_orbital_barcode_slicer',
    'mode_194_astro_pulse_weave',
    'mode_196_supernova_countdown',
    'mode_197_martian_wind_harp',
    'mode_198_teleporting_bar_choir',
    'mode_199_cosmic_vinyl_halo',
    'mode_200_photon_origination_chamber',
    'mode_201_meteor_net',
    'mode_202_deep_space_garden_hose',
    'mode_203_horizon_monoliths',
    'mode_205_solar_flare_notches',
    'mode_206_tesseract_window',
    'mode_207_interstellar_postcards',
    'mode_209_stellar_harpoon',
    'mode_210_galaxy_ticker_tape',
    'mode_211_antimatter_chess',
    'mode_212_star_nursery_conveyor',
    'mode_213_magnetar_lines',
    'mode_214_zero_kelvin_diamonds',
    'mode_215_orbital_time_garden',
    'mode_216_subspace_ribbon_printer',
    'mode_217_dark_matter_drizzle',
    'mode_218_meteor_choir_cones',
    'mode_219_folded_galaxy_map',
    'mode_220_ion_thruster_plume',
    'mode_221_cosmic_dominoes',
    'mode_222_spacesuit_hud',
    'mode_223_pulsar_barcode_beam',
    'mode_224_astro_terrarium',
    'mode_277_prism_rays',
    'mode_279_silk_road_caravan',
    'mode_280_steampunk_gears',
    'mode_281_dragon_scales',
    'mode_282_time_dilation_grid',
    'mode_283_fiber_bundle',
    'mode_284_moth_wing_shimmer',
    'mode_285_cathedral_rose',
    'mode_287_glacial_crack',
    'mode_289_origami_crane_flight',
    'mode_290_magma_chamber',
    'mode_291_spider_web_dew',
    'mode_292_nebula_birth',
    'mode_294_bioluminescent_tide',
    'mode_295_tesseract_projection',
    'mode_297_sound_wave_interference',
    'mode_298_holographic_fracture',
    'mode_300_eternal_flame_dance',
    'mode_309_leaf_fall',
    'mode_312_pond_koi',
    'mode_313_moss_growth',
    'mode_315_dandelion_seeds',
    'mode_316_fern_fractals',
    'mode_317_beehive_cells',
    'mode_318_wheat_field',
    'mode_319_spider_web',
    'mode_320_mushroom_spores',
    'mode_322_tide_pools',
    'mode_323_vine_tendrils',
    'mode_325_bird_murmuration',
    'mode_326_river_flow',
    'mode_327_seed_pods',
    'mode_328_algae_bloom',
    'mode_329_cactus_spines',
    'mode_330_snowflakes',
    'mode_333_pine_cones',
    'mode_334_geyser_eruption',
    'mode_335_pollen_cloud',
    'mode_336_desert_dunes',
    'mode_337_lily_pads',
    'mode_338_termite_mound',
    'mode_339_cherry_blossoms',
    'mode_340_root_system',
    'mode_342_frost_patterns',
    'mode_344_seaweed_sway',
    'mode_345_volcano_ash',
    'mode_346_dragonfly_wings',
    'mode_347_pebble_ripples',
    'mode_348_moss_tendrils',
    'mode_349_starfish_arms',
    'mode_350_venus_flytrap',
    'mode_353_snake_scales',
    'mode_354_whirlpool',
    'mode_355_owl_eyes',
    'mode_356_tornado_funnel',
    'mode_357_peacock_feathers',
    'mode_358_jellyfish_pulse',
    'mode_359_sand_ripples',
    'mode_361_tide_motion',
    'mode_362_lichen_growth',
    'mode_363_eagle_soar',
    'mode_364_mangrove_roots',
    'mode_366_dolphin_leap',
    'mode_367_tumbleweed_roll',
    'mode_369_smoke_wisps',
    'mode_370_nautilus_shell',
    'mode_371_wolf_howl',
    'mode_372_seashell_patterns',
    'mode_373_grass_blades',
    'mode_374_stalactites',
    'mode_375_amoeba_movement',
    'mode_376_pine_needles',
    'mode_378_succulent_rosette',
    'mode_379_salmon_upstream',
    'mode_380_cloud_formation',
    'mode_382_clover_field',
    'mode_383_geyser_field',
    'mode_384_insect_compound_eye',
    'mode_386_sand_dollar',
    'mode_387_glacier_crevasse',
    'mode_388_antler_growth',
    'mode_389_plume_worm',
    'mode_390_reed_marsh',
    'mode_391_beetle_shell',
    'mode_392_tide_anemone',
    'mode_393_earthquake_waves',
    'mode_394_butterfly_lifecycle',
    'mode_395_coconut_palm',
    'mode_396_frost_ferns',
    'mode_397_bioluminescent_bay',
    'mode_398_erosion_patterns',
    'mode_399_hedge_maze',
    'mode_402_double_helix',
    'mode_404_wave_interference',
    'mode_409_fission_reaction',
    'mode_410_doppler_effect',
    'mode_411_gravity_well',
    'mode_412_prism_spectrum',
    'mode_413_molecular_bonds',
    'mode_414_standing_wave',
    'mode_415_brownian_motion',
    'mode_416_tesla_coil',
    'mode_417_phase_transition',
    'mode_418_superconductor',
    'mode_419_neuron_firing',
    'mode_420_resonance_modes',
    'mode_421_fractal_diffusion',
    'mode_423_coriolis_effect',
    'mode_424_photoelectric_effect',
    'mode_425_lorenz_attractor',
    'mode_426_spin_precession',
    'mode_427_compton_scattering',
    'mode_429_sonoluminescence',
    'mode_430_cherenkov_radiation',
    'mode_431_hall_effect',
    'mode_432_cymatics',
    'mode_433_klein_bottle',
    'mode_434_raman_scattering',
    'mode_435_vortex_shedding',
    'mode_436_polarization',
    'mode_437_higgs_field',
    'mode_438_bose_einstein',
    'mode_439_schrodinger_cat',
    'mode_440_string_vibration',
    'mode_441_electron_cloud',
    'mode_442_thermoelectric',
    'mode_443_photon_entanglement',
    'mode_445_piezoelectric',
    'mode_446_zeeman_effect',
    'mode_447_cyclotron_motion',
    'mode_448_fusion_reactor',
    'mode_449_antimatter',
    'mode_450_hawking_radiation',
    'mode_453_laser_cavity',
    'mode_454_dielectric_breakdown',
    'mode_455_casimir_effect',
    'mode_456_sonochemistry',
    'mode_457_phonon_propagation',
    'mode_459_stefan_boltzmann',
    'mode_460_eddy_currents',
    'mode_461_wavefunction_collapse',
    'mode_462_qed_feynman',
    'mode_463_holography',
    'mode_464_metamaterial',
    'mode_465_photodiode',
    'mode_466_bremsstrahlung',
    'mode_467_optogenetics',
    'mode_468_topological_insulator',
    'mode_469_nernst_equation',
    'mode_470_mri_precession',
    'mode_471_josephson_junction',
    'mode_474_cavity_qed',
    'mode_476_soliton_wave',
    'mode_477_acoustic_levitation',
    'mode_478_mosfet_channel',
    'mode_479_spintronics',
    'mode_480_electrochemistry',
    'mode_481_langmuir_wave',
    'mode_482_bloch_sphere',
    'mode_483_curie_temperature',
    'mode_484_dyson_sphere',
    'mode_485_graphene_lattice',
    'mode_486_memristor',
    'mode_488_optomechanics',
    'mode_489_exciton',
    'mode_491_skyrmion',
    'mode_492_mott_insulator',
    'mode_493_squeezing',
    'mode_494_andreev_reflection',
    'mode_495_casimir_polder',
    'mode_496_fano_resonance',
    'mode_498_rabi_oscillation',
    'mode_499_aharonov_bohm',
    'mode_500_berry_phase',
    'mode_501_impressionist',
    'mode_502_cubist',
    'mode_503_surreal',
    'mode_504_abstract_expressionist',
    'mode_505_pop_art',
    'mode_506_minimalist',
    'mode_507_pointillist',
    'mode_508_art_deco',
    'mode_509_art_nouveau',
    'mode_510_bauhaus',
    'mode_511_futurist',
    'mode_513_expressionist',
    'mode_514_fauvism',
    'mode_515_constructivist',
    'mode_516_suprematist',
    'mode_517_vorticism',
    'mode_518_orphism',
    'mode_519_rayonism',
    'mode_520_synchromism',
    'mode_521_precisionism',
    'mode_522_regionalism',
    'mode_523_social_realism',
    'mode_524_neo_plasticism',
    'mode_525_de_stijl',
    'mode_526_color_field',
    'mode_527_hard_edge',
    'mode_528_lyrical_abstraction',
    'mode_529_tachisme',
    'mode_532_shaped_canvas',
    'mode_533_monochrome',
    'mode_534_kinetic_art',
    'mode_535_op_art',
    'mode_536_light_art',
    'mode_537_land_art',
    'mode_538_earth_art',
    'mode_539_environmental_art',
    'mode_540_installation_art',
    'mode_541_video_art',
    'mode_542_digital_art',
    'mode_543_glitch_art',
    'mode_544_pixel_art',
    'mode_545_ascii_art',
    'mode_546_vector_art',
    'mode_547_fractal_art',
    'mode_548_algorithmic_art',
    'mode_549_generative_art',
    'mode_550_data_art',
    'mode_551_bio_art',
    'mode_552_net_art',
    'mode_553_software_art',
    'mode_554_robotic_art',
    'mode_555_interactive_art',
    'mode_556_projection_mapping',
    'mode_557_holographic_art',
    'mode_558_augmented_reality_art',
    'mode_106_aurora_waves',
    'mode_559_vr_art',
    'mode_560_procedural_art',
    'mode_561_parametric_art',
    'mode_562_mathematical_art',
    'mode_563_geometric_art',
    'mode_564_tessellation_art',
    'mode_565_symmetry_art',
    'mode_567_mandala_art',
    'mode_568_zentangle_art',
    'mode_569_doodle_art',
    'mode_571_graffiti_art',
    'mode_572_mural_art',
    'mode_573_stencil_art',
    'mode_574_wheat_paste_art',
    'mode_577_collage_art',
    'mode_578_mixed_media_art',
    'mode_579_assemblage_art',
    'mode_580_found_object_art',
    'mode_581_readymade_art',
    'mode_582_appropriation_art',
    'mode_583_sampling_art',
    'mode_584_remix_art',
    'mode_585_mashup_art',
    'mode_586_photomontage',
    'mode_587_cut_up_technique',
    'mode_588_exquisite_corpse',
    'mode_589_automatic_drawing',
    'mode_590_chance_art',
    'mode_591_indeterminacy_art',
    'mode_592_aleatory_art',
    'mode_593_stochastic_art',
    'mode_594_entropy_art',
    'mode_595_chaos_art',
    'mode_596_complexity_art',
    'mode_597_emergence_art',
    'mode_598_self_organization_art',
    'mode_600_flocking_art',
    'mode_714_public_key',
    'mode_716_zero_knowledge_proof',
    'mode_717_homomorphic_encryption',
    'mode_718_secure_multiparty_computation',
    'mode_719_differential_privacy',
    'mode_720_federated_learning',
    'mode_722_deep_learning',
    'mode_723_convolutional_layer',
    'mode_724_recurrent_connection',
    'mode_725_attention_mechanism',
    'mode_726_transformer_architecture',
    'mode_727_residual_connection',
    'mode_728_skip_connection',
    'mode_729_batch_normalization',
    'mode_730_dropout_regularization',
    'mode_731_activation_function',
    'mode_732_gradient_descent',
    'mode_733_backpropagation',
    'mode_734_loss_landscape',
    'mode_735_optimizer_trajectory',
    'mode_736_learning_rate_schedule',
    'mode_737_momentum',
    'mode_738_adaptive_learning',
    'mode_739_weight_decay',
    'mode_740_early_stopping',
    'mode_741_cross_validation',
    'mode_742_ensemble_method',
    'mode_743_boosting',
    'mode_744_bagging',
    'mode_747_support_vector_machine',
    'mode_748_kernel_trick',
    'mode_749_feature_space',
    'mode_750_dimensionality_reduction',
    'mode_751_principal_component_analysis',
    'mode_752_t_sne_embedding',
    'mode_753_autoencoder_latent_space',
    'mode_754_variational_autoencoder',
    'mode_755_generative_adversarial_network',
    'mode_756_discriminator_network',
    'mode_757_generator_network',
    'mode_758_style_transfer',
    'mode_759_content_loss',
    'mode_761_perceptual_loss',
    'mode_762_adversarial_loss',
    'mode_763_cycle_consistency',
    'mode_764_identity_loss',
    'mode_765_reconstruction_loss',
    'mode_766_kl_divergence',
    'mode_767_wasserstein_distance',
    'mode_768_earth_mover_distance',
    'mode_769_inception_score',
    'mode_770_frechet_inception_distance',
    'mode_771_bleu_score',
    'mode_772_rouge_score',
    'mode_773_perplexity',
    'mode_774_cross_entropy',
    'mode_775_mutual_information',
    'mode_776_information_bottleneck',
    'mode_777_rate_distortion',
    'mode_778_source_coding',
    'mode_779_channel_coding',
    'mode_780_error_correction',
    'mode_781_hamming_distance',
    'mode_782_reed_solomon',
    'mode_783_turbo_code',
    'mode_784_ldpc_code',
    'mode_785_polar_code',
    'mode_787_surface_code',
    'mode_788_toric_code',
    'mode_789_color_code',
    'mode_790_stabilizer_formalism',
    'mode_791_clifford_gate',
    'mode_792_pauli_group',
    'mode_801_mandala',
    'mode_802_yantra',
    'mode_803_lotus',
    'mode_804_om_symbol',
    'mode_805_chakra',
    'mode_806_aura_field',
    'mode_807_third_eye',
    'mode_808_kundalini',
    'mode_809_merkaba',
    'mode_811_seed_of_life',
    'mode_813_metatron_cube',
    'mode_814_sri_yantra',
    'mode_815_shri_yantra',
    'mode_816_tibetan_sand_mandala',
    'mode_817_zen_circle',
    'mode_818_yin_yang',
    'mode_819_tao_symbol',
    'mode_820_bagua',
    'mode_821_i_ching_hexagram',
    'mode_822_trigram',
    'mode_823_medicine_wheel',
    'mode_824_dreamcatcher',
    'mode_825_totem',
    'mode_826_spirit_animal',
    'mode_827_shamanic_journey',
    'mode_828_ayahuasca_vision',
    'mode_829_dmt_realm',
    'mode_830_astral_projection',
    'mode_831_out_of_body_experience',
    'mode_832_near_death_experience',
    'mode_833_tunnel_of_light',
    'mode_834_life_review',
    'mode_835_soul_retrieval',
    'mode_836_past_life_regression',
    'mode_837_akashic_records',
    'mode_838_collective_unconscious',
    'mode_839_archetypal_realm',
    'mode_840_synchronicity',
    'mode_841_meaningful_coincidence',
    'mode_842_serendipity',
    'mode_843_providence',
    'mode_844_fate',
    'mode_845_destiny',
    'mode_846_karma',
    'mode_847_dharma',
    'mode_848_samsara',
    'mode_849_nirvana',
    'mode_850_enlightenment',
    'mode_851_samadhi',
    'mode_852_satori',
    'mode_853_kensho',
    'mode_854_moksha',
    'mode_855_liberation',
    'mode_856_self_realization',
    'mode_857_god_consciousness',
    'mode_858_cosmic_consciousness',
    'mode_859_unity_consciousness',
    'mode_860_non_dual_awareness',
    'mode_861_witness_consciousness',
    'mode_862_pure_awareness',
    'mode_863_presence',
    'mode_864_now_moment',
    'mode_865_eternal_present',
    'mode_866_timeless_being',
    'mode_867_infinite_space',
    'mode_868_boundless_compassion',
    'mode_869_unconditional_love',
    'mode_870_divine_grace',
    'mode_871_holy_spirit',
    'mode_872_shekinah',
    'mode_873_divine_feminine',
    'mode_875_sacred_masculine',
    'mode_876_hieros_gamos',
    'mode_877_alchemical_wedding',
    'mode_878_coniunctio',
    'mode_879_philosopher_stone',
    'mode_880_prima_materia',
    'mode_881_nigredo',
    'mode_882_albedo',
    'mode_883_citrinitas',
    'mode_884_rubedo',
    'mode_885_seven_stages',
    'mode_886_hermetic_principle',
    'mode_887_as_above_so_below',
    'mode_888_microcosm_macrocosm',
    'mode_889_correspondence',
    'mode_890_vibration',
    'mode_891_polarity',
    'mode_892_rhythm',
    'mode_893_cause_and_effect',
    'mode_894_gender_principle',
    'mode_895_mentalism',
    'mode_896_emerald_tablet',
    'mode_897_kybalion',
    'mode_898_corpus_hermeticum',
    'mode_899_gnostic_vision',
    'mode_900_sophia',
    'mode_901_spiral_vortex',
    'mode_902_concentric_circles',
    'mode_903_expanding_rings',
    'mode_904_contracting_circles',
    'mode_905_pulsing_orb',
    'mode_906_oscillating_wave',
    'mode_907_pendulum_swing',
    'mode_908_hypnotic_swirl',
    'mode_909_tunnel_zoom',
    'mode_910_perspective_shift',
    'mode_911_rotating_polygon',
    'mode_912_morphing_shape',
    'mode_914_ripple_effect',
    'mode_915_interference_pattern',
    'mode_916_moire_effect',
    'mode_917_strobing_light',
    'mode_918_flickering',
    'mode_919_pulsating',
    'mode_920_breathing_pattern',
    'mode_921_expansion_contraction',
    'mode_922_growth_decay',
    'mode_923_birth_death',
    'mode_924_ebb_flow',
    'mode_925_inhale_exhale',
    'mode_926_systole_diastole',
    'mode_927_tension_release',
    'mode_928_charge_discharge',
    'mode_929_loading_unloading',
    'mode_930_compression_rarefaction',
    'mode_931_dense_sparse',
    'mode_932_thick_thin',
    'mode_933_heavy_light',
    'mode_934_dark_bright',
    'mode_935_shadow_highlight',
    'mode_936_positive_negative',
    'mode_937_convex_concave',
    'mode_938_inside_outside',
    'mode_939_figure_ground',
    'mode_940_foreground_background',
    'mode_941_solid_void',
    'mode_942_matter_antimatter',
    'mode_944_discrete_continuous',
    'mode_945_quantized_smooth',
    'mode_946_digital_analog',
    'mode_948_on_off',
    'mode_949_yes_no',
    'mode_950_zero_one',
    'mode_951_presence_absence',
    'mode_952_being_nothingness',
    'mode_953_existence_void',
    'mode_954_form_emptiness',
    'mode_955_substance_essence',
    'mode_956_appearance_reality',
    'mode_957_illusion_truth',
    'mode_958_maya_brahman',
    'mode_959_phenomena_noumena',
    'mode_960_relative_absolute',
    'mode_961_changing_unchanging',
    'mode_962_temporal_eternal',
    'mode_963_finite_infinite',
    'mode_964_limited_boundless',
    'mode_965_mortal_immortal',
    'mode_966_perishable_imperishable',
    'mode_967_transient_permanent',
    'mode_968_fleeting_lasting',
    'mode_969_ephemeral_enduring',
    'mode_970_momentary_timeless',
    'mode_971_local_universal',
    'mode_972_particular_general',
    'mode_973_specific_generic',
    'mode_974_unique_common',
    'mode_975_individual_collective',
    'mode_976_one_many',
    'mode_977_unity_multiplicity',
    'mode_978_simple_complex',
    'mode_979_elementary_composite',
    'mode_981_fundamental_derived',
    'mode_982_primary_secondary',
    'mode_983_essential_accidental',
    'mode_984_necessary_contingent',
    'mode_985_a_priori_a_posteriori',
    'mode_986_analytic_synthetic',
    'mode_987_deductive_inductive',
    'mode_988_logical_empirical',
    'mode_989_rational_experiential',
    'mode_990_abstract_concrete',
    'mode_991_theoretical_practical',
    'mode_992_ideal_real',
    'mode_993_conceptual_actual',
    'mode_994_possible_necessary',
    'mode_995_potential_actual',
    'mode_996_virtual_real',
    'mode_997_simulated_genuine',
    'mode_998_artificial_natural',
    'mode_999_synthetic_organic',
    // Scientific 
    'dna_helix',
    'circuit_board',
    'mode_110_quantum_field',
    'mode_119_matrix_rain',
    'mode_124_magnetic_field',
    'mode_143_stained_glass',
    'mode_149_rain_circles',
    'mode_162_aurora_curtain',
    'mode_168_terrain_sweep',
    'mode_172_dna_ladder',
    'mode_178_quantum_foam_micro',
    'mode_181_hyperloop_spectrotrain',
    'mode_195_zero_g_paint_spheres',
    'mode_204_gravity_slingshot_trails',
    'mode_208_cosmic_braille',
    'mode_225_micrometeor_spark_curtain',
    'mode_276_quantum_lattice',
    'mode_288_quantum_dots',
    'mode_293_circuit_board_live',
    'mode_305_mountain_peaks',
    'mode_308_rain_ripples',
    'mode_343_ant_trails',
    'mode_351_rainbow_mist',
    'mode_381_fox_tail',
    'mode_401_atom_model',
    'mode_403_magnetic_field',
    'mode_407_electromagnetic_wave',
    'mode_408_quantum_tunneling',
    'mode_451_heisenberg_uncertainty',
    'mode_458_pair_production',
    'mode_473_rydberg_atoms',
    'mode_475_quantum_dots',
    'mode_487_quantum_hall',
    'mode_497_quantum_zeno',
    'mode_512_dadaist',
    'mode_530_action_painting',
    'mode_531_stain_painting',
    'mode_575_spray_paint_art',
    'mode_576_mosaic_art',
    'mode_609_comet_tail',
    'mode_623_tidal_tail',
    'mode_652_quantum_foam',
    'mode_670_quantum_decoherence',
    'mode_675_relational_quantum_mechanics',
    'mode_676_quantum_bayesianism',
    'mode_680_quantum_darwinism',
    'mode_701_binary_rain',
    'mode_703_circuit_board',
    'mode_711_blockchain',
    'mode_721_neural_network',
    'mode_786_quantum_error_correction',
    'mode_793_measurement_based_quantum_computing',
    'mode_794_one_way_quantum_computer',
    'mode_795_adiabatic_quantum_computation',
    'mode_796_quantum_annealing',
    'mode_797_variational_quantum_eigensolver',
    'mode_798_quantum_approximate_optimization',
    'mode_799_quantum_phase_estimation',
    'mode_800_quantum_fourier_transform',
    'mode_107_dna_helix',
    'mode_109_circuit_board',
    //tech
    'mode_123_neon_city',
    'mode_151_neon_halo_burst',
    'mode_286_neon_veins_pulse',
    'mode_696_retrocausality',
    'mode_760_gram_matrix',
    'shattering_glass',
    'mode_116_lightning_storm',
    'mode_130_plasma_ball',
    'mode_299_plasma_ball_arc',
    'mode_311_lightning_storm',
    'mode_422_plasma_ball',
    'mode_659_dark_energy',
    '',
    '',
    '',
    '',
    '',
    '',
];


// Visualization Modes with Categories
const VISUALIZATION_MODES = {
    // Classic Styles
    circular_bars: {
        id: 'circular_bars',
        name: 'Circular Bars',
        description: 'Classic radial bars extending from center',
        category: 'Classic',
        mode: 1,
        tags: ['radial', 'bars', 'classic'],
        parameters: {
            barCount: { min: 32, max: 128, default: 64, label: 'Bar Count' },
            innerRadius: { min: 50, max: 300, default: 150, label: 'Inner Radius' },
            barWidth: { min: 1, max: 10, default: 4, label: 'Bar Width' }
        }
    },
    waves: {
        id: 'waves',
        name: 'Waves',
        description: 'Concentric waves that pulse with music',
        category: 'Classic',
        mode: 2,
        tags: ['waves', 'pulse', 'smooth'],
        parameters: {
            waveCount: { min: 3, max: 15, default: 8, label: 'Wave Count' },
            waveSpeed: { min: 0.1, max: 3, default: 1, label: 'Wave Speed' },
            amplitude: { min: 0.5, max: 2, default: 1, label: 'Wave Amplitude' }
        }
    },
    smooth_waveform: {
        id: 'smooth_waveform',
        name: 'Smooth Waveform',
        description: 'Elegant continuous waveform',
        category: 'Classic',
        mode: 4,
        tags: ['waveform', 'smooth', 'elegant'],
        parameters: {
            lineWidth: { min: 1, max: 10, default: 3, label: 'Line Width' },
            amplitude: { min: 0.5, max: 2, default: 1, label: 'Amplitude' },
            smoothness: { min: 0.5, max: 1, default: 0.85, label: 'Smoothness' }
        }
    },
    frequency_bars: {
        id: 'frequency_bars',
        name: 'Frequency Bars',
        description: 'Traditional frequency spectrum bars',
        category: 'Classic',
        mode: 11,
        tags: ['bars', 'spectrum', 'traditional'],
        parameters: {
            barCount: { min: 32, max: 128, default: 64, label: 'Bar Count' },
            barWidth: { min: 2, max: 20, default: 8, label: 'Bar Width' },
            spacing: { min: 1, max: 10, default: 2, label: 'Bar Spacing' }
        }
    },
    linear_spectrum: {
        id: 'linear_spectrum',
        name: 'Linear Spectrum',
        description: 'Horizontal frequency bars',
        category: 'Classic',
        mode: 12,
        tags: ['linear', 'horizontal', 'clean'],
        parameters: {
            barCount: { min: 32, max: 128, default: 64, label: 'Bar Count' },
            barHeight: { min: 50, max: 400, default: 200, label: 'Max Bar Height' },
            spacing: { min: 1, max: 10, default: 3, label: 'Bar Spacing' }
        }
    },
    classic_bars: {
        id: 'classic_bars',
        name: 'Classic Bars',
        description: 'Traditional vertical bars visualization',
        category: 'Classic',
        mode: 851,
        tags: ['bars', 'vertical', 'classic', 'lines'],
        parameters: {
            barWidth: { min: 2, max: 20, default: 8, label: 'Bar Width' },
            barSpacing: { min: 1, max: 10, default: 2, label: 'Bar Spacing' },
            barRounding: { min: 0, max: 10, default: 0, label: 'Bar Rounding' }
        }
    },
    mirror_symmetry: {
        id: 'mirror_symmetry',
        name: 'Mirror Symmetry',
        description: 'Mirrored visualization with central symmetry',
        category: 'Classic',
        mode: 852,
        tags: ['mirror', 'symmetry', 'lines'],
        parameters: {
            barWidth: { min: 2, max: 20, default: 8, label: 'Bar Width' },
            barSpacing: { min: 1, max: 10, default: 2, label: 'Bar Spacing' },
            mirrorGap: { min: 0, max: 100, default: 20, label: 'Mirror Gap' }
        }
    },
    waterfall: {
        id: 'waterfall',
        name: 'Waterfall',
        description: 'Cascading effect with trailing bars',
        category: 'Classic',
        mode: 853,
        tags: ['waterfall', 'cascade', 'lines'],
        parameters: {
            trailLength: { min: 3, max: 20, default: 10, label: 'Trail Length' },
            fallSpeed: { min: 1, max: 10, default: 5, label: 'Fall Speed' },
            fadeAmount: { min: 0.1, max: 0.9, default: 0.5, label: 'Fade Amount' }
        }
    },
    converging_lines: {
        id: 'converging_lines',
        name: 'Converging Lines',
        description: 'Lines meeting at center point',
        category: 'Classic',
        mode: 854,
        tags: ['converging', 'radial', 'lines'],
        parameters: {
            lineCount: { min: 20, max: 100, default: 50, label: 'Line Count' },
            convergencePoint: { min: 0.3, max: 0.7, default: 0.5, label: 'Convergence Point' },
            lineWidth: { min: 1, max: 10, default: 2, label: 'Line Width' }
        }
    },
    wave_morph: {
        id: 'wave_morph',
        name: 'Wave Morph',
        description: 'Morphing wave patterns with dynamic shapes',
        category: 'Classic',
        mode: 855,
        tags: ['wave', 'morph', 'lines'],
        parameters: {
            waveAmplitude: { min: 10, max: 100, default: 50, label: 'Wave Amplitude' },
            waveFrequency: { min: 1, max: 10, default: 3, label: 'Wave Frequency' },
            morphSpeed: { min: 0.1, max: 2, default: 0.5, label: 'Morph Speed' }
        }
    },
    staggered_pulse: {
        id: 'staggered_pulse',
        name: 'Staggered Pulse',
        description: 'Offset pulsing bars with delay effect',
        category: 'Classic',
        mode: 856,
        tags: ['pulse', 'stagger', 'lines'],
        parameters: {
            staggerAmount: { min: 0, max: 10, default: 3, label: 'Stagger Amount' },
            pulseSpeed: { min: 0.5, max: 3, default: 1, label: 'Pulse Speed' },
            barCount: { min: 30, max: 120, default: 60, label: 'Bar Count' }
        }
    },
    geometric_tunnel: {
        id: 'geometric_tunnel',
        name: 'Geometric Tunnel',
        description: '3D tunnel effect with perspective',
        category: 'Classic',
        mode: 857,
        tags: ['3d', 'tunnel', 'geometric', 'lines'],
        parameters: {
            tunnelDepth: { min: 3, max: 15, default: 8, label: 'Tunnel Depth' },
            rotationSpeed: { min: 0, max: 5, default: 1, label: 'Rotation Speed' },
            segmentCount: { min: 3, max: 12, default: 6, label: 'Segment Count' }
        }
    },
    dancing_ribbons: {
        id: 'dancing_ribbons',
        name: 'Dancing Ribbons',
        description: 'Flowing ribbon-like curves',
        category: 'Classic',
        mode: 858,
        tags: ['ribbons', 'flow', 'lines'],
        parameters: {
            ribbonWidth: { min: 5, max: 50, default: 20, label: 'Ribbon Width' },
            flowSpeed: { min: 0.5, max: 3, default: 1.5, label: 'Flow Speed' },
            waveCount: { min: 2, max: 10, default: 4, label: 'Wave Count' }
        }
    },
    particle_stream: {
        id: 'particle_stream',
        name: 'Particle Stream',
        description: 'Particle streams flowing along lines',
        category: 'Classic',
        mode: 859,
        tags: ['particles', 'stream', 'lines'],
        parameters: {
            particleCount: { min: 50, max: 500, default: 200, label: 'Particle Count' },
            streamSpeed: { min: 1, max: 10, default: 5, label: 'Stream Speed' },
            particleSize: { min: 1, max: 10, default: 3, label: 'Particle Size' }
        }
    },
    glitch_art: {
        id: 'glitch_art',
        name: 'Glitch Art',
        description: 'Glitch aesthetic with digital artifacts',
        category: 'Classic',
        mode: 860,
        tags: ['glitch', 'digital', 'art', 'lines'],
        parameters: {
            glitchIntensity: { min: 0.1, max: 1, default: 0.5, label: 'Glitch Intensity' },
            glitchFrequency: { min: 0.1, max: 1, default: 0.3, label: 'Glitch Frequency' },
            colorShift: { min: 0, max: 50, default: 10, label: 'Color Shift' }
        }
    },
    circular_waves: {
        id: 'circular_waves',
        name: 'Circular Waves',
        description: 'Concentric circular waves that expand from center',
        category: 'Classic',
        mode: 861,
        tags: ['circular', 'waves', 'ripple', 'classic'],
        parameters: {
            waveCount: { min: 5, max: 20, default: 10, label: 'Wave Count' },
            waveThickness: { min: 1, max: 10, default: 3, label: 'Wave Thickness' },
            waveSpacing: { min: 10, max: 50, default: 25, label: 'Wave Spacing' }
        }
    },
    line_spectrum: {
        id: 'line_spectrum',
        name: 'Line Spectrum',
        description: 'Horizontal frequency lines stacked vertically',
        category: 'Classic',
        mode: 862,
        tags: ['lines', 'horizontal', 'spectrum', 'classic'],
        parameters: {
            lineCount: { min: 20, max: 100, default: 50, label: 'Line Count' },
            lineThickness: { min: 1, max: 10, default: 2, label: 'Line Thickness' },
            lineSpacing: { min: 2, max: 20, default: 5, label: 'Line Spacing' }
        }
    },
    radial_pulse: {
        id: 'radial_pulse',
        name: 'Radial Pulse',
        description: 'Pulsing circles radiating from center',
        category: 'Classic',
        mode: 863,
        tags: ['radial', 'pulse', 'circles', 'classic'],
        parameters: {
            ringCount: { min: 5, max: 30, default: 15, label: 'Ring Count' },
            pulseIntensity: { min: 0.5, max: 2, default: 1, label: 'Pulse Intensity' },
            ringThickness: { min: 1, max: 10, default: 4, label: 'Ring Thickness' }
        }
    },
    double_helix: {
        id: 'double_helix',
        name: 'Double Helix',
        description: 'DNA-like double spiral pattern',
        category: 'Classic',
        mode: 864,
        tags: ['helix', 'spiral', 'dna', 'classic'],
        parameters: {
            helixTurns: { min: 2, max: 10, default: 5, label: 'Helix Turns' },
            helixWidth: { min: 50, max: 200, default: 100, label: 'Helix Width' },
            pointSize: { min: 2, max: 15, default: 6, label: 'Point Size' }
        }
    },
    spiral_bars: {
        id: 'spiral_bars',
        name: 'Spiral Bars',
        description: 'Frequency bars arranged in spiral pattern',
        category: 'Classic',
        mode: 865,
        tags: ['spiral', 'bars', 'rotation', 'classic'],
        parameters: {
            spiralTurns: { min: 1, max: 8, default: 3, label: 'Spiral Turns' },
            barLength: { min: 20, max: 100, default: 50, label: 'Bar Length' },
            spiralTightness: { min: 0.5, max: 2, default: 1, label: 'Spiral Tightness' }
        }
    },
    classic_particles: {
        id: 'classic_particles',
        name: 'Particles',
        description: 'Classic glowing particle system',
        category: 'Classic',
        mode: 3,
        tags: ['particles', 'glow', 'dynamic', 'classic'],
        parameters: {
            particleCount: { min: 50, max: 500, default: 200, label: 'Particle Count' },
            particleSize: { min: 1, max: 10, default: 3, label: 'Particle Size' },
            glowIntensity: { min: 0.1, max: 2, default: 1, label: 'Glow Intensity' }
        }
    },
    classic_polygon: {
        id: 'classic_polygon',
        name: 'Polygon',
        description: 'Geometric polygon that pulses with music',
        category: 'Classic',
        mode: 5,
        tags: ['geometric', 'polygon', 'classic'],
        parameters: {
            sides: { min: 3, max: 12, default: 6, label: 'Number of Sides' },
            rotationSpeed: { min: 0, max: 5, default: 1, label: 'Rotation Speed' },
            pulseIntensity: { min: 0.1, max: 2, default: 1, label: 'Pulse Intensity' }
        }
    },
    classic_spiral: {
        id: 'classic_spiral',
        name: 'Spiral',
        description: 'Spiral pattern radiating from center',
        category: 'Classic',
        mode: 6,
        tags: ['spiral', 'rotation', 'classic'],
        parameters: {
            spiralArms: { min: 1, max: 8, default: 3, label: 'Spiral Arms' },
            tightness: { min: 0.1, max: 2, default: 1, label: 'Spiral Tightness' },
            rotationSpeed: { min: 0, max: 5, default: 1, label: 'Rotation Speed' }
        }
    },
    classic_dna_helix: {
        id: 'classic_dna_helix',
        name: 'DNA Helix',
        description: 'Double helix structure twisting with music',
        category: 'Classic',
        mode: 7,
        tags: ['helix', 'dna', 'classic'],
        parameters: {
            helixTightness: { min: 0.5, max: 3, default: 1, label: 'Helix Tightness' },
            rotationSpeed: { min: 0, max: 5, default: 1.5, label: 'Rotation Speed' },
            basePairs: { min: 10, max: 40, default: 20, label: 'Base Pairs' }
        }
    },
    classic_kaleidoscope: {
        id: 'classic_kaleidoscope',
        name: 'Kaleidoscope',
        description: 'Mirrored symmetric patterns',
        category: 'Classic',
        mode: 8,
        tags: ['kaleidoscope', 'symmetry', 'classic'],
        parameters: {
            segments: { min: 4, max: 16, default: 8, label: 'Mirror Segments' },
            complexity: { min: 1, max: 10, default: 5, label: 'Pattern Complexity' },
            rotationSpeed: { min: 0, max: 5, default: 1, label: 'Rotation Speed' }
        }
    },
    classic_pulse_rings: {
        id: 'classic_pulse_rings',
        name: 'Pulse Rings',
        description: 'Pulsing concentric rings',
        category: 'Classic',
        mode: 9,
        tags: ['rings', 'pulse', 'classic'],
        parameters: {
            ringCount: { min: 3, max: 15, default: 8, label: 'Number of Rings' },
            pulseSpeed: { min: 0.1, max: 3, default: 1, label: 'Pulse Speed' },
            spacing: { min: 10, max: 50, default: 25, label: 'Ring Spacing' }
        }
    },
    classic_star_burst: {
        id: 'classic_star_burst',
        name: 'Star Burst',
        description: 'Starburst effect radiating from center',
        category: 'Classic',
        mode: 10,
        tags: ['starburst', 'radial', 'classic'],
        parameters: {
            rayCount: { min: 8, max: 64, default: 24, label: 'Number of Rays' },
            rayLength: { min: 0.3, max: 1.5, default: 1, label: 'Ray Length' },
            pulseIntensity: { min: 0.1, max: 2, default: 1, label: 'Pulse Intensity' }
        }
    },

    // Particle Effects
    jazzy_fireworks: {
        id: 'jazzy_fireworks',
        name: 'Jazzy Fireworks',
        description: 'Bursting particles from center with jazz energy',
        category: 'Particles',
        mode: 47,
        tags: ['particles', 'explosive', 'jazz', 'rainbow'],
        parameters: {
            particleCount: { min: 50, max: 400, default: 200, label: 'Particle Count' },
            speed: { min: 5, max: 20, default: 10, label: 'Burst Speed' },
            secondaryBursts: { min: 0, max: 5, default: 3, label: 'Secondary Bursts' }
        }
    },
    particles: {
        id: 'particles',
        name: 'Particles',
        description: 'Glowing particle system',
        category: 'Particles',
        mode: 103,
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
    fog_smoke: {
        id: 'fog_smoke',
        name: 'Fog/Smoke',
        description: 'Wispy fog and smoke effects with audio-reactive turbulence',
        category: 'Nature',
        mode: 1008,
        tags: ['nature', 'atmospheric', 'fog', 'smoke', 'wispy'],
        parameters: {
            density: { min: 0.3, max: 1.5, default: 0.7, label: 'Particle Density' },
            speed: { min: 0.1, max: 2, default: 0.5, label: 'Movement Speed' },
            dissipation: { min: 0, max: 1, default: 0.3, label: 'Dissipation Rate' },
            particleSize: { min: 20, max: 100, default: 50, label: 'Particle Size' },
            drift: { min: 0, max: 3, default: 1, label: 'Drift Amount' },
            turbulence: { min: 0, max: 2, default: 0.5, label: 'Turbulence' }
        }
    },
    clouds: {
        id: 'clouds',
        name: 'Clouds',
        description: 'Fluffy drifting clouds with audio-reactive puffiness',
        category: 'Nature',
        mode: 1009,
        tags: ['nature', 'clouds', 'fluffy', 'atmospheric'],
        parameters: {
            cloudCount: { min: 3, max: 30, default: 12, label: 'Number of Clouds' },
            cloudSize: { min: 0.3, max: 2.5, default: 1, label: 'Cloud Size' },
            puffiness: { min: 0.2, max: 1.5, default: 0.7, label: 'Puffiness' },
            speed: { min: 0.1, max: 1.5, default: 0.3, label: 'Drift Speed' },
            verticalDrift: { min: 0, max: 1, default: 0.2, label: 'Vertical Drift' },
            density: { min: 0.2, max: 1.5, default: 0.8, label: 'Opacity/Density' }
        }
    },
    aurora_borealis: {
        id: 'aurora_borealis',
        name: 'Aurora Borealis',
        description: 'Flowing northern lights with audio-reactive waves and shimmer',
        category: 'Nature',
        mode: 1010,
        tags: ['nature', 'aurora', 'northern lights', 'atmospheric', 'flowing'],
        parameters: {
            waveCount: { min: 2, max: 8, default: 4, label: 'Number of Waves' },
            waveHeight: { min: 0.3, max: 2, default: 1, label: 'Wave Height' },
            flowSpeed: { min: 0.05, max: 1.5, default: 0.3, label: 'Flow Speed' },
            shimmer: { min: 0, max: 1.5, default: 0.7, label: 'Shimmer Intensity' },
            colorShift: { min: 0, max: 1, default: 0.5, label: 'Color Variation' },
            opacity: { min: 0.3, max: 1, default: 0.7, label: 'Opacity' }
        }
    },
    fireflies: {
        id: 'fireflies',
        name: 'Fireflies',
        description: 'Glowing fireflies floating and blinking in the night',
        category: 'Nature',
        mode: 1011,
        tags: ['nature', 'fireflies', 'particles', 'glow', 'night'],
        parameters: {
            fireflyCount: { min: 10, max: 100, default: 40, label: 'Number of Fireflies' },
            glowSize: { min: 2, max: 20, default: 8, label: 'Glow Size' },
            blinkSpeed: { min: 0.5, max: 3, default: 1.5, label: 'Blink Speed' },
            floatSpeed: { min: 0.1, max: 2, default: 0.5, label: 'Float Speed' },
            glowIntensity: { min: 0.3, max: 2, default: 1, label: 'Glow Intensity' },
            brightness: { min: 0.5, max: 1.5, default: 1, label: 'Brightness' }
        }
    },
    mode_1012_ocean_waves: {
        id: 'mode_1012_ocean_waves',
        name: 'Ocean Waves',
        description: 'Mode 1012: Realistic ocean waves with foam particles and audio-reactive swells',
        category: 'Nature',
        mode: 1012,
        tags: ['nature', 'ocean', 'waves', 'water', 'foam', 'sea'],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            waveHeight: { min: 0.3, max: 2, default: 1, label: 'Wave Height' },
            waveSpeed: { min: 0.1, max: 2, default: 0.5, label: 'Wave Speed' },
            foamDensity: { min: 0, max: 1, default: 0.5, label: 'Foam Density' },
            waveCount: { min: 2, max: 8, default: 4, label: 'Number of Waves' },
            glowIntensity: { min: 0, max: 30, default: 10, label: 'Glow Intensity' }
        }
    },
    mode_1016_quantum_flux: {
        id: 'mode_1016_quantum_flux',
        name: 'Quantum Flux',
        description: 'Mode 1016: Minimalist quantum particles phasing between wave and particle states',
        category: 'Energy',
        mode: 1016,
        tags: ['energy', 'quantum', 'particles', 'minimal', 'physics', 'modern'],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            particleCount: { min: 20, max: 150, default: 60, label: 'Particle Count' },
            phaseSpeed: { min: 0.5, max: 3, default: 1.5, label: 'Phase Speed' },
            waveAmplitude: { min: 0.2, max: 1.5, default: 0.7, label: 'Wave Amplitude' },
            coherence: { min: 0, max: 1, default: 0.5, label: 'Quantum Coherence' },
            glowIntensity: { min: 5, max: 40, default: 20, label: 'Glow Intensity' }
        }
    },
    mode_1017_photon_streams: {
        id: 'mode_1017_photon_streams',
        name: 'Photon Streams',
        description: 'Mode 1017: Elegant converging light beams with lens flare and refraction',
        category: 'Energy',
        mode: 1017,
        tags: ['energy', 'light', 'photon', 'minimal', 'elegant', 'modern'],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            streamCount: { min: 4, max: 24, default: 12, label: 'Stream Count' },
            flowSpeed: { min: 0.3, max: 3, default: 1.2, label: 'Flow Speed' },
            convergence: { min: 0, max: 1, default: 0.6, label: 'Convergence Point' },
            beamWidth: { min: 1, max: 8, default: 3, label: 'Beam Width' },
            glowIntensity: { min: 10, max: 50, default: 25, label: 'Glow Intensity' }
        }
    },
    mode_1018_magnetic_field: {
        id: 'mode_1018_magnetic_field',
        name: 'Magnetic Field',
        description: 'Mode 1018: Minimalist magnetic field lines flowing between reactive poles',
        category: 'Energy',
        mode: 1018,
        tags: ['energy', 'magnetic', 'field', 'minimal', 'physics', 'elegant'],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            fieldLines: { min: 8, max: 32, default: 16, label: 'Field Line Count' },
            poleDistance: { min: 0.3, max: 0.8, default: 0.6, label: 'Pole Distance' },
            curvature: { min: 0.3, max: 2, default: 1, label: 'Field Curvature' },
            pulseSpeed: { min: 0.5, max: 3, default: 1.5, label: 'Pulse Speed' },
            glowIntensity: { min: 5, max: 35, default: 18, label: 'Glow Intensity' }
        }
    },

    // Retro & Vintage
    soul_aura: {
        id: 'soul_aura',
        name: 'Soul Aura',
        description: 'Pulsing organic blob with soul/RnB vibe',
        category: 'Organic',
        mode: 49,
        tags: ['organic', 'soul', 'rnb', 'pulsing', 'aura'],
        parameters: {
            numPoints: { min: 30, max: 120, default: 60, label: 'Shape Complexity' },
            baseRadius: { min: 0.3, max: 0.8, default: 0.5, label: 'Base Size' },
            glowLayers: { min: 3, max: 8, default: 5, label: 'Glow Layers' }
        }
    },
    neon_rain: {
        id: 'neon_rain',
        name: 'Neon Rain',
        description: 'Cyberpunk neon droplets cascading down',
        category: 'Retro',
        mode: 46,
        tags: ['cyberpunk', 'neon', 'particles', 'rain'],
        parameters: {
            particleSize: { min: 2, max: 10, default: 5, label: 'Particle Size' },
            speed: { min: 3, max: 20, default: 10, label: 'Rain Speed' },
            spawnRate: { min: 0.1, max: 0.5, default: 0.3, label: 'Spawn Rate' }
        }
    },
    vinyl_grooves: {
        id: 'vinyl_grooves',
        name: 'Vinyl Grooves',
        description: 'Rotating vinyl record aesthetic',
        category: 'Retro',
        mode: 106,
        tags: ['vintage', 'vinyl', 'rotation']
    },
    neon_tubes: {
        id: 'neon_tubes',
        name: 'Neon Tubes',
        description: 'Minimal glowing neon tubes',
        category: 'Retro',
        mode: 105,
        tags: ['neon', 'minimal', 'glow']
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
        mode: 108,
        tags: ['fluid', 'metallic', 'smooth']
    },
    soul_aura: {
        id: 'soul_aura',
        name: 'Soul Aura',
        description: 'Pulsing organic ethereal glow',
        category: 'Fluid',
        mode: 107,
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
    organic_blob: {
        id: 'organic_blob',
        name: 'Organic Blob',
        description: 'Smooth flowing blob with audio-reactive waves',
        category: 'Fluid',
        mode: 999,
        tags: ['organic', 'blob', 'smooth', 'flowing'],
        parameters: {
            blobRadius: { min: 100, max: 400, default: 200, label: 'Blob Radius' },
            wavePoints: { min: 32, max: 128, default: 64, label: 'Wave Points' },
            waveAmplitude: { min: 10, max: 100, default: 40, label: 'Wave Amplitude' },
            smoothness: { min: 0.3, max: 0.95, default: 0.7, label: 'Smoothness' },
            showBars: { min: 0, max: 1, default: 0, label: 'Show Radial Bars' }
        }
    },
    neon_contour: {
        id: 'neon_contour',
        name: 'Neon Contour',
        description: 'Multi-layered rainbow outline with chromatic offset effect',
        category: 'Fluid',
        mode: 998,
        tags: ['neon', 'outline', 'rainbow', 'chromatic', 'layers'],
        parameters: {
            contourSize: { min: 100, max: 500, default: 250, label: 'Contour Size' },
            numLayers: { min: 2, max: 8, default: 4, label: 'Number of Layers' },
            layerOffset: { min: 5, max: 30, default: 12, label: 'Layer Offset' },
            waveIntensity: { min: 10, max: 80, default: 35, label: 'Wave Intensity' },
            complexity: { min: 24, max: 96, default: 48, label: 'Shape Complexity' }
        }
    },
    circular_spectrum_bars: {
        id: 'circular_spectrum_bars',
        name: 'Circular Spectrum Bars',
        description: 'Radial spectrum bars with blue-to-purple gradient emanating from a circular frame',
        category: 'Geometric',
        mode: 997,
        tags: ['circular', 'spectrum', 'bars', 'gradient', 'radial', 'equalizer'],
        parameters: {
            circleSize: { min: 80, max: 300, default: 150, label: 'Circle Size' },
            barCount: { min: 20, max: 80, default: 48, label: 'Bar Count' },
            barWidth: { min: 3, max: 15, default: 8, label: 'Bar Width' },
            barHeight: { min: 50, max: 250, default: 120, label: 'Max Bar Height' },
            spreadAngle: { min: 90, max: 270, default: 180, label: 'Spread Angle' }
        }
    },
    vinyl_record: {
        id: 'vinyl_record',
        name: 'Vinyl Record',
        description: 'Spinning vinyl disc with two horizontal audio spectrum lines',
        category: 'Retro',
        mode: 996,
        tags: ['vinyl', 'record', 'retro', 'disc', 'spectrum', 'sparkles'],
        parameters: {
            discSize: { min: 100, max: 350, default: 200, label: 'Disc Size' },
            grooveCount: { min: 3, max: 12, default: 6, label: 'Groove Count' },
            rotationSpeed: { min: 0.1, max: 3, default: 0.8, label: 'Rotation Speed' },
            lineWidth: { min: 400, max: 1200, default: 800, label: 'Line Width' },
            sparkleCount: { min: 0, max: 20, default: 8, label: 'Sparkle Count' }
        }
    },
    pulse_ring: {
        id: 'pulse_ring',
        name: 'Pulse Ring',
        description: 'Segmented circular ring with audio-reactive dashed border',
        category: 'Geometric',
        mode: 995,
        tags: ['circle', 'ring', 'pulse', 'segments', 'modern', 'loader'],
        parameters: {
            ringSize: { min: 100, max: 400, default: 200, label: 'Ring Size' },
            ringThickness: { min: 5, max: 30, default: 12, label: 'Ring Thickness' },
            segmentCount: { min: 8, max: 48, default: 24, label: 'Segment Count' },
            gapSize: { min: 2, max: 20, default: 8, label: 'Gap Size' },
            sparkleCount: { min: 0, max: 30, default: 12, label: 'Sparkle Count' }
        }
    },
    sunburst_arc: {
        id: 'sunburst_arc',
        name: 'Sunburst Arc',
        description: 'Semi-circular arc with radiating bars forming a sunburst pattern',
        category: 'Geometric',
        mode: 994,
        tags: ['arc', 'sunburst', 'radial', 'bars', 'elegant', 'fan'],
        parameters: {
            arcRadius: { min: 100, max: 350, default: 180, label: 'Arc Radius' },
            barCount: { min: 20, max: 60, default: 40, label: 'Bar Count' },
            barWidth: { min: 2, max: 12, default: 6, label: 'Bar Width' },
            maxBarLength: { min: 50, max: 200, default: 100, label: 'Max Bar Length' },
            arcSpread: { min: 120, max: 200, default: 160, label: 'Arc Spread (degrees)' }
        }
    },
    gradient_waveform_circle: {
        id: 'gradient_waveform_circle',
        name: 'Gradient Waveform Circle',
        description: 'Circular ring with audio-reactive jagged edge and rainbow gradient',
        category: 'Fluid',
        mode: 993,
        tags: ['circle', 'waveform', 'gradient', 'rainbow', 'audio', 'oscillating'],
        parameters: {
            circleRadius: { min: 100, max: 350, default: 200, label: 'Circle Radius' },
            waveAmplitude: { min: 10, max: 60, default: 30, label: 'Wave Amplitude' },
            lineThickness: { min: 3, max: 15, default: 8, label: 'Line Thickness' },
            resolution: { min: 100, max: 300, default: 180, label: 'Circle Resolution' },
            sparkleCount: { min: 0, max: 40, default: 20, label: 'Sparkle Count' }
        }
    },
    plasma_vortex: {
        id: 'plasma_vortex',
        name: 'Plasma Vortex',
        description: 'Swirling plasma-like tendrils with spiraling rotation and energy flow',
        category: 'Fluid',
        mode: 991,
        tags: ['plasma', 'vortex', 'spiral', 'energy', 'fluid', 'swirl'],
        parameters: {
            vortexRadius: { min: 80, max: 350, default: 180, label: 'Vortex Radius' },
            tendrilCount: { min: 3, max: 12, default: 6, label: 'Tendril Count' },
            spiralTightness: { min: 0.5, max: 3, default: 1.5, label: 'Spiral Tightness' },
            flowSpeed: { min: 0.1, max: 2, default: 0.8, label: 'Flow Speed' },
            energyIntensity: { min: 20, max: 100, default: 50, label: 'Energy Intensity' }
        }
    },
    bubble_stream: {
        id: 'bubble_stream',
        name: 'Bubble Stream',
        description: 'Rising bubbles with audio-reactive sizes and fluid physics simulation',
        category: 'Fluid',
        mode: 990,
        tags: ['bubbles', 'rising', 'fluid', 'physics', 'organic', 'float'],
        parameters: {
            bubbleCount: { min: 5, max: 30, default: 15, label: 'Bubble Count' },
            minBubbleSize: { min: 10, max: 50, default: 20, label: 'Min Bubble Size' },
            maxBubbleSize: { min: 50, max: 150, default: 80, label: 'Max Bubble Size' },
            riseSpeed: { min: 0.5, max: 3, default: 1.5, label: 'Rise Speed' },
            wobbleIntensity: { min: 0.1, max: 2, default: 0.8, label: 'Wobble Intensity' }
        }
    },
    minimal_audio_ring: {
        id: 'minimal_audio_ring',
        name: 'Minimal Audio Ring',
        description: 'Clean white circular ring with subtle audio-reactive edge',
        category: 'Minimal',
        mode: 992,
        tags: ['circle', 'minimal', 'simple', 'clean', 'white', 'ring'],
        parameters: {
            circleRadius: { min: 100, max: 400, default: 220, label: 'Circle Radius' },
            waveAmplitude: { min: 5, max: 40, default: 15, label: 'Wave Amplitude' },
            lineThickness: { min: 2, max: 12, default: 5, label: 'Line Thickness' },
            resolution: { min: 120, max: 300, default: 200, label: 'Circle Resolution' },
            glowIntensity: { min: 0, max: 20, default: 8, label: 'Glow Intensity' }
        }
    },
    triangle_spectrum: {
        id: 'triangle_spectrum',
        name: 'Triangle Spectrum',
        description: 'Glowing triangle frame with vertical waveform bars',
        category: 'Geometric',
        mode: 991,
        tags: ['triangle', 'spectrum', 'equalizer', 'glow', 'neon', 'bars'],
        parameters: {
            triangleSize: { min: 150, max: 400, default: 280, label: 'Triangle Size' },
            barCount: { min: 20, max: 80, default: 50, label: 'Bar Count' },
            barWidth: { min: 2, max: 10, default: 4, label: 'Bar Width' },
            maxBarHeight: { min: 50, max: 200, default: 100, label: 'Max Bar Height' },
            glowIntensity: { min: 5, max: 30, default: 15, label: 'Glow Intensity' }
        }
    },
    wavy_cloud_ring: {
        id: 'wavy_cloud_ring',
        name: 'Wavy Cloud Ring',
        description: 'Soft circular ring with organic wavy edges and pink gradient',
        category: 'Fluid',
        mode: 990,
        tags: ['circle', 'wavy', 'cloud', 'organic', 'soft', 'melting', 'pink'],
        parameters: {
            circleRadius: { min: 100, max: 350, default: 200, label: 'Circle Radius' },
            waveFrequency: { min: 4, max: 20, default: 10, label: 'Wave Frequency' },
            waveAmplitude: { min: 5, max: 40, default: 18, label: 'Wave Amplitude' },
            lineThickness: { min: 8, max: 25, default: 15, label: 'Line Thickness' },
            animationSpeed: { min: 0.1, max: 2, default: 0.5, label: 'Animation Speed' }
        }
    },

    // Nature & Ethereal
    aurora_waves: {
        id: 'aurora_waves',
        name: 'Aurora Waves',
        description: 'Northern lights flowing ribbons',
        category: 'Nature',
        mode: 109,
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
        mode: 110,
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
    particle_accelerator: {
        id: 'particle_accelerator',
        name: 'Particle Accelerator',
        description: 'Particles racing around a circular accelerator ring with collision effects',
        category: 'Scientific',
        mode: 989,
        tags: ['physics', 'particles', 'collision', 'accelerator', 'energy'],
        parameters: {
            ringRadius: { min: 100, max: 350, default: 200, label: 'Ring Radius' },
            particleCount: { min: 10, max: 50, default: 24, label: 'Particle Count' },
            particleSpeed: { min: 0.5, max: 3, default: 1.5, label: 'Particle Speed' },
            collisionEnergy: { min: 20, max: 100, default: 50, label: 'Collision Energy' },
            beamIntensity: { min: 0.3, max: 2, default: 1, label: 'Beam Intensity' }
        }
    },
    neural_network: {
        id: 'neural_network',
        name: 'Neural Network',
        description: 'Interconnected neurons firing with synaptic pulses based on audio',
        category: 'Scientific',
        mode: 988,
        tags: ['neuroscience', 'brain', 'neurons', 'network', 'biology'],
        parameters: {
            neuronCount: { min: 8, max: 30, default: 16, label: 'Neuron Count' },
            connectionDensity: { min: 0.2, max: 1, default: 0.6, label: 'Connection Density' },
            fireRate: { min: 0.5, max: 3, default: 1.5, label: 'Fire Rate' },
            pulseSpeed: { min: 0.5, max: 2.5, default: 1.2, label: 'Pulse Speed' },
            neuronSize: { min: 8, max: 25, default: 15, label: 'Neuron Size' }
        }
    },
    quantum_entanglement: {
        id: 'quantum_entanglement',
        name: 'Quantum Entanglement',
        description: 'Pairs of entangled particles connected by glowing quantum threads',
        category: 'Scientific',
        mode: 1014,
        tags: ['quantum', 'physics', 'particles', 'entanglement', 'energy'],
        parameters: {
            pairCount: { min: 5, max: 30, default: 12, label: 'Particle Pairs' },
            separation: { min: 0.2, max: 0.8, default: 0.5, label: 'Particle Separation' },
            oscillation: { min: 0.5, max: 3, default: 1.5, label: 'Oscillation Speed' },
            connectionGlow: { min: 0, max: 40, default: 20, label: 'Connection Glow' },
            particleSize: { min: 3, max: 15, default: 8, label: 'Particle Size' },
            waveEffect: { min: 0, max: 2, default: 1, label: 'Wave Effect' }
        }
    },
    crystal_lattice: {
        id: 'crystal_lattice',
        name: 'Crystal Lattice',
        description: 'Crystalline atomic structure with pulsing nodes and energy bonds',
        category: 'Scientific',
        mode: 1015,
        tags: ['crystal', 'chemistry', 'structure', 'atoms', 'molecular'],
        parameters: {
            gridSize: { min: 3, max: 10, default: 6, label: 'Grid Size' },
            latticeSpacing: { min: 0.5, max: 1.5, default: 1, label: 'Lattice Spacing' },
            pulseIntensity: { min: 0.3, max: 2, default: 1, label: 'Pulse Intensity' },
            bondThickness: { min: 1, max: 5, default: 2, label: 'Bond Thickness' },
            atomSize: { min: 3, max: 12, default: 6, label: 'Atom Size' },
            rotation: { min: 0, max: 2, default: 0.5, label: 'Rotation Speed' }
        }
    },
    bioluminescence_wave: {
        id: 'bioluminescence_wave',
        name: 'Bioluminescence Wave',
        description: 'Bioluminescent organisms creating rhythmic waves of light',
        category: 'Scientific',
        mode: 1019,
        tags: ['biology', 'ocean', 'bioluminescence', 'wave', 'organic'],
        parameters: {
            waveCount: { min: 3, max: 12, default: 6, label: 'Wave Count' },
            organismDensity: { min: 0.3, max: 1.5, default: 0.8, label: 'Organism Density' },
            glowIntensity: { min: 0.4, max: 2.5, default: 1.2, label: 'Glow Intensity' },
            waveSpeed: { min: 0.3, max: 2, default: 1, label: 'Wave Speed' },
            particleSize: { min: 1, max: 6, default: 2.5, label: 'Particle Size' },
            trailLength: { min: 0.2, max: 1.5, default: 0.7, label: 'Trail Length' }
        }
    },
    electromagnetic_spectrum: {
        id: 'electromagnetic_spectrum',
        name: 'Electromagnetic Spectrum',
        description: 'Wavelengths of light visualized as flowing energy bands',
        category: 'Scientific',
        mode: 1020,
        tags: ['physics', 'light', 'spectrum', 'electromagnetic', 'wavelength'],
        parameters: {
            bandCount: { min: 5, max: 15, default: 9, label: 'Band Count' },
            waveAmplitude: { min: 0.3, max: 2, default: 1, label: 'Wave Amplitude' },
            frequency: { min: 0.5, max: 3, default: 1.5, label: 'Frequency' },
            bandWidth: { min: 0.3, max: 1.2, default: 0.7, label: 'Band Width' },
            opacity: { min: 0.3, max: 1, default: 0.75, label: 'Opacity' },
            flowSpeed: { min: 0.2, max: 2.5, default: 1.2, label: 'Flow Speed' }
        }
    },
    solar_corona: {
        id: 'solar_corona',
        name: 'Solar Corona',
        description: 'Sun\'s corona with dynamic plasma loops and magnetic field lines',
        category: 'Scientific',
        mode: 1021,
        tags: ['astronomy', 'solar', 'plasma', 'corona', 'space'],
        parameters: {
            loopCount: { min: 4, max: 20, default: 10, label: 'Loop Count' },
            coreRadius: { min: 50, max: 200, default: 120, label: 'Core Radius' },
            loopHeight: { min: 0.5, max: 2.5, default: 1.5, label: 'Loop Height' },
            plasmaFlow: { min: 0.3, max: 2, default: 1.2, label: 'Plasma Flow' },
            energyIntensity: { min: 0.4, max: 2, default: 1, label: 'Energy Intensity' },
            turbulence: { min: 0, max: 1.5, default: 0.6, label: 'Turbulence' }
        }
    },
    cytoplasm_flow: {
        id: 'cytoplasm_flow',
        name: 'Cytoplasm Flow',
        description: 'Cellular organelles flowing through cytoplasm in rhythmic patterns',
        category: 'Scientific',
        mode: 1022,
        tags: ['biology', 'cellular', 'organelles', 'cytoplasm', 'microscopic'],
        parameters: {
            organelleCount: { min: 8, max: 35, default: 18, label: 'Organelle Count' },
            flowVelocity: { min: 0.3, max: 2, default: 1, label: 'Flow Velocity' },
            organelleSize: { min: 3, max: 15, default: 8, label: 'Organelle Size' },
            membraneThickness: { min: 1, max: 4, default: 2, label: 'Membrane Thickness' },
            streamCount: { min: 2, max: 8, default: 4, label: 'Stream Count' },
            cellRadius: { min: 150, max: 350, default: 240, label: 'Cell Radius' }
        }
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
        tags: ['electric', 'energy', 'intense'],
        parameters: {
            threshold: { min: 0.1, max: 0.9, default: 0.5, label: 'Strike Threshold' },
            segments: { min: 5, max: 30, default: 10, label: 'Base Segments' },
            segmentRange: { min: 5, max: 20, default: 10, label: 'Segment Range' },
            zigzagAmount: { min: 10, max: 80, default: 40, label: 'Zigzag Intensity' },
            branchProbability: { min: 0.3, max: 0.9, default: 0.7, label: 'Branch Probability' },
            lineWidth: { min: 1, max: 6, default: 2, label: 'Base Line Width' },
            lineWidthRange: { min: 2, max: 8, default: 4, label: 'Line Width Range' }
        }
    },
    plasma_storm: {
        id: 'plasma_storm',
        name: 'Plasma Storm',
        description: 'Swirling energy vortex',
        category: 'Energy',
        mode: 42,
        tags: ['chaotic', 'energy', 'vortex'],
        parameters: {
            numVortices: { min: 1, max: 6, default: 3, label: 'Number of Vortices' },
            rotationSpeed: { min: 0.01, max: 0.1, default: 0.03, label: 'Rotation Speed' },
            vortexDistance: { min: 0.2, max: 0.8, default: 0.5, label: 'Vortex Distance' },
            particleDistance: { min: 50, max: 200, default: 100, label: 'Particle Distance' },
            particleSize: { min: 1, max: 5, default: 2, label: 'Base Particle Size' },
            particleSizeRange: { min: 2, max: 10, default: 6, label: 'Particle Size Range' }
        }
    },
    laser_show: {
        id: 'laser_show',
        name: 'Laser Show',
        description: 'Concert-style laser beams',
        category: 'Energy',
        mode: 43,
        tags: ['laser', 'concert', 'edm'],
        parameters: {
            maxLasers: { min: 5, max: 40, default: 20, label: 'Max Lasers' },
            threshold: { min: 0.1, max: 0.7, default: 0.3, label: 'Activation Threshold' },
            rotationSpeed: { min: 0.01, max: 0.15, default: 0.05, label: 'Rotation Speed' },
            laserLength: { min: 1, max: 2, default: 1.5, label: 'Laser Length' },
            lineWidth: { min: 1, max: 6, default: 3, label: 'Base Line Width' },
            lineWidthRange: { min: 2, max: 10, default: 5, label: 'Line Width Range' },
            endGlowSize: { min: 3, max: 15, default: 5, label: 'End Glow Base Size' },
            endGlowRange: { min: 5, max: 20, default: 10, label: 'End Glow Range' }
        }
    },
    energy_pulses: {
        id: 'energy_pulses',
        name: 'Energy Pulses',
        description: 'Radiating shockwaves from center',
        category: 'Energy',
        mode: 44,
        tags: ['pulse', 'radial', 'waves'],
        parameters: {
            numPulses: { min: 3, max: 12, default: 6, label: 'Number of Pulses' },
            pulseSpeed: { min: 0.05, max: 0.3, default: 0.1, label: 'Pulse Speed' },
            pulseSpread: { min: 50, max: 200, default: 100, label: 'Pulse Spread' },
            lineWidth: { min: 1, max: 10, default: 3, label: 'Base Line Width' },
            lineWidthRange: { min: 2, max: 15, default: 8, label: 'Line Width Range' }
        }
    },
    rainbow_prism: {
        id: 'rainbow_prism',
        name: 'Rainbow Prism',
        description: 'Light refraction spectrum',
        category: 'Energy',
        mode: 45,
        tags: ['rainbow', 'spectrum', 'colorful']
    },
    voltage_surge: {
        id: 'voltage_surge',
        name: 'Voltage Surge',
        description: 'Vertical electrical bolts surging upward with crackling energy',
        category: 'Energy',
        mode: 1012,
        tags: ['electric', 'voltage', 'energy', 'bolts', 'intense'],
        parameters: {
            boltCount: { min: 5, max: 40, default: 15, label: 'Number of Bolts' },
            boltHeight: { min: 0.3, max: 1.5, default: 0.8, label: 'Bolt Height' },
            surgeSpeed: { min: 0.5, max: 3, default: 1.5, label: 'Surge Speed' },
            crackleIntensity: { min: 0, max: 2, default: 1, label: 'Crackle Intensity' },
            thickness: { min: 1, max: 8, default: 3, label: 'Bolt Thickness' },
            glow: { min: 0, max: 50, default: 25, label: 'Glow Amount' }
        }
    },
    particle_accelerator: {
        id: 'particle_accelerator',
        name: 'Particle Accelerator',
        description: 'High-speed particles racing in circular paths with energy trails',
        category: 'Energy',
        mode: 1013,
        tags: ['particles', 'circular', 'speed', 'energy', 'physics'],
        parameters: {
            particleCount: { min: 20, max: 200, default: 80, label: 'Particle Count' },
            orbitRadius: { min: 0.2, max: 0.8, default: 0.4, label: 'Orbit Radius' },
            speed: { min: 0.5, max: 5, default: 2, label: 'Acceleration Speed' },
            trailLength: { min: 0, max: 1, default: 0.5, label: 'Trail Length' },
            particleSize: { min: 1, max: 10, default: 4, label: 'Particle Size' },
            rings: { min: 1, max: 5, default: 2, label: 'Number of Rings' }
        }
    },
    supernova_burst: {
        id: 'supernova_burst',
        name: 'Supernova Burst',
        description: 'Explosive stellar energy with radiating particles and shockwaves',
        category: 'Energy',
        mode: 987,
        tags: ['explosion', 'star', 'particles', 'energy', 'cosmic', 'burst'],
        parameters: {
            burstIntensity: { min: 0.5, max: 3, default: 1.5, label: 'Burst Intensity' },
            particleDensity: { min: 30, max: 150, default: 80, label: 'Particle Density' },
            expansionSpeed: { min: 1, max: 5, default: 2.5, label: 'Expansion Speed' },
            shockwaveCount: { min: 2, max: 8, default: 4, label: 'Shockwave Rings' },
            coreSize: { min: 20, max: 80, default: 40, label: 'Core Size' },
            energyDecay: { min: 0.85, max: 0.99, default: 0.95, label: 'Energy Decay' }
        }
    },
    electric_web: {
        id: 'electric_web',
        name: 'Electric Web',
        description: 'Tesla coil network with arcing electricity connecting reactive nodes',
        category: 'Energy',
        mode: 986,
        tags: ['electric', 'tesla', 'arcs', 'network', 'energy', 'voltage'],
        parameters: {
            nodeCount: { min: 6, max: 20, default: 12, label: 'Node Count' },
            arcThreshold: { min: 0.2, max: 0.8, default: 0.4, label: 'Arc Threshold' },
            arcIntensity: { min: 0.5, max: 2.5, default: 1.5, label: 'Arc Intensity' },
            pulseSpeed: { min: 0.5, max: 3, default: 1.5, label: 'Pulse Speed' },
            nodeSize: { min: 5, max: 25, default: 12, label: 'Node Size' },
            webDensity: { min: 0.3, max: 1, default: 0.6, label: 'Connection Density' }
        }
    },
    kinetic_shockwave: {
        id: 'kinetic_shockwave',
        name: 'Kinetic Shockwave',
        description: 'Powerful circular shockwaves with space distortion and energy ripples',
        category: 'Energy',
        mode: 985,
        tags: ['shockwave', 'impact', 'kinetic', 'force', 'energy', 'ripple'],
        parameters: {
            waveCount: { min: 3, max: 12, default: 6, label: 'Wave Count' },
            waveSpeed: { min: 1, max: 4, default: 2, label: 'Wave Speed' },
            distortionAmount: { min: 0, max: 50, default: 20, label: 'Distortion Amount' },
            impactForce: { min: 0.5, max: 2.5, default: 1.5, label: 'Impact Force' },
            waveThickness: { min: 2, max: 15, default: 6, label: 'Wave Thickness' },
            particleTrail: { min: 0, max: 40, default: 20, label: 'Particle Trail' }
        }
    },

    // Extended Modes (51-60)
    fractal_tree: {
        id: 'fractal_tree',
        name: 'Fractal Tree',
        description: 'Generative tree with bass branches and treble blooms',
        category: 'Nature',
        mode: 51,
        tags: ['organic', 'tree', 'generative']
    },
    cityscape_extrusion: {
        id: 'cityscape_extrusion',
        name: 'Cityscape Extrusion',
        description: '3D city blocks that extrude with frequency',
        category: 'Tech',
        mode: 52,
        tags: ['3d', 'urban', 'architecture']
    },
    gravity_well: {
        id: 'gravity_well',
        name: 'Gravity Well',
        description: 'Particles pulled by pulsing bass center',
        category: 'Scientific',
        mode: 53,
        tags: ['physics', 'particles', 'gravity']
    },
    metaball_fluid: {
        id: 'metaball_fluid',
        name: 'Metaball Fluid',
        description: 'Lava lamp metaballs with frequency pulsing',
        category: 'Fluid',
        mode: 54,
        tags: ['organic', 'fluid', 'smooth']
    },
    aurora_borealis: {
        id: 'aurora_borealis',
        name: 'Aurora Borealis',
        description: 'Northern lights curtains with shimmer',
        category: 'Nature',
        mode: 55,
        tags: ['ethereal', 'waves', 'aurora']
    },
    stained_glass: {
        id: 'stained_glass',
        name: 'Stained Glass',
        description: 'Glowing window panes with frequency',
        category: 'Classic',
        mode: 56,
        tags: ['artistic', 'colorful', 'mosaic']
    },
    neon_nerve_network: {
        id: 'neural_network',
        name: 'Neural Network',
        description: 'Pulsing nodes with synapse firings',
        category: 'Tech',
        mode: 57,
        tags: ['network', 'ai', 'connections']
    },
    glitch_artifact: {
        id: 'glitch_artifact',
        name: 'Glitch Artifact',
        description: 'Clean bars corrupted by glitch effects',
        category: 'Tech',
        mode: 58,
        tags: ['glitch', 'digital', 'corruption']
    },
    warp_tunnel: {
        id: 'warp_tunnel',
        name: 'Warp Tunnel',
        description: 'Hyperspace tunnel of pulsing rings',
        category: 'Tech',
        mode: 59,
        tags: ['hyperspace', 'tunnel', '3d']
    },
    conway_life: {
        id: 'conway_life',
        name: "Conway Game of Life",
        description: 'Cellular automaton modulated by audio',
        category: 'Scientific',
        mode: 60,
        tags: ['generative', 'cellular', 'algorithm']
    },
    ascii_art: {
        id: 'ascii_art',
        name: 'ASCII Art Bars',
        description: 'Spectrum displayed as ASCII characters',
        category: 'Retro',
        mode: 61,
        tags: ['text', 'ascii', 'retro']
    },
    rippling_water: {
        id: 'rippling_water',
        name: 'Rippling Water',
        description: 'Expanding ripples from frequency sources',
        category: 'Nature',
        mode: 62,
        tags: ['water', 'ripples', 'fluid']
    },
    terrain_flyover: {
        id: 'terrain_flyover',
        name: 'Terrain Flyover',
        description: '3D wireframe terrain from audio waveform',
        category: 'Tech',
        mode: 63,
        tags: ['3d', 'wireframe', 'terrain']
    },
    string_art: {
        id: 'string_art',
        name: 'String Art',
        description: 'Points on circle with connecting lines modulated by audio',
        category: 'Geometric',
        mode: 64,
        tags: ['geometric', 'lines', 'circular']
    },
    fire_embers: {
        id: 'fire_embers',
        name: 'Fire Embers',
        description: 'Central fire with sparks rising on treble hits',
        category: 'Nature',
        mode: 65,
        tags: ['fire', 'particles', 'heat']
    },
    radial_kaleidoscope: {
        id: 'radial_kaleidoscope',
        name: 'Radial Kaleidoscope',
        description: 'Mirrored segments with rotating particles',
        category: 'Geometric',
        mode: 66,
        tags: ['kaleidoscope', 'mirror', 'radial']
    },
    orbital_system: {
        id: 'orbital_system',
        name: 'Orbital System',
        description: 'Central sun with orbiting planets and moons',
        category: 'Scientific',
        mode: 68,
        tags: ['space', 'planets', 'orbit']
    },
    spectrum_cube: {
        id: 'spectrum_cube',
        name: 'Spectrum Cube',
        description: 'Rotating 3D cube with audio visualizers',
        category: 'Tech',
        mode: 69,
        tags: ['3d', 'cube', 'rotation']
    },
    typographic_flow: {
        id: 'typographic_flow',
        name: 'Typographic Flow',
        description: 'Floating words with size based on bass',
        category: 'Tech',
        mode: 70,
        tags: ['text', 'typography', 'words']
    },
    sonar_ping: {
        id: 'sonar_ping',
        name: 'Sonar Ping',
        description: 'Rotating radar sweep with frequency blips',
        category: 'Tech',
        mode: 71,
        tags: ['radar', 'sonar', 'sweep']
    },
    vu_meters: {
        id: 'vu_meters',
        name: 'VU Meters',
        description: 'Analog stereo VU meters with needle physics',
        category: 'Retro',
        mode: 72,
        tags: ['analog', 'meters', 'stereo']
    },
    lightning_cloud: {
        id: 'lightning_cloud',
        name: 'Lightning Cloud',
        description: 'Storm cloud with lightning bolts on treble hits',
        category: 'Nature',
        mode: 73,
        tags: ['storm', 'lightning', 'weather'],
        parameters: {
            cloudDensity: { min: 10, max: 50, default: 25, label: 'Cloud Density' },
            cloudSize: { min: 20, max: 100, default: 50, label: 'Cloud Particle Size' },
            lightningFrequency: { min: 0.3, max: 0.9, default: 0.5, label: 'Lightning Threshold' },
            lightningSegments: { min: 3, max: 15, default: 8, label: 'Lightning Segments' },
            lightningWidth: { min: 2, max: 15, default: 6, label: 'Lightning Width' },
            trailOpacity: { min: 0.05, max: 0.3, default: 0.12, label: 'Trail Fade' }
        }
    },
    bouncing_balls: {
        id: 'bouncing_balls',
        name: 'Bouncing Balls',
        description: 'Physics-based bouncing balls with gravity',
        category: 'Particles',
        mode: 74,
        tags: ['physics', 'bounce', 'balls']
    },
    liquid_ink: {
        id: 'liquid_ink',
        name: 'Liquid Ink',
        description: 'Ink blooms and splatters responding to audio',
        category: 'Art',
        mode: 75,
        tags: ['ink', 'fluid', 'artistic']
    },
    stereo_landscape: {
        id: 'stereo_landscape',
        name: 'Stereo Landscape',
        description: '3D perspective with left/right stereo mountains',
        category: 'Classic',
        mode: 76,
        tags: ['stereo', '3d', 'mountains']
    },
    ai_latent_walk: {
        id: 'ai_latent_walk',
        name: 'AI Latent Walk',
        description: 'Abstract morphing shapes simulating latent space',
        category: 'Tech',
        mode: 77,
        tags: ['ai', 'abstract', 'morphing']
    },
    pixel_storm: {
        id: 'pixel_storm',
        name: 'Pixel Storm',
        description: 'Blizzard of 8-bit pixels with stereo wind direction',
        category: 'Retro',
        mode: 78,
        tags: ['8bit', 'pixels', 'storm']
    },
    growing_vine: {
        id: 'growing_vine',
        name: 'Growing Vine',
        description: 'Organic vine growth with leaves sprouting on beats',
        category: 'Nature',
        mode: 79,
        tags: ['vine', 'organic', 'growth']
    },
    haunted_faces: {
        id: 'haunted_faces',
        name: 'Haunted Faces',
        description: 'Ghostly faces with glowing eyes on bass hits',
        category: 'Nature',
        mode: 80,
        tags: ['ghost', 'spooky', 'faces']
    },
    connecting_constellations: {
        id: 'connecting_constellations',
        name: 'Connecting Constellations',
        description: 'Stars that connect when their frequencies pass threshold',
        category: 'Nature',
        mode: 81,
        tags: ['stars', 'constellation', 'connections']
    },
    matrix_rain: {
        id: 'matrix_rain',
        name: 'Matrix Rain',
        description: 'Falling Matrix-style characters with audio-reactive speed',
        category: 'Tech',
        mode: 82,
        tags: ['matrix', 'digital', 'rain']
    },
    voxel_world: {
        id: 'voxel_world',
        name: 'Voxel World',
        description: '3D voxel grid with audio shockwave',
        category: 'Tech',
        mode: 83,
        tags: ['3d', 'voxel', 'grid']
    },
    dna_helix_rungs: {
        id: 'dna_helix_rungs',
        name: 'DNA Helix Rungs',
        description: 'DNA double helix with rungs lighting up per frequency',
        category: 'Scientific',
        mode: 84,
        tags: ['dna', 'helix', 'biology']
    },
    audio_reactive_shader: {
        id: 'audio_reactive_shader',
        name: 'Audio Reactive Shader',
        description: 'Procedural shader-like effect with audio modulation',
        category: 'Tech',
        mode: 85,
        tags: ['shader', 'procedural', 'abstract']
    },
    spirograph: {
        id: 'spirograph',
        name: 'Spirograph',
        description: 'Spirograph pattern with radii controlled by frequencies',
        category: 'Geometric',
        mode: 86,
        tags: ['spirograph', 'pattern', 'geometric']
    },
    equalizer_tower: {
        id: 'equalizer_tower',
        name: 'Equalizer Tower',
        description: '3D tower of stacked glowing rings',
        category: 'Tech',
        mode: 87,
        tags: ['3d', 'tower', 'rings']
    },
    audio_driven_doodles: {
        id: 'audio_driven_doodles',
        name: 'Audio Driven Doodles',
        description: 'Generative doodle bot with bass turns and treble shakiness',
        category: 'Geometric',
        mode: 88,
        tags: ['doodle', 'generative', 'path']
    },
    firework_show: {
        id: 'firework_show',
        name: 'Firework Show',
        description: 'Bass launches rockets that explode with colored particles',
        category: 'Particles',
        mode: 89,
        tags: ['fireworks', 'particles', 'explosion'],
        parameters: {
            bassThreshold: { min: 0.1, max: 0.8, default: 0.3, label: 'Bass Threshold' },
            particleCount: { min: 50, max: 300, default: 150, label: 'Particle Count' },
            rocketSpeed: { min: 5, max: 20, default: 12, label: 'Rocket Speed' },
            particleSpeed: { min: 2, max: 12, default: 6, label: 'Explosion Speed' },
            particleSize: { min: 1, max: 10, default: 4, label: 'Particle Size' },
            trailLength: { min: 0.05, max: 0.3, default: 0.15, label: 'Trail Length' }
        }
    },
    microscopic_view: {
        id: 'microscopic_view',
        name: 'Microscopic View',
        description: 'Cells jiggle and divide based on frequency',
        category: 'Scientific',
        mode: 90,
        tags: ['cells', 'biology', 'division']
    },
    burning_paper: {
        id: 'burning_paper',
        name: 'Burning Paper',
        description: 'Spectrum bars as flames, embers on high freq, paper curls on bass',
        category: 'Energy',
        mode: 91,
        tags: ['fire', 'flames', 'heat']
    },
    swarm_intelligence: {
        id: 'swarm_intelligence',
        name: 'Swarm Intelligence',
        description: 'Boid flocking - cohesion/separation modulated by audio',
        category: 'Nature',
        mode: 92,
        tags: ['boids', 'flocking', 'swarm']
    },
    pendulum_wave: {
        id: 'pendulum_wave',
        name: 'Pendulum Wave',
        description: 'Multiple pendulums with slightly different periods - force from frequency',
        category: 'Geometric',
        mode: 93,
        tags: ['pendulum', 'wave', 'physics']
    },
    retro_scanlines: {
        id: 'retro_scanlines',
        name: 'Retro Scanlines',
        description: 'Waveform on old CRT with scanlines and static',
        category: 'Retro',
        mode: 94,
        tags: ['crt', 'scanlines', 'vintage']
    },
    pulsing_polygon: {
        id: 'pulsing_polygon',
        name: 'Pulsing Polygon',
        description: 'Central polygon with vertices pushed by frequency bands',
        category: 'Geometric',
        mode: 95,
        tags: ['polygon', 'pulse', 'geometric']
    },
    chromatic_orb: {
        id: 'chromatic_orb',
        name: 'Chromatic Orb',
        description: '3D sphere with chromatic shader and moving light source',
        category: 'Geometric',
        mode: 96,
        tags: ['3d', 'sphere', 'lighting']
    },
    textured_bars: {
        id: 'textured_bars',
        name: 'Textured Bars',
        description: 'Bars filled with scrolling animated texture',
        category: 'Classic',
        mode: 97,
        tags: ['bars', 'texture', 'pattern']
    },
    voronoi_tessellation: {
        id: 'voronoi_tessellation',
        name: 'Voronoi Tessellation',
        description: 'Voronoi diagram with cells pulsing and seed points moving',
        category: 'Geometric',
        mode: 98,
        tags: ['voronoi', 'tessellation', 'cells']
    },
    shattering_glass: {
        id: 'shattering_glass',
        name: 'Shattering Glass',
        description: 'Glass pane with cracks appearing on beats',
        category: 'Energy',
        mode: 99,
        tags: ['glass', 'cracks', 'impact']
    },
    sunrise_sunset: {
        id: 'sunrise_sunset',
        name: 'Sunrise Sunset',
        description: 'Gradient sky with pulsing sun and glittering stars',
        category: 'Nature',
        mode: 100,
        tags: ['sky', 'sun', 'stars']
    },
    neural_pulse: {
        id: 'neural_pulse',
        name: 'Neural Pulse',
        description: 'Neural network with pulsing nodes and lighting connections',
        category: 'Tech',
        mode: 101,
        tags: ['neural', 'network', 'ai'],
        parameters: {
            nodeCount: { min: 10, max: 100, default: 30, label: 'Node Count' },
            layerCount: { min: 2, max: 5, default: 3, label: 'Network Layers' },
            connectionThreshold: { min: 10, max: 200, default: 50, label: 'Connection Threshold' },
            nodeSize: { min: 2, max: 20, default: 8, label: 'Base Node Size' },
            pulseIntensity: { min: 5, max: 50, default: 20, label: 'Pulse Intensity' },
            trailFade: { min: 0.05, max: 0.3, default: 0.1, label: 'Trail Fade' },
            glowRadius: { min: 1, max: 10, default: 3, label: 'Node Glow' }
        }
    },
    liquid_mercury: {
        id: 'liquid_mercury',
        name: 'Liquid Mercury',
        description: 'Metallic liquid that ripples with physics',
        category: 'Fluid',
        mode: 102,
        tags: ['mercury', 'liquid', 'physics']
    },
    cosmic_strings: {
        id: 'cosmic_strings',
        name: 'Cosmic Strings',
        description: 'Vibrating strings in space like guitar strings',
        category: 'Nature',
        mode: 103,
        tags: ['strings', 'vibration', 'cosmic']
    },
    particle_swarm: {
        id: 'particle_swarm',
        name: 'Particle Swarm',
        description: 'Thousands of particles forming shapes',
        category: 'Particles',
        mode: 104,
        tags: ['particles', 'swarm', 'formation'],
        parameters: {
            particleCount: { min: 100, max: 3000, default: 1000, label: 'Max Particles' },
            spawnRate: { min: 1, max: 30, default: 10, label: 'Spawn Rate' },
            formationRadius: { min: 50, max: 400, default: 150, label: 'Formation Radius' },
            movementSpeed: { min: 0.01, max: 0.2, default: 0.05, label: 'Movement Speed' },
            trailLength: { min: 0, max: 20, default: 5, label: 'Trail Length' },
            particleSize: { min: 1, max: 5, default: 2, label: 'Particle Size' },
            trailOpacity: { min: 0.01, max: 0.3, default: 0.05, label: 'Trail Fade' }
        }
    },
    crystal_lattice: {
        id: 'crystal_lattice',
        name: 'Crystal Lattice',
        description: '3D crystal structure with pulsing nodes',
        category: 'Geometric',
        mode: 105,
        tags: ['3d', 'crystal', 'lattice']
    }
,
    mode_106_aurora_waves: {
        id: 'mode_106_aurora_waves',
        name: 'Aurora Waves',
        description: 'Mode 106: Aurora borealis flowing curtains',
        category: 'Nature',
        mode: 106,
        tags: ["aurora", "waves"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_107_dna_helix: {
        id: 'mode_107_dna_helix',
        name: 'Dna Helix',
        description: 'Mode 107: Rotating DNA double helix with pulsing base pairs',
        category: 'Scientific',
        mode: 107,
        tags: ["helix"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_108_fractal_bloom: {
        id: 'mode_108_fractal_bloom',
        name: 'Fractal Bloom',
        description: 'Mode 108: Fractal flower blooming and contracting',
        category: 'Geometric',
        mode: 108,
        tags: ["fractal", "bloom"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_109_circuit_board: {
        id: 'mode_109_circuit_board',
        name: 'Circuit Board',
        description: 'Mode 109: Electronic circuit with flowing electricity',
        category: 'Scientific',
        mode: 109,
        tags: ["circuit", "board"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_110_quantum_field: {
        id: 'mode_110_quantum_field',
        name: 'Quantum Field',
        description: 'Mode 110: Quantum probability field with wave function collapse',
        category: 'Scientific',
        mode: 110,
        tags: ["quantum", "field"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_111_origami_unfold: {
        id: 'mode_111_origami_unfold',
        name: 'Origami Unfold',
        description: 'Mode 111: Geometric origami folding rhythmically',
        category: 'Geometric',
        mode: 111,
        tags: ["origami", "unfold"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_112_galaxy_spiral: {
        id: 'mode_112_galaxy_spiral',
        name: 'Galaxy Spiral',
        description: 'Mode 112: Spiral galaxy with pulsing stars',
        category: 'Geometric',
        mode: 112,
        tags: ["galaxy", "spiral"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_113_rubber_bands: {
        id: 'mode_113_rubber_bands',
        name: 'Rubber Bands',
        description: 'Mode 113: Vibrating rubber bands with physics',
        category: 'Geometric',
        mode: 113,
        tags: ["rubber", "bands"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_114_ink_diffusion: {
        id: 'mode_114_ink_diffusion',
        name: 'Ink Diffusion',
        description: 'Mode 114: Ink diffusing in water',
        category: 'Fluid',
        mode: 114,
        tags: ["diffusion"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_115_geometric_kaleidoscope: {
        id: 'mode_115_geometric_kaleidoscope',
        name: 'Geometric Kaleidoscope',
        description: 'Mode 115: Rotating kaleidoscope with morphing shapes',
        category: 'Geometric',
        mode: 115,
        tags: ["geometric", "kaleidoscope"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_116_lightning_storm: {
        id: 'mode_116_lightning_storm',
        name: 'Lightning Storm',
        description: 'Mode 116: Lightning bolts with branching',
        category: 'Energy',
        mode: 116,
        tags: ["lightning", "storm"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_117_cellular_growth: {
        id: 'mode_117_cellular_growth',
        name: 'Cellular Growth',
        description: 'Mode 117: Biological cell division and growth',
        category: 'Geometric',
        mode: 117,
        tags: ["cellular", "growth"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_118_sound_ribbons: {
        id: 'mode_118_sound_ribbons',
        name: 'Sound Ribbons',
        description: 'Mode 118: 3D ribbons twisting through space',
        category: 'Geometric',
        mode: 118,
        tags: ["sound", "ribbons"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_119_matrix_rain: {
        id: 'mode_119_matrix_rain',
        name: 'Matrix Rain',
        description: 'Mode 119: Matrix code rain',
        category: 'Scientific',
        mode: 119,
        tags: ["matrix", "rain"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_120_fire_mandala: {
        id: 'mode_120_fire_mandala',
        name: 'Fire Mandala',
        description: 'Mode 120: Circular mandala made of flames',
        category: 'Nature',
        mode: 120,
        tags: ["fire", "mandala"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_121_tessellation_shift: {
        id: 'mode_121_tessellation_shift',
        name: 'Tessellation Shift',
        description: 'Mode 121: Escher-style morphing tessellations',
        category: 'Geometric',
        mode: 121,
        tags: ["tessellation", "shift"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_122_seismic_waves: {
        id: 'mode_122_seismic_waves',
        name: 'Seismic Waves',
        description: 'Mode 122: Seismograph readings with P-waves and S-waves',
        category: 'Geometric',
        mode: 122,
        tags: ["seismic", "waves"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_123_neon_city: {
        id: 'mode_123_neon_city',
        name: 'Neon City',
        description: 'Mode 123: Cyberpunk city with pulsing lights',
        category: 'Tech',
        mode: 123,
        tags: ["neon", "city"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_124_magnetic_field: {
        id: 'mode_124_magnetic_field',
        name: 'Magnetic Field',
        description: 'Mode 124: Magnetic field lines with particle clustering',
        category: 'Scientific',
        mode: 124,
        tags: ["magnetic", "field"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_125_bubble_fusion: {
        id: 'mode_125_bubble_fusion',
        name: 'Bubble Fusion',
        description: 'Mode 125: Bubbles that float, merge, and pop',
        category: 'Particles',
        mode: 125,
        tags: ["bubble", "fusion"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_126_tribal_drums: {
        id: 'mode_126_tribal_drums',
        name: 'Tribal Drums',
        description: 'Mode 126: Tribal patterns pulsing like drum skins',
        category: 'Geometric',
        mode: 126,
        tags: ["tribal", "drums"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_127_glass_shatter: {
        id: 'mode_127_glass_shatter',
        name: 'Glass Shatter',
        description: 'Mode 127: Glass forming and shattering',
        category: 'Geometric',
        mode: 127,
        tags: ["glass", "shatter"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_128_bioluminescence: {
        id: 'mode_128_bioluminescence',
        name: 'Bioluminescence',
        description: 'Mode 128: Deep ocean bioluminescent creatures',
        category: 'Geometric',
        mode: 128,
        tags: ["bioluminescence"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_129_sound_architecture: {
        id: 'mode_129_sound_architecture',
        name: 'Sound Architecture',
        description: 'Mode 129: Impossible architecture constructing/deconstructing',
        category: 'Geometric',
        mode: 129,
        tags: ["sound", "architecture"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_130_plasma_ball: {
        id: 'mode_130_plasma_ball',
        name: 'Plasma Ball',
        description: 'Mode 130: Plasma globe with electrical tendrils',
        category: 'Energy',
        mode: 130,
        tags: ["plasma", "ball"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_131_sand_mandala: {
        id: 'mode_131_sand_mandala',
        name: 'Sand Mandala',
        description: 'Mode 131: Tibetan sand mandala forming grain by grain',
        category: 'Geometric',
        mode: 131,
        tags: ["sand", "mandala"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_132_laser_show: {
        id: 'mode_132_laser_show',
        name: 'Laser Show',
        description: 'Mode 132: Concert laser beams sweeping and bouncing',
        category: 'Geometric',
        mode: 132,
        tags: ["laser", "show"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_133_coral_reef: {
        id: 'mode_133_coral_reef',
        name: 'Coral Reef',
        description: 'Mode 133: Growing coral reef with swaying polyps',
        category: 'Nature',
        mode: 133,
        tags: ["coral", "reef"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_134_wireframe_morph: {
        id: 'mode_134_wireframe_morph',
        name: 'Wireframe Morph',
        description: 'Mode 134: 3D wireframe objects morphing between shapes',
        category: 'Geometric',
        mode: 134,
        tags: ["wireframe", "morph"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_135_sound_garden: {
        id: 'mode_135_sound_garden',
        name: 'Sound Garden',
        description: 'Mode 135: Abstract garden with blooming flowers',
        category: 'Geometric',
        mode: 135,
        tags: ["sound", "garden"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_136_hologram_glitch: {
        id: 'mode_136_hologram_glitch',
        name: 'Hologram Glitch',
        description: 'Mode 136: Glitching holographic interface',
        category: 'Geometric',
        mode: 136,
        tags: ["hologram", "glitch"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_137_pendulum_wave: {
        id: 'mode_137_pendulum_wave',
        name: 'Pendulum Wave',
        description: 'Mode 137: Multiple pendulums creating wave patterns',
        category: 'Geometric',
        mode: 137,
        tags: ["pendulum", "wave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_138_volcano_eruption: {
        id: 'mode_138_volcano_eruption',
        name: 'Volcano Eruption',
        description: 'Mode 138: Volcano erupting with lava and ash',
        category: 'Geometric',
        mode: 138,
        tags: ["volcano", "eruption"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_139_butterfly_effect: {
        id: 'mode_139_butterfly_effect',
        name: 'Butterfly Effect',
        description: 'Mode 139: Chaos theory Lorenz attractor',
        category: 'Geometric',
        mode: 139,
        tags: ["butterfly", "effect"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_140_silk_weaving: {
        id: 'mode_140_silk_weaving',
        name: 'Silk Weaving',
        description: 'Mode 140: Silk threads weaving patterns',
        category: 'Geometric',
        mode: 140,
        tags: ["silk", "weaving"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_141_clock_gears: {
        id: 'mode_141_clock_gears',
        name: 'Clock Gears',
        description: 'Mode 141: Interlocking clockwork gears turning',
        category: 'Geometric',
        mode: 141,
        tags: ["clock", "gears"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_142_smoke_signals: {
        id: 'mode_142_smoke_signals',
        name: 'Smoke Signals',
        description: 'Mode 142: Rising smoke plumes forming patterns',
        category: 'Geometric',
        mode: 142,
        tags: ["smoke", "signals"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_143_stained_glass: {
        id: 'mode_143_stained_glass',
        name: 'Stained Glass',
        description: 'Mode 143: Glowing stained glass window',
        category: 'Scientific',
        mode: 143,
        tags: ["stained", "glass"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_144_string_theory: {
        id: 'mode_144_string_theory',
        name: 'String Theory',
        description: 'Mode 144: Theoretical strings vibrating in multiple dimensions',
        category: 'Geometric',
        mode: 144,
        tags: ["string", "theory"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_145_paper_craft: {
        id: 'mode_145_paper_craft',
        name: 'Paper Craft',
        description: 'Mode 145: Paper cutouts folding into 3D shapes',
        category: 'Geometric',
        mode: 145,
        tags: ["paper", "craft"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_146_northern_lights: {
        id: 'mode_146_northern_lights',
        name: 'Northern Lights',
        description: 'Mode 146: Realistic aurora borealis dancing',
        category: 'Geometric',
        mode: 146,
        tags: ["northern", "lights"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_147_cellular_automata: {
        id: 'mode_147_cellular_automata',
        name: 'Cellular Automata',
        description: 'Mode 147: Conway Game of Life with audio triggers',
        category: 'Geometric',
        mode: 147,
        tags: ["cellular", "automata"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_148_dragon_curve: {
        id: 'mode_148_dragon_curve',
        name: 'Dragon Curve',
        description: 'Mode 148: Fractal dragon curve growing',
        category: 'Geometric',
        mode: 148,
        tags: ["dragon", "curve"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_149_rain_circles: {
        id: 'mode_149_rain_circles',
        name: 'Rain Circles',
        description: 'Mode 149: Concentric circles like raindrops',
        category: 'Scientific',
        mode: 149,
        tags: ["rain", "circles"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_150_fourier_epicycles: {
        id: 'mode_150_fourier_epicycles',
        name: 'Fourier Epicycles',
        description: 'Mode 150: Rotating circles tracing Fourier series',
        category: 'Geometric',
        mode: 150,
        tags: ["fourier", "epicycles"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_151_neon_halo_burst: {
        id: 'mode_151_neon_halo_burst',
        name: 'Neon Halo Burst',
        description: 'Mode 151: Circular ring whose radius pulses with kick; emits radial spikes on snare',
        category: 'Tech',
        mode: 151,
        tags: ["neon", "halo", "burst"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_152_twin_orbiters: {
        id: 'mode_152_twin_orbiters',
        name: 'Twin Orbiters',
        description: 'Mode 152: Two dots orbit a center with elastic distance; trails draw lissajous figure',
        category: 'Geometric',
        mode: 152,
        tags: ["twin", "orbiters"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_153_bar_spiral_galaxy: {
        id: 'mode_153_bar_spiral_galaxy',
        name: 'Bar Spiral Galaxy',
        description: 'Mode 153: Bars arranged in a spiral. Each bar length follows its band',
        category: 'Geometric',
        mode: 153,
        tags: ["spiral", "galaxy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_154_ribbon_wave: {
        id: 'mode_154_ribbon_wave',
        name: 'Ribbon Wave',
        description: 'Mode 154: Wide ribbon undulates like cloth; bass lifts amplitude',
        category: 'Geometric',
        mode: 154,
        tags: ["ribbon", "wave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_155_voxel_city: {
        id: 'mode_155_voxel_city',
        name: 'Voxel City',
        description: 'Mode 155: 3D grid of extruded cubes like skyline; building heights react per frequency',
        category: 'Geometric',
        mode: 155,
        tags: ["voxel", "city"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_156_sunburst_dial: {
        id: 'mode_156_sunburst_dial',
        name: 'Sunburst Dial',
        description: 'Mode 156: 360° radial meter with ticks; ticks bend outward on mids',
        category: 'Geometric',
        mode: 156,
        tags: ["sunburst", "dial"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_157_waterline_oscilloscope: {
        id: 'mode_157_waterline_oscilloscope',
        name: 'Waterline Oscilloscope',
        description: 'Mode 157: Horizontal waveform floats like water surface',
        category: 'Fluid',
        mode: 157,
        tags: ["waterline", "oscilloscope"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_158_laser_tunnel: {
        id: 'mode_158_laser_tunnel',
        name: 'Laser Tunnel',
        description: 'Mode 158: Perspective tunnel of rings; ring scale follows kick',
        category: 'Geometric',
        mode: 158,
        tags: ["laser", "tunnel"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_159_vector_field_sprites: {
        id: 'mode_159_vector_field_sprites',
        name: 'Vector Field Sprites',
        description: 'Mode 159: Thousands of particles follow a noise flow; velocity multiplies on mids',
        category: 'Geometric',
        mode: 159,
        tags: ["vector", "field", "sprites"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_160_orbit_rings_meter: {
        id: 'mode_160_orbit_rings_meter',
        name: 'Orbit Rings Meter',
        description: 'Mode 160: Nested orbits with dots; each ring maps to a band',
        category: 'Geometric',
        mode: 160,
        tags: ["orbit", "rings", "meter"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_161_stitch_bars: {
        id: 'mode_161_stitch_bars',
        name: 'Stitch Bars',
        description: 'Mode 161: Stacked micro-bars like embroidered stitches',
        category: 'Geometric',
        mode: 161,
        tags: ["stitch", "bars"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_162_aurora_curtain: {
        id: 'mode_162_aurora_curtain',
        name: 'Aurora Curtain',
        description: 'Mode 162: Vertical curtains waving; bass widens curtain',
        category: 'Scientific',
        mode: 162,
        tags: ["aurora", "curtain"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_164_polygon_heartbeat: {
        id: 'mode_164_polygon_heartbeat',
        name: 'Polygon Heartbeat',
        description: 'Mode 164: Regular polygon in the center inflates on kicks',
        category: 'Geometric',
        mode: 164,
        tags: ["polygon", "heartbeat"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_165_confetti_impulse: {
        id: 'mode_165_confetti_impulse',
        name: 'Confetti Impulse',
        description: 'Mode 165: On peaks, spawn confetti bursts',
        category: 'Geometric',
        mode: 165,
        tags: ["confetti", "impulse"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_166_wireframe_dome: {
        id: 'mode_166_wireframe_dome',
        name: 'Wireframe Dome',
        description: 'Mode 166: Hemispherical mesh; vertices displace along normals',
        category: 'Geometric',
        mode: 166,
        tags: ["wireframe", "dome"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_167_pulse_dashes: {
        id: 'mode_167_pulse_dashes',
        name: 'Pulse Dashes',
        description: 'Mode 167: Circular dashed stroke; dash length oscillates with mids',
        category: 'Geometric',
        mode: 167,
        tags: ["pulse", "dashes"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_168_terrain_sweep: {
        id: 'mode_168_terrain_sweep',
        name: 'Terrain Sweep',
        description: 'Mode 168: Scrolling heightmap like synthwave hills',
        category: 'Scientific',
        mode: 168,
        tags: ["terrain", "sweep"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_169_chromatic_bars_mirror: {
        id: 'mode_169_chromatic_bars_mirror',
        name: 'Chromatic Bars Mirror',
        description: 'Mode 169: Mirrored bars with central symmetry; hue rotates',
        category: 'Geometric',
        mode: 169,
        tags: ["chromatic", "bars", "mirror"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_170_bubble_choir: {
        id: 'mode_170_bubble_choir',
        name: 'Bubble Choir',
        description: 'Mode 170: Bubbles rise; size from band energy; pop on snare',
        category: 'Particles',
        mode: 170,
        tags: ["bubble", "choir"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_171_starfield_quantizer: {
        id: 'mode_171_starfield_quantizer',
        name: 'Starfield Quantizer',
        description: 'Mode 171: Stars quantized to a grid; cell brightness follows local band',
        category: 'Geometric',
        mode: 171,
        tags: ["starfield", "quantizer"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_172_dna_ladder: {
        id: 'mode_172_dna_ladder',
        name: 'Dna Ladder',
        description: 'Mode 172: Two sinusoid strands; rung length follows mids',
        category: 'Scientific',
        mode: 172,
        tags: ["ladder"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_173_arc_meter_trio: {
        id: 'mode_173_arc_meter_trio',
        name: 'Arc Meter Trio',
        description: 'Mode 173: Three concentric arcs for lows/mids/highs',
        category: 'Geometric',
        mode: 173,
        tags: ["meter", "trio"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_174_ink_splatter_scope: {
        id: 'mode_174_ink_splatter_scope',
        name: 'Ink Splatter Scope',
        description: 'Mode 174: Oscilloscope line with ink-style splats at transients',
        category: 'Fluid',
        mode: 174,
        tags: ["splatter", "scope"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_175_hex_cell_bloom: {
        id: 'mode_175_hex_cell_bloom',
        name: 'Hex Cell Bloom',
        description: 'Mode 175: Hex grid; cells bloom outward with frequency bucket',
        category: 'Geometric',
        mode: 175,
        tags: ["cell", "bloom"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_176_event_horizon_lattice: {
        id: 'mode_176_event_horizon_lattice',
        name: 'Event Horizon Lattice',
        description: 'Mode 176: Event Horizon Lattice - warped grid bends toward a black hole; streaks on transients',
        category: 'Geometric',
        mode: 176,
        tags: ["event", "horizon", "lattice"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_177_comet_conveyor: {
        id: 'mode_177_comet_conveyor',
        name: 'Comet Conveyor',
        description: 'Mode 177: Comet Conveyor - endless belt carries comets; tails shear on treble',
        category: 'Geometric',
        mode: 177,
        tags: ["comet", "conveyor"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_178_quantum_foam_micro: {
        id: 'mode_178_quantum_foam_micro',
        name: 'Quantum Foam Micro',
        description: 'Mode 178: Quantum Foam Micro - foamy micro-bubbles pop; cascades on peaks',
        category: 'Scientific',
        mode: 178,
        tags: ["quantum", "foam", "micro"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_179_aurora_crown: {
        id: 'mode_179_aurora_crown',
        name: 'Aurora Crown',
        description: 'Mode 179: Aurora Crown - polar aurora dome overhead; ribbons brighten by mids',
        category: 'Nature',
        mode: 179,
        tags: ["aurora", "crown"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_180_asteroid_excavator: {
        id: 'mode_180_asteroid_excavator',
        name: 'Asteroid Excavator',
        description: 'Mode 180: Asteroid Excavator - drill depth increases with bass; debris size follows highs',
        category: 'Geometric',
        mode: 180,
        tags: ["asteroid", "excavator"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_181_hyperloop_spectrotrain: {
        id: 'mode_181_hyperloop_spectrotrain',
        name: 'Hyperloop Spectrotrain',
        description: 'Mode 181: Hyperloop Spectrotrain - car length scales to energy; station lights strobe',
        category: 'Scientific',
        mode: 181,
        tags: ["hyperloop", "spectrotrain"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_182_galactic_pinball: {
        id: 'mode_182_galactic_pinball',
        name: 'Galactic Pinball',
        description: 'Mode 182: Galactic Pinball - bumpers map to bands; ball boosts on peaks',
        category: 'Geometric',
        mode: 182,
        tags: ["galactic", "pinball"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_183_nebula_inkblot: {
        id: 'mode_183_nebula_inkblot',
        name: 'Nebula Inkblot',
        description: 'Mode 183: Nebula Inkblot - mirrored volumetric smoke; hue by dominant band',
        category: 'Fluid',
        mode: 183,
        tags: ["nebula", "inkblot"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_184_satellite_telemetry_rings: {
        id: 'mode_184_satellite_telemetry_rings',
        name: 'Satellite Telemetry Rings',
        description: 'Mode 184: Satellite Telemetry Rings - rippling rings with dashed spectrum',
        category: 'Geometric',
        mode: 184,
        tags: ["satellite", "telemetry", "rings"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_185_wormhole_origami: {
        id: 'mode_185_wormhole_origami',
        name: 'Wormhole Origami',
        description: 'Mode 185: Wormhole Origami - sheet folds into portal; depth by bass',
        category: 'Geometric',
        mode: 185,
        tags: ["wormhole", "origami"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_186_holographic_jellyfish: {
        id: 'mode_186_holographic_jellyfish',
        name: 'Holographic Jellyfish',
        description: 'Mode 186: Holographic Jellyfish - bell pulsates with lows; tentacles sparkle with highs',
        category: 'Geometric',
        mode: 186,
        tags: ["holographic", "jellyfish"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_187_moon_quarry_crane: {
        id: 'mode_187_moon_quarry_crane',
        name: 'Moon Quarry Crane',
        description: 'Mode 187: Moon Quarry Crane - bins heights equal band magnitude; dust on kicks',
        category: 'Geometric',
        mode: 187,
        tags: ["moon", "quarry", "crane"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_188_constellation_typoplot: {
        id: 'mode_188_constellation_typoplot',
        name: 'Constellation Typoplot',
        description: 'Mode 188: Constellation TypoPlot - letters as stars; lines draw when band is hot',
        category: 'Geometric',
        mode: 188,
        tags: ["constellation", "typoplot"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_189_cryo_crystal_garden: {
        id: 'mode_189_cryo_crystal_garden',
        name: 'Cryo Crystal Garden',
        description: 'Mode 189: Cryo Crystal Garden - crystals grow per frequency slice; flare on treble',
        category: 'Nature',
        mode: 189,
        tags: ["cryo", "crystal", "garden"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_190_meteorite_blueprint: {
        id: 'mode_190_meteorite_blueprint',
        name: 'Meteorite Blueprint',
        description: 'Mode 190: Meteorite Blueprint - technical UI; callouts to bands; red stamp on peaks',
        category: 'Geometric',
        mode: 190,
        tags: ["meteorite", "blueprint"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_191_lunar_tide_pool: {
        id: 'mode_191_lunar_tide_pool',
        name: 'Lunar Tide Pool',
        description: 'Mode 191: Lunar Tide Pool - water level by bass; caustics sharpen with highs',
        category: 'Geometric',
        mode: 191,
        tags: ["lunar", "tide", "pool"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_192_orbital_barcode_slicer: {
        id: 'mode_192_orbital_barcode_slicer',
        name: 'Orbital Barcode Slicer',
        description: 'Mode 192: Orbital Barcode Slicer - rings slice vertical barcode; brightness per band',
        category: 'Geometric',
        mode: 192,
        tags: ["orbital", "barcode", "slicer"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_193_satellite_swarm_flocking: {
        id: 'mode_193_satellite_swarm_flocking',
        name: 'Satellite Swarm Flocking',
        description: 'Mode 193: Satellite Swarm Flocking - simple flock; thrust bursts on kick',
        category: 'Particles',
        mode: 193,
        tags: ["satellite", "swarm", "flocking"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_194_astro_pulse_weave: {
        id: 'mode_194_astro_pulse_weave',
        name: 'Astro Pulse Weave',
        description: 'Mode 194: Astro Pulse Weave - two opposing spiral waves; brightness sum of bands',
        category: 'Geometric',
        mode: 194,
        tags: ["astro", "pulse", "weave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_195_zero_g_paint_spheres: {
        id: 'mode_195_zero_g_paint_spheres',
        name: 'Zero G Paint Spheres',
        description: 'Mode 195: Zero-G Paint Spheres - spheres merge on peaks and split on highs',
        category: 'Scientific',
        mode: 195,
        tags: ["zero", "paint", "spheres"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_196_supernova_countdown: {
        id: 'mode_196_supernova_countdown',
        name: 'Supernova Countdown',
        description: 'Mode 196: Supernova Countdown - star swells with energy; blasts at threshold',
        category: 'Geometric',
        mode: 196,
        tags: ["supernova", "countdown"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_197_martian_wind_harp: {
        id: 'mode_197_martian_wind_harp',
        name: 'Martian Wind Harp',
        description: 'Mode 197: Martian Wind Harp - dunes as strings; ripples by mids; dust devils on snares',
        category: 'Geometric',
        mode: 197,
        tags: ["martian", "wind", "harp"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_198_teleporting_bar_choir: {
        id: 'mode_198_teleporting_bar_choir',
        name: 'Teleporting Bar Choir',
        description: 'Mode 198: Teleporting Bar Choir - bars pop at random radial positions; decay persists',
        category: 'Geometric',
        mode: 198,
        tags: ["teleporting", "choir"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_199_cosmic_vinyl_halo: {
        id: 'mode_199_cosmic_vinyl_halo',
        name: 'Cosmic Vinyl Halo',
        description: 'Mode 199: Cosmic Vinyl Halo - record edge-on; grooves shimmer with spectrum',
        category: 'Geometric',
        mode: 199,
        tags: ["cosmic", "vinyl", "halo"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_200_photon_origination_chamber: {
        id: 'mode_200_photon_origination_chamber',
        name: 'Photon Origination Chamber',
        description: 'Mode 200: Photon Origination Chamber - photons exit slits; rate per band bucket',
        category: 'Geometric',
        mode: 200,
        tags: ["photon", "origination", "chamber"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_201_meteor_net: {
        id: 'mode_201_meteor_net',
        name: 'Meteor Net',
        description: 'Mode 201: Meteor Net - hex net catches meteors; nodes glow by band',
        category: 'Geometric',
        mode: 201,
        tags: ["meteor"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_202_deep_space_garden_hose: {
        id: 'mode_202_deep_space_garden_hose',
        name: 'Deep Space Garden Hose',
        description: 'Mode 202: Deep-Space Garden Hose - spray pressure by amplitude; droplets chime on highs',
        category: 'Geometric',
        mode: 202,
        tags: ["deep", "space", "garden"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_203_horizon_monoliths: {
        id: 'mode_203_horizon_monoliths',
        name: 'Horizon Monoliths',
        description: 'Mode 203: Horizon Monoliths - distant monoliths rise with band; shadow sweeps on kicks',
        category: 'Geometric',
        mode: 203,
        tags: ["horizon", "monoliths"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_204_gravity_slingshot_trails: {
        id: 'mode_204_gravity_slingshot_trails',
        name: 'Gravity Slingshot Trails',
        description: 'Mode 204: Gravity Slingshot Trails - probes slingshot around planet; trail length by highs',
        category: 'Scientific',
        mode: 204,
        tags: ["gravity", "slingshot", "trails"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_205_solar_flare_notches: {
        id: 'mode_205_solar_flare_notches',
        name: 'Solar Flare Notches',
        description: 'Mode 205: Solar Flare Notches - solar disc with notch flares per bin',
        category: 'Geometric',
        mode: 205,
        tags: ["solar", "flare", "notches"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_206_tesseract_window: {
        id: 'mode_206_tesseract_window',
        name: 'Tesseract Window',
        description: 'Mode 206: Tesseract Window - 4D cube projection; face alpha by band energy',
        category: 'Geometric',
        mode: 206,
        tags: ["tesseract", "window"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_207_interstellar_postcards: {
        id: 'mode_207_interstellar_postcards',
        name: 'Interstellar Postcards',
        description: 'Mode 207: Interstellar Postcards - tiles flip; each hosts tiny spectrum motif',
        category: 'Geometric',
        mode: 207,
        tags: ["interstellar", "postcards"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_208_cosmic_braille: {
        id: 'mode_208_cosmic_braille',
        name: 'Cosmic Braille',
        description: 'Mode 208: Cosmic Braille - raised dots scroll; dot height by band',
        category: 'Scientific',
        mode: 208,
        tags: ["cosmic", "braille"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_209_stellar_harpoon: {
        id: 'mode_209_stellar_harpoon',
        name: 'Stellar Harpoon',
        description: 'Mode 209: Stellar Harpoon - line tension by amplitude; vibrato with highs',
        category: 'Geometric',
        mode: 209,
        tags: ["stellar", "harpoon"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_210_galaxy_ticker_tape: {
        id: 'mode_210_galaxy_ticker_tape',
        name: 'Galaxy Ticker Tape',
        description: 'Mode 210: Galaxy Ticker Tape - ticker snakes; character scale by band',
        category: 'Geometric',
        mode: 210,
        tags: ["galaxy", "ticker", "tape"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_211_antimatter_chess: {
        id: 'mode_211_antimatter_chess',
        name: 'Antimatter Chess',
        description: 'Mode 211: Antimatter Chess - pieces phase in/out; height maps to band',
        category: 'Geometric',
        mode: 211,
        tags: ["antimatter", "chess"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_212_star_nursery_conveyor: {
        id: 'mode_212_star_nursery_conveyor',
        name: 'Star Nursery Conveyor',
        description: 'Mode 212: Star Nursery Conveyor - progression speed from energy',
        category: 'Geometric',
        mode: 212,
        tags: ["star", "nursery", "conveyor"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_213_magnetar_lines: {
        id: 'mode_213_magnetar_lines',
        name: 'Magnetar Lines',
        description: 'Mode 213: Magnetar Lines - field lines whip; gamma flashes on transients',
        category: 'Geometric',
        mode: 213,
        tags: ["magnetar", "lines"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_214_zero_kelvin_diamonds: {
        id: 'mode_214_zero_kelvin_diamonds',
        name: 'Zero Kelvin Diamonds',
        description: 'Mode 214: Zero-Kelvin Diamonds - refracted beams thickness tracks bands; spin with tempo',
        category: 'Geometric',
        mode: 214,
        tags: ["zero", "kelvin", "diamonds"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_215_orbital_time_garden: {
        id: 'mode_215_orbital_time_garden',
        name: 'Orbital Time Garden',
        description: 'Mode 215: Orbital Time Garden - planets are clock markers; orbits expand with bass',
        category: 'Geometric',
        mode: 215,
        tags: ["orbital", "time", "garden"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_216_subspace_ribbon_printer: {
        id: 'mode_216_subspace_ribbon_printer',
        name: 'Subspace Ribbon Printer',
        description: 'Mode 216: Subspace Ribbon Printer - ribbon thickness equals summed band energy at slice',
        category: 'Geometric',
        mode: 216,
        tags: ["subspace", "ribbon", "printer"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_217_dark_matter_drizzle: {
        id: 'mode_217_dark_matter_drizzle',
        name: 'Dark Matter Drizzle',
        description: 'Mode 217: Dark-Matter Drizzle - invisible drizzle reveals when bands exceed threshold',
        category: 'Geometric',
        mode: 217,
        tags: ["dark", "matter", "drizzle"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_218_meteor_choir_cones: {
        id: 'mode_218_meteor_choir_cones',
        name: 'Meteor Choir Cones',
        description: 'Mode 218: Meteor Choir Cones - cone aperture by band; inner rings harmonics',
        category: 'Geometric',
        mode: 218,
        tags: ["meteor", "choir", "cones"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_219_folded_galaxy_map: {
        id: 'mode_219_folded_galaxy_map',
        name: 'Folded Galaxy Map',
        description: 'Mode 219: Folded Galaxy Map - folds reveal bar clusters; refolds during breakdown',
        category: 'Geometric',
        mode: 219,
        tags: ["folded", "galaxy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_220_ion_thruster_plume: {
        id: 'mode_220_ion_thruster_plume',
        name: 'Ion Thruster Plume',
        description: 'Mode 220: Ion Thruster Plume - plume length maps to amplitude; shock diamonds on peaks',
        category: 'Geometric',
        mode: 220,
        tags: ["thruster", "plume"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_221_cosmic_dominoes: {
        id: 'mode_221_cosmic_dominoes',
        name: 'Cosmic Dominoes',
        description: 'Mode 221: Cosmic Dominoes - curved domino line; fall rate by energy; tiles display local bars',
        category: 'Geometric',
        mode: 221,
        tags: ["cosmic", "dominoes"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_222_spacesuit_hud: {
        id: 'mode_222_spacesuit_hud',
        name: 'Spacesuit Hud',
        description: 'Mode 222: Spacesuit HUD - HUD overlays with spectrum wedges; warning flashes on peaks',
        category: 'Geometric',
        mode: 222,
        tags: ["spacesuit"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_223_pulsar_barcode_beam: {
        id: 'mode_223_pulsar_barcode_beam',
        name: 'Pulsar Barcode Beam',
        description: 'Mode 223: Pulsar Barcode Beam - rotating beam; bar lengths by band; bloom on peaks',
        category: 'Geometric',
        mode: 223,
        tags: ["pulsar", "barcode", "beam"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_224_astro_terrarium: {
        id: 'mode_224_astro_terrarium',
        name: 'Astro Terrarium',
        description: 'Mode 224: Astro Terrarium - micro planet ecosystem; eruptions on kicks; biolume with highs',
        category: 'Geometric',
        mode: 224,
        tags: ["astro", "terrarium"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_225_micrometeor_spark_curtain: {
        id: 'mode_225_micrometeor_spark_curtain',
        name: 'Micrometeor Spark Curtain',
        description: 'Mode 225: Micrometeor Spark Curtain - diagonal sparks; density with amplitude',
        category: 'Scientific',
        mode: 225,
        tags: ["micrometeor", "spark", "curtain"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_276_quantum_lattice: {
        id: 'mode_276_quantum_lattice',
        name: 'Quantum Lattice',
        description: '3D-looking quantum lattice that shifts with bass',
        category: 'Scientific',
        mode: 276,
        tags: ["quantum", "lattice"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_277_prism_rays: {
        id: 'mode_277_prism_rays',
        name: 'Prism Rays',
        description: 'Light rays splitting through a prism',
        category: 'Geometric',
        mode: 277,
        tags: ["prism", "rays"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_278_liquid_nitrogen: {
        id: 'mode_278_liquid_nitrogen',
        name: 'Liquid Nitrogen',
        description: 'Freezing and shattering effects',
        category: 'Fluid',
        mode: 278,
        tags: ["liquid", "nitrogen"],
        parameters: {
            freezeIntensity: { min: 0.1, max: 2, default: 1, label: 'Freeze Intensity' },
            shatterAmount: { min: 0.1, max: 3, default: 1.5, label: 'Shatter Amount' },
            crystallization: { min: 1, max: 10, default: 5, label: 'Crystallization' }
        }
    },
    mode_279_silk_road_caravan: {
        id: 'mode_279_silk_road_caravan',
        name: 'Silk Road Caravan',
        description: 'Moving lights across the screen like a caravan',
        category: 'Geometric',
        mode: 279,
        tags: ["silk", "road", "caravan"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_280_steampunk_gears: {
        id: 'mode_280_steampunk_gears',
        name: 'Steampunk Gears',
        description: 'Rotating mechanical gears',
        category: 'Geometric',
        mode: 280,
        tags: ["steampunk", "gears"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_281_dragon_scales: {
        id: 'mode_281_dragon_scales',
        name: 'Dragon Scales',
        description: 'Overlapping scale patterns like dragon skin',
        category: 'Geometric',
        mode: 281,
        tags: ["dragon", "scales"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_282_time_dilation_grid: {
        id: 'mode_282_time_dilation_grid',
        name: 'Time Dilation Grid',
        description: 'Warped spacetime grid',
        category: 'Geometric',
        mode: 282,
        tags: ["time", "dilation", "grid"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_283_fiber_bundle: {
        id: 'mode_283_fiber_bundle',
        name: 'Fiber Bundle',
        description: 'Mathematical fiber bundle visualization',
        category: 'Geometric',
        mode: 283,
        tags: ["fiber", "bundle"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_284_moth_wing_shimmer: {
        id: 'mode_284_moth_wing_shimmer',
        name: 'Moth Wing Shimmer',
        description: 'Iridescent shimmer patterns like moth wings',
        category: 'Geometric',
        mode: 284,
        tags: ["moth", "wing", "shimmer"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_285_cathedral_rose: {
        id: 'mode_285_cathedral_rose',
        name: 'Cathedral Rose',
        description: 'Rose window geometry like a cathedral',
        category: 'Geometric',
        mode: 285,
        tags: ["cathedral", "rose"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_286_neon_veins_pulse: {
        id: 'mode_286_neon_veins_pulse',
        name: 'Neon Veins Pulse',
        description: 'Pulsing vein-like network',
        category: 'Tech',
        mode: 286,
        tags: ["neon", "veins", "pulse"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_287_glacial_crack: {
        id: 'mode_287_glacial_crack',
        name: 'Glacial Crack',
        description: 'Spreading ice crack patterns',
        category: 'Geometric',
        mode: 287,
        tags: ["glacial", "crack"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_288_quantum_dots: {
        id: 'mode_288_quantum_dots',
        name: 'Quantum Dots',
        description: 'Floating quantum dot particles',
        category: 'Scientific',
        mode: 288,
        tags: ["quantum", "dots"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_289_origami_crane_flight: {
        id: 'mode_289_origami_crane_flight',
        name: 'Origami Crane Flight',
        description: 'Geometric origami birds in flight',
        category: 'Geometric',
        mode: 289,
        tags: ["origami", "crane", "flight"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_290_magma_chamber: {
        id: 'mode_290_magma_chamber',
        name: 'Magma Chamber',
        description: 'Bubbling lava effects',
        category: 'Geometric',
        mode: 290,
        tags: ["magma", "chamber"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_291_spider_web_dew: {
        id: 'mode_291_spider_web_dew',
        name: 'Spider Web Dew',
        description: 'Dew drops on spider web',
        category: 'Geometric',
        mode: 291,
        tags: ["spider"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_292_nebula_birth: {
        id: 'mode_292_nebula_birth',
        name: 'Nebula Birth',
        description: 'Gas cloud formation',
        category: 'Geometric',
        mode: 292,
        tags: ["nebula", "birth"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_293_circuit_board_live: {
        id: 'mode_293_circuit_board_live',
        name: 'Circuit Board Live',
        description: 'Live electric circuit patterns',
        category: 'Scientific',
        mode: 293,
        tags: ["circuit", "board", "live"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_294_bioluminescent_tide: {
        id: 'mode_294_bioluminescent_tide',
        name: 'Bioluminescent Tide',
        description: 'Glowing wave patterns',
        category: 'Geometric',
        mode: 294,
        tags: ["bioluminescent", "tide"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_295_tesseract_projection: {
        id: 'mode_295_tesseract_projection',
        name: 'Tesseract Projection',
        description: '4D hypercube projection',
        category: 'Geometric',
        mode: 295,
        tags: ["tesseract", "projection"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_296_frost_crystal_growth: {
        id: 'mode_296_frost_crystal_growth',
        name: 'Frost Crystal Growth',
        description: 'Growing ice crystals',
        category: 'Nature',
        mode: 296,
        tags: ["frost", "crystal", "growth"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_297_sound_wave_interference: {
        id: 'mode_297_sound_wave_interference',
        name: 'Sound Wave Interference',
        description: 'Wave interference patterns',
        category: 'Geometric',
        mode: 297,
        tags: ["sound", "wave", "interference"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_298_holographic_fracture: {
        id: 'mode_298_holographic_fracture',
        name: 'Holographic Fracture',
        description: 'Broken hologram effect',
        category: 'Geometric',
        mode: 298,
        tags: ["holographic", "fracture"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_299_plasma_ball_arc: {
        id: 'mode_299_plasma_ball_arc',
        name: 'Plasma Ball Arc',
        description: 'Electric plasma arcs',
        category: 'Energy',
        mode: 299,
        tags: ["plasma", "ball"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_300_eternal_flame_dance: {
        id: 'mode_300_eternal_flame_dance',
        name: 'Eternal Flame Dance',
        description: 'Flowing fire patterns',
        category: 'Geometric',
        mode: 300,
        tags: ["eternal", "flame", "dance"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_301_forest_canopy: {
        id: 'mode_301_forest_canopy',
        name: 'Forest Canopy',
        description: 'Mode 301: Tree canopy with swaying branches',
        category: 'Nature',
        mode: 301,
        tags: ["forest", "canopy"],
        parameters: {
            treeCount: { min: 5, max: 25, default: 12, label: 'Number of Trees' },
            swayIntensity: { min: 0.5, max: 3, default: 1, label: 'Sway Intensity' },
            branchDensity: { min: 10, max: 60, default: 30, label: 'Branch Density' }
        }
    },
    mode_302_ocean_waves: {
        id: 'mode_302_ocean_waves',
        name: 'Ocean Waves',
        description: 'Mode 302: Flowing ocean waves with foam',
        category: 'Nature',
        mode: 302,
        tags: ["ocean", "waves"],
        parameters: {
            waveCount: { min: 3, max: 10, default: 5, label: 'Wave Layers' },
            waveSpeed: { min: 0.05, max: 0.3, default: 0.1, label: 'Wave Speed' },
            foamIntensity: { min: 0.5, max: 2, default: 1, label: 'Foam Intensity' }
        }
    },
    mode_303_coral_reef: {
        id: 'mode_303_coral_reef',
        name: 'Coral Reef',
        description: 'Mode 303: Coral formations with flowing tentacles',
        category: 'Nature',
        mode: 303,
        tags: ["coral", "reef"],
        parameters: {
            coralCount: { min: 5, max: 30, default: 15, label: 'Coral Count' },
            tentacleLength: { min: 15, max: 50, default: 30, label: 'Tentacle Length' },
            swaySpeed: { min: 0.03, max: 0.15, default: 0.08, label: 'Sway Speed' }
        }
    },
    mode_304_butterfly_swarm: {
        id: 'mode_304_butterfly_swarm',
        name: 'Butterfly Swarm',
        description: 'Mode 304: Butterflies dancing to music',
        category: 'Particles',
        mode: 304,
        tags: ["butterfly", "swarm"],
        parameters: {
            butterflyCount: { min: 10, max: 100, default: 50, label: 'Butterfly Count' },
            flightRadius: { min: 100, max: 300, default: 200, label: 'Flight Radius' },
            wingSize: { min: 5, max: 25, default: 15, label: 'Wing Size' }
        }
    },
    mode_305_mountain_peaks: {
        id: 'mode_305_mountain_peaks',
        name: 'Mountain Peaks',
        description: 'Mode 305: Mountain ranges responding to frequencies',
        category: 'Scientific',
        mode: 305,
        tags: ["mountain", "peaks"],
        parameters: {
            peakHeight: { min: 0.3, max: 0.9, default: 0.7, label: 'Peak Height' },
            snowThreshold: { min: 0.4, max: 0.8, default: 0.6, label: 'Snow Threshold' },
            smoothness: { min: 1, max: 5, default: 1, label: 'Mountain Smoothness' }
        }
    },
    mode_306_fireflies: {
        id: 'mode_306_fireflies',
        name: 'Fireflies',
        description: 'Mode 306: Fireflies glowing and flickering',
        category: 'Nature',
        mode: 306,
        tags: ["fireflies"],
        parameters: {
            fireflyCount: { min: 20, max: 200, default: 100, label: 'Firefly Count' },
            glowIntensity: { min: 0.5, max: 2, default: 1, label: 'Glow Intensity' },
            glowSize: { min: 2, max: 15, default: 8, label: 'Glow Size' }
        }
    },
    mode_307_flower_bloom: {
        id: 'mode_307_flower_bloom',
        name: 'Flower Bloom',
        description: 'Mode 307: Flowers blooming radially',
        category: 'Nature',
        mode: 307,
        tags: ["flower", "bloom"],
        parameters: {
            flowerCount: { min: 4, max: 16, default: 8, label: 'Flower Count' },
            petalCount: { min: 20, max: 50, default: 30, label: 'Petal Count' },
            bloomSize: { min: 50, max: 200, default: 100, label: 'Bloom Size' }
        }
    },
    mode_308_rain_ripples: {
        id: 'mode_308_rain_ripples',
        name: 'Rain Ripples',
        description: 'Mode 308: Rain creating ripples on water surface',
        category: 'Scientific',
        mode: 308,
        tags: ["rain", "ripples"],
        parameters: {
            dropletCount: { min: 20, max: 150, default: 80, label: 'Droplet Count' },
            rippleSpeed: { min: 1, max: 5, default: 3, label: 'Ripple Speed' },
            maxRippleSize: { min: 30, max: 100, default: 50, label: 'Max Ripple Size' }
        }
    },
    mode_309_leaf_fall: {
        id: 'mode_309_leaf_fall',
        name: 'Leaf Fall',
        description: 'Mode 309: Autumn leaves falling',
        category: 'Geometric',
        mode: 309,
        tags: ["leaf", "fall"],
        parameters: {
            leafCount: { min: 20, max: 100, default: 50, label: 'Leaf Count' },
            fallSpeed: { min: 1, max: 4, default: 2, label: 'Fall Speed' },
            swayAmount: { min: 5, max: 30, default: 20, label: 'Sway Amount' }
        }
    },
    mode_310_tree_rings: {
        id: 'mode_310_tree_rings',
        name: 'Tree Rings',
        description: 'Mode 310: Growth rings of a tree',
        category: 'Nature',
        mode: 310,
        tags: ["tree", "rings"],
        parameters: {
            ringCount: { min: 20, max: 120, default: 64, label: 'Number of Rings' },
            ringThickness: { min: 1, max: 10, default: 5, label: 'Ring Thickness' },
            ringVariation: { min: 0, max: 40, default: 20, label: 'Ring Variation' }
        }
    },
    mode_311_lightning_storm: {
        id: 'mode_311_lightning_storm',
        name: 'Lightning Storm',
        description: 'Mode 311: Lightning bolts during storm',
        category: 'Energy',
        mode: 311,
        tags: ["lightning", "storm"],
        parameters: {
            boltFrequency: { min: 0.3, max: 1, default: 0.6, label: 'Strike Frequency' },
            boltComplexity: { min: 5, max: 20, default: 10, label: 'Bolt Branches' },
            flashIntensity: { min: 0.5, max: 2, default: 1, label: 'Flash Intensity' }
        }
    },
    mode_312_pond_koi: {
        id: 'mode_312_pond_koi',
        name: 'Pond Koi',
        description: 'Mode 312: Koi fish swimming in pond',
        category: 'Geometric',
        mode: 312,
        tags: ["pond"],
        parameters: {
            fishCount: { min: 4, max: 16, default: 8, label: 'Number of Koi' },
            swimSpeed: { min: 0.01, max: 0.05, default: 0.02, label: 'Swim Speed' },
            fishSize: { min: 10, max: 30, default: 20, label: 'Fish Size' }
        }
    },
    mode_313_moss_growth: {
        id: 'mode_313_moss_growth',
        name: 'Moss Growth',
        description: 'Mode 313: Moss spreading organically',
        category: 'Geometric',
        mode: 313,
        tags: ["moss", "growth"],
        parameters: {
            mossPatches: { min: 50, max: 200, default: 100, label: 'Moss Patches' },
            spreadRadius: { min: 5, max: 25, default: 15, label: 'Spread Radius' },
            growthDensity: { min: 0.1, max: 0.5, default: 0.2, label: 'Growth Density' }
        }
    },
    mode_314_aurora_forest: {
        id: 'mode_314_aurora_forest',
        name: 'Aurora Forest',
        description: 'Mode 314: Northern lights over forest',
        category: 'Nature',
        mode: 314,
        tags: ["aurora", "forest"],
        parameters: {
            auroraLayers: { min: 5, max: 20, default: 10, label: 'Aurora Layers' },
            waveSpeed: { min: 0.05, max: 0.2, default: 0.1, label: 'Wave Speed' },
            treeCount: { min: 10, max: 30, default: 20, label: 'Tree Count' }
        }
    },
    mode_315_dandelion_seeds: {
        id: 'mode_315_dandelion_seeds',
        name: 'Dandelion Seeds',
        description: 'Mode 315: Dandelion seeds floating in wind',
        category: 'Geometric',
        mode: 315,
        tags: ["dandelion", "seeds"],
        parameters: {
            seedCount: { min: 30, max: 120, default: 60, label: 'Seed Count' },
            driftSpeed: { min: 0.5, max: 3, default: 1.5, label: 'Drift Speed' },
            windStrength: { min: 0.1, max: 1, default: 0.5, label: 'Wind Strength' }
        }
    },
    mode_316_fern_fractals: {
        id: 'mode_316_fern_fractals',
        name: 'Fern Fractals',
        description: 'Mode 316: Fractal fern patterns',
        category: 'Geometric',
        mode: 316,
        tags: ["fern", "fractals"],
        parameters: {
            branchDepth: { min: 10, max: 40, default: 20, label: 'Branch Depth' },
            branchAngle: { min: 30, max: 60, default: 45, label: 'Branch Angle' },
            fernLength: { min: 20, max: 60, default: 40, label: 'Fern Length' }
        }
    },
    mode_317_beehive_cells: {
        id: 'mode_317_beehive_cells',
        name: 'Beehive Cells',
        description: 'Mode 317: Hexagonal honeycomb pattern',
        category: 'Geometric',
        mode: 317,
        tags: ["beehive", "cells"],
        parameters: {
            hexSize: { min: 15, max: 50, default: 30, label: 'Hexagon Size' },
            cellDensity: { min: 0.1, max: 0.5, default: 0.3, label: 'Cell Activity' },
            honeycombGlow: { min: 0.5, max: 2, default: 1, label: 'Glow Intensity' }
        }
    },
    mode_318_wheat_field: {
        id: 'mode_318_wheat_field',
        name: 'Wheat Field',
        description: 'Mode 318: Wheat swaying in wind',
        category: 'Geometric',
        mode: 318,
        tags: ["wheat", "field"],
        parameters: {
            wheatStalks: { min: 20, max: 60, default: 40, label: 'Wheat Stalks' },
            swaySpeed: { min: 0.05, max: 0.2, default: 0.1, label: 'Sway Speed' },
            windWaves: { min: 5, max: 20, default: 10, label: 'Wind Wave Intensity' }
        }
    },
    mode_319_spider_web: {
        id: 'mode_319_spider_web',
        name: 'Spider Web',
        description: 'Mode 319: Spider web with dew drops',
        category: 'Geometric',
        mode: 319,
        tags: ["spider"],
        parameters: {
            radialThreads: { min: 8, max: 20, default: 12, label: 'Radial Threads' },
            concentricRings: { min: 20, max: 60, default: 40, label: 'Concentric Rings' },
            dewDrops: { min: 0.2, max: 0.6, default: 0.4, label: 'Dew Threshold' }
        }
    },
    mode_320_mushroom_spores: {
        id: 'mode_320_mushroom_spores',
        name: 'Mushroom Spores',
        description: 'Mode 320: Mushroom spores floating',
        category: 'Geometric',
        mode: 320,
        tags: ["mushroom", "spores"],
        parameters: {
            sporeCount: { min: 40, max: 160, default: 80, label: 'Spore Count' },
            floatSpeed: { min: 0.5, max: 3, default: 1.5, label: 'Float Speed' },
            driftAmount: { min: 10, max: 40, default: 30, label: 'Drift Amount' }
        }
    },
    mode_321_bamboo_forest: {
        id: 'mode_321_bamboo_forest',
        name: 'Bamboo Forest',
        description: 'Mode 321: Bamboo stalks swaying',
        category: 'Nature',
        mode: 321,
        tags: ["bamboo", "forest"],
        parameters: {
            bambooStalks: { min: 8, max: 25, default: 15, label: 'Bamboo Stalks' },
            swayAmount: { min: 5, max: 25, default: 15, label: 'Sway Amount' },
            segmentCount: { min: 5, max: 12, default: 8, label: 'Segments per Stalk' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_322_tide_pools: {
        id: 'mode_322_tide_pools',
        name: 'Tide Pools',
        description: 'Mode 322: Tide pools with sea life',
        category: 'Geometric',
        mode: 322,
        tags: ["tide", "pools"],
        parameters: {
            poolCount: { min: 3, max: 10, default: 6, label: 'Tide Pools' },
            creatureCount: { min: 5, max: 20, default: 10, label: 'Creatures per Pool' },
            waveSpeed: { min: 0.02, max: 0.1, default: 0.05, label: 'Wave Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_323_vine_tendrils: {
        id: 'mode_323_vine_tendrils',
        name: 'Vine Tendrils',
        description: 'Mode 323: Growing vine tendrils',
        category: 'Geometric',
        mode: 323,
        tags: ["vine", "tendrils"],
        parameters: {
            vineCount: { min: 4, max: 12, default: 8, label: 'Vine Count' },
            growthLength: { min: 20, max: 60, default: 40, label: 'Growth Length' },
            curlAmount: { min: 10, max: 30, default: 20, label: 'Curl Amount' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_324_crystal_cave: {
        id: 'mode_324_crystal_cave',
        name: 'Crystal Cave',
        description: 'Mode 324: Crystalline cave formations',
        category: 'Nature',
        mode: 324,
        tags: ["crystal", "cave"],
        parameters: {
            crystalCount: { min: 8, max: 20, default: 12, label: 'Crystal Count' },
            crystalSize: { min: 15, max: 40, default: 25, label: 'Crystal Size' },
            sparkleIntensity: { min: 0.5, max: 2, default: 1, label: 'Sparkle Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_325_bird_murmuration: {
        id: 'mode_325_bird_murmuration',
        name: 'Bird Murmuration',
        description: 'Mode 325: Flock of birds in murmuration',
        category: 'Geometric',
        mode: 325,
        tags: ["bird", "murmuration"],
        parameters: {
            birdCount: { min: 50, max: 200, default: 100, label: 'Bird Count' },
            flockSpeed: { min: 0.02, max: 0.1, default: 0.05, label: 'Flock Speed' },
            formationTightness: { min: 0.5, max: 2, default: 1, label: 'Formation Tightness' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_326_river_flow: {
        id: 'mode_326_river_flow',
        name: 'River Flow',
        description: 'Mode 326: River flowing with currents',
        category: 'Geometric',
        mode: 326,
        tags: ["river", "flow"],
        parameters: {
            flowLayers: { min: 4, max: 12, default: 8, label: 'Flow Layers' },
            currentSpeed: { min: 0.05, max: 0.2, default: 0.1, label: 'Current Speed' },
            rippleAmount: { min: 5, max: 25, default: 15, label: 'Ripple Amount' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_327_seed_pods: {
        id: 'mode_327_seed_pods',
        name: 'Seed Pods',
        description: 'Mode 327: Seed pods bursting open',
        category: 'Geometric',
        mode: 327,
        tags: ["seed", "pods"],
        parameters: {
            podCount: { min: 5, max: 15, default: 10, label: 'Seed Pods' },
            burstThreshold: { min: 0.3, max: 0.6, default: 0.4, label: 'Burst Threshold' },
            seedsPerPod: { min: 8, max: 16, default: 12, label: 'Seeds per Pod' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_328_algae_bloom: {
        id: 'mode_328_algae_bloom',
        name: 'Algae Bloom',
        description: 'Mode 328: Algae blooming in water',
        category: 'Geometric',
        mode: 328,
        tags: ["algae", "bloom"],
        parameters: {
            algaePatches: { min: 80, max: 250, default: 150, label: 'Algae Patches' },
            bloomSize: { min: 5, max: 25, default: 15, label: 'Bloom Size' },
            growthRate: { min: 0.1, max: 0.4, default: 0.2, label: 'Growth Rate' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_329_cactus_spines: {
        id: 'mode_329_cactus_spines',
        name: 'Cactus Spines',
        description: 'Mode 329: Cactus with radiating spines',
        category: 'Geometric',
        mode: 329,
        tags: ["cactus", "spines"],
        parameters: {
            cactusSegments: { min: 20, max: 60, default: 40, label: 'Cactus Segments' },
            spineCount: { min: 4, max: 12, default: 8, label: 'Spines per Segment' },
            spineLength: { min: 10, max: 30, default: 20, label: 'Spine Length' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_330_snowflakes: {
        id: 'mode_330_snowflakes',
        name: 'Snowflakes',
        description: 'Mode 330: Unique snowflakes falling',
        category: 'Geometric',
        mode: 330,
        tags: ["snowflakes"],
        parameters: {
            snowflakeCount: { min: 30, max: 100, default: 50, label: 'Snowflake Count' },
            fallSpeed: { min: 0.8, max: 3, default: 1.5, label: 'Fall Speed' },
            symmetryArms: { min: 4, max: 8, default: 6, label: 'Symmetry Arms' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_331_lava_flow: {
        id: 'mode_331_lava_flow',
        name: 'Lava Flow',
        description: 'Mode 331: Molten lava flowing',
        category: 'Fluid',
        mode: 331,
        tags: ["lava", "flow"],
        parameters: {
            lavaLayers: { min: 4, max: 12, default: 6, label: 'Lava Layers' },
            flowSpeed: { min: 0.5, max: 3, default: 1.5, label: 'Flow Speed' },
            viscosity: { min: 0.01, max: 0.1, default: 0.03, label: 'Viscosity' },
            waveAmplitude: { min: 10, max: 100, default: 40, label: 'Wave Height' },
            glowIntensity: { min: 0.5, max: 2, default: 1, label: 'Glow Intensity' },
            trailOpacity: { min: 0.05, max: 0.4, default: 0.15, label: 'Trail Fade' }
        }
    },
    mode_332_ice_crystals: {
        id: 'mode_332_ice_crystals',
        name: 'Ice Crystals',
        description: 'Mode 332: Ice crystal formations',
        category: 'Nature',
        mode: 332,
        tags: ["crystals"],
        parameters: {
            crystalCount: { min: 10, max: 25, default: 15, label: 'Ice Crystals' },
            branchCount: { min: 4, max: 8, default: 6, label: 'Crystal Branches' },
            rotationSpeed: { min: 0.01, max: 0.05, default: 0.02, label: 'Rotation Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_333_pine_cones: {
        id: 'mode_333_pine_cones',
        name: 'Pine Cones',
        description: 'Mode 333: Pine cone spiral patterns',
        category: 'Geometric',
        mode: 333,
        tags: ["pine", "cones"],
        parameters: {
            spiralDensity: { min: 30, max: 120, default: 64, label: 'Spiral Density' },
            coneSize: { min: 3, max: 12, default: 8, label: 'Cone Size' },
            goldenAngle: { min: 135, max: 140, default: 137.5, label: 'Golden Angle' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_334_geyser_eruption: {
        id: 'mode_334_geyser_eruption',
        name: 'Geyser Eruption',
        description: 'Mode 334: Geyser water erupting',
        category: 'Geometric',
        mode: 334,
        tags: ["geyser", "eruption"],
        parameters: {
            eruptionThreshold: { min: 0.4, max: 0.7, default: 0.5, label: 'Eruption Threshold' },
            steamHeight: { min: 15, max: 30, default: 20, label: 'Steam Height' },
            particleCount: { min: 20, max: 60, default: 40, label: 'Steam Particles' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_335_pollen_cloud: {
        id: 'mode_335_pollen_cloud',
        name: 'Pollen Cloud',
        description: 'Mode 335: Pollen drifting in air',
        category: 'Geometric',
        mode: 335,
        tags: ["pollen", "cloud"],
        parameters: {
            pollenCount: { min: 50, max: 200, default: 100, label: 'Pollen Count' },
            driftSpeed: { min: 0.01, max: 0.05, default: 0.02, label: 'Drift Speed' },
            particleSize: { min: 2, max: 8, default: 5, label: 'Particle Size' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_336_desert_dunes: {
        id: 'mode_336_desert_dunes',
        name: 'Desert Dunes',
        description: 'Mode 336: Sand dunes in wind',
        category: 'Geometric',
        mode: 336,
        tags: ["desert", "dunes"],
        parameters: {
            duneCount: { min: 3, max: 6, default: 4, label: 'Sand Dunes' },
            windSpeed: { min: 0.01, max: 0.05, default: 0.02, label: 'Wind Speed' },
            duneHeight: { min: 20, max: 60, default: 40, label: 'Dune Height' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_337_lily_pads: {
        id: 'mode_337_lily_pads',
        name: 'Lily Pads',
        description: 'Mode 337: Water lilies on pond',
        category: 'Geometric',
        mode: 337,
        tags: ["lily", "pads"],
        parameters: {
            lilyPadCount: { min: 6, max: 18, default: 12, label: 'Lily Pads' },
            flowerThreshold: { min: 0.4, max: 0.7, default: 0.5, label: 'Flower Threshold' },
            driftSpeed: { min: 0.005, max: 0.02, default: 0.01, label: 'Drift Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_338_termite_mound: {
        id: 'mode_338_termite_mound',
        name: 'Termite Mound',
        description: 'Mode 338: Termite mound structure',
        category: 'Geometric',
        mode: 338,
        tags: ["termite", "mound"],
        parameters: {
            moundLayers: { min: 20, max: 80, default: 60, label: 'Mound Layers' },
            chamberCount: { min: 10, max: 30, default: 20, label: 'Chambers' },
            chamberThreshold: { min: 0.3, max: 0.6, default: 0.4, label: 'Chamber Threshold' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_339_cherry_blossoms: {
        id: 'mode_339_cherry_blossoms',
        name: 'Cherry Blossoms',
        description: 'Mode 339: Cherry blossom petals falling',
        category: 'Geometric',
        mode: 339,
        tags: ["cherry", "blossoms"],
        parameters: {
            petalCount: { min: 30, max: 100, default: 60, label: 'Petal Count' },
            fallSpeed: { min: 0.5, max: 2, default: 0.8, label: 'Fall Speed' },
            flutter: { min: 10, max: 35, default: 25, label: 'Flutter Amount' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_340_root_system: {
        id: 'mode_340_root_system',
        name: 'Root System',
        description: 'Mode 340: Underground root network',
        category: 'Geometric',
        mode: 340,
        tags: ["root", "system"],
        parameters: {
            maxDepth: { min: 5, max: 12, default: 8, label: 'Root Depth' },
            branchThreshold: { min: 0.2, max: 0.5, default: 0.3, label: 'Branch Threshold' },
            rootThickness: { min: 1, max: 10, default: 5, label: 'Root Thickness' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_341_plankton_swarm: {
        id: 'mode_341_plankton_swarm',
        name: 'Plankton Swarm',
        description: 'Mode 341: Bioluminescent plankton',
        category: 'Particles',
        mode: 341,
        tags: ["plankton", "swarm"],
        parameters: {
            planktonCount: { min: 50, max: 150, default: 100, label: 'Plankton Count' },
            glowIntensity: { min: 0.5, max: 2, default: 1, label: 'Glow Intensity' },
            waveAmplitude: { min: 0.2, max: 0.5, default: 0.3, label: 'Wave Amplitude' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_342_frost_patterns: {
        id: 'mode_342_frost_patterns',
        name: 'Frost Patterns',
        description: 'Mode 342: Frost forming on glass',
        category: 'Geometric',
        mode: 342,
        tags: ["frost", "patterns"],
        parameters: {
            frostDensity: { min: 30, max: 80, default: 50, label: 'Frost Density' },
            branchLength: { min: 15, max: 40, default: 30, label: 'Branch Length' },
            spreadAngle: { min: 30, max: 90, default: 60, label: 'Spread Angle' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_343_ant_trails: {
        id: 'mode_343_ant_trails',
        name: 'Ant Trails',
        description: 'Mode 343: Ant colony foraging trails',
        category: 'Scientific',
        mode: 343,
        tags: ["trails"],
        parameters: {
            trailCount: { min: 6, max: 12, default: 8, label: 'Ant Trails' },
            trailLength: { min: 20, max: 60, default: 40, label: 'Trail Length' },
            antSpeed: { min: 0.3, max: 1, default: 0.5, label: 'Ant Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_344_seaweed_sway: {
        id: 'mode_344_seaweed_sway',
        name: 'Seaweed Sway',
        description: 'Mode 344: Seaweed swaying underwater',
        category: 'Geometric',
        mode: 344,
        tags: ["seaweed", "sway"],
        parameters: {
            strandCount: { min: 8, max: 20, default: 12, label: 'Seaweed Strands' },
            swayAmount: { min: 10, max: 35, default: 25, label: 'Sway Amount' },
            swaySpeed: { min: 0.05, max: 0.15, default: 0.08, label: 'Sway Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_345_volcano_ash: {
        id: 'mode_345_volcano_ash',
        name: 'Volcano Ash',
        description: 'Mode 345: Volcanic ash cloud',
        category: 'Geometric',
        mode: 345,
        tags: ["volcano"],
        parameters: {
            ashDensity: { min: 50, max: 200, default: 100, label: 'Ash Density' },
            plumeHeight: { min: 100, max: 400, default: 250, label: 'Plume Height' },
            spreadRate: { min: 1, max: 4, default: 2, label: 'Spread Rate' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_346_dragonfly_wings: {
        id: 'mode_346_dragonfly_wings',
        name: 'Dragonfly Wings',
        description: 'Mode 346: Dragonfly wing patterns',
        category: 'Geometric',
        mode: 346,
        tags: ["dragonfly", "wings"],
        parameters: {
            dragonflyCount: { min: 4, max: 10, default: 6, label: 'Dragonfly Count' },
            wingSize: { min: 15, max: 35, default: 20, label: 'Wing Size' },
            flightSpeed: { min: 0.03, max: 0.08, default: 0.05, label: 'Flight Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_347_pebble_ripples: {
        id: 'mode_347_pebble_ripples',
        name: 'Pebble Ripples',
        description: 'Mode 347: Pebbles dropping in water',
        category: 'Geometric',
        mode: 347,
        tags: ["pebble", "ripples"],
        parameters: {
            rippleCount: { min: 20, max: 80, default: 50, label: 'Ripple Count' },
            rippleLifetime: { min: 20, max: 40, default: 30, label: 'Ripple Lifetime' },
            dropThreshold: { min: 0.4, max: 0.7, default: 0.5, label: 'Drop Threshold' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_348_moss_tendrils: {
        id: 'mode_348_moss_tendrils',
        name: 'Moss Tendrils',
        description: 'Mode 348: Moss growing on stone',
        category: 'Geometric',
        mode: 348,
        tags: ["moss", "tendrils"],
        parameters: {
            mossPatches: { min: 100, max: 300, default: 200, label: 'Moss Patches' },
            patchSize: { min: 5, max: 20, default: 10, label: 'Patch Size' },
            growthDensity: { min: 5, max: 15, default: 10, label: 'Growth Density' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_349_starfish_arms: {
        id: 'mode_349_starfish_arms',
        name: 'Starfish Arms',
        description: 'Mode 349: Starfish with moving arms',
        category: 'Geometric',
        mode: 349,
        tags: ["starfish", "arms"],
        parameters: {
            armCount: { min: 4, max: 6, default: 5, label: 'Starfish Arms' },
            armLength: { min: 20, max: 50, default: 35, label: 'Arm Length' },
            waveAmount: { min: 0.1, max: 0.5, default: 0.3, label: 'Wave Amount' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_350_venus_flytrap: {
        id: 'mode_350_venus_flytrap',
        name: 'Venus Flytrap',
        description: 'Mode 350: Venus flytrap opening and closing',
        category: 'Geometric',
        mode: 350,
        tags: ["venus", "flytrap"],
        parameters: {
            openAngle: { min: 30, max: 90, default: 60, label: 'Opening Angle' },
            triggerHairs: { min: 3, max: 7, default: 5, label: 'Trigger Hairs' },
            snapSpeed: { min: 0.5, max: 2, default: 1, label: 'Snap Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_351_rainbow_mist: {
        id: 'mode_351_rainbow_mist',
        name: 'Rainbow Mist',
        description: 'Mode 351: Rainbow appearing in mist',
        category: 'Scientific',
        mode: 351,
        tags: ["rainbow", "mist"],
        parameters: {
            rainbowLayers: { min: 5, max: 9, default: 7, label: 'Rainbow Layers' },
            arcRadius: { min: 0.5, max: 0.9, default: 0.7, label: 'Arc Radius' },
            mistDensity: { min: 0.5, max: 2, default: 1, label: 'Mist Density' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_352_geode_crystals: {
        id: 'mode_352_geode_crystals',
        name: 'Geode Crystals',
        description: 'Mode 352: Crystal formations inside geode',
        category: 'Nature',
        mode: 352,
        tags: ["geode", "crystals"],
        parameters: {
            crystalCount: { min: 16, max: 32, default: 24, label: 'Inner Crystals' },
            spikeLength: { min: 10, max: 30, default: 20, label: 'Crystal Spikes' },
            shellThickness: { min: 10, max: 30, default: 20, label: 'Geode Shell' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_353_snake_scales: {
        id: 'mode_353_snake_scales',
        name: 'Snake Scales',
        description: 'Mode 353: Snake skin scale pattern',
        category: 'Geometric',
        mode: 353,
        tags: ["snake", "scales"],
        parameters: {
            scaleSize: { min: 15, max: 30, default: 20, label: 'Scale Size' },
            scaleThreshold: { min: 0.15, max: 0.35, default: 0.2, label: 'Scale Threshold' },
            patternComplexity: { min: 4, max: 8, default: 6, label: 'Pattern Sides' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_354_whirlpool: {
        id: 'mode_354_whirlpool',
        name: 'Whirlpool',
        description: 'Mode 354: Water spiraling into whirlpool',
        category: 'Geometric',
        mode: 354,
        tags: ["whirlpool"],
        parameters: {
            spiralTurns: { min: 3, max: 6, default: 4, label: 'Spiral Turns' },
            rotationSpeed: { min: 0.05, max: 0.2, default: 0.1, label: 'Rotation Speed' },
            particleSize: { min: 2, max: 10, default: 5, label: 'Particle Size' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_355_owl_eyes: {
        id: 'mode_355_owl_eyes',
        name: 'Owl Eyes',
        description: 'Mode 355: Owl eyes blinking',
        category: 'Geometric',
        mode: 355,
        tags: ["eyes"],
        parameters: {
            eyeSize: { min: 30, max: 60, default: 40, label: 'Eye Size' },
            pupilDilation: { min: 0.5, max: 1.5, default: 1, label: 'Pupil Dilation' },
            blinkSpeed: { min: 0.5, max: 2, default: 1, label: 'Blink Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_356_tornado_funnel: {
        id: 'mode_356_tornado_funnel',
        name: 'Tornado Funnel',
        description: 'Mode 356: Tornado funnel with debris',
        category: 'Geometric',
        mode: 356,
        tags: ["tornado", "funnel"],
        parameters: {
            funnelWidth: { min: 30, max: 250, default: 140, label: 'Funnel Width' },
            debrisCount: { min: 20, max: 60, default: 40, label: 'Debris Count' },
            rotationSpeed: { min: 0.2, max: 0.5, default: 0.3, label: 'Rotation Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_357_peacock_feathers: {
        id: 'mode_357_peacock_feathers',
        name: 'Peacock Feathers',
        description: 'Mode 357: Peacock tail feather display',
        category: 'Geometric',
        mode: 357,
        tags: ["peacock", "feathers"],
        parameters: {
            featherCount: { min: 8, max: 16, default: 12, label: 'Feathers' },
            eyeSize: { min: 15, max: 35, default: 25, label: 'Eye Size' },
            spreadAmount: { min: 80, max: 250, default: 150, label: 'Spread Amount' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_358_jellyfish_pulse: {
        id: 'mode_358_jellyfish_pulse',
        name: 'Jellyfish Pulse',
        description: 'Mode 358: Jellyfish pulsating',
        category: 'Geometric',
        mode: 358,
        tags: ["jellyfish", "pulse"],
        parameters: {
            bellSize: { min: 60, max: 120, default: 80, label: 'Bell Size' },
            tentacleCount: { min: 6, max: 12, default: 8, label: 'Tentacles' },
            pulseSpeed: { min: 0.2, max: 0.5, default: 0.3, label: 'Pulse Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_359_sand_ripples: {
        id: 'mode_359_sand_ripples',
        name: 'Sand Ripples',
        description: 'Mode 359: Ripples in sand from wind',
        category: 'Geometric',
        mode: 359,
        tags: ["sand", "ripples"],
        parameters: {
            rippleRows: { min: 20, max: 40, default: 30, label: 'Ripple Rows' },
            rippleDepth: { min: 4, max: 12, default: 8, label: 'Ripple Depth' },
            wavelength: { min: 0.03, max: 0.08, default: 0.05, label: 'Wavelength' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_360_bat_swarm: {
        id: 'mode_360_bat_swarm',
        name: 'Bat Swarm',
        description: 'Birds/bats moving in murmuration patterns with flocking behavior',
        category: 'Particles',
        mode: 360,
        tags: ["swarm", "bat", "murmuration", "flocking", "particles", "glow"],
        parameters: {
            batCount: { min: 30, max: 100, default: 50, label: 'Bat Count' },
            swarmSpeed: { min: 0.05, max: 0.15, default: 0.08, label: 'Swarm Speed' },
            wingSpan: { min: 8, max: 16, default: 12, label: 'Wing Span' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' },
            trailLength: { min: 0, max: 0.5, default: 0.15, label: 'Motion Trail' },
            glowIntensity: { min: 0, max: 20, default: 8, label: 'Glow Intensity' }
        }
    },
    mode_361_tide_motion: {
        id: 'mode_361_tide_motion',
        name: 'Tide Motion',
        description: 'Mode 361: Tidal motion advancing and retreating',
        category: 'Geometric',
        mode: 361,
        tags: ["tide", "motion"],
        parameters: {
            tideCycle: { min: 0.03, max: 0.08, default: 0.05, label: 'Tide Cycle' },
            waveHeight: { min: 20, max: 40, default: 30, label: 'Wave Height' },
            foamThreshold: { min: 0.4, max: 0.7, default: 0.5, label: 'Foam Threshold' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_362_lichen_growth: {
        id: 'mode_362_lichen_growth',
        name: 'Lichen Growth',
        description: 'Mode 362: Lichen spreading on rock',
        category: 'Geometric',
        mode: 362,
        tags: ["lichen", "growth"],
        parameters: {
            colonyCount: { min: 100, max: 250, default: 150, label: 'Lichen Colonies' },
            growthRadius: { min: 5, max: 35, default: 20, label: 'Growth Radius' },
            density: { min: 15, max: 40, default: 25, label: 'Colony Density' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_363_eagle_soar: {
        id: 'mode_363_eagle_soar',
        name: 'Eagle Soar',
        description: 'Mode 363: Eagle soaring in thermals',
        category: 'Geometric',
        mode: 363,
        tags: ["eagle", "soar"],
        parameters: {
            thermalCount: { min: 2, max: 5, default: 3, label: 'Thermal Currents' },
            spiralTurns: { min: 15, max: 25, default: 20, label: 'Spiral Turns' },
            eagleSize: { min: 20, max: 35, default: 25, label: 'Eagle Size' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_364_mangrove_roots: {
        id: 'mode_364_mangrove_roots',
        name: 'Mangrove Roots',
        description: 'Mode 364: Mangrove root system',
        category: 'Geometric',
        mode: 364,
        tags: ["mangrove", "roots"],
        parameters: {
            rootCount: { min: 6, max: 15, default: 10, label: 'Root Arches' },
            archHeight: { min: 0.4, max: 0.8, default: 0.6, label: 'Arch Height' },
            curvature: { min: 30, max: 70, default: 50, label: 'Arch Curvature' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_365_aurora_waves: {
        id: 'mode_365_aurora_waves',
        name: 'Aurora Waves',
        description: 'Mode 365: Aurora borealis curtain waves',
        category: 'Nature',
        mode: 365,
        tags: ["aurora", "waves"],
        parameters: {
            auroraHeight: { min: 0.3, max: 0.7, default: 0.5, label: 'Aurora Height' },
            waveSpeed: { min: 0.05, max: 0.15, default: 0.1, label: 'Wave Speed' },
            layerDensity: { min: 3, max: 8, default: 5, label: 'Layer Density' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_366_dolphin_leap: {
        id: 'mode_366_dolphin_leap',
        name: 'Dolphin Leap',
        description: 'Mode 366: Dolphins leaping from water',
        category: 'Geometric',
        mode: 366,
        tags: ["dolphin", "leap"],
        parameters: {
            leapThreshold: { min: 0.4, max: 0.7, default: 0.5, label: 'Leap Threshold' },
            arcHeight: { min: 100, max: 250, default: 200, label: 'Leap Height' },
            splashSize: { min: 5, max: 15, default: 10, label: 'Splash Size' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_367_tumbleweed_roll: {
        id: 'mode_367_tumbleweed_roll',
        name: 'Tumbleweed Roll',
        description: 'Mode 367: Tumbleweed rolling across desert',
        category: 'Geometric',
        mode: 367,
        tags: ["tumbleweed", "roll"],
        parameters: {
            tumbleweedSize: { min: 30, max: 70, default: 50, label: 'Tumbleweed Size' },
            rollSpeed: { min: 2, max: 5, default: 3, label: 'Roll Speed' },
            branchDensity: { min: 15, max: 25, default: 20, label: 'Branch Density' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_368_coral_polyps: {
        id: 'mode_368_coral_polyps',
        name: 'Coral Polyps',
        description: 'Mode 368: Coral polyps extending tentacles',
        category: 'Nature',
        mode: 368,
        tags: ["coral", "polyps"],
        parameters: {
            polypCount: { min: 15, max: 30, default: 20, label: 'Polyp Count' },
            tentacleCount: { min: 6, max: 10, default: 8, label: 'Tentacles' },
            extendThreshold: { min: 0.25, max: 0.45, default: 0.3, label: 'Extend Threshold' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_369_smoke_wisps: {
        id: 'mode_369_smoke_wisps',
        name: 'Smoke Wisps',
        description: 'Mode 369: Smoke wisps rising',
        category: 'Geometric',
        mode: 369,
        tags: ["smoke", "wisps"],
        parameters: {
            wispCount: { min: 30, max: 100, default: 60, label: 'Smoke Wisps' },
            riseHeight: { min: 15, max: 25, default: 20, label: 'Rise Height' },
            driftAmount: { min: 15, max: 40, default: 30, label: 'Drift Amount' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_370_nautilus_shell: {
        id: 'mode_370_nautilus_shell',
        name: 'Nautilus Shell',
        description: 'Mode 370: Nautilus shell spiral',
        category: 'Geometric',
        mode: 370,
        tags: ["nautilus", "shell"],
        parameters: {
            spiralTurns: { min: 4, max: 8, default: 6, label: 'Spiral Turns' },
            chamberCount: { min: 6, max: 10, default: 8, label: 'Chamber Walls' },
            growthRate: { min: 0.1, max: 0.2, default: 0.15, label: 'Growth Rate' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_371_wolf_howl: {
        id: 'mode_371_wolf_howl',
        name: 'Wolf Howl',
        description: 'Mode 371: Wolf howling at moon with sound waves',
        category: 'Geometric',
        mode: 371,
        tags: ["wolf", "howl"],
        parameters: {
            moonSize: { min: 40, max: 70, default: 50, label: 'Moon Size' },
            howlThreshold: { min: 0.3, max: 0.6, default: 0.4, label: 'Howl Threshold' },
            waveCount: { min: 4, max: 7, default: 5, label: 'Sound Waves' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_372_seashell_patterns: {
        id: 'mode_372_seashell_patterns',
        name: 'Seashell Patterns',
        description: 'Mode 372: Various seashell patterns',
        category: 'Geometric',
        mode: 372,
        tags: ["seashell", "patterns"],
        parameters: {
            shellCount: { min: 6, max: 12, default: 8, label: 'Seashell Count' },
            spiralTurns: { min: 12, max: 20, default: 15, label: 'Spiral Turns' },
            patternSize: { min: 2, max: 5, default: 3, label: 'Pattern Size' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_373_grass_blades: {
        id: 'mode_373_grass_blades',
        name: 'Grass Blades',
        description: 'Mode 373: Individual grass blades swaying',
        category: 'Geometric',
        mode: 373,
        tags: ["grass", "blades"],
        parameters: {
            bladeCount: { min: 30, max: 70, default: 50, label: 'Grass Blades' },
            swayAmount: { min: 10, max: 30, default: 20, label: 'Sway Amount' },
            bladeLength: { min: 60, max: 120, default: 100, label: 'Blade Length' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_374_stalactites: {
        id: 'mode_374_stalactites',
        name: 'Stalactites',
        description: 'Mode 374: Cave stalactites and stalagmites',
        category: 'Geometric',
        mode: 374,
        tags: ["stalactites"],
        parameters: {
            stalactiteCount: { min: 10, max: 20, default: 15, label: 'Formations' },
            maxLength: { min: 100, max: 200, default: 150, label: 'Max Length' },
            formationWidth: { min: 10, max: 30, default: 20, label: 'Formation Width' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_375_amoeba_movement: {
        id: 'mode_375_amoeba_movement',
        name: 'Amoeba Movement',
        description: 'Mode 375: Amoeba-like organic movement',
        category: 'Geometric',
        mode: 375,
        tags: ["amoeba", "movement"],
        parameters: {
            pseudopodCount: { min: 15, max: 25, default: 20, label: 'Pseudopod Count' },
            blobSize: { min: 80, max: 150, default: 100, label: 'Blob Size' },
            movementSpeed: { min: 0.05, max: 0.15, default: 0.1, label: 'Movement Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_376_pine_needles: {
        id: 'mode_376_pine_needles',
        name: 'Pine Needles',
        description: 'Mode 376: Pine needle clusters',
        category: 'Geometric',
        mode: 376,
        tags: ["pine", "needles"],
        parameters: {
            clusterCount: { min: 8, max: 16, default: 12, label: 'Needle Clusters' },
            needlesPerCluster: { min: 6, max: 10, default: 8, label: 'Needles per Cluster' },
            needleLength: { min: 25, max: 50, default: 35, label: 'Needle Length' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_377_water_droplet: {
        id: 'mode_377_water_droplet',
        name: 'Water Droplet',
        description: 'Mode 377: Water droplet impact and splash',
        category: 'Fluid',
        mode: 377,
        tags: ["water", "droplet"],
        parameters: {
            dropletSize: { min: 3, max: 15, default: 8, label: 'Droplet Size' },
            dropFrequency: { min: 0.01, max: 0.3, default: 0.1, label: 'Drop Frequency' },
            splashIntensity: { min: 0.5, max: 2, default: 1, label: 'Splash Intensity' },
            rippleCount: { min: 3, max: 8, default: 5, label: 'Ripple Waves' },
            impactThreshold: { min: 0.2, max: 0.7, default: 0.4, label: 'Impact Threshold' },
            trailOpacity: { min: 0.02, max: 0.2, default: 0.08, label: 'Trail Fade' }
        }
    },
    mode_378_succulent_rosette: {
        id: 'mode_378_succulent_rosette',
        name: 'Succulent Rosette',
        description: 'Mode 378: Succulent plant rosette pattern',
        category: 'Geometric',
        mode: 378,
        tags: ["succulent", "rosette"],
        parameters: {
            layerCount: { min: 6, max: 10, default: 8, label: 'Rosette Layers' },
            leavesPerLayer: { min: 6, max: 12, default: 8, label: 'Leaves per Layer' },
            leafSize: { min: 12, max: 25, default: 18, label: 'Leaf Size' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_379_salmon_upstream: {
        id: 'mode_379_salmon_upstream',
        name: 'Salmon Upstream',
        description: 'Mode 379: Salmon swimming upstream',
        category: 'Geometric',
        mode: 379,
        tags: ["salmon", "upstream"],
        parameters: {
            salmonCount: { min: 4, max: 12, default: 8, label: 'Salmon Count' },
            swimSpeed: { min: 2, max: 5, default: 3, label: 'Swim Speed' },
            currentSpeed: { min: 3, max: 7, default: 5, label: 'Current Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_380_cloud_formation: {
        id: 'mode_380_cloud_formation',
        name: 'Cloud Formation',
        description: 'Mode 380: Clouds forming and dispersing',
        category: 'Geometric',
        mode: 380,
        tags: ["cloud", "formation"],
        parameters: {
            cloudLayers: { min: 2, max: 4, default: 3, label: 'Cloud Layers' },
            puffiness: { min: 5, max: 15, default: 10, label: 'Puffiness' },
            cloudSize: { min: 10, max: 30, default: 20, label: 'Cloud Size' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_381_fox_tail: {
        id: 'mode_381_fox_tail',
        name: 'Fox Tail',
        description: 'Mode 381: Fox tail swishing',
        category: 'Scientific',
        mode: 381,
        tags: ["tail"],
        parameters: {
            tailSegments: { min: 15, max: 25, default: 20, label: 'Tail Segments' },
            swishSpeed: { min: 0.1, max: 0.25, default: 0.15, label: 'Swish Speed' },
            tailLength: { min: 150, max: 250, default: 200, label: 'Tail Length' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_382_clover_field: {
        id: 'mode_382_clover_field',
        name: 'Clover Field',
        description: 'Mode 382: Field of four-leaf clovers',
        category: 'Geometric',
        mode: 382,
        tags: ["clover", "field"],
        parameters: {
            cloverCount: { min: 25, max: 60, default: 40, label: 'Clover Count' },
            leafSize: { min: 5, max: 12, default: 8, label: 'Leaf Size' },
            cloverThreshold: { min: 0.15, max: 0.35, default: 0.2, label: 'Growth Threshold' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_383_geyser_field: {
        id: 'mode_383_geyser_field',
        name: 'Geyser Field',
        description: 'Mode 383: Multiple geysers erupting',
        category: 'Geometric',
        mode: 383,
        tags: ["geyser", "field"],
        parameters: {
            geyserCount: { min: 5, max: 20, default: 10, label: 'Geyser Count' },
            eruptionThreshold: { min: 0.4, max: 0.7, default: 0.5, label: 'Eruption Threshold' },
            plumeHeight: { min: 150, max: 250, default: 200, label: 'Plume Height' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_384_insect_compound_eye: {
        id: 'mode_384_insect_compound_eye',
        name: 'Insect Compound Eye',
        description: 'Mode 384: Compound eye of an insect',
        category: 'Geometric',
        mode: 384,
        tags: ["insect", "compound"],
        parameters: {
            hexSize: { min: 8, max: 18, default: 12, label: 'Facet Size' },
            curvatureRadius: { min: 0.6, max: 1, default: 0.8, label: 'Eye Curvature' },
            facetBrightness: { min: 0.5, max: 2, default: 1, label: 'Facet Brightness' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_385_moonflower_bloom: {
        id: 'mode_385_moonflower_bloom',
        name: 'Moonflower Bloom',
        description: 'Mode 385: Moonflower blooming at night',
        category: 'Nature',
        mode: 385,
        tags: ["moonflower", "bloom"],
        parameters: {
            petalCount: { min: 5, max: 8, default: 6, label: 'Petal Count' },
            bloomSpeed: { min: 0.5, max: 2, default: 1, label: 'Bloom Speed' },
            petalLength: { min: 60, max: 120, default: 90, label: 'Petal Length' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_386_sand_dollar: {
        id: 'mode_386_sand_dollar',
        name: 'Sand Dollar',
        description: 'Mode 386: Sand dollar pattern',
        category: 'Geometric',
        mode: 386,
        tags: ["sand", "dollar"],
        parameters: {
            petalSlots: { min: 4, max: 6, default: 5, label: 'Petal Slots' },
            slotDepth: { min: 15, max: 35, default: 25, label: 'Slot Depth' },
            dollarSize: { min: 0.3, max: 0.7, default: 0.5, label: 'Dollar Size' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_387_glacier_crevasse: {
        id: 'mode_387_glacier_crevasse',
        name: 'Glacier Crevasse',
        description: 'Mode 387: Deep crevasse in glacier',
        category: 'Geometric',
        mode: 387,
        tags: ["glacier", "crevasse"],
        parameters: {
            crevasseDepth: { min: 0.8, max: 1, default: 0.9, label: 'Crevasse Depth' },
            wallRoughness: { min: 0.3, max: 0.8, default: 0.5, label: 'Wall Roughness' },
            iceGradient: { min: 50, max: 150, default: 100, label: 'Ice Gradient' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_388_antler_growth: {
        id: 'mode_388_antler_growth',
        name: 'Antler Growth',
        description: 'Mode 388: Deer antler branching pattern',
        category: 'Geometric',
        mode: 388,
        tags: ["antler", "growth"],
        parameters: {
            branchDepth: { min: 4, max: 7, default: 5, label: 'Branch Depth' },
            antlerSize: { min: 30, max: 50, default: 40, label: 'Antler Size' },
            branchAngle: { min: 20, max: 40, default: 30, label: 'Branch Angle' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_389_plume_worm: {
        id: 'mode_389_plume_worm',
        name: 'Plume Worm',
        description: 'Mode 389: Feather duster worm plume',
        category: 'Geometric',
        mode: 389,
        tags: ["plume", "worm"],
        parameters: {
            filamentCount: { min: 18, max: 32, default: 24, label: 'Filament Count' },
            plumeLength: { min: 60, max: 140, default: 100, label: 'Plume Length' },
            curvature: { min: 15, max: 25, default: 20, label: 'Filament Curve' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_390_reed_marsh: {
        id: 'mode_390_reed_marsh',
        name: 'Reed Marsh',
        description: 'Mode 390: Reeds swaying in marsh',
        category: 'Geometric',
        mode: 390,
        tags: ["reed", "marsh"],
        parameters: {
            reedCount: { min: 20, max: 40, default: 30, label: 'Reed Count' },
            reedHeight: { min: 120, max: 250, default: 180, label: 'Reed Height' },
            swayAmount: { min: 15, max: 40, default: 30, label: 'Sway Amount' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_391_beetle_shell: {
        id: 'mode_391_beetle_shell',
        name: 'Beetle Shell',
        description: 'Mode 391: Iridescent beetle shell pattern',
        category: 'Geometric',
        mode: 391,
        tags: ["beetle", "shell"],
        parameters: {
            spotCount: { min: 30, max: 90, default: 60, label: 'Iridescent Spots' },
            shellSize: { min: 0.4, max: 0.8, default: 0.6, label: 'Shell Size' },
            colorShift: { min: 10, max: 25, default: 15, label: 'Color Shift Speed' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_392_tide_anemone: {
        id: 'mode_392_tide_anemone',
        name: 'Tide Anemone',
        description: 'Mode 392: Sea anemone in tidal zone',
        category: 'Geometric',
        mode: 392,
        tags: ["tide", "anemone"],
        parameters: {
            tentacleCount: { min: 15, max: 28, default: 20, label: 'Tentacles' },
            tentacleLength: { min: 50, max: 120, default: 80, label: 'Tentacle Length' },
            waveIntensity: { min: 0.5, max: 2, default: 1, label: 'Wave Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_393_earthquake_waves: {
        id: 'mode_393_earthquake_waves',
        name: 'Earthquake Waves',
        description: 'Mode 393: Seismic waves propagating',
        category: 'Geometric',
        mode: 393,
        tags: ["earthquake", "waves"],
        parameters: {
            waveCount: { min: 6, max: 12, default: 8, label: 'Wave Count' },
            waveSpeed: { min: 2, max: 4, default: 3, label: 'Wave Speed' },
            displacementAmount: { min: 15, max: 40, default: 30, label: 'Ground Displacement' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_394_butterfly_lifecycle: {
        id: 'mode_394_butterfly_lifecycle',
        name: 'Butterfly Lifecycle',
        description: 'Mode 394: Butterfly metamorphosis stages',
        category: 'Geometric',
        mode: 394,
        tags: ["butterfly", "lifecycle"],
        parameters: {
            stageSpeed: { min: 0.5, max: 2, default: 1, label: 'Stage Speed' },
            segmentCount: { min: 6, max: 10, default: 8, label: 'Caterpillar Segments' },
            wingSize: { min: 40, max: 70, default: 50, label: 'Butterfly Wing Size' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_395_coconut_palm: {
        id: 'mode_395_coconut_palm',
        name: 'Coconut Palm',
        description: 'Mode 395: Palm tree with coconuts',
        category: 'Geometric',
        mode: 395,
        tags: ["coconut", "palm"],
        parameters: {
            frondCount: { min: 6, max: 12, default: 8, label: 'Palm Fronds' },
            frondLength: { min: 80, max: 160, default: 120, label: 'Frond Length' },
            coconutCount: { min: 3, max: 6, default: 4, label: 'Coconuts' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_396_frost_ferns: {
        id: 'mode_396_frost_ferns',
        name: 'Frost Ferns',
        description: 'Mode 396: Frost fern patterns on window',
        category: 'Geometric',
        mode: 396,
        tags: ["frost", "ferns"],
        parameters: {
            fernCount: { min: 4, max: 8, default: 6, label: 'Frost Ferns' },
            branchDepth: { min: 5, max: 8, default: 6, label: 'Branch Depth' },
            branchAngle: { min: 35, max: 55, default: 45, label: 'Branch Angle' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_397_bioluminescent_bay: {
        id: 'mode_397_bioluminescent_bay',
        name: 'Bioluminescent Bay',
        description: 'Mode 397: Bioluminescent organisms in bay',
        category: 'Geometric',
        mode: 397,
        tags: ["bioluminescent"],
        parameters: {
            glowCount: { min: 60, max: 180, default: 120, label: 'Glow Organisms' },
            glowSize: { min: 4, max: 18, default: 10, label: 'Glow Size' },
            waveAmplitude: { min: 0.2, max: 0.5, default: 0.3, label: 'Wave Amplitude' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_398_erosion_patterns: {
        id: 'mode_398_erosion_patterns',
        name: 'Erosion Patterns',
        description: 'Mode 398: Water erosion creating patterns',
        category: 'Geometric',
        mode: 398,
        tags: ["erosion", "patterns"],
        parameters: {
            channelCount: { min: 6, max: 12, default: 8, label: 'Erosion Channels' },
            meanderAmount: { min: 30, max: 70, default: 50, label: 'Meander Amount' },
            channelWidth: { min: 4, max: 12, default: 8, label: 'Channel Width' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_399_hedge_maze: {
        id: 'mode_399_hedge_maze',
        name: 'Hedge Maze',
        description: 'Mode 399: Hedge maze from above',
        category: 'Geometric',
        mode: 399,
        tags: ["hedge", "maze"],
        parameters: {
            cellSize: { min: 30, max: 50, default: 40, label: 'Maze Cell Size' },
            wallThreshold: { min: 0.25, max: 0.75, default: 0.5, label: 'Wall Density' },
            wallThickness: { min: 4, max: 8, default: 5, label: 'Wall Thickness' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_400_water_lily_reflection: {
        id: 'mode_400_water_lily_reflection',
        name: 'Water Lily Reflection',
        description: 'Mode 400: Water lily with mirror reflection',
        category: 'Fluid',
        mode: 400,
        tags: ["water", "lily", "reflection"],
        parameters: {
            petalCount: { min: 6, max: 12, default: 8, label: 'Lily Petals' },
            reflectionClarity: { min: 0.5, max: 1, default: 0.7, label: 'Reflection Clarity' },
            rippleCount: { min: 4, max: 8, default: 5, label: 'Water Ripples' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_401_atom_model: {
        id: 'mode_401_atom_model',
        name: 'Atom Model',
        description: 'Mode 401: Atomic orbital model with electrons',
        category: 'Scientific',
        mode: 401,
        tags: ["atom", "model"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_402_double_helix: {
        id: 'mode_402_double_helix',
        name: 'Double Helix',
        description: 'Mode 402: DNA double helix structure',
        category: 'Geometric',
        mode: 402,
        tags: ["double", "helix"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_403_magnetic_field: {
        id: 'mode_403_magnetic_field',
        name: 'Magnetic Field',
        description: 'Mode 403: Magnetic field lines',
        category: 'Scientific',
        mode: 403,
        tags: ["magnetic", "field"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_404_wave_interference: {
        id: 'mode_404_wave_interference',
        name: 'Wave Interference',
        description: 'Mode 404: Wave interference patterns',
        category: 'Geometric',
        mode: 404,
        tags: ["wave", "interference"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_405_particle_accelerator: {
        id: 'mode_405_particle_accelerator',
        name: 'Particle Accelerator',
        description: 'Mode 405: Particle accelerator ring',
        category: 'Particles',
        mode: 405,
        tags: ["particle", "accelerator"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_406_crystal_lattice: {
        id: 'mode_406_crystal_lattice',
        name: 'Crystal Lattice',
        description: 'Mode 406: 3D crystal lattice structure',
        category: 'Nature',
        mode: 406,
        tags: ["crystal", "lattice"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_407_electromagnetic_wave: {
        id: 'mode_407_electromagnetic_wave',
        name: 'Electromagnetic Wave',
        description: 'Mode 407: Electromagnetic wave propagation',
        category: 'Scientific',
        mode: 407,
        tags: ["electromagnetic", "wave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_408_quantum_tunneling: {
        id: 'mode_408_quantum_tunneling',
        name: 'Quantum Tunneling',
        description: 'Mode 408: Quantum tunneling through barrier',
        category: 'Scientific',
        mode: 408,
        tags: ["quantum", "tunneling"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_409_fission_reaction: {
        id: 'mode_409_fission_reaction',
        name: 'Fission Reaction',
        description: 'Mode 409: Nuclear fission chain reaction',
        category: 'Geometric',
        mode: 409,
        tags: ["fission", "reaction"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_410_doppler_effect: {
        id: 'mode_410_doppler_effect',
        name: 'Doppler Effect',
        description: 'Mode 410: Doppler effect wave compression',
        category: 'Geometric',
        mode: 410,
        tags: ["doppler", "effect"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_411_gravity_well: {
        id: 'mode_411_gravity_well',
        name: 'Gravity Well',
        description: 'Mode 411: Gravitational well spacetime curvature',
        category: 'Geometric',
        mode: 411,
        tags: ["gravity", "well"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_412_prism_spectrum: {
        id: 'mode_412_prism_spectrum',
        name: 'Prism Spectrum',
        description: 'Mode 412: Light dispersing through prism',
        category: 'Geometric',
        mode: 412,
        tags: ["prism", "spectrum"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_413_molecular_bonds: {
        id: 'mode_413_molecular_bonds',
        name: 'Molecular Bonds',
        description: 'Mode 413: Molecular bonding and vibration',
        category: 'Geometric',
        mode: 413,
        tags: ["molecular", "bonds"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_414_standing_wave: {
        id: 'mode_414_standing_wave',
        name: 'Standing Wave',
        description: 'Mode 414: Standing wave with nodes and antinodes',
        category: 'Geometric',
        mode: 414,
        tags: ["standing", "wave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_415_brownian_motion: {
        id: 'mode_415_brownian_motion',
        name: 'Brownian Motion',
        description: 'Mode 415: Brownian motion of particles',
        category: 'Geometric',
        mode: 415,
        tags: ["brownian", "motion"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_416_tesla_coil: {
        id: 'mode_416_tesla_coil',
        name: 'Tesla Coil',
        description: 'Mode 416: Tesla coil electric arcs',
        category: 'Geometric',
        mode: 416,
        tags: ["tesla", "coil"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_417_phase_transition: {
        id: 'mode_417_phase_transition',
        name: 'Phase Transition',
        description: 'Mode 417: Phase transition (solid/liquid/gas)',
        category: 'Geometric',
        mode: 417,
        tags: ["phase", "transition"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_418_superconductor: {
        id: 'mode_418_superconductor',
        name: 'Superconductor',
        description: 'Mode 418: Superconductor Meissner effect',
        category: 'Geometric',
        mode: 418,
        tags: ["superconductor"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_419_neuron_firing: {
        id: 'mode_419_neuron_firing',
        name: 'Neuron Firing',
        description: 'Mode 419: Neuron action potential firing',
        category: 'Geometric',
        mode: 419,
        tags: ["neuron", "firing"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_420_resonance_modes: {
        id: 'mode_420_resonance_modes',
        name: 'Resonance Modes',
        description: 'Mode 420: Resonance modes of vibrating plate',
        category: 'Geometric',
        mode: 420,
        tags: ["resonance", "modes"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_421_fractal_diffusion: {
        id: 'mode_421_fractal_diffusion',
        name: 'Fractal Diffusion',
        description: 'Mode 421: Diffusion-limited aggregation',
        category: 'Geometric',
        mode: 421,
        tags: ["fractal", "diffusion"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_422_plasma_ball: {
        id: 'mode_422_plasma_ball',
        name: 'Plasma Ball',
        description: 'Mode 422: Plasma ball electric tendrils',
        category: 'Energy',
        mode: 422,
        tags: ["plasma", "ball"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_423_coriolis_effect: {
        id: 'mode_423_coriolis_effect',
        name: 'Coriolis Effect',
        description: 'Mode 423: Coriolis effect on rotating frame',
        category: 'Geometric',
        mode: 423,
        tags: ["coriolis", "effect"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_424_photoelectric_effect: {
        id: 'mode_424_photoelectric_effect',
        name: 'Photoelectric Effect',
        description: 'Mode 424: Photoelectric effect electron emission',
        category: 'Geometric',
        mode: 424,
        tags: ["photoelectric", "effect"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_425_lorenz_attractor: {
        id: 'mode_425_lorenz_attractor',
        name: 'Lorenz Attractor',
        description: 'Mode 425: Lorenz attractor chaos theory',
        category: 'Geometric',
        mode: 425,
        tags: ["lorenz", "attractor"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_426_spin_precession: {
        id: 'mode_426_spin_precession',
        name: 'Spin Precession',
        description: 'Mode 426: Quantum spin precession',
        category: 'Geometric',
        mode: 426,
        tags: ["spin", "precession"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_427_compton_scattering: {
        id: 'mode_427_compton_scattering',
        name: 'Compton Scattering',
        description: 'Mode 427: Compton scattering of photons',
        category: 'Geometric',
        mode: 427,
        tags: ["compton", "scattering"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_428_ferrofluid: {
        id: 'mode_428_ferrofluid',
        name: 'Ferrofluid',
        description: 'Mode 428: Ferrofluid spikes in magnetic field',
        category: 'Fluid',
        mode: 428,
        tags: ["ferrofluid"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_429_sonoluminescence: {
        id: 'mode_429_sonoluminescence',
        name: 'Sonoluminescence',
        description: 'Mode 429: Sonoluminescence bubble collapse',
        category: 'Geometric',
        mode: 429,
        tags: ["sonoluminescence"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_430_cherenkov_radiation: {
        id: 'mode_430_cherenkov_radiation',
        name: 'Cherenkov Radiation',
        description: 'Mode 430: Cherenkov radiation cone',
        category: 'Geometric',
        mode: 430,
        tags: ["cherenkov", "radiation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_431_hall_effect: {
        id: 'mode_431_hall_effect',
        name: 'Hall Effect',
        description: 'Mode 431: Hall effect charge separation',
        category: 'Geometric',
        mode: 431,
        tags: ["hall", "effect"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_432_cymatics: {
        id: 'mode_432_cymatics',
        name: 'Cymatics',
        description: 'Mode 432: Cymatic patterns from sound',
        category: 'Geometric',
        mode: 432,
        tags: ["cymatics"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_433_klein_bottle: {
        id: 'mode_433_klein_bottle',
        name: 'Klein Bottle',
        description: 'Mode 433: Klein bottle topology',
        category: 'Geometric',
        mode: 433,
        tags: ["klein", "bottle"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_434_raman_scattering: {
        id: 'mode_434_raman_scattering',
        name: 'Raman Scattering',
        description: 'Mode 434: Raman spectroscopy energy levels',
        category: 'Geometric',
        mode: 434,
        tags: ["raman", "scattering"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_435_vortex_shedding: {
        id: 'mode_435_vortex_shedding',
        name: 'Vortex Shedding',
        description: 'Mode 435: Von Kármán vortex street',
        category: 'Geometric',
        mode: 435,
        tags: ["vortex", "shedding"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_436_polarization: {
        id: 'mode_436_polarization',
        name: 'Polarization',
        description: 'Mode 436: Light polarization through filters',
        category: 'Geometric',
        mode: 436,
        tags: ["polarization"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_437_higgs_field: {
        id: 'mode_437_higgs_field',
        name: 'Higgs Field',
        description: 'Mode 437: Higgs field giving mass to particles',
        category: 'Geometric',
        mode: 437,
        tags: ["higgs", "field"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_438_bose_einstein: {
        id: 'mode_438_bose_einstein',
        name: 'Bose Einstein',
        description: 'Mode 438: Bose-Einstein condensate formation',
        category: 'Geometric',
        mode: 438,
        tags: ["bose", "einstein"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_439_schrodinger_cat: {
        id: 'mode_439_schrodinger_cat',
        name: 'Schrodinger Cat',
        description: 'Mode 439: Schrodinger cat superposition',
        category: 'Geometric',
        mode: 439,
        tags: ["schrodinger"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_440_string_vibration: {
        id: 'mode_440_string_vibration',
        name: 'String Vibration',
        description: 'Mode 440: Vibrating string harmonics',
        category: 'Geometric',
        mode: 440,
        tags: ["string", "vibration"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_441_electron_cloud: {
        id: 'mode_441_electron_cloud',
        name: 'Electron Cloud',
        description: 'Mode 441: Electron probability cloud',
        category: 'Geometric',
        mode: 441,
        tags: ["electron", "cloud"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_442_thermoelectric: {
        id: 'mode_442_thermoelectric',
        name: 'Thermoelectric',
        description: 'Mode 442: Thermoelectric Seebeck effect',
        category: 'Geometric',
        mode: 442,
        tags: ["thermoelectric"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_443_photon_entanglement: {
        id: 'mode_443_photon_entanglement',
        name: 'Photon Entanglement',
        description: 'Mode 443: Quantum entangled photon pairs',
        category: 'Geometric',
        mode: 443,
        tags: ["photon", "entanglement"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_444_superfluidity: {
        id: 'mode_444_superfluidity',
        name: 'Superfluidity',
        description: 'Mode 444: Superfluid helium climbing walls',
        category: 'Fluid',
        mode: 444,
        tags: ["superfluidity"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_445_piezoelectric: {
        id: 'mode_445_piezoelectric',
        name: 'Piezoelectric',
        description: 'Mode 445: Piezoelectric crystal stress/voltage',
        category: 'Geometric',
        mode: 445,
        tags: ["piezoelectric"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_446_zeeman_effect: {
        id: 'mode_446_zeeman_effect',
        name: 'Zeeman Effect',
        description: 'Mode 446: Zeeman effect spectral line splitting',
        category: 'Geometric',
        mode: 446,
        tags: ["zeeman", "effect"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_447_cyclotron_motion: {
        id: 'mode_447_cyclotron_motion',
        name: 'Cyclotron Motion',
        description: 'Mode 447: Charged particle in magnetic field',
        category: 'Geometric',
        mode: 447,
        tags: ["cyclotron", "motion"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_448_fusion_reactor: {
        id: 'mode_448_fusion_reactor',
        name: 'Fusion Reactor',
        description: 'Mode 448: Tokamak fusion reactor plasma',
        category: 'Geometric',
        mode: 448,
        tags: ["fusion", "reactor"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_449_antimatter: {
        id: 'mode_449_antimatter',
        name: 'Antimatter',
        description: 'Mode 449: Matter-antimatter annihilation',
        category: 'Geometric',
        mode: 449,
        tags: ["antimatter"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_450_hawking_radiation: {
        id: 'mode_450_hawking_radiation',
        name: 'Hawking Radiation',
        description: 'Mode 450: Black hole Hawking radiation',
        category: 'Geometric',
        mode: 450,
        tags: ["hawking", "radiation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_451_heisenberg_uncertainty: {
        id: 'mode_451_heisenberg_uncertainty',
        name: 'Heisenberg Uncertainty',
        description: 'Mode 451: Heisenberg uncertainty principle visualization',
        category: 'Scientific',
        mode: 451,
        tags: ["heisenberg", "uncertainty"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_452_particle_decay: {
        id: 'mode_452_particle_decay',
        name: 'Particle Decay',
        description: 'Mode 452: Radioactive particle decay chain',
        category: 'Particles',
        mode: 452,
        tags: ["particle", "decay"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_453_laser_cavity: {
        id: 'mode_453_laser_cavity',
        name: 'Laser Cavity',
        description: 'Mode 453: Laser optical cavity resonance',
        category: 'Geometric',
        mode: 453,
        tags: ["laser", "cavity"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_454_dielectric_breakdown: {
        id: 'mode_454_dielectric_breakdown',
        name: 'Dielectric Breakdown',
        description: 'Mode 454: Electric breakdown in dielectric',
        category: 'Geometric',
        mode: 454,
        tags: ["dielectric", "breakdown"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_455_casimir_effect: {
        id: 'mode_455_casimir_effect',
        name: 'Casimir Effect',
        description: 'Mode 455: Casimir effect between plates',
        category: 'Geometric',
        mode: 455,
        tags: ["casimir", "effect"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_456_sonochemistry: {
        id: 'mode_456_sonochemistry',
        name: 'Sonochemistry',
        description: 'Mode 456: Sonochemistry cavitation bubbles',
        category: 'Geometric',
        mode: 456,
        tags: ["sonochemistry"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_457_phonon_propagation: {
        id: 'mode_457_phonon_propagation',
        name: 'Phonon Propagation',
        description: 'Mode 457: Phonons in crystal lattice',
        category: 'Geometric',
        mode: 457,
        tags: ["phonon", "propagation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_458_pair_production: {
        id: 'mode_458_pair_production',
        name: 'Pair Production',
        description: 'Mode 458: Photon pair production',
        category: 'Scientific',
        mode: 458,
        tags: ["pair", "production"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_459_stefan_boltzmann: {
        id: 'mode_459_stefan_boltzmann',
        name: 'Stefan Boltzmann',
        description: 'Mode 459: Stefan-Boltzmann radiation law',
        category: 'Geometric',
        mode: 459,
        tags: ["stefan", "boltzmann"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_460_eddy_currents: {
        id: 'mode_460_eddy_currents',
        name: 'Eddy Currents',
        description: 'Mode 460: Eddy currents in conductor',
        category: 'Geometric',
        mode: 460,
        tags: ["eddy", "currents"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_461_wavefunction_collapse: {
        id: 'mode_461_wavefunction_collapse',
        name: 'Wavefunction Collapse',
        description: 'Mode 461: Quantum wavefunction collapse on measurement',
        category: 'Geometric',
        mode: 461,
        tags: ["wavefunction", "collapse"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_462_qed_feynman: {
        id: 'mode_462_qed_feynman',
        name: 'Qed Feynman',
        description: 'Mode 462: QED Feynman diagram',
        category: 'Geometric',
        mode: 462,
        tags: ["feynman"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_463_holography: {
        id: 'mode_463_holography',
        name: 'Holography',
        description: 'Mode 463: Holographic interference pattern',
        category: 'Geometric',
        mode: 463,
        tags: ["holography"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_464_metamaterial: {
        id: 'mode_464_metamaterial',
        name: 'Metamaterial',
        description: 'Mode 464: Metamaterial negative refraction',
        category: 'Geometric',
        mode: 464,
        tags: ["metamaterial"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_465_photodiode: {
        id: 'mode_465_photodiode',
        name: 'Photodiode',
        description: 'Mode 465: Photodiode photocurrent generation',
        category: 'Geometric',
        mode: 465,
        tags: ["photodiode"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_466_bremsstrahlung: {
        id: 'mode_466_bremsstrahlung',
        name: 'Bremsstrahlung',
        description: 'Mode 466: Bremsstrahlung X-ray emission',
        category: 'Geometric',
        mode: 466,
        tags: ["bremsstrahlung"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_467_optogenetics: {
        id: 'mode_467_optogenetics',
        name: 'Optogenetics',
        description: 'Mode 467: Optogenetics light-controlled neurons',
        category: 'Geometric',
        mode: 467,
        tags: ["optogenetics"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_468_topological_insulator: {
        id: 'mode_468_topological_insulator',
        name: 'Topological Insulator',
        description: 'Mode 468: Topological insulator edge states',
        category: 'Geometric',
        mode: 468,
        tags: ["topological", "insulator"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_469_nernst_equation: {
        id: 'mode_469_nernst_equation',
        name: 'Nernst Equation',
        description: 'Mode 469: Nernst equation ion concentration',
        category: 'Geometric',
        mode: 469,
        tags: ["nernst", "equation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_470_mri_precession: {
        id: 'mode_470_mri_precession',
        name: 'Mri Precession',
        description: 'Mode 470: MRI nuclear magnetic resonance',
        category: 'Geometric',
        mode: 470,
        tags: ["precession"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_471_josephson_junction: {
        id: 'mode_471_josephson_junction',
        name: 'Josephson Junction',
        description: 'Mode 471: Josephson junction supercurrent',
        category: 'Geometric',
        mode: 471,
        tags: ["josephson", "junction"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_472_liquid_crystal: {
        id: 'mode_472_liquid_crystal',
        name: 'Liquid Crystal',
        description: 'Mode 472: Liquid crystal alignment',
        category: 'Nature',
        mode: 472,
        tags: ["liquid", "crystal"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_473_rydberg_atoms: {
        id: 'mode_473_rydberg_atoms',
        name: 'Rydberg Atoms',
        description: 'Mode 473: Rydberg atoms with large orbitals',
        category: 'Scientific',
        mode: 473,
        tags: ["rydberg", "atoms"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_474_cavity_qed: {
        id: 'mode_474_cavity_qed',
        name: 'Cavity Qed',
        description: 'Mode 474: Cavity QED atom-photon coupling',
        category: 'Geometric',
        mode: 474,
        tags: ["cavity"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_475_quantum_dots: {
        id: 'mode_475_quantum_dots',
        name: 'Quantum Dots',
        description: 'Mode 475: Quantum dots emission',
        category: 'Scientific',
        mode: 475,
        tags: ["quantum", "dots"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_476_soliton_wave: {
        id: 'mode_476_soliton_wave',
        name: 'Soliton Wave',
        description: 'Mode 476: Soliton solitary wave',
        category: 'Geometric',
        mode: 476,
        tags: ["soliton", "wave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_477_acoustic_levitation: {
        id: 'mode_477_acoustic_levitation',
        name: 'Acoustic Levitation',
        description: 'Mode 477: Acoustic levitation standing wave',
        category: 'Geometric',
        mode: 477,
        tags: ["acoustic", "levitation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_478_mosfet_channel: {
        id: 'mode_478_mosfet_channel',
        name: 'Mosfet Channel',
        description: 'Mode 478: MOSFET inversion channel',
        category: 'Geometric',
        mode: 478,
        tags: ["mosfet", "channel"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_479_spintronics: {
        id: 'mode_479_spintronics',
        name: 'Spintronics',
        description: 'Mode 479: Spintronics spin current',
        category: 'Geometric',
        mode: 479,
        tags: ["spintronics"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_480_electrochemistry: {
        id: 'mode_480_electrochemistry',
        name: 'Electrochemistry',
        description: 'Mode 480: Electrochemical cell redox reaction',
        category: 'Geometric',
        mode: 480,
        tags: ["electrochemistry"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_481_langmuir_wave: {
        id: 'mode_481_langmuir_wave',
        name: 'Langmuir Wave',
        description: 'Mode 481: Langmuir plasma oscillations',
        category: 'Geometric',
        mode: 481,
        tags: ["langmuir", "wave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_482_bloch_sphere: {
        id: 'mode_482_bloch_sphere',
        name: 'Bloch Sphere',
        description: 'Mode 482: Bloch sphere qubit state',
        category: 'Geometric',
        mode: 482,
        tags: ["bloch", "sphere"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_483_curie_temperature: {
        id: 'mode_483_curie_temperature',
        name: 'Curie Temperature',
        description: 'Mode 483: Curie temperature magnetic ordering',
        category: 'Geometric',
        mode: 483,
        tags: ["curie", "temperature"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_484_dyson_sphere: {
        id: 'mode_484_dyson_sphere',
        name: 'Dyson Sphere',
        description: 'Mode 484: Dyson sphere energy collection',
        category: 'Geometric',
        mode: 484,
        tags: ["dyson", "sphere"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_485_graphene_lattice: {
        id: 'mode_485_graphene_lattice',
        name: 'Graphene Lattice',
        description: 'Mode 485: Graphene hexagonal lattice',
        category: 'Geometric',
        mode: 485,
        tags: ["graphene", "lattice"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_486_memristor: {
        id: 'mode_486_memristor',
        name: 'Memristor',
        description: 'Mode 486: Memristor resistance switching',
        category: 'Geometric',
        mode: 486,
        tags: ["memristor"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_487_quantum_hall: {
        id: 'mode_487_quantum_hall',
        name: 'Quantum Hall',
        description: 'Mode 487: Quantum Hall effect edge states',
        category: 'Scientific',
        mode: 487,
        tags: ["quantum", "hall"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_488_optomechanics: {
        id: 'mode_488_optomechanics',
        name: 'Optomechanics',
        description: 'Mode 488: Cavity optomechanics',
        category: 'Geometric',
        mode: 488,
        tags: ["optomechanics"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_489_exciton: {
        id: 'mode_489_exciton',
        name: 'Exciton',
        description: 'Mode 489: Exciton electron-hole pair',
        category: 'Geometric',
        mode: 489,
        tags: ["exciton"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_490_photonic_crystal: {
        id: 'mode_490_photonic_crystal',
        name: 'Photonic Crystal',
        description: 'Mode 490: Photonic crystal band gap',
        category: 'Nature',
        mode: 490,
        tags: ["photonic", "crystal"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_491_skyrmion: {
        id: 'mode_491_skyrmion',
        name: 'Skyrmion',
        description: 'Mode 491: Magnetic skyrmion texture',
        category: 'Geometric',
        mode: 491,
        tags: ["skyrmion"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_492_mott_insulator: {
        id: 'mode_492_mott_insulator',
        name: 'Mott Insulator',
        description: 'Mode 492: Mott insulator transition',
        category: 'Geometric',
        mode: 492,
        tags: ["mott", "insulator"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_493_squeezing: {
        id: 'mode_493_squeezing',
        name: 'Squeezing',
        description: 'Mode 493: Quantum squeezing uncertainty',
        category: 'Geometric',
        mode: 493,
        tags: ["squeezing"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_494_andreev_reflection: {
        id: 'mode_494_andreev_reflection',
        name: 'Andreev Reflection',
        description: 'Mode 494: Andreev reflection at NS interface',
        category: 'Geometric',
        mode: 494,
        tags: ["andreev", "reflection"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_495_casimir_polder: {
        id: 'mode_495_casimir_polder',
        name: 'Casimir Polder',
        description: 'Mode 495: Casimir-Polder force on atom',
        category: 'Geometric',
        mode: 495,
        tags: ["casimir", "polder"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_496_fano_resonance: {
        id: 'mode_496_fano_resonance',
        name: 'Fano Resonance',
        description: 'Mode 496: Fano resonance asymmetric lineshape',
        category: 'Geometric',
        mode: 496,
        tags: ["fano", "resonance"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_497_quantum_zeno: {
        id: 'mode_497_quantum_zeno',
        name: 'Quantum Zeno',
        description: 'Mode 497: Quantum Zeno effect frequent measurement',
        category: 'Scientific',
        mode: 497,
        tags: ["quantum", "zeno"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_498_rabi_oscillation: {
        id: 'mode_498_rabi_oscillation',
        name: 'Rabi Oscillation',
        description: 'Mode 498: Rabi oscillation between states',
        category: 'Geometric',
        mode: 498,
        tags: ["rabi", "oscillation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_499_aharonov_bohm: {
        id: 'mode_499_aharonov_bohm',
        name: 'Aharonov Bohm',
        description: 'Mode 499: Aharonov-Bohm effect phase shift',
        category: 'Geometric',
        mode: 499,
        tags: ["aharonov", "bohm"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_500_berry_phase: {
        id: 'mode_500_berry_phase',
        name: 'Berry Phase',
        description: 'Mode 500: Berry phase geometric phase',
        category: 'Geometric',
        mode: 500,
        tags: ["berry", "phase"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_501_impressionist: {
        id: 'mode_501_impressionist',
        name: 'Impressionist',
        description: 'Mode 501: Impressionist visualization',
        category: 'Geometric',
        mode: 501,
        tags: ["impressionist"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_502_cubist: {
        id: 'mode_502_cubist',
        name: 'Cubist',
        description: 'Mode 502: Cubist visualization',
        category: 'Geometric',
        mode: 502,
        tags: ["cubist"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_503_surreal: {
        id: 'mode_503_surreal',
        name: 'Surreal',
        description: 'Mode 503: Surreal visualization',
        category: 'Geometric',
        mode: 503,
        tags: ["surreal"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_504_abstract_expressionist: {
        id: 'mode_504_abstract_expressionist',
        name: 'Abstract Expressionist',
        description: 'Mode 504: Abstract expressionist visualization',
        category: 'Geometric',
        mode: 504,
        tags: ["abstract", "expressionist"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_505_pop_art: {
        id: 'mode_505_pop_art',
        name: 'Pop Art',
        description: 'Mode 505: Pop art visualization',
        category: 'Geometric',
        mode: 505,
        tags: [],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_506_minimalist: {
        id: 'mode_506_minimalist',
        name: 'Minimalist',
        description: 'Mode 506: Minimalist visualization',
        category: 'Geometric',
        mode: 506,
        tags: ["minimalist"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_507_pointillist: {
        id: 'mode_507_pointillist',
        name: 'Pointillist',
        description: 'Mode 507: Pointillist visualization',
        category: 'Geometric',
        mode: 507,
        tags: ["pointillist"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_508_art_deco: {
        id: 'mode_508_art_deco',
        name: 'Art Deco',
        description: 'Mode 508: Art deco visualization',
        category: 'Geometric',
        mode: 508,
        tags: ["deco"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_509_art_nouveau: {
        id: 'mode_509_art_nouveau',
        name: 'Art Nouveau',
        description: 'Mode 509: Art nouveau visualization',
        category: 'Geometric',
        mode: 509,
        tags: ["nouveau"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_510_bauhaus: {
        id: 'mode_510_bauhaus',
        name: 'Bauhaus',
        description: 'Mode 510: Bauhaus visualization',
        category: 'Geometric',
        mode: 510,
        tags: ["bauhaus"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_511_futurist: {
        id: 'mode_511_futurist',
        name: 'Futurist',
        description: 'Mode 511: Futurist visualization',
        category: 'Geometric',
        mode: 511,
        tags: ["futurist"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_512_dadaist: {
        id: 'mode_512_dadaist',
        name: 'Dadaist',
        description: 'Mode 512: Dadaist visualization',
        category: 'Scientific',
        mode: 512,
        tags: ["dadaist"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_513_expressionist: {
        id: 'mode_513_expressionist',
        name: 'Expressionist',
        description: 'Mode 513: Expressionist visualization',
        category: 'Geometric',
        mode: 513,
        tags: ["expressionist"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_514_fauvism: {
        id: 'mode_514_fauvism',
        name: 'Fauvism',
        description: 'Mode 514: Fauvism visualization',
        category: 'Geometric',
        mode: 514,
        tags: ["fauvism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_515_constructivist: {
        id: 'mode_515_constructivist',
        name: 'Constructivist',
        description: 'Mode 515: Constructivist visualization',
        category: 'Geometric',
        mode: 515,
        tags: ["constructivist"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_516_suprematist: {
        id: 'mode_516_suprematist',
        name: 'Suprematist',
        description: 'Mode 516: Suprematist visualization',
        category: 'Geometric',
        mode: 516,
        tags: ["suprematist"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_517_vorticism: {
        id: 'mode_517_vorticism',
        name: 'Vorticism',
        description: 'Mode 517: Vorticism visualization',
        category: 'Geometric',
        mode: 517,
        tags: ["vorticism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_518_orphism: {
        id: 'mode_518_orphism',
        name: 'Orphism',
        description: 'Mode 518: Orphism visualization',
        category: 'Geometric',
        mode: 518,
        tags: ["orphism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_519_rayonism: {
        id: 'mode_519_rayonism',
        name: 'Rayonism',
        description: 'Mode 519: Rayonism visualization',
        category: 'Geometric',
        mode: 519,
        tags: ["rayonism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_520_synchromism: {
        id: 'mode_520_synchromism',
        name: 'Synchromism',
        description: 'Mode 520: Synchromism visualization',
        category: 'Geometric',
        mode: 520,
        tags: ["synchromism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_521_precisionism: {
        id: 'mode_521_precisionism',
        name: 'Precisionism',
        description: 'Mode 521: Precisionism visualization',
        category: 'Geometric',
        mode: 521,
        tags: ["precisionism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_522_regionalism: {
        id: 'mode_522_regionalism',
        name: 'Regionalism',
        description: 'Mode 522: Regionalism visualization',
        category: 'Geometric',
        mode: 522,
        tags: ["regionalism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_523_social_realism: {
        id: 'mode_523_social_realism',
        name: 'Social Realism',
        description: 'Mode 523: Social realism visualization',
        category: 'Geometric',
        mode: 523,
        tags: ["social", "realism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_524_neo_plasticism: {
        id: 'mode_524_neo_plasticism',
        name: 'Neo Plasticism',
        description: 'Mode 524: Neo-plasticism visualization',
        category: 'Geometric',
        mode: 524,
        tags: ["plasticism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_525_de_stijl: {
        id: 'mode_525_de_stijl',
        name: 'De Stijl',
        description: 'Mode 525: De stijl visualization',
        category: 'Geometric',
        mode: 525,
        tags: ["stijl"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_526_color_field: {
        id: 'mode_526_color_field',
        name: 'Color Field',
        description: 'Mode 526: Color field visualization',
        category: 'Geometric',
        mode: 526,
        tags: ["color", "field"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_527_hard_edge: {
        id: 'mode_527_hard_edge',
        name: 'Hard Edge',
        description: 'Mode 527: Hard edge visualization',
        category: 'Geometric',
        mode: 527,
        tags: ["hard", "edge"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_528_lyrical_abstraction: {
        id: 'mode_528_lyrical_abstraction',
        name: 'Lyrical Abstraction',
        description: 'Mode 528: Lyrical abstraction visualization',
        category: 'Geometric',
        mode: 528,
        tags: ["lyrical", "abstraction"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_529_tachisme: {
        id: 'mode_529_tachisme',
        name: 'Tachisme',
        description: 'Mode 529: Tachisme visualization',
        category: 'Geometric',
        mode: 529,
        tags: ["tachisme"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_530_action_painting: {
        id: 'mode_530_action_painting',
        name: 'Action Painting',
        description: 'Mode 530: Action painting visualization',
        category: 'Scientific',
        mode: 530,
        tags: ["action", "painting"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_531_stain_painting: {
        id: 'mode_531_stain_painting',
        name: 'Stain Painting',
        description: 'Mode 531: Stain painting visualization',
        category: 'Scientific',
        mode: 531,
        tags: ["stain", "painting"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_532_shaped_canvas: {
        id: 'mode_532_shaped_canvas',
        name: 'Shaped Canvas',
        description: 'Mode 532: Shaped canvas visualization',
        category: 'Geometric',
        mode: 532,
        tags: ["shaped", "canvas"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_533_monochrome: {
        id: 'mode_533_monochrome',
        name: 'Monochrome',
        description: 'Mode 533: Monochrome visualization',
        category: 'Geometric',
        mode: 533,
        tags: ["monochrome"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_534_kinetic_art: {
        id: 'mode_534_kinetic_art',
        name: 'Kinetic Art',
        description: 'Mode 534: Kinetic art visualization',
        category: 'Geometric',
        mode: 534,
        tags: ["kinetic"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_535_op_art: {
        id: 'mode_535_op_art',
        name: 'Op Art',
        description: 'Mode 535: Op art visualization',
        category: 'Geometric',
        mode: 535,
        tags: [],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_536_light_art: {
        id: 'mode_536_light_art',
        name: 'Light Art',
        description: 'Mode 536: Light art visualization',
        category: 'Geometric',
        mode: 536,
        tags: ["light"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_537_land_art: {
        id: 'mode_537_land_art',
        name: 'Land Art',
        description: 'Mode 537: Land art visualization',
        category: 'Geometric',
        mode: 537,
        tags: ["land"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_538_earth_art: {
        id: 'mode_538_earth_art',
        name: 'Earth Art',
        description: 'Mode 538: Earth art visualization',
        category: 'Geometric',
        mode: 538,
        tags: ["earth"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_539_environmental_art: {
        id: 'mode_539_environmental_art',
        name: 'Environmental Art',
        description: 'Mode 539: Environmental art visualization',
        category: 'Geometric',
        mode: 539,
        tags: ["environmental"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_540_installation_art: {
        id: 'mode_540_installation_art',
        name: 'Installation Art',
        description: 'Mode 540: Installation art visualization',
        category: 'Geometric',
        mode: 540,
        tags: ["installation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_541_video_art: {
        id: 'mode_541_video_art',
        name: 'Video Art',
        description: 'Mode 541: Video art visualization',
        category: 'Geometric',
        mode: 541,
        tags: ["video"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_542_digital_art: {
        id: 'mode_542_digital_art',
        name: 'Digital Art',
        description: 'Mode 542: Digital art visualization',
        category: 'Geometric',
        mode: 542,
        tags: ["digital"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_543_glitch_art: {
        id: 'mode_543_glitch_art',
        name: 'Glitch Art',
        description: 'Mode 543: Glitch art visualization',
        category: 'Geometric',
        mode: 543,
        tags: ["glitch"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_544_pixel_art: {
        id: 'mode_544_pixel_art',
        name: 'Pixel Art',
        description: 'Mode 544: Pixel art visualization',
        category: 'Geometric',
        mode: 544,
        tags: ["pixel"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_545_ascii_art: {
        id: 'mode_545_ascii_art',
        name: 'Ascii Art',
        description: 'Mode 545: Ascii art visualization',
        category: 'Geometric',
        mode: 545,
        tags: ["ascii"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_546_vector_art: {
        id: 'mode_546_vector_art',
        name: 'Vector Art',
        description: 'Mode 546: Vector art visualization',
        category: 'Geometric',
        mode: 546,
        tags: ["vector"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_547_fractal_art: {
        id: 'mode_547_fractal_art',
        name: 'Fractal Art',
        description: 'Mode 547: Fractal art visualization',
        category: 'Geometric',
        mode: 547,
        tags: ["fractal"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_548_algorithmic_art: {
        id: 'mode_548_algorithmic_art',
        name: 'Algorithmic Art',
        description: 'Mode 548: Algorithmic art visualization',
        category: 'Geometric',
        mode: 548,
        tags: ["algorithmic"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_549_generative_art: {
        id: 'mode_549_generative_art',
        name: 'Generative Art',
        description: 'Mode 549: Generative art visualization',
        category: 'Geometric',
        mode: 549,
        tags: ["generative"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_550_data_art: {
        id: 'mode_550_data_art',
        name: 'Data Art',
        description: 'Mode 550: Data art visualization',
        category: 'Geometric',
        mode: 550,
        tags: ["data"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_551_bio_art: {
        id: 'mode_551_bio_art',
        name: 'Bio Art',
        description: 'Mode 551: Bio art visualization',
        category: 'Geometric',
        mode: 551,
        tags: [],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_552_net_art: {
        id: 'mode_552_net_art',
        name: 'Net Art',
        description: 'Mode 552: Net art visualization',
        category: 'Geometric',
        mode: 552,
        tags: [],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_553_software_art: {
        id: 'mode_553_software_art',
        name: 'Software Art',
        description: 'Mode 553: Software art visualization',
        category: 'Geometric',
        mode: 553,
        tags: ["software"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_554_robotic_art: {
        id: 'mode_554_robotic_art',
        name: 'Robotic Art',
        description: 'Mode 554: Robotic art visualization',
        category: 'Geometric',
        mode: 554,
        tags: ["robotic"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_555_interactive_art: {
        id: 'mode_555_interactive_art',
        name: 'Interactive Art',
        description: 'Mode 555: Interactive art visualization',
        category: 'Geometric',
        mode: 555,
        tags: ["interactive"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_556_projection_mapping: {
        id: 'mode_556_projection_mapping',
        name: 'Projection Mapping',
        description: 'Mode 556: Projection mapping visualization',
        category: 'Geometric',
        mode: 556,
        tags: ["projection", "mapping"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_557_holographic_art: {
        id: 'mode_557_holographic_art',
        name: 'Holographic Art',
        description: 'Mode 557: Holographic art visualization',
        category: 'Geometric',
        mode: 557,
        tags: ["holographic"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_558_augmented_reality_art: {
        id: 'mode_558_augmented_reality_art',
        name: 'Augmented Reality Art',
        description: 'Mode 558: Augmented reality art visualization',
        category: 'Geometric',
        mode: 558,
        tags: ["augmented", "reality"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_559_vr_art: {
        id: 'mode_559_vr_art',
        name: 'Vr Art',
        description: 'Mode 559: Vr art visualization',
        category: 'Geometric',
        mode: 559,
        tags: [],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_560_procedural_art: {
        id: 'mode_560_procedural_art',
        name: 'Procedural Art',
        description: 'Mode 560: Procedural art visualization',
        category: 'Geometric',
        mode: 560,
        tags: ["procedural"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_561_parametric_art: {
        id: 'mode_561_parametric_art',
        name: 'Parametric Art',
        description: 'Mode 561: Parametric art visualization',
        category: 'Geometric',
        mode: 561,
        tags: ["parametric"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_562_mathematical_art: {
        id: 'mode_562_mathematical_art',
        name: 'Mathematical Art',
        description: 'Mode 562: Mathematical art visualization',
        category: 'Geometric',
        mode: 562,
        tags: ["mathematical"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_563_geometric_art: {
        id: 'mode_563_geometric_art',
        name: 'Geometric Art',
        description: 'Mode 563: Geometric art visualization',
        category: 'Geometric',
        mode: 563,
        tags: ["geometric"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_564_tessellation_art: {
        id: 'mode_564_tessellation_art',
        name: 'Tessellation Art',
        description: 'Mode 564: Tessellation art visualization',
        category: 'Geometric',
        mode: 564,
        tags: ["tessellation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_565_symmetry_art: {
        id: 'mode_565_symmetry_art',
        name: 'Symmetry Art',
        description: 'Mode 565: Symmetry art visualization',
        category: 'Geometric',
        mode: 565,
        tags: ["symmetry"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_566_kaleidoscope_art: {
        id: 'mode_566_kaleidoscope_art',
        name: 'Kaleidoscope Art',
        description: 'Mode 566: Kaleidoscope art visualization',
        category: 'Geometric',
        mode: 566,
        tags: ["kaleidoscope"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_567_mandala_art: {
        id: 'mode_567_mandala_art',
        name: 'Mandala Art',
        description: 'Mode 567: Mandala art visualization',
        category: 'Geometric',
        mode: 567,
        tags: ["mandala"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_568_zentangle_art: {
        id: 'mode_568_zentangle_art',
        name: 'Zentangle Art',
        description: 'Mode 568: Zentangle art visualization',
        category: 'Geometric',
        mode: 568,
        tags: ["zentangle"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_569_doodle_art: {
        id: 'mode_569_doodle_art',
        name: 'Doodle Art',
        description: 'Mode 569: Doodle art visualization',
        category: 'Geometric',
        mode: 569,
        tags: ["doodle"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_570_street_art: {
        id: 'mode_570_street_art',
        name: 'Street Art',
        description: 'Mode 570: Street art visualization',
        category: 'Nature',
        mode: 570,
        tags: ["street"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_571_graffiti_art: {
        id: 'mode_571_graffiti_art',
        name: 'Graffiti Art',
        description: 'Mode 571: Graffiti art visualization',
        category: 'Geometric',
        mode: 571,
        tags: ["graffiti"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_572_mural_art: {
        id: 'mode_572_mural_art',
        name: 'Mural Art',
        description: 'Mode 572: Mural art visualization',
        category: 'Geometric',
        mode: 572,
        tags: ["mural"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_573_stencil_art: {
        id: 'mode_573_stencil_art',
        name: 'Stencil Art',
        description: 'Mode 573: Stencil art visualization',
        category: 'Geometric',
        mode: 573,
        tags: ["stencil"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_574_wheat_paste_art: {
        id: 'mode_574_wheat_paste_art',
        name: 'Wheat Paste Art',
        description: 'Mode 574: Wheat paste art visualization',
        category: 'Geometric',
        mode: 574,
        tags: ["wheat", "paste"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_575_spray_paint_art: {
        id: 'mode_575_spray_paint_art',
        name: 'Spray Paint Art',
        description: 'Mode 575: Spray paint art visualization',
        category: 'Scientific',
        mode: 575,
        tags: ["spray", "paint"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_576_mosaic_art: {
        id: 'mode_576_mosaic_art',
        name: 'Mosaic Art',
        description: 'Mode 576: Mosaic art visualization',
        category: 'Scientific',
        mode: 576,
        tags: ["mosaic"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_577_collage_art: {
        id: 'mode_577_collage_art',
        name: 'Collage Art',
        description: 'Mode 577: Collage art visualization',
        category: 'Geometric',
        mode: 577,
        tags: ["collage"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_578_mixed_media_art: {
        id: 'mode_578_mixed_media_art',
        name: 'Mixed Media Art',
        description: 'Mode 578: Mixed media art visualization',
        category: 'Geometric',
        mode: 578,
        tags: ["mixed", "media"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_579_assemblage_art: {
        id: 'mode_579_assemblage_art',
        name: 'Assemblage Art',
        description: 'Mode 579: Assemblage art visualization',
        category: 'Geometric',
        mode: 579,
        tags: ["assemblage"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_580_found_object_art: {
        id: 'mode_580_found_object_art',
        name: 'Found Object Art',
        description: 'Mode 580: Found object art visualization',
        category: 'Geometric',
        mode: 580,
        tags: ["found", "object"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_581_readymade_art: {
        id: 'mode_581_readymade_art',
        name: 'Readymade Art',
        description: 'Mode 581: Readymade art visualization',
        category: 'Geometric',
        mode: 581,
        tags: ["readymade"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_582_appropriation_art: {
        id: 'mode_582_appropriation_art',
        name: 'Appropriation Art',
        description: 'Mode 582: Appropriation art visualization',
        category: 'Geometric',
        mode: 582,
        tags: ["appropriation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_583_sampling_art: {
        id: 'mode_583_sampling_art',
        name: 'Sampling Art',
        description: 'Mode 583: Sampling art visualization',
        category: 'Geometric',
        mode: 583,
        tags: ["sampling"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_584_remix_art: {
        id: 'mode_584_remix_art',
        name: 'Remix Art',
        description: 'Mode 584: Remix art visualization',
        category: 'Geometric',
        mode: 584,
        tags: ["remix"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_585_mashup_art: {
        id: 'mode_585_mashup_art',
        name: 'Mashup Art',
        description: 'Mode 585: Mashup art visualization',
        category: 'Geometric',
        mode: 585,
        tags: ["mashup"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_586_photomontage: {
        id: 'mode_586_photomontage',
        name: 'Photomontage',
        description: 'Mode 586: Photomontage visualization',
        category: 'Geometric',
        mode: 586,
        tags: ["photomontage"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_587_cut_up_technique: {
        id: 'mode_587_cut_up_technique',
        name: 'Cut Up Technique',
        description: 'Mode 587: Cut-up technique visualization',
        category: 'Geometric',
        mode: 587,
        tags: ["technique"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_588_exquisite_corpse: {
        id: 'mode_588_exquisite_corpse',
        name: 'Exquisite Corpse',
        description: 'Mode 588: Exquisite corpse visualization',
        category: 'Geometric',
        mode: 588,
        tags: ["exquisite", "corpse"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_589_automatic_drawing: {
        id: 'mode_589_automatic_drawing',
        name: 'Automatic Drawing',
        description: 'Mode 589: Automatic drawing visualization',
        category: 'Geometric',
        mode: 589,
        tags: ["automatic", "drawing"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_590_chance_art: {
        id: 'mode_590_chance_art',
        name: 'Chance Art',
        description: 'Mode 590: Chance art visualization',
        category: 'Geometric',
        mode: 590,
        tags: ["chance"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_591_indeterminacy_art: {
        id: 'mode_591_indeterminacy_art',
        name: 'Indeterminacy Art',
        description: 'Mode 591: Indeterminacy art visualization',
        category: 'Geometric',
        mode: 591,
        tags: ["indeterminacy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_592_aleatory_art: {
        id: 'mode_592_aleatory_art',
        name: 'Aleatory Art',
        description: 'Mode 592: Aleatory art visualization',
        category: 'Geometric',
        mode: 592,
        tags: ["aleatory"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_593_stochastic_art: {
        id: 'mode_593_stochastic_art',
        name: 'Stochastic Art',
        description: 'Mode 593: Stochastic art visualization',
        category: 'Geometric',
        mode: 593,
        tags: ["stochastic"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_594_entropy_art: {
        id: 'mode_594_entropy_art',
        name: 'Entropy Art',
        description: 'Mode 594: Entropy art visualization',
        category: 'Geometric',
        mode: 594,
        tags: ["entropy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_595_chaos_art: {
        id: 'mode_595_chaos_art',
        name: 'Chaos Art',
        description: 'Mode 595: Chaos art visualization',
        category: 'Geometric',
        mode: 595,
        tags: ["chaos"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_596_complexity_art: {
        id: 'mode_596_complexity_art',
        name: 'Complexity Art',
        description: 'Mode 596: Complexity art visualization',
        category: 'Geometric',
        mode: 596,
        tags: ["complexity"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_597_emergence_art: {
        id: 'mode_597_emergence_art',
        name: 'Emergence Art',
        description: 'Mode 597: Emergence art visualization',
        category: 'Geometric',
        mode: 597,
        tags: ["emergence"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_598_self_organization_art: {
        id: 'mode_598_self_organization_art',
        name: 'Self Organization Art',
        description: 'Mode 598: Self-organization art visualization',
        category: 'Geometric',
        mode: 598,
        tags: ["self", "organization"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_599_swarm_art: {
        id: 'mode_599_swarm_art',
        name: 'Swarm Art',
        description: 'Mode 599: Swarm art visualization',
        category: 'Particles',
        mode: 599,
        tags: ["swarm"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_600_flocking_art: {
        id: 'mode_600_flocking_art',
        name: 'Flocking Art',
        description: 'Mode 600: Flocking art visualization',
        category: 'Geometric',
        mode: 600,
        tags: ["flocking"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_601_nebula: {
        id: 'mode_601_nebula',
        name: 'Nebula',
        description: 'Mode 601: Nebula visualization',
        category: 'Space & Cosmic',
        mode: 601,
        tags: ["nebula"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_602_galaxy_spiral: {
        id: 'mode_602_galaxy_spiral',
        name: 'Galaxy Spiral',
        description: 'Mode 602: Galaxy spiral visualization',
        category: 'Space & Cosmic',
        mode: 602,
        tags: ["galaxy", "spiral"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_603_black_hole: {
        id: 'mode_603_black_hole',
        name: 'Black Hole',
        description: 'Mode 603: Black hole visualization',
        category: 'Space & Cosmic',
        mode: 603,
        tags: ["black", "hole"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_604_pulsar: {
        id: 'mode_604_pulsar',
        name: 'Pulsar',
        description: 'Mode 604: Pulsar visualization',
        category: 'Space & Cosmic',
        mode: 604,
        tags: ["pulsar"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_605_quasar: {
        id: 'mode_605_quasar',
        name: 'Quasar',
        description: 'Mode 605: Quasar visualization',
        category: 'Space & Cosmic',
        mode: 605,
        tags: ["quasar"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_606_supernova: {
        id: 'mode_606_supernova',
        name: 'Supernova',
        description: 'Mode 606: Supernova visualization',
        category: 'Space & Cosmic',
        mode: 606,
        tags: ["supernova"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_607_star_cluster: {
        id: 'mode_607_star_cluster',
        name: 'Star Cluster',
        description: 'Mode 607: Star cluster visualization',
        category: 'Space & Cosmic',
        mode: 607,
        tags: ["star", "cluster"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_608_asteroid_belt: {
        id: 'mode_608_asteroid_belt',
        name: 'Asteroid Belt',
        description: 'Mode 608: Asteroid belt visualization',
        category: 'Space & Cosmic',
        mode: 608,
        tags: ["asteroid", "belt"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_609_comet_tail: {
        id: 'mode_609_comet_tail',
        name: 'Comet Tail',
        description: 'Mode 609: Comet tail visualization',
        category: 'Scientific',
        mode: 609,
        tags: ["comet", "tail"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_610_meteor_shower: {
        id: 'mode_610_meteor_shower',
        name: 'Meteor Shower',
        description: 'Mode 610: Meteor shower visualization',
        category: 'Space & Cosmic',
        mode: 610,
        tags: ["meteor", "shower"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_611_planetary_rings: {
        id: 'mode_611_planetary_rings',
        name: 'Planetary Rings',
        description: 'Mode 611: Planetary rings visualization',
        category: 'Space & Cosmic',
        mode: 611,
        tags: ["planetary", "rings"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_612_solar_flare: {
        id: 'mode_612_solar_flare',
        name: 'Solar Flare',
        description: 'Mode 612: Solar flare visualization',
        category: 'Space & Cosmic',
        mode: 612,
        tags: ["solar", "flare"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_613_coronal_mass_ejection: {
        id: 'mode_613_coronal_mass_ejection',
        name: 'Coronal Mass Ejection',
        description: 'Mode 613: Coronal mass ejection visualization',
        category: 'Space & Cosmic',
        mode: 613,
        tags: ["coronal", "mass", "ejection"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_614_cosmic_ray: {
        id: 'mode_614_cosmic_ray',
        name: 'Cosmic Ray',
        description: 'Mode 614: Cosmic ray visualization',
        category: 'Space & Cosmic',
        mode: 614,
        tags: ["cosmic"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_615_gamma_ray_burst: {
        id: 'mode_615_gamma_ray_burst',
        name: 'Gamma Ray Burst',
        description: 'Mode 615: Gamma ray burst visualization',
        category: 'Space & Cosmic',
        mode: 615,
        tags: ["gamma", "burst"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_616_gravitational_lens: {
        id: 'mode_616_gravitational_lens',
        name: 'Gravitational Lens',
        description: 'Mode 616: Gravitational lens visualization',
        category: 'Space & Cosmic',
        mode: 616,
        tags: ["gravitational", "lens"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_617_dark_matter_halo: {
        id: 'mode_617_dark_matter_halo',
        name: 'Dark Matter Halo',
        description: 'Mode 617: Dark matter halo visualization',
        category: 'Space & Cosmic',
        mode: 617,
        tags: ["dark", "matter", "halo"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_618_cosmic_web: {
        id: 'mode_618_cosmic_web',
        name: 'Cosmic Web',
        description: 'Mode 618: Cosmic web visualization',
        category: 'Space & Cosmic',
        mode: 618,
        tags: ["cosmic"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_619_void: {
        id: 'mode_619_void',
        name: 'Void',
        description: 'Mode 619: Void visualization',
        category: 'Space & Cosmic',
        mode: 619,
        tags: ["void"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_620_filament_structure: {
        id: 'mode_620_filament_structure',
        name: 'Filament Structure',
        description: 'Mode 620: Filament structure visualization',
        category: 'Space & Cosmic',
        mode: 620,
        tags: ["filament", "structure"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_621_hubble_deep_field: {
        id: 'mode_621_hubble_deep_field',
        name: 'Hubble Deep Field',
        description: 'Mode 621: Hubble deep field visualization',
        category: 'Space & Cosmic',
        mode: 621,
        tags: ["hubble", "deep", "field"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_622_galaxy_collision: {
        id: 'mode_622_galaxy_collision',
        name: 'Galaxy Collision',
        description: 'Mode 622: Galaxy collision visualization',
        category: 'Space & Cosmic',
        mode: 622,
        tags: ["galaxy", "collision"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_623_tidal_tail: {
        id: 'mode_623_tidal_tail',
        name: 'Tidal Tail',
        description: 'Mode 623: Tidal tail visualization',
        category: 'Scientific',
        mode: 623,
        tags: ["tidal", "tail"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_624_starburst_galaxy: {
        id: 'mode_624_starburst_galaxy',
        name: 'Starburst Galaxy',
        description: 'Mode 624: Starburst galaxy visualization',
        category: 'Space & Cosmic',
        mode: 624,
        tags: ["starburst", "galaxy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_625_active_galactic_nucleus: {
        id: 'mode_625_active_galactic_nucleus',
        name: 'Active Galactic Nucleus',
        description: 'Mode 625: Active galactic nucleus visualization',
        category: 'Space & Cosmic',
        mode: 625,
        tags: ["active", "galactic", "nucleus"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_626_blazar: {
        id: 'mode_626_blazar',
        name: 'Blazar',
        description: 'Mode 626: Blazar visualization',
        category: 'Space & Cosmic',
        mode: 626,
        tags: ["blazar"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_627_seyfert_galaxy: {
        id: 'mode_627_seyfert_galaxy',
        name: 'Seyfert Galaxy',
        description: 'Mode 627: Seyfert galaxy visualization',
        category: 'Space & Cosmic',
        mode: 627,
        tags: ["seyfert", "galaxy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_628_radio_galaxy: {
        id: 'mode_628_radio_galaxy',
        name: 'Radio Galaxy',
        description: 'Mode 628: Radio galaxy visualization',
        category: 'Space & Cosmic',
        mode: 628,
        tags: ["radio", "galaxy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_629_elliptical_galaxy: {
        id: 'mode_629_elliptical_galaxy',
        name: 'Elliptical Galaxy',
        description: 'Mode 629: Elliptical galaxy visualization',
        category: 'Space & Cosmic',
        mode: 629,
        tags: ["elliptical", "galaxy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_630_irregular_galaxy: {
        id: 'mode_630_irregular_galaxy',
        name: 'Irregular Galaxy',
        description: 'Mode 630: Irregular galaxy visualization',
        category: 'Space & Cosmic',
        mode: 630,
        tags: ["irregular", "galaxy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_631_dwarf_galaxy: {
        id: 'mode_631_dwarf_galaxy',
        name: 'Dwarf Galaxy',
        description: 'Mode 631: Dwarf galaxy visualization',
        category: 'Space & Cosmic',
        mode: 631,
        tags: ["dwarf", "galaxy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_632_globular_cluster: {
        id: 'mode_632_globular_cluster',
        name: 'Globular Cluster',
        description: 'Mode 632: Globular cluster visualization',
        category: 'Space & Cosmic',
        mode: 632,
        tags: ["globular", "cluster"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_633_open_cluster: {
        id: 'mode_633_open_cluster',
        name: 'Open Cluster',
        description: 'Mode 633: Open cluster visualization',
        category: 'Space & Cosmic',
        mode: 633,
        tags: ["open", "cluster"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_634_protoplanetary_disk: {
        id: 'mode_634_protoplanetary_disk',
        name: 'Protoplanetary Disk',
        description: 'Mode 634: Protoplanetary disk visualization',
        category: 'Space & Cosmic',
        mode: 634,
        tags: ["protoplanetary", "disk"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_635_accretion_disk: {
        id: 'mode_635_accretion_disk',
        name: 'Accretion Disk',
        description: 'Mode 635: Accretion disk visualization',
        category: 'Space & Cosmic',
        mode: 635,
        tags: ["accretion", "disk"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_636_jets_from_black_hole: {
        id: 'mode_636_jets_from_black_hole',
        name: 'Jets From Black Hole',
        description: 'Mode 636: Jets from black hole visualization',
        category: 'Space & Cosmic',
        mode: 636,
        tags: ["jets", "from", "black"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_637_event_horizon: {
        id: 'mode_637_event_horizon',
        name: 'Event Horizon',
        description: 'Mode 637: Event horizon visualization',
        category: 'Space & Cosmic',
        mode: 637,
        tags: ["event", "horizon"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_638_photon_sphere: {
        id: 'mode_638_photon_sphere',
        name: 'Photon Sphere',
        description: 'Mode 638: Photon sphere visualization',
        category: 'Space & Cosmic',
        mode: 638,
        tags: ["photon", "sphere"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_639_ergosphere: {
        id: 'mode_639_ergosphere',
        name: 'Ergosphere',
        description: 'Mode 639: Ergosphere visualization',
        category: 'Space & Cosmic',
        mode: 639,
        tags: ["ergosphere"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_640_singularity: {
        id: 'mode_640_singularity',
        name: 'Singularity',
        description: 'Mode 640: Singularity visualization',
        category: 'Space & Cosmic',
        mode: 640,
        tags: ["singularity"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_641_wormhole: {
        id: 'mode_641_wormhole',
        name: 'Wormhole',
        description: 'Mode 641: Wormhole visualization',
        category: 'Space & Cosmic',
        mode: 641,
        tags: ["wormhole"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_642_white_hole: {
        id: 'mode_642_white_hole',
        name: 'White Hole',
        description: 'Mode 642: White hole visualization',
        category: 'Space & Cosmic',
        mode: 642,
        tags: ["white", "hole"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_643_naked_singularity: {
        id: 'mode_643_naked_singularity',
        name: 'Naked Singularity',
        description: 'Mode 643: Naked singularity visualization',
        category: 'Space & Cosmic',
        mode: 643,
        tags: ["naked", "singularity"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_644_hawking_radiation: {
        id: 'mode_644_hawking_radiation',
        name: 'Hawking Radiation',
        description: 'Mode 644: Hawking radiation visualization',
        category: 'Space & Cosmic',
        mode: 644,
        tags: ["hawking", "radiation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_645_information_paradox: {
        id: 'mode_645_information_paradox',
        name: 'Information Paradox',
        description: 'Mode 645: Information paradox visualization',
        category: 'Space & Cosmic',
        mode: 645,
        tags: ["information", "paradox"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_646_multiverse_bubble: {
        id: 'mode_646_multiverse_bubble',
        name: 'Multiverse Bubble',
        description: 'Mode 646: Multiverse bubble - particle bars with floating squares',
        category: 'Particles',
        mode: 646,
        tags: ["multiverse", "bubble", "particles", "glow"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' },
            particleSize: { min: 2, max: 8, default: 4, label: 'Particle Size' },
            particleSpacing: { min: 3, max: 10, default: 5, label: 'Particle Spacing' },
            glowIntensity: { min: 0, max: 30, default: 15, label: 'Glow Intensity' }
        }
    },
    mode_647_parallel_universe: {
        id: 'mode_647_parallel_universe',
        name: 'Parallel Universe',
        description: 'Mode 647: Parallel universe visualization',
        category: 'Space & Cosmic',
        mode: 647,
        tags: ["parallel", "universe"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_648_brane_collision: {
        id: 'mode_648_brane_collision',
        name: 'Brane Collision',
        description: 'Mode 648: Brane collision visualization',
        category: 'Space & Cosmic',
        mode: 648,
        tags: ["brane", "collision"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_649_extra_dimensions: {
        id: 'mode_649_extra_dimensions',
        name: 'Extra Dimensions',
        description: 'Mode 649: Extra dimensions visualization',
        category: 'Space & Cosmic',
        mode: 649,
        tags: ["extra", "dimensions"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_650_calabi_yau_manifold: {
        id: 'mode_650_calabi_yau_manifold',
        name: 'Calabi Yau Manifold',
        description: 'Mode 650: Calabi-yau manifold visualization',
        category: 'Space & Cosmic',
        mode: 650,
        tags: ["calabi", "manifold"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_651_string_theory_vibration: {
        id: 'mode_651_string_theory_vibration',
        name: 'String Theory Vibration',
        description: 'Mode 651: String theory vibration visualization',
        category: 'Space & Cosmic',
        mode: 651,
        tags: ["string", "theory", "vibration"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_652_quantum_foam: {
        id: 'mode_652_quantum_foam',
        name: 'Quantum Foam',
        description: 'Mode 652: Quantum foam visualization',
        category: 'Scientific',
        mode: 652,
        tags: ["quantum", "foam"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_653_planck_scale: {
        id: 'mode_653_planck_scale',
        name: 'Planck Scale',
        description: 'Mode 653: Planck scale visualization',
        category: 'Space & Cosmic',
        mode: 653,
        tags: ["planck", "scale"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_654_big_bang: {
        id: 'mode_654_big_bang',
        name: 'Big Bang',
        description: 'Mode 654: Big bang visualization',
        category: 'Space & Cosmic',
        mode: 654,
        tags: ["bang"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_655_cosmic_microwave_background: {
        id: 'mode_655_cosmic_microwave_background',
        name: 'Cosmic Microwave Background',
        description: 'Mode 655: Cosmic microwave background visualization',
        category: 'Space & Cosmic',
        mode: 655,
        tags: ["cosmic", "microwave", "background"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_656_inflation_field: {
        id: 'mode_656_inflation_field',
        name: 'Inflation Field',
        description: 'Mode 656: Inflation field visualization',
        category: 'Space & Cosmic',
        mode: 656,
        tags: ["inflation", "field"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_657_density_fluctuations: {
        id: 'mode_657_density_fluctuations',
        name: 'Density Fluctuations',
        description: 'Mode 657: Density fluctuations visualization',
        category: 'Space & Cosmic',
        mode: 657,
        tags: ["density", "fluctuations"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_658_baryon_acoustic_oscillations: {
        id: 'mode_658_baryon_acoustic_oscillations',
        name: 'Baryon Acoustic Oscillations',
        description: 'Mode 658: Baryon acoustic oscillations visualization',
        category: 'Space & Cosmic',
        mode: 658,
        tags: ["baryon", "acoustic", "oscillations"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_659_dark_energy: {
        id: 'mode_659_dark_energy',
        name: 'Dark Energy',
        description: 'Mode 659: Dark energy visualization',
        category: 'Energy',
        mode: 659,
        tags: ["dark", "energy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_660_cosmological_constant: {
        id: 'mode_660_cosmological_constant',
        name: 'Cosmological Constant',
        description: 'Mode 660: Cosmological constant visualization',
        category: 'Space & Cosmic',
        mode: 660,
        tags: ["cosmological", "constant"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_661_quintessence_field: {
        id: 'mode_661_quintessence_field',
        name: 'Quintessence Field',
        description: 'Mode 661: Quintessence field visualization',
        category: 'Space & Cosmic',
        mode: 661,
        tags: ["quintessence", "field"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_662_heat_death: {
        id: 'mode_662_heat_death',
        name: 'Heat Death',
        description: 'Mode 662: Heat death visualization',
        category: 'Space & Cosmic',
        mode: 662,
        tags: ["heat", "death"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_663_big_rip: {
        id: 'mode_663_big_rip',
        name: 'Big Rip',
        description: 'Mode 663: Big rip visualization',
        category: 'Space & Cosmic',
        mode: 663,
        tags: [],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_664_big_crunch: {
        id: 'mode_664_big_crunch',
        name: 'Big Crunch',
        description: 'Mode 664: Big crunch visualization',
        category: 'Space & Cosmic',
        mode: 664,
        tags: ["crunch"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_665_big_bounce: {
        id: 'mode_665_big_bounce',
        name: 'Big Bounce',
        description: 'Mode 665: Big bounce visualization',
        category: 'Space & Cosmic',
        mode: 665,
        tags: ["bounce"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_666_cyclic_universe: {
        id: 'mode_666_cyclic_universe',
        name: 'Cyclic Universe',
        description: 'Mode 666: Cyclic universe visualization',
        category: 'Space & Cosmic',
        mode: 666,
        tags: ["cyclic", "universe"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_667_conformal_cyclic_cosmology: {
        id: 'mode_667_conformal_cyclic_cosmology',
        name: 'Conformal Cyclic Cosmology',
        description: 'Mode 667: Conformal cyclic cosmology visualization',
        category: 'Space & Cosmic',
        mode: 667,
        tags: ["conformal", "cyclic", "cosmology"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_668_eternal_inflation: {
        id: 'mode_668_eternal_inflation',
        name: 'Eternal Inflation',
        description: 'Mode 668: Eternal inflation visualization',
        category: 'Space & Cosmic',
        mode: 668,
        tags: ["eternal", "inflation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_669_landscape_multiverse: {
        id: 'mode_669_landscape_multiverse',
        name: 'Landscape Multiverse',
        description: 'Mode 669: Landscape multiverse visualization',
        category: 'Space & Cosmic',
        mode: 669,
        tags: ["landscape", "multiverse"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_670_quantum_decoherence: {
        id: 'mode_670_quantum_decoherence',
        name: 'Quantum Decoherence',
        description: 'Mode 670: Quantum decoherence visualization',
        category: 'Scientific',
        mode: 670,
        tags: ["quantum", "decoherence"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_671_many_worlds: {
        id: 'mode_671_many_worlds',
        name: 'Many Worlds',
        description: 'Mode 671: Many worlds visualization',
        category: 'Space & Cosmic',
        mode: 671,
        tags: ["many", "worlds"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_672_pilot_wave: {
        id: 'mode_672_pilot_wave',
        name: 'Pilot Wave',
        description: 'Mode 672: Pilot wave visualization',
        category: 'Space & Cosmic',
        mode: 672,
        tags: ["pilot", "wave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_673_spontaneous_collapse: {
        id: 'mode_673_spontaneous_collapse',
        name: 'Spontaneous Collapse',
        description: 'Mode 673: Spontaneous collapse visualization',
        category: 'Space & Cosmic',
        mode: 673,
        tags: ["spontaneous", "collapse"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_674_transactional_interpretation: {
        id: 'mode_674_transactional_interpretation',
        name: 'Transactional Interpretation',
        description: 'Mode 674: Transactional interpretation visualization',
        category: 'Space & Cosmic',
        mode: 674,
        tags: ["transactional", "interpretation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_675_relational_quantum_mechanics: {
        id: 'mode_675_relational_quantum_mechanics',
        name: 'Relational Quantum Mechanics',
        description: 'Mode 675: Relational quantum mechanics visualization',
        category: 'Scientific',
        mode: 675,
        tags: ["relational", "quantum", "mechanics"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_676_quantum_bayesianism: {
        id: 'mode_676_quantum_bayesianism',
        name: 'Quantum Bayesianism',
        description: 'Mode 676: Quantum bayesianism visualization',
        category: 'Scientific',
        mode: 676,
        tags: ["quantum", "bayesianism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_677_consistent_histories: {
        id: 'mode_677_consistent_histories',
        name: 'Consistent Histories',
        description: 'Mode 677: Consistent histories visualization',
        category: 'Space & Cosmic',
        mode: 677,
        tags: ["consistent", "histories"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_678_bohemian_mechanics: {
        id: 'mode_678_bohemian_mechanics',
        name: 'Bohemian Mechanics',
        description: 'Mode 678: Bohemian mechanics visualization',
        category: 'Space & Cosmic',
        mode: 678,
        tags: ["bohemian", "mechanics"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_679_stochastic_mechanics: {
        id: 'mode_679_stochastic_mechanics',
        name: 'Stochastic Mechanics',
        description: 'Mode 679: Stochastic mechanics visualization',
        category: 'Space & Cosmic',
        mode: 679,
        tags: ["stochastic", "mechanics"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_680_quantum_darwinism: {
        id: 'mode_680_quantum_darwinism',
        name: 'Quantum Darwinism',
        description: 'Mode 680: Quantum darwinism visualization',
        category: 'Scientific',
        mode: 680,
        tags: ["quantum", "darwinism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_681_einselection: {
        id: 'mode_681_einselection',
        name: 'Einselection',
        description: 'Mode 681: Einselection visualization',
        category: 'Space & Cosmic',
        mode: 681,
        tags: ["einselection"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_682_pointer_states: {
        id: 'mode_682_pointer_states',
        name: 'Pointer States',
        description: 'Mode 682: Pointer states visualization',
        category: 'Space & Cosmic',
        mode: 682,
        tags: ["pointer", "states"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_683_branching_spacetime: {
        id: 'mode_683_branching_spacetime',
        name: 'Branching Spacetime',
        description: 'Mode 683: Branching spacetime visualization',
        category: 'Space & Cosmic',
        mode: 683,
        tags: ["branching", "spacetime"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_684_worldline: {
        id: 'mode_684_worldline',
        name: 'Worldline',
        description: 'Mode 684: Worldline visualization',
        category: 'Space & Cosmic',
        mode: 684,
        tags: ["worldline"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_685_light_cone: {
        id: 'mode_685_light_cone',
        name: 'Light Cone',
        description: 'Mode 685: Light cone visualization',
        category: 'Space & Cosmic',
        mode: 685,
        tags: ["light", "cone"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_686_cauchy_surface: {
        id: 'mode_686_cauchy_surface',
        name: 'Cauchy Surface',
        description: 'Mode 686: Cauchy surface visualization',
        category: 'Space & Cosmic',
        mode: 686,
        tags: ["cauchy", "surface"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_687_spacelike_hypersurface: {
        id: 'mode_687_spacelike_hypersurface',
        name: 'Spacelike Hypersurface',
        description: 'Mode 687: Spacelike hypersurface visualization',
        category: 'Space & Cosmic',
        mode: 687,
        tags: ["spacelike", "hypersurface"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_688_timelike_curve: {
        id: 'mode_688_timelike_curve',
        name: 'Timelike Curve',
        description: 'Mode 688: Timelike curve visualization',
        category: 'Space & Cosmic',
        mode: 688,
        tags: ["timelike", "curve"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_689_closed_timelike_curve: {
        id: 'mode_689_closed_timelike_curve',
        name: 'Closed Timelike Curve',
        description: 'Mode 689: Closed timelike curve visualization',
        category: 'Space & Cosmic',
        mode: 689,
        tags: ["closed", "timelike", "curve"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_690_chronology_protection: {
        id: 'mode_690_chronology_protection',
        name: 'Chronology Protection',
        description: 'Mode 690: Chronology protection visualization',
        category: 'Space & Cosmic',
        mode: 690,
        tags: ["chronology", "protection"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_691_novikov_self_consistency: {
        id: 'mode_691_novikov_self_consistency',
        name: 'Novikov Self Consistency',
        description: 'Mode 691: Novikov self-consistency visualization',
        category: 'Space & Cosmic',
        mode: 691,
        tags: ["novikov", "self", "consistency"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_692_grandfather_paradox: {
        id: 'mode_692_grandfather_paradox',
        name: 'Grandfather Paradox',
        description: 'Mode 692: Grandfather paradox visualization',
        category: 'Space & Cosmic',
        mode: 692,
        tags: ["grandfather", "paradox"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_693_bootstrap_paradox: {
        id: 'mode_693_bootstrap_paradox',
        name: 'Bootstrap Paradox',
        description: 'Mode 693: Bootstrap paradox visualization',
        category: 'Space & Cosmic',
        mode: 693,
        tags: ["bootstrap", "paradox"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_694_predestination_paradox: {
        id: 'mode_694_predestination_paradox',
        name: 'Predestination Paradox',
        description: 'Mode 694: Predestination paradox visualization',
        category: 'Space & Cosmic',
        mode: 694,
        tags: ["predestination", "paradox"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_695_causal_loop: {
        id: 'mode_695_causal_loop',
        name: 'Causal Loop',
        description: 'Mode 695: Causal loop visualization',
        category: 'Space & Cosmic',
        mode: 695,
        tags: ["causal", "loop"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_696_retrocausality: {
        id: 'mode_696_retrocausality',
        name: 'Retrocausality',
        description: 'Mode 696: Retrocausality visualization',
        category: 'Tech',
        mode: 696,
        tags: ["retrocausality"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_697_advanced_wave: {
        id: 'mode_697_advanced_wave',
        name: 'Advanced Wave',
        description: 'Mode 697: Advanced wave visualization',
        category: 'Space & Cosmic',
        mode: 697,
        tags: ["advanced", "wave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_698_wheeler_feynman_absorber: {
        id: 'mode_698_wheeler_feynman_absorber',
        name: 'Wheeler Feynman Absorber',
        description: 'Mode 698: Wheeler-feynman absorber visualization',
        category: 'Space & Cosmic',
        mode: 698,
        tags: ["wheeler", "feynman", "absorber"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_699_transactional_interpretation: {
        id: 'mode_699_transactional_interpretation',
        name: 'Transactional Interpretation',
        description: 'Mode 699: Transactional interpretation visualization',
        category: 'Space & Cosmic',
        mode: 699,
        tags: ["transactional", "interpretation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_700_two_state_vector: {
        id: 'mode_700_two_state_vector',
        name: 'Two State Vector',
        description: 'Mode 700: Two-state vector visualization',
        category: 'Space & Cosmic',
        mode: 700,
        tags: ["state", "vector"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_701_binary_rain: {
        id: 'mode_701_binary_rain',
        name: 'Binary Rain',
        description: 'Mode 701: Binary rain visualization',
        category: 'Scientific',
        mode: 701,
        tags: ["binary", "rain"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_702_hexadecimal_grid: {
        id: 'mode_702_hexadecimal_grid',
        name: 'Hexadecimal Grid',
        description: 'Mode 702: Hexadecimal grid visualization',
        category: 'Space & Cosmic',
        mode: 702,
        tags: ["hexadecimal", "grid"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_703_circuit_board: {
        id: 'mode_703_circuit_board',
        name: 'Circuit Board',
        description: 'Mode 703: Circuit board visualization',
        category: 'Scientific',
        mode: 703,
        tags: ["circuit", "board"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_704_data_flow: {
        id: 'mode_704_data_flow',
        name: 'Data Flow',
        description: 'Mode 704: Data flow visualization',
        category: 'Space & Cosmic',
        mode: 704,
        tags: ["data", "flow"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_705_packet_transmission: {
        id: 'mode_705_packet_transmission',
        name: 'Packet Transmission',
        description: 'Mode 705: Packet transmission visualization',
        category: 'Space & Cosmic',
        mode: 705,
        tags: ["packet", "transmission"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_706_network_topology: {
        id: 'mode_706_network_topology',
        name: 'Network Topology',
        description: 'Mode 706: Network topology visualization',
        category: 'Space & Cosmic',
        mode: 706,
        tags: ["network", "topology"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_707_server_cluster: {
        id: 'mode_707_server_cluster',
        name: 'Server Cluster',
        description: 'Mode 707: Server cluster visualization',
        category: 'Space & Cosmic',
        mode: 707,
        tags: ["server", "cluster"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_708_cloud_computing: {
        id: 'mode_708_cloud_computing',
        name: 'Cloud Computing',
        description: 'Mode 708: Cloud computing visualization',
        category: 'Space & Cosmic',
        mode: 708,
        tags: ["cloud", "computing"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_709_distributed_system: {
        id: 'mode_709_distributed_system',
        name: 'Distributed System',
        description: 'Mode 709: Distributed system visualization',
        category: 'Space & Cosmic',
        mode: 709,
        tags: ["distributed", "system"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_710_peer_to_peer: {
        id: 'mode_710_peer_to_peer',
        name: 'Peer To Peer',
        description: 'Mode 710: Peer-to-peer visualization',
        category: 'Space & Cosmic',
        mode: 710,
        tags: ["peer", "peer"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_711_blockchain: {
        id: 'mode_711_blockchain',
        name: 'Blockchain',
        description: 'Mode 711: Blockchain visualization',
        category: 'Scientific',
        mode: 711,
        tags: ["blockchain"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_712_hash_function: {
        id: 'mode_712_hash_function',
        name: 'Hash Function',
        description: 'Mode 712: Hash function visualization',
        category: 'Space & Cosmic',
        mode: 712,
        tags: ["hash", "function"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_713_encryption: {
        id: 'mode_713_encryption',
        name: 'Encryption',
        description: 'Mode 713: Encryption visualization',
        category: 'Space & Cosmic',
        mode: 713,
        tags: ["encryption"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_714_public_key: {
        id: 'mode_714_public_key',
        name: 'Public Key',
        description: 'Mode 714: Public key visualization',
        category: 'Geometric',
        mode: 714,
        tags: ["public"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_715_digital_signature: {
        id: 'mode_715_digital_signature',
        name: 'Digital Signature',
        description: 'Mode 715: Digital signature visualization',
        category: 'Nature',
        mode: 715,
        tags: ["digital", "signature"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_716_zero_knowledge_proof: {
        id: 'mode_716_zero_knowledge_proof',
        name: 'Zero Knowledge Proof',
        description: 'Mode 716: Zero knowledge proof visualization',
        category: 'Geometric',
        mode: 716,
        tags: ["zero", "knowledge", "proof"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_717_homomorphic_encryption: {
        id: 'mode_717_homomorphic_encryption',
        name: 'Homomorphic Encryption',
        description: 'Mode 717: Homomorphic encryption visualization',
        category: 'Geometric',
        mode: 717,
        tags: ["homomorphic", "encryption"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_718_secure_multiparty_computation: {
        id: 'mode_718_secure_multiparty_computation',
        name: 'Secure Multiparty Computation',
        description: 'Mode 718: Secure multiparty computation visualization',
        category: 'Geometric',
        mode: 718,
        tags: ["secure", "multiparty", "computation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_719_differential_privacy: {
        id: 'mode_719_differential_privacy',
        name: 'Differential Privacy',
        description: 'Mode 719: Differential privacy visualization',
        category: 'Geometric',
        mode: 719,
        tags: ["differential", "privacy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_720_federated_learning: {
        id: 'mode_720_federated_learning',
        name: 'Federated Learning',
        description: 'Mode 720: Federated learning visualization',
        category: 'Geometric',
        mode: 720,
        tags: ["federated", "learning"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_721_neural_network: {
        id: 'mode_721_neural_network',
        name: 'Neural Network',
        description: 'Mode 721: Neural network visualization',
        category: 'Scientific',
        mode: 721,
        tags: ["neural", "network"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_722_deep_learning: {
        id: 'mode_722_deep_learning',
        name: 'Deep Learning',
        description: 'Mode 722: Deep learning visualization',
        category: 'Geometric',
        mode: 722,
        tags: ["deep", "learning"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_723_convolutional_layer: {
        id: 'mode_723_convolutional_layer',
        name: 'Convolutional Layer',
        description: 'Mode 723: Convolutional layer visualization',
        category: 'Geometric',
        mode: 723,
        tags: ["convolutional", "layer"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_724_recurrent_connection: {
        id: 'mode_724_recurrent_connection',
        name: 'Recurrent Connection',
        description: 'Mode 724: Recurrent connection visualization',
        category: 'Geometric',
        mode: 724,
        tags: ["recurrent", "connection"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_725_attention_mechanism: {
        id: 'mode_725_attention_mechanism',
        name: 'Attention Mechanism',
        description: 'Mode 725: Attention mechanism visualization',
        category: 'Geometric',
        mode: 725,
        tags: ["attention", "mechanism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_726_transformer_architecture: {
        id: 'mode_726_transformer_architecture',
        name: 'Transformer Architecture',
        description: 'Mode 726: Transformer architecture visualization',
        category: 'Geometric',
        mode: 726,
        tags: ["transformer", "architecture"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_727_residual_connection: {
        id: 'mode_727_residual_connection',
        name: 'Residual Connection',
        description: 'Mode 727: Residual connection visualization',
        category: 'Geometric',
        mode: 727,
        tags: ["residual", "connection"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_728_skip_connection: {
        id: 'mode_728_skip_connection',
        name: 'Skip Connection',
        description: 'Mode 728: Skip connection visualization',
        category: 'Geometric',
        mode: 728,
        tags: ["skip", "connection"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_729_batch_normalization: {
        id: 'mode_729_batch_normalization',
        name: 'Batch Normalization',
        description: 'Mode 729: Batch normalization visualization',
        category: 'Geometric',
        mode: 729,
        tags: ["batch", "normalization"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_730_dropout_regularization: {
        id: 'mode_730_dropout_regularization',
        name: 'Dropout Regularization',
        description: 'Mode 730: Dropout regularization visualization',
        category: 'Geometric',
        mode: 730,
        tags: ["dropout", "regularization"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_731_activation_function: {
        id: 'mode_731_activation_function',
        name: 'Activation Function',
        description: 'Mode 731: Activation function visualization',
        category: 'Geometric',
        mode: 731,
        tags: ["activation", "function"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_732_gradient_descent: {
        id: 'mode_732_gradient_descent',
        name: 'Gradient Descent',
        description: 'Mode 732: Gradient descent visualization',
        category: 'Geometric',
        mode: 732,
        tags: ["gradient", "descent"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_733_backpropagation: {
        id: 'mode_733_backpropagation',
        name: 'Backpropagation',
        description: 'Mode 733: Backpropagation visualization',
        category: 'Geometric',
        mode: 733,
        tags: ["backpropagation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_734_loss_landscape: {
        id: 'mode_734_loss_landscape',
        name: 'Loss Landscape',
        description: 'Mode 734: Loss landscape visualization',
        category: 'Geometric',
        mode: 734,
        tags: ["loss", "landscape"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_735_optimizer_trajectory: {
        id: 'mode_735_optimizer_trajectory',
        name: 'Optimizer Trajectory',
        description: 'Mode 735: Optimizer trajectory visualization',
        category: 'Geometric',
        mode: 735,
        tags: ["optimizer", "trajectory"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_736_learning_rate_schedule: {
        id: 'mode_736_learning_rate_schedule',
        name: 'Learning Rate Schedule',
        description: 'Mode 736: Learning rate schedule visualization',
        category: 'Geometric',
        mode: 736,
        tags: ["learning", "rate", "schedule"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_737_momentum: {
        id: 'mode_737_momentum',
        name: 'Momentum',
        description: 'Mode 737: Momentum visualization',
        category: 'Geometric',
        mode: 737,
        tags: ["momentum"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_738_adaptive_learning: {
        id: 'mode_738_adaptive_learning',
        name: 'Adaptive Learning',
        description: 'Mode 738: Adaptive learning visualization',
        category: 'Geometric',
        mode: 738,
        tags: ["adaptive", "learning"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_739_weight_decay: {
        id: 'mode_739_weight_decay',
        name: 'Weight Decay',
        description: 'Mode 739: Weight decay visualization',
        category: 'Geometric',
        mode: 739,
        tags: ["weight", "decay"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_740_early_stopping: {
        id: 'mode_740_early_stopping',
        name: 'Early Stopping',
        description: 'Mode 740: Early stopping visualization',
        category: 'Geometric',
        mode: 740,
        tags: ["early", "stopping"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_741_cross_validation: {
        id: 'mode_741_cross_validation',
        name: 'Cross Validation',
        description: 'Mode 741: Cross validation visualization',
        category: 'Geometric',
        mode: 741,
        tags: ["cross", "validation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_742_ensemble_method: {
        id: 'mode_742_ensemble_method',
        name: 'Ensemble Method',
        description: 'Mode 742: Ensemble method visualization',
        category: 'Geometric',
        mode: 742,
        tags: ["ensemble", "method"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_743_boosting: {
        id: 'mode_743_boosting',
        name: 'Boosting',
        description: 'Mode 743: Boosting visualization',
        category: 'Geometric',
        mode: 743,
        tags: ["boosting"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_744_bagging: {
        id: 'mode_744_bagging',
        name: 'Bagging',
        description: 'Mode 744: Bagging visualization',
        category: 'Geometric',
        mode: 744,
        tags: ["bagging"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_745_random_forest: {
        id: 'mode_745_random_forest',
        name: 'Random Forest',
        description: 'Mode 745: Random forest visualization',
        category: 'Nature',
        mode: 745,
        tags: ["random", "forest"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_746_decision_tree: {
        id: 'mode_746_decision_tree',
        name: 'Decision Tree',
        description: 'Mode 746: Decision tree visualization',
        category: 'Nature',
        mode: 746,
        tags: ["decision", "tree"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_747_support_vector_machine: {
        id: 'mode_747_support_vector_machine',
        name: 'Support Vector Machine',
        description: 'Mode 747: Support vector machine visualization',
        category: 'Geometric',
        mode: 747,
        tags: ["support", "vector", "machine"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_748_kernel_trick: {
        id: 'mode_748_kernel_trick',
        name: 'Kernel Trick',
        description: 'Mode 748: Kernel trick visualization',
        category: 'Geometric',
        mode: 748,
        tags: ["kernel", "trick"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_749_feature_space: {
        id: 'mode_749_feature_space',
        name: 'Feature Space',
        description: 'Mode 749: Feature space visualization',
        category: 'Geometric',
        mode: 749,
        tags: ["feature", "space"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_750_dimensionality_reduction: {
        id: 'mode_750_dimensionality_reduction',
        name: 'Dimensionality Reduction',
        description: 'Mode 750: Dimensionality reduction visualization',
        category: 'Geometric',
        mode: 750,
        tags: ["dimensionality", "reduction"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_751_principal_component_analysis: {
        id: 'mode_751_principal_component_analysis',
        name: 'Principal Component Analysis',
        description: 'Mode 751: Principal component analysis visualization',
        category: 'Geometric',
        mode: 751,
        tags: ["principal", "component", "analysis"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_752_t_sne_embedding: {
        id: 'mode_752_t_sne_embedding',
        name: 'T Sne Embedding',
        description: 'Mode 752: T-sne embedding visualization',
        category: 'Geometric',
        mode: 752,
        tags: ["embedding"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_753_autoencoder_latent_space: {
        id: 'mode_753_autoencoder_latent_space',
        name: 'Autoencoder Latent Space',
        description: 'Mode 753: Autoencoder latent space visualization',
        category: 'Geometric',
        mode: 753,
        tags: ["autoencoder", "latent", "space"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_754_variational_autoencoder: {
        id: 'mode_754_variational_autoencoder',
        name: 'Variational Autoencoder',
        description: 'Mode 754: Variational autoencoder visualization',
        category: 'Geometric',
        mode: 754,
        tags: ["variational", "autoencoder"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_755_generative_adversarial_network: {
        id: 'mode_755_generative_adversarial_network',
        name: 'Generative Adversarial Network',
        description: 'Mode 755: Generative adversarial network visualization',
        category: 'Geometric',
        mode: 755,
        tags: ["generative", "adversarial", "network"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_756_discriminator_network: {
        id: 'mode_756_discriminator_network',
        name: 'Discriminator Network',
        description: 'Mode 756: Discriminator network visualization',
        category: 'Geometric',
        mode: 756,
        tags: ["discriminator", "network"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_757_generator_network: {
        id: 'mode_757_generator_network',
        name: 'Generator Network',
        description: 'Mode 757: Generator network visualization',
        category: 'Geometric',
        mode: 757,
        tags: ["generator", "network"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_758_style_transfer: {
        id: 'mode_758_style_transfer',
        name: 'Style Transfer',
        description: 'Mode 758: Style transfer visualization',
        category: 'Geometric',
        mode: 758,
        tags: ["style", "transfer"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_759_content_loss: {
        id: 'mode_759_content_loss',
        name: 'Content Loss',
        description: 'Mode 759: Content loss visualization',
        category: 'Geometric',
        mode: 759,
        tags: ["content", "loss"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_760_gram_matrix: {
        id: 'mode_760_gram_matrix',
        name: 'Gram Matrix',
        description: 'Mode 760: Gram matrix visualization',
        category: 'Tech',
        mode: 760,
        tags: ["gram", "matrix"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_761_perceptual_loss: {
        id: 'mode_761_perceptual_loss',
        name: 'Perceptual Loss',
        description: 'Mode 761: Perceptual loss visualization',
        category: 'Geometric',
        mode: 761,
        tags: ["perceptual", "loss"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_762_adversarial_loss: {
        id: 'mode_762_adversarial_loss',
        name: 'Adversarial Loss',
        description: 'Mode 762: Adversarial loss visualization',
        category: 'Geometric',
        mode: 762,
        tags: ["adversarial", "loss"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_763_cycle_consistency: {
        id: 'mode_763_cycle_consistency',
        name: 'Cycle Consistency',
        description: 'Mode 763: Cycle consistency visualization',
        category: 'Geometric',
        mode: 763,
        tags: ["cycle", "consistency"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_764_identity_loss: {
        id: 'mode_764_identity_loss',
        name: 'Identity Loss',
        description: 'Mode 764: Identity loss visualization',
        category: 'Geometric',
        mode: 764,
        tags: ["identity", "loss"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_765_reconstruction_loss: {
        id: 'mode_765_reconstruction_loss',
        name: 'Reconstruction Loss',
        description: 'Mode 765: Reconstruction loss visualization',
        category: 'Geometric',
        mode: 765,
        tags: ["reconstruction", "loss"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_766_kl_divergence: {
        id: 'mode_766_kl_divergence',
        name: 'Kl Divergence',
        description: 'Mode 766: Kl divergence visualization',
        category: 'Geometric',
        mode: 766,
        tags: ["divergence"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_767_wasserstein_distance: {
        id: 'mode_767_wasserstein_distance',
        name: 'Wasserstein Distance',
        description: 'Mode 767: Wasserstein distance visualization',
        category: 'Geometric',
        mode: 767,
        tags: ["wasserstein", "distance"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_768_earth_mover_distance: {
        id: 'mode_768_earth_mover_distance',
        name: 'Earth Mover Distance',
        description: 'Mode 768: Earth mover distance visualization',
        category: 'Geometric',
        mode: 768,
        tags: ["earth", "mover", "distance"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_769_inception_score: {
        id: 'mode_769_inception_score',
        name: 'Inception Score',
        description: 'Mode 769: Inception score visualization',
        category: 'Geometric',
        mode: 769,
        tags: ["inception", "score"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_770_frechet_inception_distance: {
        id: 'mode_770_frechet_inception_distance',
        name: 'Frechet Inception Distance',
        description: 'Mode 770: Frechet inception distance visualization',
        category: 'Geometric',
        mode: 770,
        tags: ["frechet", "inception", "distance"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_771_bleu_score: {
        id: 'mode_771_bleu_score',
        name: 'Bleu Score',
        description: 'Mode 771: Bleu score visualization',
        category: 'Geometric',
        mode: 771,
        tags: ["bleu", "score"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_772_rouge_score: {
        id: 'mode_772_rouge_score',
        name: 'Rouge Score',
        description: 'Mode 772: Rouge score visualization',
        category: 'Geometric',
        mode: 772,
        tags: ["rouge", "score"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_773_perplexity: {
        id: 'mode_773_perplexity',
        name: 'Perplexity',
        description: 'Mode 773: Perplexity visualization',
        category: 'Geometric',
        mode: 773,
        tags: ["perplexity"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_774_cross_entropy: {
        id: 'mode_774_cross_entropy',
        name: 'Cross Entropy',
        description: 'Mode 774: Cross entropy visualization',
        category: 'Geometric',
        mode: 774,
        tags: ["cross", "entropy"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_775_mutual_information: {
        id: 'mode_775_mutual_information',
        name: 'Mutual Information',
        description: 'Mode 775: Mutual information visualization',
        category: 'Geometric',
        mode: 775,
        tags: ["mutual", "information"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_776_information_bottleneck: {
        id: 'mode_776_information_bottleneck',
        name: 'Information Bottleneck',
        description: 'Mode 776: Information bottleneck visualization',
        category: 'Geometric',
        mode: 776,
        tags: ["information", "bottleneck"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_777_rate_distortion: {
        id: 'mode_777_rate_distortion',
        name: 'Rate Distortion',
        description: 'Mode 777: Rate distortion visualization',
        category: 'Geometric',
        mode: 777,
        tags: ["rate", "distortion"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_778_source_coding: {
        id: 'mode_778_source_coding',
        name: 'Source Coding',
        description: 'Mode 778: Source coding visualization',
        category: 'Geometric',
        mode: 778,
        tags: ["source", "coding"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_779_channel_coding: {
        id: 'mode_779_channel_coding',
        name: 'Channel Coding',
        description: 'Mode 779: Channel coding visualization',
        category: 'Geometric',
        mode: 779,
        tags: ["channel", "coding"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_780_error_correction: {
        id: 'mode_780_error_correction',
        name: 'Error Correction',
        description: 'Mode 780: Error correction visualization',
        category: 'Geometric',
        mode: 780,
        tags: ["error", "correction"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_781_hamming_distance: {
        id: 'mode_781_hamming_distance',
        name: 'Hamming Distance',
        description: 'Mode 781: Hamming distance visualization',
        category: 'Geometric',
        mode: 781,
        tags: ["hamming", "distance"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_782_reed_solomon: {
        id: 'mode_782_reed_solomon',
        name: 'Reed Solomon',
        description: 'Mode 782: Reed solomon visualization',
        category: 'Geometric',
        mode: 782,
        tags: ["reed", "solomon"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_783_turbo_code: {
        id: 'mode_783_turbo_code',
        name: 'Turbo Code',
        description: 'Mode 783: Turbo code visualization',
        category: 'Geometric',
        mode: 783,
        tags: ["turbo", "code"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_784_ldpc_code: {
        id: 'mode_784_ldpc_code',
        name: 'Ldpc Code',
        description: 'Mode 784: Ldpc code visualization',
        category: 'Geometric',
        mode: 784,
        tags: ["ldpc", "code"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_785_polar_code: {
        id: 'mode_785_polar_code',
        name: 'Polar Code',
        description: 'Mode 785: Polar code visualization',
        category: 'Geometric',
        mode: 785,
        tags: ["polar", "code"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_786_quantum_error_correction: {
        id: 'mode_786_quantum_error_correction',
        name: 'Quantum Error Correction',
        description: 'Mode 786: Quantum error correction visualization',
        category: 'Scientific',
        mode: 786,
        tags: ["quantum", "error", "correction"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_787_surface_code: {
        id: 'mode_787_surface_code',
        name: 'Surface Code',
        description: 'Mode 787: Surface code visualization',
        category: 'Geometric',
        mode: 787,
        tags: ["surface", "code"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_788_toric_code: {
        id: 'mode_788_toric_code',
        name: 'Toric Code',
        description: 'Mode 788: Toric code visualization',
        category: 'Geometric',
        mode: 788,
        tags: ["toric", "code"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_789_color_code: {
        id: 'mode_789_color_code',
        name: 'Color Code',
        description: 'Mode 789: Color code visualization',
        category: 'Geometric',
        mode: 789,
        tags: ["color", "code"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_790_stabilizer_formalism: {
        id: 'mode_790_stabilizer_formalism',
        name: 'Stabilizer Formalism',
        description: 'Mode 790: Stabilizer formalism visualization',
        category: 'Geometric',
        mode: 790,
        tags: ["stabilizer", "formalism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_791_clifford_gate: {
        id: 'mode_791_clifford_gate',
        name: 'Clifford Gate',
        description: 'Mode 791: Clifford gate visualization',
        category: 'Geometric',
        mode: 791,
        tags: ["clifford", "gate"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_792_pauli_group: {
        id: 'mode_792_pauli_group',
        name: 'Pauli Group',
        description: 'Mode 792: Pauli group visualization',
        category: 'Geometric',
        mode: 792,
        tags: ["pauli", "group"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_793_measurement_based_quantum_computing: {
        id: 'mode_793_measurement_based_quantum_computing',
        name: 'Measurement Based Quantum Computing',
        description: 'Mode 793: Measurement based quantum computing visualization',
        category: 'Scientific',
        mode: 793,
        tags: ["measurement", "based", "quantum"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_794_one_way_quantum_computer: {
        id: 'mode_794_one_way_quantum_computer',
        name: 'One Way Quantum Computer',
        description: 'Mode 794: One way quantum computer visualization',
        category: 'Scientific',
        mode: 794,
        tags: ["quantum", "computer"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_795_adiabatic_quantum_computation: {
        id: 'mode_795_adiabatic_quantum_computation',
        name: 'Adiabatic Quantum Computation',
        description: 'Mode 795: Adiabatic quantum computation visualization',
        category: 'Scientific',
        mode: 795,
        tags: ["adiabatic", "quantum", "computation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_796_quantum_annealing: {
        id: 'mode_796_quantum_annealing',
        name: 'Quantum Annealing',
        description: 'Mode 796: Quantum annealing visualization',
        category: 'Scientific',
        mode: 796,
        tags: ["quantum", "annealing"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_797_variational_quantum_eigensolver: {
        id: 'mode_797_variational_quantum_eigensolver',
        name: 'Variational Quantum Eigensolver',
        description: 'Mode 797: Variational quantum eigensolver visualization',
        category: 'Scientific',
        mode: 797,
        tags: ["variational", "quantum", "eigensolver"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_798_quantum_approximate_optimization: {
        id: 'mode_798_quantum_approximate_optimization',
        name: 'Quantum Approximate Optimization',
        description: 'Mode 798: Quantum approximate optimization visualization',
        category: 'Scientific',
        mode: 798,
        tags: ["quantum", "approximate", "optimization"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_799_quantum_phase_estimation: {
        id: 'mode_799_quantum_phase_estimation',
        name: 'Quantum Phase Estimation',
        description: 'Mode 799: Quantum phase estimation visualization',
        category: 'Scientific',
        mode: 799,
        tags: ["quantum", "phase", "estimation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_800_quantum_fourier_transform: {
        id: 'mode_800_quantum_fourier_transform',
        name: 'Quantum Fourier Transform',
        description: 'Mode 800: Quantum fourier transform visualization',
        category: 'Scientific',
        mode: 800,
        tags: ["quantum", "fourier", "transform"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_801_mandala: {
        id: 'mode_801_mandala',
        name: 'Mandala',
        description: 'Mode 801: Mandala visualization',
        category: 'Geometric',
        mode: 801,
        tags: ["mandala"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_802_yantra: {
        id: 'mode_802_yantra',
        name: 'Yantra',
        description: 'Mode 802: Yantra visualization',
        category: 'Geometric',
        mode: 802,
        tags: ["yantra"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_803_lotus: {
        id: 'mode_803_lotus',
        name: 'Lotus',
        description: 'Mode 803: Lotus visualization',
        category: 'Geometric',
        mode: 803,
        tags: ["lotus"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_804_om_symbol: {
        id: 'mode_804_om_symbol',
        name: 'Om Symbol',
        description: 'Mode 804: Om symbol visualization',
        category: 'Geometric',
        mode: 804,
        tags: ["symbol"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_805_chakra: {
        id: 'mode_805_chakra',
        name: 'Chakra',
        description: 'Mode 805: Chakra visualization',
        category: 'Geometric',
        mode: 805,
        tags: ["chakra"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_806_aura_field: {
        id: 'mode_806_aura_field',
        name: 'Aura Field',
        description: 'Mode 806: Aura field visualization',
        category: 'Geometric',
        mode: 806,
        tags: ["aura", "field"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_807_third_eye: {
        id: 'mode_807_third_eye',
        name: 'Third Eye',
        description: 'Mode 807: Third eye visualization',
        category: 'Geometric',
        mode: 807,
        tags: ["third"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_808_kundalini: {
        id: 'mode_808_kundalini',
        name: 'Kundalini',
        description: 'Mode 808: Kundalini visualization',
        category: 'Geometric',
        mode: 808,
        tags: ["kundalini"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_809_merkaba: {
        id: 'mode_809_merkaba',
        name: 'Merkaba',
        description: 'Mode 809: Merkaba visualization',
        category: 'Geometric',
        mode: 809,
        tags: ["merkaba"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_810_flower_of_life: {
        id: 'mode_810_flower_of_life',
        name: 'Flower Of Life',
        description: 'Mode 810: Flower of life visualization',
        category: 'Nature',
        mode: 810,
        tags: ["flower", "life"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_811_seed_of_life: {
        id: 'mode_811_seed_of_life',
        name: 'Seed Of Life',
        description: 'Mode 811: Seed of life visualization',
        category: 'Geometric',
        mode: 811,
        tags: ["seed", "life"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_812_tree_of_life: {
        id: 'mode_812_tree_of_life',
        name: 'Tree Of Life',
        description: 'Mode 812: Tree of life visualization',
        category: 'Nature',
        mode: 812,
        tags: ["tree", "life"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_813_metatron_cube: {
        id: 'mode_813_metatron_cube',
        name: 'Metatron Cube',
        description: 'Mode 813: Metatron cube visualization',
        category: 'Geometric',
        mode: 813,
        tags: ["metatron", "cube"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_814_sri_yantra: {
        id: 'mode_814_sri_yantra',
        name: 'Sri Yantra',
        description: 'Mode 814: Sri yantra visualization',
        category: 'Geometric',
        mode: 814,
        tags: ["yantra"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_815_shri_yantra: {
        id: 'mode_815_shri_yantra',
        name: 'Shri Yantra',
        description: 'Mode 815: Shri yantra visualization',
        category: 'Geometric',
        mode: 815,
        tags: ["shri", "yantra"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_816_tibetan_sand_mandala: {
        id: 'mode_816_tibetan_sand_mandala',
        name: 'Tibetan Sand Mandala',
        description: 'Mode 816: Tibetan sand mandala visualization',
        category: 'Geometric',
        mode: 816,
        tags: ["tibetan", "sand", "mandala"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_817_zen_circle: {
        id: 'mode_817_zen_circle',
        name: 'Zen Circle',
        description: 'Mode 817: Zen circle visualization',
        category: 'Geometric',
        mode: 817,
        tags: ["circle"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_818_yin_yang: {
        id: 'mode_818_yin_yang',
        name: 'Yin Yang',
        description: 'Mode 818: Yin yang visualization',
        category: 'Geometric',
        mode: 818,
        tags: ["yang"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_819_tao_symbol: {
        id: 'mode_819_tao_symbol',
        name: 'Tao Symbol',
        description: 'Mode 819: Tao symbol visualization',
        category: 'Geometric',
        mode: 819,
        tags: ["symbol"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_820_bagua: {
        id: 'mode_820_bagua',
        name: 'Bagua',
        description: 'Mode 820: Bagua visualization',
        category: 'Geometric',
        mode: 820,
        tags: ["bagua"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_821_i_ching_hexagram: {
        id: 'mode_821_i_ching_hexagram',
        name: 'I Ching Hexagram',
        description: 'Mode 821: I ching hexagram visualization',
        category: 'Geometric',
        mode: 821,
        tags: ["ching", "hexagram"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_822_trigram: {
        id: 'mode_822_trigram',
        name: 'Trigram',
        description: 'Mode 822: Trigram visualization',
        category: 'Geometric',
        mode: 822,
        tags: ["trigram"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_823_medicine_wheel: {
        id: 'mode_823_medicine_wheel',
        name: 'Medicine Wheel',
        description: 'Mode 823: Medicine wheel visualization',
        category: 'Geometric',
        mode: 823,
        tags: ["medicine", "wheel"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_824_dreamcatcher: {
        id: 'mode_824_dreamcatcher',
        name: 'Dreamcatcher',
        description: 'Mode 824: Dreamcatcher visualization',
        category: 'Geometric',
        mode: 824,
        tags: ["dreamcatcher"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_825_totem: {
        id: 'mode_825_totem',
        name: 'Totem',
        description: 'Mode 825: Totem visualization',
        category: 'Geometric',
        mode: 825,
        tags: ["totem"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_826_spirit_animal: {
        id: 'mode_826_spirit_animal',
        name: 'Spirit Animal',
        description: 'Mode 826: Spirit animal visualization',
        category: 'Geometric',
        mode: 826,
        tags: ["spirit", "animal"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_827_shamanic_journey: {
        id: 'mode_827_shamanic_journey',
        name: 'Shamanic Journey',
        description: 'Mode 827: Shamanic journey visualization',
        category: 'Geometric',
        mode: 827,
        tags: ["shamanic", "journey"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_828_ayahuasca_vision: {
        id: 'mode_828_ayahuasca_vision',
        name: 'Ayahuasca Vision',
        description: 'Mode 828: Ayahuasca vision visualization',
        category: 'Geometric',
        mode: 828,
        tags: ["ayahuasca", "vision"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_829_dmt_realm: {
        id: 'mode_829_dmt_realm',
        name: 'Dmt Realm',
        description: 'Mode 829: Dmt realm visualization',
        category: 'Geometric',
        mode: 829,
        tags: ["realm"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_830_astral_projection: {
        id: 'mode_830_astral_projection',
        name: 'Astral Projection',
        description: 'Mode 830: Astral projection visualization',
        category: 'Geometric',
        mode: 830,
        tags: ["astral", "projection"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_831_out_of_body_experience: {
        id: 'mode_831_out_of_body_experience',
        name: 'Out Of Body Experience',
        description: 'Mode 831: Out of body experience visualization',
        category: 'Geometric',
        mode: 831,
        tags: ["body", "experience"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_832_near_death_experience: {
        id: 'mode_832_near_death_experience',
        name: 'Near Death Experience',
        description: 'Mode 832: Near death experience visualization',
        category: 'Geometric',
        mode: 832,
        tags: ["near", "death", "experience"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_833_tunnel_of_light: {
        id: 'mode_833_tunnel_of_light',
        name: 'Tunnel Of Light',
        description: 'Mode 833: Tunnel of light visualization',
        category: 'Geometric',
        mode: 833,
        tags: ["tunnel", "light"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_834_life_review: {
        id: 'mode_834_life_review',
        name: 'Life Review',
        description: 'Mode 834: Life review visualization',
        category: 'Geometric',
        mode: 834,
        tags: ["life", "review"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_835_soul_retrieval: {
        id: 'mode_835_soul_retrieval',
        name: 'Soul Retrieval',
        description: 'Mode 835: Soul retrieval visualization',
        category: 'Geometric',
        mode: 835,
        tags: ["soul", "retrieval"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_836_past_life_regression: {
        id: 'mode_836_past_life_regression',
        name: 'Past Life Regression',
        description: 'Mode 836: Past life regression visualization',
        category: 'Geometric',
        mode: 836,
        tags: ["past", "life", "regression"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_837_akashic_records: {
        id: 'mode_837_akashic_records',
        name: 'Akashic Records',
        description: 'Mode 837: Akashic records visualization',
        category: 'Geometric',
        mode: 837,
        tags: ["akashic", "records"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_838_collective_unconscious: {
        id: 'mode_838_collective_unconscious',
        name: 'Collective Unconscious',
        description: 'Mode 838: Collective unconscious visualization',
        category: 'Geometric',
        mode: 838,
        tags: ["collective", "unconscious"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_839_archetypal_realm: {
        id: 'mode_839_archetypal_realm',
        name: 'Archetypal Realm',
        description: 'Mode 839: Archetypal realm visualization',
        category: 'Geometric',
        mode: 839,
        tags: ["archetypal", "realm"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_840_synchronicity: {
        id: 'mode_840_synchronicity',
        name: 'Synchronicity',
        description: 'Mode 840: Synchronicity visualization',
        category: 'Geometric',
        mode: 840,
        tags: ["synchronicity"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_841_meaningful_coincidence: {
        id: 'mode_841_meaningful_coincidence',
        name: 'Meaningful Coincidence',
        description: 'Mode 841: Meaningful coincidence visualization',
        category: 'Geometric',
        mode: 841,
        tags: ["meaningful", "coincidence"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_842_serendipity: {
        id: 'mode_842_serendipity',
        name: 'Serendipity',
        description: 'Mode 842: Serendipity visualization',
        category: 'Geometric',
        mode: 842,
        tags: ["serendipity"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_843_providence: {
        id: 'mode_843_providence',
        name: 'Providence',
        description: 'Mode 843: Providence visualization',
        category: 'Geometric',
        mode: 843,
        tags: ["providence"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_844_fate: {
        id: 'mode_844_fate',
        name: 'Fate',
        description: 'Mode 844: Fate visualization',
        category: 'Geometric',
        mode: 844,
        tags: ["fate"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_845_destiny: {
        id: 'mode_845_destiny',
        name: 'Destiny',
        description: 'Mode 845: Destiny visualization',
        category: 'Geometric',
        mode: 845,
        tags: ["destiny"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_846_karma: {
        id: 'mode_846_karma',
        name: 'Karma',
        description: 'Mode 846: Karma visualization',
        category: 'Geometric',
        mode: 846,
        tags: ["karma"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_847_dharma: {
        id: 'mode_847_dharma',
        name: 'Dharma',
        description: 'Mode 847: Dharma visualization',
        category: 'Geometric',
        mode: 847,
        tags: ["dharma"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_848_samsara: {
        id: 'mode_848_samsara',
        name: 'Samsara',
        description: 'Mode 848: Samsara visualization',
        category: 'Geometric',
        mode: 848,
        tags: ["samsara"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_849_nirvana: {
        id: 'mode_849_nirvana',
        name: 'Nirvana',
        description: 'Mode 849: Nirvana visualization',
        category: 'Geometric',
        mode: 849,
        tags: ["nirvana"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_850_enlightenment: {
        id: 'mode_850_enlightenment',
        name: 'Enlightenment',
        description: 'Mode 850: Enlightenment visualization',
        category: 'Geometric',
        mode: 850,
        tags: ["enlightenment"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_851_samadhi: {
        id: 'mode_851_samadhi',
        name: 'Samadhi',
        description: 'Mode 851: Samadhi visualization',
        category: 'Geometric',
        mode: 851,
        tags: ["samadhi"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_852_satori: {
        id: 'mode_852_satori',
        name: 'Satori',
        description: 'Mode 852: Satori visualization',
        category: 'Geometric',
        mode: 852,
        tags: ["satori"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_853_kensho: {
        id: 'mode_853_kensho',
        name: 'Kensho',
        description: 'Mode 853: Kensho visualization',
        category: 'Geometric',
        mode: 853,
        tags: ["kensho"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_854_moksha: {
        id: 'mode_854_moksha',
        name: 'Moksha',
        description: 'Mode 854: Moksha visualization',
        category: 'Geometric',
        mode: 854,
        tags: ["moksha"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_855_liberation: {
        id: 'mode_855_liberation',
        name: 'Liberation',
        description: 'Mode 855: Liberation visualization',
        category: 'Geometric',
        mode: 855,
        tags: ["liberation"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_856_self_realization: {
        id: 'mode_856_self_realization',
        name: 'Self Realization',
        description: 'Mode 856: Self realization visualization',
        category: 'Geometric',
        mode: 856,
        tags: ["self", "realization"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_857_god_consciousness: {
        id: 'mode_857_god_consciousness',
        name: 'God Consciousness',
        description: 'Mode 857: God consciousness visualization',
        category: 'Geometric',
        mode: 857,
        tags: ["consciousness"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_858_cosmic_consciousness: {
        id: 'mode_858_cosmic_consciousness',
        name: 'Cosmic Consciousness',
        description: 'Mode 858: Cosmic consciousness visualization',
        category: 'Geometric',
        mode: 858,
        tags: ["cosmic", "consciousness"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_859_unity_consciousness: {
        id: 'mode_859_unity_consciousness',
        name: 'Unity Consciousness',
        description: 'Mode 859: Unity consciousness visualization',
        category: 'Geometric',
        mode: 859,
        tags: ["unity", "consciousness"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_860_non_dual_awareness: {
        id: 'mode_860_non_dual_awareness',
        name: 'Non Dual Awareness',
        description: 'Mode 860: Non-dual awareness visualization',
        category: 'Geometric',
        mode: 860,
        tags: ["dual", "awareness"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_861_witness_consciousness: {
        id: 'mode_861_witness_consciousness',
        name: 'Witness Consciousness',
        description: 'Mode 861: Witness consciousness visualization',
        category: 'Geometric',
        mode: 861,
        tags: ["witness", "consciousness"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_862_pure_awareness: {
        id: 'mode_862_pure_awareness',
        name: 'Pure Awareness',
        description: 'Mode 862: Pure awareness visualization',
        category: 'Geometric',
        mode: 862,
        tags: ["pure", "awareness"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_863_presence: {
        id: 'mode_863_presence',
        name: 'Presence',
        description: 'Mode 863: Presence visualization',
        category: 'Geometric',
        mode: 863,
        tags: ["presence"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_864_now_moment: {
        id: 'mode_864_now_moment',
        name: 'Now Moment',
        description: 'Mode 864: Now moment visualization',
        category: 'Geometric',
        mode: 864,
        tags: ["moment"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_865_eternal_present: {
        id: 'mode_865_eternal_present',
        name: 'Eternal Present',
        description: 'Mode 865: Eternal present visualization',
        category: 'Geometric',
        mode: 865,
        tags: ["eternal", "present"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_866_timeless_being: {
        id: 'mode_866_timeless_being',
        name: 'Timeless Being',
        description: 'Mode 866: Timeless being visualization',
        category: 'Geometric',
        mode: 866,
        tags: ["timeless", "being"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_867_infinite_space: {
        id: 'mode_867_infinite_space',
        name: 'Infinite Space',
        description: 'Mode 867: Infinite space visualization',
        category: 'Geometric',
        mode: 867,
        tags: ["infinite", "space"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_868_boundless_compassion: {
        id: 'mode_868_boundless_compassion',
        name: 'Boundless Compassion',
        description: 'Mode 868: Boundless compassion visualization',
        category: 'Geometric',
        mode: 868,
        tags: ["boundless", "compassion"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_869_unconditional_love: {
        id: 'mode_869_unconditional_love',
        name: 'Unconditional Love',
        description: 'Mode 869: Unconditional love visualization',
        category: 'Geometric',
        mode: 869,
        tags: ["unconditional", "love"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_870_divine_grace: {
        id: 'mode_870_divine_grace',
        name: 'Divine Grace',
        description: 'Mode 870: Divine grace visualization',
        category: 'Geometric',
        mode: 870,
        tags: ["divine", "grace"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_871_holy_spirit: {
        id: 'mode_871_holy_spirit',
        name: 'Holy Spirit',
        description: 'Mode 871: Holy spirit visualization',
        category: 'Geometric',
        mode: 871,
        tags: ["holy", "spirit"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_872_shekinah: {
        id: 'mode_872_shekinah',
        name: 'Shekinah',
        description: 'Mode 872: Shekinah visualization',
        category: 'Geometric',
        mode: 872,
        tags: ["shekinah"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_873_divine_feminine: {
        id: 'mode_873_divine_feminine',
        name: 'Divine Feminine',
        description: 'Mode 873: Divine feminine visualization',
        category: 'Geometric',
        mode: 873,
        tags: ["divine", "feminine"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_874_goddess_energy: {
        id: 'mode_874_goddess_energy',
        name: 'Goddess Energy',
        description: 'Mode 874: Flowing ethereal energy with graceful ribbons and divine aura',
        category: 'Energy',
        mode: 874,
        tags: ["goddess", "energy", "ethereal", "flowing", "divine", "elegant"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            flowSpeed: { min: 0.3, max: 3, default: 1.2, label: 'Flow Speed' },
            ribbonCount: { min: 3, max: 12, default: 6, label: 'Energy Ribbons' },
            auraSize: { min: 0.5, max: 2, default: 1, label: 'Aura Size' },
            gracefulness: { min: 0.3, max: 2, default: 1, label: 'Flow Gracefulness' },
            glowIntensity: { min: 10, max: 50, default: 30, label: 'Glow Intensity' }
        }
    },
    mode_875_sacred_masculine: {
        id: 'mode_875_sacred_masculine',
        name: 'Sacred Masculine',
        description: 'Mode 875: Sacred masculine visualization',
        category: 'Geometric',
        mode: 875,
        tags: ["sacred", "masculine"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_876_hieros_gamos: {
        id: 'mode_876_hieros_gamos',
        name: 'Hieros Gamos',
        description: 'Mode 876: Hieros gamos visualization',
        category: 'Geometric',
        mode: 876,
        tags: ["hieros", "gamos"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_877_alchemical_wedding: {
        id: 'mode_877_alchemical_wedding',
        name: 'Alchemical Wedding',
        description: 'Mode 877: Alchemical wedding visualization',
        category: 'Geometric',
        mode: 877,
        tags: ["alchemical", "wedding"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_878_coniunctio: {
        id: 'mode_878_coniunctio',
        name: 'Coniunctio',
        description: 'Mode 878: Coniunctio visualization',
        category: 'Geometric',
        mode: 878,
        tags: ["coniunctio"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_879_philosopher_stone: {
        id: 'mode_879_philosopher_stone',
        name: 'Philosopher Stone',
        description: 'Mode 879: Philosopher stone visualization',
        category: 'Geometric',
        mode: 879,
        tags: ["philosopher", "stone"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_880_prima_materia: {
        id: 'mode_880_prima_materia',
        name: 'Prima Materia',
        description: 'Mode 880: Prima materia visualization',
        category: 'Geometric',
        mode: 880,
        tags: ["prima", "materia"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_881_nigredo: {
        id: 'mode_881_nigredo',
        name: 'Nigredo',
        description: 'Mode 881: Nigredo visualization',
        category: 'Geometric',
        mode: 881,
        tags: ["nigredo"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_882_albedo: {
        id: 'mode_882_albedo',
        name: 'Albedo',
        description: 'Mode 882: Albedo visualization',
        category: 'Geometric',
        mode: 882,
        tags: ["albedo"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_883_citrinitas: {
        id: 'mode_883_citrinitas',
        name: 'Citrinitas',
        description: 'Mode 883: Citrinitas visualization',
        category: 'Geometric',
        mode: 883,
        tags: ["citrinitas"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_884_rubedo: {
        id: 'mode_884_rubedo',
        name: 'Rubedo',
        description: 'Mode 884: Rubedo visualization',
        category: 'Geometric',
        mode: 884,
        tags: ["rubedo"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_885_seven_stages: {
        id: 'mode_885_seven_stages',
        name: 'Seven Stages',
        description: 'Mode 885: Seven stages visualization',
        category: 'Geometric',
        mode: 885,
        tags: ["seven", "stages"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_886_hermetic_principle: {
        id: 'mode_886_hermetic_principle',
        name: 'Hermetic Principle',
        description: 'Mode 886: Hermetic principle visualization',
        category: 'Geometric',
        mode: 886,
        tags: ["hermetic", "principle"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_887_as_above_so_below: {
        id: 'mode_887_as_above_so_below',
        name: 'As Above So Below',
        description: 'Mode 887: As above so below visualization',
        category: 'Geometric',
        mode: 887,
        tags: ["above", "below"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_888_microcosm_macrocosm: {
        id: 'mode_888_microcosm_macrocosm',
        name: 'Microcosm Macrocosm',
        description: 'Mode 888: Microcosm macrocosm visualization',
        category: 'Geometric',
        mode: 888,
        tags: ["microcosm", "macrocosm"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_889_correspondence: {
        id: 'mode_889_correspondence',
        name: 'Correspondence',
        description: 'Mode 889: Correspondence visualization',
        category: 'Geometric',
        mode: 889,
        tags: ["correspondence"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_890_vibration: {
        id: 'mode_890_vibration',
        name: 'Vibration',
        description: 'Mode 890: Vibration visualization',
        category: 'Geometric',
        mode: 890,
        tags: ["vibration"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_891_polarity: {
        id: 'mode_891_polarity',
        name: 'Polarity',
        description: 'Mode 891: Polarity visualization',
        category: 'Geometric',
        mode: 891,
        tags: ["polarity"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_892_rhythm: {
        id: 'mode_892_rhythm',
        name: 'Rhythm',
        description: 'Mode 892: Rhythm visualization',
        category: 'Geometric',
        mode: 892,
        tags: ["rhythm"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_893_cause_and_effect: {
        id: 'mode_893_cause_and_effect',
        name: 'Cause And Effect',
        description: 'Mode 893: Cause and effect visualization',
        category: 'Geometric',
        mode: 893,
        tags: ["cause", "effect"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_894_gender_principle: {
        id: 'mode_894_gender_principle',
        name: 'Gender Principle',
        description: 'Mode 894: Gender principle visualization',
        category: 'Geometric',
        mode: 894,
        tags: ["gender", "principle"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_895_mentalism: {
        id: 'mode_895_mentalism',
        name: 'Mentalism',
        description: 'Mode 895: Mentalism visualization',
        category: 'Geometric',
        mode: 895,
        tags: ["mentalism"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_896_emerald_tablet: {
        id: 'mode_896_emerald_tablet',
        name: 'Emerald Tablet',
        description: 'Mode 896: Emerald tablet visualization',
        category: 'Geometric',
        mode: 896,
        tags: ["emerald", "tablet"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_897_kybalion: {
        id: 'mode_897_kybalion',
        name: 'Kybalion',
        description: 'Mode 897: Kybalion visualization',
        category: 'Geometric',
        mode: 897,
        tags: ["kybalion"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_898_corpus_hermeticum: {
        id: 'mode_898_corpus_hermeticum',
        name: 'Corpus Hermeticum',
        description: 'Mode 898: Corpus hermeticum visualization',
        category: 'Geometric',
        mode: 898,
        tags: ["corpus", "hermeticum"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_899_gnostic_vision: {
        id: 'mode_899_gnostic_vision',
        name: 'Gnostic Vision',
        description: 'Mode 899: Gnostic vision visualization',
        category: 'Geometric',
        mode: 899,
        tags: ["gnostic", "vision"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_900_sophia: {
        id: 'mode_900_sophia',
        name: 'Sophia',
        description: 'Mode 900: Sophia visualization',
        category: 'Geometric',
        mode: 900,
        tags: ["sophia"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_901_spiral_vortex: {
        id: 'mode_901_spiral_vortex',
        name: 'Spiral Vortex',
        description: 'Mode 901: Spiral vortex visualization',
        category: 'Geometric',
        mode: 901,
        tags: ["spiral", "vortex"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_902_concentric_circles: {
        id: 'mode_902_concentric_circles',
        name: 'Concentric Circles',
        description: 'Mode 902: Concentric circles visualization',
        category: 'Geometric',
        mode: 902,
        tags: ["concentric", "circles"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_903_expanding_rings: {
        id: 'mode_903_expanding_rings',
        name: 'Expanding Rings',
        description: 'Mode 903: Expanding rings visualization',
        category: 'Geometric',
        mode: 903,
        tags: ["expanding", "rings"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_904_contracting_circles: {
        id: 'mode_904_contracting_circles',
        name: 'Contracting Circles',
        description: 'Mode 904: Contracting circles visualization',
        category: 'Geometric',
        mode: 904,
        tags: ["contracting", "circles"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_905_pulsing_orb: {
        id: 'mode_905_pulsing_orb',
        name: 'Pulsing Orb',
        description: 'Mode 905: Pulsing orb visualization',
        category: 'Geometric',
        mode: 905,
        tags: ["pulsing"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_906_oscillating_wave: {
        id: 'mode_906_oscillating_wave',
        name: 'Oscillating Wave',
        description: 'Mode 906: Oscillating wave visualization',
        category: 'Geometric',
        mode: 906,
        tags: ["oscillating", "wave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_907_pendulum_swing: {
        id: 'mode_907_pendulum_swing',
        name: 'Pendulum Swing',
        description: 'Mode 907: Pendulum swing visualization',
        category: 'Geometric',
        mode: 907,
        tags: ["pendulum", "swing"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_908_hypnotic_swirl: {
        id: 'mode_908_hypnotic_swirl',
        name: 'Hypnotic Swirl',
        description: 'Mode 908: Hypnotic swirl visualization',
        category: 'Geometric',
        mode: 908,
        tags: ["hypnotic", "swirl"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_909_tunnel_zoom: {
        id: 'mode_909_tunnel_zoom',
        name: 'Tunnel Zoom',
        description: 'Mode 909: Tunnel zoom visualization',
        category: 'Geometric',
        mode: 909,
        tags: ["tunnel", "zoom"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_910_perspective_shift: {
        id: 'mode_910_perspective_shift',
        name: 'Perspective Shift',
        description: 'Mode 910: Perspective shift visualization',
        category: 'Geometric',
        mode: 910,
        tags: ["perspective", "shift"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_911_rotating_polygon: {
        id: 'mode_911_rotating_polygon',
        name: 'Rotating Polygon',
        description: 'Mode 911: Rotating polygon visualization',
        category: 'Geometric',
        mode: 911,
        tags: ["rotating", "polygon"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_912_morphing_shape: {
        id: 'mode_912_morphing_shape',
        name: 'Morphing Shape',
        description: 'Mode 912: Morphing shape visualization',
        category: 'Geometric',
        mode: 912,
        tags: ["morphing", "shape"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_913_flowing_liquid: {
        id: 'mode_913_flowing_liquid',
        name: 'Flowing Liquid',
        description: 'Mode 913: Flowing liquid visualization',
        category: 'Fluid',
        mode: 913,
        tags: ["flowing", "liquid"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_914_ripple_effect: {
        id: 'mode_914_ripple_effect',
        name: 'Ripple Effect',
        description: 'Mode 914: Ripple effect visualization',
        category: 'Geometric',
        mode: 914,
        tags: ["ripple", "effect"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_915_interference_pattern: {
        id: 'mode_915_interference_pattern',
        name: 'Interference Pattern',
        description: 'Mode 915: Interference pattern visualization',
        category: 'Geometric',
        mode: 915,
        tags: ["interference", "pattern"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_916_moire_effect: {
        id: 'mode_916_moire_effect',
        name: 'Moire Effect',
        description: 'Mode 916: Moire effect visualization',
        category: 'Geometric',
        mode: 916,
        tags: ["moire", "effect"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_917_strobing_light: {
        id: 'mode_917_strobing_light',
        name: 'Strobing Light',
        description: 'Mode 917: Strobing light visualization',
        category: 'Geometric',
        mode: 917,
        tags: ["strobing", "light"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_918_flickering: {
        id: 'mode_918_flickering',
        name: 'Flickering',
        description: 'Mode 918: Flickering visualization',
        category: 'Geometric',
        mode: 918,
        tags: ["flickering"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_919_pulsating: {
        id: 'mode_919_pulsating',
        name: 'Pulsating',
        description: 'Mode 919: Pulsating visualization',
        category: 'Geometric',
        mode: 919,
        tags: ["pulsating"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_920_breathing_pattern: {
        id: 'mode_920_breathing_pattern',
        name: 'Breathing Pattern',
        description: 'Mode 920: Breathing pattern visualization',
        category: 'Geometric',
        mode: 920,
        tags: ["breathing", "pattern"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_921_expansion_contraction: {
        id: 'mode_921_expansion_contraction',
        name: 'Expansion Contraction',
        description: 'Mode 921: Expansion contraction visualization',
        category: 'Geometric',
        mode: 921,
        tags: ["expansion", "contraction"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_922_growth_decay: {
        id: 'mode_922_growth_decay',
        name: 'Growth Decay',
        description: 'Mode 922: Growth decay visualization',
        category: 'Geometric',
        mode: 922,
        tags: ["growth", "decay"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_923_birth_death: {
        id: 'mode_923_birth_death',
        name: 'Birth Death',
        description: 'Mode 923: Birth death visualization',
        category: 'Geometric',
        mode: 923,
        tags: ["birth", "death"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_924_ebb_flow: {
        id: 'mode_924_ebb_flow',
        name: 'Ebb Flow',
        description: 'Mode 924: Ebb flow visualization',
        category: 'Geometric',
        mode: 924,
        tags: ["flow"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_925_inhale_exhale: {
        id: 'mode_925_inhale_exhale',
        name: 'Inhale Exhale',
        description: 'Mode 925: Inhale exhale visualization',
        category: 'Geometric',
        mode: 925,
        tags: ["inhale", "exhale"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_926_systole_diastole: {
        id: 'mode_926_systole_diastole',
        name: 'Systole Diastole',
        description: 'Mode 926: Systole diastole visualization',
        category: 'Geometric',
        mode: 926,
        tags: ["systole", "diastole"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_927_tension_release: {
        id: 'mode_927_tension_release',
        name: 'Tension Release',
        description: 'Mode 927: Tension release visualization',
        category: 'Geometric',
        mode: 927,
        tags: ["tension", "release"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_928_charge_discharge: {
        id: 'mode_928_charge_discharge',
        name: 'Charge Discharge',
        description: 'Mode 928: Charge discharge visualization',
        category: 'Geometric',
        mode: 928,
        tags: ["charge", "discharge"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_929_loading_unloading: {
        id: 'mode_929_loading_unloading',
        name: 'Loading Unloading',
        description: 'Mode 929: Loading unloading visualization',
        category: 'Geometric',
        mode: 929,
        tags: ["loading", "unloading"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_930_compression_rarefaction: {
        id: 'mode_930_compression_rarefaction',
        name: 'Compression Rarefaction',
        description: 'Mode 930: Compression rarefaction visualization',
        category: 'Geometric',
        mode: 930,
        tags: ["compression", "rarefaction"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_931_dense_sparse: {
        id: 'mode_931_dense_sparse',
        name: 'Dense Sparse',
        description: 'Mode 931: Dense sparse visualization',
        category: 'Geometric',
        mode: 931,
        tags: ["dense", "sparse"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_932_thick_thin: {
        id: 'mode_932_thick_thin',
        name: 'Thick Thin',
        description: 'Mode 932: Thick thin visualization',
        category: 'Geometric',
        mode: 932,
        tags: ["thick", "thin"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_933_heavy_light: {
        id: 'mode_933_heavy_light',
        name: 'Heavy Light',
        description: 'Mode 933: Heavy light visualization',
        category: 'Geometric',
        mode: 933,
        tags: ["heavy", "light"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_934_dark_bright: {
        id: 'mode_934_dark_bright',
        name: 'Dark Bright',
        description: 'Mode 934: Dark bright visualization',
        category: 'Geometric',
        mode: 934,
        tags: ["dark", "bright"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_935_shadow_highlight: {
        id: 'mode_935_shadow_highlight',
        name: 'Shadow Highlight',
        description: 'Mode 935: Shadow highlight visualization',
        category: 'Geometric',
        mode: 935,
        tags: ["shadow", "highlight"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_936_positive_negative: {
        id: 'mode_936_positive_negative',
        name: 'Positive Negative',
        description: 'Mode 936: Positive negative visualization',
        category: 'Geometric',
        mode: 936,
        tags: ["positive", "negative"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_937_convex_concave: {
        id: 'mode_937_convex_concave',
        name: 'Convex Concave',
        description: 'Mode 937: Convex concave visualization',
        category: 'Geometric',
        mode: 937,
        tags: ["convex", "concave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_938_inside_outside: {
        id: 'mode_938_inside_outside',
        name: 'Inside Outside',
        description: 'Mode 938: Inside outside visualization',
        category: 'Geometric',
        mode: 938,
        tags: ["inside", "outside"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_939_figure_ground: {
        id: 'mode_939_figure_ground',
        name: 'Figure Ground',
        description: 'Mode 939: Figure ground visualization',
        category: 'Geometric',
        mode: 939,
        tags: ["figure", "ground"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_940_foreground_background: {
        id: 'mode_940_foreground_background',
        name: 'Foreground Background',
        description: 'Mode 940: Foreground background visualization',
        category: 'Geometric',
        mode: 940,
        tags: ["foreground", "background"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_941_solid_void: {
        id: 'mode_941_solid_void',
        name: 'Solid Void',
        description: 'Mode 941: Solid void visualization',
        category: 'Geometric',
        mode: 941,
        tags: ["solid", "void"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_942_matter_antimatter: {
        id: 'mode_942_matter_antimatter',
        name: 'Matter Antimatter',
        description: 'Mode 942: Matter antimatter visualization',
        category: 'Geometric',
        mode: 942,
        tags: ["matter", "antimatter"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_943_particle_wave: {
        id: 'mode_943_particle_wave',
        name: 'Particle Wave',
        description: 'Mode 943: Particle wave visualization',
        category: 'Particles',
        mode: 943,
        tags: ["particle", "wave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_944_discrete_continuous: {
        id: 'mode_944_discrete_continuous',
        name: 'Discrete Continuous',
        description: 'Mode 944: Discrete continuous visualization',
        category: 'Geometric',
        mode: 944,
        tags: ["discrete", "continuous"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_945_quantized_smooth: {
        id: 'mode_945_quantized_smooth',
        name: 'Quantized Smooth',
        description: 'Mode 945: Quantized smooth visualization',
        category: 'Geometric',
        mode: 945,
        tags: ["quantized", "smooth"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_946_digital_analog: {
        id: 'mode_946_digital_analog',
        name: 'Digital Analog',
        description: 'Mode 946: Digital analog visualization',
        category: 'Geometric',
        mode: 946,
        tags: ["digital", "analog"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_947_binary_fluid: {
        id: 'mode_947_binary_fluid',
        name: 'Binary Fluid',
        description: 'Mode 947: Binary fluid visualization',
        category: 'Fluid',
        mode: 947,
        tags: ["binary", "fluid"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_948_on_off: {
        id: 'mode_948_on_off',
        name: 'On Off',
        description: 'Mode 948: On off visualization',
        category: 'Geometric',
        mode: 948,
        tags: [],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_949_yes_no: {
        id: 'mode_949_yes_no',
        name: 'Yes No',
        description: 'Mode 949: Yes no visualization',
        category: 'Geometric',
        mode: 949,
        tags: [],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_950_zero_one: {
        id: 'mode_950_zero_one',
        name: 'Zero One',
        description: 'Mode 950: Zero one visualization',
        category: 'Geometric',
        mode: 950,
        tags: ["zero"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_951_presence_absence: {
        id: 'mode_951_presence_absence',
        name: 'Presence Absence',
        description: 'Mode 951: Presence absence visualization',
        category: 'Geometric',
        mode: 951,
        tags: ["presence", "absence"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_952_being_nothingness: {
        id: 'mode_952_being_nothingness',
        name: 'Being Nothingness',
        description: 'Mode 952: Being nothingness visualization',
        category: 'Geometric',
        mode: 952,
        tags: ["being", "nothingness"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_953_existence_void: {
        id: 'mode_953_existence_void',
        name: 'Existence Void',
        description: 'Mode 953: Existence void visualization',
        category: 'Geometric',
        mode: 953,
        tags: ["existence", "void"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_954_form_emptiness: {
        id: 'mode_954_form_emptiness',
        name: 'Form Emptiness',
        description: 'Mode 954: Form emptiness visualization',
        category: 'Geometric',
        mode: 954,
        tags: ["form", "emptiness"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_955_substance_essence: {
        id: 'mode_955_substance_essence',
        name: 'Substance Essence',
        description: 'Mode 955: Substance essence visualization',
        category: 'Geometric',
        mode: 955,
        tags: ["substance", "essence"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_956_appearance_reality: {
        id: 'mode_956_appearance_reality',
        name: 'Appearance Reality',
        description: 'Mode 956: Appearance reality visualization',
        category: 'Geometric',
        mode: 956,
        tags: ["appearance", "reality"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_957_illusion_truth: {
        id: 'mode_957_illusion_truth',
        name: 'Illusion Truth',
        description: 'Mode 957: Illusion truth visualization',
        category: 'Geometric',
        mode: 957,
        tags: ["illusion", "truth"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_958_maya_brahman: {
        id: 'mode_958_maya_brahman',
        name: 'Maya Brahman',
        description: 'Mode 958: Maya brahman visualization',
        category: 'Geometric',
        mode: 958,
        tags: ["maya", "brahman"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_959_phenomena_noumena: {
        id: 'mode_959_phenomena_noumena',
        name: 'Phenomena Noumena',
        description: 'Mode 959: Phenomena noumena visualization',
        category: 'Geometric',
        mode: 959,
        tags: ["phenomena", "noumena"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_960_relative_absolute: {
        id: 'mode_960_relative_absolute',
        name: 'Relative Absolute',
        description: 'Mode 960: Relative absolute visualization',
        category: 'Geometric',
        mode: 960,
        tags: ["relative", "absolute"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_961_changing_unchanging: {
        id: 'mode_961_changing_unchanging',
        name: 'Changing Unchanging',
        description: 'Mode 961: Changing unchanging visualization',
        category: 'Geometric',
        mode: 961,
        tags: ["changing", "unchanging"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_962_temporal_eternal: {
        id: 'mode_962_temporal_eternal',
        name: 'Temporal Eternal',
        description: 'Mode 962: Temporal eternal visualization',
        category: 'Geometric',
        mode: 962,
        tags: ["temporal", "eternal"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_963_finite_infinite: {
        id: 'mode_963_finite_infinite',
        name: 'Finite Infinite',
        description: 'Mode 963: Finite infinite visualization',
        category: 'Geometric',
        mode: 963,
        tags: ["finite", "infinite"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_964_limited_boundless: {
        id: 'mode_964_limited_boundless',
        name: 'Limited Boundless',
        description: 'Mode 964: Limited boundless visualization',
        category: 'Geometric',
        mode: 964,
        tags: ["limited", "boundless"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_965_mortal_immortal: {
        id: 'mode_965_mortal_immortal',
        name: 'Mortal Immortal',
        description: 'Mode 965: Mortal immortal visualization',
        category: 'Geometric',
        mode: 965,
        tags: ["mortal", "immortal"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_966_perishable_imperishable: {
        id: 'mode_966_perishable_imperishable',
        name: 'Perishable Imperishable',
        description: 'Mode 966: Perishable imperishable visualization',
        category: 'Geometric',
        mode: 966,
        tags: ["perishable", "imperishable"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_967_transient_permanent: {
        id: 'mode_967_transient_permanent',
        name: 'Transient Permanent',
        description: 'Mode 967: Transient permanent visualization',
        category: 'Geometric',
        mode: 967,
        tags: ["transient", "permanent"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_968_fleeting_lasting: {
        id: 'mode_968_fleeting_lasting',
        name: 'Fleeting Lasting',
        description: 'Mode 968: Fleeting lasting visualization',
        category: 'Geometric',
        mode: 968,
        tags: ["fleeting", "lasting"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_969_ephemeral_enduring: {
        id: 'mode_969_ephemeral_enduring',
        name: 'Ephemeral Enduring',
        description: 'Mode 969: Ephemeral enduring visualization',
        category: 'Geometric',
        mode: 969,
        tags: ["ephemeral", "enduring"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_970_momentary_timeless: {
        id: 'mode_970_momentary_timeless',
        name: 'Momentary Timeless',
        description: 'Mode 970: Momentary timeless visualization',
        category: 'Geometric',
        mode: 970,
        tags: ["momentary", "timeless"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_971_local_universal: {
        id: 'mode_971_local_universal',
        name: 'Local Universal',
        description: 'Mode 971: Local universal visualization',
        category: 'Geometric',
        mode: 971,
        tags: ["local", "universal"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_972_particular_general: {
        id: 'mode_972_particular_general',
        name: 'Particular General',
        description: 'Mode 972: Particular general visualization',
        category: 'Geometric',
        mode: 972,
        tags: ["particular", "general"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_973_specific_generic: {
        id: 'mode_973_specific_generic',
        name: 'Specific Generic',
        description: 'Mode 973: Specific generic visualization',
        category: 'Geometric',
        mode: 973,
        tags: ["specific", "generic"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_974_unique_common: {
        id: 'mode_974_unique_common',
        name: 'Unique Common',
        description: 'Mode 974: Unique common visualization',
        category: 'Geometric',
        mode: 974,
        tags: ["unique", "common"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_975_individual_collective: {
        id: 'mode_975_individual_collective',
        name: 'Individual Collective',
        description: 'Mode 975: Individual collective visualization',
        category: 'Geometric',
        mode: 975,
        tags: ["individual", "collective"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_976_one_many: {
        id: 'mode_976_one_many',
        name: 'One Many',
        description: 'Mode 976: One many visualization',
        category: 'Geometric',
        mode: 976,
        tags: ["many"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_977_unity_multiplicity: {
        id: 'mode_977_unity_multiplicity',
        name: 'Unity Multiplicity',
        description: 'Mode 977: Unity multiplicity visualization',
        category: 'Geometric',
        mode: 977,
        tags: ["unity", "multiplicity"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_978_simple_complex: {
        id: 'mode_978_simple_complex',
        name: 'Simple Complex',
        description: 'Mode 978: Simple complex visualization',
        category: 'Geometric',
        mode: 978,
        tags: ["simple", "complex"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_979_elementary_composite: {
        id: 'mode_979_elementary_composite',
        name: 'Elementary Composite',
        description: 'Mode 979: Elementary composite visualization',
        category: 'Geometric',
        mode: 979,
        tags: ["elementary", "composite"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_980_atomic_molecular: {
        id: 'mode_980_atomic_molecular',
        name: 'Atomic Molecular',
        description: 'Mode 980: Atomic molecular visualization',
        category: 'Scientific',
        mode: 980,
        tags: ["atomic", "molecular"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_981_fundamental_derived: {
        id: 'mode_981_fundamental_derived',
        name: 'Fundamental Derived',
        description: 'Mode 981: Fundamental derived visualization',
        category: 'Geometric',
        mode: 981,
        tags: ["fundamental", "derived"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_982_primary_secondary: {
        id: 'mode_982_primary_secondary',
        name: 'Primary Secondary',
        description: 'Mode 982: Primary secondary visualization',
        category: 'Geometric',
        mode: 982,
        tags: ["primary", "secondary"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_983_essential_accidental: {
        id: 'mode_983_essential_accidental',
        name: 'Essential Accidental',
        description: 'Mode 983: Essential accidental visualization',
        category: 'Geometric',
        mode: 983,
        tags: ["essential", "accidental"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_984_necessary_contingent: {
        id: 'mode_984_necessary_contingent',
        name: 'Necessary Contingent',
        description: 'Mode 984: Necessary contingent visualization',
        category: 'Geometric',
        mode: 984,
        tags: ["necessary", "contingent"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_985_a_priori_a_posteriori: {
        id: 'mode_985_a_priori_a_posteriori',
        name: 'A Priori A Posteriori',
        description: 'Mode 985: A priori a posteriori visualization',
        category: 'Geometric',
        mode: 985,
        tags: ["priori", "posteriori"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_986_analytic_synthetic: {
        id: 'mode_986_analytic_synthetic',
        name: 'Analytic Synthetic',
        description: 'Mode 986: Analytic synthetic visualization',
        category: 'Geometric',
        mode: 986,
        tags: ["analytic", "synthetic"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_987_deductive_inductive: {
        id: 'mode_987_deductive_inductive',
        name: 'Deductive Inductive',
        description: 'Mode 987: Deductive inductive visualization',
        category: 'Geometric',
        mode: 987,
        tags: ["deductive", "inductive"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_988_logical_empirical: {
        id: 'mode_988_logical_empirical',
        name: 'Logical Empirical',
        description: 'Mode 988: Logical empirical visualization',
        category: 'Geometric',
        mode: 988,
        tags: ["logical", "empirical"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_989_rational_experiential: {
        id: 'mode_989_rational_experiential',
        name: 'Rational Experiential',
        description: 'Mode 989: Rational experiential visualization',
        category: 'Geometric',
        mode: 989,
        tags: ["rational", "experiential"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_990_abstract_concrete: {
        id: 'mode_990_abstract_concrete',
        name: 'Abstract Concrete',
        description: 'Mode 990: Abstract concrete visualization',
        category: 'Geometric',
        mode: 990,
        tags: ["abstract", "concrete"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_991_theoretical_practical: {
        id: 'mode_991_theoretical_practical',
        name: 'Theoretical Practical',
        description: 'Mode 991: Theoretical practical visualization',
        category: 'Geometric',
        mode: 991,
        tags: ["theoretical", "practical"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_992_ideal_real: {
        id: 'mode_992_ideal_real',
        name: 'Ideal Real',
        description: 'Mode 992: Ideal real visualization',
        category: 'Geometric',
        mode: 992,
        tags: ["ideal", "real"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_993_conceptual_actual: {
        id: 'mode_993_conceptual_actual',
        name: 'Conceptual Actual',
        description: 'Mode 993: Conceptual actual visualization',
        category: 'Geometric',
        mode: 993,
        tags: ["conceptual", "actual"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_994_possible_necessary: {
        id: 'mode_994_possible_necessary',
        name: 'Possible Necessary',
        description: 'Mode 994: Possible necessary visualization',
        category: 'Geometric',
        mode: 994,
        tags: ["possible", "necessary"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_995_potential_actual: {
        id: 'mode_995_potential_actual',
        name: 'Potential Actual',
        description: 'Mode 995: Potential actual visualization',
        category: 'Geometric',
        mode: 995,
        tags: ["potential", "actual"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_996_virtual_real: {
        id: 'mode_996_virtual_real',
        name: 'Virtual Real',
        description: 'Mode 996: Virtual real visualization',
        category: 'Geometric',
        mode: 996,
        tags: ["virtual", "real"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_997_simulated_genuine: {
        id: 'mode_997_simulated_genuine',
        name: 'Simulated Genuine',
        description: 'Mode 997: Simulated genuine visualization',
        category: 'Geometric',
        mode: 997,
        tags: ["simulated", "genuine"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_998_artificial_natural: {
        id: 'mode_998_artificial_natural',
        name: 'Artificial Natural',
        description: 'Mode 998: Artificial natural visualization',
        category: 'Geometric',
        mode: 998,
        tags: ["artificial", "natural"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_999_synthetic_organic: {
        id: 'mode_999_synthetic_organic',
        name: 'Synthetic Organic',
        description: 'Mode 999: Synthetic organic visualization',
        category: 'Geometric',
        mode: 999,
        tags: ["synthetic", "organic"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_1000_mechanical_living: {
        id: 'mode_1000_mechanical_living',
        name: 'Mechanical Living',
        description: 'Mode 1000: Mechanical living visualization',
        category: 'Geometric',
        mode: 1000,
        tags: ["mechanical", "living"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            complexity: { min: 1, max: 10, default: 5, label: 'Complexity' }
        }
    },
    mode_1001_cassette_tape_deck: {
        id: 'mode_1001_cassette_tape_deck',
        name: 'Cassette Tape Deck',
        description: 'Mode 1001: Retro cassette with spinning reels & VU meters',
        category: 'Retro',
        mode: 1001,
        tags: ["retro", "cassette", "vintage", "analog"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Reel Speed' },
            glowIntensity: { min: 0, max: 30, default: 10, label: 'Glow Intensity' }
        }
    },
    mode_1002_arcade_pixel_bars: {
        id: 'mode_1002_arcade_pixel_bars',
        name: 'Arcade Pixel Bars',
        description: 'Mode 1002: Chunky 8-bit bars with retro arcade style',
        category: 'Retro',
        mode: 1002,
        tags: ["retro", "8bit", "pixel", "arcade"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            pixelSize: { min: 4, max: 16, default: 8, label: 'Pixel Size' },
            glowIntensity: { min: 0, max: 30, default: 15, label: 'Glow Intensity' }
        }
    },
    mode_1003_vector_oscilloscope: {
        id: 'mode_1003_vector_oscilloscope',
        name: 'Vector Oscilloscope',
        description: 'Mode 1003: Classic green oscilloscope with glowing waveform',
        category: 'Retro',
        mode: 1003,
        tags: ["retro", "oscilloscope", "vector", "crt", "green"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Animation Speed' },
            lineThickness: { min: 1, max: 8, default: 3, label: 'Line Thickness' },
            glowIntensity: { min: 5, max: 40, default: 20, label: 'Glow Intensity' }
        }
    },
    mode_1004_led_spectrum_grid: {
        id: 'mode_1004_led_spectrum_grid',
        name: 'LED Spectrum Grid',
        description: 'Mode 1004: Old-school LED spectrum analyzer with discrete blocks',
        category: 'Retro',
        mode: 1004,
        tags: ["retro", "led", "spectrum", "grid", "analyzer"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            ledSize: { min: 4, max: 12, default: 8, label: 'LED Size' },
            ledGap: { min: 1, max: 5, default: 2, label: 'LED Gap' }
        }
    },
    mode_1008_boombox_spectrum: {
        id: 'mode_1008_boombox_spectrum',
        name: 'Boombox Spectrum',
        description: 'Mode 1008: Classic 80s boombox with dual speakers and spectrum display',
        category: 'Retro',
        mode: 1008,
        tags: ["retro", "boombox", "80s", "speakers", "stereo"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speakerSize: { min: 0.5, max: 1.5, default: 1, label: 'Speaker Size' },
            glowIntensity: { min: 0, max: 30, default: 15, label: 'Glow Intensity' },
            bassResponse: { min: 0.5, max: 2, default: 1, label: 'Bass Response' }
        }
    },
    mode_1009_synthwave_grid: {
        id: 'mode_1009_synthwave_grid',
        name: 'Synthwave Grid',
        description: 'Mode 1009: Classic 1980s synthwave perspective grid with neon sun',
        category: 'Retro',
        mode: 1009,
        tags: ["retro", "synthwave", "80s", "grid", "neon", "vaporwave"],
        parameters: {
            intensity: { min: 0.1, max: 2, default: 1, label: 'Intensity' },
            speed: { min: 0.1, max: 3, default: 1, label: 'Grid Speed' },
            gridLines: { min: 8, max: 24, default: 16, label: 'Grid Lines' },
            glowIntensity: { min: 5, max: 40, default: 20, label: 'Glow Intensity' }
        }
    },
    mode_1005_v_formation_migration: {
        id: 'mode_1005_v_formation_migration',
        name: 'V-Formation Migration',
        description: 'Geese flying in V-shaped formation with leader switching',
        category: 'Particles',
        mode: 1005,
        tags: ["birds", "geese", "migration", "formation", "v-shape"],
        parameters: {
            birdCount: { min: 15, max: 40, default: 25, label: 'Bird Count' },
            wingSpan: { min: 10, max: 20, default: 15, label: 'Wing Span' },
            formationSpread: { min: 20, max: 60, default: 40, label: 'Formation Spread' },
            speed: { min: 0.5, max: 3, default: 1.5, label: 'Flight Speed' },
            trailLength: { min: 0, max: 0.5, default: 0.2, label: 'Motion Trail' }
        }
    },
    mode_1006_diving_seagulls: {
        id: 'mode_1006_diving_seagulls',
        name: 'Diving Seagulls',
        description: 'Seagulls diving down and swooping back up in graceful arcs',
        category: 'Particles',
        mode: 1006,
        tags: ["birds", "seagulls", "diving", "swooping", "ocean"],
        parameters: {
            birdCount: { min: 10, max: 30, default: 20, label: 'Bird Count' },
            wingSpan: { min: 12, max: 22, default: 17, label: 'Wing Span' },
            diveSpeed: { min: 1, max: 4, default: 2.5, label: 'Dive Speed' },
            diveHeight: { min: 0.3, max: 0.8, default: 0.6, label: 'Dive Height' },
            trailLength: { min: 0, max: 0.5, default: 0.15, label: 'Motion Trail' }
        }
    },
    mode_1007_sparrow_scatter: {
        id: 'mode_1007_sparrow_scatter',
        name: 'Sparrow Scatter',
        description: 'Small birds that scatter explosively on bass, then regroup',
        category: 'Particles',
        mode: 1007,
        tags: ["birds", "sparrows", "scatter", "flock", "explosive"],
        parameters: {
            birdCount: { min: 30, max: 80, default: 50, label: 'Bird Count' },
            wingSpan: { min: 6, max: 12, default: 8, label: 'Wing Span' },
            scatterRadius: { min: 50, max: 200, default: 120, label: 'Scatter Radius' },
            bassThreshold: { min: 0.2, max: 0.7, default: 0.4, label: 'Bass Threshold' },
            trailLength: { min: 0, max: 0.5, default: 0.1, label: 'Motion Trail' }
        }
    },

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
    numBars: 100,
    innerRadius: 100,
    smoothing: 0.85,
    barWidthMultiplier: 0.8,
    gradient: true,
    colorScheme: 'apple_blue',
    background: 'transparent',
    fps: 30,
    format: 'square_1_1',
    width: 1080,
    height: 1080,
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
    acceptedMimeTypes: [
        'audio/mpeg',
        'audio/mp3',
        'audio/wav',      // Standard .wav MIME type
        'audio/x-wav',    // Safari/older browsers .wav MIME type
        'audio/wave'      // Alternative .wav MIME type
    ]
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
        HIDDEN_MODES,
        VISUALIZATION_MODES,
        DEFAULT_SETTINGS,
        AUDIO_CONFIG,
        FILE_CONSTRAINTS,
        ANIMATION
    };
}

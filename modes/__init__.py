"""
Mode Registry and Auto-Loader for Audio Spectrum Visualizations
Automatically discovers and loads all visualization modes
"""
from pathlib import Path
import importlib
import inspect


# Mode registry - maps mode number to (class_instance, method_name)
_mode_registry = {}
_mode_classes = {}


def register_modes(visualizer):
    """
    Discover and register all mode classes

    Args:
        visualizer: The CreativeSpectrumVisualizer instance

    Returns:
        dict: Registry mapping mode numbers to their draw methods
    """
    global _mode_registry, _mode_classes

    # Get all mode files in this directory
    modes_dir = Path(__file__).parent
    mode_files = sorted(modes_dir.glob("mode_*.py"))

    for mode_file in mode_files:
        # Import the module
        module_name = f"modes.{mode_file.stem}"
        try:
            module = importlib.import_module(module_name)

            # Find all mode classes in the module
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if name.startswith('Modes') and name != 'BaseModeVisualizer':
                    # Instantiate the mode class
                    mode_instance = obj(visualizer)
                    _mode_classes[name] = mode_instance

                    # Register all draw_mode_XXX methods
                    for method_name in dir(mode_instance):
                        if method_name.startswith('draw_mode_'):
                            # Extract mode number from method name
                            parts = method_name.split('_')
                            if len(parts) >= 3 and parts[2].isdigit():
                                mode_num = int(parts[2])
                                method = getattr(mode_instance, method_name)
                                _mode_registry[mode_num] = method

        except Exception as e:
            print(f"Warning: Could not load {mode_file.name}: {e}")

    return _mode_registry


def get_mode_method(mode_number):
    """
    Get the draw method for a specific mode number

    Args:
        mode_number: The mode number to retrieve

    Returns:
        The draw method for that mode, or None if not found
    """
    return _mode_registry.get(mode_number)


def get_all_modes():
    """Get all registered mode numbers"""
    return sorted(_mode_registry.keys())


def get_mode_count():
    """Get total number of registered modes"""
    return len(_mode_registry)


# Export public API
__all__ = [
    'register_modes',
    'get_mode_method',
    'get_all_modes',
    'get_mode_count',
]

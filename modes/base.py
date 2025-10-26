"""
Base class for audio spectrum visualization modes
Provides shared functionality and state management
"""
import numpy as np
import cv2


class BaseModeVisualizer:
    """Base class for all visualization modes"""

    def __init__(self, visualizer):
        """
        Initialize mode with reference to main visualizer

        Args:
            visualizer: Reference to CreativeSpectrumVisualizer instance
        """
        object.__setattr__(self, 'viz', visualizer)

    def __getattr__(self, name):
        """Proxy attribute access to the visualizer"""
        try:
            return getattr(self.viz, name)
        except AttributeError:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        """Proxy attribute setting to the visualizer"""
        if name == 'viz':
            object.__setattr__(self, name, value)
        else:
            setattr(self.viz, name, value)

    # Helper methods for common operations
    def get_bass(self, magnitudes):
        """Get bass frequencies (lower 25%)"""
        return float(np.mean(magnitudes[:len(magnitudes)//4]))

    def get_mids(self, magnitudes):
        """Get mid frequencies (25-75%)"""
        return float(np.mean(magnitudes[len(magnitudes)//4:3*len(magnitudes)//4]))

    def get_highs(self, magnitudes):
        """Get high frequencies (upper 25%)"""
        return float(np.mean(magnitudes[3*len(magnitudes)//4:]))

    def get_energy(self, magnitudes):
        """Get overall energy level"""
        return float(np.mean(magnitudes))

    def hsv_to_bgr(self, h, s, v):
        """Convert HSV color to BGR tuple"""
        color_hsv = np.array([[[h, s, v]]], dtype=np.uint8)
        color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0]
        return tuple(int(c) for c in color_bgr)

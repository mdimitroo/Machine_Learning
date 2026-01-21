"""
Utility functions for machine learning tasks.

This module contains helper functions for:
- Data preprocessing
- Visualization
- Model evaluation
"""

from .data_preprocessing import normalize_data, split_data
from .visualization import plot_confusion_matrix, plot_regression_results

__all__ = [
    'normalize_data',
    'split_data',
    'plot_confusion_matrix',
    'plot_regression_results'
]

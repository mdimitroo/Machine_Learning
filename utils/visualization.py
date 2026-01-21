"""
Visualization utilities for machine learning results.

This module provides functions to visualize model performance and results.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import numpy as np


def plot_confusion_matrix(y_true, y_pred, class_names=None, figsize=(8, 6)):
    """
    Plot a confusion matrix for classification results.
    
    Parameters:
    -----------
    y_true : array-like
        True labels
    y_pred : array-like
        Predicted labels
    class_names : list, optional
        Names of classes for labeling
    figsize : tuple, default=(8, 6)
        Figure size (width, height)
    
    Example:
    --------
    >>> plot_confusion_matrix(y_test, y_pred, class_names=['Class A', 'Class B'])
    """
    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=figsize)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=class_names, yticklabels=class_names)
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.title('Confusion Matrix')
    plt.tight_layout()
    plt.show()


def plot_regression_results(y_true, y_pred, figsize=(8, 6)):
    """
    Plot regression results showing predicted vs actual values.
    
    Parameters:
    -----------
    y_true : array-like
        True target values
    y_pred : array-like
        Predicted target values
    figsize : tuple, default=(8, 6)
        Figure size (width, height)
    
    Example:
    --------
    >>> plot_regression_results(y_test, y_pred)
    """
    plt.figure(figsize=figsize)
    plt.scatter(y_true, y_pred, alpha=0.5)
    
    # Plot perfect prediction line (y=x)
    min_val = min(min(y_true), min(y_pred))
    max_val = max(max(y_true), max(y_pred))
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2)
    
    plt.xlabel('True Values')
    plt.ylabel('Predicted Values')
    plt.title('Predicted vs Actual Values')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

"""
Data preprocessing utilities for machine learning.

This module provides functions to prepare and clean data before training models.
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def normalize_data(X, method='standard'):
    """
    Normalize/standardize the input features.
    
    Parameters:
    -----------
    X : array-like
        Input features to normalize
    method : str, default='standard'
        Normalization method: 'standard' (z-score) or 'minmax' (0-1 scaling)
    
    Returns:
    --------
    X_normalized : array-like
        Normalized features
    scaler : object
        Fitted scaler object (for inverse transformation if needed)
    
    Example:
    --------
    >>> X = [[1, 2], [3, 4], [5, 6]]
    >>> X_norm, scaler = normalize_data(X, method='standard')
    """
    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    else:
        raise ValueError("Method must be 'standard' or 'minmax'")
    
    X_normalized = scaler.fit_transform(X)
    return X_normalized, scaler


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split data into training and testing sets.
    
    Parameters:
    -----------
    X : array-like
        Input features
    y : array-like
        Target labels/values
    test_size : float, default=0.2
        Proportion of dataset to include in test split (0.0 to 1.0)
    random_state : int, default=42
        Random seed for reproducibility
    
    Returns:
    --------
    X_train, X_test, y_train, y_test : tuple
        Split datasets
    
    Example:
    --------
    >>> X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2)
    """
    return train_test_split(
        X, y, 
        test_size=test_size, 
        random_state=random_state
    )

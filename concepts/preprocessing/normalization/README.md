# Normalization & Standardization

## Overview

Normalization and standardization are crucial preprocessing steps that transform features to a common scale. This is essential because many machine learning algorithms are sensitive to the scale of input features.

## Normalization (Min-Max Scaling)

Normalization scales features to a fixed range, typically [0, 1].

### Formula

```
x_normalized = (x - x_min) / (x_max - x_min)
```

Where:
- `x` is the original value
- `x_min` is the minimum value in the feature
- `x_max` is the maximum value in the feature

### Characteristics

- Scales values to range [0, 1]
- Preserves relationships between values
- Sensitive to outliers (outliers can compress the range)

### When to Use

✅ **Good for:**
- Neural networks
- K-Nearest Neighbors (KNN)
- Algorithms that require features in [0, 1] range
- When you know the bounds of your data

❌ **Not ideal for:**
- When data has outliers (they can skew the scaling)
- When you don't know the bounds of future data

## Standardization (Z-Score Normalization)

Standardization transforms features to have a mean of 0 and standard deviation of 1.

### Formula

```
x_standardized = (x - μ) / σ
```

Where:
- `μ` is the mean of the feature
- `σ` is the standard deviation of the feature

### Characteristics

- Mean = 0, Standard Deviation = 1
- Less sensitive to outliers than normalization
- Can produce negative values
- Assumes data follows a normal distribution

### When to Use

✅ **Good for:**
- Linear Regression
- Logistic Regression
- Support Vector Machines (SVM)
- Principal Component Analysis (PCA)
- Most algorithms that assume normally distributed data
- When data has outliers

❌ **Not ideal for:**
- When you need features in a specific range
- Sparse data (can destroy sparsity)

## Key Differences

| Aspect | Normalization | Standardization |
|--------|--------------|----------------|
| Range | [0, 1] | (-∞, +∞) |
| Mean | Not necessarily 0 | Always 0 |
| Std Dev | Not necessarily 1 | Always 1 |
| Outlier Sensitivity | High | Low |
| Distribution | Preserves original | Assumes normal |

## When to Apply

### Apply Before Training:
- **Always**: Linear Regression, Logistic Regression, SVM, Neural Networks
- **Usually**: KNN, K-Means, PCA
- **Sometimes**: Tree-based models (less critical)

### Don't Apply:
- Tree-based algorithms (Decision Trees, Random Forest) - they're scale-invariant

## Implementation Notes

- **Fit on training data only**: Calculate min/max or mean/std from training set
- **Transform both train and test**: Apply the same transformation to test data
- **Never fit on test data**: This causes data leakage

## Common Mistakes

1. **Fitting scaler on entire dataset**: Should only fit on training data
2. **Different scaling for train/test**: Must use same scaler object
3. **Scaling target variable**: Usually not needed (except for neural networks)
4. **Scaling categorical features**: Only scale numerical features

## Code Example (Conceptual)

```python
# Standardization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use same scaler!

# Normalization
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

## References

- Scikit-learn documentation: StandardScaler, MinMaxScaler
- Feature scaling importance in ML pipelines

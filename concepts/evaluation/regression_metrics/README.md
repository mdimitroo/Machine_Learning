# Regression Metrics

## Overview

Regression metrics measure how well a regression model predicts continuous numerical values. Different metrics emphasize different aspects of prediction error and are suited for different scenarios.

## Key Metrics

### 1. Mean Squared Error (MSE)

**Formula**: `MSE = (1/n) * Σ(y_true - y_pred)²`

**Interpretation**: Average of squared differences between predicted and actual values

**Characteristics**:
- **Units**: Squared units of target variable
- **Sensitive to outliers**: Large errors are heavily penalized
- **Always non-negative**: Lower is better
- **Differentiable**: Good for optimization

**When to Use**:
- Default metric for regression
- When large errors are particularly bad
- For optimization (gradient descent)

**Example**: If predicting house prices in $1000s, MSE is in ($1000)²

### 2. Root Mean Squared Error (RMSE)

**Formula**: `RMSE = √MSE`

**Interpretation**: Square root of MSE, in same units as target variable

**Characteristics**:
- **Units**: Same as target variable (more interpretable)
- **Sensitive to outliers**: Like MSE, penalizes large errors
- **Always non-negative**: Lower is better

**When to Use**:
- When you want error in original units
- More interpretable than MSE
- Standard metric for regression

**Example**: If predicting house prices in $1000s, RMSE is in $1000s

### 3. Mean Absolute Error (MAE)

**Formula**: `MAE = (1/n) * Σ|y_true - y_pred|`

**Interpretation**: Average absolute difference between predicted and actual values

**Characteristics**:
- **Units**: Same as target variable
- **Less sensitive to outliers**: All errors weighted equally
- **Robust**: Not affected by extreme values
- **Not differentiable at 0**: Can be issue for optimization

**When to Use**:
- When outliers should be treated equally
- When you want interpretable error
- Robust alternative to MSE/RMSE

**Example**: "On average, predictions are off by X units"

### 4. R² Score (Coefficient of Determination)

**Formula**: `R² = 1 - (SS_res / SS_tot)`

Where:
- `SS_res = Σ(y_true - y_pred)²` (sum of squared residuals)
- `SS_tot = Σ(y_true - y_mean)²` (total sum of squares)

**Interpretation**: Proportion of variance in target explained by model

**Characteristics**:
- **Range**: -∞ to 1 (can be negative for bad models)
- **1.0**: Perfect predictions
- **0.0**: Model performs as well as predicting mean
- **Negative**: Model worse than predicting mean

**When to Use**:
- Compare models
- Understand explained variance
- Standard metric for regression

**Limitations**:
- Can be misleading with non-linear relationships
- Doesn't indicate prediction accuracy in absolute terms

### 5. Mean Absolute Percentage Error (MAPE)

**Formula**: `MAPE = (100/n) * Σ|(y_true - y_pred) / y_true|`

**Interpretation**: Average percentage error

**Characteristics**:
- **Units**: Percentage
- **Scale-independent**: Works across different scales
- **Problem with zeros**: Undefined when y_true = 0
- **Asymmetric**: Penalizes underestimation differently than overestimation

**When to Use**:
- When percentage error is meaningful
- Comparing models across different scales
- Business contexts where relative error matters

**Limitations**:
- Undefined for zero values
- Can be biased for small values

## Comparison of Metrics

| Metric | Outlier Sensitivity | Units | Interpretability | Optimization |
|--------|-------------------|-------|------------------|--------------|
| MSE | High | Squared | Low | Excellent |
| RMSE | High | Original | High | Good |
| MAE | Low | Original | High | Good |
| R² | Medium | Unitless | Medium | Good |
| MAPE | Medium | % | High | Poor |

## Choosing the Right Metric

### Use MSE/RMSE When:
- Large errors are particularly bad
- You want to penalize outliers
- Standard practice in your field
- Need differentiable metric for optimization

### Use MAE When:
- All errors should be treated equally
- Outliers shouldn't dominate
- You want interpretable error
- Robust predictions needed

### Use R² When:
- Comparing multiple models
- Understanding explained variance
- Standard reporting metric
- Need unitless comparison

### Use MAPE When:
- Percentage error is meaningful
- Comparing across different scales
- Business context requires relative error
- Target values are always positive

## Code Example (Conceptual)

```python
from sklearn.metrics import (
    mean_squared_error, mean_absolute_error,
    r2_score, mean_absolute_percentage_error
)

# Calculate metrics
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)
mape = mean_absolute_percentage_error(y_true, y_pred)

print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R²: {r2:.4f}")
print(f"MAPE: {mape:.2f}%")
```

## Visualizing Regression Performance

### 1. Predicted vs Actual Plot
- Scatter plot: y_pred vs y_true
- Perfect predictions: Points on diagonal line
- Shows systematic errors

### 2. Residual Plot
- Plot: residuals (y_true - y_pred) vs y_pred
- Should be randomly distributed around zero
- Patterns indicate model issues

### 3. Error Distribution
- Histogram of errors
- Should be normally distributed
- Skew indicates systematic bias

## Best Practices

1. **Report multiple metrics**: Different metrics tell different stories
2. **Consider business context**: Which errors matter most?
3. **Visualize errors**: Plots reveal issues numbers don't
4. **Use appropriate metric**: Match metric to problem requirements
5. **Compare to baseline**: How much better than predicting mean?

## Summary

- **MSE/RMSE**: Standard, penalizes large errors
- **MAE**: Robust, treats all errors equally
- **R²**: Explained variance, model comparison
- **MAPE**: Percentage error, scale-independent

Choose based on your specific needs and problem characteristics.

## References

- Scikit-learn regression metrics
- Understanding regression evaluation

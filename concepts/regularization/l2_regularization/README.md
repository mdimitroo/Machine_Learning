# L2 Regularization (Ridge)

## Overview

L2 Regularization, also known as Ridge Regression, adds a penalty term proportional to the square of model coefficients. It's effective at preventing overfitting by shrinking coefficients toward zero without eliminating them entirely.

## How It Works

L2 regularization adds a penalty term to the loss function:

**For Linear Regression:**
```
Loss = MSE + λ * Σβᵢ²
```

**For Logistic Regression:**
```
Loss = Log-Loss + λ * Σβᵢ²
```

Where:
- `λ` (lambda or alpha) is the regularization strength
- `βᵢ` are the model coefficients
- Larger λ = stronger regularization = smaller coefficients

## Key Characteristics

### Coefficient Shrinking
- Shrinks coefficients toward zero (but never exactly zero)
- Prevents coefficients from becoming too large
- Reduces model variance (less sensitive to small data changes)

### No Feature Elimination
- All features remain in the model (coefficients ≠ 0)
- Preserves all information from features
- Better for when all features might be relevant

## Parameters

### Regularization Strength (λ or α)

- **Small λ (e.g., 0.001)**: Weak regularization, model behaves like unregularized version
- **Medium λ (e.g., 0.1)**: Moderate regularization, coefficients moderately shrunk
- **Large λ (e.g., 1.0)**: Strong regularization, coefficients heavily shrunk, may underfit

### Choosing λ

- Use cross-validation to find optimal λ
- Plot validation error vs λ to find sweet spot
- Balance between bias and variance

## Use Cases

✅ **Good for:**
- Preventing overfitting
- When you have many features relative to samples
- Multicollinearity (highly correlated features)
- When all features might be relevant
- Stable, interpretable models

❌ **Not ideal for:**
- Feature selection (doesn't eliminate features)
- When you have many irrelevant features
- When you need sparse models

## Pros and Cons

### Pros
- **Prevents overfitting**: Reduces model complexity
- **Stable**: Less sensitive to small data changes
- **Handles multicollinearity**: Works well with correlated features
- **All features retained**: Preserves all information
- **Differentiable**: Easier optimization than L1

### Cons
- **No feature selection**: Doesn't eliminate irrelevant features
- **Dense models**: All coefficients remain non-zero
- **Less interpretable**: With many features, harder to interpret
- **May underfit**: If λ is too large

## Comparison with L1 Regularization

| Aspect | L2 (Ridge) | L1 (Lasso) |
|--------|------------|------------|
| Penalty | β² | |β| |
| Feature Selection | No (dense) | Yes (sparse) |
| Coefficient Values | Approaches 0 | Can be exactly 0 |
| Use Case | Prevent overfitting | Feature selection |
| Stability | More stable | Less stable |
| Multicollinearity | Handles well | May arbitrarily select |

## Mathematical Foundation

The L2 penalty term:
```
Penalty = λ * Σβᵢ²
```

Optimization:
- Uses gradient descent (smooth, differentiable)
- Has closed-form solution for linear regression
- Faster convergence than L1

**Ridge Regression Closed Form:**
```
β = (XᵀX + λI)⁻¹Xᵀy
```

Where `I` is the identity matrix.

## When to Use L2 vs L1

- **Use L2**: When you want to prevent overfitting but keep all features
- **Use L1**: When you need feature selection
- **Use Elastic Net**: Combine both for balanced approach

## Code Example (Conceptual)

```python
from sklearn.linear_model import Ridge

# L2 Regularization (Ridge)
ridge = Ridge(alpha=0.1)  # alpha is λ
ridge.fit(X_train, y_train)

# All coefficients remain non-zero
print(f"All {len(ridge.coef_)} features retained")
print(f"Largest coefficient: {ridge.coef_.max():.4f}")
print(f"Smallest coefficient: {ridge.coef_.min():.4f}")
```

## References

- Hoerl, A. E., & Kennard, R. W. (1970). "Ridge Regression"
- Scikit-learn: Ridge, RidgeCV

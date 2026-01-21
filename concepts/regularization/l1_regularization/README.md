# L1 Regularization (Lasso)

## Overview

L1 Regularization, also known as Lasso (Least Absolute Shrinkage and Selection Operator), adds a penalty term proportional to the absolute value of model coefficients. It's particularly useful for feature selection as it can drive coefficients to exactly zero.

## How It Works

L1 regularization adds a penalty term to the loss function:

**For Linear Regression:**
```
Loss = MSE + λ * Σ|βᵢ|
```

**For Logistic Regression:**
```
Loss = Log-Loss + λ * Σ|βᵢ|
```

Where:
- `λ` (lambda or alpha) is the regularization strength
- `βᵢ` are the model coefficients
- Larger λ = stronger regularization = more coefficients become zero

## Key Characteristics

### Feature Selection
- **Sparsity**: Can set coefficients to exactly zero
- **Automatic feature selection**: Eliminates irrelevant features
- **Interpretability**: Easier to interpret models with fewer features

### Coefficient Shrinking
- Shrinks coefficients toward zero
- Can eliminate features entirely (coefficient = 0)
- More aggressive than L2 regularization

## Parameters

### Regularization Strength (λ or α)

- **Small λ (e.g., 0.001)**: Weak regularization, model behaves like unregularized version
- **Medium λ (e.g., 0.1)**: Moderate regularization, some features eliminated
- **Large λ (e.g., 1.0)**: Strong regularization, many features eliminated, may underfit

### Choosing λ

- Use cross-validation to find optimal λ
- Plot coefficient paths vs λ to visualize feature selection
- Balance between model complexity and performance

## Use Cases

✅ **Good for:**
- High-dimensional data (many features)
- Feature selection when you have many irrelevant features
- When you want an interpretable model with fewer features
- Sparse models (most coefficients are zero)
- When features are correlated (L1 can select one from a group)

❌ **Not ideal for:**
- When all features are important
- When you have more features than samples (can eliminate too many)
- When features are highly correlated (may arbitrarily select one)

## Pros and Cons

### Pros
- **Feature selection**: Automatically eliminates irrelevant features
- **Sparse models**: Produces models with fewer features
- **Interpretability**: Easier to understand with fewer features
- **Handles multicollinearity**: Can select one feature from correlated group

### Cons
- **Arbitrary selection**: May randomly select one feature from correlated group
- **Unstable**: Small changes in data can change selected features
- **Can eliminate important features**: If λ is too large
- **May not converge**: With highly correlated features

## Comparison with L2 Regularization

| Aspect | L1 (Lasso) | L2 (Ridge) |
|--------|------------|------------|
| Penalty | |β| | β² |
| Feature Selection | Yes (sparse) | No (dense) |
| Coefficient Values | Can be exactly 0 | Approaches 0 but never 0 |
| Use Case | Feature selection | Prevent overfitting |
| Stability | Less stable | More stable |

## Mathematical Foundation

The L1 penalty term:
```
Penalty = λ * Σ|βᵢ|
```

Optimization:
- Uses subgradient descent (since |x| is not differentiable at 0)
- Can use coordinate descent efficiently
- Convergence can be slower than L2

## When to Use L1 vs L2

- **Use L1**: When you have many features and suspect many are irrelevant
- **Use L2**: When you want to prevent overfitting but keep all features
- **Use Elastic Net**: Combine both L1 and L2 (best of both worlds)

## Code Example (Conceptual)

```python
from sklearn.linear_model import Lasso

# L1 Regularization (Lasso)
lasso = Lasso(alpha=0.1)  # alpha is λ
lasso.fit(X_train, y_train)

# Check which features were eliminated (coefficient = 0)
selected_features = lasso.coef_ != 0
print(f"Selected {selected_features.sum()} out of {len(selected_features)} features")
```

## References

- Tibshirani, R. (1996). "Regression Shrinkage and Selection via the Lasso"
- Scikit-learn: Lasso, LassoCV

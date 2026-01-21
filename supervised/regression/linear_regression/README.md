# Linear Regression

## Overview

Linear Regression is one of the simplest and most widely used regression algorithms. It models the relationship between a dependent variable (target) and one or more independent variables (features) using a linear equation.

## How It Works

Linear regression assumes a linear relationship between features and target:

**Simple Linear Regression** (one feature):
```
y = β₀ + β₁x + ε
```

**Multiple Linear Regression** (multiple features):
```
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε
```

Where:
- `y` is the predicted target value
- `β₀` is the y-intercept (bias term)
- `β₁, β₂, ..., βₙ` are coefficients (weights) for each feature
- `x₁, x₂, ..., xₙ` are the input features
- `ε` is the error term

The algorithm finds the best coefficients by minimizing the **Mean Squared Error (MSE)** or **Sum of Squared Residuals (SSR)**.

## Parameters

### Key Parameters (scikit-learn)

- **fit_intercept** (bool, default=True)
  - Whether to calculate the intercept. If False, the intercept is set to zero.

- **normalize** (bool, default=False)
  - Whether to normalize features before regression (deprecated, use StandardScaler instead).

- **copy_X** (bool, default=True)
  - Whether to copy X. If False, X may be overwritten.

- **n_jobs** (int, optional)
  - Number of jobs to use for computation. -1 means using all processors.

### Attributes (after fitting)

- **coef_** (array)
  - Estimated coefficients for the linear regression problem.

- **intercept_** (float or array)
  - Independent term in the linear model.

## Use Cases

✅ **Good for:**
- When there's a linear relationship between features and target
- Baseline model for regression problems
- Interpretable models where you need to understand feature importance
- Large datasets (fast training and prediction)

❌ **Not ideal for:**
- Non-linear relationships
- Data with high multicollinearity
- Outliers (sensitive to outliers)
- Complex patterns requiring non-linear models

## Example Use Cases

1. **House Price Prediction**: Predict house prices based on size, location, age
2. **Sales Forecasting**: Predict sales based on advertising spend, seasonality
3. **Temperature Prediction**: Predict temperature based on various weather features
4. **Stock Price Prediction**: Predict stock prices based on market indicators

## Pros and Cons

### Pros
- Simple and easy to understand
- Fast training and prediction
- Highly interpretable (coefficients show feature importance)
- No hyperparameter tuning needed
- Works well with large datasets

### Cons
- Assumes linear relationship (may not capture non-linear patterns)
- Sensitive to outliers
- Assumes features are independent (multicollinearity issues)
- May underfit complex data

## Mathematical Foundation

The coefficients are found using **Ordinary Least Squares (OLS)**:

```
β = (XᵀX)⁻¹Xᵀy
```

Where:
- `X` is the feature matrix
- `y` is the target vector
- `β` is the coefficient vector


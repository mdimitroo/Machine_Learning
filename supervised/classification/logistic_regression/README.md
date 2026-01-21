# Logistic Regression

## Overview

Logistic Regression is a classification algorithm used to predict binary or multiclass categorical outcomes. Despite its name, it's actually a classification algorithm, not a regression algorithm. It uses the logistic function (sigmoid) to model the probability of a class.

## How It Works

Logistic Regression models the probability that an instance belongs to a particular class using the logistic function:

**Binary Classification:**
```
P(y=1|x) = 1 / (1 + e^(-z))
```

Where `z = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ`

The logistic function (sigmoid) maps any real number to a value between 0 and 1, which can be interpreted as a probability.

**Decision Boundary:**
- If P(y=1|x) ≥ 0.5, predict class 1
- If P(y=1|x) < 0.5, predict class 0

The algorithm finds optimal coefficients by maximizing the **log-likelihood** (or minimizing the negative log-likelihood).

## Parameters

### Key Parameters (scikit-learn)

- **penalty** (str, default='l2')
  - Regularization type: 'l1', 'l2', 'elasticnet', or 'none'

- **C** (float, default=1.0)
  - Inverse of regularization strength. Smaller values specify stronger regularization.

- **solver** (str, default='lbfgs')
  - Algorithm for optimization: 'lbfgs', 'liblinear', 'newton-cg', 'sag', 'saga'

- **max_iter** (int, default=100)
  - Maximum number of iterations for convergence

- **multi_class** (str, default='auto')
  - Strategy for multiclass: 'ovr' (one-vs-rest) or 'multinomial'

### Attributes (after fitting)

- **coef_** (array)
  - Coefficient of the features in the decision function

- **intercept_** (array)
  - Intercept (bias) added to the decision function

- **classes_** (array)
  - List of class labels

## Use Cases

✅ **Good for:**
- Binary classification problems
- Multiclass classification
- When you need probability estimates
- Interpretable models (coefficients show feature importance)
- Baseline model for classification

❌ **Not ideal for:**
- Non-linear decision boundaries
- Very large datasets (can be slow)
- When features are highly correlated
- Complex patterns requiring non-linear models

## Example Use Cases

1. **Email Spam Detection**: Classify emails as spam or not spam
2. **Medical Diagnosis**: Predict disease presence (yes/no)
3. **Customer Churn**: Predict if a customer will churn
4. **Image Classification**: Binary image classification tasks
5. **Sentiment Analysis**: Classify text as positive/negative

## Pros and Cons

### Pros
- Simple and interpretable
- Provides probability estimates
- Fast training and prediction
- No hyperparameter tuning required for basic use
- Works well as a baseline model

### Cons
- Assumes linear decision boundary
- Sensitive to outliers
- Requires feature scaling for best performance
- May underfit complex data

## Mathematical Foundation

The cost function (log-loss) for binary classification:

```
J(θ) = -(1/m) Σ [y·log(h(x)) + (1-y)·log(1-h(x))]
```

Where:
- `h(x)` is the sigmoid function
- `y` is the true label (0 or 1)
- `m` is the number of samples


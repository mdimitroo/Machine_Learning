# Gradient Descent

## Overview

Gradient Descent is an optimization algorithm used to minimize a cost function by iteratively moving in the direction of steepest descent (negative gradient). It's the foundation of training most machine learning models, especially neural networks.

## How It Works

### Basic Concept

1. **Start** with random initial parameters (weights)
2. **Calculate** the gradient (derivative) of the cost function
3. **Update** parameters by moving in the opposite direction of the gradient
4. **Repeat** until convergence (gradient ≈ 0)

### Update Rule

```
θ = θ - α * ∇J(θ)
```

Where:
- `θ` are the parameters (weights)
- `α` (alpha) is the learning rate
- `∇J(θ)` is the gradient of the cost function

### Intuition

Imagine standing on a mountain and wanting to reach the bottom:
- **Gradient** points in the direction of steepest ascent
- **Negative gradient** points in the direction of steepest descent
- **Learning rate** determines step size
- Take steps in the direction of steepest descent

## Types of Gradient Descent

### 1. Batch Gradient Descent
- Uses **entire dataset** to compute gradient
- **Pros**: Stable, guaranteed convergence
- **Cons**: Slow for large datasets, requires all data in memory
- **Use case**: Small to medium datasets

### 2. Stochastic Gradient Descent (SGD)
- Uses **single sample** to compute gradient
- **Pros**: Fast, can escape local minima, works with large datasets
- **Cons**: Noisy updates, may not converge smoothly
- **Use case**: Large datasets, online learning

### 3. Mini-Batch Gradient Descent
- Uses **small batch** of samples (typically 32, 64, 128)
- **Pros**: Balance between speed and stability
- **Cons**: Need to tune batch size
- **Use case**: Most common in practice (default for neural networks)

## Learning Rate

### Importance
- **Too small**: Slow convergence, may get stuck in local minima
- **Too large**: May overshoot minimum, diverge, or oscillate
- **Optimal**: Fast convergence without overshooting

### Learning Rate Schedules

1. **Fixed**: Constant learning rate
2. **Decay**: Gradually decrease over time
   - `α(t) = α₀ / (1 + decay_rate * t)`
3. **Step**: Reduce at specific epochs
4. **Adaptive**: Algorithms like Adam adjust automatically

## Convergence

### Stopping Criteria
- **Gradient magnitude**: Stop when ||∇J(θ)|| < ε
- **Change in cost**: Stop when |J(θₜ) - J(θₜ₋₁)| < ε
- **Maximum iterations**: Stop after N iterations
- **Validation performance**: Stop when validation error stops improving

## Challenges

### 1. Local Minima
- Gradient descent may get stuck in local minimum
- **Solution**: Random initialization, momentum, different starting points

### 2. Saddle Points
- Points where gradient is zero but not a minimum
- **Solution**: Momentum helps escape saddle points

### 3. Vanishing/Exploding Gradients
- Gradients become very small (vanishing) or very large (exploding)
- **Solution**: Proper initialization, gradient clipping, normalization

## Momentum

Adds a "velocity" term to smooth updates:

```
v = β * v + (1 - β) * ∇J(θ)
θ = θ - α * v
```

Where `β` is momentum coefficient (typically 0.9)

**Benefits:**
- Smoother convergence
- Faster convergence
- Helps escape local minima and saddle points

## Code Example (Conceptual)

```python
# Simple gradient descent
def gradient_descent(X, y, learning_rate=0.01, iterations=1000):
    m = len(y)
    theta = np.zeros(X.shape[1])
    
    for i in range(iterations):
        # Calculate gradient
        predictions = X @ theta
        errors = predictions - y
        gradient = (1/m) * X.T @ errors
        
        # Update parameters
        theta = theta - learning_rate * gradient
        
        # Optional: Check convergence
        if np.linalg.norm(gradient) < 1e-6:
            break
    
    return theta
```

## When to Use

✅ **Use Gradient Descent:**
- Training neural networks
- Linear/logistic regression
- Any differentiable cost function
- Large-scale optimization problems

❌ **Alternatives:**
- **Normal equations**: For linear regression (closed-form solution)
- **Newton's method**: When you can compute Hessian (faster but expensive)

## Best Practices

1. **Normalize features**: Gradient descent works better with scaled features
2. **Choose appropriate learning rate**: Start with 0.01, adjust based on results
3. **Use mini-batches**: Balance between speed and stability
4. **Monitor convergence**: Plot cost function over iterations
5. **Use momentum**: Especially for non-convex problems

## References

- Optimization in machine learning
- Gradient descent variants and improvements

# Cross-Validation

## Overview

Cross-validation is a resampling technique used to assess how well a model generalizes to an independent dataset. It helps estimate model performance more reliably than a single train-test split and is essential for model selection and hyperparameter tuning.

## Why Cross-Validation?

### Problems with Single Train-Test Split
- **High variance**: Performance depends heavily on which samples are in train/test
- **Wasteful**: Doesn't use all available data for training
- **Unreliable**: Single performance estimate may not reflect true model capability

### Benefits of Cross-Validation
- **More reliable estimates**: Average performance across multiple splits
- **Better data usage**: All data used for both training and validation
- **Reduces overfitting**: More robust model evaluation

## K-Fold Cross-Validation

The most common cross-validation technique.

### Process

1. **Split data into k folds** (typically k=5 or k=10)
2. **For each fold**:
   - Use (k-1) folds for training
   - Use 1 fold for validation
   - Train model and evaluate
3. **Average results** across all k folds

### Example: 5-Fold CV

```
Fold 1: [Train: Folds 2,3,4,5] [Val: Fold 1]
Fold 2: [Train: Folds 1,3,4,5] [Val: Fold 2]
Fold 3: [Train: Folds 1,2,4,5] [Val: Fold 3]
Fold 4: [Train: Folds 1,2,3,5] [Val: Fold 4]
Fold 5: [Train: Folds 1,2,3,4] [Val: Fold 5]

Final Score = Average of all 5 validation scores
```

## Types of Cross-Validation

### 1. K-Fold Cross-Validation
- **k folds**: Typically 5 or 10
- **Random shuffling**: Data shuffled before splitting
- **Use case**: General purpose, balanced datasets

### 2. Stratified K-Fold
- **Preserves class distribution**: Each fold has same class proportions
- **Use case**: Classification with imbalanced classes
- **Important**: Prevents some folds from having no samples of minority class

### 3. Leave-One-Out Cross-Validation (LOOCV)
- **k = n**: Each sample is validation set once
- **Maximum data usage**: Uses (n-1) samples for training
- **Computationally expensive**: Requires n model trainings
- **Use case**: Small datasets

### 4. Time Series Cross-Validation
- **Respects temporal order**: No random shuffling
- **Forward chaining**: Train on past, validate on future
- **Use case**: Time series data

## Parameters

### Number of Folds (k)

- **k=5**: Good balance between computation and reliability
- **k=10**: More reliable but more computation
- **k=n (LOOCV)**: Maximum reliability, very expensive
- **Common choice**: k=5 or k=10

### Shuffle

- **shuffle=True**: Randomize data before splitting
- **shuffle=False**: Keep original order
- **Use False**: For time series or when order matters

## When to Use

✅ **Use Cross-Validation:**
- Model selection (comparing different algorithms)
- Hyperparameter tuning
- Getting reliable performance estimates
- Small datasets (maximize data usage)

❌ **Don't Use:**
- Final model evaluation (use held-out test set)
- Time series (use time-based splits)
- When computation is extremely limited

## Common Workflow

```
1. Split data: Train + Test (80/20 or 70/30)
2. Use Cross-Validation on Train set:
   - Model selection
   - Hyperparameter tuning
   - Feature selection
3. Train final model on entire Train set
4. Evaluate on Test set (final performance estimate)
```

## Pros and Cons

### Pros
- More reliable performance estimates
- Better use of available data
- Reduces overfitting risk
- Standard practice in ML

### Cons
- More computation (k times more training)
- Can be slow for large datasets
- Doesn't eliminate need for test set

## Code Example (Conceptual)

```python
from sklearn.model_selection import cross_val_score, KFold

# K-Fold Cross-Validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')

print(f"CV Scores: {scores}")
print(f"Mean CV Score: {scores.mean():.4f}")
print(f"Std CV Score: {scores.std():.4f}")

# Stratified K-Fold (for classification)
from sklearn.model_selection import StratifiedKFold
skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

## Best Practices

1. **Always use stratified CV for classification** with imbalanced classes
2. **Use separate test set** for final evaluation (don't use CV on test set)
3. **Shuffle data** unless it's time series
4. **Report mean and std** of CV scores
5. **Use appropriate k**: 5-10 folds is usually sufficient

## References

- Scikit-learn: cross_val_score, KFold, StratifiedKFold
- Model evaluation best practices

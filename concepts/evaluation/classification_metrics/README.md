# Classification Metrics

## Overview

Classification metrics measure how well a classification model performs. Different metrics provide different insights into model performance, and the choice of metric depends on the problem and class distribution.

## Confusion Matrix

Foundation for most classification metrics. Shows predictions vs actual labels:

```
                Predicted
              Negative  Positive
Actual Negative   TN      FP
       Positive   FN      TP
```

Where:
- **TP (True Positive)**: Correctly predicted positive
- **TN (True Negative)**: Correctly predicted negative
- **FP (False Positive)**: Incorrectly predicted positive (Type I error)
- **FN (False Negative)**: Incorrectly predicted negative (Type II error)

## Key Metrics

### 1. Accuracy
**Formula**: `(TP + TN) / (TP + TN + FP + FN)`

**Interpretation**: Overall correctness of predictions

**When to Use**:
- Balanced classes
- Equal cost of errors
- General performance indicator

**Limitations**:
- Misleading with imbalanced classes
- Doesn't show which class is predicted better

### 2. Precision
**Formula**: `TP / (TP + FP)`

**Interpretation**: Of all positive predictions, how many are correct?

**When to Use**:
- When false positives are costly
- Example: Spam detection (don't want to mark good emails as spam)

**High Precision**: "When I predict positive, I'm usually right"

### 3. Recall (Sensitivity)
**Formula**: `TP / (TP + FN)`

**Interpretation**: Of all actual positives, how many did we catch?

**When to Use**:
- When false negatives are costly
- Example: Disease detection (don't want to miss diseases)

**High Recall**: "I catch most of the positive cases"

### 4. F1-Score
**Formula**: `2 * (Precision * Recall) / (Precision + Recall)`

**Interpretation**: Harmonic mean of precision and recall

**When to Use**:
- Need balance between precision and recall
- Single metric to optimize
- Imbalanced classes

**Range**: 0 to 1 (higher is better)

### 5. Specificity
**Formula**: `TN / (TN + FP)`

**Interpretation**: Of all actual negatives, how many did we correctly identify?

**When to Use**:
- Important to correctly identify negative cases
- Medical testing (true negative rate)

## Precision-Recall Tradeoff

- **High Precision, Low Recall**: Very confident positive predictions, but miss many positives
- **Low Precision, High Recall**: Catch most positives, but many false positives
- **Balanced**: Moderate precision and recall

**Adjusting Threshold**:
- **Lower threshold**: More positive predictions → Higher recall, Lower precision
- **Higher threshold**: Fewer positive predictions → Lower recall, Higher precision

## ROC Curve & AUC

### ROC Curve (Receiver Operating Characteristic)
- **X-axis**: False Positive Rate (1 - Specificity)
- **Y-axis**: True Positive Rate (Recall/Sensitivity)
- Shows performance at different classification thresholds

### AUC (Area Under Curve)
- **Range**: 0 to 1
- **0.5**: Random classifier
- **1.0**: Perfect classifier
- **>0.8**: Good classifier

**When to Use**:
- Compare models
- Threshold-independent metric
- Works well with imbalanced classes

## Multi-Class Metrics

### Macro-Averaged
- Calculate metric for each class
- Average across classes
- Treats all classes equally

### Micro-Averaged
- Aggregate all TP, TN, FP, FN
- Calculate metric from aggregates
- Weighted by class frequency

### Weighted-Averaged
- Calculate metric for each class
- Average weighted by class frequency
- Accounts for class imbalance

## Choosing the Right Metric

### Balanced Classes
- **Accuracy**: Good overall measure
- **F1-Score**: Balanced precision/recall

### Imbalanced Classes
- **Precision**: If false positives costly
- **Recall**: If false negatives costly
- **F1-Score**: Balance both
- **AUC-ROC**: Threshold-independent

### Specific Use Cases
- **Medical Diagnosis**: High recall (don't miss diseases)
- **Spam Detection**: High precision (don't mark good emails as spam)
- **Fraud Detection**: High precision (minimize false alarms)

## Code Example (Conceptual)

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, roc_auc_score
)

# Calculate metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
cm = confusion_matrix(y_true, y_pred)

# For probabilities
auc = roc_auc_score(y_true, y_proba)
```

## Best Practices

1. **Use multiple metrics**: No single metric tells the whole story
2. **Consider business context**: Which errors are more costly?
3. **Plot confusion matrix**: Visual understanding of errors
4. **Use appropriate metric for problem**: Precision vs Recall tradeoff
5. **Report metrics for each class**: In multi-class problems

## Summary Table

| Metric | Formula | Use Case | Range |
|--------|---------|----------|-------|
| Accuracy | (TP+TN)/Total | Balanced classes | 0-1 |
| Precision | TP/(TP+FP) | Minimize false positives | 0-1 |
| Recall | TP/(TP+FN) | Minimize false negatives | 0-1 |
| F1-Score | 2PR/(P+R) | Balance precision/recall | 0-1 |
| AUC-ROC | Area under ROC | Model comparison | 0-1 |

## References

- Scikit-learn metrics documentation
- Understanding classification metrics

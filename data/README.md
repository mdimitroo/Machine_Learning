# Datasets

This directory contains sample datasets used for demonstrating various machine learning models.

## Dataset Descriptions

### Regression Datasets
- **housing.csv**: House price prediction dataset
- **salary.csv**: Salary vs experience dataset

### Classification Datasets
- **iris.csv**: Classic iris flower classification dataset
- **wine.csv**: Wine quality classification dataset

### Clustering Datasets
- **customer_data.csv**: Customer segmentation dataset
- **blobs.csv**: Synthetic blob dataset for clustering

## Usage

Datasets can be loaded using pandas:

```python
import pandas as pd

# Load a dataset
df = pd.read_csv('data/housing.csv')
```

## Data Sources

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- Synthetic datasets generated for demonstration

## Note

Some datasets may be too large for GitHub. Consider using Git LFS or providing download links.

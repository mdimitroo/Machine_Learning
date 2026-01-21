# Machine Learning Models Repository

A comprehensive collection of machine learning models with detailed explanations, parameter documentation, and use-cases. This repository serves as both a learning resource and a reference guide for various ML algorithms.

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Supervised Learning](#supervised-learning)
- [Unsupervised Learning](#unsupervised-learning)
- [Getting Started](#getting-started)
- [Contributing](#contributing)

## Overview

This repository contains explanations and documentation of various machine learning models, organized by learning type. Each model includes:

- **Theory**: How the algorithm works
- **Parameters**: Detailed parameter documentation
- **Use Cases**: When to use each model
- **Pros & Cons**: Advantages and limitations

## Repository Structure

```
Machine_Learning/
│
├── README.md                 # This file - main overview
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore file
│
├── supervised/              # Supervised learning models
│   ├── README.md            # Overview of supervised learning
│   ├── regression/          # Regression models
│   │   ├── linear_regression/
│   │   ├── polynomial_regression/
│   │   ├── ridge_regression/
│   │   ├── lasso_regression/
│   │   └── random_forest_regression/
│   │
│   └── classification/      # Classification models
│       ├── logistic_regression/
│       ├── decision_tree/
│       ├── random_forest/
│       ├── svm/
│       ├── naive_bayes/
│       ├── knn/
│       └── neural_networks/
│
├── unsupervised/            # Unsupervised learning models
│   ├── README.md            # Overview of unsupervised learning
│   ├── clustering/          # Clustering algorithms
│   │   ├── kmeans/
│   │   ├── hierarchical_clustering/
│   │   ├── dbscan/
│   │   └── gaussian_mixture/
│   │
│   └── dimensionality_reduction/  # Dimensionality reduction
│       ├── pca/
│       ├── t_sne/
│       └── autoencoders/
│
├── concepts/                # ML concepts & techniques
│   ├── README.md            # Overview of concepts
│   ├── preprocessing/       # Data preprocessing techniques
│   ├── regularization/     # Regularization methods
│   ├── evaluation/          # Model evaluation techniques
│   ├── optimization/        # Optimization algorithms
│   ├── feature_engineering/ # Feature engineering methods
│   ├── hyperparameter_tuning/ # Hyperparameter tuning
│   ├── ensemble_methods/    # Ensemble techniques
│   ├── loss_functions/      # Loss functions
│   ├── overfitting_underfitting/ # Model complexity
│   └── data_imbalance/      # Handling imbalanced data
│
├── data/                    # Sample datasets
│   └── README.md            # Dataset descriptions
│
└── utils/                   # Utility functions
    ├── __init__.py
    ├── data_preprocessing.py
    └── visualization.py
```

## Supervised Learning

Models that learn from labeled training data.

### Regression Models
- **Linear Regression**: Predicting continuous values using a linear relationship
- **Polynomial Regression**: Non-linear relationships using polynomial features
- **Ridge Regression**: Linear regression with L2 regularization
- **Lasso Regression**: Linear regression with L1 regularization
- **Random Forest Regression**: Ensemble method using multiple decision trees

### Classification Models
- **Logistic Regression**: Binary and multiclass classification using logistic function
- **Decision Tree**: Tree-based model for classification
- **Random Forest**: Ensemble of decision trees
- **Support Vector Machine (SVM)**: Finding optimal hyperplane for classification
- **Naive Bayes**: Probabilistic classifier based on Bayes' theorem
- **K-Nearest Neighbors (KNN)**: Instance-based learning algorithm
- **Neural Networks**: Deep learning models for complex patterns

## Unsupervised Learning

Models that find patterns in unlabeled data.

### Clustering Algorithms
- **K-Means**: Partitioning data into k clusters
- **Hierarchical Clustering**: Building a tree of clusters
- **DBSCAN**: Density-based clustering
- **Gaussian Mixture Models**: Probabilistic clustering

### Dimensionality Reduction
- **Principal Component Analysis (PCA)**: Reducing dimensions while preserving variance
- **t-SNE**: Non-linear dimensionality reduction for visualization
- **Autoencoders**: Neural networks for feature extraction

## ML Concepts & Techniques

Fundamental concepts essential for understanding and implementing ML models effectively.

### Core Concepts
- **Data Preprocessing**: Normalization, standardization, handling missing values
- **Regularization**: L1 (Lasso), L2 (Ridge), Elastic Net, Dropout
- **Model Evaluation**: Cross-validation, metrics, bias-variance tradeoff
- **Optimization**: Gradient descent, SGD, learning rate, Adam optimizer
- **Feature Engineering**: Feature selection, extraction, importance
- **Hyperparameter Tuning**: Grid search, random search, Bayesian optimization
- **Ensemble Methods**: Bagging, boosting, stacking
- **Loss Functions**: MSE, MAE, cross-entropy, hinge loss
- **Overfitting & Underfitting**: Model complexity, regularization
- **Data Imbalance**: SMOTE, class weighting, resampling
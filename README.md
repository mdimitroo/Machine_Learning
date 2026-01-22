# Machine Learning Models Repository

A comprehensive collection of machine learning models with detailed explanations, parameter documentation, and use-cases. This repository serves as both a learning resource and a reference guide for various ML algorithms.

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Supervised Learning](#supervised-learning)
- [Unsupervised Learning](#unsupervised-learning)
- [Reinforcement Learning](#reinforcement-learning)
- [ML Concepts & Techniques](#ml-concepts--techniques)

## Overview

This repository contains explanations and documentation of various machine learning models, organized by learning type. Each model includes:

- **Theory**: How the algorithm works
- **Parameters**: Detailed parameter documentation
- **Use Cases**: When to use each model
- **Pros & Cons**: Advantages and limitations
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

## Reinforcement Learning

Models that learn optimal actions through interaction with an environment to maximize cumulative reward.

### Value-Based Algorithms
- **Q-Learning**: Off-policy value-based algorithm using Q-function
- **Deep Q-Network (DQN)**: Q-learning with deep neural networks
- **Double DQN**: Addresses overestimation bias in DQN
- **Dueling DQN**: Separates value and advantage estimation

### Policy-Based Algorithms
- **REINFORCE**: Monte Carlo policy gradient method
- **Policy Gradient**: Direct policy optimization using gradients
- **Natural Policy Gradient**: Uses natural gradient for policy updates

### Actor-Critic Algorithms
- **Actor-Critic**: Combines value function and policy learning
- **Proximal Policy Optimization (PPO)**: Stable policy optimization with clipping
- **Soft Actor-Critic (SAC)**: Off-policy maximum entropy RL
- **Deep Deterministic Policy Gradient (DDPG)**: Continuous action spaces

### Model-Based Algorithms
- **Dyna-Q**: Combines Q-learning with environment model
- **Model Predictive Control (MPC)**: Uses learned model for planning

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
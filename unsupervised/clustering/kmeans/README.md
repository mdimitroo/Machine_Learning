# K-Means Clustering

## Overview

K-Means is one of the most popular and simple clustering algorithms. It partitions data into k clusters, where each data point belongs to the cluster with the nearest mean (centroid). It's an iterative algorithm that minimizes within-cluster variance.

## How It Works

K-Means follows these steps:

1. **Initialize**: Randomly select k centroids (cluster centers)
2. **Assign**: Assign each data point to the nearest centroid
3. **Update**: Recalculate centroids as the mean of all points in each cluster
4. **Repeat**: Steps 2-3 until centroids don't change (convergence)

**Objective Function** (Within-Cluster Sum of Squares - WCSS):
```
J = Σᵢ₌₁ᵏ Σₓ∈Cᵢ ||x - μᵢ||²
```

Where:
- `k` is the number of clusters
- `Cᵢ` is the i-th cluster
- `μᵢ` is the centroid of cluster i
- `||x - μᵢ||²` is the squared distance from point x to centroid μᵢ

## Parameters

### Key Parameters (scikit-learn)

- **n_clusters** (int, default=8)
  - Number of clusters to form (k value). This is the most important parameter.

- **init** (str or array, default='k-means++')
  - Initialization method: 'k-means++' (smart initialization), 'random', or array of centroids

- **n_init** (int, default=10)
  - Number of times the algorithm will run with different centroid seeds

- **max_iter** (int, default=300)
  - Maximum number of iterations for a single run

- **tol** (float, default=1e-4)
  - Tolerance for convergence (relative change in inertia)

- **random_state** (int, optional)
  - Seed for random number generation (for reproducibility)

### Attributes (after fitting)

- **cluster_centers_** (array)
  - Coordinates of cluster centers

- **labels_** (array)
  - Labels of each point (which cluster it belongs to)

- **inertia_** (float)
  - Sum of squared distances of samples to their closest cluster center (WCSS)

## Use Cases

✅ **Good for:**
- When you know the number of clusters beforehand
- Spherical, well-separated clusters
- Large datasets (scalable)
- Customer segmentation
- Image compression
- Anomaly detection

❌ **Not ideal for:**
- Unknown number of clusters
- Non-spherical clusters
- Clusters of different sizes
- Clusters with varying densities
- Data with outliers

## Example Use Cases

1. **Customer Segmentation**: Group customers by purchasing behavior
2. **Image Compression**: Reduce color palette in images
3. **Document Clustering**: Group similar documents together
4. **Market Research**: Identify market segments
5. **Anomaly Detection**: Find outliers as points far from any centroid

## Pros and Cons

### Pros
- Simple and easy to understand
- Fast and efficient (O(n·k·d·iterations))
- Scales well to large datasets
- Works well with spherical clusters
- Guaranteed convergence

### Cons
- Requires specifying k (number of clusters) beforehand
- Sensitive to initialization (may converge to local minima)
- Assumes spherical clusters
- Sensitive to outliers
- May not work well with clusters of different sizes/densities

## Choosing K (Number of Clusters)

Common methods:
1. **Elbow Method**: Plot inertia vs k, look for "elbow"
2. **Silhouette Analysis**: Measure how similar objects are to their own cluster vs other clusters
3. **Domain Knowledge**: Use prior knowledge about the data


import numpy as np
from sklearn.datasets import make_regression

np.random.seed(42)

# Dataset sizes
sizes = [10, 100, 1000, 10_000, 100_000]

for size in sizes:
    n_features = int(np.sqrt(size) * 1.5)
    X, y = make_regression(n_samples=size, n_features=n_features, noise=10)

import numpy as np
import pandas as pd
from sklearn.datasets import make_regression

# Set random seed for reproducibility
np.random.seed(42)

# Example dataset size
size = 1000

# Number of features determined by size
n_features = int(np.sqrt(size) * 1.5)

# Create data
X, y = make_regression(n_samples=size, n_features=n_features, noise=10)

# Generate IDs for each row
ids = ["entity" + str(i) for i in range(1, len(X) + 1)]

# Create a dictionary to hold data
data_dict = {"ID": ids}
for i in range(n_features):
    data_dict[f"x{i+1}"] = X[:, i]
data_dict["y"] = y

# Create a DataFrame with the data
data = pd.DataFrame(data_dict)

# Save the DataFrame to a CSV file
data.to_csv("data.csv", index=False)

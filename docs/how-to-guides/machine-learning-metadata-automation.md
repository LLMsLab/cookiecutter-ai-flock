# Automating Machine Learning Model Metadata Creation

!!! tip "Automate Metadata Creation using `JSON` files"
    This guide provides a step-by-step approach to automate the creation of metadata for machine learning models, using a Python script. It includes an example script that trains a linear regression model, saves it, and generates a corresponding JSON metadata file.

## Overview
- The script demonstrates training a linear regression model using Scikit-Learn, saving the model as a `.pkl` file, and generating a metadata file in JSON format.
- The metadata includes model parameters, performance metrics, and data description.

## Example Script
```python
import json
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_boston
import joblib

# Load sample data
data = load_boston()
X = data.data
y = data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict using the model
y_pred = model.predict(X_test)

# Calculate performance metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save the model
model_filename = 'linear_regression_model.pkl'
joblib.dump(model, model_filename)

# Metadata
metadata = {
    'model_name': 'Linear Regression',
    'timestamp': '20240123',
    'model_parameters': model.get_params(),
    'performance_metrics': {
        'mean_squared_error': mse,
        'r2_score': r2
    },
    'data_description': 'Boston housing dataset',
    'feature_names': data.feature_names.tolist(),
    'target_name': 'Housing Price'
}

# Save metadata to a JSON file
metadata_filename = 'service_sage_v1.2.0_linearReg_20240123_metadata.json'
with open(metadata_filename, 'w') as f:
    json.dump(metadata, f, indent=4)

print(f"Model and metadata saved as {model_filename} and {metadata_filename} respectively.")
```

## Script Explanation
- The Boston housing dataset is used for demonstration purposes.
- A linear regression model is trained on the dataset.
- Performance metrics like Mean Squared Error (MSE) and R-squared (R2) are calculated.
- The model is saved as a `.pkl` file, and metadata is saved in a `.json` file.

## Hypothetical Output
```json
{
    "model_name": "Linear Regression",
    "timestamp": "20240123",
    "model_parameters": {
        "copy_X": true,
        "fit_intercept": true,
        "n_jobs": null,
        "normalize": false
    },
    "performance_metrics": {
        "mean_squared_error": 24.291119474973684,
        "r2_score": 0.6687594935356314
    },
    "data_description": "Boston housing dataset",
    "feature_names": [
        "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
    ],
    "target_name": "Housing Price"
}
```
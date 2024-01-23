# Naming Conventions for Project Assets

<!--
TODO:

- Include a max number of characters for the branching names
- Include guide to produce descriptive and sort <branch_names>
- Explain why we do not use `/` or `-`
- I guess we do not need the `junk` and `wip` branches
- Include a table to describe the branch type briefly
- Create a pre-commit hook to enforce using branch and file naming conventions
-->

## Model Persistence File Naming Conventions

!!! info "Model Persistence File"
    ```<project_name>_<model_version>_<model_type>_<timestamp>.pkl```

When persisting machine learning models, adopting a consistent naming
convention for binary files is crucial. This ensures easy identification
and management of different model versions across various projects. The
recommended format now includes the project name, model version, model
type, and a timestamp.

| Field           | Definition                                           |
|-----------------|------------------------------------------------------|
| `project_name`  | The name of the project the model is associated with |
| `model_version` | The version of the model, following semantic versioning (MAJOR.MINOR.PATCH) |
| `model_type`    | Type or name of the model (e.g., linearReg, neuralNet) |
| `timestamp`     | Date when the model was persisted (YYYYMMDD format)  |

### Examples

- `service_sage_v1.2.0_linearReg_20240123.pkl` - Indicates a linear
  regression model from the Service Sage project, version 1.2.0, updated
  on January 23, 2024.
- `one_assist_v3.0.1_neuralNet_20240215.pkl` - Represents a neural
  network model for One Assist, version 3.0.1, updated on February 15,
  2024.

### Versioning Scheme

- **MAJOR:** Incremented for incompatible API changes.
- **MINOR:** Incremented for adding functionality in a
  backward-compatible manner.
- **PATCH:** Incremented for backward-compatible bug fixes.

### Metadata Storage

- Alongside each model file, store a corresponding JSON file containing
  model metadata (e.g.,
  `service_sage_v1.2.0_linearReg_20240123_metadata.json`). This should
  include information about training data, model parameters, performance
  metrics, etc.

### Documentation and Registry

- Maintain a Makefile to automate the documentation or registry
  generation process. This file should include commands to create and
  update a comprehensive list of all models, their versions,
  descriptions, and changelogs for team collaboration and future
  reference.

### Automate Metadata Creation using `JSON` files

Below is an example of a Python script that trains a simple linear
regression model using Scikit-Learn, then saves the model along with a
JSON file containing metadata. The metadata includes information such as
the model's parameters, performance metrics, and training data
characteristics.

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

In this script:

- The Boston housing dataset is used for demonstration purposes.
- A linear regression model is trained on the dataset.
- The model is then used to make predictions on the test set.
- Performance metrics like Mean Squared Error (MSE) and R-squared (R2)
  are calculated.
- The model is saved as a pickle file using `joblib`.
- Metadata including model parameters, performance metrics, and data
  description are saved in a JSON file.

This script provides a basic framework. You might need to adjust it
according to the specifics of your dataset, model, and required metadata
details.

Assuming the script has been run as provided, the output of the JSON
file (`service_sage_v1.2.0_linearReg_20240123_metadata.json`) would
hypothetically look like this:

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

In this hypothetical example:

- The `model_parameters` section includes the parameters used for the
  linear regression model. These values are defaults from Scikit-Learn's
  `LinearRegression`.
- The `performance_metrics` show the Mean Squared Error (MSE) and
  R-squared (R2) values calculated from the model's predictions on the
  test dataset. The actual numbers (24.291119474973684 for MSE and
  0.6687594935356314 for R2) are hypothetical and would vary based on
  the training and test data splits, as well as any changes in model
  parameters or the underlying data.
- The `data_description`, `feature_names`, and `target_name` provide
  context about the dataset used for training the model.

### Using Markdown files for Model Documentation

Here's a Markdown file
(`service_sage_v1.2.0_linearReg_20240123_documentation.md`) that
documents the process and output of the Python script for training a
linear regression model and generating its metadata file. This
documentation can be included in your project repository to explain the
model and metadata creation process.

```markdown
# Linear Regression Model Documentation

## Overview
This document describes the process of training a Linear Regression model using the Boston housing dataset. It also details the generation of a metadata file that accompanies the model, capturing essential information about the model parameters, performance metrics, and data characteristics.

## Model Training
The model is trained using the Boston housing dataset from Scikit-Learn. We perform a basic train-test split, train a Linear Regression model using the training data, and then evaluate its performance on the test data.

### Data
- **Dataset Used**: Boston Housing Dataset
- **Features**: CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT
- **Target**: Housing Price

## Model Parameters
The model is trained with the following parameters:
- **fit_intercept**: true
- **normalize**: false
- **copy_X**: true
- **n_jobs**: null

These parameters are the default settings for Scikit-Learn's LinearRegression model.

## Performance Metrics
The model's performance is evaluated using the following metrics:
- **Mean Squared Error (MSE)**
- **R-squared (R2)**

The values for these metrics are computed based on the model's predictions on the test set.

## Metadata File
Alongside the model, a metadata file (`service_sage_v1.2.0_linearReg_20240123_metadata.json`) is generated. This JSON file includes:
- **Model Name**: Linear Regression
- **Timestamp**: Date when the model is trained and metadata is generated.
- **Model Parameters**: A list of parameters used to train the model.
- **Performance Metrics**: MSE and R2 values calculated from the test set.
- **Data Description**: Brief description of the dataset used.
- **Feature Names**: List of feature names from the dataset.
- **Target Name**: Name of the target variable.

## File Generation
The model is saved as a pickle file (`service_sage_v1.2.0_linearReg_20240123.pkl`), and the metadata is stored in a JSON file (`service_sage_v1.2.0_linearReg_20240123_metadata.json`). These files provide a snapshot of the model at the time of training, along with relevant information about its performance and configuration.
```

This Markdown file offers a concise yet comprehensive overview of the
model training and metadata generation process, suitable for inclusion
in project documentation or a repository readme. It explains the
dataset, model parameters, performance metrics, and the structure of the
generated metadata file.

### Directory Structure

Store related files in the same directory. For better organization,
especially for projects with multiple models, use subdirectories:

```bash
/models
    /service_sage_v1.2.0_linearReg_20240123
        service_sage_v1.2.0_linearReg_20240123.pkl
        service_sage_v1.2.0_linearReg_20240123_metadata.json
        service_sage_v1.2.0_linearReg_20240123.pkl_documentation.md
```




<!--
## GitHub repositories naming convention

!!! info "Name of the GitHub repository"
    `lowercase-with-hyphens`

!!! example
    `data-science-life-cycle`

## Git Branch Naming Conventions

!!! info "Git branch"
    ```<author>_<issue_number>_<branch_type>_<branch_name>```

| Field          | Definition            |
|----------------|-----------------------|
| `author`       | User T-number         |
| `issue_number` | Issue tracking number |
| `branch_type`  | Branch type           |
| `branch_name`  | Branch description    |

Branch type:

| Branch Type | Branch Description                                    |
|-------------|-------------------------------------------------------|
| ask         | Ask issue                                             |
| daa         | Data acquisition issue                                |
| dac         | Data creation issue                                   |
| expl        | Explore issue                                         |
| expe        | Experiment issue                                      |
| mdl         | Model issue                                           |
| fea         | Feature I'm adding or expanding                       |
| bug         | Bug fix                                               |
| htfx        | Hotfix                                                |
| wip         | Work in progress; stuff I know won't be finished soon |
| junk        | Throwaway branch created to experiment                |

!!! example
    ```text
    t93kqi0_1_ask_parent_issue
    t93kqi0_3_daa_gathering_data_from_sources
    t93kqi0_5_dac_creating_new_datasets
    t93kqi0_7_expl_exploratory_data_analysis
    t93kqi0_9_expe_feature_engineering
    t93kqi0_11_expe_model_training
    t93kqi0_20_modl_tests
    t93kqi0_40_modl_pipelines
    t93kqi0_45_modl_parametrizing_runs
    t93kqi0_170_modl_monitoring
    t93kqi0_220_modl_loging
    t93kqi0_250_modl_loging
    t93kqi0_300_bug_wrong_data_type
    ```

## Python files naming conventions

All scripts under the same branch must be authored and sharing the same
issue tracker to help to link all repo's assets. We do not want to
include the branch type or the branch name because it is redundant (all
script below the same issue tracker share the same branch type and branch
name) and become produce too long names.

!!! info "Python file name convention"
    ```<issue_number>_<internal_order>_<script_name>```

!!! example
    ```console
    28_01_model_data_prep.py
    28_02_model_selection.py
    28_03_model_evaluation.py
    28_04_model_final.py
    28_05_model_report.py
    28_06_model_pipeline.py
    ```

!!! danger
    Python programing scripts should start by a letter and not by a
    number. This is because they are Python modules. To import a Python
    module we cannot use numbers at the beginning of the file name.

Maybe use this instead...but it is too long. Using the type of branch
type is another possibility.

!!! info "Python file name convention"
    ```<author>_<issue_number>_<internal_order>_<script_name>```

!!! note
    The `<internal_order>` number automatically sort files in
    the same order they must be executed.

Notice that if there are severeal different models families like
baseline and incremental (different families of models) we cannot
distinguish between them. Maybe, it make sense to include a more
descriptive name. In this example, `expl` is the type of branch and
`service_calls` is the name of the analysis. The combination,
`expl_service_calls` makes evident that this is an analysis of service
calls.

!!! example
    ```console
    02_01_expl_service_calls.py
    02_02_expl_service_calls.py
    ```

Maybe we need to impose a limit to the length of the file names?

## Python naming conventions

When you write Python code, you have to name a lot of things: variables,
functions, classes, packages, and so on. Choosing sensible names will
save you time and energy later. You’ll be able to figure out, from the
name, what a certain variable, function, or class represents. You’ll
also avoid using inappropriate names that might result in errors that
are difficult to debug.

!!! note
    Never use `l`, `O`, or `I` single letter names as these can be mistaken
    for `1` and `0`, depending on typeface:
    ```python title="Pyhton"
    O = 2  # This may look like you're trying to reassign 2 to zero
    ```

The table below outlines some of the common naming styles in Python code
and when you should use them:

|Type|Naming Convention|Examples|
|---|---|---|
|Function|Use a lowercase word or words. Separate words by underscores to improve readability.|function `my_function`|
|Variable|Use a lowercase single letter word or words. Separate words with underscores to improve readability.|x var `my_variable`|
|Class|Start each word with a capital letter. Do not separate words with underscores. This style is called camel case or pascal case.|Model `MyClass`|
|Method|Use a lowercase word or words. Separate words with underscores toimprove readability.|class_method `method`|
|Constant|Use an uppercase single letter word or words. Separate words with underscores to improve readability.|CONSTANT `MY_CONSTANT` `MY_LONG_CONSTANT`|
|Module|Use a short, lowercase word or words. Separate words with underscores to improve readability.|module.py `my_module.py`|
|Package|Use a short, lowercase word or words. Do not separate words with underscores.|package `mypackage`|

Reference: [Naming
Styles](https://realpython.com/python-pep8/#:~:text=2%20to%20zero-,Naming%20Styles,-The%20table%20below)

<!-- IDEA: Possible implementations -@t93kqi0 at 1/9/2023, 8:46:50 AM -->
<!--
> Another possibility is to use the first later of your name and last
> name. For example, John Smith as `js`. This approach makes more
> difficult to identify the author.
-->

<!--

Reference:

- [3 Tips for Using Correct
  Abbreviations](http://www.whitesmoke.com/3-tips-for-correct-abbreviations)
- [Acronyms Generator](https://www.dcode.fr/acronym-generator)

For a definition of feature, bug and hotfix branches take a look at
[Branching](https://gist.github.com/digitaljhelms/4287848)

### Notes

In order to reuse part of the branch name wth script naming conventions,
Do not use `/` or `-`
-->
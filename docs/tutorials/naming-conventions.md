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

In the intricate world of Data Science and Machine Learning (ML), the
ability to navigate through vast amounts of code, data files, and
documentation efficiently is pivotal to the success and maintainability
of projects. Proper naming conventions are more than a mere aspect of
stylistic preference; they form the backbone of project organization and
play a critical role in ensuring that team members and automated systems
can quickly understand and manage various project components.

This document presents a comprehensive set of guidelines designed to
bring order and clarity to the diverse assets of data science and ML
projects. From the way we name our GitHub repositories to the structure
of our data directories, each convention has been thoughtfully crafted
to align with industry best practices and the unique demands of ML
workflows.

We delve into the specifics of naming branches, which enables
contributors to discern the purpose of each branch at a glance, thereby
streamlining collaboration and review processes. We also cover the
conventions for data files, including the systematic versioning and
timestamping that allow for the efficient tracking of dataset iterations
and history.

Model persistence files, the artifacts of our computational efforts, are
given a structured naming framework that facilitates version control and
model identification across different stages of a project. Furthermore,
we extend these principles to the naming of Jupyter notebooks and
scripts, recognizing their role as both developmental tools and as part
of the project's documentation.

In addition to defining these standards, we are committed to enforcing
them through automated means. This document outlines how GitHub Actions
can be leveraged to ensure adherence to these conventions, providing
examples and setup instructions for integrating these checks into your
continuous integration and deployment pipelines.

By adhering to the naming conventions and enforcement strategies
outlined in this document, teams can achieve a level of operational
harmony that not only optimizes current project workflows but also paves
the way for future scalability and knowledge transfer.

## GitHub Repository Naming Conventions for Data Science Projects

### Overview

Choosing the right naming convention for GitHub repositories in data
science projects is crucial for clarity, organization, and ease of
navigation. A well-defined naming convention helps team members and
stakeholders to quickly understand the scope and purpose of a repository
at a glance. This section outlines the guidelines for naming GitHub
repositories related to data science projects.

### Naming Convention Structure

Repositories should be named following this format:

```text
<prefix>-<descriptive-name>[-<optional-version>]
```

#### Components

- **Prefix**: A concise identifier related to the project's domain or
  main technology.
- **Descriptive Name**: A clear and specific description of the
  repository's content or purpose.
- **Optional Version**: A version number, if applicable, to distinguish
  between different iterations or stages of the project.

### Guidelines

1. **Choose an Appropriate Prefix**
   - The prefix should represent the key area or technology of the
     project, like `ml` for machine learning, `nlp` for natural language
     processing, `cv` for computer vision, etc.
   - This helps in categorizing and quickly identifying the project's
     domain.

2. **Be Clear and Specific**
   - Use descriptive and meaningful terms that accurately reflect the
     primary focus or functionality of the repository.
   - Avoid vague or overly broad terms that do not convey the specific
     purpose of the repository.

3. **Include Versioning Where Necessary**
   - For projects that have multiple versions or stages, include a
     version number at the end of the repository name.
   - This is useful for tracking development progress and
     differentiating between major project phases.

4. **Maintain Consistency**
   - Keep all repository names in lowercase and use hyphens (`-`) to
     separate words. This enhances readability and avoids issues with
     URL encoding.

### Examples

- `ml-predictive-modeling`
- `nlp-chatbot-interface`
- `cv-facial-recognition-v1`
- `ds-data-cleaning-tools`

### Conclusion

Adopting these naming conventions for GitHub repositories in data
science projects promotes a structured and systematic approach to
repository management. It ensures that the repository names are
informative, organized, and aligned with the project's objectives and
technical domain.

## Git Branch Naming Standards for ML Projects

### Overview

For machine learning projects, the clarity of the Git repository is
non-negotiable. A consistent approach to branch naming is fundamental to
this clarity. It enables rapid identification of the branch's purpose,
streamlining collaboration and making navigation within the repository
more intuitive.

### Naming Convention Structure

Branch names must be constructed as follows:

```text
<category>/<description>-<issue_number_or_jira_key>
```

#### Components

- **Category**: A concise keyword that delineates the branch based on
  the nature of the work being conducted.
- **Description**: A succinct, yet informative descriptor of the
  specific task, feature, or focus of the branch.
- **Issue Number or Jira Key**: This is a mandatory inclusion that
  connects the branch to a corresponding task or issue in your project
  management tool, be it GitHub or Jira.

#### Categories

Categories provide immediate context regarding the branch's domain of
work. Standard categories include:

| Category      | Description                                                   |
|---------------|---------------------------------------------------------------|
| `feature`     | New feature development or enhancements                       |
| `bugfix`      | Targeted branches for bug resolution                          |
| `data`        | Data management activities, like acquisition or processing    |
| `experiment`  | Exploratory or experimental development                       |
| `model`       | Model creation, testing, or deployment                        |
| `docs`        | Documentation creation or updates                             |
| `refactor`    | Code restructuring to improve performance without altering functionality |
| `test`        | Test development or modification                              |
| `chore`       | Routine tasks or minor updates                                |

### Examples

Below are examples of branch names that adhere to our standards:

- `feature/user-authentication-DATA123`
- `data/dataset-enhancement-GH15`
- `model/performance-improvement-DATA22`
- `bugfix/data-loading-error-GH45`
- `docs/api-documentation-update`
- `refactor/code-optimization-DATA78`
- `test/new-model-tests-GH27`

### Guidelines

- Maintain lowercase lettering in all branch names for uniformity.
- Use hyphens to separate words within the branch name, ensuring
  readability.
- Keep branch names brief, yet descriptive enough to clearly articulate
  their intent at a glance.
- Including the issue number or Jira key in the branch name is not
  optional; it is a required practice for traceability and coherence.

### Conclusion

Adhering to these branch naming conventions is imperative for the
organization and accessibility of our ML project repositories. It
supports our team in promptly discerning the intent of each branch,
enhancing effective collaboration and project oversight.

## Git Commit Message Standards for ML Projects

### Introduction

Clear and informative commit messages are a cornerstone of effective
team collaboration in machine learning projects. To enhance this aspect
of our workflow, we incorporate tools that facilitate the creation of
standardized commit messages and link them to their respective task
management entries. This section details the standards and tools to
assist with writing commit messages that include GitHub issue numbers or
Jira keys.

### Commit Message Structure

Commit messages should adhere to the following format:

```text
<type>(<scope>): <subject> [#issue_number | #jira_key]

<body>

<footer>
```

#### Components

- **Type**: The category of change you're committing.
- **Scope**: The particular area of the codebase affected by the
  changes.
- **Subject**: A brief description of the changes, including the issue
  tracker reference.
- **Body**: An in-depth explanation of the changes and the reasoning
  behind them.
- **Footer**: Any additional notes or references.

### Commit Types

Consistency in the types of changes committed is key for readability and
organization. Here's a table of types to use in commit messages, similar
to those used for branch naming:

| Type         | Description                                                       |
|--------------|-------------------------------------------------------------------|
| `feat`       | Introducing new features or enhancements                          |
| `fix`        | Bug fixes                                                         |
| `data`       | Modifications in data processing or management                    |
| `experiment` | Changes to experimental or exploratory code                       |
| `model`      | Changes related to model development, testing, or deployment      |
| `docs`       | Documentation additions or updates                                |
| `refactor`   | Code changes that enhance performance without altering functionality |
| `test`       | Test writing or fixing                                            |
| `chore`      | Routine tasks or updates not impacting the production code        |


### Best Practices

1.  **Make it Concise**: The subject line should be succinct yet
    descriptive. It’s the first line of communication and often what
    people will see in their notifications or logs.
2.  **Use the Imperative Mood**: Write your commit message as if you are
    giving an order or instruction. For example, “fix” instead of
    “fixed” or “fixes”.
3.  **Capitalize the Subject Line**: Start the subject line with a
    capital letter.
4.  **Do Not End the Subject Line with a Period**: The subject line is a
    title or headline; it doesn’t need a period at the end.
5.  **Separate Subject from Body with a Blank Line**: This helps various
    tools (e.g., log, shortlog) to correctly identify the subject from
    the rest of the content.
6.  **Use the Body to Explain the "What" and "Why"**: Not just the
    "how". The code itself explains “how” a change has been made; the
    commit message should explain what and why.
7.  **Reference Issues and Pull Requests Liberally**: When applicable,
    include links to the related issues and pull requests, which
    provides additional context.

### VS Code Extensions for Commit Messages

To support our commit message standards, we recommend using the
following Visual Studio Code extensions:

- **Gitmoji for VS Code**: An extension that allows you to include emoji
  in your commit messages, which can help to quickly identify the
  purpose or nature of a change. It's available on the VS Code
  Marketplace:
  [Gitmoji](https://marketplace.visualstudio.com/items?itemName=seatonjiang.gitmoji-vscode).

- **[Commit Message
  Editor](https://marketplace.visualstudio.com/items?itemName=adam-bender.commit-message-editor)**:
  This extension helps to enforce the structure of a commit message,
  ensuring that each part of our commit message standard is followed. It
  offers prompts and snippets to guide you in creating a well-formatted
  message.

### Reference for Best Practices

For an in-depth understanding of best practices for git commit messages,
refer to the following article: [Git Commit Message Best
Practices](https://www.gitkraken.com/learn/git/best-practices/git-commit-message).
This article provides a comprehensive guide and rationale behind the
composition of effective commit messages.

### Conclusion

By utilizing the outlined commit message structure, type guidelines, and
recommended VS Code extensions, our team can ensure a uniform and
informative history in our repository. Commit messages become more than
a formality; they transform into a rich log that conveys the what, why,
and how of our development process, enhancing clarity and streamlining
collaboration.

## Naming Conventions for Data Folders in ML Projects

### Overview

In Machine Learning (ML) projects, organizing and managing data
efficiently is crucial. Adopting a clear and consistent naming
convention for data folders not only facilitates better data management
but also enhances collaboration and project understanding. Below are
guidelines for naming data folders in ML projects.

### Folder Structure and Naming Convention

The data folder structure should be organized into distinct categories,
each serving a specific purpose in the data processing pipeline. Here’s
the recommended structure:

```text
data
├── raw                   # Original, immutable data dump
├── external              # Data from third-party sources
├── interim               # Intermediate data, partially processed
├── processed             # Fully processed data, ready for analysis
└── features              # Engineered features ready for model training
```

#### Guidelines for Naming

1. **Descriptive and Clear:**
   - Folder names should be self-explanatory, indicating clearly what
     type of data they contain.

2. **Consistent Format:**
   - Use a consistent naming format across all folders. The recommended
     format is all lowercase with words separated by hyphens for
     readability.

3. **Standard Categories:**
   - Stick to standard naming categories (`raw`, `external`, `interim`,
     `processed`, `features`) as they are widely recognized in data
     science and ML communities.

4. **Avoid Overly Specific Names:**
   - While being descriptive, avoid overly specific names which might
     become irrelevant as the project evolves. The name should be broad
     enough to encompass various data types that might fall into that
     category.

### Explanation of Categories

- **Raw**: 
   - Contains the original datasets. Data in this folder is immutable
     and serves as a backup for all processing steps.

- **External**: 
   - For data sourced from outside the original dataset. This includes
     third-party data, external APIs, or any supplementary data.

- **Interim**: 
   - Holds data that is in the process of being cleaned or transformed.
     Useful for datasets that are not final but are needed in
     intermediate stages.

- **Processed**: 
   - Contains the final version of the dataset, which is ready for
     analysis or modeling. Data in this folder is cleaned, formatted,
     and pre-processed.

- **Features**: 
   - Dedicated to storing feature sets that are used in machine learning
     models. This includes transformed data, new features, and selected
     features.

### Conclusion

Adhering to this naming convention for data folders will ensure a
well-organized and manageable data structure in your ML projects. It
facilitates easy access, understanding, and efficient data handling,
crucial for the success of any ML project.

## Data Files Naming Conventions in ML Projects

### Overview
Proper naming conventions for data files are essential in Machine
Learning (ML) projects to ensure easy identification, management, and
tracking of datasets. This guide provides a structured approach to
naming data files, particularly when handling multiple versions,
subsets, or types of data.

### Naming Convention Structure

Data file names should follow this format:
```
<dataset_name>_<version>_<creation_date>_<description>.<extension>
```

#### Components

- **Dataset Name**: A concise identifier for the dataset.
- **Version**: Version number or identifier of the dataset.
- **Creation Date**: Date when the dataset was created or last modified,
  in the format `YYYYMMDD`.
- **Description**: A brief, clear description of the dataset or its
  specific subset.
- **Extension**: The appropriate file extension (e.g., `.csv`, `.xlsx`,
  `.json`).

### Guidelines

1. **Clarity and Descriptiveness:**
   - Ensure the name is descriptive enough to give an immediate
     understanding of the dataset’s content and scope.

2. **Consistency:**
   - Maintain consistency in the naming convention across all data
     files. This includes consistent use of underscores, date formats,
     and versioning systems.

3. **Versioning:**
   - Use a logical versioning system, like semantic versioning (e.g.,
     `v1.0`, `v1.1`, `v2.0`) or sequential numbering (`01`, `02`, etc.).

4. **Date Format:**
   - Stick to a standard date format (`YYYYMMDD`). This avoids ambiguity
     and makes it easy to sort files chronologically.

5. **Concise Descriptions:**
   - Keep the description part brief yet informative. Avoid overly long
     names but provide enough context to distinguish the dataset.

6. **File Extensions:**
   - Use appropriate file extensions to indicate the file type, which
     helps in quickly identifying the software or tools needed to open
     them.

### Examples

- `customer_data_v1.0_20240101_initial.csv`
- `sales_report_v2.2_20240305_updated.xlsx`
- `image_dataset_v1.0_20240220_raw.json`

### Conclusion

Adhering to these naming conventions for data files in ML projects will
significantly enhance data manageability. It ensures ease of access,
effective version control, and clear understanding, facilitating
efficient data analysis and collaboration within the team.

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

## Notebook and Script Naming Conventions in ML Projects

### Overview
Properly naming Jupyter notebooks and scripts is essential for quick
identification, efficient management, and collaborative ease in machine
learning projects. A systematic naming convention helps in understanding
the file's purpose at a glance and tracking its evolution over time.

### Naming Convention Structure

Names for notebooks and scripts should follow this format:
```
<type>_<topic>_<version>_<YYYYMMDD>.<extension>
```

#### Components:
- **Type**: A short identifier indicating the nature of the work (e.g.,
  `eda` for exploratory data analysis, `preprocess` for data
  preprocessing, `model` for model training).
- **Topic**: A concise descriptor of the notebook's or script's main
  focus.
- **Version**: An optional version number or identifier, especially
  useful if the notebook or script undergoes significant iterative
  updates.
- **Date**: The creation or last modified date in `YYYYMMDD` format.
- **Extension**: The file extension, like `.ipynb` for Jupyter
  notebooks, `.py` for Python scripts.

### Guidelines:

1. **Descriptive and Purposeful:**
   - Start with a type that categorizes the file based on its primary
     purpose in the ML workflow.
   - The topic should be sufficiently descriptive to convey the specific
     focus or task of the notebook/script.

2. **Versioning:**
   - Include a version number if the file is part of an iterative
     process, such as `v1`, `v2`, or more detailed semantic versioning
     like `1.0`, `1.1`.

3. **Date Stamp:**
   - Adding the date (in `YYYYMMDD` format) helps in identifying the
     most recent version or understanding the timeline of development.

4. **Consistency:**
   - Maintain a consistent naming convention across all notebooks and
     scripts for ease of organization and retrieval.

5. **Clarity and Brevity:**
   - Ensure the name is clear yet concise. Avoid overly long names but
     provide enough information to understand the file's content and
     purpose.

### Examples:

- `eda_customer_segmentation_v1_20240101.ipynb`
- `preprocess_data_cleaning_v2_20240215.py`
- `model_train_regression_20240310.ipynb`

### Conclusion

This naming convention for Jupyter notebooks and scripts will foster a
more organized and manageable ML project environment. It aids in quickly
locating specific files, understanding their purpose, and tracking their
evolution over time.

## Enforcing Naming Conventions Using GitHub Actions

### Overview

In machine learning projects, maintaining consistent naming conventions
across various assets like Jupyter notebooks, scripts, model files, data
files, and Git branches is essential for organization and clarity. To
enforce these conventions, we can utilize GitHub Actions, an automation
tool that integrates seamlessly with GitHub repositories.

### GitHub Actions for Naming Convention Checks

GitHub Actions can be configured to automatically run checks on the
names of files and branches whenever a new commit is pushed or a pull
request is made. This process helps ensure that all team members adhere
to the established naming conventions.

### Setup and Configuration

1. **Creating the Workflow File:**
   - A YAML file is created in the `.github/workflows/` directory of the
     repository, named `check_naming_convention.yml`.
   - This file defines the GitHub Action workflow, specifying when the
     checks should run (e.g., on push and pull requests) and what script
     to execute.

2. **Writing the Validation Script:**
   - A Python script, `validate_naming.py`, is placed in the
     `.github/scripts/` directory.
   - This script contains functions to validate the naming conventions
     of Jupyter notebooks, Python scripts, model persistence files, data
     files, and Git branches.
   - The script uses regular expressions to match filenames and branch
     names against the specified patterns.

3. **Workflow Execution:**
   - The workflow runs the Python script whenever code is pushed to the
     repository or a pull request is made.
   - The script checks each file and branch name involved in the
     push/pull request against the defined naming conventions.
   - If a naming convention violation is detected, the script exits with
     a non-zero status, causing the GitHub Action to fail. This failure
     is visible in the pull request or push, alerting the contributor to
     the naming issue.

### Example Workflow File

```yaml
name: Check Naming Convention

on: [push, pull_request]

jobs:
  naming-convention-check:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - name: Validate Naming Convention
      run: python .github/scripts/validate_naming.py
      env:
        GITHUB_REF: ${{ github.ref }}
```

### Example Python Script Structure

```python
"""
This module `validate_naming.py` is part of a GitHub Actions workflow
designed to enforce naming conventions across various assets in a
machine learning project. It includes functions to validate the naming
of Jupyter notebooks, Python scripts, model persistence files, data
files, and Git branches.

The module contains the following key functions: -
`validate_ml_file_naming`: Checks naming conventions for Jupyter
notebooks and Python scripts.  - `validate_model_file_naming`: Ensures
model file names adhere to the specified naming standards.  -
`validate_data_file_naming`: Validates data file names against the
project's naming conventions.  - `validate_git_branch_naming`: Checks if
the Git branch names follow the predefined naming patterns.

The script is executed as part of a GitHub Actions workflow and is
essential for maintaining consistency, readability, and organization of
files in the repository.

Note: - This script is meant to be run as a GitHub Action and relies on
environmental variables provided by GitHub workflows.  - Regular
expressions are used for pattern matching to validate the naming
conventions.
"""

import os
import re
import sys


def validate_ml_file_naming(filename):
    """
    Check if the filename adheres to the ML project's naming convention.

    Parameters
    ----------
    filename : str
        The name of the file to be checked.

    Returns
    -------
    bool
        True if the filename matches the naming convention, False
        otherwise.

    Notes
    -----
    The naming convention expected:
    '<type>_<topic>_<version>_<YYYYMMDD>.<extension>' Where: - <type> is
    a flexible, user-defined category (e.g., 'eda', 'preprocess').  -
    <topic> is a concise descriptor of the main focus.  - <version> is
    an optional version identifier.  - <YYYYMMDD> is the creation or
    last modified date.  - <extension> is either '.ipynb' for Jupyter
    notebooks or '.py' for Python scripts.
    """
    # Regex pattern with a more flexible 'type' component
    pattern = re.compile(r"^\w+_\w+(_v\d+)?_\d{8}\.[ipynb|py]$")
    return pattern.match(filename)


def validate_model_file_naming(filename):
    """
    Check if the filename adheres to the model persistence file naming
    convention.

    Parameters
    ----------
    filename : str
        The name of the model file to be checked.

    Returns
    -------
    bool
        True if the filename matches the naming convention, False
        otherwise.

    Notes
    -----
    The naming convention for model persistence files is:
    '<project_name>_<model_version>_<model_type>_<timestamp>.pkl' This
    includes: - `project_name`: Name of the project.  - `model_version`:
    Version of the model, following semantic versioning.  -
    `model_type`: Type or name of the model.  - `timestamp`: Date when
    the model was saved (YYYYMMDD format).
    """
    pattern = re.compile(r"^\w+_(v\d+\.\d+\.\d+)_\w+_\d{8}\.pkl$")
    return pattern.match(filename)


def validate_data_file_naming(filename):
    """
    Check if the filename adheres to the data file naming convention.

    Parameters
    ----------
    filename : str
        The name of the data file to be checked.

    Returns
    -------
    bool
        True if the filename matches the naming convention, False
        otherwise.

    Notes
    -----
    The naming convention for data files is:
    '<dataset_name>_<version>_<creation_date>_<description>.<extension>'
    This includes: - `dataset_name`: Identifier for the dataset.  -
    `version`: Version of the dataset, following semantic versioning or
    numbering.  - `creation_date`: Date of creation or last modification
    (YYYYMMDD format).  - `description`: Brief description of the
    dataset or subset.  - `extension`: File extension indicating the
    file type (e.g., 'csv', 'xlsx', 'json').
    """
    pattern = re.compile(r"^\w+_(v\d+\.\d+\.\d+|\d+)_\d{8}_\w+\.\w+$")
    return pattern.match(filename)


def validate_git_branch_naming():
    """
    Check if the Git branch name adheres to the naming convention.
    """
    branch_ref = os.getenv("GITHUB_REF")
    if not branch_ref:
        print("No branch reference found.")
        return True  # Might not be a branch push, so don't fail the check.

    # Extract the branch name from refs/heads/your-branch-name
    branch_name = branch_ref.split("/")[-1]
    pattern = re.compile(
        r"^(feature|bugfix|data|experiment|model|docs|refactor|test|chore)/[\w-]+(_\d+)?$"
    )
    return pattern.match(branch_name)


def main():
    """
    The main function to validate naming conventions in a machine
    learning project.

    This function executes a series of naming convention checks on
    various file types, including model files, Jupyter notebooks, Python
    scripts, and data files. It also validates Git branch names. If any
    file or branch name does not adhere to the predefined naming
    conventions, the function flags an error.

    The checks are performed as follows: - For Git branch names, using
    the `validate_git_branch_naming` function.  - For model files
    (*.pkl), using the `validate_model_file_naming` function.  - For
    Jupyter notebooks and Python scripts (*.ipynb, *.py), using the
      `validate_ml_file_naming` function.
    - For data files (*.csv, *.xlsx, *.json), using the
      `validate_data_file_naming` function.

    If any naming convention violations are found, the script exits with
    a status code of 1, indicating an error. This is used in the context
    of GitHub Actions workflows to flag naming convention violations in
    pull requests or pushes.
    """
    error = False
    if not validate_git_branch_naming():
        print(f"Invalid Git branch naming convention.")
        error = True

    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".pkl") and not validate_model_file_naming(file):
                print(f"Invalid model file naming convention: {file}")
                error = True
            elif file.endswith((".ipynb", ".py")) and not \
                validate_ml_file_naming(file):
                print(f"Invalid notebook/script naming convention: {file}")
                error = True
            elif file.endswith((".csv", ".xlsx", ".json")) and \
                 not validate_data_file_naming(file):
                print(f"Invalid data file naming convention: {file}")
                error = True


    if error:
        sys.exit(1)


if __name__ == "__main__":
    main()
```

### Conclusion

Implementing this GitHub Actions workflow ensures that all team members
adhere to the agreed-upon naming conventions, thereby maintaining
consistency and organization across the project's assets. This automated
check acts as a first line of defense, preventing naming irregularities
from being merged into the main codebase.


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
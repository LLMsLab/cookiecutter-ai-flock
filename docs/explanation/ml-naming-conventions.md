# Notebook and Script Naming Conventions in ML Projects

## Overview
Properly naming Jupyter notebooks and scripts is essential for quick identification, efficient management, and collaborative ease in machine learning projects. A systematic naming convention helps in understanding the file's purpose at a glance and tracking its evolution over time.

!!! note "Importance of Naming"
    A well-defined naming convention is crucial for organizing and managing files in any ML project.

### Naming Convention Structure

Use the following format for naming notebooks and scripts:

```markdown
<type>_<topic>_<version>_<YYYYMMDD>.<extension>
```

### Components:

- **Type**: A short identifier indicating the nature of the work (e.g., `eda` for exploratory data analysis, `preprocess` for data preprocessing, `model` for model training).
- **Topic**: A concise descriptor of the notebook's or script's main focus.
- **Version**: An optional version number or identifier, especially useful if the notebook or script undergoes significant iterative updates.
- **Date**: The creation or last modified date in `YYYYMMDD` format.
- **Extension**: The file extension, like `.ipynb` for Jupyter notebooks, `.py` for Python scripts.

!!! tip "Components Breakdown"
    Understanding each component of the naming convention helps in creating more informative and easily recognizable file names.

## Guidelines:

1. **Descriptive and Purposeful:**
   - Start with a type that categorizes the file based on its primary purpose in the ML workflow.
   - The topic should be sufficiently descriptive to convey the specific focus or task of the notebook/script.

2. **Versioning:**
   - Include a version number if the file is part of an iterative process, such as `v1`, `v2`, or more detailed semantic versioning like `1.0`, `1.1`.

3. **Date Stamp:**
   - Adding the date (in `YYYYMMDD` format) helps in identifying the most recent version or understanding the timeline of development.

4. **Consistency:**
   - Maintain a consistent naming convention across all notebooks and scripts for ease of organization and retrieval.

5. **Clarity and Brevity:**
   - Ensure the name is clear yet concise. Avoid overly long names but provide enough information to understand the file's content and purpose.

### Examples:

- `eda_customer_segmentation_v1_20240101.ipynb`
- `preprocess_data_cleaning_v2_20240215.py`
- `model_train_regression_20240310.ipynb`

!!! example "Naming Examples"
    These examples illustrate how the naming convention is applied in practice.

## Conclusion

This naming convention for Jupyter notebooks and scripts will foster a more organized and manageable ML project environment. It aids in quickly locating specific files, understanding their purpose, and tracking their evolution over time.
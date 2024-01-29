# Model Persistence Naming Convention

!!! info "Model Persistence File Naming Conventions"
    Adopting a consistent naming convention for persisting machine learning models in binary format is essential for easy identification and management across various projects. This guide outlines the recommended format for naming these files.

### Recommended Format
- Format: ```<project_name>_<model_version>_<model_type>_<timestamp>.pkl```
- The format includes the project name, model version, model type, and a timestamp.

### Field Definitions
| Field           | Definition                                           |
|-----------------|------------------------------------------------------|
| `project_name`  | The name of the project the model is associated with |
| `model_version` | The version of the model, following semantic versioning (MAJOR.MINOR.PATCH) |
| `model_type`    | Type or name of the model (e.g., linearReg, neuralNet) |
| `timestamp`     | Date when the model was persisted (YYYYMMDD format)  |

### Naming Examples
- `service_sage_v1.2.0_linearReg_20240123.pkl`
  - Linear regression model from the Service Sage project, version 1.2.0, updated on January 23, 2024.
- `one_assist_v3.0.1_neuralNet_20240215.pkl`
  - Neural network model for One Assist, version 3.0.1, updated on February 15, 2024.

### Versioning Scheme
- **MAJOR**: Incremented for incompatible API changes.
- **MINOR**: Incremented for adding functionality in a backward-compatible manner.
- **PATCH**: Incremented for backward-compatible bug fixes.

### Metadata Storage
- Store a JSON file containing model metadata alongside each model file (e.g., `service_sage_v1.2.0_linearReg_20240123_metadata.json`).

### Documentation and Registry
- Maintain a Makefile to automate the documentation or registry generation process.

### Automating Metadata Creation
- Example Python script provided for creating a linear regression model with metadata using Scikit-Learn and saving it as a `.pkl` file and corresponding metadata as a `.json` file.

### Markdown Documentation for Models
- Example Markdown documentation (`service_sage_v1.2.0_linearReg_20240123_documentation.md`) provided, explaining the training process, model parameters, performance metrics, and metadata structure.

### Directory Structure
- Store related files in the same directory, using subdirectories for better organization in projects with multiple models.
```
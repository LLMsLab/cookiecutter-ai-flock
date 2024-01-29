# Tutorial: Managing Local Data Updates with DVC

## Introduction

!!! note "About this Tutorial"
    In this tutorial, you'll learn the practical steps to manage and track changes to datasets locally using Data Version Control (DVC). We'll cover a real-world scenario of updating a dataset and tracking these changes with DVC.

### Prerequisites

- :octicons-checklist-16: Basic understanding of version control with Git.
- :octicons-package-24: DVC installed and initialized in your project.

## Scenario: Updating Your Dataset

Imagine you've made updates to a dataset file named `dataset.csv` that's
already being tracked by DVC. Your task now is to manage these updates
efficiently.

### Step-by-Step Guide to Manage Local Data Updates

#### 1. Detecting Changes with DVC

!!! tip "How DVC Detects Changes"
    - **Checksum Mechanism**: DVC uses checksums (hash values) to track file versions. A change in the file leads to a change in its checksum, signaling an update.

#### 2. Updating the Data Version

##### Tracking the Updated File

1. **Run the DVC Add Command**:
   ```bash
   dvc add dataset.csv
   ```
   This command updates the `.dvc` file with the new checksum for `dataset.csv`.

2. **Commit the Changes in Git**:
   ```bash
   git add dataset.csv.dvc
   git commit -m "Update dataset.csv with new data"
   ```

3. **Push the Updated Data**:
   ```bash
   dvc push
   ```
   This step uploads the new version to your remote DVC storage.

### Understanding the Purpose of This Process

!!! success "Key Benefits"
    - **Reproducibility**: Ensures stages of your project can be reproduced with the exact data versions.
    - **Collaboration**: Maintains consistency in data across team environments.
    - **Traceability**: Allows tracking of data changes throughout the project's history.

## Conclusion

!!! check-circle "Wrapping Up"
    You've learned how DVC's integration with Git facilitates effective data versioning, ensuring consistent dataset management and traceable changes across your team. While focused on local data updates, remember that cloud-based updates might follow a slightly different process.
# Tutorial: Managing Cloud Data Updates with DVC

## Introduction

!!! note "Learning Objectives"
    Learn to manage and sync data updates in the cloud using Data Version Control (DVC). This tutorial is ideal for scenarios involving direct data updates in cloud storage services like AWS S3 or Azure Blob Storage.

### Prerequisites

- :octicons-checklist-16: Familiarity with DVC and cloud storage.
- :octicons-package-24: DVC setup for your cloud storage service.

## Scenario: Updates in Cloud Storage

Consider a situation where your dataset in a cloud storage service is
updated directly in the cloud, without involving your local machine.

### The Challenge of Cloud Data Updates

1. **Local vs. Cloud State**:
   - DVC's limitation in automatically detecting cloud changes.
   - The need for manual synchronization between local and cloud states.

### Step-by-Step Guide to Syncing Cloud Data

#### 1. Synchronizing Local and Cloud States

!!! tip "Syncing with DVC Pull"
    Run `dvc pull` to fetch and update your local workspace with the latest file versions from the cloud storage.

    ```bash
    dvc pull
    ```

    DVC will compare and download any updated files based on checksum differences.

#### 2. Local Tracking of Cloud Updates

1. **Pull Updated Data**:
   - Ensure your local workspace reflects the latest cloud version.

2. **Track and Commit Changes Locally**:
   - Version the cloud updates using DVC and Git.

    ```bash
    dvc add dataset.csv
    git add dataset.csv.dvc
    git commit -m "Update dataset.csv with cloud changes"
    ```

3. **Push Local Changes to Remote Storage**:
   - Sync any additional local changes or `.dvc` files to the cloud.

    ```bash
    dvc push
    ```

### Understanding the Process

!!! check-circle "Purpose of Cloud Data Syncing"
    - **Consistency and Reproducibility**: Tracks and versions changes even in cloud storage.
    - **Collaborative Work**: Ensures all team members have the latest data version.
    - **Version Control Integration**: Combines DVC with cloud storage for effective data management.

### Comparing with Local Data Handling

!!! warning "Key Differences from Local Data"
    - **Manual Synchronization**: Active steps are required to align cloud and local data states.
    - **Local Tracking of Cloud Changes**: Crucial for comprehensive version control and historical tracking.

## Conclusion

!!! success "Key Takeaways"
    Cloud data updates with DVC introduce a necessary step of manual synchronization. This tutorial equips you with the knowledge to ensure your data management practices are consistent, transparent, and collaborative, irrespective of where the data is stored or updated.
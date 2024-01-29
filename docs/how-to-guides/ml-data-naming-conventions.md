# Data Files Naming Conventions in ML Projects

## Overview
Proper naming conventions for data files are essential in Machine Learning (ML) projects to ensure easy identification, management, and tracking of datasets. This guide provides a structured approach to naming data files, particularly when handling multiple versions, subsets, or types of data.

!!! note "Naming Convention Structure"
    Data file names should follow this format:
    ```
    <dataset_name>_<version>_<creation_date>_<description>.<extension>
    ```
    Components

    - **Dataset Name**: A concise identifier for the dataset.
    - **Version**: Version number or identifier of the dataset.
    - **Creation Date**: Date when the dataset was created or last modified, in the format `YYYYMMDD`.
    - **Description**: A brief, clear description of the dataset or its specific subset.
    - **Extension**: The appropriate file extension (e.g., `.csv`, `.xlsx`, `.json`).

!!! tip "Guidelines"
    1. **Clarity and Descriptiveness**: Ensure the name is descriptive enough to give an immediate understanding of the dataset’s content and scope.
    2. **Consistency**: Maintain consistency in the naming convention across all data files. This includes consistent use of underscores, date formats, and versioning systems.
    3. **Versioning**: Use a logical versioning system, like semantic versioning (e.g., `v1.0`, `v1.1`, `v2.0`) or sequential numbering (`01`, `02`, etc.).
    4. **Date Format**: Stick to a standard date format (`YYYYMMDD`). This avoids ambiguity and makes it easy to sort files chronologically.
    5. **Concise Descriptions**: Keep the description part brief yet informative. Avoid overly long names but provide enough context to distinguish the dataset.
    6. **File Extensions**: Use appropriate file extensions to indicate the file type, which helps in quickly identifying the software or tools needed to open them.

!!! example "Examples"
    ```markdown
    - `customer_data_v1.0_20240101_initial.csv`
    - `sales_report_v2.2_20240305_updated.xlsx`
    - `image_dataset_v1.0_20240220_raw.json`
    ```

## Conclusion

Adhering to these naming conventions for data files in ML projects will significantly enhance data manageability. It ensures ease of access, effective version control, and clear understanding, facilitating efficient data analysis and collaboration within the team.
# How to organize project's data

!!! warning

    It is not a best practice to save sensitive or large project data on
    GitHub. GitHub is designed for source code management and version
    control, and while it does allow for limited file storage, it's not
    designed for storing large binary files or sensitive information.

## Data files

!!! tip "Best Practice"

    Store project's data on the remote Data Hub Linux server.

Creating separate folders for raw, external, interim, and processed data
is the best practice for organizing and managing data in a project.
This approach helps to maintain a clear and organized structure for the
data, and can also help to ensure that the different stages of data
processing are clearly defined and documented.

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

Having a clear and organized structure for the data can help to ensure
that it is properly managed throughout the project and that any
necessary modifications or transformations can be easily traced and
recorded. Additionally, it can also make it easier for other team
members or stakeholders to understand and access the data as needed.

## Centralized data folders: whether to use them or not

The answer to this question depends on the specific requirements of the
project and the organization's data management policies.

In some cases, it may be appropriate for data scientists to keep a copy
of the project's data on their local machines for ease of access and
local processing. This can be especially useful when working with large
data sets that may not be feasible to store and transfer over the
network.

However, in most cases, it is a best practice to use a centralized
shared data folder that is stored on a networked storage system or a
cloud-based data storage service. This allows all team members to access
the data, and ensures that the data is stored in a secure and organized
manner. Additionally, using a centralized data folder can help to avoid
duplication and ensure that everyone is working with the same version of
the data.

Regardless of the approach used, it's important to establish clear
guidelines and protocols for data management and access, and to ensure
that data security and privacy concerns are properly addressed. This may
involve implementing access controls, encryption, and backup and
recovery measures.

### Using VS Code on a project with a centralized shared data folder

Step 4 of the [Getting Started](getting-started.md) guide involves
creating a shared data directory for the project. To make the data
accessible and visible in VS Code, symbolic links need to be created.

!!! info "What is a symbolic link?"
    The purpose of a symbolic link (symlink) in Linux is to create a
    shortcut or alias to a file or directory. A symlink acts as a reference
    to the original file, allowing multiple paths to access the same data.
    This can be useful for creating shortcuts to frequently used files,
    linking to files in different directories, and creating backups of
    important files.

Here's a shell script that creates symbolic links for the specified
folders:

```Bash title="symlink_data_folders.sh"
folders=(raw external interim processed model_output)

for folder in "${folders[@]}"; do
  ln -s /path/to/original/"$folder" /path/to/link/"$folder"
done
```

Where the path to the original folder corresponds to the project's
shared data folder:

```text
/nyl/data/tenants/insurance/cdsamktg/mediamix/data
```

And the link folder corresponds to the location of the project's data
folder on the cloned Git repository on server user space:

```text
/nyl/data/home/t93kqi0/projects/Media-Mix/data/"$folder"
```

```Bash title="symlink_data_folders.sh"
folders=(raw external interim processed model_output)

for folder in "${folders[@]}"; do
  ln -s /nyl/data/tenants/insurance/cdsamktg/mediamix/data/"$folder" \
  /nyl/data/home/t93kqi0/projects/Media-Mix/data/"$folder"
done
```

!!! warning
    The link `data` folder must be empty before running the
    `symlink_data_folders.sh` script.

Now all shared data in each sub-directory of the `data` shared folder
must be visible from the VS Code Explorer pane.

<!--
TODO: Tasks pending completion -@t93kqi0 at 12/28/2022, 4:45:20 PM
Review this document for a non-shared folder approach
- [Ref to NYL document](https://newyorklife.sharepoint.com/:p:/s/CDSAiInternal-Projects/EfmrK_CtXKtNlOysRX7wUYEBnaTXP4mAccBIwMW892HtMg?e=0vQ61H)

## Reference

- [Creating a symlink from one folder to another with different names?](https://askubuntu.com/questions/600714/creating-a-symlink-from-one-folder-to-another-with-different-names)
-->

## Metadata and Documentation 

Discussing the importance of Metadata and Documentation in the context
of your data science project is crucial. Here's a detailed breakdown:

### Importance of Metadata and Documentation

1. **Contextual Understanding**: Metadata provides context to the data.
   It includes details like the source of the data, when and how it was
   collected, its format, and any changes it has undergone. This
   information is essential for anyone trying to understand or use the
   data effectively.

2. **Reproducibility and Traceability**: Proper documentation ensures
   that data processing steps can be replicated and understood by
   others. This is particularly important in data science, where
   reproducibility is a key aspect of project credibility and
   validation.

3. **Data Quality Insights**: Metadata can include information about
   data quality, such as accuracy, completeness, and consistency. This
   is valuable for assessing the reliability of the data and
   understanding its limitations.

4. **Compliance and Auditing**: In many industries, there are regulatory
   requirements for data management. Detailed metadata and documentation
   help in complying with these regulations and make audits more
   manageable.

### Recommendations for Effective Metadata and Documentation

1. **Standardized Format**: Adopt a standardized format or template for
   metadata and documentation. This could be a structured file like JSON
   or XML for metadata, and markdown or structured text files for
   documentation.

2. **Automated Generation**: Where possible, automate the generation of
   metadata. For instance, when data is imported or processed, scripts
   can automatically capture and record key information.

3. **Versioning of Data and Metadata**: Just like the data, its metadata
   should also be version-controlled. This is important as the data
   evolves over time due to various processing steps.

4. **Inclusion of Key Elements**: Ensure that metadata includes
   essential elements like data source, date of acquisition, data
   format, any preprocessing steps applied, data schema (if applicable),
   and information on confidentiality or sensitivity.

5. **Accessibility**: Store metadata and documentation in an easily
   accessible location. It should be clearly linked to the corresponding
   data.

6. **Training and Guidelines**: Provide team members with training or
   guidelines on how to create and maintain proper documentation and
   metadata. This ensures consistency and compliance with established
   standards.

7. **Regular Updates**: Just as data changes, so should its
   documentation. It's important to update documentation whenever the
   data or its handling procedures change.

8. **Use of Tools**: Leverage tools that support metadata management and
   documentation. For instance, data cataloging tools can be very
   helpful in larger organizations for maintaining a central repository
   of metadata.

9. **Collaboration and Reviews**: Encourage regular reviews of metadata
   and documentation by different team members. This not only improves
   the quality but also ensures that the data remains understandable and
   usable by everyone.

10. **Integration with Data Pipeline**: Integrate metadata generation
    and documentation updates into your data processing pipelines. This
    ensures that changes in data are automatically reflected in the
    metadata and documentation.

In summary, comprehensive and up-to-date metadata and documentation are
fundamental to the effective management, use, and understanding of data
in any data science project. They facilitate better collaboration,
ensure compliance with standards and regulations, and significantly
contribute to the overall integrity and usability of the data.

## Example of Metadata Creation

Using a JSON file to store metadata for a CSV file is an efficient way
to keep track of important information about your data. Below is an
example of how this can be done, along with a method to automate the
process.

### Example: JSON Metadata for a CSV File

Suppose you have a CSV file named `sales_data.csv`. The metadata for
this file could include information such as the source of the data, the
date of creation, the number of rows and columns, column names, and any
preprocessing steps applied.

Here's an example of what the JSON metadata might look like:

```json
{
  "file_name": "sales_data.csv",
  "creation_date": "2024-01-22",
  "source": "Internal Sales System",
  "number_of_rows": 1200,
  "number_of_columns": 5,
  "columns": [
    {"name": "Date", "type": "Date", "description": "Date of sale"},
    {"name": "Product_ID", "type": "String", "description": "Unique identifier for the product"},
    {"name": "Quantity", "type": "Integer", "description": "Number of products sold"},
    {"name": "Price", "type": "Float", "description": "Sale price per unit"},
    {"name": "Total_Sales", "type": "Float", "description": "Total sales amount"}
  ],
  "preprocessing": [
    {"step": "Data Cleaning", "description": "Removed null values and corrected data formats"},
    {"step": "Normalization", "description": "Normalized the Price column using min-max scaling"}
  ],
  "notes": "Data updated monthly. Last update included Q4 2023 sales data."
}
```

### Automating the Metadata Generation

To automate the process of generating this metadata, you can use a
script in Python. This script will:

1. Read the CSV file.
2. Extract relevant information such as the number of rows and columns,
   column names, etc.
3. Generate and save the metadata in a JSON file.

Here's a simple Python script to achieve this:

```python
import json
import pandas as pd
from datetime import datetime

def generate_metadata(csv_file_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Extracting information
    file_name = csv_file_path.split('/')[-1]
    creation_date = datetime.now().strftime("%Y-%m-%d")
    number_of_rows = df.shape[0]
    number_of_columns = df.shape[1]
    columns = [{"name": col, "type": str(df[col].dtype)} for col in df.columns]

    # Metadata dictionary
    metadata = {
        "file_name": file_name,
        "creation_date": creation_date,
        "source": "Specify the data source",
        "number_of_rows": number_of_rows,
        "number_of_columns": number_of_columns,
        "columns": columns,
        "preprocessing": [],  # Add any preprocessing steps manually or through code
        "notes": "Add any additional notes here"
    }

    # Saving metadata to a JSON file
    with open(file_name.replace('.csv', '_metadata.json'), 'w') as json_file:
        json.dump(metadata, json_file, indent=4)

# Example usage
generate_metadata('path/to/your/sales_data.csv')
```

### Notes:

- The `preprocessing` section is left empty in the script. This is
  because preprocessing steps can vary widely and might need to be added
  manually or captured through additional scripting logic based on your
  specific data pipeline.
- The script assumes a basic understanding of the data's source and
  nature. Adjustments may be required based on the specific context of
  your data.
- The script uses the `pandas` library for data handling. Ensure this
  library is installed in your Python environment (`pip install
  pandas`).

This automated approach can save significant time and reduce errors in
metadata creation, especially for large datasets or frequent data
updates.

## Data Documentation Example

### Overview
This document describes the `sales_data.csv` dataset, which contains
records of sales transactions for a retail company. The dataset is
updated monthly and includes detailed information about each sale,
including the date, product details, and sale amounts.

### File Details

The file is named `sales_data_documentation.md` which clearly indicates
its purpose and content.

- **File Name**: `sales_data.csv`
- **Creation Date**: 2024-01-22
- **Last Updated**: 2024-01-22
- **Total Records**: 1200
- **Source**: Internal Sales System

### Data Dictionary

| Column Name  | Data Type | Description                           |
| ------------ | --------- | ------------------------------------- |
| Date         | Date      | Date of sale (format: YYYY-MM-DD)     |
| Product_ID   | String    | Unique identifier for the product     |
| Quantity     | Integer   | Number of products sold               |
| Price        | Float     | Sale price per unit (in USD)          |
| Total_Sales  | Float     | Total sales amount (in USD)           |

### Preprocessing Steps

1. **Data Cleaning**
   - Null values in the `Price` and `Quantity` columns were removed.
   - Date formats were standardized to `YYYY-MM-DD`.
   
2. **Normalization**
   - The `Price` column was normalized using min-max scaling.

### Usage Notes

- The dataset is intended for internal use only.
- Data is confidential and should not be shared outside the organization
  without proper authorization.
- For any discrepancies or data requests, contact the Data Management
  Team.

### Versioning

- Current Version: 1.2
- Previous Versions:
  - 1.1 - Included Q3 2023 sales data.
  - 1.0 - Initial dataset creation.
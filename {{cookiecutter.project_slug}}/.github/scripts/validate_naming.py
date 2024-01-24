import os
import sys
import re


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
    error = False
    if not validate_git_branch_naming():
        print(f"Invalid Git branch naming convention.")
        error = True

    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".pkl") and not validate_model_file_naming(file):
                print(f"Invalid model file naming convention: {file}")
                error = True
            elif file.endswith((".ipynb", ".py")) and not validate_ml_file_naming(file):
                print(f"Invalid notebook/script naming convention: {file}")
                error = True
            elif file.endswith(
                (".csv", ".xlsx", ".json")
            ) and not validate_data_file_naming(file):
                print(f"Invalid data file naming convention: {file}")
                error = True

    if error:
        sys.exit(1)


if __name__ == "__main__":
    main()

# Using Cookiecutter Without Direct GitHub Command

!!! tip "Goal"
    Learn how to manually download and use a Cookiecutter template from GitHub when direct command line access to GitHub (`cookiecutter gh:...`) is not available.

## Prerequisites

- Basic understanding of command line operations.
- Python and pip installed on your system.
- Access to GitHub through a web browser.

## Steps

### 1. Downloading the Cookiecutter Template

???+ note "Find and Download the Repository"
    - **Find the Repository:** Visit the GitHub page of the desired Cookiecutter template, e.g., `LLMsLab/cookiecutter-ai-flock`.
    - **Download the Repository:** Click on the 'Code' button, select 'Download ZIP', save, and extract it to a known location on your computer.

### 2. Setting Up Your Environment

``` bash
# Install Cookiecutter if not already installed
pip install cookiecutter

# Navigate to your desired project directory
cd path/to/your/Projects
```

!!! warning
    Replace `path/to/your/Projects` with the actual path where you want to create your project.

### 3. Creating Your Project

???+ success "Run Cookiecutter and Input Project Details"
    Run Cookiecutter and provide the path to the unzipped template folder:

    ``` bash
    cookiecutter path/to/unzipped/cookiecutter-ai-flock
    ```

    Replace `path/to/unzipped/cookiecutter-ai-flock` with the actual path to the unzipped template. Follow the prompts to input details for your new project.

### 4. Finalizing the Project

After running the command, a new directory with your project name will
be created. Navigate to this directory to perform any additional setup
required by the template.

!!! check "Conclusion"
    You've successfully used a Cookiecutter template without direct GitHub command line integration. This approach is useful in environments with restricted internet access or limitations in using GitHub tools directly.
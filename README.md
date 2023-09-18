# Cookiecutter for Retrieval-Augmented Generation

_Dive into a meticulously crafted, yet adaptable blueprint tailored for cutting-edge artificial intelligence projects._

Welcome to a [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html) template that's more than just a starting point. It's a statement of best practices, a commitment to industry standards, and a toolkit for success. Whether you're developing, testing, linting, documenting, or setting up continuous integration, this template ensures you're on the front foot, right from the get-go.

## 🌟 Features

- **Poetry Integration**: Streamlined Python dependency management and packaging, ensuring consistency and reproducibility.
- **Conda Environments**: Reliable and isolated environments for your project, ensuring compatibility and stability.
- **Black & Ruff**: Elegant code formatting with Black, complemented by the comprehensive linting capabilities of Ruff.
- **Automated Workflows**: Pre-configured pre-commit hooks and GitHub Actions to maintain code quality and standards effortlessly.
- **VS Code Ready**: Dive right into coding with our curated list of extensions and settings tailored for this project.
- **Intelligent Spell Checking**: A custom dictionary for the code spell checker, dynamically generated based on your project's Python dependencies.
- **Hydra**: Simplify and manage your configuration files with the power of Hydra.
- **Professional Documentation**: MkDocs combined with the Material theme provides a sleek and responsive documentation site, right out of the box. Plus, we've included a handpicked configuration to get you started.
- **Git-Ready**: A meticulously crafted `.gitignore` file to keep your repository clean.

## 🛠 Requirements to Use the Cookiecutter Template

- **Editor**: Visual Studio Code, the modern and extensible editor loved by many.
- **Version Control**: GitHub, the heart of open-source collaboration.
- **Language**: Python 3, the lingua franca of data science and AI.
- **Operating System**: Currently tailored for Linux Ubuntu, but stay tuned for support for more OSs in upcoming releases!
- **Cloud Integration**: Designed with Azure Machine Learning in mind. Future releases will broaden horizons to other cloud platforms and local setups.
- **Tooling**: [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html) Python package, the foundation of this template.

## Usage

First, make sure you have installed Cookiecutter:

```shell
pip install cookiecutter
```

To generate a new project, run:

```shell
cookiecutter gh:LLMsLab/cookiecutter-rag
```

Follow the prompts to enter your project details.

## The resulting directory structure

The directory structure of your new project looks like this:

```text
├── .env                        <- Environment variables for the project such secrets.
├── .git                        <- Git version control repository folder.
│   ├── HEAD                    <- Points to the current branch.
│   ├── branches                <- Folder for branch references.
│   ├── config                  <- Local configuration.
│   ├── description             <- Text file for the repository description.
│   ├── hooks                   <- Client-side or server-side scripts to run during git actions.
│   ├── info                    <- Additional info for the repository.
│   ├── objects                 <- All data for the repository (trees, commits, blobs).
│   └── refs                    <- References to commits (branches, tags, remotes).
├── .github                     <- GitHub-specific settings and configurations.
│   ├── CODEOWNERS              <- Specifies individuals or teams that are responsible for code in a repository.
│   ├── ISSUE_TEMPLATE          <- Templates for issues to be used by contributors.
│   │   ├── ask_issues_template.md         <- Issue template for asking questions.
│   │   ├── bug_report_template.md         <- Issue template for reporting bugs.
│   │   ├── data_aquisition_template.md    <- Issue template for data acquisition tasks.
│   │   ├── data_creation_template.md      <- Issue template for data creation tasks.
│   │   ├── experiment_issues_template.md  <- Issue template for experiment tasks.
│   │   ├── explore_issues_template.md     <- Issue template for exploration tasks.
│   │   ├── feature_request.md             <- Issue template for feature requests.
│   │   └── model_issues_templates.md      <- Issue template for model-related tasks.
│   ├── PULL_REQUEST_TEMPLATE   <- Templates for pull requests to be used by contributors.
│   │   └── pull_request_template.md       <- Template for creating new pull requests.
│   └── workflows               <- GitHub Actions workflows for CI/CD.
│       └── black.yaml          <- Workflow for the Black code formatter.
├── .gitignore                  <- Specifies intentionally untracked files to ignore.
├── .pre-commit-config.yaml     <- Configuration for pre-commit hooks to enforce coding style and checks.
├── .ruff_cache                 <- Cache directory for the Ruff tool.
├── .vscode                     <- Configuration for Visual Studio Code editor.
│   ├── cspell.json             <- Configuration for the Code Spell Checker in VS Code.
│   ├── dictionaries            <- Custom dictionaries for the Code Spell Checker.
│   │   └── data-science-en.txt <- Dictionary file for data science terms.
│   ├── extensions.json         <- Specifies extensions recommended for the project in VS Code.
│   └── settings.json           <- Project-specific settings for VS Code.
├── Makefile                    <- Makefile with commands like `make data` or `make train`.
├── README.md                   <- The top-level README for developers using this project.
├── config                      <- Directory for project configuration files.
├── data                        <- Data for the project, divided into different stages of data processing.
│   ├── external                <- Data from third party sources.
│   ├── interim                 <- Intermediate data that has been transformed.
│   ├── processed               <- The final, canonical data sets for modeling.
│   └── raw                     <- The original, immutable data dump.
├── docs                        <- Directory for project documentation.
│   ├── api-reference.md        <- API reference documentation.
│   ├── explanation.md          <- Explanatory documentation on the project.
│   ├── how-to-guides.md        <- Step-by-step guides on tasks.
│   ├── index.md                <- The main page of the documentation.
│   └── tutorials.md            <- Tutorials for the project.
├── mkdocs.yml                  <- Configuration file for the MkDocs documentation tool.
├── models                      <- Directory for trained models.
├── notebooks                   <- Jupyter notebooks for data exploration and experimentation.
├── poetry.lock                 <- Lock file generated by Poetry to lock dependencies to specific versions.
├── pyproject.toml              <- Specifies dependencies for the project in a format that Poetry can understand.
├── src                         <- Source code for the project.
│   └── {{cookiecutter.package_name}}          <- Main module for the project.
│       ├── __init__.py         <- Makes {{cookiecutter.package_name}} a Python module.
│       ├── app.py              <- Main application script.
│       └── utils.py            <- Utility functions for the project.
└── tests                       <- Directory for test files.
```

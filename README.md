# Cookiecutter for GenAI, ML & AI

Welcome to a
[Cookiecutter](https://www.cookiecutter.io/)
template engineered for artificial intelligence, machine learning, and
generative AI projects. This template isn't just a starting point; it's
a comprehensive framework designed to guide you through the intricacies
of AI project development.  It combines best practices, industry
standards, and a suite of tools that aligns with the dynamic needs of
modern AI development.

<p align="center">
  <img src="docs/assets/logo-gh.png" alt="Logo" width="200"/>
</p>

## 🌟 Features

- **VS Code Dev Container Extension**: Fully integrated with Visual
  Studio Code Development Containers, providing a consistent and
  isolated development environment irrespective of your local setup.
- **Poetry and pyenv Integration**: Streamlined Python dependency
  management and version control with Poetry and pyenv, ensuring
  consistent and isolated environments for your projects.
- **Weight & Bias Ready**: The template is pre-configured to work
  seamlessly with Weight & Bias, a leading tool for machine learning
  experiment tracking, allowing you to monitor and compare your ML
  models effectively.
- **Black & Ruff**: Elegant code formatting with Black, augmented by the
  comprehensive linting capabilities of Ruff.
- **Automated Workflows**: Pre-configured pre-commit hooks and GitHub
  Actions automate code quality checks and standards enforcement.
- **VS Code Optimized**: A carefully selected collection of VS Code
  extensions and settings, optimized for AI development, ensures you can
  start coding right away.
- **Intelligent Spell Checking**: Tailored code spell checker with a
  custom dictionary generated from your project's Python dependencies.
- **Hydra Configuration Management**: Simplify and manage your
  configuration files efficiently with Hydra.
- **Professional Documentation**: MkDocs combined with the Material
  theme, ready to create a responsive documentation site with a curated
  initial setup.
- **Git-Ready**: A meticulously crafted `.gitignore` file tailored for
  AI projects ensures a clean and organized repository.

## 🛠 Requirements to Use the Cookiecutter Template

- **Editor**: Visual Studio Code, a modern, versatile, and extensible
  editor, ideal for Python and AI development.
- **Version Control**: GitHub, the cornerstone of collaborative
  open-source and private development projects.
- **Language**: Python 3, the go-to language for data science, machine
  learning, and AI applications.
- **Docker Desktop**: Required for managing and running your Docker
  containers, providing a consistent development environment across
  various platforms.
- **Weight & Bias**: Ready for integration with Weight & Bias for
  advanced machine learning experiment tracking and model management.

## 📖 Usage

### Installing Cookiecutter

Before starting, ensure Cookiecutter is installed on your system:

```shell
pip install cookiecutter
```

### Generate a New Project

Create a new project by running:

```shell
cookiecutter gh:LLMsLab/cookiecutter-genai-ml-ai.git
```

You will be prompted to enter details for your project, such as project
name, OS type, author name, and more. For example:

```bash
  [1/9] project_name (Project Name): My AI Project
  [2/9] project_slug (my-ai-project):
  [3/9] package_name (myaiproject):
  [4/9] environment_name (my-ai-project-env):
  [5/9] author_name (Your name or your organization/company/team): Jane Doe
  [6/9] author_email (youremail@example.com): jane.doe@example.com
  [7/9] description (A short description of the project.): AI project development
  [8/9] independent_reviewer (github_username_of_independent_reviewer):
  [9/9] site_name (My AI Project Docs):
INFO:root:Current working directory: /Users/username/Projects/my-ai-project
```

This process will generate a new project with your specific
configurations.

This will create a new project based on the `cookiecutter-rag` template
with your specified details.

```bash
cd my-ai-project
```

Once you're in your project's directory, you can open the entire
directory in Visual Studio Code:

```bash
code .
```

### Generate a Project from a Downloaded Template

If you have already downloaded the Cookiecutter template:

#### Listing Installed Cookiecutter Templates

To see installed Cookiecutter templates, use:

```bash
cookiecutter --list-installed
1 installed templates:
 * cookiecutter-rag
```

#### Locating the `.cookiecutters` Directory on a Mac

Your cloned cookiecutters are usually stored in `~/.cookiecutters/`.

1. **Open Terminal**: Find Terminal in Applications > Utilities, or use
   Spotlight.

2. **Navigate to Home Directory**: Type `cd ~` and press Enter.

3. **List Hidden Directories**: Use `ls -a` to view all files and
   directories, including hidden ones like `.cookiecutters`.

4. **Access the `.cookiecutters` Directory**: Enter `cd .cookiecutters`.

5. **View Template Contents (Optional)**: Use `ls` to view the templates
   in the `.cookiecutters` directory.

   ```bash
   pwd
   /Users/username/.cookiecutters/cookiecutter-rag
   ```

#### Creating a New Project with a Template

To create a project using the `cookiecutter-rag` template:

```bash
cookiecutter /Users/username/.cookiecutters/cookiecutter-rag
```

Enter the details for your project when prompted. For instance:

```bash
  [1/9] project_name (Project Name): My AI Project
  [2/9] project_slug (my-ai-project):
  [3/9] package_name (myaiproject):
  [4/9] environment_name (my-ai-project-env):
  [5/9] author_name (Your name or your organization/company/team): Jane Doe
  [6/9] author_email (youremail@example.com): jane.doe@example.com
  [7/9] description (A short description of the project.): AI project development
  [8/9] independent_reviewer (github_username_of_independent_reviewer):
  [9/9] site_name (My AI Project Docs):
INFO:root:Current working directory: /Users/username/Projects/my-ai-project
```

This will create a new project based on the `cookiecutter-rag` template
with your specified details.

```bash
cd my-ai-project
```

Once you're in your project's directory, you can open the entire
directory in Visual Studio Code:

```bash
code .
```

## 📁 Resulting Directory Structure

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
├── .devcontainer               <- Configurations for the VS Code Development Container.
│   └── devcontainer.json       <- Configuration file for setting up the VS Code Development Container.
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

# 🚀 {{cookiecutter.project_name}}

{{cookiecutter.description}}

Certainly! Here's your updated message with the additional text:

⚡⚡ This project has been created using the [Cookiecutter RAG](https://github.com/LLMsLab/cookiecutter-rag)
template. The following website provides information on how to use all
the tools included in the project repository: [Cookiecutter RAG Template
Docs](https://llmslab.github.io/cookiecutter-rag/) ⚡⚡

## 📂 Directory Structure

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

## 👉 Instructions

For detailed steps on setting up a Python environment on a Windows 10 OS
machine without admin rights and behind a firewall, please refer to the
Docs page of the Cookiecutter RAG website:

📖 [Cookiecutter RAG Windows OS Setup
Guide](https://llmslab.github.io/cookiecutter-rag/tutorials/windows-os-setup/)

This comprehensive guide covers all prerequisites and steps necessary to
ensure a smooth Python development setup. It includes instructions for
installing essential tools such as Visual Studio Code, Anaconda, and Git
Bash without requiring administrative privileges. Additionally, it
provides guidance on configuring your environment behind a firewall.

Ensure you follow these instructions meticulously to ensure your Python
environment is prepared effectively for your
{{cookiecutter.package_name}} project. Dive in and best of luck with
your setup!

After completing the [Cookiecutter RAG Windows OS Setup
Guide](https://llmslab.github.io/cookiecutter-rag/tutorials/windows-os-setup/),
please proceed with the following "Per-project Instructions".

## 🔄 Per-Project Instructions

To install all project's dependencies using Poetry we continue without VPN

### ✅ Create and Activate a Conda's Python Virtual Environment

```bash
make conda_create
conda activate {{cookiecutter.environment_name}}
```

### ✅ Install Dependencies

```bash
make poetry_dependencies
```

### ✅ Build Documentation

```bash
make docs_build
```

### ✅ Start the live-reloading docs server

```bash
make docs_serve
```

Ensure that the documentation is being served at:
`http://127.0.0.1:8000/{{cookiecutter.project_slug}}/`

- Terminate the server by pressing `Ctrl + C`.
- Once done, close the current VS Code session and reopen the project.

### ✅ CSpell Checker: Extracting Terms from Python Libraries

Enhance the CSpell checker's dictionary with terms from the Python
libraries:

```bash
make cspell_dictionary
```

### ✅ Secure Connection and Pushing to GitHub

Before sharing your project on GitHub, ensure you have a secure
connection to the GitHub server. Here are the steps to create a GitHub
repository, initialize your local repository, set up user information,
change the default branch name, commit, and push your project to GitHub:

1. **Create a GitHub Repository:** Go to [GitHub](https://github.com/)
   and create a new repository with the name
   `{{cookiecutter.project_slug}}`. Do not include a project description
  or a `README.md` file.

2. **Initialize the Repository:**
   ```bash
   git init
   ```
   This command initializes a new Git repository in your project
   directory.

3. **Set Up User Information:**
   ```bash
   git config user.name "Your Name"
   git config user.email "your-email@example.com"
   ```
   Replace "Your Name" and "your-email@example.com" with your own
   information.

4. **Change Default Branch Name:**
   ```bash
   git branch -M development
   ```
   This command renames the default branch from `main` to `development`.

5. **First Commit to the Repository:**
   ```bash
   git add .
   git commit -m "Initial commit"
   ```
   These commands stage all the files in your project directory and
   commit them to the repository with a message of "Initial commit".

6. **Push to GitHub:** Link your local repository to the GitHub
   repository and push your local content to GitHub:
   ```bash
   git remote add origin https://github.com/username/{{cookiecutter.project_slug}}.git
   git push -u origin development
   ```
   Replace
   "https://github.com/username/{{cookiecutter.project_slug}}.git" with
   the URL of your GitHub repository.

Remember, maintain a secure connection to GitHub to ensure the integrity
and confidentiality of your project during this process.

## 📝Notes

- Remember deactivate it when you're done using `conda deactivate`.
- This guide assumes the use of `make` commands defined in a `Makefile`.
  If you aren't using a Makefile, replace the `make` commands with the
  corresponding Python commands.
- Running the `make` command displays a menu of available options, each
  associated with a specific command for easy project management.

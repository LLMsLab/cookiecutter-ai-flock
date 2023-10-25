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

Welcome to the setup guide for creating a Python environment on a
Windows 10 OS machine without admin rights and behind a firewall. This
guide will walk you through all the prerequisites and steps required to
set up a Python development environment, ensuring you can work
seamlessly even with limited permissions on your Windows 10 machine.

In the following sections, you will find instructions on installing
essential tools like Visual Studio Code, Anaconda, and Git Bash without
requiring administrative privileges. We'll also provide guidance on
configuring your environment behind a firewall, ensuring a smooth setup
process for your {{cookiecutter.package_name}} project.

Follow these steps carefully to get your Python environment up and
running, and you'll be well-equipped to dive into your
{{cookiecutter.package_name}} project. Let's
get started!

### 🔑 Prerequisites

Before you can get started with this project, you'll need to have the
following software installed on your Windows 10 machine:

1. **Visual Studio Code (VS Code):**
   - Download and install VS Code by following the instructions on the
     official website: [VS Code
     Download](https://code.visualstudio.com/download)
   - During the installation process, choose an installation location
     within a directory where you have write permissions, typically
     within your user directory. You should not encounter any admin
     rights issues during the installation of VS Code.

2. **Anaconda Distribution:**
   - Download the Anaconda Distribution for Windows from the official
     website: [Anaconda
     Download](https://www.anaconda.com/products/distribution)
   - Follow these steps to install Anaconda without admin rights:
     - During the Anaconda installation process, when you reach the
       "Advanced Options" section, select the "Install for me only"
       option.
     - Choose a directory location where you have write permissions
       (e.g., your user directory) for the installation.
     - Complete the installation process.

3. **Git Bash:**
   - Download and install Git Bash, which provides a Unix-like
     command-line environment for Windows: [Git Bash
     Download](https://git-scm.com/downloads)
   - During the installation, choose an installation location within a
     directory where you have write permissions (e.g., your user
     directory). You should not encounter any admin rights issues when
     installing Git Bash.

Once you have installed these prerequisites, you'll be ready to set up
and run this project on your Windows 10 machine, even without admin
rights.

---

### 🛠️ One-Time Setup Instructions

#### ✅ Install Recommended VS Code Extensions

To ensure a consistent development environment and take advantage of
tools and configurations tailored for this project, we recommend
installing the extensions listed in the `.vscode/extensions.json` file.

1. Open the project in Visual Studio Code.
2. Open the Extensions panel by clicking on the square icon on the
   sidebar or pressing `Ctrl+Shift+X`.
3. In the Extensions search bar, type `@recommended` to filter and
   display the list of recommended extensions for the project.
4. For each recommended extension, click the `Install` button to add it
   to your VS Code setup.

#### ✅ Enable the Usage of Conda Commands from the Git Bash Terminal in VS Code

Follow the steps below to enable the usage of Conda commands from the
Git Bash terminal in VS Code:

1. **Identify Anaconda Installation Path**:
   - Open the Anaconda Prompt from the Start menu.
   - Type the command `conda info` and press Enter.
   - Look for the line that starts with `base environment :`. This line
     will show the path to your Anaconda installation.

```bash
conda info
```

2. **Activate Conda in Git Bash**:
   - Launch VS Code.
   - Open a new terminal (ensure it's Git Bash).
   - Execute the following command, replacing the path with your
     Anaconda installation path obtained in the previous step:

```bash
. C:/Users/T93KQI0/Anaconda3/etc/profile.d/conda.sh
```

1. **Automate Conda Activation**:

To automate the activation of Conda every time you open a Git Bash
terminal in VS Code follow the next steps.

Check the location of your `.bashrc` and `.bash_profile` files, you can
use the following command in your Git Bash terminal:

```bash
echo $HOME
```

> Remember, the `.bashrc` and `.bash_profile` files may be hidden, so
> ensure you have enabled viewing hidden files in File Explorer.

If the `.bashrc` and `.bash_profile` files are not present in your home
directory, you can create them using the following steps:

1. **Open Git Bash**:
   - Launch Git Bash from the Start menu or from within Visual Studio
     Code.

2. **Create the `.bashrc` File**:
   - In Git Bash, enter the following command to create a `.bashrc` file
     in your home directory:
     ```bash
     touch ~/.bashrc
     ```
   - The `touch` command creates an empty `.bashrc` file if it doesn't
     exist.

3. **Create the `.bash_profile` File**:
   - Similarly, create a `.bash_profile` file using the following
     command:
     ```bash
     touch ~/.bash_profile
     ```

4. **Edit the `.bash_profile` File**:
   - Now, edit the `.bash_profile` file to include a command to source
     the `.bashrc` file whenever a new Bash session is started. You can
     use a text editor like `nano` for this task:
     ```bash
     nano ~/.bash_profile
     ```
   - In the text editor, add the following lines:
     ```bash
     if [ -f ~/.bashrc ]; then
       source ~/.bashrc
     fi
     ```
   - Save the file and exit the text editor (in `nano`, press `Ctrl + X`
     to exit, press `Y` to confirm changes, and press `Enter` to save).

5. **Edit the `.bashrc` File**:
   - Now, edit the `.bashrc` file to include the Conda configuration:
     ```bash
     nano ~/.bashrc
     ```
   - In the text editor, add the following line:
     ```bash
     . C:/Users/T93KQI0/Anaconda3/etc/profile.d/conda.sh
     ```
   - Save the file and exit the text editor.

6. **Apply the Changes**:
   - You can now apply the changes by either closing and reopening Git
     Bash or by sourcing the `.bash_profile` file:
     ```bash
     source ~/.bash_profile
     ```

Now, whenever you start a new Bash session, the `.bashrc` file will be
sourced automatically thanks to the configuration in the `.bash_profile`
file, and the Conda configuration in the `.bashrc` file will be loaded,
enabling you to use Conda commands.

7. **Verify Conda Activation**:
   - Close and reopen the Git Bash terminal in VS Code.
   - Type `conda activate` and press Enter. You should see `(base)`
     appear in the terminal, indicating the base Conda environment is
     active.

Now, you can use Conda commands from the Git Bash terminal in VS Code on
your Windows 10 machine. Each time you open a new Git Bash terminal in
VS Code, Conda will be activated automatically, allowing you to manage
your Conda environments and packages seamlessly.

#### ✅ Install Linux Tools

If you don't have admin rights on a Windows computer, installing new
software system-wide might not be possible. However, you can still use
some tools within your local environment, like Git Bash, by following
these steps to install, for example, `make` tool.

`make` is a tool that controls the generation of executables and other
non-source files of a program. Here's how you can add it to Git Bash:

1. Go to the
   [ezwinports](https://sourceforge.net/projects/ezwinports/files/) to
   download `make-4.4.1-without-guile-w32-bin.zip`.
   [Ref](https://www.pascallandau.com/blog/setting-up-git-bash-mingw-msys2-on-windows/)

2. Unzip it to a directory, let's say
   `C:\Users\T93KQI0\Tools\make-4.4.1-without-guile-w32-bin`.

3. Add that directory to your Git Bash `$PATH`:
   ```bash
   echo 'export PATH=$PATH:C:\\Users\\T93KQI0\\Tools\\make-4.4.1-without-guile-w32-bin\\bin' >> ~/.bashrc
   source ~/.bashrc
   ```

Your `.bashrc` profile must be like this:

```bash
. C:/Users/T93KQI0/Anaconda3/etc/profile.d/conda.sh
export PATH=$PATH:C:\\Users\\T93KQI0\\Tools\\make-4.4.1-without-guile-w32-bin\\bin
```

4. Now you should be able to use `make` from within Git Bash.

Remember, whenever you add tools this way, you're only adding them for
your user in Git Bash. They won't be available in other command-line
environments unless you modify their paths similarly.

Also, note that some tools might have dependencies. Always check
documentation or README files to ensure you have all the required files.

#### ✅ Install Poetry for Dependency Management

Here are the steps to install Poetry in the NYL Windows 10 machine
without admin access and firewall.

##### Disconnect VPN

Disconnect your VPN is it is connected.

##### Update Conda

Open the Anaconda PowerShell Prompt and update your Conda installation:

```bash=
conda update conda
```

##### Install Poetry for Package Management

Following the Poetry's docs, let's install Poetry with `pipx`. First
install `pipx`:

```bash=
pip install pipx
```

Install Poetry using `pipx`:

```bash=
pipx install poetry
```

Output:

```bash=
installed package poetry 1.6.1, installed using Python 3.9.18

These apps are now globally available

- poetry.exe

⚠️ Note: 'C:\\Users\\T93KQI0\\.local\\bin' is not on your PATH environment variable. These apps will not be globally accessible until your PATH is
updated. Run pipx ensurepath to automatically add it, or manually modify your PATH in your shell's config file (i.e. ~/.bashrc).

done! ✨ 🌟 ✨
```

It looks like Poetry was installed successfully using Pipx, but the
`.local/bin`folder where the poetry executable is installed is not in
your PATH environment variable.

Since you don't have admin access to modify the PATH globally, you need
to update it just for your user account.

Since we are using `.bashrc` and `.bash_profile` files for our shell
configuration on Windows, here is how you can automatically add Poetry's
path to our `PATH`. Add the following line to your `.bash_profile`:

```bash
export PATH=$PATH:C:\\Users\\T93KQI0\\.local\\bin
```

Your `.bashrc` must looks like this:

```bash
# Add Anaconda to PATH
# Sourcing this script initializes Conda and adds it to the PATH
# This gives access to Conda, Python and any packages installed in the default Conda env
# This give access to Conda command from Git Bash integrated in VS Code
. C:/Users/T93KQI0/Anaconda3/etc/profile.d/conda.sh
# Add Make to PATH
# This adds the Make (GNU make) bin folder containing make.exe to the PATH
# Now Make can be run from any directory in the Git Bash terminal integrated in VS Code
export PATH=$PATH:C:\\Users\\T93KQI0\\Tools\\make-4.4.1-without-guile-w32-bin\\bin
# Add Poetry to PATH
# Poetry is used for Python dependency and package management
# It was installed using Pipx into the ~/.local/bin folder
# Adding this folder to PATH makes the poetry command globally available
# Now Make can be run from any directory in the Git Bash terminal integrated in VS Code
export PATH=$PATH:C:\\Users\\T93KQI0\\.local\\bin
# General notes:
# - Use single quotes for Windows paths
# - Escape spaces and special characters in paths
# - Export PATH additions to make commands globally available
# - Source scripts like conda.sh to initialize environments
# - Restart shell or run source ~/.bashrc after making changes
```

Now, restart your Git Bash terminal integrated in VS Code or run `source
~/.bashrc` and validate the Poetry command is available:

```bash=
$ poetry --version
Poetry (version 1.6.1)
(base) 
```

Notice that the Conda `base` environment must be activated to validate
that `conda`, `make` and, `poetry` commands are available on Git Bash:

```bash=
T93KQI0@IAG-MAGUI1-KQ10 MINGW64 ~/OneDrive - New York Life/Documents/Projects/service-sage-rag
$ conda activate
(base) 
T93KQI0@IAG-MAGUI1-KQ10 MINGW64 ~/OneDrive - New York Life/Documents/Projects/service-sage-rag
$ conda --version
conda 23.9.0
(base) 
T93KQI0@IAG-MAGUI1-KQ10 MINGW64 ~/OneDrive - New York Life/Documents/Projects/service-sage-rag
$ make --version
GNU Make 4.4.1
Built for Windows32
Copyright (C) 1988-2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
(base) 
T93KQI0@IAG-MAGUI1-KQ10 MINGW64 ~/OneDrive - New York Life/Documents/Projects/service-sage-rag
$ poetry --version
Poetry (version 1.6.1)
(base) 
```

> Notice that it is not necessary to update the project's `Makefile` to
> execute Poetry commands using Make.

---

### 🔄 Per-Project Instructions

To install all project's dependencies using Poetry we continue without VPN

#### ✅ Create and Activate a Conda's Python Virtual Environment

```bash
make conda_create
conda activate {{cookiecutter.environment_name}}
```

#### ✅ Install Dependencies

```bash

make poetry_dependencies

```

#### ✅ Build Documentation

```bash
make docs_build
```

#### ✅ Start the live-reloading docs server

```bash
make docs_serve
```

#### ✅ CSpell Checker: Extracting Terms from Python Libraries

Enhance the CSpell checker's dictionary with terms from the Python
libraries:

```bash
make cspell_dictionary
```

#### ✅ Secure Connection and Pushing to GitHub

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

### 📝Notes

- Remember deactivate it when you're done using `conda deactivate`.
- This guide assumes the use of `make` commands defined in a `Makefile`.
  If you aren't using a Makefile, replace the `make` commands with the
  corresponding Python commands.
- Running the `make` command displays a menu of available options, each
  associated with a specific command for easy project management.

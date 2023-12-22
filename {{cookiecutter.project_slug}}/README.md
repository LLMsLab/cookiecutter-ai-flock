# 🚀 {{cookiecutter.project_name}}

{{cookiecutter.description}}

Certainly! Here's your updated message with the additional text:

⚡⚡ This project has been created using the [Cookiecutter GenAI, ML &
AI](https://github.com/LLMsLab/cookiecutter-ai-flock) template. The
following website provides information on how to use all the tools
included in the project repository: [Cookiecutter Ai Flock
Template Docs](https://llmslab.github.io/cookiecutter-ai-flock/) ⚡⚡

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

## 👉 Introductions

Welcome to our Python development project! This document serves as a
comprehensive guide to our development environment, meticulously crafted
to provide a seamless and efficient workflow for Python programming.
Leveraging the power of Docker, Visual Studio Code, and a suite of
carefully selected tools, we have established a robust platform that
caters to the diverse needs of Python development. Here's an overview of
what we've set up:

- **Docker Container with VS Code Dev Container Extension**: Our
  development begins within a Docker container, created using the Visual
  Studio Code Dev Container extension. This approach ensures an isolated
  and consistent environment, crucial for reproducible development and
  testing.

- **VS Code Extensions for Python Development**: We've equipped Visual
  Studio Code with extensions specifically chosen for Python
  development. These tools enhance your coding experience with features
  like intelligent code completion, linting, and debugging.

- **Python Version Management with `pyenv`**: To accommodate varying
  Python version requirements, we've integrated `pyenv` into our
  environment. This tool allows us to effortlessly switch between
  different Python versions, ensuring compatibility across various
  projects.

- **Dependency Management with Poetry**: Managing project dependencies
  is streamlined with Poetry. It handles the definition, installation,
  and updating of libraries, contributing to reproducible builds and
  efficient dependency resolution.

- **Poetry Python Virtual Environment**: Our project dependencies reside
  in a Python virtual environment managed by Poetry. This setup isolates
  our project's dependencies, maintaining a clean global Python
  environment.

- **Installation of Python Dependencies**: All necessary Python
  dependencies are neatly installed and managed within our virtual
  environment, ready for use in our projects.

## **✅** Navigating and Initializing Your Development Environment

Following the introduction to creating a new project using Cookiecutter,
let's get started with the actual workflow. Here's how you can begin
working on your Python project in this tailored environment:

### Step 1: Move into the Project's Directory

First, you need to navigate to your project's directory. This is where
all your initial project files, set up by the Cookiecutter template, are
located. At this stage, the directory primarily includes the basic
scaffolding of your project, such directory structure and other
configuration files. Open a terminal and use the `cd` (change directory)
command to move into your project directory:

```bash
cd my-ai-project
```

Make sure to replace `my-ai-project` with the actual name of your
project directory.

### Step 2: Open Visual Studio Code

Once you're in your project's directory, you can open the entire
directory in Visual Studio Code. This will allow you to access all your
project files directly from the VS Code interface. Run the following
command in your terminal:

```bash
code .
```

The `code .` command launches Visual Studio Code and opens the current
directory (denoted by `.`), enabling you to start working on your
project immediately.

## **✅** Install Recommended VS Code Extensions Locally

To ensure a consistent development environment and take advantage of
tools and configurations tailored for this project, it's advisable to
install the extensions specified in the `.vscode/extensions.json` file.

To install all recommended extensions locally in Visual Studio Code,
follow these steps:

1. **Open the Extensions View**: Click on the Extensions icon in the
   Activity Bar on the side of your VS Code window. The icon looks like
   a square within a square.

2. **Access the Recommended Extensions**: In the Extensions view, look
   for a section titled "Recommended". This section may appear in
   different places depending on your version of VS Code and your user
   settings, but it is often at the bottom of the Extensions view or
   accessible through a tab at the top.

3. **Select Extensions to Install**: In the "Recommended" section, you
   will see a list of extensions recommended for your current workspace,
   which are typically specified in the `.vscode/extensions.json` file
   of your project. Extensions that are not already installed will have
   a green 'Install' button next to them.

4. **Install All Extensions**: Click the 'Install' button next to each
   recommended extension that is not already installed. If there are
   many extensions, you will need to click each one individually, as
   there is no built-in feature to install all recommendations at once
   from the GUI.

For an even more streamlined experience, consider using the
`@recommended` filter in the Extensions view search bar, which will show
you all the workspace-recommended extensions.

## **✅** Developing in Containers with the VS Code Extension Dev Containers

Developing within containers offers a consistent and isolated
environment, ensuring that software runs reliably when moved from one
computing environment to another. The Visual Studio Code Extension for
Development Containers simplifies this process, allowing developers to
create and manage development environments within Docker containers
seamlessly. By utilizing a `devcontainer.json` file, developers can
define their environment settings, dependencies, extensions, and more,
ensuring that every team member has a consistent development setup. This
approach is particularly beneficial for teams looking to standardize
their development environments and avoid the common "it works on my
machine" problem.

⚡⚡ **Important Note:** Before continuing with the following steps,
please ensure that Docker Desktop is up and running on your system.
Start Docker Desktop to proceed. ⚡⚡

### Section 1: Examine the Predefined Container Configuration

After opening your Cookiecutter-generated project in Visual Studio Code,
start by exploring the `.devcontainer` directory. This folder typically
contains a `devcontainer.json` file and, depending on your setup, a
`Dockerfile` or Docker Compose files. These files define your
containerized development environment. Review them to understand the
existing configuration and determine if any adjustments are needed for
your project.

### Section 2: Customize the Configuration (Optional)

You may find that the predefined container configuration needs tweaking
to suit your project's specific needs. This could involve modifying the
`devcontainer.json` file or the associated Docker files. Customizations
can range from simple settings adjustments to adding new software or
extensions required for your development workflow.

### Section 3: Reopen in Container

With your configuration reviewed (and possibly adjusted), use the
command palette in Visual Studio Code (`Ctrl+Shift+P` or `Cmd+Shift+P`)
and select "Remote-Containers: Reopen in Container". This command
instructs VS Code to build and start the container based on your
project’s Docker configuration. The first build may take some time, but
subsequent starts should be faster.

### Section 4: Work Inside the Container

Once the container is up and running, your development environment is
ready to use. This containerized environment mirrors the configuration
specified in the `devcontainer.json` file, ensuring consistency across
all developers working on the project. You can now write code, debug,
and use VS Code's features as if you were working on your local machine,
but with the benefits of a containerized environment.

### Section 5: Version Control

If you've made any modifications to the `.devcontainer` folder, it's a
good practice to commit these changes to your version control system.
This ensures that anyone else working on the project will have access to
the same development environment, further supporting the goal of a
consistent and reproducible setup.

## **✅** Install Recommended Extensions in a VS Code Development Container

Now that you have Visual Studio Code open in your containerized
development environment, a crucial first step is to install the
necessary Visual Studio Code extensions. This will ensure that you have
all the tools and functionalities you need right at your fingertips
within the container. Here's how to proceed:

1. **Open the Remote Explorer**: In Visual Studio Code, locate the
   Remote Explorer in the sidebar. This icon is typically represented by
   two small screens or resembles a remote window. This feature is
   integral for managing your connections to remote environments,
   including containers.

2. **Select Your Dev Container**: Within the Remote Explorer, identify
   and select your active development container. For your setup, it's
   named "Python 3 @ desktop-linux". Click on this container to make it
   the focus of your operations.

3. **Access Extensions for Installation**: At the bottom right corner of
   the Dev Container tab, you'll find a cloud icon with a download
   arrow. This icon is your gateway to installing extensions in the
   container. Click on it to view a list of available extensions for
   installation.

4. **Choose Extensions to Install**: A new pane will open, displaying a
   curated list of extensions suitable for your Dev Container.
   Extensions that you've already installed locally and are relevant to
   your project's environment will be pre-selected. Go through this
   list, review it, and make any necessary adjustments to your selection
   to tailor the environment to your project's needs.

5. **Confirm and Install**: Once you've selected all the desired
   extensions, click on the "OK" button. This action initiates the
   installation of your chosen extensions into the Dev Container.

By following these steps, you'll effectively equip your development
container with all the recommended extensions, making sure your working
environment is both efficient and tailored to your project’s specific
needs. This setup not only enhances your productivity but also aligns
your development experience closely with the project's requirements.

## **✅** Installing `pyenv` in Linux Debian

In the realm of Python development, managing multiple versions of Python
can be a daunting task. This is where `pyenv` becomes a vital tool for
any developer's toolkit, especially when working in Linux environments
like Debian. `pyenv` simplifies the process of handling various Python
versions, allowing you to switch between them effortlessly. Below, we
provide a comprehensive guide to installing `pyenv` on a Linux Debian
system, ensuring you have the flexibility to work with different Python
versions as required by your projects.

> Debian Linux is often the default distribution for Docker containers
> due to its stability and minimal footprint. It's a popular choice for
> containerized environments because:
>
> - **Stability**: Debian is known for being a highly stable Linux
>   distribution, which is crucial for development environments where
>   consistency is key.
> - **Lightweight**: Debian's minimal base image is advantageous for
>   Docker containers, as it keeps the size small and the performance
>   efficient.
> - **Wide Package Availability**: Debian's extensive package
>   repositories make it easy to install and run a wide range of
>   software, which is essential for diverse development needs.
> - **Security**: Debian has a strong focus on security, ensuring that
>   the containers are secure by default, an important aspect for any
>   development work.
>
> These characteristics make Debian a go-to choice for Docker
> containers, especially when used in conjunction with tools like the
> Visual Studio Code Dev Container extension, which seeks to provide a
> reliable and versatile development environment.

### 1. Install `pyenv` in Linux

#### 1.1. Install all the required packages

Before diving into the installation of `pyenv`, it's crucial to set up
the necessary prerequisites. This step involves installing packages that
are essential for `pyenv` to function correctly. Execute the following
command in your terminal to install these packages:

```shellell
# On Debian/Ubuntu/Linux Mint ------------ 
sudo apt install curl git-core gcc make zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libssl-dev
```

#### 1.2. Grab the latest **pyenv** source tree from its Github repository

With the prerequisites in place, the next step is to download `pyenv`
from its official GitHub repository. This ensures you are getting the
most recent version directly from the source:

```shellell
git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
```

#### 1.3. Set the environment variable **PYENV_ROOT**

Setting the `PYENV_ROOT` environment variable is a key step in the
installation process. This variable tells your system where `pyenv` is
located. Additionally, modifying your `$PATH` allows the shell to locate
the `pyenv` command. Use `nano` or your preferred text editor to add
these configurations to your `.bashrc` file:

```shellell
nano $HOME/.bashrc
```

Then add the following lines:

```bash
## pyenv configs
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
```

#### 1.4. Source **$HOME/.bashrc** file or restart the shell

To apply the changes made to your `.bashrc` file, you need to either
source the file or restart your shell. This step is crucial for the
changes to take effect:

```shellell
source $HOME/.bashrc
# or:
exec "$SHELL"
```

### 2. How to Install Multiple Python Versions in Linux

After successfully installing `pyenv`, you can now manage multiple
Python versions with ease. The following steps outline how to view,
install, and set different Python versions using `pyenv`:

View all available versions with this command:

```shellell
pyenv install -l
```

You can now install multiple Python versions via `pyenv`, for example:

```shellell
pyenv install 3.10.13
pyenv install 3.11.5
```

List all Python versions available to `pyenv`:

```shellell
pyenv versions
```

Check the global Python version:

```shellell
pyenv global
```

Set the global python version using the pyenv command:

```shellell
pyenv global 3.10.13
pyenv global
```

> **Reference**:[Install
> `pyenv`](https://gist.github.com/trongnghia203/9cc8157acb1a9faad2de95c3175aa875)

To verify the successful installation of `pyenv` and the default Python
version, run these commands:

```shellell
pyenv --version
```

This command will display the installed version of `pyenv`, like `pyenv
   2.3.35-2-g96f93fd5`, confirming its presence in your environment.


And,

```shellell
vscode ➜ /workspaces/my-ai-project $ python --version
```

This command will display the installed version of `python`, like
`Python 3.10.13`, confirming its presence in your environment.

This section guides you through the process of installing `pyenv` on
Linux Debian, an essential tool for managing multiple Python versions in
your development environment. With `pyenv`, you can effortlessly switch
between different Python versions, ensuring compatibility and
flexibility across various projects.

## **✅** Installing `pipx`

`pipx` is a valuable tool for Python developers, offering a neat way to
install and run Python applications in isolated environments. It's
particularly useful for installing command-line tools without worrying
about dependency conflicts or impacting the global Python environment.
In the context of your Debian-based Dev Container, `pipx` is typically
pre-installed. However, it's always good practice to verify its
installation and ensure you're using the latest version. Here's how you
can enhance this section of your documentation:

### Confirming the Installation of `pipx`

1. **Check `pipx` Version**: First, confirm that `pipx` is installed and
   determine its version. Run the following command in your container's
   terminal:

   ```bash
   pipx --version
   ```

   This command will display the installed version of `pipx`, like
   `1.2.1`, confirming its presence in your environment.

2. **Update `pipx` (Optional)**: If you wish to update `pipx` to the
   latest version, or if it's not already installed, you can install or
   upgrade it using `pip`, Python's package installer. This step ensures
   that you have the most recent features and security updates:

   ```bash
   python3 -m pip install --upgrade pipx
   ```

3. **Verify the Update**: After the installation or update, it's a good
   idea to verify that `pipx` is correctly installed and functional. You
   can do this by re-running the `pipx --version` command:

   ```bash
   pipx --version
   ```

By following these steps, you not only confirm the presence of `pipx` in
your Docker container but also ensure that it's up-to-date. This
approach adds an extra layer of verification to your setup process,
aligning with best practices in software development.

## **✅** Installing Poetry

Poetry is an increasingly popular tool among Python developers for its
efficient management of project dependencies and packaging. Using `pipx`
to install Poetry is a smart choice as it isolates Poetry in its own
environment, preventing any conflicts with other Python packages. Below
is an enhanced guide to ensure a smooth installation and upgrade process
for Poetry in your development environment.

### Installing Poetry with `pipx`

1. **Install Poetry**: To install Poetry using `pipx`, execute the
   following command in your container's terminal. This command installs
   Poetry in an isolated environment, making it globally accessible
   without affecting other Python packages.

   ```bash
   pipx install poetry
   ```

   Upon successful installation, you should see a confirmation message
   indicating the installed version of Poetry and the Python version
   used, similar to:

   ```bash
   installed package poetry 1.7.1, installed using Python 3.10.13
   These apps are now globally available
     - poetry
   done! ✨ 🌟 ✨
   ```

2. **Upgrade Poetry (Optional)**: Keeping Poetry up-to-date is important
   to benefit from the latest features and security updates. To upgrade
   Poetry, use the following command:

   ```bash
   pipx upgrade poetry
   ```

   This command checks for the latest version of Poetry and upgrades it
   if necessary. If Poetry is already at the latest version, you'll see
   a message like:

   ```bash
   poetry is already at latest version 1.7.0 (location: /Users/username/.local/pipx/venvs/poetry)
   ```

### References and Resources

- For detailed instructions on installing Poetry with `pipx`, refer to
  the [official Poetry installation
  guide](https://python-poetry.org/docs/#installing-with-pipx).
- To deepen your understanding of how Poetry can streamline your Python
  project's dependency management, check out this comprehensive article
  on [Dependency Management With Python
  Poetry](https://realpython.com/dependency-management-python-poetry/).

By following these steps, you ensure that Poetry, a crucial tool for
Python project management, is correctly installed and maintained in your
development environment. This approach not only leverages the isolation
benefits of `pipx` but also keeps your toolchain up-to-date and
efficient.

## **✅** Creating a Python Virtual Environment

In modern Python development, managing dependencies and project
environments efficiently is crucial. Poetry excels in this aspect,
providing an elegant and streamlined way to handle project dependencies.
With a `pyproject.toml` file already in place, our project is primed for
leveraging Poetry's capabilities. This section guides you through
setting up a Python virtual environment using Poetry, ensuring that all
dependencies are neatly organized and isolated. This process not only
simplifies dependency management but also aligns with best practices for
Python development, making your project more maintainable and
collaborative-friendly. Let’s walk through the steps to create this
virtual environment and get your project's dependencies up and running.

1. **Check the Python Environment**: It's important to ensure that
   Poetry is using the correct Python environment. Use the `poetry env
   info` command to verify the Python version. If it's not the one you
   need, specify the correct version for Poetry:

   ```zsh
   poetry env use 3.10.4
   ```

   Replace `3.10.4` with your desired Python version.

2. **Install Dependencies with Poetry**: Navigate to the root of your
   project (where `pyproject.toml` is located) and run the following
   command:

   ```shellell
   poetry install
   ```

   This will create a virtual environment and install all the
   dependencies defined in your `pyproject.toml` file. If you've
   configured Poetry to use a specific Python version with `pyenv`, it
   will use that version for the virtual environment.

3. **Activate the Virtual Environment**: To activate the virtual
   environment that Poetry created, use:

   ```shellell
   poetry shell
   ```

   This command will spawn a shell with the virtual environment
   activated, which means you can now run Python and any scripts or
   tools within the context of this environment.

4. **Verify Installation**: To confirm that all dependencies are
   correctly installed, list the installed packages with:

   ```shellell
   poetry show
   ```

   Alternatively, test your project's functionality to ensure everything
   is running smoothly.

Your virtual environment is now set up and ready for development. This
isolation is key for maintaining the integrity of your project and
ensuring that it remains consistent across different machines and
setups.

To manage your Poetry environments:

- To view existing environments, run:

```shellell
poetry env list
```

To deactivate the virtual environment, you can run:

```shellell
exit
```

To activate a Poetry-managed virtual environment, you have a couple of
options depending on how you prefer to work:

1. **Using `poetry shell`**:

   - This command spawns a new shell subprocess, which will activate the
     virtual environment. To use this method, just run:

     ```shell
     poetry shell
     ```

2. **Using `poetry run`**:

   - If you want to run a single command within the virtual environment
     without spawning a new shell, you can prefix your command with
     `poetry run`. For example:

     ```shell
     poetry run python
     ```

   - This will execute the Python interpreter within the context of the
     virtual environment.

3. **Sourcing the Activate Script**:

   - Poetry creates a virtual environment in a standard location. You
     can source the activate script directly to activate the environment
     in your current shell without creating a sub-shell.

   - First, find out the path to the virtual environment by running:

     ```shell
     poetry env info --path
     ```

   - Then, source the `activate` script in the environment's bin
     directory (on Unix systems) or `Scripts` directory (on Windows).
     For Unix systems, it would look like this:

     ```shell
     source /path/to/virtualenv/bin/activate
     ```

     Replace `/path/to/virtualenv` with the actual path output by the
     `poetry env info --path` command.

Once activated, your shell prompt might change to indicate that the
virtual environment is active, and you can then run Python and other
commands in the context of that environment. When you're finished, you
can deactivate the environment by typing `exit` if you used `poetry
shell`, or by running the `deactivate` command if you sourced the
`activate` script.

## **✅** Automatic Activation of Poetry Virtual Environment

To streamline your development workflow in Visual Studio Code using the
Dev Container extension, you can configure VS Code to automatically
recognize and use the Poetry-managed virtual environment for your
project. This setup ensures that every time you open your container, the
correct Python interpreter and tools from your virtual environment are
readily available. Here's a detailed guide on how to achieve this:

### Retrieving the Path to the Poetry Virtual Environment

1. **Obtain the Virtual Environment Path**: First, you need to find the
   path to the virtual environment created by Poetry. Open the container
   in VS Code and run the following command in the terminal:

   ```bash
   poetry env info --path
   ```

   This command will output the path to your virtual environment,
   something like:

   ```bash
   /home/vscode/.cache/pypoetry/virtualenvs/projectblack-sI2m5zhp-py3.10
   ```

### Configuring VS Code to Use the Poetry Virtual Environment

2. **Update the `.vscode/settings.json` File**: With the path to your
   virtual environment at hand, you'll need to update the
   `.vscode/settings.json` file in your project. This file allows you to
   customize your VS Code environment settings.

3. **Set the Default Python Interpreter**: Add the following
   configuration to your `settings.json` file. This setting informs VS
   Code to use the Python interpreter from your Poetry virtual
   environment by default:

   ```json
   "python.defaultInterpreterPath": "/home/vscode/.cache/pypoetry/virtualenvs/myaiproject-sI2m5zhp-py3.10"
   ```

4. **Configure Additional Tools (Optional)**: If you're using other
   tools like `ruff` (a Python linter), you may also want to configure
   these tools to use the binaries from your virtual environment. Add
   the following settings to your `settings.json`:

   ```json
   "ruff.path": [
       "/home/vscode/.cache/pypoetry/virtualenvs/myaiproject-sI2m5zhp-py3.10/bin/ruff"
   ],
   "ruff.interpreter": [
       "/home/vscode/.cache/pypoetry/virtualenvs/myaiproject-sI2m5zhp-py3.10/bin/python"
   ],
   ```

By following these steps, you effectively tell VS Code to automatically
use the Python interpreter and tools from the Poetry-managed virtual
environment every time you open your container. This setup simplifies
your workflow, ensuring that you're always working within the right
context with all necessary dependencies at hand.

⚡⚡ **Important Note:** Before start developing in container, please
ensure that Docker Desktop is up and running on your system.⚡⚡

## **✅** Exiting Development Containers in VS Code

To stop working inside a development container and return to your local
environment using the VS Code Dev Container extension, follow these
simple steps:

1. In the VS Code window that is connected to your Dev Container, locate
   the green bottom-left corner that indicates you are connected to a
   remote environment.

2. Click on it to reveal the remote connection options.

3. Select the "Close Remote Connection" option, as shown in the provided
   image.

> Notice that there you have available the "Reopen in Container" option too.

This will close the remote connection and return you to your local VS
Code environment.

**Note**: If you want to stop the container itself, you can do so using
Docker commands in the terminal:
   - To stop the container: `docker stop <container-name-or-id>`
   - To remove the container: `docker rm <container-name-or-id>`

Alternatively, you can use the Docker Desktop interface to stop and
remove containers.

## Conclusion

With the environment now fully set up and ready, you're all set to dive
into Python development. Whether you're writing scripts or exploring
data in Jupyter notebooks, this environment is designed to support and
enhance your development process.

This setup not only fosters a productive development experience but also
ensures that your projects are developed within a controlled and
consistent setting. We encourage you to explore the capabilities of this
environment, leverage the tools at your disposal, and enjoy the
streamlined workflow that comes with a well-configured development
platform.

Happy coding!
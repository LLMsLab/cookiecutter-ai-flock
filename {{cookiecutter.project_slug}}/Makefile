SHELL := /bin/bash
.ONESHELL:
.DEFAULT_GOAL=help

#-----------------------------------------------------------------------
# Conda virtual environments
#-----------------------------------------------------------------------
# https://gist.github.com/atifraza/b1a92ae7c549dd011590209f188ed2a0
CLONE_NAME ?= $(shell bash -c 'read -p "CloneName: " CloneName; echo $$CloneName')

conda_list: # List existing Conda virtual environments
	@conda env list

conda_create: # Create Conda virtual environment with a specific Python version
	@conda create --name {{cookiecutter.environment_name}} python=3.10.11

conda_install: # Install dependencies in Conda env from requirements.txt using pip
	@conda pip install -r requirements.txt

conda_remove: # Remove a Conda virtual environment
	@conda env remove --name {{cookiecutter.environment_name}}

conda_export: # Export the current environment's packages to an environment.yml file
	@conda env export > environment.yml

conda_create_from_file: # Create a Conda environment from an environment.yml file
	@conda env create -f environment.yml

conda_update_from_file: # Update the Conda environment from an environment.yml file
	@conda env update -f environment.yml --prune

conda_packages: # List packages in the active Conda environment
	@conda list

conda_clean: # Clean unused packages and cache from Conda
	@conda clean --all

conda_clone: # Clone an existing Conda environment to a new one
	@conda create --name $(CLONE_NAME) --clone {{cookiecutter.environment_name}}

conda_update: # Update all packages in the active Conda environment
	@conda update --all

#-----------------------------------------------------------------------
# Poetry- Python dependency management and packaging
#-----------------------------------------------------------------------
PKG ?= $(shell bash -c 'read -p "PackageName: " PackageName; echo $$PackageName')
GRP ?= $(shell bash -c 'read -p "GroupName: " GroupName; echo $$GroupName')

poetry_install: # Install Poetry on the system
	@echo "Installing Poetry..."
	curl -sSL https://install.python-poetry.org | python3 -

poetry_setup_path: # Add Poetry's bin directory to PATH environment variable
	@echo "Setting up Poetry PATH..."
	echo 'export PATH="/home/azureuser/.local/bin:$$PATH"' >> ~/.bashrc
	source ~/.bashrc

poetry_verify: # Verify that Poetry is correctly installed
	@echo "Verifying Poetry installation..."
	poetry --version

poetry_dependencies: # Install project dependencies using Poetry
	@echo "Installing project dependencies with Poetry..."
	@poetry install

poetry_update: # Update project dependencies
	@echo "Updating project dependencies..."
	@poetry update

poetry_check: # Check for consistency between pyproject.toml and poetry.lock
	@echo "Checking for consistency..."
	@poetry check

poetry_add: # Add a new regular dependency
	@echo "Adding a new dependency..."
	@poetry add $(PKG)

poetry_add_dev: # Add a new development dependency
	@echo "Adding a new dependency..."
	@poetry add --dev $(PKG)

poetry_add_group: # Add a new dependency to a specific group
	@echo "Adding a new dependency..."
	@poetry add $(PKG) --group=$(GRP)

poetry_remove: # Remove a regular dependency
	@echo "Removing a dependency..."
	@poetry remove $(PKG)

poetry_remove_dev: # Remove a development dependency
	@echo "Removing a dependency..."
	@poetry remove --dev $(PKG)

poetry_remove_group: # Remove a dependency from a specific group
	@echo "Removing a dependency..."
	@poetry remove $(PKG) --group=$(GRP)

poetry_build: # Build the project package
	@echo "Building the project..."
	@poetry build

poetry_publish: # Publish the project to PyPI
	@echo "Publishing the project..."
	@poetry publish --build

poetry_run: # Run the main script of the project
	@echo "Running the project..."
	@poetry run python main.py

poetry_test: # Run tests using pytest (assuming pytest is a dependency)
	@echo "Running tests..."
	@poetry run pytest

poetry_show: # Show project dependencies
	@echo "Listing project dependencies..."
	@poetry show

#-----------------------------------------------------------------------
# Pip
#-----------------------------------------------------------------------
PKG ?= $(shell bash -c 'read -p "PackageName: " PackageName; echo $$PackageName')

pip_install: # Install packages from requirements.txt
	@echo "Installing packages from requirements.txt..."
	@pip install -r requirements.txt

pip_upgrade_all: # Upgrade all installed pip packages
	@echo "Upgrading all installed pip packages..."
	@pip freeze | cut -d = -f 1 | xargs pip install -U

pip_uninstall: # Uninstall a specific pip package
	@echo "Uninstalling package..."
	@pip uninstall -y $(PKG)

pip_show: # Show details of a specific pip package
	@echo "Showing details for package..."
	@pip show $(PKG)

pip_outdated: # List outdated pip packages
	@echo "Listing outdated pip packages..."
	@pip list --outdated

pip_install_pkg: # Install a specific pip package
	@echo "Installing package..."
	@pip install $(PKG)

pip_list: # List all installed pip packages and their versions
	@echo "Listing all installed pip packages..."
	@pip freeze

pip_check: # Check for any dependency conflicts among installed pip packages
	@echo "Checking for pip dependency conflicts..."
	@pip check

pip_search: # Search for a pip package
	@echo "Searching for package..."
	@pip search $(PKG)

#-----------------------------------------------------------------------
# Make src a python package
#-----------------------------------------------------------------------
src_package: # Make the src folder a Python package
	@pip install -e .

#-----------------------------------------------------------------------
# Git
#-----------------------------------------------------------------------
COMMIT_MSG ?= $(shell bash -c 'read -p "Message: " Message; echo $$Message')
REPOSITORY_URL ?= $(shell bash -c 'read -p "RepositoryURL: " RepositoryURL; echo $$RepositoryURL')

git_init_repo: # Initialize a new Git repository
	@echo "Initializing Git repository..."
	@git init

git_set_default_branch: # Set the default branch to 'development'
	@echo "Setting default branch to 'development'..."
	@git config --global init.defaultBranch development

git_add_files: # Add files to the Git staging area
	@echo "Adding files to the repository..."
	@git add .

git_commit_files: # Commit the staged files with a message
	@echo "Committing the files..."
	@git commit -m "$(CLONE_NAME)"

git_add_remote: # Add a remote repository
	@echo "Adding a remote repository (if applicable)..."
	@git remote add origin $(EPOSITORY_URL) || echo "Remote 'origin' already exists or repository URL not provided."

git_push_remote: # Push commits to the remote repository
	@echo "Pushing to the remote repository (if applicable)..."
	@git push -u origin master || echo "Failed to push. Ensure remote 'origin' is set and accessible."

git_init: git_navigate git_init-repo git_add-files git_commit-files git_add-remote git_push-remote # Complete Git initialization
	@echo "Git initialization complete!"

git_show_branches: # Display the current branches in the repository
	@echo "Listing all branches..."
	@git branch

#-----------------------------------------------------------------------
# Essential Bash tools for NLP tasks (Ubuntu/Debian-based distributions)
#-----------------------------------------------------------------------
PACKAGES := make tree grep sed awk cut sort uniq wc tr paste split cat \
            head tail find xargs tee parallel curl wget jq htop tmux \
            screen git ncdu tldr csvkit rename terraform perl vim join \
            pandoc lsof pdftotext ripgrep more less zip unzip tar gzip \
            gunzip bzip2 xz rsync dd fdupes top ps pgrep pkill at

bash_install_ds: # Install essential Bash tools for data science and general tasks
	@sudo apt update
	@for package in $(PACKAGES); do \
		sudo apt install -y $$package; \
	done

#-----------------------------------------------------------------------
# CSpell Checker: Extract terms from Python libraries listed in requirements.txt
#-----------------------------------------------------------------------
cspell_dictionary: # Extract terms from Python libraries for CSpell dictionary
	@python src/{{cookiecutter.package_name}}/utils.py

#-----------------------------------------------------------------------
# Using pytest for testing
#-----------------------------------------------------------------------
test: # Run tests
	@pytest -vvv

#-----------------------------------------------------------------------
# Create new GitHub labels
#-----------------------------------------------------------------------
gh_create_labels: # Create new GitHub labels
	@gh label create ask --description "Define and scope problem and solution" --color c9ecff
	@gh label create explore --description "Explore and document data to increase understanding" --color f0f29b
	@gh label create experiment --description "Build features and train models" --color 8569c6
	@gh label create data --description "Get and transform data" --color 1c587c
	@gh label create model --description "Prepare model for deployment" --color 0b4e82
	@gh label create deploy --description "Register, package, and deploy model" --color f79499
	@gh label create communicate --description "Write reports, create dashboards, summarize findings, etc." --color f9f345
	@gh label create succeeded --description "This was successful" --color 67d157
	@gh label create failed --description "This didn't go as hoped" --color c2021c
	@gh label create onhold --description "Still seems promising, but let's revisit later" --color ffd04f
	@gh label create blocked --description "Blocked due to lack of access to data, resources, environment, etc." --color ed9a53

#-----------------------------------------------------------------------
# Pre-commit
#-----------------------------------------------------------------------
# Prompt for user input fileloc as for example:
# data/interim/cnt_cli_mapping_lana.csv
MESSAGE ?= $(shell bash -c 'read -p "Message: " message; echo $$message')
pre_commit_install: # Install the git hook scripts
	@pre-commit install
pre_commit_no_verify: # Git commit without the pre-commit hook
	@git commit -m "$(FILELOC)" --no-verify

#-----------------------------------------------------------------------
# Create docs
#-----------------------------------------------------------------------
docs_new: # Create a new project
	@mkdocs new {{cookiecutter.project_slug}}
docs_serve: # Start the live-reloading docs server
	@mkdocs serve
docs_build: # Build the documentation site
	@mkdocs build
docs_deploy: # Deploy Your Documentation to GitHub
	@mkdocs gh-deploy

#-----------------------------------------------------------------------
# Large datasets view
#-----------------------------------------------------------------------
# Prompt for user input fileloc as for example:
# data/interim/cnt_cli_mapping_lana.csv
FILELOC ?= $(shell bash -c 'read -p "Fileloc: " fileloc; echo $$fileloc')
data_view: # View first 10 lines of a large dataset
	@clear
	@head -10 $(FILELOC) | code -

#-----------------------------------------------------------------------
# Convert a jupyter notebook with the extension .ipynb into a markdown
#-----------------------------------------------------------------------
# Prompt for user input fileloc as for example:
# data/interim/filename.ipynb
FILELOC ?= $(shell bash -c 'read -p "Fileloc: " fileloc; echo $$fileloc')
jupyter_to_mk: # Convert Jupyter Notebook into Markdown
	@clear
	@jupyter nbconvert --to markdown $(FILELOC)

#-----------------------------------------------------------------------
# Hadoop
#-----------------------------------------------------------------------
# For example to monitor and kill a Spark running application
hadoop_top: # Hadopp cluster usage tool
	@yarn top
# Prompt for user input fileloc as for example.
# Enter your application ID for example:
# application_1589279798049_199286
APPLICATIONID ?= $(shell bash -c 'read -p "Application ID: " app; echo $$app')
hadoop_kill: # Kill Hadoop application
	@yarn application -kill $(APPLICATIONID)

#-----------------------------------------------------------------------
# Monitor and end background running jobs
#-----------------------------------------------------------------------
# Prompt for user input PID: Process ID (PID) as for example:
# 74265
PID ?= $(shell bash -c 'read -p "PID: " pid; echo $$pid')
job_monitor: # Monitor porcess
	@ps -aux | head -1; ps -aux | grep $(PID)
job_terminate: # Terminate the job
	@kill $(PID)
job_kill: # Force kill the job
	@kill -9 $(PID)

#-----------------------------------------------------------------------
# Help
#-----------------------------------------------------------------------
help: # Show this help
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; \
	{printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


SHELL := /bin/bash
.ONESHELL:
.DEFAULT_GOAL=help

#-----------------------------------------------------------------------
# Poetry- Python dependency management and packaging
#-----------------------------------------------------------------------
PKG ?= $(shell bash -c 'read -p "PackageName: " PackageName; echo $$PackageName')
GRP ?= $(shell bash -c 'read -p "GroupName: " GroupName; echo $$GroupName')

poetry_install: # Install Poetry on the system
	@echo "Installing Poetry..."
	curl -sSL https://install.python-poetry.org | python3 -

poetry_verify: # Verify that Poetry is correctly installed
	@echo "Verifying Poetry installation..."
	poetry --version

poetry_dependencies: # Install project dependencies using Poetry
	@echo "Installing project dependencies with Poetry..."
	@poetry install

poetry_shell: # Activate the Poetry virtual environment
	@echo "Activating the Poetry virtual environment..."
	@poetry shell

# Note: This target will only provide instructions to the user.
poetry_exit: # Instructions to deactivate the Poetry virtual environment
	@echo "To deactivate the Poetry virtual environment, simply type 'exit' and press Enter."

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

poetry_env_info: # Display Poetry environment information
	@echo "Fetching Poetry environment information..."
	@poetry env info

poetry_env_path: # Get the path to the Poetry virtual environment
	@echo "Fetching Poetry environment information..."
	@poetry env info --path



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
# CSpell Checker: Extract terms from Python libraries listed in requirements.txt
#-----------------------------------------------------------------------
cspell_dictionary: # Extract terms from Python libraries for CSpell dictionary
	@python src/{{cookiecutter.package_name}}/utils.py

#-----------------------------------------------------------------------
# Create docs
#-----------------------------------------------------------------------
docs_new: # Create a new project
	@mkdocs new {{cookiecutter.project_slug}}
docs_serve: # Start the live-reloading docs server
	@mkdocs serve
docs_serve_alt_port: # Start the live-reloading docs server on an alternative port (macOS)
	@mkdocs serve --dev-addr=127.0.0.1:8001
docs_kill_port: # Kill the process occupying port 8000 (macOS)
	@lsof -ti :8000 | xargs kill -9
docs_build: # Build the documentation site
	@mkdocs build
docs_deploy: # Deploy Your Documentation to GitHub
	@mkdocs gh-deploy

#-----------------------------------------------------------------------
# Help
#-----------------------------------------------------------------------
help: # Show this help
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; \
	{printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


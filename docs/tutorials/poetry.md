# Managing Dependencies with Poetry in Cookiecutter RAG

Welcome to the guide on managing Python dependencies using Poetry in the
context of the Cookiecutter RAG (Retrieval-Augmented Generation)
template. This tutorial assumes that you've already set up your project
using the Cookiecutter template, installed Poetry, and activated your
Conda virtual environment.

::: info This guide is intended for users who have already completed the
initial setup steps for installing Poetry, creating a Conda virtual
environment, and installing initial dependencies.
:::

## Table of Contents

- [Managing Dependencies with Poetry in Cookiecutter RAG](#managing-dependencies-with-poetry-in-cookiecutter-rag)
  - [Table of Contents](#table-of-contents)
  - [Adding New Dependencies](#adding-new-dependencies)
    - [Standard Dependencies](#standard-dependencies)
    - [Development Dependencies](#development-dependencies)
  - [Updating Existing Dependencies](#updating-existing-dependencies)
    - [Update a Specific Package](#update-a-specific-package)
    - [Update All Packages](#update-all-packages)
  - [Removing Unwanted Dependencies](#removing-unwanted-dependencies)
  - [Listing Project Dependencies](#listing-project-dependencies)
    - [List All Dependencies](#list-all-dependencies)
    - [List a Specific Dependency](#list-a-specific-dependency)
  - [Locking the Dependency Versions](#locking-the-dependency-versions)
  - [Troubleshooting Common Issues](#troubleshooting-common-issues)
    - [Resolving Dependency Conflicts](#resolving-dependency-conflicts)
    - [Debugging Environment Issues](#debugging-environment-issues)

---

## Adding New Dependencies

### Standard Dependencies

To add a new package to your project, execute the following command:

```bash
poetry add <package-name>
```

::: tip Example
To add the `numpy` package, run:

```bash
poetry add numpy
```
:::

### Development Dependencies

For packages that are only required during development and not in
production, add them as development dependencies:

```bash
poetry add --dev <package-name>
```

::: tip Example
To add `pytest` as a development dependency, run:

```bash
poetry add --dev pytest
```
:::

---

## Updating Existing Dependencies

### Update a Specific Package

To update a specific package to its latest version, use:

```bash
poetry update <package-name>
```

::: tip Example
To update the `numpy` package, run:

```bash
poetry update numpy
```
:::

### Update All Packages

To update all dependencies to their latest versions, execute:

```bash
poetry update
```

---

## Removing Unwanted Dependencies

To remove a package from your project, use the following command:

```bash
poetry remove <package-name>
```

::: tip Example
To remove the `numpy` package, run:

```bash
poetry remove numpy
```
:::

---

## Listing Project Dependencies

### List All Dependencies

To list all installed packages along with their versions, use:

```bash
poetry show
```

### List a Specific Dependency

To view details about a specific package, use:

```bash
poetry show <package-name>
```

---

## Locking the Dependency Versions

The `poetry.lock` file ensures that the same versions of dependencies
are used across different setups. If you modify `pyproject.toml`, it's
good practice to update `poetry.lock`:

```bash
poetry lock
```

---

## Troubleshooting Common Issues

### Resolving Dependency Conflicts

If you encounter version conflicts among dependencies, simulate the
update process to identify issues:

```bash
poetry update --dry-run
```

### Debugging Environment Issues

To check which Python interpreter Poetry is using, run:

```bash
poetry env info
```

::: warning
If you encounter issues, consult the [Poetry
documentation](https://python-poetry.org/docs/) for advanced
troubleshooting steps.
:::

That's it! You're now equipped to manage your Python dependencies using
Poetry within the Cookiecutter RAG template. Happy coding!
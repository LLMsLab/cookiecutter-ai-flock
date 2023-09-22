# Managing Dependencies with Poetry in Your Project

Poetry is a powerful package management tool that simplifies dependency
management in Python projects. With the Cookiecutter template, you
already have a pre-configured setup that makes it easy to manage your
project's dependencies. This guide will walk you through how to
effectively use Poetry in various scenarios, such as adding, updating,
and removing dependencies.
## Adding New Dependencies

!!! note
    The Cookiecutter template comes with a set of pre-configured dependencies specified in the `pyproject.toml` file. However, you may need to add additional packages as your project grows.

### Adding Standard Dependencies

To add a new package to your project, use the `poetry add` command:

```bash
poetry add <package-name>
```

!!! example "Adding NumPy as a Dependency"
    To add `numpy` to your project, run the following command:

    ```bash
    poetry add numpy
    ```

### Adding Development Dependencies

For packages needed only during development, you can add them as
development dependencies:

```bash
poetry add --dev <package-name>
```

!!! example "Adding Pytest as a Development Dependency"
    To add `pytest` as a development dependency, run:

    ```bash
    poetry add --dev pytest
    ```

## Updating Existing Dependencies

!!! info "Keeping Dependencies Up-to-date"
    It's a good practice to keep your dependencies updated to benefit from bug fixes, performance improvements, and new features.

### Updating a Specific Dependency

To update a specific package, use the `poetry update` command:

```bash
poetry update <package-name>
```

!!! example "Updating NumPy"
    To update `numpy` to the latest version, run:

    ```bash
    poetry update numpy
    ```

### Updating All Dependencies

To update all dependencies to their latest versions:

```bash
poetry update
```

## Removing Unneeded Dependencies

!!! warning "Clean Up Unnecessary Packages"
    Removing unused dependencies can help keep your project clean and reduce potential security risks.

To remove a package, use the `poetry remove` command:

```bash
poetry remove <package-name>
```

!!! example "Removing NumPy"
    To remove `numpy` from your project, run:

    ```bash
    poetry remove numpy
    ```

## Listing Project Dependencies

!!! info "Know What You're Using"
    It's useful to periodically review the list of installed packages and their versions.

To list all installed packages and their versions, run:

```bash
poetry show
```

## Locking Dependencies

!!! note
    Ensuring that everyone working on the project uses the same versions of dependencies is crucial for maintaining a consistent development environment. This is where the `poetry.lock` file comes into play.

### Why Use `poetry.lock`?

The `poetry.lock` file is generated when you first run `poetry install`
or `poetry update`. It contains the exact versions of each dependency
that your project relies on. By committing this file to your version
control system (e.g., GitHub), you ensure that all team members and
deployment environments use the same versions of dependencies, thereby
reducing "it works on my machine" issues.

### How to Lock Dependencies

To generate or update the `poetry.lock` file, you can run:

```bash
poetry lock
```

This will read your `pyproject.toml` file, resolve dependencies, and
generate a new `poetry.lock` file with the exact package versions.

### Committing to Version Control

To ensure that everyone is on the same page, both `pyproject.toml` and
`poetry.lock` should be committed to your version control system.

!!! info "What to Commit?"
    - **Commit `pyproject.toml`**: This file contains the list of dependencies your project needs, without specifying the exact versions. It provides the flexibility to update packages within defined version ranges.
    
    - **Commit `poetry.lock`**: This file locks the versions of all dependencies, ensuring that everyone uses the same versions. It should be committed to version control to maintain consistency across all environments.

By committing both files, you strike a balance between flexibility and
consistency. The `pyproject.toml` allows for updates within specified
ranges, while the `poetry.lock` ensures that these updates are
consistent across all environments.

!!! warning "Never Edit `poetry.lock` Manually"
    The `poetry.lock` file is auto-generated and should never be edited
    manually. Always use Poetry commands to update it.

## Conclusion

Locking dependencies is an essential practice in collaborative
development. It ensures that all contributors and environments are
aligned, reducing potential bugs and inconsistencies. With Poetry and
the Cookiecutter template, managing these dependencies becomes a
straightforward task.

## Troubleshooting and Tips

### Resolving Dependency Conflicts

If you encounter dependency conflicts, you can use the `poetry update
--dry-run` command to simulate the update process:


```bash
poetry update --dry-run
```

### Debugging Environment Issues

If you suspect environment-related issues, you can check which Python
interpreter Poetry is using:

```bash
poetry env info
```

## Conclusion

Poetry simplifies dependency management, making it easier to maintain a
clean and efficient project. With the Cookiecutter template, you have a
head start in managing your project's dependencies effectively. Whether
you're adding new packages, updating existing ones, or cleaning up
unnecessary dependencies, Poetry has got you covered.

## Further Reading and Resources

To deepen your understanding of Poetry and its capabilities, you may
find the following resources helpful:

- [Real Python's Guide on Dependency Management with Poetry](https://realpython.com/dependency-management-python-poetry/)
- [Official Poetry Documentation](https://python-poetry.org/docs/)

These references provide comprehensive tutorials and documentation that
can help you become more proficient in managing Python dependencies with
Poetry. Whether you're a beginner or an experienced developer, these
resources offer valuable insights into best practices and advanced
features.
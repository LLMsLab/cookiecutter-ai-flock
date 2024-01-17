# Ruff: Python Linting for Clean and Compliant Code

Ruff is a high-performance linter for Python that swiftly evaluates and
enhances the quality of your code. With an emphasis on speed and
practicality, Ruff assists developers in maintaining consistent coding
styles and standards within Python scripts and Jupyter notebooks alike.

## Getting Started with `ruff check`

The `ruff check` command forms the backbone of Ruff, providing a quick
and thorough analysis of your Python files to identify and flag
potential issues.

### Standard Linting Procedure

To initiate linting, utilize the following command pattern:

```bash
ruff check path/to/file_or_directory
```

For example, to lint a service component within your application, you
might use:

```bash
ruff check project_directory/services/
```

### Automated Error Correction with `--fix`

Ruff's auto-fix capability streamlines the error correction process by
automatically resolving numerous common linting issues:

```bash
ruff check --fix path/to/file_or_directory
```

For instance, to apply auto-fixes to an entire application directory:

```bash
ruff check --fix project_directory/
```

## Utilizing Nursery Rules with `--preview`

To explore beyond standard linting rules and include experimental ones,
use the `--preview` flag:

```bash
ruff check --preview --fix path/to/file_or_directory
```

This is particularly useful when linting individual files that may
leverage cutting-edge Python features:

```bash
ruff check --preview --fix project_directory/utils/advanced_parser.py
```

### Understanding Ruff's Rules

An extensive explanation of Ruff's rules, both standard and nursery, is
available at the [Ruff Rules
Documentation](https://docs.astral.sh/ruff/rules/).

### Example: Linting a Python Script

Let's say you have a Python script at
`project_directory/services/parser.py`. To lint this script, apply
standard and nursery rules, and fix issues:

```bash
ruff check --preview --fix project_directory/services/parser.py
```

### Example: Working with Jupyter Notebooks

For a Jupyter notebook, `analysis.ipynb`, located in the same directory:

```bash
ruff check --preview --fix project_directory/notebooks/analysis.ipynb
```

Ruff will lint the notebook and provide feedback or fixes in a format
compatible with Jupyter's code cells.

## Real-World Example and Terminal Output

Here's a real-world example showcasing the execution of Ruff and the
corresponding terminal output:

```python
# Non-compliant code with E201
def my_function(): # Violates "undocumented-public-function"
    my_list = [1, 2, 3, 4 ] # Violates "whitespace-after-open-bracket" and "whitespace-before-close-bracket"
    long_string = "This is a very long string..." # Violates "line-too-long"
```

Assuming you're working on `project_directory/models/data_model.py` with
some issues, you run:

```bash
ruff check --preview --fix project_directory/models/data_model.py
```

The terminal output might look like this:

```bash
project_directory/models/data_model.py:1:1: D100 Missing docstring in public module
project_directory/models/data_model.py:5:10: E231 missing whitespace after ','
project_directory/models/data_model.py:7:1: E302 expected 2 blank lines, found 1
Found 5 errors (3 fixed, 2 remaining).
```

Each line of the output directs you to the specific issue within your
code, providing guidance on the nature of the problem and its location.

!!! tip "Quick Code Navigation"
    In integrated development environments like VS Code, you can use the command-click (or control-click on some systems) feature on the path in the terminal output to jump directly to the problematic line, facilitating quick fixes.

!!! tip "Handling Nursery Rule Warnings"
    If you encounter a warning like:

    ```plaintext
    warning: Selection of nursery rule `E201` without the `--preview` flag is deprecated.
    ```

    This indicates that your `pyproject.toml` includes nursery rules, which are experimental and require the `--preview` flag during execution. In our configuration, where we utilize a set of 50 rules that encompasses several nursery rules, it's essential to always use the `--preview` flag. This ensures that Ruff considers all specified rules, including the experimental ones, to maintain the integrity of your code linting strategy.

    Always run Ruff with the `--preview` flag to avoid deprecation warnings and adhere to the complete set of rules defined for your project:

    ```bash
    ruff check --preview path/to/file_or_directory
    ```

    By doing so, you'll leverage the full capabilities of Ruff, keeping your codebase up to date with both standard and progressive linting practices.

## Advanced Integration of Ruff in Python Development

Continuing from the foundational `ruff check` usage, let's delve into
how Ruff can be integrated into more advanced development workflows.
This includes setting up pre-commit hooks, utilizing GitHub Actions for
continuous integration, and customizing Ruff to adhere to a specific set
of rules defined in a project's `pyproject.toml`.

## Pre-commit Hooks for Ruff

Pre-commit hooks are a powerful way to ensure that code is automatically
linted before it's committed to your repository, helping to maintain
code quality and consistency.

### Setting Up Pre-commit Hooks

To utilize Ruff as a pre-commit hook, you'll need to add a configuration
to your `.pre-commit-config.yaml` file:

```yaml
repos:
-   repo: https://github.com/charliermarsh/ruff
    rev: ''  # Use the tag for the desired release
    hooks:
    - id: ruff
```

This configuration will instruct the pre-commit tool to run Ruff against
staged files whenever `git commit` is executed.

### Example: Pre-commit Hook in Action

When you attempt to commit, the hook will run, and you might see output
like this if issues are found:

```bash
pre-commit running: ruff
project_directory/services/parser.py:10:1: E302 expected 2 blank lines, found 1

Failed. Ruff found linting errors. Review the issues and commit again.
```

## GitHub Actions for Continuous Linting

GitHub Actions can be set up to run Ruff on every push or pull request
to ensure that all contributions meet your coding standards.

## GitHub Actions Integration with Ruff

To ensure the codebase maintains high-quality standards and adheres to
our defined linting rules, we use GitHub Actions to automate the linting
process. This section provides an up-to-date guide on how Ruff is
integrated within our CI/CD pipeline.

### GitHub Actions Workflow for Ruff Linting

Our GitHub Actions workflow is configured to run Ruff on every push and
pull request. The action checks the code against a set of 50 rules,
including several nursery rules, ensuring all contributions are up to
the linting standards before merging into the main branch.

#### Workflow Setup

The workflow is defined in the `.github/workflows/ruff.yaml` file and
consists of the following steps:

1. **Checkout Code**: Retrieves the code from the current repository
   branch that triggered the action.
2. **Set up Python**: Prepares the Python environment using the version
   specified, ensuring compatibility with Ruff.
3. **Install Ruff**: Installs Ruff, making it available for linting.
4. **Check Code with Ruff**: Runs Ruff against the specified directories
   (`src/` and `notebooks/`) using the `--preview` flag to include
   nursery rules from our `pyproject.toml`.
5. **Fail if Linting Errors Are Detected**: If Ruff detects any linting
   errors, the action outputs an error message and fails, prompting the
   user to lint their code locally and resolve the issues before pushing
   to the repository.

#### Ruff Linting Action Definition

Here is the code snippet for the GitHub Actions workflow:

```yaml
name: Ruff Linter

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9

    - name: Install Ruff
      run: pip install ruff

    - name: Check code with Ruff
      run: ruff check --preview src/ notebooks/


    - name: Fail if linting errors are detected
      run: |
        if ruff check --preview src/ notebooks/
          --quiet | grep -q 'error'; then
          echo "Linting errors detected. Please lint your code locally with Ruff and resolve all issues before pushing."
          exit 1
        else
          echo "No linting errors detected."
        fi
```

With this setup, we do not automatically fix any issues with Ruff in the
GitHub Actions workflow. Instead, we enforce that the code must be
linted locally by the developer. This approach ensures that all team
members are actively involved in maintaining the code quality and are
aware of the coding standards enforced by our Ruff configuration.

### Example: GitHub Action Log for Linting Errors

When a developer pushes code or creates a pull request, the GitHub
Action is triggered to ensure the code meets our linting standards. If
Ruff detects linting issues, the action will fail, and the output in the
GitHub Actions log will resemble the following:

```bash
Run ruff check --preview src/ notebooks/
Linting errors detected. Please lint your code locally with Ruff and resolve all issues before pushing.

project_directory/models/data_model.py:1:1: D100 Missing docstring in public module
project_directory/services/parser.py:5:10: E231 missing whitespace after ','
project_directory/utils/calculations.py:7:1: E302 expected 2 blank lines, found 1
...

Error: Process completed with exit code 1.
```

This log provides detailed feedback about the linting errors found. The
developer is expected to address these issues by running Ruff locally
with the `--preview` flag, ensuring that the code is compliant with our
established set of rules, including nursery rules, before attempting to
push again.

## Customizing Ruff with `pyproject.toml`

Ruff allows for extensive customization of its linting rules through a
`pyproject.toml` file. This enables you to specify which rules to
enable, disable, or configure further.

### Commentary on `pyproject.toml` Configuration

```toml
# pyproject.toml
[tool.ruff]
# We're using a curated set of 50 rules, which you can review and adjust as needed
include = [ ... ]
exclude = [ ... ]
```

The `include` and `exclude` keys allow you to precisely control which
rules Ruff will apply or ignore. This ensures that the linter is aligned
with your project's standards and practices.

## Conclusion

By integrating Ruff with pre-commit hooks and GitHub Actions, and
customizing its behavior with `pyproject.toml`, you can automate and
fine-tune the linting process to fit your project's needs. This ensures
high-quality, clean code that adheres to your defined standards,
ultimately leading to a more robust and maintainable codebase.

Remember, the set of rules within `pyproject.toml` is at the core of
Ruff's operation within your project, and you should review and adapt
these rules to align with your coding principles.

## Further Resources

For more detailed information on using Ruff, customizing rules, and
integrating with your development environment, please refer to the
following:

- [Ruff Official Documentation](https://docs.astral.sh/ruff/)
- [Ruff Rules Documentation](https://docs.astral.sh/ruff/rules/)

Leverage these resources to fully harness the capabilities of Ruff for
your Python projects.









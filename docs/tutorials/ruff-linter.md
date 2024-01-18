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

Selected rules:

| Code | Rule Description                                              | Documentation Link                              |
|------|---------------------------------------------------------------|-------------------------------------------------|
| F401 | Unused imports                                                | [F401](https://docs.astral.sh/ruff/rules/#F401) |
| F402 | Import shadowed by loop var                                   | [F402](https://docs.astral.sh/ruff/rules/#F402) |
| F403 | `from module import *` used                                   | [F403](https://docs.astral.sh/ruff/rules/#F403) |
| F405 | Name may be undefined, or defined from star imports           | [F405](https://docs.astral.sh/ruff/rules/#F405) |
| F601 | Dictionary key literal repeated                               | [F601](https://docs.astral.sh/ruff/rules/#F601) |
| F602 | Dictionary key variable repeated                              | [F602](https://docs.astral.sh/ruff/rules/#F602) |
| F621 | Too many expressions in star-unpacking assignment             | [F621](https://docs.astral.sh/ruff/rules/#F621) |
| F631 | Assert test is a non-empty tuple                              | [F631](https://docs.astral.sh/ruff/rules/#F631) |
| F632 | Use `==` to compare constant literals                         | [F632](https://docs.astral.sh/ruff/rules/#F632) |
| F701 | `break` outside loop                                          | [F701](https://docs.astral.sh/ruff/rules/#F701) |
| F702 | `continue` not properly in loop                               | [F702](https://docs.astral.sh/ruff/rules/#F702) |
| F704 | Yield statement outside of a function                         | [F704](https://docs.astral.sh/ruff/rules/#F704) |
| F706 | `return` statement outside of a function/method               | [F706](https://docs.astral.sh/ruff/rules/#F706) |
| F707 | `except` block not the last exception handler                 | [F707](https://docs.astral.sh/ruff/rules/#F707) |
| F722 | Syntax error in forward annotation                            | [F722](https://docs.astral.sh/ruff/rules/#F722) |
| F811 | Redefinition of unused variable from line                     | [F811](https://docs.astral.sh/ruff/rules/#F811) |
| F821 | Undefined name                                                | [F821](https://docs.astral.sh/ruff/rules/#F821) |
| F841 | Local variable is assigned to but never used                  | [F841](https://docs.astral.sh/ruff/rules/#F841) |
| E101 | Indentation contains mixed spaces and tabs                    | [E101](https://docs.astral.sh/ruff/rules/#E101) |
| E111 | Indentation is not a multiple of four                         | [E111](https://docs.astral.sh/ruff/rules/#E111) |
| E112 | Expected an indented block                                    | [E112](https://docs.astral.sh/ruff/rules/#E112) |
| E113 | Unexpected indentation                                        | [E113](https://docs.astral.sh/ruff/rules/#E113) |
| E114 | Indentation is not a multiple of four (comment)               | [E114](https://docs.astral.sh/ruff/rules/#E114) |
| E115 | Expected an indented block (comment)                          | [E115](https://docs.astral.sh/ruff/rules/#E115) |
| E116 | Unexpected indentation (comment)                              | [E116](https://docs.astral.sh/ruff/rules/#E116) |
| E117 | Over-indented (comment)                                       | [E117](https://docs.astral.sh/ruff/rules/#E117) |
| E201 | Whitespace after '(' or '['                                   | [E201](https://docs.astral.sh/ruff/rules/#E201) |
| E202 | Whitespace before ')' or ']'                                  | [E202](https://docs.astral.sh/ruff/rules/#E202) |
| E203 | Whitespace before ':'                                         | [E203](https://docs.astral.sh/ruff/rules/#E203) |
| E211 | Whitespace before '(' or '['                                  | [E211](https://docs.astral.sh/ruff/rules/#E211) |
| E225 | Missing whitespace around operator                            | [E225](https://docs.astral.sh/ruff/rules/#E225) |
| E231 | Missing whitespace after ',', ';', or ':'                     | [E231](https://docs.astral.sh/ruff/rules/#E231) |
| E251 | Unexpected spaces around keyword / parameter equals           | [E251](https://docs.astral.sh/ruff/rules/#E251) |
| E261 | At least two spaces before inline comment                     | [E261](https://docs.astral.sh/ruff/rules/#E261) |
| E262 | Inline comment should start with '# '                         | [E262](https://docs.astral.sh/ruff/rules/#E262) |
| E265 | Block comment should start with '# '                          | [E265](https://docs.astral.sh/ruff/rules/#E265) |
| E266 | Too many leading '#' for block comment                        | [E266](https://docs.astral.sh/ruff/rules/#E266) |
| E271 | Multiple spaces after keyword                                 | [E271](https://docs.astral.sh/ruff/rules/#E271) |
| E272 | Multiple spaces before keyword                                | [E272](https://docs.astral.sh/ruff/rules/#E272) |
| E273 | Tab after keyword                                             | [E273](https://docs.astral.sh/ruff/rules/#E273) |
| E274 | Tab before keyword                                            | [E274](https://docs.astral.sh/ruff/rules/#E274) |
| E275 | Missing whitespace after keyword                              | [E275](https://docs.astral.sh/ruff/rules/#E275) |
| E401 | Multiple imports on one line                                  | [E401](https://docs.astral.sh/ruff/rules/#E401) |
| E402 | Module level import not at top of file                        | [E402](https://docs.astral.sh/ruff/rules/#E402) |
| E501 | Line too long                                                 | [E501](https://docs.astral.sh/ruff/rules/#E501) |
| E711 | Comparison to None should be 'expr is None'                   | [E711](https://docs.astral.sh/ruff/rules/#E711) |
| E712 | Comparison to True should be 'if cond is True:' or 'if cond:' | [E712](https://docs.astral.sh/ruff/rules/#E712) |
| E713 | Test for membership should be 'not in'                        | [E713](https://docs.astral.sh/ruff/rules/#E713) |
| E714 | Test for object identity should be 'is not'                   | [E714](https://docs.astral.sh/ruff/rules/#E714) |
| E721 | Do not compare types, use 'isinstance()'                      | [E721](https://docs.astral.sh/ruff/rules/#E721) |
| E722 | Do not use bare 'except'                                      | [E722](https://docs.astral.sh/ruff/rules/#E722) |
| E731 | Do not assign a lambda expression, use a def                  | [E731](https://docs.astral.sh/ruff/rules/#E731) |
| I001 | Import block is un-sorted or un-formatted                     | [I001](https://docs.astral.sh/ruff/rules/#I001) |
| I002 | Missing required import                                       | [I002](https://docs.astral.sh/ruff/rules/#I002) |
| N801 | Class name should use CapWords convention                     | [N801](https://docs.astral.sh/ruff/rules/#N801) |
| N802 | Function name should be lowercase                             | [N802](https://docs.astral.sh/ruff/rules/#N802) |
| N803 | Argument name should be lowercase                             | [N803](https://docs.astral.sh/ruff/rules/#N803) |
| N804 | First argument of a class method should be named 'cls'        | [N804](https://docs.astral.sh/ruff/rules/#N804) |
| N805 | First argument of a method should be named 'self'             | [N805](https://docs.astral.sh/ruff/rules/#N805) |
| N806 | Variable in function should be lowercase                      | [N806](https://docs.astral.sh/ruff/rules/#N806) |
| D100 | Missing docstring in public module                            | [D100](https://docs.astral.sh/ruff/rules/#D100) |
| D101 | Missing docstring in public class                             | [D101](https://docs.astral.sh/ruff/rules/#D101) |
| D102 | Missing docstring in public method                            | [D102](https://docs.astral.sh/ruff/rules/#D102) |
| D103 | Missing docstring in public function                          | [D103](https://docs.astral.sh/ruff/rules/#D103) |
| D104 | Missing docstring in public package                           | [D104](https://docs.astral.sh/ruff/rules/#D104) |
| D105 | Missing docstring in magic method                             | [D105](https://docs.astral.sh/ruff/rules/#D105) |
| D106 | Missing docstring in public nested class                      | [D106](https://docs.astral.sh/ruff/rules/#D106) |
| D107 | Missing docstring in __init__                                 | [D107](https://docs.astral.sh/ruff/rules/#D107) |

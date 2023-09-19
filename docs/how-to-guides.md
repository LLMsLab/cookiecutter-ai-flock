# How-to-Guides

## Checking and Installing Essential Bash Tools on Ubuntu

### Introduction

When configuring a new Ubuntu system – be it a server or a workstation –
ensuring that all requisite tools and commands are available is crucial,
especially for tasks involving scripting, development, or data management. This
guide outlines a systematic methodology for ensuring all essential Bash tools
are in place.

### 1. Attempt Direct Installation

Often, the name of the command is identical to the name of the package it
belongs to. Given this, a direct installation attempt for each tool can swiftly
ensure that a large portion of them are installed. Execute the following:

```bash
PACKAGES="make tree grep sed awk cut sort uniq wc tr paste split cat \
head tail find xargs tee parallel curl wget jq htop tmux \
screen git ncdu tldr csvkit rename terraform perl vim join \
pandoc lsof ripgrep more less zip unzip tar gzip \
gunzip bzip2 xz rsync dd fdupes top ps pgrep pkill at"

for package in $PACKAGES; do
    sudo apt install -y $package
done
```

This step, while not exhaustive, will help in getting the common tools up and
running promptly.

### 2. Verify Tool Availability

After attempting a direct installation, it's prudent to check which tools are
actually present. This can be achieved through the script below:

```bash
for package in $PACKAGES; do
    if command -v $package > /dev/null 2>&1; then
        echo "$package is installed."
    else
        echo "$package is NOT installed."
    fi
done
```

This script inspects the availability of each tool by trying to invoke it. If a
tool is accessible, the script confirms its installation; otherwise, it flags it
as missing.

### 3. Addressing Missing Tools

For the tools reported as missing:

1. Try running the tool with the `--version` flag, for instance, `pdftotext
   --version`. 
2. Ubuntu is generally helpful and will suggest the apt package that contains
   the missing tool, if it's available.
3. Proceed with the suggested `sudo apt install [package-name]` command to get
   the tool installed.

An example:

```
Command 'pdftotext' not found, but can be installed with:
sudo apt install poppler-utils
```

Follow the system's advice (`sudo apt install poppler-utils` in this case) to
install the necessary tool.

**Note**: While Ubuntu typically suggests packages for recognized tools, this
might not be the case for all. In such scenarios, a manual lookup on package
repositories or web resources might be necessary.

Certainly! Let's break down and prepare the content for the subsection **3.1 Essential VS Code Extensions** in the How-to-guide:

## How to setting up Black formatter

### **3. Setting Up Your VS Code Environment**

#### **3.1. Essential VS Code Extensions**

Getting your VS Code environment primed for Python development, especially for tasks related to Jupyter notebooks and code formatting, requires the incorporation of a few vital extensions. Here's a straightforward guide to setting up these extensions:

##### **Step 1: Python Extension by Microsoft**

The Python Extension by Microsoft stands out as a must-have. It not only amplifies Python's innate capabilities within VS Code but also seamlessly integrates Jupyter notebook functionalities.

**How to Install**:
1. Open your VS Code.
2. Navigate to the Extensions view by clicking on the square icon in the sidebar or pressing `Ctrl+Shift+X`.
3. In the search bar, type "Python" and look for the one by Microsoft.
4. Click on the install button next to it.

For convenience, you can also directly access the extension on the marketplace using the link below:

[Python Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

##### **Step 2: Jupyter Extension by Microsoft**

With the rise in data science and computational notebooks' popularity, having the Jupyter Extension is a no-brainer. This extension enables features like running cells, visualizing plots, and other Jupyter-specific functionalities within VS Code.

**How to Install**:
1. Still within the Extensions view in VS Code, type "Jupyter" in the search bar.
2. Look for the extension provided by Microsoft.
3. Click on the install button next to it.

Alternatively, use the direct link below for the marketplace:

[Jupyter Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

##### **Step 3: Black Formatter Extension**

Code consistency is paramount, and the Black Formatter Extension ensures just that. Though this extension comes bundled with a specific version of Black, it respects any installed version in your chosen Python environment, as long as it's version 22.3.0 or above. Designed for all actively supported Python versions (3.7 and above), this extension, despite its experimental status, is paving its way to become the primary black formatting functionality within the Python extension.

**How to Install**:
1. Within the Extensions view in VS Code, type "Black Formatter".
2. Ensure you select the one provided by Microsoft.
3. Click on the install button.

Here's the direct link to the extension on the marketplace:

[Black Formatter for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

Certainly! Let's structure and expand the content for the subsection **3.2. Python Dependencies Configuration: `requirements.txt`** in the How-to-guide:

### **3.2. Python Dependencies Configuration: `requirements.txt`**

The `requirements.txt` file is a fundamental component in a Python project. It declares the list of dependencies required for your project to function correctly. For our code formatting setup, it's essential to include certain packages.

#### **Step 1: Preparing the `requirements.txt` File**

1. **Create a File**: If you don’t already have a `requirements.txt` file in the root directory of your project, create one.
   
2. **Add the Dependencies**: Ensure the following dependencies are listed in your `requirements.txt` file:

   ```
   black==23.7.0
   ```

   This specific version of Black ensures that your code is formatted consistently with the version used in our setup.

3. **Save the File**: Once you've added the dependencies, save the `requirements.txt` file.

#### **Step 2: Installing the Dependencies**

Having declared the required dependencies, the next step is to install them. This ensures that your local development environment is equipped with the right tools.

1. **Open a Terminal**: Access the terminal or command prompt on your system.

2. **Navigate to Your Project's Root Directory**: Use the `cd` command followed by your project's directory path.

3. **Install the Dependencies**: Execute the following command:

   ```
   pip install -r requirements.txt
   ```

   This command tells `pip`, Python's package installer, to fetch and install all the packages listed in the `requirements.txt` file.

Of course! Here's the revised content for the sub-section **3.3. Black Configuration for Your Project: `pyproject.toml`**:

### **3.3. Black Configuration for Your Project: `pyproject.toml`**

#### **Introduction to `pyproject.toml`**

`pyproject.toml` is more than just a configuration file—it represents a shift in the Python community towards a standardized way of configuring and building Python packages.

- **Purpose**: Initially introduced by [PEP 518](https://www.python.org/dev/peps/pep-0518/), its primary role was to outline build system requirements. It allows tools to understand what they need before starting the building process. For instance:

  ```toml
  [build-system]
  requires = ["setuptools>=42", "wheel"]
  build-backend = "setuptools.build_meta"
  ```

  The above TOML snippet mandates the project's requirement for `setuptools` (at least version 42) and `wheel` for building purposes.

- **Versatility**: As its adoption grew, various tools began to recognize `pyproject.toml` as a central hub for configurations. This has minimized the clutter of having individual configuration files for each tool. Notable tools like `black`, `flake8`, and `mypy` either already support or are transitioning towards this standard.

  Example for `black` configuration:

  ```toml
  [tool.black]
  line-length = 79
  include = '\\.pyi?$'
  ```

- **Centralization & Future Proofing**: As more tools start using `pyproject.toml`, it can serve as a centralized configuration point. Given its increasing adoption, utilizing `pyproject.toml` positions projects well for future Python tooling enhancements.

#### **Setting Up `pyproject.toml` for Black**

For our projects, we leverage `pyproject.toml` to ensure Black's configurations remain consistent across different environments. Below is a step-by-step guide to get you started:

1. **Check for Existing File**: See if there's a `pyproject.toml` in your project root. If not, create one.

2. **Black Configuration**: Copy the following configuration into your `pyproject.toml`:

   ```toml
   [tool.black]
   line-length = 79
   target-version = ['py39']
   include = """
   (
       ^notebooks/.*\\.ipynb$
     | ^src/.*\\.py$
   )
   """
   ```

3. **Understanding the Configuration**:
   
   - `[tool.black]`: This section is designated for Black configurations.
   - `line-length = 79`: Sets the maximum line length to 79 characters for the formatted code.
   - `target-version = ['py39']`: Ensures Black formats the code to be compatible with Python 3.9.
   - `include`: Uses regex patterns to specify which files Black should format:
     - `.ipynb` files within the `notebooks/` directory.
     - `.py` files within the `src/` directory.

4. **Save the File**: Once done, save the `pyproject.toml` file.

After setting up this configuration, Black will automatically adhere to these rules when formatting your Python code, ensuring a consistent styling across the entire project.

Perfect! Here's the refined content for the sub-section **3.4. Black Configuration in VS Code: `.vscode/settings.json`**:

### **3.4. Black Configuration in VS Code: `.vscode/settings.json`**

To ensure a unified code style throughout your development in VS Code, it's imperative to configure the editor to integrate with the Black code formatter. By setting up the `.vscode/settings.json` file, you pave the way for a smooth, GUI-driven experience, obviating the need to trigger Black through a terminal.

Here's a brief rundown of the provided `settings.json` configuration:

```json
{
    // Assign Black Formatter as the primary formatter for Python files
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
    },
    // Prioritize the Black version in the selected Python environment
    "black-formatter.importStrategy": "fromEnvironment",
}
```

#### **Configuration Explained**:

1. **Black as the Default Formatter**:
   - Within the `[python]` scope, the `editor.defaultFormatter` is set to `"ms-python.black-formatter"`.
   - Translation: For every Python file, Black Formatter is designated as the default tool for formatting in VS Code.

2. **Import Strategy**:
   - The `black-formatter.importStrategy` is assigned `"fromEnvironment"`.
   - In essence, this means VS Code's Python extension will first search for the Black version present in your active Python environment (e.g., a virtualenv).
   - Absent Black in this environment, the extension will default to its inbuilt version.

> **Tip**: Avoid specifying arguments like `"black-formatter.args": ["--line-lenght", "79"]` in the settings. Why? Black inherently scours for a `pyproject.toml` in the root project directory. If located, it incorporates these configurations. For VS Code users, given the setting `"black-formatter.importStrategy": "fromEnvironment"`, and with Black installed in that environment, the `pyproject.toml` settings are inherently followed.

#### **Manual Control Over Automatic Formatting**:

To maintain precision, our approach discourages auto-formatting every time a file is saved. This philosophy is especially crucial for Jupyter notebooks to preserve the narrative flow and context. Instead, developers are entrusted to initiate Black formatting at their discretion. How? Through VS Code's "Format Document" command—usually a quick keyboard shortcut away (commonly, `Shift + Alt + F`).

This VS Code-specific setup assures a consistent, intuitive way for developers to format their code, while granting them autonomy over the timing of its application.

### **3.5. Pre-Commit Hooks: `.pre-commit-config.yaml`**

Pre-commit hooks are more than just tools—they are our project's frontline defenders, ensuring that every piece of code meets our quality standards even before it's committed. By catching and rectifying style or formatting anomalies early, we're not just maintaining a clean codebase but also streamlining the review process. The resultant focus shifts from style nitpicks to meaningful code discussions, enhancing overall productivity.

Here's our `.pre-commit-config.yaml` configuration:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
        args:
          - --config=pyproject.toml
          - --verbose
          - --preview
```

#### **Config Breakdown**:

1. **`--verbose`**:
   - **What it Does**: Running Black with the `--verbose` flag unveils a detailed output, including notifications about unchanged files or those excluded due to specific patterns.
   - **Our Reasoning**: The verbose feedback grants developers an X-ray vision into Black's operations. If a file skips formatting or is explicitly excluded, the output flags it, thereby demystifying any unexpected behavior.

2. **`--preview`**:
   - **What it Does**: This option previews potentially impactful style modifications that Black may mainstream in its subsequent major releases.
   - **Our Reasoning**: Adopting the `--preview` flag is our strategic move to stay ahead of the curve. By anticipating and adapting to Black's prospective changes, we ensure a seamless evolution of our codebase. However, since these changes may not yet be community staples, it's pivotal to routinely assess their alignment with our project's standards.

To encapsulate, while the `--verbose` flag offers transparency, the `--preview` flag prepares us for tomorrow—but it’s crucial to use it judiciously.

Every commit triggers this configuration, invoking Black with the directives in `pyproject.toml`. A non-compliant code will halt the commit, signaling the developer to amend the formatting glitches.

#### **Advantages**:

1. **Instant Feedback Loop**: Formatting hiccups are flagged instantly, fortifying code quality at the very genesis, ensuring our repository remains unblemished.
2. **Uniformity**: With `pyproject.toml` at the helm, a consistent formatting standard is guaranteed, irrespective of the developer or the environment.

In essence, our embrace of pre-commit hooks isn't just about maintaining a clean code—it's our commitment to excellence at every development juncture.

Certainly, let's tackle this sub-section step by step, beginning with the introductory portion:

### **3.6. GitHub Actions: `.github/workflows/black.yml`**

To uphold a uniform code style across the repository, regardless of contributor diversity or their working environments, we've embraced GitHub Actions. This automated mechanism examines new code submissions—whether through pushes or pull requests—to ensure they align with our established formatting benchmarks.

In our pursuit of an efficient development workflow, we've embedded an auto-fix functionality within GitHub Actions. If any code diverges from our style guide, it's automatically rectified using the Black formatter. Post formatting, the rectified code is committed back to the repository. While this automated intervention minimizes manual adjustments and boosts developer productivity, it may lead to a denser commit history. It's a calculated trade-off we've chosen, favoring automated consistency over a more streamlined commit log.

Below is our GitHub Actions configuration:

```yaml
name: Black Code Formatter
on: [push, pull_request]
jobs:
  format:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install Black with Jupyter support
      run: pip install "black[jupyter]"
    - name: Auto-format .py files in src/ with Black
      run: find src/ -type f -name "*.py" -exec black {} +
    - name: Auto-format .ipynb files in notebooks/ with Black
      run: find notebooks/ -type f -name "*.ipynb" -exec black {} +
    - name: Commit and push changes
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add -A
        git diff --exit-code && git commit -m "Apply Black formatting" && git push
```

In the subsequent sections, we'll delve deeper into the components of this GitHub Actions setup:

### **1. Workflow Name**

```yaml
name: Black Code Formatter
```

This specifies the name of the GitHub Action workflow. It's a descriptive label that helps you identify this workflow when viewing it in the GitHub Actions tab on your repository.

### **2. Trigger Events**

```yaml
on: [push, pull_request]
```

This defines the events that will trigger the workflow:

- `push`: The workflow will run whenever new commits are pushed to any branch in the repository.
- `pull_request`: The workflow will also run for every new pull request or any subsequent changes to an existing pull request.

### **3. Job Definition**

```yaml
jobs:
  format:
    runs-on: ubuntu-latest
```

- `jobs`: This section contains a collection of tasks (called jobs) that the workflow will execute.
- `format`: This is the name of the job we've defined.
- `runs-on`: Specifies the type of runner (or virtual machine) on which the job will execute. Here, it's set to use the latest version of the Ubuntu operating system.

### **4. Job Steps**

Each step in the job is a sequential task that will be executed:

#### **4.1. Checkout Code**

```yaml
    - name: Checkout code
      uses: actions/checkout@v2
```

This step fetches the contents of the repository and places them in the runner's workspace. It uses the `checkout` action provided by GitHub at version `v2`.

#### **4.2. Set Up Python**

```yaml
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
```

This step sets up a specific version of Python on the runner. The `actions/setup-python@v2` action facilitates this, and the version we want (`3.9`) is specified.

#### **4.3. Install Black**

```yaml
    - name: Install Black with Jupyter support
      run: pip install "black[jupyter]"
```

This step installs Black (with additional support for Jupyter notebooks) using `pip`, Python's package installer.

#### **4.4. Auto-format Python Files**

```yaml
    - name: Auto-format .py files in src/ with Black
      run: |
        echo "Formatting .py files in src/"
        find src/ -type f -name "*.py" -exec black {} +
```

This step automatically formats Python files located in the `src/` directory. The `find` command is used to locate `.py` files, and each located file is formatted with Black.

#### **4.5. Auto-format Jupyter Notebooks**

```yaml
    - name: Auto-format .ipynb files in notebooks/ with Black
      run: |
        echo "Formatting .ipynb files in notebooks/"
        find notebooks/ -type f -name "*.ipynb" -exec black {} +
```

Similarly, this step auto-formats Jupyter notebook files located in the `notebooks/` directory.

#### **4.6. Commit and Push Changes (If Any)**

```yaml
    - name: Commit and push changes
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add -A
        git diff --exit-code || (git commit -m "Apply Black formatting" && git push)
```

- First, it sets a local git user name and email. This is necessary because the runner doesn't have default configurations for these.
- The `git add -A` command stages all changes, which would include any formatting changes made by Black.
- `git diff --exit-code` checks for any changes. If there are changes (meaning Black made formatting adjustments), the conditional `||` is triggered, leading to the subsequent commands.
- `git commit -m "Apply Black formatting"` creates a commit with the specified message.
- Finally, `git push` pushes the new commit back to the repository.

By the end of this workflow, any pushed code or pull request will be automatically formatted to adhere to the project's Black configurations. If any code was not compliant, a new commit will be added with the necessary formatting changes.

## **4. Conclusion**

Uniform and consistent code formatting is paramount for readability and maintainability. By using Black within the VS Code environment and enforcing standards via automated checks, we create a seamless development experience. This method ensures our team produces consistently styled code, streamlining collaborative efforts and minimizing style-centric code review durations.

Stay consistent, and happy coding!

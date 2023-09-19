# Tutorials

## **Using Black Code Formatter in Your Project**

Black is an uncompromising code formatter. It ensures that your Python code adheres to a consistent, readable style. The setup you have thanks to the Cookiecutter template makes it even more convenient to use Black in various contexts: `.py` scripts, Jupyter notebooks, and during git operations. Below are the key points and examples to help you understand how to use Black in these scenarios.

### **1. VS Code Integration**

When you're writing code in VS Code, Black can automatically format your code. Here's how:

**For `.py` scripts:**
Simply save your script (`Ctrl + S` or `Cmd + S` on Mac), and Black will format your script. 

**Example**:
- **Before**: 
    ```python
    def example1(x,y):z=x+y;return z
    ```

- **After Black Formatting**:
    ```python
    def example1(x, y):
        z = x + y
        return z
    ```

**For Jupyter notebooks:**
In a Jupyter cell in VS Code, you can manually format it by pressing `Shift + Alt + F` or right-click and select `Format Cell`.

**Example**:
- **Before**:
    ```python
    def calculate(a,b):result=a+b; return result
    ```

- **After Black Formatting**:
    ```python
    def calculate(a, b):
        result = a + b
        return result
    ```

### **2. Command Line Formatting**

For those who prefer using the terminal or need to format multiple files at once, Black can be run directly from the command line. 

- For `.py` scripts, run: 
    ```bash
    black your_script.py
    ```

- For Jupyter notebooks, run: 
    ```bash
    black your_notebook.ipynb
    ```

Suppose you've written a Python script named `sample_script.py` with the following content:

```python
def calculate(a,b):result=a+b; return result
```

**Formatting with Black from the Terminal:**

To format `sample_script.py` using Black, navigate to the directory containing the script and run:

```bash
black sample_script.py
```

**Terminal Output:**

```
reformatted sample_script.py
All done! ✨ 🍰 ✨
1 file reformatted.
```

**Formatted Code:**

After running the command, your `sample_script.py` will be updated to the following:

```python
    def example1(x, y):
        z = x + y
        return z
```

The terminal output provides a clear indication that `sample_script.py` has been reformatted. It's a quick and handy way to ensure your scripts follow the desired coding style.


### **3. Pre-commit Hooks in Git**

Thanks to the pre-configured hooks, any attempt to commit unformatted Python code will trigger Black to automatically format the code for you.

**Example**:

Suppose you've written the following code in `sample.py`:

```python
def example_function(x,y):result=x+y;return result
```

You decide to commit your changes:

```bash
git add sample.py
git commit -m "Add example function"
```

The pre-commit hook will detect the unformatted code and output a message:

```bash
black....................................................................Failed
- hook id: black
- files were modified by this hook

reformatted sample.py
All done! ✨ 🍰 ✨
1 file reformatted.
```

Your commit will be halted, but Black will have automatically formatted your file. You can simply run the commit command again, and this time it will succeed with the newly formatted code.

### **Skipping Formatting Using Black**

If for some reason you need a section of your code to remain unformatted by Black (for example, due to alignment preferences or specific readability concerns), you can tell Black to skip that section.

To skip formatting for a particular section, you can wrap that section of code between `# fmt: off` and `# fmt: on` comments.


**Original Code**:

```python
def transformation_matrix():
    # For clarity, we have a 3x3 matrix below representing some transformation.
    matrix = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    return matrix
```

If you were to format the above with Black, it might put the entire matrix on a single line if it's short enough, or it might space things out differently.

**After Black Formatting**:

```python
def transformation_matrix():
    matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    return matrix
```

This is more concise, but if you're frequently looking at matrices, the original might be clearer.

Now, if we don't want this matrix to be formatted by Black, we can wrap it with the `# fmt: off` and `# fmt: on` directives:

**Code With Black Directives**:

```python
def transformation_matrix():
    # fmt: off
    matrix = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    # fmt: on
    return matrix
```

When you run Black on this last snippet, the matrix remains untouched, while the rest of your code (if there were any other parts) would still get formatted.

This way, you have a clear separation of what gets formatted and what doesn't, making your intent explicit.

### **Conclusion**

Black ensures consistency and readability across your codebase. With the integrations provided by the Cookiecutter template, it's easier than ever to maintain a clean code style, whether you're working in `.py` scripts, Jupyter notebooks, or committing changes via git. Remember, a consistent code style not only makes your codebase look professional but also reduces cognitive load, making it easier for you and others to understand and collaborate on the project.

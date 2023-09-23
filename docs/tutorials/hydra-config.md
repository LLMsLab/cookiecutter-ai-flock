# Manage Configuration Files with Hydra

## Introduction and Motivation

Welcome to this tutorial on Hydra, a Python framework designed for
elegantly configuring complex applications. If you've ever found
yourself in a situation where you have a Python script filled with both
code and configuration parameters, you know how messy it can get.
Changing a single value often means digging into the source code, making
it difficult to manage and maintain your application.

Hydra offers a solution to this problem by separating the code and
configuration parameters into different files. This separation makes it
easier to manage complex applications, especially in data science
projects where configurations can get complicated quickly. With Hydra,
your Python scripts become cleaner, more modular, and easier to
understand.

In this guide, we'll walk you through how to use Hydra in both Python
scripts and Jupyter notebooks to manage your application's configuration
elegantly.

## Using Hydra in a Python Script

To use Hydra in a Python script, you need to import the `hydra` package
and use the `@hydra.main()` decorator. This decorator will automatically
load and validate the configuration file specified.

### Example Configuration File

Create a YAML configuration file named `main.yaml` inside a folder named
`config`:

```yaml
# config/main.yaml

db:
  driver: mysql
  user: omry
  password: secret
```

### Example Python Script

Here's an example Python script that uses Hydra to read the
configuration file and perform some actions based on it:

```python
from omegaconf import DictConfig, OmegaConf
import hydra

def display_config(cfg: DictConfig) -> None:
    """Display the entire configuration."""
    print(OmegaConf.to_yaml(cfg))

def display_driver(cfg: DictConfig) -> None:
    """Display the database driver."""
    print(f"Database driver is: {cfg.db.driver}")

@hydra.main(version_base=None, config_path="../../config", config_name="main")
def my_app(cfg: DictConfig) -> None:
    display_config(cfg)
    display_driver(cfg)

    # Get the SQL driver from the config
    sql_driver = cfg.db.driver

    # Now you can use sql_driver in your code
    # For example, you might pass it to a function that initializes a
    # database connection
    initialize_database(sql_driver)

def initialize_database(driver: str) -> None:
    print(f"Initializing database with driver: {driver}")
    # Your database initialization code here

if __name__ == "__main__":
    my_app()
```

### Example Output

When you run the script, you should see output similar to the following:

```text
db:
  driver: mysql
  user: omry
  password: secret

Database driver is: mysql
Initializing database with driver: mysql
```

## Using Hydra in a Jupyter Notebook

To use Hydra in a Jupyter notebook, you can import the `omegaconf`
package and manually load the configuration file using the
`OmegaConf.load()` function.

### Example Jupyter Notebook

Here's how you can read the same configuration file in a Jupyter
notebook:

```python
# notebooks/app.ipynb

import omegaconf

# Load the config file
config = omegaconf.OmegaConf.load("../config/main.yaml")

# Print the config
print(config)
```

#### Output:

```text
{'db': {'driver': 'mysql', 'user': 'omry', 'password': 'secret'}}
```

```python
driver = config['db']['driver']
print(driver)
```

#### Output:

```text
mysql
```

This guide should give you a good starting point for managing complex
configurations in Python using Hydra. Whether you're working in a Python
script or a Jupyter notebook, Hydra and OmegaConf offer powerful tools
for this task.

## Further Reading

For more information on Hydra and its capabilities, you can refer to the
following resources:

- [Hydra Official Documentation](https://hydra.cc/docs/intro)
- [OmegaConf Documentation](https://omegaconf.readthedocs.io/en/latest/)
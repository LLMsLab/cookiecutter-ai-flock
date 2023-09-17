"""Utils module.

This module provides utility functions for the {{cookiecutter.package_name}} project.

Functions:
----------
- extract_terms_from_dependencies():
    Extracts terms from the Python libraries specified in the
    pyproject.toml file.  Reads the dependencies and dev-dependencies
    from the pyproject.toml file, imports each library, and extracts
    terms (e.g., function names, class names) from them. The extracted
    terms are then saved to a file in the .vscode/dictionaries
    directory.

Notes
-----
- The module suppresses warnings and silently skips libraries that fail
  to import.
- Ensure the pyproject.toml file is correctly formatted and located in
  the expected directory.

Author:
-------
Marcos Aguilera Keyser <{{marcosak@gmail.com}}>

"""  # noqa: EXE002

import importlib
import os
import warnings

import toml


def extract_terms_from_dependencies():
    """Extract dependencies.

    Extract terms from the Python libraries specified in the
    pyproject.toml file to produce a custom dictionary for the VS Code
    extension Code Spell Checker.

    This function reads the dependencies and dev-dependencies from the
    pyproject.toml file, imports each library, and extracts terms (e.g.,
    function names, class names) from them.  The extracted terms are
    then saved to a file in the .vscode/dictionaries directory.

    Notes
    -----
    The function suppresses warnings and silently skips libraries that
    fail to import.

    Returns
    -------
    None
    """
    # Suppress any warnings that might arise during execution
    warnings.filterwarnings("ignore")

    # Determine the path to the pyproject.toml file in the current
    # working directory
    pyproject_path = os.path.join(  # noqa: PTH118
        os.getcwd(),  # noqa: PTH109
        "pyproject.toml",
    )

    # Open and read the pyproject.toml file
    with open(pyproject_path, "r") as f:  # noqa: PTH123, UP015
        # Parse the TOML file and store its content as a dictionary
        pyproject_data = toml.load(f)

    # Extract the names of the regular dependencies from the parsed TOML data
    dependencies = list(
        pyproject_data["tool"]["poetry"]["dependencies"].keys(),
    )

    # Extract the names of the development dependencies from the parsed
    # TOML data
    dev_dependencies = list(
        pyproject_data["tool"]["poetry"]["dev-dependencies"].keys(),
    )

    # Remove the 'python' entry from the list of dependencies, if it exists
    if "python" in dependencies:
        dependencies.remove("python")

    # Combine the lists of regular and development dependencies
    libraries_names = dependencies + dev_dependencies

    # Initialize an empty list to store imported libraries
    libraries = []

    # Iterate over each library name to import it
    for name in libraries_names:
        try:
            # Attempt to import the library using its name
            lib = importlib.import_module(name)
            # If successful, add the library to the list
            libraries.append(lib)
        except:  # noqa: PERF203, E722, S110
            # If the import fails, skip to the next library without
            # raising an error
            pass

    # Determine the path to the output file where terms will be saved
    output_path = os.path.join(  # noqa: PTH118
        os.getcwd(),  # noqa: PTH109
        ".vscode",
        "dictionaries",
        "data-science-en.txt",
    )

    # Open the output file in write mode
    with open(output_path, "w") as f:  # noqa: PTH123
        # Iterate over each imported library to extract its terms
        for library in libraries:
            # Get a list of all attributes and methods of the library
            all_library_contents = dir(library)
            # Initialize an empty list to store new contents
            new_contents = []

            # Iterate over each item in the library's contents
            for item in all_library_contents:
                try:
                    # Check if the item is a class or type
                    if isinstance(getattr(library, item), type):
                        # Extract methods and attributes of the
                        # class/type that don't start with an underscore
                        methods = [
                            method
                            for method in dir(getattr(library, item))
                            if not method.startswith("_")
                        ]
                        # Add the extracted methods to the new contents list
                        new_contents.extend(methods)
                except AttributeError:  # noqa: PERF203
                    # If an AttributeError occurs, skip to the next item
                    continue

            # Combine the original library contents with the new contents
            all_library_contents.extend(new_contents)
            # Remove duplicates by converting the list to a set and back
            # to a list
            all_library_contents = list(set(all_library_contents))
            # Filter out terms that start with an underscore
            all_library_contents = [
                term
                for term in all_library_contents
                if not term.startswith("_")
            ]

            # Write each term to the output file on a new line
            for term in all_library_contents:
                f.write(term + "\n")

    # Print a message indicating where the terms were saved
    print(f"Terms extracted and saved to {output_path}")  # noqa: T201


if __name__ == "__main__":
    extract_terms_from_dependencies()

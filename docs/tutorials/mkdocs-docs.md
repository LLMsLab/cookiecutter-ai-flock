# Project Documentation With MkDocs

MkDocs is a powerful tool for building project documentation. With the
Materials theme, it becomes even more robust, offering a plethora of
features to make your documentation stand out. This tutorial focuses on
key commands and features to help you build and deploy your
documentation effectively.

## Local Development with MkDocs

When you're working on documentation in VS Code, MkDocs provides
commands to build and serve your site locally. Here's how:


!!! note
    This tutorial assumes that all necessary libraries and extensions are already installed as per the provided `pyproject.toml` and `mkdocs.yml` files.

### Building and Serving Your Documentation

To build your documentation locally, you can run the following command:

```bash
mkdocs build
```

This command will generate a `site` folder containing the HTML files for
your documentation.


To serve your documentation and view it in a web browser, use:

```bash
mkdocs serve
```

!!! example "Local Development in Action"
    **Before Running Commands**:
    Your `docs` folder contains Markdown files.

    **After Running Commands**: 
    You'll have a `site` folder containing HTML files, and you can view your documentation at `http://127.0.0.1:8000/`.

!!! note "Stopping the Local MkDocs Server"
    To stop the local MkDocs server, simply press `Ctrl + C` in the terminal window where `mkdocs serve` is running. This will shut down the site and free up the port it was using.

!!! note "Alternative Commands for Unix-like Systems"
    If you want to run the MkDocs server on an alternative port or need to kill the process occupying port 8000, you can use the following commands from the Makefile:

    - **Start MkDocs on an Alternative Port**: 
      ```bash
      make docs_serve_alt_port
      ```
      This command starts the MkDocs server on port 8001.

    - **Kill Process on Port 8000**: 
      ```bash
      make docs_kill_port
      ```
      This command kills any process that is occupying port 8000.

    These commands are useful if you encounter port conflicts or need to run multiple instances of the MkDocs server. They should work on Unix-like systems, including both macOS and Linux.

## Deploying to GitHub Pages

### Setting Up GitHub Pages on GitHub

Before deploying your documentation, you'll need to configure GitHub Pages.

!!! info "Steps to Configure GitHub Pages"
    1. **Make sure the `gh-pages` branch exists**: Create it by running `git checkout -b gh-pages` if it doesn't exist.
    2. **Navigate to your GitHub repository**: Go to the repository where your MkDocs project is hosted.
    3. **Access Repository Settings**: Click on the "Settings" tab.
    4. **Go to Pages Settings**: In the sidebar, click on "Pages."
    5. **Select Publishing Source**: Choose `gh-pages` from the branch dropdown menu.
    6. **Select Folder**: Choose `docs` from the folder dropdown menu.
    7. **Save Changes**: Click "Save."

### Deploying Your Documentation

To deploy your documentation to GitHub Pages, run:

```bash
mkdocs gh-deploy
```

!!! example "Deployment in Action"
    After running the command, your site will be available at `https://<your-github-username>.github.io/<repository-name>/`.

## Understanding `mkdocs.yml`

Your `mkdocs.yml` file is the backbone of your MkDocs project. It specifies the theme, plugins, and other settings.

!!! info "Key Components of `mkdocs.yml`"
    - `theme`: Specifies the theme, in this case, Materials.
    - `markdown_extensions`: Lists the Markdown extensions used.
    - `plugins`: Lists the plugins used in the project.

## Conclusion

MkDocs with the Materials theme offers a robust solution for building
and deploying beautiful, functional documentation. Whether you're
working locally in VS Code or deploying to GitHub Pages, the process is
streamlined and efficient.

## Further Reading and Resources

For a deeper understanding of MkDocs and its various features, the
following resources are highly recommended:

- [Official MkDocs Documentation](https://www.mkdocs.org/)
- [Materials for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Python Project Documentation with MkDocs - Real Python](https://realpython.com/python-project-documentation-with-mkdocs/)

These resources provide comprehensive guides to MkDocs' features,
configuration options, and methods for extending its capabilities. They
are valuable for both newcomers and those looking to explore more
advanced features.
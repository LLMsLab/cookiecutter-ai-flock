![](assets/Steel-Horse-Barns.jpg)

**Welcome to Cookiecutter Ai Flock Documentation**

Cookiecutter Ai Flock is a specialized Cookiecutter template designed to
facilitate collaborative artificial intelligence, machine learning, and
generative AI projects. This template serves as an extensive framework,
bringing together a comprehensive set of tools and practices that meet
the evolving demands of modern AI development.

**Purpose and Vision**

Our aim is to provide a standardized foundation for your AI projects,
much like a flock moves together in harmony, to ensure uniformity and
consistency from the outset. The Cookiecutter Ai Flock template
integrates best practices for collaboration and reproducibility, as
advocated in "[The Turing
Way](https://the-turing-way.netlify.app/index.html)," promoting an open
culture of data science and research within the AI community.

The Cookiecutter Ai Flock template is crafted for ML professionals who
aspire to engage in collaborative and reproducible research
methodologies. It lays the groundwork for projects to be conducted with
efficiency and precision, providing a robust starting point for
innovation and discovery in the field of AI.

<!--
The documentation follows the best practice for project documentation as
described by Daniele Procida in the [Diátaxis documentation
framework](https://diataxis.fr/).
-->

<div class="grid cards" markdown>

- :octicons-tools-16: **Configure the working environment**  
  Configure your data science project's working environment according to the [Explanation](explanation/toc-explanation.md) documentation.

- :material-human-male-board: **Learn how to use tools**  
  [How-To Guides](how-to-guides/toc-how-to-guides.md) teach you how to produce professional code and documentation using the tools available in your working environment.

- :material-test-tube: **Step-by-step guide**  
  [Tutorials](tutorials/toc-tutorials.md) demonstrate how to use the tools in your working environment to complete an end-to-end toy data science project.

- :octicons-info-16: **Reference**  
  Reference material, such as naming conventions for Data Science items, can be found in the [API Reference](api-reference/toc-api-reference.md) section.

</div>

## Resource Compendium

??? custom "Naming Conventions"
    - :octicons-file-code-16: [Introduction to Naming Conventions for AI Project Assets](explanation/naming-conventions.md) - An essential guide that underscores the significance of systematic naming conventions in fostering clear communication, efficient project management, and reproducibility in AI and ML collaborations.
    - :octicons-book-16: [Effective GitHub Naming Conventions](explanation/github-naming-conventions.md) - Essential guidelines for naming GitHub repositories in data science, enhancing clarity and organization.
    - :octicons-tools-16: [Git Branch Naming Standards](how-to-guides/git-branch-naming-standards.md) - A comprehensive guide on standardized branch naming for ML projects, enhancing repository clarity and collaboration.
    - :octicons-tools-16: [Commit Message Standards in ML Projects](how-to-guides/commit-message-standards-ml.md) - A guide on structuring and standardizing commit messages to improve team collaboration in ML projects.
    - :octicons-tools-16: [ML Data Folder Naming Guide](how-to-guides/ml-data-folder-naming.md) - A comprehensive guide to naming data folders in ML projects for enhanced organization and efficiency.
    - :octicons-book-16: [Data Files Naming Conventions](how-to-guides/ml-data-naming-conventions.md) - A guide to effective naming conventions for data files in ML projects, enhancing data manageability and team collaboration.
    - :octicons-book-16: [Model Persistence File Naming Conventions](explanation/model-persistence-naming-conventions.md) - Guide on naming conventions for persisting machine learning models, covering format, versioning, metadata storage, and documentation.
    - :octicons-tools-16: [Automating Metadata Creation](how-to-guides/machine-learning-metadata-automation.md) - A practical guide for automating the creation and saving of machine learning model metadata using a Python script.
    - :octicons-sync-16: [Markdown Documentation for ML Models](tutorials/markdown-ml-model-documentation.md) - Step-by-step tutorial on documenting machine learning models using Markdown, covering the training process, parameters, performance metrics, and metadata.
    - :octicons-book-16: [Notebook and Script Naming Conventions in ML Projects](explanation/ml-naming-conventions.md) - Essential guidelines for naming Jupyter notebooks and scripts in ML projects, emphasizing clarity, consistency, and efficient file management.
    - :octicons-tools-16: [Enforcing Naming Conventions with GitHub Actions](how-to-guides/github-actions-naming-convention.md) - A practical guide to set up GitHub Actions for enforcing naming conventions in machine learning projects, ensuring consistency and organization.

??? custom "Data Version Control with DVC"
    - :octicons-book-16: [Understanding DVC](explanation/dvc-understanding-dvs.md) - Essentials of DVC for large datasets management in ML, covering integration, versioning, and reproducibility.
    - :octicons-tools-16: [Setting Up DVC](how-to-guides/dvc-set-up.md) - Comprehensive setup guide for DVC, from initialization to managing data in the cloud.
    - :octicons-sync-16: [Local Data Updates](tutorials/dvc-local.md) - Step-by-step tutorial on managing and tracking local dataset updates with DVC.
    - :octicons-cloud-16: [Cloud Data Updates](tutorials/dvc-cloud.md) - Tutorial on syncing cloud data updates in services like AWS S3 or Azure Blob Storage using DVC.
    - :octicons-comment-discussion-16: [Data Version Communication](how-to-guides/dvc-communication.md) - Guidelines for effective communication of data versions in collaborative settings using DVC and GitHub.
    - :octicons-repo-push-16: [Collaborative Data Workflow](tutorials/dvc-collaboration.md) - Workflow for collaborative data updates, tracking changes, and team syncing with DVC and GitHub.
    - :octicons-git-branch-16: [Branches for Data Versions](explanation/dvc-git-branches.md) - Understanding the use of Git branches for data version management and DVC integration with collaboration tools.
    - :octicons-code-16: [DVC in VS Code](how-to-guides/dvc-vscode-extension.md) - How to use the DVC extension in Visual Studio Code for efficient data version control and management.

??? custom "Data Management"
    - :octicons-book-16: [Effective Data Documentation](explanation/effective-data-documentation.md) - A comprehensive guide on creating and managing metadata and documentation for data science projects, emphasizing importance, standard practices, and automation.
    - :octicons-tools-16: [Metadata Integration in Data Analysis](how-to-guides/metadata-integration-data-analysis.md) - A practical guide on integrating metadata with data analysis tools, detailing steps, strategies, and an example Python script for effective collaboration.
    - :octicons-sync-16: [Creating and Managing Metadata and Documentation](tutorials/creating-managing-metadata-documentation.md) - An in-depth tutorial on crafting effective metadata and maintaining thorough data documentation, complete with steps, examples, and best practices.

<!--
## Data Version Control (DVC) Documentation Index

Explore the various aspects of DVC with our tailored documentation, easily accessible through the following sections:

- :octicons-book-16: [Understanding DVC](explanation/dvc-understanding-dvs.md) - Essentials of DVC for large datasets management in ML, covering integration, versioning, and reproducibility.
- :octicons-tools-16: [Setting Up DVC](how-to-guides/dvc-set-up.md) - Comprehensive setup guide for DVC, from initialization to managing data in the cloud.
- :octicons-sync-16: [Local Data Updates](tutorials/dvc-local.md) - Step-by-step tutorial on managing and tracking local dataset updates with DVC.
- :octicons-cloud-16: [Cloud Data Updates](tutorials/dvc-cloud.md) - Tutorial on syncing cloud data updates in services like AWS S3 or Azure Blob Storage using DVC.
- :octicons-comment-discussion-16: [Data Version Communication](how-to-guides/dvc-communication.md) - Guidelines for effective communication of data versions in collaborative settings using DVC and GitHub.
- :octicons-repo-push-16: [Collaborative Data Workflow](tutorials/dvc-collaboration.md) - Workflow for collaborative data updates, tracking changes, and team syncing with DVC and GitHub.
- :octicons-git-branch-16: [Branches for Data Versions](explanation/dvc-git-branches.md) - Understanding the use of Git branches for data version management and DVC integration with collaboration tools.
- :octicons-code-16: [DVC in VS Code](how-to-guides/dvc-vscode-extension.md) - How to use the DVC extension in Visual Studio Code for efficient data version control and management.
-->
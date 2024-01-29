# Naming Conventions for Data Folders in ML Projects

!!! abstract "Overview"
    In any Machine Learning (ML) project, organizing and managing data efficiently is crucial. Adopting clear, consistent naming conventions for data folders aids in better data management, collaboration, and project comprehension. This guide provides guidelines for naming data folders in ML projects, ensuring a well-structured and manageable data environment.

!!! tip "Folder Structure and Naming Convention"
    Organize the data folder structure into categories based on their role in the data processing pipeline:

    ```markdown
    data
    ├── raw                   # Original, unaltered data
    ├── external              # Data from third-party sources
    ├── interim               # Partially processed data
    ├── processed             # Data ready for analysis
    └── features              # Features for model training
    ```

!!! note "Explanation of Categories"
    - **Raw**: Original datasets, unaltered and serving as a backup.
    - **External**: Data from outside sources, including third-party data and APIs.
    - **Interim**: Data in the process of cleaning or transformation.
    - **Processed**: The final dataset version, ready for analysis or modeling.
    - **Features**: Feature sets for ML models, including transformed and selected features.

!!! success "Conclusion"
    Adopting these naming conventions for data folders in your ML projects will lead to a more organized, accessible, and efficient data management process, crucial for any ML project's success.
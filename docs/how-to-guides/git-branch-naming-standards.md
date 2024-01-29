# Git Branch Naming Standards for ML Projects

!!! tip "Overview"
    For machine learning projects, maintaining clarity in the Git repository is crucial. A consistent approach to branch naming is key to this clarity, facilitating rapid identification of the branch's purpose, aiding in collaboration, and making repository navigation intuitive.

!!! example "Naming Convention Structure"
    Branch names should follow this pattern:

    ```plaintext
    <category>/<description>-<issue_number_or_jira_key>
    ```

    - **Category**: A keyword indicating the branch's work nature.
    - **Description**: A clear descriptor of the task or feature.
    - **Issue Number or Jira Key**: Mandatory for linking to a corresponding task in your project management tool.

!!! abstract "Categories"
    Standard categories provide context on the branch's work domain:

    | Category      | Description                                                   |
    |---------------|---------------------------------------------------------------|
    | `feature`     | New feature development or enhancements                       |
    | `bugfix`      | Targeted branches for bug resolution                          |
    | `data`        | Data management activities, like acquisition or processing    |
    | `experiment`  | Exploratory or experimental development                       |
    | `model`       | Model creation, testing, or deployment                        |
    | `docs`        | Documentation creation or updates                             |
    | `refactor`    | Code restructuring to improve performance without altering functionality |
    | `test`        | Test development or modification                              |
    | `chore`       | Routine tasks or minor updates                                |

!!! check "Examples"
    Branch names that meet our standards:

    - `feature/user-authentication-DATA123`
    - `data/dataset-enhancement-GH15`
    - `model/performance-improvement-DATA22`
    - `bugfix/data-loading-error-GH45`
    - `docs/api-documentation-update`
    - `refactor/code-optimization-DATA78`
    - `test/new-model-tests-GH27`

!!! warning "Guidelines"
    - Use lowercase for all branch names.
    - Hyphens for word separation enhance readability.
    - Keep names brief yet descriptive.
    - Including the issue number or Jira key is mandatory for traceability.

!!! summary "Conclusion"
    Following these naming conventions is vital for organizing and accessing our ML project repositories, fostering team collaboration and efficient project management.
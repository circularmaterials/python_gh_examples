# GitHub Repository Management Functions

- Quick and dirty examples.
- This documentation describes the use of three Python functions designed to manage GitHub repositories. These functions are part of a Python script using the PyGithub library.

## Functions

### 1. Create Repository in Organization and Retrieve SSH Clone URL

- **Purpose**: Creates a new GitHub repository within a specified organization. If the repository already exists, it does not recreate it. After creating the repository, it outputs the SSH clone URL, which can be used to clone the repository.
- **Usage**: Call `create_github_org_repo_and_get_ssh(repo_name)` with the desired repository name. It checks if the repository exists, creates it if it does not, and prints the SSH clone URL.

### 2. Delete Repository

- **Purpose**: Deletes a specified repository from either a user's account or an organization. This function is useful for cleaning up or removing unnecessary repositories.
- **Usage**: Call `delete_github_repo(repo_name, org_name=None)` where `repo_name` is the name of the repository to delete, and `org_name` is optionally the name of the organization (if the repository is not under a user's personal account).

### 3. Add or Update File in Repository

- **Purpose**: Adds a new file or updates an existing file in a specified GitHub repository. This function is ideal for automated file management within repositories, such as updating configuration files or documentation.
- **Usage**: Use `add_file_to_repo(repo_name, file_path, file_content, commit_message, org_name=None)` where `repo_name` is the repository name, `file_path` is the path within the repository where the file will be placed or updated, `file_content` is the content of the file, and `commit_message` is the message for the commit. Optionally specify `org_name` if the repository is within an organization.

Each function requires a valid GitHub API token with the appropriate permissions set as an environment variable (`GH_CM_API_TOKEN`) or have in .env.

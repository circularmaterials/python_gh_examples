import os
from github import Github, GithubException
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
GITHUB_TOKEN = os.getenv('GH_CM_API_TOKEN')  # Load the GitHub token from an environment variable

def add_file_to_repo(repo_name, file_path, file_content, commit_message, org_name=None):
    """Add or update a file in a GitHub repository."""
    if not GITHUB_TOKEN:
        print("GitHub API token is not set. Please set the GH_API_TOKEN environment variable.")
        return

    g = Github(GITHUB_TOKEN)

    try:
        if org_name:
            # Adding file to an organization's repository
            org = g.get_organization(org_name)
            repo = org.get_repo(repo_name)
        else:
            # Adding file to the user's personal repository
            user = g.get_user()
            repo = user.get_repo(repo_name)

        # Get the current content of the file (if it exists) to get the SHA (needed for update)
        try:
            contents = repo.get_contents(file_path)
            repo.update_file(contents.path, commit_message, file_content, contents.sha)
            print(f"Updated file '{file_path}' in repository '{repo_name}'.")
        except GithubException:
            # If the file does not exist, create it
            repo.create_file(file_path, commit_message, file_content)
            print(f"Created file '{file_path}' in repository '{repo_name}'.")
    except GithubException as e:
        print(f"Failed to add/update file in repository: {e.status} {e.data['message']}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Example usage
    repo_name = 'python_created_test'
    file_path = 'README.md'  # Path where the file will be placed in the repo
    file_content = '# This file was added through python'
    commit_message = 'Add or update README.md'
    org_name = 'circularmaterials'  # Specify if the repo is under an organization, otherwise use None

    add_file_to_repo(repo_name, file_path, file_content, commit_message, org_name)

if __name__ == "__main__":
    main()

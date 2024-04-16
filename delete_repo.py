import os
from github import Github, GithubException
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
GITHUB_TOKEN = os.getenv('GH_CM_API_TOKEN')  # Load the GitHub token from an environment variable

def delete_github_repo(repo_name, org_name=None):
    """Delete a GitHub repository from an organization or a user's account."""
    if not GITHUB_TOKEN:
        print("GitHub API token is not set. Please set the GH_API_TOKEN environment variable.")
        return
    
    g = Github(GITHUB_TOKEN)

    try:
        if org_name:
            # Deleting from an organization
            org = g.get_organization(org_name)
            repo = org.get_repo(repo_name)
        else:
            # Deleting from the user's account
            user = g.get_user()
            repo = user.get_repo(repo_name)

        repo.delete()
        print(f"Repository '{repo_name}' has been deleted successfully.")
    except GithubException as e:
        print(f"Failed to delete repository: {e.status} {e.data['message']}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Example usage
    repo_name = 'python_created_test'  # Specify the repository name to delete
    org_name = 'circularmaterials'  # Specify the organization name if applicable, or use None for user account
    delete_github_repo(repo_name, org_name)

if __name__ == "__main__":
    main()

from github import Github, GithubException
import os
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

# Constants
GITHUB_TOKEN = os.getenv('GH_CM_API_TOKEN') 
REPO_NAME = 'python_gh_examples'  # Name of the repository to create
ORG_NAME = 'circularmaterials'

def create_github_org_repo(org_name, repo_name):
    """Create a GitHub repository in an organization. If it already exists, do nothing."""
    g = Github(GITHUB_TOKEN)
    org = g.get_organization(org_name)
    repos = org.get_repos()

    # Check if the repository already exists
    if any(repo.name == repo_name for repo in repos):
        print(f"Repository '{repo_name}' already exists in organization '{org_name}'.")
        # Output the SSH clone URL
        print(f"SSH clone URL: {repo.ssh_url}")
        return

    # Create the repository if it does not exist
    try:
        repo = org.create_repo(repo_name)
        print(f"Repository '{repo_name}' created successfully in organization '{org_name}'.")
        
        # Output the SSH clone URL
        print(f"SSH clone URL: {repo.ssh_url}")        
    except GithubException as e:
        print(f"Failed to create repository in organization: {e.status} {e.data['message']}")

def main():
    try:
        create_github_org_repo(ORG_NAME, REPO_NAME)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

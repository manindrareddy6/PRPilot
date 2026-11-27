import os
from dotenv import load_dotenv
from github import Github, Auth

load_dotenv()


def get_github_client():
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise ValueError("GITHUB_TOKEN not found in .env file")

    auth = Auth.Token(token)
    return Github(auth=auth)


def get_pull_request(owner, repo_name, pr_number):
    github = get_github_client()
    repository = github.get_repo(f"{owner}/{repo_name}")

    return repository.get_pull(pr_number)


def fetch_pr_diff(owner, repo_name, pr_number):
    pull_request = get_pull_request(owner, repo_name, pr_number)

    files = []

    for file in pull_request.get_files():
        files.append({
            "filename": file.filename,
            "status": file.status,
            "additions": file.additions,
            "deletions": file.deletions,
            "changes": file.changes,
            "patch": file.patch
        })

    return files
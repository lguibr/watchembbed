import subprocess
import os

def get_git_tracked_files(repo_dir):
    """Get a list of all files tracked by git."""
    cmd = ['git', '-C', repo_dir, 'ls-files']
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Failed to list git tracked files: {result.stderr}")
    return result.stdout.splitlines()

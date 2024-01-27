import os
import hashlib
import json
from git import Repo
import threading
import time



repo_dir = './'  # Replace with your repository path
json_path = './hash_file.json'  # Replace with your desired JSON file path

def get_file_hash(file_path):
    """Compute SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def load_hashes(json_path):
    """Load existing hashes from a JSON file."""
    if os.path.exists(json_path):
        with open(json_path, "r") as json_file:
            return json.load(json_file)
    return {}

def save_hashes(hashes, json_path):
    """Save hashes to a JSON file."""
    with open(json_path, "w") as json_file:
        json.dump(hashes, json_file, indent=4)

def update_file_hashes(repo_dir, json_path):
    """Update the file hashes for a git repository."""
    repo = Repo(repo_dir)
    file_hashes = load_hashes(json_path)

    for file in repo.tree().traverse():
        file_path = os.path.join(repo_dir, file.path)
        if os.path.isfile(file_path):
            file_hashes[file.path] = {"hash": get_file_hash(file_path)}

    save_hashes(file_hashes, json_path)

def update_function():
    while True:
        # Your update code here
        print("Updating...")
        update_file_hashes(repo_dir, json_path)
        time.sleep(5)  # wait for 5 seconds before next update


def main():


    # Initial hash generation for all files
    update_thread = threading.Thread(target=update_function)
    update_thread.start()



if __name__ == "__main__":
    main()

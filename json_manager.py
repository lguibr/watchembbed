import json
import os

def load_json(json_path):
    """Load existing hashes from a JSON file. Return an empty dictionary if the file is empty or not valid JSON."""
    if os.path.exists(json_path):
        with open(json_path, "r") as json_file:
            try:
                return json.load(json_file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_json(hashes, json_path):
    """Save hashes to a JSON file."""
    with open(json_path, "w") as json_file:
        json.dump(hashes, json_file, indent=4)

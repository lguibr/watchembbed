import os
from hasher import get_file_hash
from json_manager import load_json, save_json
from git_ops import get_git_tracked_files
from document import create_documents_for_file  
from embedding import get_embedding_for_document

import logging

logger = logging.getLogger(__name__)

def update_file_hashes(repo_dir, json_path):
    """Update the file hashes for a git repository."""
    tracked_files = get_git_tracked_files(repo_dir)
    file_hashes = load_json(json_path)

    for file in tracked_files:
        full_file_path = os.path.join(repo_dir, file)
        if full_file_path == json_path:  # Skip the hash file itself
            continue
        if os.path.isfile(full_file_path):
            new_hash = get_file_hash(full_file_path)
            if file not in file_hashes or file_hashes[file]['hash'] != new_hash:
                # Hash has changed, update it and create a document
                logger.info("some hash changed")
                logger.info("full_file_path:", full_file_path)
                file_hashes[file] = {'hash': new_hash}
                raw_documents = create_documents_for_file(full_file_path)

                documents = [document.to_json() for document in raw_documents]
                for document in documents:

                    document['embedding'] = get_embedding_for_document(document)

                file_hashes[file]['documents'] = documents

    save_json(file_hashes, json_path)
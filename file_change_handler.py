from watchdog.events import FileSystemEventHandler
from file_update import update_file_hashes
from git_ops import get_git_tracked_files
import os

import logging

logger = logging.getLogger(__name__)


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, repo_dir, json_path):
        self.repo_dir = repo_dir
        self.json_path = json_path
        self.git_tracked_files = set(get_git_tracked_files(self.repo_dir))

    def on_any_event(self, event):
        if not event.is_directory and event.event_type == 'modified':
            # Check if the modified file is tracked by Git
            relative_path = os.path.relpath(event.src_path, self.repo_dir)
            if relative_path in self.git_tracked_files:
                logger.info("Git tracked file changed: %s", relative_path)
                update_file_hashes(self.repo_dir, self.json_path)
            else:
                logger.debug("Non-tracked file change ignored: %s", relative_path)

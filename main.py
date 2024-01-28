import argparse
import logging
from file_change_handler import FileChangeHandler
from watchdog.observers import Observer
from logger_config import setup_logger

def main(debug_mode,repo_dir:str, json_path  :str):
    logger = setup_logger(debug_mode)
    logger.info("Starting WatchEmbbed...")

    # Set up the file system event handler
    event_handler = FileChangeHandler(repo_dir, json_path)
    observer = Observer()
    observer.schedule(event_handler, repo_dir, recursive=True)

    # Start the observer
    observer.start()
    logger.info(f"Monitoring {repo_dir}")

    try:
        while True:
            pass  # Keep the script running
        
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
        logger.info("Stopped WatchEmbbed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WatchEmbbed - Embedding Git Repository Files")
    parser.add_argument("--i", default='./', help="Input path for the repository to monitor")
    parser.add_argument("--o", default='./hash_file.json', help="Output path for the JSON file")
    parser.add_argument("--debug", help="Enable debug mode", action="store_true")

    args = parser.parse_args()

    main(args.debug, args.i, args.o)
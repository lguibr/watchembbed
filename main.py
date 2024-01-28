import argparse
from logger_config import setup_logger
import time
from watchdog.observers import Observer
from file_change_handler import FileChangeHandler

repo_dir = './'  # Replace with your repository path
json_path = './hash_file.json'  # Replace with your desired JSON file path

def main(debug_mode):
    logger = setup_logger(debug_mode)
    logger.info("Starting the program...")
    # Set up the file system event handler

    event_handler = FileChangeHandler(repo_dir, json_path)
    observer = Observer()
    observer.schedule(event_handler, repo_dir, recursive=True)

    # Start the observer
    observer.start()

    try:
        while True:
            logger.debug("Ping!")
            time.sleep(3)


    except KeyboardInterrupt:
        observer.stop()
    logger.debug("Terminated by user.")
    
    observer.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="Enable debug mode", action="store_true")
    args = parser.parse_args()

    main(args.debug)

# WatchEmbbed

## Overview

WatchEmbbed is a Python application designed to monitor a Git repository, generating embeddings for its files using large language models (LLMs). This tool ensures real-time synchronization of file embeddings with repository changes, making it ideal for projects involving textual analysis and machine learning.

## Features

- **Real-Time Monitoring**: Uses Watchdog to monitor changes in a Git repository.
- **Git Integration**: Processes only Git-tracked files, adhering to `.gitignore` rules.
- **Language Model Embeddings**: Employs LLMs, such as OpenAI's models, for embedding textual content.
- **Automated Syncing**: Updates embeddings automatically upon file modifications, additions, or deletions.
- **Efficient Logging**: Provides detailed logging with adjustable verbosity for effective debugging.

## Git-Tracked Files

- **Git Staging Required**: WatchEmbbed only monitors files that are tracked by Git. Newly created files must be staged (added to Git) to be included in the monitoring and embedding process.
- **Hash-Based Tracking**: The system uses a SHA256 hash to maintain consistent tracking of files, ensuring accurate embedding updates even if file names change.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/lguibr/watchembbed.git
   cd watchembbed
   ```

2. **Install Dependencies** (virtual environment recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage

```bash
python main.py --i /path/to/your/repo --o /path/to/your/json/embeddings
```

Optional flags:

- `--debug`: Enable detailed logging.

## Configuration

- **Logging**: Modify `logger_config.py` to adjust logging levels and formats.
- **Embedding Models**: Set up the desired LLM model in `embedding.py`.

## Future Enhancements

- **Vector Store Integration**: Plans to support vector storage systems as an alternative to JSON for more efficient embedding management.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for bug fixes, features, or documentation.

## License

Released under [MIT License](LICENSE).

from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
import os
import logging

logger = logging.getLogger(__name__)


def create_documents_for_file(file_path):
    """Create a document for a single file using LangChain, handling non-UTF-8 files."""


    try:
        logger.debug("Trying to read file")
        with open(file_path, 'r', encoding='utf-8') as f:
            # Attempt to read the file to check if it's UTF-8 encoded
            f.read()
            logger.debug("file readed")

    except UnicodeDecodeError:
        logger.error("skipped because UnicodeDecodeError")

        # If a UnicodeDecodeError occurs, return None or an empty document
        return None

    loader = GenericLoader.from_filesystem(
      
        file_path,
        parser=LanguageParser(),
    )
    documents = loader.load()
    return documents
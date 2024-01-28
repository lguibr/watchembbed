from langchain_openai import OpenAIEmbeddings


import logging

logger = logging.getLogger(__name__)


def get_embedding_for_document(document):
    """Receive a single document and return the embedding value."""
    embeddings = OpenAIEmbeddings()
    if 'kwargs' in document and 'page_content' in document['kwargs']:
        text = document['kwargs']['page_content']
        logger.debug("Embedding document")
        doc_embedding = embeddings.embed_documents([text])
        return doc_embedding
    else:
        return None

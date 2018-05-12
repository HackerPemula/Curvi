import nltk
import logging

from services.document_services import DocumentService

def start_preprocessing():
    try:
        nltk.download('punkt')

        documents = DocumentService.get_all_documents()

        if not documents:
            raise Exception("Document is empty")

        tokenized = []
        for document in documents:
            tokenized.append(nltk.tokenize.word_tokenize(document.Content))

        return
    except Exception as e:
        logging.exception(str(e))
        
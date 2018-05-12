from __future__ import absolute_import
import time
import json
import logging

from Curvi.celery_app import app
from worker.process import preprocess, nmf, classifier
from services.document_services import DocumentService

@app.task
def predict_documents(DocumentID=None):
    try:        
        documents = DocumentService.get_document_by_id([DocumentID])
        documents = preprocess.start_preprocessing(documents, True)
        documents = nmf.model_topic(documents)
        results = classifier.predict(documents)

        for idx, doc in enumerate(documents):
            param = [doc.DocumentID, results[idx]]
            DocumentService.update_document_category_by_id(param)
        
        return
    except Exception as e:
        logging.error(str(e))

@app.task
def train_documents():
    try:
        documents = DocumentService.get_all_documents()
        documents = preprocess.start_preprocessing(documents, False)
        documents = nmf.model_topic(documents)
        classifier.train_classifier(documents)
    except Exception as e:
        logging.error(str(e))
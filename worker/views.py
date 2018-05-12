from django.shortcuts import render
import time
import json
import logging

from Curvi.celery import app
import worker.process as wprocess
import nltk

# Create your views here.
@app.task
def process_plsa():
    try:
        wprocess.preprocess.start_preprocessing()
    except Exception as e:
        logging.exception(str(e))
import nltk
import logging
import googletrans

from services.document_services import DocumentService
from services.topic_services import TopicService
from services.preprocessed_document_model import PreprocessedDocumentService
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def translate(topic):
    translator = googletrans.Translator()

    detected = translator.detect(topic).lang

    translated = []
    translated_topic = None

    if detected == 'en':
        translated_topic = translator.translate(topic, src='en', dest='id').text
        translated = [topic, translated_topic]
    else:
        translated_topic = translator.translate(topic, src='id', dest='en').text
        translated = [translated_topic, topic]

    results = TopicService.insert_topic(translated)

    return results

def start_preprocessing():
    try:
        nltk.download('punkt')

        documents = DocumentService.get_all_documents()

        if not documents:
            raise Exception("Document is empty")

        tokenized = []

        for document in documents:
            tokenized = nltk.tokenize.word_tokenize(document.Content)

        # en_stopwords = set(nltk.corpus.stopwords.words('english'))
        
        # en_removed = []
        # for word in tokenized:
        #     if word not in en_stopwords:
        #         en_removed.append(word)

            translated = []
            for word in tokenized:
                param = [word]
                topic = TopicService.get_topic(param)

                if not topic:
                    topic = translate(word)

                if topic:
                    translated.append(topic)

            id_stopwords = set(nltk.corpus.stopwords.words('indonesian'))
            id_removed = []
            for word in translated:
                if word not in id_stopwords:
                    id_removed.append(word)

            # del en_removed
            factory = StemmerFactory()
            stemmer = factory.create_stemmer()

            stemmed = stemmer.stem(' '.join(id_removed)).split()
            tokenized = ' '.join(tokenized)

            param = [document[0], tokenized, stemmed]
            PreprocessedDocumentService.insert_preprocessed_document(param)

        return
    except Exception as e:
        logging.exception(str(e))
        
from sklearn.decomposition import NMF, TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np
import logging

from services.topic_result_services import TopicResultService

params = { 'num_of_topic': 5, 'num_of_features': 1000 }

def model_topic(documents):
    logging.info("Extracting topic features")
    X_topics = None
    for category_id in list(documents):
        try:
            text = []
            for document in documents[category_id]:
                text.append(document.Stemmed)

            tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=params['num_of_features'])
            tfidf = tfidf_vectorizer.fit_transform(text)

            # Run NMF
            nmf = NMF(n_components=params['num_of_topics'], random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd')
            X_topics = nmf.fit_transform(tfidf)
            topic_word = nmf.components_
            vocabulary = tfidf_vectorizer.get_feature_names()

            topic_summaries = []
            
            if not category_id == 0:
                for i, topic_dist in enumerate(topic_word):
                    topic_words = np.array(vocabulary)[np.argsort(topic_dist)][:-(params['num_of_topics']+1):-1]
                    topic_summaries.append(' '.join(topic_words))
                    for topic in topic_words:
                        param = [documents.DocumentID, topic]
                        TopicResultService.insert_topic_result(param)

            documents[category_id] = X_topics
        except Exception as e:
            logging.error(str(e))

    logging.info("Finished extracting topic features")
    return documents
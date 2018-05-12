import nltk
import logging
import numpy as np
from sklearn.preprocessing import normalize

parameters = {'num_of_topic': 5, 'num_of_iter': 5}

def build_vocabulary(docs):
    '''
    Construct a list of unique words in the corpus.
    '''
    # ** ADD ** #
    # exclude words that appear in 90%+ of the documents
    # exclude words that are too (in)frequent
    discrete_set = set()
    for document in docs:
        for word in document.Stemmed:
            discrete_set.add(word)
    
    vocabulary = list(discrete_set)

    return vocabulary

def calculate_plsa(preprocessed_documents):
    try:
        logging.info("Start calculating PLSA")

        parameters['num_of_doc'] = len(preprocessed_documents)

        vocabulary = build_vocabulary(preprocessed_documents)

        term_doc_matrix = np.zeros([parameters['num_of_doc'], len(vocabulary)], dtype=np.int)

        for d, doc in enumerate(preprocessed_documents):
            term_freq = np.zeros(len(vocabulary), dtype=int)
            for word in doc.Stemmed:
                if word in vocabulary:
                    w = vocabulary.index(word)
                    term_freq[w] = term_freq[w] + 1
            
            term_doc_matrix[d] = term_freq


        doc_topic_prob = np.zeros([parameters['num_of_doc'], parameters['num_of_topic']], dtype=np.float)
        topic_word_prob = np.zeros([parameters['num_of_topic'], len(vocabulary)], dtype=np.float)
        topic_prob = np.zeros([parameters['num_of_doc'], len(vocabulary), parameters['num_of_topic']], dtype=np.float)

        logging.info("Initializing matrix")
        doc_topic_prob = np.random.random(size=(parameters['num_of_doc'], parameters['num_of_topic']))
        
        doc_topic_prob = normalize(doc_topic_prob)

        topic_word_prob = np.random.random(size=(parameters['num_of_topic'], len(vocabulary)))

        topic_word_prob = normalize(topic_word_prob)

        logging.info("Running EM Algorithm")
        for iter in range(parameters['num_of_iter']):
            logging.info("E-Step: ")
            for d, doc in enumerate(preprocessed_documents):
                for w in range(len(vocabulary)):
                    prob = doc_topic_prob[d,:] * topic_word_prob[:, w]
                    if sum(prob) == 0.0:
                        logging.error("Error on d: " + str(d) + ", w: " + str(w))
                        logging.error("Document topic prob: " + str(doc_topic_prob[d, :]))
                        logging.error("Topic word prob: " + str(topic_word_prob[:, w]))
                        logging.error("Topic prob: " + str(prob))
                    else:
                        prob = normalize(prob)
                    topic_prob[d][w] = prob

            logging.info("M-Step: ")
            for z in range(parameters['num_of_topic']):
                for w in range(len(vocabulary)):
                    s = 0
                    for d in range(len(preprocessed_documents)):
                        count = term_doc_matrix[d][w]
                        s += count * topic_prob[d, w, z]
                    topic_word_prob[z][w] = s
                topic_word_prob[z] =  normalize(topic_word_prob[z])

            for d in range(len(preprocessed_documents)):
                for z in range(parameters['num_of_topic']):
                    s = 0
                    for w in range(len(vocabulary)):
                        count = term_doc_matrix[d][w]
                        s = s + count * topic_prob[d, w, z]
                    doc_topic_prob[d][z] = s
                doc_topic_prob[d] = normalize(doc_topic_prob[d])

        logging.info("Finish calculating PLSA")
        return
    except Exception as e:
        logging.exception(str(e))
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
import logging
import os
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))

params = { 'loss': 'l2', 'penalty': 'l2', 'dual': False, 'tol': 1e-3, 'C': 10 }

def train_classifier(documents):
    try:
        logging.info("Training classifier")
        clf = LinearSVC(loss=params['loss'], penalty=params['penalty'], dual=params['dual'], tol=params['tol'], C = params['C'])

        for category_id in list(documents):
            X = documents[category_id]
            y = np.full((X.shape[0], 1), category_id)

            # logging.info(X)
            # logging.info(y)
            clf.fit(X, y)

        logging.info(dir_path + '/model.pkl')
        joblib.dump(clf, 'model.pkl')
        logging.info("Finished training classifier")
    except Exception as e:
        logging.error(str(e))

def predict(documents):
    try:
        logging.info("Predicting documents")
        clf = joblib.load('model.pkl')

        logging.info("Finished predicting documents")
        return clf.predict(documents[0])
    except Exception as e:
        logging.error(str(e))
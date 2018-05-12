from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
import logging

params = { 'loss': 'l2', 'penalty': 'l2', 'dual': False, 'tol': 1e-3, 'C': 10 }

def train_classifier(documents):
    try:
        logging.info("Training classifier")
        for category_id in list(documents):
            clf = LinearSVC(loss=params['loss'], penalty=params['penalty'], dual=params['dual'], tol=params['tol'], C = params['C'])
            clf.fit(documents[category_id], category_id)

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
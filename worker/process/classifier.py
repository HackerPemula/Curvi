from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
import logging

params = { 'loss': 'l2', 'penalty': 'l2', 'dual': False, 'tol': 1e-3, 'C': 10 }

def train_classifier(documents):
    try:
        for category_id in list(documents):
            clf = LinearSVC(loss=params['loss'], penalty=params['penalty'], dual=params['dual'], tol=params['tol'], C = params['C'])
            clf.fit(documents[category_id], category_id)

        joblib.dump(clf, 'model.pkl')
    except Exception as e:
        logging.error(str(e))      

def predict(documents):
    try:
        clf = joblib.load('model.pkl')

        return clf.predict(documents[0])
    except Exception as e:
        logging.error(str(e))
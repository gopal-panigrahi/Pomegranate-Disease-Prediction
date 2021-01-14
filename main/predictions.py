import pickle
from sklearn.svm import SVC


def get_predictions(values):
    svm_linear_model = pickle.load(
        open('main/static/model/svm_model.sav', 'rb'))
    result = svm_linear_model.predict(values)[0]
    return result

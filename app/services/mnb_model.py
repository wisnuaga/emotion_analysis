import pickle
import numpy as np


class MnbModel:
    def __init__(self):
        self.labels = ['MARAH', 'JIJIK', 'TAKUT', 'SENANG', 'SEDIH', 'KAGET']
        self.tokenizer = pickle.load(open('./machine_learning/models/vectorizer_mnb_v_2_1.model', 'rb'))
        self.classifier = pickle.load(open('./machine_learning/models/classifier_mnb_v_2_1.model', 'rb'))

    def model_predict(self, data):
        tfidf_data = self.tokenizer.transform(data)
        return self.classifier.predict_proba(tfidf_data)

    def PBD(self, probs, beta=0.03):
        min_prob = min(probs)
        return min_prob + beta

    def softmax(self, curr_prob, probs):
        return np.exp(curr_prob) / np.sum(np.exp(probs))

    def percentage(self, curr_prob, probs):
        return curr_prob / np.sum(probs)
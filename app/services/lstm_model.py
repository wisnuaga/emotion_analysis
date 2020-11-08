import pickle
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences


class LstmModel:
    def __init__(self):
        self.max_length = 64
        self.trunc_type = 'post'
        self.padding_type = 'post'
        self.oov_tok = "<OOV>"
        self.labels = ['MARAH', 'JIJIK', 'TAKUT', 'SENANG', 'SEDIH', 'KAGET']
        self.model = tf.keras.models.load_model('./machine_learning/models/model_lstm.h5')
        # load tokenizer
        with open('./machine_learning/models/tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)

    def tokenize(self, data):
        try:
            data_sequences = self.tokenizer.texts_to_sequences(data)
            data_padded = np.array(pad_sequences(
                data_sequences,
                maxlen=self.max_length,
                padding=self.padding_type,
                truncating=self.trunc_type
            ))
            return data_padded
        except Exception as e:
            print('Error:', e)
            raise e

    def model_predict(self, data):
        try:
            return self.model.predict(self.tokenize(data))
        except Exception as e:
            print('Error:', e)
            raise e

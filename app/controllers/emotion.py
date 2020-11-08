from app.services.preprocessing import TextPreProcessing
from app.services.lstm_model import LstmModel


class EmotionAnalysis:
    def __init__(self):
        self.text_preprocessing = TextPreProcessing()
        self.util = LstmModel()

    def predict(self, data):
        try:
            # text pre-processing
            data = [self.text_preprocessing.process(x) for x in data]

            # predict label
            y_hat = self.util.model_predict(data)

            # convert result => {label: value}
            result = [
                {
                    'tag': label,
                    'score': float(y_hat[0][idx]).__round__(4)
                } for idx, label in enumerate(self.util.labels)
            ]

            return result
        except Exception as e:
            print('Error:', e)
            raise e

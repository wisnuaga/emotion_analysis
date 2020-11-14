from app.services.preprocessing import TextPreProcessing
from app.services.mnb_model import MnbModel
import sklearn


class EmotionAnalysisMNB:
    def __init__(self):
        self.text_preprocessing = TextPreProcessing()
        self.util = MnbModel()

    def predict(self, data):
        try:
            # text pre-processing
            data = [self.text_preprocessing.process(x) for x in data]

            # predict label
            probs = self.util.model_predict(data)[0]

            # initialize dominant threshold
            threshold = self.util.PBD(probs, 0.03)

            # initialize emotion -> value
            emotion_values = {self.util.labels[i]: v for i, v in enumerate(probs)}

            # create dominant emotion by dominant threshold
            dominant_emotion = {}
            for k, v in emotion_values.items():
                if v >= threshold:
                    dominant_emotion[k] = v

            # convert dominant emotion's value with percentage function
            dominant_emotion_percentage = {k: self.util.percentage(v, list(dominant_emotion.values()))
                                           for k, v in dominant_emotion.items()}

            # convert dominant emotion's value with softmax function
            dominant_emotion_softmax = {k: self.util.softmax(v, list(dominant_emotion.values()))
                                        for k, v in dominant_emotion.items()}

            result_dom_emotion = [
                {
                    'tag': label,
                    'score': score
                } for label, score in dominant_emotion.items()
            ]

            result_dom_emotion_percent = [
                {
                    'tag': label,
                    'score': score
                } for label, score in dominant_emotion_percentage.items()
            ]

            result_dom_emotion_softmax = [
                {
                    'tag': label,
                    'score': score
                } for label, score in dominant_emotion_softmax.items()
            ]

            # convert result => {label: value}
            result = [
                {
                    'tag': label,
                    'score': float(probs[idx])
                } for idx, label in enumerate(self.util.labels)
            ]

            return result, threshold, result_dom_emotion, result_dom_emotion_percent, result_dom_emotion_softmax
        except Exception as e:
            print('Error:', e)
            raise e

# import nltk
import pandas as pd
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# nltk.download('stopwords')


class TextPreProcessing:
    STOP_WORD = []
    NOT_WORD = []
    COMBINE_WORD = []
    NON_STEM = []
    SIGN = 'non-stem-'
    factory_stemmer = StemmerFactory()
    stemmer = factory_stemmer.create_stemmer()

    def __init__(self):
        try:
            self.STOP_WORD = set(stopwords.words('indonesian'))
            self.NON_STEM = pd.read_csv('./machine_learning/assets/non-stem.txt', header=None)[0].values
            self.NOT_WORD = pd.read_csv('./machine_learning/assets/not-word.txt', header=None)[0].values
        except FileNotFoundError as err:
            print(err)

    def remove_stop_word(self, text):
        str_result = ''
        for item in text.split():
            if item not in self.STOP_WORD:
                str_result += item + ' '
            if item in self.NOT_WORD:
                str_result += item + ' '
        return str_result

    def set_non_stem(self, text):
        str_result = ''
        for item in text.split():
            if item in self.NON_STEM:
                temp = self.SIGN + str(item)
            else:
                temp = str(item)
            str_result += temp + ' '
        return str_result

    def remove_non_stem(self, text):
        str_result = ''
        for item in text.split():
            if self.SIGN in item:
                temp = item.replace(self.SIGN, '')
            else:
                temp = item
            str_result += temp + ' '
        return str_result

    def stemming(self, text):
        return self.stemmer.stem(text)

    def process(self, text):
        text = text.lower()
        text = self.set_non_stem(text)
        text = self.stemming(text)
        text = self.remove_non_stem(text)
        # text = self.remove_stop_word(text)

        return text

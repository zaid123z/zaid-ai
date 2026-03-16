import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re

class NLPProcessor:
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))

    def tokenize(self, text):
        return word_tokenize(text)

    def remove_stopwords(self, tokens):
        return [token for token in tokens if token.lower() not in self.stopwords]

    def clean_text(self, text):
        text = re.sub(r'[^\w\s]', '', text)
        text = text.lower()
        return text
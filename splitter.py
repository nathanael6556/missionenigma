import nltk.data
from nltk.tokenize import sent_tokenize


class Splitter:
    def __init__(self):
        pass

    def split(self, data):
        pass


class NLTKSplitter:
    def __init__(self, dataset='tokenizers/punkt/english.pickle'):
        self.tokenizer = nltk.data.load(dataset)
        
    def split(self, data):
        return self.tokenizer.tokenize(data)

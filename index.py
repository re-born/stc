# -*- coding: utf-8 -*-

import codecs
from collections import defaultdict
from six.moves import cPickle
import nltk


class Indexer:

    def __init__(self):
        self.index = defaultdict(list)

    def save(self, filename):
        with open(filename, 'wb') as f:
            cPickle.dump(self.index, f, protocol=cPickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        with open(filename, 'r') as f:
            self.index = cPickle.load(f)

    def add(self, tweet_id, words):
        vocab = nltk.FreqDist(words).most_common()
        for (word, tf) in vocab:
            self.index[word].append((tweet_id, tf))

    def search(self, word):
        return self.index[word]

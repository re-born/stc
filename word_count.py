# -*- coding: utf-8 -*-

import os
from os import path
import argparse
import logging
import time
from progressbar import ProgressBar, Percentage, Bar
from collections import defaultdict
from six.moves import cPickle
import re
import MeCab
import make_dic as md

import sqlconfig
import sqltostc

if __name__ == '__main__':
    dic = defaultdict({lambda: 0})
    tweets = sqltostc.all_tweet_pairs()
    for i, tweet in enumerate(tweets):
        length = len(md.noun_list(tweet['R_TEXT']))
        dic[tweet['R_ID']] = length
    with open('./word_count.pkl', 'wb') as f:
        cPickle.dump(dic, f, protocol=cPickle.HIGHEST_PROTOCOL)


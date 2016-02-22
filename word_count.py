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

parser = argparse.ArgumentParser()
parser.add_argument('--file-path', type=str, default='./word_count.pkl')
parser.add_argument('--overwrite', type=bool, default=False)
args = parser.parse_args()

if __name__ == '__main__':
    dic = defaultdict(int)
    tweets = sqltostc.all_tweet_pairs()
    for i, tweet in enumerate(tweets):
        length = len(md.noun_list(tweet['R_TEXT']))
        dic[tweet['R_ID']] = length
    with open(args.file_path, 'wb') as f:
        cPickle.dump(dic, f, protocol=cPickle.HIGHEST_PROTOCOL)


# -*- coding: utf-8 -*-

import os
from os import path
import argparse
import logging
import time
from progressbar import ProgressBar, Percentage, Bar
from collections import defaultdict
from six.moves import cPickle
import MeCab

import sqlconfig
import sqltostc

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('make_dic')

parser = argparse.ArgumentParser()
parser.add_argument('--file-path', type=str, default='./tweet_dic.pkl')
parser.add_argument('--overwrite', type=bool, default=False)
args = parser.parse_args()


def make_dic(tweet, reply, dic):
    t_list = noun_list(tweet)
    r_list = noun_list(reply)
    for x in xrange(0, len(t_list) - 1):
        if t_list[x] in dic:
            dic[t_list[x]][t_list[x + 1]] += 1
            for y in r_list:
                dic[t_list[x]][y] += 1
        else:
            dic[t_list[x]] = defaultdict(int)
            dic[t_list[x]][t_list[x + 1]] += 1
            for y in r_list:
                dic[t_list[x]][y] += 1

    for x in xrange(0, len(r_list) - 1):
        if r_list[x] in dic:
            dic[r_list[x]][r_list[x + 1]] += 1
        else:
            dic[r_list[x]] = defaultdict(int)
            dic[r_list[x]][r_list[x + 1]] += 1


def remove_twitter_id(text):
    ids = re.findall(r'@\w+',text)
    for id in ids:
        text = text.replace(id, '')
    #先頭のreply_idの直後にwhite_spaceが残るので削除
    return text.replace(' ','')

def noun_list(text):
    arr = []
    content = [r'固有名詞', r'一般', r'サ変動詞', r'形容動詞語幹']
    tagger = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    text = remove_twitter_id(text)
    encode_text = text.encode('utf-8')
    node = tagger.parseToNode(encode_text)
    while node:
        feature = node.feature
        speech = feature.split(",")[0]
        detail = feature.split(",")[1]
        if (speech in [r'名詞']) and (detail in content):
            arr.append(node.surface)
        node = node.next
    return arr


def save_dic(file_path):
    logger.info('SQL running...')
    start = time.time()
    dic = {}
    tweets = sqltostc.all_tweet_pairs()
    elapsed_time = time.time() - start
    logger.info('sql_time:{0}[sec]'.format(elapsed_time))

    logger.info('Making Dic...')
    start = time.time()
    p = ProgressBar(widgets=[Percentage(), Bar()], maxval=len(tweets)).start()
    for i, tweet in enumerate(tweets):
        make_dic(tweet['P_TEXT'], tweet['R_TEXT'], dic)
        p.update(i + 1)
    p.finish()
    elapsed_time = time.time() - start
    logger.info('making_time:{0}[sec]'.format(elapsed_time))

    logger.info('Saving...')
    with open(file_path, 'wb') as f:
        cPickle.dump(dic, f, protocol=cPickle.HIGHEST_PROTOCOL)
    logger.info('Done')


if __name__ == '__main__':
    if path.isfile(args.file_path):
        logger.info('{} already exists'.format(args.file_path))
        if args.overwrite:
            logger.info('overwrite flag is True')
            save_dic(args.file_path)
    else:
        dirname = path.dirname(args.file_path)
        if not path.isdir(dirname):
            logger.info('create {}'.format(dirname))
            os.mkdir(dirname)
        save_dic(args.file_path)

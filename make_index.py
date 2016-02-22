#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import path
import argparse
import logging
import time
from progressbar import ProgressBar, Percentage, Bar

from stcutils import noun_list
import sqlconfig
from sqltostc import read_table
from index import Indexer

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('make_index')

parser = argparse.ArgumentParser()
parser.add_argument('--file-path', type=str, default='./index.pkl')
parser.add_argument('--overwrite', type=bool, default=False)
parser.add_argument('--only-reply', type=bool, default=False)
args = parser.parse_args()


def get_query(only_reply):
    if only_reply:
        return "SELECT t.item_id, t.text FROM stc_tweet_ids AS ids INNER JOIN stc_tweets AS t ON ids.reply_id = t.item_id WHERE t.success = 1"
    else:
        return "SELECT item_id, text FROM " + sqlconfig.tweet_table_name + " WHERE success = 1"


def save_index(file_path):
    query = get_query(args.only_reply)
    logger.info('query: {}'.format(query))

    logger.info("SQL running...")
    start = time.time()
    rows = read_table(query)
    elapsed_time = time.time() - start
    logger.info("sql_time:{0}[sec]".format(elapsed_time))

    logger.info("Indexing...")
    start = time.time()
    p = ProgressBar(widgets=[Percentage(), Bar()], maxval=len(rows)).start()
    indexer = Indexer()
    for i, row in enumerate(rows):
        indexer.add(row[0], noun_list(row[1]))
        p.update(i + 1)
    p.finish()
    elapsed_time = time.time() - start
    logger.info("indexing_time:{0}[sec]".format(elapsed_time))

    logger.info("Saving...")
    indexer.save(file_path)
    logger.info('Done')


if __name__ == "__main__":
    if args.only_reply:
        file_path = './only_reply_index.pkl'
    else:
        file_path = args.file_path
    if path.isfile(file_path):
        logger.info('{} already exists'.format(file_path))
        if args.overwrite:
            logger.info('overwrite flag is True')
            save_index(file_path)
    else:
        dirname = path.dirname(file_path)
        if not path.isdir(dirname):
            logger.info('create {}'.format(dirname))
            os.mkdir(dirname)
        save_index(file_path)

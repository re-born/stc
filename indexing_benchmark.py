#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import path
import argparse
import logging
import time
from progressbar import ProgressBar, Percentage, Bar

from make_dic import noun_list
import sqlconfig
from sqltostc import read_table
from index import Indexer

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
# select count(*) from stc_tweets where success = 1;
# 921314
parser.add_argument('--max-id', type=int, default=100)
args = parser.parse_args()


def main():
    max_id = str(args.max_id)
    logger.info("MAX:{}".format(max_id))

    query = "select item_id, text from " + sqlconfig.tweet_table_name + \
        " where id <= " + max_id + " and success = 1"

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

    indexer.save("./index.pkl")


if __name__ == "__main__":
    main()

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import path
import argparse
import logging
import time
from progressbar import ProgressBar, Percentage, Bar

import sqlconfig
from sqltostc import read_table
from stcutils import Tweet
from make_dic import noun_list


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('check_tweet')

parser = argparse.ArgumentParser()
parser.add_argument('ids', type=str, nargs='+')
args = parser.parse_args()


def main():
    for item_id in args.ids:
        t = Tweet(item_id)
        logger.info('ITEM_ID:{0}, TEXT:{1}'.format(t.item_id, t.text.encode('utf-8')))
        for word in noun_list(t.text):
            logger.info('  {}'.format(word))


if __name__ == '__main__':
    main()

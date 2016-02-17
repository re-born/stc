# -*- coding: utf-8 -*-
"""Testing for Index"""

import os
import sys

sys.path.append(os.getcwd())

from unittest import TestCase
import nose
from nose.tools import eq_

from index import Indexer


class IndexerTestCase(TestCase):

    def setUp(self):
        print ""

    def test_save_and_load(self):
        indexer = Indexer()
        indexer.add("1", ["今日", "天気", "晴れ"])
        indexer.add("2", ["今日", "天気", "雨"])

        indexer.save("./tests/index.pkl")
        indexer.load("./tests/index.pkl")

        tweet_ids = indexer.search("今日")
        eq_(tweet_ids[0], "1")
        eq_(tweet_ids[1], "2")

        tweet_ids = indexer.search("雨")
        eq_(len(tweet_ids), 1)
        eq_(tweet_ids[0], "2")

    def tearDown(self):
        print "done"

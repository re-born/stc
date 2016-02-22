# -*- coding: utf-8 -*-
"""Testing for Utils"""


import os
import sys
import ipdb

sys.path.append(os.getcwd())

from unittest import TestCase
import nose
from nose.tools import eq_

from stcutils import Tweet


class UtilsTestCase(TestCase):

    def setUp(self):
        print ""

    def test_testing_tweet(self):
        item_id = '554564419162619904'
        t = Tweet(item_id)
        eq_(t.item_id, item_id)
        text = u'@take8823 三光堂さんにて、ポスター等置かせていただいたお礼を兼ねて、ご報告させていただきました。結構お持ちになられた方がいらしたようです。'
        eq_(t.text, text)

    def test_taskdata_tweet(self):
        item_id = '427930108028923905'
        t = Tweet(item_id)
        eq_(t.item_id, item_id)
        # ipdb.set_trace()
        text = u'@haramonera 遅れましたフォローサンクスです！'
        eq_(t.text, text)

    def tearDown(self):
        print "done"

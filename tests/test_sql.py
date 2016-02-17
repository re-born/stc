"""Testing for SQL"""


import os
import sys

sys.path.append(os.getcwd())

from unittest import TestCase
import nose
from nose.tools import eq_

import sqlconfig
from sqltostc import read_table


class SQLTestCase(TestCase):

    def setUp(self):
        print ""

    def test_sql_to_table(self):
        query = "select * from " + sqlconfig.id_table_name
        print query
        rows = read_table(query)
        eq_(len(rows), 500000)

    def tearDown(self):
        print "done"

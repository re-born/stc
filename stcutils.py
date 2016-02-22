# -*- coding: utf-8 -*-

import MeCab

import sqlconfig
from sqltostc import read_table

class RunFile():
    """
    <teamID>-J-R[priority].txt
    <SYSDESC>[insert a short description in English here]</SYSDESC>
    [TweetID] 0 [RetrievedTweetID] [Rank] [Score][RunName]
    """

    def __init__(self, team_id, priority):
        self.team_id = team_id
        self.priority = priority
        self.results = []

    def set_desc(self, text):
        self.description = text

    def add(self, result):
        self.results.append(result)

    def format_for_stc(result):
        # TODO
        # convert result to formated text
        return text_formated

    def save(self):
        filename = '{0}-J-R{1}.txt'.format(self.team_id, self.priority)
        with open(filename, 'wb') as f:
            f.write('<SYSDESC>{}</SYSDESC>\n'.format(self.description))
            lines = [format_for_stc(result) for result in self.results]
            text = '\n'.join(lines)
            f.write(text)


class Tweet():
    """Tweet class For Debug"""

    def __init__(self, item_id):
        if not self.get_and_set_tweet('test_tweets', item_id):
            self.get_and_set_tweet('stc_tweets', item_id)

    def get_and_set_tweet(self, table_name, item_id):
        query = 'select * from {0} where item_id = {1}'.format(table_name, item_id)
        rows = read_table(query)
        if len(rows) is 1:
            self.set_tweet(rows[0])
            return True
        else:
            return False

    def set_tweet(self, row):
        self.id = row[0]
        self.success = row[1]
        self.item_id = row[2]
        self.screen_name = row[3]
        self.name = row[4]
        self.time = row[5]
        self.text = row[6]

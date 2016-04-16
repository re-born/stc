# -*- coding: utf-8 -*-

import os.path
import re
import MeCab
from collections import defaultdict

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

    def add_text_to_results(self, tweet_dic):
        for input_id in self.results:
            for rank in self.results[input_id]["replies"]:
                output_id = self.results[input_id]["replies"][rank]["tweet_id"]
                output_text = tweet_dic[output_id]
                self.results[input_id]["replies"][rank]["text"] = output_text

            # May be, tweet_dic not includes tweets of testdata
            self.results[input_id]["text"] = Tweet(input_id).text

    def add_label_to_results(self, label_dic):
        for input_id in self.results:
            for rank in self.results[input_id]["replies"]:
                output_id = self.results[input_id]["replies"][rank]["tweet_id"]
                if label_dic[input_id].has_key(output_id):
                    self.results[input_id]["replies"][rank][
                        "labels"] = label_dic[input_id][output_id]

    @staticmethod
    def load(file_path):
        if not os.path.isfile(file_path):
            return false

        file_name = os.path.basename(file_path)
        team_id = file_name[:5]
        priority = file_name[9:10]
        run = RunFile(team_id, priority)

        f = open(file_path)
        lines = f.readlines()
        f.close()

        results = defaultdict(dict)
        for line in lines[1:]:
            data = line.split()
            input_id = data[0]
            output_id = data[2]
            rank = data[3]
            score = data[4]
            if not results[input_id].has_key("replies"):
                results[input_id]["replies"] = {}
            results[input_id]["replies"][rank] = {
                "tweet_id": output_id,
                "score": score
            }

        run.results = results
        return run


class Label(defaultdict):

    def __init__(self, file_path):
        defaultdict.__init__(self, dict)
        self.src = file_path

        if not os.path.isfile(file_path):
            return

        f = open(file_path)
        lines = f.readlines()
        f.close()

        for line in lines:
            data = line.replace("\n", "").split("\t")
            input_id = data[0]
            output_id = data[1]
            labels = data[2:]
            self[input_id][output_id] = labels


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

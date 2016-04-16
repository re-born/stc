#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import logging
import pprint
from six.moves import cPickle
from collections import Counter

from sqltostc import all_tweets


logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument('--dump-file', type=str, required=True)


def write_results(file_path, results):
    with open(file_path, "w") as f:
        for input_id in results:
            f.write("入力ツイート\n")
            f.write("ID:" + input_id + "\n")
            f.write(results[input_id]["text"].encode("utf-8") + '\n\n')

            replies = results[input_id]["replies"]
            sorted_replies = sorted(replies.items(), key=lambda x: int(x[0]), reverse=False)

            f.write("出力ツイート\n")
            for reply in sorted_replies:
                f.write("ランク：" + reply[0] + '\n')
                f.write("ID:" + reply[1]["tweet_id"] + "\n")
                f.write("スコア：" + reply[1]["score"] + '\n')
                f.write("テキスト\n")
                f.write(reply[1]["text"].encode("utf-8") + '\n')
                if reply[1].has_key("labels"):
                    f.write("ラベル\n")
                    f.write(" ".join(reply[1]["labels"]) + '\n')

            f.write("===========================\n\n\n\n\n\n")


def print_most_reply_tweet(results):

    tweet_dic = all_tweets()

    counter = Counter()
    tweet_ids = []
    for input_id in results:
        for rank in results[input_id]["replies"]:
            tweet_id = results[input_id]["replies"][rank]["tweet_id"]
            tweet_ids.append(tweet_id)

    counter = Counter(tweet_ids)
    tweet_ids = counter.most_common(10)

    for tweet_id, tf in tweet_ids:
        print tweet_id
        print str(tf) + "回"
        print tweet_dic[tweet_id]
        print ""


if __name__ == "__main__":
    logger = logging.getLogger("output_result")
    args = parser.parse_args()

    if not os.path.isfile(args.dump_file):
        logger.error("{} is not file".format(args.dump_file))
        os.exit(1)

    output_file = args.dump_file + ".txt"

    with open(args.dump_file, 'r') as f:
        results = cPickle.load(f)
        write_results(output_file, results)
        print_most_reply_tweet(results)

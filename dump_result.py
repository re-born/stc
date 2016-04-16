#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import logging
from six.moves import cPickle
from collections import Counter

from sqltostc import all_tweets
from stcutils import RunFile, Label

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument('--run-file', type=str, required=True)


def result_dump(run_file_path="results/SLSTC-STC/SLSTC-J-R2.txt", label_file_path="results/test-final-labeled.txt", output_dir="outputs"):

    logger.info("Loading {}".format(run_file_path))
    run = RunFile.load(run_file_path)

    logger.info("Fetching all tweets")
    tweet_dic = all_tweets()
    run.add_text_to_results(tweet_dic)

    logger.info("Loading {}".format(label_file_path))
    label_dic = Label(label_file_path)
    run.add_label_to_results(label_dic)

    run_file_name = os.path.basename(run_file_path)
    dump_file_path = os.path.join(output_dir, run_file_name + ".dump")

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    logger.info("Saving {}".format(dump_file_path))

    with open(dump_file_path, 'wb') as f:
        cPickle.dump(run.results, f, protocol=cPickle.HIGHEST_PROTOCOL)

    return dump_file_path


if __name__ == "__main__":
    logger = logging.getLogger("dump_result")
    args = parser.parse_args()

    dump_file = result_dump(args.run_file)

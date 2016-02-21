# -*- coding: utf-8 -*-

from collections import defaultdict
import make_dic as md
from subnetwork import SubNetwork
from indexer import Indexer
from six.moves import cPickle
from sqltostc import all_tweets
import sqlconfig

def retrieve_replies(input):
  text = input
  noun_list = md.noun_list(text)
  net = SubNetwork()
  with open('tweet_dic.pkl', 'r') as f:
    source_dic = cPickle.load(f)

  net.set_source(source_dic)
  net.gen_sub_network(noun_list)
  queries = net.page_rank()
  
  indexer = Indexer()
  indexer.load("./index.pkl")
  
  results = defaultdict(int)
  for query in queries:
    word = query
    score = queries[word]
    tuple_list = indexer.search(word)
    for tup in tuple_list:
        results = indexer.update_replies(results, tup, score)
        
  show_results(results)
  
def show_results(results):
    print results

def test_data():
    return all_tweets(sqlconfig.run_table_name)
    
def main():
    inputs = test_data()
    for input in inputs:
        retrieve_replies(iput)

if __name__ == '__main__':
  main()
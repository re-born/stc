# -*- coding: utf-8 -*-

from collections import defaultdict
import make_dic as md
import SubNetwork
from six.moves import cPickle

def main():
  text = text
  noun_list = md.noun_list(text)
  net = SubNetwork()
  with open('tweet_dic.pkl', 'r') as f:
    source_dic = cPickle.load(f)

  net.set_source(source_dic)
  net.gen_sub_network(noun_list)
  queries = net.page_rank()
  
  indexer = Indexer()
  indexer.load("./index.pkl")
  tuple_list = indexer.search(query)
  
  results = indexer.possible_replies(query)
  show_results(results)
  
def show_results(results):
    print results


if __name__ == '__main__':
  main()
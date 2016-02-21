# -*- coding: utf-8 -*-

from collections import defaultdict
import make_dic as md
from subnetwork import SubNetwork
from index import Indexer
from six.moves import cPickle
from sqltostc import all_tweets
import sqlconfig


net = SubNetwork()
print "load tweet pairs....."
with open('tweet_dic.pkl', 'r') as f:
    source_dic = cPickle.load(f)
net.set_source(source_dic)
print "Tweet Pairs loaded: len(pairs) -> " + str(len(source_dic))
print "load index....."
indexer = Indexer()
indexer.load("./index.pkl")
print "Index loaded"

def retrieve_replies(input):
  text = input
  noun_list = md.noun_list(text)

  net.gen_sub_network(noun_list)
  queries = net.page_rank()
  
  results = defaultdict(int)
  for query in queries:
    word = query
    score = queries[word]
    tuple_list = indexer.search(word)
    for tup in tuple_list:
        results = indexer.update_replies(results, tup, score)
  results = tuples_from_dict(results)
  return results
    
def tuples_from_dict(dic):
    return sorted(dic.items(), key=lambda x:x[1], reverse=False)

def test_data():
    return all_tweets(sqlconfig.run_table_name)
    
def main():
    tuples = []
    inputs = test_data()
    tweet_num = len(inputs)
    for (i,input) in enumerate(inputs):
        print "STCINFO: " + str(i) + " of " + str(tweet_num) + "@Twitter ID ->" + input
        replies = [(input,) + tup for tup in retrieve_replies(inputs[input])]
    f = open('replies.txt', 'w')
    for i in range(10):
        f.write(str(replies[i]) + '\n')
        tuples.append(replies[i])
    print tuples[0]
    f.close()

if __name__ == '__main__':
  main()

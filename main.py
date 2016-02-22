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
print "word count / tweet dic....."
with open('./word_count.pkl', 'r') as f:
    wc_dic = cPickle.load(f)
print "dic loaded"


def retrieve_replies(input):
  text = input
  noun_list = md.noun_list(text)

  net.gen_sub_network(noun_list)
  queries = net.page_rank()
  
  results = {}
  results = defaultdict(int)
  for query in queries:
    word = query
    score = queries[word]
    tuple_list = indexer.search(word)
    for tup in tuple_list:
        results = indexer.update_replies(results, tup, score)
  results = tuples_from_dict(normalize(results, wc_dic))
  return results
#  return normalize(results, wc_dic)
    
def tuples_from_dict(dic):
    return sorted(dic.items(), key=lambda x:x[1]*100000, reverse=True)

def normalize(results, dic):
    for tweet in results:
        results[tweet] = results[tweet] / (dic[tweet] + 1)
    return results

def test_data():
    return all_tweets(sqlconfig.run_table_name)
    
def main():
    tuples = []
    inputs = test_data()
    input_keys = inputs.keys()[:6]
    tweet_num = len(input_keys)
    f = open('replies.txt', 'w')
    for (i,input) in enumerate(input_keys):
        print "STCINFO: " + str(i+1) + " of " + str(tweet_num) + "@Twitter ID ->" + input
        replies = [(input,) + tup for tup in retrieve_replies(inputs[input])]
        for i in range(10):
            f.write(str(replies[i]) + '\n')
            tuples.append(replies[i])
    f.close()

if __name__ == '__main__':
  main()

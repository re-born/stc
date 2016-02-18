# -*- coding: utf-8 -*-

from collections import defaultdict
import MeCab
import sqlconfig
from sqltostc
from six.moves import cPickle

def make_dic(tweet, reply, dic):
  t_list = noun_list(tweet)
  r_list = noun_list(reply)
  for x in xrange(0,len(t_list)-1):
    if t_list[x] in dic:
      dic[t_list[x]][t_list[x+1]] += 1
      for y in r_list:
        dic[t_list[x]][y] += 1
    else:
      dic[t_list[x]] = defaultdict(lambda:0)
      dic[t_list[x]][t_list[x+1]] += 1
      for y in r_list:
        dic[t_list[x]][y] += 1

  for x in xrange(0,len(r_list)-1):
    if r_list[x] in dic:
      dic[r_list[x]][r_list[x+1]] += 1
    else:
      dic[r_list[x]] = defaultdict(lambda:0)
      dic[r_list[x]][r_list[x+1]] += 1

def noun_list(text):
  arr = []
  tagger = MeCab.Tagger("-Ochasen")
  encode_text = text.encode('utf-8')
  node = tagger.parseToNode(encode_text)
  while node:
    feature = node.feature
    speech = feature.split(",")[0]
    if speech in [r'名詞']:
      arr.append(node.surface)
    node = node.next
  return arr


if __name__ == '__main__':
  dic = {}
  tweet = u"私は早稲田大学でコンピューターの勉強をしています"
  reply = u"私はコンピューター全然わからないので来月教えて下さい。お礼にラーメンをごちそうします。"
  tweets = sqldata
  for tweet in tweets:
    make_dic(tweet.P_text,tweet.R_text,dic)
  with open(filename, 'wb') as f:
            cPickle.dump(dic, f, protocol=cPickle.HIGHEST_PROTOCOL)


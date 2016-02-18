# -*- coding: utf-8 -*-

from collections import defaultdict
import make_dic as md
import SubNetwork
from six.moves import cPickle

def main():
  text = text
  noun_list = md.noun_list(text)
  net = new SubNetwork()
  with open(filename, 'r') as f:
    source_dic = cPickle.load(f)

  net.set_source(source_dic)
  net.gen_sub_network(noun_list, distance)



if __name__ == '__main__':
  main()
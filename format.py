# -*- coding: utf-8 -*- 

import sys

if __name__ == "__main__":
    rank = 1
    filename = sys.argv[1]
    for line in open(filename, 'r'):
      if rank > 10:
        rank = 1
      line = line.replace('(', '').replace(')', '').replace('u', '').replace('\'', '').replace('\n', '')
      array = line.split(',')
      print str(int(array[0])) + " 0 " + str(int(array[1])) + " " + str(rank) + " " + str(array[2]) + " SLSTC-J-R2"
      rank += 1
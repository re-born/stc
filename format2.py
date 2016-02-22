# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    for line in open(filename, 'r'):
        line = line.replace('(', '').replace(')', '').replace(
            'u', '').replace('\'', '').replace('\n', '')
        array = line.split()
        print ' '.join(array)

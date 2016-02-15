#-*- coding: utf-8 -*-
import sys
import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()

def is_empty(l):
    return 0 == len(l)
    
def init_seeds(words):
    seeds = []
    seeds.append(words)
    return seeds
    
def sub_network(dic, start_words):
    seeds = init_seeds(start_words)
    while not is_empty(seeds):
        words = seeds.pop(0)
        for word in words:
            if dic.has_key(word):
                nodes = dic[word]
                add_all_edge(word, nodes)
                
def add_all_edge(start_word, nodes):
    for word in nodes.keys():
        value = nodes[word]
        g.add_edge(start_word, word, weight=value)

def draw_graph():
    if is_empty(nx.nodes(g)):
        return "Graph has no nodes. Please make subnetwork before drawing."
    pos = nx.spring_layout(g)
    nx.draw_networkx_labels(g, pos, font_size=16, font_color="b")
    nx.draw(g, pos)
    plt.show()
    return "Graph was shown."
    
if __name__ == '__main__':
    print "start testing"
    dic = {}
    dic["A"] = {}
    dic["A"]["C"] = 2
    dic["A"]["D"] = 1
    dic["B"] = {}
    dic["B"]["A"] = 1
    print "####dic structure####"
    print dic
    print "#################"
    sub_network(dic, ["A"])
    err = draw_graph()
    print err
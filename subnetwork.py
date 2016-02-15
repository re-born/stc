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
    
def is_neighbor_needed(remained):
    return remained > 0

def no_neighbor_needed(remained):
    return remained < 0
    
def sub_network(dic, start_words, distance):
    seeds = init_seeds(start_words)
    while not is_empty(seeds):
        distance -= 1
        next_seed = []
        words = seeds.pop(0)
        if no_neighbor_needed(distance):
            return "No edges were generated"
        for word in words:
            if dic.has_key(word):
                nodes = dic[word]
                add_all_edge(word, nodes)
                next_seed.extend(node_words(nodes))
        if is_neighbor_needed(distance):
            seeds.append(next_seed)

def node_words(nodes):
    return nodes.keys()
                
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
    dic["A"]["B"] = 2
    dic["A"]["D"] = 1
    dic["B"] = {}
    dic["B"]["C"] = 1
    dic["B"]["E"] = 1
    print "####dic structure####"
    print dic
    print "#################"
    print "input: distance"
    N = input()
    sub_network(dic, ["A"], N)
    err = draw_graph()
    print err
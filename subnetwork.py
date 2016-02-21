#-*- coding: utf-8 -*-
import sys
import networkx as nx
import matplotlib.pyplot as plt
from progressbar import ProgressBar


def is_empty(l):
    return len(l)==0

class SubNetwork(object):
    __graph = nx.DiGraph()
    __source = {}
    def __init__(self):
        pass
        
    def set_source(self, source):
        self.__source = source
        
    def __init_seeds(self, words):
        seeds = []
        seeds.append(words)
        return seeds
        
    def __is_neighbor_needed(self, remained):
        return remained > 0

    def __no_neighbor_needed(self, remained):
        return remained < 0
        
    def gen_sub_network(self, start_words, distance="2"):
        distance = int(distance)
        source = self.__source
        seeds = self.__init_seeds(start_words)
        while not is_empty(seeds):
            distance -= 1
            next_seed = []
            words = seeds.pop(0)
            p = ProgressBar(len(words))
            if self.__no_neighbor_needed(distance):
                self.add_all_nodes(words)
                return "No edges were generated"
            for (i,word) in enumerate(words):
                p.update(i+1)
                if source.has_key(word):
                    nodes = source[word]
                    self.add_all_edge(word, nodes)
                    next_seed.extend(self.__node_words(nodes))
            if self.__is_neighbor_needed(distance):
                seeds.append(next_seed)

    def __node_words(self, nodes):
        return nodes.keys()
                    
    def add_all_edge(self, start_word, nodes):
        for word in self.__node_words(nodes):
            value = nodes[word]
            self.__graph.add_edge(start_word, word, weight=value)
            
    def add_all_nodes(self, words):
        for word in words:
            self.__graph.add_node(word)

    def draw_graph(self):
        if is_empty(nx.nodes(self.__graph)):
            return "Graph has no nodes. Please make subnetwork before drawing."
        pos = nx.spring_layout(self.__graph)
        nx.draw_networkx_labels(self.__graph, pos, font_size=16, font_color="b")
        nx.draw(self.__graph, pos)
        plt.show()
        return "Graph was shown."
        
    def page_rank(self,alpha = "0.9"):
        alpha = float(alpha)
        return nx.pagerank(self.__graph, alpha)
        
    def nodes(self):
        return nx.nodes(self.__graph)
        
    def edges(self):
        return nx.edges(self.__graph)
        
    def show_source(self):
        print "####dic structure####"
        print self.__source
        print "#################"
        
if __name__ == '__main__':
    print "start testing"
    dic = {}
    dic["A"] = {}
    dic["A"]["B"] = 2
    dic["A"]["D"] = 1
    dic["B"] = {}
    dic["B"]["C"] = 1
    dic["B"]["E"] = 1
    
    network = SubNetwork()
    network.set_source(dic)
    network.show_source()
    
    print "input: distance"
    N = input()
    
    network.gen_sub_network(["A"], N)
    print network.nodes()
    print network.edges()
    print network.pagerank()
    err = network.draw_graph()
    print err

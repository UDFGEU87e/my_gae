import numpy as np
import sys
import pickle as pkl
#import networkx as nx
import scipy.sparse as sp


def parse_index_file(filename):
    index = []
    for line in open(filename):
        index.append(int(line.strip()))
    return index


def load_data(dataset):
    # load the data: x, tx, allx, graph
    with open('./data/'+dataset+'_adj.pkl', 'rb') as f1:
        adj = pkl.load(f1)
    # load adjacency matrix 
    with open('./data/yale_feats.pkl', 'rb') as f2:
        features = pkl.load(f2,encoding='latin1')
    return adj, features

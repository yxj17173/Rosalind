#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Graph Algorithms
import itertools
from collections import OrderedDict


def fun(file_name):
    seq = OrderedDict()
    f = open(file_name, 'rt')
    for line in f:
        line = line.rstrip()
        if line.startswith('>'):
            seqName = line[1:]
            seq[seqName] = ''
            continue
        seq[seqName] += line
    return seq

def is_k_overlap(s1, s2, k):
    return s1[-k:] == s2[:k]

def k_edges(data, k):
    edges = []
    # data 里面任意取两个比较
    for u, v in itertools.combinations(data, 2):
    #You may return edges in any order, so no need to use permutation
        u_dna, v_dna = data[u], data[v]
        if is_k_overlap(u_dna, v_dna, k):
            edges.append((u, v))
        if is_k_overlap(v_dna, u_dna, k):
            edges.append((v, u))
    fh = open("result_grpht.txt", "w+")
    for item in edges:
        result = str(item).replace("(", "").replace(")", "").replace("'", "").replace(",", "")+"\n"
        fh.write(result)
    fh.close()
    return edges

if __name__ == '__main__':
    print(k_edges(fun("rosalind_grph.txt"), 3))

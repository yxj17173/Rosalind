#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# String Algorithms
from collections import Counter
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
    sequences = list(seq.values())

    A, C, G, T = [], [], [], []
    result = ""
    for i in range(len(sequences[0])):
        series = ""
        for j in sequences:
            series += j[i]
        A.append(series.count('A'))
        C.append(series.count('C'))
        G.append(series.count('G'))
        T.append(series.count('T'))
        counts = Counter(series)
        result += counts.most_common()[0][0]
    fh = open("result_cons.txt", "w+")
    fh.write(result + '\n')
    fh.write('\n'.join(['A:\t' + '\t'.join(map(str, A)), 'C:\t' + '\t'.join(map(str, C)),
                        'G:\t' + '\t'.join(map(str, G)), 'T:\t' + '\t'.join(map(str, T))]))
    fh.close()

if __name__ == '__main__':
    fun("rosalind_cons.txt")

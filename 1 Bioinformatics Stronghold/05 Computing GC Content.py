#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# String Algorithms
from operator import itemgetter
from collections import OrderedDict


def fun(file_name):
    seqTest = OrderedDict()
    gcContent = OrderedDict()
    f = open(file_name, 'rt')
    for line in f:
        #print(line)
        line = line.rstrip()
        if line.startswith('>'):
            seqName = line[1:]
            seqTest[seqName] = ''
            continue
        seqTest[seqName] += line.upper()

    for key, value in seqTest.items():
        Length = len(value)
        gcNumber = value.count('G') + value.count('C')
        gcContent[key] = (float(gcNumber) / Length) * 100
    sortedGCContent = sorted(gcContent.items(), key=itemgetter(1))
    largeName = sortedGCContent[-1][0]
    largeGCContent = sortedGCContent[-1][1]
    print('most GC ratio gene is %s and it is %s ' % (largeName, largeGCContent))


if __name__ == '__main__':
    fun("rosalind_GC.txt")

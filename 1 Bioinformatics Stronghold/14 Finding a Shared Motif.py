#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# String Algorithms
# Use Dynamics Programming to optimize!!!!!!!!!!!!!!!!!!!!
import datetime
from collections import OrderedDict


startTime = datetime.datetime.now()
def readfasta(file_name):
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
 
def fragement(seq_list):
    result = []
    seq = seq_list[0]
    for i in range(len(seq)):
        s_seq = seq[i:]
        for j in range(len(s_seq)):
            result.append(s_seq[:(len(s_seq) - j)])
    return result
 
def main(infile):
    seq = readfasta(infile)
    seq_list = list(seq.values())
    frags = fragement(seq_list)
    frags.sort(key=len, reverse=True)
    for i in range(len(frags)):
        ans = []
        # s = 0
        # m+=1
        # print(m)
        # res[frags[i]] = 0
        for j in seq_list:
            r = j.count(frags[i])
            if r != 0:
                ans.append(r)
        if len(ans) >= len(seq_list):
            print(frags[i])
            break
 
if __name__ == '__main__':
    #main("test.txt")
    main("rosalind_lcsm.txt")

endTime = datetime.datetime.now()
Time = endTime - startTime
print(Time)
#0:01:13.611611

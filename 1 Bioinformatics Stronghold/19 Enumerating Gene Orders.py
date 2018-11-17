#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Combinatorics, Genome Rearrangements
import itertools


def fun(file_name):
    f = open(file_name, "rt").read().rstrip().replace("\n", "")
    fh = open("result_perm.txt", "w+")
    num = int(f)
    perm = list(itertools.permutations(range(1, num+1), num))
    fh.write(str(len(perm)) + "\n")
    for item in perm:
        result = ' '.join(map(str, list(item))) + "\n"
        fh.write(result)
    fh.close()
if __name__ == '__main__':
    #fun("test.txt")
    fun("rosalind_perm.txt")

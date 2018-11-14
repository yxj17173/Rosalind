#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Alignment
# Hamming distance
import linecache


def fun(file_name):
    string0 = linecache.getlines(file_name)[0]
    string1 = linecache.getlines(file_name)[1]
    length = len(string0)
    count = 0 
    for i in range(length):
        if string0[i] != string1[i]:
            count += 1
    return count

if __name__ == '__main__':
    print(fun("rosalind_hamm.txt"))

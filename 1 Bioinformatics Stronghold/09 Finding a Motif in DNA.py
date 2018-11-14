#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# String Algorithms
import linecache


def fun(file_name):
    # .rstrip() is essnetial
    seq = linecache.getlines(file_name)[0].rstrip()
    pattern = linecache.getlines(file_name)[1].rstrip()
    result = ""
    for i in range(len(seq)-len(pattern)):
        if seq[i : i+len(pattern)] == pattern:
            result += str(i+1)+ " "
    return result


if __name__ == '__main__':
    print(fun("rosalind_subs.txt"))




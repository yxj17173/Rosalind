#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import linecache

def fun(file_name):
    string = len(open(file_name, "rt").readlines())
    f = open("result_05.txt","w+")
    for i in range(string):
        if i % 2 == 1:
            f.write(linecache.getlines(file_name)[i])
    f.close()
    
if __name__ == '__main__':
    print(fun("rosalind_ini5.txt"))
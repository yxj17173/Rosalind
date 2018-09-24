#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import linecache

def fun(file_name):
    string = linecache.getlines(file_name)[0]
    print(string)
    num = linecache.getlines(file_name)[1].replace("\n","").split(" ")
    print(num)
    print(string[1:2])
    a = string[int(num[0]):int(num[1])+1]
    b = string[int(num[2]):int(num[3])+1]
    return a, b

if __name__ == '__main__':
    print(fun("rosalind_ini3.txt"))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun(file_name):
    values = open(file_name, "rt").read().split()
    a = int(values[0])
    b = int(values[1])
    sum = 0
    for i in range(a,b+1):
        if i % 2 == 1:
            sum += i

    return sum

if __name__ == '__main__':
    print(fun("rosalind_ini4.txt"))
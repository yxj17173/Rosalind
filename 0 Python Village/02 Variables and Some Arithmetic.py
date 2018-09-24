#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun(file_name):
    values = open(file_name, "rt").read().split()
    a = int(values[0])
    b = int(values[1])
    return a**2 + b**2

if __name__ == '__main__':
    print(fun("rosalind_ini2.txt"))
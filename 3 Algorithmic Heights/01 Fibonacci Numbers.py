#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fibonacci(n):
    if n == 0:
        result = 0
    elif n ==1:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

def fun(file_name):
    values = int(open(file_name, "rt").read())
    print(fibonacci(values))
    return None

if __name__ == '__main__':
    fun("rosalind_fibo.txt")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fibonacci(n,k):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n-1,k) + k * fibonacci(n-2,k)
    return result


def fun(file_name):
    values = open(file_name, "rt").read().split(" ")
    print(fibonacci(int(values[0]), int(values[1])))
    return None


if __name__ == '__main__':
    fun("rosalind_fib.txt")

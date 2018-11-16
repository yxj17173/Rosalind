#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Combinatorics, Dynamic Programming


def fibd(n, m):
    s = [0]*(m+1)  # s[0]=每个月出生的兔子,s[k]=每个月死的兔子
    s[0] = 1  # 初始值
    for x in range(1, n):
        s[1:m+1] = s[0:m]  # 兔子寿命+1，表格右移
        s[0] = sum(s[2:])  # 新生了多少兔子
    return sum(s[:-1])
"""
[N,  0,  1,  2,  X,  sum]
[1,  1,  0,  0,  0,  1]
[1,  1,  0,  0,  0,  1]
[1,  1,  0,  0,  0,  1]
[1,  1,  0,  0,  0,  1]
[1,  1,  0,  0,  0,  1]
[1,  1,  0,  0,  0,  1]
"""
#print(fibd(99, 19))
def fun(file_name):
    values = open(file_name, "rt").read().split(" ")
    print(fibd(int(values[0]), int(values[1])))
    return None

if __name__ == '__main__':
    fun("rosalind_fibd.txt")


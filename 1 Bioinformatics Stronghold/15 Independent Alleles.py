#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Heredity, Probability
from scipy.misc import comb


def fun(file_name):
    f = open(file_name, 'rt').read().split(" ")
    k = int(f[0])
    N = int(f[1])
    prob = 0
    for i in range(N, 2**k + 1):
        # 把大于N 的概率一个一个加起来 二项分布
        prob += comb(2**k, i) * ((1/4)**i) * ((3/4)**((2**k)-i))
    return prob


if __name__ == '__main__':
    print(fun("rosalind_lia.txt"))

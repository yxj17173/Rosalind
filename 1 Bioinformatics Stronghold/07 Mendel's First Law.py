#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Heredity, Probability
 
 
def fun(file_name):
    f = open(file_name, 'rt').read().split(" ")
    k = int(f[0])
    m = int(f[1])
    n = int(f[2])
    sum = k + m + n
    Pr_dominant = (k/sum) \
        + (m/sum) * (k/(sum-1)) + (m/sum) * ((m-1)/(sum-1)) * 3/4  + (m/sum) * (n/(sum - 1)) * 1/2 \
        + (n/sum) * (k/(sum-1))  + (n/sum) * (m/(sum-1)) * 1/2 
    return Pr_dominant


if __name__ == '__main__':
    print(fun("rosalind_iprb.txt"))

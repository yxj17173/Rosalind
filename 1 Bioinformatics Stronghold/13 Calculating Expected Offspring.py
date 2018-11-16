#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Heredity, Probability


def fun(file_name):
    values = open(file_name, "rt").read().split(" ")
    cp1 = int(values[0])
    cp2 = int(values[1])
    cp3 = int(values[2])
    cp4 = int(values[3])
    cp5 = int(values[4])
    cp6 = int(values[5])
    E_offspring = cp1 * 2 + cp2 * 2 + cp3 * 2 + cp4 * 2 * 3/4 + cp5 * 2 * 1/2
    return E_offspring


if __name__ == '__main__':
    print(fun("rosalind_iev.txt"))

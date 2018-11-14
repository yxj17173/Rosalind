#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# String Algorithms


def fun(file_name):
    string = open(file_name, "rt").read().replace("\n", "")
    string = string.replace("T","U")
    f = open("result_rna.txt", "w+")
    result = string
    f.write(result)
    f.close()

if __name__ == '__main__':
    fun("rosalind_rna.txt")

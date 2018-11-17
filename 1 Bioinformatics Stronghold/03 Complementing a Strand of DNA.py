#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# String Algorithms
import re


def replace_all(repls, str):
    """Replace all the elements in the repls dictionary  of strings,
    For example, replace dict{key(current):value(target)} """
    return re.sub('|'.join(re.escape(key) for key in repls.keys()),
                  lambda k: repls[k.group(0)], str)

def fun(file_name):
    string = open(file_name, "rt").read().replace("\n", "")
    string = replace_all({"T":"A","A":"T","C":"G","G":"C"}, string)
    result = string[::-1]
    f = open("result_revc.txt", "w+")
    f.write(result)
    f.close()

if __name__ == '__main__':
    fun("rosalind_revc.txt")

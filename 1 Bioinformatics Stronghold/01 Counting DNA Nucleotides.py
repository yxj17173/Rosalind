#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun(file_name):
    string = open(file_name, "rt").read().replace("\n", "")
    string = list(string)
    #print(string)
    counts = dict()
    f = open("result_dna.txt", "w+")
    for words in string:
        counts[words] = counts.get(words, 0) + 1
    
    result = str(counts["A"])+" "+str(counts["C"])+" "+str(counts["G"])+" "+str(counts["T"])
    f.write(result)

    f.close()


if __name__ == '__main__':
    fun("rosalind_dna.txt")

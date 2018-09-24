#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## there is a "a 'be" splited"
def fun(file_name):
    string = open(file_name, "rt").read().replace("\n","").split(" ")
    counts = dict()
    f = open("result_06.txt","w+")
    for words in string :
        counts[words] = counts.get(words,0) + 1
    for word,count in counts.items() :
        result = word + " " + str(count)+"\n"
        f.write(result)

    f.close()

if __name__ == '__main__':
    fun("rosalind_ini6.txt")
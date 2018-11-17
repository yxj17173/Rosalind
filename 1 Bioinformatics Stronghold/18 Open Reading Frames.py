#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Combinatorics


codonTable_DNA = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '', 'TAG': '',
    'TGC': 'C', 'TGT': 'C', 'TGA': '', 'TGG': 'W',
}


def orf(sequence):
    pro_list = []
    for start in range(len(sequence)-3):
        sequence_pro = ''
        if codonTable_DNA[sequence[start:start+3]] == 'M':
            # 开始遍历翻译，ATG 是启动子
            for n in range(start, len(sequence), 3):
                if sequence[n:n+3] in codonTable_DNA.keys():
                    sequence_pro += codonTable_DNA[sequence[n:n+3]]
                    # 遍历直到终止密码子
                    if codonTable_DNA[sequence[n:n+3]] == '':
                        if sequence_pro != '':
                            pro_list.append(sequence_pro)
                        break
    return pro_list

def fun(file_name):
    f = open(file_name, "rt").read().split("\n")
    sequence_dna = ''
    for line in f:
        #print(line)
        line = line.rstrip().replace("\n", "")
        if line.startswith('>'):
            continue
        sequence_dna += line
    #print(sequence_dna)
    sequence_rev = sequence_dna[::-1].replace('C', 'g').replace('G','c')\
        .replace('T', 'a').replace('A', 't').upper()
    proteins = set(orf(sequence_dna) + orf(sequence_rev))
    for one in proteins:
        print(one)


if __name__ == '__main__':
    #fun("test.txt")
    fun("rosalind_orf.txt")





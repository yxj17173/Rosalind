#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Formats, Proteomics
# sometimes it works, don't know why

import urllib
from urllib.request import urlopen
import re

def fun(file_name):
    uniprot_id_list = open(file_name, 'rt').read().rstrip().split("\n")
    for name in uniprot_id_list:
        # url地址拼接找蛋白质序列
        #print(name)
        #name0 = name.split('_')[0] #url is updated
        #print(name0)
        url = 'https://www.uniprot.org/uniprot/'+name+'.fasta'
        #url = 'https://www.uniprot.org/uniprot/'+name0+'.fasta'
        #print(url)# 获取url页面
        req = urllib.request.Request(url)
        the_page = urlopen(req).read()
#b'>sp|A2Z669|CSPLT_ORYSI CASP-like protein 5A2 OS=Oryza sativa subsp. indica OX=39946 GN=OsI_33147 PE=3 SV=1\nMRASRPVVHPVEAPPPAALAVAAAAVAVEAGVGAGGGAAAHGGENAQPRGVRMKDPPGAP\nGTPGGLGLRLVQAFFAAAALAVMASTDDFPSVSAFCYLVAAAILQCLWSLSLAVVDIYAL\nLVKRSLRNPQAVCIFTIGDGITGTLTLGAACASAGITVLIGNDLNICANNHCASFETATA\nMAFISWFALAPSCVLNFWSMASR\n'
        seq_list = str(the_page).split("\\n")[1:]
        #print(seq_list)
        seq = ''.join(seq_list)
        #print(seq)
        # 正则表达式编译
        regex = re.compile(r'N(?=[^P][ST][^P])')
        index = 0
        out = []

        while(index < len(seq)):
            index += 1
            # 如果没有匹配到，跳出循环
            if re.search(regex, seq[index:]) == None:
                break
            # 如果匹配到了，加入到字典
            if re.match(regex, seq[index:]) != None:
                out.append(index+1)
        # 如果字典不为零，把匹配到的index 输出
        if out != []:
            print(name)
            print(' '.join([str(i) for i in out]))

if __name__ == '__main__':
    #fun("test.txt")
    fun("rosalind_mprt.txt")

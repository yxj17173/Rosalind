### 5. Computing GC Content ###
from operator import itemgetter
from collections import OrderedDict
# 创建两个有序的字典
seqTest = OrderedDict()
gcContent = OrderedDict()

with open('rosalind_GC.txt', 'rt') as f:
    for line in f:
        # 去除右边的空格
        line = line.rstrip()
        if line.startswith('>'):
            # 读取名字，不要">",所以从1开始
            seqName = line[1:]
            # 把名字放入字典
            seqTest[seqName] = ''
            # 结束本次循环，进入下一个循环
            continue
        # 每行字母都大写加入字典
        seqTest[seqName] += line.upper()

for ke, val in seqTest.items():
    # 所有的碱基
    totalLength = len(val)
    # G和C的碱基和
    gcNumber = val.count('G') + val.count('C')
    # 算GC含量
    gcContent[ke] = (float(gcNumber) / totalLength) * 100
# 字典排序
sortedGCContent = sorted(gcContent.items(), key=itemgetter(1))
# 取字典最后一个的名字，即 Rosalind_0808
largeName = sortedGCContent[-1][0]
# 取GC含量的比值
largeGCContent = sortedGCContent[-1][1]

print('most GC ratio gene is %s and it is %s ' % (largeName, largeGCContent))


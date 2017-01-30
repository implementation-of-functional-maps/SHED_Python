# -*- coding: utf-8 -*-
import numpy as np
import sys

input_file=sys.argv[1]

f_in = open(input_file)
lines_in = f_in.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f_in.close()


count = 0
length_words_max = 0
for line in lines_in:
    elems = line.rstrip().split(',')
    words = elems[2].rstrip().split(' ')
    for word in words:

        if len(word) > length_words_max:
            length_words_max = len(word)
            print(len(word), word, count)
    count += 1
    
# print(answer)

# -*- coding: utf-8 -*-
import time
import mojimoji
import sys

dic=sys.argv[1]
input_file=sys.argv[2]

f_in = open(input_file)
lines_in = f_in.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f_in.close()

f_dic = open(dic)
lines_dic = f_dic.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f_dic.close()

dict={}
for line in lines_dic:
    elems=line.rstrip().split(',')
    dict[elems[2]]=elems[0]

    

line_converted=0
for line in lines_in:
    chars=list(line)
    hebrew2alphabet=[]

    for char in chars:
        
        if char in dict.keys():

            # hebrew2alphabet.append(char)
            # hebrew2alphabet.append(dict[char])
            line_converted+=int(dict[char])
    
    answer=line_converted
    line_converted=0
    line_char=line.strip()
    print(line_char+","+str(answer))

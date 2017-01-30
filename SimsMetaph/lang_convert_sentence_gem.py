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
    dict[elems[1]]=elems[0]

    

line_converted=0
for line in lines_in:
    words=line.rstrip().split("-")

    # print(words)
    answer=[]
    for word in words:
        chars=list(word)
        #print(chars)
        
        word_gematoria=0
        for char in chars:
        
            if char in dict.keys():


                word_gematoria+=int(dict[char])
        
    
        answer.append(str(word_gematoria))
        
    sentence_gematoria=" ".join(answer)
    # print(sentence_gematoria)

    # 歳後文とゲマトリア表示のために
    line_sentence=line.strip()
    print(line_sentence+","+str(sentence_gematoria))

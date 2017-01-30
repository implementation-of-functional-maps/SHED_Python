# -*- coding: utf-8 -*-
import time, sys

words=sys.argv[1]
consonants=sys.argv[2]

f_consonants = open(consonants)
lines_consonants = f_consonants.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f_consonants.close()

f_words = open(words)
lines_words = f_words.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f_words.close()


for i in range(len(lines_consonants)):
    word = lines_words[i].rstrip()
    consonant = lines_consonants[i].rstrip()

    joined_word_consonant='/'.join([word, consonant])

    print(joined_word_consonant)

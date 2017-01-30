# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: .py
#                       Last Change : 2016-10-04
#                       Editted by : Katsurou Takahashi
######################################################################

##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import
import time
# import mojimoji
import numpy as np
##################################################################
#                       Method
##################################################################
def _( wordnet_1, international_phonetic_alphabet_1, wordnet_2, international_phonetic_alphabet_2 ):
    '''
    # lang_convert_wordnet return converted list of wordnet 
    #
    #
    # Step1. letters of original text of wordnet into a dictionary of 
    # [value: international phonetic alphabet, index: senseset]
    # 
    # Step2. 
    ### If you use this code, please cite the following paper:
    #
    #  
    #  
    #  
    #
    ### Copyright (c) 2016 Katsurou Takahashi <katsurou.tkhsk@gmail.com>
    '''

    import lang_convert_wordnet
    # Step1.
    ##################################################################
    # Make Dict International Phonetic Alphabet
    ##################################################################
    # read wordnet
    f_in = open(wordnet_1)
    wordnet_lines = f_in.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f_in.close()
    
    # read international phonetic alphabet
    f_dic = open(international_phonetic_alphabet_1)
    international_phonetic_alphabet_lines = f_dic.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f_dic.close()
    # make converted dictionary
    dict_converted1 = lang_convert_wordnet._( wordnet_lines, international_phonetic_alphabet_lines )

    # Step1.
    ##################################################################
    # Make Dict International Phonetic Alphabet
    ##################################################################
    # read wordnet
    f_in = open(wordnet_2)
    wordnet_lines = f_in.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f_in.close()
    
    # read international phonetic alphabet
    f_dic = open(international_phonetic_alphabet_2)
    international_phonetic_alphabet_lines = f_dic.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f_dic.close()
    
    # make converted dictionary
    dict_converted2 = lang_convert_wordnet._( wordnet_lines, international_phonetic_alphabet_lines )

    import levenstein_wordnet
    # Step2.
    ##################################################################
    # Calucurate Levenstein Distances
    ##################################################################
    dict_of_levensteins = levenstein_wordnet._( dict_converted1, dict_converted2 )
    #-----------------------------------------------------------------
    # Return
    #-----------------------------------------------------------------
    return dict_of_levensteins

######################################################################
#                           END
######################################################################
# checked



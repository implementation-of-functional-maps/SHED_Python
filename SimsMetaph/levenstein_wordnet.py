# -*- mode:python; coding:utf-8 -*-
from __future__ import print_function # これなにをしたかった？
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
def _( dict_converted1, dict_converted2 ):
    '''
    # lang_convert_wordnet return converted list of wordnet 
    # Input: dict_converted = {key: value} = {'00015388-n': [kotob, katob]}
    #
    # Step1. letters of original text of wordnet into a dictionary of 
    # [value: international phonetic alphabet, index: senseset]
    # 
    ### If you use this code, please cite the following paper:
    #
    #  
    #  
    #  
    #
    ### Copyright (c) 2016 Katsurou Takahashi <katsurou.tkhsk@gmail.com>
    '''
    import levenstein
    import branch_regular_words_into_words
    # Step0.
    ##################################################################
    # Init Settings
    ##################################################################
    dict_of_levensteins = {}

    # Step1.
    ##################################################################
    # Make Dict International Phonetic Alphabet
    ##################################################################
    # print(dict_converted1.keys())
    for sense, regular_words_1 in dict_converted1.items():
        if sense in dict_converted2:
            regular_words_2 = dict_converted2[sense]
            levensteins = []
            # print(regular_words_1)
            words_1_branched = []
            for regular_word1 in regular_words_1:
                words_1_branched.append(branch_regular_words_into_words._(regular_word1))
            words_1_branched = sum(words_1_branched, [])
            print(words_1_branched)
            # words_2_branched = branch_regular_words_into_words._(regular_word2[0])
            words_2_branched = []
            for regular_word2 in regular_words_2:
                words_2_branched.append(branch_regular_words_into_words._(regular_word2))
            words_1_branched = sum(words_2_branched, [])
            if len(words_2_branched) != 0 and len(words_1_branched) != 0:
                for w1 in words_1_branched:
                    for w2 in words_2_branched:
                        levensteins.append(levenstein._(w1, w2))
                dict_of_levensteins.update({sense : np.min(levensteins)})
        # else:
        #     levensteins_sense.update({sense :  None})
        
    #-----------------------------------------------------------------
    # Return
    #-----------------------------------------------------------------
    return dict_of_levensteins

######################################################################
#                           END
######################################################################
# checked



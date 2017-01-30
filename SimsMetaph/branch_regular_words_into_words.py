# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: branch_regular_words_into_words.py
#                       Last Change : 2016-11-08
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
def _( regular_word ):
    '''
    # lang_convert_wordnet return converted list of wordnet 
    #
    # Input regular_words = [regular_word1, regular_word2, ..., regular_word_n]
    # regular_word1 = 'koto-b/v-u'
    # regular_word2 = 'koto-b/v-u-k/x-i'
    # -x/k-t-b/v- kotobの例見つけた.
    ### If you use this code, please cite the following paper:
    #
    #  
    #  
    #  
    #
    ### Copyright (c) 2016 Katsurou Takahashi <katsurou.tkhsk@gmail.com>
    '''
    words_branched = []
    # for regular_word in regular_words:
    elems = regular_word.rstrip().split('-')
    for i in range(len(elems)):
        reg_elems = elems[i].rstrip().split('/')
        elems[i] = reg_elems
        
    elems_branched = ['']
    elems_branched_temp = []
    for elem in elems:
        for word in elems_branched:
            for item in elem:
    
                elems_branched_temp.append(''.join([word, item]))
        elems_branched = elems_branched_temp        
        elems_branched_temp = []
            

        

    words_branched = elems_branched 
    #-----------------------------------------------------------------
    # Return
    #-----------------------------------------------------------------
    return words_branched

######################################################################
#                           END
######################################################################
# checked



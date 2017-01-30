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
##################################################################
#                       Method
##################################################################
def _(s1, s2):
    
    '''
    # lang_convert_wordnet return converted list of wordnet 
    # Input: {key: value} = {'00015388-n': [kotob, katob]}
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
    if len(s1) < len(s2):
        return _(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
        
    #-----------------------------------------------------------------
    # Return
    #-----------------------------------------------------------------
    return previous_row[-1]
######################################################################
#                           END
######################################################################
# checked


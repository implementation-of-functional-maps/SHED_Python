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
def _( wordnet_lines, international_phonetic_alphabet_lines ):
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
    # Step1.
    ##################################################################
    # Make Dict International Phonetic Alphabet
    ##################################################################
    dict_international_phonetic_alphabet = {}
    for line in international_phonetic_alphabet_lines:
        elems = line.rstrip().split(',')
        dict_international_phonetic_alphabet[elems[1]] = elems[0]
        
    # Step2.
    ##################################################################
    # Convert WordNet
    ##################################################################
    dict_converted = {}
    for line in wordnet_lines:
        # pick up wordnet line as elements # [sense, "lemma", word]
        elems = line.rstrip().split(',')
        words_list = elems[2].rstrip().split(' ')

        conved_words = []
        for word in words_list:
            chars = list(word)
            hebrew2international_phonetic_alphabet = []

            # foreign characters convert into international phonetic alphabet.
            for char in chars:
                if char in dict_international_phonetic_alphabet.keys():
                    hebrew2international_phonetic_alphabet.append(dict_international_phonetic_alphabet[char])

            line_converted = ''.join(hebrew2international_phonetic_alphabet)
            conved_words.append(line_converted)
        # word = conved_words    
        word = ' '.join(conved_words)
        # joint {key:value} to dict
        if elems[0] in dict_converted.keys():
            dict_converted[elems[0]].append(word)
        else:
            dict_converted.update({elems[0] : [word]})
        
    #-----------------------------------------------------------------
    # Return
    #-----------------------------------------------------------------
    return dict_converted

######################################################################
#                           END
######################################################################
# checked



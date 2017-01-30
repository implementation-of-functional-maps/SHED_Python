# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: CalcSimsMetaph.py
#                       Last Change : 2016-10-20
#                       Editted by : Katsurou Takahashi
######################################################################
##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import numpy as np

##################################################################
#                       Method
##################################################################
def _( shed, word_list , real_metaph, n_best=3  ):
    '''
    # SHEDfromList loads all shapes in the list file, and computes the matching
    # and SHED between each pair of shapes.
    # Note that this function uses DEFAULT weights. To run with different
    # weights use BatchShedFromMatching on the output.
    #
    # Input:
    # extension - in range(for):
    # for segments in range(".seg".):
    #
    # Output:
    # shapes in in range(list.):
    #
    # Matchings = a cell array where cell {i, j} is the matching matrix of
    #             shape i to shape j
    # Shapes = the collection of loaded segmented shapes with their computed
    #          bounding boxes and volumes
    # shape_files = the list of file names. Useful to see which shape
    #               corresponds to each file without opening the file
    #               externally.
    #
    ### If you use this code, please cite the following paper:
    #
    # for Fine-grained in range(Similarity):
    #  Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
    #  SIGGRAPH ASIA 2015
    #
    ### Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>
    '''
    assert len(shed) == len(word_list), "The size of shed must be the same with the size of word list."
    assert n_best <= len(word_list), "The size of n best must be smaller than the size of word list."
    ######################################################################
    # Batch Inv Cos Sim
    ######################################################################
    import SimsMetaph.levenstein as levenstein    
    n = len(word_list)
    levensteins = np.zeros((n, n))
    words = word_list
    for i in range(len(words)):
        for j in range(len(words)):
            levensteins[i, j] = levenstein._(words[i], words[j])

    ######################################################################
    # Batch Conv Sim
    ######################################################################
    w_shed = 0.5
    w_cos  = 1 - w_shed
    conv_sims = w_shed * shed + w_cos * levensteins

    Sims = [ shed, levensteins, conv_sims ]

    ######################################################################
    # n Best Search
    ######################################################################
    shed_arg_sorted = [[0 for col in range(n)] for row in range(n)] # np.zeros((n, n))
    for i in range(n):
        shed_arg_sorted[i] = np.argsort(shed[i], axis=None).tolist()
        # shed_arg_sorted[i, :] = np.argsort(shed, axis=None)

    levensteins_arg_sorted = [[0 for col in range(n)] for row in range(n)] # np.zeros((n, n))np.zeros((n, n))
    for i in range(n):
        levensteins_arg_sorted[i] = np.argsort(levensteins[i], axis=None).tolist()
        # levensteins_arg_sorted[i, :] = np.argsort(levensteins, axis=None)

    conv_sims_arg_sorted = [[0 for col in range(n)] for row in range(n)] # np.zeros((n, n))np.zeros((n, n))
    for i in range(n):
        conv_sims_arg_sorted[i] = np.argsort(conv_sims[i], axis=None).tolist()
        # comv_sims_arg_sorted[i, :] = np.argsort(conv_sims, axis=None)

    ######################################################################
    # n Best Word Pairs Search
    ######################################################################

    m = n-1

    best_n_word_pair_shed = []
    for i in range(n):
        best_n_word_pair_for_word_i = []
        for j in range(n_best):
            best_n_word_pair_for_word_i.append([words[i], words[shed_arg_sorted[i ][ m - j]]])
        best_n_word_pair_shed.append(best_n_word_pair_for_word_i)

    best_n_word_pair_levs = []
    for i in range(n):
        best_n_word_pair_for_word_i = []
        for j in range(n_best):
            best_n_word_pair_for_word_i.append([words[i], words[levensteins_arg_sorted[i ][ m - j]]])
        best_n_word_pair_levs.append(best_n_word_pair_for_word_i)

    best_n_word_pair_conv_sims = []
    for i in range(n):
        best_n_word_pair_for_word_i = []
        for j in range(n_best):
            best_n_word_pair_for_word_i.append([words[i], words[conv_sims_arg_sorted[i ][ m - j]]])
        best_n_word_pair_conv_sims.append(best_n_word_pair_for_word_i)
    ######################################################################
    # SHEDのベクトル類似度
    ######################################################################
    # shed_vec = [[0 for col in range(n)] for row in range(n)] # np.zeros((n, n))
    shed_vec =  np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            shed_vec[i, j] = np.sum(np.cos(shed[i], shed[j]))

    ######################################################################
    # Word2Vec
    ######################################################################
    
    ######################################################################
    # マハラノビス距離 アイディア
    ######################################################################
    # airplane_list
    # bus_list
    # import ShedFromlist
    # shed_seg1_seg2 = ShedFromlist._(airplane_list, bus_list)

    # マハラノビス距離(shed_seg1_seg2)
    
    ######################################################################
    # OutPut
    ######################################################################
    real_metaph_in_n_best_word_pair_shed = []
    for i in range(n):
        real_metaph_word_pair_for_word_i = []
        for j in range(n_best):
            if [words[i], words[shed_arg_sorted[i ][ m - j]]] in real_metaph:
                real_metaph_word_pair_for_word_i.append([words[i], words[shed_arg_sorted[i ][ m - j]]])
        real_metaph_in_n_best_word_pair_shed.append(real_metaph_word_pair_for_word_i)

    real_metaph_in_n_best_word_pair_lev = []
    for i in range(n):
        real_metaph_word_pair_for_word_i = []
        for j in range(n_best):
            if [words[i], words[levensteins_arg_sorted[i ][ m - j]]] in real_metaph:
                real_metaph_word_pair_for_word_i.append([words[i], words[levensteins_arg_sorted[i ][ m - j]]])
        real_metaph_in_n_best_word_pair_lev.append(real_metaph_word_pair_for_word_i)

    real_metaph_in_n_best_word_pair_conv = []
    for i in range(n):
        real_metaph_word_pair_for_word_i = []
        for j in range(n_best):
            if [words[i], words[conv_sims_arg_sorted[i ][ m - j]]] in real_metaph:
                real_metaph_word_pair_for_word_i.append([words[i], words[conv_sims_arg_sorted[i ][ m - j]]])
        real_metaph_in_n_best_word_pair_conv.append(real_metaph_word_pair_for_word_i)
        
    ######################################################################
    # OutPut
    ######################################################################
    import my_modules.slot_class as slot_class
    Words = slot_class.Struct('words', 'shed', 'levs', 'conv', 'shed_args', 'levs_args', 'conv_args', 'shed_metaphs', 'lev_metaphs', 'conv_metaphs', 'shed_metaphs_real', 'lev_metaphs_real', 'conv_metaphs_real')

    Words.shed = shed
    Words.levs = levensteins
    Words.conv = conv_sims

    Words.shed_args = shed_arg_sorted
    Words.levs_args = levensteins_arg_sorted
    Words.conv_args = conv_sims_arg_sorted

    Words.shed_metaphs = best_n_word_pair_shed 
    Words.levs_metaphs = best_n_word_pair_levs
    Words.conv_metaphs = best_n_word_pair_conv_sims

    Words.shed_metaphs_real = real_metaph_in_n_best_word_pair_shed
    Words.levs_metaphs_real = real_metaph_in_n_best_word_pair_lev
    Words.conv_metaphs_real = real_metaph_in_n_best_word_pair_conv
    
    #---------------------------------------------------------------------
    #                          Return
    #---------------------------------------------------------------------
    return Words

######################################################################
#                           Main
######################################################################
        
######################################################################
#                           END
######################################################################


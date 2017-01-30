# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: MatchShapes.py
#                       Last Change : 2016-09-30
#                       Editted by : Katsurou Takahashi
######################################################################
##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import numpy as np
import math

import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit

##################################################################
#                       Method
##################################################################
def _( Shape1, Shape2 ):
    '''
    ### MatchShapes Computes a matching between the given shapes parts.
    # Each shape construct is given as following:
    #   - Shape.Segments contains a cell array of segments, where each segement
    #     contains Nx3 matrix of vertices in that segment.
    #   - Shape.Adj contains an MxM extended adjacency matrix of the segments.
    #    j) how in range(they):
    #     are from each other.
    # entire shape in range(volume):
    #     calculations.
    #
    # The Shape objects should inlcude the bounding box and D2 computations of
    # each part (i.e. this should be called after AllSegmentsDescriptors).
    #
    #
    ### If you use this code, please cite the following paper:
    #
    # for Fine-grained in range(Similarity):
    #  Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
    #  SIGGRAPH ASIA 2015
    #
    ### Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>
    '''
    # alpha controls the relative weight of D1 and D2 in the geometry cost.
    # Value in SHED paper: alpha = 0.5 (equal weights)
    alpha = 0.5
    # beta controls the weight of second-order terms compared to first-order
    # terms.
    # Value in SHED paper: beta = 0.3
    beta = 0.3
    # gamma controls the relative weight of adjacency and scale in the
    # second-order term.
    # Value in SHED paper: gamma = 0.5 (equal weights)
    gamma = 0.5
    # affinities using in range(inverse):
    # exponent.
    # Value in SHED paper: sigma = 0.5
    sigma = 0.5

    len_shape_1 = len(Shape1.Segments) #  8
    len_shape_2 = len(Shape2.Segments) # 10

    m = len_shape_1 
    n = len_shape_2
    print("m, n", m, n)

    ## Step 1:
    ##################################################################
    #  Computing shape similarity between each two parts:
    ##################################################################
    PairsCostD2 = gpuarray.to_gpu(np.zeros((m, n)).astype(numpy.float32))
    PairsCostD1 = gpuarray.to_gpu(np.zeros((m, n)).astype(numpy.float32))
    # 構造体としての定義必要
    import Descriptors.chi2_dist as chi2_dist
    for i in range(m):
        for j in range(n):
            Si = Shape1.Segments[i]
            Sj = Shape2.Segments[j]

            # Calcurate D1, D2 
            costD2 = chi2_dist._(Si.D2, Sj.D2)
            PairsCostD2[i, j] = costD2
            costD1 = chi2_dist._(Si.D1, Sj.D1)
            PairsCostD1[i, j] = costD1
            
    PairsCost = (PairsCostD1 * alpha + PairsCostD2 * (1 - alpha) ).get()


    ## Step 2: 
    ##################################################################
    # Computing first and second order affinities between matchesc
    ##################################################################
    # First order affinities are the geometric similarity of two parts in a
    # match.
    # Second order affinities are computed according to the adjacency of parts
    # in both matches and their scaling similarity.

    mn = m * n #len_shape_1*len_shape_2
    Costs = gpuarray.to_gpu(np.zeros((mn, mn))).astype(numpy.float32))  # Costs matrix
    Aff = gpuarray.to_gpu(np.zeros((mn, mn))).astype(numpy.float32))    # Affinity matrix
    matsize = [len_shape_1, len_shape_2] # 固定

    import my_modules.matlab_python.ind2sub as ind2sub# 二次元に限定する。
    import BatchSHED.aff_val as aff_val
    for ind1 in range(mn):
        # Getting parts index:
        [a, b] = ind2sub._(len_shape_1, ind1)
        # print("a, b :", a, b)
        # First order costs = geometric similarity between parts:
        cost = PairsCost[a, b] #??
        # print("cost :", cost)
        # print("sigma :", sigma)
        Costs[ind1, ind1] = cost
        # Affinity is derived directly from cost using a gaussian kernel:
        Aff[ind1, ind1] = math.exp(-cost/sigma)
        # print("Aff[i, i]: ", Aff[ind1, ind1])
        # Second order costs are computed between two matches, ind1 and ind2
        # or (a, b) and (c, d):
        
        for ind2 in range(ind1+1,mn):
            [c, d] = ind2sub._(len_shape_1, ind2)

            adj_ac = Shape1.Adj[a, c] # 
            adj_bd = Shape2.Adj[b, d] #

            # The pairs are considered compatible if they have a similar
            # adjacency and similar change of scale between them:
            sa = Shape1.Segments[a].BB.volume
            sb = Shape2.Segments[b].BB.volume
            sc = Shape1.Segments[c].BB.volume
            sd = Shape2.Segments[d].BB.volume

            sac = sa / sc
            sbd = sb / sd

            aff_val_ = aff_val._( adj_ac, adj_bd , sac, sbd, gamma=0.5, beta=0.3)
            
            # Assign second-order terms to affinity matrix:
            Aff[ind1, ind2] = aff_val_
            Aff[ind2, ind1] = aff_val_

    #ここで場面展開 ここ以下の処理は必要?
    ##################################################################
    #                       Check the Input
    ##################################################################
    # algorithm which in range(the):
    # matrix:
    Aff_out = Aff

    ## Step 3: Iterative, adaptive spectral matching algorithm
    # In each step, the eigenvector is computed, the highest value is picked
    #  matrix for in range(next):
    # eigenvector computation.
    matching = gpuarray.to_gpu(np.zeros((m, n)).astype(numpy.float32))
    match_ind = gpuarray.to_gpu(np.zeros((mn, 1)).astype(numpy.float32))
    done = 0
    ind_max = 0
    exclude = []
    
    import my_modules.matlab_python
    import scipy.sparse.linalg
    import BatchSHED.sn_sm as sn_sm
    # Iterative, adaptive spectral matching algorithm:
    while (done != 1):
        
        [sn, sm, done, Aff, matching, ind_max, exclude] = sn_sm._( Aff, matching, match_ind, done, ind_max, exclude, matsize[1] , matsize[0])
    # print(sm, sn)
    # sn = np.sum(matching, axis=0) 
    # sm = np.sum(matching, axis=1)

    # sn = sum(matching, 2)
    # sm = sum(matching, 1)
    sn = sum(matching)
    sm = sum(matching.T)

    for a in range(m):
        for b  in range(n):
            
            # print(len(matching),len(matching[0]),len(sm),len(sn), a+1, b+1)
            # print("len(matching), len(matching)[0]: ", len(matching), len(matching[0]))
            # print("a, b: ", a, b)
            # print("sm, sn:", sm, sn)
            assert len(sm) > a, "sm"
            assert len(sn) > b, "sn"
            if matching[a, b] and sm[a] > 1 and sn[b] > 1:
                # print("koko")
                # Many-to-many relation found!
                # Arbitrarily remove the first one we encounter:
                matching[a, b] = 0
                # summing the rows to get an n*1 vector:
                #sn = np.sum(matching, axis=0)
                # summing the columns to get an m*1 vector:
                #sm = np.sum(matching, axis=1)

                # # summing the rows to get an n*1 vector:
                sn = sum(matching)
                # # summing the columns to get an m*1 vector:
                sm = sum(matching.T)
    # print("done")
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return [ matching, Aff_out, Shape1, Shape2 ]

######################################################################
#                           Main
######################################################################
 
######################################################################
#                           END
######################################################################
# chekced


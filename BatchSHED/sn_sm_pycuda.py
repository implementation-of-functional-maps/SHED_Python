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
import numpy as np

import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
##################################################################
#                       Method
##################################################################
def _( Aff, matching, match_ind, done, ind_max, exclude ,matsize_n, matsize_m):
    '''
    # AllSegmentsDescriptors Computes the D1 and D2 descriptors of each segment
    # in a segmented shape structure.
    #
    ### If you use this code, please cite the following paper:
    #
    #  SHED: Shape Edit Distance for Fine-grained Shape Similarity 
    #  Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
    #  SIGGRAPH ASIA 2015
    #
    ### Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>
    '''
    import my_modules.matlab_python
    import scipy.sparse.linalg
    n = matsize_n # len(shape2.segments)
    m = matsize_m # len(shape1.segments)

    # Get principal eigenvector of the affinity matrix:
    [vals, vecs] = gpuarray.to_gpu(scipy.sparse.linalg.eigs(Aff, 1).astype(numpy.float32))
    x = vecs.get()

    # vals, vecs = sparse.linalg.eigs(id, k=6)
    # [V,D] = eigs(___) 対応する固有ベクトルを列に含む行列 V = x
    # Make sure the vector is positive and avoid rounding errors:
    x = np.absolute(x)

    # If a match was selected it shouldn't be selected again:
    x[np.where(match_ind == 1)] = 0

    for i in exclude:
        x[i] = 0
    # Find maximum value of eigenvector - most likely pair to match:
    [x_max, ind_max] = [max(x), np.argmax(x)]

    print("ind max", ind_max)
    # print("x_max: ",x_max)
    # Find sub-indices of maximum value:
    [am, bn] = my_modules.matlab_python.ind2sub._(m, ind_max) # ??
    # print("am, bn",am, bn)
    # print(len(matching),len(matching[0]))
    # summing the rows to get an n*1 vector:
    sn = sum(matching)  #- matching[0, 0] - matching[0, 1]
    
    # summing the columns to get an m*s1 vector:
    sm = sum(matching.T)# - matching[0, 0]

    # If every part is matched with at least one other part, we are done:
    import my_modules.matlab_python.sub2ind
    # matsize = [m, n]
    if (min(sn) > 0 and min(sm) > 0) or x_max == 0.0:
        done = 1
        
    else:
        # This match is only possible if one of the parts is not yet
        # matched:
        # print("sn[a], sm[b]:", sn[a], sm[b])
        if int(sn[bn]) == 0 or int(sm[am]) == 0:
            matching[am, bn] = 1
            match_ind[ind_max] = 1 # ?? match_indd
            print("match_ind", match_ind.T)
            # Update affinity matrix:
            ind1 = []
            ind2 = []
            for j in range(n):
                ind1.append(my_modules.matlab_python.sub2ind._([matsize_m, matsize_n], am,  j))

            for i in range(m):
                ind2.append(my_modules.matlab_python.sub2ind._([matsize_m, matsize_n], i,  bn))

            # If one pair contains part a and the other contains part b they
            # are not compatible:
            # print("Aff: ", len(Aff))
            # print("Aff: ", len(Aff[0]))
            # print("ind1: ",ind1)
            # print("ind2: ",ind2)
            for i in ind1:
                # print("i: ", i)
                for j in ind2:
                    # print("j: ", j)
                    Aff[i, j] = 0
                    Aff[j, i] = 0
            # The affinity of the selected match becomes 1 to strengthen
            # any compatible matches:
            Aff[ind_max, ind_max] = 1
            # The affinity between all previously selected pairs is 1 since
            # they are already selected: ここがうまくいってない。
            for i in range(len(match_ind)):
                if match_ind[i] == 1:
                        Aff[i, i] = 1
            # Aff[match_ind[np.where(match_ind == 1)], match_ind[np.where(match_ind == 1)]] = 1 # 
        else:
            # The match is not valid given previous matches, add it to the
            # excluded matches list:
            exclude.append(ind_max)
        ## Remove incorrect duplications such as many-to-many relations in the matching graph:
        # This should not happen in practice, but just to be safe...
        # summing the rows to get an n*1 vector:


    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return  [sn, sm, done, Aff, matching, ind_max, exclude]

######################################################################
#                           Main
######################################################################
        
######################################################################
#                           END
######################################################################

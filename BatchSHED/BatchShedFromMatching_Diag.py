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
import time 
##################################################################
#                       Method
##################################################################
def _( Shapes, Matchings, *Weights ):
    '''
    # BATCHSHEDFROMMATCHING Given a collection of shapes and the matchings
    # for the in range(collection.):
    #
    # Shapes = the collection of shapes (cell array)
    #
    # Matchings = a cell array where each cell {i, j} contains the matching
    #             matrix of shape i to shape j
    #
    # Weights = Weights structure that can be learned from an example set and
    #           contains the following parameters. If no weights are given the
    #           default weights are used.
    #       wGeometry = cost of changing the geometry of a part
    #       wScale = cost of changing the scale of a part
    #       wPosition = cost of changing the position or connectivity of a part
    #       wDuplicate = cost of duplicating a part
    #
    #
    # Output:
    # shed = a matrix of the SHED value of each pair of shapes.
    #
    # costs = a collection of costs, where each cost is a matrix of the final
    # to know in range(costs):
    # each pair in range(shapes.):
    #         Contains costGeometry, costScale, costPosition and costDuplicate.
    #
    ### If you use this code, please cite the following paper:
    #
    # for Fine-grained in range(Similarity):
    #  Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
    #  SIGGRAPH ASIA 2015
    #
    ### Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>
    '''
    start = time.time()
    n = len(Shapes)
    shed = np.zeros((n, n))
    import my_modules.slot_class as slot_class
    costs = slot_class.Struct('Costs', 'costGeometry', 'costScale', 'costPosition', 'costDuplicate')
    # Most code here takes care of outputing the costs...
    costs.costGeometry = np.zeros((n,n))
    costs.costScale = np.zeros((n,n))
    costs.costPosition = np.zeros((n,n))
    costs.costDuplicate = np.zeros((n,n))
    
    import my_modules.matlab_python.nargin
    import BatchSHED.ShedFromMatching as ShedFromMatching
    for i in range(n-1):
       for j in range(i+1,n):
        if my_modules.matlab_python.nargin._(Shapes, Matchings, Weights ) > 2:
            # Use given weights:
            [curr_shed, cost] = ShedFromMatching._(Shapes[i], Shapes[j], Matchings[i][j])
        else:
            # Use default weights:
            [curr_shed, cost] = ShedFromMatching._(Shapes[i], Shapes[j], Matchings[i][j])
        shed[i, j] = curr_shed
        costs.costGeometry[i, j] = cost.totGeometry
        costs.costScale[i, j] = cost.totScale
        costs.costPosition[i, j] = cost.totPosition
        costs.costDuplicate[i, j] = cost.totDuplicate

    # Make matrices symmetric (not sure this part is necessary):
    # shed = shed + shed.T

    costs.costGeometry = costs.costGeometry + costs.costGeometry.T
    costs.costScale = costs.costScale + costs.costScale.T
    costs.costPosition = costs.costPosition + costs.costPosition.T
    costs.costDuplicate = costs.costDuplicate + costs.costDuplicate.T

    end = time.time()
    print("shed 算出作成時間"+'%.3f' %(end-start))    
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return [ shed, costs ]
   
######################################################################
#                           Main
######################################################################

        
######################################################################
#                           END
######################################################################

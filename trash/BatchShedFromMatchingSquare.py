# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: .py
#                       Last Change : 2016-10-04
#                       Editted by : Katsurou Takahashi
######################################################################
#
# [mus] calucurates the length of the character array input.
# [mus_xyz] is the same with [mus].
# 
### If you use this code, please cite the following paper:
#  
#  Equidistant Letter Sequence in the Book of Genesis
#  Dirib Witzym, Ekutagy Ruos and Yoav Rosenberg
#  Statistical Science 1994
#
### Copyright (c) 2016 Katsurou Takahashi <katsurou.tkhsk@gmail.com>
##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import check as ck # check, time stamp, demo, help
import numpy as np
##################################################################
#                       Method
##################################################################
def BatchShedFromMatchingSquare( Shapes, Matchings, Weights ):
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


    import nargin._ as nargin

    n = len(Shapes)


    shed = np.zeros(round(n/2))
    # Most code here takes care of outputing the costs...
    costs.costGeometry = np.zeros(n)
    costs.costScale = np.zeros(n)
    costs.costPosition = np.zeros(n)
    costs.costDuplicate = np.zeros(n)

    import ShedFromMatching
    for i in range(round(n/2)):
        for j in range(round(n/2)+1,n):
            if (nargin > 2):
                # Use given weights:
                [curr_shed, cost] = ShedFromMatching(Shapes[i], Shapes[j], Matchings[i][j], Weights)
            else:
                # Use default weights:
                [curr_shed, cost] = ShedFromMatching(Shapes[i], Shapes[j], Matchings[i][j])
            shed[i][j-round(n/2)] = curr_shed
            costs.costGeometry[i][j] = cost.totGeometry
            costs.costScale[i][j] = cost.totScale
            costs.costPosition[i][j] = cost.totPosition
            costs.costDuplicate[i][j] = cost.totDuplicate


    # Make matrices symmetric (not sure this part is necessary):
    #shed = shed + shed'
    shed_inv=shed(turn)

    costs.costGeometry = costs.costGeometry + costs.costGeometry(turn)
    costs.costScale = costs.costScale + costs.costScale(turn)
    costs.costPosition = costs.costPosition + costs.costPosition(turn)
    costs.costDuplicate = costs.costDuplicate + costs.costDuplicate(turn)
    
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return [ shed, shed_inv, costs ]
   

######################################################################
#                           Main
######################################################################
if __name__ == '__main__':

    ck.today() # time stamp
    
    if len(sys.argv) == 1:
        # input example 
        deltas = [1,2,3,4,5,6,7,8,9,10]
        # output
        func = _(deltas)
        
        ck.std_out_io(sys.argv[0], func, deltas)
        
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-help":
            
            ck.description(16, sys.argv[0])
        
            ck.function(31, 39, sys.argv[0])
            
        else: # ここに nargin を使えない？
            # exec test
            # ex) python mus_xyz.py " python mus_xyz.py "[1,2,3,4,5,6,7,8,9,10]" 4
            list_delta = sys.argv[1].lstrip("[").rstrip("]").split(",")
            deltas=[]
            for delta in list_delta:
                deltas.append(int(delta))
        
            # output
            func = _(deltas)
        
            ck.std_out_io(sys.argv[0], func, deltas)
            
    else:
        print("\nExecution Error: the valiables is invalid.\n")
        
######################################################################
#                           END
######################################################################

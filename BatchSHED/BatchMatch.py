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
##################################################################
#                       Method
##################################################################
def _( Shapes , *ind ):
    '''
    # BatchMatch Gets a list of loaded segmented shapes and calculated the
    # matchings between all pairs of shapes using MatchShapes().
    #
    # Shapes = collection of shapes
    # ind = the indices in the collection to compare (optional)
    #
    ### If you use this code, please cite the following paper:
    #
    #  SHED: Shape Edit Distance for Fine-grained Shape Similarity 
    #  Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
    #  SIGGRAPH ASIA 2015
    #
    ### Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>
    '''
    import my_modules.matlab_python.nargin as nargin
    if (nargin._( Shapes, *ind ) < 2):
        # Default index list is whole collection:
        ind = len(Shapes)

    n = ind
    Matchings = [[None for col in range(n)] for row in range(n)]# np.zeros((n, n))

    import BatchSHED.MatchShapes as MatchShapes
    for i in range(n):
        for j in range(i,n):
            # Find matching between shapes i and j:
            curr_matching   = MatchShapes._(Shapes[i], Shapes[j])
            curr_matching_T = MatchShapes._(Shapes[j], Shapes[i])

            Matchings[i][j] = curr_matching
            Matchings[j][i] = curr_matching_T # .T

    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return  Matchings
  
######################################################################
#                           Main
######################################################################
        
######################################################################
#                           END
######################################################################

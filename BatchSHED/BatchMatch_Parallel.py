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
def _( Shapes1, Shapes2, *ind ):
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
    if (nargin._( Shapes1, Shapes2, *ind ) < 2):
        # Default index list is whole collection:
        ind1 = len(Shapes1)
        ind2 = len(Shapes2)

    ind1 = len(Shapes1)
    ind2 = len(Shapes2)
    Matchings = [[None for col in range(ind1)] for row in range(ind2)]# np.zeros((n, n))
    
    import BatchSHED.MatchShapes as MatchShapes
    for i in range(ind1):
        for j in range(ind2):
            # Find matching between shapes i and j:
            curr_matching   = MatchShapes._(Shapes1[i], Shapes2[j])
            print("koko")
            Matchings[i][j] = curr_matching


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

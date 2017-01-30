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
import check as ck # check, time stamp, demo, help
import numpy as np
##################################################################
#                       Method
##################################################################
def _( Shapes, ind ):
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
    
    import nargin
    if nargin._( Shapes, ind ) < 2:
        # Default index list is whole collection:
        ind = len(Shapes)

    import MatchShapes
    for i in range(round(n/2)):
        for j in range(round(n/2)):
            # Find matching between shapes i and j:
            curr_matching = MatchShapes._(Shapes[ind[i]], Shapes[ind[j]])

            Matchings[i][j] = curr_matching
            Matchings[j][i] = curr_matching.T
            print('Computed Matching('+ num2str[i] +', '+ num2str[j] +')')

    print('Computed all matchings in '+ num2str(t) +' seconds.')

    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return  Matchings 
   

######################################################################
#                           Main
######################################################################
if __name__ == '__main__':
    inputs = []
    ck.main(_,inputs)
    # manual test がうまくいってない.
    # (exec_func, *inputs)       
######################################################################
#                           END
######################################################################

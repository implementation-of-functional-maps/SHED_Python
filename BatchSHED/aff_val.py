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
import math
##################################################################
#                       Method
##################################################################
def _( adj_ac, adj_bd , sac, sbd, gamma=0.5, beta=0.3):
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
    if adj_ac == 0 or adj_bd == 0:
        aff_val = 0
    else:
        adj_val = max(adj_ac, adj_bd) / min(adj_ac, adj_bd) - 1
        # adj_val = 0 when the adjacencies match, and high when the
        # adjacencies do not match. Also higher when the parts are
        # example 5/4 in range(3/2.):
        SACBD = np.vstack((sac,sbd))
        if min(SACBD) != 0:
            scale_val = max(SACBD) / min(SACBD) - 1
        else:
            scale_val = 0
        # scale_val = np.max(sac,sbd) / np.min(sac,sbd) - 1
        # Weighted average of adjacency and scaling factor:
        val = gamma * adj_val + (1-gamma) * scale_val
        exp_val = math.exp(-val)
        # Relative weight of second-order terms compared to first-order
        # terms:
        aff_val = beta * exp_val

    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return  aff_val

######################################################################
#                           Main
######################################################################
        
######################################################################
#                           END
######################################################################

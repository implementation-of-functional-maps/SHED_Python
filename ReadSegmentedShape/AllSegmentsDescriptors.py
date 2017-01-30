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
sys.path.append("/Users/admin/Dropbox/SHED_python/auto/ReadSegmentedShape/Descriptors")
import numpy as np
##################################################################
#                       Method
##################################################################
def _(Shape, Segments):
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
    nseg = len(Segments)

    import ReadSegmentedShape.Descriptors.calc_D1 as calc_D1 
    import ReadSegmentedShape.Descriptors.calc_D2 as calc_D2

    for i in range(nseg):
        # Compute both D1 and D2 histograms:
        Segments[i].D1 = calc_D1._(Shape, Segments[i])
        Segments[i].D2 = calc_D2._(Shape, Segments[i])

    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return  Segments

######################################################################
#                           Main
######################################################################
######################################################################
#                           END
######################################################################

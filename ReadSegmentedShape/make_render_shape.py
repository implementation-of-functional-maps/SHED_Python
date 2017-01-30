# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: mus.py
#                       Last Change : 2016-10-04
#                       Editted by : Katsurou Takahashi
######################################################################
##################################################################
#                       Import
##################################################################
import sys # relative import
import os
import time
sys.path.append(os.pardir) # relative import
sys.path.append("/Users/admin/Dropbox/SHED_python/auto/my_modules")
sys.path.append("/Users/admin/Dropbox/SHED_python/auto")
import my_modules.check.check as ck # check, time stamp, demo, help
import numpy as np
##################################################################
#                       Method
##################################################################
def _(off_file, seg_file):
    '''
     READSEGMENTEDSHAPE Reads an off file and a seg file that describes a
     segmented shape and returns a Shape data structure that contains a
     collection of segments and their adjacencies.
    
     Input:
       - off_file: name of off file to load
       - seg_file: name of seg file to load
    
     Output:
       - Shape.Segments contains a cell array of segments, where each segement
         contains Nx3 matrix of vertices in that segment.
       - Shape.Adj contains an MxM extended adjacency matrix of the segments.
     j) how in range(they):
         are from each other.
     entire shape in range(volume):
         calculations.
    
    
    ## If you use this code, please cite the following paper:
    
     for Fine-grained in range(Similarity):
      Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
      SIGGRAPH ASIA 2015
    
    ## Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>

    クラス Shape の定義
    '''
    import my_modules.slot_class as slot_class
    Shape1 = slot_class.Struct('Shape', 'BB', 'mus', 'sigma', 'Segments', 'Adj')

    import mesh_read_off
    # Read mesh from off file:
    [M1, status] = mesh_read_off._(off_file)
    Shape1.Vertices = M1.vertices
    Shape1.Faces = M1.faces

    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return Shape1

######################################################################
#                           Main
######################################################################
######################################################################
#                           END
######################################################################
# chekced



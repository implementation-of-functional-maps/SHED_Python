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
# import check as ck # check, time stamp, demo, help
import numpy.linalg as LA
import numpy as np
##################################################################
#                       Method
##################################################################
def _(Shape, Segment):

    ######################################################################
    #                          Set up
    ######################################################################
    A = np.zeros((len(Segment.Faces), 1))
    
    # Step0
    ######################################################################
    #                          Compute area
    ######################################################################
    v = [0,0,0]
    for i in range(len(Segment.Faces)): 
        # Step1
        v[0] = Shape.Vertices[Segment.Faces[i][0]]
        v[1] = Shape.Vertices[Segment.Faces[i][1]]
        v[2] = Shape.Vertices[Segment.Faces[i][2]]

        # Step2
        v0 = v[1] - v[0]
        v1 = v[2] - v[0]
        n = np.cross(v0, v1)
        area = LA.norm(n)/2.0

        # Step3
        A[i] = area

    return A
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------

######################################################################
#                           END
######################################################################

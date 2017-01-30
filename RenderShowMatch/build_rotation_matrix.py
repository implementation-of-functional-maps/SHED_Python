# -*- mode:python; coding:utf-8 -*-
######################################################################
#  File Name: build_rotation_matrix.py
#  Last Change : 2016-10-27
#  Editted by : Katsurou Takahashi
######################################################################
##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import numpy as np
import numpy.linalg as LA
##################################################################
#                       Method
##################################################################
def _(axis, angle):
    '''
     This function builds a generalized rotation matrix
    
     Input -
       - axis: rotation axis: a 3D vector
       - angle: rotation angle: a scalar
    
     Output -
       - R: rotation matrix: a 3x3 matrix
    
    Copyright (c) 2016 Katsurou Takahashi <katsurou.tkhsk@gmail.com>
    '''
    # Init matrix
    R = np.zeros((3,3))
    # Normalize axis vector
    axis = np.array(axis)
    axis = axis / LA.norm(axis, 2)
    x = axis[0]
    y = axis[1]
    z = axis[2]
    # Compute sin and cos
    cosa = np.cos(angle)
    sina = np.sin(angle)
    # Create matrix
    # http://en.wikipedia.org/wiki/Rotation_matrix
    R[0,0] = cosa + (1 - cosa)*pow(x,2)
    R[0,1] = (1 - cosa)*x*y - sina*z
    R[0,2] = (1 - cosa)*x*z + sina*y

    R[1,0] = (1 - cosa)*y*x + sina*z
    R[1,1] = cosa + (1 - cosa)*pow(y,2)
    R[1,2] = (1 - cosa)*y*z - sina*x

    R[2,0] = (1 - cosa)*z*x - sina*y
    R[2,1] = (1 - cosa)*z*y + sina*x
    R[2,2] = cosa + (1 - cosa)*pow(z,2)
    
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return R

######################################################################
#                           Main
######################################################################
        
######################################################################
#                           END
######################################################################

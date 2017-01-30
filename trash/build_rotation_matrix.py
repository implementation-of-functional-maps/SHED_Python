# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: build_rotation_matrix.py
#                       Last Change : 2016-09-30
#                       Editted by : Katsurou Takahashi
######################################################################
#
# This function builds a generalized rotation matrix
#
# Input -
#   - axis: rotation axis: a 3D vector
#   - angle: rotation angle: a scalar
#
# Output -
#   - R: rotation matrix: a 3x3 matrix
#
### Copyright (c) 2016 Katsurou Takahashi <katsurou.tkhsk@gmail.com>
##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import check as ck # check, time stamp, demo, help

##################################################################
#                       Method
##################################################################
def _(axis, angle):

    ##################################################################
    # Init matrix
    ##################################################################
    R = np.zeros(3,3)
        
    ##################################################################
    # Normalize axis vector
    ##################################################################
    axis = axis / norm(axis, 2)
    x = axis(1)
    y = axis(2)
    z = axis(3)

    ##################################################################
    # Compute sin and cos
    ##################################################################
    import cos
    import sin
    cosa = cos(angle)
    sina = sin(angle)
        
    ##################################################################
    # Create matrix
    ##################################################################    
    # http://en.wikipedia.org/wiki/Rotation_matrix
    R[1][1] = cosa + (1 - cosa)*x^2
    R[1][2] = (1 - cosa)*x*y - sina*z
    R[1][3] = (1 - cosa)*x*z + sina*y
        
        
    R[2][1] = (1 - cosa)*y*x + sina*z
    R[2][2] = cosa + (1 - cosa)*y^2
    R[2][3] = (1 - cosa)*y*z - sina*x
        
        
    R[3][1] = (1 - cosa)*z*x - sina*y
    R[3][2] = (1 - cosa)*z*y + sina*x
    R[3][3] = cosa + (1 - cosa)*z^2
        
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return R

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


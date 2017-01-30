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
# sys.path.append(os.pardir) # relative import
sys.path.append("/Users/admin/Dropbox/SHED_python/auto/my_modules")
sys.path.append("/Users/admin/Dropbox/SHED_python/auto")
sys.path.append("/Users/admin/Dropbox/SHED_python/auto/ReadSegmentedShape/Descriptors")
sys.path.append("/Users/admin/Dropbox/SHED_python/auto/ReadSegmentedShape")
# import check as ck # check, time stamp, demo, help
import numpy as np
##################################################################
#                       Method
##################################################################
def _(Shape, Segment):
    '''
    ######################################################################
    #   This function calculates D1 descriptor of a mesh.
    # See: Shape Distributions, Osada et al.
    #
    # The shape is sampled according to the respective area of each face.
    #
    # Written by Noa Fish, 2013
    # Editted by Katsurou Takahashi Sep Japan 2016
    ######################################################################
    '''
    # Step0   
    ######################################################################
    #                          Init Settings
    ######################################################################
    n = 1024
    b = 64
    faces = Segment.Faces
    vertices = Shape.Vertices
    seed_num1 = 777
    
    # Step1
    ######################################################################
    #                          Normalize Vertices
    ######################################################################
    vn = len(vertices)
    center = np.mean(vertices)
    vertices = vertices - np.matlib.repmat(center, vn, 1) 

    # Step2
    ######################################################################
    #                          Compute Area
    ######################################################################
    import ReadSegmentedShape.Descriptors.computeArea as computeArea
    areas = computeArea._(Shape, Segment)

    cum_areas = np.cumsum(areas)
    if cum_areas == []:
        cumareas = [0]
        
    cum_areas = cum_areas - cum_areas[0]
    cum_areas = cum_areas / cum_areas[len(cum_areas)-1]

    dists = np.zeros((n, 1))
    p = np.zeros((n, 3))

    import numpy.random
    np.random.seed(seed_num1)
    r = np.random.rand(n, 3)
    
    index_0 = r[:, 0]
    index_arr = []
    rand_size = min(len(index_0), len(cum_areas))
    for i in range(rand_size):
        if index_0[i] >= cum_areas[i]:
            index_arr.append(index_0[i])
    index = sum(index_arr)
    index = int(index)
    
    if faces == []:
        p = np.array([0,1,2]) # ?? ここは一時的な設定
    else:
        vind = faces[index]

        a1 = vertices[vind[0]]
        b1 = vertices[vind[1]] 
        c1 = vertices[vind[2]]

        r1 = r[:, 1]
        r2 = r[:, 2]
        o1 = np.array([1,1,1])
        
        R1 = np.matlib.repmat((1 - np.sqrt(r1)), 3, 1) # o1 の代わりにrepmat を使用.
        R2 = np.matlib.repmat((np.sqrt(r1) * (1-r2)), 3, 1)
        R3 = np.matlib.repmat((np.sqrt(r1) * r2), 3 ,1)

        p = R1.T  * a1 +  R2.T * b1 +  R3.T * c1

    pow_p = p * p
    
    dists = np.sqrt(pow_p[:, 0] +pow_p[:, 1] +pow_p[:, 2])
    
    d1 = np.histogram(dists, b)[0] / n
    
    # import math
    # d1 = math.histogram(dists, b)[0] / n

    
    #---------------------------------------------------------------------
    #                          Return
    #---------------------------------------------------------------------
    return d1

#未定義関数
# arrayfun(@(z) sum(z >= cum_areas), r(:, 1))



######################################################################
#                           Main
######################################################################
        
######################################################################
#                           END
######################################################################
# checked
                    

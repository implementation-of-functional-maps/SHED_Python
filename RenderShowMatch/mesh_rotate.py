# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: mesh_rotate.py
#                       Last Change : 2016-09-30
#                       Editted by : Katsurou Takahashi
######################################################################
##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
##################################################################
#                       Method
##################################################################
def _(M, axis, angle):
    '''
    
     This function rotates a mesh by a certain angle on a certain axis
    
     function N = mesh_rotate(M, axis, angle)
    
     Input -
       - M: triangle mesh: M.vertices(i, :) represents the 3D coordinates
       of vertex 'i', while M.faces(i, :) contains the indices of the three
       vertices that compose face 'i'
        - axis: rotation axis: a 3D vector
        - angle: rotation angle in radians: a scalar
    
     Output -
       - N: new rotated triangle mesh, with the same structure as M

     Copyright (c) 2016 Katsurou Takahashi <katsurou.tkhsk@gmail.com>
    
    '''
    # Create output mesh
    import my_modules.slot_class as slot_class
    N = slot_class.Struct('mesh', 'vertices', 'faces')
    N.vertices = M.vertices
    N.faces = M.faces
    # Rotate vertex positions
    import RenderShowMatch.build_rotation_matrix as build_rotation_matrix
    R = build_rotation_matrix._(axis, angle)
    for i in range(len(M.vertices)):
        N.vertices[i] = M.vertices[i].dot(R)
        
    # Copy colors, if defined
    if hasattr(M, 'FaceVertexCData') is True:
        N.FaceVertexCData = M.FaceVertexCData
        
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return N

######################################################################
#                           Main
######################################################################
        
######################################################################
#                           END
######################################################################


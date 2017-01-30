# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: RenderMatchingFigure.py
#                       Last Change : 2016-10-04
#                       Editted by : Katsurou Takahashi
######################################################################
##################################################################
#                       Import
##################################################################
# http://qiita.com/ynakayama/items/8d3b1f7356da5bcbe9bc
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import numpy as np
import pandas
from numpy.random import randn

from matplotlib import font_manager
import mpl_toolkits.mplot3d
import matplotlib.figure as figure
import matplotlib.pyplot as plt
import matplotlib.colors as colors
# import mpl_toolkits.mplot3d as Axes3D

import mpl_toolkits.mplot3d as a3
import pylab as pl

import scipy as sp

##################################################################
#                       Method
##################################################################
def _( Shapes_render, Shapes, Matchings, filename):
#def _( Shapes_render, Shapes, Matchings, filename, shapes_list, output_dir, *rot_step ):
    '''
    # RenderMatchingFigures renders a nice figure of the matching between 
    # shapes.
    # Each segment in the source shape is assigned a unique color, which is 
    # used to render both the original segment and any matching segment in the 
    # target shape. If several segments in the source shape match the same 
    # segment in the target shape, the segment will be rednered several times
    # with random perturbations so that it will appear in several different 
    # colors.
    #
    # Input:
    # Shapes = the collection of shapes (can include more shapes than the ones
    #          that are compared)
    # Matchings = a cell array where cell {i, j} is a matching matrix between
    #             shape i and shape j
    # filename = Prefix of the file name to save for each figure. 
    #            The figure of the source shape will be saved as
    #            "filename_Segs".
    #            The figures of the target shapes will be saved as 
    #            "filename_Matching_id.png" where id is the index of the shape 
    #            in the collection.
    # shapes_list = a list of indices of shapes. The first index is the source
    #               shape and the rest are the target shapes to compare with.
    # output_dir = a directory name in which to save the figures.
    #
    # rot = rotation of each figure around the Y axis, for better viewing angle.
    #
    #
    # Output:
    # n files will be saved into the designated folder.
    #
    ### If you use this code, please cite the following paper:
    #  
    #  SHED: Shape Edit Distance for Fine-grained Shape Similarity 
    #  Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or 
    #  SIGGRAPH ASIA 2015
    #
    ### Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>

    # This function makes a figure look nice in terms of lighting etc.
    '''
    shapes_list = [0, 1]
    src_id = shapes_list[0]
    src_id = 0
    del shapes_list[0]
    target_ids = shapes_list # [1:len(shapes_list)]
    k = len(target_ids)
    
    # This is the gap between segments, relative to the distance from the shape
    # center. Change to 0 to have a render without any gaps.
    gap = 0.05
    pi = np.pi
    
    import my_modules.matlab_python
    if (my_modules.matlab_python.nargin._() < 6):
        # Show only one rotation:
        rot_step = 0
        rot_num = 1
    else:
        # Show many rotations:
        rot_num = np.floor(2 * pi / rot_step)
    
    # Add a fixed rotation to avoid straight-on viewing angle:
    fix_rot = pi / 20
    # For vases, candles, lamps:
    elevation = - pi / 10 # or - pi / 5 For planes:

    # This color map is used in order to color segments.
    # Colors: [Yellow, Blue, Red, Turquoise, Green, Orange, Purple, Dark Blue, 
    #          Dark Green, Dark Red, Light Gray, Dark Gray, Pink]
    Colors = np.array([[0.9,0.9,0.5],[0.15,0.6,0.8],[1,0.4,0.4],[0.4,0.8,0.7],[0.5,0.8,0.45],[1,0.5,0.33],[0.55, 0.33,0.7],[0.35,0.45,1],[0.2,0.8,0.5],[0.8,0.4,0.2],[0.75,0.75,0.75],[0.5,0.5,0.5],[0.95,0.65,0.8]])#,[0.2,0.5,0.5],[0.95,0.65,0.8]])

    ## Render source shape:
    seg1 = Shapes[src_id].Segments
    s1 = len(seg1)    # number of segments
    print("s1: " , s1)
    shape_center = Shapes[src_id].BB.center
    
    import my_modules.slot_class as slot_class
    shape = slot_class.Struct('Shape', 'vertices', 'faces')
    shape.vertices = Shapes_render[src_id].Vertices
    shape.faces = Shapes_render[src_id].Faces
            
    import RenderShowMatch.mesh_rotate as mesh_rotate
    import numpy.matlib
            
    import numpy.matlib
    import random
    ## Render target shapes:
    # k = 1
    shape_center = Shapes[1].BB.center
    seg2 = Shapes[1].Segments
    s2 = len(seg2)
    print("s2: " , s2)
    matching = Matchings[0][1][0]# [:, ::-1]
    print("matching: ", matching)
    ax = a3.Axes3D(pl.figure())
    # Go over the original segments and find their matches in the current shape:
    for i in range(s1):
        print("i: ", i)
        # For each matching segment:
        for ii in range(s2):
                print("ii: ", ii)
                if matching[i, ii] == 1.0:
                    # Take patch data from target shape (ii):
                    # ax = a3.Axes3D(pl.figure())                    
                    shape_tar = slot_class.Struct('Segment', 'vertices', 'faces')
                    shape_tar.vertices = Shapes[src_id].Vertices
                    mesh = slot_class.Struct('Segment', 'vertices', 'faces')
                    mesh.faces = seg1[i].Faces
            
                    for l in range(len(mesh.faces)):
                        v1 = np.array([shape_tar.vertices[mesh.faces[l][0]][0],shape_tar.vertices[mesh.faces[l][0]][1],shape_tar.vertices[mesh.faces[l][0]][2]])
                        v2 = np.array([shape_tar.vertices[mesh.faces[l][1]][0],shape_tar.vertices[mesh.faces[l][1]][1],shape_tar.vertices[mesh.faces[l][1]][2]])
                        v3 = np.array([shape_tar.vertices[mesh.faces[l][2]][0],shape_tar.vertices[mesh.faces[l][2]][1],shape_tar.vertices[mesh.faces[l][2]][2]])
                
                        v0 = np.vstack((v1,v2))
                        v = np.vstack((v0,v3))

                        h = i % len(Colors)
                        tri = a3.art3d.Poly3DCollection([v])
                        tri.set_color(colors.rgb2hex(Colors[h]))
                        tri.set_color(Colors[h])
                        # tri を追加            
                        ax.add_collection3d(tri)

                    # 軸ラベルの設定
                    ax.set_xlabel("X-axis")
                    ax.set_ylabel("Y-axis")
                    ax.set_zlabel("Z-axis")
            
                    ax.set_xlim(np.min(shape_tar.vertices[:,0]), np.max(shape_tar.vertices[:,0]))
                    ax.set_ylim(np.min(shape_tar.vertices[:,1]), np.max(shape_tar.vertices[:,1]))
                    ax.set_zlim(np.min(shape_tar.vertices[:,2]), np.max(shape_tar.vertices[:,2]))

    ax = a3.Axes3D(pl.figure())
    for i in range(s1):
        # print("ii:", ii)
        # For each matching segment:
        for ii in range(s2):
                # print("i: ", i)
                if matching[i, ii] == 1.0:
                    # Take patch data from target shape (ii):
                    # ax = a3.Axes3D(pl.figure())
                    print("match!")
                    shape_tar = slot_class.Struct('Segment', 'vertices', 'faces')
                    shape_tar.vertices = Shapes[1].Vertices
                    mesh = slot_class.Struct('Segment', 'vertices', 'faces')
                    mesh.faces = seg2[ii].Faces
            
                    for l in range(len(mesh.faces)):
                        v1 = np.array([shape_tar.vertices[mesh.faces[l][0]][0],shape_tar.vertices[mesh.faces[l][0]][1],shape_tar.vertices[mesh.faces[l][0]][2]])
                        v2 = np.array([shape_tar.vertices[mesh.faces[l][1]][0],shape_tar.vertices[mesh.faces[l][1]][1],shape_tar.vertices[mesh.faces[l][1]][2]])
                        v3 = np.array([shape_tar.vertices[mesh.faces[l][2]][0],shape_tar.vertices[mesh.faces[l][2]][1],shape_tar.vertices[mesh.faces[l][2]][2]])
                
                        v0 = np.vstack((v1,v2))
                        v = np.vstack((v0,v3))

                        h = i % len(Colors)
                        tri = a3.art3d.Poly3DCollection([v])
                        tri.set_color(colors.rgb2hex(Colors[h]))
                        tri.set_color(Colors[h])
                        # tri を追加            
                        ax.add_collection3d(tri)

                    # 軸ラベルの設定
                    ax.set_xlabel("X-axis")
                    ax.set_ylabel("Y-axis")
                    ax.set_zlabel("Z-axis")
            
                    ax.set_xlim(np.min(shape_tar.vertices[:,0]), np.max(shape_tar.vertices[:,0]))
                    ax.set_ylim(np.min(shape_tar.vertices[:,1]), np.max(shape_tar.vertices[:,1]))
                    ax.set_zlim(np.min(shape_tar.vertices[:,2]), np.max(shape_tar.vertices[:,2]))
                    
    pl.show()
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return None
    
######################################################################
#                           Main
######################################################################

######################################################################
#                           END
######################################################################





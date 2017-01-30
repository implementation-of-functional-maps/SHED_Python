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
    # print(shape_list)
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
    elevation = - pi / 10
    # For planes:
    # elevation = - pi / 5

    # This color map is used in order to color segments.
    # Colors: [Yellow, Blue, Red, Turquoise, Green, Orange, Purple, Dark Blue, 
    #          Dark Green, Dark Red, Light Gray, Dark Gray, Pink]
    Colors = np.array([[0.9,0.9,0.5],[0.15,0.6,0.8],[1,0.4,0.4],[0.4,0.8,0.7],[0.5,0.8,0.45],[1,0.5,0.33],[0.55, 0.33,0.7],[0.35,0.45,1],[0.2,0.8,0.5],[0.8,0.4,0.2],[0.75,0.75,0.75],[0.5,0.5,0.5],[0.2,0.5,0.5],[0.95,0.65,0.8]])

    ## Render source shape:
    seg = Shapes[src_id].Segments
    s = len(seg)    # number of segments
    print("s: " , s)
    shape_center = Shapes[src_id].BB.center
    
    import my_modules.slot_class as slot_class
    shape = slot_class.Struct('Shape', 'vertices', 'faces')
    shape.vertices = Shapes_render[src_id].Vertices
    shape.faces = Shapes_render[src_id].Faces
            
    import RenderShowMatch.mesh_rotate as mesh_rotate
    import numpy.matlib
    # import RenderShowMatch.MakeFigureNice as MakeFigureNice
    for r in range(rot_num):

        # For each segment:
        for i in range(s):
            mesh = slot_class.Struct('Segment', 'vertices', 'faces')
            mesh.vertices = seg[i].Vertices
            # mesh.faces = np.fliplr(seg[i].Faces)
            mesh.faces = seg[i].Faces
            # shape.faces = np.fliplr(shapes[i].Faces)
            # Rotate mesh for better looking figures:
            mesh = mesh_rotate._(mesh, [0,1,0], rot_step * r + fix_rot)
            #0.678 for lamps and vases, 0.12 for candles
            mesh = mesh_rotate._(mesh, [1,0,0], elevation) 
            # Add relative distance from shape center:
            seg_center = np.mean(mesh.vertices)
            delta = (seg_center - shape_center) * gap
            delta = numpy.matlib.repmat(delta, len(mesh.vertices), 1)
            mesh.vertices = mesh.vertices + delta
            
    import numpy.matlib
    import random
    # 新規のウィンドウを描画            
    ax = a3.Axes3D(pl.figure())                        
    ## Render target shapes:
    # k = 1
    for j in range(k):
            seg = Shapes[j+1].Segments
            # seg = Shapes[0].Segments
            
            shape_center = Shapes[j+1].BB.center
            st = len(seg)
            print("st: " , st)
            matching = Matchings[0][j][0]
        
            # Produce K rotations of each image:
            # for r in range(rot_num):
            # fig2 = plt.figure()
            # title('Target Shape '+ num2str(j)+ ', r=' + num2str(r), fontsize=25, fontname +'serif') 
            # Go over the original segments and find their matches in the current shape:
            for i in range(s-1):
                # mult = 1
                print("i:", i)
                # For each matching segment:
                for ii in range(st-1):
                        print("ii: ", ii)
                        # if matching[i, ii] == 1: # ??
                        # Take patch data from target shape (ii):
                        mesh.vertices = seg[ii].Vertices
                        mesh.faces = seg[ii].Faces
                        # mesh.faces = np.fliplr(seg[ii].Faces) 
                        # Add relative distance from shape center:
                        # seg_center = np.mean(mesh.vertices)
                        # delta = (seg_center - shape_center) * gap
                        # delta = numpy.matlib.repmat(delta, len(mesh.vertices), 1)
                        # mesh.vertices = mesh.vertices + delta
                        # Add random perturbation to the segments' vertices:
                        # mesh.vertices = mesh.vertices + (rand.shuffle(mesh.vertices) - 0.5) / 1000
                        # Rotate mesh for better looking figures: ??
                        # mesh = mesh_rotate._(mesh, [0, 1, 0], rot_step*r + fix_rot) #0.678 for lamps and vases, 0.12 for candles
                        # mesh = mesh_rotate._(mesh, [1, 0, 0], elevation) 
                        ax = a3.Axes3D(pl.figure())
                        
                        v1 = np.array([shape.vertices[mesh.faces[0][0]]])
                        v2 = np.array([shape.vertices[mesh.faces[0][1]]])
                        v3 = np.array([shape.vertices[mesh.faces[0][2]]])

                        v0 = np.vstack((v1,v2))
                        v  = np.vstack((v0,v3))
                        #------------------------------------------------------------        
                        for l in range(1, len(mesh.faces)):
                            v1 = np.array([shape.vertices[mesh.faces[l][0]]])
                            v2 = np.array([shape.vertices[mesh.faces[l][1]]])
                            v3 = np.array([shape.vertices[mesh.faces[l][2]]])
                
                            v0 = np.vstack((v1,v2))
                            v0 = np.vstack((v0,v3))
                            
                            v  = np.vstack((v,v0))
                
                        print(v)
                        
                        h = ii % len(Colors)
                        print("color_h: ", Colors[h])
                        
                        tri = a3.art3d.Poly3DCollection([v])
                        tri.set_color(colors.rgb2hex(Colors[h])) # 縁の色の指定
                        tri.set_color(Colors[h]) # 色の指定

                        # tri を追加
                        ax.add_collection3d(tri)

                        # 軸ラベルの設定
                        ax.set_xlabel("X-axis")
                        ax.set_ylabel("Y-axis")
                        ax.set_zlabel("Z-axis")
                
                        ax.set_xlim(np.min(v[:,0]), np.max(v[:,0]))
                        ax.set_ylim(np.min(v[:,1]), np.max(v[:,1]))
                        ax.set_zlim(np.min(v[:,2]), np.max(v[:,2]))
    
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





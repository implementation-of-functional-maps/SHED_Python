# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: RenderMatchingFigure.py
#                       Last Change : 2016-10-04
#                       Editted by : Katsurou Takahashi
###################################################################
##################################################################
#                       Import
##################################################################
# http://qiita.com/ynakayama/items/8d3b1f7356da5bcbe9bc
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import numpy as np
import pandas
from numpy.random import randn
import scipy as sp
import numpy.matlib
# matplotlib
from matplotlib import font_manager
import mpl_toolkits.mplot3d
import matplotlib.figure as figure
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import mpl_toolkits.mplot3d as a3
import pylab as pl
##################################################################
#                       Method
##################################################################
def _( Shape ):
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
    Colors = np.array([[0.9,0.9,0.5],[0.15,0.6,0.8],[1,0.4,0.4],[0.4,0.8,0.7],[0.5,0.8,0.45],[1,0.5,0.33],[0.55, 0.33,0.7],[0.35,0.45,1],[0.2,0.8,0.5],[0.8,0.4,0.2],[0.75,0.75,0.75],[0.5,0.5,0.5],[0.2,0.5,0.5],[0.95,0.65,0.8]])

    ## Render source shape:
    import my_modules.slot_class as slot_class
    shape = slot_class.Struct('Shape', 'vertices', 'faces')
    shape.vertices = Shape.Vertices
    shape.faces = Shape.Faces

    ax = a3.Axes3D(pl.figure())
            
    # v1 = np.array([shape.vertices[shape.faces[0][0]][0],shape.vertices[shape.faces[0][0]][1],shape.vertices[shape.faces[0][0]][2]])
    # v2 = np.array([shape.vertices[shape.faces[0][1]][0],shape.vertices[shape.faces[0][1]][1],shape.vertices[shape.faces[0][1]][2]])
    # v3 = np.array([shape.vertices[shape.faces[0][2]][0],shape.vertices[shape.faces[0][2]][1],shape.vertices[shape.faces[0][2]][2]])

    # v0 = np.vstack((v1,v2))
    # v  = np.vstack((v0,v3))

    # for i in range(1, len(shape.faces)):
    for i in range(len(shape.faces)):
        v1 = np.array([shape.vertices[shape.faces[i][0]][0],shape.vertices[shape.faces[i][0]][1],shape.vertices[shape.faces[i][0]][2]])
        v2 = np.array([shape.vertices[shape.faces[i][1]][0],shape.vertices[shape.faces[i][1]][1],shape.vertices[shape.faces[i][1]][2]])
        v3 = np.array([shape.vertices[shape.faces[i][2]][0],shape.vertices[shape.faces[i][2]][1],shape.vertices[shape.faces[i][2]][2]])
                
        v0 = np.vstack((v1,v2))
        v = np.vstack((v0,v3))
        # v0 = np.vstack((v0,v3))
        # v  = np.vstack((v,v0))
                
        tri = a3.art3d.Poly3DCollection([v])
        tri.set_color(colors.rgb2hex(Colors[0]))
        tri.set_color(Colors[0])
            
        ax.add_collection3d(tri)
            
    # 軸ラベルの設定
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    # 表示範囲の設定
    ax.set_xlim(np.min(shape.vertices[:,0]), np.max(shape.vertices[:,0]))
    ax.set_ylim(np.min(shape.vertices[:,1]), np.max(shape.vertices[:,1]))
    ax.set_zlim(np.min(shape.vertices[:,2]), np.max(shape.vertices[:,2]))

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
# 擬似乱数 -> wikipedia
# seed



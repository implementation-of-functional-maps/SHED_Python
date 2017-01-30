# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: MakeFigureNice.py
#                       Last Change : 2016-10-04
#                       Editted by : Katsurou Takahashi
######################################################################
##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import numpy as np
import matplotlib as plt
import matplotlib.figure as figure
##################################################################
#                       Method
##################################################################
def  _():
        # Set aspect ratio
        fig = plt.figure(figsize=matplotlib.figure.figaspect(1))
        # http://d.hatena.ne.jp/bettamodoki/20120605/1338863706
        #material dull
        # Set lightning
        #lighting gouraud
        ### Three point lighting (sort of)! # light ??
        light('Position',[0.6,0.6,1],'Style','infinite', 'Color', [0.7,0.7,0.7])
        light('Position',[-1,0.3,-1],'Style','infinite', 'Color', [0.25,0.25,0.25])
        light('Position',[0,-1,1],'Style','infinite', 'Color', [0.3,0.3,0.3])
        light('Position',[-1,1,0.2],'Style','infinite', 'Color', [0.45,0.45,0.45])
        light('Position',[-0.5,0.3,1],'Style','infinite', 'Color', [0.7,0.7,0.7])
        # BLUISH Ambient: # gca
        set(gca, 'AmbientLightColor', [0.45,0.57,0.65])
        # CLAY Ambient:
        # set(gca, 'AmbientLightColor', [0.5 0.36 0.3])
        # set(p, 'AmbientStrength', 1)
        # Set view
        view(0, 90)
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
# light
# set(gca, 'AmbientLightColor', [0.5 0.36 0.3])
# view


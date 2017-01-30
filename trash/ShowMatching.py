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
import numpy as np

##################################################################
#                       Method
##################################################################
def _( Shape1, Shape2, matching ):
    # ShowMatching Shows the given matching between two given shapes in one
    # figure. On the left the shape with less parts is presented with color
    # coded segments. The other shape is presented on the right and each
    # segment is colored according to its match in Shape1.
    # If several parts are matched to the same part in the shape on the right,
    # the segment is colored with two overlaying colors.
    #
    ### If you use this code, please cite the following paper:
    #
    # for Fine-grained in range(Similarity):
    #  Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
    #  SIGGRAPH ASIA 2015
    #
    ### Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>


    [n,m] = [len(matching), len(mathing[0])]

    if (n > m):
        ##        figure('Name', 'Shape 2 : Shape 1')
        matching = matching.T
        
        # Seg1 is the source (left), Seg2 is the target (right)
        Seg2 = Shape1.Segments
        Seg1 = Shape2.Segments

    else:
        ##        figure('Name', 'Shape 1 : Shape 2')
        # Seg1 is the source (left), Seg2 is the target (right)
        Seg1 = Shape1.Segments
        Seg2 = Shape2.Segments

    h_shape1 = subplot(1, 2, 1)
    h_shape2 = subplot(1, 2, 2)
    # A set of colors that is used to color the segments:
    # colors = [
    #     0 0 1
    #     0 1 0
    #     1 0 0
    #     0.5 0.5 0
    #     0 0.5 0.5
    #     0.5 0 0.5
    #     0.1 0.1 0.1
    #     0.5 0.5 0.5
    #     0.5 0 1
    #     0 0.5 1
    #     0 1 0.5
    #     0.5 1 0
    #     1 0.5 0
    #     1 0 0.5
    #     0.25 0.5 0.75
    #     0.75 0.5 0.25
    #     0.25 0.75 0.5
    #     0.75 0.25 0.5
    #     0.5 0.25 0.75
    #     0.5 0.75 0.25
    # ]1
    f1_hold = 0
    f2_hold = 0
    v_add = 0

    for i in range(n):
        if (i <= len(Seg1)):
            Si = Seg1[i]
        else:
            Si = []
        if (i < 21):
            c = colors[i]
        else:
            c = rand[0][2]
            # Too many segments - using a random color:

        if (~isempty(Si)):
            # Draw segment in left figure:
            if (f1_hold):
                v = Si.Vertices
                subplot(h_shape1)
            # Reduce number of vertices if it is high:
            if (len(v) > 200):
                ind_large = np.random.permutation(len(v)) # randperm(len(v), 200) # randperm ??
                ind = []
                for i in range(200):
                    ind.append(ind_large[i])
            else:
                ind = len(v)
                
            # Actual drawing of the segment using scatter3:
            scatter3(v(ind, 1), v(ind, 2), v(ind, 3), 30, c, 'filled')
            f1_hold = 1
            ## axis equal         # 
            # Find matching segments to Si:
            match_ind = 0
            for j in range(m):
                if (matching(i, j)):
                    if (j <= len(Seg2)):
                        Sj = Seg2[j]
                    else:
                        Sj = []
                        
                if (~isempty(Sj)):
                    # Draw each matching segment in the right figure:
                    v = Sj.Vertices + v_add
                    subplot(h_shape2)
                    if (f2_hold):
                        ## hold on
                        pass
                    # Reduce number of vertices if it is high:
                    if (len(v) > 200):
                        ind = randperm(len(v), 200) # ??
                    else:
                        ind = len(v)

                    # Actual drawing of the segment using scatter3 with the
                    # same color as Si. If there are several matches each
                    # match will be drawn in a slightly darker color to
                    # distinguish between the parts (this only matters if
                    # the matching parts are adjacent):
                    scatter3(v(ind, 1), v(ind, 2), v(ind, 3), 30, c * (0.9^match_ind), 'filled')
                    f2_hold = 1
                    ## axis equal
                    match_ind = match_ind + 1

    v_add = v_add + 0.002

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


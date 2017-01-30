# -*- mode:python; coding:utf-8 -*-
from __future__ import print_function # これなにをしたかった？
######################################################################
#                       File Name: .py
#                       Last Change : 2016-10-04
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
def _( Shape, Segments ):
    '''
    # AllSegmentsBoundingBoxes Finds the bounding box of each segment in a
    # segmented shape structure.
    #
    ### If you use this code, please cite the following paper:
    #
    #  SHED: Shape Edit Distance for Fine-grained Shape Similarity 
    #  Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
    #  SIGGRAPH ASIA 2015
    #
    ### Copyright (c) 2016 Katsurou Takahashi <katsurou.tkhsk@gmail.com>
    '''
    ##################################################################
    #                       Init Settings
    ##################################################################

    nseg = len(Segments)

    Shape.TotalVolume = 0
    Shape.TotalRootVolume = 0
    ##################################################################
    #                       Calcurate Bounding Boxes
    ##################################################################
    import ReadSegmentedShape.Descriptors.CalcBoundingBox as CalcBoundingBox
    for i in range(nseg):
        # Calculates the bounding box of the current segment:
        BB = CalcBoundingBox._(Segments[i].Vertices)
        Segments[i].BB = BB
        # print("Segments_i.BB.volume:", BB.volume)
        # Total volume of the shape is the sum of the volume of all segments:
        Shape.TotalVolume = Shape.TotalVolume + BB.volume # BB.volume

    Shape.AverageVolume = Shape.TotalVolume / nseg
    #-----------------------------------------------------------------
    # Return
    #-----------------------------------------------------------------
    return [Shape.AverageVolume, Shape.TotalVolume]

######################################################################
#                           END
######################################################################
# checked

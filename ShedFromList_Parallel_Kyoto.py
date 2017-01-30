# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: ShedFromList.py
#                       Last Change : 2016-10-04
#                       Editted by : Katsurou Takahashi
######################################################################
##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import numpy as np
# import time
##################################################################
#                       Method
##################################################################
def _( i, j ):
    '''
    # SHEDfromList loads all shapes in the list file, and computes the matching
    # and SHED between each pair of shapes.
    # Note that this function uses DEFAULT weights. To run with different
    # weights use BatchShedFromMatching on the output.
    #
    # Input:
    # extension - in range(for):
    # for segments in range(".seg".):
    #
    # Output:
    # shapes in in range(list.):
    #
    # Matchings = a cell array where cell {i, j} is the matching matrix of
    #             shape i to shape j
    # Shapes = the collection of loaded segmented shapes with their computed
    #          bounding boxes and volumes
    # shape_files = the list of file names. Useful to see which shape
    #               corresponds to each file without opening the file
    #               externally.
    #
    ### If you use this code, please cite the following paper:
    #
    # for Fine-grained in range(Similarity):
    #  Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
    #  SIGGRAPH ASIA 2015
    #
    ### Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>
    '''
    ######################################################################
    #                           File Open
    ######################################################################
    # start = time.time()
    off_end = '.off'

    f = open('list_kyoto.txt')
    lines = f.readlines()
    f.close()

    elems = lines[i].rstrip().split("/")
    shape_file_1 = elems[1]
    
    elems = lines[j].rstrip().split("/")
    shape_file_2 = elems[1]
 
    ######################################################################
    #             Read Segmented Shape              
    ######################################################################
    shed = np.zeros(2)
    # Read shapes:
    # Add appropriate extensions:
    off1 = 'data/'+ shape_file_1 + off_end
    off2 = 'data/'+ shape_file_2 + off_end

    import ReadSegmentedShape.ReadSegmentedShape_Kyoto as ReadSegmentedShape
    # 1.Parse segmented shape files:
    # 2.segment in in range(shape:):
    # 3.descriptors for in range(segment:):
    Shape1 = ReadSegmentedShape._(off1)
    Shape2 = ReadSegmentedShape._(off2)

    # end = time.time()
    # print('シェイプ('i+','+j+')読み込み時間'+ (end-start) +' 秒')   
    ######################################################################
    #            Batch Matching Shapes
    ######################################################################
    # start = time.time()
    
    import BatchSHED.MatchShapes as MatchShapes
    Matching = MatchShapes._(Shape1, Shape2)
      
    import BatchSHED.ShedFromMatching as ShedFromMatching
    shed = ShedFromMatching._(Shape1, Shape2, Matching)
    
    # end = time.time()
    # print("shed 算出作成時間"+ (end-start)+' 秒')   
    #---------------------------------------------------------------------
    #                          Return
    #---------------------------------------------------------------------
    return shed 

######################################################################
#                           END
######################################################################


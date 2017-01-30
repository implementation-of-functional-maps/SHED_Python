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
##################################################################
#                       Method
##################################################################
def _( list1_filename, list2_filename ):
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
    off_end = '.off'
    seg_end = '.seg'

    f = open(list1_filename)
    lines_1 = f.readlines()
    f.close()

    g = open(list2_filename)
    lines_2 = g.readlines()
    g.close()

    shape_files_1_=[]
    for line in lines_1:
        elems = line.rstrip().split("/")
        shape_files_1_.append(elems[1])


    shape_files_2_=[]
    for line in lines_2:
        elems = line.rstrip().split("/")
        shape_files_2_.append(elems[1])

    # t = toc # fic は?
    # print('Read file names in '+ num2str(t) +' seconds.')
    ######################################################################
    #             Read Segmented Shape              
    ######################################################################
    n = len(shape_files_1_)
    shed = np.zeros(n)
    Shapes1 = []
    # Read shapes:
    # ticID = tic # ??
    for i in range(n):
        # Add appropriate extensions:
        off = 'data/'+ shape_files_1_[i] + off_end
        # seg = 'data/'+ shape_files_1_[i] + seg_end

        import ReadSegmentedShape.ReadSegmentedShape_Kyoto as ReadSegmentedShape
        # 1.Parse segmented shape files:
        # 2.segment in in range(shape:):
        # 3.descriptors for in range(segment:):
        Shape1 = ReadSegmentedShape._(off)
        # Output shape:
        Shapes1.append(Shape1)
        # t = toc
        # print('Read shape '+ shape_files[i] +' in '+ num2str(t) +' seconds.')
        
    m = len(shape_files_2_)
    shed = np.zeros(m)
    Shapes2 = []
    # Read shapes:
    # ticID = tic # ??
    for i in range(m):
        # Add appropriate extensions:
        off = 'data/'+ shape_files_2_[i] + off_end
        # seg = 'data/'+ shape_files_2_[i] + seg_end

        import ReadSegmentedShape.ReadSegmentedShape_Sapporo as ReadSegmentedShape_Sapporo
        # 1.Parse segmented shape files:
        # 2.segment in in range(shape:):
        # 3.descriptors for in range(segment:):
        Shape2 = ReadSegmentedShape_Sapporo._(off, seg)
        # Output shape:
        Shapes2.append(Shape2)
    # t = toc(ticID)
    # print('Read files and analyze parts in '+ num2str(t) +' seconds.')
    ######################################################################
    #            Batch Matching Shapes
    ######################################################################
    import BatchSHED.BatchMatch_Parallel as BatchMatch_Parallel
    # Find matching between each pair of shapes:
    Matchings = BatchMatch_Parallel._(Shapes1, Shapes2)
    import BatchSHED.BatchShedFromMatching_Parallel as BatchShedFromMatching_Parallel
    # each pair in range(shapes:):
    [shed, costs] = BatchShedFromMatching_Parallel._(Shapes1, Shapes2, Matchings)

    #---------------------------------------------------------------------
    #                          Return
    #---------------------------------------------------------------------
    return shed # [ shed, Matchings, Shapes1, Shapes2, shape_files_1_, shape_files_2_ ]

######################################################################
#                           Main
######################################################################

######################################################################
#                           END
######################################################################


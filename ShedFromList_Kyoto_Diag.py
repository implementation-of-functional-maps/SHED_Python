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
def _( list_filename , i_diag, j_diag, devide_n=5):
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

    f = open(list_filename)
    lines = f.readlines()
    f.close()

    shape_files=[]
    for line in lines:
        elems = line.rstrip().split("/")
        shape_files.append(elems[1])
    # print('Read file names in '+ num2str(t) +' seconds.')
    ######################################################################
    #             Read Segmented Shape              
    ######################################################################
    n = len(shape_files)
    segmented_n =  n // devide_n
    shed = np.zeros(n)
    Shapes1 = []
    Shapes2 = []

    if devide_n -1 ==  i_diag and i_diag == j_diag:
        init_shape = segmented_n * i_diag
        for i in range(init_shape, n):
            # Add appropriate extensions:
            off = 'data/'+ shape_files[i] + off_end
            print("shape_files:",shape_files[i])
            import ReadSegmentedShape.ReadSegmentedShape_Kyoto as ReadSegmentedShape_Kyoto
            # 1.Parse segmented shape files:
            # 2.segment in in range(shape:):
            # 3.descriptors for in range(segment:):
            Shape = ReadSegmentedShape_Kyoto._(off)
            # Output shape:
            Shapes1.append(Shape)
            ######################################################################
            #            Batch Matching Shapes
            ######################################################################
            import BatchSHED.BatchMatch as BatchMatch
            # Find matching between each pair of shapes:
            Matchings = BatchMatch._(Shapes1)
            import BatchSHED.BatchShedFromMatching_Diag as BatchShedFromMatching
            # each pair in range(shapes:):
            [shed, costs] = BatchShedFromMatching._(Shapes1, Matchings)
            #---------------------------------------------------------------------
            #                          Return
            #---------------------------------------------------------------------
            return [ shed, Matchings, Shapes, shape_files ]

            
    elif  devide_n -1 != i_diag and i_diag == j_diag:
        init_shape = segmented_n * i_diag
        term_shape = segmented_n * (i_diag + 1)
        for i in range(init_shape, term_shape):
            # Add appropriate extensions:
            off = 'data/'+ shape_files[i] + off_end
            print("shape_files:",shape_files[i])
            import ReadSegmentedShape.ReadSegmentedShape_Kyoto as ReadSegmentedShape_Kyoto
            # 1.Parse segmented shape files:
            # 2.segment in in range(shape:):
            # 3.descriptors for in range(segment:):
            Shape = ReadSegmentedShape_Kyoto._(off)
            # Output shape:
            Shapes1.append(Shape)
            ######################################################################
            #            Batch Matching Shapes
            ######################################################################
            import BatchSHED.BatchMatch as BatchMatch
            # Find matching between each pair of shapes:
            Matchings = BatchMatch._(Shapes1)
            import BatchSHED.BatchShedFromMatching_Diag as BatchShedFromMatching
            # each pair in range(shapes:):
            [shed, costs] = BatchShedFromMatching._(Shapes1, Matchings)
            #---------------------------------------------------------------------
            #                          Return
            #---------------------------------------------------------------------
            return [ shed, Matchings, Shapes, shape_files ]

            
    elif devide_n -1 == i_diag and i_diag != j_diag:
        init_shape = segmented_n * i_diag
        for i in range(init_shape, n):
            # Add appropriate extensions:
            off = 'data/'+ shape_files[i] + off_end
            print("shape_files:",shape_files[i])
            import ReadSegmentedShape.ReadSegmentedShape_Kyoto as ReadSegmentedShape_Kyoto
            # 1.Parse segmented shape files:
            # 2.segment in in range(shape:):
            # 3.descriptors for in range(segment:):
            Shape = ReadSegmentedShape_Kyoto._(off)
            # Output shape:
            Shapes1.append(Shape)
        init_shape = segmented_n * j_diag
        term_shape = segmented_n * (j_diag + 1)
        for j in range(init_shape, term_shape):
            # Add appropriate extensions:
            off = 'data/'+ shape_files[j] + off_end
            print("shape_files:",shape_files[j])
            import ReadSegmentedShape.ReadSegmentedShape_Kyoto as ReadSegmentedShape_Kyoto
            # 1.Parse segmented shape files:
            # 2.segment in in range(shape:):
            # 3.descriptors for in range(segment:):
            Shape = ReadSegmentedShape_Kyoto._(off)
            # Output shape:
            Shapes2.append(Shape)
            ######################################################################
            #            Batch Matching Shapes
            ######################################################################
            import BatchSHED.BatchMatch_Parallel as BatchMatch
            # Find matching between each pair of shapes:
            Matchings = BatchMatch._(Shapes1, Shapes2)
            import BatchSHED.BatchShedFromMatching_Diag as BatchShedFromMatching
            # each pair in range(shapes:):
            [shed, costs] = BatchShedFromMatching_Parallel._(Shapes1, Shapes2, Matchings)
            #---------------------------------------------------------------------
            #                          Return
            #---------------------------------------------------------------------
            return [ shed, Matchings, Shapes, shape_files ]


    elif  devide_n -1 != i_diag and i_diag != j_diag:
        init_shape = segmented_n * i_diag
        term_shape = segmented_n * (i_diag + 1)
        for i in range(init_shape, term_shape):
            # Add appropriate extensions:
            off = 'data/'+ shape_files[i] + off_end
            print("shape_files:",shape_files[i])
            import ReadSegmentedShape.ReadSegmentedShape_Kyoto as ReadSegmentedShape_Kyoto
            # 1.Parse segmented shape files:
            # 2.segment in in range(shape:):
            # 3.descriptors for in range(segment:):
            Shape = ReadSegmentedShape_Kyoto._(off)
            # Output shape:
            Shapes1.append(Shape)
        init_shape = segmented_n * j_diag
        term_shape = segmented_n * (j_diag + 1)
        for j in range(init_shape, term_shape):
            # Add appropriate extensions:
            off = 'data/'+ shape_files[j] + off_end
            print("shape_files:",shape_files[j])
            import ReadSegmentedShape.ReadSegmentedShape_Kyoto as ReadSegmentedShape_Kyoto
            # 1.Parse segmented shape files:
            # 2.segment in in range(shape:):
            # 3.descriptors for in range(segment:):
            Shape = ReadSegmentedShape_Kyoto._(off)
            # Output shape:
            Shapes2.append(Shape)
            ######################################################################
            #            Batch Matching Shapes
            ######################################################################
            import BatchSHED.BatchMatch_Parallel as BatchMatch
            # Find matching between each pair of shapes:
            Matchings = BatchMatch._(Shapes1, Shapes2)
            import BatchSHED.BatchShedFromMatching_Diag as BatchShedFromMatching
            # each pair in range(shapes:):
            [shed, costs] = BatchShedFromMatching_Parallel._(Shapes1, Shapes2, Matchings)
            #---------------------------------------------------------------------
            #                          Return
            #---------------------------------------------------------------------
            return [ shed, Matchings, Shapes, shape_files ]


######################################################################
#                           Main
######################################################################

######################################################################
#                           END
######################################################################


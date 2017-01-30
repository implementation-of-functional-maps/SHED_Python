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
def _( list_filename ):
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

    f = open(list_filename)
    lines = f.readlines()
    f.close()

    shape_files=[]
    for line in lines:
        elems = line.rstrip().split("/")
        shape_files.append(elems[1])
    # t = toc # fic は?
    # print('Read file names in '+ num2str(t) +' seconds.')
    ######################################################################
    #             Read Segmented Shape              
    ######################################################################
    n = len(shape_files)
    shed = np.zeros(n)
    Shapes = []
    # Read shapes:
    # ticID = tic # ??
    # proc個のプロセスを用意
    # def read_shapes(i):
    #     # Add appropriate extensions:
    #     off = 'data/'+ shape_files[i] + off_end
    #     seg = 'data/'+ shape_files[i] + seg_end

    #     # import ReadSegmentedShape.ReadSegmentedShape_Sapporo as ReadSegmentedShape_Sapporo
    #     import ReadSegmentedShape.ReadSegmentedShape_Sapporo as ReadSegmentedShape_Sapporo
    #     # 1.Parse segmented shape files:
    #     # 2.segment in in range(shape:):
    #     # 3.descriptors for in range(segment:):
    #     Shape = ReadSegmentedShape_Sapporo._(off, seg)
    #     # Output shape:
    #     Shapes.append(Shape)
    #     return Shapes
        # t = toc
    # print("shapes:",n)
    for i in range(n):
        # Add appropriate extensions:
        off = 'data/'+ shape_files[i] + off_end
        seg = 'data/'+ shape_files[i] + seg_end
        print("shape_files:",shape_files[i])
        import ReadSegmentedShape.ReadSegmentedShape_Sapporo as ReadSegmentedShape_Sapporo
        # 1.Parse segmented shape files:
        # 2.segment in in range(shape:):
        # 3.descriptors for in range(segment:):
        Shape = ReadSegmentedShape_Sapporo._(off, seg)
        # Output shape:
        Shapes.append(Shape)
        # t = toc
        # print('Read shape '+ shape_files[i] +' in '+ num2str(t) +' seconds.')
    
    # t = toc(ticID)
    # print('Read files and analyze parts in '+ num2str(t) +' seconds.')
    ######################################################################
    #            Batch Matching Shapes
    ######################################################################
    import BatchSHED.BatchMatch as BatchMatch
    # Find matching between each pair of shapes:
    Matchings = BatchMatch._(Shapes)
    import BatchSHED.BatchShedFromMatching as BatchShedFromMatching
    # each pair in range(shapes:):
    [shed, costs] = BatchShedFromMatching._(Shapes, Matchings)

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


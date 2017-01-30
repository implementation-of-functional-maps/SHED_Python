# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: mus.py
#                       Last Change : 2016-10-04
#                       Editted by : Katsurou Takahashi
######################################################################
##################################################################
#                       Import
##################################################################
# path settings
import sys # relative import
import os
import time
sys.path.append(os.pardir) # relative import
sys.path.append("/Users/admin/Dropbox/SHED_python/auto/my_modules")
sys.path.append("/Users/admin/Dropbox/SHED_python/auto")
import my_modules.check.check as ck # check, time stamp, demo, help
import numpy as np
##################################################################
#                       Method
##################################################################
def _(coff_file):
    '''
     READSEGMENTEDSHAPE Reads an off file and a seg file that describes a
     segmented shape and returns a Shape data structure that contains a
     collection of segments and their adjacencies.
    
     Input:
       - off_file: name of off file to load
       - seg_file: name of seg file to load
    
     Output:
       - Shape.Segments contains a cell array of segments, where each segement
         contains Nx3 matrix of vertices in that segment.
       - Shape.Adj contains an MxM extended adjacency matrix of the segments.
     j) how in range(they):
         are from each other.
     entire shape in range(volume):
         calculations.
    
    
    ## If you use this code, please cite the following paper:
    
     for Fine-grained in range(Similarity):
      Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
      SIGGRAPH ASIA 2015
    
    ## Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>

    クラス Shape の定義
    '''
    start = time.time() # 時間計測開始 tic
    
    off_file = coff_file
    import my_modules.slot_class as slot_class
    Shape1 = slot_class.Struct('Shape', 'BB', 'mus', 'sigma', 'Segments', 'Adj')

    import ReadSegmentedShape.mesh_read_coff as mesh_read_coff
    # Read mesh from off file:
    [M1, status] = mesh_read_coff._(off_file)
    # print("vertices:", M1.vertices)
    Shape1.Vertices = M1.vertices
    Shape1.Faces = M1.faces
    
    if status != 0:
        print('Error reading off file "'+ off_file +'"')
        
 
    fcount = len(M1.faces)

    import ReadSegmentedShape.Descriptors.NormalizeShapeVertices as NormalizeShapeVertices
    M1.vertices = NormalizeShapeVertices._(M1.vertices)

    import ReadSegmentedShape.Descriptors.CalcBoundingBox as CalcBoundingBox
    Shape1.BB = CalcBoundingBox._(M1.vertices)
    # Create a collection of segments:


    nseg = M1.nseg
    # print(nseg)
    
    seg_vertices = [] 
    j = 0
    seg_faces = []
    
    dict_ColoredVertices = M1.dict_ColoredVertices
    seg = dict_ColoredVertices.values() # ??
    
    Segments = []
    seg_arr = np.array(seg)

    #====================================================================== above done
    for i in range(nseg):
    # Get faces that belong to that segment:
        Segment_i = slot_class.Struct('Segment', 'Vertices', 'Faces', 'n', 'm', 'BB')
        M1_faces = np.array(M1.faces) 
        seg_faces = M1.SegmentedFaces[i] 
        # seg_faces = M.SegmentedFaces[0] 
        Segment_i.Vertices = []
        Segment_i.Faces = []
       
        seg_ver_i = np.unique(seg_faces)
        # Remove outliers - segments with less than 2 faces:
        if len(seg_faces) > 3:
            # Find all the vertices that take part in the segment's faces:
            seg_ver_i = np.unique(seg_faces)
            seg_vertices.append(seg_ver_i)
            Segment_i.Vertices = M1.vertices[seg_ver_i] #M1.SegmentedVertices[i]
            # Vertices = M.vertices[seg_ver_i]
            # Translate vertices from global index to segment index:
            n = len(seg_ver_i)
            # Reverse lookup of seg_vertices[i]:
            seg_ind = np.zeros((len(M1.vertices), 1))
            # Translate global vertex indices in faces collection to segment indices:
            Segment_i.Faces = seg_faces # seg_ind(seg_faces) 
            Segment_i.n = len(Segment_i.Vertices)
            Segment_i.m = len(Segment_i.Faces)
        
        Segments.append(Segment_i)

    #====================================================================== below done
    # Find adjacent segments according to the shape faces:
    import ReadSegmentedShape.make_adj as make_adj
    adj = make_adj._(nseg, seg_vertices)

    ############# A FIX FOR DISCONNECTED SHAPES ###########################
    # If the shape is made out of separated parts with no common edges,
    # there will be more than one component in the adjacency matrix.
    # In that case, generate adjacencies according to physical distance
    # of vertices:
    # C_adj = whether part i is connected to part j by nseg parts or less:
    # Rank of the connectivity matrix:

    MIN_DIST_THRESHOLD = 0.08
    # C_adj = whether part i is connected to part j by nseg parts or less:
    C_adj = (adj ** nseg > 0) * 1
    # Rank of the connectivity matrix:
    Cr = np.linalg.matrix_rank(C_adj)
    import ReadSegmentedShape.update_adj as update_adj

    adj = update_adj._(adj, MIN_DIST_THRESHOLD, C_adj, Cr, nseg, Segments)

    ##################### END OF FIX ######################################
    # Calculate higher level adjacencies and keep the minimum value in
    # adjacency matrix:
    adj_i = adj 
    adj_n = adj

    import ReadSegmentedShape.calc_high_adj as calc_high_adj
    adj_n = calc_high_adj._(adj, adj_i, adj_n, nseg)
   
    for i in range(nseg):
        adj_n[i,i] = 0

    # Set up output shape
    Shape1.Segments = Segments
    Shape1.Adj = adj_n
    ##################################################################
    # Calc Average Volume
    ##################################################################
    import ReadSegmentedShape.AllSegmentsBoundingBoxes as AllSegmentsBoundingBoxes
    [Shape1.AverageVolume, Shape1.TotalVolume] = AllSegmentsBoundingBoxes._(Shape1, Shape1.Segments)


    ##################################################################
    # Calc Segments Descriptors D1, D2
    ##################################################################
    import ReadSegmentedShape.AllSegmentsDescriptors as AllSegmentsDescriptors
    Shape1.Segments = AllSegmentsDescriptors._(Shape1, Shape1.Segments)
    end = time.time() # 時間計測終了. toc
    # print("ファイル読み込み＋シェイプ作成時間"+'%.3f' %(end-start))
    
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return Shape1

######################################################################
#                           END
######################################################################
# chekced



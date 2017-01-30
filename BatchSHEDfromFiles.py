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
import check as ck # check, time stamp, demo, help
import numpy as np
##################################################################
#                       Method
##################################################################
def _( shapes_id ):

    #BATCHPMD Calculates pmd for several shapes in a batch, and outputs all of
    # the distances, matching, etc.


    path_start = 'C:\Yanir\Documents\Projects\SHED\data\Lamps\BigSet\conv\L'
    # path_start = 'C:\Yanir\Documents\Projects\SHED\data\candle\All\conv\'
    # path_start = 'c:\Yanir\Documents\Projects\SHED\data\Vases\Set1\'
    # path_start = 'c:\Yanir\Documents\Projects\SHED\data\Articulated\conv\'
    # path_start = 'c:\Yanir\Documents\Projects\SHED\data\Planes\GoodSet2\P'
    # off_end = '.off'
    # seg_end = '.seg'
    off_end = '-graphcut.off'
    seg_end = '-graphcut.seg'


    n = len(shapes_id)


    shed = zeros(n)
    Matchings = cell(n)
    Shapes = cell[n][1]


    # Read shapes:

    import AllSegmentsBoundingBoxes._ as AllSegmentsBoundingBoxes
    import AllSegmentsD2._ as AllSegmentsD2
    import ReadSegmentedShape._ as ReadSegmentedShape
    for i in range(n):
        off = [path_start, num2str(shapes_id(i)), off_end]
        seg = [path_start, num2str(shapes_id(i)), seg_end]


        # Parse segmented shape files:
        Shape = ReadSegmentedShape(off, seg)
        # Compute the bounding box of each shape:
        Shape = AllSegmentsBoundingBoxes(Shape)
        Shape = AllSegmentsD2(Shape)
        Shapes[i] = Shape


        print('Read shape '+ str(shapes_id(i)) +'.')



    print('Read files and analyze parts in '+ str(t) +' seconds.')

    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return [ shed, Matchings, Shapes ]
   

######################################################################
#                           Main
######################################################################
if __name__ == '__main__':

    ck.today() # time stamp
    
    if len(sys.argv) == 1:
        # input example 
        deltas = [1,2,3,4,5,6,7,8,9,10]
        # output
        func = _(deltas)
        
        ck.std_out_io(sys.argv[0], func, deltas)
        
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-help":
            
            ck.description(16, sys.argv[0])
        
            ck.function(31, 39, sys.argv[0])
            
        else: # ここに nargin を使えない？
            # exec test
            # ex) python mus_xyz.py " python mus_xyz.py "[1,2,3,4,5,6,7,8,9,10]" 4
            list_delta = sys.argv[1].lstrip("[").rstrip("]").split(",")
            deltas=[]
            for delta in list_delta:
                deltas.append(int(delta))
        
            # output
            func = _(deltas)
        
            ck.std_out_io(sys.argv[0], func, deltas)
            
    else:
        print("\nExecution Error: the valiables is invalid.\n")
        
######################################################################
#                           END
######################################################################

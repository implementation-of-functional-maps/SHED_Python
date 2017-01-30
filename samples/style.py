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

##################################################################
#                       Method
##################################################################




    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------

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


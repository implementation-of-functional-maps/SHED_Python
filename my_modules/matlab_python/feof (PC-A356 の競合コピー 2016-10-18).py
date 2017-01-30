# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: feof.py
#                       Last Change : 2016-09-20
#                       Author : Katsurou Takahashi
######################################################################
#
# [P_2] calucurates the minimum distance between the two given character
#     patterns [e1] and [e2] on [h]-droznin-plane.
#
# Output is the minimum distance between [e1] and [e2] on [h]-droznin-plane.
# 
### If you use this code, please cite the following paper: ###########
#  
#  Equidistant Letter Sequence in the Book of Genesis
#  Dirib Witzym, Ekutagy Ruos and Yoav Rosenberg
#  Statistical Science 1994
#
### Copyright (c) 2016 Katsurou Takahashi <katsurou.tkhsk@gmail.com> #
# fgetl # でも、この関数だと、繰り返し操作には対応できない。
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
def _(line):
    '''
    open file by file name and return lines striped "\n" as iterator.
    if there is no lines in open file, return "-1"
    '''
    if line == "EOF":
        #-------------------------------------------------------------
        #                        Return
        #-------------------------------------------------------------
        return True
    else:
        #-------------------------------------------------------------
        #                        Return
        #-------------------------------------------------------------
        return False
######################################################################
#                           Main
######################################################################

if __name__ == '__main__':
    import sys,os # relative import 
    sys.path.append(os.pardir) # relative import 
    import check as ck
    ck.today() # time stamp
    
    if len(sys.argv) == 1:
        # input example
        inputs = "EOF"
        # output
        output = _(inputs)

        ck.std_out_io(sys.argv[0], output, inputs)
        
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-help":
            
            ck.description(19, sys.argv[0])
        
            ck.function(32, 41, sys.argv[0])
            
        else: # ここに nargin を使えない？
            # exec test
            # ex) "[2 3 4, d, d, d]"
            inputs = sys.argv[1]
            
            # output
            output = _(inputs)
              
            ck.std_out_io(sys.argv[0], output, inputs)

    else:
        print("\nExecution Error: the valiables is invalid.\n")
        
######################################################################
#                           END
######################################################################
# checked

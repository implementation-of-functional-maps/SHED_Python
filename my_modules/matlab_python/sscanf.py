# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: sscanf.py
#                       Last Change : 2016-10-14
#                       Author : Katsurou Takahashi
######################################################################
#
# [sscanf] calucurates the minimum distance between the two given character
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
##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import
sys.path.append("/Users/admin/Dropbox/SHED_python/auto/my_modules")
sys.path.append("/Users/admin/Dropbox/SHED_python/auto")
import my_modules.check.check as ck # check, time stamp, demo, help
import numpy as np
##################################################################
#                       Method
##################################################################
def _(target_line, *args):
    '''
    input a string line and types of each element spaced
    we split the string line by space"\ " into the elements
    if the types are valid, return the elements.
    else if the types are invalid, return error.
    The scanf is not the same of matlab"s sscanf at the point of treet when the type is "str". 
    Because We use the function for only SHED, 
    and because SHED use sscanf only for float and integer objects, 
    then we can use this module for SHED properly.
    
    '''
    ##################################################################
    # Init Settings
    ##################################################################
    elems = target_line.split(" ")
    count = len(elems)
    ##################################################################
    # Check the Input is Vacant
    ##################################################################
    if target_line == "":
        #-------------------------------------------------------------
        #                        Return
        #-------------------------------------------------------------
        return [[], 0]
    else:
        ck.length_array(elems, len(args))
        
    ##################################################################
    # Check the Input is Integer or Float
    ##################################################################
    elems_type_checked = []
    for i in range(count):
        if args[i] is 'd':
            assert elems[i].find(".") == -1, elems[i]+" must be an integer object."
            ck.input_int(int(elems[i]))
            elems_type_checked.append(int(elems[i]))
        elif args[i] is 'f':
            #if i < 3:
            # print(elems)
            
            # assert elems[i].find(".") != -1, elems[i]+" must be a float object."
            ck.input_float(float(elems[i]))
            elems_type_checked.append(float(elems[i]))
            # else:
                
            
    #-----------------------------------------------------------------
    #                        Return
    #-----------------------------------------------------------------
    return [elems_type_checked, count]

######################################################################
#                           Main
######################################################################
if __name__ == '__main__':
    
    import check as ck
    ck.today() # time stamp
    
    if len(sys.argv) == 1:
        # input example
        f = "f"
        d = "d"
        inputs = "2 3 4"
        import matlab_python.sscanf as sscanf
        [data, count] = sscanf._(inputs, d, d, d)

        # output
        output = [data, count]   
        ck.std_out_io(sys.argv[0], output, inputs, d, d, d)
        
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-help":
            
            ck.description(19, sys.argv[0])
        
            ck.function(32, 41, sys.argv[0])
            
        else: # ここに nargin を使えない？
            # exec test
            # ex) "[2 3 4, d, d, d]"
            list_input = sys.argv[1].lstrip("[").rstrip("]").split(",")
            import matlab_python.sscanf as sscanf
            del listinput[0]
            args = list_input
            [data, count] = sscanf._(inputs, args)
              
            # output
            output = [data, count]   
            ck.std_out_io(sys.argv[0], output, inputs)

    else:
        print("\nExecution Error: the valiables is invalid.\n")
######################################################################
#                           END
######################################################################
# checked

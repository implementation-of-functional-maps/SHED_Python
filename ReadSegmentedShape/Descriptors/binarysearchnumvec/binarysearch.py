# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: sigmas.py
#                       Last Change : 2016-10-03
#                       Editor : Katsurou Takahashi
######################################################################
#  Binary search.
#  Search 'sval' in sorted vector 'x', returns index of 'sval' in 'x'
# 
#  INPUT:
#  x: vector of numeric values, x should already be sorted in ascending order
#     (e.g. 2,7,20,...120)
#  sval: numeric value to be search in x
# 
#  OUTPUT:
#  index: index of sval with respect to x. If sval is not found in x
#         then index is empty.
#
######################################################################
#  Author: Dr. Murtaza Khan
#  Email : drkhanmurtaza@gmail.com
#
### Copyright (c) 2016 Katsurou Takahashi <katsurou.tkhsk@gmail.com> #
##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 


##################################################################
#                       Method
##################################################################
def _(x,val):
    '''
    Binary search. Search 'sval' in sorted vector 'x', returns index of 'sval' in 'x'
    # ex) Input: binarysearch.func([1,2,5,6,18],17)
    #    Output: 3
    '''
    # Step 0
    # ##################################################################
    # #                       Check the Input
    # ##################################################################
    # ck.input_int(val)

    # for item in x:
    #     ck.input_int(item)
    
    # Step 1
    ##################################################################
    #                          Init Setting
    ##################################################################
    # print("x",x)
    if x == []:
        index = 0
        return index
    
    else:
        if val == x[0:1]:
            index = 1
            return index

        if val == (x[len(x)-1:len(x)]):
            index = len(x)
            return index
    
        index = []
        _from = 1
        to    = len(x)
    
        # Step 2.
        ##################################################################
        #                          Binary Search
        ##################################################################
        while _from <= to: 
            mid = round((_from + to)/2)    
            if x[mid:mid+1] <= val and x[mid+1:mid+2] > val:
                index = mid
                return index

            elif x[mid] < val:
                _from = mid + 1
            
            else:
                to = mid - 1
            
        #-----------------------------------------------------------------
        #                        Return
        #-----------------------------------------------------------------  
        return index

######################################################################
#                           Main
######################################################################
if __name__ == '__main__':

    ck.today() # time stamp
    
    if len(sys.argv) == 1:
        # input example 
        x = [1,2,5,6,18]
        val = 17
        # output
        func = _(x, val)
        
        ck.std_out_io(sys.argv[0], func, x, val)
        
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-help":
            
            ck.description(24, sys.argv[0])
        
            ck.function(37, 40, sys.argv[0])
            
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
#                          END
######################################################################
# checked

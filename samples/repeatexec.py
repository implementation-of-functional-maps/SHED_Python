# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: repexec.py
#                       Last Change : 2016-10-14
#                       Editted by : Katsurou Takahashi
######################################################################

######################################################################
#                       Import
######################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import check as ck # check, time stamp, demo, help

######################################################################
#                       Method
######################################################################
def _(L):
    ''' Quick Sort''' # -help でここのディスクリプションも出したい。
    if not L: return L
    pivot = L[0]
    def lt(x): return x <  pivot
    def ge(x): return x >= pivot
    return _(filter(lt, L[1:]))+[pivot]+_(filter(ge, L[1:]))

def test(inputs):
    ''' test Quick Sort'''
    import random
    joe = range(inputs)
    random.shuffle(joe)
    qsJoe = _(joe)
    for i in range(len(qsJoe)):
        assert qsJoe[i] == i, 'qsort is broken at %d!' %i
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return qsJoe

######################################################################
#                           Main
######################################################################
if __name__ == '__main__':
    ck.main(test, 10) 
    # (exec_func, *inputs)
######################################################################
#                           END
######################################################################
# chekced

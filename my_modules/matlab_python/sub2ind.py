# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: ind2sub.py
#                       Last Change : 2016-10-14
#                       Editted by : Katsurou Takahashi
######################################################################

######################################################################
#                       Import
######################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 

######################################################################
#                       Method
######################################################################
def _(matSize, rowSub, colSub): # [%d, %d], %d, %d # 入力がどの型か記録したほうがよい.

    ind = (rowSub) + matSize[0]*(colSub) 
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return ind

######################################################################
#                           Main
######################################################################

######################################################################
#                           END
######################################################################
# chekced

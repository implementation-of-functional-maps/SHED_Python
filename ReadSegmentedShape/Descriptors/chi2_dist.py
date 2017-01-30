# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: chi2_dist.py
#                       Last Change : 2016-10-03
#                       Editor : Katsurou Takahashi
######################################################################
# CHI2_DIST Computes chi-squared distance between the histograms
#
# Author: Yanir Kleiman, 2014
# Editor: Katsurou Takahahsi, 2016
#
### Copyright (c) 2016 Katsurou Takahashi <katsurou.tkhsk@gmail.com> #
##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import numpy as np

##################################################################
#                       Method
##################################################################
def _( hist1, hist2 ):
    '''
    ##################################################################
    # CHI2_DIST Computes chi-squared distance between the histograms
    #
    # Written by Yanir Kleiman, 2014
    # Pythonized by Katsurou Takahahsi, 2016
    ##################################################################
    '''
    
    # Step 1
    ##################################################################
    #                          Init Settings
    ##################################################################
    hist1 = np.array(hist1)
    hist2 = np.array(hist2)
    
    s = hist1 + hist2
    
    diff = pow((hist1 - hist2)[np.where(s != 0)], 2) / s[np.where(s != 0)] 

    d = np.sum(diff)

    #-----------------------------------------------------------------
    #                          Return
    #-----------------------------------------------------------------
    return  d
    
######################################################################
#                           Main
######################################################################
######################################################################
#                          END
######################################################################
# checked

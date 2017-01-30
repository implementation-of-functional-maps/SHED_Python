# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: supertuple.py
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
def _(filename):
    '''
    open file by file name and return lines striped "\n" as iterator.
    if there is no lines in open file, return "-1"
    '''
    try:
        f = open(filename)
        lines = f.readlines()

        f.close()
        lines_striped = []
        for line in lines:
            lines_striped.append(line.strip())
        iterator = iter(lines_striped)
        f.close()
        #-----------------------------------------------------------------
        #                       Return
        #-----------------------------------------------------------------
        return iterator
    
    except IOError:
        #-----------------------------------------------------------------
        #                       Return
        #-----------------------------------------------------------------
        return -1
######################################################################
#                           END
######################################################################
# checked

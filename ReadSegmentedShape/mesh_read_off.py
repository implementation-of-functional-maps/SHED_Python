# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: mesh_read_off.py
#                       Last Change : 2016-10-04
#                       Editted by : Katsurou Takahashi
######################################################################

##################################################################
#                       Import
##################################################################
import sys, os # relative import 
sys.path.append(os.pardir) # relative import
sys.path.append("/Users/admin/Dropgotbox/SHED_python/auto/my_modules")
sys.path.append("/Users/admin/Dropbox/SHED_python/auto")
import my_modules
import numpy as np
##################################################################
#                       Method
##################################################################
def  _(filename):
    '''
    
    This function reads an off file and returns a mesh structure
    
    function [M, status] = mesh_read_off(filename)
    
    Input -
       - filename: name of off file to load
    
    Output -
       - M: triangle mesh: M.vertices(i] represents the 3D coordinates
       of vertex 'i', while M.faces(i] contains the indices of the three
       vertices that compose face 'i'
       - status: this variable is 0 if the file was succesfuly opened, or 1
       otherwise
    
    See also mesh_read
    
    
    Copyright (c) 2008, 2009 Oliver van Kaick <ovankaic@cs.sfu.ca>
    Edit into Python3 by Katsurou Takahashi 2016 <katsurou.tkhs@gmail.com>
    クラス M　の定義
    
    '''
    ##################################################################
    #                           Open file Check
    ##################################################################
    import my_modules.matlab_python.fopen as fopen
    fileID = fopen._(filename) # fileIDは一度呼び出すと消える使いきりのIDなので、使うたびにこの行は必要。何回呼び出してもFileIDはかわらない。
    status = 0
    if fileID == -1:
        print(['ERROR: could not open file "'+ filename +'"'])
        M = []
        status = 1
        #-----------------------------------------------------------------
        #                       Return
        #-----------------------------------------------------------------
        return [M, status]

    ##################################################################
    #                  Read Header, Read Off identifier
    ##################################################################
    import my_modules.matlab_python.fgetiter as fgetiter
    f_iter = fgetiter._(filename)
    import my_modules.matlab_python.fgetl as fgetl
    line = fgetl._(f_iter)

    if line != "OFF": 
        print(['ERROR: file does not have the "OFF" identifier'])
        M = []
        status = 2
        #-----------------------------------------------------------------
        #                       Return
        #-----------------------------------------------------------------
        return [M, status] 

    ##################################################################
    #              Read number of vertices, faces, and edges
    ##################################################################
    line = fgetl._(f_iter)

    import my_modules.matlab_python.sscanf as sscanf
    [data, count] = sscanf._(line, 'd', 'd', 'd')##, '#d #d #d')
    
    if count == 0:
        line = fgetl._(fid)
        [data, count] = sscanf._(line, 'd', 'd', 'd')##, '#d #d #d')
        
    vcount = data[0]
    fcount = data[1]

    V = np.zeros((vcount, 3))
    F = [] 
    
    ##################################################################
    #                           Read content
    ##################################################################
    # read M.vertices
    import my_modules.matlab_python.feof as feof
    for vnum in range(vcount):
        if feof._(line) is False:
            print(['ERROR: file too short'])
        line = fgetl._(f_iter)
        [V[vnum], count] = sscanf._(line, 'f', 'f', 'f')

    for i in range(fcount):
        if feof._(line) is False:
            print(['ERROR: file too short'])
        line = fgetl._(f_iter)
        [data, count] = sscanf._(line, 'd', 'd', 'd', 'd')
        del data[0]
        F.append(data)
        # F.append([data[0]-1, data[1]-1, data[2]-1])

    ##################################################################
    #                      Set up output mesh
    ##################################################################
    import my_modules.slot_class as slot_class
    M_type = slot_class.Struct('M', 'vertices', 'faces')
    M_instance = M_type(V, F)

    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return [M_instance, status]

######################################################################
#                           END
######################################################################
# checked

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
def _( Si, Sj, name ): # name はどこに使用されているか？
    '''
    # ShowMatch Shows a match between segment i and segment j in one figure.
    #
    # Input:
    # Shape construct, in range(example:):
    #          ShowMatch(Shape.Segments{i}, Shape2.Segments{j}, figure_name);
    # name = Name of the output figure.
    #
    ### If you use this code, please cite the following paper:
    #
    # for Fine-grained in range(Similarity):
    #  Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
    #  SIGGRAPH ASIA 2015
    #
    ### Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>
    '''
    import matlab_python.isempty as isempty
    
    if isempty._(Si) == 0:
        v = Si.Vertices
        subplot(1, 2, 1) # ??
        scatter3(v[1], v[2], v[3], 30, 'filled') # ??
        ## axis equal
        
    if isempty._(Sj) == 0:
        v = Sj.Vertices
        subplot(1, 2, 2)
        ## scatter3(v(:, 1), v(:, 2), v(:, 3), 30, 'filled') 
        scatter3(v[1], v[2], v[3], 30, 'filled') 
        ## axis equal
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return None

######################################################################
#                           Main
######################################################################
if __name__ == '__main__':
    inputs = []
    ck.main(_,inputs)
    # manual test がうまくいってない.
    # (exec_func, *inputs)       
        
######################################################################
#                           END
######################################################################
# subplot
# scatter3

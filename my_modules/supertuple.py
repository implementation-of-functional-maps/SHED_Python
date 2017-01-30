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
try:
    from operator import itemgetter
except ImportError:
    def itemgetter(i):
        def getter(self): return selt[i]
        return getter

def superTuple(typename, *attribute_names):
    """名前付き属性を持つ「タプル」のサブクラスを生成して返す"""
    # 適切な __new と __repr__ をサブクラスに持たせる
    nargs = len(attribute_names)
    class supertup(tuple):
        __slots__ = () # メモリを節約。インスタンス毎のディクショナリは不要
        def __new__(cls, *args):
            if len(args) != nargs:
                raise TypeError('%s takes exactly %d arguments (%d given)' %(typename, nargs, len(args)))
            return tuple.__new__(cls, args)
        def __repr__(self):
            return '%s(%s)' % (typename, ', '.join(map(repr, self)))

    # 大事な仕上げ
    for index, attr_name in enumerate(attribute_names):
        setattr(supertup, attr_name, property(itemgetter(index)))
    supertup.__name__ = typename
    return supertup
    
######################################################################
#                           END
######################################################################
# checked

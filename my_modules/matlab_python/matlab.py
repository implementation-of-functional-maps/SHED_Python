# -*- mode:python; coding:utf-8 -*-
#=====================================================================================
#                   File Name: style.py
#                   Last Updated at: 2016-06-20 09:13:19
#                   Last change by: Katsurou Takahashi
#=====================================================================================
# 
# 機  能 : 
#
# 使用法: python style.py file 
#
# 実  例: python style.py file 
#
# 注意点 : 
#
# 参  考 :
#
#-------------------------------------------------------------------------------------
#                        import
#-------------------------------------------------------------------------------------
import sys # 標準入出力
#import Image



# 時間や場所
#import datetime # datetimeモジュールのインポート
#import locale   # import文はどこに書いてもOK(可読性などの為、慣例でコードの始めの方)

# 数値計算
from math import * # 数学の基礎関数
import scipy # 数値計算用 scipy は小さいモジュールを必要に応じて一つ一つ入れていかないといけない.
#from sklearn.metrics.pairwise import paired_distances # 新たに加えたモジュールも自動的に style.py に追加したい。 # pdist2 に必要
import numpy as np # 行列計算用 # eigs 用 http://oppython.hatenablog.com/entry/2015/01/12/042028
import scipy.linalg
import scipy.sparse.linalg as ssl


from numpy.linalg import matrix_rank # rank 用 http://docs.scipy.org/doc/numpy-1.10.4/reference/generated/numpy.linalg.matrix_rank.html


# NLP
#import Mykytea # kyteaのラッパー
import re # 正規表現

# グラフ
#import matplotlib as plt # グラフ描画用

# New
#import 
#-------------------------------------------------------------------------------------
#                        method
#-------------------------------------------------------------------------------------
#標準入力
def Option(input_number):
    if input_number == "-help":
        print("""
#=====================================================================================
#                   File Name: style.py
#                   Last Updated at: 2016-06-20 09:13:19
#                   Last change by: Katsurou Takahashi
#=====================================================================================
# 
# 機  能 : 
#
# 使用法: python style.py file 
#
# 実  例: python style.py file 
#
# 注意点 : 
#
# 参  考 : 
#
#-------------------------------------------------------------------------------------
""")
        sys.exit()
 
# def function():
#
#    return

######################################################################
#                         ファイル処理系
######################################################################
# isempty ~は否定を指す。
def isempty(array):

    if array == []:
        return 1
    else:
        return 0
# array=[1,2]
# print(isempty(array))



# isfield
# M.vertices = X; #  クラス?
def isfield(cls, instances): #instanceは配列として入力 clsはクラスのこと（matlabでは構造体）
    length = len(instances)
    answer=[]
    for instance in instances:
        if hasattr(cls, instance) == True: # hasattr がクラスの属性が定義されているかを判定。
            answer.append(1)
        else:
            answer.append(0)
    return answer
# class Shape(object):
#     def _init_(self, ang):
#         self.ang = ang
# shape = Shape()
# shape.ang = '30'
# array = ['ang','hoge']
# print(isfield(shape, array))

# set
def matlab_set(H, Name, Value):
    H.Name = Value
    return H


# fopen
# fclose(fid); fclose(fid) の python 版
# >>> i = open("trial.txt")
# i = open("trial.txt")
# >>> fid_i = i.fileno()
# fid_i = i.fileno()
# >>> os.close(fid_i)
# os.close(fid_i)
# >>> i
# i
# <_io.TextIOWrapper name='trial.txt' mode='r' encoding='UTF-8'>
# >>> os.close(fid_i)
# os.close(fid_i)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# OSError: [Errno 9] Bad file descriptor
# >>>

def fopen(filename):
    import io
    try:
        f = open(filename, 'r')
        fileID = f.fileno()
        return fileID
    except IOError:
        return -1
# filename = sys.argv[1]
# print(fopen(filename))
# 下記でおなじことができる。
# import io
# f = open("matlab.py")
# # http://python-reference.readthedocs.io/en/latest/docs/file/fileno.html
# f.fileno() # ディスクリプターの表示 # 4 を返す。
# 標準入力のファイル記述子はいつでも 0 で、標準出力は 1、標準エラーは 2 です。 その他にさらにプロセスから開かれたファイルには 3、4、5、などが割り振られます。
# http://docs.python.jp/2.5/lib/os-fd-ops.html

# import io
# f = open("mesh_read_off.py", 'r')
# fileID = f.fileno()
# h = io.open(fileID)
# h_lines = h.readlines()
# f.close()
# for line in h_lines:
#     print(line)


#fgetl, feofと併用のこと
def fgetiter(fileID):
    import io
    try:
        f = io.open(fileID)
        lines = f.readlines()
        lines_striped=[]
        for line in lines:
            lines_striped.append(line.strip())
        iterator = iter(lines_striped)
        f.close()
        return iterator
    except IOError:
        return -1


# fgetl # でも、この関数だと、繰り返し操作には対応できない。
def fgetl(f_iter):
    import io
    f = io.open(fileID)
    f_lines = f.readlines()
    f_iter = iter(f_lines)
    try:
        line = next(f_iter)
        return line
    except StopIteration:
        return -1
    # 例1
# hoge = [1,2,3]
# fid = iter(hoge)
# print(fgetl(fid))
# print(fgetl(fid))
# print(fgetl(fid))
# print(fgetl(fid))
    # 例2
# filename = sys.argv[1]
# fid = f_iter(filename)
# print(fgetl(fid))
# print(fgetl(fid))
# print(fgetl(fid))
# print(fgetl(fid))

# >>> i = open("trial.txt")
# i = open("trial.txt")
# >>> i.read()
# i.read()
# 'EOF?\n'
# >>> i.read()
# i.read()
# ''
# >>> i = open("trial.txt")
# i = open("trial.txt")
# >>> i.readline()
# i.readline()
# 'EOF?\n'
# >>> i.readline()
# i.readline()
# ''
# >>> i.readline()
# i.readline()
# ''
# >>> 
# feof

# def get_input():
#     while True:
#         try:
#             yield ''.join(raw_input())
#         except EOFError:
#             break

# if __name__ == '__main__':
#     a = list(get_input()) # [a1, a2, a3, ...]

# def get_input():
#     while True:
#         try:
#             s = raw_input()
#             if s == '-1':
#                 break
#             yield ''.join(s)
#         except EOFError:
#             break

# 上記の様にEOFError をつかった分岐を利用して　feof 関数を自作
    

# 案1
# # -*- coding: utf-8 -*-

# #!/usr/bin/env python

# filename = 'test.txt'

# with open(filename,'r') as fi:
#     while True:
#         line = fi.readline()
#         if not line:
#             break

# 案2
# # -*- coding: utf-8 -*-

#   #!/usr/bin/env python

#   filename = 'test.txt'

#   with open(filename,'r') as fi
#     while True:
#         try:
#             line = fi.next()
#         except StopIteration: # EOFに到達
#                 break

            
# 上記で同じことができる。
def feof(fid_iter):
    try:
        line = next(fid_iter)
        return None
    except StopIteration:
        return -1
# hoge = [1,2,3]
# fid = iter(hoge)
# print(feof(fid))
# print(feof(fid))
# print(feof(fid))
# print(feof(fid))

# saveas( Image をインポートできない。ただ、これは画像ファイルの保存なので、後回しで良い。
def saveas(image_filename, image_format):
    image.save(image_filename, image_format)
    return None

import inspect
# nargin
def nargin(function):
    nargin = function.func_code.co_argcount
    return nargin
# hoge = [1,2,3]
# fid = iter(hoge)
# print(nargin(feof(fid)))

######################################################################
#                         数値計算系
######################################################################

# chi2_dist # χ2乗距離 ??) /Decs/chi2_dist.m で定義済み
# earthMoverDist ??) 使用されていない関数だった。

import numpy as np
import numpy.matlib 
# repmat
def repmat(A, m, n):
    answer = np.matlib.repmat(A, m, n)
    return answer
# repmat(center, Vn, 1)

# fliplr(
def fliplr(A):
    return np.fliplr(A)

# svd
def svd(X):
    U, S, V = np.linalg.svd(X, full_matrices=True)
    answer = [U, S, V]
    return answer

######################################################################
#                         集合処理系
######################################################################

# cell(n);
def cell(n, m):
    return [[None] * m ] * n
# print(cell(2,3))

def intersect(A, B):
    return set(A).intersection(set(B))
# print( intersect([2,1,3],[2]))

def ind2sub(B, ind):
    indexes = [i for i, x in enumerate(B)]
    ans_indexes=[]
    for i in indexes:
        indexes2 = [j for j,x in enumerate(B[i]) if x == ind]
        if indexes2 != []:
            for j in indexes2:
                ans_indexes.append([i, j]) 
    I=[]
    J=[]
    for item in ans_indexes:
        I.append(item[0])
        J.append(item[1])
    return [I, J]
        
B = [[1,4,7],[2,5,8],[3,6,9]] 
print(ind2sub(B, 3))

def strcmp(S1, S2):
    if S1 == S2:
        return True
    else:
        return False

######################################################################
#                         Matlab未定義関数リスト
######################################################################

# matlab特有の関数
    # 画像処理系
    # lighting gouraud;
    # view(0, 90);
    # daspect(
    # patch(

#-------------------------------------------------------------------------------------
#                        main
#-------------------------------------------------------------------------------------


# import io
# f = open("matlab.py")
# # http://python-reference.readthedocs.io/en/latest/docs/file/fileno.html
# f.fileno() # 
# ディスクリプターの表示 # 4 を返す。
# 標準入力のファイル記述子はいつでも 0 で、標準出力は 1、標準エラーは 2 です。 その他にさらにプロセスから開かれたファイルには 3、4、5、などが割り振られます。
# http://docs.python.jp/2.5/lib/os-fd-ops.html

#=====================================================================================
#                        END
#=====================================================================================

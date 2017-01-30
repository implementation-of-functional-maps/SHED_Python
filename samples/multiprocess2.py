# -*- coding: utf-8 -*-
import multiprocessing

def fuga(x): # 並列実行したい関数
    return x*x

def hoge():
    p = multiprocessing.Pool(8) # 8スレッドで実行
    print(p.map(fuga, range(10))) # fugaに0,1,..のそれぞれを与えて並列演算

if __name__ == "__main__":
    hoge()


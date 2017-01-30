# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: .py
#                       Last Change : 2016-10-04
#                       Editted by : Katsurou Takahashi
######################################################################
##################################################################
#                       Import
##################################################################
import sys,os # relative import 
sys.path.append(os.pardir) # relative import 
import numpy as np
import  scipy.spatial.Delaunay as delaunay
import scipy.spatial.cKDTree as cKDTree
import scipy.sparse.linalg as LA
##################################################################
#                       Method
##################################################################
def _(C_0, d, X, P, iterate_num=100):
    #########  ICP   #######
    #データ入力
    #X=[1 2 3; 1 2 7; 8 5 1; 41 90 312; 13 0 38];
    #P=[ 1 3 5; 7 8 9; 4 3 1; 9 0 3213; 32 32 232];
    # X = Coordinate[:, 1:3]
    # P = C_0.real*Coordinate[:, 1:3]
    # C = C_0
    # d_k = 0
    # iterate_number = 100
    n = iterate_num
    f = n
    while n > 1:
        # Update iterate number
        n -= 1
        #P 最近傍点探索
        T = delaunay(P) # , {'QJ'}) optionが不明
        [index_Y_k,d] = cKDTree(P,T,X)
        d_min = min(d)
        #index_Y_k = cKDTree(P,X)
        index_Y_k_index = len(index_Y_k)
        #{Xのインデックス#}
        Xnm =  [len(X), len(X[0])]
        Xn = Xnm[0]
        Xm = Xnm[1]
        #{Pのインデックス#} 
        Pnm =  [len(P), len(P[0])]
        Pn = Pnm[0]# 固有ベクトルの個数　　
        Pm = Pnm[1]# 各固有ベクトルの座標
        #R_qk 更新
        q_k = np.array([1, 0, 0, 0, 0, 0, 0])
        q0 = q_k[0]
        q1 = q_k[1]
        q2 = q_k[2]
        q3 = q_k[3]
        
        R_qk = [q0**2+q1**2-q2**2-q3**2, 2*(q1*q2-q0*q3), 2*(q1*q3+q0*q3), 2*(q1*q2+q0*q3), q0**2+q2**2 - q1**2**q3**2, 2*(q2*q3-q0*q1), 2*(q1*q3 -q0*q2), 2*(q2*q3+q0*q1), q0**2+q3**2-q1**2-q2**2]
        #tau
        x_n = np.array([Xn, Xn, Xn])
        tau = 0
        for i in range(len(Xn)):
            tau = tau + np.sqrt(LA.norm(X[i]-P[i])*LA.norm(X[i]-P[i]))
        tau = tau / Xn
        #mu_x
        mu_x = np.array([0, 0, 0])
        for i in range(Xn):
            mu_x = mu_x + X[i]
        mu_x = mu_x ./ x_n
        #mu_p
        p_n = np.array([Pn, Pn, Pn])
        mu_p = np.array([0, 0, 0])
        for i in range(Pn):
            mu_p = mu_p + P[i]
        mu_p = mu_p / p_n
        # Sigma_PX 更新
        Sigma_PX = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
        x_nn = np.array([Xn, Xn, Xn, Xn, Xn, Xn, Xn, Xn, Xn])
        for j in range(Pn):
            Sigma_PX = Sigma_PX + (P[j] - mu_p).T*(X[j] - mu_x)
        Sigma_PX = Sigma_PX / x_nn
        # trace , A , delta 更新
        tr_Sigma = np.trace(Sigma_PX)
        A = Sigma_PX-Sigma_PX.T
        delta = np.array([A[1, 2] A[2, 0] A[0, 1]]).T
        # 単位行列
        I = np.identity(3)
        # trace*I3
        tr_Sigma_I3 = tr_Sigma*I
        # A  変形
        A2 = A + tr_Sigma_I3
        # Q_Sigma  更新　
        Q_Sigma_PX = np.array([tr_Sigma, delta.T, delta[0], A2[0, 0], A2[1, 0], A2[2, 0], delta[1], A2[1, 0], A2[1, 1], A2[1, 2], delta[2], A2[2, 0], A2[2, 1], A2[2, 2]])
        # Q 固有値算出
        #q_Rの更新
        q_R = LA.eigs(Q_Sigma_PX) 
        #q_Tの更新
        q_T = mu_x.T - R_qk*mu_p.T
        #Pの更新　
        QT = []
        for i in range(len(Pn)):
            QT = [QT, q_T.T]
        P_k = P*R_qk + QT
        P = P_k
        T = delaunay(P, {'QJ'})
        V2 = linsolve(P.T, QT.T)
        C = V2.T + C# is updae.
        if d_min - d_k < tau :
	    break

        d_k = d_min

    matching = C
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return matching

######################################################################
#                           Main
######################################################################
        
######################################################################
#                           END
######################################################################


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
import numpy.linalg as NL
##################################################################
#                       Method
##################################################################
def _(M, Coodinate, iterate_number, argv, argv2):
    ######## LaplaceBertrami Operator ############
    '''
    Calcurate laplace Bertrami operator between two shapes.
    '''
    M = csvread(argv) # ?? ファイル１読み込み
    Size_M=[len(M), len(M[0])]
    M_dim = Size_M[0]
    Adj = np.zeros((M_dim, M_dim))

    for i in range(M_dim-1):
        Adj(M[i], M[i+1])=1
        Adj(M[i+1], M[i])=1

    # ?? ファイル2読み込み 座標?
    cor = csvread(argv2)
    Size_cor = [len(cor), len(cor[0])]
    cor_dim = Size_cor[0]
    
    A = np.zeros((cor_dim, cor_dim))
    B = np.zeros((cor_dim, cor_dim))
    import scipy.spatial.distance as scp
    for i in len(cor_dim):
        for j in len(cor_dim):
            if (i!=j) and (Adj(i, j)==1):
                for k in range(cor_dim):
                for l in range(cor_dim):
                    if (Adj[k, i]==1) and (Adj[k, j]==1) and (Adj[l, i]==1) and (Adj[l, j]==1):
                        Pi = [cor[i, 0] cor[i, 1] cor[i, 2]]
                        Pj = [cor[j, 0] cor[j, 1] cor[j, 2]]
                        Pk = [cor[k, 0] cor[k, 1] cor[k, 2]]
                        Pl = [cor[l, 0] cor[l, 1] cor[l, 2]]
                        
                        Dik = scp.pdist(Pi, Pj) # pdist2 --> scp.pdist ??
                        Djk = scp.pdist(Pj, Pk)
                        Dij = scp.pdist(Pj, Pk)
                        Dil = scp.pdist(Pi, Pl)
                        Djl = scp.pdist(Pj, Pl)
                        #T=delaunayn(P, {'Qt','Qbb','Qc'})
                        # dot == inner_Product
                        dot_Pij_K = np.dot(Pk-Pi, Pk-Pj)
                        dot_Pij_L = np.dot(Pl-Pi, Pl-Pj)
                   
                        AreaK = 0.5 * np.sqrt(Dik*Djk-dot_Pij_K)
                        AreaL = 0.5 * np.sqrt(Dil*Djl-dot_Pij_L)
                        
                        A[i, j] = 0.125 * (Dik*Dik + Djk*Djk - Dij*Dij) / AreaK + 0.125*(Dil*Dil + Djl*Djl - Dij*Dij) / AreaL
                        B[i, j] = (1 / 12) * (AreaK + AreaL)
            elif (i==j) and (Adj[i, j]==1):
                for l in range(cor_dim):
                    for m in range(cor_dim):
                        if (Adj[i, l]==1) and (Adj[i, m]==1) and (Adj[l, m]==1):
                            Pi = [cor[i, 0] cor[i, 1] cor[i, 2]]
                            Pm = [cor[m, 0] cor[m, 1] cor[m, 2]]
                            Pl = [cor[l, 0] cor[l, 1] cor[l, 2]]
                   
                            Dlm = scp.pdist(Pl, Pm)
                            dot_Plm_i = np.dot(Pl-Pi, Pm-Pi)
                            Area =  np.sqrt(Dlm*Dlm-dot_Plm_i)
                   
                            A[i, j] = -0.25 * Dlm / Area
                            B[i, j] = (1/6) * Area
                        

    [V, D] = LA.eig(A, B) # ?

    C_0 = NL.solve(cor[:, 0:2].T, (V*cor[:, 1:3])).T) 
    
    return C_0
######################################################################
#                           Main
######################################################################
        
######################################################################
#                           END
######################################################################
# checked

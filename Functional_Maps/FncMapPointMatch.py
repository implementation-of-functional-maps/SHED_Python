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
##################################################################
#                       Method
##################################################################
def FunctionalMaps(M, Coodinate, iterate_number, argv, argv2):
    ######## LaplaceBertrami Operator ############

    M = csvread(argv) # ?? ファイル１読み込み
    Size_M=[len(M), len(M[0])]
    M_dim=len(Size_M[0])
    Adj=np.zeros((M_dim, M_dim))

    for i in range(M_dim-1):
        Adj(M[i], M[i+1])=1
        Adj(M[i+1], M[i])=1

    # ?? ファイル2読み込み 座標?
    Coordinate = csvread(argv2)
    Size_Coordinate = [len(Coordinate), len(Coordinate[0])]
    Coordinate_dim = Size_Coordinate[0]
    
    A = np.zeros((Coordinate_dim, Coordinate_dim))
    B = np.zeros((Coordinate_dim, Coordinate_dim))
    import scipy.spatial.distance as scp
    for i in len(Coordinate_dim):
        for j in len(Coordinate_dim):
            if (i!=j) and (Adj(i, j)==1):
                for k in range(Coordinate_dim):
                for l in range(Coordinate_dim):
                    if (Adj[k, i]==1) and (Adj[k, j]==1) and (Adj[l, i]==1) and (Adj[l, j]==1):
                        Pi = [Coordinate[i, 1] Coordinate[i, 2] Coordinate[i, 3]]
                        Pj = [Coordinate[j, 1] Coordinate[j, 2] Coordinate[j, 3]]
                        Pk = [Coordinate[k, 1] Coordinate[k, 2] Coordinate[k, 3]]
                        Pl = [Coordinate[l, 1] Coordinate[l, 2] Coordinate[l, 3]]
                        
                        Dik = scp.pdist(Pi, Pj) # scp.pdist --> ??
                        Djk = scp.pdist(Pj, Pk)
                        Dij = scp.pdist(Pj, Pk)
                        Dil = scp.pdist(Pi, Pl)
                        Djl = scp.pdist(Pj, Pl)
                        #T=delaunayn(P, {'Qt','Qbb','Qc'})       
                        inner_Product_Pij_K = dot(Pk-Pi, Pk-Pj)
                        inner_Product_Pij_L = dot(Pl-Pi, Pl-Pj)
                   
                        AreaK = 0.5 * np.sqrt(Dik*Djk-inner_Product_Pij_K)
                        AreaL = 0.5 * np.sqrt(Dil*Djl-inner_Product_Pij_L)
                        
                        A[i, j] = 0.125*(Dik*Dik+Djk*Djk-Dij*Dij)/AreaK+0.125*(Dil*Dil+Djl*Djl-Dij*Dij)/AreaL
                        B[i, j]=1/12*(AreaK+AreaL)
            elif (i==j) and (Adj[i, j]==1):
                for l in range(Coordinate_dim):
                    for m in range(Coordinate_dim):
                        if (Adj[i, l]==1) and (Adj[i, m]==1) and (Adj[l, m]==1):
                            Pi = [Coordinate[i, 1] Coordinate[i, 2] Coordinate[i, 3]]
                            Pm = [Coordinate[m, 1] Coordinate[m, 2] Coordinate[m, 3]]
                            Pl = [Coordinate[l, 1] Coordinate[l, 2] Coordinate[l, 3]]
                   
                            Dlm = scp.pdist(Pl, Pm)
                 
                            inner_Product_Plm_i = dot(Pl-Pi, Pm-Pi)
                   
                            Area =  np.sqrt(Dlm*Dlm-inner_Product_Plm_i)
                   
                   
                            A(i, j)=-0.25*Dlm/Area
                            B(i, j)=1/6*Area
                        
    # checked
    [V, D]=eig(A, B) # ?

    C_0 = linsolve(Coordinate[:, 1:3].T, (V*Coordinate[:, 2:4)).T) #?

    #########  ICP   #######
    #データ入力
    #X=[1 2 3; 1 2 7; 8 5 1; 41 90 312; 13 0 38];
    #P=[ 1 3 5; 7 8 9; 4 3 1; 9 0 3213; 32 32 232];

    X=Coordinate[:, 2:4);
    P=real(C_0)*Coordinate[:, 2:4);
    C=C_0

    d_k=0
    iterate_number = 100
    n = iterate_number
    #n=1000;
    f = n 
    while n>1:

        n=n-1;
        #P 最近傍点探索
        T=delaunayn(P, {'QJ'})
        [index_Y_k,d] = dsearchn(P,T,X)
        d_min=min(d)

        #index_Y_k = dsearchn(P,X)
        index_Y_k_index = size(index_Y_k)

        #{Xのインデックス#}
        Xnm=  len(X)
        Xn= Xnm(1, 1)
        Xm= Xnm(1, 2)
        #{Pのインデックス#} 
        Pnm=  size(P)
        Pn= Pnm(1, 1)# 固有ベクトルの個数　　
        Pm= Pnm(1, 2)# 各固有ベクトルの座標


        #R_qk 更新
        q_k = [1 0 0 0 0 0 0]
        q0 = q_k(1, 1)
        q1 = q_k(1, 2)
        q2 =  q_k(1, 3)
        q3 = q_k(1, 4)
        R_qk = [q0^2+q1^2-q2^2-q3^2 2*(q1*q2-q0*q3) 2*(q1*q3+q0*q3); 2*(q1*q2+q0*q3) q0^2+q2^2-q1^2^q3^2 2*(q2*q3-q0*q1); 2*(q1*q3 -q0*q2) 2*(q2*q3+q0*q1) q0^2+q3^2-q1^2-q2^2]
        #tau
        x_n = [Xn Xn Xn]
        tau = 0
        for i in range(len(Xn)):
            tau=tau+np.sqrt(norm(X(i:i, :)-P(i:i, :))*norm(X(i:i, :)-P(i:i, :)))

        tau = tau ./ Xn

        #mu_x
        x_n = [Xn Xn Xn]
        mu_x = [0 0 0]
        for i in range(len(Xn)):
            mu_x = mu_x+X(i:i, :)
            
        mu_x=mu_x ./ x_n
        #mu_p
        p_n = [Pn Pn Pn]
        mu_p = [0 0 0]
        for i in range(Pn):
            mu_p = mu_p+P(i:i, :)

        mu_p = mu_p ./ p_n
        # Sigma_PX 更新
        Sigma_PX = [0 0 0; 0 0 0;0 0 0]
        x_nn = [Xn Xn Xn;Xn Xn Xn;Xn Xn Xn]
        for j in range(len(Pn)):
            Sigma_PX = Sigma_PX+(P(j:j,:)-mu_p).T*(X(j:j,:)-mu_x)

        Sigma_PX = Sigma_PX./x_nn
        # trace , A , delta 更新
        tr_Sigma = trace(Sigma_PX);
        A = Sigma_PX-Sigma_PX.T;
        delta = [A(2, 3) A(3, 1) A(1, 2)].T;


        # 単位行列
        I=eye(3)
        # trace*I3
        tr_Sigma_I3 = tr_Sigma*I
        # A  変形
        A2 = A+tr_Sigma_I3
        # Q_Sigma  更新　
        Q_Sigma_PX = [tr_Sigma delta.T; delta(1, 1) A2(1, 1) A2(2, 1) A2(3, 1); delta(2, 1) A2(2, 1) A2(2, 2) A2(2, 3); delta(3, 1) A2(3, 1) A2(3, 2) A2(3, 3)]
        # Q 固有値算出
        eigs_Q_Sigma_PX = eigs(Q_Sigma_PX) 
        #q_Rの更新
        q_R = eigs_Q_Sigma_PX
        
        #q_Tの更新V*Coordinate[:, 2:4)
        q_T = mu_x.T-R_qk*mu_p.T
        #Pの更新　
        QT = []
        for i in range(len(Pn)):
            QT = [QT ; q_T.T]

        P_k = P*R_qk + QT
        P = P_k#*IV*Coordinate[:, 2:4]
        T = delaunayn(P, {'QJ'})

        V2 = linsolve(P.T, QT.T)
        C = V2.T+C# is updae.


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




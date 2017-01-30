import numpy as np
def _(adj, adj_i, adj_n, nseg):
    for i in range(nseg):
        adj_i = adj_i * adj
        # If segment b can be reached from segment a in i steps and no less
        # the value of adj_n(a, b) will be i:
        adj_n[ np.where((adj_n==0)&(adj_i>0)) ]

    ##### FIX: taking care of parts that cannot be reached (adj = 0):
    adj_n[np.where(adj_n == 0)] = nseg + 1
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return adj_n

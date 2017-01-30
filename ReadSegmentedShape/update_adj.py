def _(adj, MIN_DIST_THRESHOLD, C_adj, Cr, nseg, Segments):
    import scipy.spatial
    import numpy as np
    if (Cr > 1):
        # There is more than one component in the adjacency graph!
        # Add parts which are close to each other to the adjacency graph:
        for i in range( nseg - 1 ):
            for j in range(i+1, nseg):
                if adj[i, j] == 0:
                    si = Segments[i].Vertices
                    sj = Segments[j].Vertices
                    Dij = scipy.spatial.distance.cdist(si, sj) # pdist2(si, sj) ??

                    min_dist = np.min( Dij )

                    if (min_dist < MIN_DIST_THRESHOLD): # この判定うまくいってる？　??
                        adj[i, j] = 1
                        adj[j, i] = 1
    return adj

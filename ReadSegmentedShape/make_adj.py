def _(nseg, seg_vertices ):
    import numpy as np
    import my_modules.matlab_python
    adj=np.zeros((nseg, nseg))
    for i in range( len(seg_vertices) ):
        for j in range( len(seg_vertices) ):
            if np.intersect1d(seg_vertices[i], seg_vertices[j]) != np.array([]):
                adj[i, j] = 1
    return adj

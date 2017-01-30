# -*- coding: utf-8 -*-
def _(words1, words2):
    import numpy as np
    lev_dists = np.zeros((len(words1), len(words2)))
    import levenstein
    for i in range(len(words1)):
    	for j in range(len(words2)):
    	    lev_dists[i, j] = levenstein.dist(words1[i], words2[j])

    cos_sims = np.zeros((len(words1), len(words2)))
    import scipy.spatial.distance as dis
    for i in range(len(words1)):
    	for j in range(len(words2)):
    	    cos_sims[i, j] = dis.cosine(lev_dists[i], lev_dists[j])

    cos_sim_mins = []
    for i in range(len(cos_sims)):
    	cos_sim_mins.append(np.min(cos_sims[i]))

    cos_sim_mins_indexes = []
    for i in range(len(cos_sim_mins)):
    	cos_sim_mins_indexes.append(cos_sims[i][np.where(cos_sim_mins[i] == cos_sims[i])])
    
    return lev_dists

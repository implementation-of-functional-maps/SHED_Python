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
def _( Shape1, Shape2, Matching, *W ):
    '''
    # for the in range(shapes):
    # according to the given matching and weights.
    #
    #
    # Shape1, Shape2 = Input shapes to match. Shapes should be initialized with
    #                  a bounding box and descriptors (obtained using
    #                  AllSegmentsBoundingBoxes and AllSegmentsDescriptors
    #                  functions)
    #
    # Matching = Binary matrix which provides the matching between shape parts.
    #            Computed by MatchShapes.
    #
    # W = Weights structure that can be learned from an example set and
    #     contains the following parameters. If no weights are given the
    #     default weights are used.
    #       wGeometry = cost of changing the geometry of a part
    #       wScale = cost of changing the scale of a part
    #       wPosition = cost of changing the position or connectivity of a part
    #       wDuplicate = cost of duplicating a part
    #
    # Outputs:
    # shed = a number that reflects the shape edit distance between the shapes.
    #
    # costs = a structure that contains the following costs. This can be used
    #         to quickly change the weights and recompute SHED without recomputing the
    #         costs.
    # based on in range(descriptors.):
    #                  A complete change in shape geometry should cost "1 unit"
    #                  Weighted by the average volume of the part in the two shapes.
    #
    # their scale in range(volume.):
    #               Doubling (or halving) the size of a single part should cost "1 unit"
    #               Weighted by the average volume of the four parts in the two pairs.
    #
    # based on in range(adjacency.):
    #                  Switching the positions of two parts should cost "1 unit"
    #                  Weighted by the average volume of the four parts in the two pairs.
    #
    # by counting in range(many):
    #                   matches each part have.
    # "1 unit" in range(each):
    #                   additional copy.
    #                   Weighted by the total volume of the duplicated instances.
    #
    ### If you use this code, please cite the following paper:
    #
    # for Fine-grained in range(Similarity):
    #  Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
    #  SIGGRAPH ASIA 2015
    #
    ### Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>
    '''
    # Shape の定義が必要
    def nargin(*arg):
        return len(arg)

    if (nargin( Shape1, Shape2, Matching, W ) < 4):
        #        for the in range(of):
        # shapes that appear in the SHED paper.
        import my_modules.slot_class as slot_class
        W = slot_class.Struct('Weight', 'wGeometry', 'wScale', 'wPosition', 'wDuplicate')
        W.wGeometry = 0.4795
        W.wScale = 0.1258
        W.wPosition = 0.0034
        W.wDuplicate = 0.3914

    alpha = 0.5    # Controls the ratio between D1 and D2 costs
    # checked
    n = len(Matching[0])
    m = len(Matching[0][:,0])

    # Find the indices of matches:
    #import my_modules.matlab_python
    #[row, col] = my_modules.matlab_python.find._(Matching) # ?? find

    [row, col] =  np.nonzero(Matching[0])
    # [row, col] = [ np.nonzero(Matching[0])[0]%len(Shape1.Segments), np.nonzero(Matching[0])[1]%len(Shape2.Segments)] 
    # N = len(row)
    # M = len(col)
    M = len(Matching[0])
    N = len(Matching[0][:,0])
    L = max(N, M)
    # print("M, N, size PositionCosts: ", M, N)
    ## Step 1:
    ##################################################################
    # Computing Geometry costs - shape similarity between each two parts:
    ##################################################################
    GeometryCosts = np.zeros((L, 1))
    MatchVolume = np.zeros((L, 1))
    # MatchVolume = [[None for col in range(1)] for row in range(N)]
    # print("row, col :",row, col)
    
    for i in range(len(row)):
        a = row[i]
        b = col[i]
        Sa = Shape1.Segments[a]
        Sb = Shape2.Segments[b]
        import Descriptors
        costD2 = Descriptors.chi2_dist._(Sa.D2, Sb.D2)
        costD1 = Descriptors.chi2_dist._(Sa.D1, Sb.D1)
        GeometryCosts[i] = (1 - alpha) * costD2 + alpha * costD1
        # print("Sa.BB.volume :", Sa.BB.volume)
        # print("Sb.BB.volume :", Sb.BB.volume)
        MatchVolume[i] = (Sa.BB.volume + Sb.BB.volume) / 2
        # print("MatchVolume[i]: ",MatchVolume[i])

    totalMatchVolume = np.sum(MatchVolume)
    # Normalize volume based so the sum of all match volumes is 1:
    MatchVolume = MatchVolume / totalMatchVolume
    PairsVolume = MatchVolume .dot( MatchVolume.T )
    ## Step 2:
    ##################################################################
    # Computing Scale costs, by measuring the difference in scales in pairs of pairs.
    ##################################################################
    ScaleCosts = np.zeros((L, L))
    for i in range(len(row)-1):
        for j in range(i+1,len(row)):
            a = row[i]
            b = col[i]
            c = row[j]
            d = col[j]
            # Getting the volume of each part from the structure:
            Sa = Shape1.Segments[a].BB.volume
            Sb = Shape2.Segments[b].BB.volume
            Sc = Shape1.Segments[c].BB.volume
            Sd = Shape2.Segments[d].BB.volume
            # Those ratios are 1 if the parts are similar in volume:
            if Sa < Sb :# and Sa[1] < Sb[1] and Sa[2] < Sb[2]: # ここただしい？
                
                # Pairs scale change from a to b (Sab is always less than 1):
                Sab = Sa / Sb
                Scd = Sc / Sd
            else:
                # Pairs scale change from b to a (Sab is always less than 1):
                Sab = Sb / Sa
                Scd = Sd / Sc
            # This value is 1 if the two pairs have similar CHANGE of volume.
            # It is high when the two pairs have very different change of
            # volume. And it is 2 if the change in one pair is exactly twice
            # the change in the other pair.
            
            Smax = max(Sab/Scd, Scd/Sab)
            
            # Make sure the cost is 1 when one pair have exactly twice the change
            # in scale the other pair have. The range of values is now 0 to Inf.
            costScale = Smax - 1
            
            ScaleCosts[i, j] = costScale
            ScaleCosts[j, i] = ScaleCosts[i, j]

    ## Step 3:
    ##################################################################
    # Compute Position costs by comparing the adjacency of each pair of matches.
    ##################################################################
    # If a part has duplicated matches, check the difference in adjacency
    # between the closest pair of duplicated parts.
    PositionCosts = np.zeros((L, L))
    # adjacency for in range(pairs:):
    for i in range(len(row)):
        for j in range(i+1,len(row)):
            a = row[i]
            b = col[i]
            c = row[j]
            d = col[j]

            if a != c and b != d:
                adj_ac = Shape1.Adj[a][c]
                adj_bd = Shape2.Adj[b][d]
                # print("adj_ac, adj_bd :", adj_ac, adj_bd)
                # same adjacency, in range(for):
                # highest for in range(where):
                # parts are adjacent in one shape and far away in the other:
                adj_val = (max(adj_ac, adj_bd)) / (min(adj_ac, adj_bd)) - 1

                PositionCosts[i][j] = adj_val
                PositionCosts[j][i] = adj_val

    # Then fix pairs which are duplicates such that the error is based on the
    # closest instance:
    # For each row with duplicated parts in shape 2:
    for i in range(n):
        if np.sum(Matching[1][i]) > 1:
            # Find indices that belong to that row:
            # ind = np.where(row == i)
            # minCost = np.min(PositionCosts[ind])
            # PositionCosts[ind] = np.matlib.repmat(minCost, len(ind), 1)
            ind = []
            for r in row:
                if r == i:
                    ind.append(r)
                    # ind = np.where(col == j)
                    # if len(ind) != 0:
                    print("ind: ", ind)
                    minCost = np.min(PositionCosts[ind])
                    PositionCosts[ind] = np.matlib.repmat(minCost, len(ind), 1)
            # The cost is no longer symmetric: each duplicated part is compared with
            # its real neighbors and they on the other hand can be compared to
            # the closest instance of the duplicated part.
    # For each column with duplicated parts in shape 1:
    for j in range(m): # m → m-1 は一時的な対処
        if np.sum(Matching[1][:, j]) > 1:
            # Find indices that belong to that column:
            # ind = find(col == j)
            # ind = np.where(col == i)
            # minCost = np.min(PositionCosts[ind[0]])
            # PositionCosts[ind] = np.matlib.repmat(minCost, len(ind[0]), 1)
            ind = []
            for c in col:
                if c == j:
                    ind.append(c)
                    # ind = np.where(col == j)
                    # if len(ind) != 0:
                    print("ind: ", ind)
                    minCost = np.min(PositionCosts[ind])
                    PositionCosts[ind] = np.matlib.repmat(minCost, len(ind), 1)

    ## Step 4: 
    ##################################################################
    # Computing Duplication costs, by aggregating the volume of all duplicated parts:
    ##################################################################
    # When there are no duplicated parts the total match volume is the exactly
    # the average of the total volumes of the two shapes.
    totDuplicate = (totalMatchVolume - Shape1.TotalVolume / 2 - Shape2.TotalVolume / 2) / totalMatchVolume
    if (totDuplicate < 0):
        totDuplicate = 0

    ## Step 5: 
    ##################################################################
    # Aggregate all the costs into one cost function
    # using the given weight parameters:
    ##################################################################
    # Geometry costs are normalized by the relative volume of a match:
    totGeometry = np.sum(GeometryCosts * MatchVolume)
    # Scale and Position costs are normalized by the combined volume of the
    # pair of matches:
    totScale = np.sum(sum(ScaleCosts * PairsVolume))
    totPosition = np.sum(sum(PositionCosts * PairsVolume))

    import my_modules.slot_class as slot_class
    costs = slot_class.Struct('Costs', 'GeometryCosts', 'ScaleCosts', 'PositionCosts', 'AddedCosts', 'MatchVolume', 'PairsVolume', 'totGeometry', 'totScale', 'totPosition', 'totDuplicate')
    costs.GeometryCosts = GeometryCosts
    costs.ScaleCosts = ScaleCosts
    costs.PositionCosts = PositionCosts
    costs.AddedCosts = np.zeros((N, 1))
    # the structure, in range(for):
    # debugging:
    costs.MatchVolume = MatchVolume
    costs.PairsVolume = PairsVolume
    costs.totGeometry = totGeometry
    costs.totScale = totScale
    costs.totPosition = totPosition
    costs.totDuplicate = totDuplicate

    # Computing the final SHED value:
    # shed = W.wGeometry *( totGeometry ) + W.wScale *( totScale )+ W.wPosition *( totPosition) + W.wDuplicate *( totDuplicate)
    shed =  0.4795*( totGeometry ) + 0.1258*( totScale )+ 0.0034*( totPosition) + 0.3914*( totDuplicate)
    print("shed : ",shed)
    #-----------------------------------------------------------------
    #                       Return
    #-----------------------------------------------------------------
    return [ shed, costs ]

######################################################################
#                           Main
######################################################################

######################################################################
#                           END
######################################################################

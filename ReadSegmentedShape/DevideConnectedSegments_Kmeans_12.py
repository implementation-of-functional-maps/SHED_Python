def _(VerticesColored, Faces):
    """ make segments from non connected and same colored segment Fs.
        It returns connected and same colored segments Segments.
    """
    from itertools import chain
    import sklearn.cluster as clu
    import numpy as np
    # devide the same colored Segments from ColoredFaces dict_ColoredFaces.
    
    FaceVerticesColored = []
    SegmentedVertices = []

    for face in Faces:
        summed_face_vertices_color = []
        summed_face_vertices_color.extend(face)
        summed_face_vertices_color.extend(VerticesColored[face[0]+1])

        # summed_face_vertices_color = [face[0], face[1], face[2], VerticesColored[face[0]+1][0], VerticesColored[face[0]+1][1], VerticesColored[face[0]+1][2], VerticesColored[face[1]+1][0], VerticesColored[face[1]+1][1], VerticesColored[face[1]+1][2], VerticesColored[face[2]+1][0], VerticesColored[face[2]+1][1], VerticesColored[face[2]+1][2]]
        FaceVerticesColored.append(summed_face_vertices_color)

    FaceVerticesColoredKmeansFittingData = FaceVerticesColored[3:]
    
    clustering_num = 10
    
    km = clu.KMeans(n_clusters=clustering_num)
    km.fit(FaceVerticesColoredKmeansFittingData)
    labels = km.labels_
    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)
    print("number of estimated clusters : %d" % n_clusters_)

    SegmentedFaces = []
    for color_label in labels_unique: # for 回さずに得たい。    
        Segment_temp = []
        SegmentedVertices_temp = []
        for i in range(len(labels)):
            if labels[i] == color_label:
                Segment_temp.append(Faces[i]) # VerticesColored[0:3])
                SegmentedVertices_temp.append(Faces[i])
                # SegmentedVertices_temp.append(' '.join([str(Faces[i][0]), str(Faces[i][1]), str(Faces[i][2])]))
        SegmentedFaces.append(Segment_temp)
        SegmentedVertices.append(SegmentedVertices_temp)
        
    nseg = len(SegmentedFaces)
    print("koko")
    return [nseg, SegmentedFaces, SegmentedVertices]
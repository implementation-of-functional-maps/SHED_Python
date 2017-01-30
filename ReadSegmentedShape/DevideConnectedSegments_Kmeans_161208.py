def _(dict_ColoredFaces):
    """ make segments from non connected and same colored segment Fs.
        It returns connected and same colored segments Segments.
    """
    from itertools import chain
    import sklearn.cluster as clu
    import numpy as np
    # devide the same colored Segments from ColoredFaces dict_ColoredFaces.
    Segments = []
    Fs=[]
    Fs_color=[]

    # Face read
    for face, color_face in dict_ColoredFaces.items(): # for 回さずに得たい。
        color = color_face.split(' ')
        face_arr = face.split(' ')
        Fs_color.append(np.array([int(color[0]), int(color[1]), int(color[2])]))
        Fs.append(np.array([int(face_arr[0]), int(face_arr[1]), int(face_arr[2])]))
    print(len(Fs_color))
    # K-means Clustering
    km = clu.KMeans(n_clusters=12)
    km.fit(Fs_color)
    labels = km.labels_
    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)


    for i in range(12):
        Segments.append([])

    for label_face, face in zip(labels, Fs):
        for i_color in range(len(labels_unique)):
            if label_face == labels_unique[i_color]:
                Segments[i_color].append(face)

    # print(len(Fs_ms))
    SegmentedVertices = dict_ColoredFaces.keys()
    # print(len(Fss))
    # print(count)
    nseg = len(Segments)
    
    return [nseg, Segments, SegmentedVertices]

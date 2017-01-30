def _(dict_ColoredFaces):
    """ make segments from non connected and same colored segment Fs.
        It returns connected and same colored segments Segments.
    """
    from itertools import chain
    import sklearn.cluster as clu
    import numpy as np
    # devide the same colored Segments from ColoredFaces dict_ColoredFaces.
    Segments = []
    Fss = []
    Colors = list(set(dict_ColoredFaces.values()))
    # print(Colors)
    for color_label in Colors:
        Fs_temp = []
        for face, color_face in dict_ColoredFaces.items(): # for 回さずに得たい。
            # print(face, color_face)
            if color_face == color_label:
                face_arr = face.split(' ')
                
                Fs_temp.append(np.array([int(face_arr[0]), int(face_arr[1]), int(face_arr[2])]))
        Fss.append(Fs_temp)
        # print("1")
    count = 0
    for Fs in Fss:
        print(len(Fs))
        km = clu.KMeans(n_clusters=12)
        km.fit(Fs)
        labels = km.labels_
        labels_unique = np.unique(labels)
        n_clusters_ = len(labels_unique)
        print("number of estimated clusters : %d" % n_clusters_)
        count += n_clusters_
        # print(labels)
        Fs_0 = []
        Fs_1 = []
        for label, face in zip(labels, Fs):
            if label == 1:
                Fs_1.append(face)
            elif label == 0:
                Fs_0.append(face)
        Segments.append(Fs_0)
        Segments.append(Fs_1)

    # print(len(Fs_ms))
    SegmentedVertices = dict_ColoredFaces.keys()
    # print(len(Fss))
    # print(count)
    nseg = len(Segments) 
    return [nseg, Segments, SegmentedVertices]

def _(dict_ColoredFaces):
    """ make segments from non connected and same colored segment Fs.
        It returns connected and same colored segments Segments.
    """
    from itertools import chain
    # devide the same colored Segments from ColoredFaces dict_ColoredFaces.
    Segments = []
    Fss = []
    Colors = list(set(dict_ColoredFaces.values()))
    print(Colors)
    for color_label in Colors:
        Fs_temp = []
        for face, color_face in dict_ColoredFaces.items(): # for 回さずに得たい。
            # print(face, color_face)
            if color_face == color_label:
                face_arr = face.split(' ')
                
                Fs_temp.append(face_arr)
        Fss.append(Fs_temp)
        print("1")
        
    SegmentedVertices = dict_ColoredFaces.keys()
    print(len(Fss))
    count = 0
    for Fs in Fss:
        segment = []
        while  len(Fs) != 0:
            
            # print(len(Fs))
            F1 = Fs[0]
            # print(Fs[0], Fs[1])
            seg_faces = [F1]
            temp = [F1]
            del Fs[0]
            # print(Fs[0])
            connected_vertices = set(F1)
            # connected_vertices = set()
            # print(connected_vertices)
            while len(temp) != 0:
                temp = []
                for F_i in Fs:
                    # print(connected_vertices, set(F_i))
                    # print(F_i)
                    # print((set(F_i) & connected_vertices))
                    if len(connected_vertices.intersection(set(F_i))) != 0: # connected_vertices と F_i が共通部分をもつ.
                        # print('koko')
                        # print((set(F_i) & connected_vertices))
                        temp.append(F_i)
                        
                        seg_faces.append(F_i)
                        
                        # print(len(Fs))
                        connected_vertices = connected_vertices.union(set(F_i))
                        # print(len(connected_vertices), len(F_i), len(Fs))#, connected_vertices, F_i)
                        Fs.remove(F_i) # delete F_i from Fs
                        # print("gogo")
                    # print(len(connected_vertices), len(F_i), connected_vertices, F_i)
                # print(temp)
            #, connected_vertices, F_i)
            if len(seg_faces) > 7000:
                count += 1
                print(len(segment), len(connected_vertices), len(F_i), len(Fs), count)
            else:
                segment.extend(seg_faces)
        count += 1
        Segments.append(segment)
            
    return [Colors, Segments, SegmentedVertices]

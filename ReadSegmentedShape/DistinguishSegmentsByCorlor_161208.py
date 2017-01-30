def _(Faces, dict_ColoredVertices):
    """ dict_ColoredVertices which is a dict { [vx, vy, vz] : Color } label Faces by the same Color.
        dict_ColoredVertices = { [vx, vy, vz] : Color }
        Faces = [[v11, v12, v13], [v21, v22, v23],..., [vn1, vn2, vn3]]
        It returns ColoredFaces.

    """
    # make dict_color
    # print(dict_ColoredVertices.values())
    Colors = list(set(dict_ColoredVertices.values()))
    dict_color = {}
    for i in range(len(Colors)):
        dict_color.update( {Colors[i] : i} )
        
    # make dict_IndexedVertices
    dict_IndexedVertices = {}
    count = 0
    for color in dict_ColoredVertices.values():
        dict_IndexedVertices.update( {count :  color} )
        count += 1
    # print(dict_IndexedVertices)
    # coloring Faces
    dict_ColoredFaces = {}
    for face in Faces:
        # print(face)
        color_vertex_1 = dict_IndexedVertices[face[0]]
        color_vertex_2 = dict_IndexedVertices[face[1]]
        color_vertex_3 = dict_IndexedVertices[face[2]]
        face = " ".join([str(face[0]), str(face[1]), str(face[2])])
        if color_vertex_1 == color_vertex_2 and color_vertex_3 == color_vertex_1:
            dict_ColoredFaces.update( {face : color_vertex_1} )
        elif color_vertex_1 != color_vertex_2 and color_vertex_3 == color_vertex_1:
            dict_ColoredFaces.update( {face : color_vertex_2} )
        elif color_vertex_1 == color_vertex_2 and color_vertex_3 != color_vertex_1:
            dict_ColoredFaces.update( {face : color_vertex_3} )
        else:
            dict_ColoredFaces.update( {face : color_vertex_1} )
            
    return dict_ColoredFaces

# あとは以下の二つを COFF から作成するコードを書いて終了
# dict_ColoredVertices = { [vx, vy, vz] : Color }
# Faces = [[v11, v12, v13], [v21, v22, v23],..., [vn1, vn2, vn3]]
# → mesh_read_off.py を少し改変する

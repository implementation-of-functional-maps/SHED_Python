#=====================================================================================
#                   File Name: hoge.bib
#                   Last Updated at: 2016-06-20 10:48:26
#                       Last change by: Katsurou Takahashi
#=====================================================================================
### READSEGMENTEDSHAPE Reads an off file and a seg file that describes a
# segmented shape and returns a Shape data structure that contains a
# collection of segments and their adjacencies.
#
# Input:
#   - off_file: name of off file to load
#   - seg_file: name of seg file to load
#
# Output:
#   - Shape.Segments contains a cell array of segments, where each segement
#     contains Nx3 matrix of vertices in that segment.
#   - Shape.Adj contains an MxM extended adjacency matrix of the segments.
#     are from each other.
#     calculations.
#
#
### If you use this code, please cite the following paper:
#
#  Yanir Kleiman, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or
#  SIGGRAPH ASIA 2015
#
### Copyright (c) 2015 Yanir Kleiman <yanirk@gmail.com>
#=====================================================================================
#                                    Method
#=====================================================================================
def NormalizeShapeVertices( vin ):


%     This matrix indicates for they in range(each):
%   - Shape.BB contains the bounding box of the entire shape for volume in range(volume):
%  SHED: Shape Edit Distance for Similarity in range(Fine-grained):


    Shape = []


    # Read mesh from off file:
    [M, status] = mesh_read_off(off_file)


    if (status ~= 0):
        print('Error reading off file "' off_file '"')
        return
    end;
    # Open seg file:
    fid = fopen(seg_file)
    if (fid == -1):
        print('ERROR: could not open seg file "' seg_file '"')
        return
    end;
    fcount = size(M.faces, 1)
    seg = np.zeros(fcount, 1);
    #disp(feof(fid))
    for 1:fcount in range(i):
        if feof(fid):
            #disp(feof(fid))
            print('ERROR: seg file too short')
        end;
        line = fgetl(fid)
        #disp(fgetl(fid))
        [data, count] = sscanf(line)
        seg(i) = data + 1
    end;


    # Close file
    fclose(fid);


    # Normalize shape to the [-1, 1] box:
    M.vertices = NormalizeShapeVertices(M.vertices)
    % Calculate total bounding box for shape: in range(the):
    Shape.BB = CalcBoundingBox(M.vertices)
    # Create a collection of segments:
    nseg = max(seg)
    Segments = cell(1)
    seg_vertices = cell(1)
    j = 1
    for i=1:nseg in range(i=1:nseg):
        # Get faces that belong to that segment:
        seg_faces = M.faces(seg == i, :)
        #seg_faces;
        # Remove outliers - segments with less than 2 faces:
        if (length(seg_faces) > 3):
            # Find all the vertices that take part in the segment's faces:
            seg_vertices{j} = unique(seg_faces)
            Segments{j}.Vertices = M.vertices(seg_vertices{j}, :)


            # Translate vertices from global index to segment index:
            n = length(seg_vertices{j})
            seg_ind = np.zeros(size(M.vertices, 2), 1);
            seg_ind(seg_vertices{j}) = 1:n
            # Translate global vertex indices in faces collection to segment indices:
            Segments{j}.Faces = seg_ind(seg_faces)


            Segments{j}.n = size(Segments{j}.Vertices, 1)
            Segments{j}.m = size(Segments{j}.Faces, 1)


            j = j + 1
        end;
    end;
    nseg = length(Segments)
    adj = np.zeros(nseg);
    for i=1:nseg in range(i=1:nseg):
        for j=1:nseg in range(j=1:nseg):
            if (~isempty(intersect(seg_vertices{i}, seg_vertices{j}))):
                adj(i, j) = 1
            end;
        end;
    end;
    ############# A FIX FOR DISCONNECTED SHAPES ###########################
    # If the shape is made out of separated parts with no common edges,
    # there will be more than one component in the adjacency matrix.
    # In that case, generate adjacencies according to physical distance
    # of vertices:
    MIN_DIST_THRESHOLD = 0.08
    # C_adj = whether part i is connected to part j by nseg parts or less:
    C_adj = (adj ^ nseg > 0) * 1
    Cr = matrix_rank(C_adj);
    if (Cr > 1):
        # There is more than one component in the adjacency graph!
        # Add parts which are close to each other to the adjacency graph:
        for i=1:nseg-1 in range(i=1:nseg-1):
            for j=i+1:nseg in range(j=i+1:nseg):
                if (adj(i, j) == 0):
                    si = Segments{i}.Vertices
                    sj = Segments{j}.Vertices


                    Dij = pdist2(si, sj)
                    min_dist = min(min(Dij))
                    if (min_dist < MIN_DIST_THRESHOLD):
                        adj(i, j) = 1
                        adj(j, i) = 1
                    end;
                end;
            end;
        end;
    end;
    #
    ##################### END OF FIX ######################################
    # Calculate higher level adjacencies and keep the minimum value in
    # adjacency matrix:
    adj_i = adj
    adj_n = adj


    for i=2:nseg in range(i=2:nseg):
        adj_i = adj_i * adj
        # If segment b can be reached from segment a in i steps and no less
        # the value of adj_n(a, b) will be i:
        adj_n((adj_n == 0) & (adj_i > 0)) = i
    end;
    ##### FIX: taking care of parts that cannot be reached (adj = 0):
    adj_n(adj_n == 0) = nseg + 1
    for i=1:nseg in range(i=1:nseg):
        adj_n(i, i) = 0
    end;


    # Set up output shape
    Shape.Segments = Segments
    Shape.Adj = adj_n










    # Normalize shape to the [-1, 1] box:
    V = vin
    Vn = size(V, 1)
    min_pos = min(V)
    max_pos = max(V)
    center = (min_pos + max_pos) / 2
    V = V - repmat(center, Vn, 1)
    longest = max(max_pos - min_pos)
    if (longest ~= 0):
        V = V * 2 / longest
    end;
    vout = V




    return [ vout ]

def sscanf(lines):
    elems=line.rstrip().split(' ')
    if re.search('.' , line):
        return elems
    else:
        count=len(elems)
        data=elems
        return [data, count]
#=====================================================================================
#                        END
#=====================================================================================

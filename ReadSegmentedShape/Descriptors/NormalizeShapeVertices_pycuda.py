
def _(vin):
        import json
        import numpy as np
        import pdb
        import pycuda.gpuarray as gpuarray
        import pycuda.driver as cuda
        import pycuda.autoinit


        # Normalize shape to the [-1, 1] box:
        V = gpuarray.to_gpu(vin)
        min_pos = gpuarray.to_gpu(np.array([min(V[:,0]), min(V[:,1]), min(V[:,2])]).astype(numpy.float32)))
        max_pos = gpuarray.to_gpu(np.array([max(V[:,0]), max(V[:,1]), max(V[:,2])]).astype(numpy.float32)))
        center = (min_pos + max_pos) / 2
     
        import numpy.matlib
        Vn = len(V)
        a0 = gpuarray.to_gpu(np.array(0).astype(numpy.float32))
        Vn_zeros = gpuarray.to_gpu(np.array(np.matlib.repmat(a0, Vn, 3)))
        Vn_center = Vn_zeros + center
        
        V = V - Vn_center 
        longest = max_pos - min_pos
        
        if  longest[0] != 0.0 and longest[1] != 0.0 and longest[2] != 0.0:
            V = V * 2 / longest
            
        vout = (V).get()
     
        #-----------------------------------------------------------------
        #                       Return
        #-----------------------------------------------------------------
        return  vout 

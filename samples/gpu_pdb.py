# import pycuda.gpuarray as gpuarray
# import pycuda.driver as cuda
# import pycuda.autoinit

import json
import numpy as np
import pdb
f = open("1.vertices_json") 
lines = f.read()
array = np.array(json.loads(lines))
f.close()
points = array

def func_with_error():
    local_var='hidden'
    raise Exception()

# vin = np.array([[1,2,3],[4,5,6],[7,8,9]])
vin = np.array(array)
# Normalize shape to the [-1, 1] box:
Vin = np.array(vin)
V = np.array(Vin[:,0])
# V = V.T

print(array)
print("V")
print(V)

min_pos = min(V)
max_pos = max(V)
print("min: "+ str(min_pos) +",max: "+ str(max_pos))
center = ( min_pos + max_pos) / 2

import numpy.matlib
Vn = len(V)
# Vm = len(Vn[0])
a0 = np.array(0)
# Vn_zeros = np.matlib.repmat(a0, Vn, Vm)
Vn_zeros = np.matlib.repmat(a0, 1, Vn)
Vn_center = Vn_zeros + center
print("Vn_center")
print(Vn_center)

V = V -  Vn_center # ここが怪しい.
print("V")
print(np.array(V))
print("koko")
longest = max_pos - min_pos
print("longest: "+ str(longest))

if (longest != 0) or (longest != 0.0) :
    V = V * 2 / longest
    print("kokokoko")
    print(V)
    vout = V

try:
    for i in range(10):
        a = a+a
        print(a)
        if i == 1:
            pdb.set_trace()
        elif i == 4:
            func_with_error()

except:
    import sys
    traceback = sys.exc_info()[2]
    pdb.post_mortem(traceback)

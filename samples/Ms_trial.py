def _():
    import sys,os # relative import 
    sys.path.append(os.pardir) # relative import
    sys.path.append("/Users/admin/Dropbox/SHED_python/auto/my_modules")
    sys.path.append("/Users/admin/Dropbox/SHED_python/auto")
    import matlab_python.supertuple as supertuple

    X = [1,2,3]
    F = [111,222,333]

    M = supertuple.superTuple('M', 'vertices', 'faces')
    Ms = M(X,F)
    print(Ms.vertices)
    return Ms

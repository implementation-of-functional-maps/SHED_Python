import pdb
def func_with_error():
    local_var='hidden'
    raise Exception()

try:
    for i in range(10):
        print(i)
        if i == 1:
            pdb.set_trace()
        elif i == 4:
            func_with_error()

except:
    import sys
    traceback = sys.exc_info()[2]
    pdb.post_mortem(traceback)

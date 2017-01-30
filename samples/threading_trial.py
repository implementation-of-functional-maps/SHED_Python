import threading

def worker():
    """thread worker function"""
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()



import numpy as np
n = 1000
server = ["A", "B", "C", "D", "E"]
work_proceeding = np.zeros((n, n))

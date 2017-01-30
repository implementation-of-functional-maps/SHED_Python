# -*- coding: utf-8 -*-
import time
import multiprocessing

q12 = multiprocessing.Queue()
q23 = multiprocessing.Queue()

def Calc1(number):
    time.sleep(1)
    q12.put(number)

def Calc2(number):
    data=q12.get()
    time.sleep(2)
    q23.put(data)

def Calc3(number):
    data=q23.get()
    time.sleep(1)
    print("result"+str(data))


if __name__ == '__main__':
    start = time.time() # 時間計測開始 tic
    for i in range(10):
        p1 = multiprocessing.Process(target=Calc1, args=(i,))
        p1.start()
        p2 = multiprocessing.Process(target=Calc2, args=(1,))
        p2.start()
        p3 = multiprocessing.Process(target=Calc3, args=(1,))
        p3.start()

    p1.join()
    p2.join()
    p3.join()
    end = time.time() # 時間計測終了. toc
    print('%.3f' %(end-start))

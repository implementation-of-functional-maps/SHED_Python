import cProfile as profile
def bench1(list1, list2):
    list1 += list2
    return list1

def bench2(list1, list2):
    list3 = list1 + list2
    return list3

def loop(bench):
    for i in range(10000):
        bench([1,] * i, [2,] * i)

profile.run('loop(bench1)')

import random


def Random_array():
    list1 = []
    for c in range(0, 10):
        d = random.randint(0, 100)
        list1.append(d)
    list1.sort()
    print(list1)
    return list1


# y最小的数
def small(b, list1):
    list2 = list1.copy()
    for f in range(int(b) - 1):
        list2.remove(min(list2))
        # print(list2)
    print(min(list2))


# 最大的数
def big(a, list1):
    list2 = list1.copy()
    for e in range(int(a) - 1):
        list2.remove(max(list2))
        # print(list2)
    ZD = max(list2)
    print(ZD)
    return ZD

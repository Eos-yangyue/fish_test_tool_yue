#  -*- coding: utf-8 -*-

# 输出所有五位数的五进制
"""
sum = 0
for a in range(1, 5):
    for b in range(0, 5):
        for c in range(0, 5):
            for d in range(0, 5):
                for e in range(0, 5):
                    print("%d%d%d%d%d" % (a, b, c, d, e))
                    sum = sum+1
print("五位数的五进制共有：", sum)
"""

"""
for num1 in range(1000, 10000):
    num2 = str(num1)
    for a in range(1):
        if num2[0] == num2[1] and num2[0] != num2[2] and num2[0] != num2[3]:
            num3 = int(num2)
            for i in range(2, num3):
                if num3 % i == 0:
                    break
            else:
                print("质数：", num3)
"""
"""
                if num2[0] != num2[1] and num2[0] == num2[2] and num2[0] != num2[3]:
                if num2[0] != num2[1] and num2[0] != num2[2] and num2[0] == num2[3]:
"""

"""
# 输出所有4位数中，有且只有两位相同（如1134，2557）的数字中，所有的质数
for num1 in range(1000, 10000):
    num2 = str(num1)
    x = 0
    for a in range(4):
        for b in range(a+1, 4):
            if num2[a] == num2[b]:
                x = x+1
    if x == 1:
        # print(num2)
        num3 = int(num2)
        for i in range(2, num3):
            if num3 % i == 0:
                break
        if i == num3-1:
            print("质数：", num3)
"""

dict1 = {input("请输入字符串：")}






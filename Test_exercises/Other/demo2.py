'''#  -*- coding: utf-8 -*-

# 打印输出螺旋矩阵

"""
def gen_matrix(n):
    # 用二维数组来代表矩阵
    matrix = [[0 for col in range(n)] for row in range(n)]
    return matrix


def get_rota_matrix(n):
    mat = gen_matrix(n)  # 初始矩阵，所有元素都为0
    x = y = 0
    total = mat[x][y] = 1 # 将数组第一个元素设为1，即mat[0][0] = 1
    while total != n * n:
        while y + 1 < n and not mat[x][y + 1]: # 从左至右
            y += 1
            total += 1
            mat[x][y] = total
        while x + 1 < n and not mat[x + 1][y]: # 从上之下
            x += 1
            total += 1
            mat[x][y] = total
        while y - 1 >= 0 and not mat[x][y - 1]: # 从右至左
            y -= 1
            total += 1
            mat[x][y] = total
        while x - 1 >= 0 and not mat[x - 1][y]: # 从下至上
            x -= 1
            total += 1
            mat[x][y] = total
    return mat


if __name__ == '__main__':
    n = int(input("请输入矩形数组的大小:"))
    matrix = get_rota_matrix(n)
    # print(matrix)
    for i in range(n):
        for j in range(n):
            print('%4d' % matrix[i][j], end=" ")
        print()
        """
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
import random
from shutil import move

from click._compat import raw_input

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

# 输出所有4位数中，有且只有两位相同（如1134，2557）的数字中，所有的质数
"""
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

# 输入一串字符串，统计其中各个字符出现的个数（使用字典记录）
"""
# 输入字符串，定义给a
a = input("输入内容：")
# 定义一个空字典，用来存放数据
dict1 = {}
# i for循环的条件为a的长度
for i in a:
    # 将a赋值给字典中的i键，并且计数
    dict1[i] = a.count(i)

print(dict1)
"""

# 建立一个电话号码薄，增加、删除、查询、修改单独功能
"""
# 增加
phone = {"h": "111", "j": "222"}
phone2 = {"111": "h", "222": "j"}

key = input("请输入增加的姓名：")
value = input("请输入增加的电话:")
phone[key] = value
phone2[value] = [key]
print(phone)

# 删除
del1 = input("「删除」请输入玩家姓名：")
del phone[del1]
print("已删除")
print(phone)

# 通过人名查电话
check = input("「查询电话」请输入玩家姓名：")
print(check, "的电话为：", phone[check])

# 通过电话查人名
check2 = input("「查询姓名」请输入玩家电话：")
print(check2, "的玩家姓名为：", phone2[check2])

# 通过姓名修改电话
print(phone)
update_name = input("请输入需要修改电话的姓名：")
update_phone = input("请输入修改的电话：")
phone[update_name] = update_phone
print(phone)

# 通过电话修改姓名
print(phone2)
update_phone = input("请输入需要修改姓名的电话：")
update_name = input("请输入修改的姓名：")
phone2[update_phone] = update_name
print(phone2)

"""
# 建立一个电话号码薄，可以增加和删除内容，可以通过人名查电话，电话查人名
"""
phone = {"a": "111", "b": "222", "c": "333"}
phone2 = {"111": "a", "222": "b", "333": "c"}
while True:
    a = input("请输入想要执行的操作序号：\n1、增加姓名和电话\n2、删除姓名和电话\n3、输入姓名查询电话\n4、输入电话查询姓名\n")
    if int(a) == 1:
        print("电话簿：", phone)
        key = input("请输入增加的姓名：")
        value = input("请输入增加的电话:")
        phone[key] = value
        phone2[value] = [key]
        print(phone)
    elif int(a) == 2:
        print("电话簿：", phone)
        del1 = input("「删除」请输入玩家姓名：")
        del phone2[phone[del1]]
        del phone[del1]
        print("已删除")
        print(phone)
    elif int(a) == 3:
        print("电话簿：", phone)
        check = input("「查询电话」请输入玩家姓名：")
        print(check, "的电话为：", phone[check])
    elif int(a) == 4:
        print("电话簿：", phone2)
        check2 = input("「查询姓名」请输入玩家电话：")
        print(check2, "的玩家姓名为：", phone2[check2])
    else:
        print("亲，该操作不存在，请输入正确序号哦~")
"""
# 建立一个可以存储学生信息的程序，可以添加或修改某个人的基本信息，可以通过姓名查询学生的个人信息。信息暂时包括姓名、性别、年龄、班级
"""
student = {}
information = {'name': "a", 'sex': "b", 'age': "c", 'ban': "d"}
# 修改
name1 = input("请输入学生姓名：")
sex1 = input("请输入学生性别：")
age1 = input("请输入学生年龄：")
ban1 = input("请输入学生班级：")
information['name'] = name1
information['sex'] = sex1
information['age'] = age1
information['ban'] = ban1
print(information)
"""
"""
# 增加
student = {'姓名': "", '性别': "", '年龄': "", '班级': ""}
information = {'姓名': "", '性别': "", '年龄': "", '班级': ""}
while True:
    name = input("请输入学生姓名：")
    sex = input("请输入学生性别：")
    age = input("请输入学生年龄：")
    ban = input("请输入学生班级：")
    information['姓名'] = name
    information['性别'] = sex
    information['年龄'] = age
    information['班级'] = ban
    student['信息'] = information
    print(student['信息'])
"""

"""
# 增加
name = input("请输入学生姓名：")
sex = input("请输入学生性别：")
age = input("请输入学生年龄：")
ban = input("请输入学生班级：")
student = {}
information = {'性别': sex, '年龄': age, '班级': ban}
student[name] = information
print(student)

# 修改
print("当前学生信息：", student)
up = input("请输入想要修改的学生名称：")
print("当前该学生的信息为：", student[up])
sex1 = input("请输入修改的学生性别：")
age1 = input("请输入修改的学生年龄：")
ban1 = input("请输入修改的学生班级：")
information['性别'] = sex1
information['年龄'] = age1
information['班级'] = ban1
print('修改后该学生的信息为：', student)
"""
# 建立一个可以存储学生信息的程序，可以添加或修改某个人的基本信息，可以通过姓名查询学生的个人信息。信息暂时包括姓名、性别、年龄、班级
"""
student = {}
while True:
    a = input("请输入想要执行的操作序号\n 1、增加学生信息 \n 2、修改学生信息")
    if int(a) == 1:
        name = input("请输入学生姓名：")
        sex = input("请输入学生性别：")
        age = input("请输入学生年龄：")
        ban = input("请输入学生班级：")
        information = {'性别': sex, '年龄': age, '班级': ban}
        student[name] = information
        print("当前学生系统中信息为：", student)
    elif int(a) == 2:
        print("当前学生信息：", student)
        up = input("请输入想要修改的学生名称：")
        print("当前该学生的信息为：", student[up])
        sex1 = input("请输入修改的学生性别：")
        age1 = input("请输入修改的学生年龄：")
        ban1 = input("请输入修改的学生班级：")
        information['性别'] = sex1
        information['年龄'] = age1
        information['班级'] = ban1
        print('修改后该学生的信息为：', student)
    elif int(a) == 0:
        break
    else:
        print("请输入正确序号哦~")
"""

# 递归汉诺塔
"""
# n=盘子数量，abc三根柱子
def move(n, a, b, c):
    # 判断：如果只有一个盘子，则直接移动到c柱子上
    if n == 1:
        print(a, '-->', c)
    else:
        # 一共有5个，把最下面的留下，把4个移动到b柱子
        move(n - 1, a, c, b)
        # 把最下面的移动到C柱子
        move(1, a, b, c)
        move(n - 1, b, a, c)


a = input('请输入A柱盘子的个数：')
num = int(a)
print('把', num, '个盘子全部移到C柱子的顺序为：')
move(num, '柱子1', '柱子2', '柱子3')
"""
# 输入两个数xy，产生10个随机数存入列表，随后求出列表中第x大的数和第y小的数
"""
import random
a = input("请输入第x大的数字：")
b = input("请输入第y小的数字：")
list1 = []

for c in range(0, 10):
    d = random.randint(0, 100)
    list1.append(d)

# y最小的数
def small(b):
    list2 = list1.copy()
    for f in range(int(b)):
        list2.remove(min(list2))
        print(list2)
    print(min(list2))

def big(a):
    list2 = list1.copy()
    for e in range(int(a)):
        list2.remove(max(list2))
        print(list2)
    print(max(list2))

big(a)
small(b)
"""
# 输入两个二维数组，检查二者中有没有相同的一维数组，如果有，就把第一个数组，此一维数组前面的部分与第二个数组，此一维数组后面的部分，拼接成一个新数组
"""
# 切片 比较 拼接
list1 = [[1, 2, 3], [3, 4, 5], [9, 8, 2]]
list2 = [[2, 9, 8], [8, 1, 3], [2, 3, 1]]

def C1():
    # 双层循环，自增下标赋值
    for b in list1:
        x = b[0]
        y = b[1]
        z = b[2]
        for a in list2:
            list3 = B1(a, x, y, z)
            if list3 != None:
                print(list3)

# B和A可以合并
def B1(list, x, y, z):
    x1 = A1(list, x)
    x2 = A1(list, y)
    x3 = A1(list, z)
    if x1 != None and x2 != None and x3 != None:
        y1 = [x1, x2, x3]
        # print(y1)
        return y1

# 一维数组顺序不同，也能比较
def A1(list, x):
    for i in list:
        if i != x:
            continue
        else:
            print(i)
            return i
            break


if __name__ == '__main__':
    C1()
"""

# 将二维数组拆分成单个的一维数组
# 将一维数组去比较
# 把相同的一维数组前后两个数组相加

# 比较一维数组的函数
"""
def C1(list1, list2):
    x = 0

    if len(list1) != len(list2):
        return False
    for b in range(0, len(list1)):
        for c in range(0, len(list2)):
            if list1[b] == list2[c]:
                x = x + 1
            else:
                continue
    if x == len(list2):
        return True
    else:
        return False

if __name__ == '__main__':
    list1 = [[1, 2, 5, 8, 3, 7], [2, 8, 5]]
    list2 = [[1, 2, 5, 8, 3, 7], [2, 3, 5]]
    print(C1(list1, list2))
"""


def C1(list1, list2):

    x = 0
    if len(list1) != len(list2):
        return False
    else:
        list3 = list1.copy()
        list3.sort()
        list4 = list2.copy()
        list4.sort()
    for b in range(0, len(list3)):
        if list3[b] == list4[b]:
            x = x + 1
        else:
            break

    if x == len(list4):
        return True
    else:
        return False


# 将二维数组拆分为一维数组

def B1(list1, list2):
    for b in range(0, len(list1)):
        for c in range(0, len(list2)):
            A = list1[b]
            B = list2[c]
            D = C1(A, B)
            if D == True:
                print(c)
                print(list1[:b]+list2[c:])
                print(A, B, D, "一维数组相同")
            # print(A, B, D)


if __name__ == '__main__':
    list1 = [[2, 5, 3, 6], [2, 5, 3, 8, 5], [4, 39, 5, 3], [2, 3, 4, 5, 6]]
    list2 = [[2, 5, 3, 11, 16, 17], [2, 3, 5], [4, 39, 5, 3], [2, 3, 4, 5, 6, 8]]
    print(B1(list1, list2))

    # append 135 1345 remove 4 比较两个是否相等
# 数组切片【1:5】取这个数组中第一位~第五位的数值
# 数值越界
import Test_exercises.test_package.test1

from Test_exercises.test_package.test1 import *'''



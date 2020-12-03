# 输入两个数xy，产生10个随机数存入列表，随后求出列表中第x大的数和第y小的数
from test_package import function_list
from test_package import function_spiral
import random

if __name__ == '__main__':
    a = input("请输入第x大的数字：")
    b = input("请输入第y小的数字：")

    c = function_list.Random_array()
    # 调用small函数，将最小数b和list1传入
    function_list.small(b, c)
    # 调用big函数，将最大数a和list1传入
    d = function_list.big(a, c)
    # 最大的数当做螺旋矩阵的边长
    matrix = function_spiral.get_rota_matrix(d)

    # print(matrix)
    for i in range(d):
        for j in range(d):
            print('%4d' % matrix[i][j], end=" ")
        print()
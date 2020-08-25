#  -*- coding: utf-8 -*-
# 打印输出螺旋矩阵


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
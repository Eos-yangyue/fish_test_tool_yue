def gen_matrix(d):
    # 用二维数组来代表矩阵
    hh = int(d)
    matrix = [[0 for col in range(hh)] for row in range(hh)]
    return matrix


def get_rota_matrix(d):
    mat = gen_matrix(d)  # 初始矩阵，所有元素都为0
    x = y = 0
    total = mat[x][y] = 1 # 将数组第一个元素设为1，即mat[0][0] = 1
    while total != d * d:
        while y + 1 < d and not mat[x][y + 1]: # 从左至右
            y += 1
            total += 1
            mat[x][y] = total
        while x + 1 < d and not mat[x + 1][y]: # 从上之下
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
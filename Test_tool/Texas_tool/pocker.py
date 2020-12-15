"""
修改德州牌型工具
"""

# 一开始的5个元组代表5张公牌，前一个数字取0，1，2，3代表4种花色(0=方片 1=梅花 2=红桃 3=黑桃)
# 后续数字代表牌上数字，2-13为2-K，14为A
a = (1, 14)
b = (1, 10)
c = (1, 7)
d = (1, 8)
e = (1, 13)
# 这两个元组同理，代表两张手牌
f = (1, 12)
g = (2, 7)
# 组合为一个list
cardList = [a, b, c, d, e, f, g]
# 从大到小存储牌型名称
kindlist = ["皇家", "同花顺", "四条", "葫芦", "同花", "顺子", "三条", "两对", "一对", "高牌"]
# 记录输出次数
global times
times = 0


# 格式化输出函数，匹配客户端接口牌型信息模板
def makeRes(cardList1):
    global times
    times += 1
    res = "{\"cards\":\""
    for each in cardList1:
        res += str(each[0])
        res += ","
        res += str(each[1])
        res += "|"
    res = res[0:len(res) - 1]
    res += "\"}"
    print(times, res, end="    ")


# 全排列函数，使用递归产生an中第m到第n个数的全排列，并使用函数产生输出
def perm(an, m, n):
    if m == n:
        makeRes(an)
    else:
        for i in range(m, n):
            temp = an[m]
            an[m] = an[i]
            an[i] = temp
            perm(an, m + 1, n)
            temp = an[m]
            an[m] = an[i]
            an[i] = temp


# 全组合函数，使用多重循环产生手牌与公牌的21种组合
# 同时调用判断牌型函数产生发3张、4张、5张公牌时的牌型
def coun(bn):
    cn = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    for i in range(0, 7):
        for j in range(i + 1, 7):
            seq = 0
            for k in range(7):
                if k == i:
                    cn[5] = bn[k]
                elif k == j:
                    cn[6] = bn[k]
                else:
                    cn[seq] = bn[k]
                    seq += 1
            makeRes(cn)
            a = justic75(cn)
            print(kindlist[a], end="    ")
            b = justic76(cn)
            print(kindlist[b], end="    ")
            justic2(cn)


# 判断5张牌牌型
def justic(dn5):
    # 牌型数组，对应上述牌型名称数组，值为1即满足改种牌型，为0则不满足
    # 最高位的1对应牌型即显示的最大牌型
    shape = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    # 计算对数总和
    couples = 0
    for i in range(0, 5):
        for j in range(i + 1, 5):
            if dn5[i][1] == dn5[j][1]:
                couples += 1
    # 总共1对即满足一对牌型
    if (couples == 1): shape[8] = 1
    # 总共2对即满足两对牌型
    if (couples == 2): shape[7] = 1
    # 总共3对即满足三条牌型
    if (couples == 3): shape[6] = 1
    # 总共4对即满足葫芦牌型
    if (couples == 4): shape[3] = 1
    # 总共6对即满足四条牌型
    if (couples == 6): shape[2] = 1
    # 若排序后数字连续即顺子
    num = [dn5[0][1], dn5[1][1], dn5[2][1], dn5[3][1], dn5[4][1]]
    num.sort()
    if num[1] == num[0] + 1 and num[2] == num[0] + 2 and num[3] == num[0] + 3 and num[4] == num[0] + 4:
        shape[5] = 1
    # 若花色相同即同花
    if dn5[0][0] == dn5[1][0] and dn5[0][0] == dn5[2][0] and dn5[0][0] == dn5[3][0] and dn5[0][0] == dn5[4][0]:
        shape[4] = 1
    # 即是同花又是顺子即同花顺
    if shape[4] == 1 and shape[5] == 1:
        shape[1] = 1
    # 同花顺最高牌为A即皇家同花顺
    if shape[1] == 1 and num[4] == 14:
        shape[0] = 1
    resu = 0
    # 最高位的下标为牌型结果编号
    for resu in range(10):
        if shape[resu] == 1:
            break
    # print(kindlist[resu])
    return resu


# 判断六张牌牌型，即分别判断6种5张牌组合
def justic1(dn6):
    realR = 9
    for i in range(6):
        dn6c = dn6.copy()
        cont = dn6[i]
        dn6c.remove(cont)
        re = justic(dn6c)
        if re < realR:
            realR = re
    # print(kindlist[realR])
    return realR


# 判断七张牌牌型，即分别判断21种5张牌组合
def justic2(dn7):
    realR = 9
    for i in range(7):
        for j in range(i + 1, 7):
            dn7c = dn7.copy()
            count1 = dn7[i]
            count2 = dn7[j]
            dn7c.remove(count1)
            dn7c.remove(count2)
            re = justic(dn7c)
            if re < realR:
                realR = re
    print(kindlist[realR])


# 判断七张牌发4张公牌（共6张牌）时牌型
def justic76(dn7):
    dn6 = [dn7[0], dn7[1], dn7[2], dn7[3], dn7[5], dn7[6]]
    return justic1(dn6)


# 判断七张牌发3张公牌（共5张牌）时牌型
def justic75(dn7):
    dn5 = [dn7[0], dn7[1], dn7[2], dn7[5], dn7[6]]
    return justic(dn5)


# 调用一次全组合，形成结果
coun(cardList)

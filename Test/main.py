# ！python3
# 九九乘法表：第一种
"""
for i in range(1, 10):
    for j in range(1, i+1):
        if i == j:
            print("%d*%d=%d" % (j, i, i*j), end="\n")
        else:
            print("%d*%d=%d" % (j, i, i * j), end="\t")
"""
# 九九乘法表：第二种


"""
# range=长度，（1, 10）只取前面的数，最后10不取，也就是123456789
for i in range(1, 10):
    for j in range(1, i+1):
        # %s=占位符，end=' '=空格
        print('%s*%s=%s' % (i, j, i*j), end=' ')
    # 换行
    print()
"""
# sum函数
"""
# 定义一个名字为sum的函数，声明两个参数num1和num2
# 函数的第一句话进行函数说明
# 最终return结束函数，返回两数之和
# 在外部调用sum函数，并赋值给num1和num2，最后输出两数之和
def sum(num1, num2):
    "这是一个sum函数"
    return num1 + num2


print(sum(1,2))
"""
# 数据类型检查函数
"""
def sum(num1, num2):
    if not(isinstance (num1, (int, float)) and isinstance (num2, (int, float))):
        raise TypeError('参数类型错误，不是int或float')
    return num1+num2

# 符合int和float的则会调用num1+num2
print(sum(1,2))
# 不符合int和float的则会报错
print(sum('环境','就'))
"""
# 修改字典中的值
"""
# 创建一个字典
name={'ming': '哈哈哈', 'xng':'bb'}
# 输出ming的值
print(name['ming'])
# 修改ming的值
name['ming']='jjj'
print(name['ming'])
"""


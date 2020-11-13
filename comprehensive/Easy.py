import random

class zoo(object):
    def mao(slef):
        print("猫吃完饭啦~")
        a = 1
        b = 2
        c = random.randint(a, b)
        if c == 1:
            print("猫吃完饭要睡觉啦~")
        else:
            print("喵~")
        return

    def gou(slef):
        print("狗吃完饭啦~")
        a = 1
        b = 2
        c = random.randint(a, b)
        if c == 1:
            print("狗吃完饭要睡觉啦~")
        else:
            print("旺旺~")
        return

    def niu(slef):
        print("牛吃完饭啦~")
        a = 1
        b = 2
        c = random.randint(a, b)
        if c == 1:
            print("牛吃完饭要睡觉啦~")
        else:
            print("哞~")
        return

    def yang(slef):
        print("羊吃完饭啦~")
        a = 1
        b = 2
        c = random.randint(a, b)
        if c == 1:
            print("羊吃完饭要睡觉啦~")
        else:
            print("咩~")
        return

while True:
    print("1、猫\n2、狗\n3、牛\n4、羊")
    choice = int(input("请输入要喂的动物编号："))
    if choice == 1:
        zoo().mao()
    elif choice == 2:
        zoo().gou()
    elif choice == 3:
        zoo().niu()
    elif choice == 4:
        zoo().yang()
    else:
        print("亲，该动物暂时不在动物园内哦~")
        break
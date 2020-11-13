'''import random
class ren(object):
    pass

# 类
class zoo(object):
    # 类的方法
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
'''

# 设计一个人类和一个动物类，动物类有猫狗牛羊四个子类
# 每个动物都有相同的吃饭和睡觉方法，有不同的叫的方法，人类有喂动物的方法，最终实现人类可以喂每一个动物，动物吃完后随机睡觉或叫
# 设计一个父类（睡觉和吃饭），延伸四个子类（四个动物，有一个单独的叫，继承父类的两个方法）
# 人类（去喂这些动物）
# 创建一个父类，父类中有公用的方法(吃饭、睡觉)
import random
class public(object):
    # 做的事情是方法，本身的特质是属性
    # name的属性是yangyue
    # name = "yangyue"

    def eat(self):
        print("吃完饭啦~")

    def sleep(self):
        print("睡觉")


# 创建四个子类，每个子类中调用父类的公用方法和建立自己的单独方法
class niu(public):
    def eat(self):
        public.eat(self)

    def sleep(self):
        public.sleep(self)

    def call(self):
        print("哞~")


class yang(public):
    def eat(self):
        public.eat(self)

    def sleep(self):
        public.sleep(self)

    def call(self):
        print("咩~")


class mao(public):
    def eat(self):
        public.eat(self)

    def sleep(self):
        public.sleep(self)

    def call(self):
        print("喵~")


class gou(public):
    def eat(self):
        public.eat(self)

    def sleep(self):
        public.sleep(self)

    def call(self):
        print("汪汪~")


# 创建一个人类,传入人类要喂的动物，调用该动物吃饭和叫的方法
class people(object):
    def wei(self, dongwu):
        dongwu.eat()
        a = random.randint(1, 2)
        if a == 1:
            dongwu.call()
        else:
            dongwu.sleep()

# 创建一个人对象
Amy = people()
# 先随机人要喂什么动物
c = random.randint(1, 4)
print(c)
if c == 1:
    print("喂猫")
    # 实例化猫这个动物
    cat = mao()
    # 调用amy 调用wei 去喂猫这个实例化的动物
    Amy.wei(cat)
elif c == 2:
    print("喂狗")
    # 实例化这个动物
    dog = gou()
    # 调用amy 调用wei 去喂猫这个实例化的动物
    Amy.wei(dog)
elif c == 3:
    print("喂牛")
    # 实例化这个动物
    cow = niu()
    # 调用amy 调用wei 去喂猫这个实例化的动物
    Amy.wei(cow)
elif c == 4:
    print("喂羊")
    # 实例化这个动物
    sheep = yang()
    # 调用amy 调用wei 去喂猫这个实例化的动物
    Amy.wei(sheep)
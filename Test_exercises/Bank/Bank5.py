"""
           * * * * * * * * * * * * * * * * * * * * * * * * * * *
               开户【0】 销户【1】 查询余额【2】 存款【3】 取款【4】
               转账【5】 冻结【6】 解冻【7】  查询信息【8】退出【9】
           * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

import time
import random


class User(object):
    def __init__(self, name, idCard, phone, password):
        self.name = name
        self.idCard = idCard
        self.phone = phone
        self.password = password

    def user_a(self):
        return self.name


class Card(object):
    pass


class Bank:
    allUser = {}

    # 开户
    def Open_card(self):
        name = input("请输入您的名字：")
        idCard = input("请输入您的身份证号：")
        phone = input("请输入您的电话号码：")
        password = input("请设置银行卡密码：")
        print("正在为您生成卡号.....")
        time.sleep(2)
        bank_card = self.random_card()

        user = User(name, idCard, phone, password)
        self.allUser = {bank_card:user}
        print("开户成功，您的卡号为：", bank_card)

    # 随机生成卡号
    def random_card(self):
        str = ""
        for i in range(0, 16):
            """for i in range(0, 16):
                number = random.randint(1, 9)"""
            ch = chr(random.randrange(ord("1"), ord("9")))
            str = str + ch
        return str

    # 查询
    def select_msg(self):
        bank_card = input("请输入银行卡号：")
        print(self.allUser[bank_card].user_a())



yue = Bank()
yue.Open_card()
yue.select_msg()


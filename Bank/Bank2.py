"""
银行系统
"""

import time


# 存储银行信息
class Bank_message:
    bank_all_user = []

    def __init__(self, name="", age=0, id_card=0, money=0):
        self.name = name
        self.age = age
        self.id_card = id_card
        self.money = money


# 界面操作类
class Bank_View:
    def __init__(self):
        # 把逻辑处理类传进来，变成属性
        self.controller = Bank_Controller()

    # 管理员登录界面
    def Admin_login(self):
        account = input("请输入后台管理账号：")
        password = input("请输入密码：")
        # 使用a对象去调用内部逻辑，传入账号和密码
        a = self.controller.judge_Admin(account, password)
        # 如果内部返回值是1，则登录成功
        if a == 1:
            print("登录成功，请稍后.....")
            time.sleep(2)
            self.__Bank_menu()
            return
        else:
            print("登录失败")
            return

    # 界面操作列表
    def __Bank_menu(self):
        print(
            """
            * * * * * * * * * * * * * * * * * * * * * * * * * * * 
                开户【0】 销户【1】 查询余额【2】 存款【3】 取款【4】
                转账【5】 冻结【6】 解冻【7】  查询信息【8】退出【9】
            * * * * * * * * * * * * * * * * * * * * * * * * * * * 
            """
        )

    # 操作调用
    def __select__menu(self):
        cmd = input("请输入选项ID：")

        # 开户
        if cmd == 0:
            self.controller.Open_card()
        # 销户
        elif cmd == 1:
            self.controller.Pin_card()
        # 查询余额
        elif cmd == 2:
            self.controller.Select_money()
        # 存款
        elif cmd == 3:
            self.controller.Save_money()
        # 取款
        elif cmd == 4:
            self.controller.Take_money()
        # 转账
        elif cmd == 5:
            self.controller.Shift_money()
        # 冻结
        elif cmd == 6:
            self.controller.Freeze_card()
        # 解冻
        elif cmd == 7:
            self.controller.Thaw_card()
        # 查询信息
        elif cmd == 8:
            self.controller.Select_message()
        # 退出
        elif cmd == 9:
            self.controller.Exit()
        # 兜底
        else:
            print("请输入正确的选项ID")

    # 启动程序
    def main(self):
        while True:
            self.__Bank_menu()
            self.__select__menu()


# 内部逻辑处理类
class Bank_Controller(object):  # object指这是一个可实例化的类
    # 用户字典
    def __init__(self, allUsers):
        self.allUsers = allUsers

        # 管理员登录

    def judge_Admin(self, account, password):
        right_account = "admin"
        right_password = "123456"
        # 如果传入值=默认值则返回1
        if account == right_account and password == right_password:
            return 1
        else:
            return -1

    # 开户
    def Open_card(self):
        pass

        # 销户

    def Pin_card(self):
        pass

    # 查询余额
    def Select_money(self):
        pass

    # 存钱
    def Save_money(self):
        pass

    # 取钱
    def Take_money(self):
        pass

    # 转账
    def Shift_money(self):
        pass

    def Freeze_card(self):
        pass

    def Thaw_card(self):
        pass

    def Select_message(self):
        pass

    def Exit(self):
        pass


user_yang = Bank_View()
user_yang.Admin_login()
# user_yang.main()

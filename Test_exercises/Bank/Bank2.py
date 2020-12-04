"""
银行系统
"""
import random
import time


# 存储用户信息
class User(object):
    def __init__(self, user_name, user_phone, usr_idCard):
        self.user_name = user_name
        self.user_phone = user_phone
        self.usr_idCard = usr_idCard


# 存储银行信息
class Bank(object):
    def __init__(self, user_password, user_money, user_card_number):
        self.user_password = user_password
        self.user_money = user_money
        self.user_card_number = user_card_number


# 界面操作类
class Bank_View(object):
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
        self.allUsers = allUsers()

    # 管理员登录
    def judge_Admin(self, account, password):
        right_account = "admin"
        right_password = "123456"
        # 如果 用户输入值=默认值 则返回1
        if account == right_account and password == right_password:
            return 1
        else:
            return -1

    # 开户
    def Open_card(self):
        name = input("请输入开户姓名：")
        phone = input("请输入电话号码：")
        idCard = input("请输入身份证号：")
        password = input("请设置银行卡密码：")


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

    # 冻结
    def Freeze_card(self):
        pass

    # 解冻
    def Thaw_card(self):
        pass

    # 查询信息
    def Select_message(self):
        pass

    # 退出
    def Exit(self):
        pass


user_yang = Bank_View()
user_yang.Admin_login()
# user_yang.main()

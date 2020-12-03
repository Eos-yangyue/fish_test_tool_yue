"""
设计一个模拟银行管理系统
用户可以登录银行管理员账号,并且能够执行开户（包括录入开户人信息）
查询、存钱、取钱（使用input输入数字）、改密码、转账、冻结、解冻、补办银行卡、销户的操作

"""


# 银行类
class Bank:
    # 银行卡信息
    def card(self, cid, pwd):
        pass

    # 操作列表
    def __Bank_menu(self):
        print(
            """
                    ('开户【0】 销户【1】 查询余额【2】 存款【3】 取款【4】')
                    ('转账【5】 冻结【6】 解冻【7】  查询信息【8】退出【9】')
            """
        )

    # 启动程序
    def main(self):
        while True:
            self.menu()
            # 选择功能
            self.__select__menu()


# 管理员
class Admin:
    # 管理员账号密码
    def __init__(self, user_name="", user_password="", user_Id_card="", admin_user="", admin_password=""):
        self.admin_user = admin_user
        self.user_name = user_name
        self.user_password = user_password
        self.user_Id_card = user_Id_card
        self.admin_password = admin_password

    # 登录
    def login(self):
        if admin_user == admin_user and admin_password == admin_password:
            print("登录成功")
            return True
        else:
            print("登录失败")
            return False

    # 开户
    def open_card(self):
        name = input("请输入开户姓名：")

    # 销户
    def del_card(self):
        pass

    # 冻结
    def freeze(self, account):
        pass

    # 解冻
    def thaw(self, account):
        pass

    # 补办银行卡
    def reapply_card(self):
        pass


# 用户类
class User:

    # 查询
    def select_msg(self):
        pass

    # 存钱
    def add_money(self, num):
        pass

    # 取钱
    def get_money(self, num):
        pass

    # 修改密码
    def upd_pwd(self, new_pwd):
        pass

    # 转账
    def shift_money(self, account, money):
        pass


ming = Admin()
account = input("请输入管理员账号：")
pwd = input("请输入管理员密码：")
ming.login(account, pwd)
#Bank().menu()
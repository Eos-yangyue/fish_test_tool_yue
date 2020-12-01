"""
银行系统
"""

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

    def Admin_login(self):
        account = input("请输入后台管理账号：")
        password = input("请输入密码：")
        self.controller.judge_Admin(account, password)

    # 操作列表
    def Bank_menu(self):
        print(
            """
                    '开户【0】 销户【1】 查询余额【2】 存款【3】 取款【4】'
                    '转账【5】 冻结【6】 解冻【7】  查询信息【8】退出【9】'
            """
        )

    # 调用操作
    class select_menu:
        def __init__(self, operation_id):
            self.operation_id = operation_id

        def Open_card(self):
            pass

        def Pin_card(self):
            pass

        def Select_money(self):
            pass

        def Save_money(self):
            pass

        def Take_money(self):
            pass

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

        # 开户
        def call_methods(self):
            cmd = input("请输入选项ID:")

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


# 后台挂哪里
class Admin(object):

    def judge_Admin(self, account, password):
        right_account = "admin"
        right_password = "123456"
        if account != right_account:
            print("账号错误，请重新输入:")
            return -1
        if password != right_password:
            print("密码错误，请重新输入:")
            return -1

        print("登录成功")
        Bank_View.Bank_menu()


user_yang = Bank_View()
user_yang.Admin_login()
user_yang.main()

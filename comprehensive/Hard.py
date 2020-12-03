# 设计一个模拟银行管理系统，用户可以登录银行管理员账号，并且能够执行开户（包括录入开户人信息）
# 查询、存钱、取钱（使用input输入数字）、改密码、转账、冻结、解冻、补办银行卡、销户的操作

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:14:31 2018
@author: Administrator
一个简单的登录注册Demo
"""


def showMessage():
    print('---新建用户：（键入N/n）---')
    print('---登录帐号：（键入E/e）---')
    print('---退出程序：（键入Q/q）---')


def new_user():
    while True:
        myname = input("请输入用户名：")
        if myname in user:
            print('你输入的用户名已存在，重新输入。')
            continue
        else:
            user[myname] = input('请输入密码：')
            print('注册成功，赶紧登录试试吧！')
            break


def older_user():
    while True:
        in_name = input('请输入登录用户名：')
        if in_name in user:
            in_password = input('请输入登录密码：')
            if in_password == user[in_name]:
                print('登录成功！\n')
                break
            else:
                print('你输入的密码有误！\n')
                break

        else:
            print('你输入的用户名不存在')
            continue


user = {}
while True:
    showMessage()
    myIn = input('---请输入指令代码：')
    if myIn in 'nN':
        new_user()

    elif myIn in 'eE':
        older_user()

    elif myIn in 'Qq':
        print('程序已退出')
        break
    else:
        print('你输入的指令有误，重新输入。')
        continue
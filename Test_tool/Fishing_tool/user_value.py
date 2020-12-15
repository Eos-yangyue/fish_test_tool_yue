"""
a)	每次增加pay值时，根据用户的付费渠道信息，计算real_pay增加值=pay增加值×渠道系数（渠道系数可配置）
b)	用户价值=real_pay+（outcome- income）-（exchangeincome）-cpl奖励（cpl_reward）

"""


# 计算充值后的real_pay
def calculate_real_pay():
    pay = float(input("请输入充值数："))
    proportion = float(input("请输入渠道系数："))
    now_real_pay = float(input("请输入现在real_pay的值："))
    add_real_pay = pay * proportion
    end_real_pay = now_real_pay + add_real_pay
    print("最终的real_pay应是：", end_real_pay)


# 计算用户价值
def user_vlaue():
    real_pay = float(input("请输入real_pay值："))
    outcome = float(input("请输入outcome值："))
    income = float(input("请输入income值："))
    exchangeincome = float(input("请输入exchangeincome值："))
    cpl_reward = float(input("请输入cpl_reward值："))
    user_vlaue = real_pay + (outcome - income) - (exchangeincome) - cpl_reward
    print("用户价值为：", user_vlaue)


# 计算垃圾用户剩余价值
def garbage_user_value():
    real_pay = float(input("请输入real_pay值："))
    outcome = float(input("请输入outcome值："))
    income = float(input("请输入income值："))
    exchangeincome = float(input("请输入exchangeincome值："))
    cpl_reward = float(input("请输入cpl_reward值："))
    most_pure_pay = float(input("请输入most_pure_pay值："))
    garbage_user_value = (real_pay + outcome - income - exchangeincome - cpl_reward) / most_pure_pay
    print("垃圾用户剩余价值更新为：", garbage_user_value)


if __name__ == '__main__':
    # calculate_real_pay()
    # user_vlaue()
    garbage_user_value()

def win_day_pool():
    """
    捕鱼-10亿奖金赛
    print: 每日奖池+盈利值后的最终值
    """
    while True:
        initial_pool = float(input("输入初始每日奖池："))
        if initial_pool == 0:
            break
        else:
            win = float(input("输入本次盈利金额："))
            right_pool = initial_pool + (win * 0.03 * 0.1)
            print("盈利后的奖池值为：", right_pool)


win_day_pool()

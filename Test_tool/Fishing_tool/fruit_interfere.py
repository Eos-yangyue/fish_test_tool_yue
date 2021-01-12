"""
公式总结：


亏损用户干涉a公式（参数位置：fruitini.json）：
a = interfereLosePercent * (1 + interfereCoin / (盈利差值 - interfereCoin)) ^ (interfereBetCoin / 下注)
盈利用户的干涉a公式（参数位置：fruitini.json）：
a = -interfereWinPercent * (1 - interfereCoin / (盈利差值 + interfereCoin)) ^ (interfereBetCoin / 下注)

盈利额外加值（公式参数位置：tb_game_user_pay）
gain = Income - Outcome - Pay

期望盈利 = 总投注 * 抽水
diff = (实际盈利+gain)-(-期望盈利)-上\下限
"""


# 亏损用户
def fruit_low_user(all_bet, actual_win, bet, Income, Outcome, Pay):
    # gain 额外+值
    gain = Income - Outcome - Pay
    if gain > 0.9:
        gain_end = gain * 100000
    elif gain < -0.9:
        gain_end = gain * 1000
    else:
        gain_end = 0

    # 期望盈利 = 总投注 * 抽水
    Expected_profit = all_bet * 0.05
    # diff = (实际盈利+gain)-(-期望盈利)-下限
    diff = (actual_win + gain_end) - (-Expected_profit) - (-20000000)
    # 亏损用户的a = interfereLosePercent * (1 + interfereCoin / (盈利差值 - interfereCoin)) ^ (interfereBetCoin / 下注)
    low_user_a = 0.3 * (1 + 10000000 / (diff - 10000000)) ** (8000000 / bet)

    print("diff:", diff, "亏损用户a：", low_user_a)


# 盈利用户
def fruit_win_user(all_bet, actual_win, bet, Income, Outcome, Pay):
    # gain 盈利的额外加值
    gain = Income - Outcome - Pay
    if gain > 0.9:
        gain_end = gain * 100000
    elif gain < -0.9:
        gain_end = gain * 1000
    else:
        gain_end = 0

    # 期望盈利 = 总投注 * 抽水
    Expected_profit = all_bet * 0.05
    # diff = (实际盈利+gain)-(-期望盈利)-上限
    diff = (actual_win + gain_end) - (-Expected_profit) - 20000000

    # 盈利用户的a = -interfereWinPercent * (1 - interfereCoin / (盈利差值 + interfereCoin)) ^ (interfereBetCoin / 下注)
    win_user_a = -0.3 * (1 - 10000000 / (diff + 10000000)) ** (8000000 / bet)

    print("diff:", diff, "盈利用户a：", win_user_a)


if __name__ == '__main__':
    all_bet = float(input("请输入总投注："))
    actual_win = float(input("请输入实际盈利："))
    bet = float(input("请输入此次投注值："))
    Income = float(input("请输入该用户income："))
    Outcome = float(input("请输入该用户Outcome："))
    Pay = float(input("请输入该用户pay："))

    # 调用亏损用户函数
    # fruit_low_user(all_bet, actual_win, bet, Income, Outcome, Pay)

    # 调用盈利用户函数
    fruit_win_user(all_bet, actual_win, bet, Income, Outcome, Pay)

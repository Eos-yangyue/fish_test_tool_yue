# 水果机-盈利用户干涉值
# difference = 盈利差值
interfereWinPercent = 0.3
interfereCoin = 10000000
interfereBetCoin = 8000000
difference = 253358000
bet = 100000
a = -interfereWinPercent * (1 - interfereCoin / (difference + interfereCoin)) ** (interfereBetCoin / bet)
print(float(a))

# 水果机-亏损用户干涉值
# difference = 盈利差值
interfereWinPercent = 0.3
interfereCoin = 10000000
interfereBetCoin = 8000000
difference = -25000000
bet = 28000000
b = interfereWinPercent * (1 + interfereCoin / (difference - interfereCoin)) ** (interfereBetCoin / bet)
print(float(b))

# 龙凤-左右区域-盈利用户干涉值
# difference = 盈利差值、bet = 区域下注
interfereWinProbability = 0.2
interfereCoin = 10000000
interfereBetCoin = 30000000
difference = 28000000
bet = 100000
c = -interfereWinProbability * (1 - interfereCoin /(difference + interfereCoin)) ^ (interfereBetCoin / bet)

# 龙凤-左右区域-亏损用户干涉值
# difference = 盈利差值、bet = 区域下注
interfereLoseProbability = 0.2
interfereCoin = 10000000
interfereBetCoin = 30000000
difference = 28000000
bet = 100000
d = interfereLoseProbability * (1 + interfereCoin /(difference - interfereCoin )) ^ (interfereBetCoin / bet)

# 龙凤-暴击区域-盈利用户干涉值
# difference = 盈利差值、bet = 区域下注
interfereCritWinProbability = -0.15
interfereCoin = 10000000
interfereCritBetCoin = 10000000
difference = 28000000
bet = 100000
e = -interfereCritWinProbability * (1 - interfereCoin /(difference + interfereCoin )) ^ (interfereCritBetCoin / bet)

# 龙凤-暴击区域-亏损用户干涉值
# difference = 盈利差值、bet = 区域下注
interfereCritLoseProbability = 0.15
interfereCoin = 10000000
interfereCritBetCoin = 10000000
difference = 28000000
bet = 100000
f = interfereCritLoseProbability * (1 + interfereCoin /(difference - interfereCoin )) ^ (interfereCritBetCoin / bet)
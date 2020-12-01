# 黑杰克-基础干涉的概率,diff>0
def base_interference():
    InterfereWinPercent = 0.5
    coin = 10000000
    InterfereWinScale = 15
    diff = float(input("请输入diff:"))

    baseProbability = InterfereWinPercent * (1 - coin / (diff + coin)) ** InterfereWinPercent
    return print(float(baseProbability))


# 解除某个玩家的Facebook绑定
def remove_facebook():
    import uuid
    import time
    import requests

    # 需要更改绑定玩家的ID
    userId = 145083438
    x = uuid.uuid1()
    t = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))[:-4]
    url = "http://10.10.243.229:8100/management/changeAccount.html?userId=" + str(userId) + "&accountId=" + str(
        x) + "&password=07CUXFJIXZlYZx0V" + str(t)
    cookie = dict(WC='*****************')
    res = requests.get(url, cookies=cookie)
    print(res.text)

remove_facebook()
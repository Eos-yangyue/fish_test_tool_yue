#  计算干涉

def calInterferenceSicbo(bet,win,onebet,kind):
    diff,diff2=calDiffSicbo(bet,win)
    if kind==1:
        if diff>0:
            a=-0.3*(1-10000000/(diff+10000000))**(30000000/onebet)
        elif diff<0:
            a=0.3*(1+10000000/(diff-10000000))**(30000000/onebet)
        else:
            a=0
    else:
        if diff2>0:
            a=-0.3*(1-10000000/(diff2+10000000))**(30000000/onebet)
        elif diff2<0:
            a=0.3*(1+10000000/(diff2-10000000))**(30000000/onebet)
        else:
            a=0
    print(a)
def calInterferenceSicbo2(diff,onebet):
    if diff>0:
        a=-0.3*(1-10000000/(diff+10000000))**(30000000/onebet)
    elif diff<0:
        a=0.3*(1+10000000/(diff-10000000))**(30000000/onebet)
    else:
        a=0
    print(a)
    return a

# 通过下注，diff1和diff2，计算出所有干涉总和
def allInterferences(diff1,diff2):
    allInters=[]
    for i in range(56):
        allInters.append(0)
    for k,v in allBets.items():
        if v==0:continue
        if k<15:
            connect=area[k]["prizeID"].split(",")
            interf=calInterferenceSicbo2(diff1,v)
            for i in range(len(connect)):
                pos=int(connect[i])-1
                allInters[pos]+=interf
            continue
        else:
            connect = area[k]["prizeID"].split(",")
            interf = calInterferenceSicbo2(diff2, v)
            for i in range(len(connect)):
                pos = int(connect[i]) - 1
                allInters[pos] += interf
            continue

    print(allInters)
    return allInters

# 检测log输出是否正确
def checkRight(diff1,diff2,res1,res2):
    myAnswer=allInterferences(diff1,diff2)
    for i in range(len(myAnswer)):
        propob=prize[i]["prob"]
        newPob=int(propob*(1+myAnswer[i]))
        if newPob==res2[i] and myAnswer[i]>=res1[i]*0.9999 and myAnswer[i]<=res1[i]*1.0001:
            continue
        else:
            break
    if i<len(myAnswer)-1:
        print(False)
    else:
        print(True)

allBets= {
    49:20000000,
}
a=[0.0, 0.0, 0.0, 0.0, 0.0, 0.28847122261705777, 0.0, 0.0, 0.0, 0.0, 0.28847122261705777, 0.0, 0.0, 0.0, 0.0, 0.28847122261705777, 0.0, 0.0, 0.0, 0.0, 0.28847122261705777, 0.0, 0.0, 0.0, 0.0, 0.28847122261705777, 0.0, 0.0, 0.0, 0.0, 0.28847122261705777, 0.28847122261705777, 0.28847122261705777, 0.28847122261705777, 0.28847122261705777, 0.28847122261705777, 0.0, 0.0, 0.0, 0.28847122261705777, 0.0, 0.0, 0.28847122261705777, 0.0, 0.28847122261705777, 0.28847122261705777, 0.0, 0.0, 0.28847122261705777, 0.0, 0.28847122261705777, 0.28847122261705777, 0.0, 0.28847122261705777, 0.28847122261705777, 0.28847122261705777]

b=[10, 10, 10, 10, 10, 12, 30, 30, 30, 30, 38, 30, 30, 30, 30, 38, 30, 30, 30, 30, 38, 30, 30, 30, 30, 38, 30, 30, 30, 30, 38, 38, 38, 38, 38, 38, 60, 60, 60, 77, 60, 60, 77, 60, 77, 77, 60, 60, 77, 60, 77, 77, 60, 77, 77, 77]

checkRight(-426240001,-377799999,a,b)








#  第二个奖池上下限

def calPoolSicbo2(money):
    #将各个下注区间的抽水和波动写入数组
    moneyLevel=[1000000000,4000000000-1000000000,10000000000-4000000000,20000000000-10000000000]
    pumpLevel=[0.1,0.08,0.06,0.04,0.02]
    up=[1000000,2000000,3000000,4000000,5000000]
    down=[-1000000,-2000000,-3000000,-4000000,-5000000]
    #结果数组，入池的钱以及波动值
    inPool=0
    shake=0
    # 计算出前4个阶段的入池钱数
    for i in range(4):
        if money>moneyLevel[i]:
            inPool+=moneyLevel[i]*(1-pumpLevel[i])
            money=money-moneyLevel[i]
        else:
            inPool+=money*(1-pumpLevel[i])
            money=0
            upRes=up[i]
            downRes=down[i]
            break
    # 若有钱超过前四个阶段，余钱直接使用最后一档
    if money!=0:
        inPool += money * (1 - pumpLevel[4])
        upRes = up[4]
        downRes = down[4]
    # 返回计算结果
    return inPool+upRes,inPool+downRes

# 计算两个diff
def calDiffSicbo(bet,win):
    up,down=calPoolSicbo(bet)
    up2,down2=calPoolSicbo2(bet)
    real=bet+win
    if (real > up):
        diff = real - up
    elif real < down:
        diff = real - down
    else:
        diff = 0
    real2 = bet + win
    if (real2 > up2):
        diff2 = real2 - up2
    elif real2 < down2:
        diff2 = real2 - down2
    else:
        diff = 0
    print(diff,diff2)
    return diff,diff2
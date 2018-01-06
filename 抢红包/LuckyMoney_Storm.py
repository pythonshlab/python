import random
#抢红包程序,最多支持100个红包，可以用正则控制input
strLuckyMoneySum=input('红包总额：')
strLuckyMoneyCount=input('红包个数：')
floLuckyMoneySum=float(strLuckyMoneySum)
IntLuckyMoneyCount=int(strLuckyMoneyCount)
floLuckyMoneySum=round(floLuckyMoneySum,2)
#先生成随机数，然后将随机数相加，最后按比例分配红包
resultList=random.sample(range(1,100),IntLuckyMoneyCount)
SumList=sum(resultList)
index=0
luckySum=0
BalMoney=round(floLuckyMoneySum,2)
while len(resultList)>1:  #list大余1
    index=index+1
    luckyIndex=resultList.pop()
    luckyratio=luckyIndex/SumList
    luckyMoney=round(floLuckyMoneySum*luckyratio,2)
    luckySum=round(luckySum+luckyMoney,2)
    BalMoney=round(BalMoney-luckyMoney,2)
    print('你抢到了红包的金额为：',luckyMoney)
    print('余额为：',BalMoney)
    print('已抢的金额为：',luckySum)
else:  #最后一次循环，直接用余额作为红包
    print('你抢到了红包的金额为：',BalMoney)
print(SumList)

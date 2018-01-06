#Coding=UTF-8
import random
import sys

def calLuckyMoney(total,num): #计算红包函数
    total=float(total) #红包总金额
    num=int(num) #红包数量
    min=0.01 #红包最小金额，0.01元
    if(num<1):
        print("你也太抠门了，红包数量都小于1了，还打算发不发？")
        return
    if num==1:
        print("恭喜第%d个人，拿到红包数为：%.2f" %(num,total))
        return
    i=1 #循环判断条件
    while(i<num): #当红包数量大于1时，继续发放
        max=total-min*(num-i)
        '''设定红包的最大值，确保不会出现第2个抢红包的人，就把剩下所有的红包抢完
        total代表剩下的金额，(num-i)代表还剩多少个红包要分，min代表每个红包的最小金额
        红包的最大金额=剩下的金额-最小金额*（剩下多少个红包需要发）
        '''
        # k = int(num - i)
        k=int((num-i)/2)
        if(num-i>=1):
            k=num-i
        max=max/k
        money=random.randint(int(min*100),int(max*100))
        money=float(money/100)
        total=total-money
        print("第%d个人拿到红包数为：%.2f, 余额为: %.2f" %(i,money,total))
        i+=1
    print("第%d个人拿到红包数为：%.2f, 余额为: %.2f" %(i, total, 0.0))
if __name__ == "__main__":
    total =input("输入红包总金额:")
    num = input("输入发红包数量:")
    calLuckyMoney(total,num)
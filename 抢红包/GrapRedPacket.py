# 模拟抢红包

import random
# 备姓、名信息
xin = ('张', '王', '李', '赵', '陈', '钱', '孙', '周', '吴', '郑', '冯', '蒋', '沈', '韩', '杨')
ming = ('进', '刚', '鹏', '兰', '爱国', '建华', '庆余', '榕', '花', '华', '洁', '霞', '强', '丽丽', '辰')

money = 100 * int(input('请输入红包金额：'))
redNumber = int(input('请输入红包数量：'))

# 定义存储红包的集合
redPacketlist = []

# 生成5个随机的红包
for i in range(0, redNumber):
    if i == redNumber-1:
        redPacketlist.append(money)
        break
    redPacketlist.append(random.randint(1,money))
    money -= redPacketlist[i]
# 生成5个明细
# 定义随机生成5个名字
name = []
while True:
    current = str(xin[random.randint(0, len(xin)-1)]) + str(ming[random.randint(0, len(ming)-1)])
    if current in name:
        continue
    name.append(current)
    if len(name) == redNumber:
        break

# 抢红包
for i in range(0,len(name)):
    myred = redPacketlist[random.randint(0,len(redPacketlist)-1)]
    print(name[i] + '抢到了红包，金额为：' + str(myred/100) )
    redPacketlist.remove(myred)








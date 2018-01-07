# 实现人民币小写转大写


# 实现转换格式的优化
def rmb_format(money_text):
    if (str(money_text)).endswith("零角零分"):
        money_text = str(money_text).replace("零角零分", "") + "整"
    if (str(money_text)).endswith("零分"):
        money_text = str(money_text).replace("零分", "")
    if "零仟零佰零拾" in (str(money_text)):
        money_text = str(money_text).replace("零仟零佰零拾", "零")
    if "零佰零拾" in (str(money_text)):
        money_text = str(money_text).replace("零佰零拾", "零")
    if "零仟零佰" in (str(money_text)):
        money_text = str(money_text).replace("零仟零佰", "零")
    if "零仟" in (str(money_text)):
        money_text = str(money_text).replace("零仟", "零")
    if "零佰" in (str(money_text)):
        money_text = str(money_text).replace("零佰", "零")
    if "零拾" in (str(money_text)):
        money_text = str(money_text).replace("零拾", "零")
    if "零零" in (str(money_text)):
        money_text = str(money_text).replace("零零", "零")
    if "零万" in (str(money_text)):
        money_text = str(money_text).replace("零万", "万")
    if "零亿" in (str(money_text)):
        money_text = str(money_text).replace("零亿", "亿")
    if "亿万" in (str(money_text)):
        money_text = str(money_text).replace("亿万", "亿")
    if "零圆" in (str(money_text)):
        money_text = str(money_text).replace("零圆", "圆")
    if (str(money_text)).startswith("圆"):
        money_text = str(money_text)[1: len(str(money_text))]
    return money_text


# 定义人民币的单位
chinese = ['分', '角', '圆', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿', '拾', '佰', '仟']
chinese_number = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
# 提醒并接收输入，转换成二位小数的字符串
RMB = str.format('%.2f' % float(input("请输入人民币金额：")))
# 替换字符串的小数点并反序
RMBString = (str(RMB).replace('.', ''))[::-1]
# 判断金额是不是有效范围
if "-" in RMBString:
    print("金额不能为负数！")
elif len(RMBString) > 14:
    print("金额太大！最大金额数到千亿！")
else:
    # 定义变量存储转换后的值
    result = ""
    # 开始拼接转换的大写文本
    for i in range(0, len(RMBString)):
        result += chinese[i] + chinese_number[int(RMBString[i])]
    # 打印结果
    print(rmb_format(result[::-1]))



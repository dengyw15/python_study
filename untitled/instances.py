#!/usr/bin/python
import cmath
import calendar
import datetime
from urllib import  request

'''实例1'''
# num1 = input("请输入第一个数字：");
# num2 = input("请输入第二个数字：");
# sum = float(num1) + float(num2);
# print("数字{0}和数字{1}之和为{2}".format(num1, num2, sum));

'''实例2'''
# print(cmath.sqrt(float(input("请输入第一个数字："))));
'''实例3  最大公约数'''
def hcf(x,y):
    if (x < y):
        smaller = x;
    else:
        smaller = y;
    for i in range(1, smaller + 1):
        if ((x%i == 0) and (y%i ==0)):
            hcf = i;
    return hcf;

print(hcf(27,63));

'''实例4 最小公倍数'''
def lcm(x,y):
    if (x < y):
        bigger = y;
    else:
        bigger = x;
    i = 1;
    while True:
        tmp = bigger * i;
        if (tmp % x == 0):
            lcm = tmp;
            break;
        i += 1;
    return lcm;
print(lcm(2,9));

'''实例4 获取昨天的日期'''
def getYestoday():
    today = datetime.date.today();
    oneday = datetime.timedelta(days=-1);
    return today + oneday;
print(getYestoday());
'''实例5 判断素数'''

def sushu(num) :
    for i in range(2, num-1):
        if (num % i == 0):
            print("{0}不是素数".format(num));
            break;
    else:
        print("{0}是素数".format(num));

while True:
    num = input("请输入一个整数：");
    if num != 'exit':
        try:
            sushu(int(num));
        except:
            print("输入的{0}不是整数".format(num));
        finally:
            print("哈哈哈 不管怎样 你都要执行我");
    else:
        break;

'''实例 读取文件'''
with open("H:/test.txt", "r+") as of:
    print(of.read(10).encode("utf-8"));


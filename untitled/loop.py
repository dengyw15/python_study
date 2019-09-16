#!/usr/bin/python
import random
list = [21,23,10,56,12];
while len(list) > 0:
    num = list.pop();
    if num % 2 == 0:
        print("even num :" , num);
    else:
        print("odd num:", num);

var = 1;
# while var == 1:
#     num = int(input("pls input a num："));
#     if num > 0 :
#         print("the num you input is ", num);
#     else:
#         break;

'''''''''''''''
print("============================================");
pai = {'1':'石头', '2':'剪刀', '3':'布'};
print(pai['1'])
while 1 :
    num = random.randint(1,3);
    inputnum = int(input("请猜拳 1 石头，2 剪刀， 3 布："));
    if num == 1:
        if inputnum == 1:
            print("你和电脑均出了" + pai.get(str(num)) + ";平局");
        elif inputnum == 2 :
            print("你出了" + pai.get(str(inputnum)) + ",电脑出了" + pai.get(str(num)) + ",你输了");
        else:
            print("你出了" + pai.get(str(inputnum)) + ",电脑出了" + pai.get(str(num)) + ",你赢了了");
    elif num ==2:
        if inputnum == 1:
            print("你出了" + pai.get(str(inputnum)) + ",电脑出了" + pai.get(str(num)) + ",你输了");
        elif inputnum == 2 :
            print("你和电脑均出了" + pai.get(str(num)) + ";平局");
        else:
            print("你出了" + pai.get(str(inputnum)) + ",电脑出了" + pai.get(str(num)) + ",你赢了");
    else:
        if inputnum == 1:
            print("你出了" + pai.get(str(inputnum)) + ",电脑出了" + pai.get(str(num)) + ",你赢了");
        elif inputnum == 2 :
            print("你出了" + pai.get(str(inputnum)) + ",电脑出了" + pai.get(str(num)) + ",你赢了");
        else:
            print("你和电脑均出了" + pai.get(str(num)) + ";平局");

    if inputnum == 0:
        break;
'''
list1 = ['aaa','bbb','ccc'];
for le in 'test':
    print(le);
# for s in list1:
#     print(s);

for i in range(len(list1)):
    print(list1[i]);

for i, j in enumerate(list1):
    print(str(i) + " " + str(j));

'''判断质数'''
for num in range(10, 20):
    for i in range(2,num):
        if num % i == 0:
            print(str(num) + "=" + str(i) + "*" + str(int(num/i)) + "，不是质数");
            continue;
    else:
        print(str(num) + "是质数！");

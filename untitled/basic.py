#!/usr/bin/python
from urllib import request
import os
import shutil
import glob
print("你好");
print ("hello");
x="a"
y='b';
print(x)
print(y)

counter=1000;
miles=1000.0;
name="john";
print(counter);
print(miles);
print(name);
a,b,c=1,2,name;
print(a);
print(b);
print(c);
del c;
str1= "Hello world";

print(str1[0]);
print(str1[0:5]);
print(str1[2:]);
print(str1 * 3);
print(str1 + "hahahha");
list1 = ["dfs","ddd","eee","fff"];
list1[2] = "ttt";
list2 = ["ggg"];
print(list1[0]);
print(list1[2:4]);
print(list2 * 2);
print(list1 + list2);

dict = {};
dict['one'] = "this is dict one";
tinydict = {'one' : 'onedict', 'two' : 'twodict'};
print(dict['one']);
print(tinydict['one'] + " " + tinydict["two"]);
print(tinydict.keys());
print(tinydict.values());
print(type(tinydict));print(type(a));
print(isinstance(a,int));
print("cdezhiwei:", a);
if (a == b) :
    print("a=b");
else :
    print("a!=b")

if ("aaa" in list1) :
    print("aaa in list1");
else :
    print("aaa not in list1");

b = 4444.0; a = 4444.0;
print(a is b);

for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4));

print('-1.2'.zfill(6));
print('"{}:128.160.96.126",{}'.format("a","b"));

# fo = open("H:/test.txt", "r+");
# fo.write("This is a test line");
# fo.buffer
# for line in fo:
#     print(line, end='');

# response = request.urlopen("http://11.33.186.41:1158/Login.jsf");
# fi = open("H:/test.txt", "w");
# page = fi.write(str(response.read()));
# fi.close();

# dir(shutil);
# help(shutil);
# shutil.copyfile("H:/test.txt","H:/test.txt1")

# print(glob.glob("*"));

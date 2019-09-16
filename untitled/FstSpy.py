#!/usr/bin/python3
import requests
import urllib
# import urllib2
from bs4 import BeautifulSoup as bs
import os
import re

# html = requests.get("http://icsp.jh:1340/ICSPWeb/jsp/fundProd/manualSql.jsp");
# print(html.text);
html = open("H:/test.txt", "r+");
# print(html.read());
content = html.read();
soup = bs(content, "html.parser");
ipt = soup.findAll("input");
# print(ipt)
for inpt in ipt:
    print(inpt.get('value'))

values = {};
values['j_username'] = 'dengyaowen.zh';
values['j_password'] = 'abcd1234';
# data = urllib.urldecode(values)
# request = urllib.requst("http://itsm2.management.ccb/CAisd/pdmweb3.exe", data);
response = urllib.request.urlopen("http://itsm2.management.ccb/CAisd/pdmweb3.exe");
print(response.read(), "UTF-8")

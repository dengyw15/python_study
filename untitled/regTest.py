#!/usr/bin/python3
import re
import xml.sax
import time

print(re.search("ccb", "www.ccb.com").span());

print(time.localtime());
print(time.strftime("%Y-%m-%d %H:%M:%S %A %B %D", time.localtime()));
#!/usr/lib/python
from urllib import request
from datetime import date,datetime

# for line in request.urlopen("http://128.160.214.12/Citrix/XDWeb/auth/loggedout.aspx?CTX_MessageType=INFORMATION&CTX_MessageKey=SessionExpired"):
#     line = line.decode("UTF-8");
#     if 'div' in line:
#         print(line);

now = date.today()
print(now);print(now.strftime('yyyy-MM-dd HH:mm:ss'))
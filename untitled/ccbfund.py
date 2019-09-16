import requests
import json
from multiprocessing.managers import BaseManager

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'tranCCBIBS1=MuIkWSdvSk3fOp5IV3mhmp58ARoUqm8Lb0WP4G6Hn0XQNWpDo72WFHo0DpChCmTHV4GPaGODx5wPDGcXnzlPNWGXN65QqGMXlCiB7O31yP; WCCTC=996631183_905436718_131714450; ccbcustomid=915e5401866c6184s4nWAgwIzDP3uCzzmDuq1500604387386elfXdRgGufj2Kke4DqXQ23b363bed976d024834b257d6dd579d6; ccbsessionid=MydXU1zbynrK7nYb033d6d2eab5-20170721103307; ccbdatard=1; cookieidTagFlag=1; tagInfoId=%26_000094%3D1%26_000050%3D07; lastUpdateTime=2017-07-21%2010%3A33%3A27; cityName=%E5%8C%97%E4%BA%AC%E5%B8%82; cityCode=110000; bankName=%E5%8C%97%E4%BA%AC%E5%B8%82%E5%88%86%E8%A1%8C; bankCode=110000000; cityCodeFlag=2; cityCodeCustId=; BIGipServerccvcc_jt_197.1_80_web_pool=1176699658.20480.0000; JSESSIONID=GC9jB2YN4NXehtccvvgKinH1ku9yfq1EkRcZeWbtoFlEFZjoF212!-1623685127; INFO=9a9d|WXFqW; ticket=; cs_cid=; custName=; userType=; lastLoginTime=; tranFAVOR=OvAB6B8F8wm2vesIKTB2hesIZTr2EeCINTi2fe0ICTN21e0IITu2jX3WSWuNBmlAzl',
    'Host': 'fund.ccb.com',
    'Referer': 'http://fund.ccb.com/cn/fund/product/product_index.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
param = {
    'CCB_IBSVersion': 'V5',
    'isAjaxRequest': 'true',
    'SERVLET_NAME': 'WCCMainPlatV5',
    'TXCODE': 'NF4J01',
    'PERPAGE': '12',
    'ISCURRFUND': '1',
    'PAGE': 1
}

resp = requests.get("http://fund.ccb.com/tran/WCCMainPlatV5", params=param, headers=headers)
print(resp.url)
funddata = json.loads(resp.text)
totalpage = funddata['TotalPage']
print(totalpage)

for info in funddata['INFO']:
    print(info['FUNDNAME'], info['CCBFUNDCODE'], info['NAVPUBDATE'], info['NETVALUE'])

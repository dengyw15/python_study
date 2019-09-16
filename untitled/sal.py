# -*- coding: UTF-8 -*-
import requests
from lxml import etree
from selenium import webdriver
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class Salary:
    def __init__(self, username, password, startmonth=1, endmonth=12):
        self.username = username
        self.password = password
        self.startmonth = startmonth
        self.endmonth = endmonth
        currcookie = self.__login()

        print(currcookie)
        if currcookie is not None:
            self.cookie = currcookie

    def __login(self):
        # chromdriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver_x64.exe'
        # os.environ['webdriver.chrome.dirver'] = chromdriver
        # browser = webdriver.Chrome(chromdriver)
        browser = webdriver.Chrome()
        browser.get('http://11.33.186.41:1158/Login.jsf')
        #开始登陆
        try:
            usernamelem = browser.find_element_by_id('form1:loginName')
            usernamelem.send_keys(self.username)
            pwdelem = browser.find_element_by_id('form1:password')
            pwdelem.send_keys(self.password)
            browser.find_element_by_id('form1:_id0').click()
            sallink = browser.find_element_by_id('tree:_id89')
            sallink.click()

        except NoSuchElementException:
            print('no such element')
        currcookie = browser.get_cookies()[0]['value']
        return currcookie

    def requestsalurl(self, month):
        url = 'http://11.33.186.41:1158/self/PayOneQuery.jsf'
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '298',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'JSESSIONID=' + self.cookie,
            'Host': '11.33.186.41:1158',
            'Origin': 'http://11.33.186.41:1158',
            'Referer': 'http://11.33.186.41:1158/self/SelfIndex.jsf',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/40.0.2214.94 Safari/537.36'
        }
        data = {
            'content:form1:_id179:': '',
            'content:form1:_id184': '2016',
            'content:form1:_id187': month,
            'content:form1_SUBMIT': '1',
            'content:form1:beginTime': '2016-01-01',
            'content:form1:endTime': '2016-12-31',
            'autoScroll': '0,100',
            'content:form1:_id212': '按月明细查询',
            'content:form1:_link_hidden_': ''
        }

        salresp = requests.post(url, headers=header, data=data)
        return salresp.text

    def parserhtml(self):
        allsaldata = []
        for month in range(self.startmonth, self.endmonth + 1):
            if month < 10:
                strmonth = '0' + str(month)
            else:
                strmonth = str(month)
            content = self.requestsalurl(strmonth)
            # print(content)
            tree = etree.HTML(content)
            tbody = tree.xpath("//tbody[@id='content:form1:userdata:tbody_element']")
            # print(tbody)
            if tbody is not None and len(tbody) > 0:
                tbodyelements = tbody[0]
                onemonthsal = {}

                for tr in tbodyelements.getchildren():
                    colname = tr.findtext("td[@class='h_css_Column2']/span")
                    colvalue = tr.findtext("td[@class='h_css_Column3']/span")
                    onemonthsal.__setitem__(colname, colvalue)
                allsaldata.append(onemonthsal)
            else:
                print('{0}月无发薪记录'.format(month))
        return allsaldata

    def outputresult(self):
        allsaldata = self.parserhtml()
        th = ['基本工资', '岗位工资', '绩效工资', '通讯补贴', '交通补贴', '住房补贴', '应发工资',
              '应纳税工资额', '实际代扣个人所得税额', '住房公积金个人缴费', '企业年金个人缴费', '应扣工资',
              '实发工资', '发放说明']
        html = '''
        <html>
            <body>
                <table align="center" border="1" cellpadding="4">
                    <thead>
                        <tr>
        '''
        allhead = ''
        for head in th:
            onehead = '<th>' + head + '</th>\n'
            allhead += onehead
        html += allhead
        html += '</tr></thead>'

        onetr = ''
        for onemonsal in allsaldata:
            onetd = ''
            for head in th:
                value = onemonsal.get(head)
                if value is None:
                    continue
                onetd += '<td>' + value + '</td>'
            onetr = '<tr>' + onetd + '</tr>'
            print(onetr)
            html = html + onetr

        html = html + '</table></body></html>'
        with open('H:/tmp/python/sal.html', 'w') as f:
            f.seek(0, 0)
            f.write(html)

if __name__ == '__main__':
    sal = Salary('dengyaowen.zh', 'kevin200711')
    sal.outputresult()


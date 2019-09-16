from selenium import webdriver
import requests
from bs4 import BeautifulSoup


class Sal:

    def __init__(self, username, pwd, begintime, endtime):
        self.username = username
        self.pwd = pwd
        self.begintime = begintime
        self.endtime = endtime

    def __login(self):
        url = 'http://11.33.186.41:1158/Login.jsf'
        browser = webdriver.Chrome()
        browser.get(url)
        browser.find_element_by_id('form1:loginName').send_keys(self.username)
        browser.find_element_by_id('form1:password').send_keys(self.pwd)
        browser.find_element_by_id('form1:_id0').click()
        try:
            cookies = browser.get_cookies()
            if cookies is not None and len(cookies) > 0:
                return cookies[0]['value']
        except Exception as ex:
            print('login failed')
            exit()

    def parseData(self, html=''):
        filepath = 'H:/tmp/python/salsource.html'
        with open(filepath, 'r+', encoding='utf-8') as f:
            bs = BeautifulSoup(f.read(), "html.parser")
            print(bs.find("td", class_='td_middle_center').has_attr('class'))

    def queryDetail(self):
        url = 'http://11.33.186.41:1158/self/PayAll.jsf'
        data = {
                'beginTime': self.begintime,
                'endTime': self.endtime
                }
        cookies = {'JSESSIONID': self.__login()}
        resp = requests.get(url, params=data, cookies=cookies)
        filepath = 'H:/tmp/python/salsource11.html'
        with open(filepath, 'w+') as f:
            f.write(resp.text)

if __name__ == '__main__':
    sal = Sal('dengyaowen.zh', 'kevin200711', '2017-01-01', '2017-08-31')
    sal.parseData()

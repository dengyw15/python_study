from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import os
import requests

chromdriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver_x64.exe'
os.environ['webdriver.chrome.dirver'] = chromdriver

browser = webdriver.Chrome(chromdriver)
browser.get('http://11.33.186.41:1158/Login.jsf')
try:
    userelem = browser.find_element_by_id('form1:loginName')
    userelem.send_keys('dengyaowen.zh')
    pwdelem = browser.find_element_by_id('form1:password')
    pwdelem.send_keys('kevin200711')
    loginelem = browser.find_element_by_id('form1:_id0')
    loginelem.send_keys(Keys.RETURN)
    sallink = browser.find_element_by_id('tree:_id89')
    sallink.click()
    print(browser.current_url)

    yearsel = browser.find_element_by_name('content:form1:_id184')
    Select(yearsel).select_by_value('2015')
    monthsel = browser.find_element_by_name('content:form1:_id187')
    Select(monthsel).select_by_value('11')
    detailbutton = browser.find_element_by_id('content:form1:_id212')
    detailbutton.click()
except NoSuchElementException:
    print('nosuchElement')
print(browser.page_source)
# print(browser.find_elements_by_xpath("//*[contains(text(),'建设')]")[0])

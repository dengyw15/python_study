import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchFrameException

# chromdriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver_x64.exe'
# os.environ['webdriver.chrome.dirver'] = chromdriver
# browser = webdriver.Chrome(chromdriver)
# browser = webdriver.Ie()
browser = webdriver.Chrome()
browser.get('http://11.33.186.42:8008/signInfo/faces/login.jsp')
usernameelem = browser.find_element_by_id('loginform:staffId')
usernameelem.send_keys('dengyaowen')
pwdelem = browser.find_element_by_id('loginform:password')
pwdelem.send_keys('password')
browser.find_element_by_id('loginform:loginBtn').click()
print('==========1 login===============')
print(browser.page_source)
print('==========1 login end============')

try:
    browser.switch_to_frame('left')
    print('========1 left=========')
    print(browser.page_source)
    print('========1 left end==============')
except NoSuchFrameException:
    try:
        browser.switch_to_frame('mainFrame')
        print('=========mainFrame========')
        print(browser.page_source)
        print('========mainFrame end==========')
    except NoSuchFrameException as ex:
        print(ex)

browser.switch_to_frame('left')
print('========2 left=========')
print(browser.page_source)
print('========2 left end==============')

# browser.find_element_by_id('pdiv_10000').click()
# browser.get('http://11.33.186.42:8008/signInfo/faces/check/person_do_check1.jsp')
# print(browser.find_element_by_xpath("//div[@id='init']/div[@id='div_10000_01']/ul/li"))
browser.find_element_by_id("pdiv_10000").click()
browser.find_element_by_xpath("//div[@id='init']/div[@id='div_10000_01']/ul/li").click()
browser.switch_to_default_content()
browser.switch_to_frame('mainFrame')
browser.switch_to_frame('right')
print(browser.page_source)
browser.find_element_by_id('form1:_idJsp1').send_keys('2017-08-01')
browser.find_element_by_id('form1:endDate').send_keys('2017-08-10')
browser.find_element_by_id('form1:_idJsp9').click()
browser.switch_to_default_content()
browser.close()

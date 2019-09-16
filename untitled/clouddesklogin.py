from selenium import webdriver
import os
import time

# chromdriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# os.environ['webdriver.chrome.dirver'] = chromdriver
# browser = webdriver.Chrome(chromdriver)
# browser = webdriver.Chrome()
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.PhantomJS()
browser.get('http://128.160.214.12/Citrix/XDWeb/auth/login.aspx')
time.sleep(5)
try:
    browser.find_element_by_id('skipWizardLink').click()
except NoSuchElementException:
    print(browser.page_source)
browser.find_element_by_xpath("//td/input[@id='user']").send_keys('dengyaowen.zh')
browser.find_element_by_xpath("//td/input[@id='password']").send_keys('abcd1234')
browser.find_element_by_xpath("//td/div/a[@id='btnLogin']").click()
browser.find_element_by_xpath("//*[@id='desktopSpinner_idCitrix.MPS.Desktop.XenDesktop._0024S10-10']").click()
print(browser.page_source)

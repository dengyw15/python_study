from selenium import webdriver
import os

# chromdriver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver_x64.exe'
# os.environ['webdriver.chrome.dirver'] = chromdriver
# browser = webdriver.Chrome(chromdriver)
browser = webdriver.Ie()
browser.get('http://itsm3.management.ccb/CAisd/pdmweb.exe')
print(browser.current_url)
browser.find_element_by_xpath("//*[@id='j_username']").send_keys('dengyaowen.zh')
browser.find_element_by_xpath("//*[@id='j_userpwd']").send_keys('abcd1234')
browser.find_element_by_xpath("/html/body/table/tbody/tr/td/div[2]/div/form/p[3]/input").click()
print(browser.page_source)

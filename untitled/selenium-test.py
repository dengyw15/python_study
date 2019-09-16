from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.get('C:/Users/dengyw/Desktop/PycharmProjects/js/s_0808_history.html')

browser.find_element_by_xpath("//input[@id='tid1']").send_keys(Keys.CONTROL, 'a')
browser.find_element_by_xpath("//input[@id='tid1']").send_keys(Keys.CONTROL, 'c')
browser.find_element_by_xpath("//input[@id='tid']").send_keys(Keys.CONTROL, 'v')
sleep(3)
browser.find_element_by_xpath("//input[@id='tid']").send_keys(Keys.CONTROL, 'a')
sleep(3)
browser.find_element_by_xpath("//input[@id='tid']").send_keys(Keys.BACKSPACE)

browser.find_element_by_xpath("//input[@id='tid']").send_keys('我是中国人')
browser.find_element_by_tag_name('button').click()
browser.back()
print(browser.page_source)

from selenium import webdriver
import datetime
import time


def getdate(days=0):
    return (datetime.date.today() + datetime.timedelta(days)).strftime('%Y%m%d')


def execute_sql():
    browser = webdriver.Chrome()
    url = 'http://icsp.jh:1340/ICSPWeb/jsp/fundProd/manualSql.jsp'
    browser.get(url)
    sqlinput = browser.find_element_by_id('sqlStr')
    today = getdate(-2)
    insertday = getdate(-1)
    sec_cod = ['01']
    for cod in sec_cod:
        sqlinput.clear()
        sql = "insert into dual values ('" + time.strftime('%H%M%S', time.localtime()) + "')"
        print(sql)
        sqlinput.send_keys(sql)
        select_button = browser.find_element_by_name('sou')
        select_button.click()
        time.sleep(2)

        print(browser.page_source)
    browser.close()


# print(getdate(-1))
execute_sql()

# print(time.strftime('%H%M%S', time.localtime()))
from selenium import webdriver
import datetime
import time


def getdate(days=0):
    return (datetime.date.today() + datetime.timedelta(days)).strftime('%Y%m%d')


def execute_sql():
    # browser = webdriver.Chrome()
    url = 'http://icsp.jh:1340/ICSPWeb/jsp/fundProd/manualSql.jsp'
    # browser.get(url)
    # sqlinput = browser.find_element_by_id('sqlStr')
    datatoday = getdate(-2)
    insertday = getdate(-1)
    sec_cod = ['01', '02', '15', '16', '17', '18', '19', '20', '21', '22']
    for cod in sec_cod:
        # sqlinput.clear()
        sql = "insert into icsp_mktgold_fenshi(sec_mkt_cod, sec_cod, curr_cod, buy_pri, sel_pri, price_date, price_time, mid_pri)" \
              + " select sec_mkt_cod, sec_cod, curr_cod, buy_pri, sel_pri, " + insertday + ", price_time, mid_pri from icsp_mktgold_fenshi where price_date='" \
              + datatoday + "' and sec_cod='" + cod + "' and price_time=(select max(price_time) from icsp_mktgold_fenshi where price_date='" \
              + datatoday + "' and sec_cod='" + cod + "')"
        print(sql)
        # sqlinput.send_keys(sql)
        # select_button = browser.find_element_by_name('sou')
        # select_button.click()
        # time.sleep(2)

        # print(browser.page_source)
    # browser.close()

# print(getdate(-1))
execute_sql()

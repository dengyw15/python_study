import requests
from bs4 import BeautifulSoup
import re

def connHtml(url,data={}):
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate, sdch",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Cache-Control": "max-age=0",
               "Connection": "keep-alive",
               "Cookie": "JSESSIONID=-_krO5QkmnjRfPscqJPxcyrzreK1OzfyaXACTcwmTor1yN7d2KlI!798887286",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36"
               }
    # data = {'fid':'5','page': i};
    # data = {'form1:loginName':'dengyaowen.zh', 'form1:password':'kevin200711','form1_SUBMIT':'1'}
    res = requests.get(url, params=data, headers=headers);
    print(res.url, '\n{}\n'.format("*"*49))
    # print(res.status_code)
    # # print(res.headers)
    res.encoding = "UTF-8"
    cnt = res.text;
    soup = BeautifulSoup(cnt, "lxml")
    soup.prettify()
    return soup;

def findAllThemeUrl():
    soup = connHtml("http://11.135.148.193/apu/");
    listUrl = [];
    for tr in soup.find_all("tr", id = re.compile('^fid')):
        url = 'http://11.135.148.193/apu/' + tr.h2.a['href']
        blockname = tr.h2.get_text();
        listUrl.append(url);
        listUrl.append(blockname)
    return listUrl;

def findAllIssues():
    listUrl = findAllThemeUrl();
    for j in range(0, len(listUrl), 2):
        url = listUrl[j];
        blockname = listUrl[j+1]
        print(url,blockname)
        for i in range(1, 11):
            data = {'page': i};
            soup = connHtml(url, data);
            for tr in soup.find_all("tr", class_="tr3"):
                # tr = soup.find("tr", class_="tr3");
                typetag = tr.find("td", class_="icon tar");
                if typetag.a.has_attr('title'):
                    type = typetag.a['title']
                else:
                    type = typetag.a.img['title']
                issuetag = tr.find("td", class_="subject").a;
                issuename = issuetag.get_text();
                issuesite = 'http://11.135.148.193/apu/' + issuetag['href']
                authortag = tr.find_all("td", attrs={'class': 'author'});
                publishauthortag = authortag[0];
                replyauthortag = authortag[1];
                print(blockname, type, (issuename+'('+issuesite+')'),publishauthortag.a.get_text(), publishauthortag.p.get_text(), replyauthortag.a.get_text(),
                      replyauthortag.p.get_text())

        print('{}'.format('*'*10),blockname + "  overhah",'{}\n'.format('*'*10));

# findIssues();
findAllIssues()
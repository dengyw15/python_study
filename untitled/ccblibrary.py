import requests
from bs4 import BeautifulSoup
import os

class bookSpy:

    def __init__(self, keyword):
        self.keyword = keyword
        self.data = {'flag':'2',
                'opacFacet':'callNumber',
                'opacFacet':'dateField',
                'opacFacet':'genre',
                'opacFacet':'opacPic',
                'opacFacet':'ziyuanType',
                'opacFacet':'authorSort',
                'opacFacet':'bookName',
                'opacFacet':'author',
                'opacFacet':'title',
                'opacFacet':'language',
                'opacFacet':'era',
                'opacFacet':'area',
                'opacFacet':'relationTopic',
                'opacFacet':'opacTag',
                'opacFacet':'shangjiaTime',
                'opacFacet':'shangjiaTime',
                'baseQueryValue': keyword,
                'baseQueryPoint':'all'
        }
        self.headers = {'Host': 'lms.jh:8080',
                    'Connection': 'keep-alive',
                    'Content-Length': '364',
                    'Cache-Control': 'max-age=0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Origin': 'http://lms.jh:8080',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Referer': 'http://lms.jh:8080/libraryservice/moreConditionSearching/goToSearchPage.action?flag=2',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.8'
        }

    def getHtml(self,page = None):
        if page == None or page == 1:
            url = "http://lms.jh:8080/libraryservice/moreConditionSearching/moreConditionSearch.action";
        else:
            url = "http://lms.jh:8080/libraryservice/moreConditionSearching/moreConditionSearch.action?pageCount=" + str(page)
        res = requests.post(url,data=self.data, headers=self.headers);
        soup = BeautifulSoup(res.text, "lxml");
        return soup;


    def findMaxPage(self):
        soup = self.getHtml();
        pages = soup.find("select",id = 'selectPageID').find_all('option');
        maxpage = pages[len(pages)-1].get_text();
        return maxpage;

    # def writefile(self, content):
    #     if os.path.exists("H:/2学习资料/python 爬虫学习/test/bookDetail.txt") == False:
    #         open("H:/2学习资料/python 爬虫学习/test/bookDetail.txt", "w");
    #     with open("H:/2学习资料/python 爬虫学习/test/bookDetail.txt", "r+", encoding="GBK") as fo:
    #         fo.seek(0, 2);
    #         fo.write(content);

    def findBookDetal(self):
        maxpage = self.findMaxPage();
        # with open("H:/test.txt", "r", encoding="UTF-8") as f:
        #     soup = BeautifulSoup(f.read(),"lxml");
        print("查询关键词为：{0}，总共有{1}页数据".format(self.keyword, maxpage))
        # self.writefile("查询关键词为：{0}，总共有{1}页数据".format(self.keyword, maxpage) + '\n')

        for i in range(1, int(maxpage)+1):
            soup = self.getHtml(i);
            for tb in soup.find_all("td", attrs={'width':'60%'}):
                details = tb.table.find_all('tr');
                print('{0}'.format("*"*49))
                # self.writefile('{0}'.format("*"*49) + '\n')
                for d in details:
                    if (d.th is not None):
                        print(d.th.next_element.strip(),d.th.a.next_element.strip());
                        # self.writefile(d.th.next_element.strip() + d.th.a.next_element.strip() + '\n')
                    if (d.td is not None):
                        print(d.td.get_text().strip());
                        # self.writefile(d.td.get_text().strip() + '\n')
                print('{0}'.format("*" * 49))
                # self.writefile('{0}'.format("*" * 49))
            print('{0}第{1}页数据获取完毕{2}'.format("*" * 20, i, "*" * 20));
            # self.writefile('{0}第{1}页数据获取完毕{2}'.format("*" * 20, i, "*" * 20) + '\n')

spy = bookSpy('心理')
spy.findBookDetal();
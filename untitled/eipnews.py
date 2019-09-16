import requests
from lxml import etree
from bs4 import BeautifulSoup
import re

# resp = requests.get('http://wcm.ccb.com/wcmau/ccbcache/zh/ns:LHQ6NixmOjE2ODEsYzoscDosYTosbTo=/channel.vsml');
# with open('H:/tmp/news.html', 'r+', encoding='utf-8') as f:
#     tree = etree.HTML(f.read())
# for pub in tree.xpath("//td[@class='pub_list']"):
#     atag = pub.xpath("a")[0]
#     href = "http://wcm.ccb.com/" + atag.get('href')
#     title = atag.get('title')
#     datetag = pub.xpath("../td[@class='list_date_time']")[0]
#     print(datetag.text)
#     print(href, title)


def getnextpage(currenpageurl):
    resp = requests.get(currenpageurl)
    tree = etree.HTML(resp.text)
    nextpage = tree.xpath("//td[@valign='bottom']/a")[0]
    nextpageurl = 'http://wcm.ccb.com' + nextpage.get('href')
    return nextpageurl


def getnewscontent(url):
    resp = requests.get(url)
    bs = BeautifulSoup(resp.text, 'lxml')
    return bs.find('div', id='ccb_content').get_text(), bs.find('td', width='56%').get_text()


def gennewscontent(datas):
    content = ''
    for d in datas:
        content += "<tr>\n"
        titleline = "<td>" + d['title'] + "</td>\n"
        pubdateline = "<td>" + d['pubdate'] + "</td>\n"
        recommdline = "<td>" + d['recommd'] + "</td>\n"
        detailline = "<td>" + d['content'] + "</td>\n"
        content = content + titleline + pubdateline + recommdline + detailline + "</tr>\n"
    return content


def writefile(content):
    with open("H:/tmp/result.html", "r+", encoding='utf-8') as of:
        of.seek(0, 2)
        of.write(content)


def genResult(datas, currsize, totalsize):
    htmlcontent = ''
    if currsize == 1:
        htmlhead = '''
        <html>
            <head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head>
            <body>
                <table>
                    <th>标题</th>
                    <th>发布时间</th>
                    <th>推荐人</th>
                    <th>详情</th>
        '''
        writefile(htmlhead + gennewscontent(datas))
    else:
        writefile(gennewscontent(datas))

    if currsize == totalsize:
        htmltail = '''
            </table>
            </body>
            </html>
        '''
        writefile(htmltail)


def parseOneHTML(tree, currsize, totalsize, keyword=''):
    datas = []
    for pub in tree.xpath("//td[@class='pub_list']"):
        onenews = {}
        atag = pub.xpath("a")[0]
        contenthref = "http://wcm.ccb.com/" + atag.get('href')
        title = atag.get('title')
        pubdate = pub.xpath("../td[@class='list_date_time']")[0].text

        content, recommd = getnewscontent(contenthref);
        if keyword != '': #不包含关键字则不爬取
            if keyword not in content:
                continue
        print(contenthref, title, pubdate)
        recommd = re.search(r':(.*\))', recommd).group()[1:]
        onenews.__setitem__('title', title)
        onenews.__setitem__('pubdate', pubdate)
        onenews.__setitem__('content', contenthref + '\n' + content)
        onenews.__setitem__('recommd', recommd)
        datas.append(onenews)
        # break
    genResult(datas, currsize, totalsize)


def getAllNews(totalsize, pageurl, keyword):
    tree = etree.HTML(requests.get(pageurl).text)
    parseOneHTML(tree, 1, totalsize, keyword)
    print("第{0}页爬取完毕".format('1'))
    for i in range(1, totalsize):
        nextpageurl = getnextpage(pageurl)
        tree = etree.HTML(requests.get(nextpageurl).text)
        parseOneHTML(tree, i+1, totalsize, keyword)
        pageurl = nextpageurl
        print("第{0}页爬取完毕".format(i+1))


firsturl = 'http://wcm.ccb.com/wcmau/ccbcache/zh/ns:LHQ6NixmOjE2ODEsYzoscDosYTosbTo=/channel.vsml'
keyword = '成都'
getAllNews(2, firsturl, keyword)

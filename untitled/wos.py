import requests
from lxml.html import etree
from bs4 import BeautifulSoup
import codecs
import re
import time
import random


def get_useragent():
    user_agents = ['Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
                   , 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
                   , 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)'
                   , 'Opera/9.27 (Windows NT 5.2; U; zh-cn)'
                   , 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'
                   ]
    return user_agents[random.randint(0, len(user_agents) - 1)]


def get_papaer_detail(url, count):

    resp = ss.get(url)
    html = etree.HTML(resp.text)
    print(url + str(resp.status_code))

    if resp.status_code is not 200:
        print(url + '响应失败，继续爬取下一页')
        return
    # with codecs.open('H:/tmp/python/paper_detail.html', 'r+', encoding='utf-8') as f:
    #     html = etree.HTML(f.read())
    try:
        title = html.xpath("//div[@class='title']")[0].xpath('string(.)').strip()  # 论文题目

        author_add_map_list = []  # 用于存放作者 及其对应的地址
        for author_info in html.xpath("//a[@title='Find more records by this author']"):
            author_name = author_info.text + (author_info.tail if author_info.tail else '')
            author_add_text = ''.join(author_info.xpath("./following-sibling::sup[1]/b/a/@href"))
            author_add = ''
            if author_add_text is not None and author_add_text.strip() is not '':  # 判断是否存在作者对应的地址信息
                author_add = ''.join(html.xpath(
                    "//a[@id='" + author_add_text.split('#')[1] + "']/text()"))  # 不包含Organization-Enhanced Name
            author_add_map_list.append({'author_name': author_name, 'author_add': author_add})

        paper_info_map = {}  # 用于存放论文发表的 卷 期 页码
        for paper_info in html.xpath("//div[@class='block-record-info-source-values']/p"):
            # key = paper_info.xpath("./span")[0].text.split(":")[0]
            # value = paper_info.xpath("./value")[0].text
            key = paper_info.xpath("string(.)").strip().split(":")[0].strip()
            value = paper_info.xpath("string(.)").strip().split(":")[1].strip()
            paper_info_map.__setitem__(key, value)

        doi = ''.join(
            html.xpath("//span[@class='FR_label' and text()='DOI:']/following-sibling::value[1]/text()"))  # doi
        pubdate = ''.join(
            html.xpath("//span[@class='FR_label' and text()='Published:']/following-sibling::value[1]/text()"))  # 发表日期
        abstract = ''.join(html.xpath(
            "//div[@class='title3' and text()='Abstract']/following-sibling::p[@class='FR_field']/text()"))  # 英文摘要
        keywords = ';'.join(html.xpath(
            "//div[@class='title3' and text()='Keywords']/following-sibling::p[@class='FR_field']/a/text()"))  # 将list转换为str

        reference_times = html.xpath("//span[@class='TCcountFR']")[0].xpath("string(.)")
        # 作者信息
        reprint_authors = []  # 通讯作者
        for au in html.xpath("//div[@class='title3' and text()='Author Information']/following-sibling::p[1]/span"):
            reprint_authors.append(''.join(au.xpath("./following::text()[1]")))
        email = ';\n'.join(html.xpath("//span[@class='FR_label' and contains(text(), 'E-mail "
                                      "Addresses')]/following-sibling::a/text()"))  # 将list转换为str
        # detail_address = info_div[4].find_all('table', class_='FR_table_noborders')[1].text.strip()
        # 刊物信息
        publication_name = ''.join(
            html.xpath("//span[@class='sourceTitle_txt']/source_title_txt_label/value/text()"))  # 刊物名称
        publisher = ''.join(html.xpath("//div[@class='block-record-info']/div[@class='title3' and text("
                                       ")='Publisher']/following-sibling::p[@class='FR_field']/value/text()"))  # 出版商
        research_area = (''.join(html.xpath(
            "//span[@class='FR_label' and text()='Research Areas:']/parent::p[1]/text()"))).strip()  # 研究领域
        documentType = (''.join(html.xpath("//span[@class='FR_label' and text()='Document Type:']/parent::p["
                                           "1]/text()"))).strip()  # 文档类型
        issn = ''.join(
            html.xpath("//span[@class='FR_label' and text()='ISSN:']/following-sibling::value[1]/text()"))  # ISSN
        eissn = ''.join(html.xpath("//span[@class='FR_label' and text()='eISSN:']/following-sibling::value["
                                   "1]/text()"))  # eISSN
        # 期刊影响
        impact_node = html.xpath("//table[@class='Impact_Factor_table']")
        impact_string = ''
        if len(impact_node) > 0:
            impact_num = html.xpath("//table[@class='Impact_Factor_table']/tr/td/text()")
            impact_during = html.xpath("//table[@class='Impact_Factor_table']/tr/th/text()")
            if len(impact_num) == len(impact_during):
                for i in range(0, len(impact_num)):
                    if impact_string is not '':
                        impact_string += '/'
                    impact_string += impact_num[i].strip() + '(' + impact_during[i].strip() + ')'

        # 生成结果
        if count % 2 == 0:
            color = '#D9DFED'
        else:
            color = '#E6E6E6'
        result = '<tr bgcolor=\'' + color + '\'><td>' + str(
            count) + '</td><td>' + title + '</td><td>' + pubdate + '</td>'
        keywordshtml = '<td><details><summary>keywords</summary>' + keywords + '</details></td>'
        abstracthtml = '<td><details><summary>abstract</summary>' + abstract + '</details></td>'
        referencehtml = '<td>' + reference_times + '</td>'
        doihtml = '<td>' + doi + '</td>'
        authorhtml = '<td>'
        for au in author_add_map_list:
            authorhtml += '<details><summary>' + au['author_name'] + '</summary>' + au['author_add'] + '</details>'
        authorhtml += '</td>'

        reprint_authorshtml = '<td>'
        for au in reprint_authors:
            reprint_authorshtml += '<details><summary>' + au + '</summary></details>'
        reprint_authorshtml += '</td>'
        reprint_auth_contact = '<td>' + email + '</td>'
        publicationhtml = '<td>' + publication_name + '</td>'
        volumehtml = '<td>' + (paper_info_map.get('Volume') if paper_info_map.get('Volume') else '') + '</td>'  # 卷
        issuehtml = '<td>' + (paper_info_map.get('Issue') if paper_info_map.get('Issue') else '') + '</td>'  # 期
        pageshtml = '<td>' + (paper_info_map.get('Pages') if paper_info_map.get('Pages') else '') + '</td>'  # 页码

        publisherhtml = '<td>' + publisher + '</td>'
        issnhtml = '<td>' + issn + '</td>'
        research_domainhtml = '<td>' + research_area + '</td>'
        impact_html = '<td>' + impact_string + '</td>'
        result = '{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}{15}</tr>'.format(result, keywordshtml,
                                                                                      abstracthtml, referencehtml,
                                                                                      doihtml, authorhtml,
                                                                                      reprint_authorshtml,
                                                                                      reprint_auth_contact,
                                                                                      publicationhtml, volumehtml,
                                                                                      issuehtml, pageshtml,
                                                                                      publisherhtml, issnhtml,
                                                                                      research_domainhtml,
                                                                                      impact_html)
        return result

    except IndexError as ie:
        print(ie.args)
    finally:
        pass


def begin_search(keywords):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '1367',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie':'SID="3Av24V8A4FdijR794bB"; CUSTOMER="UNIV OF ELECTRONIC SCIENCES AND TECH OF CHINA - UESTC"; E_GROUP_NAME="University of Electronic Science and Technology of China"; JSESSIONID=46DFC9B03DC36A199DC45B91CC08B4CE',
        'Host': 'apps.webofknowledge.com',
        'Origin': 'http://apps.webofknowledge.com',
        # 'Referer':'http://apps.webofknowledge.com/UA_GeneralSearch_input.do?product=UA&search_mode=GeneralSearch&SID=3Av24V8A4FdijR794bB&preferencesSaved=',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }

    datas = {
        'fieldCount': '1',
        'action': 'search',
        'product': 'UA',
        'search_mode': 'GeneralSearch',
        # 'SID': '3Av24V8A4FdijR794bB',
        'max_field_count': '25',
        # 'max_field_notice':'注意: 无法添加另一字段。',
        # 'input_invalid_notice':'检索错误: 请输入检索词。',
        # 'exp_notice':'检索错误: 专利检索词可在多个家族中找到 (',
        # 'input_invalid_notice_limits':' <br/>注: 滚动框中显示的字段必须至少与一个其他检索字段相组配。',
        # 'sa_params':'UA||3Av24V8A4FdijR794bB|http://apps.webofknowledge.com|',
        'formUpdated': 'true',
        'value(input1)': searchkeywords,
        'value(select1)': 'TS',
        'x': '868',
        'y': '330',
        'value(hidInput1)': '',
        'limitStatus': 'expanded',
        'ss_lemmatization': 'On',
        'ss_spellchecking': 'Suggest',
        'SinceLastVisit_UTC': '',
        'SinceLastVisit_DATE': '',
        'period': 'Range Selection',
        'range': 'Latest5Years',
        'startYear': '1950',
        'endYear': '2017',
        'update_back2search_link_param': 'yes',
        'ssStatus:display': 'none',
        'ss_showsuggestions': 'ON',
        'ss_query_language': 'auto',
        'ss_numDefaultGeneralSearchFields': '1',
        'rs_sort_by': 'PY.D;LD.D;SO.A;VL.D;PG.A;AU.A'
    }

    url = 'http://apps.webofknowledge.com/UA_GeneralSearch.do'
    tmp = ss.get(url)
    sid = ss.cookies.get('SID').split('\"')[1]
    headers.__setitem__('SID', sid)
    datas.__setitem__('SID', sid)
    ss.headers = headers
    tmp1 = ss.post(url, headers=headers, data=datas)  # 页面跳转
    return tmp1.url


def writeheadtohtml():
    head = '''<html>
<head> 
<meta charset="utf-8"> 
<title>web of science</title> 
</head>
<body>

<h4>主题:''' + searchkeywords + '''</h4>
<table  border='5%' width='100%' cellpadding='0' cellspacing='0'>
<tr bgcolor='#D9DFED'>
  <th rowspan="2">序号</th>
  <th colspan="6">论文信息</th>
  <th colspan="3">作者信息</th>
  <th colspan="8">发表刊物信息</th>
</tr>
<tr bgcolor='#D9DFED'>
  <th>题目</th>
  <th>发表日期</th>
  <th>关键词</th>
  <th>英文摘要</th>
  <th>被引用次数</th>
  <th>DOI</th>
  
  <th>作者名称及地址</th>
  <th>通讯作者</th>
  <th>通讯作者联系方式</th>
  
  <th>刊物名称</th>
  <th>卷</th>
  <th>期</th>
  <th>页码</th>  
  <th>出版商</th>
  <th>ISSN</th>
  <th>研究领域</th>
  <th>影响因子</th>
</tr>
    '''

    with codecs.open(outputfile, "r+", encoding='utf-8') as of:
        of.seek(0)
        of.write(head)


def writetailtohtml():
    tail = '''</table>
            </body>
            </html>
        '''
    with codecs.open(outputfile, "r+", encoding='utf-8') as of:
        of.seek(0, 2)
        of.write(tail)


def writebodytohtml(content):
    # if os.path.exists(outputfile) is False:
    #     os.chdir(os.path.split(outputfile)[0])
    #     open(os.path.split(outputfile)[1])

    with codecs.open(outputfile, "r+", encoding='utf-8') as of:
        of.seek(0, 2)
        of.write(content)


def scral_by_loop(start_url, querytotalpage):
    resp = ss.get(start_url)
    print(start_url + str(resp.status_code))
    html = etree.HTML(resp.text)
    # 直接构建论文详情页的url
    frt_url = 'http://apps.webofknowledge.com/' + html.xpath("//a[@class='smallV110']/@href")[0] + '&locale=en_US'
    totalpage = int(''.join(html.xpath("//span[@id='pageCount.bottom']/text()")[0].split(',')))
    # frt_url = '''http://apps.webofknowledge.com//full_record.do?product=UA&search_mode=GeneralSearch&qid=11&SID=3Av24V8A4FdijR794bB&page=1&doc=1&locale=en_US'''
    result = ''
    # 每页显示十篇论文，一共查询querytotalpage页
    for pages in range(1, int(querytotalpage) + 1):
        ss.headers.__setitem__('User-Agent', get_useragent())
        print(ss.headers.get('User-Agent'))
        if pages > totalpage:
            break
        for i in range(1, 11):
            doc_count = i + (pages - 1) * 10
            detail_url = frt_url.replace(re.compile(r'page=\d+').findall(frt_url)[0], 'page=' + str(pages)).replace(
                re.compile(r'doc=\d+').findall(frt_url)[0], 'doc=' + str(doc_count))  # 根据页码和论文数量构建url

            onepageresult = get_papaer_detail(detail_url, doc_count)
            if onepageresult is not None and onepageresult is not '':
                result += onepageresult

    writebodytohtml(result)


def scrawl(url, querytotalpage):
    if 'http://' not in url:
        return 'end'
    # resp = ss.get(url)
    with codecs.open('H:/tmp/python/science.html', 'r+', encoding='utf-8') as f:
        # bs = BeautifulSoup(f.read(), 'lxml')
        html = etree.HTML(f.read())
    # bs = BeautifulSoup(resp.text, 'lxml')
    onepageresult = ''
    countofeachpage = 10
    nextpageurl = html.xpath("//a[@class='paginationNext']")[0].get('href')
    nextpagecode = nextpageurl.split('page=')[1]

    for i, paper_detail_page in enumerate(html.xpath("//a[@class='smallV110']/@href")):
        detail_rul = 'http://apps.webofknowledge.com/' + paper_detail_page + '&locale=en_US'
        onepageresult += get_papaer_detail(detail_rul, i + 1 + (int(nextpagecode) - 2) * countofeachpage)

    writebodytohtml(onepageresult)
    if int(querytotalpage) < int(nextpagecode):
        return 'end'
    return scrawl(nextpageurl, querytotalpage)


if __name__ == '__main__':
    ss = requests.session()
    searchkeywords = 'combination material'
    outputfile = "H:/tmp/result.html"
    writeheadtohtml()
    scral_by_loop(begin_search(searchkeywords), 1)
    writetailtohtml()
    # url = 'http://apps.webofknowledge.com//full_record.do?product=UA&search_mode=GeneralSearch&qid=1&SID=4BTicmyl7hOlngatnr9&&page=1&doc=7&locale=en_US'
    # get_papaer_detail(url, 1)

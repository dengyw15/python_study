import requests
from lxml.html import etree
from bs4 import BeautifulSoup
import codecs
import re


def get_paper_detail():
    # resp = cookies.get(url)
    with codecs.open('H:/tmp/python/paper_detail.html', 'r+', encoding='utf-8') as f:
        bs = BeautifulSoup(f.read(), 'lxml')
        author_add_map_list = [] #用于存放作者 及其对应的地址
        # 论文信息
        title = bs.find('div', class_='title').text  #论文题目
        info_div = bs.find_all('div', class_='block-record-info')
        author_div = info_div[0]
        author_info = ' '.join(author_div.find('p', class_='FR_field').text.strip().split()) #作者xinxi
        for author_info in author_div.find_all('a', title='Find more records by this author'):
            author_name = author_info.text + author_info.next_sibling if author_info.next_sibling else ''
            author_add_text = author_info.find_next_sibling().find('a')['href'].split('#')[1]
            # author_add = info_div[4].find('a', attrs={'name': author_add_text}).parent.text #包含Organization-Enhanced Name
            author_add = info_div[4].find('a', attrs={'name': author_add_text}).text  #不包含Organization-Enhanced Name
            author_add_map_list.append({'author_name': author_name, 'author_add': author_add})
        # print(author_add_map_list)
        publication_div = info_div[1]
        paper_pub_info_div = publication_div.find_all('p', class_='FR_field')
        volumn = paper_pub_info_div[0].find('value').text  #卷
        issue = paper_pub_info_div[1].find('value').text #期
        pages = paper_pub_info_div[2].find('value').text #页
        doi = paper_pub_info_div[3].find('value').text #doi
        pubdate = paper_pub_info_div[4].find('value').text #发表日期
        abstract = info_div[2].find('p', class_='FR_field').text #英文摘要
        keywords_node = info_div[3].find_all('a', alt='Find more records by this author keywords')
        keywords = ''
        for i, node in enumerate(keywords_node):
            keywords = keywords + node.text
            if (i<len(keywords_node)-1):
                keywords = keywords + ';'
        # 作者信息
        author_info_node = info_div[4].find_all('p', class_='FR_field')
        t = type(author_info_node[0].extract())
        reprint_authors = [] #通讯作者
        for au in author_info_node[0].find_all('span', class_='FR_label'):
            reprint_authors.append(au.next_sibling)
        email = author_info_node[2].text.split(':')[1]
        school = info_div[4].find('td', class_='fr_address_row2').text.strip()
        reprint_address = info_div[4].find_all('table', class_='FR_table_noborders')[0].text.strip()
        # detail_address = info_div[4].find_all('table', class_='FR_table_noborders')[1].text.strip()
        #刊物信息
        publication_name = publication_div.find('p', class_='sourceTitle').get_text().strip() #刊物名称
        publisher = paper_pub_info_div[5].find('span', attrs={'class': False}).text.strip()  # 出版商
        issn = paper_pub_info_div[6].find_all('value')[0].text.strip() #ISSN
        eissn = paper_pub_info_div[6].find_all('value')[1].text.strip()  # eISSN
        research_domain = paper_pub_info_div[7].find('value').text.strip() #研究领域

        #生成结果
        result = '<tr><td>' + title + '</td><td>' + pubdate + '</td>'
        keywordshtml = '<td><details><summary>keywords</summary>' + keywords + '</details></td>'
        abstracthtml = '<td><details><summary>abstract</summary>' + abstract + '</details></td>'
        referencehtml = '<td>' + '0' + '</td>'
        doihtml = '<td>' + doi + '</td>'
        authorhtml = '<td>'
        for au in author_add_map_list:
            authorhtml += '<details><summary>' + au['author_name'] + '</summary>' + au['author_add'] + '</details>'
        authorhtml += '</td>'

        reprint_authorshtml = '<td>'
        for au in reprint_authors:
            reprint_authorshtml += '<details><summary>' + au + '</summary></details>'
        reprint_authorshtml += '</td>'
        publicationhtml = '<td>' + publication_name + '</td>'
        publisherhtml = '<td>' + publisher + '</td>'
        issnhtml = '<td>' + issn + '</td>'
        research_domainhtml = '<td>' + research_domain + '</td>'
        result = result + keywordshtml + abstracthtml + referencehtml + doihtml + authorhtml + reprint_authorshtml + publicationhtml + publisherhtml + issnhtml + research_domainhtml + '</tr>'
        return result


def search():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '1367',
        'Content-Type':  'application/x-www-form-urlencoded',
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
        'value(input1)': 'test',
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
    # ss = requests.session()
    # url = 'http://apps.webofknowledge.com/UA_GeneralSearch.do'
    # tmp = ss.get("http://apps.webofknowledge.com/UA_GeneralSearch.do")
    # sid = ss.cookies.get('SID').split('\"')[1]
    # print('###########ss.cookies###########')
    # print(ss.cookies)
    # print('###########tmp.cookies#########')
    # print(tmp.cookies)
    # print('###########ss.headers###########')
    # print(ss.headers)
    # print('###########tmp.url###########')
    # print(tmp.url)
    # headers.__setitem__('SID', sid)
    # datas.__setitem__('SID', sid)
    # tmp1 = ss.post(url, headers=headers, data=datas)
    # print('#########tmp1后：ss.cookies#############')
    # print(ss.cookies)
    # print('#########tmp1后：ss.headers#############')
    # print(ss.headers)
    # print('##########tmp1后：tmp1.url############')
    # print(tmp1.url)
    # print('##########tmp1后：tmp1.cookies############')
    # print(tmp1.cookies)
    # print(tmp1.status_code)
    # resp = ss.get(tmp1.url)
    # print(resp.text)
    # tree = etree.parse(resp.text)
    # print(tree.xpath("//a[@class='smallV110']"))
    # bs = BeautifulSoup(resp.text, 'lxml')
    # print(bs.find_all("a", class_="smallV110"))
    with codecs.open('H:/tmp/python/science.html', 'r+', encoding='utf-8') as f:
        bs = BeautifulSoup(f.read(), 'lxml')
        # bs = BeautifulSoup(resp.text, 'lxml')
        onepageresult = ''
        for paper in bs.find_all("div", attrs={"id": re.compile(r"RECORD_\d+")}):
            number = paper.find("div", class_='search-results-number-align').text.strip()
            detail_url = 'http://apps.webofknowledge.com/' + paper.find("a", class_='smallV110')['href']
            # print(detail_url)
            # paper_title = paper.find("a", class_='smallV110').find('value').text
            # author_node = paper.find("span", string=re.compile('By:')).find_parent("div")
            # author = author_node.text.split("By:")[1]
            # publisher_node = author_node.find_next_sibling("div")
            # publisher = publisher_node.find("value").text
            # pub_info_node = publisher_node.find_all("span", class_="data_bold")
            # volumn = pub_info_node[0].text.strip()
            # issue = pub_info_node[1].text.strip()
            # pages = pub_info_node[2].text.strip()
            # pubdate = pub_info_node[3].text.strip()
            # cited_times = paper.find("div", class_='search-results-data-cite').text
            # cited_times = re.search("\d+", cited_times).group()
            onepageresult += get_paper_detail()

        print(onepageresult)
search()
# get_paper_detail()

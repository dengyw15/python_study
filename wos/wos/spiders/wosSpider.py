# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor


class WosspiderSpider(CrawlSpider):
    name = 'wosSpider'
    allowed_domains = ['webofknowledge.com']
    # start_urls = ['http://apps.webofknowledge.com/UA_GeneralSearch.do']

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

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=False),
    )

    def start_requests(self):
        print('start_requests')
        # url = 'http://apps.webofknowledge.com/UA_GeneralSearch_input.do?product=UA&search_mode=GeneralSearch'
        url = 'http://eip.ccb.com/'
        return [Request(url,
                        meta={'cookiejar': 1}, callback=self.post_search)]

    def post_search(self, response):
        print('prepare search')
        datas = {
            'fieldCount': '1',
            'action': 'search',
            'product': 'UA',
            'search_mode': 'GeneralSearch',
            'max_field_count': '25',
            # 'max_fiel:'UA||3Av24V8A4FdijR794bB|http://apps.webofknowledge.com|',
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
        print("cookie is {0}".format(response))
        return [FormRequest.from_response(response,
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          headers=self.headers,
                                          formdata=datas,
                                          callback=self.after_search,
                                          dont_filter=False)]

    def after_search(self, response):
        print("url is {0}".format(response.url))
        # yield self.make_requests_from_url(response.url)

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

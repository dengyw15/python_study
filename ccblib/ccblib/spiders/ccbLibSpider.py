# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request, FormRequest


class CcblibspiderSpider(CrawlSpider):
    name = 'ccbLibSpider'
    # allowed_domains = ['lib.com']
    # start_urls = ['http://lib.com/']

    data = {'flag': '2',
            'opacFacet': 'callNumber',
            'opacFacet': 'dateField',
            'opacFacet': 'genre',
            'opacFacet': 'opacPic',
            'opacFacet': 'ziyuanType',
            'opacFacet': 'authorSort',
            'opacFacet': 'bookName',
            'opacFacet': 'author',
            'opacFacet': 'title',
            'opacFacet': 'language',
            'opacFacet': 'era',
            'opacFacet': 'area',
            'opacFacet': 'relationTopic',
            'opacFacet': 'opacTag',
            'opacFacet': 'shangjiaTime',
            'opacFacet': 'shangjiaTime',
            'baseQueryValue': '经济',
            'baseQueryPoint': 'all'
            }
    headers = {'Host': 'lms.jh:8080',
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

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        print('start_requests')
        url = 'http://lms.jh:8080/libraryservice/moreConditionSearching/goToSearchPage.action?flag=2'
        r = FormRequest(url,
                        headers=self.headers,
                        formdata=self.data,
                        callback=self.parse_detail)
        print('ttttttt{0}'.format(r.headers))
        print('ttttttt{0}'.format(r.url))
        print('ttttttt{0}'.format(r.cookies))
        return [r]

    def parse_detail(self, response):
        print('ttttttt{0}'.format(response.text))
        pass

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

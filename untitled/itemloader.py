from ccbnews.items import CcbnewsItem
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst
from scrapy.contrib.loader import ItemLoader
from scrapy import Item, Field
from w3lib.html import remove_tags


def filterdata(value):
    return value.split('发布时间:')[1]


class CcbnewsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    pubdate = Field()
    content = Field()
    author = Field()

    il = ItemLoader(Item=CcbnewsItem())
    il.add_value('title', ['testTitle'])
    il.add_value('author', 'fff 发布时间:2017-08-29')

    il.load_item()